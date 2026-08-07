```c
[16:26:12.911]  device factoryreset
[16:26:12.915]  Performing factory reset ... 
[16:26:12.915]  Done
[16:26:12.915]  [00:02:31.268][info  ][DL] Performing factory reset
[16:26:13.392]  [00:02:31.745][detail][DL] SRP update succeeded
[16:26:13.392]  [00:02:31.745][info  ][DL] Clearing Thread provision
[16:26:13.393]  [00:02:31.745][info  ][DL] Erasing Thread persistent info...
[16:26:13.421]  [00:02:31.773][info  ][DL] System restarting
[16:26:14.150]  [00:00:00.068][info  ][DL] Starting scheduler
[16:26:14.151]  [00:00:00.068][info  ][DL] ==================================================
[16:26:14.151]  [00:00:00.068][info  ][DL]  starting
[16:26:14.151]  [00:00:00.068][info  ][DL] ==================================================
[16:26:14.153]  [00:00:00.068][info  ][DL] Init CHIP Stack
[16:26:14.153]  [00:00:00.070][info  ][DL] Provision mode disabled
[16:26:14.153]  [00:00:00.070][info  ][DL] Initializing OpenThread stack
[16:26:14.154]  [00:00:00.071][info  ][DL] OpenThread started: OK
[16:26:14.155]  [00:00:00.071][info  ][DL] Setting OpenThread device type to SLEEPY END DEVICE
[16:26:14.162]  [00:00:00.133][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[16:26:14.162]  [00:00:00.133][info  ][DL] RAIL version:, v3.0.0-b0
[16:26:14.162]  [00:00:00.133][silabs ]BLE: product type [Pergolux]
[16:26:14.163]  [00:00:00.134][silabs ]BLE: identify addr: D2:60:9E:6A:74:E1 type=1
[16:26:14.164]  [00:00:00.135][silabs ]BLE: MTU size 249
[16:26:14.165]  [00:00:00.135][detail][DL] CHIP event task running
[16:26:14.165]  [00:00:00.136][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:26:14.166]  [00:00:00.136][detail][DL] OpenThread State Changed (Flags: 0x00038210)
[16:26:14.167]  [00:00:00.136][detail][DL]    Network Name: OpenThread
[16:26:14.167]  [00:00:00.137][detail][DL]    PAN Id: 0xFFFF
[16:26:14.168]  [00:00:00.137][detail][DL]    Extended PAN Id: 0xDEAD00BEEF00CAFE
[16:26:14.169]  [00:00:00.137][detail][DL]    Channel: 11 
[16:26:14.169]  [00:00:00.137][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64
[16:26:14.170]  [00:00:00.138][info  ][SVR] Current Software Version String: 0.9.7 
[16:26:14.171]  [00:00:00.138][info  ][SVR] Current Software Version: 97
[16:26:14.172]  [00:00:00.138][info  ][DL] Device Configuration:
[16:26:14.172]  [00:00:00.139][info  ][DL]   Serial Number: 38398FFFFE520BF5
[16:26:14.173]  [00:00:00.139][info  ][DL]   Vendor Id: 65521 (0xFFF1)
[16:26:14.174]  [00:00:00.139][info  ][DL]   Product Id: 32784 (0x8010)
[16:26:14.174]  [00:00:00.139][info  ][DL]   Product Name: SL_Sample
[16:26:14.175]  [00:00:00.140][info  ][DL]   Hardware Version: 1
[16:26:14.176]  [00:00:00.140][info  ][DL]   Manufacturing Date: (not set)
[16:26:14.176]  [00:00:00.141][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[16:26:14.177]  [00:00:00.142][silabs ]Ver: 97 Btl: 0x03000001 Time:Feb  7 2026 16:21:38
[16:26:14.184]  [00:00:00.155][info  ][DL] Configuring BLE Channel
[16:26:14.184]  [00:00:00.156][detail][DL] BLE Static Device Address E6:DE:2F:C2:CD:24
[16:26:14.184]  [00:00:00.156][silabs ]BLE: _create_second_adv, adv Handle = 0
[16:26:14.185]  [00:00:00.157][silabs ]BLE: advertiser start
[16:26:14.187]  [00:00:00.159][silabs ]COM: Init done
[16:26:14.187]  [00:00:00.159][silabs ]NWK: open basic commissioning window time 300 sec
[16:26:14.189]  [00:00:00.160][detail][IN] SecureSession[0x20007030]: Allocated Type:1 LSID:25600
[16:26:14.189]  [00:00:00.161][detail][SC] Assigned local session key ID 25600
[16:26:14.190]  [00:00:00.161][detail][SC] Waiting for PBKDF param request
[16:26:14.191]  [00:00:00.161][info  ][DIS] Updating services using commissioning mode 1
[16:26:14.191]  [00:00:00.161][error ][DIS] Failed to remove advertised services: 3
[16:26:14.192]  [00:00:00.161][detail][DL] Using Thread extended MAC for hostname.
[16:26:14.193]  [00:00:00.162][detail][DIS] DNS-SD Pairing Instruction not set
[16:26:14.194]  [00:00:00.162][info  ][DIS] Advertise commission parameter vendorID=65521 productID=32784 discriminator=3840/15 cm=1 cp=0 jf=0  
[16:26:14.195]  [00:00:00.162][error ][DIS] Failed to advertise commissionable node: 3
[16:26:14.196]  [00:00:00.162][error ][DIS] Failed to finalize service update: 3
[16:26:14.196]  [00:00:00.163][detail][DL] Start BLE advertisement
[16:26:14.197]  [00:00:00.163][detail][DL] BLE Static Device Address C0:AD:37:EF:2A:08
[16:26:14.198]  [00:00:00.164][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[16:26:14.199]  [00:00:00.165][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:26:14.200]  [00:00:00.165][silabs ]NWK: platform event type 800d
[16:26:14.201]  [00:00:00.166][silabs ]COM: notify network [Leave]
[16:26:14.201]  [00:00:00.166][silabs ]App Task started
[16:26:23.366]  [00:00:09.337][info  ][DL] Connect Event for CHIPoBLE on handle : 2
[16:26:23.366]  [00:00:09.338][info  ][DL] Connection Parameters Event for handle : 2
[16:26:23.367]  [00:00:09.338][info  ][DL] Connection parameter ID received - i:24, l:0, t:72, sm:0
[16:26:23.368]  [00:00:09.338][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:100
[16:26:23.369]  [00:00:09.339][info  ][DL] Connection phy status ID received - phy:1
[16:26:23.526]  [00:00:09.498][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:251, rxL:2120
[16:26:23.826]  [00:00:09.797][info  ][DL] Connection Parameters Event for handle : 2
[16:26:23.826]  [00:00:09.798][info  ][DL] Connection parameter ID received - i:72, l:0, t:100, sm:0
[16:26:24.425]  [00:00:10.397][info  ][DL] Handling CCCD Write
[16:26:24.425]  [00:00:10.397][error ][-] mConnectionState.allocated:430 false: 3
[16:26:24.425]  [00:00:10.397][error ][-] Error CHIP:0x00000003 at C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:303
[16:26:24.785]  [00:00:10.756][info  ][DL] Char Write Req, char : 47
[16:26:24.785]  [00:00:10.757][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 9)
[16:26:24.787]  [00:00:10.757][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:24.787]  [00:00:10.757][info  ][BLE] local and remote recv window sizes = 5
[16:26:24.788]  [00:00:10.757][info  ][BLE] selected BTP version 4
[16:26:24.789]  [00:00:10.757][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[16:26:25.235]  [00:00:11.207][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[16:26:25.235]  [00:00:11.207][info  ][DL] CHIPoBLE subscribe received
[16:26:25.236]  [00:00:11.208][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[16:26:25.237]  [00:00:11.209][detail][IN] BLE EndPoint 0x20012a2c Connection Complete
[16:26:25.238]  [00:00:11.210][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[16:26:25.239]  [00:00:11.210][silabs ]NWK: platform event type 8006
[16:26:25.239]  [00:00:11.210][silabs ]COM: notify network [Leave]
[16:26:25.415]  [00:00:11.386][info  ][DL] Tx Confirmation received
[16:26:25.415]  [00:00:11.386][info  ][DL]  stop soft timer
[16:26:25.415]  [00:00:11.387][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:25.416]  [00:00:11.388][info  ][DL] Char Write Req, char : 47
[16:26:25.417]  [00:00:11.388][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 103)
[16:26:25.418]  [00:00:11.389][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:25.419]  [00:00:11.389][info  ][EM] >>> [E:4257r S:0 M:203526973] (U) Msg RX from 0:F79A361141070FA1 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[16:26:25.420]  [00:00:11.389][detail][EM] Handling via exchange: 4257r, Delegate: 0x200097b8
[16:26:25.422]  [00:00:11.390][detail][SC] Received PBKDF param request
[16:26:25.422]  [00:00:11.390][detail][SC] Peer assigned session ID 39870
[16:26:25.423]  [00:00:11.390][detail][SC] Found MRP parameters in the message
[16:26:25.424]  [00:00:11.392][info  ][EM] <<< [E:4257r S:0 M:139474074] (U) Msg TX from 0000000000000000 to 0:F79A361141070FA1 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[16:26:25.425]  [00:00:11.393][detail][SC] Sent PBKDF param response
[16:26:25.426]  [00:00:11.393][info  ][SVR] Commissioning session establishment step started
[16:26:25.594]  [00:00:11.567][info  ][DL] Tx Confirmation received
[16:26:25.594]  [00:00:11.567][info  ][DL]  stop soft timer
[16:26:25.595]  [00:00:11.567][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:25.596]  [00:00:11.568][info  ][DL] Char Write Req, char : 47
[16:26:25.596]  [00:00:11.569][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 97)
[16:26:25.598]  [00:00:11.569][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:25.598]  [00:00:11.569][info  ][EM] >>> [E:4257r S:0 M:203526974] (U) Msg RX from 0:F79A361141070FA1 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[16:26:25.600]  [00:00:11.570][detail][EM] Found matching exchange: 4257r, Delegate: 0x200097b8
[16:26:25.601]  [00:00:11.570][detail][SC] Received spake2p msg1
[16:26:25.655]  [00:00:11.626][info  ][EM] <<< [E:4257r S:0 M:139474075] (U) Msg TX from 0000000000000000 to 0:F79A361141070FA1 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[16:26:25.656]  [00:00:11.627][detail][SC] Sent spake2p msg2
[16:26:25.775]  [00:00:11.747][info  ][DL] Tx Confirmation received
[16:26:25.775]  [00:00:11.747][info  ][DL]  stop soft timer
[16:26:25.775]  [00:00:11.747][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:25.776]  [00:00:11.748][info  ][DL] Char Write Req, char : 47
[16:26:25.777]  [00:00:11.749][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 64)
[16:26:25.778]  [00:00:11.749][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:25.779]  [00:00:11.749][info  ][EM] >>> [E:4257r S:0 M:203526975] (U) Msg RX from 0:F79A361141070FA1 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[16:26:25.780]  [00:00:11.750][detail][EM] Found matching exchange: 4257r, Delegate: 0x200097b8
[16:26:25.781]  [00:00:11.750][detail][SC] Received spake2p msg3
[16:26:25.781]  [00:00:11.750][detail][SC] Sending status report. Protocol code 0, exchange 4257
[16:26:25.783]  [00:00:11.750][info  ][EM] <<< [E:4257r S:0 M:139474076] (U) Msg TX from 0000000000000000 to 0:F79A361141070FA1 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[16:26:25.784]  [00:00:11.754][info  ][SC] SecureSession[0x20007030, LSID:25600]: State change 'kEstablishing' --> 'kActive'
[16:26:25.785]  [00:00:11.755][detail][IN] SecureSession[0x20007030]: Activated - Type:1 LSID:25600
[16:26:25.787]  [00:00:11.755][detail][IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:25600 PSID:39870!
[16:26:25.788]  [00:00:11.755][info  ][SVR] Commissioning completed session establishment step
[16:26:25.789]  [00:00:11.755][info  ][DIS] Updating services using commissioning mode 0
[16:26:25.790]  [00:00:11.756][error ][DIS] Failed to remove advertised services: 3
[16:26:25.790]  [00:00:11.756][error ][DIS] Failed to finalize service update: 3
[16:26:25.791]  [00:00:11.756][info  ][SVR] Device completed Rendezvous process
[16:26:25.792]  [00:00:11.756][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:26:25.792]  [00:00:11.756][silabs ]NWK: platform event type 8018
[16:26:25.793]  [00:00:11.757][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:26:25.954]  [00:00:11.926][info  ][DL] Tx Confirmation received
[16:26:25.954]  [00:00:11.926][info  ][DL]  stop soft timer
[16:26:25.955]  [00:00:11.927][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:25.956]  [00:00:11.928][info  ][DL] Char Write Req, char : 47
[16:26:25.956]  [00:00:11.929][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 141)
[16:26:25.958]  [00:00:11.929][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:25.958]  [00:00:11.931][info  ][EM] >>> [E:4258r S:25600 M:193131811] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:136)
[16:26:25.961]  [00:00:11.931][detail][EM] Handling via exchange: 4258r, Delegate: 0x2000413c
[16:26:25.961]  [00:00:11.932][detail][IM] Received Read request
[16:26:25.963]  [00:00:11.936][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:25.964]  [00:00:11.936][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:25.965]  [00:00:11.937][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:26:25.966]  [00:00:11.938][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:26:25.967]  [00:00:11.940][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:26:25.968]  [00:00:11.941][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:26:25.970]  [00:00:11.942][detail][DMG] <RE:Run> Cluster 30, Attribute c is dirty
[16:26:25.973]  [00:00:11.946][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0030, attributeId: 0x0000_000Cerr = 586
[16:26:25.974]  [00:00:11.947][detail][DMG] <RE:Run> Cluster 30, Attribute 3 is dirty
[16:26:25.975]  [00:00:11.948][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:26:25.976]  [00:00:11.949][detail][DMG] <RE:Run> Cluster 30, Attribute 2 is dirty
[16:26:25.977]  [00:00:11.950][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:26:25.979]  [00:00:11.951][detail][DMG] <RE:Run> Cluster 30, Attribute 1 is dirty
[16:26:25.979]  [00:00:11.952][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:26:25.981]  [00:00:11.953][detail][DMG] <RE:Run> Cluster 30, Attribute 0 is dirty
[16:26:25.981]  [00:00:11.954][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:26:25.983]  [00:00:11.955][detail][DMG] <RE:Run> Cluster 30, Attribute 4 is dirty
[16:26:25.983]  [00:00:11.956][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:26:25.984]  [00:00:11.957][detail][DMG] <RE> Sending report (payload has 223 bytes)...
[16:26:25.986]  [00:00:11.958][info  ][EM] <<< [E:4258r S:25600 M:98722564] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:253)
[16:26:25.987]  [00:00:11.959][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:25.988]  [00:00:11.959][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:26:25.990]  [00:00:11.959][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:25.990]  [00:00:11.959][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:26.135]  [00:00:12.107][info  ][DL] Tx Confirmation received
[16:26:26.135]  [00:00:12.107][info  ][DL]  stop soft timer
[16:26:26.136]  [00:00:12.107][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:26.314]  [00:00:12.287][info  ][DL] Tx Confirmation received
[16:26:26.314]  [00:00:12.287][info  ][DL]  stop soft timer
[16:26:26.315]  [00:00:12.287][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:26.316]  [00:00:12.289][info  ][DL] Char Write Req, char : 47
[16:26:26.317]  [00:00:12.289][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 133)
[16:26:26.318]  [00:00:12.289][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:26.319]  [00:00:12.291][info  ][EM] >>> [E:4259r S:25600 M:193131812] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:128)
[16:26:26.321]  [00:00:12.291][detail][EM] Handling via exchange: 4259r, Delegate: 0x2000413c
[16:26:26.322]  [00:00:12.291][detail][IM] Received Read request
[16:26:26.323]  [00:00:12.295][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:26.324]  [00:00:12.295][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:26.325]  [00:00:12.296][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.326]  [00:00:12.297][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.328]  [00:00:12.298][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.328]  [00:00:12.298][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.330]  [00:00:12.299][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.330]  [00:00:12.299][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.332]  [00:00:12.300][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.332]  [00:00:12.301][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.334]  [00:00:12.301][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.334]  [00:00:12.302][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.336]  [00:00:12.303][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:26.337]  [00:00:12.303][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:26:26.338]  [00:00:12.304][detail][DMG] <RE:Run> Cluster 46, Attribute 2 is dirty
[16:26:26.339]  [00:00:12.305][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:26:26.339]  [00:00:12.306][detail][DMG] <RE:Run> Cluster 46, Attribute 1 is dirty
[16:26:26.341]  [00:00:12.307][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:26:26.341]  [00:00:12.308][detail][DMG] <RE:Run> Cluster 46, Attribute 0 is dirty
[16:26:26.343]  [00:00:12.309][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:26:26.343]  [00:00:12.311][detail][DMG] <RE:Run> Cluster 46, Attribute 7 is dirty
[16:26:26.344]  [00:00:12.312][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0007err = 586
[16:26:26.346]  [00:00:12.313][detail][DMG] <RE:Run> Cluster 46, Attribute 6 is dirty
[16:26:26.347]  [00:00:12.315][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0006err = 586
[16:26:26.348]  [00:00:12.316][detail][DMG] <RE:Run> Cluster 31, Attribute 2 is dirty
[16:26:26.349]  [00:00:12.317][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:26.350]  [00:00:12.319][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[16:26:26.351]  [00:00:12.320][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.352]  [00:00:12.321][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[16:26:26.353]  [00:00:12.322][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:26.355]  [00:00:12.324][detail][DMG] <RE> Sending report (payload has 439 bytes)...
[16:26:26.355]  [00:00:12.326][info  ][EM] <<< [E:4259r S:25600 M:98722565] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:469)
[16:26:26.357]  [00:00:12.327][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:26.358]  [00:00:12.327][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:26:26.359]  [00:00:12.327][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:26.359]  [00:00:12.327][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:26.495]  [00:00:12.466][info  ][DL] Tx Confirmation received
[16:26:26.495]  [00:00:12.467][info  ][DL]  stop soft timer
[16:26:26.496]  [00:00:12.467][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:26.764]  [00:00:12.737][info  ][DL] Tx Confirmation received
[16:26:26.764]  [00:00:12.737][info  ][DL]  stop soft timer
[16:26:26.765]  [00:00:12.737][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:26.766]  [00:00:12.738][info  ][DL] Char Write Req, char : 47
[16:26:26.766]  [00:00:12.739][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 86)
[16:26:26.768]  [00:00:12.739][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:26.769]  [00:00:12.741][info  ][EM] >>> [E:4260r S:25600 M:193131813] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:81)
[16:26:26.770]  [00:00:12.742][detail][EM] Handling via exchange: 4260r, Delegate: 0x2000413c
[16:26:26.771]  [00:00:12.742][detail][IM] Received Read request
[16:26:26.771]  [00:00:12.744][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:26.772]  [00:00:12.744][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:26.774]  [00:00:12.745][detail][DMG] <RE:Run> Cluster 31, Attribute 1 is dirty
[16:26:26.775]  [00:00:12.746][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:26.776]  [00:00:12.748][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[16:26:26.777]  [00:00:12.748][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:26:26.778]  [00:00:12.750][detail][DMG] <RE:Run> Cluster 1349fc00, Attribute 1 is dirty
[16:26:26.779]  [00:00:12.750][error ][DMG] Read request on unknown cluster - no data version available
[16:26:26.780]  [00:00:12.750][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x1349_FC00, attributeId: 0x0000_0001err = 5c3
[16:26:26.781]  [00:00:12.752][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.782]  [00:00:12.752][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.783]  [00:00:12.753][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.784]  [00:00:12.754][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.785]  [00:00:12.755][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.786]  [00:00:12.755][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.787]  [00:00:12.756][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.788]  [00:00:12.756][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.789]  [00:00:12.757][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.790]  [00:00:12.757][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.791]  [00:00:12.758][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:26.792]  [00:00:12.758][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0003 (expanded=1)
[16:26:26.794]  [00:00:12.759][detail][DMG] <RE> Sending report (payload has 295 bytes)...
[16:26:26.794]  [00:00:12.761][info  ][EM] <<< [E:4260r S:25600 M:98722566] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:325)
[16:26:26.796]  [00:00:12.762][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:26.797]  [00:00:12.762][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:26:26.798]  [00:00:12.762][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:26.798]  [00:00:12.762][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:26.945]  [00:00:12.916][info  ][DL] Tx Confirmation received
[16:26:26.945]  [00:00:12.916][info  ][DL]  stop soft timer
[16:26:26.946]  [00:00:12.917][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:27.125]  [00:00:13.097][info  ][DL] Tx Confirmation received
[16:26:27.125]  [00:00:13.097][info  ][DL]  stop soft timer
[16:26:27.126]  [00:00:13.097][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:27.215]  [00:00:13.187][info  ][DL] Char Write Req, char : 47
[16:26:27.215]  [00:00:13.188][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:26:27.216]  [00:00:13.188][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:27.217]  [00:00:13.190][info  ][EM] >>> [E:4261r S:25600 M:193131814] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:26:27.219]  [00:00:13.190][detail][EM] Handling via exchange: 4261r, Delegate: 0x2000413c
[16:26:27.220]  [00:00:13.192][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:26:27.221]  [00:00:13.192][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[16:26:27.222]  [00:00:13.192][detail][DMG] Command handler moving to [NewRespons]
[16:26:27.223]  [00:00:13.192][detail][DMG] Command handler moving to [ Preparing]
[16:26:27.224]  [00:00:13.192][detail][DMG] Command handler moving to [AddingComm]
[16:26:27.224]  [00:00:13.193][detail][DMG] Command handler moving to [AddedComma]
[16:26:27.225]  [00:00:13.193][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:27.226]  [00:00:13.193][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:27.227]  [00:00:13.193][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:27.228]  [00:00:13.195][info  ][EM] <<< [E:4261r S:25600 M:98722567] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:27.230]  [00:00:13.196][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:27.395]  [00:00:13.367][info  ][DL] Tx Confirmation received
[16:26:27.395]  [00:00:13.367][info  ][DL]  stop soft timer
[16:26:27.395]  [00:00:13.367][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:27.396]  [00:00:13.368][info  ][DL] Char Write Req, char : 47
[16:26:27.397]  [00:00:13.369][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 75)
[16:26:27.398]  [00:00:13.369][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:27.399]  [00:00:13.371][info  ][EM] >>> [E:4262r S:25600 M:193131815] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[16:26:27.400]  [00:00:13.371][detail][EM] Handling via exchange: 4262r, Delegate: 0x2000413c
[16:26:27.401]  [00:00:13.372][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0002
[16:26:27.402]  [00:00:13.373][detail][DMG] Command handler moving to [NewRespons]
[16:26:27.403]  [00:00:13.373][detail][DMG] Command handler moving to [ Preparing]
[16:26:27.403]  [00:00:13.373][detail][DMG] Command handler moving to [AddingComm]
[16:26:27.404]  [00:00:13.374][detail][DMG] Command handler moving to [AddedComma]
[16:26:27.405]  [00:00:13.374][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:27.406]  [00:00:13.374][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:27.407]  [00:00:13.374][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:27.408]  [00:00:13.375][info  ][EM] <<< [E:4262r S:25600 M:98722568] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:27.410]  [00:00:13.376][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:27.664]  [00:00:13.636][info  ][DL] Tx Confirmation received
[16:26:27.664]  [00:00:13.636][info  ][DL]  stop soft timer
[16:26:27.665]  [00:00:13.637][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:27.665]  [00:00:13.638][info  ][DL] Char Write Req, char : 47
[16:26:27.666]  [00:00:13.638][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:26:27.667]  [00:00:13.638][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:27.668]  [00:00:13.640][info  ][EM] >>> [E:4263r S:25600 M:193131816] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:26:27.670]  [00:00:13.641][detail][EM] Handling via exchange: 4263r, Delegate: 0x2000413c
[16:26:27.671]  [00:00:13.642][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:26:27.672]  [00:00:13.642][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[16:26:27.672]  [00:00:13.642][detail][DMG] Command handler moving to [NewRespons]
[16:26:27.674]  [00:00:13.643][detail][DMG] Command handler moving to [ Preparing]
[16:26:27.674]  [00:00:13.643][detail][DMG] Command handler moving to [AddingComm]
[16:26:27.675]  [00:00:13.643][detail][DMG] Command handler moving to [AddedComma]
[16:26:27.676]  [00:00:13.643][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:27.676]  [00:00:13.644][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:27.678]  [00:00:13.644][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:27.679]  [00:00:13.646][info  ][EM] <<< [E:4263r S:25600 M:98722569] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[16:26:27.681]  [00:00:13.647][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:27.845]  [00:00:13.817][info  ][DL] Tx Confirmation received
[16:26:27.845]  [00:00:13.817][info  ][DL]  stop soft timer
[16:26:27.846]  [00:00:13.817][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.025]  [00:00:13.997][info  ][DL] Tx Confirmation received
[16:26:28.025]  [00:00:13.997][info  ][DL]  stop soft timer
[16:26:28.025]  [00:00:13.998][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.204]  [00:00:14.176][info  ][DL] Tx Confirmation received
[16:26:28.204]  [00:00:14.176][info  ][DL]  stop soft timer
[16:26:28.205]  [00:00:14.177][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.206]  [00:00:14.178][info  ][DL] Char Write Req, char : 47
[16:26:28.206]  [00:00:14.178][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:26:28.208]  [00:00:14.178][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:28.209]  [00:00:14.180][info  ][EM] >>> [E:4264r S:25600 M:193131817] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:26:28.210]  [00:00:14.181][detail][EM] Handling via exchange: 4264r, Delegate: 0x2000413c
[16:26:28.211]  [00:00:14.182][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:26:28.212]  [00:00:14.182][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[16:26:28.213]  [00:00:14.182][detail][DMG] Command handler moving to [NewRespons]
[16:26:28.214]  [00:00:14.183][detail][DMG] Command handler moving to [ Preparing]
[16:26:28.215]  [00:00:14.183][detail][DMG] Command handler moving to [AddingComm]
[16:26:28.215]  [00:00:14.183][detail][DMG] Command handler moving to [AddedComma]
[16:26:28.216]  [00:00:14.183][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:28.217]  [00:00:14.184][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:28.218]  [00:00:14.184][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:28.219]  [00:00:14.186][info  ][EM] <<< [E:4264r S:25600 M:98722570] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[16:26:28.221]  [00:00:14.187][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:28.384]  [00:00:14.357][info  ][DL] Tx Confirmation received
[16:26:28.384]  [00:00:14.357][info  ][DL]  stop soft timer
[16:26:28.386]  [00:00:14.357][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.565]  [00:00:14.537][info  ][DL] Tx Confirmation received
[16:26:28.565]  [00:00:14.537][info  ][DL]  stop soft timer
[16:26:28.566]  [00:00:14.538][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.745]  [00:00:14.716][info  ][DL] Tx Confirmation received
[16:26:28.745]  [00:00:14.716][info  ][DL]  stop soft timer
[16:26:28.746]  [00:00:14.717][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:28.746]  [00:00:14.718][info  ][DL] Char Write Req, char : 47
[16:26:28.747]  [00:00:14.718][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[16:26:28.748]  [00:00:14.719][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:28.749]  [00:00:14.721][info  ][EM] >>> [E:4265r S:25600 M:193131818] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[16:26:28.751]  [00:00:14.721][detail][EM] Handling via exchange: 4265r, Delegate: 0x2000413c
[16:26:28.752]  [00:00:14.722][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0000
[16:26:28.753]  [00:00:14.722][info  ][ZCL] OpCreds: Received an AttestationRequest command
[16:26:28.757]  [00:00:14.729][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:599, sig_size:64, err:0x00
[16:26:28.758]  [00:00:14.729][info  ][ZCL] OpCreds: AttestationRequest successful.
[16:26:28.759]  [00:00:14.729][detail][DMG] Command handler moving to [NewRespons]
[16:26:28.759]  [00:00:14.729][detail][DMG] Command handler moving to [ Preparing]
[16:26:28.760]  [00:00:14.730][detail][DMG] Command handler moving to [AddingComm]
[16:26:28.761]  [00:00:14.730][detail][DMG] Command handler moving to [AddedComma]
[16:26:28.761]  [00:00:14.730][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:28.763]  [00:00:14.731][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:28.764]  [00:00:14.731][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:28.764]  [00:00:14.733][info  ][EM] <<< [E:4265r S:25600 M:98722571] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[16:26:28.766]  [00:00:14.734][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:28.925]  [00:00:14.897][info  ][DL] Tx Confirmation received
[16:26:28.925]  [00:00:14.897][info  ][DL]  stop soft timer
[16:26:28.925]  [00:00:14.897][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:29.104]  [00:00:15.077][info  ][DL] Tx Confirmation received
[16:26:29.104]  [00:00:15.077][info  ][DL]  stop soft timer
[16:26:29.105]  [00:00:15.078][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:29.375]  [00:00:15.346][info  ][DL] Tx Confirmation received
[16:26:29.375]  [00:00:15.346][info  ][DL]  stop soft timer
[16:26:29.376]  [00:00:15.347][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:29.376]  [00:00:15.348][info  ][DL] Char Write Req, char : 47
[16:26:29.377]  [00:00:15.348][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:26:29.378]  [00:00:15.348][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:29.379]  [00:00:15.350][info  ][EM] >>> [E:4266r S:25600 M:193131819] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:26:29.380]  [00:00:15.351][detail][EM] Handling via exchange: 4266r, Delegate: 0x2000413c
[16:26:29.382]  [00:00:15.352][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:26:29.383]  [00:00:15.352][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[16:26:29.383]  [00:00:15.352][detail][DMG] Command handler moving to [NewRespons]
[16:26:29.384]  [00:00:15.353][detail][DMG] Command handler moving to [ Preparing]
[16:26:29.385]  [00:00:15.353][detail][DMG] Command handler moving to [AddingComm]
[16:26:29.386]  [00:00:15.353][detail][DMG] Command handler moving to [AddedComma]
[16:26:29.387]  [00:00:15.353][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:29.387]  [00:00:15.354][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:29.389]  [00:00:15.354][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:29.389]  [00:00:15.356][info  ][EM] <<< [E:4266r S:25600 M:98722572] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:29.391]  [00:00:15.357][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:29.555]  [00:00:15.527][info  ][DL] Tx Confirmation received
[16:26:29.555]  [00:00:15.527][info  ][DL]  stop soft timer
[16:26:29.555]  [00:00:15.527][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:31.266]  [00:00:17.238][info  ][DL] Char Write Req, char : 47
[16:26:31.266]  [00:00:17.238][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[16:26:31.267]  [00:00:17.238][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:31.268]  [00:00:17.241][info  ][EM] >>> [E:4267r S:25600 M:193131820] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[16:26:31.270]  [00:00:17.241][detail][EM] Handling via exchange: 4267r, Delegate: 0x2000413c
[16:26:31.271]  [00:00:17.242][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0004
[16:26:31.272]  [00:00:17.242][info  ][ZCL] OpCreds: Received a CSRRequest command
[16:26:31.282]  [00:00:17.254][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[16:26:31.289]  [00:00:17.260][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:277, sig_size:64, err:0x00
[16:26:31.289]  [00:00:17.261][info  ][ZCL] OpCreds: CSRRequest successful.
[16:26:31.290]  [00:00:17.261][detail][DMG] Command handler moving to [NewRespons]
[16:26:31.291]  [00:00:17.261][detail][DMG] Command handler moving to [ Preparing]
[16:26:31.292]  [00:00:17.261][detail][DMG] Command handler moving to [AddingComm]
[16:26:31.292]  [00:00:17.261][detail][DMG] Command handler moving to [AddedComma]
[16:26:31.293]  [00:00:17.262][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:31.294]  [00:00:17.262][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:31.295]  [00:00:17.262][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:31.296]  [00:00:17.264][info  ][EM] <<< [E:4267r S:25600 M:98722573] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[16:26:31.298]  [00:00:17.265][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:31.535]  [00:00:17.506][info  ][DL] Tx Confirmation received
[16:26:31.535]  [00:00:17.507][info  ][DL]  stop soft timer
[16:26:31.536]  [00:00:17.507][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:31.714]  [00:00:17.687][info  ][DL] Tx Confirmation received
[16:26:31.714]  [00:00:17.687][info  ][DL]  stop soft timer
[16:26:31.715]  [00:00:17.687][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:31.717]  [00:00:17.689][info  ][DL] Char Write Req, char : 47
[16:26:31.717]  [00:00:17.690][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:26:31.718]  [00:00:17.690][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.075]  [00:00:18.047][info  ][DL] Char Write Req, char : 47
[16:26:32.075]  [00:00:18.047][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 71)
[16:26:32.076]  [00:00:18.048][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.078]  [00:00:18.050][info  ][EM] >>> [E:4268r S:25600 M:193131821] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:308)
[16:26:32.079]  [00:00:18.050][detail][EM] Handling via exchange: 4268r, Delegate: 0x2000413c
[16:26:32.081]  [00:00:18.051][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B
[16:26:32.081]  [00:00:18.051][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[16:26:32.092]  [00:00:18.065][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[16:26:32.093]  [00:00:18.065][detail][DMG] Command handler moving to [NewRespons]
[16:26:32.094]  [00:00:18.065][detail][DMG] Command handler moving to [ Preparing]
[16:26:32.094]  [00:00:18.065][detail][DMG] Command handler moving to [AddingComm]
[16:26:32.095]  [00:00:18.066][detail][DMG] Command handler moving to [AddedComma]
[16:26:32.096]  [00:00:18.066][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:32.097]  [00:00:18.066][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:32.098]  [00:00:18.066][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:32.099]  [00:00:18.068][info  ][EM] <<< [E:4268r S:25600 M:98722574] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[16:26:32.101]  [00:00:18.069][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:32.255]  [00:00:18.226][info  ][DL] Tx Confirmation received
[16:26:32.255]  [00:00:18.227][info  ][DL]  stop soft timer
[16:26:32.256]  [00:00:18.227][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:32.258]  [00:00:18.229][info  ][DL] Char Write Req, char : 47
[16:26:32.258]  [00:00:18.230][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:26:32.259]  [00:00:18.230][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.296]  
[16:26:32.436]  [00:00:18.408][info  ][DL] Char Write Req, char : 47
[16:26:32.436]  [00:00:18.408][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 110)
[16:26:32.438]  [00:00:18.409][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.439]  [00:00:18.411][info  ][EM] >>> [E:4269r S:25600 M:193131822] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:347)
[16:26:32.440]  [00:00:18.411][detail][EM] Handling via exchange: 4269r, Delegate: 0x2000413c
[16:26:32.441]  [00:00:18.412][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0006
[16:26:32.442]  [00:00:18.413][info  ][ZCL] OpCreds: Received an AddNOC command
[16:26:32.443]  [00:00:18.415][info  ][FP] Validating NOC chain
[16:26:32.459]  [00:00:18.430][info  ][FP] NOC chain validation successful
[16:26:32.459]  [00:00:18.430][info  ][FP] Added new fabric at index: 0x1
[16:26:32.459]  [00:00:18.431][info  ][FP] Assigned compressed fabric ID: 0x48703F2ABA76AAAB, node ID: 0x00000000FCB0C0DF
[16:26:32.461]  [00:00:18.431][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[16:26:32.461]  [00:00:18.431][info  ][TS] New proposed Last Known Good Time: 2026-02-07T08:26:31
[16:26:32.462]  [00:00:18.431][info  ][TS] Updating pending Last Known Good Time to 2026-02-07T08:26:31
[16:26:32.472]  [00:00:18.443][detail][EVL] LogEvent event number: 0x0000000000000002 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6ACFF3C6
[16:26:32.473]  [00:00:18.444][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0x0000000036E47752
[16:26:32.474]  [00:00:18.444][detail][DL] Using Thread extended MAC for hostname.
[16:26:32.475]  [00:00:18.444][info  ][DIS] Advertise operational node 48703F2ABA76AAAB-00000000FCB0C0DF
[16:26:32.476]  [00:00:18.444][error ][SVR] Operational advertising failed: 3
[16:26:32.477]  [00:00:18.444][detail][DMG] Command handler moving to [NewRespons]
[16:26:32.478]  [00:00:18.444][detail][DMG] Command handler moving to [ Preparing]
[16:26:32.478]  [00:00:18.445][detail][DMG] Command handler moving to [AddingComm]
[16:26:32.479]  [00:00:18.445][detail][DMG] Command handler moving to [AddedComma]
[16:26:32.480]  [00:00:18.445][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[16:26:32.480]  [00:00:18.445][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:32.482]  [00:00:18.446][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:32.483]  [00:00:18.448][info  ][EM] <<< [E:4269r S:25600 M:98722575] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [AAAB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:32.485]  [00:00:18.448][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:32.615]  [00:00:18.586][info  ][DL] Tx Confirmation received
[16:26:32.615]  [00:00:18.586][info  ][DL]  stop soft timer
[16:26:32.615]  [00:00:18.587][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:32.617]  [00:00:18.589][info  ][DL] Char Write Req, char : 47
[16:26:32.617]  [00:00:18.589][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 177)
[16:26:32.618]  [00:00:18.589][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.619]  [00:00:18.591][info  ][EM] >>> [E:4270r S:25600 M:193131823] (S) Msg RX from 1:FFFFFFFB00000000 [AAAB] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:172)
[16:26:32.621]  [00:00:18.592][detail][EM] Handling via exchange: 4270r, Delegate: 0x2000413c
[16:26:32.622]  [00:00:18.593][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0003
[16:26:32.623]  [00:00:18.594][detail][DMG] Command handler moving to [NewRespons]
[16:26:32.624]  [00:00:18.595][detail][DMG] Command handler moving to [ Preparing]
[16:26:32.625]  [00:00:18.595][detail][DMG] Command handler moving to [AddingComm]
[16:26:32.625]  [00:00:18.595][detail][DMG] Command handler moving to [AddedComma]
[16:26:32.626]  [00:00:18.595][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:32.627]  [00:00:18.595][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:32.628]  [00:00:18.596][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:32.629]  [00:00:18.598][info  ][EM] <<< [E:4270r S:25600 M:98722576] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [AAAB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:32.631]  [00:00:18.599][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:32.795]  [00:00:18.766][info  ][DL] Tx Confirmation received
[16:26:32.795]  [00:00:18.767][info  ][DL]  stop soft timer
[16:26:32.795]  [00:00:18.767][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:32.796]  [00:00:18.768][info  ][DL] Char Write Req, char : 47
[16:26:32.797]  [00:00:18.768][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:26:32.798]  [00:00:18.769][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.799]  [00:00:18.771][info  ][EM] >>> [E:4271r S:25600 M:193131824] (S) Msg RX from 1:FFFFFFFB00000000 [AAAB] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:26:32.800]  [00:00:18.771][detail][EM] Handling via exchange: 4271r, Delegate: 0x2000413c
[16:26:32.802]  [00:00:18.772][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:26:32.802]  [00:00:18.772][info  ][FS] GeneralCommissioning: Received ArmFailSafe (108s)
[16:26:32.803]  [00:00:18.773][detail][DMG] Command handler moving to [NewRespons]
[16:26:32.804]  [00:00:18.773][detail][DMG] Command handler moving to [ Preparing]
[16:26:32.805]  [00:00:18.773][detail][DMG] Command handler moving to [AddingComm]
[16:26:32.806]  [00:00:18.773][detail][DMG] Command handler moving to [AddedComma]
[16:26:32.806]  [00:00:18.774][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:32.807]  [00:00:18.774][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:32.809]  [00:00:18.774][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:32.809]  [00:00:18.776][info  ][EM] <<< [E:4271r S:25600 M:98722577] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [AAAB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:26:32.811]  [00:00:18.777][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:32.974]  [00:00:18.947][info  ][DL] Tx Confirmation received
[16:26:32.974]  [00:00:18.947][info  ][DL]  stop soft timer
[16:26:32.975]  [00:00:18.947][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:32.976]  [00:00:18.948][info  ][DL] Char Write Req, char : 47
[16:26:32.976]  [00:00:18.949][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 78)
[16:26:32.978]  [00:00:18.949][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:32.978]  [00:00:18.951][info  ][EM] >>> [E:4272r S:25600 M:193131825] (S) Msg RX from 1:FFFFFFFB00000000 [AAAB] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[16:26:32.980]  [00:00:18.951][detail][EM] Handling via exchange: 4272r, Delegate: 0x2000413c
[16:26:32.981]  [00:00:18.953][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0006
[16:26:32.982]  [00:00:18.953][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 3
[16:26:32.990]  [00:00:18.962][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 2
[16:26:32.991]  [00:00:18.962][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:32.991]  [00:00:18.962][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[16:26:32.993]  [00:00:18.962][silabs ]NWK: platform event type 8004
[16:26:32.993]  [00:00:18.963][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:26:32.994]  [00:00:18.963][detail][DL] OpenThread State Changed (Flags: 0x1117d11d)
[16:26:32.995]  [00:00:18.963][detail][DL]    Device Role: DETACHED
[16:26:32.995]  [00:00:18.964][detail][DL]    Network Name: MyHome1077284020
[16:26:32.996]  [00:00:18.964][detail][DL]    PAN Id: 0xE298
[16:26:32.997]  [00:00:18.964][detail][DL]    Extended PAN Id: 0x536F423A33064EFE
[16:26:32.997]  [00:00:18.964][detail][DL]    Channel: 25
[16:26:32.997]  [00:00:18.964][detail][DL]    Mesh Prefix: fded:8f52:1985:d930:0:0:0:0/64
[16:26:32.998]  [00:00:18.965][detail][DL]    Thread Unicast Addresses:
[16:26:32.999]  [00:00:18.965][detail][DL]         fded:8f52:1985:d930:e8ec:76af:1cf4:da3f/64 valid preferred
[16:26:33.000]  [00:00:18.965][detail][DL]         fe80:0:0:0:d476:812b:9246:a3cd/64 valid preferred
[16:26:33.974]  [00:00:19.946][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:26:33.975]  [00:00:19.946][detail][DL] OpenThread State Changed (Flags: 0x00000100)
[16:26:33.975]  [00:00:19.946][silabs ]NWK: platform event type 800b
[16:26:34.449]  [00:00:20.420][info  ][DL] SRP Client was started, detected server: fded:8f52:1985:d930:0000:00ff:fe00:fc11
[16:26:34.450]  [00:00:20.421][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:26:34.450]  [00:00:20.421][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[16:26:34.452]  [00:00:20.421][detail][EVL] LogEvent event number: 0x0000000000000003 priority: 1, endpoint id:  0x0 cluster id: 0x0000_0035 event id: 0x0 Epoch timestamp: 0x000000DC6ACFFB80
[16:26:34.454]  [00:00:20.422][detail][DL] OpenThread State Changed (Flags: 0x200002a4) 
[16:26:34.454]  [00:00:20.422][detail][DL]    Device Role: CHILD
[16:26:34.455]  [00:00:20.422][detail][DL]    Partition Id: 0x4F36B956
[16:26:34.456]  [00:00:20.422][silabs ]NWK: platform event type 800b
[16:26:34.457]  [00:00:20.423][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[16:26:34.457]  [00:00:20.423][silabs ]NWK: platform event type 8001
[16:26:34.458]  [00:00:20.423][silabs ]COM: notify network [Joined]
[16:26:34.459]  [00:00:20.424][silabs ]NWK: Thread Established 
[16:26:34.459]  [00:00:20.424][info  ][SVR] Scheduling OTA Requestor initialization
[16:26:34.460]  [00:00:20.424][detail][DL] Thread Attached updating Multicast address
[16:26:34.461]  [00:00:20.426][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:34.462]  [00:00:20.428][info  ][EM] <<< [E:4272r S:25600 M:98722578] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [AAAB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[16:26:34.464]  [00:00:20.429][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:34.465]  [00:00:20.429][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[16:26:34.466]  [00:00:20.429][detail][DL] Using Thread extended MAC for hostname.
[16:26:34.466]  [00:00:20.429][info  ][DIS] Advertise operational node 48703F2ABA76AAAB-00000000FCB0C0DF
[16:26:34.468]  [00:00:20.430][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:26:34.468]  [00:00:20.431][detail][DL]         fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117/64 valid preferred
[16:26:34.469]  [00:00:20.431][detail][DL]         fded:8f52:1985:d930:0:ff:fe00:b80c/64 valid preferred rloc
[16:26:34.471]  [00:00:20.433][silabs ]NWK: platform event type 800b
[16:26:34.594]  [00:00:20.567][info  ][DL] Tx Confirmation received
[16:26:34.594]  [00:00:20.567][info  ][DL]  stop soft timer
[16:26:34.595]  [00:00:20.567][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:26:35.226]  [00:00:21.198][detail][DL] SRP update succeeded
[16:26:35.226]  [00:00:21.198][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[16:26:35.228]  [00:00:21.199][silabs ]NWK: platform event type 8012
[16:26:35.228]  [00:00:21.201][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[16:26:35.230]  [00:00:21.201][info  ][SVR] Server initialization complete
[16:26:35.230]  [00:00:21.201][info  ][DIS] Updating services using commissioning mode 0
[16:26:35.231]  [00:00:21.201][detail][DL] Using Thread extended MAC for hostname.
[16:26:35.232]  [00:00:21.201][info  ][DIS] Advertise operational node 48703F2ABA76AAAB-00000000FCB0C0DF
[16:26:35.233]  [00:00:21.202][info  ][DL] advertising srp service: 48703F2ABA76AAAB-00000000FCB0C0DF._matter._tcp
[16:26:35.234]  [00:00:21.202][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[16:26:35.235]  [00:00:21.202][silabs ]NWK: platform event type 8016
[16:26:35.241]  [00:00:21.212][info  ][IM] No subscriptions to resume
[16:26:35.416]  [00:00:21.388][detail][DL] SRP update succeeded
[16:26:35.961]  [00:00:21.933][detail][IN] UDP Message Received packet nb : 1 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 196
[16:26:35.963]  [00:00:21.933][info  ][EM] >>> [E:4273r S:0 M:203526976] (U) Msg RX from 0:AD5CBEC7D3810DD9 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:26:35.964]  [00:00:21.934][detail][EM] Handling via exchange: 4273r, Delegate: 0x20007de8
[16:26:35.965]  [00:00:21.934][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200089b0
[16:26:35.966]  [00:00:21.935][info  ][EM] <<< [E:4273r S:0 M:139474077 (Ack:203526976)] (U) Msg TX from 0000000000000000 to 0:AD5CBEC7D3810DD9 [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:35.969]  [00:00:21.935][detail][EM] Flushed pending ack for MessageCounter:203526976 on exchange 4273r
[16:26:35.970]  [00:00:21.935][info  ][SC] Received Sigma1 msg
[16:26:35.970]  [00:00:21.936][detail][SC] Found MRP parameters in the message
[16:26:35.971]  [00:00:21.936][detail][SC] Peer (Initiator) assigned session ID 39871
[16:26:35.974]  [00:00:21.946][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000FCB0C0DF
[16:26:35.995]  [00:00:21.967][detail][CR] AES_CCM_encrypt: Using aad == null path
[16:26:35.997]  [00:00:21.969][info  ][EM] <<< [E:4273r S:0 M:139474078 (Ack:203526976)] (U) Msg TX from 0000000000000000 to 0:AD5CBEC7D3810DD9 [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:528)
[16:26:35.999]  [00:00:21.970][info  ][EM] ??1 [E:4273r S:0 M:139474078] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3334ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:36.001]  [00:00:21.971][info  ][SC] Sent Sigma2 msg  
[16:26:36.559]  [00:00:22.531][detail][IN] UDP Message Received packet nb : 2 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 380
[16:26:36.561]  [00:00:22.531][info  ][EM] >>> [E:4273r S:0 M:203526977 (Ack:139474078)] (U) Msg RX from 0:AD5CBEC7D3810DD9 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:380)
[16:26:36.562]  [00:00:22.531][detail][EM] Found matching exchange: 4273r, Delegate: 0x20007e04
[16:26:36.563]  [00:00:22.532][detail][EM] Rxd Ack; Removing MessageCounter:139474078 from Retrans Table on exchange 4273r
[16:26:36.564]  [00:00:22.532][info  ][EM] <<< [E:4273r S:0 M:139474079 (Ack:203526977)] (U) Msg TX from 0000000000000000 to 0:AD5CBEC7D3810DD9 [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:36.567]  [00:00:22.533][detail][EM] Flushed pending ack for MessageCounter:203526977 on exchange 4273r
[16:26:36.568]  [00:00:22.533][info  ][SC] Received Sigma3 msg
[16:26:36.568]  [00:00:22.537][detail][CR] AES_CCM_decrypt: Using aad == null path
[16:26:36.570]  [00:00:22.540][detail][SC] Certificate's mNotBeforeTime (823607378) is after current time (22)
[16:26:36.570]  [00:00:22.540][detail][SC] Certificate's mNotBeforeTime (823767991) is after current time (22)
[16:26:36.597]  [00:00:22.569][detail][SC] Sending status report. Protocol code 0, exchange 4273
[16:26:36.598]  [00:00:22.570][info  ][EM] <<< [E:4273r S:0 M:139474080 (Ack:203526977)] (U) Msg TX from 0000000000000000 to 0:AD5CBEC7D3810DD9 [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:26:36.601]  [00:00:22.571][info  ][EM] ??1 [E:4273r S:0 M:139474080] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3411ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:36.602]  [00:00:22.575][info  ][SC] SecureSession[0x20006f58, LSID:25599]: State change 'kEstablishing' --> 'kActive'
[16:26:36.604]  [00:00:22.575][detail][IN] SecureSession[0x20006f58]: Activated - Type:2 LSID:25599
[16:26:36.604]  [00:00:22.575][detail][IN] New secure session activated for device <0000000036E47752, 1>, LSID:25599 PSID:39871!
[16:26:36.606]  [00:00:22.575][info  ][IN] CASE Session established to peer: <0000000036E47752, 1>
[16:26:36.606]  [00:00:22.576][detail][IN] SecureSession[0x20007108]: Allocated Type:2 LSID:25601
[16:26:36.608]  [00:00:22.576][detail][SC] Allocated SecureSession (0x20007108) - waiting for Sigma1 msg
[16:26:36.608]  [00:00:22.576][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:26:36.609]  [00:00:22.577][silabs ]NWK: platform event type 8018
[16:26:37.025]  [00:00:22.997][info  ][DL] Char Write Req, char : 47
[16:26:37.025]  [00:00:22.997][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 3)
[16:26:37.026]  [00:00:22.998][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:26:37.075]  [00:00:23.047][detail][IN] UDP Message Received packet nb : 3 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 59
[16:26:37.077]  [00:00:23.049][info  ][EM] >>> [E:4274r S:25599 M:47048203] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[16:26:37.079]  [00:00:23.049][detail][EM] Handling via exchange: 4274r, Delegate: 0x2000413c
[16:26:37.079]  [00:00:23.050][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0004
[16:26:37.081]  [00:00:23.051][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[16:26:37.081]  [00:00:23.052][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:26:37.090]  [00:00:23.062][info  ][TS] Committing Last Known Good Time to storage: 2026-02-07T08:26:31
[16:26:37.097]  [00:00:23.069][detail][IN] UDP Message Received packet nb : 4 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 26
[16:26:37.099]  [00:00:23.070][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x48703F2ABA76AAAB, FabricId 00000000113DE407, NodeId 00000000FCB0C0DF, VendorId 0x1349
[16:26:37.100]  [00:00:23.070][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[16:26:37.102]  [00:00:23.071][info  ][FS] Fail-safe cleanly disarmed
[16:26:37.102]  [00:00:23.071][detail][DMG] Command handler moving to [NewRespons]
[16:26:37.103]  [00:00:23.071][detail][DMG] Command handler moving to [ Preparing]
[16:26:37.104]  
[16:26:37.104]  [00:00:23.071][detail][DMG] Command handler moving to [AddingComm]
[16:26:37.104]  
[16:26:37.105]  [00:00:23.071][detail][DMG] Command handler moving to [AddedComma]
[16:26:37.106]  
[16:26:37.106]  [00:00:23.072][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:37.106]  
[16:26:37.107]  [00:00:23.072][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:37.108]  
[16:26:37.108]  [00:00:23.072][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:37.108]  
[16:26:37.109]  [00:00:23.074][info  ][EM] <<< [E:4274r S:25599 M:83709788 (Ack:47048203)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:26:37.111]  [00:00:23.075][info  ][EM] ??1 [E:4274r S:25599 M:83709788] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3358ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:37.113]  [00:00:23.075][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:37.114]  [00:00:23.076][info  ][EM] >>> [E:4273r S:0 M:203526978 (Ack:139474080)] (U) Msg RX from 0:AD5CBEC7D3810DD9 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:37.116]  [00:00:23.076][detail][EM] Found matching exchange: 4273r, Delegate: 0
[16:26:37.117]  [00:00:23.077][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[16:26:37.118]  [00:00:23.078][detail][IN] Expiring all PASE sessions
[16:26:37.118]  [00:00:23.079][detail][IN] SecureSession[0x20007030]: Released - Type:1 LSID:25600
[16:26:37.120]  [00:00:23.080][detail][ZCL] Commissioning complete, notify platform driver to persist network credentials.
[16:26:37.205]  [00:00:23.177][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[16:26:37.205]  [00:00:23.177][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[16:26:37.206]  [00:00:23.177][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[16:26:37.207]  [00:00:23.178][detail][BLE] No endpoint for connection error
[16:26:37.716]  [00:00:23.688][detail][IN] UDP Message Received packet nb : 5 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:37.718]  [00:00:23.690][info  ][EM] >>> [E:4274r S:25599 M:47048204 (Ack:83709788)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:37.720]  [00:00:23.690][detail][EM] Found matching exchange: 4274r, Delegate: 0
[16:26:37.721]  [00:00:23.690][detail][EM] Rxd Ack; Removing MessageCounter:83709788 from Retrans Table on exchange 4274r
[16:26:37.865]  [00:00:23.837][detail][IN] UDP Message Received packet nb : 6 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 110
[16:26:37.867]  [00:00:23.839][info  ][EM] >>> [E:4275r S:25599 M:47048205] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:06 (IM:WriteRequest) (B:110)
[16:26:37.869]  [00:00:23.840][detail][EM] Handling via exchange: 4275r, Delegate: 0x2000413c
[16:26:37.869]  [00:00:23.840][detail][IM] Received Write request
[16:26:37.870]  [00:00:23.840][detail][DMG] IM WH moving to [Initialized]
[16:26:37.871]  [00:00:23.841][detail][DMG] Writing attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000
[16:26:37.872]  [00:00:23.844][detail][EVL] LogEvent event number: 0x0000000000000004 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6AD008DE
[16:26:37.873]  [00:00:23.845][detail][EVL] LogEvent event number: 0x0000000000000005 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6AD008E0
[16:26:37.876]  [00:00:23.846][detail][DMG] IM WH moving to [AddStatus]
[16:26:37.876]  [00:00:23.848][info  ][EM] <<< [E:4275r S:25599 M:83709789 (Ack:47048205)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:07 (IM:WriteResponse) (B:62)
[16:26:37.879]  [00:00:23.849][info  ][EM] ??1 [E:4275r S:25599 M:83709789] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3358ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:37.880]  [00:00:23.849][detail][DMG] IM WH moving to [Sending]
[16:26:37.881]  [00:00:23.849][detail][DMG] IM WH moving to [Uninitialized]
[16:26:38.230]  [00:00:24.202][info  ][SWU] Stopping the watchdog timer
[16:26:38.230]  [00:00:24.203][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:26:38.231]  [00:00:24.203][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888a
[16:26:38.232]  [00:00:24.203][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888b
[16:26:38.296]  
[16:26:38.378]  [00:00:24.349][detail][IN] UDP Message Received packet nb : 7 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:38.380]  [00:00:24.351][info  ][EM] >>> [E:4275r S:25599 M:47048206 (Ack:83709789)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:38.382]  [00:00:24.352][detail][EM] Found matching exchange: 4275r, Delegate: 0
[16:26:38.383]  [00:00:24.352][detail][EM] Rxd Ack; Removing MessageCounter:83709789 from Retrans Table on exchange 4275r
[16:26:38.401]  [00:00:24.373][detail][IN] UDP Message Received packet nb : 8 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 58
[16:26:38.403]  [00:00:24.375][info  ][EM] >>> [E:4276r S:25599 M:47048207] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:03 (IM:SubscribeRequest) (B:58)
[16:26:38.404]  [00:00:24.375][detail][EM] Handling via exchange: 4276r, Delegate: 0x2000413c
[16:26:38.405]  [00:00:24.375][detail][IM] Received Subscribe request
[16:26:38.406]  [00:00:24.377][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[16:26:38.407]  [00:00:24.378][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:38.418]  [00:00:24.390][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:38.420]  [00:00:24.391][detail][DMG] <RE:Run> Cluster 41, Attribute 0 is dirty
[16:26:38.420]  [00:00:24.391][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.422]  [00:00:24.392][detail][DMG] <RE:Run> Cluster 41, Attribute fffc is dirty
[16:26:38.422]  [00:00:24.393][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:38.424]  [00:00:24.393][detail][DMG] <RE:Run> Cluster 41, Attribute fffd is dirty
[16:26:38.424]  [00:00:24.393][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.426]  [00:00:24.394][detail][DMG] <RE:Run> Cluster 41, Attribute fff8 is dirty
[16:26:38.427]  [00:00:24.395][detail][DMG] <RE:Run> Cluster 41, Attribute fff9 is dirty
[16:26:38.427]  [00:00:24.395][detail][DMG] <RE:Run> Cluster 41, Attribute fffb is dirty
[16:26:38.428]  [00:00:24.396][detail][DMG] <RE:Run> Cluster 40, Attribute 0 is dirty
[16:26:38.429]  [00:00:24.397][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.430]  [00:00:24.398][detail][DMG] <RE:Run> Cluster 40, Attribute fffc is dirty
[16:26:38.431]  [00:00:24.398][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:38.432]  [00:00:24.399][detail][DMG] <RE:Run> Cluster 40, Attribute fffd is dirty
[16:26:38.433]  [00:00:24.399][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.434]  [00:00:24.400][detail][DMG] <RE:Run> Cluster 40, Attribute fff8 is dirty
[16:26:38.435]  [00:00:24.401][detail][DMG] <RE:Run> Cluster 40, Attribute fff9 is dirty
[16:26:38.436]  [00:00:24.402][detail][DMG] <RE:Run> Cluster 40, Attribute fffb is dirty
[16:26:38.437]  [00:00:24.402][detail][DMG] <RE:Run> Cluster 3f, Attribute 0 is dirty
[16:26:38.438]  [00:00:24.403][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.439]  
[16:26:38.439]  [00:00:24.404][detail][DMG] <RE:Run> Cluster 3f, Attribute 1 is dirty
[16:26:38.440]  [00:00:24.405][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:38.441]  [00:00:24.406][detail][DMG] <RE:Run> Cluster 3f, Attribute 2 is dirty
[16:26:38.442]  [00:00:24.406][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:38.443]  [00:00:24.407][detail][DMG] <RE:Run> Cluster 3f, Attribute 3 is dirty
[16:26:38.444]  [00:00:24.407][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:38.445]  [00:00:24.408][detail][DMG] <RE:Run> Cluster 3f, Attribute fffc is dirty
[16:26:38.446]  [00:00:24.409][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:38.447]  
[16:26:38.447]  [00:00:24.409][detail][DMG] <RE:Run> Cluster 3f, Attribute fffd is dirty
[16:26:38.448]  [00:00:24.410][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.449]  
[16:26:38.449]  [00:00:24.412][detail][DMG] <RE:Run> Cluster 3f, Attribute fffb is dirty
[16:26:38.450]  
[16:26:38.451]  [00:00:24.413][detail][DMG] <RE:Run> Cluster 3e, Attribute 0 is dirty
[16:26:38.452]  [00:00:24.413][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.453]  [00:00:24.416][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:26:38.454]  [00:00:24.416][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:38.455]  [00:00:24.416][detail][DMG] <RE:Run> Cluster 3e, Attribute 2 is dirty
[16:26:38.456]  [00:00:24.417][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:38.457]  [00:00:24.418][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:26:38.458]  [00:00:24.420][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:38.459]  [00:00:24.420][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_003E, attributeId: 0x0000_0004, err = b
[16:26:38.461]  [00:00:24.422][detail][DMG] Fetched 1 events
[16:26:38.461]  [00:00:24.424][info  ][EM] <<< [E:4276r S:25599 M:83709790 (Ack:47048207)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1181)
[16:26:38.463]  [00:00:24.426][info  ][EM] ??1 [E:4276r S:25599 M:83709790] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3395ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:38.465]  [00:00:24.426][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:38.466]  [00:00:24.426][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:38.477]  [00:00:24.449][detail][IN] UDP Message Received packet nb : 9 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:26:38.479]  [00:00:24.451][info  ][EM] >>> [E:4277r S:25599 M:47048208] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:26:38.480]  [00:00:24.451][detail][EM] Handling via exchange: 4277r, Delegate: 0x2000413c
[16:26:38.481]  [00:00:24.452][detail][IM] Received Read request
[16:26:38.482]  [00:00:24.452][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:38.482]  [00:00:24.453][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:38.484]  [00:00:24.453][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:26:38.485]  [00:00:24.454][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:26:38.486]  [00:00:24.456][detail][DMG] <RE> Sending report (payload has 128 bytes)...
[16:26:38.487]  [00:00:24.458][info  ][EM] <<< [E:4277r S:25599 M:83709791 (Ack:47048208)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:162)
[16:26:38.489]  [00:00:24.459][info  ][EM] ??1 [E:4277r S:25599 M:83709791] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3362ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:38.491]  [00:00:24.460][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:26:38.492]  [00:00:24.460][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has no more messages
[16:26:38.493]  [00:00:24.460][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:38.924]  [00:00:24.896][detail][IN] UDP Message Received packet nb : 10 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:38.926]  [00:00:24.898][info  ][EM] >>> [E:4276r S:25599 M:47048209 (Ack:83709790)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:38.927]  [00:00:24.898][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:38.928]  [00:00:24.899][detail][EM] Rxd Ack; Removing MessageCounter:83709790 from Retrans Table on exchange 4276r
[16:26:38.929]  [00:00:24.899][info  ][IM] Received status response, status is 0x00
[16:26:38.930]  [00:00:24.899][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:38.931]  [00:00:24.899][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:38.931]  [00:00:24.900][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:38.933]  [00:00:24.900][detail][DMG] <RE:Run> Cluster 3e, Attribute 4 is dirty
[16:26:38.934]  [00:00:24.901][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:38.935]  [00:00:24.902][detail][DMG] <RE:Run> Cluster 3e, Attribute 5 is dirty
[16:26:38.936]  [00:00:24.902][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:26:38.937]  
[16:26:38.937]  [00:00:24.903][detail][DMG] <RE:Run> Cluster 3e, Attribute fffc is dirty
[16:26:38.938]  [00:00:24.903][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:38.939]  
[16:26:38.939]  [00:00:24.904][detail][DMG] <RE:Run> Cluster 3e, Attribute fffd is dirty
[16:26:38.940]  
[16:26:38.941]  [00:00:24.905][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.942]  [00:00:24.905][detail][DMG] <RE:Run> Cluster 3e, Attribute fff8 is dirty
[16:26:38.943]  [00:00:24.906][detail][DMG] <RE:Run> Cluster 3e, Attribute fff9 is dirty
[16:26:38.944]  [00:00:24.907][detail][DMG] <RE:Run> Cluster 3e, Attribute fffb is dirty
[16:26:38.946]  [00:00:24.908][detail][DMG] <RE:Run> Cluster 3c, Attribute 0 is dirty
[16:26:38.947]  [00:00:24.909][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.948]  [00:00:24.909][detail][DMG] <RE:Run> Cluster 3c, Attribute 1 is dirty
[16:26:38.949]  [00:00:24.911][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:38.950]  [00:00:24.911][detail][DMG] <RE:Run> Cluster 3c, Attribute fffc is dirty
[16:26:38.951]  [00:00:24.913][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.952]  [00:00:24.915][detail][DMG] <RE:Run> Cluster 3c, Attribute fff9 is dirty
[16:26:38.953]  [00:00:24.915][detail][DMG] <RE:Run> Cluster 3c, Attribute fffb is dirty
[16:26:38.954]  
[16:26:38.954]  [00:00:24.916][detail][DMG] <RE:Run> Cluster 34, Attribute 0 is dirty
[16:26:38.955]  
[16:26:38.955]  [00:00:24.916][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:38.956]  [00:00:24.921][detail][DMG] <RE:Run> Cluster 34, Attribute 1 is dirty
[16:26:38.957]  
[16:26:38.957]  [00:00:24.922][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:38.959]  
[16:26:38.959]  [00:00:24.922][detail][DMG] <RE:Run> Cluster 34, Attribute 2 is dirty
[16:26:38.959]  [00:00:24.923][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:38.961]  [00:00:24.924][detail][DMG] <RE:Run> Cluster 34, Attribute 3 is dirty
[16:26:38.961]  [00:00:24.924][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:38.963]  [00:00:24.925][detail][DMG] <RE:Run> Cluster 34, Attribute fffc is dirty
[16:26:38.964]  [00:00:24.925][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:38.965]  [00:00:24.927][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:38.966]  [00:00:24.928][detail][DMG] <RE:Run> Cluster 34, Attribute fff9 is dirty
[16:26:38.967]  [00:00:24.929][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0034, attributeId: 0x0000_FFF9, err = b
[16:26:38.968]  [00:00:24.930][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:38.970]  [00:00:24.933][info  ][EM] <<< [E:4276r S:25599 M:83709792 (Ack:47048209)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1189)
[16:26:38.972]  [00:00:24.934][info  ][EM] ??1 [E:4276r S:25599 M:83709792] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3347ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:38.974]  [00:00:24.935][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:38.975]  [00:00:24.935][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:38.989]  [00:00:24.960][detail][IN] UDP Message Received packet nb : 11 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:38.991]  [00:00:24.961][info  ][EM] >>> [E:4277r S:25599 M:47048210 (Ack:83709791)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:38.993]  [00:00:24.962][detail][EM] Found matching exchange: 4277r, Delegate: 0
[16:26:38.993]  [00:00:24.962][detail][EM] Rxd Ack; Removing MessageCounter:83709791 from Retrans Table on exchange 4277r
[16:26:39.551]  [00:00:25.523][detail][IN] UDP Message Received packet nb : 12 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:39.553]  [00:00:25.525][info  ][EM] >>> [E:4276r S:25599 M:47048211 (Ack:83709792)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:39.555]  [00:00:25.526][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:39.556]  [00:00:25.526][detail][EM] Rxd Ack; Removing MessageCounter:83709792 from Retrans Table on exchange 4276r
[16:26:39.557]  [00:00:25.526][info  ][IM] Received status response, status is 0x00
[16:26:39.557]  [00:00:25.526][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:39.558]  [00:00:25.526][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:39.559]  [00:00:25.527][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:39.561]  [00:00:25.527][detail][DMG] <RE:Run> Cluster 34, Attribute fff9 is dirty
[16:26:39.562]  [00:00:25.528][detail][DMG] <RE:Run> Cluster 34, Attribute fffb is dirty
[16:26:39.562]  [00:00:25.529][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[16:26:39.563]  [00:00:25.530][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:39.564]  
[16:26:39.564]  [00:00:25.531][detail][DMG] <RE:Run> Cluster 33, Attribute 1 is dirty
[16:26:39.565]  
[16:26:39.566]  [00:00:25.531][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:39.566]  
[16:26:39.567]  [00:00:25.532][detail][DMG] <RE:Run> Cluster 33, Attribute 8 is dirty
[16:26:39.568]  
[16:26:39.568]  [00:00:25.533][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:26:39.569]  
[16:26:39.569]  [00:00:25.533][detail][DMG] <RE:Run> Cluster 33, Attribute 3 is dirty
[16:26:39.570]  [00:00:25.534][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:39.571]  
[16:26:39.572]  [00:00:25.534][detail][DMG] <RE:Run> Cluster 33, Attribute 4 is dirty
[16:26:39.573]  [00:00:25.535][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:39.573]  
[16:26:39.574]  [00:00:25.535][detail][DMG] <RE:Run> Cluster 33, Attribute 5 is dirty
[16:26:39.575]  
[16:26:39.575]  [00:00:25.536][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:26:39.576]  
[16:26:39.576]  [00:00:25.537][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:26:39.578]  
[16:26:39.578]  [00:00:25.539][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:26:39.579]  
[16:26:39.580]  [00:00:25.540][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:39.580]  
[16:26:39.581]  [00:00:25.541][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:39.582]  
[16:26:39.582]  [00:00:25.541][detail][DMG] <RE:Run> Cluster 33, Attribute fff8 is dirty
[16:26:39.583]  [00:00:25.542][detail][DMG] <RE:Run> Cluster 33, Attribute fff9 is dirty
[16:26:39.584]  
[16:26:39.584]  [00:00:25.544][detail][DMG] <RE:Run> Cluster 30, Attribute 0 is dirty
[16:26:39.584]  [00:00:25.545][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:39.586]  
[16:26:39.586]  [00:00:25.546][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:39.587]  
[16:26:39.588]  [00:00:25.547][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:39.589]  
[16:26:39.589]  [00:00:25.548][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:39.591]  
[16:26:39.591]  [00:00:25.550][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:39.592]  
[16:26:39.592]  [00:00:25.552][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:39.593]  
[16:26:39.593]  [00:00:25.553][detail][DMG] <RE:Run> Cluster 30, Attribute fff9 is dirty
[16:26:39.594]  [00:00:25.555][detail][DMG] <RE:Run> Cluster 2b, Attribute 0 is dirty
[16:26:39.595]  [00:00:25.555][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:39.596]  [00:00:25.557][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:39.598]  [00:00:25.557][detail][DMG] <RE:Run> Cluster 2b, Attribute fffc is dirty
[16:26:39.598]  [00:00:25.559][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:39.600]  [00:00:25.560][detail][DMG] <RE:Run> Cluster 2b, Attribute fff9 is dirty
[16:26:39.600]  [00:00:25.562][detail][DMG] <RE:Run> Cluster 28, Attribute 0 is dirty
[16:26:39.601]  [00:00:25.563][detail][DMG] <RE:Run> Cluster 28, Attribute 1 is dirty
[16:26:39.603]  [00:00:25.565][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:39.603]  [00:00:25.568][info  ][EM] <<< [E:4276r S:25599 M:83709793 (Ack:47048211)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1207)
[16:26:39.606]  [00:00:25.569][info  ][EM] ??1 [E:4276r S:25599 M:83709793] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3354ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:39.608]  [00:00:25.569][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:39.609]  [00:00:25.570][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:40.165]  [00:00:26.137][detail][IN] UDP Message Received packet nb : 13 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:40.168]  [00:00:26.140][info  ][EM] >>> [E:4276r S:25599 M:47048212 (Ack:83709793)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:40.169]  [00:00:26.140][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:40.170]  [00:00:26.140][detail][EM] Rxd Ack; Removing MessageCounter:83709793 from Retrans Table on exchange 4276r
[16:26:40.171]  [00:00:26.141][info  ][IM] Received status response, status is 0x00
[16:26:40.172]  [00:00:26.141][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:40.172]  [00:00:26.141][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:40.173]  [00:00:26.141][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:40.175]  
[16:26:40.175]  [00:00:26.141][detail][DMG] <RE:Run> Cluster 28, Attribute 1 is dirty
[16:26:40.176]  [00:00:26.142][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:40.177]  
[16:26:40.177]  [00:00:26.143][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:26:40.178]  [00:00:26.143][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:40.179]  
[16:26:40.179]  [00:00:26.144][detail][DMG] <RE:Run> Cluster 28, Attribute 3 is dirty
[16:26:40.181]  
[16:26:40.181]  [00:00:26.145][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:40.182]  
[16:26:40.182]  [00:00:26.145][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:26:40.183]  [00:00:26.146][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:40.184]  
[16:26:40.184]  [00:00:26.146][detail][DMG] <RE:Run> Cluster 28, Attribute 5 is dirty
[16:26:40.185]  [00:00:26.147][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:26:40.186]  
[16:26:40.186]  [00:00:26.148][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:26:40.188]  
[16:26:40.188]  [00:00:26.149][detail][DMG] <RE:Run> Cluster 28, Attribute 7 is dirty
[16:26:40.189]  [00:00:26.151][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:26:40.191]  
[16:26:40.191]  [00:00:26.151][detail][DMG] <RE:Run> Cluster 28, Attribute 9 is dirty
[16:26:40.191]  
[16:26:40.191]  [00:00:26.153][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:26:40.193]  
[16:26:40.193]  [00:00:26.154][detail][DMG] <RE:Run> Cluster 28, Attribute 13 is dirty
[16:26:40.193]  
[16:26:40.194]  [00:00:26.156][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:26:40.195]  
[16:26:40.195]  [00:00:26.156][detail][DMG] <RE:Run> Cluster 28, Attribute 16 is dirty
[16:26:40.196]  
[16:26:40.196]  [00:00:26.158][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:26:40.197]  
[16:26:40.197]  [00:00:26.158][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0028, attributeId: 0x0000_000Berr = 2f
[16:26:40.200]  [00:00:26.159][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000C (expanded=1)
[16:26:40.200]  
[16:26:40.201]  [00:00:26.161][detail][DMG] <RE:Run> Cluster 28, Attribute e is dirty
[16:26:40.202]  
[16:26:40.202]  [00:00:26.162][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:26:40.203]  
[16:26:40.203]  [00:00:26.164][detail][DMG] <RE:Run> Cluster 28, Attribute 10 is dirty
[16:26:40.204]  
[16:26:40.204]  [00:00:26.165][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:26:40.205]  
[16:26:40.206]  [00:00:26.166][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0012 (expanded=1)
[16:26:40.207]  
[16:26:40.207]  [00:00:26.166][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:40.209]  
[16:26:40.209]  [00:00:26.168][detail][DMG] <RE:Run> Cluster 28, Attribute fff8 is dirty
[16:26:40.209]  
[16:26:40.209]  [00:00:26.169][detail][DMG] <RE:Run> Cluster 28, Attribute fff9 is dirty
[16:26:40.211]  [00:00:26.171][detail][DMG] <RE:Run> Cluster 1f, Attribute 0 is dirty
[16:26:40.211]  [00:00:26.172][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:40.213]  
[16:26:40.213]  [00:00:26.173][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:40.214]  [00:00:26.174][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:40.215]  [00:00:26.176][detail][DMG] <RE:Run> Cluster 1f, Attribute fffc is dirty
[16:26:40.216]  [00:00:26.176][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:40.218]  [00:00:26.179][detail][DMG] <RE:Run> Cluster 1f, Attribute fff9 is dirty
[16:26:40.218]  [00:00:26.180][detail][DMG] <RE:Run> Cluster 1f, Attribute fffb is dirty
[16:26:40.219]  [00:00:26.181][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:40.220]  [00:00:26.183][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:40.222]  [00:00:26.183][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_001D, attributeId: 0x0000_0001, err = b
[16:26:40.223]  [00:00:26.184][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:26:40.224]  [00:00:26.187][info  ][EM] <<< [E:4276r S:25599 M:83709794 (Ack:47048212)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1202)
[16:26:40.227]  [00:00:26.189][info  ][EM] ??1 [E:4276r S:25599 M:83709794] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3358ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:40.229]  [00:00:26.189][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:40.229]  [00:00:26.189][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:40.320]  
[16:26:40.671]  [00:00:26.643][detail][IN] UDP Message Received packet nb : 14 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:40.673]  [00:00:26.645][info  ][EM] >>> [E:4276r S:25599 M:47048213 (Ack:83709794)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:40.675]  [00:00:26.645][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:40.676]  [00:00:26.646][detail][EM] Rxd Ack; Removing MessageCounter:83709794 from Retrans Table on exchange 4276r
[16:26:40.677]  [00:00:26.646][info  ][IM] Received status response, status is 0x00
[16:26:40.678]  [00:00:26.646][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:40.678]  [00:00:26.646][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:40.679]  [00:00:26.647][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:40.681]  
[16:26:40.681]  [00:00:26.647][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:26:40.682]  [00:00:26.648][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:40.683]  [00:00:26.649][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:26:40.684]  [00:00:26.649][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:40.685]  
[16:26:40.685]  [00:00:26.650][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:40.686]  [00:00:26.650][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:40.687]  [00:00:26.651][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:26:40.688]  [00:00:26.652][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:40.689]  
[16:26:40.689]  [00:00:26.652][detail][DMG] <RE:Run> Cluster 1d, Attribute fffd is dirty
[16:26:40.691]  
[16:26:40.691]  [00:00:26.653][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:40.692]  [00:00:26.654][detail][DMG] <RE:Run> Cluster 1d, Attribute fff9 is dirty
[16:26:40.693]  [00:00:26.655][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:26:40.693]  [00:00:26.656][detail][DMG] <RE:Run> Cluster 31, Attribute 0 is dirty
[16:26:40.694]  [00:00:26.657][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:40.695]  
[16:26:40.695]  [00:00:26.658][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:40.697]  
[16:26:40.697]  [00:00:26.659][detail][DMG] <RE:Run> Cluster 31, Attribute 4 is dirty
[16:26:40.698]  [00:00:26.660][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:40.699]  
[16:26:40.700]  [00:00:26.661][detail][DMG] <RE:Run> Cluster 31, Attribute 5 is dirty
[16:26:40.700]  [00:00:26.663][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:26:40.702]  [00:00:26.664][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:26:40.702]  
[16:26:40.703]  [00:00:26.664][detail][DMG] <RE:Run> Cluster 31, Attribute 2 is dirty
[16:26:40.704]  [00:00:26.666][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:40.705]  
[16:26:40.705]  [00:00:26.666][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[16:26:40.706]  
[16:26:40.706]  [00:00:26.666][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:40.707]  
[16:26:40.707]  [00:00:26.667][detail][DMG] <RE:Run> Cluster 31, Attribute a is dirty
[16:26:40.709]  [00:00:26.669][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:40.709]  
[16:26:40.710]  [00:00:26.670][detail][DMG] <RE:Run> Cluster 31, Attribute fffd is dirty
[16:26:40.711]  [00:00:26.672][detail][DMG] <RE:Run> Cluster 31, Attribute fff9 is dirty
[16:26:40.712]  [00:00:26.673][detail][DMG] <RE:Run> Cluster 31, Attribute fffb is dirty
[16:26:40.712]  [00:00:26.674][detail][DMG] <RE:Run> Cluster 2a, Attribute 0 is dirty
[16:26:40.713]  [00:00:26.676][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:40.714]  
[16:26:40.714]  [00:00:26.676][detail][DMG] <RE:Run> Cluster 2a, Attribute 2 is dirty
[16:26:40.715]  
[16:26:40.716]  [00:00:26.678][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:40.717]  
[16:26:40.717]  [00:00:26.678][detail][DMG] <RE:Run> Cluster 2a, Attribute fffc is dirty
[16:26:40.718]  
[16:26:40.718]  [00:00:26.680][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:40.719]  
[16:26:40.719]  [00:00:26.681][detail][DMG] <RE:Run> Cluster 2a, Attribute fff8 is dirty
[16:26:40.720]  [00:00:26.682][detail][DMG] <RE:Run> Cluster 2a, Attribute fffb is dirty
[16:26:40.721]  [00:00:26.684][detail][DMG] <RE:Run> Cluster 2d, Attribute 0 is dirty
[16:26:40.722]  [00:00:26.684][detail][DMG] Reading attribute: Cluster=0x0000_002D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:40.723]  [00:00:26.685][detail][DMG] <RE:Run> Cluster 2d, Attribute fffc is dirty
[16:26:40.724]  [00:00:26.685][detail][DMG] Reading attribute: Cluster=0x0000_002D Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:40.726]  [00:00:26.687][detail][DMG] <RE:Run> Cluster 2d, Attribute fff8 is dirty
[16:26:40.726]  [00:00:26.688][detail][DMG] <RE:Run> Cluster 2d, Attribute fff9 is dirty
[16:26:40.727]  [00:00:26.690][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_002D, attributeId: 0x0000_FFFB, err = b
[16:26:40.728]  [00:00:26.691][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:40.730]  [00:00:26.693][info  ][EM] <<< [E:4276r S:25599 M:83709795 (Ack:47048213)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1197)
[16:26:40.732]  [00:00:26.695][info  ][EM] ??1 [E:4276r S:25599 M:83709795] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3377ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:40.734]  [00:00:26.695][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:40.735]  [00:00:26.695][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:41.147]  [00:00:27.119][detail][IN] UDP Message Received packet nb : 15 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:41.149]  [00:00:27.121][info  ][EM] >>> [E:4276r S:25599 M:47048214 (Ack:83709795)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:41.150]  [00:00:27.122][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:41.151]  [00:00:27.122][detail][EM] Rxd Ack; Removing MessageCounter:83709795 from Retrans Table on exchange 4276r
[16:26:41.152]  [00:00:27.122][info  ][IM] Received status response, status is 0x00
[16:26:41.153]  [00:00:27.122][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:41.154]  [00:00:27.123][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:41.154]  [00:00:27.123][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:41.156]  [00:00:27.123][detail][DMG] <RE:Run> Cluster 2d, Attribute fffb is dirty
[16:26:41.157]  [00:00:27.125][detail][DMG] <RE:Run> Cluster 2f, Attribute 0 is dirty
[16:26:41.158]  [00:00:27.125][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:41.159]  
[16:26:41.159]  [00:00:27.125][detail][DMG] <RE:Run> Cluster 2f, Attribute 1 is dirty
[16:26:41.160]  
[16:26:41.160]  [00:00:27.126][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:41.161]  
[16:26:41.162]  [00:00:27.126][detail][DMG] <RE:Run> Cluster 2f, Attribute 2 is dirty
[16:26:41.163]  
[16:26:41.163]  [00:00:27.127][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:41.164]  
[16:26:41.164]  [00:00:27.127][detail][DMG] <RE:Run> Cluster 2f, Attribute e is dirty
[16:26:41.165]  
[16:26:41.165]  [00:00:27.128][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:26:41.166]  
[16:26:41.167]  [00:00:27.128][detail][DMG] <RE:Run> Cluster 2f, Attribute f is dirty
[16:26:41.167]  [00:00:27.129][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_000F (expanded=1)
[16:26:41.169]  [00:00:27.130][detail][DMG] <RE:Run> Cluster 2f, Attribute 10 is dirty
[16:26:41.169]  [00:00:27.130][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:26:41.171]  [00:00:27.131][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_001A (expanded=1)
[16:26:41.172]  [00:00:27.133][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_001C (expanded=1)
[16:26:41.173]  
[16:26:41.174]  [00:00:27.134][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_001F (expanded=1)
[16:26:41.174]  
[16:26:41.175]  [00:00:27.135][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:41.176]  
[16:26:41.176]  [00:00:27.136][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:41.178]  
[16:26:41.178]  [00:00:27.138][detail][DMG] <RE:Run> Cluster 2f, Attribute fff9 is dirty
[16:26:41.179]  [00:00:27.140][detail][DMG] <RE:Run> Cluster 35, Attribute 0 is dirty
[16:26:41.179]  [00:00:27.141][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:41.181]  [00:00:27.142][detail][DMG] <RE:Run> Cluster 35, Attribute 1 is dirty
[16:26:41.181]  [00:00:27.143][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:41.183]  [00:00:27.144][detail][DMG] <RE:Run> Cluster 35, Attribute 2 is dirty
[16:26:41.183]  [00:00:27.145][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:41.185]  
[16:26:41.185]  [00:00:27.146][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:41.186]  
[16:26:41.186]  [00:00:27.148][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:26:41.188]  [00:00:27.150][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:26:41.189]  
[16:26:41.189]  [00:00:27.151][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:26:41.190]  [00:00:27.152][detail][DMG] <RE:Run> Cluster 35, Attribute 7 is dirty
[16:26:41.191]  
[16:26:41.192]  [00:00:27.153][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:26:41.192]  [00:00:27.154][detail][DMG] <RE:Run> Cluster 35, Attribute 8 is dirty
[16:26:41.193]  [00:00:27.155][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:26:41.194]  
[16:26:41.195]  [00:00:27.156][detail][DMG] <RE:Run> Cluster 35, Attribute 9 is dirty
[16:26:41.196]  [00:00:27.157][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:26:41.197]  [00:00:27.159][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:26:41.198]  
[16:26:41.199]  [00:00:27.160][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:26:41.200]  
[16:26:41.200]  [00:00:27.161][detail][DMG] <RE:Run> Cluster 35, Attribute c is dirty
[16:26:41.201]  [00:00:27.163][detail][DMG] <RE:Run> Cluster 35, Attribute d is dirty
[16:26:41.201]  [00:00:27.164][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000D (expanded=1)
[16:26:41.203]  [00:00:27.165][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:26:41.204]  [00:00:27.166][detail][DMG] <RE:Run> Cluster 35, Attribute f is dirty
[16:26:41.205]  
[16:26:41.205]  [00:00:27.166][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000F (expanded=1)
[16:26:41.206]  [00:00:27.168][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:26:41.208]  
[16:26:41.208]  [00:00:27.169][detail][DMG] <RE:Run> Cluster 35, Attribute 11 is dirty
[16:26:41.208]  [00:00:27.170][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0011 (expanded=1)
[16:26:41.210]  [00:00:27.171][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0012 (expanded=1)
[16:26:41.211]  [00:00:27.173][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0013 (expanded=1)
[16:26:41.213]  [00:00:27.174][detail][DMG] <RE:Run> Cluster 35, Attribute 14 is dirty
[16:26:41.213]  [00:00:27.175][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0014 (expanded=1)
[16:26:41.215]  [00:00:27.176][detail][DMG] <RE:Run> Cluster 35, Attribute 15 is dirty
[16:26:41.215]  [00:00:27.176][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:26:41.217]  [00:00:27.178][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0016 (expanded=1)
[16:26:41.218]  [00:00:27.179][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0035, attributeId: 0x0000_0016, err = b
[16:26:41.220]  [00:00:27.182][info  ][EM] <<< [E:4276r S:25599 M:83709796 (Ack:47048214)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1205)
[16:26:41.222]  [00:00:27.185][info  ][EM] ??1 [E:4276r S:25599 M:83709796] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3410ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:41.224]  [00:00:27.186][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:41.224]  [00:00:27.187][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:41.648]  [00:00:27.620][detail][IN] UDP Message Received packet nb : 16 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:41.650]  [00:00:27.622][info  ][EM] >>> [E:4276r S:25599 M:47048215 (Ack:83709796)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:41.651]  [00:00:27.622][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:41.652]  [00:00:27.622][detail][EM] Rxd Ack; Removing MessageCounter:83709796 from Retrans Table on exchange 4276r
[16:26:41.653]  [00:00:27.623][info  ][IM] Received status response, status is 0x00
[16:26:41.654]  [00:00:27.623][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:41.655]  [00:00:27.623][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:41.655]  [00:00:27.623][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:41.657]  [00:00:27.624][detail][DMG] <RE:Run> Cluster 35, Attribute 16 is dirty
[16:26:41.658]  [00:00:27.625][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0016 (expanded=1)
[16:26:41.659]  [00:00:27.625][detail][DMG] <RE:Run> Cluster 35, Attribute 17 is dirty
[16:26:41.660]  [00:00:27.626][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0017 (expanded=1)
[16:26:41.661]  [00:00:27.626][detail][DMG] <RE:Run> Cluster 35, Attribute 18 is dirty
[16:26:41.662]  [00:00:27.628][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0018 (expanded=1)
[16:26:41.664]  [00:00:27.628][detail][DMG] <RE:Run> Cluster 35, Attribute 19 is dirty
[16:26:41.664]  [00:00:27.629][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0019 (expanded=1)
[16:26:41.666]  [00:00:27.630][detail][DMG] <RE:Run> Cluster 35, Attribute 1a is dirty
[16:26:41.666]  [00:00:27.631][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001A (expanded=1)
[16:26:41.668]  [00:00:27.632][detail][DMG] <RE:Run> Cluster 35, Attribute 1b is dirty
[16:26:41.668]  [00:00:27.633][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001B (expanded=1)
[16:26:41.670]  [00:00:27.633][detail][DMG] <RE:Run> Cluster 35, Attribute 1c is dirty
[16:26:41.670]  [00:00:27.634][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001C (expanded=1)
[16:26:41.671]  
[16:26:41.672]  [00:00:27.635][detail][DMG] <RE:Run> Cluster 35, Attribute 1d is dirty
[16:26:41.672]  [00:00:27.636][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001D (expanded=1)
[16:26:41.674]  [00:00:27.637][detail][DMG] <RE:Run> Cluster 35, Attribute 1e is dirty
[16:26:41.675]  [00:00:27.638][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001E (expanded=1)
[16:26:41.676]  [00:00:27.639][detail][DMG] <RE:Run> Cluster 35, Attribute 1f is dirty
[16:26:41.677]  
[16:26:41.677]  [00:00:27.639][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001F (expanded=1)
[16:26:41.678]  [00:00:27.640][detail][DMG] <RE:Run> Cluster 35, Attribute 20 is dirty
[16:26:41.679]  [00:00:27.641][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0020 (expanded=1)
[16:26:41.680]  
[16:26:41.680]  [00:00:27.642][detail][DMG] <RE:Run> Cluster 35, Attribute 21 is dirty
[16:26:41.681]  [00:00:27.643][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0021 (expanded=1)
[16:26:41.682]  [00:00:27.645][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0022 (expanded=1)
[16:26:41.684]  
[16:26:41.684]  [00:00:27.645][detail][DMG] <RE:Run> Cluster 35, Attribute 23 is dirty
[16:26:41.684]  [00:00:27.646][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0023 (expanded=1)
[16:26:41.686]  [00:00:27.647][detail][DMG] <RE:Run> Cluster 35, Attribute 24 is dirty
[16:26:41.686]  [00:00:27.648][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0024 (expanded=1)
[16:26:41.688]  
[16:26:41.688]  [00:00:27.650][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0025 (expanded=1)
[16:26:41.689]  [00:00:27.651][detail][DMG] <RE:Run> Cluster 35, Attribute 26 is dirty
[16:26:41.690]  
[16:26:41.691]  [00:00:27.652][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0026 (expanded=1)
[16:26:41.692]  [00:00:27.653][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0027 (expanded=1)
[16:26:41.693]  
[16:26:41.693]  [00:00:27.654][detail][DMG] <RE:Run> Cluster 35, Attribute 28 is dirty
[16:26:41.694]  [00:00:27.655][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0028 (expanded=1)
[16:26:41.695]  
[16:26:41.695]  [00:00:27.657][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0029 (expanded=1)
[16:26:41.697]  [00:00:27.658][detail][DMG] <RE:Run> Cluster 35, Attribute 2a is dirty
[16:26:41.697]  [00:00:27.658][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002A (expanded=1)
[16:26:41.699]  
[16:26:41.699]  [00:00:27.659][detail][DMG] <RE:Run> Cluster 35, Attribute 2b is dirty
[16:26:41.700]  [00:00:27.661][detail][DMG] <RE:Run> Cluster 35, Attribute 2c is dirty
[16:26:41.700]  [00:00:27.662][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002C (expanded=1)
[16:26:41.702]  [00:00:27.664][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002D (expanded=1)
[16:26:41.703]  [00:00:27.664][detail][DMG] <RE:Run> Cluster 35, Attribute 2e is dirty
[16:26:41.704]  
[16:26:41.704]  [00:00:27.666][detail][DMG] <RE:Run> Cluster 35, Attribute 2f is dirty
[16:26:41.705]  [00:00:27.666][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002F (expanded=1)
[16:26:41.706]  [00:00:27.668][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0030 (expanded=1)
[16:26:41.707]  
[16:26:41.708]  [00:00:27.669][detail][DMG] <RE:Run> Cluster 35, Attribute 31 is dirty
[16:26:41.709]  [00:00:27.670][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0031 (expanded=1)
[16:26:41.709]  [00:00:27.671][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0032 (expanded=1)
[16:26:41.711]  [00:00:27.672][detail][DMG] <RE:Run> Cluster 35, Attribute 33 is dirty
[16:26:41.711]  [00:00:27.673][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0033 (expanded=1)
[16:26:41.713]  [00:00:27.674][detail][DMG] <RE:Run> Cluster 35, Attribute 34 is dirty
[16:26:41.714]  
[16:26:41.714]  [00:00:27.675][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0034 (expanded=1)
[16:26:41.716]  [00:00:27.677][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0035 (expanded=1)
[16:26:41.716]  [00:00:27.678][detail][DMG] <RE:Run> Cluster 35, Attribute 36 is dirty
[16:26:41.718]  [00:00:27.679][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0036 (expanded=1)
[16:26:41.718]  [00:00:27.680][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0037 (expanded=1)
[16:26:41.720]  [00:00:27.681][detail][DMG] <RE:Run> Cluster 35, Attribute 38 is dirty
[16:26:41.720]  [00:00:27.682][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0038 (expanded=1)
[16:26:41.722]  [00:00:27.683][detail][DMG] <RE:Run> Cluster 35, Attribute 39 is dirty
[16:26:41.723]  [00:00:27.684][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0039 (expanded=1)
[16:26:41.724]  
[16:26:41.724]  [00:00:27.686][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003A (expanded=1)
[16:26:41.725]  
[16:26:41.726]  [00:00:27.687][detail][DMG] <RE:Run> Cluster 35, Attribute 3b is dirty
[16:26:41.727]  
[16:26:41.727]  [00:00:27.688][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003B (expanded=1)
[16:26:41.728]  
[16:26:41.728]  [00:00:27.689][detail][DMG] <RE:Run> Cluster 35, Attribute 3c is dirty
[16:26:41.729]  [00:00:27.690][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003C (expanded=1)
[16:26:41.730]  [00:00:27.691][detail][DMG] <RE:Run> Cluster 35, Attribute 3d is dirty
[16:26:41.731]  [00:00:27.692][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003D (expanded=1)
[16:26:41.732]  [00:00:27.694][detail][DMG] <RE:Run> Cluster 35, Attribute 3e is dirty
[16:26:41.733]  [00:00:27.695][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003E (expanded=1)
[16:26:41.734]  [00:00:27.695][detail][DMG] <RE:Run> Cluster 35, Attribute fffc is dirty
[16:26:41.735]  [00:00:27.697][detail][DMG] <RE:Run> Cluster 35, Attribute fffd is dirty
[16:26:41.736]  [00:00:27.698][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0035, attributeId: 0x0000_FFFD, err = b
[16:26:41.738]  [00:00:27.699][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:41.738]  [00:00:27.702][info  ][EM] <<< [E:4276r S:25599 M:83709797 (Ack:47048215)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1185)
[16:26:41.741]  [00:00:27.703][info  ][EM] ??1 [E:4276r S:25599 M:83709797] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:41.743]  [00:00:27.704][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:41.744]  [00:00:27.704][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:42.155]  [00:00:28.126][detail][IN] UDP Message Received packet nb : 17 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:42.157]  [00:00:28.128][info  ][EM] >>> [E:4276r S:25599 M:47048216 (Ack:83709797)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:42.158]  [00:00:28.129][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:42.160]  [00:00:28.129][detail][EM] Rxd Ack; Removing MessageCounter:83709797 from Retrans Table on exchange 4276r
[16:26:42.160]  [00:00:28.129][info  ][IM] Received status response, status is 0x00
[16:26:42.161]  [00:00:28.129][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:42.162]  [00:00:28.130][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:42.162]  [00:00:28.130][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:42.164]  [00:00:28.130][detail][DMG] <RE:Run> Cluster 35, Attribute fffd is dirty
[16:26:42.165]  [00:00:28.132][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:42.166]  [00:00:28.132][detail][DMG] <RE:Run> Cluster 35, Attribute fff8 is dirty
[16:26:42.167]  [00:00:28.135][detail][DMG] <RE:Run> Cluster 35, Attribute fff9 is dirty
[16:26:42.168]  [00:00:28.136][detail][DMG] <RE:Run> Cluster 35, Attribute fffb is dirty
[16:26:42.169]  [00:00:28.138][detail][DMG] <RE:Run> Cluster 46, Attribute 0 is dirty
[16:26:42.169]  [00:00:28.139][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:26:42.171]  [00:00:28.139][detail][DMG] <RE:Run> Cluster 46, Attribute 1 is dirty
[16:26:42.171]  [00:00:28.140][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:42.173]  [00:00:28.140][detail][DMG] <RE:Run> Cluster 46, Attribute 2 is dirty
[16:26:42.173]  [00:00:28.141][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:26:42.175]  [00:00:28.141][detail][DMG] <RE:Run> Cluster 46, Attribute fffc is dirty
[16:26:42.176]  [00:00:28.142][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:26:42.177]  
[16:26:42.177]  [00:00:28.143][detail][DMG] <RE:Run> Cluster 46, Attribute fffd is dirty
[16:26:42.178]  
[16:26:42.178]  [00:00:28.143][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:26:42.180]  
[16:26:42.180]  [00:00:28.144][detail][DMG] <RE:Run> Cluster 46, Attribute fff8 is dirty
[16:26:42.180]  
[16:26:42.180]  [00:00:28.145][detail][DMG] <RE:Run> Cluster 46, Attribute fff9 is dirty
[16:26:42.181]  
[16:26:42.182]  [00:00:28.145][detail][DMG] <RE:Run> Cluster 46, Attribute fffb is dirty
[16:26:42.182]  
[16:26:42.182]  [00:00:28.147][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:42.183]  
[16:26:42.184]  [00:00:28.147][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:26:42.185]  
[16:26:42.185]  [00:00:28.147][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:26:42.186]  
[16:26:42.186]  [00:00:28.148][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:26:42.187]  
[16:26:42.187]  [00:00:28.148][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:26:42.188]  
[16:26:42.189]  [00:00:28.150][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:26:42.189]  [00:00:28.151][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_FFFD (expanded=1)
[16:26:42.191]  
[16:26:42.191]  [00:00:28.152][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:26:42.191]  [00:00:28.154][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:26:42.193]  [00:00:28.154][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:26:42.194]  [00:00:28.155][detail][DMG] <RE:Run> Cluster 3, Attribute fffd is dirty
[16:26:42.195]  [00:00:28.157][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:42.196]  [00:00:28.158][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:26:42.196]  [00:00:28.159][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:26:42.198]  [00:00:28.161][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:26:42.198]  [00:00:28.161][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:26:42.199]  [00:00:28.162][detail][DMG] List does not fit in packet, chunk between list items for clusterId: 0x0000_0004, attributeId: 0x0000_FFFB
[16:26:42.200]  [00:00:28.166][info  ][EM] <<< [E:4276r S:25599 M:83709798 (Ack:47048216)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1209)
[16:26:42.203]  [00:00:28.166][info  ][EM] ??1 [E:4276r S:25599 M:83709798] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3391ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:42.205]  [00:00:28.167][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:42.206]  [00:00:28.167][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:42.320]  
[16:26:43.156]  [00:00:29.127][detail][IN] UDP Message Received packet nb : 18 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:43.158]  [00:00:29.129][info  ][EM] >>> [E:4276r S:25599 M:47048217 (Ack:83709798)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:43.159]  [00:00:29.130][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:43.161]  [00:00:29.130][detail][EM] Rxd Ack; Removing MessageCounter:83709798 from Retrans Table on exchange 4276r
[16:26:43.161]  [00:00:29.130][info  ][IM] Received status response, status is 0x00
[16:26:43.162]  [00:00:29.130][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:43.163]  [00:00:29.130][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:43.164]  
[16:26:43.164]  [00:00:29.131][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:43.166]  
[16:26:43.166]  [00:00:29.131][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:26:43.166]  
[16:26:43.167]  [00:00:29.132][detail][DMG] <RE:Run> Cluster 102, Attribute 0 is dirty
[16:26:43.168]  
[16:26:43.168]  [00:00:29.133][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.169]  
[16:26:43.169]  [00:00:29.133][detail][DMG] <RE:Run> Cluster 102, Attribute 1 is dirty
[16:26:43.170]  
[16:26:43.170]  [00:00:29.133][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:26:43.171]  
[16:26:43.172]  [00:00:29.134][detail][DMG] <RE:Run> Cluster 102, Attribute 3 is dirty
[16:26:43.172]  
[16:26:43.172]  [00:00:29.134][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0003 (expanded=1)
[16:26:43.174]  
[16:26:43.174]  [00:00:29.135][detail][DMG] <RE:Run> Cluster 102, Attribute 5 is dirty
[16:26:43.175]  
[16:26:43.175]  [00:00:29.135][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0005 (expanded=1)
[16:26:43.177]  
[16:26:43.177]  [00:00:29.136][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0007 (expanded=1)
[16:26:43.178]  
[16:26:43.178]  [00:00:29.138][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000A (expanded=1)
[16:26:43.179]  
[16:26:43.179]  [00:00:29.139][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000B (expanded=1)
[16:26:43.181]  
[16:26:43.181]  [00:00:29.140][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000D (expanded=1)
[16:26:43.182]  
[16:26:43.182]  [00:00:29.141][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0010 (expanded=1)
[16:26:43.184]  
[16:26:43.184]  [00:00:29.142][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0011 (expanded=1)
[16:26:43.185]  
[16:26:43.186]  [00:00:29.144][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_001A (expanded=1)
[16:26:43.186]  
[16:26:43.187]  [00:00:29.145][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:26:43.188]  
[16:26:43.188]  [00:00:29.147][detail][DMG] <RE:Run> Cluster 102, Attribute fff9 is dirty
[16:26:43.189]  [00:00:29.148][detail][DMG] <RE:Run> Cluster 102, Attribute fffb is dirty
[16:26:43.190]  [00:00:29.149][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.191]  [00:00:29.151][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0002 (expanded=1)
[16:26:43.193]  [00:00:29.152][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:26:43.194]  [00:00:29.154][detail][DMG] <RE:Run> Cluster 1d, Attribute fff9 is dirty
[16:26:43.195]  [00:00:29.155][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.196]  [00:00:29.157][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:26:43.197]  [00:00:29.158][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:43.198]  [00:00:29.160][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:43.199]  [00:00:29.162][info  ][EM] <<< [E:4276r S:25599 M:83709799 (Ack:47048217)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1185)
[16:26:43.202]  [00:00:29.164][info  ][EM] ??1 [E:4276r S:25599 M:83709799] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3352ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:43.204]  [00:00:29.164][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:43.204]  [00:00:29.164][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:43.646]  [00:00:29.618][detail][IN] UDP Message Received packet nb : 19 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:43.648]  [00:00:29.620][info  ][EM] >>> [E:4276r S:25599 M:47048218 (Ack:83709799)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:43.649]  [00:00:29.621][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:43.651]  [00:00:29.621][detail][EM] Rxd Ack; Removing MessageCounter:83709799 from Retrans Table on exchange 4276r
[16:26:43.651]  [00:00:29.621][info  ][IM] Received status response, status is 0x00
[16:26:43.652]  [00:00:29.621][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:43.653]  
[16:26:43.653]  [00:00:29.622][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:43.654]  
[16:26:43.654]  [00:00:29.622][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:43.655]  
[16:26:43.656]  [00:00:29.622][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:43.657]  
[16:26:43.657]  [00:00:29.623][detail][DMG] <RE:Run> Cluster 3, Attribute fffb is dirty
[16:26:43.657]  
[16:26:43.657]  [00:00:29.623][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:26:43.658]  
[16:26:43.659]  [00:00:29.624][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.660]  
[16:26:43.660]  [00:00:29.624][detail][DMG] <RE:Run> Cluster 4, Attribute fffc is dirty
[16:26:43.661]  
[16:26:43.661]  [00:00:29.624][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:26:43.662]  
[16:26:43.662]  [00:00:29.625][detail][DMG] <RE:Run> Cluster 4, Attribute fffd is dirty
[16:26:43.664]  
[16:26:43.664]  [00:00:29.625][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x2 AttributeId=0x0000_FFFD (expanded=1)
[16:26:43.665]  
[16:26:43.665]  [00:00:29.625][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:26:43.666]  
[16:26:43.666]  [00:00:29.627][detail][DMG] <RE:Run> Cluster 102, Attribute 0 is dirty
[16:26:43.667]  
[16:26:43.667]  [00:00:29.628][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0001 (expanded=1)
[16:26:43.668]  
[16:26:43.668]  [00:00:29.629][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0003 (expanded=1)
[16:26:43.670]  
[16:26:43.670]  [00:00:29.630][detail][DMG] <RE:Run> Cluster 102, Attribute 7 is dirty
[16:26:43.671]  [00:00:29.631][detail][DMG] <RE:Run> Cluster 102, Attribute 8 is dirty
[16:26:43.671]  [00:00:29.633][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000A (expanded=1)
[16:26:43.673]  
[16:26:43.673]  [00:00:29.633][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000B (expanded=1)
[16:26:43.674]  
[16:26:43.675]  [00:00:29.635][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000E (expanded=1)
[16:26:43.675]  
[16:26:43.676]  [00:00:29.636][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0010 (expanded=1)
[16:26:43.677]  
[16:26:43.677]  [00:00:29.638][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0017 (expanded=1)
[16:26:43.679]  
[16:26:43.679]  [00:00:29.639][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_001A (expanded=1)
[16:26:43.680]  
[16:26:43.680]  [00:00:29.640][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:26:43.682]  [00:00:29.641][detail][DMG] <RE:Run> Cluster 102, Attribute fff8 is dirty
[16:26:43.682]  [00:00:29.643][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:43.683]  [00:00:29.644][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.684]  [00:00:29.644][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:26:43.685]  [00:00:29.646][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:26:43.686]  [00:00:29.648][detail][DMG] <RE:Run> Cluster 1d, Attribute fffd is dirty
[16:26:43.686]  [00:00:29.649][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:26:43.688]  [00:00:29.650][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:26:43.689]  [00:00:29.652][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:26:43.690]  [00:00:29.655][info  ][EM] <<< [E:4276r S:25599 M:83709800 (Ack:47048218)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1207)
[16:26:43.693]  [00:00:29.656][info  ][EM] ??1 [E:4276r S:25599 M:83709800] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3404ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:43.694]  [00:00:29.657][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:43.695]  [00:00:29.657][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:44.147]  [00:00:30.119][detail][IN] UDP Message Received packet nb : 20 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:44.149]  [00:00:30.122][info  ][EM] >>> [E:4276r S:25599 M:47048219 (Ack:83709800)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:44.150]  [00:00:30.122][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:44.152]  [00:00:30.122][detail][EM] Rxd Ack; Removing MessageCounter:83709800 from Retrans Table on exchange 4276r
[16:26:44.152]  
[16:26:44.153]  [00:00:30.123][info  ][IM] Received status response, status is 0x00
[16:26:44.154]  
[16:26:44.154]  [00:00:30.123][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:44.154]  [00:00:30.123][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:44.155]  
[16:26:44.155]  [00:00:30.123][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:44.157]  
[16:26:44.157]  [00:00:30.123][detail][DMG] <RE:Run> Cluster 3, Attribute 1 is dirty
[16:26:44.158]  
[16:26:44.158]  [00:00:30.124][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:26:44.159]  
[16:26:44.159]  [00:00:30.124][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:26:44.160]  
[16:26:44.161]  [00:00:30.124][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:26:44.162]  
[16:26:44.162]  [00:00:30.125][detail][DMG] <RE:Run> Cluster 3, Attribute fffd is dirty
[16:26:44.163]  
[16:26:44.163]  [00:00:30.125][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x3 AttributeId=0x0000_FFFD (expanded=1)
[16:26:44.164]  
[16:26:44.164]  [00:00:30.125][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:44.166]  [00:00:30.127][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:26:44.166]  [00:00:30.127][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:26:44.168]  
[16:26:44.168]  [00:00:30.128][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:26:44.169]  
[16:26:44.169]  [00:00:30.129][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:26:44.170]  
[16:26:44.170]  [00:00:30.131][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[16:26:44.170]  
[16:26:44.171]  [00:00:30.132][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_4000 (expanded=1)
[16:26:44.172]  
[16:26:44.172]  [00:00:30.133][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_4001 (expanded=1)
[16:26:44.175]  
[16:26:44.175]  [00:00:30.135][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_4003 (expanded=1)
[16:26:44.176]  
[16:26:44.176]  [00:00:30.136][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:26:44.177]  
[16:26:44.177]  [00:00:30.137][detail][DMG] <RE:Run> Cluster 6, Attribute fff9 is dirty
[16:26:44.178]  
[16:26:44.179]  [00:00:30.138][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:26:44.179]  
[16:26:44.179]  [00:00:30.139][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:26:44.180]  [00:00:30.140][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:26:44.181]  
[16:26:44.181]  [00:00:30.142][detail][DMG] <RE:Run> Cluster 8, Attribute 3 is dirty
[16:26:44.182]  
[16:26:44.183]  [00:00:30.143][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_000F (expanded=1)
[16:26:44.183]  [00:00:30.144][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0010 (expanded=1)
[16:26:44.185]  [00:00:30.145][detail][DMG] <RE:Run> Cluster 8, Attribute 12 is dirty
[16:26:44.185]  [00:00:30.147][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0013 (expanded=1)
[16:26:44.187]  [00:00:30.148][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_4000 (expanded=1)
[16:26:44.188]  [00:00:30.150][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_FFFD (expanded=1)
[16:26:44.190]  [00:00:30.151][detail][DMG] <RE:Run> Cluster 8, Attribute fff9 is dirty
[16:26:44.190]  [00:00:30.152][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:26:44.191]  [00:00:30.153][detail][DMG] List does not fit in packet, chunk between list items for clusterId: 0x0000_0008, attributeId: 0x0000_FFFB
[16:26:44.192]  [00:00:30.154][detail][DMG] Fetched 0 events
[16:26:44.193]  [00:00:30.157][info  ][EM] <<< [E:4276r S:25599 M:83709801 (Ack:47048219)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1207)
[16:26:44.196]  [00:00:30.158][info  ][EM] ??1 [E:4276r S:25599 M:83709801] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3387ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:44.197]  [00:00:30.158][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:44.199]  [00:00:30.158][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:44.319]  
[16:26:44.653]  [00:00:30.625][detail][IN] UDP Message Received packet nb : 21 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:44.655]  [00:00:30.627][info  ][EM] >>> [E:4276r S:25599 M:47048220 (Ack:83709801)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:44.657]  [00:00:30.627][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:44.658]  [00:00:30.628][detail][EM] Rxd Ack; Removing MessageCounter:83709801 from Retrans Table on exchange 4276r
[16:26:44.659]  [00:00:30.628][info  ][IM] Received status response, status is 0x00
[16:26:44.659]  [00:00:30.628][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:44.660]  [00:00:30.628][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:44.661]  
[16:26:44.661]  [00:00:30.628][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:44.663]  
[16:26:44.663]  [00:00:30.629][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:26:44.663]  
[16:26:44.664]  [00:00:30.630][detail][DMG] <RE:Run> Cluster 300, Attribute 0 is dirty
[16:26:44.665]  
[16:26:44.665]  [00:00:30.630][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:26:44.666]  
[16:26:44.666]  [00:00:30.631][detail][DMG] <RE:Run> Cluster 300, Attribute 1 is dirty
[16:26:44.667]  [00:00:30.631][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:26:44.668]  
[16:26:44.668]  [00:00:30.631][detail][DMG] <RE:Run> Cluster 300, Attribute 2 is dirty
[16:26:44.670]  
[16:26:44.670]  [00:00:30.632][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[16:26:44.671]  
[16:26:44.671]  [00:00:30.632][detail][DMG] <RE:Run> Cluster 300, Attribute 8 is dirty
[16:26:44.672]  
[16:26:44.672]  [00:00:30.633][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0008 (expanded=1)
[16:26:44.673]  
[16:26:44.674]  [00:00:30.634][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_000F (expanded=1)
[16:26:44.675]  
[16:26:44.675]  [00:00:30.635][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_4001 (expanded=1)
[16:26:44.677]  
[16:26:44.677]  [00:00:30.636][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_400A (expanded=1)
[16:26:44.678]  [00:00:30.638][detail][DMG] <RE:Run> Cluster 300, Attribute fffd is dirty
[16:26:44.679]  [00:00:30.639][detail][DMG] <RE:Run> Cluster 300, Attribute fff9 is dirty
[16:26:44.680]  [00:00:30.640][detail][DMG] <RE:Run> Cluster 300, Attribute fffb is dirty
[16:26:44.680]  [00:00:30.641][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:26:44.682]  
[16:26:44.682]  [00:00:30.643][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:26:44.682]  
[16:26:44.683]  [00:00:30.644][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0003 (expanded=1)
[16:26:44.684]  
[16:26:44.684]  [00:00:30.645][detail][DMG] <RE:Run> Cluster 1d, Attribute fffd is dirty
[16:26:44.685]  
[16:26:44.685]  [00:00:30.647][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:26:44.686]  [00:00:30.647][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:26:44.687]  
[16:26:44.688]  [00:00:30.650][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:26:44.689]  [00:00:30.653][detail][DMG] <RE:Run> Cluster 3, Attribute fffd is dirty
[16:26:44.689]  [00:00:30.653][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:26:44.691]  [00:00:30.653][detail][DMG] <RE:Run> Cluster 3, Attribute fff8 is dirty
[16:26:44.691]  [00:00:30.654][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:44.693]  [00:00:30.655][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:26:44.693]  [00:00:30.656][detail][DMG] <RE:Run> Cluster 4, Attribute fffc is dirty
[16:26:44.694]  [00:00:30.657][detail][DMG] <RE:Run> Cluster 4, Attribute fff8 is dirty
[16:26:44.695]  [00:00:30.659][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:26:44.696]  [00:00:30.659][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0004, attributeId: 0x0000_FFFB, err = b
[16:26:44.697]  [00:00:30.661][detail][DMG] <RE> Sending report (payload has 1158 bytes)...
[16:26:44.698]  [00:00:30.663][info  ][EM] <<< [E:4276r S:25599 M:83709802 (Ack:47048220)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1192)
[16:26:44.700]  [00:00:30.664][info  ][EM] ??1 [E:4276r S:25599 M:83709802] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3397ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:44.702]  [00:00:30.665][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:44.703]  [00:00:30.665][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:45.150]  [00:00:31.122][detail][IN] UDP Message Received packet nb : 22 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:45.152]  [00:00:31.124][info  ][EM] >>> [E:4276r S:25599 M:47048221 (Ack:83709802)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:45.153]  [00:00:31.125][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:45.155]  [00:00:31.125][detail][EM] Rxd Ack; Removing MessageCounter:83709802 from Retrans Table on exchange 4276r
[16:26:45.156]  [00:00:31.125][info  ][IM] Received status response, status is 0x00
[16:26:45.156]  [00:00:31.125][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:45.157]  
[16:26:45.157]  [00:00:31.125][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:45.158]  
[16:26:45.158]  [00:00:31.125][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:45.160]  
[16:26:45.160]  [00:00:31.125][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:26:45.161]  [00:00:31.126][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[16:26:45.162]  [00:00:31.126][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:26:45.163]  
[16:26:45.163]  [00:00:31.127][detail][DMG] <RE:Run> Cluster 6, Attribute 4000 is dirty
[16:26:45.164]  
[16:26:45.164]  [00:00:31.127][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x4 AttributeId=0x0000_4000 (expanded=1)
[16:26:45.165]  
[16:26:45.165]  [00:00:31.128][detail][DMG] <RE:Run> Cluster 6, Attribute 4001 is dirty
[16:26:45.166]  
[16:26:45.166]  [00:00:31.128][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x4 AttributeId=0x0000_4001 (expanded=1)
[16:26:45.168]  
[16:26:45.168]  [00:00:31.128][detail][DMG] <RE:Run> Cluster 6, Attribute 4002 is dirty
[16:26:45.169]  
[16:26:45.169]  [00:00:31.129][detail][DMG] <RE:Run> Cluster 6, Attribute 4003 is dirty
[16:26:45.170]  
[16:26:45.170]  [00:00:31.130][detail][DMG] <RE:Run> Cluster 6, Attribute fffc is dirty
[16:26:45.171]  
[16:26:45.171]  [00:00:31.133][detail][DMG] <RE:Run> Cluster 6, Attribute fff9 is dirty
[16:26:45.171]  
[16:26:45.172]  [00:00:31.133][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:26:45.173]  
[16:26:45.173]  [00:00:31.134][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:26:45.173]  
[16:26:45.173]  [00:00:31.135][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0001 (expanded=1)
[16:26:45.175]  
[16:26:45.175]  [00:00:31.136][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0002 (expanded=1)
[16:26:45.176]  
[16:26:45.177]  [00:00:31.138][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_000F (expanded=1)
[16:26:45.178]  
[16:26:45.178]  [00:00:31.139][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0010 (expanded=1)
[16:26:45.180]  
[16:26:45.180]  [00:00:31.140][detail][DMG] <RE:Run> Cluster 8, Attribute 12 is dirty
[16:26:45.180]  
[16:26:45.180]  [00:00:31.142][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0013 (expanded=1)
[16:26:45.182]  
[16:26:45.182]  [00:00:31.143][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0014 (expanded=1)
[16:26:45.183]  
[16:26:45.184]  [00:00:31.144][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_4000 (expanded=1)
[16:26:45.184]  
[16:26:45.185]  [00:00:31.145][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:26:45.187]  [00:00:31.145][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:26:45.187]  [00:00:31.147][detail][DMG] <RE:Run> Cluster 8, Attribute fff9 is dirty
[16:26:45.189]  [00:00:31.148][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:26:45.189]  [00:00:31.149][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:26:45.191]  [00:00:31.151][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0003 (expanded=1)
[16:26:45.191]  [00:00:31.153][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_FFFD (expanded=1)
[16:26:45.193]  [00:00:31.154][detail][DMG] <RE:Run> Cluster 1d, Attribute fff9 is dirty
[16:26:45.194]  [00:00:31.155][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:26:45.195]  [00:00:31.156][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:26:45.196]  [00:00:31.160][info  ][EM] <<< [E:4276r S:25599 M:83709803 (Ack:47048221)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1185)
[16:26:45.198]  [00:00:31.161][info  ][EM] ??1 [E:4276r S:25599 M:83709803] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:45.200]  [00:00:31.162][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:45.201]  [00:00:31.162][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:45.660]  [00:00:31.631][detail][IN] UDP Message Received packet nb : 23 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:45.662]  [00:00:31.633][info  ][EM] >>> [E:4276r S:25599 M:47048222 (Ack:83709803)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:45.663]  [00:00:31.634][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:45.664]  [00:00:31.634][detail][EM] Rxd Ack; Removing MessageCounter:83709803 from Retrans Table on exchange 4276r
[16:26:45.665]  
[16:26:45.666]  [00:00:31.634][info  ][IM] Received status response, status is 0x00
[16:26:45.667]  
[16:26:45.667]  [00:00:31.635][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:45.667]  [00:00:31.635][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:45.668]  
[16:26:45.668]  [00:00:31.635][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:45.670]  
[16:26:45.670]  [00:00:31.635][detail][DMG] <RE:Run> Cluster 3, Attribute 1 is dirty
[16:26:45.671]  [00:00:31.635][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:26:45.672]  
[16:26:45.672]  [00:00:31.636][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:26:45.673]  
[16:26:45.673]  [00:00:31.636][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:26:45.674]  
[16:26:45.675]  [00:00:31.637][detail][DMG] <RE:Run> Cluster 3, Attribute fffd is dirty
[16:26:45.675]  
[16:26:45.675]  [00:00:31.637][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_FFFD (expanded=1)
[16:26:45.677]  
[16:26:45.677]  [00:00:31.638][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:26:45.678]  [00:00:31.639][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:26:45.678]  [00:00:31.640][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:26:45.680]  
[16:26:45.680]  [00:00:31.641][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:26:45.681]  
[16:26:45.682]  [00:00:31.643][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:26:45.682]  
[16:26:45.682]  [00:00:31.644][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[16:26:45.683]  
[16:26:45.683]  [00:00:31.645][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_4000 (expanded=1)
[16:26:45.685]  
[16:26:45.685]  [00:00:31.646][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_4001 (expanded=1)
[16:26:45.686]  
[16:26:45.687]  [00:00:31.647][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_4003 (expanded=1)
[16:26:45.688]  
[16:26:45.688]  [00:00:31.648][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:26:45.689]  
[16:26:45.689]  [00:00:31.650][detail][DMG] <RE:Run> Cluster 6, Attribute fff9 is dirty
[16:26:45.690]  
[16:26:45.690]  [00:00:31.651][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:26:45.691]  [00:00:31.652][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:26:45.692]  [00:00:31.653][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:26:45.693]  
[16:26:45.694]  [00:00:31.655][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0003 (expanded=1)
[16:26:45.695]  [00:00:31.656][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_000F (expanded=1)
[16:26:45.696]  [00:00:31.656][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0010 (expanded=1)
[16:26:45.697]  [00:00:31.658][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0012 (expanded=1)
[16:26:45.698]  [00:00:31.659][detail][DMG] <RE:Run> Cluster 8, Attribute 14 is dirty
[16:26:45.699]  [00:00:31.661][detail][DMG] <RE:Run> Cluster 8, Attribute fffc is dirty
[16:26:45.700]  [00:00:31.662][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_FFFD (expanded=1)
[16:26:45.701]  [00:00:31.663][detail][DMG] <RE:Run> Cluster 8, Attribute fff9 is dirty
[16:26:45.702]  [00:00:31.664][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:26:45.703]  [00:00:31.665][detail][DMG] List does not fit in packet, chunk between list items for clusterId: 0x0000_0008, attributeId: 0x0000_FFFB
[16:26:45.705]  [00:00:31.668][info  ][EM] <<< [E:4276r S:25599 M:83709804 (Ack:47048222)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:1207)
[16:26:45.706]  [00:00:31.669][info  ][EM] ??1 [E:4276r S:25599 M:83709804] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3371ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:45.709]  [00:00:31.669][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:45.710]  [00:00:31.669][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has more messages
[16:26:46.260]  [00:00:32.233][detail][IN] UDP Message Received packet nb : 24 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:46.262]  [00:00:32.235][info  ][EM] >>> [E:4276r S:25599 M:47048223 (Ack:83709804)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:46.264]  [00:00:32.235][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:46.265]  [00:00:32.235][detail][EM] Rxd Ack; Removing MessageCounter:83709804 from Retrans Table on exchange 4276r
[16:26:46.266]  [00:00:32.236][info  ][IM] Received status response, status is 0x00
[16:26:46.267]  [00:00:32.236][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:46.267]  [00:00:32.236][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:46.268]  [00:00:32.236][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:46.270]  [00:00:32.236][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:26:46.271]  [00:00:32.242][detail][DMG] Fetched 5 events
[16:26:46.271]  [00:00:32.242][detail][DMG] <RE> Sending report (payload has 411 bytes)...
[16:26:46.272]  [00:00:32.244][info  ][EM] <<< [E:4276r S:25599 M:83709805 (Ack:47048223)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:445)
[16:26:46.274]  [00:00:32.245][info  ][EM] ??1 [E:4276r S:25599 M:83709805] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3340ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:46.276]  [00:00:32.245][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:46.277]  [00:00:32.246][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:26:46.278]  [00:00:32.246][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:46.319]  
[16:26:46.764]  [00:00:32.736][detail][IN] UDP Message Received packet nb : 25 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:46.766]  [00:00:32.738][info  ][EM] >>> [E:4276r S:25599 M:47048224 (Ack:83709805)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:46.767]  [00:00:32.738][detail][EM] Found matching exchange: 4276r, Delegate: 0x20005dd0
[16:26:46.768]  [00:00:32.738][detail][EM] Rxd Ack; Removing MessageCounter:83709805 from Retrans Table on exchange 4276r
[16:26:46.769]  [00:00:32.739][info  ][IM] Received status response, status is 0x00
[16:26:46.770]  [00:00:32.741][info  ][EM] <<< [E:4276r S:25599 M:83709806 (Ack:47048224)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:26:46.773]  [00:00:32.742][info  ][EM] ??1 [E:4276r S:25599 M:83709806] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3344ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:46.775]  [00:00:32.742][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x0000000000007FE6 and system Timestamp 0x000000000009A7A6.
[16:26:46.776]  [00:00:32.743][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:46.777]  [00:00:32.743][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:47.008]  [00:00:32.980][detail][IN] UDP Message Received packet nb : 26 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:26:47.010]  [00:00:32.982][info  ][EM] >>> [E:4278r S:25599 M:47048225] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:26:47.011]  [00:00:32.983][detail][EM] Handling via exchange: 4278r, Delegate: 0x2000413c
[16:26:47.012]  [00:00:32.983][detail][IM] Received Read request
[16:26:47.013]  [00:00:32.984][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:47.014]  [00:00:32.984][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:47.015]  [00:00:32.985][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:26:47.016]  [00:00:32.986][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:26:47.017]  [00:00:32.987][detail][DMG] <RE> Sending report (payload has 128 bytes)...
[16:26:47.018]  [00:00:32.990][info  ][EM] <<< [E:4278r S:25599 M:83709807 (Ack:47048225)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:162)
[16:26:47.020]  [00:00:32.991][info  ][EM] ??1 [E:4278r S:25599 M:83709807] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3408ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:47.022]  [00:00:32.991][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:47.023]  [00:00:32.991][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:26:47.024]  [00:00:32.991][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:47.025]  [00:00:32.992][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:47.026]  [00:00:32.999][detail][IN] UDP Message Received packet nb : 27 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:47.028]  [00:00:33.000][info  ][EM] >>> [E:4276r S:25599 M:47048226 (Ack:83709806)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:47.030]  [00:00:33.000][detail][EM] Found matching exchange: 4276r, Delegate: 0
[16:26:47.031]  [00:00:33.000][detail][EM] Rxd Ack; Removing MessageCounter:83709806 from Retrans Table on exchange 4276r
[16:26:47.532]  [00:00:33.503][detail][IN] UDP Message Received packet nb : 28 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:47.534]  [00:00:33.505][info  ][EM] >>> [E:4278r S:25599 M:47048227 (Ack:83709807)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:47.536]  [00:00:33.505][detail][EM] Found matching exchange: 4278r, Delegate: 0
[16:26:47.536]  [00:00:33.505][detail][EM] Rxd Ack; Removing MessageCounter:83709807 from Retrans Table on exchange 4278r
[16:26:47.561]  [00:00:33.533][detail][IN] UDP Message Received packet nb : 29 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 65
[16:26:47.563]  [00:00:33.535][info  ][EM] >>> [E:4279r S:25599 M:47048228] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:26:47.564]  [00:00:33.536][detail][EM] Handling via exchange: 4279r, Delegate: 0x2000413c
[16:26:47.565]  [00:00:33.537][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:26:47.566]  [00:00:33.537][info  ][FS] GeneralCommissioning: Received ArmFailSafe (30s)
[16:26:47.567]  [00:00:33.537][detail][DMG] Command handler moving to [NewRespons]
[16:26:47.568]  [00:00:33.537][detail][DMG] Command handler moving to [ Preparing]
[16:26:47.568]  [00:00:33.538][detail][DMG] Command handler moving to [AddingComm]
[16:26:47.569]  [00:00:33.538][detail][DMG] Command handler moving to [AddedComma]
[16:26:47.570]  [00:00:33.538][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:47.571]  [00:00:33.538][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:47.572]  [00:00:33.539][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:47.572]  [00:00:33.541][info  ][EM] <<< [E:4279r S:25599 M:83709808 (Ack:47048228)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:26:47.575]  [00:00:33.541][info  ][EM] ??1 [E:4279r S:25599 M:83709808] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3397ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:47.577]  [00:00:33.541][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:48.264]  [00:00:34.237][detail][IN] UDP Message Received packet nb : 30 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:48.266]  [00:00:34.238][info  ][EM] >>> [E:4279r S:25599 M:47048229 (Ack:83709808)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:48.269]  [00:00:34.239][detail][EM] Found matching exchange: 4279r, Delegate: 0
[16:26:48.269]  [00:00:34.239][detail][EM] Rxd Ack; Removing MessageCounter:83709808 from Retrans Table on exchange 4279r
[16:26:48.305]  [00:00:34.277][detail][IN] UDP Message Received packet nb : 31 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 94
[16:26:48.307]  [00:00:34.279][info  ][EM] >>> [E:4280r S:25599 M:47048230] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[16:26:48.308]  [00:00:34.279][detail][EM] Handling via exchange: 4280r, Delegate: 0x2000413c
[16:26:48.309]  [00:00:34.281][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0004
[16:26:48.310]  [00:00:34.281][info  ][ZCL] OpCreds: Received a CSRRequest command
[16:26:48.311]  [00:00:34.282][error ][CR] WARNING: PSA key recycled: 1 / 17409
[16:26:48.341]  [00:00:34.314][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[16:26:48.348]  [00:00:34.320][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:278, sig_size:64, err:0x00
[16:26:48.348]  [00:00:34.320][info  ][ZCL] OpCreds: CSRRequest successful.
[16:26:48.349]  [00:00:34.320][detail][DMG] Command handler moving to [NewRespons]
[16:26:48.350]  [00:00:34.321][detail][DMG] Command handler moving to [ Preparing]
[16:26:48.351]  [00:00:34.321][detail][DMG] Command handler moving to [AddingComm]
[16:26:48.351]  [00:00:34.321][detail][DMG] Command handler moving to [AddedComma]
[16:26:48.352]  [00:00:34.321][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:48.353]  [00:00:34.321][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:48.354]  [00:00:34.322][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:48.355]  [00:00:34.327][info  ][EM] <<< [E:4280r S:25599 M:83709809 (Ack:47048230)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:397)
[16:26:48.357]  [00:00:34.328][info  ][EM] ??1 [E:4280r S:25599 M:83709809] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3357ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:48.359]  [00:00:34.328][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:48.362]  
[16:26:48.813]  [00:00:34.786][detail][IN] UDP Message Received packet nb : 32 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:48.815]  [00:00:34.787][info  ][EM] >>> [E:4280r S:25599 M:47048231 (Ack:83709809)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:48.817]  [00:00:34.787][detail][EM] Found matching exchange: 4280r, Delegate: 0
[16:26:48.818]  [00:00:34.788][detail][EM] Rxd Ack; Removing MessageCounter:83709809 from Retrans Table on exchange 4280r
[16:26:48.917]  [00:00:34.888][detail][IN] UDP Message Received packet nb : 33 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 316
[16:26:48.919]  [00:00:34.890][info  ][EM] >>> [E:4281r S:25599 M:47048232] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:316)
[16:26:48.920]  [00:00:34.891][detail][EM] Handling via exchange: 4281r, Delegate: 0x2000413c
[16:26:48.921]  [00:00:34.892][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B
[16:26:48.922]  [00:00:34.892][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[16:26:48.933]  [00:00:34.906][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[16:26:48.934]  [00:00:34.906][detail][DMG] Command handler moving to [NewRespons]
[16:26:48.935]  [00:00:34.906][detail][DMG] Command handler moving to [ Preparing]
[16:26:48.936]  [00:00:34.906][detail][DMG] Command handler moving to [AddingComm]
[16:26:48.936]  [00:00:34.906][detail][DMG] Command handler moving to [AddedComma]
[16:26:48.937]  [00:00:34.907][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:48.938]  [00:00:34.907][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:48.939]  [00:00:34.907][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:48.940]  [00:00:34.909][info  ][EM] <<< [E:4281r S:25599 M:83709810 (Ack:47048232)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[16:26:48.942]  [00:00:34.910][info  ][EM] ??1 [E:4281r S:25599 M:83709810] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3411ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:48.944]  [00:00:34.911][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:49.403]  [00:00:35.375][detail][IN] UDP Message Received packet nb : 34 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:49.405]  [00:00:35.376][info  ][EM] >>> [E:4281r S:25599 M:47048233 (Ack:83709810)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:49.407]  [00:00:35.377][detail][EM] Found matching exchange: 4281r, Delegate: 0
[16:26:49.408]  [00:00:35.377][detail][EM] Rxd Ack; Removing MessageCounter:83709810 from Retrans Table on exchange 4281r
[16:26:50.319]  
[16:26:51.602]  [00:00:37.574][detail][IN] UDP Message Received packet nb : 35 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 353
[16:26:51.604]  [00:00:37.576][info  ][EM] >>> [E:4282r S:25599 M:47048234] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:353)
[16:26:51.605]  [00:00:37.577][detail][EM] Handling via exchange: 4282r, Delegate: 0x2000413c
[16:26:51.606]  [00:00:37.578][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0006
[16:26:51.607]  [00:00:37.578][info  ][ZCL] OpCreds: Received an AddNOC command
[16:26:51.608]  [00:00:37.580][info  ][FP] Validating NOC chain
[16:26:51.624]  [00:00:37.596][info  ][FP] NOC chain validation successful
[16:26:51.624]  [00:00:37.596][info  ][FP] Added new fabric at index: 0x2
[16:26:51.625]  [00:00:37.597][info  ][FP] Assigned compressed fabric ID: 0x22BF8DCC5C200CC8, node ID: 0x00000000B2E8E432
[16:26:51.626]  [00:00:37.597][info  ][TS] Last Known Good Time: 2026-02-07T08:26:31
[16:26:51.627]  [00:00:37.597][info  ][TS] New proposed Last Known Good Time: 2026-02-07T08:26:51
[16:26:51.628]  [00:00:37.597][info  ][TS] Updating pending Last Known Good Time to 2026-02-07T08:26:51
[16:26:51.629]  [00:00:37.598][info  ][DMG] Handler: 0x20001230 with min: 0x0000000000007FE6 and max: 0x000000000009A7A6
[16:26:51.630]  [00:00:37.598][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:26:51.631]  [00:00:37.599][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:26:51.639]  [00:00:37.611][detail][EVL] LogEvent event number: 0x0000000000000006 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6AD03EA5
[16:26:51.640]  [00:00:37.612][detail][DMG] Urgent event will be sent once reporting is not blocked by the min interval
[16:26:51.642]  
[16:26:51.642]  [00:00:37.612][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x2 CASE Admin Subject 0x58180CE51292A84A
[16:26:51.643]  
[16:26:51.643]  [00:00:37.612][detail][DL] Using Thread extended MAC for hostname.
[16:26:51.644]  [00:00:37.612][info  ][DIS] Advertise operational node 48703F2ABA76AAAB-00000000FCB0C0DF
[16:26:51.645]  [00:00:37.613][detail][DL] Using Thread extended MAC for hostname.
[16:26:51.646]  [00:00:37.613][info  ][DIS] Advertise operational node 22BF8DCC5C200CC8-00000000B2E8E432
[16:26:51.647]  [00:00:37.613][info  ][DL] advertising srp service: 22BF8DCC5C200CC8-00000000B2E8E432._matter._tcp
[16:26:51.648]  [00:00:37.614][detail][DMG] Command handler moving to [NewRespons]
[16:26:51.649]  [00:00:37.614][detail][DMG] Command handler moving to [ Preparing]
[16:26:51.650]  [00:00:37.614][detail][DMG] Command handler moving to [AddingComm]
[16:26:51.650]  [00:00:37.614][detail][DMG] Command handler moving to [AddedComma]
[16:26:51.651]  [00:00:37.616][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:51.652]  [00:00:37.618][info  ][EM] <<< [E:4282r S:25599 M:83709811 (Ack:47048234)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:26:51.654]  [00:00:37.619][info  ][EM] ??1 [E:4282r S:25599 M:83709811] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3399ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:51.656]  [00:00:37.619][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:51.657]  [00:00:37.620][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x000000000000001D DirtyGeneration = 0x0000000000000021
[16:26:51.659]  [00:00:37.621][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:26:51.660]  [00:00:37.622][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:26:51.661]  [00:00:37.623][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:26:51.661]  [00:00:37.624][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:26:51.663]  [00:00:37.632][detail][DMG] Fetched 1 events
[16:26:51.664]  [00:00:37.632][detail][DMG] <RE> Sending report (payload has 309 bytes)...
[16:26:51.664]  [00:00:37.635][info  ][EM] <<< [E:49925i S:25599 M:83709812] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:339)
[16:26:51.667]  [00:00:37.636][info  ][EM] ??1 [E:49925i S:25599 M:83709812] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3358ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:51.668]  [00:00:37.636][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:26:51.669]  [00:00:37.636][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:26:51.670]  [00:00:37.636][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:52.107]  [00:00:38.080][detail][IN] UDP Message Received packet nb : 36 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:52.109]  [00:00:38.082][info  ][EM] >>> [E:4282r S:25599 M:47048235 (Ack:83709811)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:52.111]  [00:00:38.082][detail][EM] Found matching exchange: 4282r, Delegate: 0
[16:26:52.112]  [00:00:38.082][detail][EM] Rxd Ack; Removing MessageCounter:83709811 from Retrans Table on exchange 4282r
[16:26:52.122]  [00:00:38.095][detail][IN] UDP Message Received packet nb : 37 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:26:52.124]  [00:00:38.097][info  ][EM] >>> [E:49925i S:25599 M:47048236 (Ack:83709812)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:26:52.126]  [00:00:38.097][detail][EM] Found matching exchange: 49925i, Delegate: 0x20005dd0
[16:26:52.127]  [00:00:38.097][detail][EM] Rxd Ack; Removing MessageCounter:83709812 from Retrans Table on exchange 49925i
[16:26:52.128]  [00:00:38.097][info  ][IM] Received status response, status is 0x00
[16:26:52.129]  [00:00:38.098][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:52.129]  [00:00:38.098][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:52.141]  [00:00:38.114][info  ][EM] <<< [E:49925i S:25599 M:83709813 (Ack:47048236)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:52.143]  [00:00:38.115][detail][EM] Flushed pending ack for MessageCounter:47048236 on exchange 49925i
[16:26:52.311]  [00:00:38.284][detail][DL] SRP update succeeded
[16:26:52.319]  
[16:26:52.864]  [00:00:38.836][detail][IN] UDP Message Received packet nb : 38 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 196
[16:26:52.866]  [00:00:38.836][info  ][EM] >>> [E:4283r S:0 M:203526979] (U) Msg RX from 0:519FAF8469131A7A [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:26:52.868]  [00:00:38.837][detail][EM] Handling via exchange: 4283r, Delegate: 0x20007de8
[16:26:52.868]  [00:00:38.837][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200089b0
[16:26:52.870]  [00:00:38.838][info  ][EM] <<< [E:4283r S:0 M:139474081 (Ack:203526979)] (U) Msg TX from 0000000000000000 to 0:519FAF8469131A7A [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:52.872]  [00:00:38.839][detail][EM] Flushed pending ack for MessageCounter:203526979 on exchange 4283r
[16:26:52.873]  [00:00:38.839][info  ][SC] Received Sigma1 msg
[16:26:52.874]  [00:00:38.839][detail][SC] Found MRP parameters in the message
[16:26:52.875]  [00:00:38.840][detail][SC] Peer (Initiator) assigned session ID 39872
[16:26:52.885]  [00:00:38.858][info  ][SC] CASE matched destination ID: fabricIndex 2, NodeID 0x00000000B2E8E432
[16:26:52.906]  [00:00:38.878][detail][CR] AES_CCM_encrypt: Using aad == null path
[16:26:52.909]  [00:00:38.881][info  ][EM] <<< [E:4283r S:0 M:139474082 (Ack:203526979)] (U) Msg TX from 0000000000000000 to 0:519FAF8469131A7A [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:533)
[16:26:52.911]  [00:00:38.882][info  ][EM] ??1 [E:4283r S:0 M:139474082] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3390ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:52.913]  [00:00:38.882][info  ][SC] Sent Sigma2 msg
[16:26:53.714]  [00:00:39.686][detail][IN] UDP Message Received packet nb : 39 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 382
[16:26:53.716]  [00:00:39.687][info  ][EM] >>> [E:4283r S:0 M:203526980 (Ack:139474082)] (U) Msg RX from 0:519FAF8469131A7A [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:382)
[16:26:53.717]  [00:00:39.687][detail][EM] Found matching exchange: 4283r, Delegate: 0x20007e04
[16:26:53.719]  [00:00:39.687][detail][EM] Rxd Ack; Removing MessageCounter:139474082 from Retrans Table on exchange 4283r
[16:26:53.719]  [00:00:39.688][info  ][EM] <<< [E:4283r S:0 M:139474083 (Ack:203526980)] (U) Msg TX from 0000000000000000 to 0:519FAF8469131A7A [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:53.722]  [00:00:39.689][detail][EM] Flushed pending ack for MessageCounter:203526980 on exchange 4283r
[16:26:53.723]  [00:00:39.689][info  ][SC] Received Sigma3 msg
[16:26:53.723]  [00:00:39.693][detail][CR] AES_CCM_decrypt: Using aad == null path
[16:26:53.725]  [00:00:39.696][detail][SC] Certificate's mNotBeforeTime (752291503) is after current time (39)
[16:26:53.725]  [00:00:39.696][detail][SC] Certificate's mNotBeforeTime (751534635) is after current time (39)
[16:26:53.753]  [00:00:39.726][detail][SC] Sending status report. Protocol code 0, exchange 4283
[16:26:53.754]  [00:00:39.726][info  ][EM] <<< [E:4283r S:0 M:139474084 (Ack:203526980)] (U) Msg TX from 0000000000000000 to 0:519FAF8469131A7A [0000] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:26:53.757]  [00:00:39.727][info  ][EM] ??1 [E:4283r S:0 M:139474084] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3379ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:53.758]  [00:00:39.731][info  ][SC] SecureSession[0x20007108, LSID:25601]: State change 'kEstablishing' --> 'kActive'
[16:26:53.759]  [00:00:39.731][detail][IN] SecureSession[0x20007108]: Activated - Type:2 LSID:25601
[16:26:53.760]  [00:00:39.731][detail][IN] New secure session activated for device <58180CE51292A84A, 2>, LSID:25601 PSID:39872!
[16:26:53.761]  [00:00:39.732][info  ][IN] CASE Session established to peer: <58180CE51292A84A, 2>
[16:26:53.762]  [00:00:39.732][detail][IN] SecureSession[0x20007030]: Allocated Type:2 LSID:25602
[16:26:53.763]  [00:00:39.732][detail][SC] Allocated SecureSession (0x20007030) - waiting for Sigma1 msg
[16:26:53.764]  [00:00:39.733][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:26:53.765]  [00:00:39.733][silabs ]NWK: platform event type 8018
[16:26:54.319]  
[16:26:54.395]  [00:00:40.368][detail][IN] UDP Message Received packet nb : 40 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:26:54.397]  [00:00:40.370][info  ][EM] >>> [E:4284r S:25601 M:96722862] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:26:54.399]  [00:00:40.371][detail][EM] Handling via exchange: 4284r, Delegate: 0x2000413c
[16:26:54.399]  [00:00:40.371][detail][IM] Received Read request
[16:26:54.400]  [00:00:40.372][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:54.401]  [00:00:40.372][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:54.402]  [00:00:40.373][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:26:54.404]  [00:00:40.374][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:26:54.404]  [00:00:40.375][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:26:54.406]  [00:00:40.376][info  ][EM] <<< [E:4284r S:25601 M:9588139 (Ack:96722862)] (S) Msg TX from 00000000B2E8E432 to 2:58180CE51292A84A [0CC8] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:70)
[16:26:54.408]  [00:00:40.377][info  ][EM] ??1 [E:4284r S:25601 M:9588139] (S) Msg Retransmission to 2:58180CE51292A84A scheduled for 3334ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:54.410]  [00:00:40.377][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:54.411]  [00:00:40.378][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:26:54.411]  [00:00:40.378][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:54.412]  [00:00:40.378][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:54.421]  [00:00:40.394][detail][IN] UDP Message Received packet nb : 41 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 26
[16:26:54.423]  [00:00:40.394][info  ][EM] >>> [E:4283r S:0 M:203526981 (Ack:139474084)] (U) Msg RX from 0:519FAF8469131A7A [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:26:54.425]  [00:00:40.394][detail][EM] Found matching exchange: 4283r, Delegate: 0
[16:26:54.426]  [00:00:40.395][detail][EM] Rxd Ack; Removing MessageCounter:139474084 from Retrans Table on exchange 4283r
[16:26:54.916]  [00:00:40.888][detail][IN] UDP Message Received packet nb : 42 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 59
[16:26:54.919]  [00:00:40.890][info  ][EM] >>> [E:4285r S:25601 M:96722863] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[16:26:54.920]  [00:00:40.891][detail][EM] Handling via exchange: 4285r, Delegate: 0x2000413c
[16:26:54.921]  [00:00:40.892][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0004
[16:26:54.922]  [00:00:40.892][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[16:26:54.923]  [00:00:40.894][info  ][FP] Metadata for Fabric 0x2 persisted to storage.
[16:26:54.931]  [00:00:40.903][info  ][TS] Committing Last Known Good Time to storage: 2026-02-07T08:26:51
[16:26:54.933]  [00:00:40.905][info  ][ZCL] OpCreds: Fabric index 0x2 was committed to storage. Compressed Fabric Id 0x22BF8DCC5C200CC8, FabricId 00000000AA39E9D5, NodeId 00000000B2E8E432, VendorId 0x1384
[16:26:54.934]  [00:00:40.906][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[16:26:54.936]  [00:00:40.906][info  ][FS] Fail-safe cleanly disarmed
[16:26:54.936]  [00:00:40.906][detail][DMG] Command handler moving to [NewRespons]
[16:26:54.937]  [00:00:40.906][detail][DMG] Command handler moving to [ Preparing]
[16:26:54.938]  [00:00:40.906][detail][DMG] Command handler moving to [AddingComm]
[16:26:54.938]  [00:00:40.907][detail][DMG] Command handler moving to [AddedComma]
[16:26:54.939]  [00:00:40.907][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:26:54.940]  [00:00:40.907][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:26:54.941]  [00:00:40.907][detail][DMG] Command handler moving to [AwaitingDe]
[16:26:54.943]  [00:00:40.916][detail][IN] UDP Message Received packet nb : 43 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:54.946]  [00:00:40.916][info  ][EM] <<< [E:4285r S:25601 M:9588140 (Ack:96722863)] (S) Msg TX from 00000000B2E8E432 to 2:58180CE51292A84A [0CC8] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:26:54.948]  [00:00:40.917][info  ][EM] ??1 [E:4285r S:25601 M:9588140] (S) Msg Retransmission to 2:58180CE51292A84A scheduled for 3397ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:54.950]  
[16:26:54.950]  [00:00:40.917][detail][DMG] Command response sender moving to [AllInvokeR]
[16:26:54.950]  [00:00:40.917][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[16:26:54.952]  [00:00:40.917][info  ][SWU] Device commissioned, schedule a default provider query
[16:26:54.953]  [00:00:40.917][silabs ]NWK: platform event type 800f
[16:26:54.953]  [00:00:40.918][silabs ]COM: notify network [Joined]
[16:26:54.954]  [00:00:40.918][detail][ZCL] Commissioning complete, notify platform driver to persist network credentials.
[16:26:54.955]  [00:00:40.920][info  ][EM] >>> [E:4284r S:25601 M:96722864 (Ack:9588139)] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:54.957]  [00:00:40.920][detail][EM] Found matching exchange: 4284r, Delegate: 0
[16:26:54.957]  [00:00:40.920][detail][EM] Rxd Ack; Removing MessageCounter:9588139 from Retrans Table on exchange 4284r
[16:26:55.577]  [00:00:41.549][detail][IN] UDP Message Received packet nb : 44 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:55.579]  [00:00:41.550][info  ][EM] >>> [E:4285r S:25601 M:96722865 (Ack:9588140)] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:55.581]  [00:00:41.551][detail][EM] Found matching exchange: 4285r, Delegate: 0
[16:26:55.582]  [00:00:41.551][detail][EM] Rxd Ack; Removing MessageCounter:9588140 from Retrans Table on exchange 4285r
[16:26:55.594]  [00:00:41.566][detail][IN] UDP Message Received packet nb : 45 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:26:55.596]  [00:00:41.568][info  ][EM] >>> [E:4286r S:25601 M:96722866] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:26:55.598]  [00:00:41.568][detail][EM] Handling via exchange: 4286r, Delegate: 0x2000413c
[16:26:55.598]  [00:00:41.569][detail][IM] Received Read request
[16:26:55.599]  [00:00:41.569][detail][DMG] IM RH moving to [CanStartReporting]
[16:26:55.599]  [00:00:41.570][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:26:55.601]  [00:00:41.571][detail][DMG] <RE:Run> Cluster 28, Attribute f is dirty
[16:26:55.602]  [00:00:41.572][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000F (expanded=0)
[16:26:55.603]  [00:00:41.573][detail][DMG] <RE> Sending report (payload has 52 bytes)...
[16:26:55.604]  [00:00:41.575][info  ][EM] <<< [E:4286r S:25601 M:9588141 (Ack:96722866)] (S) Msg TX from 00000000B2E8E432 to 2:58180CE51292A84A [0CC8] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:86)
[16:26:55.606]  [00:00:41.577][info  ][EM] ??1 [E:4286r S:25601 M:9588141] (S) Msg Retransmission to 2:58180CE51292A84A scheduled for 3383ms from now [State:Active II:500 AI:300 AT:4000]
[16:26:55.609]  [00:00:41.577][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:26:55.609]  [00:00:41.577][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:26:55.610]  [00:00:41.577][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:26:55.611]  [00:00:41.577][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:26:56.094]  [00:00:42.066][detail][IN] UDP Message Received packet nb : 46 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:26:56.096]  [00:00:42.068][info  ][EM] >>> [E:4286r S:25601 M:96722867 (Ack:9588141)] (S) Msg RX from 2:58180CE51292A84A [0CC8] to 00000000B2E8E432 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:26:56.098]  [00:00:42.068][detail][EM] Found matching exchange: 4286r, Delegate: 0
[16:26:56.099]  [00:00:42.068][detail][EM] Rxd Ack; Removing MessageCounter:9588141 from Retrans Table on exchange 4286r
[16:26:56.319]  
[16:26:58.319]  
[16:27:00.320]  
[16:27:00.349]  [00:00:46.321][detail][IN] UDP Message Received packet nb : 47 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 196
[16:27:00.350]  [00:00:46.322][info  ][EM] >>> [E:41955r S:0 M:112609450] (U) Msg RX from 0:32E7D130B3F1638F [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:27:00.352]  [00:00:46.322][detail][EM] Handling via exchange: 41955r, Delegate: 0x20007de8
[16:27:00.353]  [00:00:46.322][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200089b0
[16:27:00.354]  [00:00:46.323][info  ][EM] <<< [E:41955r S:0 M:139474085 (Ack:112609450)] (U) Msg TX from 0000000000000000 to 0:32E7D130B3F1638F [0000] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:27:00.357]  [00:00:46.324][detail][EM] Flushed pending ack for MessageCounter:112609450 on exchange 41955r
[16:27:00.358]  [00:00:46.324][info  ][SC] Received Sigma1 msg
[16:27:00.358]  [00:00:46.324][detail][SC] Found MRP parameters in the message
[16:27:00.359]  [00:00:46.324][detail][SC] Peer (Initiator) assigned session ID 27174
[16:27:00.361]  [00:00:46.333][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000FCB0C0DF
[16:27:00.388]  [00:00:46.361][detail][CR] AES_CCM_encrypt: Using aad == null path
[16:27:00.391]  [00:00:46.363][info  ][EM] <<< [E:41955r S:0 M:139474086 (Ack:112609450)] (U) Msg TX from 0000000000000000 to 0:32E7D130B3F1638F [0000] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:528)
[16:27:00.393]  [00:00:46.364][info  ][EM] ??1 [E:41955r S:0 M:139474086] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3367ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:00.395]  [00:00:46.365][info  ][SC] Sent Sigma2 msg
[16:27:00.523]  [00:00:46.496][detail][IN] UDP Message Received packet nb : 48 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 71
[16:27:00.525]  [00:00:46.498][info  ][EM] >>> [E:4287r S:25599 M:47048237] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:71)
[16:27:00.527]  [00:00:46.498][detail][EM] Handling via exchange: 4287r, Delegate: 0x2000413c
[16:27:00.528]  [00:00:46.499][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0009
[16:27:00.529]  [00:00:46.500][info  ][ZCL] OpCreds: Received an UpdateFabricLabel command
[16:27:00.530]  [00:00:46.500][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:27:00.530]  [00:00:46.500][detail][DMG] Command handler moving to [NewRespons]
[16:27:00.531]  [00:00:46.500][detail][DMG] Command handler moving to [ Preparing]
[16:27:00.532]  [00:00:46.500][detail][DMG] Command handler moving to [AddingComm]
[16:27:00.533]  [00:00:46.500][detail][DMG] Command handler moving to [AddedComma]
[16:27:00.534]  [00:00:46.501][info  ][DMG] Handler: 0x20001230 with min: 0x0000000000009304 and max: 0x000000000009BAC4
[16:27:00.534]  [00:00:46.501][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:00.536]  [00:00:46.502][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:27:00.537]  [00:00:46.502][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:27:00.538]  [00:00:46.502][detail][DMG] Command handler moving to [AwaitingDe]
[16:27:00.539]  [00:00:46.505][info  ][EM] <<< [E:4287r S:25599 M:83709814 (Ack:47048237)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:27:00.541]  [00:00:46.506][info  ][EM] ??1 [E:4287r S:25599 M:83709814] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3385ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:00.543]  [00:00:46.506][detail][DMG] Command response sender moving to [AllInvokeR]
[16:27:00.543]  [00:00:46.507][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000021 DirtyGeneration = 0x0000000000000022
[16:27:00.546]  [00:00:46.508][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:27:00.546]  [00:00:46.509][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:00.548]  [00:00:46.519][detail][DMG] Fetched 0 events
[16:27:00.548]  [00:00:46.519][detail][DMG] <RE> Sending report (payload has 233 bytes)...
[16:27:00.548]  [00:00:46.521][info  ][EM] <<< [E:49926i S:25599 M:83709815] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:263)
[16:27:00.551]  [00:00:46.522][info  ][EM] ??1 [E:49926i S:25599 M:83709815] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3409ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:00.553]  [00:00:46.522][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:00.554]  [00:00:46.523][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:27:00.555]  [00:00:46.523][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:00.711]  [00:00:46.683][detail][IN] UDP Message Received packet nb : 49 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 373
[16:27:00.712]  [00:00:46.683][info  ][EM] >>> [E:41955r S:0 M:112609451 (Ack:139474086)] (U) Msg RX from 0:32E7D130B3F1638F [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:373)
[16:27:00.714]  [00:00:46.684][detail][EM] Found matching exchange: 41955r, Delegate: 0x20007e04
[16:27:00.716]  [00:00:46.684][detail][EM] Rxd Ack; Removing MessageCounter:139474086 from Retrans Table on exchange 41955r
[16:27:00.716]  [00:00:46.685][info  ][EM] <<< [E:41955r S:0 M:139474087 (Ack:112609451)] (U) Msg TX from 0000000000000000 to 0:32E7D130B3F1638F [0000] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:27:00.719]  [00:00:46.685][detail][EM] Flushed pending ack for MessageCounter:112609451 on exchange 41955r
[16:27:00.721]  [00:00:46.685][info  ][SC] Received Sigma3 msg
[16:27:00.721]  [00:00:46.689][detail][CR] AES_CCM_decrypt: Using aad == null path
[16:27:00.722]  [00:00:46.693][detail][SC] Certificate's mNotBeforeTime (823660739) is after current time (46)
[16:27:00.723]  [00:00:46.693][detail][SC] Certificate's mNotBeforeTime (823767991) is after current time (46)
[16:27:00.750]  [00:00:46.723][detail][SC] Sending status report. Protocol code 0, exchange 41955
[16:27:00.751]  [00:00:46.723][info  ][EM] <<< [E:41955r S:0 M:139474088 (Ack:112609451)] (U) Msg TX from 0000000000000000 to 0:32E7D130B3F1638F [0000] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:27:00.754]  [00:00:46.724][info  ][EM] ??1 [E:41955r S:0 M:139474088] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3370ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:00.755]  [00:00:46.728][info  ][SC] SecureSession[0x20007030, LSID:25602]: State change 'kEstablishing' --> 'kActive'
[16:27:00.757]  [00:00:46.728][detail][IN] SecureSession[0x20007030]: Activated - Type:2 LSID:25602
[16:27:00.757]  [00:00:46.728][detail][IN] New secure session activated for device <00000000A5E93870, 1>, LSID:25602 PSID:27174!
[16:27:00.759]  [00:00:46.728][info  ][IN] CASE Session established to peer: <00000000A5E93870, 1>
[16:27:00.760]  [00:00:46.729][detail][IN] SecureSession[0x200071e0]: Allocated Type:2 LSID:25603
[16:27:00.761]  [00:00:46.729][detail][SC] Allocated SecureSession (0x200071e0) - waiting for Sigma1 msg
[16:27:00.762]  [00:00:46.730][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:27:00.762]  [00:00:46.730][silabs ]NWK: platform event type 8018
[16:27:00.779]  [00:00:46.751][detail][IN] UDP Message Received packet nb : 50 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:00.781]  [00:00:46.752][info  ][EM] >>> [E:4287r S:25599 M:47048238 (Ack:83709814)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:00.783]  [00:00:46.753][detail][EM] Found matching exchange: 4287r, Delegate: 0
[16:27:00.784]  [00:00:46.753][detail][EM] Rxd Ack; Removing MessageCounter:83709814 from Retrans Table on exchange 4287r
[16:27:00.803]  [00:00:46.775][detail][IN] UDP Message Received packet nb : 51 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:00.805]  [00:00:46.777][info  ][EM] >>> [E:49926i S:25599 M:47048239 (Ack:83709815)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:00.806]  [00:00:46.778][detail][EM] Found matching exchange: 49926i, Delegate: 0x20005dd0
[16:27:00.808]  [00:00:46.778][detail][EM] Rxd Ack; Removing MessageCounter:83709815 from Retrans Table on exchange 49926i
[16:27:00.808]  [00:00:46.778][info  ][IM] Received status response, status is 0x00
[16:27:00.809]  [00:00:46.778][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:00.810]  [00:00:46.778][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:00.811]  [00:00:46.780][info  ][EM] <<< [E:49926i S:25599 M:83709816 (Ack:47048239)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:00.813]  [00:00:46.781][detail][EM] Flushed pending ack for MessageCounter:47048239 on exchange 49926i
[16:27:01.304]  [00:00:47.276][detail][IN] UDP Message Received packet nb : 52 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:27:01.305]  [00:00:47.278][info  ][EM] >>> [E:41956r S:25602 M:245903546] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:27:01.307]  [00:00:47.279][detail][EM] Handling via exchange: 41956r, Delegate: 0x2000413c
[16:27:01.308]  [00:00:47.279][detail][IM] Received Read request
[16:27:01.309]  [00:00:47.280][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:01.309]  [00:00:47.280][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:27:01.311]  [00:00:47.281][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:27:01.311]  [00:00:47.282][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:27:01.313]  [00:00:47.283][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:27:01.318]  [00:00:47.291][detail][IN] UDP Message Received packet nb : 53 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:27:01.320]  [00:00:47.291][info  ][EM] <<< [E:41956r S:25602 M:181174531 (Ack:245903546)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:70)
[16:27:01.322]  [00:00:47.292][info  ][EM] ??1 [E:41956r S:25602 M:181174531] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3339ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.324]  [00:00:47.292][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:01.325]  [00:00:47.292][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:27:01.326]  [00:00:47.292][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:27:01.326]  [00:00:47.293][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:01.328]  [00:00:47.294][info  ][EM] >>> [E:41957r S:25602 M:245903547] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:27:01.329]  [00:00:47.295][detail][EM] Handling via exchange: 41957r, Delegate: 0x2000413c
[16:27:01.330]  
[16:27:01.331]  [00:00:47.295][detail][IM] Received Read request
[16:27:01.331]  [00:00:47.296][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:01.332]  [00:00:47.296][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:27:01.333]  [00:00:47.297][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:27:01.334]  [00:00:47.298][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:27:01.336]  [00:00:47.299][detail][DMG] <RE> Sending report (payload has 36 bytes)...
[16:27:01.336]  [00:00:47.301][info  ][EM] <<< [E:41957r S:25602 M:181174532 (Ack:245903547)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:70)
[16:27:01.339]  [00:00:47.302][info  ][EM] ??1 [E:41957r S:25602 M:181174532] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3360ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.340]  [00:00:47.302][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:01.341]  [00:00:47.302][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:27:01.442]  [00:00:47.415][detail][IN] UDP Message Received packet nb : 54 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 26
[16:27:01.443]  [00:00:47.415][info  ][EM] >>> [E:41955r S:0 M:112609452 (Ack:139474088)] (U) Msg RX from 0:32E7D130B3F1638F [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:27:01.445]  [00:00:47.415][detail][EM] Found matching exchange: 41955r, Delegate: 0
[16:27:01.447]  [00:00:47.416][detail][EM] Rxd Ack; Removing MessageCounter:139474088 from Retrans Table on exchange 41955r
[16:27:01.465]  [00:00:47.438][detail][IN] UDP Message Received packet nb : 55 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 51
[16:27:01.467]  [00:00:47.440][info  ][EM] >>> [E:41958r S:25602 M:245903548] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:02 (IM:ReadRequest) (B:51)
[16:27:01.469]  [00:00:47.440][detail][EM] Handling via exchange: 41958r, Delegate: 0x2000413c
[16:27:01.470]  [00:00:47.441][detail][IM] Received Read request
[16:27:01.470]  [00:00:47.442][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:01.471]  [00:00:47.442][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:27:01.472]  [00:00:47.443][detail][DMG] <RE:Run> Cluster 1f, Attribute 0 is dirty
[16:27:01.473]  [00:00:47.443][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:27:01.474]  [00:00:47.445][detail][DMG] <RE> Sending report (payload has 91 bytes)...
[16:27:01.476]  [00:00:47.448][info  ][EM] <<< [E:41958r S:25602 M:181174533 (Ack:245903548)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:125)
[16:27:01.478]  [00:00:47.449][info  ][EM] ??1 [E:41958r S:25602 M:181174533] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3404ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.480]  [00:00:47.450][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:01.481]  [00:00:47.450][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 1, RE has no more messages
[16:27:01.482]  [00:00:47.450][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:27:01.482]  [00:00:47.450][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:01.507]  [00:00:47.479][detail][IN] UDP Message Received packet nb : 56 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:01.508]  [00:00:47.481][info  ][EM] >>> [E:41956r S:25602 M:245903549 (Ack:181174531)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:01.511]  [00:00:47.481][detail][EM] Found matching exchange: 41956r, Delegate: 0
[16:27:01.512]  [00:00:47.481][detail][EM] Rxd Ack; Removing MessageCounter:181174531 from Retrans Table on exchange 41956r
[16:27:01.530]  [00:00:47.503][detail][IN] UDP Message Received packet nb : 57 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 58
[16:27:01.532]  [00:00:47.505][info  ][EM] >>> [E:41959r S:25602 M:245903550] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:03 (IM:SubscribeRequest) (B:58)
[16:27:01.534]  [00:00:47.505][detail][EM] Handling via exchange: 41959r, Delegate: 0x2000413c
[16:27:01.535]  [00:00:47.505][detail][IM] Received Subscribe request
[16:27:01.535]  [00:00:47.508][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[16:27:01.537]  [00:00:47.508][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:01.548]  [00:00:47.521][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:27:01.549]  [00:00:47.521][detail][DMG] <RE:Run> Cluster 41, Attribute 0 is dirty
[16:27:01.550]  [00:00:47.522][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:01.551]  [00:00:47.523][detail][DMG] <RE:Run> Cluster 41, Attribute fffc is dirty
[16:27:01.552]  [00:00:47.524][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:01.554]  [00:00:47.524][detail][DMG] <RE:Run> Cluster 41, Attribute fffd is dirty
[16:27:01.554]  [00:00:47.524][detail][DMG] Reading attribute: Cluster=0x0000_0041 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:01.556]  [00:00:47.525][detail][DMG] <RE:Run> Cluster 41, Attribute fff8 is dirty
[16:27:01.556]  [00:00:47.526][detail][DMG] <RE:Run> Cluster 41, Attribute fff9 is dirty
[16:27:01.557]  [00:00:47.526][detail][DMG] <RE:Run> Cluster 41, Attribute fffb is dirty
[16:27:01.558]  [00:00:47.527][detail][DMG] <RE:Run> Cluster 40, Attribute 0 is dirty
[16:27:01.558]  [00:00:47.528][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:01.560]  [00:00:47.528][detail][DMG] <RE:Run> Cluster 40, Attribute fffc is dirty
[16:27:01.561]  [00:00:47.529][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:01.562]  [00:00:47.529][detail][DMG] <RE:Run> Cluster 40, Attribute fffd is dirty
[16:27:01.563]  [00:00:47.530][detail][DMG] Reading attribute: Cluster=0x0000_0040 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:01.564]  [00:00:47.531][detail][DMG] <RE:Run> Cluster 40, Attribute fff8 is dirty
[16:27:01.565]  [00:00:47.532][detail][DMG] <RE:Run> Cluster 40, Attribute fff9 is dirty
[16:27:01.565]  [00:00:47.532][detail][DMG] <RE:Run> Cluster 40, Attribute fffb is dirty
[16:27:01.567]  [00:00:47.533][detail][DMG] <RE:Run> Cluster 3f, Attribute 0 is dirty
[16:27:01.567]  [00:00:47.534][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:01.569]  [00:00:47.536][detail][DMG] <RE:Run> Cluster 3f, Attribute 1 is dirty
[16:27:01.570]  [00:00:47.536][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:01.571]  [00:00:47.538][detail][DMG] <RE:Run> Cluster 3f, Attribute 2 is dirty
[16:27:01.572]  [00:00:47.539][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:01.572]  
[16:27:01.573]  [00:00:47.539][detail][DMG] <RE:Run> Cluster 3f, Attribute 3 is dirty
[16:27:01.574]  [00:00:47.540][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:01.575]  [00:00:47.540][detail][DMG] <RE:Run> Cluster 3f, Attribute fffc is dirty
[16:27:01.576]  [00:00:47.541][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:01.577]  [00:00:47.541][detail][DMG] <RE:Run> Cluster 3f, Attribute fffd is dirty
[16:27:01.578]  [00:00:47.541][detail][DMG] Reading attribute: Cluster=0x0000_003F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:01.579]  [00:00:47.541][detail][DMG] <RE:Run> Cluster 3f, Attribute fff8 is dirty
[16:27:01.580]  [00:00:47.542][detail][DMG] <RE:Run> Cluster 3f, Attribute fff9 is dirty
[16:27:01.581]  [00:00:47.543][detail][DMG] <RE:Run> Cluster 3f, Attribute fffb is dirty
[16:27:01.581]  [00:00:47.544][detail][DMG] <RE:Run> Cluster 3e, Attribute 0 is dirty
[16:27:01.582]  [00:00:47.549][detail][DMG] List does not fit in packet, chunk between list items for clusterId: 0x0000_003E, attributeId: 0x0000_0000
[16:27:01.583]  [00:00:47.549][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:27:01.585]  [00:00:47.553][detail][DMG] Fetched 4 events
[16:27:01.585]  [00:00:47.553][detail][DMG] <RE> Sending report (payload has 1124 bytes)...
[16:27:01.586]  [00:00:47.556][info  ][EM] <<< [E:41959r S:25602 M:181174534 (Ack:245903550)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1158)
[16:27:01.589]  [00:00:47.559][info  ][EM] ??1 [E:41959r S:25602 M:181174534] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3364ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.590]  [00:00:47.560][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:01.591]  [00:00:47.560][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:01.606]  [00:00:47.579][detail][IN] UDP Message Received packet nb : 58 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:01.608]  [00:00:47.581][info  ][EM] >>> [E:41957r S:25602 M:245903551 (Ack:181174532)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:01.610]  [00:00:47.581][detail][EM] Found matching exchange: 41957r, Delegate: 0
[16:27:01.611]  [00:00:47.581][detail][EM] Rxd Ack; Removing MessageCounter:181174532 from Retrans Table on exchange 41957r
[16:27:01.627]  [00:00:47.600][detail][IN] UDP Message Received packet nb : 59 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:01.629]  [00:00:47.601][info  ][EM] >>> [E:41958r S:25602 M:245903552 (Ack:181174533)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:01.631]  [00:00:47.602][detail][EM] Found matching exchange: 41958r, Delegate: 0
[16:27:01.632]  [00:00:47.602][detail][EM] Rxd Ack; Removing MessageCounter:181174533 from Retrans Table on exchange 41958r
[16:27:01.680]  [00:00:47.653][detail][IN] UDP Message Received packet nb : 60 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 110
[16:27:01.681]  [00:00:47.655][info  ][EM] >>> [E:41960r S:25602 M:245903553] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:06 (IM:WriteRequest) (B:110)
[16:27:01.683]  [00:00:47.655][detail][EM] Handling via exchange: 41960r, Delegate: 0x2000413c
[16:27:01.684]  [00:00:47.655][detail][IM] Received Write request
[16:27:01.685]  [00:00:47.655][detail][DMG] IM WH moving to [Initialized]
[16:27:01.686]  [00:00:47.657][detail][DMG] Writing attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000
[16:27:01.687]  [00:00:47.660][detail][EVL] Copy Event to next buffer with priority 1
[16:27:01.688]  [00:00:47.661][detail][EVL] LogEvent event number: 0x0000000000000007 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6AD065E5
[16:27:01.690]  [00:00:47.662][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000B5BA and max: 0x000000000009DD7A
[16:27:01.691]  [00:00:47.662][detail][DMG] Urgent event will be sent once reporting is not blocked by the min interval
[16:27:01.692]  [00:00:47.663][detail][EVL] Copy Event to next buffer with priority 1
[16:27:01.693]  [00:00:47.664][detail][EVL] Copy Event to next buffer with priority 1
[16:27:01.694]  [00:00:47.665][detail][EVL] LogEvent event number: 0x0000000000000008 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6AD065E9
[16:27:01.696]  [00:00:47.665][detail][DMG] Urgent event will be sent once reporting is not blocked by the min interval
[16:27:01.696]  [00:00:47.666][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:01.698]  [00:00:47.666][detail][DMG] IM WH moving to [AddStatus]
[16:27:01.698]  [00:00:47.669][info  ][EM] <<< [E:41960r S:25602 M:181174535 (Ack:245903553)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:07 (IM:WriteResponse) (B:62)
[16:27:01.701]  [00:00:47.669][info  ][EM] ??1 [E:41960r S:25602 M:181174535] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3359ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.703]  [00:00:47.670][detail][DMG] IM WH moving to [Sending]
[16:27:01.703]  [00:00:47.670][detail][DMG] IM WH moving to [Uninitialized]
[16:27:01.704]  [00:00:47.670][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000022 DirtyGeneration = 0x0000000000000023
[16:27:01.705]  [00:00:47.672][detail][DMG] <RE:Run> Cluster 1f, Attribute 0 is dirty
[16:27:01.706]  [00:00:47.673][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:01.710]  [00:00:47.683][detail][DMG] Fetched 2 events
[16:27:01.710]  [00:00:47.683][detail][DMG] <RE> Sending report (payload has 260 bytes)...
[16:27:01.712]  [00:00:47.685][info  ][EM] <<< [E:49927i S:25599 M:83709817] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:290)
[16:27:01.714]  [00:00:47.686][info  ][EM] ??1 [E:49927i S:25599 M:83709817] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3357ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.717]  [00:00:47.686][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:01.717]  [00:00:47.686][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 0, RE has no more messages
[16:27:01.813]  [00:00:47.786][detail][IN] UDP Message Received packet nb : 61 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:01.815]  [00:00:47.788][info  ][EM] >>> [E:41959r S:25602 M:245903554 (Ack:181174534)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:01.817]  [00:00:47.789][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:01.818]  [00:00:47.789][detail][EM] Rxd Ack; Removing MessageCounter:181174534 from Retrans Table on exchange 41959r
[16:27:01.819]  [00:00:47.789][info  ][IM] Received status response, status is 0x00
[16:27:01.820]  [00:00:47.789][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:01.820]  [00:00:47.790][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:01.821]  [00:00:47.790][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:01.823]  [00:00:47.790][detail][DMG] <RE:Run> Cluster 3e, Attribute 0 is dirty
[16:27:01.824]  [00:00:47.791][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:01.825]  [00:00:47.795][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:27:01.826]  [00:00:47.795][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:01.827]  [00:00:47.797][detail][DMG] <RE:Run> Cluster 3e, Attribute 2 is dirty
[16:27:01.828]  [00:00:47.797][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:01.829]  [00:00:47.798][detail][DMG] <RE:Run> Cluster 3e, Attribute 3 is dirty
[16:27:01.830]  [00:00:47.798][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:01.831]  [00:00:47.799][detail][DMG] <RE:Run> Cluster 3e, Attribute 4 is dirty
[16:27:01.832]  [00:00:47.799][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:27:01.833]  [00:00:47.801][detail][DMG] <RE:Run> Cluster 3e, Attribute 5 is dirty
[16:27:01.834]  [00:00:47.802][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:01.835]  [00:00:47.802][detail][DMG] <RE:Run> Cluster 3e, Attribute fffc is dirty
[16:27:01.836]  [00:00:47.803][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:01.837]  [00:00:47.803][detail][DMG] <RE:Run> Cluster 3e, Attribute fffd is dirty
[16:27:01.838]  [00:00:47.804][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:01.839]  [00:00:47.804][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_003E, attributeId: 0x0000_FFFD, err = b
[16:27:01.841]  [00:00:47.804][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:27:01.842]  [00:00:47.806][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:01.843]  [00:00:47.806][detail][DMG] Fetched 0 events
[16:27:01.844]  [00:00:47.807][detail][DMG] <RE> Sending report (payload has 1164 bytes)...
[16:27:01.845]  [00:00:47.809][info  ][EM] <<< [E:41959r S:25602 M:181174536 (Ack:245903554)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1198)
[16:27:01.847]  [00:00:47.811][info  ][EM] ??1 [E:41959r S:25602 M:181174536] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3389ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:01.849]  [00:00:47.811][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:01.849]  [00:00:47.811][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has more messages
[16:27:01.854]  [00:00:47.827][detail][IN] UDP Message Received packet nb : 62 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:01.855]  [00:00:47.828][info  ][EM] >>> [E:41960r S:25602 M:245903555 (Ack:181174535)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:01.858]  [00:00:47.829][detail][EM] Found matching exchange: 41960r, Delegate: 0
[16:27:01.859]  [00:00:47.829][detail][EM] Rxd Ack; Removing MessageCounter:181174535 from Retrans Table on exchange 41960r
[16:27:02.023]  [00:00:47.995][detail][IN] UDP Message Received packet nb : 63 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:02.025]  [00:00:47.997][info  ][EM] >>> [E:49927i S:25599 M:47048240 (Ack:83709817)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:02.026]  [00:00:47.998][detail][EM] Found matching exchange: 49927i, Delegate: 0x20005dd0
[16:27:02.028]  [00:00:47.998][detail][EM] Rxd Ack; Removing MessageCounter:83709817 from Retrans Table on exchange 49927i
[16:27:02.028]  [00:00:47.998][info  ][IM] Received status response, status is 0x00
[16:27:02.029]  [00:00:47.998][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:02.030]  [00:00:47.998][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:02.030]  [00:00:48.000][info  ][EM] <<< [E:49927i S:25599 M:83709818 (Ack:47048240)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:02.033]  [00:00:48.000][detail][EM] Flushed pending ack for MessageCounter:47048240 on exchange 49927i
[16:27:02.165]  [00:00:48.137][detail][IN] UDP Message Received packet nb : 64 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:02.166]  [00:00:48.139][info  ][EM] >>> [E:41959r S:25602 M:245903556 (Ack:181174536)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:02.168]  [00:00:48.139][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:02.170]  [00:00:48.139][detail][EM] Rxd Ack; Removing MessageCounter:181174536 from Retrans Table on exchange 41959r
[16:27:02.171]  [00:00:48.139][info  ][IM] Received status response, status is 0x00
[16:27:02.171]  [00:00:48.140][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:02.172]  [00:00:48.140][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:02.173]  [00:00:48.140][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:02.175]  [00:00:48.140][detail][DMG] <RE:Run> Cluster 3e, Attribute fffd is dirty
[16:27:02.175]  [00:00:48.141][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:02.177]  
[16:27:02.177]  [00:00:48.141][detail][DMG] <RE:Run> Cluster 3e, Attribute fff8 is dirty
[16:27:02.177]  [00:00:48.142][detail][DMG] <RE:Run> Cluster 3e, Attribute fff9 is dirty
[16:27:02.178]  [00:00:48.143][detail][DMG] <RE:Run> Cluster 3e, Attribute fffb is dirty
[16:27:02.179]  [00:00:48.145][detail][DMG] <RE:Run> Cluster 3c, Attribute 0 is dirty
[16:27:02.180]  [00:00:48.145][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:02.183]  
[16:27:02.183]  [00:00:48.146][detail][DMG] <RE:Run> Cluster 3c, Attribute 1 is dirty
[16:27:02.184]  [00:00:48.146][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:02.185]  [00:00:48.147][detail][DMG] <RE:Run> Cluster 3c, Attribute 2 is dirty
[16:27:02.186]  [00:00:48.147][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:02.187]  [00:00:48.148][detail][DMG] <RE:Run> Cluster 3c, Attribute fffc is dirty
[16:27:02.188]  [00:00:48.150][detail][DMG] Reading attribute: Cluster=0x0000_003C Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:02.190]  
[16:27:02.190]  [00:00:48.150][detail][DMG] <RE:Run> Cluster 3c, Attribute fff8 is dirty
[16:27:02.190]  [00:00:48.151][detail][DMG] <RE:Run> Cluster 3c, Attribute fff9 is dirty
[16:27:02.191]  [00:00:48.152][detail][DMG] <RE:Run> Cluster 3c, Attribute fffb is dirty
[16:27:02.192]  
[16:27:02.192]  [00:00:48.153][detail][DMG] <RE:Run> Cluster 34, Attribute 0 is dirty
[16:27:02.193]  [00:00:48.159][detail][DMG] <RE:Run> Cluster 34, Attribute 1 is dirty
[16:27:02.194]  [00:00:48.159][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:02.195]  [00:00:48.160][detail][DMG] <RE:Run> Cluster 34, Attribute 2 is dirty
[16:27:02.196]  [00:00:48.161][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:02.197]  
[16:27:02.197]  [00:00:48.161][detail][DMG] <RE:Run> Cluster 34, Attribute 3 is dirty
[16:27:02.198]  [00:00:48.162][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:02.199]  
[16:27:02.199]  [00:00:48.163][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:02.201]  
[16:27:02.201]  [00:00:48.163][detail][DMG] <RE:Run> Cluster 34, Attribute fffd is dirty
[16:27:02.202]  
[16:27:02.202]  [00:00:48.164][detail][DMG] Reading attribute: Cluster=0x0000_0034 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:02.203]  
[16:27:02.203]  [00:00:48.165][detail][DMG] <RE:Run> Cluster 34, Attribute fff9 is dirty
[16:27:02.204]  
[16:27:02.204]  [00:00:48.166][detail][DMG] <RE:Run> Cluster 34, Attribute fffb is dirty
[16:27:02.205]  [00:00:48.166][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[16:27:02.206]  [00:00:48.167][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:02.208]  [00:00:48.168][detail][DMG] <RE:Run> Cluster 33, Attribute 1 is dirty
[16:27:02.208]  [00:00:48.170][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:27:02.209]  [00:00:48.170][detail][DMG] <RE:Run> Cluster 33, Attribute 3 is dirty
[16:27:02.210]  [00:00:48.172][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:27:02.211]  [00:00:48.173][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:02.213]  [00:00:48.176][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:02.214]  [00:00:48.176][detail][DMG] Fetched 0 events
[16:27:02.215]  [00:00:48.179][info  ][EM] <<< [E:41959r S:25602 M:181174537 (Ack:245903556)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1189)
[16:27:02.217]  [00:00:48.180][info  ][EM] ??1 [E:41959r S:25602 M:181174537] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3373ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:02.219]  [00:00:48.180][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:02.219]  [00:00:48.180][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:02.320]  
[16:27:02.668]  [00:00:48.640][detail][IN] UDP Message Received packet nb : 65 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:02.669]  [00:00:48.642][info  ][EM] >>> [E:41959r S:25602 M:245903557 (Ack:181174537)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:02.671]  [00:00:48.642][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:02.673]  [00:00:48.642][detail][EM] Rxd Ack; Removing MessageCounter:181174537 from Retrans Table on exchange 41959r
[16:27:02.673]  [00:00:48.643][info  ][IM] Received status response, status is 0x00
[16:27:02.674]  [00:00:48.643][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:02.675]  [00:00:48.643][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:02.676]  [00:00:48.643][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:02.678]  
[16:27:02.678]  [00:00:48.644][detail][DMG] <RE:Run> Cluster 33, Attribute 5 is dirty
[16:27:02.678]  [00:00:48.644][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:02.680]  
[16:27:02.680]  [00:00:48.645][detail][DMG] <RE:Run> Cluster 33, Attribute 6 is dirty
[16:27:02.680]  [00:00:48.645][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:27:02.682]  
[16:27:02.682]  [00:00:48.646][detail][DMG] <RE:Run> Cluster 33, Attribute 7 is dirty
[16:27:02.683]  [00:00:48.646][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:27:02.684]  
[16:27:02.685]  [00:00:48.647][detail][DMG] <RE:Run> Cluster 33, Attribute 2 is dirty
[16:27:02.685]  [00:00:48.648][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:02.687]  
[16:27:02.687]  [00:00:48.648][detail][DMG] <RE:Run> Cluster 33, Attribute fffc is dirty
[16:27:02.687]  
[16:27:02.687]  [00:00:48.649][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:02.689]  
[16:27:02.689]  [00:00:48.650][detail][DMG] <RE:Run> Cluster 33, Attribute fff8 is dirty
[16:27:02.690]  [00:00:48.651][detail][DMG] <RE:Run> Cluster 33, Attribute fff9 is dirty
[16:27:02.691]  [00:00:48.653][detail][DMG] <RE:Run> Cluster 30, Attribute 0 is dirty
[16:27:02.691]  [00:00:48.654][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:02.693]  
[16:27:02.693]  [00:00:48.655][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:02.694]  
[16:27:02.694]  [00:00:48.656][detail][DMG] <RE:Run> Cluster 30, Attribute 2 is dirty
[16:27:02.695]  [00:00:48.658][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:02.696]  
[16:27:02.696]  [00:00:48.658][detail][DMG] <RE:Run> Cluster 30, Attribute 4 is dirty
[16:27:02.698]  [00:00:48.660][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:02.698]  [00:00:48.661][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:02.700]  
[16:27:02.700]  [00:00:48.662][detail][DMG] <RE:Run> Cluster 30, Attribute fff9 is dirty
[16:27:02.701]  [00:00:48.663][detail][DMG] <RE:Run> Cluster 30, Attribute fffb is dirty
[16:27:02.702]  
[16:27:02.702]  [00:00:48.664][detail][DMG] <RE:Run> Cluster 2b, Attribute 0 is dirty
[16:27:02.703]  [00:00:48.665][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:02.704]  
[16:27:02.704]  [00:00:48.666][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:02.705]  
[16:27:02.705]  [00:00:48.666][detail][DMG] <RE:Run> Cluster 2b, Attribute fffd is dirty
[16:27:02.707]  
[16:27:02.707]  [00:00:48.667][detail][DMG] Reading attribute: Cluster=0x0000_002B Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:02.708]  
[16:27:02.708]  [00:00:48.669][detail][DMG] <RE:Run> Cluster 2b, Attribute fffb is dirty
[16:27:02.709]  
[16:27:02.709]  [00:00:48.670][detail][DMG] <RE:Run> Cluster 28, Attribute 0 is dirty
[16:27:02.710]  [00:00:48.671][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:02.711]  
[16:27:02.712]  [00:00:48.673][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:27:02.712]  [00:00:48.673][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:02.714]  
[16:27:02.714]  [00:00:48.675][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:02.715]  [00:00:48.675][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:27:02.716]  
[16:27:02.716]  [00:00:48.677][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:02.717]  
[16:27:02.717]  [00:00:48.678][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:27:02.719]  [00:00:48.679][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:27:02.720]  
[16:27:02.720]  [00:00:48.681][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:27:02.721]  [00:00:48.682][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:27:02.723]  [00:00:48.682][detail][DMG] <RE:Run> Cluster 28, Attribute a is dirty
[16:27:02.723]  [00:00:48.684][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0013 (expanded=1)
[16:27:02.725]  [00:00:48.685][detail][DMG] <RE:Run> Cluster 28, Attribute 15 is dirty
[16:27:02.725]  [00:00:48.686][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:27:02.727]  [00:00:48.688][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:02.728]  [00:00:48.691][info  ][EM] <<< [E:41959r S:25602 M:181174538 (Ack:245903557)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1208)
[16:27:02.730]  [00:00:48.692][info  ][EM] ??1 [E:41959r S:25602 M:181174538] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3346ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:02.732]  [00:00:48.692][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:03.472]  [00:00:49.445][detail][IN] UDP Message Received packet nb : 66 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:03.474]  [00:00:49.447][info  ][EM] >>> [E:41959r S:25602 M:245903558 (Ack:181174538)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:03.476]  [00:00:49.447][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:03.477]  [00:00:49.448][detail][EM] Rxd Ack; Removing MessageCounter:181174538 from Retrans Table on exchange 41959r
[16:27:03.478]  [00:00:49.448][info  ][IM] Received status response, status is 0x00
[16:27:03.479]  [00:00:49.448][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:03.479]  [00:00:49.448][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:03.480]  [00:00:49.448][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:03.482]  
[16:27:03.482]  [00:00:49.449][detail][DMG] <RE:Run> Cluster 28, Attribute 15 is dirty
[16:27:03.483]  [00:00:49.449][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:27:03.484]  
[16:27:03.484]  [00:00:49.450][detail][DMG] <RE:Run> Cluster 28, Attribute 16 is dirty
[16:27:03.485]  [00:00:49.451][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0016 (expanded=1)
[16:27:03.486]  
[16:27:03.487]  [00:00:49.451][detail][DMG] <RE:Run> Cluster 28, Attribute b is dirty
[16:27:03.488]  [00:00:49.452][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:27:03.488]  
[16:27:03.489]  [00:00:49.452][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0028, attributeId: 0x0000_000Berr = 2f
[16:27:03.491]  
[16:27:03.491]  [00:00:49.453][detail][DMG] <RE:Run> Cluster 28, Attribute c is dirty
[16:27:03.491]  [00:00:49.453][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000C (expanded=1)
[16:27:03.493]  [00:00:49.454][detail][DMG] <RE:Run> Cluster 28, Attribute d is dirty
[16:27:03.493]  [00:00:49.456][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:27:03.495]  
[16:27:03.495]  [00:00:49.456][detail][DMG] <RE:Run> Cluster 28, Attribute f is dirty
[16:27:03.496]  
[16:27:03.496]  [00:00:49.457][detail][DMG] <RE:Run> Cluster 28, Attribute 10 is dirty
[16:27:03.497]  [00:00:49.458][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:27:03.498]  
[16:27:03.498]  [00:00:49.459][detail][DMG] <RE:Run> Cluster 28, Attribute fffc is dirty
[16:27:03.499]  
[16:27:03.499]  [00:00:49.460][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:03.500]  [00:00:49.461][detail][DMG] <RE:Run> Cluster 28, Attribute fff8 is dirty
[16:27:03.501]  [00:00:49.463][detail][DMG] <RE:Run> Cluster 28, Attribute fffb is dirty
[16:27:03.502]  [00:00:49.465][detail][DMG] <RE:Run> Cluster 1f, Attribute 0 is dirty
[16:27:03.503]  
[16:27:03.503]  [00:00:49.465][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:03.504]  [00:00:49.466][detail][DMG] <RE:Run> Cluster 1f, Attribute 2 is dirty
[16:27:03.505]  [00:00:49.468][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:03.507]  
[16:27:03.507]  [00:00:49.469][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:27:03.508]  
[16:27:03.508]  [00:00:49.469][detail][DMG] <RE:Run> Cluster 1f, Attribute fffc is dirty
[16:27:03.509]  [00:00:49.471][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:03.510]  
[16:27:03.511]  [00:00:49.472][detail][DMG] <RE:Run> Cluster 1f, Attribute fff9 is dirty
[16:27:03.511]  [00:00:49.473][detail][DMG] <RE:Run> Cluster 1f, Attribute fffb is dirty
[16:27:03.512]  [00:00:49.474][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:03.513]  [00:00:49.475][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:03.514]  
[16:27:03.514]  [00:00:49.476][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:03.516]  [00:00:49.477][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:27:03.516]  
[16:27:03.516]  [00:00:49.478][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:03.518]  [00:00:49.479][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:27:03.518]  [00:00:49.481][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:03.520]  [00:00:49.481][detail][DMG] <RE:Run> Cluster 1d, Attribute fff8 is dirty
[16:27:03.520]  [00:00:49.483][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:27:03.521]  [00:00:49.484][detail][DMG] <RE:Run> Cluster 31, Attribute 0 is dirty
[16:27:03.522]  [00:00:49.485][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:03.523]  [00:00:49.485][detail][DMG] <RE:Run> Cluster 31, Attribute 1 is dirty
[16:27:03.524]  [00:00:49.489][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:03.525]  [00:00:49.489][detail][DMG] Fetched 0 events
[16:27:03.526]  [00:00:49.491][info  ][EM] <<< [E:41959r S:25602 M:181174539 (Ack:245903558)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1189)
[16:27:03.529]  [00:00:49.493][info  ][EM] ??1 [E:41959r S:25602 M:181174539] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3402ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:03.530]  [00:00:49.493][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:03.531]  [00:00:49.493][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:03.989]  [00:00:49.961][detail][IN] UDP Message Received packet nb : 67 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:03.990]  [00:00:49.963][info  ][EM] >>> [E:41959r S:25602 M:245903559 (Ack:181174539)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:03.992]  [00:00:49.963][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:03.993]  [00:00:49.963][detail][EM] Rxd Ack; Removing MessageCounter:181174539 from Retrans Table on exchange 41959r
[16:27:03.994]  [00:00:49.963][info  ][IM] Received status response, status is 0x00
[16:27:03.995]  [00:00:49.964][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:03.996]  [00:00:49.964][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:03.996]  [00:00:49.964][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:03.998]  [00:00:49.964][detail][DMG] <RE:Run> Cluster 31, Attribute 1 is dirty
[16:27:03.999]  [00:00:49.965][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:04.000]  [00:00:49.967][detail][DMG] <RE:Run> Cluster 31, Attribute 4 is dirty
[16:27:04.001]  [00:00:49.968][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:27:04.002]  
[16:27:04.002]  [00:00:49.969][detail][DMG] <RE:Run> Cluster 31, Attribute 5 is dirty
[16:27:04.003]  
[16:27:04.003]  [00:00:49.970][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:04.005]  
[16:27:04.005]  [00:00:49.970][detail][DMG] <RE:Run> Cluster 31, Attribute 6 is dirty
[16:27:04.006]  
[16:27:04.006]  [00:00:49.970][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:27:04.007]  
[16:27:04.007]  [00:00:49.971][detail][DMG] <RE:Run> Cluster 31, Attribute 7 is dirty
[16:27:04.008]  [00:00:49.972][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:27:04.009]  [00:00:49.972][detail][DMG] <RE:Run> Cluster 31, Attribute 2 is dirty
[16:27:04.010]  [00:00:49.973][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:04.012]  
[16:27:04.012]  [00:00:49.973][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[16:27:04.012]  [00:00:49.974][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:04.014]  
[16:27:04.014]  [00:00:49.975][detail][DMG] <RE:Run> Cluster 31, Attribute a is dirty
[16:27:04.014]  [00:00:49.976][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:27:04.016]  
[16:27:04.016]  [00:00:49.977][detail][DMG] <RE:Run> Cluster 31, Attribute fffd is dirty
[16:27:04.017]  [00:00:49.979][detail][DMG] <RE:Run> Cluster 31, Attribute fff8 is dirty
[16:27:04.018]  [00:00:49.980][detail][DMG] <RE:Run> Cluster 31, Attribute fffb is dirty
[16:27:04.018]  [00:00:49.982][detail][DMG] <RE:Run> Cluster 2a, Attribute 0 is dirty
[16:27:04.019]  [00:00:49.983][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:04.021]  [00:00:49.983][detail][DMG] <RE:Run> Cluster 2a, Attribute 1 is dirty
[16:27:04.021]  
[16:27:04.021]  [00:00:49.985][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:04.023]  
[16:27:04.023]  [00:00:49.985][detail][DMG] <RE:Run> Cluster 2a, Attribute 3 is dirty
[16:27:04.024]  
[16:27:04.024]  [00:00:49.987][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:04.025]  [00:00:49.988][detail][DMG] <RE:Run> Cluster 2a, Attribute fffd is dirty
[16:27:04.026]  
[16:27:04.026]  [00:00:49.990][detail][DMG] <RE:Run> Cluster 2a, Attribute fff9 is dirty
[16:27:04.027]  [00:00:49.991][detail][DMG] <RE:Run> Cluster 2a, Attribute fffb is dirty
[16:27:04.028]  [00:00:49.992][detail][DMG] <RE:Run> Cluster 2d, Attribute 0 is dirty
[16:27:04.029]  
[16:27:04.029]  [00:00:49.993][detail][DMG] Reading attribute: Cluster=0x0000_002D Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:04.030]  
[16:27:04.030]  [00:00:49.993][detail][DMG] <RE:Run> Cluster 2d, Attribute fffc is dirty
[16:27:04.031]  
[16:27:04.031]  [00:00:49.994][detail][DMG] Reading attribute: Cluster=0x0000_002D Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:04.032]  
[16:27:04.033]  [00:00:49.995][detail][DMG] Reading attribute: Cluster=0x0000_002D Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:04.034]  
[16:27:04.034]  [00:00:49.997][detail][DMG] <RE:Run> Cluster 2d, Attribute fffb is dirty
[16:27:04.035]  
[16:27:04.035]  [00:00:49.998][detail][DMG] <RE:Run> Cluster 2f, Attribute 0 is dirty
[16:27:04.036]  
[16:27:04.036]  [00:00:49.999][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:04.037]  
[16:27:04.038]  [00:00:50.000][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:04.039]  
[16:27:04.039]  [00:00:50.000][detail][DMG] <RE:Run> Cluster 2f, Attribute 2 is dirty
[16:27:04.040]  [00:00:50.000][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:04.041]  
[16:27:04.041]  [00:00:50.002][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:27:04.043]  [00:00:50.003][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_000F (expanded=1)
[16:27:04.044]  [00:00:50.004][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:27:04.046]  
[16:27:04.046]  [00:00:50.005][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_001A (expanded=1)
[16:27:04.047]  [00:00:50.007][detail][DMG] <RE:Run> Cluster 2f, Attribute 1f is dirty
[16:27:04.048]  [00:00:50.008][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_001F (expanded=1)
[16:27:04.049]  [00:00:50.009][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:04.051]  [00:00:50.010][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:04.051]  [00:00:50.013][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:04.053]  [00:00:50.013][detail][DMG] Fetched 0 events
[16:27:04.053]  [00:00:50.015][info  ][EM] <<< [E:41959r S:25602 M:181174540 (Ack:245903559)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1205)
[16:27:04.056]  [00:00:50.016][info  ][EM] ??1 [E:41959r S:25602 M:181174540] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3356ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:04.058]  [00:00:50.017][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:04.320]  
[16:27:04.480]  [00:00:50.453][detail][IN] UDP Message Received packet nb : 68 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:04.482]  [00:00:50.455][info  ][EM] >>> [E:41959r S:25602 M:245903560 (Ack:181174540)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:04.484]  [00:00:50.456][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:04.485]  [00:00:50.456][detail][EM] Rxd Ack; Removing MessageCounter:181174540 from Retrans Table on exchange 41959r
[16:27:04.486]  [00:00:50.456][info  ][IM] Received status response, status is 0x00
[16:27:04.487]  [00:00:50.456][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:04.487]  [00:00:50.457][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:04.488]  [00:00:50.457][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:04.490]  [00:00:50.457][detail][DMG] <RE:Run> Cluster 2f, Attribute fffd is dirty
[16:27:04.491]  [00:00:50.458][detail][DMG] Reading attribute: Cluster=0x0000_002F Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:04.492]  [00:00:50.458][detail][DMG] <RE:Run> Cluster 2f, Attribute fff8 is dirty
[16:27:04.493]  [00:00:50.458][detail][DMG] <RE:Run> Cluster 2f, Attribute fff9 is dirty
[16:27:04.494]  [00:00:50.459][detail][DMG] <RE:Run> Cluster 2f, Attribute fffb is dirty
[16:27:04.494]  [00:00:50.461][detail][DMG] <RE:Run> Cluster 35, Attribute 0 is dirty
[16:27:04.495]  [00:00:50.462][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:04.496]  [00:00:50.463][detail][DMG] <RE:Run> Cluster 35, Attribute 1 is dirty
[16:27:04.497]  [00:00:50.464][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:04.498]  [00:00:50.464][detail][DMG] <RE:Run> Cluster 35, Attribute 2 is dirty
[16:27:04.499]  [00:00:50.465][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:04.500]  [00:00:50.466][detail][DMG] <RE:Run> Cluster 35, Attribute 3 is dirty
[16:27:04.501]  [00:00:50.467][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:27:04.503]  [00:00:50.468][detail][DMG] <RE:Run> Cluster 35, Attribute 4 is dirty
[16:27:04.503]  [00:00:50.469][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=1)
[16:27:04.505]  [00:00:50.470][detail][DMG] <RE:Run> Cluster 35, Attribute 5 is dirty
[16:27:04.505]  [00:00:50.471][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0005 (expanded=1)
[16:27:04.507]  [00:00:50.471][detail][DMG] <RE:Run> Cluster 35, Attribute 6 is dirty
[16:27:04.507]  [00:00:50.472][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0006 (expanded=1)
[16:27:04.509]  [00:00:50.473][detail][DMG] <RE:Run> Cluster 35, Attribute 7 is dirty
[16:27:04.510]  [00:00:50.474][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0007 (expanded=1)
[16:27:04.511]  
[16:27:04.511]  [00:00:50.475][detail][DMG] <RE:Run> Cluster 35, Attribute 8 is dirty
[16:27:04.512]  [00:00:50.476][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0008 (expanded=1)
[16:27:04.513]  [00:00:50.477][detail][DMG] <RE:Run> Cluster 35, Attribute 9 is dirty
[16:27:04.514]  [00:00:50.478][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0009 (expanded=1)
[16:27:04.515]  
[16:27:04.515]  [00:00:50.478][detail][DMG] <RE:Run> Cluster 35, Attribute a is dirty
[16:27:04.516]  [00:00:50.479][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000A (expanded=1)
[16:27:04.517]  
[16:27:04.518]  [00:00:50.480][detail][DMG] <RE:Run> Cluster 35, Attribute b is dirty
[16:27:04.519]  [00:00:50.481][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000B (expanded=1)
[16:27:04.519]  [00:00:50.482][detail][DMG] <RE:Run> Cluster 35, Attribute c is dirty
[16:27:04.521]  [00:00:50.483][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000C (expanded=1)
[16:27:04.521]  [00:00:50.485][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000D (expanded=1)
[16:27:04.523]  [00:00:50.485][detail][DMG] <RE:Run> Cluster 35, Attribute e is dirty
[16:27:04.523]  [00:00:50.486][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_000E (expanded=1)
[16:27:04.525]  [00:00:50.487][detail][DMG] <RE:Run> Cluster 35, Attribute f is dirty
[16:27:04.525]  [00:00:50.489][detail][DMG] <RE:Run> Cluster 35, Attribute 10 is dirty
[16:27:04.526]  [00:00:50.490][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0010 (expanded=1)
[16:27:04.528]  [00:00:50.492][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0011 (expanded=1)
[16:27:04.529]  [00:00:50.492][detail][DMG] <RE:Run> Cluster 35, Attribute 12 is dirty
[16:27:04.530]  [00:00:50.494][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0012 (expanded=1)
[16:27:04.531]  [00:00:50.495][detail][DMG] <RE:Run> Cluster 35, Attribute 13 is dirty
[16:27:04.532]  [00:00:50.496][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0013 (expanded=1)
[16:27:04.533]  
[16:27:04.533]  [00:00:50.498][detail][DMG] <RE:Run> Cluster 35, Attribute 14 is dirty
[16:27:04.535]  [00:00:50.499][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0014 (expanded=1)
[16:27:04.535]  [00:00:50.500][detail][DMG] <RE:Run> Cluster 35, Attribute 15 is dirty
[16:27:04.536]  [00:00:50.500][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0015 (expanded=1)
[16:27:04.537]  [00:00:50.501][detail][DMG] <RE:Run> Cluster 35, Attribute 16 is dirty
[16:27:04.538]  
[16:27:04.539]  [00:00:50.502][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0016 (expanded=1)
[16:27:04.540]  [00:00:50.502][detail][DMG] <RE:Run> Cluster 35, Attribute 17 is dirty
[16:27:04.541]  [00:00:50.503][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0017 (expanded=1)
[16:27:04.542]  
[16:27:04.542]  [00:00:50.504][detail][DMG] <RE:Run> Cluster 35, Attribute 18 is dirty
[16:27:04.543]  [00:00:50.505][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0018 (expanded=1)
[16:27:04.544]  [00:00:50.507][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0019 (expanded=1)
[16:27:04.546]  
[16:27:04.546]  [00:00:50.508][detail][DMG] <RE:Run> Cluster 35, Attribute 1a is dirty
[16:27:04.546]  [00:00:50.509][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001A (expanded=1)
[16:27:04.548]  [00:00:50.509][detail][DMG] <RE:Run> Cluster 35, Attribute 1b is dirty
[16:27:04.548]  
[16:27:04.548]  [00:00:50.510][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001B (expanded=1)
[16:27:04.550]  [00:00:50.512][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001C (expanded=1)
[16:27:04.551]  
[16:27:04.551]  [00:00:50.513][detail][DMG] <RE:Run> Cluster 35, Attribute 1d is dirty
[16:27:04.552]  [00:00:50.514][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001D (expanded=1)
[16:27:04.553]  
[16:27:04.554]  [00:00:50.515][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001E (expanded=1)
[16:27:04.555]  [00:00:50.516][detail][DMG] <RE:Run> Cluster 35, Attribute 1f is dirty
[16:27:04.555]  [00:00:50.517][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_001F (expanded=1)
[16:27:04.557]  
[16:27:04.557]  [00:00:50.519][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0020 (expanded=1)
[16:27:04.558]  [00:00:50.520][detail][DMG] <RE:Run> Cluster 35, Attribute 21 is dirty
[16:27:04.560]  [00:00:50.521][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0021 (expanded=1)
[16:27:04.560]  [00:00:50.522][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0022 (expanded=1)
[16:27:04.562]  [00:00:50.523][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0035, attributeId: 0x0000_0022, err = b
[16:27:04.564]  [00:00:50.525][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:04.564]  [00:00:50.525][detail][DMG] Fetched 0 events
[16:27:04.565]  [00:00:50.528][info  ][EM] <<< [E:41959r S:25602 M:181174541 (Ack:245903560)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1204)
[16:27:04.568]  [00:00:50.529][info  ][EM] ??1 [E:41959r S:25602 M:181174541] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3364ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:04.569]  [00:00:50.530][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:05.193]  [00:00:51.166][detail][IN] UDP Message Received packet nb : 69 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:05.194]  [00:00:51.167][info  ][EM] >>> [E:41959r S:25602 M:245903561 (Ack:181174541)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:05.196]  [00:00:51.167][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:05.198]  [00:00:51.167][detail][EM] Rxd Ack; Removing MessageCounter:181174541 from Retrans Table on exchange 41959r
[16:27:05.198]  [00:00:51.168][info  ][IM] Received status response, status is 0x00
[16:27:05.199]  [00:00:51.168][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:05.200]  [00:00:51.168][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:05.201]  [00:00:51.168][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:05.203]  [00:00:51.169][detail][DMG] <RE:Run> Cluster 35, Attribute 22 is dirty
[16:27:05.203]  [00:00:51.170][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0022 (expanded=1)
[16:27:05.205]  [00:00:51.171][detail][DMG] <RE:Run> Cluster 35, Attribute 23 is dirty
[16:27:05.205]  [00:00:51.172][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0023 (expanded=1)
[16:27:05.207]  [00:00:51.172][detail][DMG] <RE:Run> Cluster 35, Attribute 24 is dirty
[16:27:05.207]  [00:00:51.173][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0024 (expanded=1)
[16:27:05.209]  [00:00:51.174][detail][DMG] <RE:Run> Cluster 35, Attribute 25 is dirty
[16:27:05.209]  [00:00:51.175][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0025 (expanded=1)
[16:27:05.211]  [00:00:51.176][detail][DMG] <RE:Run> Cluster 35, Attribute 26 is dirty
[16:27:05.211]  [00:00:51.177][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0026 (expanded=1)
[16:27:05.213]  [00:00:51.178][detail][DMG] <RE:Run> Cluster 35, Attribute 27 is dirty
[16:27:05.214]  [00:00:51.179][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0027 (expanded=1)
[16:27:05.215]  [00:00:51.179][detail][DMG] <RE:Run> Cluster 35, Attribute 28 is dirty
[16:27:05.216]  [00:00:51.180][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0028 (expanded=1)
[16:27:05.217]  
[16:27:05.217]  [00:00:51.181][detail][DMG] <RE:Run> Cluster 35, Attribute 29 is dirty
[16:27:05.218]  [00:00:51.182][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0029 (expanded=1)
[16:27:05.219]  [00:00:51.183][detail][DMG] <RE:Run> Cluster 35, Attribute 2a is dirty
[16:27:05.220]  [00:00:51.184][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002A (expanded=1)
[16:27:05.221]  [00:00:51.184][detail][DMG] <RE:Run> Cluster 35, Attribute 2b is dirty
[16:27:05.222]  
[16:27:05.222]  [00:00:51.185][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002B (expanded=1)
[16:27:05.223]  [00:00:51.186][detail][DMG] <RE:Run> Cluster 35, Attribute 2c is dirty
[16:27:05.224]  [00:00:51.187][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002C (expanded=1)
[16:27:05.225]  
[16:27:05.225]  [00:00:51.188][detail][DMG] <RE:Run> Cluster 35, Attribute 2d is dirty
[16:27:05.226]  [00:00:51.189][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002D (expanded=1)
[16:27:05.227]  [00:00:51.191][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002E (expanded=1)
[16:27:05.229]  
[16:27:05.229]  [00:00:51.191][detail][DMG] <RE:Run> Cluster 35, Attribute 2f is dirty
[16:27:05.230]  [00:00:51.192][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_002F (expanded=1)
[16:27:05.231]  [00:00:51.193][detail][DMG] <RE:Run> Cluster 35, Attribute 30 is dirty
[16:27:05.232]  [00:00:51.194][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0030 (expanded=1)
[16:27:05.233]  
[16:27:05.234]  [00:00:51.196][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0031 (expanded=1)
[16:27:05.234]  [00:00:51.197][detail][DMG] <RE:Run> Cluster 35, Attribute 32 is dirty
[16:27:05.236]  [00:00:51.198][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0032 (expanded=1)
[16:27:05.236]  [00:00:51.199][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0033 (expanded=1)
[16:27:05.238]  
[16:27:05.238]  [00:00:51.200][detail][DMG] <RE:Run> Cluster 35, Attribute 34 is dirty
[16:27:05.239]  [00:00:51.201][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0034 (expanded=1)
[16:27:05.240]  [00:00:51.203][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0035 (expanded=1)
[16:27:05.241]  [00:00:51.204][detail][DMG] <RE:Run> Cluster 35, Attribute 36 is dirty
[16:27:05.242]  [00:00:51.205][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0036 (expanded=1)
[16:27:05.243]  [00:00:51.205][detail][DMG] <RE:Run> Cluster 35, Attribute 37 is dirty
[16:27:05.244]  [00:00:51.207][detail][DMG] <RE:Run> Cluster 35, Attribute 38 is dirty
[16:27:05.245]  [00:00:51.208][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0038 (expanded=1)
[16:27:05.246]  [00:00:51.208][detail][DMG] <RE:Run> Cluster 35, Attribute 39 is dirty
[16:27:05.247]  [00:00:51.209][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_0039 (expanded=1)
[16:27:05.248]  [00:00:51.211][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003A (expanded=1)
[16:27:05.250]  
[16:27:05.250]  [00:00:51.212][detail][DMG] <RE:Run> Cluster 35, Attribute 3b is dirty
[16:27:05.251]  
[16:27:05.251]  [00:00:51.213][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003B (expanded=1)
[16:27:05.252]  [00:00:51.214][detail][DMG] <RE:Run> Cluster 35, Attribute 3c is dirty
[16:27:05.253]  [00:00:51.215][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003C (expanded=1)
[16:27:05.254]  [00:00:51.216][detail][DMG] <RE:Run> Cluster 35, Attribute 3d is dirty
[16:27:05.255]  [00:00:51.218][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003D (expanded=1)
[16:27:05.257]  [00:00:51.219][detail][DMG] <RE:Run> Cluster 35, Attribute 3e is dirty
[16:27:05.257]  [00:00:51.220][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_003E (expanded=1)
[16:27:05.259]  [00:00:51.220][detail][DMG] <RE:Run> Cluster 35, Attribute fffc is dirty
[16:27:05.259]  [00:00:51.221][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:05.261]  [00:00:51.223][detail][DMG] Reading attribute: Cluster=0x0000_0035 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:05.261]  [00:00:51.225][detail][DMG] <RE:Run> Cluster 35, Attribute fff9 is dirty
[16:27:05.263]  
[16:27:05.263]  [00:00:51.228][detail][DMG] <RE:Run> Cluster 35, Attribute fffb is dirty
[16:27:05.264]  [00:00:51.231][detail][DMG] <RE:Run> Cluster 46, Attribute 0 is dirty
[16:27:05.264]  
[16:27:05.264]  [00:00:51.231][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:05.266]  [00:00:51.232][detail][DMG] <RE:Run> Cluster 46, Attribute 1 is dirty
[16:27:05.266]  [00:00:51.232][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:05.268]  [00:00:51.233][detail][DMG] <RE:Run> Cluster 46, Attribute 2 is dirty
[16:27:05.268]  [00:00:51.233][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:05.270]  [00:00:51.234][detail][DMG] <RE:Run> Cluster 46, Attribute fffc is dirty
[16:27:05.270]  [00:00:51.234][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:05.272]  [00:00:51.235][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0046, attributeId: 0x0000_FFFC, err = b
[16:27:05.273]  [00:00:51.237][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:05.275]  [00:00:51.237][detail][DMG] Fetched 0 events
[16:27:05.275]  [00:00:51.240][info  ][EM] <<< [E:41959r S:25602 M:181174542 (Ack:245903561)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1203)
[16:27:05.278]  [00:00:51.241][info  ][EM] ??1 [E:41959r S:25602 M:181174542] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3377ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:05.279]  [00:00:51.242][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:05.280]  [00:00:51.242][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:05.686]  [00:00:51.659][detail][IN] UDP Message Received packet nb : 70 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:05.688]  [00:00:51.661][info  ][EM] >>> [E:41959r S:25602 M:245903562 (Ack:181174542)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:05.690]  [00:00:51.661][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:05.691]  [00:00:51.661][detail][EM] Rxd Ack; Removing MessageCounter:181174542 from Retrans Table on exchange 41959r
[16:27:05.692]  [00:00:51.662][info  ][IM] Received status response, status is 0x00
[16:27:05.693]  [00:00:51.662][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:05.693]  [00:00:51.662][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:05.694]  [00:00:51.662][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:05.696]  [00:00:51.662][detail][DMG] <RE:Run> Cluster 46, Attribute fffc is dirty
[16:27:05.697]  [00:00:51.663][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:27:05.698]  
[16:27:05.698]  [00:00:51.663][detail][DMG] <RE:Run> Cluster 46, Attribute fffd is dirty
[16:27:05.699]  
[16:27:05.699]  [00:00:51.664][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_FFFD (expanded=1)
[16:27:05.700]  
[16:27:05.701]  [00:00:51.665][detail][DMG] <RE:Run> Cluster 46, Attribute fff8 is dirty
[16:27:05.702]  
[16:27:05.702]  [00:00:51.665][detail][DMG] <RE:Run> Cluster 46, Attribute fff9 is dirty
[16:27:05.702]  
[16:27:05.702]  [00:00:51.666][detail][DMG] <RE:Run> Cluster 46, Attribute fffb is dirty
[16:27:05.704]  
[16:27:05.704]  [00:00:51.667][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:05.704]  
[16:27:05.704]  [00:00:51.667][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:27:05.706]  
[16:27:05.706]  [00:00:51.668][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:27:05.707]  
[16:27:05.707]  [00:00:51.668][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:27:05.709]  
[16:27:05.709]  [00:00:51.669][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:27:05.709]  [00:00:51.670][detail][DMG] <RE:Run> Cluster 1d, Attribute fffc is dirty
[16:27:05.710]  [00:00:51.671][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x1 AttributeId=0x0000_FFFD (expanded=1)
[16:27:05.711]  
[16:27:05.711]  [00:00:51.673][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:27:05.712]  
[16:27:05.713]  [00:00:51.674][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:27:05.714]  
[16:27:05.714]  [00:00:51.675][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:27:05.715]  
[16:27:05.715]  [00:00:51.676][detail][DMG] <RE:Run> Cluster 3, Attribute fffd is dirty
[16:27:05.715]  
[16:27:05.716]  [00:00:51.677][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:27:05.717]  
[16:27:05.717]  [00:00:51.679][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x1 AttributeId=0x0000_0000 (expanded=1)
[16:27:05.718]  
[16:27:05.718]  [00:00:51.679][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x1 AttributeId=0x0000_FFFC (expanded=1)
[16:27:05.720]  
[16:27:05.720]  [00:00:51.681][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:27:05.721]  
[16:27:05.721]  [00:00:51.682][detail][DMG] <RE:Run> Cluster 4, Attribute fffb is dirty
[16:27:05.722]  
[16:27:05.722]  [00:00:51.682][detail][DMG] <RE:Run> Cluster 102, Attribute 0 is dirty
[16:27:05.722]  [00:00:51.684][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0001 (expanded=1)
[16:27:05.724]  [00:00:51.685][detail][DMG] <RE:Run> Cluster 102, Attribute 5 is dirty
[16:27:05.725]  [00:00:51.686][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0007 (expanded=1)
[16:27:05.726]  [00:00:51.687][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0008 (expanded=1)
[16:27:05.727]  
[16:27:05.727]  [00:00:51.689][detail][DMG] <RE:Run> Cluster 102, Attribute b is dirty
[16:27:05.728]  [00:00:51.690][detail][DMG] <RE:Run> Cluster 102, Attribute d is dirty
[16:27:05.729]  [00:00:51.691][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_000E (expanded=1)
[16:27:05.730]  [00:00:51.693][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0011 (expanded=1)
[16:27:05.732]  [00:00:51.695][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:05.733]  [00:00:51.696][detail][DMG] Fetched 0 events
[16:27:05.734]  [00:00:51.696][detail][DMG] <RE> Sending report (payload has 1157 bytes)...
[16:27:05.734]  [00:00:51.698][info  ][EM] <<< [E:41959r S:25602 M:181174543 (Ack:245903562)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1191)
[16:27:05.736]  [00:00:51.699][info  ][EM] ??1 [E:41959r S:25602 M:181174543] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3363ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:05.738]  [00:00:51.700][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:06.188]  [00:00:52.161][detail][IN] UDP Message Received packet nb : 71 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:06.190]  [00:00:52.163][info  ][EM] >>> [E:41959r S:25602 M:245903563 (Ack:181174543)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:06.192]  [00:00:52.164][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:06.193]  [00:00:52.164][detail][EM] Rxd Ack; Removing MessageCounter:181174543 from Retrans Table on exchange 41959r
[16:27:06.194]  [00:00:52.164][info  ][IM] Received status response, status is 0x00
[16:27:06.195]  
[16:27:06.195]  [00:00:52.164][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:06.196]  
[16:27:06.196]  [00:00:52.165][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:06.197]  [00:00:52.165][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:06.198]  
[16:27:06.199]  [00:00:52.165][detail][DMG] <RE:Run> Cluster 102, Attribute 11 is dirty
[16:27:06.199]  
[16:27:06.199]  [00:00:52.166][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0011 (expanded=1)
[16:27:06.201]  
[16:27:06.201]  [00:00:52.166][detail][DMG] <RE:Run> Cluster 102, Attribute 17 is dirty
[16:27:06.201]  
[16:27:06.202]  [00:00:52.166][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_0017 (expanded=1)
[16:27:06.203]  
[16:27:06.204]  [00:00:52.166][detail][DMG] <RE:Run> Cluster 102, Attribute 1a is dirty
[16:27:06.204]  [00:00:52.166][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x1 AttributeId=0x0000_001A (expanded=1)
[16:27:06.206]  
[16:27:06.206]  [00:00:52.167][detail][DMG] <RE:Run> Cluster 102, Attribute fffc is dirty
[16:27:06.206]  [00:00:52.168][detail][DMG] <RE:Run> Cluster 102, Attribute fffd is dirty
[16:27:06.207]  
[16:27:06.208]  [00:00:52.169][detail][DMG] <RE:Run> Cluster 102, Attribute fff8 is dirty
[16:27:06.208]  
[16:27:06.208]  [00:00:52.169][detail][DMG] <RE:Run> Cluster 102, Attribute fff9 is dirty
[16:27:06.209]  
[16:27:06.209]  [00:00:52.171][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:06.211]  [00:00:52.172][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_0001 (expanded=1)
[16:27:06.211]  
[16:27:06.212]  [00:00:52.173][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:27:06.213]  
[16:27:06.213]  [00:00:52.175][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:27:06.214]  
[16:27:06.214]  [00:00:52.176][detail][DMG] <RE:Run> Cluster 1d, Attribute fff8 is dirty
[16:27:06.215]  [00:00:52.177][detail][DMG] <RE:Run> Cluster 1d, Attribute fff9 is dirty
[16:27:06.216]  
[16:27:06.216]  [00:00:52.179][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:27:06.217]  
[16:27:06.217]  [00:00:52.179][detail][DMG] <RE:Run> Cluster 3, Attribute 1 is dirty
[16:27:06.218]  
[16:27:06.218]  [00:00:52.181][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x2 AttributeId=0x0000_FFFC (expanded=1)
[16:27:06.220]  
[16:27:06.220]  [00:00:52.181][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x2 AttributeId=0x0000_FFFD (expanded=1)
[16:27:06.221]  
[16:27:06.222]  [00:00:52.183][detail][DMG] <RE:Run> Cluster 3, Attribute fffb is dirty
[16:27:06.222]  
[16:27:06.222]  [00:00:52.183][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:27:06.223]  [00:00:52.185][detail][DMG] <RE:Run> Cluster 4, Attribute fffd is dirty
[16:27:06.224]  [00:00:52.186][detail][DMG] <RE:Run> Cluster 4, Attribute fff8 is dirty
[16:27:06.224]  [00:00:52.188][detail][DMG] <RE:Run> Cluster 102, Attribute 0 is dirty
[16:27:06.225]  [00:00:52.188][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0000 (expanded=1)
[16:27:06.226]  [00:00:52.189][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0001 (expanded=1)
[16:27:06.228]  [00:00:52.191][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0005 (expanded=1)
[16:27:06.229]  [00:00:52.192][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0007 (expanded=1)
[16:27:06.231]  [00:00:52.193][detail][DMG] <RE:Run> Cluster 102, Attribute a is dirty
[16:27:06.231]  [00:00:52.195][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0102, attributeId: 0x0000_000B, err = b
[16:27:06.233]  [00:00:52.197][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:06.234]  [00:00:52.197][detail][DMG] Fetched 0 events
[16:27:06.235]  [00:00:52.197][detail][DMG] <RE> Sending report (payload has 1169 bytes)...
[16:27:06.236]  [00:00:52.200][info  ][EM] <<< [E:41959r S:25602 M:181174544 (Ack:245903563)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1203)
[16:27:06.238]  [00:00:52.201][info  ][EM] ??1 [E:41959r S:25602 M:181174544] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3359ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:06.240]  [00:00:52.201][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:06.240]  [00:00:52.201][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:06.332]  
[16:27:06.686]  [00:00:52.659][detail][IN] UDP Message Received packet nb : 72 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:06.688]  [00:00:52.661][info  ][EM] >>> [E:41959r S:25602 M:245903564 (Ack:181174544)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:06.690]  [00:00:52.661][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:06.691]  [00:00:52.662][detail][EM] Rxd Ack; Removing MessageCounter:181174544 from Retrans Table on exchange 41959r
[16:27:06.692]  [00:00:52.662][info  ][IM] Received status response, status is 0x00
[16:27:06.693]  
[16:27:06.693]  [00:00:52.662][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:06.694]  
[16:27:06.694]  [00:00:52.662][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:06.695]  [00:00:52.662][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:06.696]  
[16:27:06.697]  [00:00:52.663][detail][DMG] <RE:Run> Cluster 102, Attribute b is dirty
[16:27:06.697]  
[16:27:06.697]  [00:00:52.663][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000B (expanded=1)
[16:27:06.699]  
[16:27:06.699]  [00:00:52.664][detail][DMG] <RE:Run> Cluster 102, Attribute d is dirty
[16:27:06.699]  [00:00:52.664][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000D (expanded=1)
[16:27:06.701]  
[16:27:06.701]  [00:00:52.665][detail][DMG] <RE:Run> Cluster 102, Attribute e is dirty
[16:27:06.702]  
[16:27:06.702]  [00:00:52.665][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_000E (expanded=1)
[16:27:06.704]  
[16:27:06.704]  [00:00:52.665][detail][DMG] <RE:Run> Cluster 102, Attribute 10 is dirty
[16:27:06.704]  
[16:27:06.704]  [00:00:52.666][detail][DMG] <RE:Run> Cluster 102, Attribute 11 is dirty
[16:27:06.705]  
[16:27:06.706]  [00:00:52.666][detail][DMG] <RE:Run> Cluster 102, Attribute 17 is dirty
[16:27:06.706]  [00:00:52.667][detail][DMG] Reading attribute: Cluster=0x0000_0102 Endpoint=0x2 AttributeId=0x0000_0017 (expanded=1)
[16:27:06.708]  
[16:27:06.708]  [00:00:52.669][detail][DMG] <RE:Run> Cluster 102, Attribute fffd is dirty
[16:27:06.708]  
[16:27:06.708]  [00:00:52.670][detail][DMG] <RE:Run> Cluster 102, Attribute fff8 is dirty
[16:27:06.710]  
[16:27:06.710]  [00:00:52.672][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:06.711]  
[16:27:06.711]  [00:00:52.673][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:27:06.712]  
[16:27:06.712]  [00:00:52.673][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:27:06.713]  
[16:27:06.714]  [00:00:52.674][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[16:27:06.715]  
[16:27:06.715]  [00:00:52.676][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:27:06.717]  
[16:27:06.717]  [00:00:52.677][detail][DMG] <RE:Run> Cluster 1d, Attribute fff8 is dirty
[16:27:06.718]  
[16:27:06.718]  [00:00:52.678][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:27:06.718]  
[16:27:06.719]  [00:00:52.679][detail][DMG] <RE:Run> Cluster 3, Attribute 0 is dirty
[16:27:06.720]  
[16:27:06.720]  [00:00:52.680][detail][DMG] <RE:Run> Cluster 3, Attribute fffc is dirty
[16:27:06.720]  [00:00:52.682][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x3 AttributeId=0x0000_FFFD (expanded=1)
[16:27:06.722]  
[16:27:06.722]  [00:00:52.683][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:27:06.722]  [00:00:52.684][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:27:06.724]  [00:00:52.685][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:27:06.724]  [00:00:52.687][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:27:06.726]  [00:00:52.688][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[16:27:06.727]  [00:00:52.690][detail][DMG] <RE:Run> Cluster 6, Attribute 4001 is dirty
[16:27:06.727]  [00:00:52.690][detail][DMG] <RE:Run> Cluster 6, Attribute 4002 is dirty
[16:27:06.728]  [00:00:52.692][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:27:06.729]  [00:00:52.694][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:06.730]  [00:00:52.694][detail][DMG] Fetched 0 events
[16:27:06.731]  [00:00:52.696][info  ][EM] <<< [E:41959r S:25602 M:181174545 (Ack:245903564)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1202)
[16:27:06.734]  [00:00:52.698][info  ][EM] ??1 [E:41959r S:25602 M:181174545] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3332ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:06.735]  [00:00:52.698][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:06.736]  [00:00:52.699][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:07.185]  [00:00:53.158][detail][IN] UDP Message Received packet nb : 73 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:07.187]  [00:00:53.160][info  ][EM] >>> [E:41959r S:25602 M:245903565 (Ack:181174545)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:07.189]  [00:00:53.160][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:07.190]  [00:00:53.160][detail][EM] Rxd Ack; Removing MessageCounter:181174545 from Retrans Table on exchange 41959r
[16:27:07.191]  
[16:27:07.192]  [00:00:53.161][info  ][IM] Received status response, status is 0x00
[16:27:07.192]  
[16:27:07.192]  [00:00:53.161][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:07.193]  [00:00:53.161][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:07.194]  [00:00:53.161][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:07.195]  
[16:27:07.196]  [00:00:53.162][detail][DMG] <RE:Run> Cluster 6, Attribute 4002 is dirty
[16:27:07.197]  
[16:27:07.197]  [00:00:53.162][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_4002 (expanded=1)
[16:27:07.198]  
[16:27:07.198]  [00:00:53.162][detail][DMG] <RE:Run> Cluster 6, Attribute 4003 is dirty
[16:27:07.199]  
[16:27:07.199]  [00:00:53.163][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_4003 (expanded=1)
[16:27:07.200]  
[16:27:07.201]  [00:00:53.163][detail][DMG] <RE:Run> Cluster 6, Attribute fffc is dirty
[16:27:07.201]  
[16:27:07.201]  [00:00:53.164][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:27:07.203]  
[16:27:07.203]  [00:00:53.165][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_FFFD (expanded=1)
[16:27:07.204]  
[16:27:07.204]  [00:00:53.166][detail][DMG] <RE:Run> Cluster 6, Attribute fff9 is dirty
[16:27:07.205]  
[16:27:07.206]  [00:00:53.166][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:27:07.206]  
[16:27:07.206]  [00:00:53.166][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:27:07.207]  [00:00:53.168][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[16:27:07.208]  
[16:27:07.208]  [00:00:53.168][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[16:27:07.210]  
[16:27:07.210]  [00:00:53.170][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_000F (expanded=1)
[16:27:07.211]  
[16:27:07.212]  [00:00:53.171][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0010 (expanded=1)
[16:27:07.213]  
[16:27:07.213]  [00:00:53.172][detail][DMG] <RE:Run> Cluster 8, Attribute 12 is dirty
[16:27:07.214]  
[16:27:07.214]  [00:00:53.174][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0013 (expanded=1)
[16:27:07.215]  
[16:27:07.215]  [00:00:53.175][detail][DMG] <RE:Run> Cluster 8, Attribute 4000 is dirty
[16:27:07.216]  
[16:27:07.217]  [00:00:53.177][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_FFFC (expanded=1)
[16:27:07.218]  
[16:27:07.218]  [00:00:53.177][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_FFFD (expanded=1)
[16:27:07.219]  
[16:27:07.219]  [00:00:53.179][detail][DMG] <RE:Run> Cluster 8, Attribute fff9 is dirty
[16:27:07.220]  
[16:27:07.220]  [00:00:53.179][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:27:07.222]  
[16:27:07.222]  [00:00:53.181][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[16:27:07.223]  
[16:27:07.223]  [00:00:53.182][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[16:27:07.224]  
[16:27:07.224]  [00:00:53.184][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_000F (expanded=1)
[16:27:07.226]  [00:00:53.186][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_4001 (expanded=1)
[16:27:07.227]  
[16:27:07.227]  [00:00:53.187][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_400A (expanded=1)
[16:27:07.228]  [00:00:53.188][detail][DMG] <RE:Run> Cluster 300, Attribute fffd is dirty
[16:27:07.229]  [00:00:53.189][detail][DMG] <RE:Run> Cluster 300, Attribute fff8 is dirty
[16:27:07.230]  [00:00:53.191][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:07.231]  [00:00:53.192][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:27:07.231]  [00:00:53.193][detail][DMG] <RE:Run> We cannot put more chunks into this report. Enable chunking.
[16:27:07.233]  [00:00:53.195][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:07.234]  [00:00:53.198][info  ][EM] <<< [E:41959r S:25602 M:181174546 (Ack:245903565)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1198)
[16:27:07.236]  [00:00:53.199][info  ][EM] ??1 [E:41959r S:25602 M:181174546] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3380ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:07.238]  [00:00:53.199][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:07.789]  [00:00:53.761][detail][IN] UDP Message Received packet nb : 74 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:07.791]  [00:00:53.763][info  ][EM] >>> [E:41959r S:25602 M:245903566 (Ack:181174546)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:07.793]  [00:00:53.764][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:07.794]  [00:00:53.764][detail][EM] Rxd Ack; Removing MessageCounter:181174546 from Retrans Table on exchange 41959r
[16:27:07.795]  
[16:27:07.796]  [00:00:53.764][info  ][IM] Received status response, status is 0x00
[16:27:07.796]  
[16:27:07.796]  [00:00:53.764][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:07.797]  
[16:27:07.797]  [00:00:53.764][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:07.798]  
[16:27:07.798]  [00:00:53.765][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:07.800]  
[16:27:07.800]  [00:00:53.765][detail][DMG] <RE:Run> Cluster 1d, Attribute 1 is dirty
[16:27:07.800]  
[16:27:07.801]  [00:00:53.765][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0001 (expanded=1)
[16:27:07.802]  
[16:27:07.803]  [00:00:53.766][detail][DMG] <RE:Run> Cluster 1d, Attribute 2 is dirty
[16:27:07.803]  
[16:27:07.803]  [00:00:53.766][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0002 (expanded=1)
[16:27:07.805]  
[16:27:07.805]  [00:00:53.767][detail][DMG] <RE:Run> Cluster 1d, Attribute 3 is dirty
[16:27:07.805]  
[16:27:07.806]  [00:00:53.767][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_0003 (expanded=1)
[16:27:07.807]  
[16:27:07.807]  [00:00:53.768][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:27:07.809]  
[16:27:07.809]  [00:00:53.768][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:27:07.810]  
[16:27:07.810]  [00:00:53.770][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:27:07.811]  
[16:27:07.811]  [00:00:53.771][detail][DMG] <RE:Run> Cluster 3, Attribute 0 is dirty
[16:27:07.812]  
[16:27:07.812]  [00:00:53.773][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x4 AttributeId=0x0000_FFFC (expanded=1)
[16:27:07.814]  
[16:27:07.814]  [00:00:53.773][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:27:07.815]  
[16:27:07.815]  [00:00:53.775][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:27:07.816]  
[16:27:07.816]  [00:00:53.776][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:27:07.817]  
[16:27:07.818]  [00:00:53.777][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:27:07.818]  
[16:27:07.819]  [00:00:53.779][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:27:07.820]  
[16:27:07.820]  [00:00:53.780][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:27:07.821]  
[16:27:07.821]  [00:00:53.781][detail][DMG] <RE:Run> Cluster 6, Attribute 4001 is dirty
[16:27:07.822]  
[16:27:07.823]  [00:00:53.783][detail][DMG] <RE:Run> Cluster 6, Attribute 4003 is dirty
[16:27:07.823]  [00:00:53.784][detail][DMG] <RE:Run> Cluster 6, Attribute fffc is dirty
[16:27:07.824]  [00:00:53.785][detail][DMG] <RE:Run> Cluster 6, Attribute fffd is dirty
[16:27:07.825]  [00:00:53.787][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:27:07.825]  [00:00:53.788][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0000 (expanded=1)
[16:27:07.827]  [00:00:53.789][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0001 (expanded=1)
[16:27:07.828]  [00:00:53.791][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0003 (expanded=1)
[16:27:07.830]  [00:00:53.791][detail][DMG] <RE:Run> Cluster 8, Attribute 10 is dirty
[16:27:07.830]  [00:00:53.792][detail][DMG] <RE:Run> Cluster 8, Attribute 11 is dirty
[16:27:07.831]  [00:00:53.793][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0012 (expanded=1)
[16:27:07.832]  [00:00:53.796][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:07.833]  [00:00:53.796][detail][DMG] Fetched 0 events
[16:27:07.834]  [00:00:53.796][detail][DMG] <RE> Sending report (payload has 1160 bytes)...
[16:27:07.834]  [00:00:53.799][info  ][EM] <<< [E:41959r S:25602 M:181174547 (Ack:245903566)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1194)
[16:27:07.837]  [00:00:53.800][info  ][EM] ??1 [E:41959r S:25602 M:181174547] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3388ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:07.839]  [00:00:53.800][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:07.840]  [00:00:53.801][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:08.291]  [00:00:54.263][detail][IN] UDP Message Received packet nb : 75 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:08.292]  [00:00:54.265][info  ][EM] >>> [E:41959r S:25602 M:245903567 (Ack:181174547)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:08.294]  [00:00:54.265][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:08.296]  [00:00:54.265][detail][EM] Rxd Ack; Removing MessageCounter:181174547 from Retrans Table on exchange 41959r
[16:27:08.296]  [00:00:54.266][info  ][IM] Received status response, status is 0x00
[16:27:08.297]  
[16:27:08.298]  [00:00:54.266][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:08.298]  
[16:27:08.298]  [00:00:54.266][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:08.299]  [00:00:54.266][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:08.301]  
[16:27:08.301]  [00:00:54.267][detail][DMG] <RE:Run> Cluster 8, Attribute 12 is dirty
[16:27:08.302]  [00:00:54.267][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0012 (expanded=1)
[16:27:08.304]  
[16:27:08.304]  [00:00:54.267][detail][DMG] <RE:Run> Cluster 8, Attribute 13 is dirty
[16:27:08.304]  
[16:27:08.304]  [00:00:54.268][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0013 (expanded=1)
[16:27:08.306]  
[16:27:08.306]  [00:00:54.268][detail][DMG] <RE:Run> Cluster 8, Attribute 14 is dirty
[16:27:08.306]  
[16:27:08.307]  [00:00:54.269][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_0014 (expanded=1)
[16:27:08.308]  
[16:27:08.308]  [00:00:54.269][detail][DMG] <RE:Run> Cluster 8, Attribute 4000 is dirty
[16:27:08.309]  [00:00:54.270][detail][DMG] <RE:Run> Cluster 8, Attribute fffc is dirty
[16:27:08.310]  
[16:27:08.310]  [00:00:54.271][detail][DMG] <RE:Run> Cluster 8, Attribute fffd is dirty
[16:27:08.311]  
[16:27:08.311]  [00:00:54.272][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x4 AttributeId=0x0000_FFFD (expanded=1)
[16:27:08.313]  
[16:27:08.313]  [00:00:54.275][detail][DMG] <RE:Run> Cluster 1d, Attribute 0 is dirty
[16:27:08.313]  
[16:27:08.313]  [00:00:54.275][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:27:08.315]  
[16:27:08.315]  [00:00:54.276][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:27:08.316]  
[16:27:08.317]  [00:00:54.277][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0002 (expanded=1)
[16:27:08.317]  
[16:27:08.318]  [00:00:54.278][detail][DMG] Reading attribute: Cluster=0x0000_001D Endpoint=0x5 AttributeId=0x0000_0003 (expanded=1)
[16:27:08.319]  
[16:27:08.319]  [00:00:54.280][detail][DMG] <RE:Run> Cluster 1d, Attribute fffd is dirty
[16:27:08.320]  
[16:27:08.320]  [00:00:54.281][detail][DMG] <RE:Run> Cluster 1d, Attribute fffb is dirty
[16:27:08.321]  
[16:27:08.322]  [00:00:54.282][detail][DMG] <RE:Run> Cluster 3, Attribute 0 is dirty
[16:27:08.322]  
[16:27:08.322]  [00:00:54.283][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:27:08.324]  
[16:27:08.324]  [00:00:54.284][detail][DMG] Reading attribute: Cluster=0x0000_0003 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:27:08.325]  
[16:27:08.325]  [00:00:54.285][detail][DMG] <RE:Run> Cluster 3, Attribute fff9 is dirty
[16:27:08.326]  
[16:27:08.326]  [00:00:54.287][detail][DMG] <RE:Run> Cluster 4, Attribute 0 is dirty
[16:27:08.327]  
[16:27:08.327]  [00:00:54.288][detail][DMG] Reading attribute: Cluster=0x0000_0004 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:27:08.329]  [00:00:54.290][detail][DMG] <RE:Run> Cluster 4, Attribute fff9 is dirty
[16:27:08.329]  [00:00:54.291][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[16:27:08.330]  [00:00:54.292][detail][DMG] <RE:Run> Cluster 6, Attribute 4001 is dirty
[16:27:08.331]  [00:00:54.292][detail][DMG] <RE:Run> Cluster 6, Attribute 4002 is dirty
[16:27:08.332]  [00:00:54.294][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_4003 (expanded=1)
[16:27:08.333]  [00:00:54.295][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:27:08.334]  [00:00:54.296][detail][DMG] Next attribute value does not fit in packet, roll back on clusterId: 0x0000_0006, attributeId: 0x0000_FFFD, err = b
[16:27:08.335]  [00:00:54.298][detail][DMG] <RE:Run> first cluster event is too big so that it fails to fit in the packet!
[16:27:08.337]  [00:00:54.301][info  ][EM] <<< [E:41959r S:25602 M:181174548 (Ack:245903567)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1192)
[16:27:08.340]  [00:00:54.302][info  ][EM] ??1 [E:41959r S:25602 M:181174548] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3402ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:08.342]  [00:00:54.303][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:08.342]  [00:00:54.303][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has more messages
[16:27:08.345]  
[16:27:08.790]  [00:00:54.763][detail][IN] UDP Message Received packet nb : 76 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:08.792]  [00:00:54.765][info  ][EM] >>> [E:41959r S:25602 M:245903568 (Ack:181174548)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:08.794]  [00:00:54.765][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:08.795]  [00:00:54.765][detail][EM] Rxd Ack; Removing MessageCounter:181174548 from Retrans Table on exchange 41959r
[16:27:08.796]  [00:00:54.766][info  ][IM] Received status response, status is 0x00
[16:27:08.797]  [00:00:54.766][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:08.797]  [00:00:54.766][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:08.798]  [00:00:54.766][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000023
[16:27:08.800]  
[16:27:08.800]  [00:00:54.766][detail][DMG] <RE:Run> Cluster 6, Attribute fffd is dirty
[16:27:08.801]  
[16:27:08.801]  [00:00:54.767][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x5 AttributeId=0x0000_FFFD (expanded=1)
[16:27:08.802]  
[16:27:08.803]  [00:00:54.767][detail][DMG] <RE:Run> Cluster 6, Attribute fff8 is dirty
[16:27:08.804]  
[16:27:08.804]  [00:00:54.768][detail][DMG] <RE:Run> Cluster 6, Attribute fff9 is dirty
[16:27:08.804]  
[16:27:08.804]  [00:00:54.768][detail][DMG] <RE:Run> Cluster 6, Attribute fffb is dirty
[16:27:08.806]  
[16:27:08.806]  [00:00:54.769][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[16:27:08.806]  
[16:27:08.806]  [00:00:54.770][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0000 (expanded=1)
[16:27:08.808]  
[16:27:08.808]  [00:00:54.770][detail][DMG] <RE:Run> Cluster 8, Attribute 1 is dirty
[16:27:08.808]  
[16:27:08.809]  [00:00:54.771][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0001 (expanded=1)
[16:27:08.810]  [00:00:54.771][detail][DMG] <RE:Run> Cluster 8, Attribute 2 is dirty
[16:27:08.811]  [00:00:54.773][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_000F (expanded=1)
[16:27:08.812]  [00:00:54.774][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0010 (expanded=1)
[16:27:08.813]  [00:00:54.776][detail][DMG] <RE:Run> Cluster 8, Attribute 12 is dirty
[16:27:08.814]  [00:00:54.776][detail][DMG] <RE:Run> Cluster 8, Attribute 13 is dirty
[16:27:08.815]  [00:00:54.778][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_0014 (expanded=1)
[16:27:08.816]  [00:00:54.779][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_4000 (expanded=1)
[16:27:08.817]  [00:00:54.780][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x5 AttributeId=0x0000_FFFC (expanded=1)
[16:27:08.819]  [00:00:54.781][detail][DMG] <RE:Run> Cluster 8, Attribute fff8 is dirty
[16:27:08.820]  [00:00:54.783][detail][DMG] <RE:Run> Cluster 8, Attribute fffb is dirty
[16:27:08.820]  [00:00:54.789][detail][DMG] Fetched 5 events
[16:27:08.821]  [00:00:54.789][detail][DMG] <RE> Sending report (payload has 1012 bytes)...
[16:27:08.822]  [00:00:54.791][info  ][EM] <<< [E:41959r S:25602 M:181174549 (Ack:245903568)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:1046)
[16:27:08.824]  [00:00:54.791][info  ][EM] ??1 [E:41959r S:25602 M:181174549] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3345ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:08.826]  [00:00:54.792][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:08.827]  [00:00:54.792][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 1, RE has no more messages
[16:27:09.295]  [00:00:55.267][detail][IN] UDP Message Received packet nb : 77 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:09.296]  [00:00:55.269][info  ][EM] >>> [E:41959r S:25602 M:245903569 (Ack:181174549)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:09.298]  [00:00:55.270][detail][EM] Found matching exchange: 41959r, Delegate: 0x20005e60
[16:27:09.300]  [00:00:55.270][detail][EM] Rxd Ack; Removing MessageCounter:181174549 from Retrans Table on exchange 41959r
[16:27:09.300]  [00:00:55.270][info  ][IM] Received status response, status is 0x00
[16:27:09.301]  [00:00:55.273][info  ][EM] <<< [E:41959r S:25602 M:181174550 (Ack:245903569)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[16:27:09.304]  [00:00:55.273][info  ][EM] ??1 [E:41959r S:25602 M:181174550] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3387ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:09.306]  [00:00:55.274][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000D7EA and system Timestamp 0x000000000009FFAA.
[16:27:09.307]  [00:00:55.274][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:09.309]  [00:00:55.274][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:09.309]  [00:00:55.274][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000BA46 and max: 0x000000000009E206
[16:27:09.310]  [00:00:55.275][info  ][DMG] Handler: 0x20001258 with min: 0x000000000000D7EA and max: 0x000000000009FFAA
[16:27:09.311]  [00:00:55.275][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000023 DirtyGeneration = 0x0000000000000023
[16:27:09.313]  [00:00:55.286][detail][DMG] Fetched 0 events
[16:27:09.314]  [00:00:55.286][detail][DMG] <RE> Sending report (payload has 11 bytes)...
[16:27:09.315]  [00:00:55.288][info  ][EM] <<< [E:49928i S:25599 M:83709819] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:41)
[16:27:09.317]  [00:00:55.289][info  ][EM] ??1 [E:49928i S:25599 M:83709819] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3574ms from now [State:Idle II:500 AI:300 AT:4000]
[16:27:09.319]  [00:00:55.289][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:09.320]  [00:00:55.289][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:27:09.320]  [00:00:55.290][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000022 DirtyGeneration = 0x0000000000000023
[16:27:09.323]  [00:00:55.291][detail][DMG] <RE:Run> Cluster 1f, Attribute 0 is dirty
[16:27:09.323]  [00:00:55.291][detail][DMG] Reading attribute: Cluster=0x0000_001F Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:09.327]  [00:00:55.300][detail][DMG] Fetched 0 events
[16:27:09.327]  [00:00:55.300][detail][DMG] <RE> Sending report (payload has 100 bytes)...
[16:27:09.330]  [00:00:55.303][info  ][EM] <<< [E:49929i S:25602 M:181174551] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:130)
[16:27:09.332]  [00:00:55.303][info  ][EM] ??1 [E:49929i S:25602 M:181174551] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3334ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:09.334]  [00:00:55.304][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:09.335]  [00:00:55.304][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[16:27:09.335]  [00:00:55.304][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:09.362]  [00:00:55.333][detail][IN] UDP Message Received packet nb : 78 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:09.363]  [00:00:55.335][info  ][EM] >>> [E:41959r S:25602 M:245903570 (Ack:181174550)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:09.366]  [00:00:55.335][detail][EM] Found matching exchange: 41959r, Delegate: 0
[16:27:09.367]  [00:00:55.335][detail][EM] Rxd Ack; Removing MessageCounter:181174550 from Retrans Table on exchange 41959r
[16:27:09.390]  [00:00:55.362][detail][IN] UDP Message Received packet nb : 79 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:09.392]  [00:00:55.364][info  ][EM] >>> [E:49928i S:25599 M:47048241 (Ack:83709819)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:09.394]  [00:00:55.365][detail][EM] Found matching exchange: 49928i, Delegate: 0x20005dd0
[16:27:09.395]  [00:00:55.365][detail][EM] Rxd Ack; Removing MessageCounter:83709819 from Retrans Table on exchange 49928i
[16:27:09.396]  [00:00:55.365][info  ][IM] Received status response, status is 0x00
[16:27:09.396]  [00:00:55.365][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:09.397]  [00:00:55.365][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:09.398]  [00:00:55.367][info  ][EM] <<< [E:49928i S:25599 M:83709820 (Ack:47048241)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:09.401]  [00:00:55.368][detail][EM] Flushed pending ack for MessageCounter:47048241 on exchange 49928i
[16:27:09.886]  [00:00:55.858][detail][IN] UDP Message Received packet nb : 80 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:09.887]  [00:00:55.860][info  ][EM] >>> [E:49929i S:25602 M:245903571 (Ack:181174551)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:09.889]  [00:00:55.861][detail][EM] Found matching exchange: 49929i, Delegate: 0x20005e60
[16:27:09.890]  [00:00:55.861][detail][EM] Rxd Ack; Removing MessageCounter:181174551 from Retrans Table on exchange 49929i
[16:27:09.891]  [00:00:55.861][info  ][IM] Received status response, status is 0x00
[16:27:09.892]  [00:00:55.861][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:09.893]  [00:00:55.861][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:09.893]  [00:00:55.863][info  ][EM] <<< [E:49929i S:25602 M:181174552 (Ack:245903571)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:09.896]  [00:00:55.864][detail][EM] Flushed pending ack for MessageCounter:245903571 on exchange 49929i
[16:27:09.961]  [00:00:55.933][detail][IN] UDP Message Received packet nb : 81 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 89
[16:27:09.962]  [00:00:55.935][info  ][EM] >>> [E:41961r S:25602 M:245903572] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:06 (IM:WriteRequest) (B:89)
[16:27:09.964]  [00:00:55.936][detail][EM] Handling via exchange: 41961r, Delegate: 0x2000413c
[16:27:09.965]  [00:00:55.936][detail][IM] Received Write request
[16:27:09.966]  [00:00:55.936][detail][DMG] IM WH moving to [Initialized]
[16:27:09.966]  [00:00:55.937][detail][DMG] Writing attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0000
[16:27:09.968]  [00:00:55.938][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888c
[16:27:09.968]  [00:00:55.938][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000D7F9 and max: 0x000000000009FFB9
[16:27:09.970]  [00:00:55.939][info  ][DMG] Handler: 0x20001258 with min: 0x000000000000D808 and max: 0x000000000009FFC8
[16:27:09.971]  [00:00:55.939][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:09.972]  [00:00:55.940][detail][DMG] IM WH moving to [AddStatus]
[16:27:09.973]  [00:00:55.940][detail][DMG] Writing attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0000
[16:27:09.973]  [00:00:55.941][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888d
[16:27:09.975]  [00:00:55.942][detail][DMG] IM WH moving to [AddStatus]
[16:27:09.975]  [00:00:55.945][info  ][EM] <<< [E:41961r S:25602 M:181174553 (Ack:245903572)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:07 (IM:WriteResponse) (B:84)
[16:27:09.977]  [00:00:55.946][info  ][EM] ??1 [E:41961r S:25602 M:181174553] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3388ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:09.980]  [00:00:55.946][detail][DMG] IM WH moving to [Sending]
[16:27:09.980]  [00:00:55.947][detail][DMG] IM WH moving to [Uninitialized]
[16:27:09.981]  [00:00:55.947][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000023 DirtyGeneration = 0x0000000000000025
[16:27:09.982]  [00:00:55.949][detail][DMG] <RE:Run> Cluster 2a, Attribute 0 is dirty
[16:27:09.983]  [00:00:55.950][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:09.986]  [00:00:55.958][detail][DMG] Fetched 0 events
[16:27:09.986]  [00:00:55.959][detail][DMG] <RE> Sending report (payload has 54 bytes)...
[16:27:09.991]  [00:00:55.963][info  ][EM] <<< [E:49930i S:25599 M:83709821] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:84)
[16:27:09.993]  [00:00:55.964][info  ][EM] ??1 [E:49930i S:25599 M:83709821] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3349ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:09.995]  [00:00:55.964][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:09.996]  [00:00:55.964][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:27:09.996]  [00:00:55.964][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000023 DirtyGeneration = 0x0000000000000025
[16:27:09.998]  [00:00:55.967][detail][DMG] <RE:Run> Cluster 2a, Attribute 0 is dirty
[16:27:09.999]  [00:00:55.967][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0000 (expanded=1)
[16:27:10.003]  [00:00:55.976][detail][DMG] Fetched 0 events
[16:27:10.003]  [00:00:55.976][detail][DMG] <RE> Sending report (payload has 54 bytes)...
[16:27:10.006]  [00:00:55.978][info  ][EM] <<< [E:49931i S:25602 M:181174554] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:84)
[16:27:10.008]  [00:00:55.979][info  ][EM] ??1 [E:49931i S:25602 M:181174554] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3343ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:10.010]  [00:00:55.979][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:10.011]  [00:00:55.980][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[16:27:10.011]  [00:00:55.980][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:10.015]  [00:00:55.988][detail][IN] UDP Message Received packet nb : 82 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 71
[16:27:10.017]  [00:00:55.990][info  ][EM] >>> [E:41962r S:25602 M:245903573] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:08 (IM:InvokeCommandRequest) (B:71)
[16:27:10.019]  [00:00:55.991][detail][EM] Handling via exchange: 41962r, Delegate: 0x2000413c
[16:27:10.020]  [00:00:55.992][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0009
[16:27:10.021]  [00:00:55.992][info  ][ZCL] OpCreds: Received an UpdateFabricLabel command
[16:27:10.022]  [00:00:55.993][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:27:10.022]  [00:00:55.993][detail][DMG] Command handler moving to [NewRespons]
[16:27:10.023]  [00:00:55.993][detail][DMG] Command handler moving to [ Preparing]
[16:27:10.024]  [00:00:55.993][detail][DMG] Command handler moving to [AddingComm]
[16:27:10.025]  [00:00:55.993][detail][DMG] Command handler moving to [AddedComma]
[16:27:10.026]  [00:00:55.994][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:10.027]  [00:00:55.995][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:27:10.027]  [00:00:55.995][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:27:10.029]  [00:00:55.995][detail][DMG] Command handler moving to [AwaitingDe]
[16:27:10.029]  [00:00:55.998][info  ][EM] <<< [E:41962r S:25602 M:181174555 (Ack:245903573)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:27:10.032]  [00:00:55.999][info  ][EM] ??1 [E:41962r S:25602 M:181174555] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3371ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:10.033]  [00:00:55.999][detail][DMG] Command response sender moving to [AllInvokeR]
[16:27:10.161]  [00:00:56.133][detail][IN] UDP Message Received packet nb : 83 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:10.162]  [00:00:56.134][info  ][EM] >>> [E:41961r S:25602 M:245903574 (Ack:181174553)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:10.165]  [00:00:56.135][detail][EM] Found matching exchange: 41961r, Delegate: 0
[16:27:10.166]  [00:00:56.135][detail][EM] Rxd Ack; Removing MessageCounter:181174553 from Retrans Table on exchange 41961r
[16:27:10.333]  
[16:27:11.114]  [00:00:57.086][detail][IN] UDP Message Received packet nb : 84 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:11.115]  [00:00:57.087][info  ][EM] >>> [E:41962r S:25602 M:245903576 (Ack:181174555)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:11.118]  [00:00:57.088][detail][EM] Found matching exchange: 41962r, Delegate: 0
[16:27:11.119]  [00:00:57.088][detail][EM] Rxd Ack; Removing MessageCounter:181174555 from Retrans Table on exchange 41962r
[16:27:11.132]  [00:00:57.105][detail][IN] UDP Message Received packet nb : 85 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:11.134]  [00:00:57.107][info  ][EM] >>> [E:49930i S:25599 M:47048242 (Ack:83709821)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:11.136]  [00:00:57.107][detail][EM] Found matching exchange: 49930i, Delegate: 0x20005dd0
[16:27:11.137]  [00:00:57.108][detail][EM] Rxd Ack; Removing MessageCounter:83709821 from Retrans Table on exchange 49930i
[16:27:11.138]  [00:00:57.108][info  ][IM] Received status response, status is 0x00
[16:27:11.139]  [00:00:57.108][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:11.139]  [00:00:57.108][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:11.140]  [00:00:57.108][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000DA9C and max: 0x00000000000A025C
[16:27:11.141]  [00:00:57.111][info  ][EM] <<< [E:49930i S:25599 M:83709822 (Ack:47048242)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:11.144]  [00:00:57.112][detail][EM] Flushed pending ack for MessageCounter:47048242 on exchange 49930i
[16:27:11.145]  [00:00:57.112][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000025 DirtyGeneration = 0x0000000000000026
[16:27:11.147]  [00:00:57.113][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:27:11.148]  [00:00:57.114][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:11.151]  [00:00:57.124][detail][DMG] Fetched 0 events
[16:27:11.151]  [00:00:57.125][detail][DMG] <RE> Sending report (payload has 233 bytes)...
[16:27:11.154]  [00:00:57.126][info  ][EM] <<< [E:49932i S:25599 M:83709823] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:263)
[16:27:11.156]  [00:00:57.127][info  ][EM] ??1 [E:49932i S:25599 M:83709823] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3367ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:11.158]  [00:00:57.127][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:11.159]  [00:00:57.127][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 0, RE has no more messages
[16:27:11.651]  [00:00:57.624][detail][IN] UDP Message Received packet nb : 86 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:11.653]  [00:00:57.625][info  ][EM] >>> [E:49932i S:25599 M:47048243 (Ack:83709823)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:11.654]  [00:00:57.626][detail][EM] Found matching exchange: 49932i, Delegate: 0x20005dd0
[16:27:11.656]  [00:00:57.626][detail][EM] Rxd Ack; Removing MessageCounter:83709823 from Retrans Table on exchange 49932i
[16:27:11.656]  [00:00:57.626][info  ][IM] Received status response, status is 0x00
[16:27:11.657]  [00:00:57.626][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:11.658]  [00:00:57.626][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:11.658]  [00:00:57.628][info  ][EM] <<< [E:49932i S:25599 M:83709824 (Ack:47048243)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:11.661]  [00:00:57.629][detail][EM] Flushed pending ack for MessageCounter:47048243 on exchange 49932i
[16:27:12.333]  
[16:27:13.349]  [00:00:59.322][info  ][EM] <<1 [E:49931i S:25602 M:181174554] (S) Msg Retransmission to 1:00000000A5E93870
[16:27:13.349]  [00:00:59.322][info  ][EM] ??2 [E:49931i S:25602 M:181174554] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3398ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:13.387]  [00:00:59.360][detail][IN] UDP Message Received packet nb : 87 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:13.389]  [00:00:59.362][info  ][EM] >>> [E:49931i S:25602 M:245903575 (Ack:181174554)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:13.391]  [00:00:59.363][detail][EM] Found matching exchange: 49931i, Delegate: 0x20005e60
[16:27:13.392]  [00:00:59.363][detail][EM] Rxd Ack; Removing MessageCounter:181174554 from Retrans Table on exchange 49931i
[16:27:13.393]  [00:00:59.363][info  ][IM] Received status response, status is 0x00
[16:27:13.394]  [00:00:59.363][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:13.395]  [00:00:59.364][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:13.395]  [00:00:59.364][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000DF27 and max: 0x00000000000A06E7
[16:27:13.397]  [00:00:59.364][info  ][DMG] Handler: 0x20001258 with min: 0x000000000000DAAC and max: 0x00000000000A026C
[16:27:13.398]  [00:00:59.366][info  ][EM] <<< [E:49931i S:25602 M:181174556 (Ack:245903575)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:13.401]  [00:00:59.367][detail][EM] Flushed pending ack for MessageCounter:245903575 on exchange 49931i
[16:27:13.401]  [00:00:59.367][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000026 DirtyGeneration = 0x0000000000000026
[16:27:13.404]  [00:00:59.377][detail][DMG] Fetched 0 events
[16:27:13.404]  [00:00:59.377][detail][DMG] <RE> Sending report (payload has 11 bytes)...
[16:27:13.407]  [00:00:59.379][info  ][EM] <<< [E:49933i S:25599 M:83709825] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:41)
[16:27:13.409]  [00:00:59.380][info  ][EM] ??1 [E:49933i S:25599 M:83709825] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:13.411]  [00:00:59.380][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:13.411]  [00:00:59.380][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:27:13.412]  [00:00:59.381][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000025 DirtyGeneration = 0x0000000000000026
[16:27:13.414]  [00:00:59.382][detail][DMG] <RE:Run> Cluster 3e, Attribute 1 is dirty
[16:27:13.415]  [00:00:59.382][detail][DMG] Reading attribute: Cluster=0x0000_003E Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[16:27:13.420]  [00:00:59.393][detail][DMG] Fetched 0 events
[16:27:13.420]  [00:00:59.393][detail][DMG] <RE> Sending report (payload has 233 bytes)...
[16:27:13.422]  [00:00:59.395][info  ][EM] <<< [E:49934i S:25602 M:181174557] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:263)
[16:27:13.425]  [00:00:59.396][info  ][EM] ??1 [E:49934i S:25602 M:181174557] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3386ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:13.427]  [00:00:59.397][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:13.427]  [00:00:59.397][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[16:27:13.428]  [00:00:59.397][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:13.445]  [00:00:59.417][detail][IN] UDP Message Received packet nb : 88 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 34
[16:27:13.447]  [00:00:59.419][info  ][EM] >>> [E:49931i S:25602 M:245903577 (Ack:181174554)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:13.476]  [00:00:59.448][detail][IN] UDP Message Received packet nb : 89 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:13.478]  [00:00:59.450][info  ][EM] >>> [E:49933i S:25599 M:47048244 (Ack:83709825)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:13.479]  [00:00:59.450][detail][EM] Found matching exchange: 49933i, Delegate: 0x20005dd0
[16:27:13.480]  [00:00:59.451][detail][EM] Rxd Ack; Removing MessageCounter:83709825 from Retrans Table on exchange 49933i
[16:27:13.481]  [00:00:59.451][info  ][IM] Received status response, status is 0x00
[16:27:13.482]  [00:00:59.451][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:13.482]  [00:00:59.451][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:13.483]  [00:00:59.453][info  ][EM] <<< [E:49933i S:25599 M:83709826 (Ack:47048244)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:13.486]  [00:00:59.453][detail][EM] Flushed pending ack for MessageCounter:47048244 on exchange 49933i
[16:27:13.512]  [00:00:59.484][detail][IN] UDP Message Received packet nb : 90 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:13.513]  [00:00:59.486][info  ][EM] >>> [E:49934i S:25602 M:245903578 (Ack:181174557)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:13.515]  [00:00:59.487][detail][EM] Found matching exchange: 49934i, Delegate: 0x20005e60
[16:27:13.517]  [00:00:59.487][detail][EM] Rxd Ack; Removing MessageCounter:181174557 from Retrans Table on exchange 49934i
[16:27:13.518]  [00:00:59.487][info  ][IM] Received status response, status is 0x00
[16:27:13.518]  [00:00:59.487][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:13.519]  [00:00:59.487][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:13.520]  [00:00:59.489][info  ][EM] <<< [E:49934i S:25602 M:181174558 (Ack:245903578)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:13.522]  [00:00:59.490][detail][EM] Flushed pending ack for MessageCounter:245903578 on exchange 49934i
[16:27:14.333]  
[16:27:16.333]  
[16:27:18.333]  
[16:27:20.333]  
[16:27:22.333]  
[16:27:24.333]  
[16:27:24.945]  [00:01:10.917][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888e
[16:27:24.945]  [00:01:10.917][info  ][DMG] Handler: 0x20001230 with min: 0x000000000000E7F4 and max: 0x00000000000A0FB4
[16:27:24.946]  [00:01:10.917][info  ][DMG] Handler: 0x20001258 with min: 0x000000000000E805 and max: 0x00000000000A0FC5
[16:27:24.947]  [00:01:10.918][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:24.949]  [00:01:10.918][detail][EVL] LogEvent event number: 0x0000000000000009 priority: 1, endpoint id:  0x0 cluster id: 0x0000_002A event id: 0x0 Epoch timestamp: 0x000000DC6AD0C0C1
[16:27:24.950]  [00:01:10.919][detail][DMG] Urgent event will be sent once reporting is not blocked by the min interval
[16:27:24.951]  [00:01:10.919][info  ][SWU] Stopping the Periodic Query timer
[16:27:24.952]  
[16:27:24.952]  [00:01:10.919][info  ][SWU] Starting the watchdog timer, timeout: 21600 seconds
[16:27:24.953]  [00:01:10.919][detail][SWU] Establishing session to provider node ID 0x00000000A5E93870 on fabric index 1
[16:27:24.954]  [00:01:10.920][detail][CSM] FindOrEstablishSession: PeerId = [1:00000000A5E93870]
[16:27:24.955]  [00:01:10.920][detail][CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[16:27:24.956]  [00:01:10.920][info  ][DIS] Found an existing secure session to [1:00000000A5E93870]!
[16:27:24.957]  [00:01:10.920][detail][DIS] OperationalSessionSetup[1:00000000A5E93870]: State change 1 --> 5
[16:27:24.958]  [00:01:10.921][detail][DMG] ICR moving to [AddingComm]
[16:27:24.959]  [00:01:10.921][detail][DMG] ICR moving to [AddedComma]
[16:27:24.960]  [00:01:10.923][info  ][EM] <<< [E:49935i S:25602 M:181174559] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[16:27:24.962]  [00:01:10.924][info  ][EM] ??1 [E:49935i S:25602 M:181174559] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3682ms from now [State:Idle II:500 AI:300 AT:4000]
[16:27:24.964]  [00:01:10.925][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000026 DirtyGeneration = 0x0000000000000027
[16:27:24.965]  [00:01:10.927][detail][DMG] <RE:Run> Cluster 2a, Attribute 2 is dirty
[16:27:24.966]  [00:01:10.928][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:24.967]  [00:01:10.937][detail][DMG] Fetched 1 events
[16:27:24.968]  [00:01:10.938][detail][DMG] <RE> Sending report (payload has 90 bytes)...
[16:27:24.969]  [00:01:10.940][info  ][EM] <<< [E:49936i S:25599 M:83709827] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:120)
[16:27:24.971]  [00:01:10.941][info  ][EM] ??1 [E:49936i S:25599 M:83709827] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3663ms from now [State:Idle II:500 AI:300 AT:4000]
[16:27:24.973]  [00:01:10.941][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:24.974]  [00:01:10.941][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[16:27:24.975]  [00:01:10.942][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000026 DirtyGeneration = 0x0000000000000027
[16:27:24.976]  [00:01:10.944][detail][DMG] <RE:Run> Cluster 2a, Attribute 2 is dirty
[16:27:24.977]  [00:01:10.945][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:24.980]  [00:01:10.954][detail][DMG] Fetched 1 events
[16:27:24.980]  [00:01:10.954][detail][DMG] <RE> Sending report (payload has 90 bytes)...
[16:27:24.983]  [00:01:10.956][info  ][EM] <<< [E:49937i S:25602 M:181174560] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:120)
[16:27:24.985]  [00:01:10.957][info  ][EM] ??1 [E:49937i S:25602 M:181174560] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3653ms from now [State:Idle II:500 AI:300 AT:4000]
[16:27:24.987]  [00:01:10.957][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:24.988]  [00:01:10.957][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[16:27:24.988]  [00:01:10.958][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:25.038]  [00:01:11.010][detail][IN] UDP Message Received packet nb : 91 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 67
[16:27:25.039]  [00:01:11.012][info  ][EM] >>> [E:49935i S:25602 M:245903579 (Ack:181174559)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[16:27:25.042]  [00:01:11.013][detail][EM] Found matching exchange: 49935i, Delegate: 0x2002734c
[16:27:25.043]  [00:01:11.013][detail][EM] Rxd Ack; Removing MessageCounter:181174559 from Retrans Table on exchange 49935i
[16:27:25.044]  [00:01:11.013][detail][DMG] ICR moving to [ResponseRe]
[16:27:25.044]  [00:01:11.014][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[16:27:25.046]  [00:01:11.014][detail][SWU] QueryImageResponse:
[16:27:25.046]  [00:01:11.014][detail][SWU]   status: 2
[16:27:25.046]  [00:01:11.015][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 8505888f
[16:27:25.048]  [00:01:11.016][detail][DMG] Cannot merge the new path into any existing path, create one.
[16:27:25.049]  [00:01:11.016][detail][EVL] Copy Event to next buffer with priority 1
[16:27:25.049]  [00:01:11.017][detail][EVL] LogEvent event number: 0x000000000000000A priority: 1, endpoint id:  0x0 cluster id: 0x0000_002A event id: 0x0 Epoch timestamp: 0x000000DC6AD0C123
[16:27:25.051]  [00:01:11.017][detail][DMG] Urgent event will be sent once reporting is not blocked by the min interval
[16:27:25.053]  [00:01:11.017][info  ][SWU] Stopping the watchdog timer
[16:27:25.053]  [00:01:11.017][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:27:25.054]  [00:01:11.018][detail][DMG] ICR moving to [AwaitingDe]
[16:27:25.055]  [00:01:11.020][info  ][EM] <<< [E:49935i S:25602 M:181174561 (Ack:245903579)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:25.058]  [00:01:11.021][detail][EM] Flushed pending ack for MessageCounter:245903579 on exchange 49935i
[16:27:25.540]  [00:01:11.512][detail][IN] UDP Message Received packet nb : 92 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:25.541]  [00:01:11.514][info  ][EM] >>> [E:49937i S:25602 M:245903580 (Ack:181174560)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:25.543]  [00:01:11.514][detail][EM] Found matching exchange: 49937i, Delegate: 0x20005e60
[16:27:25.545]  [00:01:11.514][detail][EM] Rxd Ack; Removing MessageCounter:181174560 from Retrans Table on exchange 49937i
[16:27:25.545]  [00:01:11.515][info  ][IM] Received status response, status is 0x00
[16:27:25.546]  [00:01:11.515][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:25.547]  [00:01:11.515][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:25.547]  [00:01:11.515][info  ][DMG] Handler: 0x20001258 with min: 0x000000000001152D and max: 0x00000000000A3CED
[16:27:25.549]  [00:01:11.517][info  ][EM] <<< [E:49937i S:25602 M:181174562 (Ack:245903580)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:25.551]  [00:01:11.518][detail][EM] Flushed pending ack for MessageCounter:245903580 on exchange 49937i
[16:27:25.552]  [00:01:11.518][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000027 DirtyGeneration = 0x0000000000000028
[16:27:25.554]  [00:01:11.521][detail][DMG] <RE:Run> Cluster 2a, Attribute 2 is dirty
[16:27:25.555]  [00:01:11.522][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:25.558]  [00:01:11.531][detail][DMG] Fetched 1 events
[16:27:25.558]  [00:01:11.531][detail][DMG] <RE> Sending report (payload has 90 bytes)...
[16:27:25.561]  [00:01:11.533][info  ][EM] <<< [E:49938i S:25602 M:181174563] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:120)
[16:27:25.563]  [00:01:11.534][info  ][EM] ??1 [E:49938i S:25602 M:181174563] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3370ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:25.565]  [00:01:11.534][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:25.565]  [00:01:11.535][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[16:27:25.569]  [00:01:11.541][detail][IN] UDP Message Received packet nb : 93 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:25.571]  [00:01:11.543][info  ][EM] >>> [E:49936i S:25599 M:47048245 (Ack:83709827)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:25.572]  [00:01:11.543][detail][EM] Found matching exchange: 49936i, Delegate: 0x20005dd0
[16:27:25.574]  [00:01:11.543][detail][EM] Rxd Ack; Removing MessageCounter:83709827 from Retrans Table on exchange 49936i
[16:27:25.574]  [00:01:11.544][info  ][IM] Received status response, status is 0x00
[16:27:25.575]  [00:01:11.544][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:25.576]  [00:01:11.544][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:25.576]  [00:01:11.544][info  ][DMG] Handler: 0x20001230 with min: 0x000000000001151D and max: 0x00000000000A3CDD
[16:27:25.578]  [00:01:11.546][info  ][EM] <<< [E:49936i S:25599 M:83709828 (Ack:47048245)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:25.580]  [00:01:11.547][detail][EM] Flushed pending ack for MessageCounter:47048245 on exchange 49936i
[16:27:25.581]  [00:01:11.547][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000027 DirtyGeneration = 0x0000000000000028
[16:27:25.583]  [00:01:11.550][detail][DMG] <RE:Run> Cluster 2a, Attribute 2 is dirty
[16:27:25.584]  [00:01:11.550][detail][DMG] Reading attribute: Cluster=0x0000_002A Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[16:27:25.587]  [00:01:11.559][detail][DMG] Fetched 1 events
[16:27:25.587]  [00:01:11.560][detail][DMG] <RE> Sending report (payload has 90 bytes)...
[16:27:25.589]  [00:01:11.562][info  ][EM] <<< [E:49939i S:25599 M:83709829] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0001:05 (IM:ReportData) (B:120)
[16:27:25.592]  [00:01:11.563][info  ][EM] ??1 [E:49939i S:25599 M:83709829] (S) Msg Retransmission to 1:0000000036E47752 scheduled for 3349ms from now [State:Active II:500 AI:300 AT:4000]
[16:27:25.594]  [00:01:11.563][detail][DMG] IM RH moving to [AwaitingReportResponse]
[16:27:25.594]  [00:01:11.563][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 0, RE has no more messages
[16:27:25.595]  [00:01:11.563][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:27:25.648]  [00:01:11.621][detail][IN] UDP Message Received packet nb : 94 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:25.649]  [00:01:11.623][info  ][EM] >>> [E:49938i S:25602 M:245903581 (Ack:181174563)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:25.651]  [00:01:11.623][detail][EM] Found matching exchange: 49938i, Delegate: 0x20005e60
[16:27:25.652]  [00:01:11.623][detail][EM] Rxd Ack; Removing MessageCounter:181174563 from Retrans Table on exchange 49938i
[16:27:25.653]  [00:01:11.624][info  ][IM] Received status response, status is 0x00
[16:27:25.654]  [00:01:11.624][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[16:27:25.655]  [00:01:11.624][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:25.655]  [00:01:11.625][info  ][EM] <<< [E:49938i S:25602 M:181174564 (Ack:245903581)] (S) Msg TX from 00000000FCB0C0DF to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:25.658]  [00:01:11.625][detail][EM] Flushed pending ack for MessageCounter:245903581 on exchange 49938i
[16:27:26.137]  [00:01:12.109][detail][IN] UDP Message Received packet nb : 95 SrcAddr : fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5[53237] DestAddr : fdf7:dc9d:f190:0:2767:f8ea:e5cb:5117[5540] Payload Length 42
[16:27:26.139]  [00:01:12.111][info  ][EM] >>> [E:49939i S:25599 M:47048246 (Ack:83709829)] (S) Msg RX from 1:0000000036E47752 [AAAB] to 00000000FCB0C0DF --- Type 0001:01 (IM:StatusResponse) (B:42)
[16:27:26.140]  [00:01:12.111][detail][EM] Found matching exchange: 49939i, Delegate: 0x20005dd0
[16:27:26.142]  [00:01:12.112][detail][EM] Rxd Ack; Removing MessageCounter:83709829 from Retrans Table on exchange 49939i
[16:27:26.142]  [00:01:12.112][info  ][IM] Received status response, status is 0x00
[16:27:26.143]  [00:01:12.112][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:27:26.144]  [00:01:12.112][detail][DMG] IM RH moving to [CanStartReporting]
[16:27:26.145]  [00:01:12.114][info  ][EM] <<< [E:49939i S:25599 M:83709830 (Ack:47048246)] (S) Msg TX from 00000000FCB0C0DF to 1:0000000036E47752 [AAAB] [UDP:[fd53:6f42:3a33:4efe:108d:25bb:c834:7ab5]:53237] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:27:26.147]  [00:01:12.115][detail][EM] Flushed pending ack for MessageCounter:47048246 on exchange 49939i 
```