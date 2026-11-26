```c

> [00:00:00.093][info  ][DL] Starting scheduler
[00:00:00.093][info  ][DL] ==================================================
[00:00:00.093][info  ][DL] SL-Window starting
[00:00:00.093][info  ][DL] ==================================================
[00:00:00.094][info  ][DL] Init CHIP Stack
[00:00:00.125][info  ][DL] Configuring BLE Channel

Missed Logs: 22
[00:00:00.127][info  ][DL] BLE Advertising started successfully

Missed Logs: 3
[00:00:00.127][info  ][DL] Setting device name to : "SL-Window"

Missed Logs: 8
[00:00:00.128][info  ][DL] Provision mode disabled

Missed Logs: 5
[00:00:00.128][info  ][DL] Initializing OpenThread stack
[00:00:00.130][info  ][DL] OpenThread started: OK
[00:00:00.130][info  ][DL] Setting OpenThread device type to SLEEPY END DEVICE
[00:00:00.131][info  ][DL] Starting OpenThread task
[00:00:00.132][info  ][SVR] Initializing subscription resumption storage...
[00:00:00.134][info  ][SVR] Server initializing...
[00:00:00.135][info  ][TS] Last Known Good Time: [unknown]
[00:00:00.188][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.197][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:00.458][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[00:00:00.459][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[00:00:00.459][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3ASAGA442C00KA0648G00
[00:00:00.477][silabs ]App Task started
[00:00:00.477][info  ][ZCL] ConfigStatus 0x7B Operational=1 OnlineReserved=1
[00:00:00.478][info  ][ZCL] Lift(PA=1 Encoder=1 Reversed=0) Tilt(PA=1 Encoder=1)
[00:00:00.478][info  ][ZCL] ConfigStatus 0x7B Operational=1 OnlineReserved=1
[00:00:00.478][info  ][ZCL] Lift(PA=1 Encoder=1 Reversed=0) Tilt(PA=1 Encoder=1)
[00:00:00.479][info  ][ZCL] Mode 0x08 MotorDirReversed=0 LedFeedback=1 Maintenance=0 Calibration=0
[00:00:00.479][info  ][ZCL] ConfigStatus 0x7B Operational=1 OnlineReserved=1
[00:00:00.480][info  ][ZCL] Lift(PA=1 Encoder=1 Reversed=0) Tilt(PA=1 Encoder=1)
[00:00:00.481][info  ][ZCL] ConfigStatus 0x7B Operational=1 OnlineReserved=1
[00:00:00.481][info  ][ZCL] Lift(PA=1 Encoder=1 Reversed=0) Tilt(PA=1 Encoder=1)
[00:00:00.482][info  ][ZCL] Mode 0x08 MotorDirReversed=0 LedFeedback=1 Maintenance=0 Calibration=0
matterCli> [00:00:29.333][info  ][DL] Connect Event for CHIPoBLE on handle : 2
[00:00:29.334][info  ][DL] Connection Parameters Event for handle : 2
[00:00:29.334][info  ][DL] Connection parameter ID received - i:39, l:0, t:42, sm:0
[00:00:29.334][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:100
[00:00:29.335][info  ][DL] Connection phy status ID received - phy:1
[00:00:29.337][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:29.761][info  ][DL] Connection Parameters Event for handle : 2
[00:00:29.761][info  ][DL] Connection parameter ID received - i:78, l:0, t:100, sm:0
[00:00:32.217][info  ][DL] Handling CCCD Write
[00:00:32.217][error ][-] mConnectionState.allocated:347 false: 3
[00:00:32.218][error ][-] Error CHIP:0x00000003 at C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:253
[00:00:32.802][info  ][DL] Char Write Req, char : 23
[00:00:32.803][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.804][info  ][BLE] local and remote recv window sizes = 5
[00:00:32.804][info  ][BLE] selected BTP version 4
[00:00:32.805][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[00:00:33.095][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[00:00:33.095][info  ][DL] CHIPoBLE subscribe received
[00:00:33.095][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[00:00:33.096][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[00:00:33.386][info  ][DL] Tx Confirmation received
[00:00:33.387][info  ][DL]  stop soft timer
[00:00:33.389][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:33.583][info  ][DL] Char Write Req, char : 23
[00:00:33.583][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.583][info  ][EM] >>> [E:33030r S:0 M:18185579] (U) Msg RX from 0:6C66530A2D118324 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[00:00:33.587][info  ][EM] <<< [E:33030r S:0 M:121134560] (U) Msg TX from 0000000000000000 to 0:6C66530A2D118324 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[00:00:33.588][info  ][SVR] Commissioning session establishment step started
[00:00:33.875][info  ][DL] Tx Confirmation received
[00:00:33.875][info  ][DL]  stop soft timer
[00:00:33.876][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:33.877][info  ][DL] Char Write Req, char : 23
[00:00:33.878][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.879][info  ][EM] >>> [E:33030r S:0 M:18185580] (U) Msg RX from 0:6C66530A2D118324 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[00:00:33.969][info  ][EM] <<< [E:33030r S:0 M:121134561] (U) Msg TX from 0000000000000000 to 0:6C66530A2D118324 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[00:00:34.362][info  ][DL] Tx Confirmation received
[00:00:34.363][info  ][DL]  stop soft timer
[00:00:34.365][info  ][DL] Char Write Req, char : 23
[00:00:34.365][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:34.367][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:34.368][info  ][EM] >>> [E:33030r S:0 M:18185581] (U) Msg RX from 0:6C66530A2D118324 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[00:00:34.369][info  ][EM] <<< [E:33030r S:0 M:121134562] (U) Msg TX from 0000000000000000 to 0:6C66530A2D118324 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[00:00:34.376][info  ][SC] SecureSession[0x20006d70, LSID:48002]: State change 'kEstablishing' --> 'kActive'
[00:00:34.376][info  ][SVR] Commissioning completed session establishment step
[00:00:34.377][info  ][DIS] Updating services using commissioning mode 0
[00:00:34.377][error ][DIS] Failed to remove advertised services: 3
[00:00:34.377][error ][DIS] Failed to finalize service update: 3
[00:00:34.378][info  ][SVR] Device completed Rendezvous process
[00:00:34.378][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:34.654][info  ][DL] Tx Confirmation received
[00:00:34.655][info  ][DL]  stop soft timer
[00:00:34.656][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:34.753][info  ][DL] Char Write Req, char : 23
[00:00:34.753][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:34.756][info  ][EM] >>> [E:33031r S:48002 M:258242100] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:134)
[00:00:34.790][info  ][EM] <<< [E:33031r S:48002 M:7332067] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:257)
[00:00:35.240][info  ][DL] Tx Confirmation received
[00:00:35.240][info  ][DL]  stop soft timer
[00:00:35.241][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.434][info  ][DL] Tx Confirmation received
[00:00:35.435][info  ][DL]  stop soft timer
[00:00:35.436][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.629][info  ][DL] Char Write Req, char : 23
[00:00:35.630][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:35.633][info  ][EM] >>> [E:33032r S:48002 M:258242101] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:103)
[00:00:35.651][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0007err = 586
[00:00:35.655][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0006err = 586
[00:00:35.661][info  ][EM] <<< [E:33032r S:48002 M:7332068] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:191)
[00:00:36.019][info  ][DL] Tx Confirmation received
[00:00:36.020][info  ][DL]  stop soft timer
[00:00:36.022][info  ][DL] Char Write Req, char : 23
[00:00:36.022][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.023][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.027][info  ][EM] >>> [E:33033r S:48002 M:258242102] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:36.030][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[00:00:36.033][info  ][EM] <<< [E:33033r S:48002 M:7332069] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:36.214][info  ][DL] Tx Confirmation received
[00:00:36.214][info  ][DL]  stop soft timer
[00:00:36.215][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.314][info  ][DL] Char Write Req, char : 23
[00:00:36.315][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.318][info  ][EM] >>> [E:33034r S:48002 M:258242103] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[00:00:36.324][info  ][EM] <<< [E:33034r S:48002 M:7332070] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:36.897][info  ][DL] Tx Confirmation received
[00:00:36.898][info  ][DL]  stop soft timer
[00:00:36.899][info  ][DL] Char Write Req, char : 23
[00:00:36.900][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.900][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.903][info  ][EM] >>> [E:33035r S:48002 M:258242104] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:36.907][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[00:00:36.911][info  ][EM] <<< [E:33035r S:48002 M:7332071] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[00:00:37.190][info  ][DL] Tx Confirmation received
[00:00:37.190][info  ][DL]  stop soft timer
[00:00:37.191][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:37.677][info  ][DL] Tx Confirmation received
[00:00:37.677][info  ][DL]  stop soft timer
[00:00:37.678][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:37.969][info  ][DL] Tx Confirmation received
[00:00:37.970][info  ][DL]  stop soft timer
[00:00:37.972][info  ][DL] Char Write Req, char : 23
[00:00:37.972][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:37.972][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:37.975][info  ][EM] >>> [E:33036r S:48002 M:258242105] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:37.978][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[00:00:37.982][info  ][EM] <<< [E:33036r S:48002 M:7332072] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[00:00:38.652][info  ][DL] Tx Confirmation received
[00:00:38.653][info  ][DL]  stop soft timer
[00:00:38.653][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:39.042][info  ][DL] Tx Confirmation received
[00:00:39.042][info  ][DL]  stop soft timer
[00:00:39.043][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:39.237][info  ][DL] Tx Confirmation received
[00:00:39.238][info  ][DL]  stop soft timer
[00:00:39.238][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:39.241][info  ][DL] Char Write Req, char : 23
[00:00:39.242][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:39.244][info  ][EM] >>> [E:33037r S:48002 M:258242106] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:39.247][info  ][ZCL] OpCreds: Received an AttestationRequest command
[00:00:39.254][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:599, sig_size:64, err:0x00
[00:00:39.254][info  ][ZCL] OpCreds: AttestationRequest successful.
[00:00:39.258][info  ][EM] <<< [E:33037r S:48002 M:7332073] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[00:00:39.530][info  ][DL] Tx Confirmation received
[00:00:39.531][info  ][DL]  stop soft timer
[00:00:39.531][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:39.822][info  ][DL] Tx Confirmation received
[00:00:39.823][info  ][DL]  stop soft timer
[00:00:39.823][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:40.309][info  ][DL] Tx Confirmation received
[00:00:40.310][info  ][DL]  stop soft timer
[00:00:40.311][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:40.313][info  ][DL] Char Write Req, char : 23
[00:00:40.313][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:40.316][info  ][EM] >>> [E:33038r S:48002 M:258242107] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:40.319][info  ][ZCL] OpCreds: Received a CSRRequest command
[00:00:40.320][error ][CR] WARNING: PSA key recycled: 0 / 17408
[00:00:40.335][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[00:00:40.342][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:277, sig_size:64, err:0x00
[00:00:40.342][info  ][ZCL] OpCreds: CSRRequest successful.
[00:00:40.345][info  ][EM] <<< [E:33038r S:48002 M:7332074] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[00:00:40.797][info  ][DL] Tx Confirmation received
[00:00:40.797][info  ][DL]  stop soft timer
[00:00:40.798][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:41.089][info  ][DL] Tx Confirmation received
[00:00:41.091][info  ][DL]  stop soft timer
[00:00:41.091][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:41.578][info  ][DL] Char Write Req, char : 23
[00:00:41.578][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:41.774][info  ][DL] Char Write Req, char : 23
[00:00:41.774][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:41.777][info  ][EM] >>> [E:33039r S:48002 M:258242108] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[00:00:41.780][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[00:00:41.794][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[00:00:41.797][info  ][EM] <<< [E:33039r S:48002 M:7332075] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[00:00:42.064][info  ][DL] Tx Confirmation received
[00:00:42.065][info  ][DL]  stop soft timer
[00:00:42.066][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:42.260][info  ][DL] Char Write Req, char : 23
[00:00:42.260][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:42.555][info  ][DL] Char Write Req, char : 23
[00:00:42.555][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:42.750][info  ][DL] Char Write Req, char : 23
[00:00:42.750][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:42.753][info  ][EM] >>> [E:33040r S:48002 M:258242109] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[00:00:42.756][info  ][ZCL] OpCreds: Received an AddNOC command
[00:00:42.759][info  ][FP] Validating NOC chain
[00:00:42.791][info  ][FP] NOC chain validation successful
[00:00:42.792][info  ][FP] Added new fabric at index: 0x1
[00:00:42.792][info  ][FP] Assigned compressed fabric ID: 0x2F35D622378DB6C5, node ID: 0x00000000000008CA
[00:00:42.792][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[00:00:42.793][info  ][TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[00:00:42.793][info  ][TS] Retaining current Last Known Good Time
[00:00:42.813][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0x000000000001B669
[00:00:42.813][info  ][DIS] Advertise operational node 2F35D622378DB6C5-00000000000008CA
[00:00:42.814][error ][SVR] Operational advertising failed: 3
[00:00:42.814][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[00:00:42.818][info  ][EM] <<< [E:33040r S:48002 M:7332076] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [B6C5] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:42.942][info  ][DL] Tx Confirmation received
[00:00:42.943][info  ][DL]  stop soft timer
[00:00:42.944][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:43.041][info  ][DL] Char Write Req, char : 23
[00:00:43.041][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:43.044][info  ][EM] >>> [E:33041r S:48002 M:258242110] (S) Msg RX from 1:FFFFFFFB00000000 [B6C5] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[00:00:43.053][info  ][EM] <<< [E:33041r S:48002 M:7332077] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [B6C5] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:43.234][info  ][DL] Tx Confirmation received
[00:00:43.235][info  ][DL]  stop soft timer
[00:00:43.237][info  ][DL] Char Write Req, char : 23
[00:00:43.237][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:43.238][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:43.241][info  ][EM] >>> [E:33042r S:48002 M:258242111] (S) Msg RX from 1:FFFFFFFB00000000 [B6C5] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:43.244][info  ][FS] GeneralCommissioning: Received ArmFailSafe (164s)
[00:00:43.247][info  ][EM] <<< [E:33042r S:48002 M:7332078] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [B6C5] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:43.429][info  ][DL] Tx Confirmation received
[00:00:43.430][info  ][DL]  stop soft timer
[00:00:43.432][info  ][DL] Char Write Req, char : 23
[00:00:43.433][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:43.433][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:43.436][info  ][EM] >>> [E:33043r S:48002 M:258242112] (S) Msg RX from 1:FFFFFFFB00000000 [B6C5] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[00:00:43.467][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[00:00:43.470][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:44.660][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[00:00:44.661][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:44.661][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[00:00:44.666][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[00:00:44.666][info  ][SVR] Scheduling OTA Requestor initialization
[00:00:44.666][info  ][SVR] Joining Multicast groups
[00:00:44.670][info  ][EM] <<< [E:33043r S:48002 M:7332079] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [B6C5] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[00:00:44.671][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[00:00:44.671][info  ][DIS] Advertise operational node 2F35D622378DB6C5-00000000000008CA
[00:00:44.672][error ][SVR] Operational advertising failed: 3
[00:00:44.672][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:44.795][info  ][DL] Tx Confirmation received
[00:00:44.795][info  ][DL]  stop soft timer
[00:00:44.796][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:45.509][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[00:00:45.509][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[00:00:45.509][info  ][SVR] Server initialization complete
[00:00:45.510][info  ][DIS] Updating services using commissioning mode 0
[00:00:45.511][info  ][DIS] Advertise operational node 2F35D622378DB6C5-00000000000008CA
[00:00:45.512][info  ][DL] advertising srp service: 2F35D622378DB6C5-00000000000008CA._matter._tcp
[00:00:45.512][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[00:00:45.530][info  ][IM] No subscriptions to resume
[00:00:47.233][info  ][DL] Char Write Req, char : 23
[00:00:47.233][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:47.602][info  ][EM] >>> [E:33044r S:0 M:18185582] (U) Msg RX from 0:A64A2491F1CDF04A [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[00:00:47.603][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x20008900
[00:00:47.604][info  ][EM] <<< [E:33044r S:0 M:121134563 (Ack:18185582)] (U) Msg TX from 0000000000000000 to 0:A64A2491F1CDF04A [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:45083] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:47.605][info  ][SC] Received Sigma1 msg
[00:00:47.622][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[00:00:47.652][info  ][EM] <<< [E:33044r S:0 M:121134564 (Ack:18185582)] (U) Msg TX from 0000000000000000 to 0:A64A2491F1CDF04A [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:45083] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[00:00:47.654][info  ][EM] ??1 [E:33044r S:0 M:121134564] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3410ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:47.654][info  ][SC] Sent Sigma2 msg
[00:00:48.511][info  ][SWU] Stopping the watchdog timer
[00:00:48.512][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[00:00:49.865][info  ][DL] Tx Confirmation received
[00:00:49.865][info  ][DL]  stop soft timer
[00:00:49.866][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:51.064][info  ][EM] <<1 [E:33044r S:0 M:121134564] (U) Msg Retransmission to 0:0000000000000000
[00:00:51.065][info  ][EM] ??2 [E:33044r S:0 M:121134564] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3380ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:52.282][info  ][EM] >>> [E:33044r S:0 M:18185584 (Ack:121134564)] (U) Msg RX from 0:A64A2491F1CDF04A [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:52.302][info  ][DL] Char Write Req, char : 23
[00:00:52.303][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:54.935][info  ][DL] Tx Confirmation received
[00:00:54.935][info  ][DL]  stop soft timer
[00:00:54.935][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:57.469][info  ][DL] Char Write Req, char : 23
[00:00:57.470][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:01:00.102][info  ][DL] Tx Confirmation received
[00:01:00.103][info  ][DL]  stop soft timer
[00:01:00.103][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:01:00.166][info  ][EM] >>> [E:33044r S:0 M:18185583 (Ack:121134564)] (U) Msg RX from 0:A64A2491F1CDF04A [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[00:01:00.168][info  ][EM] <<< [E:33044r S:0 M:121134565 (Ack:18185583)] (U) Msg TX from 0000000000000000 to 0:A64A2491F1CDF04A [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:45083] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:01:00.169][info  ][SC] Received Sigma3 msg
[00:01:00.228][info  ][EM] <<< [E:33044r S:0 M:121134566 (Ack:18185583)] (U) Msg TX from 0000000000000000 to 0:A64A2491F1CDF04A [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:45083] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[00:01:00.229][info  ][EM] ??1 [E:33044r S:0 M:121134566] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3378ms from now [State:Active II:500 AI:300 AT:4000]
[00:01:00.235][info  ][SC] SecureSession[0x20006e48, LSID:48003]: State change 'kEstablishing' --> 'kActive'
[00:01:00.236][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[00:01:00.237][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:01:00.891][info  ][EM] >>> [E:33045r S:48003 M:263190221] (S) Msg RX from 1:000000000001B669 [B6C5] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[00:01:00.895][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[00:01:00.898][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[00:01:00.911][info  ][TS] Committing Last Known Good Time to storage: 2023-10-10T16:28:52
[00:01:00.924][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x2F35D622378DB6C5, FabricId 0000000000000001, NodeId 00000000000008CA, VendorId 0xFFF1

Missed Logs: 3
[00:01:00.925][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[00:01:00.925][info  ][FS] Fail-safe cleanly disarmed
[00:01:00.929][info  ][EM] <<< [E:33045r S:48003 M:249795557 (Ack:263190221)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [B6C5] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:45083] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[00:01:00.930][info  ][EM] ??1 [E:33045r S:48003 M:249795557] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3368ms from now [State:Active II:500 AI:300 AT:4000]
[00:01:00.931][info  ][EM] >>> [E:33044r S:0 M:18185585 (Ack:121134566)] (U) Msg RX from 0:A64A2491F1CDF04A [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:01:00.932][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[00:01:00.932][info  ][SWU] Device commissioned, schedule a default provider query
[00:01:00.933][info  ][SVR] Commissioning completed successfully
[00:01:00.933][info  ][DIS] Updating services using commissioning mode 0
[00:01:00.933][info  ][DIS] Advertise operational node 2F35D622378DB6C5-00000000000008CA
[00:01:01.078][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[00:01:01.078][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[00:01:01.078][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[00:01:01.554][info  ][EM] >>> [E:33045r S:48003 M:263190222 (Ack:249795557)] (S) Msg RX from 1:000000000001B669 [B6C5] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
```
