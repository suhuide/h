```c
[16:30:33.500]  device factoryreset
[16:30:33.504]  Performing factory reset ... 
[16:30:33.504]  Done
[16:30:33.504]  [00:02:13.129][info  ][DL] Performing factory reset
[16:30:34.007]  [00:02:13.633][detail][DL] SRP update succeeded
[16:30:34.007]  [00:02:13.633][info  ][DL] Clearing Thread provision
[16:30:34.008]  [00:02:13.633][info  ][DL] Erasing Thread persistent info...
[16:30:34.038]  [00:02:13.663][info  ][DL] System restarting

[16:30:34.766]  [00:00:00.065][info  ][DL] Starting scheduler
[16:30:34.766]  [00:00:00.065][info  ][DL] ==================================================
[16:30:34.767]  [00:00:00.065][info  ][DL]  starting
[16:30:34.767]  [00:00:00.066][info  ][DL] ==================================================
[16:30:34.768]  [00:00:00.066][info  ][DL] Init CHIP Stack
[16:30:34.768]  [00:00:00.068][info  ][DL] Provision mode disabled
[16:30:34.769]  [00:00:00.068][info  ][DL] Initializing OpenThread stack
[16:30:34.770]  [00:00:00.068][info  ][DL] OpenThread started: OK
[16:30:34.771]  [00:00:00.068][info  ][DL] Setting OpenThread device type to SLEEPY END DEVICE
[16:30:34.777]  [00:00:00.130][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[16:30:34.777]  [00:00:00.130][info  ][DL] RAIL version:, v3.0.0-b0
[16:30:34.778]  [00:00:00.131][silabs ]BLE: product type [Pergolux]
[16:30:34.779]  [00:00:00.131][silabs ]BLE: identify addr: D2:60:9E:6A:74:E1 type=1
[16:30:34.779]  [00:00:00.132][silabs ]BLE: MTU size 249
[16:30:34.780]  [00:00:00.133][detail][DL] CHIP event task running
[16:30:34.781]  [00:00:00.133][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:30:34.781]  [00:00:00.134][detail][DL] OpenThread State Changed (Flags: 0x00038210)
[16:30:34.782]  [00:00:00.134][detail][DL]    Network Name: OpenThread
[16:30:34.783]  [00:00:00.134][detail][DL]    PAN Id: 0xFFFF
[16:30:34.784]  [00:00:00.134][detail][DL]    Extended PAN Id: 0xDEAD00BEEF00CAFE
[16:30:34.784]  [00:00:00.134][detail][DL]    Channel: 11
[16:30:34.785]  [00:00:00.135][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64
[16:30:34.786]  [00:00:00.135][info  ][SVR] Current Software Version String: 0.9.7
[16:30:34.787]  [00:00:00.135][info  ][SVR] Current Software Version: 97
[16:30:34.788]  [00:00:00.136][info  ][DL] Device Configuration:
[16:30:34.788]  [00:00:00.136][info  ][DL]   Serial Number: 38398FFFFE520BF5
[16:30:34.788]  [00:00:00.136][info  ][DL]   Vendor Id: 65521 (0xFFF1)
[16:30:34.789]  [00:00:00.137][info  ][DL]   Product Id: 32784 (0x8010)
[16:30:34.790]  [00:00:00.137][info  ][DL]   Product Name: SL_Sample
[16:30:34.790]  [00:00:00.137][info  ][DL]   Hardware Version: 1
[16:30:34.791]  [00:00:00.138][info  ][DL]   Manufacturing Date: (not set)
[16:30:34.792]  [00:00:00.139][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[16:30:34.792]  [00:00:00.139][silabs ]Ver: 97 Btl: 0x03000001 Time:Feb  7 2026 16:21:38
[16:30:34.799]  [00:00:00.152][info  ][DL] Configuring BLE Channel
[16:30:34.799]  [00:00:00.153][detail][DL] BLE Static Device Address C6:8F:60:81:59:44
[16:30:34.800]  [00:00:00.153][silabs ]BLE: _create_second_adv, adv Handle = 0
[16:30:34.800]  [00:00:00.154][silabs ]BLE: advertiser start
[16:30:34.802]  [00:00:00.156][silabs ]COM: Init done
[16:30:34.802]  [00:00:00.156][silabs ]NWK: open basic commissioning window time 300 sec
[16:30:34.804]  [00:00:00.158][detail][IN] SecureSession[0x20007030]: Allocated Type:1 LSID:8047
[16:30:34.804]  [00:00:00.158][detail][SC] Assigned local session key ID 8047
[16:30:34.805]  [00:00:00.158][detail][SC] Waiting for PBKDF param request
[16:30:34.806]  [00:00:00.158][info  ][DIS] Updating services using commissioning mode 1
[16:30:34.807]  [00:00:00.158][error ][DIS] Failed to remove advertised services: 3
[16:30:34.807]  [00:00:00.159][detail][DL] Using Thread extended MAC for hostname.
[16:30:34.808]  [00:00:00.159][detail][DIS] DNS-SD Pairing Instruction not set
[16:30:34.809]  [00:00:00.159][info  ][DIS] Advertise commission parameter vendorID=65521 productID=32784 discriminator=3840/15 cm=1 cp=0 jf=0
[16:30:34.810]  [00:00:00.159][error ][DIS] Failed to advertise commissionable node: 3
[16:30:34.811]  [00:00:00.160][error ][DIS] Failed to finalize service update: 3
[16:30:34.811]  [00:00:00.160][detail][DL] Start BLE advertisement
[16:30:34.812]  [00:00:00.161][detail][DL] BLE Static Device Address EF:47:1A:8D:E4:BC
[16:30:34.813]  [00:00:00.161][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[16:30:34.814]  [00:00:00.162][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:30:34.816]  [00:00:00.163][silabs ]NWK: platform event type 800d
[16:30:34.816]  [00:00:00.163][silabs ]COM: notify network [Leave]
[16:30:34.816]  [00:00:00.163][silabs ]App Task started
[16:30:41.047]  [00:00:06.400][info  ][DL] Connect Event for CHIPoBLE on handle : 2
[16:30:41.047]  [00:00:06.401][info  ][DL] Connection Parameters Event for handle : 2
[16:30:41.048]  [00:00:06.401][info  ][DL] Connection parameter ID received - i:39, l:0, t:42, sm:0
[16:30:41.049]  [00:00:06.401][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:100
[16:30:41.050]  [00:00:06.401][info  ][DL] Connection phy status ID received - phy:1
[16:30:41.479]  [00:00:06.833][info  ][DL] Connection Parameters Event for handle : 2
[16:30:41.480]  [00:00:06.833][info  ][DL] Connection parameter ID received - i:78, l:0, t:100, sm:0
[16:30:45.120]  [00:00:10.474][info  ][DL] Handling CCCD Write
[16:30:45.120]  [00:00:10.474][error ][-] mConnectionState.allocated:430 false: 3
[16:30:45.121]  [00:00:10.474][error ][-] Error CHIP:0x00000003 at C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:303
[16:30:46.095]  [00:00:11.450][info  ][DL] Char Write Req, char : 47
[16:30:46.095]  [00:00:11.450][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 9)
[16:30:46.097]  [00:00:11.450][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:46.097]  [00:00:11.450][info  ][BLE] local and remote recv window sizes = 5
[16:30:46.098]  [00:00:11.450][info  ][BLE] selected BTP version 4
[16:30:46.099]  [00:00:11.451][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[16:30:46.388]  [00:00:11.742][info  ][DL] Handling CCCD Write
[16:30:46.388]  [00:00:11.742][error ][-] mConnectionState.allocated:430 false: 3
[16:30:46.388]  [00:00:11.742][error ][-] Error CHIP:0x00000003 at C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:303
[16:30:46.680]  [00:00:12.035][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[16:30:46.681]  [00:00:12.035][info  ][DL] CHIPoBLE subscribe received
[16:30:46.682]  [00:00:12.035][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[16:30:46.682]  [00:00:12.036][detail][IN] BLE EndPoint 0x20012a2c Connection Complete
[16:30:46.683]  [00:00:12.036][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[16:30:46.684]  [00:00:12.036][silabs ]NWK: platform event type 8006
[16:30:46.684]  [00:00:12.036][silabs ]COM: notify network [Leave]
[16:30:47.070]  [00:00:12.424][info  ][DL] Tx Confirmation received
[16:30:47.070]  [00:00:12.424][info  ][DL]  stop soft timer
[16:30:47.071]  [00:00:12.424][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:47.168]  [00:00:12.522][info  ][DL] Char Write Req, char : 47
[16:30:47.168]  [00:00:12.522][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 103)
[16:30:47.169]  [00:00:12.522][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:47.170]  [00:00:12.523][info  ][EM] >>> [E:28666r S:0 M:35572782] (U) Msg RX from 0:40C7052742D2DE78 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[16:30:47.172]  [00:00:12.523][detail][EM] Handling via exchange: 28666r, Delegate: 0x200097b8
[16:30:47.173]  [00:00:12.523][detail][SC] Received PBKDF param request
[16:30:47.173]  [00:00:12.524][detail][SC] Peer assigned session ID 42557
[16:30:47.174]  [00:00:12.524][detail][SC] Found MRP parameters in the message
[16:30:47.175]  [00:00:12.526][info  ][EM] <<< [E:28666r S:0 M:137509410] (U) Msg TX from 0000000000000000 to 0:40C7052742D2DE78 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[16:30:47.177]  [00:00:12.527][detail][SC] Sent PBKDF param response
[16:30:47.177]  [00:00:12.527][info  ][SVR] Commissioning session establishment step started
[16:30:47.460]  [00:00:12.814][info  ][DL] Tx Confirmation received
[16:30:47.460]  [00:00:12.814][info  ][DL]  stop soft timer
[16:30:47.461]  [00:00:12.815][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:47.463]  [00:00:12.817][info  ][DL] Char Write Req, char : 47
[16:30:47.463]  [00:00:12.817][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 97)
[16:30:47.465]  [00:00:12.817][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:47.465]  [00:00:12.818][info  ][EM] >>> [E:28666r S:0 M:35572783] (U) Msg RX from 0:40C7052742D2DE78 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[16:30:47.468]  [00:00:12.818][detail][EM] Found matching exchange: 28666r, Delegate: 0x200097b8
[16:30:47.468]  [00:00:12.818][detail][SC] Received spake2p msg1
[16:30:47.522]  [00:00:12.875][info  ][EM] <<< [E:28666r S:0 M:137509411] (U) Msg TX from 0000000000000000 to 0:40C7052742D2DE78 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[16:30:47.524]  [00:00:12.876][detail][SC] Sent spake2p msg2
[16:30:47.753]  [00:00:13.106][info  ][DL] Tx Confirmation received
[16:30:47.753]  [00:00:13.107][info  ][DL]  stop soft timer
[16:30:47.754]  [00:00:13.107][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:47.755]  [00:00:13.109][info  ][DL] Char Write Req, char : 47
[16:30:47.755]  [00:00:13.109][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 64)
[16:30:47.757]  [00:00:13.109][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:47.757]  [00:00:13.110][info  ][EM] >>> [E:28666r S:0 M:35572784] (U) Msg RX from 0:40C7052742D2DE78 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[16:30:47.759]  [00:00:13.110][detail][EM] Found matching exchange: 28666r, Delegate: 0x200097b8
[16:30:47.760]  [00:00:13.110][detail][SC] Received spake2p msg3
[16:30:47.761]  [00:00:13.111][detail][SC] Sending status report. Protocol code 0, exchange 28666
[16:30:47.762]  [00:00:13.111][info  ][EM] <<< [E:28666r S:0 M:137509412] (U) Msg TX from 0000000000000000 to 0:40C7052742D2DE78 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[16:30:47.764]  [00:00:13.116][info  ][SC] SecureSession[0x20007030, LSID:8047]: State change 'kEstablishing' --> 'kActive'
[16:30:47.765]  
[16:30:47.765]  [00:00:13.116][detail][IN] SecureSession[0x20007030]: Activated - Type:1 LSID:8047
[16:30:47.766]  [00:00:13.116][detail][IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:8047 PSID:42557!
[16:30:47.767]  [00:00:13.116][info  ][SVR] Commissioning completed session establishment step
[16:30:47.768]  [00:00:13.117][info  ][DIS] Updating services using commissioning mode 0
[16:30:47.768]  [00:00:13.117][error ][DIS] Failed to remove advertised services: 3
[16:30:47.769]  [00:00:13.117][error ][DIS] Failed to finalize service update: 3
[16:30:47.770]  [00:00:13.117][info  ][SVR] Device completed Rendezvous process
[16:30:47.771]  [00:00:13.117][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:30:47.772]  [00:00:13.118][silabs ]NWK: platform event type 8018
[16:30:47.773]  [00:00:13.118][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[16:30:47.948]  [00:00:13.301][info  ][DL] Tx Confirmation received
[16:30:47.948]  [00:00:13.301][info  ][DL]  stop soft timer
[16:30:47.948]  [00:00:13.302][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:48.046]  [00:00:13.400][info  ][DL] Char Write Req, char : 47
[16:30:48.046]  [00:00:13.400][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 139)
[16:30:48.047]  [00:00:13.401][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:48.049]  [00:00:13.403][info  ][EM] >>> [E:28667r S:8047 M:216523822] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:134)
[16:30:48.050]  [00:00:13.403][detail][EM] Handling via exchange: 28667r, Delegate: 0x2000413c
[16:30:48.051]  [00:00:13.403][detail][IM] Received Read request
[16:30:48.055]  [00:00:13.409][detail][DMG] IM RH moving to [CanStartReporting]
[16:30:48.055]  [00:00:13.409][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:30:48.057]  [00:00:13.410][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[16:30:48.058]  [00:00:13.411][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[16:30:48.059]  [00:00:13.413][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[16:30:48.060]  [00:00:13.414][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:30:48.061]  [00:00:13.416][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[16:30:48.062]  [00:00:13.416][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:30:48.064]  [00:00:13.417][detail][DMG] <RE:Run> Cluster 30, Attribute 3 is dirty
[16:30:48.064]  [00:00:13.418][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[16:30:48.066]  [00:00:13.419][detail][DMG] <RE:Run> Cluster 30, Attribute 2 is dirty
[16:30:48.067]  [00:00:13.420][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:30:48.088]  [00:00:13.442][detail][DMG] <RE:Run> Cluster 30, Attribute 1 is dirty
[16:30:48.089]  [00:00:13.442][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:30:48.089]  [00:00:13.444][detail][DMG] <RE:Run> Cluster 30, Attribute 0 is dirty
[16:30:48.091]  [00:00:13.445][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:30:48.092]  [00:00:13.446][detail][DMG] <RE:Run> Cluster 30, Attribute 4 is dirty
[16:30:48.093]  [00:00:13.447][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[16:30:48.094]  [00:00:13.448][detail][DMG] <RE> Sending report (payload has 227 bytes)...
[16:30:48.096]  [00:00:13.450][info  ][EM] <<< [E:28667r S:8047 M:9561277] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:257)
[16:30:48.097]  [00:00:13.450][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:30:48.098]  [00:00:13.451][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:30:48.099]  [00:00:13.451][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:30:48.100]  [00:00:13.451][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:30:48.338]  [00:00:13.692][info  ][DL] Tx Confirmation received
[16:30:48.338]  [00:00:13.692][info  ][DL]  stop soft timer
[16:30:48.338]  [00:00:13.692][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:48.532]  [00:00:13.886][info  ][DL] Tx Confirmation received
[16:30:48.532]  [00:00:13.887][info  ][DL]  stop soft timer
[16:30:48.533]  [00:00:13.887][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:48.633]  [00:00:13.987][info  ][DL] Char Write Req, char : 47
[16:30:48.633]  [00:00:13.987][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 108)
[16:30:48.635]  [00:00:13.988][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:48.636]  [00:00:13.990][info  ][EM] >>> [E:28668r S:8047 M:216523823] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:103)
[16:30:48.638]  [00:00:13.990][detail][EM] Handling via exchange: 28668r, Delegate: 0x2000413c
[16:30:48.638]  [00:00:13.990][detail][IM] Received Read request
[16:30:48.639]  [00:00:13.993][detail][DMG] IM RH moving to [CanStartReporting]
[16:30:48.640]  [00:00:13.994][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[16:30:48.641]  [00:00:13.995][detail][DMG] <RE:Run> Cluster 46, Attribute 2 is dirty
[16:30:48.643]  [00:00:13.995][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[16:30:48.643]  [00:00:13.997][detail][DMG] <RE:Run> Cluster 46, Attribute 1 is dirty
[16:30:48.644]  [00:00:13.997][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[16:30:48.645]  [00:00:13.999][detail][DMG] <RE:Run> Cluster 46, Attribute 0 is dirty
[16:30:48.646]  [00:00:14.000][detail][DMG] Reading attribute: Cluster=0x0000_0046 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[16:30:48.647]  [00:00:14.000][detail][DMG] <RE:Run> Cluster 46, Attribute 7 is dirty
[16:30:48.648]  [00:00:14.001][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0007err = 586
[16:30:48.650]  [00:00:14.003][detail][DMG] <RE:Run> Cluster 46, Attribute 6 is dirty
[16:30:48.651]  [00:00:14.004][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0006err = 586
[16:30:48.652]  [00:00:14.005][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[16:30:48.653]  [00:00:14.006][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[16:30:48.654]  [00:00:14.008][detail][DMG] <RE> Sending report (payload has 161 bytes)...
[16:30:48.657]  [00:00:14.010][info  ][EM] <<< [E:28668r S:8047 M:9561278] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:191)
[16:30:48.658]  [00:00:14.010][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[16:30:48.659]  [00:00:14.011][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[16:30:48.660]  [00:00:14.011][detail][DMG] IM RH moving to [AwaitingDestruction]
[16:30:48.661]  [00:00:14.011][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[16:30:49.118]  [00:00:14.471][info  ][DL] Tx Confirmation received
[16:30:49.118]  [00:00:14.471][info  ][DL]  stop soft timer
[16:30:49.119]  [00:00:14.472][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:49.120]  [00:00:14.474][info  ][DL] Char Write Req, char : 47
[16:30:49.120]  [00:00:14.474][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:30:49.122]  [00:00:14.474][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:49.123]  [00:00:14.476][info  ][EM] >>> [E:28669r S:8047 M:216523824] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:30:49.125]  [00:00:14.477][detail][EM] Handling via exchange: 28669r, Delegate: 0x2000413c
[16:30:49.125]  [00:00:14.478][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:30:49.127]  [00:00:14.478][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[16:30:49.127]  [00:00:14.478][detail][DMG] Command handler moving to [NewRespons]
[16:30:49.128]  [00:00:14.478][detail][DMG] Command handler moving to [ Preparing]
[16:30:49.129]  [00:00:14.479][detail][DMG] Command handler moving to [AddingComm]
[16:30:49.129]  [00:00:14.479][detail][DMG] Command handler moving to [AddedComma]
[16:30:49.131]  [00:00:14.479][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:49.132]  [00:00:14.480][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:49.132]  [00:00:14.480][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:49.133]  [00:00:14.482][info  ][EM] <<< [E:28669r S:8047 M:9561279] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:30:49.135]  [00:00:14.483][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:49.313]  [00:00:14.666][info  ][DL] Tx Confirmation received
[16:30:49.313]  [00:00:14.666][info  ][DL]  stop soft timer
[16:30:49.313]  [00:00:14.667][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:49.316]  [00:00:14.669][info  ][DL] Char Write Req, char : 47
[16:30:49.316]  [00:00:14.669][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 75)
[16:30:49.317]  [00:00:14.669][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:49.318]  [00:00:14.671][info  ][EM] >>> [E:28670r S:8047 M:216523825] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[16:30:49.320]  [00:00:14.672][detail][EM] Handling via exchange: 28670r, Delegate: 0x2000413c
[16:30:49.321]  [00:00:14.673][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0002
[16:30:49.322]  [00:00:14.673][detail][DMG] Command handler moving to [NewRespons]
[16:30:49.323]  [00:00:14.674][detail][DMG] Command handler moving to [ Preparing]
[16:30:49.324]  [00:00:14.674][detail][DMG] Command handler moving to [AddingComm]
[16:30:49.324]  [00:00:14.674][detail][DMG] Command handler moving to [AddedComma]
[16:30:49.325]  [00:00:14.674][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:49.326]  [00:00:14.675][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:49.327]  [00:00:14.675][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:49.328]  [00:00:14.677][info  ][EM] <<< [E:28670r S:8047 M:9561280] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:30:49.330]  [00:00:14.678][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:49.507]  [00:00:14.862][info  ][DL] Tx Confirmation received
[16:30:49.507]  [00:00:14.862][info  ][DL]  stop soft timer
[16:30:49.508]  [00:00:14.862][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:49.510]  [00:00:14.864][info  ][DL] Char Write Req, char : 47
[16:30:49.510]  [00:00:14.864][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:30:49.511]  [00:00:14.865][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:49.512]  [00:00:14.867][info  ][EM] >>> [E:28671r S:8047 M:216523826] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:30:49.514]  [00:00:14.867][detail][EM] Handling via exchange: 28671r, Delegate: 0x2000413c
[16:30:49.515]  [00:00:14.868][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:30:49.516]  [00:00:14.868][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[16:30:49.517]  [00:00:14.869][detail][DMG] Command handler moving to [NewRespons]
[16:30:49.517]  [00:00:14.869][detail][DMG] Command handler moving to [ Preparing]
[16:30:49.518]  [00:00:14.869][detail][DMG] Command handler moving to [AddingComm]
[16:30:49.519]  [00:00:14.869][detail][DMG] Command handler moving to [AddedComma]
[16:30:49.520]  [00:00:14.870][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:49.521]  [00:00:14.870][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:49.522]  [00:00:14.870][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:49.522]  [00:00:14.872][info  ][EM] <<< [E:28671r S:8047 M:9561281] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[16:30:49.524]  [00:00:14.873][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:49.801]  [00:00:15.154][info  ][DL] Tx Confirmation received
[16:30:49.801]  [00:00:15.155][info  ][DL]  stop soft timer
[16:30:49.801]  [00:00:15.155][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:50.288]  [00:00:15.642][info  ][DL] Tx Confirmation received
[16:30:50.288]  [00:00:15.642][info  ][DL]  stop soft timer
[16:30:50.289]  [00:00:15.642][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:50.483]  [00:00:15.836][info  ][DL] Tx Confirmation received
[16:30:50.483]  [00:00:15.836][info  ][DL]  stop soft timer
[16:30:50.484]  [00:00:15.837][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:50.485]  [00:00:15.839][info  ][DL] Char Write Req, char : 47
[16:30:50.485]  [00:00:15.839][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[16:30:50.487]  [00:00:15.839][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:50.488]  [00:00:15.841][info  ][EM] >>> [E:28672r S:8047 M:216523827] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[16:30:50.490]  [00:00:15.842][detail][EM] Handling via exchange: 28672r, Delegate: 0x2000413c
[16:30:50.490]  [00:00:15.843][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[16:30:50.492]  [00:00:15.843][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[16:30:50.492]  [00:00:15.843][detail][DMG] Command handler moving to [NewRespons]
[16:30:50.493]  [00:00:15.843][detail][DMG] Command handler moving to [ Preparing]
[16:30:50.494]  [00:00:15.844][detail][DMG] Command handler moving to [AddingComm]
[16:30:50.495]  [00:00:15.844][detail][DMG] Command handler moving to [AddedComma]
[16:30:50.496]  [00:00:15.844][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:50.496]  [00:00:15.844][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:50.497]  [00:00:15.845][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:50.499]  [00:00:15.847][info  ][EM] <<< [E:28672r S:8047 M:9561282] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[16:30:50.500]  [00:00:15.848][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:50.873]  [00:00:16.227][info  ][DL] Tx Confirmation received
[16:30:50.873]  [00:00:16.227][info  ][DL]  stop soft timer
[16:30:50.874]  [00:00:16.227][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:51.165]  [00:00:16.519][info  ][DL] Tx Confirmation received
[16:30:51.165]  [00:00:16.519][info  ][DL]  stop soft timer
[16:30:51.166]  [00:00:16.520][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:51.360]  [00:00:16.714][info  ][DL] Tx Confirmation received
[16:30:51.360]  [00:00:16.714][info  ][DL]  stop soft timer
[16:30:51.361]  [00:00:16.714][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:51.363]  [00:00:16.717][info  ][DL] Char Write Req, char : 47
[16:30:51.363]  [00:00:16.717][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[16:30:51.365]  [00:00:16.717][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:51.366]  [00:00:16.719][info  ][EM] >>> [E:28673r S:8047 M:216523828] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[16:30:51.367]  [00:00:16.720][detail][EM] Handling via exchange: 28673r, Delegate: 0x2000413c
[16:30:51.368]  [00:00:16.721][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0000
[16:30:51.369]  [00:00:16.721][info  ][ZCL] OpCreds: Received an AttestationRequest command
[16:30:51.374]  [00:00:16.728][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:599, sig_size:64, err:0x00
[16:30:51.375]  [00:00:16.728][info  ][ZCL] OpCreds: AttestationRequest successful.
[16:30:51.375]  [00:00:16.728][detail][DMG] Command handler moving to [NewRespons]
[16:30:51.376]  [00:00:16.728][detail][DMG] Command handler moving to [ Preparing]
[16:30:51.377]  [00:00:16.728][detail][DMG] Command handler moving to [AddingComm]
[16:30:51.377]  [00:00:16.729][detail][DMG] Command handler moving to [AddedComma]
[16:30:51.378]  [00:00:16.729][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:51.379]  [00:00:16.729][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:51.380]  [00:00:16.729][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:51.381]  [00:00:16.731][info  ][EM] <<< [E:28673r S:8047 M:9561283] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[16:30:51.383]  [00:00:16.732][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:51.751]  [00:00:17.104][info  ][DL] Tx Confirmation received
[16:30:51.751]  [00:00:17.104][info  ][DL]  stop soft timer
[16:30:51.751]  [00:00:17.105][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:52.141]  [00:00:17.495][info  ][DL] Tx Confirmation received
[16:30:52.141]  [00:00:17.495][info  ][DL]  stop soft timer
[16:30:52.141]  [00:00:17.495][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:52.433]  [00:00:17.787][info  ][DL] Tx Confirmation received
[16:30:52.433]  [00:00:17.787][info  ][DL]  stop soft timer
[16:30:52.433]  [00:00:17.788][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:52.436]  [00:00:17.790][info  ][DL] Char Write Req, char : 47
[16:30:52.436]  [00:00:17.790][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[16:30:52.437]  [00:00:17.790][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:52.438]  [00:00:17.792][info  ][EM] >>> [E:28674r S:8047 M:216523829] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[16:30:52.440]  [00:00:17.792][detail][EM] Handling via exchange: 28674r, Delegate: 0x2000413c
[16:30:52.441]  [00:00:17.793][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0004
[16:30:52.442]  [00:00:17.793][info  ][ZCL] OpCreds: Received a CSRRequest command
[16:30:52.443]  [00:00:17.794][error ][CR] WARNING: PSA key recycled: 0 / 17408
[16:30:52.453]  [00:00:17.807][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[16:30:52.459]  [00:00:17.813][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:276, sig_size:64, err:0x00
[16:30:52.460]  [00:00:17.814][info  ][ZCL] OpCreds: CSRRequest successful.
[16:30:52.461]  [00:00:17.814][detail][DMG] Command handler moving to [NewRespons]
[16:30:52.462]  [00:00:17.814][detail][DMG] Command handler moving to [ Preparing]
[16:30:52.462]  [00:00:17.814][detail][DMG] Command handler moving to [AddingComm]
[16:30:52.463]  [00:00:17.814][detail][DMG] Command handler moving to [AddedComma]
[16:30:52.464]  [00:00:17.815][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:52.465]  [00:00:17.815][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:52.466]  [00:00:17.815][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:52.466]  [00:00:17.817][info  ][EM] <<< [E:28674r S:8047 M:9561284] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:391)
[16:30:52.469]  [00:00:17.818][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:52.823]  [00:00:18.177][info  ][DL] Tx Confirmation received
[16:30:52.823]  [00:00:18.177][info  ][DL]  stop soft timer
[16:30:52.823]  [00:00:18.177][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:53.115]  [00:00:18.469][info  ][DL] Tx Confirmation received
[16:30:53.115]  [00:00:18.469][info  ][DL]  stop soft timer
[16:30:53.116]  [00:00:18.470][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:53.508]  [00:00:18.862][info  ][DL] Char Write Req, char : 47
[16:30:53.508]  [00:00:18.863][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:30:53.509]  [00:00:18.863][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:53.701]  [00:00:19.056][info  ][DL] Char Write Req, char : 47
[16:30:53.701]  [00:00:19.056][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 56)
[16:30:53.703]  [00:00:19.056][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:53.704]  [00:00:19.058][info  ][EM] >>> [E:28675r S:8047 M:216523830] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[16:30:53.706]  [00:00:19.059][detail][EM] Handling via exchange: 28675r, Delegate: 0x2000413c
[16:30:53.706]  [00:00:19.060][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B
[16:30:53.708]  [00:00:19.060][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[16:30:53.719]  [00:00:19.073][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[16:30:53.719]  [00:00:19.074][detail][DMG] Command handler moving to [NewRespons]
[16:30:53.720]  [00:00:19.074][detail][DMG] Command handler moving to [ Preparing]
[16:30:53.721]  [00:00:19.074][detail][DMG] Command handler moving to [AddingComm]
[16:30:53.722]  [00:00:19.074][detail][DMG] Command handler moving to [AddedComma]
[16:30:53.722]  [00:00:19.075][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:53.723]  [00:00:19.075][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:53.724]  [00:00:19.076][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:53.725]  [00:00:19.078][info  ][EM] <<< [E:28675r S:8047 M:9561285] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[16:30:53.727]  [00:00:19.079][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:53.895]  [00:00:19.250][info  ][DL] Tx Confirmation received
[16:30:53.895]  [00:00:19.250][info  ][DL]  stop soft timer
[16:30:53.896]  [00:00:19.250][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:54.090]  [00:00:19.445][info  ][DL] Char Write Req, char : 47
[16:30:54.090]  [00:00:19.445][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:30:54.092]  [00:00:19.445][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:54.386]  [00:00:19.740][info  ][DL] Char Write Req, char : 47
[16:30:54.386]  [00:00:19.740][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 244)
[16:30:54.387]  [00:00:19.740][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:54.580]  [00:00:19.934][info  ][DL] Char Write Req, char : 47
[16:30:54.580]  [00:00:19.934][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 88)
[16:30:54.581]  [00:00:19.934][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:54.583]  [00:00:19.937][info  ][EM] >>> [E:28676r S:8047 M:216523831] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[16:30:54.584]  [00:00:19.937][detail][EM] Handling via exchange: 28676r, Delegate: 0x2000413c
[16:30:54.585]  [00:00:19.938][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0006
[16:30:54.586]  [00:00:19.938][info  ][ZCL] OpCreds: Received an AddNOC command
[16:30:54.587]  [00:00:19.940][info  ][FP] Validating NOC chain
[16:30:54.614]  [00:00:19.968][info  ][FP] NOC chain validation successful
[16:30:54.614]  [00:00:19.968][info  ][FP] Added new fabric at index: 0x1
[16:30:54.615]  [00:00:19.969][info  ][FP] Assigned compressed fabric ID: 0x9BB8A0DFD2A8507B, node ID: 0x00000000000008CA
[16:30:54.616]  [00:00:19.969][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[16:30:54.618]  [00:00:19.969][info  ][TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[16:30:54.618]  [00:00:19.969][info  ][TS] Retaining current Last Known Good Time
[16:30:54.627]  [00:00:19.982][detail][EVL] LogEvent event number: 0x0000000000000002 priority: 1, endpoint id:  0x0 cluster id: 0x0000_001F event id: 0x0 Epoch timestamp: 0x000000DC6ACFF9CB
[16:30:54.629]  [00:00:19.982][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0x000000000001B669
[16:30:54.630]  
[16:30:54.630]  [00:00:19.982][detail][DL] Using Thread extended MAC for hostname.
[16:30:54.631]  [00:00:19.982][info  ][DIS] Advertise operational node 9BB8A0DFD2A8507B-00000000000008CA
[16:30:54.632]  [00:00:19.982][error ][SVR] Operational advertising failed: 3
[16:30:54.633]  [00:00:19.983][detail][DMG] Command handler moving to [NewRespons]
[16:30:54.633]  [00:00:19.983][detail][DMG] Command handler moving to [ Preparing]
[16:30:54.635]  [00:00:19.983][detail][DMG] Command handler moving to [AddingComm]
[16:30:54.635]  [00:00:19.983][detail][DMG] Command handler moving to [AddedComma]
[16:30:54.635]  [00:00:19.983][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[16:30:54.636]  [00:00:19.984][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:54.638]  [00:00:19.984][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:54.638]  [00:00:19.986][info  ][EM] <<< [E:28676r S:8047 M:9561286] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [507B] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:30:54.640]  [00:00:19.987][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:54.912]  
[16:30:54.968]  [00:00:20.322][info  ][DL] Tx Confirmation received
[16:30:54.968]  [00:00:20.322][info  ][DL]  stop soft timer
[16:30:54.969]  [00:00:20.323][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:55.067]  [00:00:20.421][info  ][DL] Char Write Req, char : 47
[16:30:55.067]  [00:00:20.421][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 176)
[16:30:55.069]  [00:00:20.421][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:55.070]  [00:00:20.423][info  ][EM] >>> [E:28677r S:8047 M:216523832] (S) Msg RX from 1:FFFFFFFB00000000 [507B] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[16:30:55.072]  [00:00:20.424][detail][EM] Handling via exchange: 28677r, Delegate: 0x2000413c
[16:30:55.072]  [00:00:20.425][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0003
[16:30:55.074]  [00:00:20.426][detail][DMG] Command handler moving to [NewRespons]
[16:30:55.074]  [00:00:20.426][detail][DMG] Command handler moving to [ Preparing]
[16:30:55.075]  [00:00:20.427][detail][DMG] Command handler moving to [AddingComm]
[16:30:55.076]  [00:00:20.427][detail][DMG] Command handler moving to [AddedComma]
[16:30:55.076]  [00:00:20.427][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:55.078]  [00:00:20.427][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:55.079]  [00:00:20.428][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:55.079]  [00:00:20.429][info  ][EM] <<< [E:28677r S:8047 M:9561287] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [507B] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:30:55.081]  [00:00:20.430][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:55.357]  [00:00:20.711][info  ][DL] Tx Confirmation received
[16:30:55.357]  [00:00:20.711][info  ][DL]  stop soft timer
[16:30:55.358]  [00:00:20.712][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:55.360]  [00:00:20.714][info  ][DL] Char Write Req, char : 47
[16:30:55.360]  [00:00:20.714][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[16:30:55.361]  [00:00:20.714][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:55.362]  [00:00:20.716][info  ][EM] >>> [E:28678r S:8047 M:216523833] (S) Msg RX from 1:FFFFFFFB00000000 [507B] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[16:30:55.364]  [00:00:20.717][detail][EM] Handling via exchange: 28678r, Delegate: 0x2000413c
[16:30:55.365]  [00:00:20.718][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[16:30:55.366]  [00:00:20.718][info  ][FS] GeneralCommissioning: Received ArmFailSafe (108s)
[16:30:55.367]  [00:00:20.718][detail][DMG] Command handler moving to [NewRespons]
[16:30:55.367]  [00:00:20.718][detail][DMG] Command handler moving to [ Preparing]
[16:30:55.368]  [00:00:20.719][detail][DMG] Command handler moving to [AddingComm]
[16:30:55.369]  [00:00:20.719][detail][DMG] Command handler moving to [AddedComma]
[16:30:55.370]  [00:00:20.719][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:55.371]  [00:00:20.719][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:55.371]  [00:00:20.720][detail][DMG] Command handler moving to [AwaitingDe]
[16:30:55.372]  [00:00:20.722][info  ][EM] <<< [E:28678r S:8047 M:9561288] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [507B] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[16:30:55.374]  [00:00:20.722][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:55.552]  [00:00:20.907][info  ][DL] Tx Confirmation received
[16:30:55.552]  [00:00:20.907][info  ][DL]  stop soft timer
[16:30:55.553]  [00:00:20.908][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:55.555]  [00:00:20.910][info  ][DL] Char Write Req, char : 47
[16:30:55.555]  [00:00:20.910][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 78)
[16:30:55.556]  [00:00:20.910][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:55.558]  [00:00:20.912][info  ][EM] >>> [E:28679r S:8047 M:216523834] (S) Msg RX from 1:FFFFFFFB00000000 [507B] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[16:30:55.559]  [00:00:20.913][detail][EM] Handling via exchange: 28679r, Delegate: 0x2000413c
[16:30:55.560]  [00:00:20.914][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0006
[16:30:55.561]  [00:00:20.914][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 3
[16:30:55.570]  [00:00:20.923][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 2
[16:30:55.570]  [00:00:20.924][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:30:55.571]  [00:00:20.924][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[16:30:55.572]  [00:00:20.924][silabs ]NWK: platform event type 8004
[16:30:55.572]  [00:00:20.925][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:30:55.573]  
[16:30:55.573]  [00:00:20.925][detail][DL] OpenThread State Changed (Flags: 0x1117d11d)
[16:30:55.574]  [00:00:20.925][detail][DL]    Device Role: DETACHED
[16:30:55.575]  [00:00:20.925][detail][DL]    Network Name: OpenThread-cdd2
[16:30:55.576]  [00:00:20.925][detail][DL]    PAN Id: 0xCDD2
[16:30:55.576]  [00:00:20.926][detail][DL]    Extended PAN Id: 0x4C579A3A07CA6346
[16:30:55.577]  [00:00:20.926][detail][DL]    Channel: 24
[16:30:55.577]  [00:00:20.926][detail][DL]    Mesh Prefix: fdf9:32b5:229:8114:0:0:0:0/64
[16:30:55.578]  [00:00:20.926][detail][DL]    Thread Unicast Addresses:
[16:30:55.578]  [00:00:20.927][detail][DL]         fdf9:32b5:229:8114:d5ed:65af:b33f:9706/64 valid preferred
[16:30:55.580]  [00:00:20.927][detail][DL]         fe80:0:0:0:7cb3:a056:f6b7:a056/64 valid preferred
[16:30:56.509]  [00:00:21.863][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[16:30:56.510]  [00:00:21.864][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:30:56.511]  [00:00:21.864][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[16:30:56.512]  [00:00:21.864][detail][EVL] LogEvent event number: 0x0000000000000003 priority: 1, endpoint id:  0x0 cluster id: 0x0000_0035 event id: 0x0 Epoch timestamp: 0x000000DC6AD00125
[16:30:56.513]  
[16:30:56.514]  [00:00:21.864][detail][DL] OpenThread State Changed (Flags: 0x200002a4)
[16:30:56.515]  
[16:30:56.515]  [00:00:21.865][detail][DL]    Device Role: CHILD
[16:30:56.516]  [00:00:21.865][detail][DL]    Partition Id: 0x13AAA5D9
[16:30:56.516]  [00:00:21.865][silabs ]NWK: platform event type 800b
[16:30:56.517]  [00:00:21.866][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[16:30:56.518]  [00:00:21.866][silabs ]NWK: platform event type 8001
[16:30:56.518]  
[16:30:56.518]  [00:00:21.866][silabs ]COM: notify network [Joined]
[16:30:56.519]  
[16:30:56.519]  [00:00:21.866][silabs ]NWK: Thread Established
[16:30:56.520]  
[16:30:56.520]  [00:00:21.866][info  ][SVR] Scheduling OTA Requestor initialization
[16:30:56.520]  
[16:30:56.520]  [00:00:21.867][detail][DL] Thread Attached updating Multicast address
[16:30:56.522]  
[16:30:56.522]  [00:00:21.868][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[16:30:56.522]  [00:00:21.870][info  ][EM] <<< [E:28679r S:8047 M:9561289] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [507B] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[16:30:56.524]  [00:00:21.872][detail][DMG] Command response sender moving to [AllInvokeR]
[16:30:56.525]  [00:00:21.872][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[16:30:56.526]  [00:00:21.872][detail][DL] Using Thread extended MAC for hostname.
[16:30:56.527]  [00:00:21.872][info  ][DIS] Advertise operational node 9BB8A0DFD2A8507B-00000000000008CA
[16:30:56.529]  [00:00:21.874][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:30:56.529]  [00:00:21.874][detail][DL]    Thread Unicast Addresses:
[16:30:56.530]  [00:00:21.875][detail][DL]         fdf9:32b5:229:8114:d5ed:65af:b33f:9706/64 valid preferred
[16:30:56.626]  [00:00:21.980][info  ][DL] Tx Confirmation received
[16:30:56.626]  [00:00:21.980][info  ][DL]  stop soft timer
[16:30:56.626]  [00:00:21.980][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[16:30:56.911]  
[16:30:57.250]  [00:00:22.604][detail][DL] SRP update succeeded
[16:30:57.250]  [00:00:22.604][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[16:30:57.250]  [00:00:22.604][silabs ]NWK: platform event type 8012
[16:30:57.251]  [00:00:22.605][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[16:30:57.252]  [00:00:22.605][info  ][SVR] Server initialization complete
[16:30:57.253]  [00:00:22.605][info  ][DIS] Updating services using commissioning mode 0
[16:30:57.254]  [00:00:22.605][detail][DL] Using Thread extended MAC for hostname.
[16:30:57.254]  [00:00:22.605][info  ][DIS] Advertise operational node 9BB8A0DFD2A8507B-00000000000008CA
[16:30:57.255]  [00:00:22.606][info  ][DL] advertising srp service: 9BB8A0DFD2A8507B-00000000000008CA._matter._tcp
[16:30:57.257]  [00:00:22.607][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[16:30:57.257]  [00:00:22.607][silabs ]NWK: platform event type 8016
[16:30:57.263]  [00:00:22.618][info  ][IM] No subscriptions to resume
[16:30:58.607]  [00:00:23.960][detail][DL] SRP update succeeded
[16:30:59.063]  [00:00:24.417][info  ][DL] Char Write Req, char : 47
[16:30:59.063]  [00:00:24.417][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 3)
[16:30:59.065]  [00:00:24.417][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[16:30:59.156]  [00:00:24.510][detail][IN] UDP Message Received packet nb : 1 SrcAddr : fd98:42ee:f6b4:1:cc62:db03:753:ecd0[50065] DestAddr : fd98:42ee:f6b4:1:b8af:f97:7b89:6195[5540] Payload Length 196
[16:30:59.157]  [00:00:24.511][info  ][EM] >>> [E:28680r S:0 M:35572785] (U) Msg RX from 0:D62791A8431B9F85 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:30:59.159]  [00:00:24.511][detail][EM] Handling via exchange: 28680r, Delegate: 0x20007de8
[16:30:59.160]  [00:00:24.511][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200089b0
[16:30:59.161]  [00:00:24.512][info  ][EM] <<< [E:28680r S:0 M:137509413 (Ack:35572785)] (U) Msg TX from 0000000000000000 to 0:D62791A8431B9F85 [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:50065] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:30:59.164]  [00:00:24.512][detail][EM] Flushed pending ack for MessageCounter:35572785 on exchange 28680r
[16:30:59.165]  [00:00:24.513][info  ][SC] Received Sigma1 msg
[16:30:59.166]  [00:00:24.513][detail][SC] Found MRP parameters in the message
[16:30:59.166]  [00:00:24.514][detail][SC] Peer (Initiator) assigned session ID 42558
[16:30:59.169]  [00:00:24.523][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[16:30:59.190]  [00:00:24.544][detail][CR] AES_CCM_encrypt: Using aad == null path
[16:30:59.193]  [00:00:24.547][info  ][EM] <<< [E:28680r S:0 M:137509414 (Ack:35572785)] (U) Msg TX from 0000000000000000 to 0:D62791A8431B9F85 [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:50065] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[16:30:59.195]  [00:00:24.548][info  ][EM] ??1 [E:28680r S:0 M:137509414] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3373ms from now [State:Active II:500 AI:300 AT:4000]
[16:30:59.197]  [00:00:24.548][info  ][SC] Sent Sigma2 msg
[16:30:59.820]  [00:00:25.174][detail][IN] UDP Message Received packet nb : 2 SrcAddr : fd98:42ee:f6b4:1:cc62:db03:753:ecd0[50065] DestAddr : fd98:42ee:f6b4:1:b8af:f97:7b89:6195[5540] Payload Length 598
[16:30:59.821]  [00:00:25.175][info  ][EM] >>> [E:28680r S:0 M:35572786 (Ack:137509414)] (U) Msg RX from 0:D62791A8431B9F85 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[16:30:59.824]  [00:00:25.175][detail][EM] Found matching exchange: 28680r, Delegate: 0x20007e04
[16:30:59.825]  [00:00:25.175][detail][EM] Rxd Ack; Removing MessageCounter:137509414 from Retrans Table on exchange 28680r
[16:30:59.826]  [00:00:25.176][info  ][EM] <<< [E:28680r S:0 M:137509415 (Ack:35572786)] (U) Msg TX from 0000000000000000 to 0:D62791A8431B9F85 [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:50065] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:30:59.828]  [00:00:25.176][detail][EM] Flushed pending ack for MessageCounter:35572786 on exchange 28680r
[16:30:59.830]  [00:00:25.177][info  ][SC] Received Sigma3 msg
[16:30:59.830]  [00:00:25.180][detail][CR] AES_CCM_decrypt: Using aad == null path
[16:30:59.830]  [00:00:25.185][detail][SC] Certificate's mNotBeforeTime (662774400) is after current time (25)
[16:30:59.832]  [00:00:25.185][detail][SC] Certificate's mNotBeforeTime (662774400) is after current time (25)
[16:30:59.832]  [00:00:25.185][detail][SC] Certificate's mNotBeforeTime (662774400) is after current time (25)
[16:30:59.872]  [00:00:25.226][detail][SC] Sending status report. Protocol code 0, exchange 28680
[16:30:59.873]  [00:00:25.227][info  ][EM] <<< [E:28680r S:0 M:137509416 (Ack:35572786)] (U) Msg TX from 0000000000000000 to 0:D62791A8431B9F85 [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:50065] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:30:59.876]  [00:00:25.228][info  ][EM] ??1 [E:28680r S:0 M:137509416] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3367ms from now [State:Active II:500 AI:300 AT:4000]
[16:30:59.877]  [00:00:25.232][info  ][SC] SecureSession[0x20006f58, LSID:8046]: State change 'kEstablishing' --> 'kActive'
[16:30:59.878]  [00:00:25.232][detail][IN] SecureSession[0x20006f58]: Activated - Type:2 LSID:8046
[16:30:59.879]  [00:00:25.232][detail][IN] New secure session activated for device <000000000001B669, 1>, LSID:8046 PSID:42558!
[16:30:59.880]  [00:00:25.232][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[16:30:59.881]  [00:00:25.233][detail][IN] SecureSession[0x20007108]: Allocated Type:2 LSID:8048
[16:30:59.882]  [00:00:25.233][detail][SC] Allocated SecureSession (0x20007108) - waiting for Sigma1 msg
[16:30:59.883]  [00:00:25.234][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:30:59.884]  [00:00:25.234][silabs ]NWK: platform event type 8018
[16:31:00.252]  [00:00:25.606][info  ][SWU] Stopping the watchdog timer
[16:31:00.252]  [00:00:25.607][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:31:00.253]  [00:00:25.607][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to f4115f11
[16:31:00.254]  [00:00:25.607][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to f4115f12
[16:31:00.424]  [00:00:25.779][detail][IN] UDP Message Received packet nb : 3 SrcAddr : fd98:42ee:f6b4:1:cc62:db03:753:ecd0[50065] DestAddr : fd98:42ee:f6b4:1:b8af:f97:7b89:6195[5540] Payload Length 59
[16:31:00.426]  [00:00:25.781][info  ][EM] >>> [E:28681r S:8046 M:53663149] (S) Msg RX from 1:000000000001B669 [507B] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[16:31:00.428]  [00:00:25.782][detail][EM] Handling via exchange: 28681r, Delegate: 0x2000413c
[16:31:00.429]  [00:00:25.783][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0004
[16:31:00.430]  [00:00:25.784][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[16:31:00.431]  [00:00:25.785][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[16:31:00.441]  [00:00:25.795][info  ][TS] Committing Last Known Good Time to storage: 2023-10-10T16:28:52
[16:31:00.450]  [00:00:25.805][detail][IN] UDP Message Received packet nb : 4 SrcAddr : fd98:42ee:f6b4:1:cc62:db03:753:ecd0[50065] DestAddr : fd98:42ee:f6b4:1:b8af:f97:7b89:6195[5540] Payload Length 26
[16:31:00.452]  [00:00:25.805][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x9BB8A0DFD2A8507B, FabricId 0000000000000001, NodeId 00000000000008CA, VendorId 0xFFF1
[16:31:00.454]  [00:00:25.806][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[16:31:00.455]  [00:00:25.806][info  ][FS] Fail-safe cleanly disarmed
[16:31:00.456]  [00:00:25.806][detail][DMG] Command handler moving to [NewRespons]
[16:31:00.457]  [00:00:25.807][detail][DMG] Command handler moving to [ Preparing]
[16:31:00.457]  [00:00:25.807][detail][DMG] Command handler moving to [AddingComm]
[16:31:00.458]  [00:00:25.807][detail][DMG] Command handler moving to [AddedComma]
[16:31:00.459]  
[16:31:00.459]  [00:00:25.807][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[16:31:00.460]  
[16:31:00.460]  [00:00:25.808][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0

[16:31:00.461]  [00:00:25.808][detail][DMG] Command handler moving to [AwaitingDe]

[16:31:00.462]  [00:00:25.810][info  ][EM] <<< [E:28681r S:8046 M:103191473 (Ack:53663149)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [507B] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:50065] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:31:00.465]  [00:00:25.811][info  ][EM] ??1 [E:28681r S:8046 M:103191473] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3389ms from now [State:Active II:500 AI:300 AT:4000]
[16:31:00.466]  [00:00:25.811][detail][DMG] Command response sender moving to [AllInvokeR]
[16:31:00.468]  [00:00:25.812][info  ][EM] >>> [E:28680r S:0 M:35572787 (Ack:137509416)] (U) Msg RX from 0:D62791A8431B9F85 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:31:00.470]  [00:00:25.812][detail][EM] Found matching exchange: 28680r, Delegate: 0
[16:31:00.470]  [00:00:25.812][detail][EM] Rxd Ack; Removing MessageCounter:137509416 from Retrans Table on exchange 28680r
[16:31:00.471]  [00:00:25.813][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[16:31:00.473]  [00:00:25.814][info  ][DIS] Advertise operational node 9BB8A0DFD2A8507B-00000000000008CA
[16:31:00.473]  [00:00:25.815][detail][IN] Clearing BLE pending packets.
[16:31:00.622]  [00:00:25.977][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[16:31:00.623]  [00:00:25.977][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[16:31:00.624]  [00:00:25.978][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[16:31:00.625]  [00:00:25.978][detail][BLE] No endpoint for connection error
[16:31:00.947]  [00:00:26.300][detail][IN] UDP Message Received packet nb : 5 SrcAddr : fd98:42ee:f6b4:1:cc62:db03:753:ecd0[50065] DestAddr : fd98:42ee:f6b4:1:b8af:f97:7b89:6195[5540] Payload Length 34
[16:31:00.948]  [00:00:26.301][info  ][EM] >>> [E:28681r S:8046 M:53663150 (Ack:103191473)] (S) Msg RX from 1:000000000001B669 [507B] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:31:00.950]  [00:00:26.302][detail][EM] Found matching exchange: 28681r, Delegate: 0
[16:31:00.951]  [00:00:26.302][detail][EM] Rxd Ack; Removing MessageCounter:103191473 from Retrans Table on exchange 28681r
```
