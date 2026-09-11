[attestation](attestation.md)  
```c
ubuntu@ubuntu:~$ ./pair.py MT:MNKA1SWV175I8O7IO10
2026-09-09 11:26:07.960 [INFO] ================================================================================
2026-09-09 11:26:07.960 [INFO] CHIP-Tool Pairing Script
2026-09-09 11:26:07.961 [INFO] ================================================================================
2026-09-09 11:26:07.961 [INFO] Log file: 20260909112607.log
2026-09-09 11:26:07.961 [INFO] Timestamp: 2026-09-09 11:26:07
2026-09-09 11:26:07.961 [INFO] QR Code: MT:MNKA1SWV175I8O7IO10
2026-09-09 11:26:07.961 [INFO] Node ID: 2250
2026-09-09 11:26:07.961 [INFO] Thread Dataset: hex:0e0800000000000100004a0300000b35060004001fffe0...
2026-09-09 11:26:07.962 [INFO] Use Certificate: True
2026-09-09 11:26:07.962 [INFO] PAA Trust Store Path: /home/ubuntu/paa-root-certs

Log file: 20260909112607.log
================================================================================
2026-09-09 11:26:07.962 [INFO]
================================================================================
2026-09-09 11:26:07.962 [INFO] STEP 1: Clean Temporary Files
2026-09-09 11:26:07.962 [INFO] ================================================================================
2026-09-09 11:26:07.963 [INFO] [CLEAN] Cleaning CHIP temporary files...
2026-09-09 11:26:07.964 [INFO] [CLEAN] Executing: sudo rm -rf /tmp/chip_counters.ini /tmp/chip_tool_kvs-MVQeVx /tmp/chip_factory.ini /tmp/chip_tool_kvs /tmp/chip_factory.ini-PT3ksG /tmp/chip_tool_config.alpha.ini /tmp/chip_tool_config.ini /tmp/chip_config.ini
2026-09-09 11:26:08.033 [INFO] [CLEAN] Command completed successfully
2026-09-09 11:26:08.034 [INFO] [CLEAN] Successfully cleaned /tmp/chip_* files
2026-09-09 11:26:08.535 [INFO]
================================================================================
2026-09-09 11:26:08.536 [INFO] STEP 2: Parse Setup Payload
2026-09-09 11:26:08.537 [INFO] ================================================================================
2026-09-09 11:26:08.537 [INFO] [PARSE] Parsing QR code: MT:MNKA1SWV175I8O7IO10
2026-09-09 11:26:08.537 [INFO] [COMMAND] sudo ./chip-tool payload parse-setup-payload MT:MNKA1SWV175I8O7IO10
2026-09-09 11:26:08.843 [INFO] [PARSE] Extracted Passcode: 77822335
2026-09-09 11:26:08.843 [INFO] [PARSE] Extracted Discriminator: 3087
2026-09-09 11:26:08.844 [INFO] Passcode: 77822335
2026-09-09 11:26:08.844 [INFO] Discriminator: 3087

[INFO] Passcode: 77822335
[INFO] Discriminator: 3087
2026-09-09 11:26:08.844 [INFO]
================================================================================
2026-09-09 11:26:08.844 [INFO] STEP 3: Pair Device
2026-09-09 11:26:08.844 [INFO] ================================================================================
2026-09-09 11:26:08.844 [INFO] [PAIR] Attempting to pair device...
2026-09-09 11:26:08.845 [INFO] [PAIR] Passcode: 77822335, Discriminator: 3087
2026-09-09 11:26:08.845 [INFO] [PAIR] Node ID: 2250
2026-09-09 11:26:08.845 [INFO] [PAIR] Use certificate: True
2026-09-09 11:26:08.845 [INFO] [PAIR] PAA trust store path: /home/ubuntu/paa-root-certs
2026-09-09 11:26:08.845 [INFO] [PAIR] Executing: sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 77822335 3087 --paa-trust-store-path /home/ubuntu/paa-root-certs

[1788924387.438] [857359:857359] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1788924387.440] [857359:857359] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1788924387.445] [857359:857359] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1788924387.445] [857359:857359] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1788924387.445] [857359:857359] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1788924387.451] [857359:857359] [DL] Wrote settings to /tmp/chip_counters.ini
[1788924387.451] [857359:857359] [DL] NVS set: chip-counters/reboot-count = 2 (0x2)
[1788924387.452] [857359:857359] [DL] Got Ethernet interface: eth0
[1788924387.452] [857359:857359] [DL] Found the primary Ethernet interface:eth0
[1788924387.452] [857359:857359] [DL] Got WiFi interface: wlan0
[1788924387.453] [857359:857359] [DL] Failed to reset WiFi statistic counts
[1788924387.453] [857359:857359] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1788924387.453] [857359:857359] [IN] UDP::Init bind&listen port=0
[1788924387.453] [857359:857359] [IN] UDP::Init bound to port=35108
[1788924387.453] [857359:857359] [IN] UDP::Init bind&listen port=0
[1788924387.453] [857359:857359] [IN] UDP::Init bound to port=47285
[1788924387.453] [857359:857359] [IN] BLEBase::Init - setting/overriding transport
[1788924387.453] [857359:857359] [IN] WiFiPAFBase::Init - setting/overriding transport
[1788924387.453] [857359:857359] [IN] TransportMgr initialized
[1788924387.453] [857359:857359] [FP] Initializing FabricTable from persistent storage
[1788924387.453] [857359:857359] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1788924387.455] [857359:857359] [FP] Fabric index 0x1 was retrieved from storage. Compressed FabricId 0x873AC76EFBA3164B, FabricId 0x0000000000000001, NodeId 0x000000000001B669, VendorId 0xFFF1
[1788924387.457] [857359:857359] [DMG] Ember attribute persistence requires setting up
[1788924387.457] [857359:857359] [ZCL] Using ZAP configuration...
[1788924387.461] [857359:857359] [CTL] System State Initialized...
[1788924387.727] [857359:857359] [CTL] Setting attestation nonce to random value
[1788924387.728] [857359:857359] [CTL] Setting CSR nonce to random value
[1788924387.728] [857359:857359] [IN] UDP::Init bind&listen port=5550
[1788924387.728] [857359:857359] [IN] UDP::Init bound to port=5550
[1788924387.728] [857359:857359] [IN] UDP::Init bind&listen port=5550
[1788924387.728] [857359:857359] [IN] UDP::Init bound to port=5550
[1788924387.728] [857359:857359] [IN] TransportMgr initialized
[1788924387.728] [857359:857361] [DL] CHIP task running
[1788924387.729] [857359:857361] [CTL] Setting attestation nonce to random value
[1788924387.729] [857359:857361] [CTL] Setting CSR nonce to random value
[1788924387.730] [857359:857361] [CTL] Generating NOC
[1788924387.730] [857359:857361] [FP] Validating NOC chain
[1788924387.732] [857359:857361] [FP] NOC chain validation successful
[1788924387.732] [857359:857361] [FP] Updated fabric at index: 0x1, Node ID: 0x000000000001B669
[1788924387.732] [857359:857361] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1788924387.732] [857359:857361] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1788924387.732] [857359:857361] [TS] Retaining current Last Known Good Time
[1788924387.735] [857359:857361] [FP] Metadata for Fabric 0x1 persisted to storage.
[1788924387.736] [857359:857361] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1788924387.738] [857359:857361] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 873AC76EFBA3164B)
[1788924387.738] [857359:857361] [IN] UDP::Init bind&listen port=5551
[1788924387.738] [857359:857361] [IN] UDP::Init bound to port=5551
[1788924387.738] [857359:857361] [IN] UDP::Init bind&listen port=5551
[1788924387.738] [857359:857361] [IN] UDP::Init bound to port=5551
[1788924387.738] [857359:857361] [IN] TransportMgr initialized
[1788924387.751] [857359:857361] [CTL] Setting thread operational dataset from parameters
[1788924387.751] [857359:857361] [CTL] Setting attestation nonce to random value
[1788924387.751] [857359:857361] [CTL] Setting CSR nonce to random value
[1788924387.751] [857359:857361] [CTL] Commission called for node ID 0x00000000000008CA
[1788924387.784] [857359:857360] [BLE] BLE removing known devices
[1788924390.010] [857359:857360] [BLE] BLE initiating scan
[1788924390.050] [857359:857361] [BLE] ChipDeviceScanner has started scanning!
[1788924390.051] [857359:857361] [DL] Long dispatch time: 2299 ms, for event type 3
[1788924390.071] [857359:857360] [BLE] Device 63:A1:50:00:01:23 does not look like a CHIP device.
[1788924390.074] [857359:857360] [BLE] Device 34:D8:A4:9A:13:20 does not look like a CHIP device.
[1788924390.076] [857359:857360] [BLE] Device 46:A7:4B:A3:0A:BC does not look like a CHIP device.
[1788924390.078] [857359:857360] [BLE] Device 16:2E:74:3F:18:C6 does not look like a CHIP device.
[1788924390.084] [857359:857360] [BLE] Device 5B:0C:B7:4E:2E:09 does not look like a CHIP device.
[1788924390.085] [857359:857360] [BLE] Device 33:9F:73:89:B2:1C does not look like a CHIP device.
[1788924390.090] [857359:857360] [BLE] Device 7B:0B:FF:07:52:DF does not look like a CHIP device.
[1788924390.095] [857359:857360] [BLE] Device 4E:69:14:75:2D:A7 does not look like a CHIP device.
[1788924390.098] [857359:857360] [BLE] Device 57:33:27:08:00:2B does not look like a CHIP device.
[1788924390.108] [857359:857360] [BLE] Device 23:3B:E4:28:A4:0C does not look like a CHIP device.
[1788924390.109] [857359:857360] [BLE] New device scanned: FF:20:DB:D6:D9:90
[1788924390.109] [857359:857360] [BLE] Device discriminator match. Attempting to connect.
[1788924390.114] [857359:857360] [BLE] ChipDeviceScanner has stopped scanning!
[1788924390.298] [857359:857360] [DL] ConnectDevice complete
[1788924390.298] [857359:857360] [BLE] New device connected: FF:20:DB:D6:D9:90
[1788924392.171] [857359:857360] [DL] CHIP service found
[1788924392.171] [857359:857360] [DL] Valid C1 characteristic found
[1788924392.171] [857359:857360] [DL] Valid C2 characteristic found
[1788924392.171] [857359:857360] [DL] New BLE connection: conn=0xffff8404f320 device=FF:20:DB:D6:D9:90 path=/org/bluez/hci0/dev_FF_20_DB_D6_D9_90
[1788924392.172] [857359:857361] [DIS] Closing all BLE connections
[1788924392.172] [857359:857361] [IN] BleConnectionComplete: endPoint 0xaaaab7b94f80
[1788924392.173] [857359:857361] [IN] SecureSession[0xffff8c002c60]: Allocated Type:1 LSID:37659
[1788924392.173] [857359:857361] [SC] Assigned local session key ID 37659
[1788924392.173] [857359:857361] [EM] <<< [E:38762i S:0 M:23679077] (U) Msg TX from D1A4FE0D60D37D53 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1788924392.173] [857359:857361] [IN] Message appended to BLE send queue
[1788924392.173] [857359:857361] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1788924393.028] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924393.029] [857359:857361] [BLE] subscribe complete, ep = 0xaaaab7b94f80
[1788924393.029] [857359:857361] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1788924393.029] [857359:857361] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1788924393.029] [857359:857361] [BLE] local and remote recv window size = 5
[1788924393.029] [857359:857361] [IN] BLE EndPoint 0xaaaab7b94f80 Connection Complete
[1788924393.419] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924393.419] [857359:857361] [EM] >>> [E:38762i S:0 M:241631426] (U) Msg RX from 0:0000000000000000 [0000] to D1A4FE0D60D37D53 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:154)
[1788924393.419] [857359:857361] [EM] Found matching exchange: 38762i, Delegate: 0xffff8c00de80
[1788924393.419] [857359:857361] [SC] Received PBKDF param response
[1788924393.419] [857359:857361] [SC] Peer assigned session ID 55442
[1788924393.419] [857359:857361] [SC] Found MRP parameters in the message
[1788924393.426] [857359:857361] [EM] <<< [E:38762i S:0 M:23679078] (U) Msg TX from D1A4FE0D60D37D53 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1788924393.427] [857359:857361] [SC] Sent spake2p msg1
[1788924393.712] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924393.712] [857359:857361] [EM] >>> [E:38762i S:0 M:241631427] (U) Msg RX from 0:0000000000000000 [0000] to D1A4FE0D60D37D53 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1788924393.712] [857359:857361] [EM] Found matching exchange: 38762i, Delegate: 0xffff8c00de80
[1788924393.712] [857359:857361] [SC] Received spake2p msg2
[1788924393.713] [857359:857361] [EM] <<< [E:38762i S:0 M:23679079] (U) Msg TX from D1A4FE0D60D37D53 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1788924393.714] [857359:857361] [SC] Sent spake2p msg3
[1788924393.906] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924393.907] [857359:857361] [EM] >>> [E:38762i S:0 M:241631428] (U) Msg RX from 0:0000000000000000 [0000] to D1A4FE0D60D37D53 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1788924393.907] [857359:857361] [EM] Found matching exchange: 38762i, Delegate: 0xffff8c00de80
[1788924393.907] [857359:857361] [SC] SecureSession[0xffff8c002c60, LSID:37659]: State change 'kEstablishing' --> 'kActive'
[1788924393.907] [857359:857361] [IN] SecureSession[0xffff8c002c60]: Activated - Type:1 LSID:37659
[1788924393.907] [857359:857361] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:37659 PSID:55442!
[1788924393.907] [857359:857361] [CTL] Remote device completed SPAKE2+ handshake
[1788924393.907] [857359:857361] [TOO] Pairing Success
[1788924393.907] [857359:857361] [TOO] PASE establishment successful
[1788924393.907] [857359:857361] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1788924393.907] [857359:857361] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1788924393.907] [857359:857361] [TOO] Starting commissioning stage 'ReadCommissioningInfo'
[1788924393.907] [857359:857361] [CTL] Sending read requests for commissioning information
[1788924393.908] [857359:857361] [DMG] SendReadRequest ReadClient[0xffff8c00fe90]: Sending Read Request
[1788924393.908] [857359:857361] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1788924393.908] [857359:857361] [EM] <<< [E:38763i S:37659 M:214058673] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:136)
[1788924393.909] [857359:857361] [DMG] MoveToState ReadClient[0xffff8c00fe90]: Moving to [AwaitingIn]
[1788924394.103] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924394.392] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924394.393] [857359:857361] [EM] >>> [E:38763i S:37659 M:215342917] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:253)
[1788924394.393] [857359:857361] [EM] Found matching exchange: 38763i, Delegate: 0xffff8c00fea0
[1788924394.393] [857359:857361] [DMG] ReportDataMessage =
[1788924394.393] [857359:857361] [DMG] {
[1788924394.393] [857359:857361] [DMG]  AttributeReportIBs =
[1788924394.393] [857359:857361] [DMG]  [
[1788924394.393] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.393] [857359:857361] [DMG]          {
[1788924394.393] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.393] [857359:857361] [DMG]                  {
[1788924394.393] [857359:857361] [DMG]                          DataVersion = 0x6f714f44,
[1788924394.393] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.393] [857359:857361] [DMG]                          {
[1788924394.393] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.394] [857359:857361] [DMG]                                  Cluster = 0x28,
[1788924394.394] [857359:857361] [DMG]                                  Attribute = 0x0000_0004,
[1788924394.394] [857359:857361] [DMG]                          }
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]                          Data = 12293 (unsigned),
[1788924394.394] [857359:857361] [DMG]                  },
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]          },
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.394] [857359:857361] [DMG]          {
[1788924394.394] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.394] [857359:857361] [DMG]                  {
[1788924394.394] [857359:857361] [DMG]                          DataVersion = 0x6f714f44,
[1788924394.394] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.394] [857359:857361] [DMG]                          {
[1788924394.394] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.394] [857359:857361] [DMG]                                  Cluster = 0x28,
[1788924394.394] [857359:857361] [DMG]                                  Attribute = 0x0000_0002,
[1788924394.394] [857359:857361] [DMG]                          }
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]                          Data = 5274 (unsigned),
[1788924394.394] [857359:857361] [DMG]                  },
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]          },
[1788924394.394] [857359:857361] [DMG]
[1788924394.394] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.394] [857359:857361] [DMG]          {
[1788924394.395] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.395] [857359:857361] [DMG]                  {
[1788924394.395] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.395] [857359:857361] [DMG]                          {
[1788924394.395] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.395] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.395] [857359:857361] [DMG]                                  Attribute = 0x0000_000C,
[1788924394.395] [857359:857361] [DMG]                          }
[1788924394.395] [857359:857361] [DMG]
[1788924394.395] [857359:857361] [DMG]                          StatusIB =
[1788924394.395] [857359:857361] [DMG]                          {
[1788924394.395] [857359:857361] [DMG]                                  status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1788924394.395] [857359:857361] [DMG]                          },
[1788924394.395] [857359:857361] [DMG]
[1788924394.395] [857359:857361] [DMG]                  },
[1788924394.395] [857359:857361] [DMG]
[1788924394.395] [857359:857361] [DMG]          },
[1788924394.395] [857359:857361] [DMG]
[1788924394.395] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.395] [857359:857361] [DMG]          {
[1788924394.395] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.395] [857359:857361] [DMG]                  {
[1788924394.395] [857359:857361] [DMG]                          DataVersion = 0xe7a1e65c,
[1788924394.395] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.395] [857359:857361] [DMG]                          {
[1788924394.395] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.395] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.396] [857359:857361] [DMG]                                  Attribute = 0x0000_0003,
[1788924394.396] [857359:857361] [DMG]                          }
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]                          Data = 0 (unsigned),
[1788924394.396] [857359:857361] [DMG]                  },
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]          },
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.396] [857359:857361] [DMG]          {
[1788924394.396] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.396] [857359:857361] [DMG]                  {
[1788924394.396] [857359:857361] [DMG]                          DataVersion = 0xe7a1e65c,
[1788924394.396] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.396] [857359:857361] [DMG]                          {
[1788924394.396] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.396] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.396] [857359:857361] [DMG]                                  Attribute = 0x0000_0002,
[1788924394.396] [857359:857361] [DMG]                          }
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]                          Data = 0 (unsigned),
[1788924394.396] [857359:857361] [DMG]                  },
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]          },
[1788924394.396] [857359:857361] [DMG]
[1788924394.396] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.396] [857359:857361] [DMG]          {
[1788924394.396] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.396] [857359:857361] [DMG]                  {
[1788924394.396] [857359:857361] [DMG]                          DataVersion = 0xe7a1e65c,
[1788924394.396] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.396] [857359:857361] [DMG]                          {
[1788924394.397] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.397] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.397] [857359:857361] [DMG]                                  Attribute = 0x0000_0001,
[1788924394.397] [857359:857361] [DMG]                          }
[1788924394.397] [857359:857361] [DMG]
[1788924394.397] [857359:857361] [DMG]                          Data =
[1788924394.397] [857359:857361] [DMG]                          {
[1788924394.397] [857359:857361] [DMG]                                  0x0 = 60 (unsigned),
[1788924394.398] [857359:857361] [DMG]                                  0x1 = 900 (unsigned),
[1788924394.398] [857359:857361] [DMG]                          },
[1788924394.398] [857359:857361] [DMG]                  },
[1788924394.398] [857359:857361] [DMG]
[1788924394.398] [857359:857361] [DMG]          },
[1788924394.398] [857359:857361] [DMG]
[1788924394.398] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.398] [857359:857361] [DMG]          {
[1788924394.398] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.398] [857359:857361] [DMG]                  {
[1788924394.399] [857359:857361] [DMG]                          DataVersion = 0xe7a1e65c,
[1788924394.399] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.399] [857359:857361] [DMG]                          {
[1788924394.399] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.399] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.399] [857359:857361] [DMG]                                  Attribute = 0x0000_0000,
[1788924394.399] [857359:857361] [DMG]                          }
[1788924394.400] [857359:857361] [DMG]
[1788924394.400] [857359:857361] [DMG]                          Data = 0 (unsigned),
[1788924394.400] [857359:857361] [DMG]                  },
[1788924394.400] [857359:857361] [DMG]
[1788924394.400] [857359:857361] [DMG]          },
[1788924394.400] [857359:857361] [DMG]
[1788924394.400] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.400] [857359:857361] [DMG]          {
[1788924394.400] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.400] [857359:857361] [DMG]                  {
[1788924394.401] [857359:857361] [DMG]                          DataVersion = 0xe7a1e65c,
[1788924394.401] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.401] [857359:857361] [DMG]                          {
[1788924394.401] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.401] [857359:857361] [DMG]                                  Cluster = 0x30,
[1788924394.401] [857359:857361] [DMG]                                  Attribute = 0x0000_0004,
[1788924394.401] [857359:857361] [DMG]                          }
[1788924394.401] [857359:857361] [DMG]
[1788924394.401] [857359:857361] [DMG]                          Data = true,
[1788924394.401] [857359:857361] [DMG]                  },
[1788924394.401] [857359:857361] [DMG]
[1788924394.401] [857359:857361] [DMG]          },
[1788924394.401] [857359:857361] [DMG]
[1788924394.401] [857359:857361] [DMG]  ],
[1788924394.401] [857359:857361] [DMG]
[1788924394.401] [857359:857361] [DMG]  SuppressResponse = true,
[1788924394.401] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924394.401] [857359:857361] [DMG] }
[1788924394.402] [857359:857361] [DMG] SendReadRequest ReadClient[0xffff8c00fe90]: Sending Read Request
[1788924394.402] [857359:857361] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1788924394.402] [857359:857361] [EM] <<< [E:38764i S:37659 M:214058674] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:112)
[1788924394.403] [857359:857361] [DMG] MoveToState ReadClient[0xffff8c00fe90]: Moving to [AwaitingIn]
[1788924394.688] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924394.688] [857359:857361] [EM] >>> [E:38764i S:37659 M:215342918] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:208)
[1788924394.688] [857359:857361] [EM] Found matching exchange: 38764i, Delegate: 0xffff8c00fea0
[1788924394.688] [857359:857361] [DMG] ReportDataMessage =
[1788924394.688] [857359:857361] [DMG] {
[1788924394.688] [857359:857361] [DMG]  AttributeReportIBs =
[1788924394.688] [857359:857361] [DMG]  [
[1788924394.688] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.688] [857359:857361] [DMG]          {
[1788924394.688] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.688] [857359:857361] [DMG]                  {
[1788924394.688] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.688] [857359:857361] [DMG]                          {
[1788924394.688] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.688] [857359:857361] [DMG]                                  Cluster = 0x46,
[1788924394.688] [857359:857361] [DMG]                                  Attribute = 0x0000_0002,
[1788924394.688] [857359:857361] [DMG]                          }
[1788924394.688] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]                          StatusIB =
[1788924394.689] [857359:857361] [DMG]                          {
[1788924394.689] [857359:857361] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788924394.689] [857359:857361] [DMG]                          },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]                  },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]          },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.689] [857359:857361] [DMG]          {
[1788924394.689] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.689] [857359:857361] [DMG]                  {
[1788924394.689] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.689] [857359:857361] [DMG]                          {
[1788924394.689] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.689] [857359:857361] [DMG]                                  Cluster = 0x46,
[1788924394.689] [857359:857361] [DMG]                                  Attribute = 0x0000_0001,
[1788924394.689] [857359:857361] [DMG]                          }
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]                          StatusIB =
[1788924394.689] [857359:857361] [DMG]                          {
[1788924394.689] [857359:857361] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788924394.689] [857359:857361] [DMG]                          },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]                  },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]          },
[1788924394.689] [857359:857361] [DMG]
[1788924394.689] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.689] [857359:857361] [DMG]          {
[1788924394.689] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.689] [857359:857361] [DMG]                  {
[1788924394.689] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.689] [857359:857361] [DMG]                          {
[1788924394.690] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.690] [857359:857361] [DMG]                                  Cluster = 0x46,
[1788924394.690] [857359:857361] [DMG]                                  Attribute = 0x0000_0000,
[1788924394.690] [857359:857361] [DMG]                          }
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]                          StatusIB =
[1788924394.690] [857359:857361] [DMG]                          {
[1788924394.690] [857359:857361] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788924394.690] [857359:857361] [DMG]                          },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]                  },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]          },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.690] [857359:857361] [DMG]          {
[1788924394.690] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.690] [857359:857361] [DMG]                  {
[1788924394.690] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.690] [857359:857361] [DMG]                          {
[1788924394.690] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.690] [857359:857361] [DMG]                                  Cluster = 0x46,
[1788924394.690] [857359:857361] [DMG]                                  Attribute = 0x0000_0007,
[1788924394.690] [857359:857361] [DMG]                          }
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]                          StatusIB =
[1788924394.690] [857359:857361] [DMG]                          {
[1788924394.690] [857359:857361] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788924394.690] [857359:857361] [DMG]                          },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]                  },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]          },
[1788924394.690] [857359:857361] [DMG]
[1788924394.690] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.690] [857359:857361] [DMG]          {
[1788924394.691] [857359:857361] [DMG]                  AttributeStatusIB =
[1788924394.691] [857359:857361] [DMG]                  {
[1788924394.691] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.691] [857359:857361] [DMG]                          {
[1788924394.691] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.691] [857359:857361] [DMG]                                  Cluster = 0x46,
[1788924394.691] [857359:857361] [DMG]                                  Attribute = 0x0000_0006,
[1788924394.691] [857359:857361] [DMG]                          }
[1788924394.691] [857359:857361] [DMG]
[1788924394.691] [857359:857361] [DMG]                          StatusIB =
[1788924394.691] [857359:857361] [DMG]                          {
[1788924394.691] [857359:857361] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788924394.691] [857359:857361] [DMG]                          },
[1788924394.691] [857359:857361] [DMG]
[1788924394.691] [857359:857361] [DMG]                  },
[1788924394.691] [857359:857361] [DMG]
[1788924394.691] [857359:857361] [DMG]          },
[1788924394.691] [857359:857361] [DMG]
[1788924394.691] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.692] [857359:857361] [DMG]          {
[1788924394.692] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.692] [857359:857361] [DMG]                  {
[1788924394.692] [857359:857361] [DMG]                          DataVersion = 0x987d9e75,
[1788924394.692] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.692] [857359:857361] [DMG]                          {
[1788924394.692] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.692] [857359:857361] [DMG]                                  Cluster = 0x31,
[1788924394.692] [857359:857361] [DMG]                                  Attribute = 0x0000_0003,
[1788924394.692] [857359:857361] [DMG]                          }
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]                          Data = 20 (unsigned),
[1788924394.692] [857359:857361] [DMG]                  },
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]          },
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]          AttributeReportIB =
[1788924394.692] [857359:857361] [DMG]          {
[1788924394.692] [857359:857361] [DMG]                  AttributeDataIB =
[1788924394.692] [857359:857361] [DMG]                  {
[1788924394.692] [857359:857361] [DMG]                          DataVersion = 0x987d9e75,
[1788924394.692] [857359:857361] [DMG]                          AttributePathIB =
[1788924394.692] [857359:857361] [DMG]                          {
[1788924394.692] [857359:857361] [DMG]                                  Endpoint = 0x0,
[1788924394.692] [857359:857361] [DMG]                                  Cluster = 0x31,
[1788924394.692] [857359:857361] [DMG]                                  Attribute = 0x0000_FFFC,
[1788924394.692] [857359:857361] [DMG]                          }
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]                          Data = 2 (unsigned),
[1788924394.692] [857359:857361] [DMG]                  },
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]          },
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]  ],
[1788924394.692] [857359:857361] [DMG]
[1788924394.692] [857359:857361] [DMG]  SuppressResponse = true,
[1788924394.692] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924394.693] [857359:857361] [DMG] }
[1788924394.693] [857359:857361] [CTL] Ignoring failure to read IsCommissioningWithoutPower: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1788924394.693] [857359:857361] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1788924394.694] [857359:857361] [SVR] OnReadCommissioningInfo - vendorId=0x149A productId=0x3005
[1788924394.694] [857359:857361] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1788924394.694] [857359:857361] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1788924394.694] [857359:857361] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1788924394.694] [857359:857361] [CTL] Performing next commissioning step 'ArmFailSafe'
[1788924394.694] [857359:857361] [TOO] Starting commissioning stage 'ArmFailSafe'
[1788924394.694] [857359:857361] [CTL] Arming failsafe (60 seconds)
[1788924394.694] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924394.694] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924394.695] [857359:857361] [EM] <<< [E:38765i S:37659 M:214058675] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1788924394.696] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924394.978] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924394.979] [857359:857361] [EM] >>> [E:38765i S:37659 M:215342919] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788924394.979] [857359:857361] [EM] Found matching exchange: 38765i, Delegate: 0xffff8c014578
[1788924394.979] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924394.979] [857359:857361] [DMG] InvokeResponseMessage =
[1788924394.979] [857359:857361] [DMG] {
[1788924394.979] [857359:857361] [DMG]  suppressResponse = false,
[1788924394.979] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924394.979] [857359:857361] [DMG]  [
[1788924394.979] [857359:857361] [DMG]          InvokeResponseIB =
[1788924394.979] [857359:857361] [DMG]          {
[1788924394.979] [857359:857361] [DMG]                  CommandDataIB =
[1788924394.979] [857359:857361] [DMG]                  {
[1788924394.979] [857359:857361] [DMG]                          CommandPathIB =
[1788924394.979] [857359:857361] [DMG]                          {
[1788924394.979] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924394.979] [857359:857361] [DMG]                                  ClusterId = 0x30,
[1788924394.979] [857359:857361] [DMG]                                  CommandId = 0x1,
[1788924394.979] [857359:857361] [DMG]                          },
[1788924394.979] [857359:857361] [DMG]
[1788924394.979] [857359:857361] [DMG]                          CommandFields =
[1788924394.979] [857359:857361] [DMG]                          {
[1788924394.979] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924394.979] [857359:857361] [DMG]                                  0x1 = "" (0 chars),
[1788924394.979] [857359:857361] [DMG]                          },
[1788924394.979] [857359:857361] [DMG]                  },
[1788924394.979] [857359:857361] [DMG]
[1788924394.979] [857359:857361] [DMG]          },
[1788924394.979] [857359:857361] [DMG]
[1788924394.979] [857359:857361] [DMG]  ],
[1788924394.980] [857359:857361] [DMG]
[1788924394.980] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924394.980] [857359:857361] [DMG] },
[1788924394.980] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1788924394.980] [857359:857361] [CTL] Received ArmFailSafe response errorCode=0
[1788924394.980] [857359:857361] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1788924394.980] [857359:857361] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1788924394.980] [857359:857361] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1788924394.980] [857359:857361] [TOO] Starting commissioning stage 'ConfigRegulatory'
[1788924394.980] [857359:857361] [CTL] Setting Regulatory Config
[1788924394.980] [857359:857361] [CTL] Device does not support configurable regulatory location
[1788924394.980] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924394.980] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924394.980] [857359:857361] [EM] <<< [E:38766i S:37659 M:214058676] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1788924394.981] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924394.981] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924395.173] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924395.174] [857359:857361] [EM] >>> [E:38766i S:37659 M:215342920] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788924395.174] [857359:857361] [EM] Found matching exchange: 38766i, Delegate: 0xffff8c014048
[1788924395.174] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924395.174] [857359:857361] [DMG] InvokeResponseMessage =
[1788924395.174] [857359:857361] [DMG] {
[1788924395.174] [857359:857361] [DMG]  suppressResponse = false,
[1788924395.174] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924395.174] [857359:857361] [DMG]  [
[1788924395.174] [857359:857361] [DMG]          InvokeResponseIB =
[1788924395.174] [857359:857361] [DMG]          {
[1788924395.174] [857359:857361] [DMG]                  CommandDataIB =
[1788924395.174] [857359:857361] [DMG]                  {
[1788924395.174] [857359:857361] [DMG]                          CommandPathIB =
[1788924395.174] [857359:857361] [DMG]                          {
[1788924395.174] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924395.174] [857359:857361] [DMG]                                  ClusterId = 0x30,
[1788924395.174] [857359:857361] [DMG]                                  CommandId = 0x3,
[1788924395.174] [857359:857361] [DMG]                          },
[1788924395.174] [857359:857361] [DMG]
[1788924395.174] [857359:857361] [DMG]                          CommandFields =
[1788924395.174] [857359:857361] [DMG]                          {
[1788924395.174] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924395.174] [857359:857361] [DMG]                                  0x1 = "" (0 chars),
[1788924395.174] [857359:857361] [DMG]                          },
[1788924395.174] [857359:857361] [DMG]                  },
[1788924395.174] [857359:857361] [DMG]
[1788924395.175] [857359:857361] [DMG]          },
[1788924395.175] [857359:857361] [DMG]
[1788924395.175] [857359:857361] [DMG]  ],
[1788924395.175] [857359:857361] [DMG]
[1788924395.175] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924395.175] [857359:857361] [DMG] },
[1788924395.175] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1788924395.175] [857359:857361] [CTL] Received SetRegulatoryConfig response errorCode=0
[1788924395.175] [857359:857361] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1788924395.175] [857359:857361] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1788924395.175] [857359:857361] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1788924395.175] [857359:857361] [TOO] Starting commissioning stage 'ConfigureTCAcknowledgments'
[1788924395.175] [857359:857361] [CTL] Setting Terms and Conditions
[1788924395.175] [857359:857361] [CTL] Setting Terms and Conditions: Skipped
[1788924395.175] [857359:857361] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'
[1788924395.175] [857359:857361] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1788924395.175] [857359:857361] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1788924395.175] [857359:857361] [TOO] Starting commissioning stage 'SendPAICertificateRequest'
[1788924395.175] [857359:857361] [CTL] Sending request for PAI certificate
[1788924395.175] [857359:857361] [CTL] Sending Certificate Chain request to 0xffff8c00de20 device
[1788924395.175] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924395.175] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924395.176] [857359:857361] [EM] <<< [E:38767i S:37659 M:214058677] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1788924395.176] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924395.176] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924395.370] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924395.565] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924395.758] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924395.758] [857359:857361] [EM] >>> [E:38767i S:37659 M:215342921] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:534)
[1788924395.758] [857359:857361] [EM] Found matching exchange: 38767i, Delegate: 0xffff8c014578
[1788924395.758] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924395.758] [857359:857361] [DMG] InvokeResponseMessage =
[1788924395.758] [857359:857361] [DMG] {
[1788924395.758] [857359:857361] [DMG]  suppressResponse = false,
[1788924395.758] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924395.758] [857359:857361] [DMG]  [
[1788924395.759] [857359:857361] [DMG]          InvokeResponseIB =
[1788924395.759] [857359:857361] [DMG]          {
[1788924395.759] [857359:857361] [DMG]                  CommandDataIB =
[1788924395.759] [857359:857361] [DMG]                  {
[1788924395.759] [857359:857361] [DMG]                          CommandPathIB =
[1788924395.759] [857359:857361] [DMG]                          {
[1788924395.759] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924395.759] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924395.759] [857359:857361] [DMG]                                  CommandId = 0x3,
[1788924395.759] [857359:857361] [DMG]                          },
[1788924395.759] [857359:857361] [DMG]
[1788924395.759] [857359:857361] [DMG]                          CommandFields =
[1788924395.759] [857359:857361] [DMG]                          {
[1788924395.759] [857359:857361] [DMG]                                  0x0 = [
[1788924395.759] [857359:857361] [DMG]                                                  0x30, 0x82, 0x01, 0xd2, 0x30, 0x82, 0x01, 0x77, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x11, 0x00, 0xeb, 0x49, 0xbf, 0xaa, 0x73, 0x8f, 0xa5, 0x5d, 0xa8, 0xeb, 0x1b, 0x36, 0x94, 0x58, 0x3f, 0xec, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x41, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x33, 0x30, 0x39, 0x30, 0x35, 0x30, 0x30, 0x31, 0x39, 0x34, 0x30, 0x5a, 0x18, 0x0f, 0x32, 0x32, 0x32, 0x30, 0x31, 0x30, 0x32, 0x32, 0x30, 0x31, 0x31, 0x39, 0x34, 0x30, 0x5a, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x02, 0x37, 0xc9, 0x8e, 0xc5, 0xfb, 0xfc, 0x70, 0x3b, 0x9c, 0x17, 0x63, 0x4a, 0x94, 0x4a, 0xe1, 0x0e, 0x06, 0x22, 0x2e, 0xab, 0x58, 0x8e, 0x60, 0xe4, 0xc8, 0x8c, 0x71, 0x07, 0xbe, 0xe9, 0xeb, 0xb6, 0x43, 0x36, 0xe5, 0xea, 0x19, 0xf3, 0x4f, 0x69, 0x16, 0x42, 0x63, 0xca, 0xe2, 0x09, 0x7e, 0x65, 0xa5, 0x16, 0xf8, 0xa0, 0x5f, 0xb3, 0x6d, 0x0c, 0x45, 0x1f, 0x3c, 0xa6, 0x50, 0x88, 0x24, 0xa3, 0x66, 0x30, 0x64, 0x
[1788924395.759] [857359:857361] [DMG]                                  ] (470 bytes)
[1788924395.759] [857359:857361] [DMG]                          },
[1788924395.760] [857359:857361] [DMG]                  },
[1788924395.760] [857359:857361] [DMG]
[1788924395.760] [857359:857361] [DMG]          },
[1788924395.760] [857359:857361] [DMG]
[1788924395.760] [857359:857361] [DMG]  ],
[1788924395.760] [857359:857361] [DMG]
[1788924395.760] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924395.760] [857359:857361] [DMG] },
[1788924395.760] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1788924395.760] [857359:857361] [CTL] Received certificate chain from the device
[1788924395.760] [857359:857361] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1788924395.760] [857359:857361] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1788924395.760] [857359:857361] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1788924395.760] [857359:857361] [TOO] Starting commissioning stage 'SendDACCertificateRequest'
[1788924395.760] [857359:857361] [CTL] Sending request for DAC certificate
[1788924395.760] [857359:857361] [CTL] Sending Certificate Chain request to 0xffff8c00de20 device
[1788924395.760] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924395.760] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924395.760] [857359:857361] [EM] <<< [E:38768i S:37659 M:214058678] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1788924395.761] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924395.761] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924395.956] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924396.247] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924396.636] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924396.637] [857359:857361] [EM] >>> [E:38768i S:37659 M:215342922] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:545)
[1788924396.637] [857359:857361] [EM] Found matching exchange: 38768i, Delegate: 0xffff8c014048
[1788924396.637] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924396.637] [857359:857361] [DMG] InvokeResponseMessage =
[1788924396.637] [857359:857361] [DMG] {
[1788924396.637] [857359:857361] [DMG]  suppressResponse = false,
[1788924396.637] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924396.637] [857359:857361] [DMG]  [
[1788924396.637] [857359:857361] [DMG]          InvokeResponseIB =
[1788924396.637] [857359:857361] [DMG]          {
[1788924396.637] [857359:857361] [DMG]                  CommandDataIB =
[1788924396.638] [857359:857361] [DMG]                  {
[1788924396.638] [857359:857361] [DMG]                          CommandPathIB =
[1788924396.638] [857359:857361] [DMG]                          {
[1788924396.638] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924396.638] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924396.638] [857359:857361] [DMG]                                  CommandId = 0x3,
[1788924396.638] [857359:857361] [DMG]                          },
[1788924396.638] [857359:857361] [DMG]
[1788924396.638] [857359:857361] [DMG]                          CommandFields =
[1788924396.638] [857359:857361] [DMG]                          {
[1788924396.638] [857359:857361] [DMG]                                  0x0 = [
[1788924396.639] [857359:857361] [DMG]                                                  0x30, 0x82, 0x01, 0xdd, 0x30, 0x82, 0x01, 0x83, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x10, 0x0e, 0xcb, 0x29, 0xb3, 0x32, 0x16, 0xa9, 0x9d, 0x31, 0x83, 0xfc, 0x5d, 0xfe, 0xc9, 0x24, 0xf9, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x34, 0x31, 0x30, 0x32, 0x31, 0x30, 0x35, 0x31, 0x30, 0x32, 0x38, 0x5a, 0x18, 0x0f, 0x32, 0x31, 0x32, 0x34, 0x30, 0x39, 0x32, 0x37, 0x30, 0x36, 0x31, 0x30, 0x32, 0x38, 0x5a, 0x30, 0x48, 0x31, 0x1a, 0x30, 0x18, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x11, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x41, 0x43, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x30, 0x36, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xe9, 0x56, 0x79, 0x4b, 0x3d, 0x63, 0xe4, 0xe6, 0x32, 0xb1, 0x60, 0xac, 0xb2, 0x3d, 0xe6, 0x50, 0x47, 0x76, 0x1f, 0xe6, 0xdc, 0x20, 0xe2, 0x16, 0x11, 0xd1, 0x7e, 0x9e, 0x7b, 0x3d, 0x73, 0x5c, 0xa9, 0xf7, 0x3a, 0x60, 0x84, 0xca, 0x2d, 0x61, 0x07, 0x29, 0x4b, 0xbb, 0x0a, 0xf9, 0xbd, 0xeb, 0x92, 0x98, 0x
[1788924396.639] [857359:857361] [DMG]                                  ] (481 bytes)
[1788924396.639] [857359:857361] [DMG]                          },
[1788924396.639] [857359:857361] [DMG]                  },
[1788924396.639] [857359:857361] [DMG]
[1788924396.639] [857359:857361] [DMG]          },
[1788924396.639] [857359:857361] [DMG]
[1788924396.640] [857359:857361] [DMG]  ],
[1788924396.640] [857359:857361] [DMG]
[1788924396.640] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924396.640] [857359:857361] [DMG] },
[1788924396.640] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1788924396.640] [857359:857361] [CTL] Received certificate chain from the device
[1788924396.640] [857359:857361] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1788924396.640] [857359:857361] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1788924396.640] [857359:857361] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1788924396.641] [857359:857361] [TOO] Starting commissioning stage 'SendAttestationRequest'
[1788924396.641] [857359:857361] [CTL] Sending Attestation Request to the device.
[1788924396.641] [857359:857361] [CTL] Sending Attestation request to 0xffff8c00de20 device
[1788924396.641] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924396.641] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924396.641] [857359:857361] [EM] <<< [E:38769i S:37659 M:214058679] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1788924396.642] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924396.642] [857359:857361] [CTL] Sent Attestation request, waiting for the Attestation Information
[1788924396.642] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924397.028] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924397.223] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924397.514] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924397.514] [857359:857361] [EM] >>> [E:38769i S:37659 M:215342923] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:554)
[1788924397.514] [857359:857361] [EM] Found matching exchange: 38769i, Delegate: 0xffff8c014578
[1788924397.514] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924397.515] [857359:857361] [DMG] InvokeResponseMessage =
[1788924397.515] [857359:857361] [DMG] {
[1788924397.515] [857359:857361] [DMG]  suppressResponse = false,
[1788924397.515] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924397.515] [857359:857361] [DMG]  [
[1788924397.515] [857359:857361] [DMG]          InvokeResponseIB =
[1788924397.515] [857359:857361] [DMG]          {
[1788924397.515] [857359:857361] [DMG]                  CommandDataIB =
[1788924397.515] [857359:857361] [DMG]                  {
[1788924397.515] [857359:857361] [DMG]                          CommandPathIB =
[1788924397.515] [857359:857361] [DMG]                          {
[1788924397.515] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924397.516] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924397.516] [857359:857361] [DMG]                                  CommandId = 0x1,
[1788924397.516] [857359:857361] [DMG]                          },
[1788924397.516] [857359:857361] [DMG]
[1788924397.516] [857359:857361] [DMG]                          CommandFields =
[1788924397.516] [857359:857361] [DMG]                          {
[1788924397.516] [857359:857361] [DMG]                                  0x0 = [
[1788924397.516] [857359:857361] [DMG]                                                  0x15, 0x31, 0x01, 0x7b, 0x01, 0x30, 0x82, 0x01, 0x77, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x01, 0x68, 0x30, 0x82, 0x01, 0x64, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x81, 0xd0, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x81, 0xc2, 0x04, 0x81, 0xbf, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0x9a, 0x14, 0x36, 0x02, 0x05, 0x05, 0x30, 0x05, 0x15, 0x30, 0x05, 0x25, 0x30, 0x05, 0x35, 0x30, 0x05, 0x45, 0x30, 0x05, 0x55, 0x30, 0x05, 0x65, 0x30, 0x05, 0x75, 0x30, 0x05, 0x85, 0x30, 0x05, 0x95, 0x30, 0x05, 0xa5, 0x30, 0x05, 0xb5, 0x30, 0x05, 0xc5, 0x30, 0x05, 0xd5, 0x30, 0x05, 0xe5, 0x30, 0x05, 0xf5, 0x30, 0x05, 0x05, 0x40, 0x05, 0x15, 0x40, 0x05, 0x25, 0x40, 0x05, 0x35, 0x40, 0x05, 0x45, 0x40, 0x05, 0x55, 0x40, 0x05, 0x65, 0x40, 0x05, 0x75, 0x40, 0x05, 0x85, 0x40, 0x05, 0x95, 0x40, 0x05, 0xa5, 0x40, 0x05, 0xb5, 0x40, 0x05, 0xc5, 0x40, 0x05, 0xd5, 0x40, 0x05, 0xe5, 0x40, 0x05, 0xf5, 0x40, 0x05, 0x05, 0x42, 0x05, 0x15, 0x42, 0x05, 0x25, 0x42, 0x05, 0x35, 0x42, 0x18, 0x25, 0x03, 0x02, 0x02, 0x2c, 0x04, 0x13, 0x46, 0x41, 0x4d, 0x32, 0x32, 0x36, 0x34, 0x39, 0x37, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x24, 0x05, 0x00, 0x24, 0x06, 0x00, 0x24, 0x07, 0x01, 0x24, 0x08, 0x02, 0x25, 0x09, 0x70, 0x14, 0x25, 0x0a, 0x06, 0x80, 0x36, 0x0b, 0x10, 0x14, 0xe9, 0x16, 0x0d, 0xc4, 0x17, 0xf7, 0x41, 0x9c, 0x95, 0x32, 0x0b, 0xbf, 0x36, 0x56, 0x71, 0x93, 0x3f, 0xf3, 0x12, 0x22, 0x18, 0x18, 0x31, 0x7d, 0x30, 0x7b, 0x02, 0x01, 0x03, 0x80, 0x14, 0xfe, 0x34, 0x3f, 0x95, 0x99, 0x47, 0x76, 0x3b, 0x61, 0xee, 0x45, 0x39, 0x13, 0x13, 0x38, 0x49, 0x4f, 0x
[1788924397.517] [857359:857361] [DMG]                                  ] (423 bytes)
[1788924397.517] [857359:857361] [DMG]                                  0x1 = [
[1788924397.517] [857359:857361] [DMG]                                                  0x61, 0xdc, 0xad, 0x7d, 0xe7, 0x19, 0xf6, 0xcf, 0x47, 0x81, 0xf8, 0xa5, 0xaf, 0xb2, 0x64, 0xaf, 0x6b, 0x88, 0xfc, 0x43, 0x2d, 0x8e, 0x0b, 0xd0, 0x89, 0xac, 0xba, 0xa8, 0x60, 0xa8, 0x5f, 0xd4, 0xc5, 0x20, 0x39, 0x0d, 0xb8, 0x75, 0xe1, 0x22, 0xb5, 0x73, 0xa9, 0x4e, 0x45, 0xb4, 0x5f, 0x0c, 0x7d, 0x05, 0x65, 0x4b, 0xb0, 0x9e, 0x76, 0x07, 0xf8, 0xad, 0x56, 0x67, 0x92, 0xd6, 0x52, 0x14,
[1788924397.517] [857359:857361] [DMG]                                  ] (64 bytes)
[1788924397.517] [857359:857361] [DMG]                          },
[1788924397.517] [857359:857361] [DMG]                  },
[1788924397.517] [857359:857361] [DMG]
[1788924397.517] [857359:857361] [DMG]          },
[1788924397.517] [857359:857361] [DMG]
[1788924397.517] [857359:857361] [DMG]  ],
[1788924397.518] [857359:857361] [DMG]
[1788924397.518] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924397.518] [857359:857361] [DMG] },
[1788924397.518] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1788924397.518] [857359:857361] [CTL] Received Attestation Information from the device
[1788924397.518] [857359:857361] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1788924397.518] [857359:857361] [CTL] AutoCommissioner setting attestationElements buffer size 423/423
[1788924397.518] [857359:857361] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1788924397.518] [857359:857361] [CTL] Performing next commissioning step 'AttestationVerification'
[1788924397.518] [857359:857361] [TOO] Starting commissioning stage 'AttestationVerification'
[1788924397.518] [857359:857361] [CTL] Verifying Device Attestation information received from the device
[1788924397.532] [857359:857361] [-] Device candidate DAC chain details:
[1788924397.532] [857359:857361] [-] --> DAC's VID: 0x1470, PID: 0x8006
[1788924397.532] [857359:857361] [-] ==== DAC certificate considered (481 bytes) ====
[1788924397.532] [857359:857361] [-] -----BEGIN CERTIFICATE-----
[1788924397.532] [857359:857361] [-] MIIB3TCCAYOgAwIBAgIQDsspszIWqZ0xg/xd/skk+TAKBggqhkjOPQQDAjA1MR0w
[1788924397.532] [857359:857361] [-] GwYDVQQDDBRIT1BFUkYgTWF0dGVyIFBBSSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0
[1788924397.532] [857359:857361] [-] NzAwIBcNMjQxMDIxMDUxMDI4WhgPMjEyNDA5MjcwNjEwMjhaMEgxGjAYBgNVBAMM
[1788924397.532] [857359:857361] [-] EUhPUEVSRiBNYXR0ZXIgREFDMRQwEgYKKwYBBAGConwCAQwEMTQ3MDEUMBIGCisG
[1788924397.532] [857359:857361] [-] AQQBgqJ8AgIMBDgwMDYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATpVnlLPWPk
[1788924397.532] [857359:857361] [-] 5jKxYKyyPeZQR3Yf5twg4hYR0X6eez1zXKn3OmCEyi1hBylLuwr5veuSmLR/fBFz
[1788924397.532] [857359:857361] [-] ADmydjbJoqCOo2AwXjAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaAFOu0mvEt1SNX
[1788924397.532] [857359:857361] [-] vT5a0j1vRwbQv5+aMB0GA1UdDgQWBBScROSpadKqznYFUcvoTNvpaDk8vDAOBgNV
[1788924397.532] [857359:857361] [-] HQ8BAf8EBAMCB4AwCgYIKoZIzj0EAwIDSAAwRQIhAPd+rIia1s69ZfGEi/Q1eYUJ
[1788924397.532] [857359:857361] [-] w9O4F6M6vf5wrTWCulbUAiAC9YZTeZWzo3vmoh8zdbCkIaiEmtPjgQ9ybO0Optbx
[1788924397.532] [857359:857361] [-] Lg==
[1788924397.532] [857359:857361] [-] -----END CERTIFICATE-----
[1788924397.533] [857359:857361] [-] --> DAC certificate SKID: 9C:44:E4:A9:69:D2:AA:CE:76:05:51:CB:E8:4C:DB:E9:68:39:3C:BC
[1788924397.534] [857359:857361] [-] --> DAC certificate AKID: EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
[1788924397.535] [857359:857361] [-] ==== PAI certificate considered (470 bytes) ====
[1788924397.535] [857359:857361] [-] -----BEGIN CERTIFICATE-----
[1788924397.535] [857359:857361] [-] MIIB0jCCAXegAwIBAgIRAOtJv6pzj6VdqOsbNpRYP+wwCgYIKoZIzj0EAwIwNTEd
[1788924397.535] [857359:857361] [-] MBsGA1UEAwwUSE9QRVJGIE1hdHRlciBQQUEgMDExFDASBgorBgEEAYKifAIBDAQx
[1788924397.535] [857359:857361] [-] NDcwMCAXDTIzMDkwNTAwMTk0MFoYDzIyMjAxMDIyMDExOTQwWjA1MR0wGwYDVQQD
[1788924397.535] [857359:857361] [-] DBRIT1BFUkYgTWF0dGVyIFBBSSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0NzAwWTAT
[1788924397.535] [857359:857361] [-] BgcqhkjOPQIBBggqhkjOPQMBBwNCAAQCN8mOxfv8cDucF2NKlErhDgYiLqtYjmDk
[1788924397.535] [857359:857361] [-] yIxxB77p67ZDNuXqGfNPaRZCY8riCX5lpRb4oF+zbQxFHzymUIgko2YwZDASBgNV
[1788924397.535] [857359:857361] [-] HRMBAf8ECDAGAQH/AgEAMB8GA1UdIwQYMBaAFOkWDcQX90GclTILvzZWcZM/8xIi
[1788924397.535] [857359:857361] [-] MB0GA1UdDgQWBBTrtJrxLdUjV70+WtI9b0cG0L+fmjAOBgNVHQ8BAf8EBAMCAQYw
[1788924397.535] [857359:857361] [-] CgYIKoZIzj0EAwIDSQAwRgIhAJmF3MWaAB3+WFav89D3a0KoDZ+7c4SGmJtjDdyz
[1788924397.535] [857359:857361] [-] CPaCAiEA8DfnzFMaVz8QaDyI/ygdCGEPMBbpvHxx9KNEiJs7gcE=
[1788924397.535] [857359:857361] [-] -----END CERTIFICATE-----
[1788924397.536] [857359:857361] [-] --> PAI certificate SKID: EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
[1788924397.537] [857359:857361] [-] --> PAI certificate AKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788924397.543] [857359:857361] [-] ==== PAA certificate considered (466 bytes) ====
[1788924397.543] [857359:857361] [-] -----BEGIN CERTIFICATE-----
[1788924397.543] [857359:857361] [-] MIIBzjCCAXSgAwIBAgIRAMB+YpaZQeu05JIuF/AMsiYwCgYIKoZIzj0EAwIwNTEd
[1788924397.543] [857359:857361] [-] MBsGA1UEAwwUSE9QRVJGIE1hdHRlciBQQUEgMDExFDASBgorBgEEAYKifAIBDAQx
[1788924397.543] [857359:857361] [-] NDcwMCAXDTIzMDgyNTA1Mjk1N1oYDzIyMjMwNzA4MDYyOTU3WjA1MR0wGwYDVQQD
[1788924397.543] [857359:857361] [-] DBRIT1BFUkYgTWF0dGVyIFBBQSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0NzAwWTAT
[1788924397.543] [857359:857361] [-] BgcqhkjOPQIBBggqhkjOPQMBBwNCAATVxJPVN3fr7vg9sOX24AO3WyMLWN/O9u5Z
[1788924397.543] [857359:857361] [-] pjjquJNYiPXVziNj1Yq7o1fFT+JJ/V8gEkq3az3CMfTgr5A3DhHko2MwYTAPBgNV
[1788924397.543] [857359:857361] [-] HRMBAf8EBTADAQH/MB0GA1UdDgQWBBTpFg3EF/dBnJUyC782VnGTP/MSIjAOBgNV
[1788924397.543] [857359:857361] [-] HQ8BAf8EBAMCAYYwHwYDVR0jBBgwFoAU6RYNxBf3QZyVMgu/NlZxkz/zEiIwCgYI
[1788924397.543] [857359:857361] [-] KoZIzj0EAwIDSAAwRQIhAMghj3vry4WnuZhyPK8ZGqyFG2aNdKkJCqwy/4SkcHT7
[1788924397.543] [857359:857361] [-] AiBxxCLcAC5bDcze/6tJcCuLX5vWaVQYw6IVwBwciEo+rw==
[1788924397.543] [857359:857361] [-] -----END CERTIFICATE-----
[1788924397.544] [857359:857361] [-] --> PAA certificate SKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788924397.545] [857359:857361] [-] --> PAA certificate AKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788924397.552] [857359:857361] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1788924397.552] [857359:857361] [-] Device certification declaration details:
[1788924397.552] [857359:857361] [-] --> VID: 0x149A
[1788924397.553] [857359:857361] [-] --> Device type ID: 0x0000_0202
[1788924397.553] [857359:857361] [-] --> Certification type: 2 (Certified device)
[1788924397.553] [857359:857361] [-] --> DAC origin VID: 0x1470, PID: 0x8006
[1788924397.553] [857359:857361] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1788924397.553] [857359:857361] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1788924397.553] [857359:857361] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1788924397.553] [857359:857361] [TOO] Starting commissioning stage 'AttestationRevocationCheck'
[1788924397.553] [857359:857361] [CTL] Verifying the device's DAC chain revocation status
[1788924397.553] [857359:857361] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1788924397.553] [857359:857361] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1788924397.553] [857359:857361] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1788924397.553] [857359:857361] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1788924397.553] [857359:857361] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1788924397.553] [857359:857361] [TOO] Starting commissioning stage 'SendOpCertSigningRequest'
[1788924397.553] [857359:857361] [CTL] Sending CSR request to 0xffff8c00de20 device
[1788924397.553] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924397.553] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924397.553] [857359:857361] [EM] <<< [E:38770i S:37659 M:214058680] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1788924397.554] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924397.554] [857359:857361] [CTL] Sent CSR request, waiting for the CSR
[1788924397.554] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924397.711] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924397.904] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924397.905] [857359:857361] [EM] >>> [E:38770i S:37659 M:215342924] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1788924397.905] [857359:857361] [EM] Found matching exchange: 38770i, Delegate: 0xffff8c014048
[1788924397.905] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924397.905] [857359:857361] [DMG] InvokeResponseMessage =
[1788924397.905] [857359:857361] [DMG] {
[1788924397.905] [857359:857361] [DMG]  suppressResponse = false,
[1788924397.905] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924397.905] [857359:857361] [DMG]  [
[1788924397.906] [857359:857361] [DMG]          InvokeResponseIB =
[1788924397.906] [857359:857361] [DMG]          {
[1788924397.906] [857359:857361] [DMG]                  CommandDataIB =
[1788924397.906] [857359:857361] [DMG]                  {
[1788924397.906] [857359:857361] [DMG]                          CommandPathIB =
[1788924397.906] [857359:857361] [DMG]                          {
[1788924397.906] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924397.906] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924397.906] [857359:857361] [DMG]                                  CommandId = 0x5,
[1788924397.907] [857359:857361] [DMG]                          },
[1788924397.907] [857359:857361] [DMG]
[1788924397.907] [857359:857361] [DMG]                          CommandFields =
[1788924397.907] [857359:857361] [DMG]                          {
[1788924397.907] [857359:857361] [DMG]                                  0x0 = [
[1788924397.907] [857359:857361] [DMG]                                                  0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x09, 0x8c, 0x2e, 0xbe, 0x44, 0xc9, 0x11, 0x52, 0xc7, 0xdc, 0x7e, 0x7c, 0x95, 0x5a, 0xcb, 0x3f, 0xde, 0x6d, 0x44, 0xd0, 0x02, 0x59, 0x2b, 0xbf, 0xcc, 0x01, 0xca, 0x86, 0x97, 0xfb, 0xd5, 0x5d, 0x1b, 0x24, 0xe6, 0x85, 0x3a, 0x66, 0x54, 0x46, 0x2c, 0x77, 0xc4, 0x7b, 0x77, 0xcf, 0x38, 0x18, 0xba, 0x45, 0x44, 0x0b, 0xf3, 0x3f, 0xe3, 0x66, 0x9a, 0x73, 0x2f, 0xeb, 0x4c, 0x56, 0xce, 0xa5, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x21, 0x00, 0xfd, 0x8c, 0xaa, 0x5b, 0x7b, 0x74, 0xbe, 0x9a, 0x1f, 0x06, 0xd4, 0xc4, 0xd4, 0x4a, 0x79, 0xb6, 0x6a, 0x1c, 0xaf, 0xe6, 0xec, 0xdb, 0xf4, 0xcc, 0xc2, 0x7e, 0x28, 0xf1, 0x53, 0x2d, 0x28, 0x8e, 0x02, 0x20, 0x0c, 0x9e, 0x91, 0x7b, 0xdb, 0x8c, 0x33, 0x77, 0xb1, 0x3b, 0x34, 0xa3, 0x8a, 0x2b, 0x08, 0x68, 0x70, 0x78, 0x9a, 0xe4, 0xa4, 0x5e, 0x5f, 0x72, 0xa6, 0x22, 0x26, 0xc3, 0xad, 0xb7, 0xa1, 0x3a, 0x30, 0x02, 0x20, 0x8c, 0xfa, 0x8f, 0xd5, 0x1a, 0x81, 0xb1, 0x40, 0xc4, 0xd7, 0x39, 0xdb, 0x75, 0x28, 0xce, 0x47, 0x92, 0x33, 0xe3, 0xac, 0xf3, 0x08, 0xd1, 0x8b, 0x43, 0xb5, 0xfc, 0xeb, 0xd8, 0xb8, 0xd7, 0x28, 0x18,
[1788924397.908] [857359:857361] [DMG]                                  ] (261 bytes)
[1788924397.908] [857359:857361] [DMG]                                  0x1 = [
[1788924397.908] [857359:857361] [DMG]                                                  0x99, 0xa9, 0xf1, 0x0c, 0x98, 0xf3, 0x0d, 0x6b, 0xa0, 0xde, 0xd9, 0x8b, 0x45, 0x70, 0xfa, 0xab, 0x7e, 0xe7, 0x87, 0x4f, 0x23, 0x34, 0xb1, 0x93, 0x3b, 0x19, 0xb7, 0x2c, 0x3e, 0xe4, 0x17, 0x3d, 0x80, 0xae, 0x3e, 0xf1, 0x44, 0x3c, 0x34, 0x45, 0x28, 0x64, 0x7f, 0x70, 0x87, 0x53, 0xca, 0xa8, 0xb0, 0xed, 0x78, 0xca, 0x03, 0x62, 0xbf, 0xb8, 0x61, 0x9d, 0xb8, 0xfa, 0xbd, 0xbb, 0xf2, 0x21,
[1788924397.908] [857359:857361] [DMG]                                  ] (64 bytes)
[1788924397.908] [857359:857361] [DMG]                          },
[1788924397.908] [857359:857361] [DMG]                  },
[1788924397.908] [857359:857361] [DMG]
[1788924397.908] [857359:857361] [DMG]          },
[1788924397.909] [857359:857361] [DMG]
[1788924397.909] [857359:857361] [DMG]  ],
[1788924397.909] [857359:857361] [DMG]
[1788924397.909] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924397.909] [857359:857361] [DMG] },
[1788924397.909] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1788924397.909] [857359:857361] [CTL] Received certificate signing request from the device
[1788924397.909] [857359:857361] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1788924397.909] [857359:857361] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1788924397.909] [857359:857361] [CTL] Performing next commissioning step 'ValidateCSR'
[1788924397.909] [857359:857361] [TOO] Starting commissioning stage 'ValidateCSR'
[1788924397.918] [857359:857361] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1788924397.918] [857359:857361] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1788924397.918] [857359:857361] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1788924397.918] [857359:857361] [TOO] Starting commissioning stage 'GenerateNOCChain'
[1788924397.918] [857359:857361] [CTL] Getting certificate chain for the device from the issuer
[1788924397.920] [857359:857361] [CTL] Verifying Certificate Signing Request
[1788924397.922] [857359:857361] [CTL] Generating NOC
[1788924397.923] [857359:857361] [CTL] Providing certificate chain to the commissioner
[1788924397.923] [857359:857361] [CTL] Received callback from the CA for NOC Chain generation. Status: Success
[1788924397.923] [857359:857361] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1788924397.923] [857359:857361] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1788924397.923] [857359:857361] [TOO] Starting commissioning stage 'SendTrustedRootCert'
[1788924397.923] [857359:857361] [CTL] Sending root certificate to the device
[1788924397.923] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924397.923] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924397.923] [857359:857361] [EM] <<< [E:38771i S:37659 M:214058681] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1788924397.924] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924397.924] [857359:857361] [CTL] Sent root certificate to the device
[1788924397.924] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924398.294] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924398.294] [857359:857361] [EM] >>> [E:38771i S:37659 M:215342925] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1788924398.294] [857359:857361] [EM] Found matching exchange: 38771i, Delegate: 0xffff8c014578
[1788924398.295] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924398.295] [857359:857361] [DMG] InvokeResponseMessage =
[1788924398.295] [857359:857361] [DMG] {
[1788924398.295] [857359:857361] [DMG]  suppressResponse = false,
[1788924398.295] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924398.295] [857359:857361] [DMG]  [
[1788924398.295] [857359:857361] [DMG]          InvokeResponseIB =
[1788924398.295] [857359:857361] [DMG]          {
[1788924398.295] [857359:857361] [DMG]                  CommandStatusIB =
[1788924398.295] [857359:857361] [DMG]                  {
[1788924398.295] [857359:857361] [DMG]                          CommandPathIB =
[1788924398.296] [857359:857361] [DMG]                          {
[1788924398.296] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924398.296] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924398.296] [857359:857361] [DMG]                                  CommandId = 0xb,
[1788924398.296] [857359:857361] [DMG]                          },
[1788924398.296] [857359:857361] [DMG]
[1788924398.296] [857359:857361] [DMG]                          StatusIB =
[1788924398.296] [857359:857361] [DMG]                          {
[1788924398.296] [857359:857361] [DMG]                                  status = 0x00 (SUCCESS),
[1788924398.296] [857359:857361] [DMG]                          },
[1788924398.297] [857359:857361] [DMG]
[1788924398.297] [857359:857361] [DMG]                  },
[1788924398.297] [857359:857361] [DMG]
[1788924398.297] [857359:857361] [DMG]          },
[1788924398.297] [857359:857361] [DMG]
[1788924398.297] [857359:857361] [DMG]  ],
[1788924398.297] [857359:857361] [DMG]
[1788924398.297] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924398.297] [857359:857361] [DMG] },
[1788924398.297] [857359:857361] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1788924398.297] [857359:857361] [CTL] Device confirmed that it has received the root certificate
[1788924398.298] [857359:857361] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1788924398.298] [857359:857361] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1788924398.298] [857359:857361] [CTL] Performing next commissioning step 'SendNOC'
[1788924398.298] [857359:857361] [TOO] Starting commissioning stage 'SendNOC'
[1788924398.298] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924398.298] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924398.298] [857359:857361] [EM] <<< [E:38772i S:37659 M:214058682] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1788924398.299] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924398.299] [857359:857361] [CTL] Sent operational certificate to the device
[1788924398.300] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924399.073] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924399.074] [857359:857361] [EM] >>> [E:38772i S:37659 M:215342926] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788924399.074] [857359:857361] [EM] Found matching exchange: 38772i, Delegate: 0xffff8c014048
[1788924399.074] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924399.074] [857359:857361] [DMG] InvokeResponseMessage =
[1788924399.074] [857359:857361] [DMG] {
[1788924399.074] [857359:857361] [DMG]  suppressResponse = false,
[1788924399.074] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924399.074] [857359:857361] [DMG]  [
[1788924399.074] [857359:857361] [DMG]          InvokeResponseIB =
[1788924399.074] [857359:857361] [DMG]          {
[1788924399.075] [857359:857361] [DMG]                  CommandDataIB =
[1788924399.075] [857359:857361] [DMG]                  {
[1788924399.075] [857359:857361] [DMG]                          CommandPathIB =
[1788924399.075] [857359:857361] [DMG]                          {
[1788924399.075] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924399.075] [857359:857361] [DMG]                                  ClusterId = 0x3e,
[1788924399.075] [857359:857361] [DMG]                                  CommandId = 0x8,
[1788924399.075] [857359:857361] [DMG]                          },
[1788924399.075] [857359:857361] [DMG]
[1788924399.075] [857359:857361] [DMG]                          CommandFields =
[1788924399.076] [857359:857361] [DMG]                          {
[1788924399.076] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924399.076] [857359:857361] [DMG]                                  0x1 = 1 (unsigned),
[1788924399.076] [857359:857361] [DMG]                          },
[1788924399.076] [857359:857361] [DMG]                  },
[1788924399.076] [857359:857361] [DMG]
[1788924399.076] [857359:857361] [DMG]          },
[1788924399.076] [857359:857361] [DMG]
[1788924399.076] [857359:857361] [DMG]  ],
[1788924399.076] [857359:857361] [DMG]
[1788924399.076] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924399.076] [857359:857361] [DMG] },
[1788924399.077] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1788924399.077] [857359:857361] [CTL] Device returned status 0 on receiving the NOC
[1788924399.077] [857359:857361] [CTL] Operational credentials provisioned on device 0xffff8c00de20
[1788924399.077] [857359:857361] [TOO] Secure Pairing Success
[1788924399.077] [857359:857361] [TOO] CASE establishment successful
[1788924399.077] [857359:857361] [CTL] Successfully finished commissioning step 'SendNOC'
[1788924399.077] [857359:857361] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1788924399.077] [857359:857361] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1788924399.077] [857359:857361] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1788924399.077] [857359:857361] [TOO] Starting commissioning stage 'ThreadNetworkSetup'
[1788924399.077] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924399.077] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924399.078] [857359:857361] [EM] <<< [E:38773i S:37659 M:214058683] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:176)
[1788924399.079] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924399.079] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924399.269] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924399.269] [857359:857361] [EM] >>> [E:38773i S:37659 M:215342927] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788924399.270] [857359:857361] [EM] Found matching exchange: 38773i, Delegate: 0xffff8c014578
[1788924399.270] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924399.270] [857359:857361] [DMG] InvokeResponseMessage =
[1788924399.270] [857359:857361] [DMG] {
[1788924399.270] [857359:857361] [DMG]  suppressResponse = false,
[1788924399.270] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924399.270] [857359:857361] [DMG]  [
[1788924399.270] [857359:857361] [DMG]          InvokeResponseIB =
[1788924399.270] [857359:857361] [DMG]          {
[1788924399.270] [857359:857361] [DMG]                  CommandDataIB =
[1788924399.270] [857359:857361] [DMG]                  {
[1788924399.270] [857359:857361] [DMG]                          CommandPathIB =
[1788924399.271] [857359:857361] [DMG]                          {
[1788924399.271] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924399.271] [857359:857361] [DMG]                                  ClusterId = 0x31,
[1788924399.271] [857359:857361] [DMG]                                  CommandId = 0x5,
[1788924399.271] [857359:857361] [DMG]                          },
[1788924399.271] [857359:857361] [DMG]
[1788924399.271] [857359:857361] [DMG]                          CommandFields =
[1788924399.271] [857359:857361] [DMG]                          {
[1788924399.271] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924399.271] [857359:857361] [DMG]                                  0x2 = 0 (unsigned),
[1788924399.271] [857359:857361] [DMG]                          },
[1788924399.271] [857359:857361] [DMG]                  },
[1788924399.272] [857359:857361] [DMG]
[1788924399.272] [857359:857361] [DMG]          },
[1788924399.272] [857359:857361] [DMG]
[1788924399.272] [857359:857361] [DMG]  ],
[1788924399.272] [857359:857361] [DMG]
[1788924399.272] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924399.272] [857359:857361] [DMG] },
[1788924399.272] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1788924399.272] [857359:857361] [CTL] Received NetworkConfig response, networkingStatus=0
[1788924399.272] [857359:857361] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1788924399.272] [857359:857361] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1788924399.272] [857359:857361] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1788924399.272] [857359:857361] [TOO] Starting commissioning stage 'FailsafeBeforeThreadEnable'
[1788924399.272] [857359:857361] [CTL] Arming failsafe (94 seconds)
[1788924399.273] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924399.273] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924399.273] [857359:857361] [EM] <<< [E:38774i S:37659 M:214058684] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1788924399.274] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924399.274] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924399.464] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924399.464] [857359:857361] [EM] >>> [E:38774i S:37659 M:215342928] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788924399.465] [857359:857361] [EM] Found matching exchange: 38774i, Delegate: 0xffff8c014048
[1788924399.465] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924399.465] [857359:857361] [DMG] InvokeResponseMessage =
[1788924399.465] [857359:857361] [DMG] {
[1788924399.465] [857359:857361] [DMG]  suppressResponse = false,
[1788924399.465] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924399.465] [857359:857361] [DMG]  [
[1788924399.465] [857359:857361] [DMG]          InvokeResponseIB =
[1788924399.465] [857359:857361] [DMG]          {
[1788924399.465] [857359:857361] [DMG]                  CommandDataIB =
[1788924399.466] [857359:857361] [DMG]                  {
[1788924399.466] [857359:857361] [DMG]                          CommandPathIB =
[1788924399.466] [857359:857361] [DMG]                          {
[1788924399.466] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924399.466] [857359:857361] [DMG]                                  ClusterId = 0x30,
[1788924399.466] [857359:857361] [DMG]                                  CommandId = 0x1,
[1788924399.466] [857359:857361] [DMG]                          },
[1788924399.467] [857359:857361] [DMG]
[1788924399.467] [857359:857361] [DMG]                          CommandFields =
[1788924399.467] [857359:857361] [DMG]                          {
[1788924399.467] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924399.467] [857359:857361] [DMG]                                  0x1 = "" (0 chars),
[1788924399.467] [857359:857361] [DMG]                          },
[1788924399.467] [857359:857361] [DMG]                  },
[1788924399.467] [857359:857361] [DMG]
[1788924399.468] [857359:857361] [DMG]          },
[1788924399.468] [857359:857361] [DMG]
[1788924399.468] [857359:857361] [DMG]  ],
[1788924399.468] [857359:857361] [DMG]
[1788924399.468] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924399.468] [857359:857361] [DMG] },
[1788924399.468] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1788924399.468] [857359:857361] [CTL] Received ArmFailSafe response errorCode=0
[1788924399.468] [857359:857361] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1788924399.468] [857359:857361] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1788924399.469] [857359:857361] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1788924399.469] [857359:857361] [TOO] Starting commissioning stage 'ThreadNetworkEnable'
[1788924399.469] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924399.469] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924399.469] [857359:857361] [EM] <<< [E:38775i S:37659 M:214058685] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1788924399.470] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924399.470] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924400.730] [857359:857360] [DL] Indication received: conn=0xffff8404f320
[1788924400.731] [857359:857361] [EM] >>> [E:38775i S:37659 M:215342929] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1788924400.731] [857359:857361] [EM] Found matching exchange: 38775i, Delegate: 0xffff8c014578
[1788924400.731] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924400.731] [857359:857361] [DMG] InvokeResponseMessage =
[1788924400.731] [857359:857361] [DMG] {
[1788924400.731] [857359:857361] [DMG]  suppressResponse = false,
[1788924400.731] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924400.731] [857359:857361] [DMG]  [
[1788924400.731] [857359:857361] [DMG]          InvokeResponseIB =
[1788924400.731] [857359:857361] [DMG]          {
[1788924400.731] [857359:857361] [DMG]                  CommandDataIB =
[1788924400.731] [857359:857361] [DMG]                  {
[1788924400.731] [857359:857361] [DMG]                          CommandPathIB =
[1788924400.731] [857359:857361] [DMG]                          {
[1788924400.731] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924400.731] [857359:857361] [DMG]                                  ClusterId = 0x31,
[1788924400.731] [857359:857361] [DMG]                                  CommandId = 0x7,
[1788924400.731] [857359:857361] [DMG]                          },
[1788924400.731] [857359:857361] [DMG]
[1788924400.731] [857359:857361] [DMG]                          CommandFields =
[1788924400.731] [857359:857361] [DMG]                          {
[1788924400.731] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924400.731] [857359:857361] [DMG]                                  0x2 = NULL
[1788924400.731] [857359:857361] [DMG]                          },
[1788924400.731] [857359:857361] [DMG]                  },
[1788924400.731] [857359:857361] [DMG]
[1788924400.731] [857359:857361] [DMG]          },
[1788924400.732] [857359:857361] [DMG]
[1788924400.732] [857359:857361] [DMG]  ],
[1788924400.732] [857359:857361] [DMG]
[1788924400.732] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924400.732] [857359:857361] [DMG] },
[1788924400.732] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1788924400.732] [857359:857361] [CTL] Received ConnectNetwork response, networkingStatus=0
[1788924400.732] [857359:857361] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1788924400.732] [857359:857361] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'EvictPreviousCaseSessions'
[1788924400.732] [857359:857361] [CTL] Performing next commissioning step 'EvictPreviousCaseSessions'
[1788924400.732] [857359:857361] [TOO] Starting commissioning stage 'EvictPreviousCaseSessions'
[1788924400.732] [857359:857361] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1788924400.732] [857359:857361] [CTL] Successfully finished commissioning step 'EvictPreviousCaseSessions'
[1788924400.732] [857359:857361] [CTL] Commissioning stage next step: 'EvictPreviousCaseSessions' -> 'FindOperationalForStayActive'
[1788924400.732] [857359:857361] [CTL] Performing next commissioning step 'FindOperationalForStayActive'
[1788924400.732] [857359:857361] [TOO] Starting commissioning stage 'FindOperationalForStayActive'
[1788924400.732] [857359:857361] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1788924400.732] [857359:857361] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1788924400.732] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1788924400.733] [857359:857361] [DIS] Lookup started for 873AC76EFBA3164B-00000000000008CA
[1788924400.733] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924400.933] [857359:857361] [DIS] Checking node lookup status for 873AC76EFBA3164B-00000000000008CA after 200 ms
[1788924402.619] [857359:857361] [DIS] SRV record already actively processed.
[1788924402.619] [857359:857361] [DIS] SRV record already actively processed.
[1788924402.620] [857359:857361] [DIS] Lookup clearing interface for non LL address
[1788924402.620] [857359:857361] [DIS] UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e%eth0]:5540: new best score: 5 (for 873AC76EFBA3164B-00000000000008CA)
[1788924402.620] [857359:857361] [DIS] Checking node lookup status for 873AC76EFBA3164B-00000000000008CA after 1888 ms
[1788924402.620] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540 while in state 2
[1788924402.620] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1788924402.620] [857359:857361] [IN] SecureSession[0xffff8c016e10]: Allocated Type:2 LSID:37660
[1788924402.620] [857359:857361] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1788924402.621] [857359:857361] [EM] <<< [E:38776i S:0 M:23679080] (U) Msg TX from A1824ED9B59E4223 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1788924402.621] [857359:857361] [EM] ??1 [E:38776i S:0 M:23679080] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2731ms from now [State:Idle II:2000 AI:2000 AT:4000]
[1788924402.622] [857359:857361] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1788924402.622] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1788924402.739] [857359:857361] [EM] >>> [E:38776i S:0 M:241631429 (Ack:23679080)] (U) Msg RX from 0:0000000000000000 [0000] to A1824ED9B59E4223 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788924402.739] [857359:857361] [EM] Found matching exchange: 38776i, Delegate: 0xffff8c014f58
[1788924402.739] [857359:857361] [EM] Rxd Ack; Removing MessageCounter:23679080 from Retrans Table on exchange 38776i
[1788924402.816] [857359:857361] [EM] >>> [E:38776i S:0 M:241631430 (Ack:23679080)] (U) Msg RX from 0:0000000000000000 [0000] to A1824ED9B59E4223 --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:752)
[1788924402.816] [857359:857361] [EM] Found matching exchange: 38776i, Delegate: 0xffff8c014f58
[1788924402.816] [857359:857361] [EM] CHIP MessageCounter:23679080 not in RetransTable on exchange 38776i
[1788924402.816] [857359:857361] [SC] Received Sigma2 msg
[1788924402.816] [857359:857361] [SC] Found MRP parameters in the message
[1788924402.820] [857359:857361] [SC] Peer <00000000000008CA, 1> assigned session ID 55441
[1788924402.820] [857359:857361] [SC] Sending Sigma3
[1788924402.821] [857359:857361] [EM] <<< [E:38776i S:0 M:23679081 (Ack:241631430)] (U) Msg TX from A1824ED9B59E4223 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1788924402.822] [857359:857361] [EM] ??1 [E:38776i S:0 M:23679081] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2516ms from now [State:Active II:2000 AI:2000 AT:4000]
[1788924402.822] [857359:857361] [SC] Sent Sigma3 msg
[1788924403.009] [857359:857361] [EM] >>> [E:38776i S:0 M:241631431 (Ack:23679081)] (U) Msg RX from 0:0000000000000000 [0000] to A1824ED9B59E4223 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788924403.009] [857359:857361] [EM] Found matching exchange: 38776i, Delegate: 0xffff8c014f58
[1788924403.009] [857359:857361] [EM] Rxd Ack; Removing MessageCounter:23679081 from Retrans Table on exchange 38776i
[1788924403.016] [857359:857361] [EM] >>> [E:38776i S:0 M:241631432 (Ack:23679081)] (U) Msg RX from 0:0000000000000000 [0000] to A1824ED9B59E4223 --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1788924403.016] [857359:857361] [EM] Found matching exchange: 38776i, Delegate: 0xffff8c014f58
[1788924403.016] [857359:857361] [EM] CHIP MessageCounter:23679081 not in RetransTable on exchange 38776i
[1788924403.016] [857359:857361] [SC] Success status report received. Session was established
[1788924403.023] [857359:857361] [SC] SecureSession[0xffff8c016e10, LSID:37660]: State change 'kEstablishing' --> 'kActive'
[1788924403.023] [857359:857361] [IN] SecureSession[0xffff8c016e10]: Activated - Type:2 LSID:37660
[1788924403.023] [857359:857361] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:37660 PSID:55441!
[1788924403.023] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1788924403.023] [857359:857361] [CTL] Successfully finished commissioning step 'FindOperationalForStayActive'
[1788924403.023] [857359:857361] [CTL] Commissioning stage next step: 'FindOperationalForStayActive' -> 'ICDSendStayActive'
[1788924403.023] [857359:857361] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1788924403.023] [857359:857361] [TOO] Starting commissioning stage 'ICDSendStayActive'
[1788924403.023] [857359:857361] [CTL] Skipping kICDSendStayActive
[1788924403.023] [857359:857361] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1788924403.023] [857359:857361] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'FindOperationalForCommissioningComplete'
[1788924403.023] [857359:857361] [CTL] Performing next commissioning step 'FindOperationalForCommissioningComplete'
[1788924403.023] [857359:857361] [TOO] Starting commissioning stage 'FindOperationalForCommissioningComplete'
[1788924403.023] [857359:857361] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1788924403.023] [857359:857361] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1788924403.024] [857359:857361] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1788924403.024] [857359:857361] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1788924403.024] [857359:857361] [CTL] Successfully finished commissioning step 'FindOperationalForCommissioningComplete'
[1788924403.024] [857359:857361] [CTL] Commissioning stage next step: 'FindOperationalForCommissioningComplete' -> 'SendComplete'
[1788924403.024] [857359:857361] [CTL] Performing next commissioning step 'SendComplete'
[1788924403.024] [857359:857361] [TOO] Starting commissioning stage 'SendComplete'
[1788924403.024] [857359:857361] [DMG] ICR moving to [AddingComm]
[1788924403.024] [857359:857361] [DMG] ICR moving to [AddedComma]
[1788924403.024] [857359:857361] [EM] <<< [E:38777i S:37660 M:77002549] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [164B] [UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1788924403.024] [857359:857361] [EM] ??1 [E:38777i S:37660 M:77002549] (S) Msg Retransmission to 1:00000000000008CA scheduled for 2637ms from now [State:Active II:2000 AI:2000 AT:4000]
[1788924403.024] [857359:857361] [DMG] ICR moving to [AwaitingRe]
[1788924403.024] [857359:857361] [EM] <<< [E:38776i S:0 M:23679082 (Ack:241631432)] (U) Msg TX from A1824ED9B59E4223 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788924403.024] [857359:857361] [EM] Flushed pending ack for MessageCounter:241631432 on exchange 38776i
[1788924403.091] [857359:857361] [EM] >>> [E:38777i S:37660 M:36297677 (Ack:77002549)] (S) Msg RX from 1:00000000000008CA [164B] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1788924403.091] [857359:857361] [EM] Found matching exchange: 38777i, Delegate: 0xffff8c014578
[1788924403.091] [857359:857361] [EM] Rxd Ack; Removing MessageCounter:77002549 from Retrans Table on exchange 38777i
[1788924403.091] [857359:857361] [DMG] ICR moving to [ResponseRe]
[1788924403.091] [857359:857361] [DMG] InvokeResponseMessage =
[1788924403.091] [857359:857361] [DMG] {
[1788924403.091] [857359:857361] [DMG]  suppressResponse = false,
[1788924403.091] [857359:857361] [DMG]  InvokeResponseIBs =
[1788924403.091] [857359:857361] [DMG]  [
[1788924403.091] [857359:857361] [DMG]          InvokeResponseIB =
[1788924403.091] [857359:857361] [DMG]          {
[1788924403.091] [857359:857361] [DMG]                  CommandDataIB =
[1788924403.091] [857359:857361] [DMG]                  {
[1788924403.091] [857359:857361] [DMG]                          CommandPathIB =
[1788924403.091] [857359:857361] [DMG]                          {
[1788924403.091] [857359:857361] [DMG]                                  EndpointId = 0x0,
[1788924403.092] [857359:857361] [DMG]                                  ClusterId = 0x30,
[1788924403.092] [857359:857361] [DMG]                                  CommandId = 0x5,
[1788924403.092] [857359:857361] [DMG]                          },
[1788924403.092] [857359:857361] [DMG]
[1788924403.092] [857359:857361] [DMG]                          CommandFields =
[1788924403.092] [857359:857361] [DMG]                          {
[1788924403.092] [857359:857361] [DMG]                                  0x0 = 0 (unsigned),
[1788924403.092] [857359:857361] [DMG]                                  0x1 = "" (0 chars),
[1788924403.092] [857359:857361] [DMG]                          },
[1788924403.092] [857359:857361] [DMG]                  },
[1788924403.092] [857359:857361] [DMG]
[1788924403.092] [857359:857361] [DMG]          },
[1788924403.092] [857359:857361] [DMG]
[1788924403.092] [857359:857361] [DMG]  ],
[1788924403.092] [857359:857361] [DMG]
[1788924403.092] [857359:857361] [DMG]  InteractionModelRevision = 12
[1788924403.092] [857359:857361] [DMG] },
[1788924403.092] [857359:857361] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1788924403.092] [857359:857361] [CTL] Received CommissioningComplete response, errorCode=0
[1788924403.092] [857359:857361] [CTL] Successfully finished commissioning step 'SendComplete'
[1788924403.092] [857359:857361] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1788924403.092] [857359:857361] [CTL] Performing next commissioning step 'Cleanup'
[1788924403.092] [857359:857361] [TOO] Starting commissioning stage 'Cleanup'
[1788924403.092] [857359:857361] [CTL] Successfully finished commissioning step 'Cleanup'
[1788924403.092] [857359:857361] [DIS] Closing all BLE connections
[1788924403.092] [857359:857361] [IN] Clearing BLE pending packets.
[1788924403.093] [857359:857361] [BLE] Auto-closing end point's BLE connection.
[1788924403.093] [857359:857361] [DL] Closing BLE GATT connection (con 0xffff8404f320)
[1788924403.093] [857359:857360] [DL] Close BLE connection: peer=FF:20:DB:D6:D9:90
[1788924403.655] [857359:857361] [IN] SecureSession[0xffff8c002c60]: MarkForEviction Type:1 LSID:37659
[1788924403.655] [857359:857361] [SC] SecureSession[0xffff8c002c60, LSID:37659]: State change 'kActive' --> 'kPendingEviction'
[1788924403.656] [857359:857361] [IN] SecureSession[0xffff8c002c60]: Released - Type:1 LSID:37659
[1788924403.656] [857359:857361] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1788924403.656] [857359:857361] [TOO] Device commissioning completed with success
[1788924403.656] [857359:857361] [DMG] ICR moving to [AwaitingDe]
[1788924403.656] [857359:857360] [DL] BLE connection closed: conn=0xffff8404f320
[1788924403.656] [857359:857361] [EM] <<< [E:38777i S:37660 M:77002550 (Ack:36297677)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [164B] [UDP:[fd00:dcff:665f:1:8c06:209f:67dc:397e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1788924403.656] [857359:857361] [EM] Flushed pending ack for MessageCounter:36297677 on exchange 38777i
[1788924403.656] [857359:857361] [BLE] No endpoint for unsubscribe complete
[1788924403.656] [857359:857361] [BLE] No endpoint for connection error
[1788924403.656] [857359:857361] [DL] Freeing BLE connection: conn=0xffff8404f320
[1788924403.656] [857359:857359] [CTL] Shutting down the commissioner
[1788924403.657] [857359:857359] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788924403.657] [857359:857359] [CTL] Shutting down the controller
[1788924403.657] [857359:857359] [IN] Expiring all sessions for fabric 0x1!!
[1788924403.657] [857359:857359] [IN] SecureSession[0xffff8c016e10]: MarkForEviction Type:2 LSID:37660
[1788924403.657] [857359:857359] [SC] SecureSession[0xffff8c016e10, LSID:37660]: State change 'kActive' --> 'kPendingEviction'
[1788924403.657] [857359:857359] [IN] SecureSession[0xffff8c016e10]: Released - Type:2 LSID:37660
[1788924403.657] [857359:857359] [FP] Forgetting fabric 0x1
[1788924403.657] [857359:857359] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1788924403.657] [857359:857359] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1788924403.657] [857359:857359] [TS] Reverted Last Known Good Time to previous value
[1788924403.657] [857359:857359] [CTL] Shutting down the commissioner
[1788924403.657] [857359:857359] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788924403.657] [857359:857359] [CTL] Shutting down the controller
[1788924403.657] [857359:857359] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1788924403.657] [857359:857359] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1788924403.658] [857359:857359] [FP] Shutting down FabricTable
[1788924403.658] [857359:857359] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1788924403.658] [857359:857359] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1788924403.658] [857359:857359] [TS] Reverted Last Known Good Time to previous value
[1788924403.735] [857359:857359] [DL] Wrote settings to /tmp/chip_counters.ini
[1788924403.735] [857359:857359] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1788924403.735] [857359:857359] [DL] Inet Layer shutdown
[1788924403.735] [857359:857359] [DL] BLE Layer shutdown
[1788924403.739] [857359:857359] [DL] WiFi-PAF Layer shutdown
[1788924403.739] [857359:857359] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788924403.739] [857359:857359] [DL] System Layer shutdown
```
[attestation](attestation.md)  
