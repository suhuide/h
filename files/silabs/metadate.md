# Bootloader Config
```c
//config/btl_interface_cfg_s2c4.h
#define BOOTLOADER_DISABLE_OLD_BOOTLOADER_MITIGATION 0
// |
// V
#define BOOTLOADER_DISABLE_OLD_BOOTLOADER_MITIGATION 1
```
# Metadata Callback
```c
//third_party/matter_sdk/src/platform/silabs/efr32/OTAImageProcessorImpl.cpp
#ifndef MIN
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#endif
#define MAX_METADATA_LENGTH   512
uint8_t metadata[MAX_METADATA_LENGTH];

void metadataCallback(uint32_t address, uint8_t *data, size_t length, void *context)
{
    uint8_t i;
    ChipLogError(SoftwareUpdate, "%s", __func__);
    for (i = 0; i < MIN(length , MAX_METADATA_LENGTH - address); i++)
    {
        metadata[address + i] = data[i];
        ChipLogError(SoftwareUpdate, "[%ld]:%d", (address + i), metadata[address + i]);
    }
}
void OTAImageProcessorImpl::HandleApply(intptr_t context)
{
    uint32_t err = SL_BOOTLOADER_OK;

    ChipLogProgress(SoftwareUpdate, "HandleApply: verifying image");
    SILABS_TRACE_BEGIN(TimeTraceOperation::kImageVerification);

    // Force KVS to store pending keys such as data from StoreCurrentUpdateInfo()
    PersistedStorage::KeyValueStoreMgrImpl().ForceKeyMapSave();
#if SL_BTLCTRL_MUX
    err = sl_wfx_host_pre_bootloader_spi_transfer();
    if (err != SL_STATUS_OK)
    {
        ChipLogError(SoftwareUpdate, "sl_wfx_host_pre_bootloader_spi_transfer() error: %ld", err);
        SILABS_TRACE_END_ERROR(TimeTraceOperation::kImageVerification, CHIP_ERROR_INTERNAL);
        return;
    }
#endif // SL_BTLCTRL_MUX

#if defined(_SILICON_LABS_32B_SERIES_3) && CHIP_PROGRESS_LOGGING
    osDelay(100); // sl-temp: delay for uart print before verifyImage
#endif            // _SILICON_LABS_32B_SERIES_3 && CHIP_PROGRESS_LOGGING
    LockRadioProcessing();
#if defined(SL_TRUSTZONE_NONSECURE)
    WRAP_BL_DFU_CALL(err = bootloader_verifyImage(mSlotId))
#else
    WRAP_BL_DFU_CALL(err = bootloader_verifyImage(mSlotId, metadataCallback)) //NULL
#endif
    UnlockRadioProcessing();
```