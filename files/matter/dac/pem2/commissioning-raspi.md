```c
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840
[1770364774.344] [2443:2443] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770364774.358] [2443:2443] [DL] Wrote settings to /tmp/chip_tool_kvs
[1770364774.370] [2443:2443] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770364774.386] [2443:2443] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770364774.394] [2443:2443] [DL] Wrote settings to /tmp/chip_factory.ini
[1770364774.394] [2443:2443] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770364774.403] [2443:2443] [DL] Wrote settings to /tmp/chip_config.ini
[1770364774.403] [2443:2443] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770364774.412] [2443:2443] [DL] Wrote settings to /tmp/chip_counters.ini
[1770364774.424] [2443:2443] [DL] Wrote settings to /tmp/chip_config.ini
[1770364774.424] [2443:2443] [DL] NVS set: chip-config/unique-id = "0E25472B0C4C5169"
[1770364774.435] [2443:2443] [DL] Wrote settings to /tmp/chip_factory.ini
[1770364774.435] [2443:2443] [DL] NVS set: chip-factory/vendor-id = 65521 (0xFFF1)
[1770364774.445] [2443:2443] [DL] Wrote settings to /tmp/chip_factory.ini
[1770364774.445] [2443:2443] [DL] NVS set: chip-factory/product-id = 32769 (0x8001)
[1770364774.453] [2443:2443] [DL] Wrote settings to /tmp/chip_counters.ini
[1770364774.454] [2443:2443] [DL] NVS set: chip-counters/reboot-count = 1 (0x1)
[1770364774.464] [2443:2443] [DL] Wrote settings to /tmp/chip_counters.ini
[1770364774.464] [2443:2443] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770364774.474] [2443:2443] [DL] Wrote settings to /tmp/chip_counters.ini
[1770364774.474] [2443:2443] [DL] NVS set: chip-counters/boot-reason = 0 (0x0)
[1770364774.484] [2443:2443] [DL] Wrote settings to /tmp/chip_config.ini
[1770364774.484] [2443:2443] [DL] NVS set: chip-config/regulatory-location = 0 (0x0)
[1770364774.494] [2443:2443] [DL] Wrote settings to /tmp/chip_config.ini
[1770364774.494] [2443:2443] [DL] NVS set: chip-config/location-capability = 2 (0x2)
[1770364774.506] [2443:2443] [DL] Wrote settings to /tmp/chip_config.ini
[1770364774.506] [2443:2443] [DL] NVS set: chip-config/configuration-version = 1 (0x1)
[1770364774.509] [2443:2443] [DL] Got Ethernet interface: eth0
[1770364774.510] [2443:2443] [DL] Found the primary Ethernet interface:eth0
[1770364774.512] [2443:2443] [DL] Got WiFi interface: wlan0
[1770364774.512] [2443:2443] [DL] Failed to reset WiFi statistic counts
[1770364774.512] [2443:2443] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770364774.708] [2443:2443] [IN] UDP::Init bind&listen port=0
[1770364774.709] [2443:2443] [IN] UDP::Init bound to port=53110
[1770364774.709] [2443:2443] [IN] BLEBase::Init - setting/overriding transport
[1770364774.709] [2443:2443] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770364774.709] [2443:2443] [CTL] NFCBase::Init
[1770364774.709] [2443:2443] [IN] TransportMgr initialized
[1770364774.709] [2443:2443] [FP] Initializing FabricTable from persistent storage
[1770364774.709] [2443:2443] [TS] Last Known Good Time: [unknown]
[1770364774.709] [2443:2443] [TS] Setting Last Known Good Time to firmware build time 2023-10-14T01:16:48
[1770364774.714] [2443:2443] [DMG] Ember attribute persistence requires setting up
[1770364774.714] [2443:2443] [ZCL] Using ZAP configuration...
[1770364774.721] [2443:2443] [CTL] System State Initialized...
[1770364774.747] [2443:2443] [CTL] Setting attestation nonce to random value
[1770364774.747] [2443:2443] [CTL] Setting CSR nonce to random value
[1770364774.748] [2443:2443] [IN] UDP::Init bind&listen port=5550
[1770364774.748] [2443:2443] [IN] UDP::Init bound to port=5550
[1770364774.748] [2443:2443] [IN] TransportMgr initialized
[1770364774.751] [2443:2465] [DL] CHIP task running
[1770364774.751] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 32786
[1770364774.753] [2443:2465] [CTL] Setting attestation nonce to random value
[1770364774.753] [2443:2465] [CTL] Setting CSR nonce to random value
[1770364774.754] [2443:2465] [CTL] Couldn't get ExampleOpCredsCAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770364774.757] [2443:2465] [CTL] Couldn't get ExampleOpCredsICAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770364774.761] [2443:2465] [CTL] Generating RCAC
[1770364774.765] [2443:2465] [CTL] Generating ICAC
[1770364774.768] [2443:2465] [CTL] Generating NOC
[1770364774.769] [2443:2465] [FP] Validating NOC chain
[1770364774.774] [2443:2465] [FP] NOC chain validation successful
[1770364774.775] [2443:2465] [FP] Added new fabric at index: 0x1
[1770364774.775] [2443:2465] [FP] Assigned compressed fabric ID: 0x4B6873C4587CC6ED, node ID: 0x000000000001B669
[1770364774.775] [2443:2465] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770364774.775] [2443:2465] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770364774.775] [2443:2465] [TS] Retaining current Last Known Good Time
[1770364774.778] [2443:2465] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770364774.782] [2443:2465] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770364774.792] [2443:2465] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 4B6873C4587CC6ED)
[1770364774.792] [2443:2465] [IN] UDP::Init bind&listen port=5551
[1770364774.792] [2443:2465] [IN] UDP::Init bound to port=5551
[1770364774.793] [2443:2465] [IN] TransportMgr initialized
[1770364774.870] [2443:2465] [CTL] Setting thread operational dataset from parameters
[1770364774.871] [2443:2465] [CTL] Setting attestation nonce to random value
[1770364774.871] [2443:2465] [CTL] Setting CSR nonce to random value
[1770364774.871] [2443:2465] [CTL] Commission called for node ID 0x00000000000008CA
[1770364774.871] [2443:2465] [DL] Long dispatch time: 119 ms, for event type 2
[1770364774.909] [2443:2450] [BLE] BLE removing known devices
[1770364774.913] [2443:2450] [BLE] BLE initiating scan
[1770364774.919] [2443:2465] [BLE] ChipDeviceScanner has started scanning!
[1770364774.943] [2443:2450] [BLE] Device E4:75:D8:AD:A6:1D does not look like a CHIP device.
[1770364774.945] [2443:2450] [BLE] Device 1F:D7:54:CA:FC:83 does not look like a CHIP device.
[1770364774.946] [2443:2450] [BLE] Device 1C:C4:E5:DE:04:09 does not look like a CHIP device.
[1770364774.948] [2443:2450] [BLE] Device 5D:66:91:50:6F:4E does not look like a CHIP device.
[1770364774.979] [2443:2450] [BLE] New device scanned: CC:C0:BF:C1:8D:CE
[1770364774.979] [2443:2450] [BLE] Device discriminator match. Attempting to connect.
[1770364774.986] [2443:2450] [BLE] ChipDeviceScanner has stopped scanning!
[1770364775.146] [2443:2450] [DL] ConnectDevice complete
[1770364775.146] [2443:2450] [BLE] New device connected: CC:C0:BF:C1:8D:CE
[1770364777.792] [2443:2450] [DL] CHIP service found
[1770364777.792] [2443:2450] [DL] Valid C1 characteristic found
[1770364777.792] [2443:2450] [DL] Valid C2 characteristic found
[1770364777.792] [2443:2450] [DL] New BLE connection: conn=0xffff88028d20 device=CC:C0:BF:C1:8D:CE path=/org/bluez/hci0/dev_CC_C0_BF_C1_8D_CE
[1770364777.792] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16387
[1770364777.793] [2443:2465] [DIS] Closing all BLE connections
[1770364777.793] [2443:2465] [IN] BleConnectionComplete: endPoint 0xaaaab6196fd0
[1770364777.794] [2443:2465] [IN] SecureSession[0xffff80022d50]: Allocated Type:1 LSID:1492
[1770364777.794] [2443:2465] [SC] Assigned local session key ID 1492
[1770364777.794] [2443:2465] [EM] <<< [E:51540i S:0 M:237354424] (U) Msg TX from 62C1268F274E3116 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770364777.795] [2443:2465] [IN] Message appended to BLE send queue
[1770364777.795] [2443:2465] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770364778.713] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364778.909] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16390
[1770364778.909] [2443:2465] [BLE] subscribe complete, ep = 0xaaaab6196fd0
[1770364778.909] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364778.910] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364778.910] [2443:2465] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770364778.910] [2443:2465] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770364778.910] [2443:2465] [BLE] local and remote recv window size = 5
[1770364778.911] [2443:2465] [IN] BLE EndPoint 0xaaaab6196fd0 Connection Complete
[1770364779.298] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364779.398] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364779.398] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364779.399] [2443:2465] [EM] >>> [E:51540i S:0 M:204966106] (U) Msg RX from 0:0000000000000000 [0000] to 62C1268F274E3116 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[1770364779.399] [2443:2465] [EM] Found matching exchange: 51540i, Delegate: 0xffff80021818
[1770364779.399] [2443:2465] [SC] Received PBKDF param response
[1770364779.399] [2443:2465] [SC] Peer assigned session ID 54307
[1770364779.399] [2443:2465] [SC] Found MRP parameters in the message
[1770364779.421] [2443:2465] [EM] <<< [E:51540i S:0 M:237354425] (U) Msg TX from 62C1268F274E3116 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770364779.422] [2443:2465] [SC] Sent spake2p msg1
[1770364779.589] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364779.688] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364779.689] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364779.689] [2443:2465] [EM] >>> [E:51540i S:0 M:204966107] (U) Msg RX from 0:0000000000000000 [0000] to 62C1268F274E3116 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770364779.689] [2443:2465] [EM] Found matching exchange: 51540i, Delegate: 0xffff80021818
[1770364779.689] [2443:2465] [SC] Received spake2p msg2
[1770364779.694] [2443:2465] [EM] <<< [E:51540i S:0 M:237354426] (U) Msg TX from 62C1268F274E3116 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770364779.696] [2443:2465] [SC] Sent spake2p msg3
[1770364780.175] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364780.177] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364780.177] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364780.177] [2443:2465] [EM] >>> [E:51540i S:0 M:204966108] (U) Msg RX from 0:0000000000000000 [0000] to 62C1268F274E3116 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770364780.177] [2443:2465] [EM] Found matching exchange: 51540i, Delegate: 0xffff80021818
[1770364780.178] [2443:2465] [SC] SecureSession[0xffff80022d50, LSID:1492]: State change 'kEstablishing' --> 'kActive'
[1770364780.178] [2443:2465] [IN] SecureSession[0xffff80022d50]: Activated - Type:1 LSID:1492
[1770364780.178] [2443:2465] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:1492 PSID:54307!
[1770364780.179] [2443:2465] [CTL] Remote device completed SPAKE2+ handshake
[1770364780.179] [2443:2465] [TOO] Pairing Success
[1770364780.179] [2443:2465] [TOO] PASE establishment successful
[1770364780.179] [2443:2465] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770364780.179] [2443:2465] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770364780.179] [2443:2465] [CTL] Sending read requests for commissioning information
[1770364780.180] [2443:2465] [DMG] SendReadRequest ReadClient[0xffff80023750]: Sending Read Request
[1770364780.185] [2443:2465] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770364780.185] [2443:2465] [EM] <<< [E:51541i S:1492 M:264736067] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770364780.186] [2443:2465] [DMG] MoveToState ReadClient[0xffff80023750]: Moving to [AwaitingIn]
[1770364780.186] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 32792
[1770364780.662] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364780.858] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364780.859] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364781.249] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364781.250] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364781.250] [2443:2465] [EM] >>> [E:51541i S:1492 M:78474672] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:257)
[1770364781.250] [2443:2465] [EM] Found matching exchange: 51541i, Delegate: 0xffff80023760
[1770364781.251] [2443:2465] [DMG] ReportDataMessage =
[1770364781.251] [2443:2465] [DMG] {
[1770364781.251] [2443:2465] [DMG]      AttributeReportIBs =
[1770364781.251] [2443:2465] [DMG]      [
[1770364781.251] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.251] [2443:2465] [DMG]              {
[1770364781.251] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.251] [2443:2465] [DMG]                      {
[1770364781.251] [2443:2465] [DMG]                              DataVersion = 0x3bf1e4f2,
[1770364781.252] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.252] [2443:2465] [DMG]                              {
[1770364781.252] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.252] [2443:2465] [DMG]                                      Cluster = 0x31,
[1770364781.252] [2443:2465] [DMG]                                      Attribute = 0x0000_FFFC,
[1770364781.253] [2443:2465] [DMG]                              }
[1770364781.253] [2443:2465] [DMG]
[1770364781.253] [2443:2465] [DMG]                              Data = 2 (unsigned),
[1770364781.253] [2443:2465] [DMG]                      },
[1770364781.253] [2443:2465] [DMG]
[1770364781.253] [2443:2465] [DMG]              },
[1770364781.253] [2443:2465] [DMG]
[1770364781.253] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.254] [2443:2465] [DMG]              {
[1770364781.254] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.254] [2443:2465] [DMG]                      {
[1770364781.254] [2443:2465] [DMG]                              DataVersion = 0xbe43575,
[1770364781.254] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.254] [2443:2465] [DMG]                              {
[1770364781.254] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.255] [2443:2465] [DMG]                                      Cluster = 0x28,
[1770364781.255] [2443:2465] [DMG]                                      Attribute = 0x0000_0004,
[1770364781.255] [2443:2465] [DMG]                              }
[1770364781.255] [2443:2465] [DMG]
[1770364781.255] [2443:2465] [DMG]                              Data = 32784 (unsigned),
[1770364781.255] [2443:2465] [DMG]                      },
[1770364781.256] [2443:2465] [DMG]
[1770364781.256] [2443:2465] [DMG]              },
[1770364781.256] [2443:2465] [DMG]
[1770364781.256] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.256] [2443:2465] [DMG]              {
[1770364781.256] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.256] [2443:2465] [DMG]                      {
[1770364781.256] [2443:2465] [DMG]                              DataVersion = 0xbe43575,
[1770364781.256] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.257] [2443:2465] [DMG]                              {
[1770364781.257] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.257] [2443:2465] [DMG]                                      Cluster = 0x28,
[1770364781.257] [2443:2465] [DMG]                                      Attribute = 0x0000_0002,
[1770364781.257] [2443:2465] [DMG]                              }
[1770364781.257] [2443:2465] [DMG]
[1770364781.257] [2443:2465] [DMG]                              Data = 65521 (unsigned),
[1770364781.257] [2443:2465] [DMG]                      },
[1770364781.257] [2443:2465] [DMG]
[1770364781.257] [2443:2465] [DMG]              },
[1770364781.257] [2443:2465] [DMG]
[1770364781.257] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.257] [2443:2465] [DMG]              {
[1770364781.257] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.258] [2443:2465] [DMG]                      {
[1770364781.258] [2443:2465] [DMG]                              DataVersion = 0x664af2c9,
[1770364781.258] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.258] [2443:2465] [DMG]                              {
[1770364781.258] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.258] [2443:2465] [DMG]                                      Cluster = 0x30,
[1770364781.258] [2443:2465] [DMG]                                      Attribute = 0x0000_0003,
[1770364781.258] [2443:2465] [DMG]                              }
[1770364781.258] [2443:2465] [DMG]
[1770364781.258] [2443:2465] [DMG]                              Data = 0 (unsigned),
[1770364781.258] [2443:2465] [DMG]                      },
[1770364781.258] [2443:2465] [DMG]
[1770364781.259] [2443:2465] [DMG]              },
[1770364781.259] [2443:2465] [DMG]
[1770364781.259] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.259] [2443:2465] [DMG]              {
[1770364781.259] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.259] [2443:2465] [DMG]                      {
[1770364781.259] [2443:2465] [DMG]                              DataVersion = 0x664af2c9,
[1770364781.259] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.259] [2443:2465] [DMG]                              {
[1770364781.259] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.259] [2443:2465] [DMG]                                      Cluster = 0x30,
[1770364781.259] [2443:2465] [DMG]                                      Attribute = 0x0000_0002,
[1770364781.259] [2443:2465] [DMG]                              }
[1770364781.259] [2443:2465] [DMG]
[1770364781.260] [2443:2465] [DMG]                              Data = 0 (unsigned),
[1770364781.260] [2443:2465] [DMG]                      },
[1770364781.260] [2443:2465] [DMG]
[1770364781.260] [2443:2465] [DMG]              },
[1770364781.260] [2443:2465] [DMG]
[1770364781.260] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.260] [2443:2465] [DMG]              {
[1770364781.260] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.260] [2443:2465] [DMG]                      {
[1770364781.260] [2443:2465] [DMG]                              DataVersion = 0x664af2c9,
[1770364781.260] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.260] [2443:2465] [DMG]                              {
[1770364781.260] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.261] [2443:2465] [DMG]                                      Cluster = 0x30,
[1770364781.261] [2443:2465] [DMG]                                      Attribute = 0x0000_0001,
[1770364781.261] [2443:2465] [DMG]                              }
[1770364781.261] [2443:2465] [DMG]
[1770364781.261] [2443:2465] [DMG]                              Data =
[1770364781.261] [2443:2465] [DMG]                              {
[1770364781.261] [2443:2465] [DMG]                                      0x0 = 60 (unsigned),
[1770364781.261] [2443:2465] [DMG]                                      0x1 = 900 (unsigned),
[1770364781.261] [2443:2465] [DMG]                              },
[1770364781.261] [2443:2465] [DMG]                      },
[1770364781.261] [2443:2465] [DMG]
[1770364781.261] [2443:2465] [DMG]              },
[1770364781.261] [2443:2465] [DMG]
[1770364781.262] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.262] [2443:2465] [DMG]              {
[1770364781.262] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.262] [2443:2465] [DMG]                      {
[1770364781.262] [2443:2465] [DMG]                              DataVersion = 0x664af2c9,
[1770364781.262] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.262] [2443:2465] [DMG]                              {
[1770364781.262] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.262] [2443:2465] [DMG]                                      Cluster = 0x30,
[1770364781.262] [2443:2465] [DMG]                                      Attribute = 0x0000_0000,
[1770364781.262] [2443:2465] [DMG]                              }
[1770364781.262] [2443:2465] [DMG]
[1770364781.263] [2443:2465] [DMG]                              Data = 0 (unsigned),
[1770364781.263] [2443:2465] [DMG]                      },
[1770364781.263] [2443:2465] [DMG]
[1770364781.263] [2443:2465] [DMG]              },
[1770364781.263] [2443:2465] [DMG]
[1770364781.263] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.263] [2443:2465] [DMG]              {
[1770364781.263] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.263] [2443:2465] [DMG]                      {
[1770364781.263] [2443:2465] [DMG]                              DataVersion = 0x664af2c9,
[1770364781.263] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.263] [2443:2465] [DMG]                              {
[1770364781.263] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.263] [2443:2465] [DMG]                                      Cluster = 0x30,
[1770364781.264] [2443:2465] [DMG]                                      Attribute = 0x0000_0004,
[1770364781.264] [2443:2465] [DMG]                              }
[1770364781.264] [2443:2465] [DMG]
[1770364781.264] [2443:2465] [DMG]                              Data = true,
[1770364781.264] [2443:2465] [DMG]                      },
[1770364781.264] [2443:2465] [DMG]
[1770364781.264] [2443:2465] [DMG]              },
[1770364781.264] [2443:2465] [DMG]
[1770364781.264] [2443:2465] [DMG]      ],
[1770364781.264] [2443:2465] [DMG]
[1770364781.264] [2443:2465] [DMG]      SuppressResponse = true,
[1770364781.264] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364781.264] [2443:2465] [DMG] }
[1770364781.267] [2443:2465] [DMG] SendReadRequest ReadClient[0xffff80023750]: Sending Read Request
[1770364781.267] [2443:2465] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770364781.267] [2443:2465] [EM] <<< [E:51542i S:1492 M:264736068] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770364781.268] [2443:2465] [DMG] MoveToState ReadClient[0xffff80023750]: Moving to [AwaitingIn]
[1770364781.637] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364781.930] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364781.930] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364781.931] [2443:2465] [EM] >>> [E:51542i S:1492 M:78474673] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:191)
[1770364781.931] [2443:2465] [EM] Found matching exchange: 51542i, Delegate: 0xffff80023760
[1770364781.931] [2443:2465] [DMG] ReportDataMessage =
[1770364781.931] [2443:2465] [DMG] {
[1770364781.931] [2443:2465] [DMG]      AttributeReportIBs =
[1770364781.931] [2443:2465] [DMG]      [
[1770364781.931] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.931] [2443:2465] [DMG]              {
[1770364781.931] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.931] [2443:2465] [DMG]                      {
[1770364781.932] [2443:2465] [DMG]                              DataVersion = 0x580626ad,
[1770364781.932] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.932] [2443:2465] [DMG]                              {
[1770364781.932] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.932] [2443:2465] [DMG]                                      Cluster = 0x46,
[1770364781.932] [2443:2465] [DMG]                                      Attribute = 0x0000_0002,
[1770364781.932] [2443:2465] [DMG]                              }
[1770364781.932] [2443:2465] [DMG]
[1770364781.932] [2443:2465] [DMG]                              Data = 0 (unsigned),
[1770364781.932] [2443:2465] [DMG]                      },
[1770364781.933] [2443:2465] [DMG]
[1770364781.933] [2443:2465] [DMG]              },
[1770364781.933] [2443:2465] [DMG]
[1770364781.933] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.933] [2443:2465] [DMG]              {
[1770364781.933] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.933] [2443:2465] [DMG]                      {
[1770364781.933] [2443:2465] [DMG]                              DataVersion = 0x580626ad,
[1770364781.933] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.933] [2443:2465] [DMG]                              {
[1770364781.934] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.934] [2443:2465] [DMG]                                      Cluster = 0x46,
[1770364781.934] [2443:2465] [DMG]                                      Attribute = 0x0000_0001,
[1770364781.934] [2443:2465] [DMG]                              }
[1770364781.934] [2443:2465] [DMG]
[1770364781.934] [2443:2465] [DMG]                              Data = 0 (unsigned),
[1770364781.934] [2443:2465] [DMG]                      },
[1770364781.934] [2443:2465] [DMG]
[1770364781.934] [2443:2465] [DMG]              },
[1770364781.934] [2443:2465] [DMG]
[1770364781.934] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.935] [2443:2465] [DMG]              {
[1770364781.935] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.935] [2443:2465] [DMG]                      {
[1770364781.935] [2443:2465] [DMG]                              DataVersion = 0x580626ad,
[1770364781.935] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.935] [2443:2465] [DMG]                              {
[1770364781.935] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.935] [2443:2465] [DMG]                                      Cluster = 0x46,
[1770364781.935] [2443:2465] [DMG]                                      Attribute = 0x0000_0000,
[1770364781.935] [2443:2465] [DMG]                              }
[1770364781.935] [2443:2465] [DMG]
[1770364781.936] [2443:2465] [DMG]                              Data = 600 (unsigned),
[1770364781.936] [2443:2465] [DMG]                      },
[1770364781.936] [2443:2465] [DMG]
[1770364781.936] [2443:2465] [DMG]              },
[1770364781.936] [2443:2465] [DMG]
[1770364781.936] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.936] [2443:2465] [DMG]              {
[1770364781.936] [2443:2465] [DMG]                      AttributeStatusIB =
[1770364781.936] [2443:2465] [DMG]                      {
[1770364781.936] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.936] [2443:2465] [DMG]                              {
[1770364781.937] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.937] [2443:2465] [DMG]                                      Cluster = 0x46,
[1770364781.937] [2443:2465] [DMG]                                      Attribute = 0x0000_0007,
[1770364781.937] [2443:2465] [DMG]                              }
[1770364781.937] [2443:2465] [DMG]
[1770364781.937] [2443:2465] [DMG]                              StatusIB =
[1770364781.937] [2443:2465] [DMG]                              {
[1770364781.937] [2443:2465] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770364781.937] [2443:2465] [DMG]                              },
[1770364781.937] [2443:2465] [DMG]
[1770364781.937] [2443:2465] [DMG]                      },
[1770364781.938] [2443:2465] [DMG]
[1770364781.938] [2443:2465] [DMG]              },
[1770364781.938] [2443:2465] [DMG]
[1770364781.938] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.938] [2443:2465] [DMG]              {
[1770364781.938] [2443:2465] [DMG]                      AttributeStatusIB =
[1770364781.938] [2443:2465] [DMG]                      {
[1770364781.938] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.938] [2443:2465] [DMG]                              {
[1770364781.938] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.938] [2443:2465] [DMG]                                      Cluster = 0x46,
[1770364781.938] [2443:2465] [DMG]                                      Attribute = 0x0000_0006,
[1770364781.939] [2443:2465] [DMG]                              }
[1770364781.939] [2443:2465] [DMG]
[1770364781.939] [2443:2465] [DMG]                              StatusIB =
[1770364781.939] [2443:2465] [DMG]                              {
[1770364781.939] [2443:2465] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770364781.939] [2443:2465] [DMG]                              },
[1770364781.939] [2443:2465] [DMG]
[1770364781.939] [2443:2465] [DMG]                      },
[1770364781.939] [2443:2465] [DMG]
[1770364781.939] [2443:2465] [DMG]              },
[1770364781.940] [2443:2465] [DMG]
[1770364781.940] [2443:2465] [DMG]              AttributeReportIB =
[1770364781.940] [2443:2465] [DMG]              {
[1770364781.940] [2443:2465] [DMG]                      AttributeDataIB =
[1770364781.940] [2443:2465] [DMG]                      {
[1770364781.940] [2443:2465] [DMG]                              DataVersion = 0x3bf1e4f2,
[1770364781.940] [2443:2465] [DMG]                              AttributePathIB =
[1770364781.940] [2443:2465] [DMG]                              {
[1770364781.940] [2443:2465] [DMG]                                      Endpoint = 0x0,
[1770364781.940] [2443:2465] [DMG]                                      Cluster = 0x31,
[1770364781.940] [2443:2465] [DMG]                                      Attribute = 0x0000_0003,
[1770364781.941] [2443:2465] [DMG]                              }
[1770364781.941] [2443:2465] [DMG]
[1770364781.941] [2443:2465] [DMG]                              Data = 20 (unsigned),
[1770364781.941] [2443:2465] [DMG]                      },
[1770364781.941] [2443:2465] [DMG]
[1770364781.941] [2443:2465] [DMG]              },
[1770364781.941] [2443:2465] [DMG]
[1770364781.941] [2443:2465] [DMG]      ],
[1770364781.941] [2443:2465] [DMG]
[1770364781.941] [2443:2465] [DMG]      SuppressResponse = true,
[1770364781.941] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364781.941] [2443:2465] [DMG] }
[1770364781.949] [2443:2465] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1770364781.949] [2443:2465] [SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010
[1770364781.950] [2443:2465] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1770364781.950] [2443:2465] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1770364781.950] [2443:2465] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1770364781.950] [2443:2465] [CTL] Performing next commissioning step 'ArmFailSafe'
[1770364781.950] [2443:2465] [CTL] Arming failsafe (60 seconds)
[1770364781.950] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364781.950] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364781.950] [2443:2465] [EM] <<< [E:51543i S:1492 M:264736069] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770364781.951] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364782.319] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364782.419] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364782.419] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364782.420] [2443:2465] [EM] >>> [E:51543i S:1492 M:78474674] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770364782.420] [2443:2465] [EM] Found matching exchange: 51543i, Delegate: 0xffff8000db18
[1770364782.420] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364782.420] [2443:2465] [DMG] InvokeResponseMessage =
[1770364782.420] [2443:2465] [DMG] {
[1770364782.420] [2443:2465] [DMG]      suppressResponse = false,
[1770364782.421] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364782.421] [2443:2465] [DMG]      [
[1770364782.421] [2443:2465] [DMG]              InvokeResponseIB =
[1770364782.421] [2443:2465] [DMG]              {
[1770364782.421] [2443:2465] [DMG]                      CommandDataIB =
[1770364782.421] [2443:2465] [DMG]                      {
[1770364782.421] [2443:2465] [DMG]                              CommandPathIB =
[1770364782.421] [2443:2465] [DMG]                              {
[1770364782.422] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364782.422] [2443:2465] [DMG]                                      ClusterId = 0x30,
[1770364782.422] [2443:2465] [DMG]                                      CommandId = 0x1,
[1770364782.422] [2443:2465] [DMG]                              },
[1770364782.422] [2443:2465] [DMG]
[1770364782.422] [2443:2465] [DMG]                              CommandFields =
[1770364782.422] [2443:2465] [DMG]                              {
[1770364782.423] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364782.423] [2443:2465] [DMG]                                      0x1 = "" (0 chars),
[1770364782.423] [2443:2465] [DMG]                              },
[1770364782.423] [2443:2465] [DMG]                      },
[1770364782.423] [2443:2465] [DMG]
[1770364782.423] [2443:2465] [DMG]              },
[1770364782.423] [2443:2465] [DMG]
[1770364782.423] [2443:2465] [DMG]      ],
[1770364782.424] [2443:2465] [DMG]
[1770364782.424] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364782.424] [2443:2465] [DMG] },
[1770364782.424] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770364782.425] [2443:2465] [CTL] Received ArmFailSafe response errorCode=0
[1770364782.425] [2443:2465] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1770364782.425] [2443:2465] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1770364782.425] [2443:2465] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1770364782.425] [2443:2465] [CTL] Setting Regulatory Config
[1770364782.425] [2443:2465] [CTL] Device does not support configurable regulatory location
[1770364782.425] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364782.425] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364782.426] [2443:2465] [EM] <<< [E:51544i S:1492 M:264736070] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1770364782.427] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364782.427] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364782.612] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364782.615] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364782.616] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364782.616] [2443:2465] [EM] >>> [E:51544i S:1492 M:78474675] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770364782.616] [2443:2465] [EM] Found matching exchange: 51544i, Delegate: 0xffff8000e0b8
[1770364782.616] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364782.616] [2443:2465] [DMG] InvokeResponseMessage =
[1770364782.616] [2443:2465] [DMG] {
[1770364782.616] [2443:2465] [DMG]      suppressResponse = false,
[1770364782.617] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364782.617] [2443:2465] [DMG]      [
[1770364782.617] [2443:2465] [DMG]              InvokeResponseIB =
[1770364782.617] [2443:2465] [DMG]              {
[1770364782.617] [2443:2465] [DMG]                      CommandDataIB =
[1770364782.617] [2443:2465] [DMG]                      {
[1770364782.617] [2443:2465] [DMG]                              CommandPathIB =
[1770364782.617] [2443:2465] [DMG]                              {
[1770364782.617] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364782.617] [2443:2465] [DMG]                                      ClusterId = 0x30,
[1770364782.617] [2443:2465] [DMG]                                      CommandId = 0x3,
[1770364782.618] [2443:2465] [DMG]                              },
[1770364782.618] [2443:2465] [DMG]
[1770364782.618] [2443:2465] [DMG]                              CommandFields =
[1770364782.618] [2443:2465] [DMG]                              {
[1770364782.618] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364782.618] [2443:2465] [DMG]                                      0x1 = "" (0 chars),
[1770364782.618] [2443:2465] [DMG]                              },
[1770364782.618] [2443:2465] [DMG]                      },
[1770364782.618] [2443:2465] [DMG]
[1770364782.618] [2443:2465] [DMG]              },
[1770364782.619] [2443:2465] [DMG]
[1770364782.619] [2443:2465] [DMG]      ],
[1770364782.619] [2443:2465] [DMG]
[1770364782.619] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364782.619] [2443:2465] [DMG] },
[1770364782.619] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1770364782.619] [2443:2465] [CTL] Received SetRegulatoryConfig response errorCode=0
[1770364782.619] [2443:2465] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1770364782.619] [2443:2465] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1770364782.619] [2443:2465] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1770364782.620] [2443:2465] [CTL] Setting Terms and Conditions
[1770364782.620] [2443:2465] [CTL] Setting Terms and Conditions: Skipped
[1770364782.620] [2443:2465] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'
[1770364782.620] [2443:2465] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1770364782.620] [2443:2465] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770364782.620] [2443:2465] [CTL] Sending request for PAI certificate
[1770364782.620] [2443:2465] [CTL] Sending Certificate Chain request to 0xffff800217c0 device
[1770364782.620] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364782.627] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364782.627] [2443:2465] [EM] <<< [E:51545i S:1492 M:264736071] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770364782.628] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364782.628] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364782.807] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364782.909] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364782.910] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364783.686] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364783.687] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364784.271] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364784.272] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364784.272] [2443:2465] [EM] >>> [E:51545i S:1492 M:78474676] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[1770364784.272] [2443:2465] [EM] Found matching exchange: 51545i, Delegate: 0xffff8000db18
[1770364784.272] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364784.272] [2443:2465] [DMG] InvokeResponseMessage =
[1770364784.273] [2443:2465] [DMG] {
[1770364784.273] [2443:2465] [DMG]      suppressResponse = false,
[1770364784.273] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364784.273] [2443:2465] [DMG]      [
[1770364784.273] [2443:2465] [DMG]              InvokeResponseIB =
[1770364784.273] [2443:2465] [DMG]              {
[1770364784.273] [2443:2465] [DMG]                      CommandDataIB =
[1770364784.273] [2443:2465] [DMG]                      {
[1770364784.273] [2443:2465] [DMG]                              CommandPathIB =
[1770364784.274] [2443:2465] [DMG]                              {
[1770364784.274] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364784.274] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364784.274] [2443:2465] [DMG]                                      CommandId = 0x3,
[1770364784.274] [2443:2465] [DMG]                              },
[1770364784.274] [2443:2465] [DMG]
[1770364784.274] [2443:2465] [DMG]                              CommandFields =
[1770364784.275] [2443:2465] [DMG]                              {
[1770364784.275] [2443:2465] [DMG]                                      0x0 = [
[1770364784.275] [2443:2465] [DMG]                                                      0x30, 0x82, 0x01, 0xcb, 0x30, 0x82, 0x01, 0x71, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x56, 0xad, 0x82, 0x22, 0xad, 0x94, 0x5b, 0x64, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x30, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x0f, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x54, 0x65, 0x73, 0x74, 0x20, 0x50, 0x41, 0x41, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x41, 0x9a, 0x93, 0x15, 0xc2, 0x17, 0x3e, 0x0c, 0x8c, 0x87, 0x6d, 0x03, 0xcc, 0xfc, 0x94, 0x48, 0x52, 0x64, 0x7f, 0x7f, 0xec, 0x5e, 0x50, 0x82, 0xf4, 0x05, 0x99, 0x28, 0xec, 0xa8, 0x94, 0xc5, 0x94, 0x15, 0x13, 0x09, 0xac, 0x63, 0x1e, 0x4c, 0xb0, 0x33, 0x92, 0xaf, 0x68, 0x4b, 0x0b, 0xaf, 0xb7, 0xe6, 0x5b, 0x3b, 0x81, 0x62, 0xc2, 0xf5, 0x2b, 0xf9, 0x31, 0xb8, 0xe7, 0x7a, 0xaa, 0x82, 0xa3, 0x66, 0x30, 0x64, 0x30, 0x12, 0x06, 0x03, 0x55, 0x1d, 0x
[1770364784.275] [2443:2465] [DMG]                                      ] (463 bytes)
[1770364784.276] [2443:2465] [DMG]                              },
[1770364784.276] [2443:2465] [DMG]                      },
[1770364784.276] [2443:2465] [DMG]
[1770364784.276] [2443:2465] [DMG]              },
[1770364784.276] [2443:2465] [DMG]
[1770364784.276] [2443:2465] [DMG]      ],
[1770364784.277] [2443:2465] [DMG]
[1770364784.277] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364784.277] [2443:2465] [DMG] },
[1770364784.277] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770364784.277] [2443:2465] [CTL] Received certificate chain from the device
[1770364784.277] [2443:2465] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1770364784.277] [2443:2465] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1770364784.277] [2443:2465] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1770364784.278] [2443:2465] [CTL] Sending request for DAC certificate
[1770364784.278] [2443:2465] [CTL] Sending Certificate Chain request to 0xffff800217c0 device
[1770364784.278] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364784.278] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364784.278] [2443:2465] [EM] <<< [E:51546i S:1492 M:264736072] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770364784.279] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364784.279] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364784.563] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364784.758] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364784.759] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364785.151] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364785.152] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364785.345] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364785.346] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364785.346] [2443:2465] [EM] >>> [E:51546i S:1492 M:78474677] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[1770364785.346] [2443:2465] [EM] Found matching exchange: 51546i, Delegate: 0xffff8000e0b8
[1770364785.346] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364785.346] [2443:2465] [DMG] InvokeResponseMessage =
[1770364785.347] [2443:2465] [DMG] {
[1770364785.347] [2443:2465] [DMG]      suppressResponse = false,
[1770364785.347] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364785.347] [2443:2465] [DMG]      [
[1770364785.347] [2443:2465] [DMG]              InvokeResponseIB =
[1770364785.347] [2443:2465] [DMG]              {
[1770364785.347] [2443:2465] [DMG]                      CommandDataIB =
[1770364785.347] [2443:2465] [DMG]                      {
[1770364785.347] [2443:2465] [DMG]                              CommandPathIB =
[1770364785.348] [2443:2465] [DMG]                              {
[1770364785.348] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364785.348] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364785.348] [2443:2465] [DMG]                                      CommandId = 0x3,
[1770364785.348] [2443:2465] [DMG]                              },
[1770364785.349] [2443:2465] [DMG]
[1770364785.349] [2443:2465] [DMG]                              CommandFields =
[1770364785.349] [2443:2465] [DMG]                              {
[1770364785.349] [2443:2465] [DMG]                                      0x0 = [
[1770364785.350] [2443:2465] [DMG]                                                      0x30, 0x82, 0x01, 0xe7, 0x30, 0x82, 0x01, 0x8e, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x46, 0x7f, 0x57, 0x62, 0xc8, 0xdc, 0x90, 0xd5, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x33, 0x33, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x53, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x44, 0x41, 0x43, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x2f, 0x30, 0x78, 0x38, 0x30, 0x31, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x31, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x39, 0xef, 0x6c, 0x9d, 0x9c, 0x99, 0x7b, 0xa2, 0xc7, 0x31, 0x9a, 0x4c, 0x73, 0xc9, 0xbf, 0x47, 0xdb, 0xcd, 0xbc, 0x42, 0xc5, 0x41, 0x3e, 0xec, 0x14, 0x52, 0x75, 0xb8, 0x8f, 0xc1, 0x1a, 0xb1, 0xad, 0x0b, 0xc3, 0x3e, 0xf1, 0x4c, 0x27, 0x
[1770364785.350] [2443:2465] [DMG]                                      ] (491 bytes)
[1770364785.350] [2443:2465] [DMG]                              },
[1770364785.350] [2443:2465] [DMG]                      },
[1770364785.350] [2443:2465] [DMG]
[1770364785.351] [2443:2465] [DMG]              },
[1770364785.351] [2443:2465] [DMG]
[1770364785.351] [2443:2465] [DMG]      ],
[1770364785.351] [2443:2465] [DMG]
[1770364785.351] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364785.351] [2443:2465] [DMG] },
[1770364785.351] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770364785.351] [2443:2465] [CTL] Received certificate chain from the device
[1770364785.352] [2443:2465] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1770364785.352] [2443:2465] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1770364785.352] [2443:2465] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1770364785.352] [2443:2465] [CTL] Sending Attestation Request to the device.
[1770364785.352] [2443:2465] [CTL] Sending Attestation request to 0xffff800217c0 device
[1770364785.352] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364785.352] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364785.352] [2443:2465] [EM] <<< [E:51547i S:1492 M:264736073] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770364785.353] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364785.354] [2443:2465] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770364785.354] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364785.635] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364785.736] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364785.737] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364786.029] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364786.029] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364786.321] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364786.321] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364786.322] [2443:2465] [EM] >>> [E:51547i S:1492 M:78474678] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[1770364786.322] [2443:2465] [EM] Found matching exchange: 51547i, Delegate: 0xffff8000db18
[1770364786.322] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364786.322] [2443:2465] [DMG] InvokeResponseMessage =
[1770364786.322] [2443:2465] [DMG] {
[1770364786.322] [2443:2465] [DMG]      suppressResponse = false,
[1770364786.323] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364786.323] [2443:2465] [DMG]      [
[1770364786.323] [2443:2465] [DMG]              InvokeResponseIB =
[1770364786.323] [2443:2465] [DMG]              {
[1770364786.323] [2443:2465] [DMG]                      CommandDataIB =
[1770364786.323] [2443:2465] [DMG]                      {
[1770364786.323] [2443:2465] [DMG]                              CommandPathIB =
[1770364786.323] [2443:2465] [DMG]                              {
[1770364786.323] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364786.324] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364786.324] [2443:2465] [DMG]                                      CommandId = 0x1,
[1770364786.324] [2443:2465] [DMG]                              },
[1770364786.324] [2443:2465] [DMG]
[1770364786.324] [2443:2465] [DMG]                              CommandFields =
[1770364786.324] [2443:2465] [DMG]                              {
[1770364786.324] [2443:2465] [DMG]                                      0x0 = [
[1770364786.325] [2443:2465] [DMG]                                                      0x15, 0x31, 0x01, 0x1b, 0x02, 0x30, 0x82, 0x02, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x02, 0x08, 0x30, 0x82, 0x02, 0x04, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x82, 0x01, 0x70, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x01, 0x61, 0x04, 0x82, 0x01, 0x5d, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0xf1, 0xff, 0x36, 0x02, 0x05, 0x00, 0x80, 0x05, 0x01, 0x80, 0x05, 0x02, 0x80, 0x05, 0x03, 0x80, 0x05, 0x04, 0x80, 0x05, 0x05, 0x80, 0x05, 0x06, 0x80, 0x05, 0x07, 0x80, 0x05, 0x08, 0x80, 0x05, 0x09, 0x80, 0x05, 0x0a, 0x80, 0x05, 0x0b, 0x80, 0x05, 0x0c, 0x80, 0x05, 0x0d, 0x80, 0x05, 0x0e, 0x80, 0x05, 0x0f, 0x80, 0x05, 0x10, 0x80, 0x05, 0x11, 0x80, 0x05, 0x12, 0x80, 0x05, 0x13, 0x80, 0x05, 0x14, 0x80, 0x05, 0x15, 0x80, 0x05, 0x16, 0x80, 0x05, 0x17, 0x80, 0x05, 0x18, 0x80, 0x05, 0x19, 0x80, 0x05, 0x1a, 0x80, 0x05, 0x1b, 0x80, 0x05, 0x1c, 0x80, 0x05, 0x1d, 0x80, 0x05, 0x1e, 0x80, 0x05, 0x1f, 0x80, 0x05, 0x20, 0x80, 0x05, 0x21, 0x80, 0x05, 0x22, 0x80, 0x05, 0x23, 0x80, 0x05, 0x24, 0x80, 0x05, 0x25, 0x80, 0x05, 0x26, 0x80, 0x05, 0x27, 0x80, 0x05, 0x28, 0x80, 0x05, 0x29, 0x80, 0x05, 0x2a, 0x80, 0x05, 0x2b, 0x80, 0x05, 0x2c, 0x80, 0x05, 0x2d, 0x80, 0x05, 0x2e, 0x80, 0x05, 0x2f, 0x80, 0x05, 0x30, 0x80, 0x05, 0x31, 0x80, 0x05, 0x32, 0x80, 0x05, 0x33, 0x80, 0x05, 0x34, 0x80, 0x05, 0x35, 0x80, 0x05, 0x36, 0x80, 0x05, 0x37, 0x80, 0x05, 0x38, 0x80, 0x05, 0x39, 0x80, 0x05, 0x3a, 0x80, 0x05, 0x3b, 0x80, 0x05, 0x3c, 0x80, 0x05, 0x3d, 0x80, 0x05, 0x3e, 0x80, 0x05, 0x3f, 0x80, 0x05, 0x40, 0x80, 0x05, 0x41, 0x80, 0x05, 0x42, 0x80, 0x05, 0x43, 0x80, 0x
[1770364786.325] [2443:2465] [DMG]                                      ] (583 bytes)
[1770364786.325] [2443:2465] [DMG]                                      0x1 = [
[1770364786.325] [2443:2465] [DMG]                                                      0x9d, 0xcc, 0x45, 0x27, 0x0b, 0xcd, 0x5f, 0xd1, 0x2b, 0xda, 0x38, 0xdf, 0x19, 0x55, 0xa0, 0xc6, 0x8e, 0x10, 0xa0, 0x75, 0x3e, 0xcd, 0x90, 0x1d, 0x07, 0xc6, 0xa3, 0x7f, 0x7c, 0x7c, 0x5b, 0x44, 0x7a, 0x6a, 0xdc, 0xd1, 0x04, 0x15, 0x63, 0x50, 0x33, 0x13, 0x6e, 0x36, 0x1d, 0x2e, 0x20, 0x73, 0x62, 0xe7, 0xa4, 0x77, 0xee, 0x37, 0xbc, 0xe4, 0xa8, 0x86, 0x41, 0x80, 0xea, 0x39, 0x94, 0x3f,
[1770364786.325] [2443:2465] [DMG]                                      ] (64 bytes)
[1770364786.325] [2443:2465] [DMG]                              },
[1770364786.325] [2443:2465] [DMG]                      },
[1770364786.325] [2443:2465] [DMG]
[1770364786.326] [2443:2465] [DMG]              },
[1770364786.326] [2443:2465] [DMG]
[1770364786.326] [2443:2465] [DMG]      ],
[1770364786.326] [2443:2465] [DMG]
[1770364786.326] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364786.326] [2443:2465] [DMG] },
[1770364786.326] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1770364786.326] [2443:2465] [CTL] Received Attestation Information from the device
[1770364786.326] [2443:2465] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1770364786.326] [2443:2465] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[1770364786.327] [2443:2465] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1770364786.327] [2443:2465] [CTL] Performing next commissioning step 'AttestationVerification'
[1770364786.327] [2443:2465] [CTL] Verifying Device Attestation information received from the device
[1770364786.353] [2443:2465] [-] Device candidate DAC chain details:
[1770364786.353] [2443:2465] [-] --> DAC's VID: 0xFFF1, PID: 0x8010
[1770364786.353] [2443:2465] [-] ==== DAC certificate considered (491 bytes) ====
[1770364786.353] [2443:2465] [-] -----BEGIN CERTIFICATE-----
[1770364786.353] [2443:2465] [-] MIIB5zCCAY6gAwIBAgIIRn9XYsjckNUwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770364786.353] [2443:2465] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
[1770364786.353] [2443:2465] [-] RjEwIBcNMjIwMzMxMDAwMDAwWhgPOTk5OTEyMzEyMzU5NTlaMFMxJTAjBgNVBAMM
[1770364786.354] [2443:2465] [-] HE1hdHRlciBEZXYgREFDIDB4RkZGMS8weDgwMTAxFDASBgorBgEEAYKifAIBDARG
[1770364786.354] [2443:2465] [-] RkYxMRQwEgYKKwYBBAGConwCAgwEODAxMDBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770364786.354] [2443:2465] [-] A0IABDnvbJ2cmXuixzGaTHPJv0fbzbxCxUE+7BRSdbiPwRqxrQvDPvFMJ5QEQp8v
[1770364786.354] [2443:2465] [-] XucKBRty5se55zVO2vkqtP/4hC+jYDBeMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/
[1770364786.354] [2443:2465] [-] BAQDAgeAMB0GA1UdDgQWBBQy/CfR71NDovNk8Cz0cMtnR4DlqjAfBgNVHSMEGDAW
[1770364786.354] [2443:2465] [-] gBRjVA5H9kscONE4hKRi0WwZXY/7PDAKBggqhkjOPQQDAgNHADBEAiBvEbIFC9PS
[1770364786.354] [2443:2465] [-] 42wkYTAIbCIBsIz5nVp3sjqQBQD77wkTsgIgE2q2oLuL1PSt+AoSNM/vtn8K+3NV
[1770364786.354] [2443:2465] [-] 8dykctoWrEo2ZOU=
[1770364786.354] [2443:2465] [-] -----END CERTIFICATE-----
[1770364786.356] [2443:2465] [-] --> DAC certificate SKID: 32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
[1770364786.359] [2443:2465] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770364786.359] [2443:2465] [-] ==== PAI certificate considered (463 bytes) ====
[1770364786.359] [2443:2465] [-] -----BEGIN CERTIFICATE-----
[1770364786.359] [2443:2465] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770364786.359] [2443:2465] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMjAyMDUw
[1770364786.359] [2443:2465] [-] MDAwMDBaGA85OTk5MTIzMTIzNTk1OVowPTElMCMGA1UEAwwcTWF0dGVyIERldiBQ
[1770364786.359] [2443:2465] [-] QUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZGRjEwWTATBgcqhkjO
[1770364786.359] [2443:2465] [-] PQIBBggqhkjOPQMBBwNCAARBmpMVwhc+DIyHbQPM/JRIUmR/f+xeUIL0BZko7KiU
[1770364786.359] [2443:2465] [-] xZQVEwmsYx5MsDOSr2hLC6+35ls7gWLC9Sv5MbjneqqCo2YwZDASBgNVHRMBAf8E
[1770364786.359] [2443:2465] [-] CDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUY1QOR/ZLHDjROISk
[1770364786.359] [2443:2465] [-] YtFsGV2P+zwwHwYDVR0jBBgwFoAUav0idx9RH+y/FkGXZxDc3DGhcX4wCgYIKoZI
[1770364786.359] [2443:2465] [-] zj0EAwIDSAAwRQIhALLvJ/Sa6bUPuR7qyUxNC9u415KcbLiPrOUpNo0SBUwMAiBl
[1770364786.359] [2443:2465] [-] Xckrhr2QmIKmxiF3uCXX0F7b58Ivn+pxIg5+pwP4kQ==
[1770364786.359] [2443:2465] [-] -----END CERTIFICATE-----
[1770364786.362] [2443:2465] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770364786.364] [2443:2465] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770364786.375] [2443:2465] [-] ==== PAA certificate considered (449 bytes) ====
[1770364786.375] [2443:2465] [-] -----BEGIN CERTIFICATE-----
[1770364786.375] [2443:2465] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770364786.375] [2443:2465] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMTA2Mjgx
[1770364786.375] [2443:2465] [-] NDIzNDNaGA85OTk5MTIzMTIzNTk1OVowMDEYMBYGA1UEAwwPTWF0dGVyIFRlc3Qg
[1770364786.375] [2443:2465] [-] UEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770364786.375] [2443:2465] [-] A0IABLbLY3KIfyko9brIGqnZOuJDHK2p154kL2UXfvnO2TKijs0Duq9qj8oYShpQ
[1770364786.375] [2443:2465] [-] NUKWDUU/MD8fGUIddR6Pjxqam3WjZjBkMBIGA1UdEwEB/wQIMAYBAf8CAQEwDgYD
[1770364786.375] [2443:2465] [-] VR0PAQH/BAQDAgEGMB0GA1UdDgQWBBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAfBgNV
[1770364786.375] [2443:2465] [-] HSMEGDAWgBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAKBggqhkjOPQQDAgNHADBEAiBQ
[1770364786.375] [2443:2465] [-] qoAC9NkyqaAFOPZTaK0P/8jvu8m+t9pWmDXPmqdRDgIgI7rI/g8j51RFtlM5CBpH
[1770364786.375] [2443:2465] [-] mUkpxyqvChVI1A0DTVFLJd4=
[1770364786.375] [2443:2465] [-] -----END CERTIFICATE-----
[1770364786.378] [2443:2465] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770364786.380] [2443:2465] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770364786.394] [2443:2465] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770364786.396] [2443:2465] [-] Device certification declaration details:
[1770364786.396] [2443:2465] [-] --> VID: 0xFFF1
[1770364786.396] [2443:2465] [-] --> Device type ID: 0x0000_0016
[1770364786.396] [2443:2465] [-] --> Certification type: 0 (Development and testing)
[1770364786.396] [2443:2465] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1770364786.396] [2443:2465] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1770364786.396] [2443:2465] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1770364786.396] [2443:2465] [CTL] Verifying the device's DAC chain revocation status
[1770364786.396] [2443:2465] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770364786.396] [2443:2465] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1770364786.396] [2443:2465] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1770364786.396] [2443:2465] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1770364786.397] [2443:2465] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1770364786.397] [2443:2465] [CTL] Sending CSR request to 0xffff800217c0 device
[1770364786.397] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364786.397] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364786.397] [2443:2465] [EM] <<< [E:51548i S:1492 M:264736074] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770364786.398] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364786.398] [2443:2465] [CTL] Sent CSR request, waiting for the CSR
[1770364786.398] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364786.513] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364786.709] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364786.709] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364787.099] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364787.100] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364787.100] [2443:2465] [EM] >>> [E:51548i S:1492 M:78474679] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1770364787.100] [2443:2465] [EM] Found matching exchange: 51548i, Delegate: 0xffff8000e0b8
[1770364787.100] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364787.100] [2443:2465] [DMG] InvokeResponseMessage =
[1770364787.100] [2443:2465] [DMG] {
[1770364787.101] [2443:2465] [DMG]      suppressResponse = false,
[1770364787.101] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364787.101] [2443:2465] [DMG]      [
[1770364787.101] [2443:2465] [DMG]              InvokeResponseIB =
[1770364787.101] [2443:2465] [DMG]              {
[1770364787.101] [2443:2465] [DMG]                      CommandDataIB =
[1770364787.101] [2443:2465] [DMG]                      {
[1770364787.101] [2443:2465] [DMG]                              CommandPathIB =
[1770364787.101] [2443:2465] [DMG]                              {
[1770364787.102] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364787.102] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364787.102] [2443:2465] [DMG]                                      CommandId = 0x5,
[1770364787.102] [2443:2465] [DMG]                              },
[1770364787.102] [2443:2465] [DMG]
[1770364787.102] [2443:2465] [DMG]                              CommandFields =
[1770364787.102] [2443:2465] [DMG]                              {
[1770364787.102] [2443:2465] [DMG]                                      0x0 = [
[1770364787.103] [2443:2465] [DMG]                                                      0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xcd, 0xa1, 0x8c, 0x9c, 0x2e, 0xe3, 0xfd, 0xca, 0xb9, 0x48, 0xff, 0x1c, 0x08, 0xf2, 0x90, 0xf8, 0xb8, 0x92, 0x44, 0xf6, 0x76, 0x0d, 0x0a, 0xf5, 0x5e, 0xe0, 0x60, 0x83, 0xfa, 0x92, 0x97, 0x3e, 0xb0, 0x9e, 0x72, 0x90, 0xc6, 0x4c, 0x39, 0x74, 0x85, 0x37, 0x44, 0xc1, 0x4f, 0x6c, 0xae, 0x95, 0x30, 0x92, 0x18, 0x6c, 0x97, 0xde, 0xee, 0x7b, 0xed, 0x22, 0x6d, 0x6b, 0x4c, 0x3c, 0xfd, 0xc0, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x20, 0x0a, 0x67, 0xf4, 0x0c, 0xfb, 0xbc, 0x86, 0xc6, 0xd4, 0xf2, 0x54, 0x9f, 0xa1, 0xeb, 0x10, 0x64, 0xd7, 0xb3, 0xc7, 0x5a, 0x70, 0xaf, 0x7e, 0x15, 0xdf, 0x70, 0x01, 0x11, 0x80, 0xd5, 0x9f, 0xbf, 0x02, 0x21, 0x00, 0xad, 0x91, 0xa3, 0x68, 0x81, 0x98, 0xa1, 0x00, 0x04, 0x5f, 0x38, 0x1b, 0x80, 0x9c, 0x1a, 0xb3, 0x5f, 0xba, 0xf3, 0x33, 0x26, 0x04, 0x04, 0x8f, 0x9d, 0xee, 0xa2, 0x50, 0xb2, 0xb5, 0x3c, 0x16, 0x30, 0x02, 0x20, 0x10, 0x16, 0x3e, 0x93, 0x7d, 0x46, 0x8e, 0x0b, 0x8c, 0xb8, 0xcf, 0xe4, 0x64, 0x2e, 0x5f, 0x27, 0xc8, 0x99, 0xcc, 0xbf, 0x53, 0xf2, 0x2c, 0xe6, 0x07, 0x09, 0xd9, 0x4c, 0x86, 0xc9, 0x8e, 0x75, 0x18,
[1770364787.103] [2443:2465] [DMG]                                      ] (261 bytes)
[1770364787.103] [2443:2465] [DMG]                                      0x1 = [
[1770364787.104] [2443:2465] [DMG]                                                      0x76, 0x49, 0x65, 0xec, 0x5f, 0xfc, 0xc5, 0x4b, 0x20, 0x17, 0x63, 0x27, 0x49, 0x2f, 0xca, 0x33, 0x0f, 0xcd, 0x76, 0xc2, 0xa8, 0xde, 0xab, 0x0b, 0x2a, 0x2f, 0x98, 0xa5, 0x2d, 0x62, 0x56, 0xbd, 0x61, 0xbd, 0x2a, 0x8f, 0xac, 0x62, 0x6f, 0x79, 0x8e, 0x31, 0x69, 0xf1, 0xb0, 0x72, 0x08, 0x41, 0x77, 0x32, 0x62, 0xd8, 0x53, 0x7d, 0x04, 0xdf, 0xd0, 0x67, 0xe2, 0x6e, 0x49, 0x40, 0x7b, 0x23,
[1770364787.104] [2443:2465] [DMG]                                      ] (64 bytes)
[1770364787.104] [2443:2465] [DMG]                              },
[1770364787.104] [2443:2465] [DMG]                      },
[1770364787.104] [2443:2465] [DMG]
[1770364787.104] [2443:2465] [DMG]              },
[1770364787.105] [2443:2465] [DMG]
[1770364787.105] [2443:2465] [DMG]      ],
[1770364787.105] [2443:2465] [DMG]
[1770364787.105] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364787.105] [2443:2465] [DMG] },
[1770364787.105] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1770364787.105] [2443:2465] [CTL] Received certificate signing request from the device
[1770364787.105] [2443:2465] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1770364787.105] [2443:2465] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1770364787.106] [2443:2465] [CTL] Performing next commissioning step 'ValidateCSR'
[1770364787.114] [2443:2465] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1770364787.114] [2443:2465] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1770364787.114] [2443:2465] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1770364787.114] [2443:2465] [CTL] Getting certificate chain for the device from the issuer
[1770364787.120] [2443:2465] [CTL] Verifying Certificate Signing Request
[1770364787.124] [2443:2465] [CTL] Generating NOC
[1770364787.125] [2443:2465] [CTL] Providing certificate chain to the commissioner
[1770364787.125] [2443:2465] [CTL] Received callback from the CA for NOC Chain generation. Status src/controller/ExampleOperationalCredentialsIssuer.cpp:409: Success
[1770364787.125] [2443:2465] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1770364787.125] [2443:2465] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1770364787.125] [2443:2465] [CTL] Sending root certificate to the device
[1770364787.125] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364787.125] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364787.126] [2443:2465] [EM] <<< [E:51549i S:1492 M:264736075] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1770364787.127] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364787.127] [2443:2465] [CTL] Sent root certificate to the device
[1770364787.128] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364787.584] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364787.780] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364787.878] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364787.879] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364787.879] [2443:2465] [EM] >>> [E:51549i S:1492 M:78474680] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770364787.879] [2443:2465] [EM] Found matching exchange: 51549i, Delegate: 0xffff8000db18
[1770364787.880] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364787.880] [2443:2465] [DMG] InvokeResponseMessage =
[1770364787.880] [2443:2465] [DMG] {
[1770364787.880] [2443:2465] [DMG]      suppressResponse = false,
[1770364787.880] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364787.880] [2443:2465] [DMG]      [
[1770364787.880] [2443:2465] [DMG]              InvokeResponseIB =
[1770364787.880] [2443:2465] [DMG]              {
[1770364787.881] [2443:2465] [DMG]                      CommandStatusIB =
[1770364787.881] [2443:2465] [DMG]                      {
[1770364787.881] [2443:2465] [DMG]                              CommandPathIB =
[1770364787.881] [2443:2465] [DMG]                              {
[1770364787.881] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364787.881] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364787.881] [2443:2465] [DMG]                                      CommandId = 0xb,
[1770364787.881] [2443:2465] [DMG]                              },
[1770364787.882] [2443:2465] [DMG]
[1770364787.882] [2443:2465] [DMG]                              StatusIB =
[1770364787.882] [2443:2465] [DMG]                              {
[1770364787.882] [2443:2465] [DMG]                                      status = 0x00 (SUCCESS),
[1770364787.882] [2443:2465] [DMG]                              },
[1770364787.882] [2443:2465] [DMG]
[1770364787.882] [2443:2465] [DMG]                      },
[1770364787.882] [2443:2465] [DMG]
[1770364787.883] [2443:2465] [DMG]              },
[1770364787.883] [2443:2465] [DMG]
[1770364787.883] [2443:2465] [DMG]      ],
[1770364787.883] [2443:2465] [DMG]
[1770364787.883] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364787.883] [2443:2465] [DMG] },
[1770364787.883] [2443:2465] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1770364787.883] [2443:2465] [CTL] Device confirmed that it has received the root certificate
[1770364787.884] [2443:2465] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1770364787.884] [2443:2465] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1770364787.884] [2443:2465] [CTL] Performing next commissioning step 'SendNOC'
[1770364787.884] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364787.884] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364787.885] [2443:2465] [EM] <<< [E:51550i S:1492 M:264736076] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1770364787.886] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364787.886] [2443:2465] [CTL] Sent operational certificate to the device
[1770364787.886] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364788.268] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364788.560] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364788.755] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364788.758] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364788.758] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364788.759] [2443:2465] [EM] >>> [E:51550i S:1492 M:78474681] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770364788.759] [2443:2465] [EM] Found matching exchange: 51550i, Delegate: 0xffff8000e0b8
[1770364788.759] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364788.759] [2443:2465] [DMG] InvokeResponseMessage =
[1770364788.759] [2443:2465] [DMG] {
[1770364788.760] [2443:2465] [DMG]      suppressResponse = false,
[1770364788.760] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364788.760] [2443:2465] [DMG]      [
[1770364788.760] [2443:2465] [DMG]              InvokeResponseIB =
[1770364788.760] [2443:2465] [DMG]              {
[1770364788.760] [2443:2465] [DMG]                      CommandDataIB =
[1770364788.760] [2443:2465] [DMG]                      {
[1770364788.760] [2443:2465] [DMG]                              CommandPathIB =
[1770364788.760] [2443:2465] [DMG]                              {
[1770364788.761] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364788.761] [2443:2465] [DMG]                                      ClusterId = 0x3e,
[1770364788.761] [2443:2465] [DMG]                                      CommandId = 0x8,
[1770364788.761] [2443:2465] [DMG]                              },
[1770364788.761] [2443:2465] [DMG]
[1770364788.761] [2443:2465] [DMG]                              CommandFields =
[1770364788.761] [2443:2465] [DMG]                              {
[1770364788.762] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364788.762] [2443:2465] [DMG]                                      0x1 = 1 (unsigned),
[1770364788.762] [2443:2465] [DMG]                              },
[1770364788.762] [2443:2465] [DMG]                      },
[1770364788.762] [2443:2465] [DMG]
[1770364788.762] [2443:2465] [DMG]              },
[1770364788.762] [2443:2465] [DMG]
[1770364788.762] [2443:2465] [DMG]      ],
[1770364788.763] [2443:2465] [DMG]
[1770364788.763] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364788.763] [2443:2465] [DMG] },
[1770364788.763] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1770364788.763] [2443:2465] [CTL] Device returned status 0 on receiving the NOC
[1770364788.763] [2443:2465] [CTL] Operational credentials provisioned on device 0xffff800217c0
[1770364788.763] [2443:2465] [TOO] Secure Pairing Success
[1770364788.763] [2443:2465] [TOO] CASE establishment successful
[1770364788.763] [2443:2465] [CTL] Successfully finished commissioning step 'SendNOC'
[1770364788.763] [2443:2465] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1770364788.763] [2443:2465] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1770364788.764] [2443:2465] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1770364788.764] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364788.764] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364788.764] [2443:2465] [EM] <<< [E:51551i S:1492 M:264736077] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[1770364788.765] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364788.765] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364789.340] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364789.440] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364789.441] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364789.441] [2443:2465] [EM] >>> [E:51551i S:1492 M:78474682] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770364789.441] [2443:2465] [EM] Found matching exchange: 51551i, Delegate: 0xffff8000db18
[1770364789.441] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364789.442] [2443:2465] [DMG] InvokeResponseMessage =
[1770364789.442] [2443:2465] [DMG] {
[1770364789.442] [2443:2465] [DMG]      suppressResponse = false,
[1770364789.442] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364789.442] [2443:2465] [DMG]      [
[1770364789.442] [2443:2465] [DMG]              InvokeResponseIB =
[1770364789.442] [2443:2465] [DMG]              {
[1770364789.442] [2443:2465] [DMG]                      CommandDataIB =
[1770364789.443] [2443:2465] [DMG]                      {
[1770364789.443] [2443:2465] [DMG]                              CommandPathIB =
[1770364789.443] [2443:2465] [DMG]                              {
[1770364789.443] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364789.443] [2443:2465] [DMG]                                      ClusterId = 0x31,
[1770364789.443] [2443:2465] [DMG]                                      CommandId = 0x5,
[1770364789.444] [2443:2465] [DMG]                              },
[1770364789.444] [2443:2465] [DMG]
[1770364789.444] [2443:2465] [DMG]                              CommandFields =
[1770364789.444] [2443:2465] [DMG]                              {
[1770364789.444] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364789.444] [2443:2465] [DMG]                                      0x2 = 0 (unsigned),
[1770364789.445] [2443:2465] [DMG]                              },
[1770364789.445] [2443:2465] [DMG]                      },
[1770364789.445] [2443:2465] [DMG]
[1770364789.445] [2443:2465] [DMG]              },
[1770364789.445] [2443:2465] [DMG]
[1770364789.445] [2443:2465] [DMG]      ],
[1770364789.445] [2443:2465] [DMG]
[1770364789.445] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364789.446] [2443:2465] [DMG] },
[1770364789.446] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1770364789.446] [2443:2465] [CTL] Received NetworkConfig response, networkingStatus=0
[1770364789.446] [2443:2465] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1770364789.446] [2443:2465] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1770364789.446] [2443:2465] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1770364789.446] [2443:2465] [CTL] Arming failsafe (164 seconds)
[1770364789.447] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364789.447] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364789.447] [2443:2465] [EM] <<< [E:51552i S:1492 M:264736078] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770364789.448] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364789.448] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364789.633] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364789.636] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364789.636] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364789.637] [2443:2465] [EM] >>> [E:51552i S:1492 M:78474683] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770364789.637] [2443:2465] [EM] Found matching exchange: 51552i, Delegate: 0xffff8000e0b8
[1770364789.637] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364789.637] [2443:2465] [DMG] InvokeResponseMessage =
[1770364789.637] [2443:2465] [DMG] {
[1770364789.637] [2443:2465] [DMG]      suppressResponse = false,
[1770364789.638] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364789.638] [2443:2465] [DMG]      [
[1770364789.638] [2443:2465] [DMG]              InvokeResponseIB =
[1770364789.638] [2443:2465] [DMG]              {
[1770364789.638] [2443:2465] [DMG]                      CommandDataIB =
[1770364789.638] [2443:2465] [DMG]                      {
[1770364789.638] [2443:2465] [DMG]                              CommandPathIB =
[1770364789.638] [2443:2465] [DMG]                              {
[1770364789.639] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364789.639] [2443:2465] [DMG]                                      ClusterId = 0x30,
[1770364789.639] [2443:2465] [DMG]                                      CommandId = 0x1,
[1770364789.639] [2443:2465] [DMG]                              },
[1770364789.639] [2443:2465] [DMG]
[1770364789.639] [2443:2465] [DMG]                              CommandFields =
[1770364789.639] [2443:2465] [DMG]                              {
[1770364789.640] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364789.640] [2443:2465] [DMG]                                      0x1 = "" (0 chars),
[1770364789.640] [2443:2465] [DMG]                              },
[1770364789.640] [2443:2465] [DMG]                      },
[1770364789.640] [2443:2465] [DMG]
[1770364789.640] [2443:2465] [DMG]              },
[1770364789.640] [2443:2465] [DMG]
[1770364789.641] [2443:2465] [DMG]      ],
[1770364789.641] [2443:2465] [DMG]
[1770364789.641] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364789.641] [2443:2465] [DMG] },
[1770364789.641] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770364789.641] [2443:2465] [CTL] Received ArmFailSafe response errorCode=0
[1770364789.642] [2443:2465] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1770364789.642] [2443:2465] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1770364789.642] [2443:2465] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1770364789.642] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364789.642] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364789.643] [2443:2465] [EM] <<< [E:51553i S:1492 M:264736079] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1770364789.644] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364789.644] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364789.827] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364791.290] [2443:2450] [DL] Indication received, conn = 0xffff88028d20
[1770364791.291] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16391
[1770364791.291] [2443:2465] [EM] >>> [E:51553i S:1492 M:78474684] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1770364791.291] [2443:2465] [EM] Found matching exchange: 51553i, Delegate: 0xffff8000db18
[1770364791.291] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364791.291] [2443:2465] [DMG] InvokeResponseMessage =
[1770364791.291] [2443:2465] [DMG] {
[1770364791.291] [2443:2465] [DMG]      suppressResponse = false,
[1770364791.291] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364791.291] [2443:2465] [DMG]      [
[1770364791.291] [2443:2465] [DMG]              InvokeResponseIB =
[1770364791.292] [2443:2465] [DMG]              {
[1770364791.292] [2443:2465] [DMG]                      CommandDataIB =
[1770364791.292] [2443:2465] [DMG]                      {
[1770364791.292] [2443:2465] [DMG]                              CommandPathIB =
[1770364791.292] [2443:2465] [DMG]                              {
[1770364791.292] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364791.292] [2443:2465] [DMG]                                      ClusterId = 0x31,
[1770364791.292] [2443:2465] [DMG]                                      CommandId = 0x7,
[1770364791.292] [2443:2465] [DMG]                              },
[1770364791.292] [2443:2465] [DMG]
[1770364791.292] [2443:2465] [DMG]                              CommandFields =
[1770364791.292] [2443:2465] [DMG]                              {
[1770364791.292] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364791.292] [2443:2465] [DMG]                                      0x2 = NULL
[1770364791.292] [2443:2465] [DMG]                              },
[1770364791.292] [2443:2465] [DMG]                      },
[1770364791.292] [2443:2465] [DMG]
[1770364791.292] [2443:2465] [DMG]              },
[1770364791.293] [2443:2465] [DMG]
[1770364791.293] [2443:2465] [DMG]      ],
[1770364791.293] [2443:2465] [DMG]
[1770364791.293] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364791.293] [2443:2465] [DMG] },
[1770364791.293] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1770364791.293] [2443:2465] [CTL] Received ConnectNetwork response, networkingStatus=0
[1770364791.293] [2443:2465] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1770364791.293] [2443:2465] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'
[1770364791.293] [2443:2465] [CTL] Performing next commissioning step 'kEvictPreviousCaseSessions'
[1770364791.293] [2443:2465] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1770364791.293] [2443:2465] [CTL] Successfully finished commissioning step 'kEvictPreviousCaseSessions'
[1770364791.293] [2443:2465] [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'
[1770364791.293] [2443:2465] [CTL] Performing next commissioning step 'kFindOperationalForStayActive'
[1770364791.293] [2443:2465] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770364791.293] [2443:2465] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770364791.293] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1770364791.295] [2443:2465] [DIS] Lookup started for 4B6873C4587CC6ED-00000000000008CA
[1770364791.295] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364791.494] [2443:2465] [DIS] Checking node lookup status for 4B6873C4587CC6ED-00000000000008CA after 201 ms
[1770364792.731] [2443:2465] [DIS] SRV record already actively processed.
[1770364792.736] [2443:2465] [DIS] Lookup clearing interface for non LL address
[1770364792.736] [2443:2465] [DIS] UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143%eth0]:5540: new best score: 5 (for 4B6873C4587CC6ED-00000000000008CA)
[1770364792.736] [2443:2465] [DIS] Checking node lookup status for 4B6873C4587CC6ED-00000000000008CA after 1443 ms
[1770364792.737] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540 while in state 2
[1770364792.737] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1770364792.737] [2443:2465] [IN] SecureSession[0xffff8803a4a0]: Allocated Type:2 LSID:1493
[1770364792.737] [2443:2465] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1770364792.741] [2443:2465] [EM] <<< [E:51554i S:0 M:237354427] (U) Msg TX from 02C9A27FCA63A7BE to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1770364792.741] [2443:2465] [EM] ??1 [E:51554i S:0 M:237354427] (U) Msg Retransmission to 0:0000000000000000 scheduled for 8531ms from now [State:Idle II:7000 AI:2500 AT:4000]
[1770364792.742] [2443:2465] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1770364792.742] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1770364793.282] [2443:2465] [EM] >>> [E:51554i S:0 M:204966109 (Ack:237354427)] (U) Msg RX from 0:0000000000000000 [0000] to 02C9A27FCA63A7BE --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770364793.283] [2443:2465] [EM] Found matching exchange: 51554i, Delegate: 0xffff80025058
[1770364793.283] [2443:2465] [EM] Rxd Ack; Removing MessageCounter:237354427 from Retrans Table on exchange 51554i
[1770364793.379] [2443:2465] [EM] >>> [E:51554i S:0 M:204966110 (Ack:237354427)] (U) Msg RX from 0:0000000000000000 [0000] to 02C9A27FCA63A7BE --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[1770364793.379] [2443:2465] [EM] Found matching exchange: 51554i, Delegate: 0xffff80025058
[1770364793.379] [2443:2465] [EM] CHIP MessageCounter:237354427 not in RetransTable on exchange 51554i
[1770364793.379] [2443:2465] [SC] Received Sigma2 msg
[1770364793.379] [2443:2465] [SC] Found MRP parameters in the message
[1770364793.392] [2443:2465] [SC] Peer <00000000000008CA, 1> assigned session ID 54308
[1770364793.393] [2443:2465] [SC] Sending Sigma3
[1770364793.395] [2443:2465] [EM] <<< [E:51554i S:0 M:237354428 (Ack:204966110)] (U) Msg TX from 02C9A27FCA63A7BE to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1770364793.395] [2443:2465] [EM] ??1 [E:51554i S:0 M:237354428] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3006ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770364793.395] [2443:2465] [SC] Sent Sigma3 msg
[1770364793.923] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16389
[1770364794.115] [2443:2465] [EM] >>> [E:51554i S:0 M:204966111 (Ack:237354428)] (U) Msg RX from 0:0000000000000000 [0000] to 02C9A27FCA63A7BE --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770364794.115] [2443:2465] [EM] Found matching exchange: 51554i, Delegate: 0xffff80025058
[1770364794.116] [2443:2465] [EM] Rxd Ack; Removing MessageCounter:237354428 from Retrans Table on exchange 51554i
[1770364794.125] [2443:2465] [EM] >>> [E:51554i S:0 M:204966112 (Ack:237354428)] (U) Msg RX from 0:0000000000000000 [0000] to 02C9A27FCA63A7BE --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1770364794.125] [2443:2465] [EM] Found matching exchange: 51554i, Delegate: 0xffff80025058
[1770364794.125] [2443:2465] [EM] CHIP MessageCounter:237354428 not in RetransTable on exchange 51554i
[1770364794.126] [2443:2465] [SC] Success status report received. Session was established
[1770364794.132] [2443:2465] [SC] SecureSession[0xffff8803a4a0, LSID:1493]: State change 'kEstablishing' --> 'kActive'
[1770364794.132] [2443:2465] [IN] SecureSession[0xffff8803a4a0]: Activated - Type:2 LSID:1493
[1770364794.132] [2443:2465] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:1493 PSID:54308!
[1770364794.132] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1770364794.133] [2443:2465] [CTL] Successfully finished commissioning step 'kFindOperationalForStayActive'
[1770364794.133] [2443:2465] [CTL] Commissioning stage next step: 'kFindOperationalForStayActive' -> 'ICDSendStayActive'
[1770364794.133] [2443:2465] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1770364794.133] [2443:2465] [CTL] Skipping kICDSendStayActive
[1770364794.133] [2443:2465] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1770364794.133] [2443:2465] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'kFindOperationalForCommissioningComplete'
[1770364794.133] [2443:2465] [CTL] Performing next commissioning step 'kFindOperationalForCommissioningComplete'
[1770364794.133] [2443:2465] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770364794.133] [2443:2465] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770364794.133] [2443:2465] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1770364794.133] [2443:2465] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1770364794.133] [2443:2465] [CTL] Successfully finished commissioning step 'kFindOperationalForCommissioningComplete'
[1770364794.133] [2443:2465] [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'
[1770364794.133] [2443:2465] [CTL] Performing next commissioning step 'SendComplete'
[1770364794.134] [2443:2465] [DMG] ICR moving to [AddingComm]
[1770364794.134] [2443:2465] [DMG] ICR moving to [AddedComma]
[1770364794.134] [2443:2465] [EM] <<< [E:51555i S:1493 M:45911556] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [C6ED] [UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1770364794.134] [2443:2465] [EM] ??1 [E:51555i S:1493 M:45911556] (S) Msg Retransmission to 1:00000000000008CA scheduled for 8937ms from now [State:Idle II:7000 AI:2500 AT:0]
[1770364794.134] [2443:2465] [DMG] ICR moving to [AwaitingRe]
[1770364794.135] [2443:2465] [EM] <<< [E:51554i S:0 M:237354429 (Ack:204966112)] (U) Msg TX from 02C9A27FCA63A7BE to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770364794.135] [2443:2465] [EM] Flushed pending ack for MessageCounter:204966112 on exchange 51554i
[1770364794.135] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 32792
[1770364794.686] [2443:2465] [EM] >>> [E:51555i S:1493 M:5928595 (Ack:45911556)] (S) Msg RX from 1:00000000000008CA [C6ED] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1770364794.686] [2443:2465] [EM] Found matching exchange: 51555i, Delegate: 0xffff8000e0b8
[1770364794.686] [2443:2465] [EM] Rxd Ack; Removing MessageCounter:45911556 from Retrans Table on exchange 51555i
[1770364794.686] [2443:2465] [DMG] ICR moving to [ResponseRe]
[1770364794.686] [2443:2465] [DMG] InvokeResponseMessage =
[1770364794.687] [2443:2465] [DMG] {
[1770364794.687] [2443:2465] [DMG]      suppressResponse = false,
[1770364794.688] [2443:2465] [DMG]      InvokeResponseIBs =
[1770364794.688] [2443:2465] [DMG]      [
[1770364794.689] [2443:2465] [DMG]              InvokeResponseIB =
[1770364794.689] [2443:2465] [DMG]              {
[1770364794.689] [2443:2465] [DMG]                      CommandDataIB =
[1770364794.689] [2443:2465] [DMG]                      {
[1770364794.689] [2443:2465] [DMG]                              CommandPathIB =
[1770364794.689] [2443:2465] [DMG]                              {
[1770364794.689] [2443:2465] [DMG]                                      EndpointId = 0x0,
[1770364794.689] [2443:2465] [DMG]                                      ClusterId = 0x30,
[1770364794.689] [2443:2465] [DMG]                                      CommandId = 0x5,
[1770364794.690] [2443:2465] [DMG]                              },
[1770364794.690] [2443:2465] [DMG]
[1770364794.690] [2443:2465] [DMG]                              CommandFields =
[1770364794.690] [2443:2465] [DMG]                              {
[1770364794.690] [2443:2465] [DMG]                                      0x0 = 0 (unsigned),
[1770364794.691] [2443:2465] [DMG]                                      0x1 = "" (0 chars),
[1770364794.691] [2443:2465] [DMG]                              },
[1770364794.691] [2443:2465] [DMG]                      },
[1770364794.691] [2443:2465] [DMG]
[1770364794.691] [2443:2465] [DMG]              },
[1770364794.691] [2443:2465] [DMG]
[1770364794.691] [2443:2465] [DMG]      ],
[1770364794.691] [2443:2465] [DMG]
[1770364794.691] [2443:2465] [DMG]      InteractionModelRevision = 12
[1770364794.692] [2443:2465] [DMG] },
[1770364794.692] [2443:2465] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1770364794.692] [2443:2465] [CTL] Received CommissioningComplete response, errorCode=0
[1770364794.692] [2443:2465] [CTL] Successfully finished commissioning step 'SendComplete'
[1770364794.692] [2443:2465] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1770364794.692] [2443:2465] [CTL] Performing next commissioning step 'Cleanup'
[1770364794.692] [2443:2465] [CTL] Successfully finished commissioning step 'Cleanup'
[1770364794.692] [2443:2465] [DIS] Closing all BLE connections
[1770364794.692] [2443:2465] [IN] Clearing BLE pending packets.
[1770364794.693] [2443:2465] [BLE] Auto-closing end point's BLE connection.
[1770364794.693] [2443:2465] [DL] Closing BLE GATT connection (con 0xffff88028d20)
[1770364794.693] [2443:2450] [DL] Close BLE connection: peer=CC:C0:BF:C1:8D:CE
[1770364794.703] [2443:2465] [IN] SecureSession[0xffff80022d50]: MarkForEviction Type:1 LSID:1492
[1770364794.703] [2443:2465] [SC] SecureSession[0xffff80022d50, LSID:1492]: State change 'kActive' --> 'kPendingEviction'
[1770364794.703] [2443:2465] [IN] SecureSession[0xffff80022d50]: Released - Type:1 LSID:1492
[1770364794.703] [2443:2465] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1770364794.703] [2443:2465] [TOO] Device commissioning completed with success
[1770364794.704] [2443:2465] [DMG] ICR moving to [AwaitingDe]
[1770364794.704] [2443:2450] [DL] BLE connection closed: conn=0xffff88028d20
[1770364794.704] [2443:2465] [EM] <<< [E:51555i S:1493 M:45911557 (Ack:5928595)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [C6ED] [UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1770364794.704] [2443:2465] [EM] Flushed pending ack for MessageCounter:5928595 on exchange 51555i
[1770364794.704] [2443:2465] [DL] HandlePlatformSpecificBLEEvent 16390
[1770364794.704] [2443:2465] [BLE] No endpoint for unsubscribe complete
[1770364794.704] [2443:2465] [BLE] No endpoint for connection error
[1770364794.705] [2443:2443] [CTL] Shutting down the commissioner
[1770364794.705] [2443:2443] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770364794.705] [2443:2443] [CTL] Shutting down the controller
[1770364794.705] [2443:2443] [IN] Expiring all sessions for fabric 0x1!!
[1770364794.706] [2443:2443] [IN] SecureSession[0xffff8803a4a0]: MarkForEviction Type:2 LSID:1493
[1770364794.706] [2443:2443] [SC] SecureSession[0xffff8803a4a0, LSID:1493]: State change 'kActive' --> 'kPendingEviction'
[1770364794.706] [2443:2443] [IN] SecureSession[0xffff8803a4a0]: Released - Type:2 LSID:1493
[1770364794.706] [2443:2443] [FP] Forgetting fabric 0x1
[1770364794.706] [2443:2443] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770364794.706] [2443:2443] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770364794.706] [2443:2443] [TS] Reverted Last Known Good Time to previous value
[1770364794.706] [2443:2443] [CTL] Shutting down the commissioner
[1770364794.707] [2443:2443] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770364794.707] [2443:2443] [CTL] Shutting down the controller
[1770364794.707] [2443:2443] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770364794.707] [2443:2443] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770364794.707] [2443:2443] [FP] Shutting down FabricTable
[1770364794.707] [2443:2443] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770364794.708] [2443:2443] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770364794.708] [2443:2443] [TS] Reverted Last Known Good Time to previous value
[1770364794.721] [2443:2443] [DL] Wrote settings to /tmp/chip_counters.ini
[1770364794.721] [2443:2443] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770364794.721] [2443:2443] [DL] Inet Layer shutdown
[1770364794.721] [2443:2443] [DL] BLE Layer shutdown
[1770364794.726] [2443:2443] [DL] WiFi-PAF Layer shutdown
[1770364794.726] [2443:2443] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770364794.726] [2443:2443] [DL] NFCCommissioningMgr shutdown
[1770364794.727] [2443:2443] [DL] System Layer shutdown

```