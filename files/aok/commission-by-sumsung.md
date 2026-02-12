```c
[16:28:19.230]  device factoryreset
[16:28:19.234]  Performing factory reset ... 
[16:28:19.234]  Done
[16:28:19.234]  [00:02:05.206][info  ][DL] Performing factory reset
[16:28:19.735]  [00:02:05.707][detail][DL] SRP update succeeded
[16:28:19.735]  [00:02:05.707][info  ][DL] Clearing Thread provision
[16:28:19.736]  [00:02:05.707][info  ][DL] Erasing Thread persistent info...
[16:28:19.765]  [00:02:05.736][info  ][DL] System restarting
[16:28:20.492]  [00:00:00.065][info  ][DL] Starting scheduler
[16:28:20.492]  [00:00:00.066][info  ][DL] ==================================================
[16:28:20.493]  [00:00:00.066][info  ][DL]  starting
[16:28:20.493]  [00:00:00.066][info  ][DL] ==================================================
[16:28:20.494]  [00:00:00.066][info  ][DL] Init CHIP Stack
[16:28:20.494]  [00:00:00.068][info  ][DL] Provision mode disabled
[16:28:20.495]  [00:00:00.068][info  ][DL] Initializing OpenThread stack
[16:28:20.496]  [00:00:00.068][info  ][DL] OpenThread started: OK
[16:28:20.496]  [00:00:00.069][info  ][DL] Setting OpenThread device type to SLEEPY END DEVICE
[16:28:20.503]  [00:00:00.130][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[16:28:20.503]  [00:00:00.131][info  ][DL] RAIL version:, v3.0.0-b0
[16:28:20.504]  [00:00:00.131][silabs ]BLE: product type [Pergolux]
[16:28:20.505]  [00:00:00.131][silabs ]BLE: identify addr: D2:60:9E:6A:74:E1 type=1
[16:28:20.506]  [00:00:00.132][silabs ]BLE: MTU size 249
[16:28:20.506]  [00:00:00.133][detail][DL] CHIP event task running
[16:28:20.507]  [00:00:00.134][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:28:20.508]  [00:00:00.134][detail][DL] OpenThread State Changed (Flags: 0x00038210)
[16:28:20.508]  [00:00:00.134][detail][DL]    Network Name: OpenThread
[16:28:20.509]  [00:00:00.134][detail][DL]    PAN Id: 0xFFFF
[16:28:20.510]  [00:00:00.135][detail][DL]    Extended PAN Id: 0xDEAD00BEEF00CAFE
[16:28:20.510]  [00:00:00.135][detail][DL]    Channel: 11
[16:28:20.511]  [00:00:00.135][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64
[16:28:20.512]  [00:00:00.135][info  ][SVR] Current Software Version String: 0.9.7
[16:28:20.513]  [00:00:00.136][info  ][SVR] Current Software Version: 97
[16:28:20.514]  [00:00:00.136][info  ][DL] Device Configuration:
[16:28:20.514]  [00:00:00.136][info  ][DL]   Serial Number: 38398FFFFE520BF5
[16:28:20.514]  [00:00:00.136][info  ][DL]   Vendor Id: 65521 (0xFFF1)
[16:28:20.515]  [00:00:00.137][info  ][DL]   Product Id: 32784 (0x8010)
[16:28:20.516]  [00:00:00.137][info  ][DL]   Product Name: SL_Sample
[16:28:20.517]  [00:00:00.137][info  ][DL]   Hardware Version: 1
[16:28:20.517]  [00:00:00.138][info  ][DL]   Manufacturing Date: (not set)
[16:28:20.518]  [00:00:00.139][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[16:28:20.519]  [00:00:00.139][silabs ]Ver: 97 Btl: 0x03000001 Time:Feb  7 2026 16:21:38
[16:28:20.525]  [00:00:00.153][info  ][DL] Configuring BLE Channel
[16:28:20.525]  [00:00:00.153][detail][DL] BLE Static Device Address D3:DA:8A:D5:E1:C1
[16:28:20.526]  [00:00:00.154][silabs ]BLE: _create_second_adv, adv Handle = 0
[16:28:20.527]  [00:00:00.154][silabs ]BLE: advertiser start
[16:28:20.529]  [00:00:00.156][silabs ]COM: Init done
[16:28:20.529]  [00:00:00.157][silabs ]NWK: open basic commissioning window time 300 sec
[16:28:20.530]  [00:00:00.158][detail][IN] SecureSession[0x20007030]: Allocated Type:1 LSID:15300
[16:28:20.531]  [00:00:00.158][detail][SC] Assigned local session key ID 15300
[16:28:20.532]  [00:00:00.158][detail][SC] Waiting for PBKDF param request
[16:28:20.532]  [00:00:00.159][info  ][DIS] Updating services using commissioning mode 1
[16:28:20.533]  [00:00:00.159][error ][DIS] Failed to remove advertised services: 3
[16:28:20.534]  [00:00:00.159][detail][DL] Using Thread extended MAC for hostname.
[16:28:20.535]  [00:00:00.159][detail][DIS] DNS-SD Pairing Instruction not set
[16:28:20.535]  [00:00:00.160][info  ][DIS] Advertise commission parameter vendorID=65521 productID=32784 discriminator=3840/15 cm=1 cp=0 jf=0
[16:28:20.537]  [00:00:00.160][error ][DIS] Failed to advertise commissionable node: 3
[16:28:20.537]  [00:00:00.160][error ][DIS] Failed to finalize service update: 3
[16:28:20.538]  [00:00:00.160][detail][DL] Start BLE advertisement
[16:28:20.539]  [00:00:00.161][detail][DL] BLE Static Device Address C1:9D:B9:CC:70:B0
[16:28:20.539]  [00:00:00.162][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[16:28:20.541]  [00:00:00.163][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:28:20.541]  [00:00:00.163][silabs ]NWK: platform event type 800d
[16:28:20.542]  [00:00:00.163][silabs ]COM: notify network [Leave]
[16:28:20.543]  [00:00:00.164][silabs ]App Task started
[16:28:33.761]  [00:00:13.388][info  ][DL] Connect Event for CHIPoBLE on handle : 2
[16:28:33.762]  [00:00:13.388][info  ][DL] Connection Parameters Event for handle : 2
[16:28:33.762]  [00:00:13.388][info  ][DL] Connection parameter ID received - i:24, l:0, t:500, sm:0
[16:28:33.763]  [00:00:13.388][info  ][DL] Connection phy status ID received - phy:1
[16:28:33.764]  [00:00:13.389][info  ][DL] Handling CCCD Write
[16:28:33.764]  [00:00:13.389][error ][-] mConnectionState.allocated:430 false: 3
[16:28:33.765]  [00:00:13.389][error ][-] Error CHIP:0x00000003 at C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:303
[16:28:33.802]  [00:00:13.429][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:27, rxL:328
[16:28:33.890]  [00:00:13.518][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:247, rxL:2120
[16:28:33.921]  [00:00:13.547][info  ][DL] Char Write Req, char : 47
[16:28:33.921]  [00:00:13.548][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 9)
[16:28:33.922]  [00:00:13.548][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:33.922]  [00:00:13.548][info  ][BLE] local and remote recv window sizes = 5
[16:28:33.923]  [00:00:13.548][info  ][BLE] selected BTP version 4
[16:28:33.924]  [00:00:13.548][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[16:28:33.980]  [00:00:13.608][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[16:28:33.981]  [00:00:13.608][info  ][DL] CHIPoBLE subscribe received
[16:28:33.982]  [00:00:13.609][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[16:28:33.982]  [00:00:13.609][detail][IN] BLE EndPoint 0x20012a2c Connection Complete
[16:28:33.983]  [00:00:13.609][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[16:28:33.984]  [00:00:13.609][silabs ]NWK: platform event type 8006
[16:28:33.984]  [00:00:13.610][silabs ]COM: notify network [Leave]
[16:28:34.040]  [00:00:13.667][info  ][DL] Tx Confirmation received
[16:28:34.040]  [00:00:13.667][info  ][DL]  stop soft timer
[16:28:34.040]  [00:00:13.667][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.041]  [00:00:13.669][info  ][DL] Char Write Req, char : 47
[16:28:34.042]  [00:00:13.669][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 103)
[16:28:34.043]  [00:00:13.669][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.044]  [00:00:13.670][info  ][EM] >>> [E:5458r S:0 M:177138339] (U) Msg RX from 0:14F5C1C2202AF01C [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[16:28:34.045]  [00:00:13.670][detail][EM] Handling via exchange: 5458r, Delegate: 0x200097b8
[16:28:34.047]  [00:00:13.670][detail][SC] Received PBKDF param request
[16:28:34.047]  [00:00:13.671][detail][SC] Peer assigned session ID 11624
[16:28:34.048]  [00:00:13.671][detail][SC] Found MRP parameters in the message
[16:28:34.049]  [00:00:13.673][info  ][EM] <<< [E:5458r S:0 M:18459222] (U) Msg TX from 0000000000000000 to 0:14F5C1C2202AF01C [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[16:28:34.050]  [00:00:13.674][detail][SC] Sent PBKDF param response
[16:28:34.051]  [00:00:13.674][info  ][SVR] Commissioning session establishment step started
[16:28:34.100]  [00:00:13.727][info  ][DL] Tx Confirmation received
[16:28:34.100]  [00:00:13.728][info  ][DL]  stop soft timer
[16:28:34.100]  [00:00:13.728][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.101]  [00:00:13.729][info  ][DL] Char Write Req, char : 47
[16:28:34.102]  [00:00:13.730][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 97)
[16:28:34.103]  [00:00:13.730][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.104]  [00:00:13.731][info  ][EM] >>> [E:5458r S:0 M:177138340] (U) Msg RX from 0:14F5C1C2202AF01C [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[16:28:34.105]  [00:00:13.731][detail][EM] Found matching exchange: 5458r, Delegate: 0x200097b8
[16:28:34.107]  [00:00:13.731][detail][SC] Received spake2p msg1
[16:28:34.161]  [00:00:13.790][info  ][EM] <<< [E:5458r S:0 M:18459223] (U) Msg TX from 0000000000000000 to 0:14F5C1C2202AF01C [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[16:28:34.163]  [00:00:13.790][detail][SC] Sent spake2p msg2
[16:28:34.220]  [00:00:13.847][info  ][DL] Tx Confirmation received
[16:28:34.220]  [00:00:13.847][info  ][DL]  stop soft timer
[16:28:34.221]  [00:00:13.848][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.222]  [00:00:13.849][info  ][DL] Char Write Req, char : 47
[16:28:34.222]  [00:00:13.849][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 64)
[16:28:34.223]  [00:00:13.849][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.224]  [00:00:13.850][info  ][EM] >>> [E:5458r S:0 M:177138341] (U) Msg RX from 0:14F5C1C2202AF01C [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[16:28:34.226]  [00:00:13.850][detail][EM] Found matching exchange: 5458r, Delegate: 0x200097b8
[16:28:34.226]  [00:00:13.850][detail][SC] Received spake2p msg3
[16:28:34.227]  [00:00:13.851][detail][SC] Sending status report. Protocol code 0, exchange 5458
[16:28:34.228]  [00:00:13.852][info  ][EM] <<< [E:5458r S:0 M:18459224] (U) Msg TX from 0000000000000000 to 0:14F5C1C2202AF01C [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[16:28:34.230]  [00:00:13.856][info  ][SC] SecureSession[0x20007030, LSID:15300]: State change 'kEstablishing' --> 'kActive'
[16:28:34.231]  [00:00:13.856][detail][IN] SecureSession[0x20007030]: Activated - Type:1 LSID:15300
[16:28:34.232]  [00:00:13.856][detail][IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:15300 PSID:11624!
[16:28:34.233]  [00:00:13.857][info  ][SVR] Commissioning completed session establishment step
[16:28:34.234]  [00:00:13.857][info  ][DIS] Updating services using commissioning mode 0
[16:28:34.235]  [00:00:13.857][error ][DIS] Failed to remove advertised services: 3
[16:28:34.236]  [00:00:13.857][error ][DIS] Failed to finalize service update: 3
[16:28:34.237]  [00:00:13.857][info  ][SVR] Device completed Rendezvous process
[16:28:34.238]  [00:00:13.858][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:28:34.238]  [00:00:13.858][silabs ]NWK: platform event type 8018
[16:28:34.239]  [00:00:13.859][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:28:34.280]  [00:00:13.908][info  ][DL] Tx Confirmation received
[16:28:34.280]  [00:00:13.908][info  ][DL]  stop soft timer
[16:28:34.281]  [00:00:13.908][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.282]  [00:00:13.909][info  ][DL] Char Write Req, char : 47
[16:28:34.282]  [00:00:13.909][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.284]  [00:00:13.910][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.284]  [00:00:13.912][info  ][EM] >>> [E:5459r S:15300 M:267692763] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.286]  [00:00:13.912][detail][EM] Handling via exchange: 5459r, Delegate: 0x2000413c
[16:28:34.287]  [00:00:13.912][detail][IM] Received Read request
[16:28:34.287]  [00:00:13.913][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.288]  [00:00:13.914][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.290]  [00:00:13.914][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:28:34.291]  [00:00:13.915][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:28:34.292]  [00:00:13.916][detail][DMG] <RE> Sending report (payload has 37 bytes)...
[16:28:34.293]  [00:00:13.917][info  ][EM] <<< [E:5459r S:15300 M:41349844] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[16:28:34.294]  [00:00:13.918][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.295]  [00:00:13.918][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.296]  [00:00:13.919][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.297]  [00:00:13.919][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.340]  [00:00:13.967][info  ][DL] Tx Confirmation received
[16:28:34.340]  [00:00:13.967][info  ][DL]  stop soft timer
[16:28:34.341]  [00:00:13.968][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.342]  [00:00:13.969][info  ][DL] Char Write Req, char : 47
[16:28:34.342]  [00:00:13.969][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.343]  [00:00:13.969][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.344]  [00:00:13.971][info  ][EM] >>> [E:5460r S:15300 M:267692764] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.346]  [00:00:13.972][detail][EM] Handling via exchange: 5460r, Delegate: 0x2000413c
[16:28:34.347]  [00:00:13.972][detail][IM] Received Read request
[16:28:34.347]  [00:00:13.973][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.348]  [00:00:13.973][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.349]  [00:00:13.974][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:28:34.350]  [00:00:13.975][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:28:34.351]  [00:00:13.976][detail][DMG] <RE> Sending report (payload has 37 bytes)...
[16:28:34.352]  [00:00:13.978][info  ][EM] <<< [E:5460r S:15300 M:41349845] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[16:28:34.354]  [00:00:13.979][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.355]  [00:00:13.979][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.356]  [00:00:13.979][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.356]  [00:00:13.979][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.400]  [00:00:14.028][info  ][DL] Tx Confirmation received
[16:28:34.400]  [00:00:14.028][info  ][DL]  stop soft timer
[16:28:34.400]  [00:00:14.028][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.401]  [00:00:14.029][info  ][DL] Char Write Req, char : 47
[16:28:34.402]  [00:00:14.029][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.403]  [00:00:14.030][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.404]  [00:00:14.032][info  ][EM] >>> [E:5461r S:15300 M:267692765] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.405]  [00:00:14.032][detail][EM] Handling via exchange: 5461r, Delegate: 0x2000413c
[16:28:34.407]  [00:00:14.032][detail][IM] Received Read request
[16:28:34.407]  [00:00:14.033][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.408]  [00:00:14.033][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.409]  [00:00:14.034][detail][DMG] <RE:Run> Cluster 28, Attribute 12 is dirty
[16:28:34.410]  [00:00:14.035][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0012 (expanded=0)
[16:28:34.411]  [00:00:14.036][detail][DMG] <RE> Sending report (payload has 52 bytes)...
[16:28:34.412]  [00:00:14.038][info  ][EM] <<< [E:5461r S:15300 M:41349846] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:82)
[16:28:34.413]  [00:00:14.039][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.414]  [00:00:14.039][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.416]  [00:00:14.040][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.416]  [00:00:14.040][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.460]  [00:00:14.087][info  ][DL] Tx Confirmation received
[16:28:34.460]  [00:00:14.087][info  ][DL]  stop soft timer
[16:28:34.461]  [00:00:14.087][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.462]  [00:00:14.089][info  ][DL] Char Write Req, char : 47
[16:28:34.462]  [00:00:14.089][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.463]  [00:00:14.089][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.464]  [00:00:14.091][info  ][EM] >>> [E:5462r S:15300 M:267692766] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.466]  [00:00:14.092][detail][EM] Handling via exchange: 5462r, Delegate: 0x2000413c
[16:28:34.466]  [00:00:14.092][detail][IM] Received Read request
[16:28:34.467]  [00:00:14.093][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.468]  [00:00:14.093][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.469]  [00:00:14.094][detail][DMG] <RE:Run> Cluster 28, Attribute 5 is dirty
[16:28:34.470]  [00:00:14.095][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=0)
[16:28:34.471]  [00:00:14.096][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:34.472]  [00:00:14.098][info  ][EM] <<< [E:5462r S:15300 M:41349847] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:34.474]  [00:00:14.099][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.475]  [00:00:14.099][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.476]  [00:00:14.099][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.476]  [00:00:14.099][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.520]  [00:00:14.147][info  ][DL] Tx Confirmation received
[16:28:34.520]  [00:00:14.148][info  ][DL]  stop soft timer
[16:28:34.520]  [00:00:14.148][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.521]  [00:00:14.149][info  ][DL] Char Write Req, char : 47
[16:28:34.522]  [00:00:14.149][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.523]  [00:00:14.150][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.525]  [00:00:14.152][info  ][EM] >>> [E:5463r S:15300 M:267692767] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.526]  [00:00:14.153][detail][EM] Handling via exchange: 5463r, Delegate: 0x2000413c
[16:28:34.527]  [00:00:14.153][detail][IM] Received Read request
[16:28:34.527]  [00:00:14.154][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.528]  [00:00:14.154][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.529]  [00:00:14.155][detail][DMG] <RE:Run> Cluster 28, Attribute 9 is dirty
[16:28:34.531]  [00:00:14.156][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=0)
[16:28:34.531]  [00:00:14.157][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:34.533]  [00:00:14.159][info  ][EM] <<< [E:5463r S:15300 M:41349848] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:34.534]  [00:00:14.160][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.535]  [00:00:14.160][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.536]  [00:00:14.160][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.537]  [00:00:14.160][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.580]  [00:00:14.208][info  ][DL] Tx Confirmation received
[16:28:34.580]  [00:00:14.208][info  ][DL]  stop soft timer
[16:28:34.580]  [00:00:14.208][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.581]  [00:00:14.208][info  ][DL] Char Write Req, char : 47
[16:28:34.582]  [00:00:14.209][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.583]  [00:00:14.209][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.584]  [00:00:14.211][info  ][EM] >>> [E:5464r S:15300 M:267692768] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.585]  [00:00:14.211][detail][EM] Handling via exchange: 5464r, Delegate: 0x2000413c
[16:28:34.586]  [00:00:14.212][detail][IM] Received Read request
[16:28:34.586]  [00:00:14.212][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.587]  [00:00:14.213][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.589]  [00:00:14.214][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:28:34.590]  [00:00:14.214][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:28:34.591]  [00:00:14.215][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:34.592]  [00:00:14.217][info  ][EM] <<< [E:5464r S:15300 M:41349849] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:34.593]  [00:00:14.218][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.594]  [00:00:14.218][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.596]  [00:00:14.218][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.596]  [00:00:14.219][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet 
[16:28:34.640]  [00:00:14.268][info  ][DL] Tx Confirmation received
[16:28:34.640]  [00:00:14.268][info  ][DL]  stop soft timer
[16:28:34.640]  [00:00:14.268][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.731]  [00:00:14.358][info  ][DL] Char Write Req, char : 47
[16:28:34.731]  [00:00:14.359][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.733]  [00:00:14.359][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.734]  [00:00:14.361][info  ][EM] >>> [E:5465r S:15300 M:267692769] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.736]  [00:00:14.361][detail][EM] Handling via exchange: 5465r, Delegate: 0x2000413c
[16:28:34.736]  [00:00:14.361][detail][IM] Received Read request
[16:28:34.737]  [00:00:14.362][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.738]  [00:00:14.363][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.739]  [00:00:14.364][detail][DMG] <RE:Run> Cluster 3e, Attribute 2 is dirty
[16:28:34.740]  [00:00:14.365][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:28:34.741]  [00:00:14.367][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:34.742]  [00:00:14.369][info  ][EM] <<< [E:5465r S:15300 M:41349850] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:34.744]  [00:00:14.370][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.745]  [00:00:14.370][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.745]  [00:00:14.370][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.746]  [00:00:14.370][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.790]  [00:00:14.417][info  ][DL] Tx Confirmation received
[16:28:34.790]  [00:00:14.417][info  ][DL]  stop soft timer
[16:28:34.792]  [00:00:14.417][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.792]  [00:00:14.419][info  ][DL] Char Write Req, char : 47
[16:28:34.792]  [00:00:14.419][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:34.794]  [00:00:14.419][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.794]  [00:00:14.421][info  ][EM] >>> [E:5466r S:15300 M:267692770] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:34.797]  [00:00:14.421][detail][EM] Handling via exchange: 5466r, Delegate: 0x2000413c
[16:28:34.797]  [00:00:14.422][detail][IM] Received Read request
[16:28:34.798]  [00:00:14.423][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:34.799]  [00:00:14.423][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:34.800]  [00:00:14.424][detail][DMG] <RE:Run> Cluster 30, Attribute 4 is dirty
[16:28:34.801]  [00:00:14.424][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:28:34.802]  [00:00:14.425][detail][DMG] <RE> Sending report (payload has 35 bytes)...
[16:28:34.803]  [00:00:14.428][info  ][EM] <<< [E:5466r S:15300 M:41349851] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:65)
[16:28:34.805]  [00:00:14.428][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:34.806]  [00:00:14.429][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:34.806]  [00:00:14.429][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:34.807]  [00:00:14.429][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:34.850]  [00:00:14.477][info  ][DL] Tx Confirmation received
[16:28:34.850]  [00:00:14.478][info  ][DL]  stop soft timer
[16:28:34.851]  [00:00:14.478][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.852]  [00:00:14.479][info  ][DL] Char Write Req, char : 47
[16:28:34.853]  [00:00:14.479][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 44)
[16:28:34.854]  [00:00:14.479][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.855]  [00:00:14.481][info  ][EM] >>> [E:5467r S:15300 M:267692771] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[16:28:34.856]  [00:00:14.481][detail][EM] Handling via exchange: 5467r, Delegate: 0x2000413c
[16:28:34.857]  [00:00:14.482][detail][DMG] Got Timed Request with timeout 10000: handler 0x200046b8 exchange 5467r
[16:28:34.858]  [00:00:14.483][info  ][EM] <<< [E:5467r S:15300 M:41349852] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[16:28:34.860]  [00:00:14.484][detail][DMG] Timed Request time limit 0x0000000000005FA4: handler 0x200046b8 exchange 5467r
[16:28:34.910]  [00:00:14.538][info  ][DL] Tx Confirmation received
[16:28:34.910]  [00:00:14.538][info  ][DL]  stop soft timer
[16:28:34.911]  [00:00:14.538][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.912]  [00:00:14.539][info  ][DL] Char Write Req, char : 47
[16:28:34.912]  [00:00:14.540][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:28:34.914]  [00:00:14.540][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.914]  [00:00:14.541][info  ][EM] >>> [E:5467r S:15300 M:267692772] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:28:34.916]  [00:00:14.541][detail][EM] Found matching exchange: 5467r, Delegate: 0x200046b8
[16:28:34.917]  [00:00:14.542][detail][DMG] Timed following action arrived at 0x00000000000038CE: handler 0x200046b8 exchange 5467r
[16:28:34.918]  [00:00:14.542][detail][DMG] Handing timed invoke to IM engine: handler 0x200046b8 exchange 5467r
[16:28:34.919]  [00:00:14.543][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:28:34.921]  [00:00:14.543][info  ][FS] GeneralCommissioning: Received ArmFailSafe (240s)
[16:28:34.921]  [00:00:14.543][detail][DMG] Command handler moving to [NewRespons]
[16:28:34.922]  [00:00:14.544][detail][DMG] Command handler moving to [ Preparing]
[16:28:34.923]  [00:00:14.544][detail][DMG] Command handler moving to [AddingComm]
[16:28:34.923]  [00:00:14.544][detail][DMG] Command handler moving to [AddedComma]
[16:28:34.924]  [00:00:14.544][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:34.925]  [00:00:14.544][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:34.926]  [00:00:14.545][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:34.927]  [00:00:14.547][info  ][EM] <<< [E:5467r S:15300 M:41349853] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:28:34.929]  [00:00:14.547][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:34.970]  [00:00:14.597][info  ][DL] Tx Confirmation received
[16:28:34.970]  [00:00:14.597][info  ][DL]  stop soft timer
[16:28:34.971]  [00:00:14.598][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:34.971]  [00:00:14.599][info  ][DL] Char Write Req, char : 47
[16:28:34.972]  [00:00:14.599][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:28:34.974]  [00:00:14.599][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:34.974]  [00:00:14.601][info  ][EM] >>> [E:5468r S:15300 M:267692773] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:28:34.976]  [00:00:14.602][detail][EM] Handling via exchange: 5468r, Delegate: 0x2000413c
[16:28:34.977]  [00:00:14.603][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:28:34.978]  [00:00:14.603][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[16:28:34.978]  [00:00:14.604][detail][DMG] Command handler moving to [NewRespons]
[16:28:34.980]  [00:00:14.604][detail][DMG] Command handler moving to [ Preparing]
[16:28:34.981]  [00:00:14.604][detail][DMG] Command handler moving to [AddingComm]
[16:28:34.981]  [00:00:14.604][detail][DMG] Command handler moving to [AddedComma]
[16:28:34.982]  [00:00:14.604][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:34.983]  [00:00:14.605][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:34.984]  [00:00:14.605][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:34.985]  [00:00:14.607][info  ][EM] <<< [E:5468r S:15300 M:41349854] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[16:28:34.987]  [00:00:14.608][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:35.030]  [00:00:14.658][info  ][DL] Tx Confirmation received
[16:28:35.030]  [00:00:14.658][info  ][DL]  stop soft timer
[16:28:35.031]  [00:00:14.658][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:35.090]  [00:00:14.717][info  ][DL] Tx Confirmation received
[16:28:35.090]  [00:00:14.718][info  ][DL]  stop soft timer
[16:28:35.091]  [00:00:14.718][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:35.150]  [00:00:14.778][info  ][DL] Tx Confirmation received
[16:28:35.150]  [00:00:14.778][info  ][DL]  stop soft timer
[16:28:35.151]  [00:00:14.778][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:35.151]  [00:00:14.779][info  ][DL] Char Write Req, char : 47
[16:28:35.152]  [00:00:14.779][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:28:35.153]  [00:00:14.780][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:35.154]  [00:00:14.782][info  ][EM] >>> [E:5469r S:15300 M:267692774] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:28:35.155]  [00:00:14.782][detail][EM] Handling via exchange: 5469r, Delegate: 0x2000413c
[16:28:35.157]  [00:00:14.783][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:28:35.157]  [00:00:14.784][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[16:28:35.158]  [00:00:14.784][detail][DMG] Command handler moving to [NewRespons]
[16:28:35.159]  [00:00:14.785][detail][DMG] Command handler moving to [ Preparing]
[16:28:35.160]  [00:00:14.785][detail][DMG] Command handler moving to [AddingComm]
[16:28:35.161]  [00:00:14.785][detail][DMG] Command handler moving to [AddedComma]
[16:28:35.162]  [00:00:14.786][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:35.162]  [00:00:14.786][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:35.163]  [00:00:14.786][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:35.164]  [00:00:14.789][info  ][EM] <<< [E:5469r S:15300 M:41349855] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[16:28:35.166]  [00:00:14.789][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:35.210]  [00:00:14.837][info  ][DL] Tx Confirmation received
[16:28:35.210]  [00:00:14.837][info  ][DL]  stop soft timer
[16:28:35.211]  [00:00:14.838][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:35.270]  [00:00:14.898][info  ][DL] Tx Confirmation received
[16:28:35.270]  [00:00:14.898][info  ][DL]  stop soft timer
[16:28:35.271]  [00:00:14.898][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:35.330]  [00:00:14.958][info  ][DL] Tx Confirmation received
[16:28:35.330]  [00:00:14.958][info  ][DL]  stop soft timer
[16:28:35.331]  [00:00:14.958][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:37.042]  [00:00:16.668][info  ][DL] Char Write Req, char : 47
[16:28:37.042]  [00:00:16.668][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 101)
[16:28:37.043]  [00:00:16.669][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:37.044]  [00:00:16.671][info  ][EM] >>> [E:5470r S:15300 M:267692775] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:96)
[16:28:37.046]  [00:00:16.672][detail][EM] Handling via exchange: 5470r, Delegate: 0x2000413c
[16:28:37.046]  [00:00:16.673][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0004
[16:28:37.048]  [00:00:16.674][info  ][ZCL] OpCreds: Received a CSRRequest command
[16:28:37.049]  [00:00:16.674][error ][CR] WARNING: PSA key recycled: 0 / 17408
[16:28:37.060]  [00:00:16.688][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[16:28:37.067]  [00:00:16.694][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:278, sig_size:64, err:0x00
[16:28:37.067]  [00:00:16.694][info  ][ZCL] OpCreds: CSRRequest successful.
[16:28:37.068]  [00:00:16.694][detail][DMG] Command handler moving to [NewRespons]
[16:28:37.069]  [00:00:16.694][detail][DMG] Command handler moving to [ Preparing]
[16:28:37.070]  [00:00:16.695][detail][DMG] Command handler moving to [AddingComm]
[16:28:37.070]  [00:00:16.695][detail][DMG] Command handler moving to [AddedComma]
[16:28:37.071]  [00:00:16.695][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:37.072]  [00:00:16.695][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:37.073]  [00:00:16.696][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:37.074]  [00:00:16.698][info  ][EM] <<< [E:5470r S:15300 M:41349856] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:393)
[16:28:37.076]  [00:00:16.699][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:37.130]  [00:00:16.757][info  ][DL] Tx Confirmation received
[16:28:37.130]  [00:00:16.758][info  ][DL]  stop soft timer
[16:28:37.131]  [00:00:16.758][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:37.190]  [00:00:16.818][info  ][DL] Tx Confirmation received
[16:28:37.190]  [00:00:16.818][info  ][DL]  stop soft timer
[16:28:37.191]  [00:00:16.818][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:37.821]  [00:00:17.449][info  ][DL] Char Write Req, char : 47
[16:28:37.821]  [00:00:17.449][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:37.823]  [00:00:17.449][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:37.823]  [00:00:17.451][info  ][EM] >>> [E:5471r S:15300 M:267692776] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:37.826]  [00:00:17.452][detail][EM] Handling via exchange: 5471r, Delegate: 0x2000413c
[16:28:37.826]  [00:00:17.452][detail][IM] Received Read request
[16:28:37.827]  [00:00:17.453][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:37.828]  [00:00:17.453][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:37.829]  [00:00:17.454][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:28:37.830]  [00:00:17.454][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:28:37.831]  [00:00:17.456][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:37.832]  [00:00:17.457][info  ][EM] <<< [E:5471r S:15300 M:41349857] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:37.834]  [00:00:17.458][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:37.835]  [00:00:17.458][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:37.835]  [00:00:17.458][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:37.836]  [00:00:17.458][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:37.880]  [00:00:17.507][info  ][DL] Tx Confirmation received
[16:28:37.880]  [00:00:17.507][info  ][DL]  stop soft timer
[16:28:37.881]  [00:00:17.508][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:37.883]  [00:00:17.511][info  ][DL] Char Write Req, char : 47
[16:28:37.883]  [00:00:17.511][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:28:37.885]  [00:00:17.511][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:37.941]  [00:00:17.569][info  ][DL] Char Write Req, char : 47
[16:28:37.941]  [00:00:17.569][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 87)
[16:28:37.943]  [00:00:17.569][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:37.944]  [00:00:17.571][info  ][EM] >>> [E:5472r S:15300 M:267692777] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:324)
[16:28:37.945]  [00:00:17.572][detail][EM] Handling via exchange: 5472r, Delegate: 0x2000413c
[16:28:37.946]  [00:00:17.573][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B
[16:28:37.948]  [00:00:17.573][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[16:28:37.959]  [00:00:17.586][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[16:28:37.960]  [00:00:17.586][detail][DMG] Command handler moving to [NewRespons]
[16:28:37.960]  [00:00:17.586][detail][DMG] Command handler moving to [ Preparing]
[16:28:37.961]  [00:00:17.586][detail][DMG] Command handler moving to [AddingComm]
[16:28:37.962]  [00:00:17.586][detail][DMG] Command handler moving to [AddedComma]
[16:28:37.962]  [00:00:17.587][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:37.963]  [00:00:17.587][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:37.964]  [00:00:17.587][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:37.965]  [00:00:17.589][info  ][EM] <<< [E:5472r S:15300 M:41349858] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[16:28:37.967]  [00:00:17.590][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:38.030]  [00:00:17.658][info  ][DL] Tx Confirmation received
[16:28:38.030]  [00:00:17.658][info  ][DL]  stop soft timer
[16:28:38.031]  [00:00:17.658][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.033]  [00:00:17.661][info  ][DL] Char Write Req, char : 47
[16:28:38.033]  [00:00:17.661][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:28:38.035]  [00:00:17.662][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.093]  [00:00:17.720][info  ][DL] Char Write Req, char : 47
[16:28:38.093]  [00:00:17.720][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:28:38.094]  [00:00:17.721][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.152]  [00:00:17.779][info  ][DL] Char Write Req, char : 47
[16:28:38.152]  [00:00:17.779][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 150)
[16:28:38.153]  [00:00:17.780][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.154]  [00:00:17.782][info  ][EM] >>> [E:5473r S:15300 M:267692778] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:629)
[16:28:38.156]  [00:00:17.782][detail][EM] Handling via exchange: 5473r, Delegate: 0x2000413c
[16:28:38.157]  [00:00:17.783][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0006
[16:28:38.158]  [00:00:17.784][info  ][ZCL] OpCreds: Received an AddNOC command
[16:28:38.159]  [00:00:17.786][info  ][FP] Validating NOC chain
[16:28:38.186]  [00:00:17.814][info  ][FP] NOC chain validation successful
[16:28:38.186]  [00:00:17.814][info  ][FP] Added new fabric at index: 0x1
[16:28:38.187]  [00:00:17.814][info  ][FP] Assigned compressed fabric ID: 0xFDA99EDEC35D5933, node ID: 0x0724338E7B78E61C
[16:28:38.189]  [00:00:17.815][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[16:28:38.189]  [00:00:17.815][info  ][TS] New proposed Last Known Good Time: 2026-02-07T08:28:37
[16:28:38.190]  [00:00:17.815][info  ][TS] Updating pending Last Known Good Time to 2026-02-07T08:28:37
[16:28:38.220]  [00:00:17.847][detail][EVL] LogEvent event number: 0x0000000000000002 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6ACFF175
[16:28:38.222]  [00:00:17.848][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0xFFFFFFFD00000001
[16:28:38.223]  
[16:28:38.223]  [00:00:17.848][detail][DL] Using Thread extended MAC for hostname.
[16:28:38.224]  [00:00:17.848][info  ][DIS] Advertise operational node FDA99EDEC35D5933-0724338E7B78E61C
[16:28:38.225]  [00:00:17.848][error ][SVR] Operational advertising failed: 3
[16:28:38.226]  [00:00:17.848][detail][DMG] Command handler moving to [NewRespons]
[16:28:38.226]  [00:00:17.849][detail][DMG] Command handler moving to [ Preparing]
[16:28:38.227]  [00:00:17.849][detail][DMG] Command handler moving to [AddingComm]
[16:28:38.228]  [00:00:17.849][detail][DMG] Command handler moving to [AddedComma]
[16:28:38.229]  [00:00:17.849][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[16:28:38.229]  [00:00:17.849][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:38.231]  [00:00:17.850][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:38.231]  [00:00:17.852][info  ][EM] <<< [E:5473r S:15300 M:41349859] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:28:38.234]  [00:00:17.852][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:38.270]  [00:00:17.898][info  ][DL] Tx Confirmation received
[16:28:38.270]  [00:00:17.898][info  ][DL]  stop soft timer
[16:28:38.271]  [00:00:17.898][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.271]  [00:00:17.899][info  ][DL] Char Write Req, char : 47
[16:28:38.272]  [00:00:17.899][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.274]  [00:00:17.900][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.274]  [00:00:17.902][info  ][EM] >>> [E:5474r S:15300 M:267692779] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.276]  [00:00:17.902][detail][EM] Handling via exchange: 5474r, Delegate: 0x2000413c
[16:28:38.277]  [00:00:17.902][detail][IM] Received Read request
[16:28:38.277]  [00:00:17.903][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.278]  [00:00:17.903][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.280]  [00:00:17.904][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.281]  [00:00:17.905][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.282]  [00:00:17.906][detail][DMG] <RE> Sending report (payload has 60 bytes)...
[16:28:38.283]  [00:00:17.908][info  ][EM] <<< [E:5474r S:15300 M:41349860] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:90)
[16:28:38.284]  [00:00:17.909][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.285]  [00:00:17.909][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.286]  [00:00:17.909][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.287]  [00:00:17.909][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.330]  [00:00:17.958][info  ][DL] Tx Confirmation received
[16:28:38.330]  [00:00:17.958][info  ][DL]  stop soft timer
[16:28:38.331]  [00:00:17.958][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.332]  [00:00:17.959][info  ][DL] Char Write Req, char : 47
[16:28:38.332]  [00:00:17.959][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.334]  [00:00:17.959][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.334]  [00:00:17.961][info  ][EM] >>> [E:5475r S:15300 M:267692780] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.336]  [00:00:17.961][detail][EM] Handling via exchange: 5475r, Delegate: 0x2000413c
[16:28:38.337]  [00:00:17.962][detail][IM] Received Read request
[16:28:38.338]  [00:00:17.963][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.338]  [00:00:17.963][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.340]  [00:00:17.964][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:38.341]  [00:00:17.964][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:28:38.342]  [00:00:17.965][detail][DMG] <RE> Sending report (payload has 46 bytes)...
[16:28:38.343]  [00:00:17.968][info  ][EM] <<< [E:5475r S:15300 M:41349861] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:76)
[16:28:38.345]  [00:00:17.968][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.345]  [00:00:17.969][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.346]  [00:00:17.969][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.347]  [00:00:17.969][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.390]  [00:00:18.017][info  ][DL] Tx Confirmation received
[16:28:38.390]  [00:00:18.018][info  ][DL]  stop soft timer
[16:28:38.391]  [00:00:18.018][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.392]  [00:00:18.019][info  ][DL] Char Write Req, char : 47
[16:28:38.392]  [00:00:18.019][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.394]  [00:00:18.019][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.394]  [00:00:18.022][info  ][EM] >>> [E:5476r S:15300 M:267692781] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.396]  [00:00:18.022][detail][EM] Handling via exchange: 5476r, Delegate: 0x2000413c
[16:28:38.397]  [00:00:18.022][detail][IM] Received Read request
[16:28:38.398]  [00:00:18.023][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.398]  [00:00:18.023][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.400]  [00:00:18.024][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.401]  [00:00:18.024][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.402]  [00:00:18.025][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.403]  [00:00:18.027][info  ][EM] <<< [E:5476r S:15300 M:41349862] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.405]  [00:00:18.028][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.405]  [00:00:18.028][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.406]  [00:00:18.028][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.407]  [00:00:18.028][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.450]  [00:00:18.078][info  ][DL] Tx Confirmation received
[16:28:38.450]  [00:00:18.078][info  ][DL]  stop soft timer
[16:28:38.451]  [00:00:18.078][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.452]  [00:00:18.079][info  ][DL] Char Write Req, char : 47
[16:28:38.452]  [00:00:18.080][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.454]  [00:00:18.080][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.454]  [00:00:18.082][info  ][EM] >>> [E:5477r S:15300 M:267692782] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.456]  [00:00:18.082][detail][EM] Handling via exchange: 5477r, Delegate: 0x2000413c
[16:28:38.457]  [00:00:18.082][detail][IM] Received Read request
[16:28:38.457]  [00:00:18.083][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.458]  [00:00:18.083][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.460]  [00:00:18.083][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.461]  [00:00:18.084][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.462]  [00:00:18.084][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.463]  [00:00:18.086][info  ][EM] <<< [E:5477r S:15300 M:41349863] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.464]  [00:00:18.087][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.465]  [00:00:18.087][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.466]  [00:00:18.087][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.467]  [00:00:18.087][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.510]  [00:00:18.137][info  ][DL] Tx Confirmation received
[16:28:38.510]  [00:00:18.137][info  ][DL]  stop soft timer
[16:28:38.511]  [00:00:18.138][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.512]  [00:00:18.139][info  ][DL] Char Write Req, char : 47
[16:28:38.512]  [00:00:18.139][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.513]  [00:00:18.139][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.514]  [00:00:18.141][info  ][EM] >>> [E:5478r S:15300 M:267692783] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.516]  [00:00:18.142][detail][EM] Handling via exchange: 5478r, Delegate: 0x2000413c
[16:28:38.517]  [00:00:18.142][detail][IM] Received Read request
[16:28:38.518]  [00:00:18.143][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.518]  [00:00:18.143][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.520]  [00:00:18.144][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.520]  [00:00:18.144][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.522]  [00:00:18.146][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.522]  [00:00:18.148][info  ][EM] <<< [E:5478r S:15300 M:41349864] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.524]  [00:00:18.149][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.525]  [00:00:18.149][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.526]  [00:00:18.149][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.527]  [00:00:18.149][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.570]  [00:00:18.198][info  ][DL] Tx Confirmation received
[16:28:38.570]  [00:00:18.198][info  ][DL]  stop soft timer
[16:28:38.571]  [00:00:18.198][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.571]  [00:00:18.199][info  ][DL] Char Write Req, char : 47
[16:28:38.572]  [00:00:18.199][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.573]  [00:00:18.200][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.574]  [00:00:18.202][info  ][EM] >>> [E:5479r S:15300 M:267692784] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.575]  [00:00:18.202][detail][EM] Handling via exchange: 5479r, Delegate: 0x2000413c
[16:28:38.577]  [00:00:18.202][detail][IM] Received Read request
[16:28:38.577]  [00:00:18.203][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.578]  [00:00:18.203][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.580]  [00:00:18.204][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.580]  [00:00:18.204][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.582]  [00:00:18.205][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.583]  [00:00:18.207][info  ][EM] <<< [E:5479r S:15300 M:41349865] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.584]  [00:00:18.208][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.584]  [00:00:18.208][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.586]  [00:00:18.208][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.587]  [00:00:18.208][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.630]  [00:00:18.257][info  ][DL] Tx Confirmation received
[16:28:38.630]  [00:00:18.257][info  ][DL]  stop soft timer
[16:28:38.631]  [00:00:18.258][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.632]  [00:00:18.259][info  ][DL] Char Write Req, char : 47
[16:28:38.632]  [00:00:18.259][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.633]  [00:00:18.259][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.634]  [00:00:18.261][info  ][EM] >>> [E:5480r S:15300 M:267692785] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.636]  [00:00:18.262][detail][EM] Handling via exchange: 5480r, Delegate: 0x2000413c
[16:28:38.637]  [00:00:18.262][detail][IM] Received Read request
[16:28:38.637]  [00:00:18.263][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.638]  [00:00:18.263][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.640]  [00:00:18.264][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.640]  [00:00:18.264][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.642]  [00:00:18.265][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.642]  [00:00:18.267][info  ][EM] <<< [E:5480r S:15300 M:41349866] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.644]  [00:00:18.267][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.645]  [00:00:18.267][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.646]  [00:00:18.268][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.646]  [00:00:18.268][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.649]  
[16:28:38.690]  [00:00:18.318][info  ][DL] Tx Confirmation received
[16:28:38.690]  [00:00:18.318][info  ][DL]  stop soft timer
[16:28:38.691]  [00:00:18.318][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.691]  [00:00:18.319][info  ][DL] Char Write Req, char : 47
[16:28:38.692]  [00:00:18.319][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.693]  [00:00:18.320][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.694]  [00:00:18.322][info  ][EM] >>> [E:5481r S:15300 M:267692786] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.695]  [00:00:18.322][detail][EM] Handling via exchange: 5481r, Delegate: 0x2000413c
[16:28:38.697]  [00:00:18.322][detail][IM] Received Read request
[16:28:38.697]  [00:00:18.323][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.698]  [00:00:18.323][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.700]  [00:00:18.324][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:38.700]  [00:00:18.325][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:28:38.702]  [00:00:18.326][detail][DMG] <RE> Sending report (payload has 46 bytes)...
[16:28:38.702]  [00:00:18.328][info  ][EM] <<< [E:5481r S:15300 M:41349867] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:76)
[16:28:38.704]  [00:00:18.329][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.704]  [00:00:18.329][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.706]  [00:00:18.329][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.707]  [00:00:18.329][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.750]  [00:00:18.377][info  ][DL] Tx Confirmation received
[16:28:38.750]  [00:00:18.377][info  ][DL]  stop soft timer
[16:28:38.751]  [00:00:18.378][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.752]  [00:00:18.379][info  ][DL] Char Write Req, char : 47
[16:28:38.752]  [00:00:18.379][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.754]  [00:00:18.379][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.754]  [00:00:18.381][info  ][EM] >>> [E:5482r S:15300 M:267692787] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.757]  [00:00:18.382][detail][EM] Handling via exchange: 5482r, Delegate: 0x2000413c
[16:28:38.757]  [00:00:18.382][detail][IM] Received Read request
[16:28:38.758]  [00:00:18.383][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.759]  [00:00:18.383][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.759]  [00:00:18.383][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.760]  [00:00:18.384][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.762]  [00:00:18.384][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.762]  [00:00:18.387][info  ][EM] <<< [E:5482r S:15300 M:41349868] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.765]  [00:00:18.387][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.766]  [00:00:18.387][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.766]  [00:00:18.388][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.766]  [00:00:18.388][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.810]  [00:00:18.438][info  ][DL] Tx Confirmation received
[16:28:38.810]  [00:00:18.438][info  ][DL]  stop soft timer
[16:28:38.811]  [00:00:18.438][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.811]  [00:00:18.439][info  ][DL] Char Write Req, char : 47
[16:28:38.812]  [00:00:18.439][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.813]  [00:00:18.440][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.814]  [00:00:18.442][info  ][EM] >>> [E:5483r S:15300 M:267692788] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.815]  [00:00:18.442][detail][EM] Handling via exchange: 5483r, Delegate: 0x2000413c
[16:28:38.817]  [00:00:18.442][detail][IM] Received Read request
[16:28:38.817]  [00:00:18.443][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.818]  [00:00:18.443][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.820]  [00:00:18.444][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.820]  [00:00:18.444][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.822]  [00:00:18.445][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.822]  [00:00:18.447][info  ][EM] <<< [E:5483r S:15300 M:41349869] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.824]  [00:00:18.448][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.824]  [00:00:18.448][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.826]  [00:00:18.448][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.826]  [00:00:18.448][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.870]  [00:00:18.498][info  ][DL] Tx Confirmation received
[16:28:38.870]  [00:00:18.498][info  ][DL]  stop soft timer
[16:28:38.871]  [00:00:18.498][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.871]  [00:00:18.499][info  ][DL] Char Write Req, char : 47
[16:28:38.872]  [00:00:18.500][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.873]  [00:00:18.500][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.874]  [00:00:18.501][info  ][EM] >>> [E:5484r S:15300 M:267692789] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.875]  [00:00:18.501][detail][EM] Handling via exchange: 5484r, Delegate: 0x2000413c
[16:28:38.877]  [00:00:18.502][detail][IM] Received Read request
[16:28:38.877]  [00:00:18.502][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.878]  [00:00:18.503][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.880]  [00:00:18.503][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.880]  [00:00:18.504][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.882]  [00:00:18.504][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.882]  [00:00:18.506][info  ][EM] <<< [E:5484r S:15300 M:41349870] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.884]  [00:00:18.507][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.884]  [00:00:18.507][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.886]  [00:00:18.507][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.887]  [00:00:18.508][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.930]  [00:00:18.557][info  ][DL] Tx Confirmation received
[16:28:38.930]  [00:00:18.558][info  ][DL]  stop soft timer
[16:28:38.930]  [00:00:18.558][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.931]  [00:00:18.559][info  ][DL] Char Write Req, char : 47
[16:28:38.932]  [00:00:18.559][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.933]  [00:00:18.559][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.934]  [00:00:18.562][info  ][EM] >>> [E:5485r S:15300 M:267692790] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.935]  [00:00:18.562][detail][EM] Handling via exchange: 5485r, Delegate: 0x2000413c
[16:28:38.937]  [00:00:18.562][detail][IM] Received Read request
[16:28:38.937]  [00:00:18.564][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.937]  [00:00:18.564][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.940]  [00:00:18.565][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:38.940]  [00:00:18.566][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0000 (expanded=0)
[16:28:38.942]  [00:00:18.566][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:38.942]  [00:00:18.568][info  ][EM] <<< [E:5485r S:15300 M:41349871] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:38.944]  [00:00:18.569][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:38.944]  [00:00:18.569][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:38.946]  [00:00:18.569][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:38.947]  [00:00:18.570][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:38.990]  [00:00:18.618][info  ][DL] Tx Confirmation received
[16:28:38.990]  [00:00:18.618][info  ][DL]  stop soft timer
[16:28:38.990]  [00:00:18.618][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:38.991]  [00:00:18.619][info  ][DL] Char Write Req, char : 47
[16:28:38.992]  [00:00:18.619][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:38.993]  [00:00:18.620][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:38.994]  [00:00:18.622][info  ][EM] >>> [E:5486r S:15300 M:267692791] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:38.995]  [00:00:18.622][detail][EM] Handling via exchange: 5486r, Delegate: 0x2000413c
[16:28:38.997]  [00:00:18.623][detail][IM] Received Read request
[16:28:38.997]  [00:00:18.623][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:38.997]  [00:00:18.624][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:38.999]  [00:00:18.624][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:39.000]  [00:00:18.624][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0000 (expanded=0)
[16:28:39.001]  [00:00:18.625][detail][DMG] <RE> Sending report (payload has 45 bytes)...
[16:28:39.002]  [00:00:18.626][info  ][EM] <<< [E:5486r S:15300 M:41349872] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:39.004]  [00:00:18.627][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:39.004]  [00:00:18.627][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:39.006]  [00:00:18.627][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:39.006]  [00:00:18.627][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:39.050]  [00:00:18.677][info  ][DL] Tx Confirmation received
[16:28:39.050]  [00:00:18.677][info  ][DL]  stop soft timer
[16:28:39.051]  [00:00:18.678][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:39.052]  [00:00:18.679][info  ][DL] Char Write Req, char : 47
[16:28:39.052]  [00:00:18.679][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 57)
[16:28:39.053]  [00:00:18.679][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:39.054]  [00:00:18.681][info  ][EM] >>> [E:5487r S:15300 M:267692792] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:52)
[16:28:39.056]  [00:00:18.682][detail][EM] Handling via exchange: 5487r, Delegate: 0x2000413c
[16:28:39.057]  [00:00:18.682][detail][IM] Received Read request
[16:28:39.057]  [00:00:18.683][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:39.058]  [00:00:18.683][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:39.059]  [00:00:18.684][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[16:28:39.060]  [00:00:18.685][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=0)
[16:28:39.061]  [00:00:18.686][detail][DMG] <RE> Sending report (payload has 37 bytes)...
[16:28:39.062]  [00:00:18.688][info  ][EM] <<< [E:5487r S:15300 M:41349873] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[16:28:39.064]  [00:00:18.689][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:39.065]  [00:00:18.689][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:39.066]  [00:00:18.689][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:39.066]  [00:00:18.689][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:39.110]  [00:00:18.738][info  ][DL] Tx Confirmation received
[16:28:39.110]  [00:00:18.738][info  ][DL]  stop soft timer
[16:28:39.111]  [00:00:18.738][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.639]  
[16:28:40.670]  [00:00:20.298][info  ][DL] Char Write Req, char : 47
[16:28:40.670]  [00:00:20.298][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 44)
[16:28:40.672]  [00:00:20.298][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.672]  [00:00:20.300][info  ][EM] >>> [E:5488r S:15300 M:267692793] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[16:28:40.675]  [00:00:20.300][detail][EM] Handling via exchange: 5488r, Delegate: 0x2000413c
[16:28:40.675]  [00:00:20.301][detail][DMG] Got Timed Request with timeout 10000: handler 0x200046b8 exchange 5488r
[16:28:40.676]  [00:00:20.302][info  ][EM] <<< [E:5488r S:15300 M:41349874] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[16:28:40.678]  [00:00:20.303][detail][DMG] Timed Request time limit 0x000000000000765F: handler 0x200046b8 exchange 5488r
[16:28:40.730]  [00:00:20.358][info  ][DL] Tx Confirmation received
[16:28:40.730]  [00:00:20.358][info  ][DL]  stop soft timer
[16:28:40.730]  [00:00:20.358][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.731]  [00:00:20.359][info  ][DL] Char Write Req, char : 47
[16:28:40.732]  [00:00:20.359][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 71)
[16:28:40.733]  [00:00:20.360][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.734]  [00:00:20.362][info  ][EM] >>> [E:5488r S:15300 M:267692794] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:66)
[16:28:40.735]  [00:00:20.362][detail][EM] Found matching exchange: 5488r, Delegate: 0x200046b8
[16:28:40.737]  [00:00:20.362][detail][DMG] Timed following action arrived at 0x0000000000004F8A: handler 0x200046b8 exchange 5488r
[16:28:40.738]  [00:00:20.363][detail][DMG] Handing timed invoke to IM engine: handler 0x200046b8 exchange 5488r
[16:28:40.739]  [00:00:20.364][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:28:40.740]  [00:00:20.364][info  ][FS] GeneralCommissioning: Received ArmFailSafe (270s)
[16:28:40.741]  [00:00:20.364][detail][DMG] Command handler moving to [NewRespons]
[16:28:40.741]  [00:00:20.364][detail][DMG] Command handler moving to [ Preparing]
[16:28:40.742]  [00:00:20.365][detail][DMG] Command handler moving to [AddingComm]
[16:28:40.743]  [00:00:20.365][detail][DMG] Command handler moving to [AddedComma]
[16:28:40.744]  [00:00:20.365][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:40.745]  [00:00:20.365][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:40.746]  [00:00:20.365][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:40.746]  [00:00:20.367][info  ][EM] <<< [E:5488r S:15300 M:41349875] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:28:40.748]  [00:00:20.368][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:40.790]  [00:00:20.417][info  ][DL] Tx Confirmation received
[16:28:40.790]  [00:00:20.417][info  ][DL]  stop soft timer
[16:28:40.791]  [00:00:20.417][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.792]  [00:00:20.419][info  ][DL] Char Write Req, char : 47
[16:28:40.792]  [00:00:20.419][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:40.793]  [00:00:20.419][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.794]  [00:00:20.421][info  ][EM] >>> [E:5489r S:15300 M:267692795] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:40.796]  [00:00:20.422][detail][EM] Handling via exchange: 5489r, Delegate: 0x2000413c
[16:28:40.797]  [00:00:20.422][detail][IM] Received Read request
[16:28:40.797]  [00:00:20.423][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:40.798]  [00:00:20.423][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:40.799]  [00:00:20.424][detail][DMG] <RE:Run> Cluster 31, Attribute 1 is dirty
[16:28:40.800]  [00:00:20.424][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:28:40.801]  [00:00:20.426][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:40.802]  [00:00:20.428][info  ][EM] <<< [E:5489r S:15300 M:41349876] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:40.804]  [00:00:20.428][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:40.805]  [00:00:20.429][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:40.806]  [00:00:20.429][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:40.806]  [00:00:20.429][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:40.850]  [00:00:20.478][info  ][DL] Tx Confirmation received
[16:28:40.850]  [00:00:20.478][info  ][DL]  stop soft timer
[16:28:40.850]  [00:00:20.478][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.851]  [00:00:20.479][info  ][DL] Char Write Req, char : 47
[16:28:40.852]  [00:00:20.479][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 44)
[16:28:40.853]  [00:00:20.479][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.854]  [00:00:20.481][info  ][EM] >>> [E:5490r S:15300 M:267692796] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[16:28:40.855]  [00:00:20.481][detail][EM] Handling via exchange: 5490r, Delegate: 0x2000413c
[16:28:40.857]  [00:00:20.482][detail][DMG] Got Timed Request with timeout 10000: handler 0x200046b8 exchange 5490r
[16:28:40.858]  [00:00:20.483][info  ][EM] <<< [E:5490r S:15300 M:41349877] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[16:28:40.859]  [00:00:20.484][detail][DMG] Timed Request time limit 0x0000000000007714: handler 0x200046b8 exchange 5490r
[16:28:40.909]  [00:00:20.538][info  ][DL] Tx Confirmation received
[16:28:40.910]  [00:00:20.538][info  ][DL]  stop soft timer
[16:28:40.910]  [00:00:20.538][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.911]  [00:00:20.540][info  ][DL] Char Write Req, char : 47
[16:28:40.912]  [00:00:20.540][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 107)
[16:28:40.913]  [00:00:20.540][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.914]  [00:00:20.542][info  ][EM] >>> [E:5490r S:15300 M:267692797] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:102)
[16:28:40.915]  [00:00:20.542][detail][EM] Found matching exchange: 5490r, Delegate: 0x200046b8
[16:28:40.917]  [00:00:20.542][detail][DMG] Timed following action arrived at 0x000000000000503E: handler 0x200046b8 exchange 5490r
[16:28:40.918]  [00:00:20.542][detail][DMG] Handing timed invoke to IM engine: handler 0x200046b8 exchange 5490r
[16:28:40.919]  [00:00:20.543][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0003
[16:28:40.920]  [00:00:20.545][detail][DMG] Command handler moving to [NewRespons]
[16:28:40.921]  [00:00:20.545][detail][DMG] Command handler moving to [ Preparing]
[16:28:40.922]  [00:00:20.545][detail][DMG] Command handler moving to [AddingComm]
[16:28:40.922]  [00:00:20.545][detail][DMG] Command handler moving to [AddedComma]
[16:28:40.923]  [00:00:20.546][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:40.924]  [00:00:20.546][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:40.925]  [00:00:20.546][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:40.926]  [00:00:20.548][info  ][EM] <<< [E:5490r S:15300 M:41349878] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:28:40.928]  [00:00:20.549][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:40.970]  [00:00:20.597][info  ][DL] Tx Confirmation received
[16:28:40.970]  [00:00:20.598][info  ][DL]  stop soft timer
[16:28:40.970]  [00:00:20.598][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:40.971]  [00:00:20.599][info  ][DL] Char Write Req, char : 47
[16:28:40.972]  [00:00:20.599][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:28:40.973]  [00:00:20.599][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:40.974]  [00:00:20.601][info  ][EM] >>> [E:5491r S:15300 M:267692798] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:40.975]  [00:00:20.602][detail][EM] Handling via exchange: 5491r, Delegate: 0x2000413c
[16:28:40.977]  [00:00:20.602][detail][IM] Received Read request
[16:28:40.977]  [00:00:20.603][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:40.977]  [00:00:20.603][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:40.979]  [00:00:20.604][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[16:28:40.980]  [00:00:20.605][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:28:40.981]  [00:00:20.606][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:40.982]  [00:00:20.608][info  ][EM] <<< [E:5491r S:15300 M:41349879] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[16:28:40.983]  [00:00:20.609][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:40.984]  [00:00:20.609][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:28:40.986]  [00:00:20.609][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:40.986]  [00:00:20.609][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:41.030]  [00:00:20.658][info  ][DL] Tx Confirmation received
[16:28:41.030]  [00:00:20.658][info  ][DL]  stop soft timer
[16:28:41.030]  [00:00:20.658][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:41.031]  [00:00:20.659][info  ][DL] Char Write Req, char : 47
[16:28:41.032]  [00:00:20.660][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 44)
[16:28:41.033]  [00:00:20.660][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:41.034]  [00:00:20.663][info  ][EM] >>> [E:5492r S:15300 M:267692799] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[16:28:41.036]  [00:00:20.663][detail][EM] Handling via exchange: 5492r, Delegate: 0x2000413c
[16:28:41.037]  [00:00:20.663][detail][DMG] Got Timed Request with timeout 32000: handler 0x200046b8 exchange 5492r
[16:28:41.038]  [00:00:20.665][info  ][EM] <<< [E:5492r S:15300 M:41349880] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[16:28:41.040]  [00:00:20.666][detail][DMG] Timed Request time limit 0x000000000000CDBA: handler 0x200046b8 exchange 5492r
[16:28:41.089]  [00:00:20.717][info  ][DL] Tx Confirmation received
[16:28:41.090]  [00:00:20.717][info  ][DL]  stop soft timer
[16:28:41.090]  [00:00:20.718][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:41.091]  [00:00:20.719][info  ][DL] Char Write Req, char : 47
[16:28:41.092]  [00:00:20.719][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 78)
[16:28:41.093]  [00:00:20.719][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:41.094]  [00:00:20.721][info  ][EM] >>> [E:5492r S:15300 M:267692800] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[16:28:41.095]  [00:00:20.722][detail][EM] Found matching exchange: 5492r, Delegate: 0x200046b8
[16:28:41.096]  [00:00:20.722][detail][DMG] Timed following action arrived at 0x00000000000050F2: handler 0x200046b8 exchange 5492r
[16:28:41.098]  [00:00:20.722][detail][DMG] Handing timed invoke to IM engine: handler 0x200046b8 exchange 5492r
[16:28:41.099]  [00:00:20.723][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0006
[16:28:41.100]  [00:00:20.724][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 3
[16:28:41.105]  [00:00:20.733][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 2
[16:28:41.106]  [00:00:20.733][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:41.106]  [00:00:20.733][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[16:28:41.108]  [00:00:20.734][silabs ]NWK: platform event type 8004
[16:28:41.108]  [00:00:20.734][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:28:41.109]  [00:00:20.735][detail][DL] OpenThread State Changed (Flags: 0x1106d10d)
[16:28:41.110]  [00:00:20.735][detail][DL]    Device Role: DETACHED
[16:28:41.111]  [00:00:20.735][detail][DL]    Network Name: OpenThread
[16:28:41.111]  [00:00:20.735][detail][DL]    PAN Id: 0x632B
[16:28:41.111]  [00:00:20.735][detail][DL]    Extended PAN Id: 0x666E661B5E36F960
[16:28:41.112]  [00:00:20.735][detail][DL]    Channel: 11
[16:28:41.113]  [00:00:20.736][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64
[16:28:41.113]  [00:00:20.736][detail][DL]    Thread Unicast Addresses:
[16:28:41.114]  [00:00:20.736][detail][DL]         fdde:ad00:beef:0:172b:8e9b:c4b0:8776/64 valid preferred
[16:28:41.115]  [00:00:20.737][detail][DL]         fe80:0:0:0:80a6:8c:1113:e2f6/64 valid preferred
[16:28:41.947]  [00:00:21.575][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:28:41.948]  [00:00:21.576][detail][DL] OpenThread State Changed (Flags: 0x00000100)
[16:28:41.948]  [00:00:21.576][silabs ]NWK: platform event type 800b
[16:28:42.877]  [00:00:22.504][info  ][DL] SRP Client was started, detected server: fd6e:d157:02b4:cdbf:9518:944f:837d:f011
[16:28:42.878]  [00:00:22.505][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:28:42.878]  [00:00:22.505][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[16:28:42.880]  [00:00:22.505][detail][EVL] LogEvent event number: 0x0000000000000003 priority: 1, endpoint id:  0x0 cluster id: 0x0000_0035 event id: 0x0 Epoch timestamp: 0x000000DC6AD003A7  
[16:28:42.882]  [00:00:22.505][detail][DL] OpenThread State Changed (Flags: 0x301132b7)  
[16:28:42.883]  [00:00:22.506][detail][DL]    Device Role: CHILD
[16:28:42.883]  [00:00:22.506][detail][DL]    Network Name: ST-1JNY
[16:28:42.884]  [00:00:22.506][detail][DL]    PAN Id: 0x632B  
[16:28:42.885]  [00:00:22.506][detail][DL]    Extended PAN Id: 0x666E661B5E36F960 
[16:28:42.885]  [00:00:22.506][detail][DL]    Channel: 11
[16:28:42.886]  [00:00:22.507][detail][DL]    Mesh Prefix: fd6e:d157:2b4:cdbf:0:0:0:0/64
[16:28:42.887]  [00:00:22.507][detail][DL]    Partition Id: 0x5F44B68F
[16:28:42.888]  [00:00:22.507][detail][DL]    Thread Unicast Addresses:
[16:28:42.888]  [00:00:22.507][detail][DL]         fddc:8360:97e9:1:d259:da37:4937:b266/64 valid preferred
[16:28:42.889]  
[16:28:42.889]  [00:00:22.509][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[16:28:42.890]  
[16:28:42.890]  [00:00:22.510][info  ][SVR] Joining Multicast groups
[16:28:42.891]  [00:00:22.511][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:42.892]  
[16:28:42.892]  [00:00:22.512][detail][DMG] Command handler moving to [NewRespons]
[16:28:42.892]  
[16:28:42.893]  [00:00:22.512][detail][DMG] Command handler moving to [AddedComma]
[16:28:42.894]  [00:00:22.514][info  ][EM] <<< [E:5492r S:15300 M:41349881] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[16:28:42.896]  [00:00:22.515][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:42.896]  [00:00:22.516][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[16:28:42.897]  [00:00:22.516][detail][DL] Using Thread extended MAC for hostname.
[16:28:42.898]  [00:00:22.516][info  ][DIS] Advertise operational node FDA99EDEC35D5933-0724338E7B78E61C
[16:28:42.899]  [00:00:22.517][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:28:42.900]  [00:00:22.518][detail][DL]         fddc:8360:97e9:1:d259:da37:4937:b266/64 valid preferred
[16:28:42.901]  [00:00:22.519][detail][DL]         fd6e:d157:2b4:cdbf:0:ff:fe00:c005/64 valid preferred rloc
[16:28:42.903]  
[16:28:42.921]  [00:00:22.549][info  ][DL] Tx Confirmation received
[16:28:42.921]  [00:00:22.549][info  ][DL]  stop soft timer
[16:28:42.922]  [00:00:22.549][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:43.630]  [00:00:23.257][detail][DL] SRP update succeeded
[16:28:43.630]  [00:00:23.257][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[16:28:43.630]  [00:00:23.257][silabs ]NWK: platform event type 8012
[16:28:43.631]  [00:00:23.257][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[16:28:43.633]  [00:00:23.257][info  ][SVR] Server initialization complete
[16:28:43.633]  [00:00:23.258][info  ][DIS] Updating services using commissioning mode 0
[16:28:43.634]  [00:00:23.258][detail][DL] Using Thread extended MAC for hostname.
[16:28:43.635]  [00:00:23.258][info  ][DIS] Advertise operational node FDA99EDEC35D5933-0724338E7B78E61C
[16:28:43.635]  [00:00:23.259][info  ][DL] advertising srp service: FDA99EDEC35D5933-0724338E7B78E61C._matter._tcp
[16:28:43.637]  [00:00:23.259][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[16:28:43.637]  [00:00:23.259][silabs ]NWK: platform event type 8016
[16:28:43.644]  [00:00:23.271][info  ][IM] No subscriptions to resume
[16:28:44.639]  
[16:28:45.121]  [00:00:24.749][detail][DL] SRP update succeeded
[16:28:45.440]  [00:00:25.068][info  ][DL] Char Write Req, char : 47
[16:28:45.440]  [00:00:25.068][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 3)
[16:28:45.441]  [00:00:25.068][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:28:46.413]  [00:00:26.041][detail][IN] UDP Message Received packet nb : 1 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 196
[16:28:46.414]  [00:00:26.041][info  ][EM] >>> [E:1161r S:0 M:29120953] (U) Msg RX from 0:4B2C0FC6ADE5C4BF [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:28:46.416]  [00:00:26.041][detail][EM] Handling via exchange: 1161r, Delegate: 0x20007de8
[16:28:46.417]  [00:00:26.041][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200089b0
[16:28:46.418]  [00:00:26.041][info  ][EM] <<< [E:1161r S:0 M:18459225 (Ack:29120953)] (U) Msg TX from 0000000000000000 to 0:4B2C0FC6ADE5C4BF [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:28:46.421]  [00:00:26.042][detail][EM] Flushed pending ack for MessageCounter:29120953 on exchange 1161r
[16:28:46.422]  [00:00:26.042][info  ][SC] Received Sigma1 msg
[16:28:46.422]  [00:00:26.043][detail][SC] Found MRP parameters in the message
[16:28:46.423]  [00:00:26.043][detail][SC] Peer (Initiator) assigned session ID 19378
[16:28:46.424]  [00:00:26.052][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x0724338E7B78E61C
[16:28:46.446]  [00:00:26.074][detail][CR] AES_CCM_encrypt: Using aad == null path
[16:28:46.448]  [00:00:26.077][info  ][EM] <<< [E:1161r S:0 M:18459226 (Ack:29120953)] (U) Msg TX from 0000000000000000 to 0:4B2C0FC6ADE5C4BF [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:809)
[16:28:46.451]  [00:00:26.078][info  ][EM] ??1 [E:1161r S:0 M:18459226] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3398ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:46.453]  [00:00:26.078][info  ][SC] Sent Sigma2 msg
[16:28:46.631]  [00:00:26.258][info  ][SWU] Stopping the watchdog timer
[16:28:46.631]  [00:00:26.259][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:28:46.632]  [00:00:26.259][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 6e146848
[16:28:46.633]  [00:00:26.259][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 6e146849
[16:28:46.638]  
[16:28:47.438]  [00:00:27.066][detail][IN] UDP Message Received packet nb : 2 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 657
[16:28:47.440]  [00:00:27.066][info  ][EM] >>> [E:1161r S:0 M:29120954 (Ack:18459226)] (U) Msg RX from 0:4B2C0FC6ADE5C4BF [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:657)
[16:28:47.442]  [00:00:27.067][detail][EM] Found matching exchange: 1161r, Delegate: 0x20007e04
[16:28:47.443]  [00:00:27.067][detail][EM] Rxd Ack; Removing MessageCounter:18459226 from Retrans Table on exchange 1161r
[16:28:47.444]  [00:00:27.068][info  ][EM] <<< [E:1161r S:0 M:18459227 (Ack:29120954)] (U) Msg TX from 0000000000000000 to 0:4B2C0FC6ADE5C4BF [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:28:47.447]  [00:00:27.068][detail][EM] Flushed pending ack for MessageCounter:29120954 on exchange 1161r
[16:28:47.448]  [00:00:27.068][info  ][SC] Received Sigma3 msg
[16:28:47.448]  [00:00:27.072][detail][CR] AES_CCM_decrypt: Using aad == null path
[16:28:47.449]  [00:00:27.077][detail][SC] Certificate's mNotBeforeTime (796984461) is after current time (27)
[16:28:47.450]  [00:00:27.077][detail][SC] Certificate's mNotBeforeTime (796841559) is after current time (27)
[16:28:47.451]  [00:00:27.077][detail][SC] Certificate's mNotBeforeTime (780009733) is after current time (27)
[16:28:47.491]  [00:00:27.119][detail][SC] Sending status report. Protocol code 0, exchange 1161
[16:28:47.492]  [00:00:27.119][info  ][EM] <<< [E:1161r S:0 M:18459228 (Ack:29120954)] (U) Msg TX from 0000000000000000 to 0:4B2C0FC6ADE5C4BF [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:28:47.494]  [00:00:27.120][info  ][EM] ??1 [E:1161r S:0 M:18459228] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3353ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:47.496]  [00:00:27.124][info  ][SC] SecureSession[0x20006f58, LSID:15299]: State change 'kEstablishing' --> 'kActive'
[16:28:47.497]  [00:00:27.124][detail][IN] SecureSession[0x20006f58]: Activated - Type:2 LSID:15299
[16:28:47.498]  [00:00:27.124][detail][IN] New secure session activated for device <8CBDA24D2F21C48C, 1>, LSID:15299 PSID:19378!
[16:28:47.499]  [00:00:27.125][info  ][IN] CASE Session established to peer: <8CBDA24D2F21C48C, 1>
[16:28:47.500]  [00:00:27.125][detail][IN] SecureSession[0x20007108]: Allocated Type:2 LSID:15301
[16:28:47.501]  [00:00:27.125][detail][SC] Allocated SecureSession (0x20007108) - waiting for Sigma1 msg
[16:28:47.502]  [00:00:27.125][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:28:47.503]  [00:00:27.125][silabs ]NWK: platform event type 8018
[16:28:47.932]  [00:00:27.560][detail][IN] UDP Message Received packet nb : 3 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 26
[16:28:47.934]  [00:00:27.560][info  ][EM] >>> [E:1161r S:0 M:29120955 (Ack:18459228)] (U) Msg RX from 0:4B2C0FC6ADE5C4BF [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:28:47.936]  [00:00:27.561][detail][EM] Found matching exchange: 1161r, Delegate: 0
[16:28:47.937]  [00:00:27.561][detail][EM] Rxd Ack; Removing MessageCounter:18459228 from Retrans Table on exchange 1161r
[16:28:47.955]  [00:00:27.583][detail][IN] UDP Message Received packet nb : 4 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 59
[16:28:47.956]  [00:00:27.584][info  ][EM] >>> [E:1162r S:15299 M:80708135] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:03 (IM:SubscribeRequest) (B:59)
[16:28:47.959]  [00:00:27.584][detail][EM] Handling via exchange: 1162r, Delegate: 0x2000413c
[16:28:47.959]  [00:00:27.585][detail][IM] Received Subscribe request
[16:28:47.960]  [00:00:27.586][info  ][DMG] Final negotiated min/max parameters: Min = 2s, Max = 600s
[16:28:47.961]  [00:00:27.587][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:47.971]  [00:00:27.599][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:47.973]  [00:00:27.600][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:28:47.974]  [00:00:27.600][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:28:47.975]  [00:00:27.602][detail][DMG] <RE> Sending report (payload has 41 bytes)...
[16:28:47.976]  [00:00:27.604][info  ][EM] <<< [E:1162r S:15299 M:137613938 (Ack:80708135)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:75)
[16:28:47.978]  [00:00:27.605][info  ][EM] ??1 [E:1162r S:15299 M:137613938] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3405ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:47.981]  [00:00:27.605][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:28:47.981]  [00:00:27.605][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:28:47.982]  [00:00:27.605][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:47.990]  [00:00:27.618][info  ][DL] Tx Confirmation received
[16:28:47.990]  [00:00:27.619][info  ][DL]  stop soft timer
[16:28:47.991]  [00:00:27.619][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:28:48.458]  [00:00:28.085][detail][IN] UDP Message Received packet nb : 5 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 42
[16:28:48.459]  [00:00:28.086][info  ][EM] >>> [E:1162r S:15299 M:80708136 (Ack:137613938)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:28:48.461]  [00:00:28.087][detail][EM] Found matching exchange: 1162r, Delegate: 0x20005dd0
[16:28:48.463]  [00:00:28.087][detail][EM] Rxd Ack; Removing MessageCounter:137613938 from Retrans Table on exchange 1162r
[16:28:48.463]  [00:00:28.087][info  ][IM] Received status response, status is 0x00
[16:28:48.464]  [00:00:28.090][info  ][EM] <<< [E:1162r S:15299 M:137613939 (Ack:80708136)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:28:48.467]  [00:00:28.090][info  ][EM] ??1 [E:1162r S:15299 M:137613939] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3378ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:48.469]  [00:00:28.091][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000758B and system Timestamp 0x000000000009957B.
[16:28:48.471]  [00:00:28.091][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:48.471]  [00:00:28.091][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:48.639]  
[16:28:48.966]  [00:00:28.593][detail][IN] UDP Message Received packet nb : 6 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:48.967]  [00:00:28.595][info  ][EM] >>> [E:1162r S:15299 M:80708137 (Ack:137613939)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:48.969]  [00:00:28.595][detail][EM] Found matching exchange: 1162r, Delegate: 0
[16:28:48.971]  [00:00:28.595][detail][EM] Rxd Ack; Removing MessageCounter:137613939 from Retrans Table on exchange 1162r
[16:28:48.987]  [00:00:28.614][detail][IN] UDP Message Received packet nb : 7 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 62
[16:28:48.988]  [00:00:28.616][info  ][EM] >>> [E:1163r S:15299 M:80708138] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:28:48.990]  [00:00:28.617][detail][EM] Handling via exchange: 1163r, Delegate: 0x2000413c
[16:28:48.991]  [00:00:28.618][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0004
[16:28:48.992]  [00:00:28.618][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[16:28:48.993]  [00:00:28.620][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:28:49.002]  [00:00:28.630][info  ][TS] Committing Last Known Good Time to storage: 2026-02-07T08:28:37
[16:28:49.004]  [00:00:28.631][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0xFDA99EDEC35D5933, FabricId 670E44471D85389F, NodeId 0724338E7B78E61C, VendorId 0x110A
[16:28:49.006]  [00:00:28.632][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[16:28:49.007]  [00:00:28.632][info  ][FS] Fail-safe cleanly disarmed
[16:28:49.008]  [00:00:28.633][detail][DMG] Command handler moving to [NewRespons]
[16:28:49.008]  [00:00:28.633][detail][DMG] Command handler moving to [ Preparing]
[16:28:49.009]  [00:00:28.633][detail][DMG] Command handler moving to [AddingComm]
[16:28:49.010]  [00:00:28.633][detail][DMG] Command handler moving to [AddedComma]
[16:28:49.010]  [00:00:28.633][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:49.011]  
[16:28:49.012]  [00:00:28.633][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:49.012]  
[16:28:49.012]  [00:00:28.634][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:49.014]  
[16:28:49.014]  [00:00:28.636][info  ][EM] <<< [E:1163r S:15299 M:137613940 (Ack:80708138)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:73)
[16:28:49.017]  
[16:28:49.017]  [00:00:28.637][info  ][EM] ??1 [E:1163r S:15299 M:137613940] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3405ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:49.019]  [00:00:28.638][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:49.019]  [00:00:28.638][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[16:28:49.020]  [00:00:28.638][info  ][SWU] Device commissioned, schedule a default provider query
[16:28:49.021]  [00:00:28.639][info  ][SVR] Commissioning completed successfully
[16:28:49.021]  [00:00:28.639][info  ][DIS] Updating services using commissioning mode 0
[16:28:49.022]  [00:00:28.639][detail][DL] Using Thread extended MAC for hostname.
[16:28:49.024]  [00:00:28.640][detail][IN] Expiring all PASE sessions
[16:28:49.024]  [00:00:28.641][info  ][BLE] Releasing end point's BLE connection back to application.
[16:28:49.025]  [00:00:28.641][detail][ZCL] Commissioning complete, notify platform driver to persist network credentials.
[16:28:49.070]  [00:00:28.698][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[16:28:49.071]  [00:00:28.699][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[16:28:49.072]  [00:00:28.699][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[16:28:49.072]  [00:00:28.699][detail][BLE] No endpoint for connection error
[16:28:49.138]  [00:00:28.765][detail][IN] UDP Message Received packet nb : 8 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:49.139]  [00:00:28.767][info  ][EM] >>> [E:1163r S:15299 M:80708139 (Ack:137613940)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:49.141]  [00:00:28.767][detail][EM] Found matching exchange: 1163r, Delegate: 0
[16:28:49.142]  [00:00:28.767][detail][EM] Rxd Ack; Removing MessageCounter:137613940 from Retrans Table on exchange 1163r
[16:28:49.161]  [00:00:28.789][detail][IN] UDP Message Received packet nb : 9 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 49
[16:28:49.162]  [00:00:28.791][info  ][EM] >>> [E:1164r S:15299 M:80708140] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:49)
[16:28:49.164]  [00:00:28.791][detail][EM] Handling via exchange: 1164r, Delegate: 0x2000413c
[16:28:49.165]  [00:00:28.791][detail][IM] Received Read request
[16:28:49.166]  [00:00:28.791][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:49.166]  [00:00:28.792][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:49.168]  [00:00:28.793][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[16:28:49.168]  [00:00:28.793][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:49.170]  [00:00:28.795][detail][DMG] <RE> Sending report (payload has 37 bytes)...
[16:28:49.171]  [00:00:28.797][info  ][EM] <<< [E:1164r S:15299 M:137613941 (Ack:80708140)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:71)
[16:28:49.173]  [00:00:28.798][info  ][EM] ??1 [E:1164r S:15299 M:137613941] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3380ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:49.175]  [00:00:28.798][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:49.176]  [00:00:28.798][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:49.177]  [00:00:28.799][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:49.177]  [00:00:28.799][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:49.673]  [00:00:29.300][detail][IN] UDP Message Received packet nb : 10 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:49.675]  [00:00:29.302][info  ][EM] >>> [E:1164r S:15299 M:80708141 (Ack:137613941)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:49.677]  [00:00:29.302][detail][EM] Found matching exchange: 1164r, Delegate: 0
[16:28:49.678]  [00:00:29.302][detail][EM] Rxd Ack; Removing MessageCounter:137613941 from Retrans Table on exchange 1164r
[16:28:49.693]  [00:00:29.320][detail][IN] UDP Message Received packet nb : 11 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:49.694]  [00:00:29.322][info  ][EM] >>> [E:1165r S:15299 M:80708142] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:49.696]  [00:00:29.323][detail][EM] Handling via exchange: 1165r, Delegate: 0x2000413c
[16:28:49.697]  [00:00:29.323][detail][IM] Received Read request
[16:28:49.698]  [00:00:29.324][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:49.699]  [00:00:29.324][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:49.700]  [00:00:29.325][detail][DMG] <RE:Run> Cluster 28, Attribute 0 is dirty
[16:28:49.701]  [00:00:29.326][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:28:49.702]  [00:00:29.326][detail][DMG] <RE:Run> Cluster 28, Attribute 1 is dirty
[16:28:49.703]  [00:00:29.327][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:28:49.704]  [00:00:29.328][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:28:49.705]  [00:00:29.328][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:28:49.706]  [00:00:29.329][detail][DMG] <RE:Run> Cluster 28, Attribute 3 is dirty
[16:28:49.707]  [00:00:29.330][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:28:49.708]  
[16:28:49.708]  [00:00:29.330][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:28:49.710]  
[16:28:49.710]  [00:00:29.331][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:28:49.711]  
[16:28:49.711]  [00:00:29.331][detail][DMG] <RE:Run> Cluster 28, Attribute 5 is dirty
[16:28:49.712]  
[16:28:49.712]  [00:00:29.332][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:28:49.713]  
[16:28:49.713]  [00:00:29.332][detail][DMG] <RE:Run> Cluster 28, Attribute 6 is dirty
[16:28:49.714]  [00:00:29.333][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:28:49.715]  
[16:28:49.716]  [00:00:29.333][detail][DMG] <RE:Run> Cluster 28, Attribute 7 is dirty
[16:28:49.717]  
[16:28:49.717]  [00:00:29.333][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:28:49.718]  
[16:28:49.718]  [00:00:29.334][detail][DMG] <RE:Run> Cluster 28, Attribute 8 is dirty
[16:28:49.719]  
[16:28:49.719]  [00:00:29.334][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:28:49.720]  
[16:28:49.721]  [00:00:29.336][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:28:49.722]  
[16:28:49.722]  [00:00:29.337][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:28:49.723]  
[16:28:49.723]  [00:00:29.338][detail][DMG] <RE:Run> Cluster 28, Attribute 15 is dirty
[16:28:49.724]  
[16:28:49.724]  [00:00:29.339][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:28:49.726]  
[16:28:49.726]  [00:00:29.341][detail][DMG] <RE:Run> Cluster 28, Attribute b is dirty
[16:28:49.727]  [00:00:29.342][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:28:49.728]  [00:00:29.343][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000C (expanded=1)
[16:28:49.729]  [00:00:29.344][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000D (expanded=1)
[16:28:49.730]  [00:00:29.346][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:28:49.732]  
[16:28:49.732]  [00:00:29.347][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000F (expanded=1)
[16:28:49.733]  [00:00:29.348][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:28:49.735]  [00:00:29.350][detail][DMG] <RE:Run> Cluster 28, Attribute fffc is dirty
[16:28:49.735]  [00:00:29.352][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:28:49.737]  [00:00:29.352][detail][DMG] <RE:Run> Cluster 28, Attribute fff8 is dirty
[16:28:49.737]  [00:00:29.354][detail][DMG] <RE:Run> Cluster 28, Attribute fffb is dirty
[16:28:49.738]  [00:00:29.355][detail][DMG] <RE> Sending report (payload has 821 bytes)...
[16:28:49.739]  [00:00:29.358][info  ][EM] <<< [E:1165r S:15299 M:137613942 (Ack:80708142)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:855)
[16:28:49.742]  [00:00:29.359][info  ][EM] ??1 [E:1165r S:15299 M:137613942] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3356ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:49.744]  [00:00:29.359][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:49.744]  [00:00:29.360][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:50.201]  [00:00:29.829][detail][IN] UDP Message Received packet nb : 12 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:50.202]  [00:00:29.831][info  ][EM] >>> [E:1165r S:15299 M:80708143 (Ack:137613942)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:50.204]  [00:00:29.831][detail][EM] Found matching exchange: 1165r, Delegate: 0
[16:28:50.206]  [00:00:29.831][detail][EM] Rxd Ack; Removing MessageCounter:137613942 from Retrans Table on exchange 1165r
[16:28:50.222]  [00:00:29.850][detail][IN] UDP Message Received packet nb : 13 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:50.224]  [00:00:29.852][info  ][EM] >>> [E:1166r S:15299 M:80708144] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:50.226]  [00:00:29.853][detail][EM] Handling via exchange: 1166r, Delegate: 0x2000413c
[16:28:50.227]  [00:00:29.853][detail][IM] Received Read request
[16:28:50.227]  [00:00:29.854][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:50.228]  [00:00:29.854][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:50.229]  [00:00:29.855][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.230]  [00:00:29.856][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.231]  [00:00:29.857][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.232]  [00:00:29.857][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.233]  [00:00:29.858][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.234]  [00:00:29.858][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.235]  [00:00:29.859][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.236]  [00:00:29.860][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.238]  [00:00:29.860][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.238]  [00:00:29.861][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.240]  [00:00:29.862][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:28:50.240]  [00:00:29.862][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:28:50.242]  [00:00:29.863][detail][DMG] <RE> Sending report (payload has 235 bytes)...
[16:28:50.242]  [00:00:29.865][info  ][EM] <<< [E:1166r S:15299 M:137613943 (Ack:80708144)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:269)
[16:28:50.245]  [00:00:29.866][info  ][EM] ??1 [E:1166r S:15299 M:137613943] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3365ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:50.247]  [00:00:29.866][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:50.248]  [00:00:29.866][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:50.249]  [00:00:29.867][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:50.249]  [00:00:29.867][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:50.638]  
[16:28:50.727]  [00:00:30.355][detail][IN] UDP Message Received packet nb : 14 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:50.729]  [00:00:30.357][info  ][EM] >>> [E:1166r S:15299 M:80708145 (Ack:137613943)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:50.731]  [00:00:30.357][detail][EM] Found matching exchange: 1166r, Delegate: 0
[16:28:50.732]  [00:00:30.357][detail][EM] Rxd Ack; Removing MessageCounter:137613943 from Retrans Table on exchange 1166r
[16:28:50.749]  [00:00:30.377][detail][IN] UDP Message Received packet nb : 15 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:50.751]  [00:00:30.379][info  ][EM] >>> [E:1167r S:15299 M:80708146] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:50.753]  [00:00:30.379][detail][EM] Handling via exchange: 1167r, Delegate: 0x2000413c
[16:28:50.754]  [00:00:30.380][detail][IM] Received Read request
[16:28:50.754]  [00:00:30.380][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:50.755]  [00:00:30.381][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:50.756]  [00:00:30.381][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.757]  [00:00:30.382][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.758]  [00:00:30.384][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.759]  [00:00:30.384][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.760]  [00:00:30.385][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.761]  [00:00:30.386][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.762]  [00:00:30.387][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.763]  [00:00:30.387][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.765]  [00:00:30.388][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.765]  [00:00:30.388][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.767]  [00:00:30.389][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:28:50.767]  [00:00:30.390][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:28:50.769]  [00:00:30.390][detail][DMG] <RE> Sending report (payload has 253 bytes)...
[16:28:50.769]  [00:00:30.393][info  ][EM] <<< [E:1167r S:15299 M:137613944 (Ack:80708146)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:287)
[16:28:50.772]  [00:00:30.394][info  ][EM] ??1 [E:1167r S:15299 M:137613944] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3337ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:50.774]  [00:00:30.394][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:50.775]  [00:00:30.394][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:50.776]  [00:00:30.394][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:50.776]  [00:00:30.395][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:51.252]  [00:00:30.879][detail][IN] UDP Message Received packet nb : 16 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:51.253]  [00:00:30.881][info  ][EM] >>> [E:1167r S:15299 M:80708147 (Ack:137613944)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:51.255]  [00:00:30.881][detail][EM] Found matching exchange: 1167r, Delegate: 0
[16:28:51.257]  [00:00:30.881][detail][EM] Rxd Ack; Removing MessageCounter:137613944 from Retrans Table on exchange 1167r
[16:28:51.279]  [00:00:30.907][detail][IN] UDP Message Received packet nb : 17 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:51.281]  [00:00:30.909][info  ][EM] >>> [E:1168r S:15299 M:80708148] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:51.283]  [00:00:30.910][detail][EM] Handling via exchange: 1168r, Delegate: 0x2000413c
[16:28:51.283]  [00:00:30.910][detail][IM] Received Read request
[16:28:51.284]  [00:00:30.911][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:51.285]  [00:00:30.911][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:51.286]  [00:00:30.912][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.287]  [00:00:30.913][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.288]  [00:00:30.914][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.289]  [00:00:30.915][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.290]  [00:00:30.915][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.291]  [00:00:30.916][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.292]  [00:00:30.916][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.293]  [00:00:30.916][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.294]  [00:00:30.917][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.295]  [00:00:30.917][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.297]  [00:00:30.918][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:28:51.297]  [00:00:30.918][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0002 (expanded=1)
[16:28:51.299]  [00:00:30.919][detail][DMG] <RE> Sending report (payload has 168 bytes)...
[16:28:51.299]  [00:00:30.921][info  ][EM] <<< [E:1168r S:15299 M:137613945 (Ack:80708148)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:202)
[16:28:51.302]  [00:00:30.922][info  ][EM] ??1 [E:1168r S:15299 M:137613945] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3359ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:51.304]  [00:00:30.922][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:51.305]  [00:00:30.923][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:51.306]  [00:00:30.923][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:51.306]  [00:00:30.923][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:51.778]  [00:00:31.406][detail][IN] UDP Message Received packet nb : 18 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:51.780]  [00:00:31.407][info  ][EM] >>> [E:1168r S:15299 M:80708149 (Ack:137613945)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:51.782]  [00:00:31.407][detail][EM] Found matching exchange: 1168r, Delegate: 0
[16:28:51.783]  [00:00:31.408][detail][EM] Rxd Ack; Removing MessageCounter:137613945 from Retrans Table on exchange 1168r
[16:28:51.802]  [00:00:31.429][detail][IN] UDP Message Received packet nb : 19 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 46
[16:28:51.803]  [00:00:31.431][info  ][EM] >>> [E:1169r S:15299 M:80708150] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:46)
[16:28:51.805]  [00:00:31.431][detail][EM] Handling via exchange: 1169r, Delegate: 0x2000413c
[16:28:51.806]  [00:00:31.432][detail][IM] Received Read request
[16:28:51.807]  [00:00:31.432][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:51.807]  [00:00:31.432][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:51.809]  [00:00:31.433][detail][DMG] <RE:Run> Cluster 41, Attribute fffc is dirty
[16:28:51.810]  [00:00:31.434][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.811]  [00:00:31.435][detail][DMG] <RE:Run> Cluster 40, Attribute fffc is dirty
[16:28:51.812]  [00:00:31.435][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.813]  [00:00:31.436][detail][DMG] <RE:Run> Cluster 3f, Attribute fffc is dirty
[16:28:51.814]  [00:00:31.437][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.815]  [00:00:31.437][detail][DMG] <RE:Run> Cluster 3e, Attribute fffc is dirty
[16:28:51.816]  [00:00:31.438][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.817]  
[16:28:51.818]  [00:00:31.438][detail][DMG] <RE:Run> Cluster 3c, Attribute fffc is dirty
[16:28:51.818]  [00:00:31.439][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.820]  
[16:28:51.820]  [00:00:31.440][detail][DMG] <RE:Run> Cluster 34, Attribute fffc is dirty
[16:28:51.820]  
[16:28:51.820]  [00:00:31.440][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.822]  
[16:28:51.822]  [00:00:31.441][detail][DMG] <RE:Run> Cluster 33, Attribute fffc is dirty
[16:28:51.823]  [00:00:31.442][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.824]  
[16:28:51.825]  [00:00:31.442][detail][DMG] <RE:Run> Cluster 30, Attribute fffc is dirty
[16:28:51.825]  
[16:28:51.825]  [00:00:31.443][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.827]  [00:00:31.443][detail][DMG] <RE:Run> Cluster 2b, Attribute fffc is dirty
[16:28:51.827]  [00:00:31.444][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.829]  [00:00:31.446][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.830]  
[16:28:51.830]  [00:00:31.446][detail][DMG] <RE:Run> Cluster 1f, Attribute fffc is dirty
[16:28:51.831]  
[16:28:51.831]  [00:00:31.448][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.832]  
[16:28:51.833]  [00:00:31.449][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[16:28:51.833]  [00:00:31.450][detail][DMG] <RE:Run> Cluster 2a, Attribute fffc is dirty
[16:28:51.834]  [00:00:31.451][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.836]  
[16:28:51.836]  [00:00:31.453][detail][DMG] <RE:Run> Cluster 2f, Attribute fffc is dirty
[16:28:51.836]  
[16:28:51.837]  [00:00:31.454][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.838]  
[16:28:51.838]  [00:00:31.455][detail][DMG] <RE:Run> Cluster 35, Attribute fffc is dirty
[16:28:51.839]  
[16:28:51.839]  [00:00:31.456][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.840]  
[16:28:51.840]  [00:00:31.457][detail][DMG] <RE:Run> Cluster 46, Attribute fffc is dirty
[16:28:51.841]  
[16:28:51.842]  [00:00:31.458][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.843]  
[16:28:51.843]  [00:00:31.459][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.845]  
[16:28:51.845]  [00:00:31.460][detail][DMG] <RE:Run> Cluster 102, Attribute fffc is dirty
[16:28:51.845]  
[16:28:51.845]  [00:00:31.461][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.847]  
[16:28:51.847]  [00:00:31.462][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:28:51.848]  
[16:28:51.848]  [00:00:31.463][detail][DMG] <RE:Run> Cluster 4, Attribute fffc is dirty
[16:28:51.849]  [00:00:31.465][detail][DMG] <RE:Run> Cluster 102, Attribute fffc is dirty
[16:28:51.849]  
[16:28:51.850]  [00:00:31.466][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:28:51.851]  [00:00:31.467][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:28:51.852]  
[16:28:51.852]  [00:00:31.468][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.853]  
[16:28:51.853]  [00:00:31.469][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.854]  
[16:28:51.854]  [00:00:31.471][detail][DMG] <RE:Run> Cluster 300, Attribute fffc is dirty
[16:28:51.856]  
[16:28:51.856]  [00:00:31.472][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:28:51.856]  [00:00:31.473][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:28:51.857]  [00:00:31.475][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.858]  [00:00:31.476][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.860]  
[16:28:51.860]  [00:00:31.477][detail][DMG] <RE:Run> Cluster 8, Attribute fffc is dirty
[16:28:51.861]  [00:00:31.478][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:28:51.861]  [00:00:31.478][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.863]  [00:00:31.479][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.864]  [00:00:31.481][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.865]  [00:00:31.482][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:28:51.867]  [00:00:31.486][info  ][EM] <<< [E:1169r S:15299 M:137613946 (Ack:80708150)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:1181)
[16:28:51.869]  [00:00:31.487][info  ][EM] ??1 [E:1169r S:15299 M:137613946] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3409ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:51.871]  [00:00:31.487][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:51.872]  [00:00:31.487][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:52.302]  [00:00:31.930][detail][IN] UDP Message Received packet nb : 20 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:52.304]  [00:00:31.931][info  ][EM] >>> [E:1169r S:15299 M:80708151 (Ack:137613946)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:52.306]  [00:00:31.932][detail][EM] Found matching exchange: 1169r, Delegate: 0
[16:28:52.307]  [00:00:31.932][detail][EM] Rxd Ack; Removing MessageCounter:137613946 from Retrans Table on exchange 1169r
[16:28:52.323]  [00:00:31.951][detail][IN] UDP Message Received packet nb : 21 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 51
[16:28:52.324]  [00:00:31.953][info  ][EM] >>> [E:1170r S:15299 M:80708152] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:52.326]  [00:00:31.954][detail][EM] Handling via exchange: 1170r, Delegate: 0x2000413c
[16:28:52.327]  [00:00:31.954][detail][IM] Received Read request
[16:28:52.328]  [00:00:31.955][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:52.328]  [00:00:31.955][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:52.330]  [00:00:31.956][detail][DMG] <RE:Run> Cluster 28, Attribute 5 is dirty
[16:28:52.331]  [00:00:31.957][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=0)
[16:28:52.332]  [00:00:31.958][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:52.333]  [00:00:31.959][info  ][EM] <<< [E:1170r S:15299 M:137613947 (Ack:80708152)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:70)
[16:28:52.335]  [00:00:31.960][info  ][EM] ??1 [E:1170r S:15299 M:137613947] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3351ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:52.337]  [00:00:31.960][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:52.338]  [00:00:31.961][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:52.339]  [00:00:31.961][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:52.339]  [00:00:31.961][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:52.638]  
[16:28:52.837]  [00:00:32.465][detail][IN] UDP Message Received packet nb : 22 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:52.838]  [00:00:32.466][info  ][EM] >>> [E:1170r S:15299 M:80708153 (Ack:137613947)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:52.840]  [00:00:32.467][detail][EM] Found matching exchange: 1170r, Delegate: 0
[16:28:52.842]  [00:00:32.467][detail][EM] Rxd Ack; Removing MessageCounter:137613947 from Retrans Table on exchange 1170r
[16:28:52.857]  [00:00:32.485][detail][IN] UDP Message Received packet nb : 23 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 51
[16:28:52.858]  [00:00:32.487][info  ][EM] >>> [E:1171r S:15299 M:80708154] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:28:52.860]  [00:00:32.487][detail][EM] Handling via exchange: 1171r, Delegate: 0x2000413c
[16:28:52.861]  [00:00:32.488][detail][IM] Received Read request
[16:28:52.861]  [00:00:32.489][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:52.862]  [00:00:32.489][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:52.864]  [00:00:32.491][detail][DMG] <RE:Run> Cluster 35, Attribute 1 is dirty
[16:28:52.864]  [00:00:32.492][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:28:52.866]  [00:00:32.493][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:28:52.866]  [00:00:32.495][info  ][EM] <<< [E:1171r S:15299 M:137613948 (Ack:80708154)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:70)
[16:28:52.869]  [00:00:32.496][info  ][EM] ??1 [E:1171r S:15299 M:137613948] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3350ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:52.871]  [00:00:32.497][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:52.872]  [00:00:32.497][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:52.873]  [00:00:32.497][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:52.873]  [00:00:32.497][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:53.358]  [00:00:32.986][detail][IN] UDP Message Received packet nb : 24 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:53.359]  [00:00:32.987][info  ][EM] >>> [E:1171r S:15299 M:80708155 (Ack:137613948)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:53.361]  [00:00:32.988][detail][EM] Found matching exchange: 1171r, Delegate: 0
[16:28:53.363]  [00:00:32.988][detail][EM] Rxd Ack; Removing MessageCounter:137613948 from Retrans Table on exchange 1171r
[16:28:53.378]  [00:00:33.006][detail][IN] UDP Message Received packet nb : 25 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:53.380]  [00:00:33.008][info  ][EM] >>> [E:1172r S:15299 M:80708156] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:53.382]  [00:00:33.008][detail][EM] Handling via exchange: 1172r, Delegate: 0x2000413c
[16:28:53.382]  [00:00:33.008][detail][IM] Received Read request
[16:28:53.383]  [00:00:33.009][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:53.384]  [00:00:33.009][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:53.385]  [00:00:33.010][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.386]  [00:00:33.011][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.387]  [00:00:33.012][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.388]  [00:00:33.013][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.389]  [00:00:33.014][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.390]  [00:00:33.014][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.391]  [00:00:33.015][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.392]  [00:00:33.015][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.394]  [00:00:33.016][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.394]  [00:00:33.016][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.396]  [00:00:33.017][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:28:53.396]  [00:00:33.018][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0003 (expanded=1)
[16:28:53.398]  [00:00:33.018][detail][DMG] <RE> Sending report (payload has 176 bytes)...
[16:28:53.398]  [00:00:33.020][info  ][EM] <<< [E:1172r S:15299 M:137613949 (Ack:80708156)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:210)
[16:28:53.401]  [00:00:33.021][info  ][EM] ??1 [E:1172r S:15299 M:137613949] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3335ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:53.403]  [00:00:33.022][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:53.404]  [00:00:33.022][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:53.405]  [00:00:33.022][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:53.405]  [00:00:33.022][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:53.883]  [00:00:33.511][detail][IN] UDP Message Received packet nb : 26 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:53.884]  [00:00:33.512][info  ][EM] >>> [E:1172r S:15299 M:80708157 (Ack:137613949)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:53.886]  [00:00:33.513][detail][EM] Found matching exchange: 1172r, Delegate: 0
[16:28:53.888]  [00:00:33.513][detail][EM] Rxd Ack; Removing MessageCounter:137613949 from Retrans Table on exchange 1172r
[16:28:53.921]  [00:00:33.549][detail][IN] UDP Message Received packet nb : 27 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 85
[16:28:53.923]  [00:00:33.551][info  ][EM] >>> [E:1173r S:15299 M:80708158] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[16:28:53.925]  [00:00:33.552][detail][EM] Handling via exchange: 1173r, Delegate: 0x2000413c
[16:28:53.925]  [00:00:33.553][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0009
[16:28:53.927]  [00:00:33.553][info  ][ZCL] OpCreds: Received an UpdateFabricLabel command
[16:28:53.927]  [00:00:33.554][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:28:53.928]  [00:00:33.554][detail][DMG] Command handler moving to [NewRespons]
[16:28:53.929]  [00:00:33.554][detail][DMG] Command handler moving to [ Preparing]
[16:28:53.929]  [00:00:33.555][detail][DMG] Command handler moving to [AddingComm]
[16:28:53.931]  [00:00:33.555][detail][DMG] Command handler moving to [AddedComma]
[16:28:53.932]  [00:00:33.555][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:28:53.932]  [00:00:33.555][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:28:53.933]  [00:00:33.556][detail][DMG] Command handler moving to [AwaitingDe]
[16:28:53.934]  [00:00:33.558][info  ][EM] <<< [E:1173r S:15299 M:137613950 (Ack:80708158)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:73)
[16:28:53.936]  [00:00:33.559][info  ][EM] ??1 [E:1173r S:15299 M:137613950] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3364ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:53.938]  [00:00:33.559][detail][DMG] Command response sender moving to [AllInvokeR]
[16:28:54.432]  [00:00:34.060][detail][IN] UDP Message Received packet nb : 28 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:54.433]  [00:00:34.061][info  ][EM] >>> [E:1173r S:15299 M:80708159 (Ack:137613950)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:54.436]  [00:00:34.062][detail][EM] Found matching exchange: 1173r, Delegate: 0
[16:28:54.437]  [00:00:34.062][detail][EM] Rxd Ack; Removing MessageCounter:137613950 from Retrans Table on exchange 1173r
[16:28:54.638]  
[16:28:55.430]  [00:00:35.057][detail][IN] UDP Message Received packet nb : 29 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:55.433]  [00:00:35.060][info  ][EM] >>> [E:1174r S:15299 M:80708160] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:55.434]  [00:00:35.061][detail][EM] Handling via exchange: 1174r, Delegate: 0x2000413c
[16:28:55.435]  [00:00:35.061][detail][IM] Received Read request
[16:28:55.435]  [00:00:35.062][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:55.436]  [00:00:35.062][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:55.437]  [00:00:35.063][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[16:28:55.438]  [00:00:35.064][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:28:55.440]  [00:00:35.064][detail][DMG] <RE:Run> Cluster 33, Attribute 1 is dirty
[16:28:55.440]  [00:00:35.065][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:28:55.442]  [00:00:35.065][detail][DMG] <RE:Run> Cluster 33, Attribute 8 is dirty
[16:28:55.442]  [00:00:35.066][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:28:55.444]  [00:00:35.066][detail][DMG] <RE:Run> Cluster 33, Attribute 3 is dirty
[16:28:55.444]  [00:00:35.067][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:28:55.446]  
[16:28:55.446]  [00:00:35.068][detail][DMG] <RE:Run> Cluster 33, Attribute 4 is dirty
[16:28:55.447]  
[16:28:55.447]  [00:00:35.068][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:28:55.448]  
[16:28:55.448]  [00:00:35.069][detail][DMG] <RE:Run> Cluster 33, Attribute 5 is dirty
[16:28:55.449]  [00:00:35.069][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:28:55.451]  [00:00:35.070][detail][DMG] <RE:Run> Cluster 33, Attribute 6 is dirty
[16:28:55.451]  [00:00:35.071][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:28:55.453]  [00:00:35.071][detail][DMG] <RE:Run> Cluster 33, Attribute 7 is dirty
[16:28:55.453]  [00:00:35.072][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:28:55.455]  [00:00:35.072][detail][DMG] <RE:Run> Cluster 33, Attribute 2 is dirty
[16:28:55.455]  
[16:28:55.455]  [00:00:35.073][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:28:55.457]  [00:00:35.074][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:55.458]  [00:00:35.075][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:28:55.460]  [00:00:35.077][detail][DMG] <RE:Run> Cluster 33, Attribute fffb is dirty
[16:28:55.460]  [00:00:35.079][detail][DMG] <RE> Sending report (payload has 527 bytes)...
[16:28:55.461]  [00:00:35.081][info  ][EM] <<< [E:1174r S:15299 M:137613951 (Ack:80708160)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:561)
[16:28:55.464]  [00:00:35.082][info  ][EM] ??1 [E:1174r S:15299 M:137613951] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3336ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:55.465]  [00:00:35.083][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:55.466]  [00:00:35.083][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:55.467]  [00:00:35.083][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:55.468]  [00:00:35.089][detail][IN] UDP Message Received packet nb : 30 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:55.470]  [00:00:35.091][info  ][EM] >>> [E:1175r S:15299 M:80708161] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:55.472]  
[16:28:55.472]  [00:00:35.092][detail][EM] Handling via exchange: 1175r, Delegate: 0x2000413c
[16:28:55.473]  [00:00:35.092][detail][IM] Received Read request
[16:28:55.473]  [00:00:35.093][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:55.474]  [00:00:35.093][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:55.476]  [00:00:35.094][detail][DMG] <RE> Sending report (payload has 7 bytes)...
[16:28:55.476]  [00:00:35.096][info  ][EM] <<< [E:1175r S:15299 M:137613952 (Ack:80708161)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:41)
[16:28:55.479]  [00:00:35.097][info  ][EM] ??1 [E:1175r S:15299 M:137613952] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3363ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:55.481]  [00:00:35.098][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:55.482]  [00:00:35.098][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:55.482]  [00:00:35.098][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:55.628]  [00:00:35.255][detail][IN] UDP Message Received packet nb : 31 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 83
[16:28:55.629]  [00:00:35.257][info  ][EM] >>> [E:1176r S:15299 M:80708162] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:06 (IM:WriteRequest) (B:83)
[16:28:55.631]  [00:00:35.257][detail][EM] Handling via exchange: 1176r, Delegate: 0x2000413c
[16:28:55.632]  [00:00:35.258][detail][IM] Received Write request
[16:28:55.632]  [00:00:35.258][detail][DMG] IM WH moving to [Initialized]
[16:28:55.633]  [00:00:35.259][detail][DMG] Writing attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005
[16:28:55.635]  [00:00:35.260][detail][DMG] IM WH moving to [AddStatus]
[16:28:55.635]  [00:00:35.263][info  ][EM] <<< [E:1176r S:15299 M:137613953 (Ack:80708162)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:07 (IM:WriteResponse) (B:62)
[16:28:55.637]  [00:00:35.264][info  ][EM] ??1 [E:1176r S:15299 M:137613953] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3352ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:55.640]  [00:00:35.264][detail][DMG] IM WH moving to [Sending]
[16:28:55.640]  [00:00:35.264][detail][DMG] IM WH moving to [Uninitialized]
[16:28:55.670]  [00:00:35.298][detail][IN] UDP Message Received packet nb : 32 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:55.672]  [00:00:35.300][info  ][EM] >>> [E:1177r S:15299 M:80708163] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:55.674]  [00:00:35.300][detail][EM] Handling via exchange: 1177r, Delegate: 0x2000413c
[16:28:55.674]  [00:00:35.300][detail][IM] Received Read request
[16:28:55.675]  [00:00:35.301][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:55.676]  [00:00:35.301][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:55.677]  [00:00:35.302][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[16:28:55.678]  [00:00:35.303][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:28:55.679]  [00:00:35.304][detail][DMG] <RE:Run> Cluster 33, Attribute 1 is dirty
[16:28:55.680]  [00:00:35.305][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:28:55.681]  [00:00:35.305][detail][DMG] <RE:Run> Cluster 33, Attribute 8 is dirty
[16:28:55.682]  [00:00:35.306][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:28:55.683]  [00:00:35.307][detail][DMG] <RE:Run> Cluster 33, Attribute 3 is dirty
[16:28:55.684]  [00:00:35.307][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:28:55.685]  
[16:28:55.685]  [00:00:35.308][detail][DMG] <RE:Run> Cluster 33, Attribute 4 is dirty
[16:28:55.687]  
[16:28:55.687]  [00:00:35.309][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:28:55.688]  
[16:28:55.688]  [00:00:35.309][detail][DMG] <RE:Run> Cluster 33, Attribute 5 is dirty
[16:28:55.689]  [00:00:35.310][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:28:55.690]  [00:00:35.310][detail][DMG] <RE:Run> Cluster 33, Attribute 6 is dirty
[16:28:55.691]  [00:00:35.311][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:28:55.692]  [00:00:35.311][detail][DMG] <RE:Run> Cluster 33, Attribute 7 is dirty
[16:28:55.693]  [00:00:35.312][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:28:55.694]  
[16:28:55.694]  [00:00:35.312][detail][DMG] <RE:Run> Cluster 33, Attribute 2 is dirty
[16:28:55.695]  
[16:28:55.695]  [00:00:35.313][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:28:55.697]  [00:00:35.314][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:55.698]  [00:00:35.315][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:28:55.699]  [00:00:35.317][detail][DMG] <RE:Run> Cluster 33, Attribute fff9 is dirty
[16:28:55.700]  [00:00:35.317][detail][DMG] <RE:Run> Cluster 33, Attribute fffb is dirty
[16:28:55.701]  [00:00:35.319][detail][DMG] <RE> Sending report (payload has 527 bytes)...
[16:28:55.702]  [00:00:35.321][info  ][EM] <<< [E:1177r S:15299 M:137613954 (Ack:80708163)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:561)
[16:28:55.704]  [00:00:35.322][info  ][EM] ??1 [E:1177r S:15299 M:137613954] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3365ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:55.706]  [00:00:35.323][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:55.707]  [00:00:35.323][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:55.708]  [00:00:35.334][detail][IN] UDP Message Received packet nb : 33 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 57
[16:28:55.710]  [00:00:35.336][info  ][EM] >>> [E:1178r S:15299 M:80708164] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:03 (IM:SubscribeRequest) (B:57)
[16:28:55.712]  [00:00:35.337][detail][EM] Handling via exchange: 1178r, Delegate: 0x2000413c
[16:28:55.713]  [00:00:35.337][detail][IM] Received Subscribe request
[16:28:55.713]  [00:00:35.337][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[16:28:55.721]  [00:00:35.349][info  ][DMG] Subscription id 0x49a60982 from node <8CBDA24D2F21C48C, 1> torn down
[16:28:55.722]  [00:00:35.349][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:55.723]  [00:00:35.351][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[16:28:55.723]  [00:00:35.352][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:55.735]  [00:00:35.363][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:55.736]  [00:00:35.364][detail][DMG] <RE:Run> Cluster 28, Attribute 9 is dirty
[16:28:55.737]  [00:00:35.365][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:28:55.739]  [00:00:35.366][detail][DMG] <RE> Sending report (payload has 40 bytes)...
[16:28:55.741]  [00:00:35.369][info  ][EM] <<< [E:1178r S:15299 M:137613955 (Ack:80708164)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:74)
[16:28:55.743]  [00:00:35.370][info  ][EM] ??1 [E:1178r S:15299 M:137613955] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3387ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:55.745]  [00:00:35.370][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:28:55.745]  [00:00:35.370][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:28:55.746]  [00:00:35.370][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:55.832]  [00:00:35.459][detail][IN] UDP Message Received packet nb : 34 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:55.833]  [00:00:35.461][info  ][EM] >>> [E:1174r S:15299 M:80708165 (Ack:137613951)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:55.836]  [00:00:35.461][detail][EM] Found matching exchange: 1174r, Delegate: 0
[16:28:55.837]  [00:00:35.462][detail][EM] Rxd Ack; Removing MessageCounter:137613951 from Retrans Table on exchange 1174r
[16:28:55.861]  [00:00:35.490][detail][IN] UDP Message Received packet nb : 35 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:55.863]  [00:00:35.491][info  ][EM] >>> [E:1175r S:15299 M:80708166 (Ack:137613952)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:55.865]  [00:00:35.491][detail][EM] Found matching exchange: 1175r, Delegate: 0
[16:28:55.866]  [00:00:35.492][detail][EM] Rxd Ack; Removing MessageCounter:137613952 from Retrans Table on exchange 1175r
[16:28:55.924]  [00:00:35.552][detail][IN] UDP Message Received packet nb : 36 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:55.925]  [00:00:35.553][info  ][EM] >>> [E:1176r S:15299 M:80708167 (Ack:137613953)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:55.927]  [00:00:35.553][detail][EM] Found matching exchange: 1176r, Delegate: 0
[16:28:55.929]  [00:00:35.554][detail][EM] Rxd Ack; Removing MessageCounter:137613953 from Retrans Table on exchange 1176r
[16:28:56.426]  [00:00:36.053][detail][IN] UDP Message Received packet nb : 37 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:56.427]  [00:00:36.055][info  ][EM] >>> [E:1177r S:15299 M:80708168 (Ack:137613954)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:56.429]  [00:00:36.055][detail][EM] Found matching exchange: 1177r, Delegate: 0
[16:28:56.430]  [00:00:36.056][detail][EM] Rxd Ack; Removing MessageCounter:137613954 from Retrans Table on exchange 1177r
[16:28:56.448]  [00:00:36.076][detail][IN] UDP Message Received packet nb : 38 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 42
[16:28:56.450]  [00:00:36.078][info  ][EM] >>> [E:1178r S:15299 M:80708169 (Ack:137613955)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:28:56.452]  [00:00:36.079][detail][EM] Found matching exchange: 1178r, Delegate: 0x20005dd0
[16:28:56.453]  [00:00:36.079][detail][EM] Rxd Ack; Removing MessageCounter:137613955 from Retrans Table on exchange 1178r
[16:28:56.454]  [00:00:36.080][info  ][IM] Received status response, status is 0x00
[16:28:56.454]  [00:00:36.082][info  ][EM] <<< [E:1178r S:15299 M:137613956 (Ack:80708169)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:28:56.457]  [00:00:36.083][info  ][EM] ??1 [E:1178r S:15299 M:137613956] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3404ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:56.459]  [00:00:36.083][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x0000000000008CF3 and system Timestamp 0x000000000009B4B3.
[16:28:56.461]  [00:00:36.083][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:56.461]  [00:00:36.083][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:56.470]  [00:00:36.098][detail][IN] UDP Message Received packet nb : 39 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 48
[16:28:56.471]  [00:00:36.100][info  ][EM] >>> [E:1179r S:15299 M:80708170] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:48)
[16:28:56.473]  [00:00:36.100][detail][EM] Handling via exchange: 1179r, Delegate: 0x2000413c
[16:28:56.474]  [00:00:36.101][detail][IM] Received Read request
[16:28:56.475]  [00:00:36.101][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:56.476]  [00:00:36.102][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:56.477]  [00:00:36.103][detail][DMG] <RE:Run> Cluster 35, Attribute 0 is dirty
[16:28:56.478]  [00:00:36.104][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:28:56.479]  [00:00:36.105][detail][DMG] <RE:Run> Cluster 35, Attribute 1 is dirty
[16:28:56.480]  [00:00:36.106][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:28:56.481]  [00:00:36.107][detail][DMG] <RE:Run> Cluster 35, Attribute 2 is dirty
[16:28:56.482]  [00:00:36.108][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:28:56.483]  [00:00:36.108][detail][DMG] <RE:Run> Cluster 35, Attribute 3 is dirty
[16:28:56.484]  [00:00:36.109][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:28:56.485]  [00:00:36.110][detail][DMG] <RE:Run> Cluster 35, Attribute 4 is dirty
[16:28:56.486]  [00:00:36.111][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:28:56.487]  [00:00:36.112][detail][DMG] <RE:Run> Cluster 35, Attribute 5 is dirty
[16:28:56.488]  [00:00:36.114][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:28:56.489]  [00:00:36.115][detail][DMG] <RE:Run> Cluster 35, Attribute 6 is dirty
[16:28:56.490]  [00:00:36.116][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:28:56.492]  [00:00:36.117][detail][DMG] <RE:Run> Cluster 35, Attribute 7 is dirty
[16:28:56.492]  [00:00:36.118][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:28:56.494]  [00:00:36.119][detail][DMG] <RE:Run> Cluster 35, Attribute 8 is dirty
[16:28:56.494]  [00:00:36.120][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:28:56.496]  [00:00:36.120][detail][DMG] <RE:Run> Cluster 35, Attribute 9 is dirty
[16:28:56.496]  [00:00:36.121][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:28:56.498]  [00:00:36.122][detail][DMG] <RE:Run> Cluster 35, Attribute a is dirty
[16:28:56.498]  [00:00:36.123][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:28:56.500]  [00:00:36.124][detail][DMG] <RE:Run> Cluster 35, Attribute b is dirty
[16:28:56.501]  [00:00:36.125][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:28:56.502]  [00:00:36.125][detail][DMG] <RE:Run> Cluster 35, Attribute c is dirty
[16:28:56.503]  [00:00:36.125][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000C (expanded=1)
[16:28:56.504]  [00:00:36.126][detail][DMG] <RE:Run> Cluster 35, Attribute d is dirty
[16:28:56.505]  [00:00:36.127][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000D (expanded=1)
[16:28:56.506]  [00:00:36.128][detail][DMG] <RE:Run> Cluster 35, Attribute e is dirty
[16:28:56.507]  [00:00:36.129][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:28:56.508]  [00:00:36.130][detail][DMG] <RE:Run> Cluster 35, Attribute f is dirty
[16:28:56.509]  [00:00:36.131][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000F (expanded=1)
[16:28:56.510]  [00:00:36.131][detail][DMG] <RE:Run> Cluster 35, Attribute 10 is dirty
[16:28:56.511]  [00:00:36.132][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:28:56.512]  [00:00:36.133][detail][DMG] <RE:Run> Cluster 35, Attribute 11 is dirty
[16:28:56.513]  [00:00:36.134][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0011 (expanded=1)
[16:28:56.514]  [00:00:36.135][detail][DMG] <RE:Run> Cluster 35, Attribute 12 is dirty
[16:28:56.515]  [00:00:36.136][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0012 (expanded=1)
[16:28:56.517]  [00:00:36.137][detail][DMG] <RE:Run> Cluster 35, Attribute 13 is dirty
[16:28:56.517]  [00:00:36.138][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0013 (expanded=1)
[16:28:56.518]  [00:00:36.138][detail][DMG] <RE:Run> Cluster 35, Attribute 14 is dirty
[16:28:56.519]  [00:00:36.139][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0014 (expanded=1)
[16:28:56.520]  
[16:28:56.521]  [00:00:36.140][detail][DMG] <RE:Run> Cluster 35, Attribute 15 is dirty
[16:28:56.521]  [00:00:36.141][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:28:56.523]  [00:00:36.142][detail][DMG] <RE:Run> Cluster 35, Attribute 16 is dirty
[16:28:56.524]  [00:00:36.143][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0016 (expanded=1)
[16:28:56.525]  
[16:28:56.525]  [00:00:36.143][detail][DMG] <RE:Run> Cluster 35, Attribute 17 is dirty
[16:28:56.526]  [00:00:36.144][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0017 (expanded=1)
[16:28:56.527]  
[16:28:56.527]  [00:00:36.145][detail][DMG] <RE:Run> Cluster 35, Attribute 18 is dirty
[16:28:56.528]  [00:00:36.146][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0018 (expanded=1)
[16:28:56.529]  [00:00:36.147][detail][DMG] <RE:Run> Cluster 35, Attribute 19 is dirty
[16:28:56.530]  [00:00:36.148][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0019 (expanded=1)
[16:28:56.531]  [00:00:36.150][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001A (expanded=1)
[16:28:56.532]  
[16:28:56.532]  [00:00:36.150][detail][DMG] <RE:Run> Cluster 35, Attribute 1b is dirty
[16:28:56.533]  [00:00:36.151][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001B (expanded=1)
[16:28:56.535]  
[16:28:56.535]  [00:00:36.152][detail][DMG] <RE:Run> Cluster 35, Attribute 1c is dirty
[16:28:56.536]  [00:00:36.154][detail][DMG] <RE:Run> Cluster 35, Attribute 1d is dirty
[16:28:56.537]  [00:00:36.155][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001D (expanded=1)
[16:28:56.538]  [00:00:36.157][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001E (expanded=1)
[16:28:56.539]  
[16:28:56.539]  [00:00:36.157][detail][DMG] <RE:Run> Cluster 35, Attribute 1f is dirty
[16:28:56.540]  [00:00:36.158][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001F (expanded=1)
[16:28:56.542]  [00:00:36.159][detail][DMG] <RE:Run> Cluster 35, Attribute 20 is dirty
[16:28:56.542]  [00:00:36.160][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0020 (expanded=1)
[16:28:56.544]  
[16:28:56.544]  [00:00:36.162][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0021 (expanded=1)
[16:28:56.545]  [00:00:36.162][detail][DMG] <RE:Run> Cluster 35, Attribute 22 is dirty
[16:28:56.546]  [00:00:36.164][detail][DMG] <RE:Run> Cluster 35, Attribute 23 is dirty
[16:28:56.546]  
[16:28:56.546]  [00:00:36.165][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0023 (expanded=1)
[16:28:56.548]  [00:00:36.166][detail][DMG] <RE:Run> Cluster 35, Attribute 24 is dirty
[16:28:56.548]  [00:00:36.166][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0024 (expanded=1)
[16:28:56.550]  [00:00:36.168][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0025 (expanded=1)
[16:28:56.551]  [00:00:36.169][detail][DMG] <RE:Run> Cluster 35, Attribute 26 is dirty
[16:28:56.552]  [00:00:36.170][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0026 (expanded=1)
[16:28:56.553]  [00:00:36.170][detail][DMG] <RE:Run> Cluster 35, Attribute 27 is dirty
[16:28:56.554]  [00:00:36.172][detail][DMG] <RE:Run> Cluster 35, Attribute 28 is dirty
[16:28:56.555]  [00:00:36.173][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0028 (expanded=1)
[16:28:56.556]  [00:00:36.174][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0035, attributeId: 0x0000_0028, err = b
[16:28:56.558]  [00:00:36.176][info  ][EM] <<< [E:1179r S:15299 M:137613957 (Ack:80708170)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:1201)
[16:28:56.560]  [00:00:36.178][info  ][EM] ??1 [E:1179r S:15299 M:137613957] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3378ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:56.562]  [00:00:36.178][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:28:56.563]  [00:00:36.178][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:28:56.585]  [00:00:36.212][detail][IN] UDP Message Received packet nb : 40 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:56.586]  [00:00:36.214][info  ][EM] >>> [E:1178r S:15299 M:80708171 (Ack:137613956)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:56.588]  [00:00:36.214][detail][EM] Found matching exchange: 1178r, Delegate: 0
[16:28:56.590]  [00:00:36.214][detail][EM] Rxd Ack; Removing MessageCounter:137613956 from Retrans Table on exchange 1178r
[16:28:56.653]  
[16:28:57.092]  [00:00:36.720][detail][IN] UDP Message Received packet nb : 41 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 42
[16:28:57.093]  [00:00:36.722][info  ][EM] >>> [E:1179r S:15299 M:80708172 (Ack:137613957)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:28:57.095]  [00:00:36.722][detail][EM] Found matching exchange: 1179r, Delegate: 0x20005e60
[16:28:57.097]  [00:00:36.722][detail][EM] Rxd Ack; Removing MessageCounter:137613957 from Retrans Table on exchange 1179r
[16:28:57.097]  [00:00:36.722][info  ][IM] Received status response, status is 0x00
[16:28:57.098]  [00:00:36.723][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:57.099]  [00:00:36.723][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:57.100]  [00:00:36.723][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:57.102]  [00:00:36.724][detail][DMG] <RE:Run> Cluster 35, Attribute 28 is dirty
[16:28:57.102]  [00:00:36.725][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0028 (expanded=1)
[16:28:57.104]  [00:00:36.725][detail][DMG] <RE:Run> Cluster 35, Attribute 29 is dirty
[16:28:57.104]  [00:00:36.726][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0029 (expanded=1)
[16:28:57.106]  [00:00:36.727][detail][DMG] <RE:Run> Cluster 35, Attribute 2a is dirty
[16:28:57.106]  [00:00:36.728][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002A (expanded=1)
[16:28:57.108]  [00:00:36.729][detail][DMG] <RE:Run> Cluster 35, Attribute 2b is dirty
[16:28:57.109]  [00:00:36.730][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002B (expanded=1)
[16:28:57.110]  [00:00:36.731][detail][DMG] <RE:Run> Cluster 35, Attribute 2c is dirty
[16:28:57.111]  [00:00:36.732][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002C (expanded=1)
[16:28:57.112]  [00:00:36.732][detail][DMG] <RE:Run> Cluster 35, Attribute 2d is dirty
[16:28:57.113]  [00:00:36.733][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002D (expanded=1)
[16:28:57.114]  [00:00:36.734][detail][DMG] <RE:Run> Cluster 35, Attribute 2e is dirty
[16:28:57.115]  [00:00:36.735][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002E (expanded=1)
[16:28:57.116]  [00:00:36.736][detail][DMG] <RE:Run> Cluster 35, Attribute 2f is dirty
[16:28:57.117]  [00:00:36.737][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002F (expanded=1)
[16:28:57.118]  [00:00:36.738][detail][DMG] <RE:Run> Cluster 35, Attribute 30 is dirty
[16:28:57.119]  [00:00:36.739][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0030 (expanded=1)
[16:28:57.120]  [00:00:36.739][detail][DMG] <RE:Run> Cluster 35, Attribute 31 is dirty
[16:28:57.121]  [00:00:36.740][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0031 (expanded=1)
[16:28:57.122]  [00:00:36.741][detail][DMG] <RE:Run> Cluster 35, Attribute 32 is dirty
[16:28:57.123]  [00:00:36.742][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0032 (expanded=1)
[16:28:57.124]  
[16:28:57.125]  [00:00:36.743][detail][DMG] <RE:Run> Cluster 35, Attribute 33 is dirty
[16:28:57.125]  [00:00:36.744][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0033 (expanded=1)
[16:28:57.127]  [00:00:36.745][detail][DMG] <RE:Run> Cluster 35, Attribute 34 is dirty
[16:28:57.127]  [00:00:36.747][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0034 (expanded=1)
[16:28:57.129]  [00:00:36.748][detail][DMG] <RE:Run> Cluster 35, Attribute 35 is dirty
[16:28:57.129]  [00:00:36.749][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0035 (expanded=1)
[16:28:57.131]  [00:00:36.749][detail][DMG] <RE:Run> Cluster 35, Attribute 36 is dirty
[16:28:57.132]  [00:00:36.750][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0036 (expanded=1)
[16:28:57.133]  [00:00:36.750][detail][DMG] <RE:Run> Cluster 35, Attribute 37 is dirty
[16:28:57.134]  [00:00:36.751][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0037 (expanded=1)
[16:28:57.134]  [00:00:36.753][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0038 (expanded=1)
[16:28:57.136]  [00:00:36.754][detail][DMG] <RE:Run> Cluster 35, Attribute 39 is dirty
[16:28:57.136]  [00:00:36.755][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0039 (expanded=1)
[16:28:57.138]  
[16:28:57.138]  [00:00:36.756][detail][DMG] <RE:Run> Cluster 35, Attribute 3a is dirty
[16:28:57.139]  [00:00:36.757][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003A (expanded=1)
[16:28:57.141]  [00:00:36.758][detail][DMG] <RE:Run> Cluster 35, Attribute 3b is dirty
[16:28:57.141]  
[16:28:57.141]  [00:00:36.759][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003B (expanded=1)
[16:28:57.143]  [00:00:36.760][detail][DMG] <RE:Run> Cluster 35, Attribute 3c is dirty
[16:28:57.143]  [00:00:36.761][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003C (expanded=1)
[16:28:57.145]  [00:00:36.762][detail][DMG] <RE:Run> Cluster 35, Attribute 3d is dirty
[16:28:57.145]  [00:00:36.763][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003D (expanded=1)
[16:28:57.147]  [00:00:36.764][detail][DMG] <RE:Run> Cluster 35, Attribute 3e is dirty
[16:28:57.147]  [00:00:36.765][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003E (expanded=1)
[16:28:57.149]  [00:00:36.767][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:28:57.150]  
[16:28:57.150]  [00:00:36.768][detail][DMG] <RE:Run> Cluster 35, Attribute fffd is dirty
[16:28:57.151]  [00:00:36.769][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:28:57.152]  [00:00:36.770][detail][DMG] <RE:Run> Cluster 35, Attribute fff9 is dirty
[16:28:57.153]  [00:00:36.771][detail][DMG] <RE:Run> Cluster 35, Attribute fffb is dirty
[16:28:57.154]  [00:00:36.774][detail][DMG] <RE> Sending report (payload has 928 bytes)...
[16:28:57.154]  [00:00:36.776][info  ][EM] <<< [E:1179r S:15299 M:137613958 (Ack:80708172)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:962)
[16:28:57.157]  [00:00:36.777][info  ][EM] ??1 [E:1179r S:15299 M:137613958] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3331ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:57.159]  [00:00:36.778][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:57.160]  [00:00:36.778][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:57.161]  [00:00:36.778][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:57.585]  [00:00:37.212][detail][IN] UDP Message Received packet nb : 42 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:57.586]  [00:00:37.214][info  ][EM] >>> [E:1179r S:15299 M:80708173 (Ack:137613958)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:57.588]  [00:00:37.214][detail][EM] Found matching exchange: 1179r, Delegate: 0
[16:28:57.590]  [00:00:37.214][detail][EM] Rxd Ack; Removing MessageCounter:137613958 from Retrans Table on exchange 1179r
[16:28:58.600]  [00:00:38.227][detail][IN] UDP Message Received packet nb : 43 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 83
[16:28:58.601]  [00:00:38.229][info  ][EM] >>> [E:1180r S:15299 M:80708174] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:03 (IM:SubscribeRequest) (B:83)
[16:28:58.604]  [00:00:38.230][detail][EM] Handling via exchange: 1180r, Delegate: 0x2000413c
[16:28:58.604]  [00:00:38.230][detail][IM] Received Subscribe request
[16:28:58.605]  [00:00:38.231][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[16:28:58.614]  [00:00:38.242][info  ][DMG] Subscription id 0xea8231cb from node <8CBDA24D2F21C48C, 1> torn down
[16:28:58.615]  [00:00:38.242][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:58.620]  [00:00:38.248][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[16:28:58.621]  [00:00:38.248][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:58.632]  [00:00:38.259][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:58.633]  [00:00:38.260][detail][DMG] <RE:Run> Cluster 102, Attribute e is dirty
[16:28:58.634]  [00:00:38.261][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000E (expanded=1)
[16:28:58.635]  [00:00:38.262][detail][DMG] <RE:Run> Cluster 102, Attribute e is dirty
[16:28:58.636]  [00:00:38.262][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000E (expanded=1)
[16:28:58.638]  [00:00:38.264][detail][DMG] <RE:Run> Cluster 102, Attribute a is dirty
[16:28:58.638]  [00:00:38.264][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000A (expanded=1)
[16:28:58.640]  [00:00:38.266][detail][DMG] <RE:Run> Cluster 102, Attribute a is dirty
[16:28:58.640]  [00:00:38.266][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000A (expanded=1)
[16:28:58.642]  [00:00:38.268][detail][DMG] <RE:Run> Cluster 28, Attribute 9 is dirty
[16:28:58.642]  [00:00:38.269][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:28:58.644]  [00:00:38.271][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:28:58.645]  [00:00:38.272][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:28:58.646]  [00:00:38.273][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:28:58.647]  [00:00:38.273][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:28:58.647]  [00:00:38.275][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:28:58.649]  [00:00:38.275][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:28:58.649]  [00:00:38.276][detail][DMG] <RE> Sending report (payload has 226 bytes)...
[16:28:58.651]  [00:00:38.278][info  ][EM] <<< [E:1180r S:15299 M:137613959 (Ack:80708174)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:260)
[16:28:58.653]  [00:00:38.279][info  ][EM] ??1 [E:1180r S:15299 M:137613959] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3360ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:58.655]  [00:00:38.279][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:28:58.656]  [00:00:38.279][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:28:58.657]  [00:00:38.280][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:58.659]  
[16:28:58.660]  [00:00:38.288][detail][IN] UDP Message Received packet nb : 44 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 49
[16:28:58.661]  [00:00:38.290][info  ][EM] >>> [E:1181r S:15299 M:80708175] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:49)
[16:28:58.663]  [00:00:38.290][detail][EM] Handling via exchange: 1181r, Delegate: 0x2000413c
[16:28:58.664]  [00:00:38.290][detail][IM] Received Read request
[16:28:58.665]  [00:00:38.291][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:58.665]  [00:00:38.291][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:58.667]  [00:00:38.291][detail][DMG] <RE:Run> Cluster 2f, Attribute fffb is dirty
[16:28:58.668]  [00:00:38.294][detail][DMG] <RE> Sending report (payload has 70 bytes)...
[16:28:58.669]  [00:00:38.296][info  ][EM] <<< [E:1181r S:15299 M:137613960 (Ack:80708175)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:104)
[16:28:58.671]  [00:00:38.297][info  ][EM] ??1 [E:1181r S:15299 M:137613960] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3389ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:58.673]  [00:00:38.297][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:28:58.674]  [00:00:38.297][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has no more messages
[16:28:58.675]  [00:00:38.298][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:58.676]  [00:00:38.298][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:59.129]  [00:00:38.756][detail][IN] UDP Message Received packet nb : 45 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 42
[16:28:59.130]  [00:00:38.758][info  ][EM] >>> [E:1180r S:15299 M:80708176 (Ack:137613959)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:28:59.132]  [00:00:38.758][detail][EM] Found matching exchange: 1180r, Delegate: 0x20005dd0
[16:28:59.134]  [00:00:38.759][detail][EM] Rxd Ack; Removing MessageCounter:137613959 from Retrans Table on exchange 1180r
[16:28:59.134]  [00:00:38.759][info  ][IM] Received status response, status is 0x00
[16:28:59.135]  [00:00:38.761][info  ][EM] <<< [E:1180r S:15299 M:137613961 (Ack:80708176)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:28:59.138]  [00:00:38.762][info  ][EM] ??1 [E:1180r S:15299 M:137613961] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3378ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:59.140]  [00:00:38.762][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000976A and system Timestamp 0x000000000009BF2A.
[16:28:59.141]  [00:00:38.763][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:59.142]  [00:00:38.763][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:59.152]  [00:00:38.779][detail][IN] UDP Message Received packet nb : 46 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:59.153]  [00:00:38.781][info  ][EM] >>> [E:1181r S:15299 M:80708177 (Ack:137613960)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:59.155]  [00:00:38.781][detail][EM] Found matching exchange: 1181r, Delegate: 0
[16:28:59.156]  [00:00:38.781][detail][EM] Rxd Ack; Removing MessageCounter:137613960 from Retrans Table on exchange 1181r
[16:28:59.201]  [00:00:38.829][detail][IN] UDP Message Received packet nb : 47 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 74
[16:28:59.202]  [00:00:38.831][info  ][EM] >>> [E:1182r S:15299 M:80708178] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:06 (IM:WriteRequest) (B:74)
[16:28:59.205]  [00:00:38.831][detail][EM] Handling via exchange: 1182r, Delegate: 0x2000413c
[16:28:59.205]  [00:00:38.832][detail][IM] Received Write request
[16:28:59.206]  [00:00:38.832][detail][DMG] IM WH moving to [Initialized]
[16:28:59.207]  [00:00:38.833][detail][DMG] Writing attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005
[16:28:59.208]  [00:00:38.833][detail][DMG] IM WH moving to [AddStatus]
[16:28:59.209]  [00:00:38.836][info  ][EM] <<< [E:1182r S:15299 M:137613962 (Ack:80708178)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:07 (IM:WriteResponse) (B:62)
[16:28:59.211]  [00:00:38.837][info  ][EM] ??1 [E:1182r S:15299 M:137613962] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3407ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:59.213]  [00:00:38.838][detail][DMG] IM WH moving to [Sending]
[16:28:59.214]  [00:00:38.838][detail][DMG] IM WH moving to [Uninitialized]
[16:28:59.232]  [00:00:38.860][detail][IN] UDP Message Received packet nb : 48 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 49
[16:28:59.234]  [00:00:38.862][info  ][EM] >>> [E:1183r S:15299 M:80708179] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:02 (IM:ReadRequest) (B:49)
[16:28:59.236]  [00:00:38.862][detail][EM] Handling via exchange: 1183r, Delegate: 0x2000413c
[16:28:59.237]  [00:00:38.863][detail][IM] Received Read request
[16:28:59.237]  [00:00:38.863][detail][DMG] IM RH moving to [CanStartReporting]
[16:28:59.238]  [00:00:38.864][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:28:59.239]  [00:00:38.865][detail][DMG] <RE:Run> Cluster 2f, Attribute fffb is dirty
[16:28:59.241]  [00:00:38.867][detail][DMG] <RE> Sending report (payload has 70 bytes)...
[16:28:59.242]  [00:00:38.870][info  ][EM] <<< [E:1183r S:15299 M:137613963 (Ack:80708179)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:104)
[16:28:59.244]  [00:00:38.871][info  ][EM] ??1 [E:1183r S:15299 M:137613963] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3365ms from now [State:Active II:500 AI:300 AT:4000]
[16:28:59.246]  [00:00:38.871][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:28:59.247]  [00:00:38.871][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:28:59.248]  [00:00:38.871][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:28:59.248]  [00:00:38.872][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:28:59.269]  [00:00:38.897][detail][IN] UDP Message Received packet nb : 49 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:59.271]  [00:00:38.898][info  ][EM] >>> [E:1180r S:15299 M:80708180 (Ack:137613961)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:59.273]  [00:00:38.899][detail][EM] Found matching exchange: 1180r, Delegate: 0
[16:28:59.274]  [00:00:38.899][detail][EM] Rxd Ack; Removing MessageCounter:137613961 from Retrans Table on exchange 1180r
[16:28:59.309]  [00:00:38.937][detail][IN] UDP Message Received packet nb : 50 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:59.310]  [00:00:38.939][info  ][EM] >>> [E:1182r S:15299 M:80708181 (Ack:137613962)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:59.313]  [00:00:38.939][detail][EM] Found matching exchange: 1182r, Delegate: 0
[16:28:59.314]  [00:00:38.939][detail][EM] Rxd Ack; Removing MessageCounter:137613962 from Retrans Table on exchange 1182r
[16:28:59.799]  [00:00:39.426][detail][IN] UDP Message Received packet nb : 51 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:28:59.800]  [00:00:39.428][info  ][EM] >>> [E:1183r S:15299 M:80708182 (Ack:137613963)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:28:59.802]  [00:00:39.428][detail][EM] Found matching exchange: 1183r, Delegate: 0
[16:28:59.804]  [00:00:39.428][detail][EM] Rxd Ack; Removing MessageCounter:137613963 from Retrans Table on exchange 1183r
[16:29:00.655]  
[16:29:01.025]  [00:00:40.653][detail][IN] UDP Message Received packet nb : 52 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 91
[16:29:01.026]  [00:00:40.655][info  ][EM] >>> [E:1184r S:15299 M:80708183] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:03 (IM:SubscribeRequest) (B:91)
[16:29:01.029]  [00:00:40.656][detail][EM] Handling via exchange: 1184r, Delegate: 0x2000413c
[16:29:01.029]  [00:00:40.656][detail][IM] Received Subscribe request
[16:29:01.030]  [00:00:40.657][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[16:29:01.040]  [00:00:40.668][info  ][DMG] Subscription id 0xfe5691ef from node <8CBDA24D2F21C48C, 1> torn down
[16:29:01.041]  [00:00:40.668][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:29:01.046]  [00:00:40.674][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[16:29:01.047]  [00:00:40.675][detail][DMG] IM RH moving to [CanStartReporting]
[16:29:01.058]  [00:00:40.686][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:29:01.060]  [00:00:40.688][detail][DMG] <RE:Run> Cluster 102, Attribute e is dirty
[16:29:01.060]  [00:00:40.688][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000E (expanded=1)
[16:29:01.062]  [00:00:40.689][detail][DMG] <RE:Run> Cluster 102, Attribute e is dirty
[16:29:01.062]  [00:00:40.690][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000E (expanded=1)
[16:29:01.064]  [00:00:40.691][detail][DMG] <RE:Run> Cluster 102, Attribute a is dirty
[16:29:01.065]  [00:00:40.692][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000A (expanded=1)
[16:29:01.066]  [00:00:40.693][detail][DMG] <RE:Run> Cluster 102, Attribute a is dirty
[16:29:01.067]  [00:00:40.693][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000A (expanded=1)
[16:29:01.068]  [00:00:40.695][detail][DMG] <RE:Run> Cluster 2f, Attribute e is dirty
[16:29:01.069]  [00:00:40.696][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:29:01.070]  [00:00:40.698][detail][DMG] <RE:Run> Cluster 28, Attribute 9 is dirty
[16:29:01.071]  [00:00:40.699][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:29:01.073]  [00:00:40.702][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:29:01.074]  [00:00:40.702][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:29:01.075]  [00:00:40.703][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:29:01.076]  [00:00:40.704][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:29:01.077]  [00:00:40.705][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:29:01.077]  [00:00:40.705][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:29:01.079]  [00:00:40.706][detail][DMG] <RE> Sending report (payload has 252 bytes)...
[16:29:01.080]  [00:00:40.708][info  ][EM] <<< [E:1184r S:15299 M:137613964 (Ack:80708183)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:286)
[16:29:01.082]  [00:00:40.708][info  ][EM] ??1 [E:1184r S:15299 M:137613964] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3383ms from now [State:Active II:500 AI:300 AT:4000]
[16:29:01.084]  [00:00:40.709][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:29:01.085]  [00:00:40.709][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:29:01.086]  [00:00:40.709][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:29:01.546]  [00:00:41.174][detail][IN] UDP Message Received packet nb : 53 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 42
[16:29:01.548]  [00:00:41.176][info  ][EM] >>> [E:1184r S:15299 M:80708184 (Ack:137613964)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:29:01.550]  [00:00:41.176][detail][EM] Found matching exchange: 1184r, Delegate: 0x20005dd0
[16:29:01.551]  [00:00:41.177][detail][EM] Rxd Ack; Removing MessageCounter:137613964 from Retrans Table on exchange 1184r
[16:29:01.552]  [00:00:41.177][info  ][IM] Received status response, status is 0x00
[16:29:01.553]  [00:00:41.179][info  ][EM] <<< [E:1184r S:15299 M:137613965 (Ack:80708184)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:29:01.555]  [00:00:41.180][info  ][EM] ??1 [E:1184r S:15299 M:137613965] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3337ms from now [State:Active II:500 AI:300 AT:4000]
[16:29:01.558]  [00:00:41.180][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000A0DC and system Timestamp 0x000000000009C89C.
[16:29:01.559]  [00:00:41.181][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:29:01.560]  [00:00:41.181][detail][DMG] IM RH moving to [CanStartReporting]
[16:29:02.034]  [00:00:41.663][detail][IN] UDP Message Received packet nb : 54 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:29:02.036]  [00:00:41.664][info  ][EM] >>> [E:1184r S:15299 M:80708185 (Ack:137613965)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:29:02.038]  [00:00:41.665][detail][EM] Found matching exchange: 1184r, Delegate: 0
[16:29:02.039]  [00:00:41.665][detail][EM] Rxd Ack; Removing MessageCounter:137613965 from Retrans Table on exchange 1184r
//Operation
[16:29:19.011]  [00:00:58.639][error ][SWU] No suitable OTA Provider candidate found
[16:29:19.012]  [00:00:58.639][info  ][SWU] No provider available
[16:29:23.043]  [00:01:02.671][detail][IN] UDP Message Received packet nb : 55 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 67
[16:29:23.044]  [00:01:02.673][info  ][EM] >>> [E:1185r S:15299 M:80708186] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:08 (IM:InvokeCommandRequest) (B:67)
[16:29:23.046]  [00:01:02.673][detail][EM] Handling via exchange: 1185r, Delegate: 0x2000413c
[16:29:23.047]  [00:01:02.675][detail][DMG] Received command for Endpoint=1 Cluster=0x0000_0102 Command=0x0000_0005
[16:29:23.048]  [00:01:02.675][info  ][ZCL] GoToLiftPercentage 5400 command received
[16:29:23.049]  [00:01:02.676][detail][DMG] Endpoint 1, Cluster 0x0000_0102 update version to 6e06781f
[16:29:23.050]  [00:01:02.676][info  ][ZCL] WindowCovering has no delegate set for endpoint:1
[16:29:23.051]  [00:01:02.676][detail][DMG] Command handler moving to [NewRespons]
[16:29:23.052]  [00:01:02.677][detail][DMG] Command handler moving to [ Preparing]
[16:29:23.052]  [00:01:02.677][detail][DMG] Command handler moving to [AddingComm]
[16:29:23.053]  [00:01:02.677][detail][DMG] Command handler moving to [AddedComma]
[16:29:23.054]  [00:01:02.678][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:29:23.055]  [00:01:02.678][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:29:23.056]  [00:01:02.678][detail][DMG] Command handler moving to [AwaitingDe]
[16:29:23.057]  [00:01:02.680][info  ][EM] <<< [E:1185r S:15299 M:137613966 (Ack:80708186)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:71)
[16:29:23.059]  [00:01:02.681][info  ][EM] ??1 [E:1185r S:15299 M:137613966] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3345ms from now [State:Active II:500 AI:300 AT:4000]
[16:29:23.061]  [00:01:02.682][detail][DMG] Command response sender moving to [AllInvokeR]
[16:29:23.062]  [00:01:02.683][silabs ]WDC: Invalid wdc endpoint 1
[16:29:23.541]  [00:01:03.168][detail][IN] UDP Message Received packet nb : 56 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:29:23.542]  [00:01:03.170][info  ][EM] >>> [E:1185r S:15299 M:80708187 (Ack:137613966)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:29:23.544]  [00:01:03.170][detail][EM] Found matching exchange: 1185r, Delegate: 0
[16:29:23.546]  [00:01:03.170][detail][EM] Rxd Ack; Removing MessageCounter:137613966 from Retrans Table on exchange 1185r
[16:29:24.655]  
[16:29:26.656]  
[16:29:28.656]  
[16:29:29.532]  [00:01:09.160][detail][IN] UDP Message Received packet nb : 57 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 63
[16:29:29.533]  [00:01:09.162][info  ][EM] >>> [E:1186r S:15299 M:80708188] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:08 (IM:InvokeCommandRequest) (B:63)
[16:29:29.535]  [00:01:09.163][detail][EM] Handling via exchange: 1186r, Delegate: 0x2000413c
[16:29:29.536]  [00:01:09.164][detail][DMG] Received command for Endpoint=1 Cluster=0x0000_0102 Command=0x0000_0001
[16:29:29.537]  [00:01:09.164][info  ][ZCL] DownOrClose command received
[16:29:29.538]  [00:01:09.164][detail][DMG] Endpoint 1, Cluster 0x0000_0102 update version to 6e067820
[16:29:29.539]  [00:01:09.165][detail][DMG] Command handler moving to [NewRespons]
[16:29:29.539]  [00:01:09.165][detail][DMG] Command handler moving to [ Preparing]
[16:29:29.540]  [00:01:09.165][detail][DMG] Command handler moving to [AddingComm]
[16:29:29.541]  [00:01:09.165][detail][DMG] Command handler moving to [AddedComma]
[16:29:29.542]  [00:01:09.165][info  ][ZCL] WindowCovering has no delegate set for endpoint:1
[16:29:29.543]  [00:01:09.166][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:29:29.543]  [00:01:09.166][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:29:29.545]  [00:01:09.166][detail][DMG] Command handler moving to [AwaitingDe]
[16:29:29.546]  [00:01:09.167][info  ][EM] <<< [E:1186r S:15299 M:137613967 (Ack:80708188)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:71)
[16:29:29.548]  [00:01:09.168][info  ][EM] ??1 [E:1186r S:15299 M:137613967] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3341ms from now [State:Active II:500 AI:300 AT:4000]
[16:29:29.550]  [00:01:09.169][detail][DMG] Command response sender moving to [AllInvokeR]
[16:29:29.550]  [00:01:09.169][silabs ]WDC: Invalid wdc endpoint 1
[16:29:30.039]  [00:01:09.666][detail][IN] UDP Message Received packet nb : 58 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:29:30.040]  [00:01:09.667][info  ][EM] >>> [E:1186r S:15299 M:80708189 (Ack:137613967)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:29:30.042]  [00:01:09.668][detail][EM] Found matching exchange: 1186r, Delegate: 0
[16:29:30.043]  [00:01:09.668][detail][EM] Rxd Ack; Removing MessageCounter:137613967 from Retrans Table on exchange 1186r
[16:29:30.655]  
[16:29:32.655]  
[16:29:34.037]  [00:01:13.666][detail][IN] UDP Message Received packet nb : 59 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 63
[16:29:34.039]  [00:01:13.667][info  ][EM] >>> [E:1187r S:15299 M:80708190] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0001:08 (IM:InvokeCommandRequest) (B:63)
[16:29:34.041]  [00:01:13.667][detail][EM] Handling via exchange: 1187r, Delegate: 0x2000413c
[16:29:34.042]  [00:01:13.668][detail][DMG] Received command for Endpoint=1 Cluster=0x0000_0102 Command=0x0000_0000
[16:29:34.043]  [00:01:13.669][info  ][ZCL] UpOrOpen command received
[16:29:34.044]  [00:01:13.669][detail][DMG] Endpoint 1, Cluster 0x0000_0102 update version to 6e067821
[16:29:34.044]  [00:01:13.669][info  ][ZCL] WindowCovering has no delegate set for endpoint:1
[16:29:34.045]  [00:01:13.669][detail][DMG] Command handler moving to [NewRespons]
[16:29:34.046]  [00:01:13.670][detail][DMG] Command handler moving to [ Preparing]
[16:29:34.047]  [00:01:13.670][detail][DMG] Command handler moving to [AddingComm]
[16:29:34.048]  [00:01:13.670][detail][DMG] Command handler moving to [AddedComma]
[16:29:34.049]  [00:01:13.670][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:29:34.049]  [00:01:13.671][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:29:34.051]  [00:01:13.671][detail][DMG] Command handler moving to [AwaitingDe]
[16:29:34.051]  [00:01:13.673][info  ][EM] <<< [E:1187r S:15299 M:137613968 (Ack:80708190)] (S) Msg TX from 0724338E7B78E61C to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:71)
[16:29:34.053]  [00:01:13.674][info  ][EM] ??1 [E:1187r S:15299 M:137613968] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3353ms from now [State:Active II:500 AI:300 AT:4000]
[16:29:34.055]  [00:01:13.674][detail][DMG] Command response sender moving to [AllInvokeR]
[16:29:34.056]  [00:01:13.675][silabs ]WDC: Invalid wdc endpoint 1
[16:29:34.536]  [00:01:14.164][detail][IN] UDP Message Received packet nb : 60 SrcAddr : fddc:8360:97e9:1:8174:a1c6:1ab8:5e81[42257] DestAddr : fddc:8360:97e9:1:d259:da37:4937:b266[5540] Payload Length 34
[16:29:34.538]  [00:01:14.166][info  ][EM] >>> [E:1187r S:15299 M:80708191 (Ack:137613968)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to 0724338E7B78E61C --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:29:34.540]  [00:01:14.166][detail][EM] Found matching exchange: 1187r, Delegate: 0
[16:29:34.541]  [00:01:14.166][detail][EM] Rxd Ack; Removing MessageCounter:137613968 from Retrans Table on exchange 1187r
 
```