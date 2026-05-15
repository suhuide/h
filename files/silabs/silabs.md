

## SDK
[SiliconLabs](https://github.com/SiliconLabs)  
[Matter Extension](https://github.com/SiliconLabs/matter_extension)  
### SiliconLabsSoftware
[Matter Extension](https://github.com/SiliconLabsSoftware/matter_extension/tags)  
[Matter Extension v2.8.0-1.5](https://github.com/SiliconLabsSoftware/matter_extension/pull/297)  
```c
//SSv6 SDK ME
C:\Users\huide\.silabs\slt\installs\conan\p\matte66ea43dc8d7de\p\third_party\matter_sdk
C:\Users\huide\.silabs\slt\installs\conan\p\matte66ea43dc8d7de\p\third_party\matter_sdk\src\platform\silabs\efr32\BLEManagerImpl.cpp
C:\Users\huide\.silabs\slt\installs\conan\p\matte66ea43dc8d7de\p\third_party\matter_sdk\src\platform\silabs\efr32\BLEManagerImpl.h
```
```c
//SiSDK2025.12.3
C:\Users\huide\.silabs\slt\installs\conan\p\simpl35774a752829c\p
//SiSDK2025.12.2
C:\Users\huide\.silabs\slt\installs\conan\p\simpl965e19baece23\p
```
```c
//ME v2.8.1
C:\Users\huide\.silabs\slt\installs\conan\p\matte8bada656e9e76\p\third_party\matter_sdk
C:\Users\huide\.silabs\slt\installs\conan\p\mattef07831835e490\p\third_party\matter_sdk
//ME v2.8.0
C:\Users\huide\.silabs\slt\installs\conan\p\mattecce5da49b7e37\p\third_party\matter_sdk
//ME v2.5.1
C:\Users\huide\.silabs\slt\installs\conan\p\matte67027640a7b4a\p\third_party\matter_sdk
```
## Matter Log Level
```c
config\sl_matter_config.h
// <o SL_MATTER_LOG_LEVEL> Log Level
// <SL_MATTER_LOG_NONE=> None
// <SL_MATTER_LOG_ERROR=> Error
// <SL_MATTER_LOG_PROGRESS=> Progress
// <SL_MATTER_LOG_DETAIL=> Detailed log (debug)
// <SL_MATTER_LOG_AUTOMATION=> Automation
// <i> Default: SL_MATTER_LOG_PROGRESS
// <i> Sets the verbosity of Matter stack logging output
#ifndef SL_MATTER_LOG_LEVEL
#define SL_MATTER_LOG_LEVEL SL_MATTER_LOG_PROGRESS
#endif
```
## [Commander](commander.md)  
## Serial Config
```c
//Lunch Console -> Admin
Usage: serial vcom config [--nostore] [handshake <rts/cts/rtscts/disable/auto>] [speed <9600,921600>]
WSTK> ----- Virtual COM port -----
Stored port speed  : 921600
Active port speed  : 923076
Stored handshake   : disabled
Actual handshake   : disabled

serial vcom config
serial vcom config speed 9600
serial vcom config speed 115200
serial vcom config speed 921600
serial vcom config handshake disable
```
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
## SSv6 log
```c
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] SL-Window starting
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] Init CHIP Stack
[00:00:00.091][info  ][DL] Starting scheduler

Missed Logs: 9
[00:00:00.095][info  ][DL] Setting device name to : "SL-Window"

Missed Logs: 2
[00:00:00.095][info  ][DL] Provision mode disabled
[00:00:00.095][info  ][DL] Initializing OpenThread stack
[00:00:00.097][info  ][DL] OpenThread started: OK
[00:00:00.165][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.165][info  ][DL] RAIL version:, v3.0.0-b0
[00:00:00.166][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[00:00:00.169][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:00.172][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:00.171][info  ][SVR] Current Software Version String: 1
[00:00:00.412][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[00:00:00.413][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[00:00:00.413][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3ASAGA442C00KA0648G00
[00:00:00.416][silabs ]App Task started
```
```c
ParseEvent
    ->sl_bt_evt_system_boot_id
        ->DriveBLEState
            ->StartAdvertising
        ->RAIL_GetVersion
```