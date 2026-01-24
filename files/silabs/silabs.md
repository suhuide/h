

## SDK
[SiliconLabs](https://github.com/SiliconLabs)  
[Matter Extension](https://github.com/SiliconLabs/matter_extension)  
### SiliconLabsSoftware
[Matter Extension](https://github.com/SiliconLabsSoftware/matter_extension/tags)  
[Matter Extension v2.8.0-1.5](https://github.com/SiliconLabsSoftware/matter_extension/pull/297)  
## Radio
```c
// Radio interrupts.
NVIC_SetPriority(FRC_PRI_IRQn, 1);
NVIC_SetPriority(FRC_IRQn, 1);
NVIC_SetPriority(MODEM_IRQn, 1);
NVIC_SetPriority(RAC_SEQ_IRQn, 1);
NVIC_SetPriority(RAC_RSM_IRQn, 1);
NVIC_SetPriority(BUFC_IRQn, 1);
NVIC_SetPriority(AGC_IRQn, 1);
NVIC_SetPriority(PROTIMER_IRQn, 1);
NVIC_SetPriority(RTCC_IRQn, 4);      // Required for EFR32BG1 and EFR32BG12 only.
```
## Reset Reason
### Bootloader
```c
/// Unknown bootloader cause (should never occur)
#define BOOTLOADER_RESET_REASON_UNKNOWN       0x0200u
/// Bootloader caused reset telling app to run
#define BOOTLOADER_RESET_REASON_GO            0x0201u
/// Application requested that bootloader runs
#define BOOTLOADER_RESET_REASON_BOOTLOAD      0x0202u
/// Bootloader detected bad external upgrade image
#define BOOTLOADER_RESET_REASON_BADIMAGE      0x0203u
/// Fatal Error or assert in bootloader
#define BOOTLOADER_RESET_REASON_FATAL         0x0204u
/// Forced bootloader activation
#define BOOTLOADER_RESET_REASON_FORCE         0x0205u
/// OTA Bootloader mode activation
#define BOOTLOADER_RESET_REASON_OTAVALID      0x0206u
/// Bootloader initiated deep sleep
#define BOOTLOADER_RESET_REASON_DEEPSLEEP     0x0207u
/// Application verification failed
#define BOOTLOADER_RESET_REASON_BADAPP        0x0208u
/// Bootloader requested that first stage upgrades main bootloader
#define BOOTLOADER_RESET_REASON_UPGRADE       0x0209u
/// Bootloader timed out waiting for upgrade image
#define BOOTLOADER_RESET_REASON_TIMEOUT       0x020Au
/// Soft-reset was forced to handle a fault
#define BOOTLOADER_RESET_REASON_FAULT         0x020Bu
/// Soft-reset was forced to handle a security fault
#define BOOTLOADER_RESET_REASON_TZ_FAULT      0x020Cu

/// Insufficient slot space to re-create a new firmware
#define BOOTLOADER_RESET_REASON_NO_SLOT_SPACE 0x020Du
/// CRC mismatch of the newly re-constructed firmware
#define BOOTLOADER_RESET_REASON_BADCRC        0x020Eu
/// Re-creation of the new application using the DDFU library failed
#define BOOTLOADER_RESET_REASON_DDFU_FAIL     0x020Fu

/// Reset signature is valid
#define BOOTLOADER_RESET_SIGNATURE_VALID      0xF00Fu
/// Reset signature is invalid
#define BOOTLOADER_RESET_SIGNATURE_INVALID    0xC33Cu
```
### App
```c
typedef enum
{
    OT_PLAT_RESET_REASON_POWER_ON = 0,
    OT_PLAT_RESET_REASON_EXTERNAL = 1,
    OT_PLAT_RESET_REASON_SOFTWARE = 2,
    OT_PLAT_RESET_REASON_FAULT    = 3,
    OT_PLAT_RESET_REASON_CRASH    = 4,
    OT_PLAT_RESET_REASON_ASSERT   = 5,
    OT_PLAT_RESET_REASON_OTHER    = 6,
    OT_PLAT_RESET_REASON_UNKNOWN  = 7,
    OT_PLAT_RESET_REASON_WATCHDOG = 8,

    OT_PLAT_RESET_REASON_COUNT,
} otPlatResetReason;
```