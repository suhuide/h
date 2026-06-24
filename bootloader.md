[hrf](hrf.md)  
# Bootloader Error
## [SWU] bootloader_init Failed error: 259
```c
//Check if we received a valid SFDP signature from the flash device
  if (signature != SFDP_SIGNATURE) {
    return BOOTLOADER_ERROR_INIT_SFDP;
  }
```
**Check Hardware**
## [SWU] bootloader_eraseWriteStorage() error: 1025
```c
/// Invalid slot
#define BOOTLOADER_ERROR_STORAGE_INVALID_SLOT  (BOOTLOADER_ERROR_STORAGE_BASE | 0x01L)
```
**Check Spec and driver**

# External Flash
## Operation(Erase,Write,Read)
```c
//C:\Users\Administrator\.silabs\slt\installs\conan\p\simpl965e19baece23\p\bootloader\platform\bootloader\core\btl_main.c
int main(void)
{
  int32_t ret = BOOTLOADER_ERROR_STORAGE_BOOTLOAD;
  CHIP_Init();
  BTL_DEBUG_PRINTLN("BTL entry");

#if defined(EMU_CMD_EM01VSCALE2) && defined(EMU_STATUS_VSCALEBUSY)
  // Device supports voltage scaling, and the bootloader may have been entered
  // with a downscaled voltage. Scale voltage up to allow flash programming.
  if ((EMU->STATUS & EMU_STATUS_VSCALE_VSCALE2) != EMU_STATUS_VSCALE_VSCALE2) {
    EMU->CMD = EMU_CMD_EM01VSCALE2;
    while (EMU->STATUS & EMU_STATUS_VSCALEBUSY) {
      // Do nothing
    }
  }
#endif

  btl_init();
  #if 0
  ret= storage_eraseRaw(0,4096*2);
  
  if(ret == BOOTLOADER_OK){
    BootloadInfo_t btlInfo = { 0,1,2,3,4,5,6 };
    BootloadInfo_t btlInfo1 = { 0 };
    BootloadInfo_t btlInfo2 = { 0 };
    BootloadInfo_t btlInfo11 = { 0 };
    BootloadInfo_t btlInfo22 = { 0 };
    uint32_t btlInfoAddress0 = 0;
    ret = storage_writeRaw(btlInfoAddress0,
                            (uint8_t *)&btlInfo,
                            sizeof(btlInfo));
    ret = storage_writeRaw(btlInfoAddress0+4096,
                            (uint8_t *)&btlInfo,
                            sizeof(btlInfo));     
    ret = storage_readRaw(btlInfoAddress0, (uint8_t *)&btlInfo1, sizeof(btlInfo1));
    ret = storage_readRaw(btlInfoAddress0+4096, (uint8_t *)&btlInfo2, sizeof(btlInfo2));                                                   
    ret= storage_eraseRaw(0,4096);                        
    // Try reading from first page
    ret = storage_readRaw(btlInfoAddress0, (uint8_t *)&btlInfo11, sizeof(btlInfo11));
    ret = storage_readRaw(btlInfoAddress0+4096, (uint8_t *)&btlInfo22, sizeof(btlInfo22));
    if(ret == BOOTLOADER_OK){
      return ret;
    }
  }
  #endif
#ifdef BOOTLOADER_SUPPORT_STORAGE
  if (!reset_resetCounterEnabled()) {
    // Storage bootloaders might use part of the reason signature as a counter,
    // so only invalidate the signature when the counter is not in use.
    reset_invalidateResetReason();
  }
#else
  reset_invalidateResetReason();
#endif
```

# GBL
## [GBL Format](https://docs.silabs.com/mcu-bootloader/latest/bootloader-user-guide-gsdk-4/02-gecko-bootloader-file-format)  
```c
[HEADER] → [APPLICATION] → [SE UPGRADE] → [BOOTLOADER] → [METADATA / PROG] → [CERTIFICATE] → [SIGNATURE] → [END]
```
## Silabs 文档
GBL 文件的 tag 顺序：
1. GBL_HEADER_TAG    (0x03A6) ← 快
2. GBL_METADATA_TAG  (0x03A4) ← 快  
3. GBL_APP_DATA_TAG  (0x03A8) ← 这里面是2MB的fw+metadata内容，慢！
4. GBL_SIGNATURE_TAG (0x03A7) ← 签名验证
5. GBL_END_TAG       (0x03A9)
我们的 MCU metadata (10字节 header + firmware) 嵌在 GBL_APP_DATA_TAG 里面。这个 tag 的内容有 2MB，bootloader_continueVerifyImage 需要逐块（每次64字节）读出并验证，才能到我们的 metadata 内容。这是顺序的、不可跳过的。

## 官方文档参考
[UG266: Gecko Bootloader User's Guide](https://docs.silabs.com/mcu-bootloader/latest/bootloader-user-guide-gsdk-4/) — GBL 文件格式、tag 结构  
[AN1086: Gecko Bootloader Application Note](https://docs.silabs.com/mcu-bootloader/latest/using-gecko-bootloader-with-bluetooth-apps/) — 验证流程  
[Gecko Bootloader API Reference](https://docs.silabs.com/mcu-bootloader/latest/gecko-bootloader-api/) — bootloader_continueVerifyImage API  