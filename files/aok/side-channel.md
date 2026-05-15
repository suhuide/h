[hrf](../../hrf.md)  
[aok](../../aok.md)  
[SSv6 side channel](sideChannelTestLog.md)

SideChannel 和 Matter CHIPoBLE 在 BLE 栈层面就是两个独立的 advertiser——不同的 handle、不同的数据、不同的 interval。  
真正的区别不在底层 API，而在软件层面的职责分工和事件分发秩序：

||Matter CHIPoBLE|SideChannel|
|------|------|------|
|协议行为	|Matter 规范定义的配网协议，栈自动管理 fast→slow 切换	|无协议约束，应用自由控制|
|事件分发秩序	|优先权：先消费，标记 MatterReservedEvent 就不往下传	|次要权：只拿到 Matter 不处理的事件|

**SideChannel 的真正价值是一个"软件框架"——给你一个结构化的方式在 Matter 旁边加自定义 BLE，保证事件不冲突。**  
**底层就是两个 advertiser 并行广播，谁先处理事件由 sl_bt_on_event() 里的优先级决定。**

## File
```c
matter_2.7.0/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp
STUDIO_SDK_LOC\extension\matter_extension\third_party\matter_sdk\src\platform\silabs\efr32\BLEChannelImpl.cpp
C:\Si\SDKs\simplicity_sdk_v2025.6.2\extension\matter_extension\third_party\matter_sdk\src\platform\silabs\efr32\BLEChannelImpl.cpp
```
```c
/aok02_matter_dc_si_ch/matter_2.7.0/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.h
STUDIO_SDK_LOC\extension\matter_extension\third_party\matter_sdk\src\platform\silabs\efr32\BLEChannelImpl.h
C:\Si\SDKs\simplicity_sdk_v2025.6.2\extension\matter_extension\third_party\matter_sdk\src\platform\silabs\efr32\BLEChannelImpl.h
```
```c
matter_2.7.0/third_party/matter_sdk/examples/platform/silabs/shell/ble/BLEShellCommands.cpp
STUDIO_SDK_LOC\extension\matter_extension\third_party\matter_sdk\examples\platform\silabs\shell\ble
C:\Si\SDKs\simplicity_sdk_v2025.6.2\extension\matter_extension\third_party\matter_sdk\examples\platform\silabs\shell\ble\BLEShellCommands.cpp
```
```c
matter_2.7.0/third_party/matter_sdk/examples/platform/silabs/shell/ble/BLEShellCommands.h
STUDIO_SDK_LOC\extension\matter_extension\third_party\matter_sdk\examples\platform\silabs\shell\ble
C:\Si\SDKs\simplicity_sdk_v2025.6.2\extension\matter_extension\third_party\matter_sdk\examples\platform\silabs\shell\ble\BLEShellCommands.h
```
```c
simplicity_sdk_2025.6.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_gatt_client.a
STUDIO_SDK_LOC\protocol\bluetooth\build\gcc\cortex-m33\ble_host\ble_bgapi\release\libble_bgapi_gatt_client.a
C:\Si\SDKs\simplicity_sdk_v2025.6.2\protocol\bluetooth\build\gcc\cortex-m33\ble_host\ble_bgapi\release\libble_bgapi_gatt_client.a
```
### SSv6
```c
//source
    "${SDK_PATH}/../../matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp"
    "${SDK_PATH}/../../matte66ea43dc8d7de/p/third_party/matter_sdk/examples/platform/silabs/shell/ble/BLEShellCommands.cpp"

//include
    "${SDK_PATH}/../../matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32"
    "${SDK_PATH}/../../matte66ea43dc8d7de/p/third_party/matter_sdk/examples/platform/silabs/shell/ble"    
```
## Cli
```c
matterCli> ble-side

help        Output the BLE Commands help menu
AdvStart    Start BLE Side Channel advertising with default parameters
AdvStop     Stop BLE Side Channel advertising
Notify      Make the side channel send a notify event for its tx characteristic (if the CCCD is set)
Indicate    Make the side channel send an indicate event for its tx characteristic (if the CCCD is set)
Done
```
## BaseApplication
```c
//BaseApplication.cpp                                              
#if defined(SL_BLE_SIDE_CHANNEL_ENABLED) && SL_BLE_SIDE_CHANNEL_ENABLED
    ReturnErrorOnFailure(sBleSideChannel.Init());
    DeviceLayer::Internal::BLEMgrImpl().InjectSideChannel(&sBleSideChannel);

    DeviceLayer::Internal::BLEMgrImpl().SideChannelConfigureAdvertisingDefaultData();
    DeviceLayer::Internal::BLEMgrImpl().SideChannelStartAdvertising();
#endif
```
## Init
```c
//BLEChannelImpl.cpp
CHIP_ERROR BLEChannelImpl::Init()
{
    uint16_t session;
    sl_status_t ret = sl_bt_gattdb_new_session(&session);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Add service
    ret = sl_bt_gattdb_add_service(session, sl_bt_gattdb_primary_service,
                                   0, // not advertised
                                   sizeof(kSideServiceUUID), kSideServiceUUID, &mSideServiceHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Add RX characteristic
    mSideRxChar.buffer = MutableByteSpan(sRxValueBuffer, sizeof(sRxValueBuffer));
    ret                = sl_bt_gattdb_add_uuid128_characteristic(session, mSideServiceHandle,
                                                                 SL_BT_GATTDB_CHARACTERISTIC_READ | SL_BT_GATTDB_CHARACTERISTIC_WRITE,
                                                                 0, // No security
                                                                 0, // No flags
                                                                 kRxUUID, sl_bt_gattdb_variable_length_value,
                                                                 kCharacteristicBufferSize, // Max length
                                                                 kCharacteristicBufferSize, mSideRxChar.buffer.data(), &mSideRxChar.handle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Add TX characteristic
    mSideTxChar.buffer = MutableByteSpan(sTxValueBuffer, sizeof(sTxValueBuffer));
    ret                = sl_bt_gattdb_add_uuid128_characteristic(session, mSideServiceHandle,
                                                                 SL_BT_GATTDB_CHARACTERISTIC_READ | SL_BT_GATTDB_CHARACTERISTIC_WRITE |
                                                                     SL_BT_GATTDB_CHARACTERISTIC_WRITE_NO_RESPONSE |
                                                                     SL_BT_GATTDB_CHARACTERISTIC_NOTIFY | SL_BT_GATTDB_CHARACTERISTIC_INDICATE,
                                                                 0, // No security
                                                                 0, // No flags
                                                                 kTxUUID, sl_bt_gattdb_variable_length_value,
                                                                 kCharacteristicBufferSize, // Max length
                                                                 kCharacteristicBufferSize, mSideTxChar.buffer.data(), &mSideTxChar.handle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_service(session, mSideServiceHandle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_characteristic(session, mSideRxChar.handle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_start_characteristic(session, mSideTxChar.handle);
    VerifyOrReturnError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_gattdb_commit(session);
    return MapBLEError(ret);
}
```
```c
CHIP_ERROR BLEChannelImpl::SetConnectionParams()
    CHIP_ERROR SideChannelSetConnectionParams(const Optional<uint8_t> & connectionHandle, uint32_t intervalMin,
                                              uint32_t intervalMax, uint16_t latency, uint16_t timeout)
```
## InjectSideChannel
```c
//BLEManagerImpl.cpp
CHIP_ERROR BLEManagerImpl::InjectSideChannel(BLEChannel * channel)
{
    VerifyOrReturnError(nullptr != channel, CHIP_ERROR_INVALID_ARGUMENT);
    mBleSideChannel = channel;
    return CHIP_NO_ERROR;
}
```
## SideChannelConfigureAdvertisingDefaultData
```c
//BLEManagerImpl.cpp
CHIP_ERROR BLEManagerImpl::SideChannelConfigureAdvertisingDefaultData(void)
{
    VerifyOrReturnError(mBleSideChannel != nullptr, CHIP_ERROR_INCORRECT_STATE);

    uint8_t advData[MAX_ADV_DATA_LEN];
    uint32_t index = 0;

    // Flags
    advData[index++] = 2;                        // Length
    advData[index++] = CHIP_ADV_DATA_TYPE_FLAGS; // Flags AD Type
    advData[index++] = 0x06;                     // LE General Discoverable Mode, BR/EDR not supported

    // Service UUID
    advData[index++] = 3;                       // Length
    advData[index++] = CHIP_ADV_DATA_TYPE_UUID; // 16-bit UUID
    advData[index++] = 0x34;                    // UUID 0x1234 (little endian)
    advData[index++] = 0x12;
    ByteSpan advDataSpan(advData, index);

    uint8_t responseData[MAX_RESPONSE_DATA_LEN];
    index = 0;

    const char * sideChannelName = "Si-Channel";
    size_t sideChannelNameLen    = strlen(sideChannelName);

    responseData[index++] = static_cast<uint8_t>(sideChannelNameLen + 1);
    responseData[index++] = 0x09; // Complete Local Name
    memcpy(&responseData[index], sideChannelName, sideChannelNameLen);
    index += sideChannelNameLen;
    ByteSpan responseDataSpan(responseData, index);

    AdvConfigStruct config = { advDataSpan,
                               responseDataSpan,
                               BLE_CONFIG_MIN_INTERVAL_SC,
                               BLE_CONFIG_MAX_INTERVAL_SC,
                               sl_bt_advertiser_connectable_scannable,
                               0,
                               0 };
    return mBleSideChannel->ConfigureAdvertising(config);
}
```
## SideChannelStartAdvertising
```c
//BLEManagerImpl.cpp
CHIP_ERROR BLEManagerImpl::SideChannelStartAdvertising(void)
{
    VerifyOrReturnError(mBleSideChannel != nullptr, CHIP_ERROR_INCORRECT_STATE);
    return mBleSideChannel->StartAdvertising();
}
```
```c
//BLEChannelImpl.cpp
CHIP_ERROR BLEChannelImpl::StartAdvertising(void)
{
    // If already advertising, stop it, before changing values
    if (mFlags.Has(Flags::kAdvertising))
    {
        sl_bt_advertiser_stop(mAdvHandle);
    }

    sl_status_t ret;

    ret = sl_bt_advertiser_set_timing(mAdvHandle, mAdvIntervalMin, mAdvIntervalMax, mAdvDuration, mAdvMaxEvents);
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    ret = sl_bt_advertiser_configure(mAdvHandle, kAdvertisingFlagStaticRandomAddress);
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    // Start advertising
    ret = sl_bt_legacy_advertiser_start(mAdvHandle, mAdvConnectableMode);
    VerifyOrReturnLogError(ret == SL_STATUS_OK, MapBLEError(ret));

    mFlags.Set(Flags::kAdvertising);
    ChipLogProgress(DeviceLayer, "BLE Advertising started successfully");

    return CHIP_NO_ERROR;
}
```
## ble on
```c
extern "C" void sl_bt_on_event(sl_bt_msg_t * evt)
{
    [[maybe_unused]] chip::DeviceLayer::Internal::BLEManagerImpl::EventFilter eventFilter;
    eventFilter = chip::DeviceLayer::Internal::BLEMgrImpl().ParseEvent(evt);

#if SL_BLE_SIDE_CHANNEL_ENABLED
    if (chip::DeviceLayer::Internal::BLEMgrImpl().GetSideChannel() != nullptr &&
        eventFilter != chip::DeviceLayer::Internal::BLEManagerImpl::EventFilter::MatterReservedEvent)
    {
        // The side channel may process events directly.
        chip::DeviceLayer::Internal::BLEMgrImpl().GetSideChannel()->ParseEvent(evt);
    }
#endif

#ifdef SL_CATALOG_MATTER_BLE_DMP_TEST_PRESENT
    zigbee_bt_on_event(evt);
#endif // SL_CATALOG_MATTER_BLE_DMP_TEST_PRESENT
}
```