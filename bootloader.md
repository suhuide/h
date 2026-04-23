[hrf](hrf.md)  

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