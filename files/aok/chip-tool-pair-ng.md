
```c

ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840 --paa-trust-store-path ~/paa-root-certs
[1770349719.564] [2665:2665] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770349719.567] [2665:2665] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770349719.580] [2665:2665] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770349719.581] [2665:2665] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770349719.581] [2665:2665] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770349719.592] [2665:2665] [DL] Wrote settings to /tmp/chip_counters.ini
[1770349719.593] [2665:2665] [DL] NVS set: chip-counters/reboot-count = 2 (0x2)
[1770349719.595] [2665:2665] [DL] Got Ethernet interface: eth0
[1770349719.596] [2665:2665] [DL] Found the primary Ethernet interface:eth0
[1770349719.598] [2665:2665] [DL] Got WiFi interface: wlan0
[1770349719.598] [2665:2665] [DL] Failed to reset WiFi statistic counts
[1770349719.598] [2665:2665] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770349719.761] [2665:2665] [IN] UDP::Init bind&listen port=0
[1770349719.761] [2665:2665] [IN] UDP::Init bound to port=53845
[1770349719.761] [2665:2665] [IN] BLEBase::Init - setting/overriding transport
[1770349719.761] [2665:2665] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770349719.761] [2665:2665] [CTL] NFCBase::Init
[1770349719.761] [2665:2665] [IN] TransportMgr initialized
[1770349719.762] [2665:2665] [FP] Initializing FabricTable from persistent storage
[1770349719.762] [2665:2665] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770349719.766] [2665:2665] [FP] Fabric index 0x1 was retrieved from storage. Compressed FabricId 0x998A6BB5C57A2963, FabricId 0x0000000000000001, NodeId 0x000000000001B669, VendorId 0xFFF1
[1770349719.771] [2665:2665] [DMG] Ember attribute persistence requires setting up
[1770349719.771] [2665:2665] [ZCL] Using ZAP configuration...
[1770349719.776] [2665:2665] [CTL] System State Initialized...
[1770349720.368] [2665:2665] [CTL] Setting attestation nonce to random value
[1770349720.369] [2665:2665] [CTL] Setting CSR nonce to random value
[1770349720.369] [2665:2665] [IN] UDP::Init bind&listen port=5550
[1770349720.369] [2665:2665] [IN] UDP::Init bound to port=5550
[1770349720.369] [2665:2665] [IN] TransportMgr initialized
[1770349720.370] [2665:2683] [DL] CHIP task running
[1770349720.371] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 32786
[1770349720.372] [2665:2683] [CTL] Setting attestation nonce to random value
[1770349720.372] [2665:2683] [CTL] Setting CSR nonce to random value
[1770349720.375] [2665:2683] [CTL] Generating NOC
[1770349720.378] [2665:2683] [FP] Validating NOC chain
[1770349720.383] [2665:2683] [FP] NOC chain validation successful
[1770349720.383] [2665:2683] [FP] Updated fabric at index: 0x1, Node ID: 0x000000000001B669
[1770349720.383] [2665:2683] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770349720.383] [2665:2683] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770349720.383] [2665:2683] [TS] Retaining current Last Known Good Time
[1770349720.387] [2665:2683] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770349720.391] [2665:2683] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770349720.394] [2665:2683] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 998A6BB5C57A2963)
[1770349720.394] [2665:2683] [IN] UDP::Init bind&listen port=5551
[1770349720.394] [2665:2683] [IN] UDP::Init bound to port=5551
[1770349720.394] [2665:2683] [IN] TransportMgr initialized
[1770349720.430] [2665:2683] [CTL] Setting thread operational dataset from parameters
[1770349720.430] [2665:2683] [CTL] Setting attestation nonce to random value
[1770349720.430] [2665:2683] [CTL] Setting CSR nonce to random value
[1770349720.430] [2665:2683] [CTL] Commission called for node ID 0x00000000000008CA
[1770349720.468] [2665:2668] [BLE] BLE removing known devices
[1770349720.472] [2665:2668] [BLE] BLE initiating scan
[1770349720.478] [2665:2683] [BLE] ChipDeviceScanner has started scanning!
[1770349720.490] [2665:2668] [BLE] Device 23:BD:37:8A:64:FA does not look like a CHIP device.
[1770349720.510] [2665:2668] [BLE] Device 18:70:3B:FD:B9:4F does not look like a CHIP device.
[1770349720.512] [2665:2668] [BLE] Device 5A:63:B8:FD:E5:59 does not look like a CHIP device.
[1770349720.535] [2665:2668] [BLE] New device scanned: E3:05:6D:C2:73:42
[1770349720.535] [2665:2668] [BLE] Device discriminator match. Attempting to connect.
[1770349720.542] [2665:2668] [BLE] ChipDeviceScanner has stopped scanning!
[1770349720.719] [2665:2668] [DL] ConnectDevice complete
[1770349720.719] [2665:2668] [BLE] New device connected: E3:05:6D:C2:73:42
[1770349724.896] [2665:2668] [DL] CHIP service found
[1770349724.896] [2665:2668] [DL] Valid C1 characteristic found
[1770349724.896] [2665:2668] [DL] Valid C2 characteristic found
[1770349724.896] [2665:2668] [DL] New BLE connection: conn=0xffffa4027880 device=E3:05:6D:C2:73:42 path=/org/bluez/hci0/dev_E3_05_6D_C2_73_42
[1770349724.897] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16387
[1770349724.897] [2665:2683] [DIS] Closing all BLE connections
[1770349724.897] [2665:2683] [IN] BleConnectionComplete: endPoint 0xaaaada2e6fd0
[1770349724.898] [2665:2683] [IN] SecureSession[0xffff9c009c70]: Allocated Type:1 LSID:2829
[1770349724.898] [2665:2683] [SC] Assigned local session key ID 2829
[1770349724.899] [2665:2683] [EM] <<< [E:28545i S:0 M:149805776] (U) Msg TX from A44357A98976FD14 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770349724.899] [2665:2683] [IN] Message appended to BLE send queue
[1770349724.899] [2665:2683] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770349726.380] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349726.771] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16390
[1770349726.771] [2665:2683] [BLE] subscribe complete, ep = 0xaaaada2e6fd0
[1770349726.772] [2665:2668] [DL] Indication received, conn = 0xffffa4027880
[1770349726.773] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16391
[1770349726.773] [2665:2683] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770349726.773] [2665:2683] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770349726.773] [2665:2683] [BLE] local and remote recv window size = 5
[1770349726.774] [2665:2683] [IN] BLE EndPoint 0xaaaada2e6fd0 Connection Complete
[1770349727.160] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349727.259] [2665:2668] [DL] Indication received, conn = 0xffffa4027880
[1770349727.259] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16391
[1770349727.260] [2665:2683] [EM] >>> [E:28545i S:0 M:120823227] (U) Msg RX from 0:0000000000000000 [0000] to A44357A98976FD14 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[1770349727.260] [2665:2683] [EM] Found matching exchange: 28545i, Delegate: 0xffff9c00f7a8
[1770349727.260] [2665:2683] [SC] Received PBKDF param response
[1770349727.260] [2665:2683] [SC] Peer assigned session ID 57446
[1770349727.260] [2665:2683] [SC] Found MRP parameters in the message
[1770349727.282] [2665:2683] [EM] <<< [E:28545i S:0 M:149805777] (U) Msg TX from A44357A98976FD14 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770349727.282] [2665:2683] [SC] Sent spake2p msg1
[1770349727.452] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349727.551] [2665:2668] [DL] Indication received, conn = 0xffffa4027880
[1770349727.551] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16391
[1770349727.551] [2665:2683] [EM] >>> [E:28545i S:0 M:120823228] (U) Msg RX from 0:0000000000000000 [0000] to A44357A98976FD14 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770349727.551] [2665:2683] [EM] Found matching exchange: 28545i, Delegate: 0xffff9c00f7a8
[1770349727.552] [2665:2683] [SC] Received spake2p msg2
[1770349727.555] [2665:2683] [EM] <<< [E:28545i S:0 M:149805778] (U) Msg TX from A44357A98976FD14 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770349727.556] [2665:2683] [SC] Sent spake2p msg3
[1770349727.744] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349727.747] [2665:2668] [DL] Indication received, conn = 0xffffa4027880
[1770349727.747] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16391
[1770349727.748] [2665:2683] [EM] >>> [E:28545i S:0 M:120823229] (U) Msg RX from 0:0000000000000000 [0000] to A44357A98976FD14 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770349727.748] [2665:2683] [EM] Found matching exchange: 28545i, Delegate: 0xffff9c00f7a8
[1770349727.749] [2665:2683] [SC] SecureSession[0xffff9c009c70, LSID:2829]: State change 'kEstablishing' --> 'kActive'
[1770349727.749] [2665:2683] [IN] SecureSession[0xffff9c009c70]: Activated - Type:1 LSID:2829
[1770349727.749] [2665:2683] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:2829 PSID:57446!
[1770349727.749] [2665:2683] [CTL] Remote device completed SPAKE2+ handshake
[1770349727.749] [2665:2683] [TOO] Pairing Success
[1770349727.749] [2665:2683] [TOO] PASE establishment successful
[1770349727.749] [2665:2683] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770349727.750] [2665:2683] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770349727.750] [2665:2683] [CTL] Sending read requests for commissioning information
[1770349727.750] [2665:2683] [DMG] SendReadRequest ReadClient[0xffff9c010de0]: Sending Read Request
[1770349727.750] [2665:2683] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770349727.751] [2665:2683] [EM] <<< [E:28546i S:2829 M:32417909] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770349727.752] [2665:2683] [DMG] MoveToState ReadClient[0xffff9c010de0]: Moving to [AwaitingIn]
[1770349727.752] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 32792
[1770349728.232] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349728.528] [2665:2668] [DL] Indication received, conn = 0xffffa4027880
[1770349728.529] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16391
[1770349728.529] [2665:2683] [EM] >>> [E:28546i S:2829 M:6780828] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:201)
[1770349728.529] [2665:2683] [EM] Found matching exchange: 28546i, Delegate: 0xffff9c010df0
[1770349728.530] [2665:2683] [DMG] ReportDataMessage =
[1770349728.530] [2665:2683] [DMG] {
[1770349728.530] [2665:2683] [DMG]      AttributeReportIBs =
[1770349728.530] [2665:2683] [DMG]      [
[1770349728.530] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.530] [2665:2683] [DMG]              {
[1770349728.530] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.531] [2665:2683] [DMG]                      {
[1770349728.531] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.531] [2665:2683] [DMG]                              {
[1770349728.531] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.531] [2665:2683] [DMG]                                      Cluster = 0x28,
[1770349728.531] [2665:2683] [DMG]                                      Attribute = 0x0000_0004,
[1770349728.531] [2665:2683] [DMG]                              }
[1770349728.532] [2665:2683] [DMG]
[1770349728.532] [2665:2683] [DMG]                              StatusIB =
[1770349728.532] [2665:2683] [DMG]                              {
[1770349728.532] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.532] [2665:2683] [DMG]                              },
[1770349728.532] [2665:2683] [DMG]
[1770349728.532] [2665:2683] [DMG]                      },
[1770349728.532] [2665:2683] [DMG]
[1770349728.532] [2665:2683] [DMG]              },
[1770349728.532] [2665:2683] [DMG]
[1770349728.532] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.532] [2665:2683] [DMG]              {
[1770349728.532] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.532] [2665:2683] [DMG]                      {
[1770349728.533] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.533] [2665:2683] [DMG]                              {
[1770349728.533] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.533] [2665:2683] [DMG]                                      Cluster = 0x28,
[1770349728.533] [2665:2683] [DMG]                                      Attribute = 0x0000_0002,
[1770349728.533] [2665:2683] [DMG]                              }
[1770349728.533] [2665:2683] [DMG]
[1770349728.533] [2665:2683] [DMG]                              StatusIB =
[1770349728.533] [2665:2683] [DMG]                              {
[1770349728.533] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.533] [2665:2683] [DMG]                              },
[1770349728.533] [2665:2683] [DMG]
[1770349728.533] [2665:2683] [DMG]                      },
[1770349728.533] [2665:2683] [DMG]
[1770349728.533] [2665:2683] [DMG]              },
[1770349728.534] [2665:2683] [DMG]
[1770349728.534] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.534] [2665:2683] [DMG]              {
[1770349728.534] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.534] [2665:2683] [DMG]                      {
[1770349728.534] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.534] [2665:2683] [DMG]                              {
[1770349728.534] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.534] [2665:2683] [DMG]                                      Cluster = 0x30,
[1770349728.534] [2665:2683] [DMG]                                      Attribute = 0x0000_0003,
[1770349728.534] [2665:2683] [DMG]                              }
[1770349728.534] [2665:2683] [DMG]
[1770349728.534] [2665:2683] [DMG]                              StatusIB =
[1770349728.534] [2665:2683] [DMG]                              {
[1770349728.535] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.535] [2665:2683] [DMG]                              },
[1770349728.535] [2665:2683] [DMG]
[1770349728.535] [2665:2683] [DMG]                      },
[1770349728.535] [2665:2683] [DMG]
[1770349728.535] [2665:2683] [DMG]              },
[1770349728.535] [2665:2683] [DMG]
[1770349728.535] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.535] [2665:2683] [DMG]              {
[1770349728.535] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.535] [2665:2683] [DMG]                      {
[1770349728.535] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.535] [2665:2683] [DMG]                              {
[1770349728.535] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.535] [2665:2683] [DMG]                                      Cluster = 0x30,
[1770349728.536] [2665:2683] [DMG]                                      Attribute = 0x0000_0002,
[1770349728.536] [2665:2683] [DMG]                              }
[1770349728.536] [2665:2683] [DMG]
[1770349728.536] [2665:2683] [DMG]                              StatusIB =
[1770349728.536] [2665:2683] [DMG]                              {
[1770349728.536] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.536] [2665:2683] [DMG]                              },
[1770349728.536] [2665:2683] [DMG]
[1770349728.536] [2665:2683] [DMG]                      },
[1770349728.536] [2665:2683] [DMG]
[1770349728.536] [2665:2683] [DMG]              },
[1770349728.536] [2665:2683] [DMG]
[1770349728.536] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.536] [2665:2683] [DMG]              {
[1770349728.537] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.537] [2665:2683] [DMG]                      {
[1770349728.537] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.537] [2665:2683] [DMG]                              {
[1770349728.537] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.537] [2665:2683] [DMG]                                      Cluster = 0x30,
[1770349728.537] [2665:2683] [DMG]                                      Attribute = 0x0000_0001,
[1770349728.537] [2665:2683] [DMG]                              }
[1770349728.537] [2665:2683] [DMG]
[1770349728.537] [2665:2683] [DMG]                              StatusIB =
[1770349728.537] [2665:2683] [DMG]                              {
[1770349728.537] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.537] [2665:2683] [DMG]                              },
[1770349728.537] [2665:2683] [DMG]
[1770349728.538] [2665:2683] [DMG]                      },
[1770349728.538] [2665:2683] [DMG]
[1770349728.538] [2665:2683] [DMG]              },
[1770349728.538] [2665:2683] [DMG]
[1770349728.538] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.538] [2665:2683] [DMG]              {
[1770349728.538] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.538] [2665:2683] [DMG]                      {
[1770349728.538] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.538] [2665:2683] [DMG]                              {
[1770349728.538] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.538] [2665:2683] [DMG]                                      Cluster = 0x30,
[1770349728.538] [2665:2683] [DMG]                                      Attribute = 0x0000_0000,
[1770349728.538] [2665:2683] [DMG]                              }
[1770349728.539] [2665:2683] [DMG]
[1770349728.539] [2665:2683] [DMG]                              StatusIB =
[1770349728.539] [2665:2683] [DMG]                              {
[1770349728.539] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.539] [2665:2683] [DMG]                              },
[1770349728.539] [2665:2683] [DMG]
[1770349728.539] [2665:2683] [DMG]                      },
[1770349728.539] [2665:2683] [DMG]
[1770349728.539] [2665:2683] [DMG]              },
[1770349728.539] [2665:2683] [DMG]
[1770349728.539] [2665:2683] [DMG]              AttributeReportIB =
[1770349728.539] [2665:2683] [DMG]              {
[1770349728.540] [2665:2683] [DMG]                      AttributeStatusIB =
[1770349728.540] [2665:2683] [DMG]                      {
[1770349728.540] [2665:2683] [DMG]                              AttributePathIB =
[1770349728.540] [2665:2683] [DMG]                              {
[1770349728.540] [2665:2683] [DMG]                                      Endpoint = 0x0,
[1770349728.540] [2665:2683] [DMG]                                      Cluster = 0x30,
[1770349728.540] [2665:2683] [DMG]                                      Attribute = 0x0000_0004,
[1770349728.540] [2665:2683] [DMG]                              }
[1770349728.540] [2665:2683] [DMG]
[1770349728.540] [2665:2683] [DMG]                              StatusIB =
[1770349728.540] [2665:2683] [DMG]                              {
[1770349728.540] [2665:2683] [DMG]                                      status = 0x7f (UNSUPPORTED_ENDPOINT),
[1770349728.540] [2665:2683] [DMG]                              },
[1770349728.541] [2665:2683] [DMG]
[1770349728.541] [2665:2683] [DMG]                      },
[1770349728.541] [2665:2683] [DMG]
[1770349728.541] [2665:2683] [DMG]              },
[1770349728.541] [2665:2683] [DMG]
[1770349728.541] [2665:2683] [DMG]      ],
[1770349728.541] [2665:2683] [DMG]
[1770349728.541] [2665:2683] [DMG]      SuppressResponse = true,
[1770349728.541] [2665:2683] [DMG]      InteractionModelRevision = 11
[1770349728.541] [2665:2683] [DMG] }
[1770349728.542] [2665:2683] [DMG] SendReadRequest ReadClient[0xffff9c010de0]: Sending Read Request
[1770349728.542] [2665:2683] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770349728.543] [2665:2683] [EM] <<< [E:28547i S:2829 M:32417910] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770349728.544] [2665:2683] [DMG] MoveToState ReadClient[0xffff9c010de0]: Moving to [AwaitingIn]
[1770349728.915] [2665:2683] [DL] HandlePlatformSpecificBLEEvent 16389
[1770349734.962] [2665:2668] [DL] BLE connection closed: conn=0xffffa4027880
[1770349734.963] [2665:2683] [IN] Clearing BLE pending packets.
[1770349760.543] [2665:2683] [DMG] Time out! failed to receive report data from Exchange: 28547i
[1770349760.543] [2665:2683] [CTL] Failed to read BasicCommissioningInfo: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.543] [2665:2683] [CTL] Failed to read RegulatoryConfig: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.543] [2665:2683] [CTL] Failed to read LocationCapability: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read Breadcrumb: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Ignoring failure to read SupportsConcurrentConnection: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read VendorID: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read ProductID: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Error on commissioning step 'ReadCommissioningInfo': 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error'
[1770349760.544] [2665:2683] [CTL] Going from commissioning step 'ReadCommissioningInfo' with lastErr = 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error' -> 'Cleanup'
[1770349760.544] [2665:2683] [CTL] Performing next commissioning step 'Cleanup' with completion status = 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error'
[1770349760.544] [2665:2683] [CTL] Disarming failsafe on device 0xffff9c00f750
[1770349760.544] [2665:2683] [DMG] ICR moving to [AddingComm]
[1770349760.545] [2665:2683] [DMG] ICR moving to [AddedComma]
[1770349760.545] [2665:2683] [EM] <<< [E:28548i S:2829 M:32417911] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770349760.545] [2665:2683] [IN] SendMessage() to BLE failed: src/transport/raw/BLE.cpp:100: CHIP Error 0x00000003: Incorrect state
[1770349760.545] [2665:2683] [CTL] Failed to send command to disarm fail-safe: src/transport/raw/BLE.cpp:100: CHIP Error 0x00000003: Incorrect state
[1770349760.545] [2665:2683] [CTL] Successfully finished commissioning step 'Cleanup'
[1770349760.546] [2665:2683] [DIS] Closing all BLE connections
[1770349760.546] [2665:2683] [IN] SecureSession[0xffff9c009c70]: MarkForEviction Type:1 LSID:2829
[1770349760.546] [2665:2683] [SC] SecureSession[0xffff9c009c70, LSID:2829]: State change 'kActive' --> 'kPendingEviction'
[1770349760.546] [2665:2683] [IN] SecureSession[0xffff9c009c70]: Released - Type:1 LSID:2829
[1770349760.546] [2665:2683] [CTL] Commissioning complete for node ID 0x00000000000008CA: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.546] [2665:2683] [TOO] Device commissioning Failure: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.547] [2665:2665] [CTL] Shutting down the commissioner
[1770349760.548] [2665:2665] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770349760.548] [2665:2665] [CTL] Shutting down the controller
[1770349760.548] [2665:2665] [IN] Expiring all sessions for fabric 0x1!!
[1770349760.548] [2665:2665] [FP] Forgetting fabric 0x1
[1770349760.548] [2665:2665] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770349760.549] [2665:2665] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770349760.549] [2665:2665] [TS] Reverted Last Known Good Time to previous value
[1770349760.549] [2665:2665] [CTL] Shutting down the commissioner
[1770349760.550] [2665:2665] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770349760.550] [2665:2665] [CTL] Shutting down the controller
[1770349760.550] [2665:2665] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770349760.550] [2665:2665] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770349760.551] [2665:2665] [FP] Shutting down FabricTable
[1770349760.551] [2665:2665] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770349760.551] [2665:2665] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770349760.551] [2665:2665] [TS] Reverted Last Known Good Time to previous value
[1770349760.563] [2665:2665] [DL] Wrote settings to /tmp/chip_counters.ini
[1770349760.563] [2665:2665] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770349760.563] [2665:2665] [DL] Inet Layer shutdown
[1770349760.563] [2665:2665] [DL] BLE Layer shutdown
[1770349760.568] [2665:2665] [DL] WiFi-PAF Layer shutdown
[1770349760.568] [2665:2665] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770349760.568] [2665:2665] [DL] NFCCommissioningMgr shutdown
[1770349760.568] [2665:2665] [DL] System Layer shutdown
[1770349760.570] [2665:2665] [TOO] Run command failure: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
ubuntu@ubuntu:~$
```
