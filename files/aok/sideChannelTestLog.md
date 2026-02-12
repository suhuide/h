
# Default Config
Only "SL-Window" BLE enable
## Log
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
# Enable before CHIPoBLE
Only "side Channel" BLE enable
## Code
```c
CHIP_ERROR BLEManagerImpl::_Init()
//...
#if SL_USE_INTERNAL_BLE_SIDE_CHANNEL
    ReturnErrorOnFailure(sBleSideChannel.Init());
    BLEMgrImpl().InjectSideChannel(&sBleSideChannel);
    BLEMgrImpl().SideChannelConfigureAdvertisingDefaultData();
    BLEMgrImpl().SideChannelStartAdvertising();
#endif

    PlatformMgr().ScheduleWork(DriveBLEState, 0);
```
## Log
```c
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] SL-Window starting
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.093][info  ][DL] Init CHIP Stack
[00:00:00.123][info  ][DL] Configuring BLE Channel

Missed Logs: 21
[00:00:00.125][info  ][DL] BLE Advertising started successfully

Missed Logs: 4
[00:00:00.125][info  ][DL] Setting device name to : "SL-Window"

Missed Logs: 12
[00:00:00.126][info  ][DL] Provision mode disabled
[00:00:00.126][info  ][DL] Initializing OpenThread stack
[00:00:00.128][info  ][DL] OpenThread started: OK
[00:00:00.128][info  ][DL] Setting OpenThread device type to SLEEPY END DEVICE
[00:00:00.129][info  ][DL] Starting OpenThread task
[00:00:00.130][info  ][SVR] Initializing subscription resumption storage...
[00:00:00.131][info  ][SVR] Server initializing...
[00:00:00.132][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[00:00:00.182][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.188][info  ][SVR] Current Software Version: 1
[00:00:00.427][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[00:00:00.427][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[00:00:00.427][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3ASAGA442C00KA0648G00
[00:00:00.430][silabs ]App Task started
matterCli> [00:15:00.172][info  ][SVR] Closing pairing window
[00:15:00.172][info  ][DIS] Updating services using commissioning mode 0
[00:15:00.173][error ][DIS] Failed to remove advertised services: 3
[00:15:00.173][error ][DIS] Failed to finalize service update: 3
```

# Enable after CHIPoBLE
Only "SL-Window" BLE enable
## Code
```c
void BLEManagerImpl::DriveBLEState(void)
//...
exit:
    if (err != CHIP_NO_ERROR)
    {
        ChipLogError(DeviceLayer, "Disabling CHIPoBLE service due to error: %" CHIP_ERROR_FORMAT, err.Format());
        mServiceMode = ConnectivityManager::kCHIPoBLEServiceMode_Disabled;
    }
    #if SL_USE_INTERNAL_BLE_SIDE_CHANNEL
    sBleSideChannel.Init();
    BLEMgrImpl().InjectSideChannel(&sBleSideChannel);
    BLEMgrImpl().SideChannelConfigureAdvertisingDefaultData();
    BLEMgrImpl().SideChannelStartAdvertising();
    #endif
```
## Log
```c
[00:00:00.092][info  ][DL] Starting scheduler
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] SL-Window starting
[00:00:00.093][info  ][DL] ==================================================
[00:00:00.093][info  ][DL] Init CHIP Stack
[00:00:00.095][info  ][DL] Setting device name to : "SL-Window"
[00:00:00.096][info  ][DL] Provision mode disabled
[00:00:00.096][info  ][DL] Initializing OpenThread stack
[00:00:00.097][info  ][DL] OpenThread started: OK
[00:00:00.165][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.166][info  ][DL] RAIL version:, v3.0.0-b0
[00:00:00.167][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[00:00:00.184][info  ][DL] Configuring BLE Channel
[00:00:00.184][error ][-] ret == SL_STATUS_OK:117 false: 5c0001a
[00:00:00.184][error ][-] ret == SL_STATUS_OK:165 false: 2f

Missed Logs: 6
[00:00:00.203][info  ][DL] Configuring BLE Channel

Missed Logs: 4
[00:00:00.203][error ][-] ret == SL_STATUS_OK:117 false: 5c0001a
[00:00:00.204][error ][-] ret == SL_STATUS_OK:165 false: 2f
[00:00:00.224][info  ][DL] Configuring BLE Channel
[00:00:00.225][error ][-] ret == SL_STATUS_OK:117 false: 5c0001a
[00:00:00.225][error ][-] ret == SL_STATUS_OK:165 false: 2f
[00:00:00.226][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:00.228][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:00.229][info  ][SVR] Current Software Version String: 1
[00:00:00.229][info  ][SVR] Current Software Version: 1
[00:00:00.466][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[00:00:00.467][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[00:00:00.467][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3ASAGA442C00KA0648G00
[00:00:00.470][silabs ]App Task started
matterCli> [00:00:30.170][info  ][DL] Starting advertising with interval_min=240, intverval_max=1920 (units of 625us)
[00:00:30.195][info  ][DL] Configuring BLE Channel
[00:00:30.196][error ][-] ret == SL_STATUS_OK:117 false: 5c0001a
[00:00:30.196][error ][-] ret == SL_STATUS_OK:165 false: 2f
```