# Polymorphic 
```c
#include "sl_bt_api.h"
#include "gatt_db.h"

// 假设在 GATT Configurator 中声明的能力 ID
// 这些 ID 通常在 gatt_db.h 中定义
#define CAPABILITY_PRODUCT_A   gattdb_cap_product_a
#define CAPABILITY_PRODUCT_B   gattdb_cap_product_b

// 假设读取 IO 引脚来确定产品型号
// 返回 true 表示是产品 A，false 表示是产品 B
bool is_product_a(void);

void app_init(void)
{
    // 确保没有连接时进行配置，这是官方推荐的最安全方式
    if (sl_bt_connection_get_active_count() == 0) {
        if (is_product_a()) {
            // 启用产品 A 所需的能力，禁用产品 B 的
            sl_bt_gatt_set_capability(CAPABILITY_PRODUCT_A, 1);
            sl_bt_gatt_set_capability(CAPABILITY_PRODUCT_B, 0);
        } else {
            sl_bt_gatt_set_capability(CAPABILITY_PRODUCT_A, 0);
            sl_bt_gatt_set_capability(CAPABILITY_PRODUCT_B, 1);
        }
    }
}
```
# dynamic

```c
/***************************************************************************
 * @file BLEChannelImpl.cpp
 * @brief Implementation of BLE channel operations for the Silicon Labs platform.
 *******************************************************************************
 * # License
 * <b>Copyright 2024 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * The licensor of this software is Silicon Laboratories Inc. Your use of this
 * software is governed by the terms of Silicon Labs Master Software License
 * Agreement (MSLA) available at
 * www.silabs.com/about-us/legal/master-software-license-agreement. This
 * software is distributed to you in Source Code format and is governed by the
 * sections of the MSLA applicable to Source Code.
 *
 ******************************************************************************/

#include "BLEChannelImpl.h"
#include <crypto/RandUtils.h>
#include <lib/support/logging/CHIPLogging.h>
#include <platform/CHIPDeviceLayer.h>
#include <platform/internal/CHIPDeviceLayerInternal.h>

#if defined(AOK02_MATTER_PROJECT)
/**
 * @brief The write_request event call from BLE stack
 *
 * @param evt
 */
extern void ble_manager_gatt_server_user_write_request_event_callback(volatile sl_bt_msg_t * evt);

/**
 * @brief The read_request event call from BLE stack
 *
 * @param evt
 */
extern void ble_manager_gatt_server_user_read_request_event_callback(volatile sl_bt_msg_t * evt);

/**
 * @brief Fill the BLE Scan response data
 *
 * @param responseData
 * @param max_data_len The max len responseData
 * @param index The offset of responseData
 * @return The Offset of responseData buffer
 */
extern uint32_t ble_manager_fill_scan_response_data(uint8_t *responseData, uint32_t max_data_len, uint32_t index);

/**
 * @brief Fill the BLE Advertising data
 *
 * @param advData
 * @param max_data_len The max len responseData
 * @param index The offset of responseData
 * @return The Offset of responseData buffer
 */
extern uint32_t ble_manager_fill_advertising_data(uint8_t *advData, uint32_t max_data_len, uint32_t index);

extern bool ble_manager_gatt_server_connection_opened(volatile sl_bt_msg_t * evt);
extern void ble_manager_gatt_server_connection_closed(volatile sl_bt_msg_t * evt);
extern void ble_manager_evt_system_boot(volatile sl_bt_msg_t * evt);
extern void ble_manager_evt_sm_confirm_bonding(volatile sl_bt_msg_t * evt);
extern void ble_manager_evt_sm_bonding_failed(volatile sl_bt_msg_t * evt);
extern void ble_manager_evt_sm_bonded(volatile sl_bt_msg_t * evt);
extern void ble_manager_evt_advertiser_scan_request(volatile sl_bt_msg_t * evt);
extern void ble_manager_gatt_server_characteristic_status_event_callback(volatile sl_bt_msg_t * evt);
extern uint8_t matter_adv_handle;
#endif

namespace chip {
namespace DeviceLayer {
namespace Internal {

namespace {
#if defined(AOK02_MATTER_PROJECT)
// Device Information Service (0x180A)
const uint8_t DeviceInformationUUID[2] = { 0x0A, 0x18 };

// Device Information Service Characteristics UUIDs (16-bit)
const sl_bt_uuid_16_t ManufacturerNameStringUUID     = { 0x29, 0x2A };
const sl_bt_uuid_16_t ModelNumberStringUUID          = { 0x24, 0x2A };
const sl_bt_uuid_16_t SystemIDUUID                   = { 0x23, 0x2A };
const sl_bt_uuid_16_t SerialNumberStringUUID         = { 0x25, 0x2A };
const sl_bt_uuid_16_t HardwareRevisionStringUUID     = { 0x27, 0x2A };
const sl_bt_uuid_16_t FirmwareRevisionStringUUID     = { 0x26, 0x2A };
const sl_bt_uuid_16_t RegulatoryCertDataListUUID     = { 0x2A, 0x2A };
const sl_bt_uuid_16_t PnPIDUUID                      = { 0x50, 0x2A };

// SMP Service (128-bit UUID: da2edc1d-1db7-4cd3-868b-8a527460aa84)
// Little-endian byte order
const uint8_t kSmpServiceUUID[16] = {
    0x1d, 0xdc, 0x2e, 0xda, 0xb7, 0x1d, 0xd3, 0x4c,
    0x8b, 0x86, 0x84, 0xaa, 0x60, 0x74, 0x52, 0x8a
};

#else
// Side Channel UUIDS
const uint8_t kSideServiceUUID[16] = { 0x01, 0x00, 0x00, 0xEE, 0xFF, 0xC0, 0x00, 0x80,
                                       0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
const uuid_128 kRxUUID = { .data = { 0x01, 0x00, 0x00, 0xEE, 0xFF, 0xC0, 0xAD, 0xDE, 0xEF, 0xBE, 0xAD, 0xDE, 0x00, 0xEE, 0xFF,
                                     0xC0 } };
const uuid_128 kTxUUID = { .data = { 0x02, 0x00, 0x00, 0xEE, 0xFF, 0xC0, 0xAD, 0xDE, 0xEF, 0xBE, 0xAD, 0xDE, 0x00, 0xEE, 0xFF,
                                     0xC0 } };

uint8_t InitialValueRX[16] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
uint8_t InitialValueTX[16] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF };
#endif

CHIP_ERROR MapBLEError(int bleErr)
{
    switch (bleErr)
    {
    case SL_STATUS_OK:
        return CHIP_NO_ERROR;
    case SL_STATUS_BT_ATT_INVALID_ATT_LENGTH:
        return CHIP_ERROR_INVALID_STRING_LENGTH;
    case SL_STATUS_INVALID_PARAMETER:
        return CHIP_ERROR_INVALID_ARGUMENT;
    case SL_STATUS_INVALID_STATE:
        return CHIP_ERROR_INCORRECT_STATE;
    case SL_STATUS_NOT_SUPPORTED:
        return CHIP_ERROR_UNSUPPORTED_CHIP_FEATURE;
    default:
        return CHIP_ERROR(ChipError::Range::kPlatform, bleErr + CHIP_DEVICE_CONFIG_SILABS_BLE_ERROR_MIN);
    }
}

} // namespace

CHIP_ERROR BLEChannelImpl::Init()
{
    uint16_t session;
    #if 0//defined(AOK02_MATTER_PROJECT)
    uint16_t service;
    uint16_t characteristic;
    uint16_t cccd;  // For Client Characteristic Configuration Descriptor
    uint16_t smpService;
	
    sl_status_t ret = sl_bt_gattdb_new_session(&session);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // ========== 1. Device Information Service (UUID 0x180A) ==========
    ret = sl_bt_gattdb_add_service(session, sl_bt_gattdb_primary_service,
                                   0, // not advertised
                                   sizeof(DeviceInformationUUID), DeviceInformationUUID, &service);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Manufacturer Name String
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, // No security
                                                  0, // No flags
                                                  ManufacturerNameStringUUID, sl_bt_gattdb_variable_length_value,
                                                  255, // Max length
                                                  12, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Model Number String
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  ModelNumberStringUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // System ID (fixed length 8 bytes)
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  SystemIDUUID,
                                                  sl_bt_gattdb_fixed_length_value,
                                                  8, 
												  8, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Serial Number String
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  SerialNumberStringUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Hardware Revision String
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  HardwareRevisionStringUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Firmware Revision String
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  FirmwareRevisionStringUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Regulatory Certification Data List
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  RegulatoryCertDataListUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // PnP ID
    ret = sl_bt_gattdb_add_uuid16_characteristic(session, service,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ,
                                                  0, 
												  0,
                                                  PnPIDUUID,
                                                  sl_bt_gattdb_variable_length_value,
                                                  20, 
												  1, 0, &characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    ret = sl_bt_gattdb_start_characteristic(session, characteristic);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Start Device Information Service
    ret = sl_bt_gattdb_start_service(session, service);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    #if 0
    // ========== 2. SMP Service (128-bit UUID) ==========
    ret = sl_bt_gattdb_add_service(session, sl_bt_gattdb_primary_service,
                                           0, // not advertised
                                           sizeof(kSmpServiceUUID), kSmpServiceUUID, &smpService);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Start SMP Service (no characteristics added)
    ret = sl_bt_gattdb_start_service(session, smpService);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    #endif
    // Commit the entire database
    ret = sl_bt_gattdb_commit(session);
    return MapBLEError(ret);

#else   // !defined(AOK02_MATTER_PROJECT)
    sl_status_t ret = sl_bt_gattdb_new_session(&session);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));                               
    // Add service
    ret = sl_bt_gattdb_add_service(session, sl_bt_gattdb_primary_service,
                                   0, // not advertised
                                   sizeof(kSideServiceUUID), kSideServiceUUID, &mSideServiceHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Add RX characteristic
    ret = sl_bt_gattdb_add_uuid128_characteristic(session, mSideServiceHandle,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ | SL_BT_GATTDB_CHARACTERISTIC_WRITE,
                                                  0, // No security
                                                  0, // No flags
                                                  kRxUUID, sl_bt_gattdb_variable_length_value,
                                                  255, // Max length
                                                  sizeof(InitialValueRX), InitialValueRX, &mSideRxCharHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_add_uuid128_characteristic(session, mSideServiceHandle,
                                                  SL_BT_GATTDB_CHARACTERISTIC_READ | SL_BT_GATTDB_CHARACTERISTIC_WRITE |
                                                      SL_BT_GATTDB_CHARACTERISTIC_WRITE_NO_RESPONSE |
                                                      SL_BT_GATTDB_CHARACTERISTIC_INDICATE,
                                                  0, // No security
                                                  0, // No flags
                                                  kTxUUID, sl_bt_gattdb_variable_length_value,
                                                  255, // Max length
                                                  sizeof(InitialValueTX), InitialValueTX, &mSideTxCharHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_service(session, mSideServiceHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_characteristic(session, mSideRxCharHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_characteristic(session, mSideTxCharHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    #endif
    ret = sl_bt_gattdb_commit(session);
    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::ConfigureAdvertising(const AdvConfigStruct & config)
{
    ChipLogProgress(DeviceLayer, "Configuring BLE Channel");

    sl_status_t ret;

    if (mAdvHandle == kInvalidAdvertisingHandle)
    {
        ret = sl_bt_advertiser_create_set(&mAdvHandle);
        VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

        // TODO: Check if we need to randomize the address
        uint64_t random = Crypto::GetRandU64();
        memcpy(&mConnectionState.address, &random, sizeof(mConnectionState.address));

        // Set two MSBs to 11 to properly the address - BLE Static Device Address requirement
        mConnectionState.address.addr[5] |= 0xC0;
        #if defined(AOK02_MATTER_PROJECT)
        #else
        ret = sl_bt_advertiser_set_random_address(mAdvHandle, sl_bt_gap_static_address, mConnectionState.address,
                                                  &mConnectionState.address);
        VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));
        #endif
        ChipLogDetail(DeviceLayer, "BLE Static Device Address %02X:%02X:%02X:%02X:%02X:%02X", mConnectionState.address.addr[5],
                      mConnectionState.address.addr[4], mConnectionState.address.addr[3], mConnectionState.address.addr[2],
                      mConnectionState.address.addr[1], mConnectionState.address.addr[0]);
    }

    ret = sl_bt_legacy_advertiser_set_data(mAdvHandle, sl_bt_advertiser_advertising_data_packet, config.advData.size(),
                                           config.advData.data());
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_legacy_advertiser_set_data(mAdvHandle, sl_bt_advertiser_scan_response_packet, config.responseData.size(),
                                           config.responseData.data());
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    mAdvIntervalMin     = config.intervalMin;
    mAdvIntervalMax     = config.intervalMax;
    mAdvDuration        = config.duration;
    mAdvMaxEvents       = config.maxEvents;
    mAdvConnectableMode = config.advConnectableMode;

    mFlags.Set(Flags::kConfigured);
    return CHIP_NO_ERROR;
}

CHIP_ERROR BLEChannelImpl::PrintAdvertisingInfo()
{
    ChipLogProgress(DeviceLayer, "Advertising Info:");
    ChipLogProgress(DeviceLayer, "  Interval Min: %ld", mAdvIntervalMin);
    ChipLogProgress(DeviceLayer, "  Interval Max: %ld", mAdvIntervalMax);
    ChipLogProgress(DeviceLayer, "  Duration: %d", mAdvDuration);
    ChipLogProgress(DeviceLayer, "  Max Events: %d", mAdvMaxEvents);
    ChipLogProgress(DeviceLayer, "  Connectable Mode: %d", mAdvConnectableMode);
    ChipLogProgress(DeviceLayer, "  Advertising Handle: %d", mAdvHandle);
    ChipLogProgress(DeviceLayer, "  Random Static Address: %02X:%02X:%02X:%02X:%02X:%02X", mConnectionState.address.addr[5],
                    mConnectionState.address.addr[4], mConnectionState.address.addr[3], mConnectionState.address.addr[2],
                    mConnectionState.address.addr[1], mConnectionState.address.addr[0]);
    return CHIP_NO_ERROR;
}

CHIP_ERROR BLEChannelImpl::StartAdvertising(void)
{
    // TODO: Check for handling max connection per handle vs globally

    // If already advertising, stop it, before changing values
    if (mFlags.Has(Flags::kAdvertising))
    {
        sl_bt_advertiser_stop(mAdvHandle);
    }

    sl_status_t ret;

    ret = sl_bt_advertiser_set_timing(mAdvHandle, mAdvIntervalMin, mAdvIntervalMax, mAdvDuration, mAdvMaxEvents);
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_advertiser_configure(mAdvHandle, 1); // TODO : Figure out this magic 1 in the sl_bt_advertiser_flags
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Start advertising
    ret = sl_bt_legacy_advertiser_start(mAdvHandle, mAdvConnectableMode);
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    mFlags.Set(Flags::kAdvertising);
    ChipLogProgress(DeviceLayer, "BLE Advertising started successfully");

    return CHIP_NO_ERROR;
}

CHIP_ERROR BLEChannelImpl::StopAdvertising(void)
{
    if (mFlags.Has(Flags::kAdvertising))
    {
        sl_status_t ret = SL_STATUS_OK;

        mFlags.Clear(Flags::kAdvertising);
        // TODO: Confirm the fast vs slow advertising concept from a channel perspective vs from CHIPoBLE perspective
        // mFlags.Set(Flags::kFastAdvertisingEnabled, true);

        ret = sl_bt_advertiser_stop(mAdvHandle);
        sl_bt_advertiser_clear_random_address(mAdvHandle);
        sl_bt_advertiser_delete_set(mAdvHandle);
        mAdvHandle = kInvalidAdvertisingHandle;
        VerifyOrReturnLogError(CHIP_NO_ERROR == MapBLEError(ret), MapBLEError(ret));
    }

    return CHIP_NO_ERROR;
}

bool BLEChannelImpl::CanHandleEvent(uint32_t event)
{
    #if defined(AOK02_MATTER_PROJECT)
    return (event == sl_bt_evt_system_boot_id || event == sl_bt_evt_connection_opened_id ||
            event == sl_bt_evt_connection_closed_id || event == sl_bt_evt_gatt_mtu_exchanged_id ||
            event == sl_bt_evt_gatt_server_attribute_value_id || event == sl_bt_evt_gatt_server_user_read_request_id ||
            event == sl_bt_evt_gatt_server_characteristic_status_id || event == sl_bt_evt_gatt_server_user_write_request_id ||
            event == sl_bt_evt_sm_confirm_bonding_id || event == sl_bt_evt_sm_bonding_failed_id ||
            event == sl_bt_evt_sm_bonded_id || event == sl_bt_evt_advertiser_scan_request_id);
    #else
    return (event == sl_bt_evt_system_boot_id || event == sl_bt_evt_connection_opened_id ||
            event == sl_bt_evt_connection_closed_id || event == sl_bt_evt_gatt_mtu_exchanged_id ||
            event == sl_bt_evt_gatt_server_attribute_value_id || event == sl_bt_evt_gatt_server_user_read_request_id ||
            event == sl_bt_evt_gatt_server_characteristic_status_id);
    #endif        
}

void BLEChannelImpl::ParseEvent(volatile sl_bt_msg_t * evt)
{
    VerifyOrReturn(CanHandleEvent(SL_BT_MSG_ID(evt->header)));
    switch (SL_BT_MSG_ID(evt->header))
    {
    case sl_bt_evt_system_boot_id: {
        ChipLogProgress(DeviceLayer, "BLE boot event received by SideChannel");
    }
    break;
    case sl_bt_evt_connection_opened_id: {
        sl_bt_evt_connection_opened_t * conn_evt = (sl_bt_evt_connection_opened_t *) &(evt->data);
        ChipLogProgress(DeviceLayer, "Connect Event for SideChannel on handle : %d", conn_evt->connection);
        AddConnection(conn_evt->connection, conn_evt->bonding);
        #if defined(AOK02_MATTER_PROJECT)
        ble_manager_gatt_server_connection_opened(evt);
        #endif
    }
    break;
    case sl_bt_evt_connection_closed_id: {
        sl_bt_evt_connection_closed_t * conn_evt = (sl_bt_evt_connection_closed_t *) &(evt->data);
        ChipLogProgress(DeviceLayer, "Disconnect Event for the Side Channel on handle : %d", conn_evt->connection);
        RemoveConnection(conn_evt->connection);
        #if defined(AOK02_MATTER_PROJECT)
        ble_manager_gatt_server_connection_closed(evt);
        StartAdvertising();
        #endif
    }
    break;
    case sl_bt_evt_gatt_mtu_exchanged_id: {
        UpdateMtu(evt);
    }
    break;
    case sl_bt_evt_gatt_server_attribute_value_id: {
        uint8_t dataBuff[255] = { 0 };
        MutableByteSpan dataSpan(dataBuff);
        HandleWriteRequest(evt, dataSpan);

        // Buffered (&Deleted) the following data:
        ChipLogProgress(DeviceLayer, "Buffered (&Deleted) the following data:");
        ChipLogByteSpan(DeviceLayer, dataSpan);
    }
    break;
    case sl_bt_evt_gatt_server_characteristic_status_id: {
        sl_bt_gatt_server_characteristic_status_flag_t StatusFlags;

        StatusFlags = (sl_bt_gatt_server_characteristic_status_flag_t) evt->data.evt_gatt_server_characteristic_status.status_flags;
        if (StatusFlags != sl_bt_gatt_server_confirmation)
        {
            bool isNewSubscription = false;
            LogErrorOnFailure(HandleCCCDWriteRequest(evt, isNewSubscription));
        }
        #if defined(AOK02_MATTER_PROJECT)
        ble_manager_gatt_server_characteristic_status_event_callback(evt);
        #endif
    }
    break;
    case sl_bt_evt_gatt_server_user_read_request_id: {

        ChipLogProgress(DeviceLayer, "Char Read Req, char : %d", evt->data.evt_gatt_server_user_read_request.characteristic);

        char dataBuff[] = "You are reading the Si-Channel TX characteristic";
        ByteSpan dataSpan((const uint8_t *) dataBuff, sizeof(dataBuff));
        HandleReadRequest(evt, dataSpan);
        #if defined(AOK02_MATTER_PROJECT)
        ble_manager_gatt_server_user_read_request_event_callback(evt);
        #endif
    }
    break;
	#if defined(AOK02_MATTER_PROJECT)
    case sl_bt_evt_gatt_server_user_write_request_id: {
        ble_manager_gatt_server_user_write_request_event_callback(evt);
    }
    break;


    case sl_bt_evt_sm_confirm_bonding_id: {
        ble_manager_evt_sm_confirm_bonding(evt);
    }
    break;
    
    case sl_bt_evt_sm_bonding_failed_id: {
        ble_manager_evt_sm_bonding_failed(evt);
    }
    break;

    case sl_bt_evt_sm_bonded_id: {
        ble_manager_evt_sm_bonded(evt);
    }
    break;

    case sl_bt_evt_advertiser_scan_request_id: {
        ble_manager_evt_advertiser_scan_request(evt);
    }
    break;
    #endif
    default: {
        ChipLogProgress(DeviceLayer, "BLESideChannel Unknown Event id = %08" PRIx32, SL_BT_MSG_ID(evt->header));
        break;
    }
    }
}

void BLEChannelImpl::AddConnection(uint8_t connectionHandle, uint8_t bondingHandle)
{
    // TODO: Verify if we want to allow multiple connections at once, this is tied to the Endpoint usage as well
    // We currently only support one connection at a time on our side channel
    VerifyOrReturn(!mConnectionState.allocated, ChipLogError(DeviceLayer, "Connection already exists"));

    mConnectionState.connectionHandle = connectionHandle;
    mConnectionState.bondingHandle    = bondingHandle;
    mConnectionState.allocated        = 1;
    mConnectionState.subscribed       = 0;
}

bool BLEChannelImpl::RemoveConnection(uint8_t connectionHandle)
{
    VerifyOrReturnValue(mConnectionState.allocated, false);
    VerifyOrReturnValue(mConnectionState.connectionHandle == connectionHandle, false);
    memset(&mConnectionState, 0, sizeof(mConnectionState));
    return true;
}

void BLEChannelImpl::HandleReadRequest(volatile sl_bt_msg_t * evt, ByteSpan data)
{
    uint16_t sent_length; // TODO: Confirm how to leverage this or use a nullptr instead

    // Add logic to handle received data
    sl_bt_evt_gatt_server_user_read_request_t * readReq =
        (sl_bt_evt_gatt_server_user_read_request_t *) &(evt->data.evt_gatt_server_user_read_request);

    // TODO: define uint8_t error logic for app error for BLE response
    ChipLogProgress(DeviceLayer, "Handling Read Request for characteristic: %d", readReq->characteristic);
    sl_status_t ret = sl_bt_gatt_server_send_user_read_response(readReq->connection, readReq->characteristic, 0, data.size(),
                                                                data.data(), &sent_length);

    ChipLogProgress(DeviceLayer, "Sent %d of the %d bytes requested", sent_length, data.size());

    if (ret != SL_STATUS_OK)
    {
        ChipLogDetail(DeviceLayer, "Failed to send read response, err:%ld", ret);
    }
}

void BLEChannelImpl::HandleWriteRequest(volatile sl_bt_msg_t * evt, MutableByteSpan data)
{
    sl_bt_evt_gatt_server_user_write_request_t * writeReq =
        (sl_bt_evt_gatt_server_user_write_request_t *) &(evt->data.evt_gatt_server_user_write_request);
    ChipLogProgress(DeviceLayer, "Handling Write Request for characteristic: %d", writeReq->characteristic);
    // TODO: Review what characteristic we want to offer as default, for now we just copy the data to a buffer

    VerifyOrReturn(data.size() >= writeReq->value.len, ChipLogError(DeviceLayer, "Buffer too small for write request"));
    memcpy(data.data(), writeReq->value.data, writeReq->value.len);

    ChipLogProgress(DeviceLayer, "Received Write Request for characteristic: %d, data size: %d", writeReq->characteristic,
                    writeReq->value.len);
    // Log the data received
    ChipLogByteSpan(DeviceLayer, data);

    // TODO: define uint8_t error logic for app error for BLE response
    sl_status_t ret = sl_bt_gatt_server_send_user_write_response(writeReq->connection, writeReq->characteristic, 0);
    if (ret != SL_STATUS_OK)
    {
        ChipLogDetail(DeviceLayer, "Failed to send write response, err:%ld", ret);
    }
}

CHIP_ERROR BLEChannelImpl::HandleCCCDWriteRequest(volatile sl_bt_msg_t * evt, bool & isNewSubscription)
{
    ChipLogProgress(DeviceLayer, "Handling CCCD Write");

    sl_bt_evt_gatt_server_characteristic_status_t * CCCDWriteReq =
        (sl_bt_evt_gatt_server_characteristic_status_t *) &(evt->data.evt_gatt_server_characteristic_status);

    bool isIndicationEnabled = false;
    isNewSubscription        = false;

    VerifyOrReturnLogError(mConnectionState.allocated, CHIP_ERROR_INCORRECT_STATE);
    VerifyOrReturnLogError(mConnectionState.connectionHandle == CCCDWriteReq->connection, CHIP_ERROR_INCORRECT_STATE);

    isIndicationEnabled = (CCCDWriteReq->client_config_flags == sl_bt_gatt_indication);

    if (isIndicationEnabled)
    {
        if (mConnectionState.subscribed)
        {
            isNewSubscription = false; // Already subscribed
        }
        else
        {
            mConnectionState.subscribed = 1;
            ChipLogProgress(DeviceLayer, "CHIPoBLE Subscribe received for characteristic: %d", CCCDWriteReq->characteristic);
            isNewSubscription = true;
        }
    }
    else
    {
        mConnectionState.subscribed = 0;
        ChipLogProgress(DeviceLayer, "CHIPoBLE Unsubscribe received for characteristic: %d", CCCDWriteReq->characteristic);
        isNewSubscription = false;
    }

    // TODO: Leverage Endpoint to send event or implement a timer + callback here
    ChipLogProgress(DeviceLayer, "Note: This is not implemented yet");

    return CHIP_NO_ERROR;
}

void BLEChannelImpl::UpdateMtu(volatile sl_bt_msg_t * evt)
{
    mConnectionState.mtu = evt->data.evt_gatt_mtu_exchanged.mtu;
    ChipLogProgress(DeviceLayer, "MTU exchanged: %d", evt->data.evt_gatt_mtu_exchanged.mtu);
}

CHIP_ERROR BLEChannelImpl::GeneratAdvertisingData(uint8_t discoverMove, uint8_t connectMode, const Optional<uint16_t> & maxEvents)
{
    sl_status_t ret = sl_bt_legacy_advertiser_generate_data(mAdvHandle, discoverMove);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    if (maxEvents.HasValue())
    {
        mAdvMaxEvents = maxEvents.Value();
        // TODO: Revisit a set timing function for the advertising handle
        ret = sl_bt_advertiser_set_timing(mAdvHandle, 160, 160, 0, mAdvMaxEvents);
        VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    }
    mAdvConnectableMode = connectMode;

    ret = sl_bt_legacy_advertiser_start(mAdvHandle, mAdvConnectableMode);

    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::OpenConnection(bd_addr address, uint8_t addrType)
{
    VerifyOrReturnError(addrType <= sl_bt_gap_random_nonresolvable_address, CHIP_ERROR_INVALID_ARGUMENT);
    if (mConnectionState.allocated)
    {
        // We only support one connection at a time for now
        ChipLogError(DeviceLayer, "Connection already allocated");
        return CHIP_ERROR_INCORRECT_STATE;
    }

    sl_status_t ret = sl_bt_connection_open(address, addrType, sl_bt_gap_1m_phy, &mConnectionState.connectionHandle);

    // TODO: Confirm this generates a connection event and the AddConnection gets called so that the connection state is updated
    return MapBLEError(ret);
}
CHIP_ERROR BLEChannelImpl::SetConnectionParams(const Optional<uint8_t> & connectionHandle, uint32_t intervalMin,
                                               uint32_t intervalMax, uint16_t latency, uint16_t timeout)
{
    sl_status_t ret;
    if (connectionHandle.HasValue())
    {
        ret = sl_bt_connection_set_parameters(connectionHandle.Value(), intervalMin, intervalMax, latency, timeout, 0,
                                              kDefaultConnectionEventLength);
    }
    else
    {
        ret = sl_bt_connection_set_default_parameters(intervalMin, intervalMax, latency, timeout, 0, kDefaultConnectionEventLength);
    }
    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::SetAdvertisingParams(uint32_t intervalMin, uint32_t intervalMax, uint16_t duration,
                                                const Optional<uint16_t> & maxEvents, const Optional<uint8_t> & channelMap)
{
    sl_status_t ret;

    mAdvIntervalMin = intervalMin;
    mAdvIntervalMax = intervalMax;
    mAdvDuration    = duration;
    mAdvMaxEvents   = maxEvents.ValueOr(0);

    if (channelMap.HasValue())
    {
        ret = sl_bt_advertiser_set_channel_map(mAdvHandle, channelMap.Value());
        VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    }

    ret = sl_bt_advertiser_set_timing(mAdvHandle, mAdvIntervalMin, mAdvIntervalMax, mAdvDuration, mAdvMaxEvents);
    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::CloseConnection()
{
    sl_status_t ret = sl_bt_connection_close(mConnectionState.connectionHandle);
    // Todo: Confirm this generates a disconnect event and the RemoveConnection gets called
    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::SetAdvHandle(uint8_t handle)
{
    sl_status_t ret;
    if (mAdvHandle == kInvalidAdvertisingHandle)
    {
        mAdvHandle = handle;
        ret        = sl_bt_advertiser_create_set(&mAdvHandle);
    }
    else if (handle == mAdvHandle)
    {
        return CHIP_NO_ERROR;
    }
    else
    {
        ret = sl_bt_advertiser_delete_set(mAdvHandle);
        VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

        mAdvHandle = handle;
        ret        = sl_bt_advertiser_create_set(&mAdvHandle);
    }
    return MapBLEError(ret);
}

CHIP_ERROR BLEChannelImpl::DiscoverServices()
{
    sl_status_t ret = sl_bt_gatt_discover_primary_services(mConnectionState.connectionHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    return CHIP_NO_ERROR;
}
CHIP_ERROR BLEChannelImpl::DiscoverCharacteristics(uint32_t serviceHandle)
{
    sl_status_t ret = sl_bt_gatt_discover_characteristics(mConnectionState.connectionHandle, serviceHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    return CHIP_NO_ERROR;
}

CHIP_ERROR BLEChannelImpl::SetCharacteristicNotification(uint8_t characteristicHandle, uint8_t flags)
{
    sl_status_t ret = sl_bt_gatt_set_characteristic_notification(mConnectionState.connectionHandle, characteristicHandle, flags);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    return CHIP_NO_ERROR;
}

CHIP_ERROR BLEChannelImpl::SetCharacteristicValue(uint8_t characteristicHandle, const ByteSpan & value)
{
    sl_status_t ret =
        sl_bt_gatt_write_characteristic_value(mConnectionState.connectionHandle, characteristicHandle, value.size(), value.data());
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));
    return CHIP_NO_ERROR;
}

} // namespace Internal
} // namespace DeviceLayer
} // namespace chip

```