```c
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840
[1770371847.375] [5255:5255] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770371847.378] [5255:5255] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770371847.392] [5255:5255] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770371847.392] [5255:5255] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770371847.393] [5255:5255] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770371847.486] [5255:5255] [DL] Wrote settings to /tmp/chip_counters.ini
[1770371847.486] [5255:5255] [DL] NVS set: chip-counters/reboot-count = 4 (0x4)
[1770371847.488] [5255:5255] [DL] Got Ethernet interface: eth0
[1770371847.490] [5255:5255] [DL] Found the primary Ethernet interface:eth0
[1770371847.492] [5255:5255] [DL] Got WiFi interface: wlan0
[1770371847.492] [5255:5255] [DL] Failed to reset WiFi statistic counts
[1770371847.492] [5255:5255] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770371847.658] [5255:5255] [IN] UDP::Init bind&listen port=0
[1770371847.658] [5255:5255] [IN] UDP::Init bound to port=45083
[1770371847.658] [5255:5255] [IN] BLEBase::Init - setting/overriding transport
[1770371847.658] [5255:5255] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770371847.658] [5255:5255] [CTL] NFCBase::Init
[1770371847.658] [5255:5255] [IN] TransportMgr initialized
[1770371847.658] [5255:5255] [FP] Initializing FabricTable from persistent storage
[1770371847.659] [5255:5255] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770371847.664] [5255:5255] [FP] Fabric index 0x1 was retrieved from storage. Compressed FabricId 0x2F35D622378DB6C5, FabricId 0x0000000000000001, NodeId 0x000000000001B669, VendorId 0xFFF1
[1770371847.669] [5255:5255] [DMG] Ember attribute persistence requires setting up
[1770371847.669] [5255:5255] [ZCL] Using ZAP configuration...
[1770371847.674] [5255:5255] [CTL] System State Initialized...
[1770371847.674] [5255:5255] [CTL] Setting attestation nonce to random value
[1770371847.675] [5255:5255] [CTL] Setting CSR nonce to random value
[1770371847.675] [5255:5255] [IN] UDP::Init bind&listen port=5550
[1770371847.675] [5255:5255] [IN] UDP::Init bound to port=5550
[1770371847.675] [5255:5255] [IN] TransportMgr initialized
[1770371847.676] [5255:5273] [DL] CHIP task running
[1770371847.677] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 32786
[1770371847.678] [5255:5273] [CTL] Setting attestation nonce to random value
[1770371847.678] [5255:5273] [CTL] Setting CSR nonce to random value
[1770371847.682] [5255:5273] [CTL] Generating NOC
[1770371847.684] [5255:5273] [FP] Validating NOC chain
[1770371847.689] [5255:5273] [FP] NOC chain validation successful
[1770371847.689] [5255:5273] [FP] Updated fabric at index: 0x1, Node ID: 0x000000000001B669
[1770371847.689] [5255:5273] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770371847.689] [5255:5273] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770371847.689] [5255:5273] [TS] Retaining current Last Known Good Time
[1770371847.699] [5255:5273] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770371847.702] [5255:5273] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770371847.706] [5255:5273] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 2F35D622378DB6C5)
[1770371847.706] [5255:5273] [IN] UDP::Init bind&listen port=5551
[1770371847.706] [5255:5273] [IN] UDP::Init bound to port=5551
[1770371847.706] [5255:5273] [IN] TransportMgr initialized
[1770371847.742] [5255:5273] [CTL] Setting thread operational dataset from parameters
[1770371847.742] [5255:5273] [CTL] Setting attestation nonce to random value
[1770371847.742] [5255:5273] [CTL] Setting CSR nonce to random value
[1770371847.742] [5255:5273] [CTL] Commission called for node ID 0x00000000000008CA
[1770371847.778] [5255:5264] [BLE] BLE removing known devices
[1770371847.782] [5255:5264] [BLE] BLE initiating scan
[1770371847.788] [5255:5273] [BLE] ChipDeviceScanner has started scanning!
[1770371847.801] [5255:5264] [BLE] New device scanned: E8:48:61:70:67:2D
[1770371847.801] [5255:5264] [BLE] Device discriminator match. Attempting to connect.
[1770371847.807] [5255:5264] [BLE] ChipDeviceScanner has stopped scanning!
[1770371847.990] [5255:5264] [DL] ConnectDevice complete
[1770371847.990] [5255:5264] [BLE] New device connected: E8:48:61:70:67:2D
[1770371850.502] [5255:5264] [DL] CHIP service found
[1770371850.502] [5255:5264] [DL] Valid C2 characteristic found
[1770371850.503] [5255:5264] [DL] Valid C1 characteristic found
[1770371850.503] [5255:5264] [DL] New BLE connection: conn=0xffffa0013d80 device=E8:48:61:70:67:2D path=/org/bluez/hci0/dev_E8_48_61_70_67_2D
[1770371850.503] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16387
[1770371850.503] [5255:5273] [DIS] Closing all BLE connections
[1770371850.503] [5255:5273] [IN] BleConnectionComplete: endPoint 0xaaaae63d6fd0
[1770371850.504] [5255:5273] [IN] SecureSession[0xffff9800d750]: Allocated Type:1 LSID:39568
[1770371850.505] [5255:5273] [SC] Assigned local session key ID 39568
[1770371850.505] [5255:5273] [EM] <<< [E:33030i S:0 M:18185579] (U) Msg TX from 6C66530A2D118324 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770371850.505] [5255:5273] [IN] Message appended to BLE send queue
[1770371850.505] [5255:5273] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770371851.421] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371851.715] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16390
[1770371851.715] [5255:5273] [BLE] subscribe complete, ep = 0xaaaae63d6fd0
[1770371851.715] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371851.716] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371851.716] [5255:5273] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770371851.716] [5255:5273] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770371851.716] [5255:5273] [BLE] local and remote recv window size = 5
[1770371851.717] [5255:5273] [IN] BLE EndPoint 0xaaaae63d6fd0 Connection Complete
[1770371852.200] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371852.299] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371852.300] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371852.300] [5255:5273] [EM] >>> [E:33030i S:0 M:121134560] (U) Msg RX from 0:0000000000000000 [0000] to 6C66530A2D118324 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[1770371852.300] [5255:5273] [EM] Found matching exchange: 33030i, Delegate: 0xffff9800fd28
[1770371852.301] [5255:5273] [SC] Received PBKDF param response
[1770371852.301] [5255:5273] [SC] Peer assigned session ID 48002
[1770371852.301] [5255:5273] [SC] Found MRP parameters in the message
[1770371852.323] [5255:5273] [EM] <<< [E:33030i S:0 M:18185580] (U) Msg TX from 6C66530A2D118324 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770371852.324] [5255:5273] [SC] Sent spake2p msg1
[1770371852.493] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371852.786] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371852.787] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371852.787] [5255:5273] [EM] >>> [E:33030i S:0 M:121134561] (U) Msg RX from 0:0000000000000000 [0000] to 6C66530A2D118324 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770371852.787] [5255:5273] [EM] Found matching exchange: 33030i, Delegate: 0xffff9800fd28
[1770371852.788] [5255:5273] [SC] Received spake2p msg2
[1770371852.793] [5255:5273] [EM] <<< [E:33030i S:0 M:18185581] (U) Msg TX from 6C66530A2D118324 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770371852.794] [5255:5273] [SC] Sent spake2p msg3
[1770371852.981] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371852.982] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371852.983] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371852.983] [5255:5273] [EM] >>> [E:33030i S:0 M:121134562] (U) Msg RX from 0:0000000000000000 [0000] to 6C66530A2D118324 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770371852.983] [5255:5273] [EM] Found matching exchange: 33030i, Delegate: 0xffff9800fd28
[1770371852.984] [5255:5273] [SC] SecureSession[0xffff9800d750, LSID:39568]: State change 'kEstablishing' --> 'kActive'
[1770371852.984] [5255:5273] [IN] SecureSession[0xffff9800d750]: Activated - Type:1 LSID:39568
[1770371852.984] [5255:5273] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:39568 PSID:48002!
[1770371852.985] [5255:5273] [CTL] Remote device completed SPAKE2+ handshake
[1770371852.985] [5255:5273] [TOO] Pairing Success
[1770371852.985] [5255:5273] [TOO] PASE establishment successful
[1770371852.985] [5255:5273] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770371852.985] [5255:5273] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770371852.985] [5255:5273] [CTL] Sending read requests for commissioning information
[1770371852.985] [5255:5273] [DMG] SendReadRequest ReadClient[0xffff98011020]: Sending Read Request
[1770371852.986] [5255:5273] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770371852.986] [5255:5273] [EM] <<< [E:33031i S:39568 M:258242100] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770371852.988] [5255:5273] [DMG] MoveToState ReadClient[0xffff98011020]: Moving to [AwaitingIn]
[1770371852.988] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 32792
[1770371853.371] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371853.568] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371853.568] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371853.860] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371853.860] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371853.861] [5255:5273] [EM] >>> [E:33031i S:39568 M:7332067] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:257)
[1770371853.861] [5255:5273] [EM] Found matching exchange: 33031i, Delegate: 0xffff98011030
[1770371853.861] [5255:5273] [DMG] ReportDataMessage =
[1770371853.861] [5255:5273] [DMG] {
[1770371853.861] [5255:5273] [DMG]      AttributeReportIBs =
[1770371853.862] [5255:5273] [DMG]      [
[1770371853.862] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.862] [5255:5273] [DMG]              {
[1770371853.862] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.862] [5255:5273] [DMG]                      {
[1770371853.862] [5255:5273] [DMG]                              DataVersion = 0x9b300a04,
[1770371853.862] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.862] [5255:5273] [DMG]                              {
[1770371853.862] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.863] [5255:5273] [DMG]                                      Cluster = 0x31,
[1770371853.863] [5255:5273] [DMG]                                      Attribute = 0x0000_FFFC,
[1770371853.863] [5255:5273] [DMG]                              }
[1770371853.863] [5255:5273] [DMG]
[1770371853.863] [5255:5273] [DMG]                              Data = 2 (unsigned),
[1770371853.863] [5255:5273] [DMG]                      },
[1770371853.863] [5255:5273] [DMG]
[1770371853.864] [5255:5273] [DMG]              },
[1770371853.864] [5255:5273] [DMG]
[1770371853.864] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.864] [5255:5273] [DMG]              {
[1770371853.864] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.864] [5255:5273] [DMG]                      {
[1770371853.864] [5255:5273] [DMG]                              DataVersion = 0x9adb653a,
[1770371853.864] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.865] [5255:5273] [DMG]                              {
[1770371853.865] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.865] [5255:5273] [DMG]                                      Cluster = 0x28,
[1770371853.865] [5255:5273] [DMG]                                      Attribute = 0x0000_0004,
[1770371853.865] [5255:5273] [DMG]                              }
[1770371853.865] [5255:5273] [DMG]
[1770371853.865] [5255:5273] [DMG]                              Data = 32784 (unsigned),
[1770371853.866] [5255:5273] [DMG]                      },
[1770371853.866] [5255:5273] [DMG]
[1770371853.866] [5255:5273] [DMG]              },
[1770371853.866] [5255:5273] [DMG]
[1770371853.866] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.866] [5255:5273] [DMG]              {
[1770371853.866] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.867] [5255:5273] [DMG]                      {
[1770371853.867] [5255:5273] [DMG]                              DataVersion = 0x9adb653a,
[1770371853.867] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.867] [5255:5273] [DMG]                              {
[1770371853.867] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.867] [5255:5273] [DMG]                                      Cluster = 0x28,
[1770371853.867] [5255:5273] [DMG]                                      Attribute = 0x0000_0002,
[1770371853.867] [5255:5273] [DMG]                              }
[1770371853.867] [5255:5273] [DMG]
[1770371853.868] [5255:5273] [DMG]                              Data = 65521 (unsigned),
[1770371853.868] [5255:5273] [DMG]                      },
[1770371853.868] [5255:5273] [DMG]
[1770371853.868] [5255:5273] [DMG]              },
[1770371853.868] [5255:5273] [DMG]
[1770371853.868] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.868] [5255:5273] [DMG]              {
[1770371853.868] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.868] [5255:5273] [DMG]                      {
[1770371853.868] [5255:5273] [DMG]                              DataVersion = 0x3324ba79,
[1770371853.868] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.868] [5255:5273] [DMG]                              {
[1770371853.868] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.869] [5255:5273] [DMG]                                      Cluster = 0x30,
[1770371853.869] [5255:5273] [DMG]                                      Attribute = 0x0000_0003,
[1770371853.869] [5255:5273] [DMG]                              }
[1770371853.869] [5255:5273] [DMG]
[1770371853.869] [5255:5273] [DMG]                              Data = 0 (unsigned),
[1770371853.869] [5255:5273] [DMG]                      },
[1770371853.869] [5255:5273] [DMG]
[1770371853.869] [5255:5273] [DMG]              },
[1770371853.869] [5255:5273] [DMG]
[1770371853.869] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.870] [5255:5273] [DMG]              {
[1770371853.870] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.870] [5255:5273] [DMG]                      {
[1770371853.870] [5255:5273] [DMG]                              DataVersion = 0x3324ba79,
[1770371853.870] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.870] [5255:5273] [DMG]                              {
[1770371853.870] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.870] [5255:5273] [DMG]                                      Cluster = 0x30,
[1770371853.870] [5255:5273] [DMG]                                      Attribute = 0x0000_0002,
[1770371853.870] [5255:5273] [DMG]                              }
[1770371853.870] [5255:5273] [DMG]
[1770371853.870] [5255:5273] [DMG]                              Data = 0 (unsigned),
[1770371853.870] [5255:5273] [DMG]                      },
[1770371853.870] [5255:5273] [DMG]
[1770371853.870] [5255:5273] [DMG]              },
[1770371853.870] [5255:5273] [DMG]
[1770371853.871] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.871] [5255:5273] [DMG]              {
[1770371853.871] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.871] [5255:5273] [DMG]                      {
[1770371853.871] [5255:5273] [DMG]                              DataVersion = 0x3324ba79,
[1770371853.871] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.871] [5255:5273] [DMG]                              {
[1770371853.871] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.871] [5255:5273] [DMG]                                      Cluster = 0x30,
[1770371853.871] [5255:5273] [DMG]                                      Attribute = 0x0000_0001,
[1770371853.871] [5255:5273] [DMG]                              }
[1770371853.871] [5255:5273] [DMG]
[1770371853.871] [5255:5273] [DMG]                              Data =
[1770371853.871] [5255:5273] [DMG]                              {
[1770371853.871] [5255:5273] [DMG]                                      0x0 = 60 (unsigned),
[1770371853.872] [5255:5273] [DMG]                                      0x1 = 900 (unsigned),
[1770371853.872] [5255:5273] [DMG]                              },
[1770371853.872] [5255:5273] [DMG]                      },
[1770371853.872] [5255:5273] [DMG]
[1770371853.872] [5255:5273] [DMG]              },
[1770371853.872] [5255:5273] [DMG]
[1770371853.872] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.872] [5255:5273] [DMG]              {
[1770371853.872] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.872] [5255:5273] [DMG]                      {
[1770371853.872] [5255:5273] [DMG]                              DataVersion = 0x3324ba79,
[1770371853.872] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.872] [5255:5273] [DMG]                              {
[1770371853.872] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.873] [5255:5273] [DMG]                                      Cluster = 0x30,
[1770371853.873] [5255:5273] [DMG]                                      Attribute = 0x0000_0000,
[1770371853.873] [5255:5273] [DMG]                              }
[1770371853.873] [5255:5273] [DMG]
[1770371853.873] [5255:5273] [DMG]                              Data = 0 (unsigned),
[1770371853.873] [5255:5273] [DMG]                      },
[1770371853.873] [5255:5273] [DMG]
[1770371853.873] [5255:5273] [DMG]              },
[1770371853.873] [5255:5273] [DMG]
[1770371853.873] [5255:5273] [DMG]              AttributeReportIB =
[1770371853.873] [5255:5273] [DMG]              {
[1770371853.873] [5255:5273] [DMG]                      AttributeDataIB =
[1770371853.873] [5255:5273] [DMG]                      {
[1770371853.873] [5255:5273] [DMG]                              DataVersion = 0x3324ba79,
[1770371853.873] [5255:5273] [DMG]                              AttributePathIB =
[1770371853.874] [5255:5273] [DMG]                              {
[1770371853.874] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371853.874] [5255:5273] [DMG]                                      Cluster = 0x30,
[1770371853.874] [5255:5273] [DMG]                                      Attribute = 0x0000_0004,
[1770371853.874] [5255:5273] [DMG]                              }
[1770371853.874] [5255:5273] [DMG]
[1770371853.874] [5255:5273] [DMG]                              Data = true,
[1770371853.874] [5255:5273] [DMG]                      },
[1770371853.874] [5255:5273] [DMG]
[1770371853.874] [5255:5273] [DMG]              },
[1770371853.874] [5255:5273] [DMG]
[1770371853.874] [5255:5273] [DMG]      ],
[1770371853.874] [5255:5273] [DMG]
[1770371853.874] [5255:5273] [DMG]      SuppressResponse = true,
[1770371853.875] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371853.875] [5255:5273] [DMG] }
[1770371853.876] [5255:5273] [DMG] SendReadRequest ReadClient[0xffff98011020]: Sending Read Request
[1770371853.877] [5255:5273] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770371853.877] [5255:5273] [EM] <<< [E:33032i S:39568 M:258242101] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770371853.878] [5255:5273] [DMG] MoveToState ReadClient[0xffff98011020]: Moving to [AwaitingIn]
[1770371854.248] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371854.444] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371854.444] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371854.445] [5255:5273] [EM] >>> [E:33032i S:39568 M:7332068] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:191)
[1770371854.445] [5255:5273] [EM] Found matching exchange: 33032i, Delegate: 0xffff98011030
[1770371854.445] [5255:5273] [DMG] ReportDataMessage =
[1770371854.445] [5255:5273] [DMG] {
[1770371854.445] [5255:5273] [DMG]      AttributeReportIBs =
[1770371854.445] [5255:5273] [DMG]      [
[1770371854.445] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.445] [5255:5273] [DMG]              {
[1770371854.445] [5255:5273] [DMG]                      AttributeDataIB =
[1770371854.446] [5255:5273] [DMG]                      {
[1770371854.446] [5255:5273] [DMG]                              DataVersion = 0x9614dc20,
[1770371854.446] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.446] [5255:5273] [DMG]                              {
[1770371854.446] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.446] [5255:5273] [DMG]                                      Cluster = 0x46,
[1770371854.446] [5255:5273] [DMG]                                      Attribute = 0x0000_0002,
[1770371854.446] [5255:5273] [DMG]                              }
[1770371854.446] [5255:5273] [DMG]
[1770371854.447] [5255:5273] [DMG]                              Data = 0 (unsigned),
[1770371854.447] [5255:5273] [DMG]                      },
[1770371854.447] [5255:5273] [DMG]
[1770371854.447] [5255:5273] [DMG]              },
[1770371854.447] [5255:5273] [DMG]
[1770371854.447] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.447] [5255:5273] [DMG]              {
[1770371854.447] [5255:5273] [DMG]                      AttributeDataIB =
[1770371854.447] [5255:5273] [DMG]                      {
[1770371854.448] [5255:5273] [DMG]                              DataVersion = 0x9614dc20,
[1770371854.448] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.448] [5255:5273] [DMG]                              {
[1770371854.448] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.448] [5255:5273] [DMG]                                      Cluster = 0x46,
[1770371854.448] [5255:5273] [DMG]                                      Attribute = 0x0000_0001,
[1770371854.448] [5255:5273] [DMG]                              }
[1770371854.448] [5255:5273] [DMG]
[1770371854.449] [5255:5273] [DMG]                              Data = 0 (unsigned),
[1770371854.449] [5255:5273] [DMG]                      },
[1770371854.449] [5255:5273] [DMG]
[1770371854.449] [5255:5273] [DMG]              },
[1770371854.449] [5255:5273] [DMG]
[1770371854.449] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.449] [5255:5273] [DMG]              {
[1770371854.449] [5255:5273] [DMG]                      AttributeDataIB =
[1770371854.449] [5255:5273] [DMG]                      {
[1770371854.449] [5255:5273] [DMG]                              DataVersion = 0x9614dc20,
[1770371854.450] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.450] [5255:5273] [DMG]                              {
[1770371854.450] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.450] [5255:5273] [DMG]                                      Cluster = 0x46,
[1770371854.450] [5255:5273] [DMG]                                      Attribute = 0x0000_0000,
[1770371854.450] [5255:5273] [DMG]                              }
[1770371854.450] [5255:5273] [DMG]
[1770371854.450] [5255:5273] [DMG]                              Data = 600 (unsigned),
[1770371854.450] [5255:5273] [DMG]                      },
[1770371854.451] [5255:5273] [DMG]
[1770371854.451] [5255:5273] [DMG]              },
[1770371854.451] [5255:5273] [DMG]
[1770371854.451] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.451] [5255:5273] [DMG]              {
[1770371854.451] [5255:5273] [DMG]                      AttributeStatusIB =
[1770371854.451] [5255:5273] [DMG]                      {
[1770371854.451] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.451] [5255:5273] [DMG]                              {
[1770371854.452] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.452] [5255:5273] [DMG]                                      Cluster = 0x46,
[1770371854.452] [5255:5273] [DMG]                                      Attribute = 0x0000_0007,
[1770371854.452] [5255:5273] [DMG]                              }
[1770371854.452] [5255:5273] [DMG]
[1770371854.452] [5255:5273] [DMG]                              StatusIB =
[1770371854.452] [5255:5273] [DMG]                              {
[1770371854.452] [5255:5273] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770371854.452] [5255:5273] [DMG]                              },
[1770371854.452] [5255:5273] [DMG]
[1770371854.452] [5255:5273] [DMG]                      },
[1770371854.452] [5255:5273] [DMG]
[1770371854.452] [5255:5273] [DMG]              },
[1770371854.452] [5255:5273] [DMG]
[1770371854.453] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.453] [5255:5273] [DMG]              {
[1770371854.453] [5255:5273] [DMG]                      AttributeStatusIB =
[1770371854.453] [5255:5273] [DMG]                      {
[1770371854.453] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.453] [5255:5273] [DMG]                              {
[1770371854.453] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.453] [5255:5273] [DMG]                                      Cluster = 0x46,
[1770371854.453] [5255:5273] [DMG]                                      Attribute = 0x0000_0006,
[1770371854.453] [5255:5273] [DMG]                              }
[1770371854.453] [5255:5273] [DMG]
[1770371854.453] [5255:5273] [DMG]                              StatusIB =
[1770371854.453] [5255:5273] [DMG]                              {
[1770371854.453] [5255:5273] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770371854.453] [5255:5273] [DMG]                              },
[1770371854.454] [5255:5273] [DMG]
[1770371854.454] [5255:5273] [DMG]                      },
[1770371854.454] [5255:5273] [DMG]
[1770371854.454] [5255:5273] [DMG]              },
[1770371854.454] [5255:5273] [DMG]
[1770371854.454] [5255:5273] [DMG]              AttributeReportIB =
[1770371854.454] [5255:5273] [DMG]              {
[1770371854.454] [5255:5273] [DMG]                      AttributeDataIB =
[1770371854.454] [5255:5273] [DMG]                      {
[1770371854.454] [5255:5273] [DMG]                              DataVersion = 0x9b300a04,
[1770371854.454] [5255:5273] [DMG]                              AttributePathIB =
[1770371854.454] [5255:5273] [DMG]                              {
[1770371854.454] [5255:5273] [DMG]                                      Endpoint = 0x0,
[1770371854.454] [5255:5273] [DMG]                                      Cluster = 0x31,
[1770371854.455] [5255:5273] [DMG]                                      Attribute = 0x0000_0003,
[1770371854.455] [5255:5273] [DMG]                              }
[1770371854.455] [5255:5273] [DMG]
[1770371854.455] [5255:5273] [DMG]                              Data = 20 (unsigned),
[1770371854.455] [5255:5273] [DMG]                      },
[1770371854.455] [5255:5273] [DMG]
[1770371854.455] [5255:5273] [DMG]              },
[1770371854.455] [5255:5273] [DMG]
[1770371854.455] [5255:5273] [DMG]      ],
[1770371854.455] [5255:5273] [DMG]
[1770371854.455] [5255:5273] [DMG]      SuppressResponse = true,
[1770371854.455] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371854.455] [5255:5273] [DMG] }
[1770371854.457] [5255:5273] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1770371854.457] [5255:5273] [SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010
[1770371854.457] [5255:5273] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1770371854.457] [5255:5273] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1770371854.457] [5255:5273] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1770371854.457] [5255:5273] [CTL] Performing next commissioning step 'ArmFailSafe'
[1770371854.457] [5255:5273] [CTL] Arming failsafe (60 seconds)
[1770371854.457] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371854.458] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371854.458] [5255:5273] [EM] <<< [E:33033i S:39568 M:258242102] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770371854.459] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371854.638] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371854.641] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371854.642] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371854.642] [5255:5273] [EM] >>> [E:33033i S:39568 M:7332069] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770371854.642] [5255:5273] [EM] Found matching exchange: 33033i, Delegate: 0xffff98008ae8
[1770371854.642] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371854.643] [5255:5273] [DMG] InvokeResponseMessage =
[1770371854.643] [5255:5273] [DMG] {
[1770371854.643] [5255:5273] [DMG]      suppressResponse = false,
[1770371854.643] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371854.643] [5255:5273] [DMG]      [
[1770371854.643] [5255:5273] [DMG]              InvokeResponseIB =
[1770371854.643] [5255:5273] [DMG]              {
[1770371854.644] [5255:5273] [DMG]                      CommandDataIB =
[1770371854.644] [5255:5273] [DMG]                      {
[1770371854.644] [5255:5273] [DMG]                              CommandPathIB =
[1770371854.644] [5255:5273] [DMG]                              {
[1770371854.644] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371854.644] [5255:5273] [DMG]                                      ClusterId = 0x30,
[1770371854.644] [5255:5273] [DMG]                                      CommandId = 0x1,
[1770371854.645] [5255:5273] [DMG]                              },
[1770371854.645] [5255:5273] [DMG]
[1770371854.645] [5255:5273] [DMG]                              CommandFields =
[1770371854.645] [5255:5273] [DMG]                              {
[1770371854.645] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371854.646] [5255:5273] [DMG]                                      0x1 = "" (0 chars),
[1770371854.646] [5255:5273] [DMG]                              },
[1770371854.646] [5255:5273] [DMG]                      },
[1770371854.646] [5255:5273] [DMG]
[1770371854.646] [5255:5273] [DMG]              },
[1770371854.646] [5255:5273] [DMG]
[1770371854.647] [5255:5273] [DMG]      ],
[1770371854.647] [5255:5273] [DMG]
[1770371854.647] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371854.647] [5255:5273] [DMG] },
[1770371854.647] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770371854.648] [5255:5273] [CTL] Received ArmFailSafe response errorCode=0
[1770371854.648] [5255:5273] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1770371854.648] [5255:5273] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1770371854.648] [5255:5273] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1770371854.648] [5255:5273] [CTL] Setting Regulatory Config
[1770371854.648] [5255:5273] [CTL] Device does not support configurable regulatory location
[1770371854.648] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371854.649] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371854.649] [5255:5273] [EM] <<< [E:33034i S:39568 M:258242103] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1770371854.650] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371854.650] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371854.931] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371855.225] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371855.225] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371855.226] [5255:5273] [EM] >>> [E:33034i S:39568 M:7332070] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770371855.226] [5255:5273] [EM] Found matching exchange: 33034i, Delegate: 0xffff9800ad28
[1770371855.226] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371855.226] [5255:5273] [DMG] InvokeResponseMessage =
[1770371855.226] [5255:5273] [DMG] {
[1770371855.226] [5255:5273] [DMG]      suppressResponse = false,
[1770371855.227] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371855.227] [5255:5273] [DMG]      [
[1770371855.227] [5255:5273] [DMG]              InvokeResponseIB =
[1770371855.227] [5255:5273] [DMG]              {
[1770371855.227] [5255:5273] [DMG]                      CommandDataIB =
[1770371855.227] [5255:5273] [DMG]                      {
[1770371855.227] [5255:5273] [DMG]                              CommandPathIB =
[1770371855.228] [5255:5273] [DMG]                              {
[1770371855.228] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371855.228] [5255:5273] [DMG]                                      ClusterId = 0x30,
[1770371855.228] [5255:5273] [DMG]                                      CommandId = 0x3,
[1770371855.228] [5255:5273] [DMG]                              },
[1770371855.229] [5255:5273] [DMG]
[1770371855.229] [5255:5273] [DMG]                              CommandFields =
[1770371855.229] [5255:5273] [DMG]                              {
[1770371855.229] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371855.229] [5255:5273] [DMG]                                      0x1 = "" (0 chars),
[1770371855.230] [5255:5273] [DMG]                              },
[1770371855.230] [5255:5273] [DMG]                      },
[1770371855.230] [5255:5273] [DMG]
[1770371855.230] [5255:5273] [DMG]              },
[1770371855.230] [5255:5273] [DMG]
[1770371855.230] [5255:5273] [DMG]      ],
[1770371855.231] [5255:5273] [DMG]
[1770371855.231] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371855.231] [5255:5273] [DMG] },
[1770371855.231] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1770371855.232] [5255:5273] [CTL] Received SetRegulatoryConfig response errorCode=0
[1770371855.232] [5255:5273] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1770371855.232] [5255:5273] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1770371855.232] [5255:5273] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1770371855.232] [5255:5273] [CTL] Setting Terms and Conditions
[1770371855.232] [5255:5273] [CTL] Setting Terms and Conditions: Skipped
[1770371855.232] [5255:5273] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'
[1770371855.232] [5255:5273] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1770371855.232] [5255:5273] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770371855.232] [5255:5273] [CTL] Sending request for PAI certificate
[1770371855.232] [5255:5273] [CTL] Sending Certificate Chain request to 0xffff9800fcd0 device
[1770371855.233] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371855.233] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371855.233] [5255:5273] [EM] <<< [E:33035i S:39568 M:258242104] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770371855.234] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371855.235] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371855.515] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371855.617] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371855.617] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371856.104] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371856.105] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371856.298] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371856.298] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371856.299] [5255:5273] [EM] >>> [E:33035i S:39568 M:7332071] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[1770371856.299] [5255:5273] [EM] Found matching exchange: 33035i, Delegate: 0xffff98008ae8
[1770371856.299] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371856.299] [5255:5273] [DMG] InvokeResponseMessage =
[1770371856.299] [5255:5273] [DMG] {
[1770371856.299] [5255:5273] [DMG]      suppressResponse = false,
[1770371856.299] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371856.300] [5255:5273] [DMG]      [
[1770371856.300] [5255:5273] [DMG]              InvokeResponseIB =
[1770371856.300] [5255:5273] [DMG]              {
[1770371856.300] [5255:5273] [DMG]                      CommandDataIB =
[1770371856.300] [5255:5273] [DMG]                      {
[1770371856.300] [5255:5273] [DMG]                              CommandPathIB =
[1770371856.300] [5255:5273] [DMG]                              {
[1770371856.300] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371856.300] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371856.300] [5255:5273] [DMG]                                      CommandId = 0x3,
[1770371856.301] [5255:5273] [DMG]                              },
[1770371856.301] [5255:5273] [DMG]
[1770371856.301] [5255:5273] [DMG]                              CommandFields =
[1770371856.301] [5255:5273] [DMG]                              {
[1770371856.301] [5255:5273] [DMG]                                      0x0 = [
[1770371856.301] [5255:5273] [DMG]                                                      0x30, 0x82, 0x01, 0xcb, 0x30, 0x82, 0x01, 0x71, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x56, 0xad, 0x82, 0x22, 0xad, 0x94, 0x5b, 0x64, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x30, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x0f, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x54, 0x65, 0x73, 0x74, 0x20, 0x50, 0x41, 0x41, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x41, 0x9a, 0x93, 0x15, 0xc2, 0x17, 0x3e, 0x0c, 0x8c, 0x87, 0x6d, 0x03, 0xcc, 0xfc, 0x94, 0x48, 0x52, 0x64, 0x7f, 0x7f, 0xec, 0x5e, 0x50, 0x82, 0xf4, 0x05, 0x99, 0x28, 0xec, 0xa8, 0x94, 0xc5, 0x94, 0x15, 0x13, 0x09, 0xac, 0x63, 0x1e, 0x4c, 0xb0, 0x33, 0x92, 0xaf, 0x68, 0x4b, 0x0b, 0xaf, 0xb7, 0xe6, 0x5b, 0x3b, 0x81, 0x62, 0xc2, 0xf5, 0x2b, 0xf9, 0x31, 0xb8, 0xe7, 0x7a, 0xaa, 0x82, 0xa3, 0x66, 0x30, 0x64, 0x30, 0x12, 0x06, 0x03, 0x55, 0x1d, 0x
[1770371856.302] [5255:5273] [DMG]                                      ] (463 bytes)
[1770371856.302] [5255:5273] [DMG]                              },
[1770371856.302] [5255:5273] [DMG]                      },
[1770371856.302] [5255:5273] [DMG]
[1770371856.302] [5255:5273] [DMG]              },
[1770371856.302] [5255:5273] [DMG]
[1770371856.302] [5255:5273] [DMG]      ],
[1770371856.302] [5255:5273] [DMG]
[1770371856.302] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371856.302] [5255:5273] [DMG] },
[1770371856.303] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770371856.303] [5255:5273] [CTL] Received certificate chain from the device
[1770371856.303] [5255:5273] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1770371856.303] [5255:5273] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1770371856.303] [5255:5273] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1770371856.303] [5255:5273] [CTL] Sending request for DAC certificate
[1770371856.303] [5255:5273] [CTL] Sending Certificate Chain request to 0xffff9800fcd0 device
[1770371856.303] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371856.303] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371856.304] [5255:5273] [EM] <<< [E:33036i S:39568 M:258242105] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770371856.305] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371856.305] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371856.686] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371857.076] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371857.077] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371857.470] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371857.470] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371857.663] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371857.664] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371857.664] [5255:5273] [EM] >>> [E:33036i S:39568 M:7332072] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[1770371857.664] [5255:5273] [EM] Found matching exchange: 33036i, Delegate: 0xffff9800ad28
[1770371857.665] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371857.665] [5255:5273] [DMG] InvokeResponseMessage =
[1770371857.665] [5255:5273] [DMG] {
[1770371857.665] [5255:5273] [DMG]      suppressResponse = false,
[1770371857.665] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371857.665] [5255:5273] [DMG]      [
[1770371857.665] [5255:5273] [DMG]              InvokeResponseIB =
[1770371857.665] [5255:5273] [DMG]              {
[1770371857.666] [5255:5273] [DMG]                      CommandDataIB =
[1770371857.666] [5255:5273] [DMG]                      {
[1770371857.666] [5255:5273] [DMG]                              CommandPathIB =
[1770371857.666] [5255:5273] [DMG]                              {
[1770371857.666] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371857.666] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371857.666] [5255:5273] [DMG]                                      CommandId = 0x3,
[1770371857.667] [5255:5273] [DMG]                              },
[1770371857.667] [5255:5273] [DMG]
[1770371857.667] [5255:5273] [DMG]                              CommandFields =
[1770371857.667] [5255:5273] [DMG]                              {
[1770371857.667] [5255:5273] [DMG]                                      0x0 = [
[1770371857.668] [5255:5273] [DMG]                                                      0x30, 0x82, 0x01, 0xe7, 0x30, 0x82, 0x01, 0x8e, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x46, 0x7f, 0x57, 0x62, 0xc8, 0xdc, 0x90, 0xd5, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x33, 0x33, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x53, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x44, 0x41, 0x43, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x2f, 0x30, 0x78, 0x38, 0x30, 0x31, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x31, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x39, 0xef, 0x6c, 0x9d, 0x9c, 0x99, 0x7b, 0xa2, 0xc7, 0x31, 0x9a, 0x4c, 0x73, 0xc9, 0xbf, 0x47, 0xdb, 0xcd, 0xbc, 0x42, 0xc5, 0x41, 0x3e, 0xec, 0x14, 0x52, 0x75, 0xb8, 0x8f, 0xc1, 0x1a, 0xb1, 0xad, 0x0b, 0xc3, 0x3e, 0xf1, 0x4c, 0x27, 0x
[1770371857.668] [5255:5273] [DMG]                                      ] (491 bytes)
[1770371857.668] [5255:5273] [DMG]                              },
[1770371857.668] [5255:5273] [DMG]                      },
[1770371857.668] [5255:5273] [DMG]
[1770371857.669] [5255:5273] [DMG]              },
[1770371857.669] [5255:5273] [DMG]
[1770371857.669] [5255:5273] [DMG]      ],
[1770371857.669] [5255:5273] [DMG]
[1770371857.669] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371857.669] [5255:5273] [DMG] },
[1770371857.670] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770371857.670] [5255:5273] [CTL] Received certificate chain from the device
[1770371857.670] [5255:5273] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1770371857.670] [5255:5273] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1770371857.670] [5255:5273] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1770371857.670] [5255:5273] [CTL] Sending Attestation Request to the device.
[1770371857.670] [5255:5273] [CTL] Sending Attestation request to 0xffff9800fcd0 device
[1770371857.670] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371857.671] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371857.671] [5255:5273] [EM] <<< [E:33037i S:39568 M:258242106] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770371857.672] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371857.672] [5255:5273] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770371857.672] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371857.856] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371857.957] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371857.958] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371858.250] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371858.250] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371858.640] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371858.640] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371858.641] [5255:5273] [EM] >>> [E:33037i S:39568 M:7332073] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[1770371858.641] [5255:5273] [EM] Found matching exchange: 33037i, Delegate: 0xffff98008ae8
[1770371858.641] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371858.641] [5255:5273] [DMG] InvokeResponseMessage =
[1770371858.642] [5255:5273] [DMG] {
[1770371858.642] [5255:5273] [DMG]      suppressResponse = false,
[1770371858.642] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371858.642] [5255:5273] [DMG]      [
[1770371858.642] [5255:5273] [DMG]              InvokeResponseIB =
[1770371858.642] [5255:5273] [DMG]              {
[1770371858.642] [5255:5273] [DMG]                      CommandDataIB =
[1770371858.642] [5255:5273] [DMG]                      {
[1770371858.643] [5255:5273] [DMG]                              CommandPathIB =
[1770371858.643] [5255:5273] [DMG]                              {
[1770371858.643] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371858.643] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371858.643] [5255:5273] [DMG]                                      CommandId = 0x1,
[1770371858.643] [5255:5273] [DMG]                              },
[1770371858.643] [5255:5273] [DMG]
[1770371858.643] [5255:5273] [DMG]                              CommandFields =
[1770371858.644] [5255:5273] [DMG]                              {
[1770371858.644] [5255:5273] [DMG]                                      0x0 = [
[1770371858.644] [5255:5273] [DMG]                                                      0x15, 0x31, 0x01, 0x1b, 0x02, 0x30, 0x82, 0x02, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x02, 0x08, 0x30, 0x82, 0x02, 0x04, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x82, 0x01, 0x70, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x01, 0x61, 0x04, 0x82, 0x01, 0x5d, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0xf1, 0xff, 0x36, 0x02, 0x05, 0x00, 0x80, 0x05, 0x01, 0x80, 0x05, 0x02, 0x80, 0x05, 0x03, 0x80, 0x05, 0x04, 0x80, 0x05, 0x05, 0x80, 0x05, 0x06, 0x80, 0x05, 0x07, 0x80, 0x05, 0x08, 0x80, 0x05, 0x09, 0x80, 0x05, 0x0a, 0x80, 0x05, 0x0b, 0x80, 0x05, 0x0c, 0x80, 0x05, 0x0d, 0x80, 0x05, 0x0e, 0x80, 0x05, 0x0f, 0x80, 0x05, 0x10, 0x80, 0x05, 0x11, 0x80, 0x05, 0x12, 0x80, 0x05, 0x13, 0x80, 0x05, 0x14, 0x80, 0x05, 0x15, 0x80, 0x05, 0x16, 0x80, 0x05, 0x17, 0x80, 0x05, 0x18, 0x80, 0x05, 0x19, 0x80, 0x05, 0x1a, 0x80, 0x05, 0x1b, 0x80, 0x05, 0x1c, 0x80, 0x05, 0x1d, 0x80, 0x05, 0x1e, 0x80, 0x05, 0x1f, 0x80, 0x05, 0x20, 0x80, 0x05, 0x21, 0x80, 0x05, 0x22, 0x80, 0x05, 0x23, 0x80, 0x05, 0x24, 0x80, 0x05, 0x25, 0x80, 0x05, 0x26, 0x80, 0x05, 0x27, 0x80, 0x05, 0x28, 0x80, 0x05, 0x29, 0x80, 0x05, 0x2a, 0x80, 0x05, 0x2b, 0x80, 0x05, 0x2c, 0x80, 0x05, 0x2d, 0x80, 0x05, 0x2e, 0x80, 0x05, 0x2f, 0x80, 0x05, 0x30, 0x80, 0x05, 0x31, 0x80, 0x05, 0x32, 0x80, 0x05, 0x33, 0x80, 0x05, 0x34, 0x80, 0x05, 0x35, 0x80, 0x05, 0x36, 0x80, 0x05, 0x37, 0x80, 0x05, 0x38, 0x80, 0x05, 0x39, 0x80, 0x05, 0x3a, 0x80, 0x05, 0x3b, 0x80, 0x05, 0x3c, 0x80, 0x05, 0x3d, 0x80, 0x05, 0x3e, 0x80, 0x05, 0x3f, 0x80, 0x05, 0x40, 0x80, 0x05, 0x41, 0x80, 0x05, 0x42, 0x80, 0x05, 0x43, 0x80, 0x
[1770371858.644] [5255:5273] [DMG]                                      ] (583 bytes)
[1770371858.645] [5255:5273] [DMG]                                      0x1 = [
[1770371858.645] [5255:5273] [DMG]                                                      0x0e, 0x0e, 0xc2, 0x2b, 0xca, 0xa0, 0xc5, 0xa1, 0x1f, 0xfd, 0xdd, 0x49, 0x78, 0x34, 0xcd, 0x04, 0x7d, 0xeb, 0x0d, 0x57, 0x89, 0x04, 0x74, 0xe7, 0x77, 0x05, 0x2b, 0xef, 0x40, 0xc6, 0x5d, 0x46, 0xc0, 0xe9, 0xae, 0xb1, 0xb3, 0x29, 0x95, 0x33, 0x70, 0x5a, 0x5e, 0x99, 0xd5, 0xff, 0xbf, 0xd8, 0x58, 0xff, 0x8e, 0xa2, 0x76, 0x79, 0x9a, 0xec, 0xee, 0xbd, 0xd7, 0x38, 0xf8, 0xfc, 0xa1, 0x96,
[1770371858.645] [5255:5273] [DMG]                                      ] (64 bytes)
[1770371858.645] [5255:5273] [DMG]                              },
[1770371858.645] [5255:5273] [DMG]                      },
[1770371858.645] [5255:5273] [DMG]
[1770371858.645] [5255:5273] [DMG]              },
[1770371858.645] [5255:5273] [DMG]
[1770371858.645] [5255:5273] [DMG]      ],
[1770371858.645] [5255:5273] [DMG]
[1770371858.645] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371858.645] [5255:5273] [DMG] },
[1770371858.646] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1770371858.646] [5255:5273] [CTL] Received Attestation Information from the device
[1770371858.646] [5255:5273] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1770371858.646] [5255:5273] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[1770371858.646] [5255:5273] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1770371858.646] [5255:5273] [CTL] Performing next commissioning step 'AttestationVerification'
[1770371858.646] [5255:5273] [CTL] Verifying Device Attestation information received from the device
[1770371858.671] [5255:5273] [-] Device candidate DAC chain details:
[1770371858.671] [5255:5273] [-] --> DAC's VID: 0xFFF1, PID: 0x8010
[1770371858.671] [5255:5273] [-] ==== DAC certificate considered (491 bytes) ====
[1770371858.671] [5255:5273] [-] -----BEGIN CERTIFICATE-----
[1770371858.671] [5255:5273] [-] MIIB5zCCAY6gAwIBAgIIRn9XYsjckNUwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770371858.671] [5255:5273] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
[1770371858.671] [5255:5273] [-] RjEwIBcNMjIwMzMxMDAwMDAwWhgPOTk5OTEyMzEyMzU5NTlaMFMxJTAjBgNVBAMM
[1770371858.671] [5255:5273] [-] HE1hdHRlciBEZXYgREFDIDB4RkZGMS8weDgwMTAxFDASBgorBgEEAYKifAIBDARG
[1770371858.671] [5255:5273] [-] RkYxMRQwEgYKKwYBBAGConwCAgwEODAxMDBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770371858.671] [5255:5273] [-] A0IABDnvbJ2cmXuixzGaTHPJv0fbzbxCxUE+7BRSdbiPwRqxrQvDPvFMJ5QEQp8v
[1770371858.672] [5255:5273] [-] XucKBRty5se55zVO2vkqtP/4hC+jYDBeMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/
[1770371858.672] [5255:5273] [-] BAQDAgeAMB0GA1UdDgQWBBQy/CfR71NDovNk8Cz0cMtnR4DlqjAfBgNVHSMEGDAW
[1770371858.672] [5255:5273] [-] gBRjVA5H9kscONE4hKRi0WwZXY/7PDAKBggqhkjOPQQDAgNHADBEAiBvEbIFC9PS
[1770371858.672] [5255:5273] [-] 42wkYTAIbCIBsIz5nVp3sjqQBQD77wkTsgIgE2q2oLuL1PSt+AoSNM/vtn8K+3NV
[1770371858.672] [5255:5273] [-] 8dykctoWrEo2ZOU=
[1770371858.672] [5255:5273] [-] -----END CERTIFICATE-----
[1770371858.674] [5255:5273] [-] --> DAC certificate SKID: 32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
[1770371858.677] [5255:5273] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770371858.677] [5255:5273] [-] ==== PAI certificate considered (463 bytes) ====
[1770371858.677] [5255:5273] [-] -----BEGIN CERTIFICATE-----
[1770371858.677] [5255:5273] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770371858.677] [5255:5273] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMjAyMDUw
[1770371858.677] [5255:5273] [-] MDAwMDBaGA85OTk5MTIzMTIzNTk1OVowPTElMCMGA1UEAwwcTWF0dGVyIERldiBQ
[1770371858.677] [5255:5273] [-] QUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZGRjEwWTATBgcqhkjO
[1770371858.677] [5255:5273] [-] PQIBBggqhkjOPQMBBwNCAARBmpMVwhc+DIyHbQPM/JRIUmR/f+xeUIL0BZko7KiU
[1770371858.677] [5255:5273] [-] xZQVEwmsYx5MsDOSr2hLC6+35ls7gWLC9Sv5MbjneqqCo2YwZDASBgNVHRMBAf8E
[1770371858.677] [5255:5273] [-] CDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUY1QOR/ZLHDjROISk
[1770371858.677] [5255:5273] [-] YtFsGV2P+zwwHwYDVR0jBBgwFoAUav0idx9RH+y/FkGXZxDc3DGhcX4wCgYIKoZI
[1770371858.677] [5255:5273] [-] zj0EAwIDSAAwRQIhALLvJ/Sa6bUPuR7qyUxNC9u415KcbLiPrOUpNo0SBUwMAiBl
[1770371858.677] [5255:5273] [-] Xckrhr2QmIKmxiF3uCXX0F7b58Ivn+pxIg5+pwP4kQ==
[1770371858.677] [5255:5273] [-] -----END CERTIFICATE-----
[1770371858.680] [5255:5273] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770371858.682] [5255:5273] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770371858.693] [5255:5273] [-] ==== PAA certificate considered (449 bytes) ====
[1770371858.693] [5255:5273] [-] -----BEGIN CERTIFICATE-----
[1770371858.693] [5255:5273] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770371858.693] [5255:5273] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMTA2Mjgx
[1770371858.693] [5255:5273] [-] NDIzNDNaGA85OTk5MTIzMTIzNTk1OVowMDEYMBYGA1UEAwwPTWF0dGVyIFRlc3Qg
[1770371858.693] [5255:5273] [-] UEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770371858.693] [5255:5273] [-] A0IABLbLY3KIfyko9brIGqnZOuJDHK2p154kL2UXfvnO2TKijs0Duq9qj8oYShpQ
[1770371858.693] [5255:5273] [-] NUKWDUU/MD8fGUIddR6Pjxqam3WjZjBkMBIGA1UdEwEB/wQIMAYBAf8CAQEwDgYD
[1770371858.693] [5255:5273] [-] VR0PAQH/BAQDAgEGMB0GA1UdDgQWBBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAfBgNV
[1770371858.693] [5255:5273] [-] HSMEGDAWgBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAKBggqhkjOPQQDAgNHADBEAiBQ
[1770371858.693] [5255:5273] [-] qoAC9NkyqaAFOPZTaK0P/8jvu8m+t9pWmDXPmqdRDgIgI7rI/g8j51RFtlM5CBpH
[1770371858.693] [5255:5273] [-] mUkpxyqvChVI1A0DTVFLJd4=
[1770371858.693] [5255:5273] [-] -----END CERTIFICATE-----
[1770371858.696] [5255:5273] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770371858.698] [5255:5273] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770371858.712] [5255:5273] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770371858.714] [5255:5273] [-] Device certification declaration details:
[1770371858.714] [5255:5273] [-] --> VID: 0xFFF1
[1770371858.714] [5255:5273] [-] --> Device type ID: 0x0000_0016
[1770371858.714] [5255:5273] [-] --> Certification type: 0 (Development and testing)
[1770371858.714] [5255:5273] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1770371858.714] [5255:5273] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1770371858.714] [5255:5273] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1770371858.714] [5255:5273] [CTL] Verifying the device's DAC chain revocation status
[1770371858.714] [5255:5273] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770371858.714] [5255:5273] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1770371858.714] [5255:5273] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1770371858.714] [5255:5273] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1770371858.715] [5255:5273] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1770371858.715] [5255:5273] [CTL] Sending CSR request to 0xffff9800fcd0 device
[1770371858.715] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371858.715] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371858.715] [5255:5273] [EM] <<< [E:33038i S:39568 M:258242107] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770371858.716] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371858.716] [5255:5273] [CTL] Sent CSR request, waiting for the CSR
[1770371858.716] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371858.928] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371859.223] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371859.224] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371859.515] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371859.516] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371859.516] [5255:5273] [EM] >>> [E:33038i S:39568 M:7332074] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1770371859.516] [5255:5273] [EM] Found matching exchange: 33038i, Delegate: 0xffff9800ad28
[1770371859.516] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371859.516] [5255:5273] [DMG] InvokeResponseMessage =
[1770371859.516] [5255:5273] [DMG] {
[1770371859.516] [5255:5273] [DMG]      suppressResponse = false,
[1770371859.517] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371859.517] [5255:5273] [DMG]      [
[1770371859.517] [5255:5273] [DMG]              InvokeResponseIB =
[1770371859.517] [5255:5273] [DMG]              {
[1770371859.517] [5255:5273] [DMG]                      CommandDataIB =
[1770371859.517] [5255:5273] [DMG]                      {
[1770371859.517] [5255:5273] [DMG]                              CommandPathIB =
[1770371859.517] [5255:5273] [DMG]                              {
[1770371859.518] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371859.518] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371859.518] [5255:5273] [DMG]                                      CommandId = 0x5,
[1770371859.518] [5255:5273] [DMG]                              },
[1770371859.518] [5255:5273] [DMG]
[1770371859.518] [5255:5273] [DMG]                              CommandFields =
[1770371859.519] [5255:5273] [DMG]                              {
[1770371859.519] [5255:5273] [DMG]                                      0x0 = [
[1770371859.519] [5255:5273] [DMG]                                                      0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xb9, 0xae, 0xd2, 0x46, 0x2d, 0x57, 0x42, 0xc4, 0x95, 0xe7, 0x4c, 0x7f, 0xe7, 0x76, 0x7b, 0x70, 0x38, 0x4f, 0x81, 0xed, 0x3f, 0xe3, 0x15, 0xc9, 0x6d, 0x71, 0xf6, 0x4f, 0xc7, 0xf0, 0x2f, 0x04, 0xb3, 0x1d, 0x5b, 0x08, 0x5f, 0x6f, 0xf1, 0x77, 0xe2, 0x44, 0xf6, 0x60, 0xb9, 0x08, 0xe2, 0xd7, 0xd0, 0xda, 0x97, 0xd4, 0x3c, 0xa2, 0xaf, 0xcb, 0x29, 0xf2, 0x8d, 0x38, 0xbd, 0x52, 0xda, 0xa4, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x21, 0x00, 0xc8, 0x41, 0xbf, 0xd8, 0xcf, 0x36, 0x11, 0xfe, 0x39, 0xff, 0x6f, 0x24, 0xdd, 0x37, 0x2f, 0x55, 0xa9, 0x8d, 0xe7, 0x08, 0x90, 0x84, 0xc4, 0xaa, 0x71, 0xd2, 0x6c, 0xd0, 0xf4, 0x0f, 0x58, 0x19, 0x02, 0x20, 0x0d, 0x0e, 0xe7, 0xa0, 0xea, 0x32, 0x92, 0xb3, 0x1f, 0xc3, 0x04, 0xd9, 0x4f, 0xd9, 0x2a, 0x39, 0xa8, 0x2f, 0x63, 0x7b, 0x9b, 0x18, 0x00, 0x45, 0x04, 0x93, 0x2e, 0x41, 0xa6, 0xa3, 0x8f, 0x4e, 0x30, 0x02, 0x20, 0x96, 0x7d, 0xc7, 0xd1, 0x21, 0xd1, 0xb1, 0xdd, 0x56, 0xe2, 0x06, 0xf9, 0x00, 0x9d, 0xf3, 0x93, 0x79, 0xa9, 0x96, 0x28, 0xbf, 0x18, 0xd0, 0x17, 0xe3, 0x93, 0xe0, 0xe9, 0x33, 0xcf, 0xe9, 0x14, 0x18,
[1770371859.519] [5255:5273] [DMG]                                      ] (261 bytes)
[1770371859.520] [5255:5273] [DMG]                                      0x1 = [
[1770371859.520] [5255:5273] [DMG]                                                      0xaf, 0xe4, 0xd2, 0x2e, 0xb1, 0x8c, 0x55, 0x22, 0x95, 0xb1, 0x4a, 0x56, 0x9f, 0x3a, 0xce, 0x46, 0x53, 0x1c, 0xe6, 0x8c, 0x50, 0x65, 0x34, 0xd4, 0x63, 0x41, 0xd5, 0x97, 0x8c, 0x46, 0x5a, 0x9d, 0x3b, 0xc7, 0x6e, 0xcb, 0x56, 0x34, 0x9b, 0xe4, 0x47, 0x2b, 0xec, 0x12, 0xbc, 0x6c, 0x39, 0x27, 0x33, 0x7c, 0xd2, 0xeb, 0x3b, 0x09, 0x09, 0x1f, 0xa2, 0x6c, 0x95, 0x30, 0xcc, 0x88, 0x8c, 0x2a,
[1770371859.520] [5255:5273] [DMG]                                      ] (64 bytes)
[1770371859.520] [5255:5273] [DMG]                              },
[1770371859.520] [5255:5273] [DMG]                      },
[1770371859.520] [5255:5273] [DMG]
[1770371859.521] [5255:5273] [DMG]              },
[1770371859.521] [5255:5273] [DMG]
[1770371859.521] [5255:5273] [DMG]      ],
[1770371859.521] [5255:5273] [DMG]
[1770371859.521] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371859.521] [5255:5273] [DMG] },
[1770371859.522] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1770371859.522] [5255:5273] [CTL] Received certificate signing request from the device
[1770371859.522] [5255:5273] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1770371859.522] [5255:5273] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1770371859.522] [5255:5273] [CTL] Performing next commissioning step 'ValidateCSR'
[1770371859.530] [5255:5273] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1770371859.530] [5255:5273] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1770371859.530] [5255:5273] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1770371859.530] [5255:5273] [CTL] Getting certificate chain for the device from the issuer
[1770371859.537] [5255:5273] [CTL] Verifying Certificate Signing Request
[1770371859.541] [5255:5273] [CTL] Generating NOC
[1770371859.541] [5255:5273] [CTL] Providing certificate chain to the commissioner
[1770371859.542] [5255:5273] [CTL] Received callback from the CA for NOC Chain generation. Status src/controller/ExampleOperationalCredentialsIssuer.cpp:409: Success
[1770371859.542] [5255:5273] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1770371859.542] [5255:5273] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1770371859.542] [5255:5273] [CTL] Sending root certificate to the device
[1770371859.543] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371859.543] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371859.543] [5255:5273] [EM] <<< [E:33039i S:39568 M:258242108] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1770371859.544] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371859.544] [5255:5273] [CTL] Sent root certificate to the device
[1770371859.545] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371860.195] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371860.391] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371860.490] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371860.491] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371860.491] [5255:5273] [EM] >>> [E:33039i S:39568 M:7332075] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770371860.491] [5255:5273] [EM] Found matching exchange: 33039i, Delegate: 0xffff98008ae8
[1770371860.492] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371860.492] [5255:5273] [DMG] InvokeResponseMessage =
[1770371860.492] [5255:5273] [DMG] {
[1770371860.492] [5255:5273] [DMG]      suppressResponse = false,
[1770371860.492] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371860.492] [5255:5273] [DMG]      [
[1770371860.492] [5255:5273] [DMG]              InvokeResponseIB =
[1770371860.492] [5255:5273] [DMG]              {
[1770371860.493] [5255:5273] [DMG]                      CommandStatusIB =
[1770371860.493] [5255:5273] [DMG]                      {
[1770371860.493] [5255:5273] [DMG]                              CommandPathIB =
[1770371860.493] [5255:5273] [DMG]                              {
[1770371860.493] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371860.493] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371860.493] [5255:5273] [DMG]                                      CommandId = 0xb,
[1770371860.494] [5255:5273] [DMG]                              },
[1770371860.494] [5255:5273] [DMG]
[1770371860.494] [5255:5273] [DMG]                              StatusIB =
[1770371860.494] [5255:5273] [DMG]                              {
[1770371860.494] [5255:5273] [DMG]                                      status = 0x00 (SUCCESS),
[1770371860.494] [5255:5273] [DMG]                              },
[1770371860.494] [5255:5273] [DMG]
[1770371860.495] [5255:5273] [DMG]                      },
[1770371860.495] [5255:5273] [DMG]
[1770371860.495] [5255:5273] [DMG]              },
[1770371860.495] [5255:5273] [DMG]
[1770371860.495] [5255:5273] [DMG]      ],
[1770371860.495] [5255:5273] [DMG]
[1770371860.496] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371860.496] [5255:5273] [DMG] },
[1770371860.496] [5255:5273] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1770371860.496] [5255:5273] [CTL] Device confirmed that it has received the root certificate
[1770371860.496] [5255:5273] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1770371860.496] [5255:5273] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1770371860.496] [5255:5273] [CTL] Performing next commissioning step 'SendNOC'
[1770371860.497] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371860.497] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371860.497] [5255:5273] [EM] <<< [E:33040i S:39568 M:258242109] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1770371860.498] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371860.498] [5255:5273] [CTL] Sent operational certificate to the device
[1770371860.498] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371860.879] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371861.171] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371861.366] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371861.369] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371861.369] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371861.370] [5255:5273] [EM] >>> [E:33040i S:39568 M:7332076] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770371861.370] [5255:5273] [EM] Found matching exchange: 33040i, Delegate: 0xffff9800ad28
[1770371861.370] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371861.370] [5255:5273] [DMG] InvokeResponseMessage =
[1770371861.370] [5255:5273] [DMG] {
[1770371861.370] [5255:5273] [DMG]      suppressResponse = false,
[1770371861.371] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371861.371] [5255:5273] [DMG]      [
[1770371861.371] [5255:5273] [DMG]              InvokeResponseIB =
[1770371861.371] [5255:5273] [DMG]              {
[1770371861.371] [5255:5273] [DMG]                      CommandDataIB =
[1770371861.371] [5255:5273] [DMG]                      {
[1770371861.371] [5255:5273] [DMG]                              CommandPathIB =
[1770371861.372] [5255:5273] [DMG]                              {
[1770371861.372] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371861.372] [5255:5273] [DMG]                                      ClusterId = 0x3e,
[1770371861.372] [5255:5273] [DMG]                                      CommandId = 0x8,
[1770371861.372] [5255:5273] [DMG]                              },
[1770371861.372] [5255:5273] [DMG]
[1770371861.373] [5255:5273] [DMG]                              CommandFields =
[1770371861.373] [5255:5273] [DMG]                              {
[1770371861.373] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371861.373] [5255:5273] [DMG]                                      0x1 = 1 (unsigned),
[1770371861.373] [5255:5273] [DMG]                              },
[1770371861.373] [5255:5273] [DMG]                      },
[1770371861.373] [5255:5273] [DMG]
[1770371861.374] [5255:5273] [DMG]              },
[1770371861.374] [5255:5273] [DMG]
[1770371861.374] [5255:5273] [DMG]      ],
[1770371861.374] [5255:5273] [DMG]
[1770371861.374] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371861.374] [5255:5273] [DMG] },
[1770371861.374] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1770371861.375] [5255:5273] [CTL] Device returned status 0 on receiving the NOC
[1770371861.375] [5255:5273] [CTL] Operational credentials provisioned on device 0xffff9800fcd0
[1770371861.375] [5255:5273] [TOO] Secure Pairing Success
[1770371861.375] [5255:5273] [TOO] CASE establishment successful
[1770371861.375] [5255:5273] [CTL] Successfully finished commissioning step 'SendNOC'
[1770371861.375] [5255:5273] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1770371861.375] [5255:5273] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1770371861.375] [5255:5273] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1770371861.375] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371861.375] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371861.376] [5255:5273] [EM] <<< [E:33041i S:39568 M:258242110] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[1770371861.376] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371861.377] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371861.658] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371861.661] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371861.662] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371861.662] [5255:5273] [EM] >>> [E:33041i S:39568 M:7332077] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770371861.662] [5255:5273] [EM] Found matching exchange: 33041i, Delegate: 0xffff98008ae8
[1770371861.662] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371861.663] [5255:5273] [DMG] InvokeResponseMessage =
[1770371861.663] [5255:5273] [DMG] {
[1770371861.663] [5255:5273] [DMG]      suppressResponse = false,
[1770371861.663] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371861.663] [5255:5273] [DMG]      [
[1770371861.663] [5255:5273] [DMG]              InvokeResponseIB =
[1770371861.663] [5255:5273] [DMG]              {
[1770371861.663] [5255:5273] [DMG]                      CommandDataIB =
[1770371861.664] [5255:5273] [DMG]                      {
[1770371861.664] [5255:5273] [DMG]                              CommandPathIB =
[1770371861.664] [5255:5273] [DMG]                              {
[1770371861.664] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371861.664] [5255:5273] [DMG]                                      ClusterId = 0x31,
[1770371861.664] [5255:5273] [DMG]                                      CommandId = 0x5,
[1770371861.665] [5255:5273] [DMG]                              },
[1770371861.665] [5255:5273] [DMG]
[1770371861.665] [5255:5273] [DMG]                              CommandFields =
[1770371861.665] [5255:5273] [DMG]                              {
[1770371861.665] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371861.665] [5255:5273] [DMG]                                      0x2 = 0 (unsigned),
[1770371861.665] [5255:5273] [DMG]                              },
[1770371861.666] [5255:5273] [DMG]                      },
[1770371861.666] [5255:5273] [DMG]
[1770371861.666] [5255:5273] [DMG]              },
[1770371861.666] [5255:5273] [DMG]
[1770371861.667] [5255:5273] [DMG]      ],
[1770371861.667] [5255:5273] [DMG]
[1770371861.667] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371861.667] [5255:5273] [DMG] },
[1770371861.667] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1770371861.667] [5255:5273] [CTL] Received NetworkConfig response, networkingStatus=0
[1770371861.667] [5255:5273] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1770371861.667] [5255:5273] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1770371861.667] [5255:5273] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1770371861.667] [5255:5273] [CTL] Arming failsafe (164 seconds)
[1770371861.668] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371861.668] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371861.668] [5255:5273] [EM] <<< [E:33042i S:39568 M:258242111] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770371861.669] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371861.669] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371861.853] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371861.857] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371861.857] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371861.857] [5255:5273] [EM] >>> [E:33042i S:39568 M:7332078] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770371861.858] [5255:5273] [EM] Found matching exchange: 33042i, Delegate: 0xffff9800ad28
[1770371861.858] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371861.858] [5255:5273] [DMG] InvokeResponseMessage =
[1770371861.858] [5255:5273] [DMG] {
[1770371861.858] [5255:5273] [DMG]      suppressResponse = false,
[1770371861.858] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371861.858] [5255:5273] [DMG]      [
[1770371861.858] [5255:5273] [DMG]              InvokeResponseIB =
[1770371861.858] [5255:5273] [DMG]              {
[1770371861.859] [5255:5273] [DMG]                      CommandDataIB =
[1770371861.859] [5255:5273] [DMG]                      {
[1770371861.859] [5255:5273] [DMG]                              CommandPathIB =
[1770371861.859] [5255:5273] [DMG]                              {
[1770371861.859] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371861.859] [5255:5273] [DMG]                                      ClusterId = 0x30,
[1770371861.859] [5255:5273] [DMG]                                      CommandId = 0x1,
[1770371861.860] [5255:5273] [DMG]                              },
[1770371861.860] [5255:5273] [DMG]
[1770371861.860] [5255:5273] [DMG]                              CommandFields =
[1770371861.860] [5255:5273] [DMG]                              {
[1770371861.860] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371861.860] [5255:5273] [DMG]                                      0x1 = "" (0 chars),
[1770371861.861] [5255:5273] [DMG]                              },
[1770371861.861] [5255:5273] [DMG]                      },
[1770371861.861] [5255:5273] [DMG]
[1770371861.861] [5255:5273] [DMG]              },
[1770371861.861] [5255:5273] [DMG]
[1770371861.861] [5255:5273] [DMG]      ],
[1770371861.861] [5255:5273] [DMG]
[1770371861.861] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371861.861] [5255:5273] [DMG] },
[1770371861.862] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770371861.862] [5255:5273] [CTL] Received ArmFailSafe response errorCode=0
[1770371861.862] [5255:5273] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1770371861.862] [5255:5273] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1770371861.862] [5255:5273] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1770371861.862] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371861.862] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371861.862] [5255:5273] [EM] <<< [E:33043i S:39568 M:258242112] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1770371861.863] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371861.864] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371862.049] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371863.221] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371863.222] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371863.222] [5255:5273] [EM] >>> [E:33043i S:39568 M:7332079] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1770371863.222] [5255:5273] [EM] Found matching exchange: 33043i, Delegate: 0xffff98008ae8
[1770371863.222] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371863.222] [5255:5273] [DMG] InvokeResponseMessage =
[1770371863.223] [5255:5273] [DMG] {
[1770371863.223] [5255:5273] [DMG]      suppressResponse = false,
[1770371863.223] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371863.223] [5255:5273] [DMG]      [
[1770371863.223] [5255:5273] [DMG]              InvokeResponseIB =
[1770371863.223] [5255:5273] [DMG]              {
[1770371863.223] [5255:5273] [DMG]                      CommandDataIB =
[1770371863.223] [5255:5273] [DMG]                      {
[1770371863.223] [5255:5273] [DMG]                              CommandPathIB =
[1770371863.223] [5255:5273] [DMG]                              {
[1770371863.224] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371863.224] [5255:5273] [DMG]                                      ClusterId = 0x31,
[1770371863.224] [5255:5273] [DMG]                                      CommandId = 0x7,
[1770371863.224] [5255:5273] [DMG]                              },
[1770371863.224] [5255:5273] [DMG]
[1770371863.224] [5255:5273] [DMG]                              CommandFields =
[1770371863.225] [5255:5273] [DMG]                              {
[1770371863.225] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371863.225] [5255:5273] [DMG]                                      0x2 = NULL
[1770371863.225] [5255:5273] [DMG]                              },
[1770371863.225] [5255:5273] [DMG]                      },
[1770371863.225] [5255:5273] [DMG]
[1770371863.226] [5255:5273] [DMG]              },
[1770371863.226] [5255:5273] [DMG]
[1770371863.226] [5255:5273] [DMG]      ],
[1770371863.226] [5255:5273] [DMG]
[1770371863.226] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371863.226] [5255:5273] [DMG] },
[1770371863.226] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1770371863.226] [5255:5273] [CTL] Received ConnectNetwork response, networkingStatus=0
[1770371863.226] [5255:5273] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1770371863.226] [5255:5273] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'
[1770371863.226] [5255:5273] [CTL] Performing next commissioning step 'kEvictPreviousCaseSessions'
[1770371863.227] [5255:5273] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1770371863.227] [5255:5273] [CTL] Successfully finished commissioning step 'kEvictPreviousCaseSessions'
[1770371863.227] [5255:5273] [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'
[1770371863.227] [5255:5273] [CTL] Performing next commissioning step 'kFindOperationalForStayActive'
[1770371863.227] [5255:5273] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770371863.227] [5255:5273] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770371863.227] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1770371863.228] [5255:5273] [DIS] Lookup started for 2F35D622378DB6C5-00000000000008CA
[1770371863.228] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371863.428] [5255:5273] [DIS] Checking node lookup status for 2F35D622378DB6C5-00000000000008CA after 200 ms
[1770371865.555] [5255:5273] [DIS] SRV record already actively processed.
[1770371865.557] [5255:5273] [DIS] Lookup clearing interface for non LL address
[1770371865.558] [5255:5273] [DIS] UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3%eth0]:5540: new best score: 5 (for 2F35D622378DB6C5-00000000000008CA)
[1770371865.558] [5255:5273] [DIS] Checking node lookup status for 2F35D622378DB6C5-00000000000008CA after 2330 ms
[1770371865.558] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540 while in state 2
[1770371865.558] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1770371865.558] [5255:5273] [IN] SecureSession[0xffffa003c3d0]: Allocated Type:2 LSID:39569
[1770371865.558] [5255:5273] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1770371865.562] [5255:5273] [EM] <<< [E:33044i S:0 M:18185582] (U) Msg TX from A64A2491F1CDF04A to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1770371865.562] [5255:5273] [EM] ??1 [E:33044i S:0 M:18185582] (U) Msg Retransmission to 0:0000000000000000 scheduled for 7937ms from now [State:Idle II:7000 AI:2500 AT:4000]
[1770371865.562] [5255:5273] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1770371865.562] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1770371865.851] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371866.188] [5255:5273] [EM] >>> [E:33044i S:0 M:121134563 (Ack:18185582)] (U) Msg RX from 0:0000000000000000 [0000] to A64A2491F1CDF04A --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770371866.188] [5255:5273] [EM] Found matching exchange: 33044i, Delegate: 0xffff980125b8
[1770371866.188] [5255:5273] [EM] Rxd Ack; Removing MessageCounter:18185582 from Retrans Table on exchange 33044i
[1770371866.273] [5255:5273] [EM] >>> [E:33044i S:0 M:121134564 (Ack:18185582)] (U) Msg RX from 0:0000000000000000 [0000] to A64A2491F1CDF04A --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[1770371866.273] [5255:5273] [EM] Found matching exchange: 33044i, Delegate: 0xffff980125b8
[1770371866.273] [5255:5273] [EM] CHIP MessageCounter:18185582 not in RetransTable on exchange 33044i
[1770371866.273] [5255:5273] [SC] Received Sigma2 msg
[1770371866.273] [5255:5273] [SC] Found MRP parameters in the message
[1770371866.284] [5255:5273] [SC] Peer <00000000000008CA, 1> assigned session ID 48003
[1770371866.285] [5255:5273] [SC] Sending Sigma3
[1770371866.286] [5255:5273] [EM] <<< [E:33044i S:0 M:18185583 (Ack:121134564)] (U) Msg TX from A64A2491F1CDF04A to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1770371866.287] [5255:5273] [EM] ??1 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3242ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770371866.287] [5255:5273] [SC] Sent Sigma3 msg
[1770371868.290] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371868.290] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371869.530] [5255:5273] [EM] <<1 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000
[1770371869.531] [5255:5273] [EM] ??2 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3097ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770371870.298] [5255:5273] [IN] Received a duplicate message with MessageCounter:121134564 on exchange 33044i
[1770371870.298] [5255:5273] [EM] >>> [E:33044i S:0 M:121134564 (Ack:18185582)] (U) Msg RX from 0:0000000000000000 [0000] to A64A2491F1CDF04A --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[1770371870.298] [5255:5273] [EM] Found matching exchange: 33044i, Delegate: 0xffff980125b8
[1770371870.299] [5255:5273] [EM] Forcing tx of solitary ack for duplicate MessageCounter:121134564 on exchange 33044i
[1770371870.299] [5255:5273] [EM] <<< [E:33044i S:0 M:18185584 (Ack:121134564)] (U) Msg TX from A64A2491F1CDF04A to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770371870.922] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371872.628] [5255:5273] [EM] <<2 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000
[1770371872.629] [5255:5273] [EM] ??3 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000 scheduled for 4568ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770371873.360] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371873.360] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371876.089] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16389
[1770371877.198] [5255:5273] [EM] <<3 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000
[1770371877.198] [5255:5273] [EM] ??4 [E:33044i S:0 M:18185583] (U) Msg Retransmission to 0:0000000000000000 scheduled for 7475ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770371878.527] [5255:5264] [DL] Indication received, conn = 0xffffa0013d80
[1770371878.527] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16391
[1770371878.769] [5255:5273] [EM] >>> [E:33044i S:0 M:121134565 (Ack:18185583)] (U) Msg RX from 0:0000000000000000 [0000] to A64A2491F1CDF04A --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770371878.769] [5255:5273] [EM] Found matching exchange: 33044i, Delegate: 0xffff980125b8
[1770371878.769] [5255:5273] [EM] Rxd Ack; Removing MessageCounter:18185583 from Retrans Table on exchange 33044i
[1770371878.790] [5255:5273] [EM] >>> [E:33044i S:0 M:121134566 (Ack:18185583)] (U) Msg RX from 0:0000000000000000 [0000] to A64A2491F1CDF04A --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1770371878.790] [5255:5273] [EM] Found matching exchange: 33044i, Delegate: 0xffff980125b8
[1770371878.791] [5255:5273] [EM] CHIP MessageCounter:18185583 not in RetransTable on exchange 33044i
[1770371878.791] [5255:5273] [SC] Success status report received. Session was established
[1770371878.798] [5255:5273] [SC] SecureSession[0xffffa003c3d0, LSID:39569]: State change 'kEstablishing' --> 'kActive'
[1770371878.798] [5255:5273] [IN] SecureSession[0xffffa003c3d0]: Activated - Type:2 LSID:39569
[1770371878.798] [5255:5273] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:39569 PSID:48003!
[1770371878.798] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1770371878.799] [5255:5273] [CTL] Successfully finished commissioning step 'kFindOperationalForStayActive'
[1770371878.799] [5255:5273] [CTL] Commissioning stage next step: 'kFindOperationalForStayActive' -> 'ICDSendStayActive'
[1770371878.799] [5255:5273] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1770371878.799] [5255:5273] [CTL] Skipping kICDSendStayActive
[1770371878.799] [5255:5273] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1770371878.799] [5255:5273] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'kFindOperationalForCommissioningComplete'
[1770371878.799] [5255:5273] [CTL] Performing next commissioning step 'kFindOperationalForCommissioningComplete'
[1770371878.799] [5255:5273] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770371878.799] [5255:5273] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770371878.799] [5255:5273] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1770371878.799] [5255:5273] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1770371878.799] [5255:5273] [CTL] Successfully finished commissioning step 'kFindOperationalForCommissioningComplete'
[1770371878.799] [5255:5273] [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'
[1770371878.799] [5255:5273] [CTL] Performing next commissioning step 'SendComplete'
[1770371878.800] [5255:5273] [DMG] ICR moving to [AddingComm]
[1770371878.800] [5255:5273] [DMG] ICR moving to [AddedComma]
[1770371878.800] [5255:5273] [EM] <<< [E:33045i S:39569 M:263190221] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [B6C5] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1770371878.800] [5255:5273] [EM] ??1 [E:33045i S:39569 M:263190221] (S) Msg Retransmission to 1:00000000000008CA scheduled for 9426ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770371878.801] [5255:5273] [DMG] ICR moving to [AwaitingRe]
[1770371878.801] [5255:5273] [EM] <<< [E:33044i S:0 M:18185585 (Ack:121134566)] (U) Msg TX from A64A2491F1CDF04A to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770371878.801] [5255:5273] [EM] Flushed pending ack for MessageCounter:121134566 on exchange 33044i
[1770371878.801] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 32792
[1770371879.560] [5255:5273] [EM] >>> [E:33045i S:39569 M:249795557 (Ack:263190221)] (S) Msg RX from 1:00000000000008CA [B6C5] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1770371879.561] [5255:5273] [EM] Found matching exchange: 33045i, Delegate: 0xffff9800ad28
[1770371879.561] [5255:5273] [EM] Rxd Ack; Removing MessageCounter:263190221 from Retrans Table on exchange 33045i
[1770371879.561] [5255:5273] [DMG] ICR moving to [ResponseRe]
[1770371879.561] [5255:5273] [DMG] InvokeResponseMessage =
[1770371879.561] [5255:5273] [DMG] {
[1770371879.561] [5255:5273] [DMG]      suppressResponse = false,
[1770371879.561] [5255:5273] [DMG]      InvokeResponseIBs =
[1770371879.561] [5255:5273] [DMG]      [
[1770371879.561] [5255:5273] [DMG]              InvokeResponseIB =
[1770371879.561] [5255:5273] [DMG]              {
[1770371879.561] [5255:5273] [DMG]                      CommandDataIB =
[1770371879.561] [5255:5273] [DMG]                      {
[1770371879.561] [5255:5273] [DMG]                              CommandPathIB =
[1770371879.561] [5255:5273] [DMG]                              {
[1770371879.562] [5255:5273] [DMG]                                      EndpointId = 0x0,
[1770371879.562] [5255:5273] [DMG]                                      ClusterId = 0x30,
[1770371879.562] [5255:5273] [DMG]                                      CommandId = 0x5,
[1770371879.562] [5255:5273] [DMG]                              },
[1770371879.562] [5255:5273] [DMG]
[1770371879.562] [5255:5273] [DMG]                              CommandFields =
[1770371879.562] [5255:5273] [DMG]                              {
[1770371879.562] [5255:5273] [DMG]                                      0x0 = 0 (unsigned),
[1770371879.562] [5255:5273] [DMG]                                      0x1 = "" (0 chars),
[1770371879.563] [5255:5273] [DMG]                              },
[1770371879.564] [5255:5273] [DMG]                      },
[1770371879.564] [5255:5273] [DMG]
[1770371879.564] [5255:5273] [DMG]              },
[1770371879.564] [5255:5273] [DMG]
[1770371879.564] [5255:5273] [DMG]      ],
[1770371879.564] [5255:5273] [DMG]
[1770371879.564] [5255:5273] [DMG]      InteractionModelRevision = 12
[1770371879.564] [5255:5273] [DMG] },
[1770371879.565] [5255:5273] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1770371879.565] [5255:5273] [CTL] Received CommissioningComplete response, errorCode=0
[1770371879.565] [5255:5273] [CTL] Successfully finished commissioning step 'SendComplete'
[1770371879.565] [5255:5273] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1770371879.565] [5255:5273] [CTL] Performing next commissioning step 'Cleanup'
[1770371879.565] [5255:5273] [CTL] Successfully finished commissioning step 'Cleanup'
[1770371879.565] [5255:5273] [DIS] Closing all BLE connections
[1770371879.565] [5255:5273] [IN] Clearing BLE pending packets.
[1770371879.566] [5255:5273] [BLE] Auto-closing end point's BLE connection.
[1770371879.566] [5255:5273] [DL] Closing BLE GATT connection (con 0xffffa0013d80)
[1770371879.566] [5255:5264] [DL] Close BLE connection: peer=E8:48:61:70:67:2D
[1770371879.600] [5255:5273] [IN] SecureSession[0xffff9800d750]: MarkForEviction Type:1 LSID:39568
[1770371879.600] [5255:5273] [SC] SecureSession[0xffff9800d750, LSID:39568]: State change 'kActive' --> 'kPendingEviction'
[1770371879.600] [5255:5273] [IN] SecureSession[0xffff9800d750]: Released - Type:1 LSID:39568
[1770371879.600] [5255:5273] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1770371879.600] [5255:5273] [TOO] Device commissioning completed with success
[1770371879.601] [5255:5273] [DMG] ICR moving to [AwaitingDe]
[1770371879.601] [5255:5264] [DL] BLE connection closed: conn=0xffffa0013d80
[1770371879.601] [5255:5273] [EM] <<< [E:33045i S:39569 M:263190222 (Ack:249795557)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [B6C5] [UDP:[fd98:42ee:f6b4:1:5c2a:f699:2ea3:c3b3]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1770371879.602] [5255:5273] [EM] Flushed pending ack for MessageCounter:249795557 on exchange 33045i
[1770371879.602] [5255:5273] [DL] HandlePlatformSpecificBLEEvent 16390
[1770371879.602] [5255:5273] [BLE] No endpoint for unsubscribe complete
[1770371879.602] [5255:5273] [BLE] No endpoint for connection error
[1770371879.603] [5255:5255] [CTL] Shutting down the commissioner
[1770371879.603] [5255:5255] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770371879.603] [5255:5255] [CTL] Shutting down the controller
[1770371879.604] [5255:5255] [IN] Expiring all sessions for fabric 0x1!!
[1770371879.604] [5255:5255] [IN] SecureSession[0xffffa003c3d0]: MarkForEviction Type:2 LSID:39569
[1770371879.604] [5255:5255] [SC] SecureSession[0xffffa003c3d0, LSID:39569]: State change 'kActive' --> 'kPendingEviction'
[1770371879.604] [5255:5255] [IN] SecureSession[0xffffa003c3d0]: Released - Type:2 LSID:39569
[1770371879.604] [5255:5255] [FP] Forgetting fabric 0x1
[1770371879.604] [5255:5255] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770371879.605] [5255:5255] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770371879.605] [5255:5255] [TS] Reverted Last Known Good Time to previous value
[1770371879.605] [5255:5255] [CTL] Shutting down the commissioner
[1770371879.606] [5255:5255] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770371879.606] [5255:5255] [CTL] Shutting down the controller
[1770371879.606] [5255:5255] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770371879.607] [5255:5255] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770371879.608] [5255:5255] [FP] Shutting down FabricTable
[1770371879.608] [5255:5255] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770371879.610] [5255:5255] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770371879.610] [5255:5255] [TS] Reverted Last Known Good Time to previous value
[1770371879.622] [5255:5255] [DL] Wrote settings to /tmp/chip_counters.ini
[1770371879.622] [5255:5255] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770371879.622] [5255:5255] [DL] Inet Layer shutdown
[1770371879.622] [5255:5255] [DL] BLE Layer shutdown
[1770371879.627] [5255:5255] [DL] WiFi-PAF Layer shutdown
[1770371879.627] [5255:5255] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770371879.627] [5255:5255] [DL] NFCCommissioningMgr shutdown
[1770371879.628] [5255:5255] [DL] System Layer shutdown

```