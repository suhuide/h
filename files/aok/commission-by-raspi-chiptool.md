```c
ubuntu@ubuntu:~$ sudo rm -rf /tmp/chip_*
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840
[1770453039.955] [38622:38622] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770453040.157] [38622:38622] [DL] Wrote settings to /tmp/chip_tool_kvs
[1770453040.160] [38622:38622] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770453040.178] [38622:38622] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770453040.185] [38622:38622] [DL] Wrote settings to /tmp/chip_factory.ini
[1770453040.186] [38622:38622] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770453040.194] [38622:38622] [DL] Wrote settings to /tmp/chip_config.ini
[1770453040.194] [38622:38622] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770453040.203] [38622:38622] [DL] Wrote settings to /tmp/chip_counters.ini
[1770453040.220] [38622:38622] [DL] Wrote settings to /tmp/chip_config.ini
[1770453040.220] [38622:38622] [DL] NVS set: chip-config/unique-id = "84FD73751187AB20"
[1770453040.229] [38622:38622] [DL] Wrote settings to /tmp/chip_factory.ini
[1770453040.229] [38622:38622] [DL] NVS set: chip-factory/vendor-id = 65521 (0xFFF1)
[1770453040.239] [38622:38622] [DL] Wrote settings to /tmp/chip_factory.ini
[1770453040.239] [38622:38622] [DL] NVS set: chip-factory/product-id = 32769 (0x8001)
[1770453040.248] [38622:38622] [DL] Wrote settings to /tmp/chip_counters.ini
[1770453040.248] [38622:38622] [DL] NVS set: chip-counters/reboot-count = 1 (0x1)
[1770453040.259] [38622:38622] [DL] Wrote settings to /tmp/chip_counters.ini
[1770453040.259] [38622:38622] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770453040.268] [38622:38622] [DL] Wrote settings to /tmp/chip_counters.ini
[1770453040.268] [38622:38622] [DL] NVS set: chip-counters/boot-reason = 0 (0x0)
[1770453040.280] [38622:38622] [DL] Wrote settings to /tmp/chip_config.ini
[1770453040.281] [38622:38622] [DL] NVS set: chip-config/regulatory-location = 0 (0x0)
[1770453040.290] [38622:38622] [DL] Wrote settings to /tmp/chip_config.ini
[1770453040.290] [38622:38622] [DL] NVS set: chip-config/location-capability = 2 (0x2)
[1770453040.303] [38622:38622] [DL] Wrote settings to /tmp/chip_config.ini
[1770453040.303] [38622:38622] [DL] NVS set: chip-config/configuration-version = 1 (0x1)
[1770453040.305] [38622:38622] [DL] Got Ethernet interface: eth0
[1770453040.306] [38622:38622] [DL] Found the primary Ethernet interface:eth0
[1770453040.308] [38622:38622] [DL] Got WiFi interface: wlan0
[1770453040.308] [38622:38622] [DL] Failed to reset WiFi statistic counts
[1770453040.309] [38622:38622] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770453040.470] [38622:38622] [IN] UDP::Init bind&listen port=0
[1770453040.470] [38622:38622] [IN] UDP::Init bound to port=50065
[1770453040.471] [38622:38622] [IN] BLEBase::Init - setting/overriding transport
[1770453040.471] [38622:38622] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770453040.471] [38622:38622] [CTL] NFCBase::Init
[1770453040.471] [38622:38622] [IN] TransportMgr initialized
[1770453040.471] [38622:38622] [FP] Initializing FabricTable from persistent storage
[1770453040.471] [38622:38622] [TS] Last Known Good Time: [unknown]
[1770453040.471] [38622:38622] [TS] Setting Last Known Good Time to firmware build time 2023-10-14T01:16:48
[1770453040.477] [38622:38622] [DMG] Ember attribute persistence requires setting up
[1770453040.477] [38622:38622] [ZCL] Using ZAP configuration...
[1770453040.483] [38622:38622] [CTL] System State Initialized...
[1770453040.484] [38622:38622] [CTL] Setting attestation nonce to random value
[1770453040.484] [38622:38622] [CTL] Setting CSR nonce to random value
[1770453040.484] [38622:38622] [IN] UDP::Init bind&listen port=5550
[1770453040.484] [38622:38622] [IN] UDP::Init bound to port=5550
[1770453040.484] [38622:38622] [IN] TransportMgr initialized
[1770453040.488] [38622:38638] [DL] CHIP task running
[1770453040.488] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 32786
[1770453040.489] [38622:38638] [CTL] Setting attestation nonce to random value
[1770453040.490] [38622:38638] [CTL] Setting CSR nonce to random value
[1770453040.490] [38622:38638] [CTL] Couldn't get ExampleOpCredsCAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770453040.493] [38622:38638] [CTL] Couldn't get ExampleOpCredsICAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770453040.496] [38622:38638] [CTL] Generating RCAC
[1770453040.499] [38622:38638] [CTL] Generating ICAC
[1770453040.502] [38622:38638] [CTL] Generating NOC
[1770453040.504] [38622:38638] [FP] Validating NOC chain
[1770453040.509] [38622:38638] [FP] NOC chain validation successful
[1770453040.509] [38622:38638] [FP] Added new fabric at index: 0x1
[1770453040.509] [38622:38638] [FP] Assigned compressed fabric ID: 0x9BB8A0DFD2A8507B, node ID: 0x000000000001B669
[1770453040.509] [38622:38638] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770453040.509] [38622:38638] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770453040.509] [38622:38638] [TS] Retaining current Last Known Good Time
[1770453040.512] [38622:38638] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770453040.516] [38622:38638] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770453040.521] [38622:38638] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 9BB8A0DFD2A8507B)
[1770453040.521] [38622:38638] [IN] UDP::Init bind&listen port=5551
[1770453040.521] [38622:38638] [IN] UDP::Init bound to port=5551
[1770453040.521] [38622:38638] [IN] TransportMgr initialized
[1770453040.590] [38622:38638] [CTL] Setting thread operational dataset from parameters
[1770453040.590] [38622:38638] [CTL] Setting attestation nonce to random value
[1770453040.590] [38622:38638] [CTL] Setting CSR nonce to random value
[1770453040.590] [38622:38638] [CTL] Commission called for node ID 0x00000000000008CA
[1770453040.590] [38622:38638] [DL] Long dispatch time: 103 ms, for event type 2
[1770453040.624] [38622:38629] [BLE] BLE removing known devices
[1770453040.628] [38622:38629] [BLE] BLE initiating scan
[1770453040.635] [38622:38638] [BLE] ChipDeviceScanner has started scanning!
[1770453040.673] [38622:38629] [BLE] New device scanned: EF:47:1A:8D:E4:BC
[1770453040.673] [38622:38629] [BLE] Device discriminator match. Attempting to connect.
[1770453040.680] [38622:38629] [BLE] ChipDeviceScanner has stopped scanning!
[1770453041.008] [38622:38629] [DL] FAIL: ConnectDevice: GDBus.Error:org.bluez.Error.Failed: le-connection-abort-by-local (36)
[1770453041.008] [38622:38629] [DL] ConnectDevice retry: 1 out of 4
[1770453041.228] [38622:38629] [DL] ConnectDevice complete
[1770453041.228] [38622:38629] [BLE] New device connected: EF:47:1A:8D:E4:BC
[1770453044.929] [38622:38629] [DL] CHIP service found
[1770453044.930] [38622:38629] [DL] Valid C1 characteristic found
[1770453044.930] [38622:38629] [DL] Valid C2 characteristic found
[1770453044.930] [38622:38629] [DL] New BLE connection: conn=0xffffac023710 device=EF:47:1A:8D:E4:BC path=/org/bluez/hci0/dev_EF_47_1A_8D_E4_BC
[1770453044.930] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16387
[1770453044.930] [38622:38638] [DIS] Closing all BLE connections
[1770453044.930] [38622:38638] [IN] BleConnectionComplete: endPoint 0xaaaab59d6fd0
[1770453044.932] [38622:38638] [IN] SecureSession[0xffffa4022cb0]: Allocated Type:1 LSID:42557
[1770453044.932] [38622:38638] [SC] Assigned local session key ID 42557
[1770453044.932] [38622:38638] [EM] <<< [E:28666i S:0 M:35572782] (U) Msg TX from 40C7052742D2DE78 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770453044.932] [38622:38638] [IN] Message appended to BLE send queue
[1770453044.932] [38622:38638] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770453046.331] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453046.917] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16390
[1770453046.917] [38622:38638] [BLE] subscribe complete, ep = 0xaaaab59d6fd0
[1770453046.918] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453046.918] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453046.918] [38622:38638] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770453046.918] [38622:38638] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770453046.918] [38622:38638] [BLE] local and remote recv window size = 5
[1770453046.920] [38622:38638] [IN] BLE EndPoint 0xaaaab59d6fd0 Connection Complete
[1770453047.305] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453047.404] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453047.405] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453047.405] [38622:38638] [EM] >>> [E:28666i S:0 M:137509410] (U) Msg RX from 0:0000000000000000 [0000] to 40C7052742D2DE78 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[1770453047.405] [38622:38638] [EM] Found matching exchange: 28666i, Delegate: 0xffffa4021818
[1770453047.406] [38622:38638] [SC] Received PBKDF param response
[1770453047.406] [38622:38638] [SC] Peer assigned session ID 8047
[1770453047.406] [38622:38638] [SC] Found MRP parameters in the message
[1770453047.428] [38622:38638] [EM] <<< [E:28666i S:0 M:35572783] (U) Msg TX from 40C7052742D2DE78 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770453047.428] [38622:38638] [SC] Sent spake2p msg1
[1770453047.598] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453047.696] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453047.697] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453047.697] [38622:38638] [EM] >>> [E:28666i S:0 M:137509411] (U) Msg RX from 0:0000000000000000 [0000] to 40C7052742D2DE78 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770453047.697] [38622:38638] [EM] Found matching exchange: 28666i, Delegate: 0xffffa4021818
[1770453047.697] [38622:38638] [SC] Received spake2p msg2
[1770453047.703] [38622:38638] [EM] <<< [E:28666i S:0 M:35572784] (U) Msg TX from 40C7052742D2DE78 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770453047.704] [38622:38638] [SC] Sent spake2p msg3
[1770453047.890] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453047.892] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453047.893] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453047.893] [38622:38638] [EM] >>> [E:28666i S:0 M:137509412] (U) Msg RX from 0:0000000000000000 [0000] to 40C7052742D2DE78 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770453047.893] [38622:38638] [EM] Found matching exchange: 28666i, Delegate: 0xffffa4021818
[1770453047.894] [38622:38638] [SC] SecureSession[0xffffa4022cb0, LSID:42557]: State change 'kEstablishing' --> 'kActive'
[1770453047.894] [38622:38638] [IN] SecureSession[0xffffa4022cb0]: Activated - Type:1 LSID:42557
[1770453047.894] [38622:38638] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:42557 PSID:8047!
[1770453047.894] [38622:38638] [CTL] Remote device completed SPAKE2+ handshake
[1770453047.894] [38622:38638] [TOO] Pairing Success
[1770453047.894] [38622:38638] [TOO] PASE establishment successful
[1770453047.895] [38622:38638] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770453047.895] [38622:38638] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770453047.895] [38622:38638] [CTL] Sending read requests for commissioning information
[1770453047.895] [38622:38638] [DMG] SendReadRequest ReadClient[0xffffa4023720]: Sending Read Request
[1770453047.895] [38622:38638] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770453047.896] [38622:38638] [EM] <<< [E:28667i S:42557 M:216523822] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770453047.897] [38622:38638] [DMG] MoveToState ReadClient[0xffffa4023720]: Moving to [AwaitingIn]
[1770453047.897] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 32792
[1770453048.183] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453048.283] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453048.284] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453048.477] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453048.478] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453048.478] [38622:38638] [EM] >>> [E:28667i S:42557 M:9561277] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:257)
[1770453048.478] [38622:38638] [EM] Found matching exchange: 28667i, Delegate: 0xffffa4023730
[1770453048.478] [38622:38638] [DMG] ReportDataMessage =
[1770453048.479] [38622:38638] [DMG] {
[1770453048.479] [38622:38638] [DMG]    AttributeReportIBs =
[1770453048.479] [38622:38638] [DMG]    [
[1770453048.479] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.479] [38622:38638] [DMG]            {
[1770453048.479] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.479] [38622:38638] [DMG]                    {
[1770453048.479] [38622:38638] [DMG]                            DataVersion = 0xdb6e9b6a,
[1770453048.480] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.480] [38622:38638] [DMG]                            {
[1770453048.480] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.480] [38622:38638] [DMG]                                    Cluster = 0x31,
[1770453048.480] [38622:38638] [DMG]                                    Attribute = 0x0000_FFFC,
[1770453048.480] [38622:38638] [DMG]                            }
[1770453048.480] [38622:38638] [DMG]
[1770453048.481] [38622:38638] [DMG]                            Data = 2 (unsigned),
[1770453048.481] [38622:38638] [DMG]                    },
[1770453048.481] [38622:38638] [DMG]
[1770453048.481] [38622:38638] [DMG]            },
[1770453048.481] [38622:38638] [DMG]
[1770453048.481] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.481] [38622:38638] [DMG]            {
[1770453048.482] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.482] [38622:38638] [DMG]                    {
[1770453048.482] [38622:38638] [DMG]                            DataVersion = 0xd4d493f0,
[1770453048.482] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.482] [38622:38638] [DMG]                            {
[1770453048.482] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.482] [38622:38638] [DMG]                                    Cluster = 0x28,
[1770453048.482] [38622:38638] [DMG]                                    Attribute = 0x0000_0004,
[1770453048.483] [38622:38638] [DMG]                            }
[1770453048.483] [38622:38638] [DMG]
[1770453048.483] [38622:38638] [DMG]                            Data = 32784 (unsigned),
[1770453048.483] [38622:38638] [DMG]                    },
[1770453048.483] [38622:38638] [DMG]
[1770453048.483] [38622:38638] [DMG]            },
[1770453048.483] [38622:38638] [DMG]
[1770453048.484] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.484] [38622:38638] [DMG]            {
[1770453048.484] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.484] [38622:38638] [DMG]                    {
[1770453048.484] [38622:38638] [DMG]                            DataVersion = 0xd4d493f0,
[1770453048.484] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.484] [38622:38638] [DMG]                            {
[1770453048.485] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.485] [38622:38638] [DMG]                                    Cluster = 0x28,
[1770453048.485] [38622:38638] [DMG]                                    Attribute = 0x0000_0002,
[1770453048.485] [38622:38638] [DMG]                            }
[1770453048.485] [38622:38638] [DMG]
[1770453048.485] [38622:38638] [DMG]                            Data = 65521 (unsigned),
[1770453048.485] [38622:38638] [DMG]                    },
[1770453048.485] [38622:38638] [DMG]
[1770453048.485] [38622:38638] [DMG]            },
[1770453048.485] [38622:38638] [DMG]
[1770453048.486] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.486] [38622:38638] [DMG]            {
[1770453048.486] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.486] [38622:38638] [DMG]                    {
[1770453048.486] [38622:38638] [DMG]                            DataVersion = 0x19afbbff,
[1770453048.486] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.486] [38622:38638] [DMG]                            {
[1770453048.486] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.486] [38622:38638] [DMG]                                    Cluster = 0x30,
[1770453048.486] [38622:38638] [DMG]                                    Attribute = 0x0000_0003,
[1770453048.486] [38622:38638] [DMG]                            }
[1770453048.486] [38622:38638] [DMG]
[1770453048.486] [38622:38638] [DMG]                            Data = 0 (unsigned),
[1770453048.486] [38622:38638] [DMG]                    },
[1770453048.486] [38622:38638] [DMG]
[1770453048.487] [38622:38638] [DMG]            },
[1770453048.487] [38622:38638] [DMG]
[1770453048.487] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.487] [38622:38638] [DMG]            {
[1770453048.487] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.487] [38622:38638] [DMG]                    {
[1770453048.487] [38622:38638] [DMG]                            DataVersion = 0x19afbbff,
[1770453048.487] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.487] [38622:38638] [DMG]                            {
[1770453048.487] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.487] [38622:38638] [DMG]                                    Cluster = 0x30,
[1770453048.487] [38622:38638] [DMG]                                    Attribute = 0x0000_0002,
[1770453048.487] [38622:38638] [DMG]                            }
[1770453048.487] [38622:38638] [DMG]
[1770453048.487] [38622:38638] [DMG]                            Data = 0 (unsigned),
[1770453048.488] [38622:38638] [DMG]                    },
[1770453048.488] [38622:38638] [DMG]
[1770453048.488] [38622:38638] [DMG]            },
[1770453048.488] [38622:38638] [DMG]
[1770453048.488] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.488] [38622:38638] [DMG]            {
[1770453048.488] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.488] [38622:38638] [DMG]                    {
[1770453048.488] [38622:38638] [DMG]                            DataVersion = 0x19afbbff,
[1770453048.488] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.488] [38622:38638] [DMG]                            {
[1770453048.488] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.488] [38622:38638] [DMG]                                    Cluster = 0x30,
[1770453048.488] [38622:38638] [DMG]                                    Attribute = 0x0000_0001,
[1770453048.489] [38622:38638] [DMG]                            }
[1770453048.489] [38622:38638] [DMG]
[1770453048.489] [38622:38638] [DMG]                            Data =
[1770453048.489] [38622:38638] [DMG]                            {
[1770453048.489] [38622:38638] [DMG]                                    0x0 = 60 (unsigned),
[1770453048.489] [38622:38638] [DMG]                                    0x1 = 900 (unsigned),
[1770453048.489] [38622:38638] [DMG]                            },
[1770453048.489] [38622:38638] [DMG]                    },
[1770453048.489] [38622:38638] [DMG]
[1770453048.489] [38622:38638] [DMG]            },
[1770453048.489] [38622:38638] [DMG]
[1770453048.489] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.489] [38622:38638] [DMG]            {
[1770453048.489] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.490] [38622:38638] [DMG]                    {
[1770453048.490] [38622:38638] [DMG]                            DataVersion = 0x19afbbff,
[1770453048.490] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.490] [38622:38638] [DMG]                            {
[1770453048.490] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.490] [38622:38638] [DMG]                                    Cluster = 0x30,
[1770453048.490] [38622:38638] [DMG]                                    Attribute = 0x0000_0000,
[1770453048.490] [38622:38638] [DMG]                            }
[1770453048.490] [38622:38638] [DMG]
[1770453048.490] [38622:38638] [DMG]                            Data = 0 (unsigned),
[1770453048.490] [38622:38638] [DMG]                    },
[1770453048.490] [38622:38638] [DMG]
[1770453048.490] [38622:38638] [DMG]            },
[1770453048.490] [38622:38638] [DMG]
[1770453048.491] [38622:38638] [DMG]            AttributeReportIB =
[1770453048.491] [38622:38638] [DMG]            {
[1770453048.491] [38622:38638] [DMG]                    AttributeDataIB =
[1770453048.491] [38622:38638] [DMG]                    {
[1770453048.491] [38622:38638] [DMG]                            DataVersion = 0x19afbbff,
[1770453048.491] [38622:38638] [DMG]                            AttributePathIB =
[1770453048.491] [38622:38638] [DMG]                            {
[1770453048.491] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453048.491] [38622:38638] [DMG]                                    Cluster = 0x30,
[1770453048.491] [38622:38638] [DMG]                                    Attribute = 0x0000_0004,
[1770453048.491] [38622:38638] [DMG]                            }
[1770453048.491] [38622:38638] [DMG]
[1770453048.491] [38622:38638] [DMG]                            Data = true,
[1770453048.491] [38622:38638] [DMG]                    },
[1770453048.492] [38622:38638] [DMG]
[1770453048.492] [38622:38638] [DMG]            },
[1770453048.492] [38622:38638] [DMG]
[1770453048.492] [38622:38638] [DMG]    ],
[1770453048.492] [38622:38638] [DMG]
[1770453048.492] [38622:38638] [DMG]    SuppressResponse = true,
[1770453048.492] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453048.492] [38622:38638] [DMG] }
[1770453048.494] [38622:38638] [DMG] SendReadRequest ReadClient[0xffffa4023720]: Sending Read Request
[1770453048.494] [38622:38638] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770453048.494] [38622:38638] [EM] <<< [E:28668i S:42557 M:216523823] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770453048.495] [38622:38638] [DMG] MoveToState ReadClient[0xffffa4023720]: Moving to [AwaitingIn]
[1770453048.865] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453049.062] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453049.062] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453049.063] [38622:38638] [EM] >>> [E:28668i S:42557 M:9561278] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:191)
[1770453049.063] [38622:38638] [EM] Found matching exchange: 28668i, Delegate: 0xffffa4023730
[1770453049.063] [38622:38638] [DMG] ReportDataMessage =
[1770453049.063] [38622:38638] [DMG] {
[1770453049.063] [38622:38638] [DMG]    AttributeReportIBs =
[1770453049.063] [38622:38638] [DMG]    [
[1770453049.063] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.064] [38622:38638] [DMG]            {
[1770453049.064] [38622:38638] [DMG]                    AttributeDataIB =
[1770453049.064] [38622:38638] [DMG]                    {
[1770453049.064] [38622:38638] [DMG]                            DataVersion = 0x94abd6c2,
[1770453049.064] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.064] [38622:38638] [DMG]                            {
[1770453049.064] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.064] [38622:38638] [DMG]                                    Cluster = 0x46,
[1770453049.064] [38622:38638] [DMG]                                    Attribute = 0x0000_0002,
[1770453049.064] [38622:38638] [DMG]                            }
[1770453049.064] [38622:38638] [DMG]
[1770453049.064] [38622:38638] [DMG]                            Data = 0 (unsigned),
[1770453049.065] [38622:38638] [DMG]                    },
[1770453049.065] [38622:38638] [DMG]
[1770453049.065] [38622:38638] [DMG]            },
[1770453049.065] [38622:38638] [DMG]
[1770453049.065] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.065] [38622:38638] [DMG]            {
[1770453049.065] [38622:38638] [DMG]                    AttributeDataIB =
[1770453049.065] [38622:38638] [DMG]                    {
[1770453049.065] [38622:38638] [DMG]                            DataVersion = 0x94abd6c2,
[1770453049.065] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.065] [38622:38638] [DMG]                            {
[1770453049.066] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.066] [38622:38638] [DMG]                                    Cluster = 0x46,
[1770453049.066] [38622:38638] [DMG]                                    Attribute = 0x0000_0001,
[1770453049.066] [38622:38638] [DMG]                            }
[1770453049.066] [38622:38638] [DMG]
[1770453049.066] [38622:38638] [DMG]                            Data = 0 (unsigned),
[1770453049.066] [38622:38638] [DMG]                    },
[1770453049.066] [38622:38638] [DMG]
[1770453049.066] [38622:38638] [DMG]            },
[1770453049.066] [38622:38638] [DMG]
[1770453049.066] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.066] [38622:38638] [DMG]            {
[1770453049.066] [38622:38638] [DMG]                    AttributeDataIB =
[1770453049.067] [38622:38638] [DMG]                    {
[1770453049.067] [38622:38638] [DMG]                            DataVersion = 0x94abd6c2,
[1770453049.067] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.067] [38622:38638] [DMG]                            {
[1770453049.067] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.067] [38622:38638] [DMG]                                    Cluster = 0x46,
[1770453049.067] [38622:38638] [DMG]                                    Attribute = 0x0000_0000,
[1770453049.067] [38622:38638] [DMG]                            }
[1770453049.067] [38622:38638] [DMG]
[1770453049.067] [38622:38638] [DMG]                            Data = 600 (unsigned),
[1770453049.067] [38622:38638] [DMG]                    },
[1770453049.068] [38622:38638] [DMG]
[1770453049.068] [38622:38638] [DMG]            },
[1770453049.068] [38622:38638] [DMG]
[1770453049.068] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.068] [38622:38638] [DMG]            {
[1770453049.068] [38622:38638] [DMG]                    AttributeStatusIB =
[1770453049.068] [38622:38638] [DMG]                    {
[1770453049.068] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.068] [38622:38638] [DMG]                            {
[1770453049.068] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.068] [38622:38638] [DMG]                                    Cluster = 0x46,
[1770453049.068] [38622:38638] [DMG]                                    Attribute = 0x0000_0007,
[1770453049.068] [38622:38638] [DMG]                            }
[1770453049.069] [38622:38638] [DMG]
[1770453049.069] [38622:38638] [DMG]                            StatusIB =
[1770453049.069] [38622:38638] [DMG]                            {
[1770453049.069] [38622:38638] [DMG]                                    status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770453049.069] [38622:38638] [DMG]                            },
[1770453049.069] [38622:38638] [DMG]
[1770453049.069] [38622:38638] [DMG]                    },
[1770453049.069] [38622:38638] [DMG]
[1770453049.069] [38622:38638] [DMG]            },
[1770453049.069] [38622:38638] [DMG]
[1770453049.069] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.069] [38622:38638] [DMG]            {
[1770453049.069] [38622:38638] [DMG]                    AttributeStatusIB =
[1770453049.070] [38622:38638] [DMG]                    {
[1770453049.070] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.070] [38622:38638] [DMG]                            {
[1770453049.070] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.070] [38622:38638] [DMG]                                    Cluster = 0x46,
[1770453049.070] [38622:38638] [DMG]                                    Attribute = 0x0000_0006,
[1770453049.070] [38622:38638] [DMG]                            }
[1770453049.070] [38622:38638] [DMG]
[1770453049.070] [38622:38638] [DMG]                            StatusIB =
[1770453049.070] [38622:38638] [DMG]                            {
[1770453049.070] [38622:38638] [DMG]                                    status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770453049.070] [38622:38638] [DMG]                            },
[1770453049.070] [38622:38638] [DMG]
[1770453049.070] [38622:38638] [DMG]                    },
[1770453049.071] [38622:38638] [DMG]
[1770453049.071] [38622:38638] [DMG]            },
[1770453049.071] [38622:38638] [DMG]
[1770453049.071] [38622:38638] [DMG]            AttributeReportIB =
[1770453049.071] [38622:38638] [DMG]            {
[1770453049.071] [38622:38638] [DMG]                    AttributeDataIB =
[1770453049.071] [38622:38638] [DMG]                    {
[1770453049.071] [38622:38638] [DMG]                            DataVersion = 0xdb6e9b6a,
[1770453049.071] [38622:38638] [DMG]                            AttributePathIB =
[1770453049.071] [38622:38638] [DMG]                            {
[1770453049.071] [38622:38638] [DMG]                                    Endpoint = 0x0,
[1770453049.071] [38622:38638] [DMG]                                    Cluster = 0x31,
[1770453049.071] [38622:38638] [DMG]                                    Attribute = 0x0000_0003,
[1770453049.072] [38622:38638] [DMG]                            }
[1770453049.072] [38622:38638] [DMG]
[1770453049.072] [38622:38638] [DMG]                            Data = 20 (unsigned),
[1770453049.072] [38622:38638] [DMG]                    },
[1770453049.072] [38622:38638] [DMG]
[1770453049.072] [38622:38638] [DMG]            },
[1770453049.072] [38622:38638] [DMG]
[1770453049.072] [38622:38638] [DMG]    ],
[1770453049.072] [38622:38638] [DMG]
[1770453049.072] [38622:38638] [DMG]    SuppressResponse = true,
[1770453049.072] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453049.072] [38622:38638] [DMG] }
[1770453049.074] [38622:38638] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1770453049.074] [38622:38638] [SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010
[1770453049.074] [38622:38638] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1770453049.074] [38622:38638] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1770453049.074] [38622:38638] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1770453049.074] [38622:38638] [CTL] Performing next commissioning step 'ArmFailSafe'
[1770453049.074] [38622:38638] [CTL] Arming failsafe (60 seconds)
[1770453049.074] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453049.075] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453049.075] [38622:38638] [EM] <<< [E:28669i S:42557 M:216523824] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770453049.076] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453049.256] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453049.259] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453049.260] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453049.260] [38622:38638] [EM] >>> [E:28669i S:42557 M:9561279] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770453049.260] [38622:38638] [EM] Found matching exchange: 28669i, Delegate: 0xffffa400db18
[1770453049.261] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453049.261] [38622:38638] [DMG] InvokeResponseMessage =
[1770453049.261] [38622:38638] [DMG] {
[1770453049.261] [38622:38638] [DMG]    suppressResponse = false,
[1770453049.261] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453049.261] [38622:38638] [DMG]    [
[1770453049.261] [38622:38638] [DMG]            InvokeResponseIB =
[1770453049.261] [38622:38638] [DMG]            {
[1770453049.262] [38622:38638] [DMG]                    CommandDataIB =
[1770453049.262] [38622:38638] [DMG]                    {
[1770453049.262] [38622:38638] [DMG]                            CommandPathIB =
[1770453049.262] [38622:38638] [DMG]                            {
[1770453049.263] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453049.263] [38622:38638] [DMG]                                    ClusterId = 0x30,
[1770453049.263] [38622:38638] [DMG]                                    CommandId = 0x1,
[1770453049.263] [38622:38638] [DMG]                            },
[1770453049.263] [38622:38638] [DMG]
[1770453049.263] [38622:38638] [DMG]                            CommandFields =
[1770453049.263] [38622:38638] [DMG]                            {
[1770453049.263] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453049.264] [38622:38638] [DMG]                                    0x1 = "" (0 chars),
[1770453049.264] [38622:38638] [DMG]                            },
[1770453049.264] [38622:38638] [DMG]                    },
[1770453049.264] [38622:38638] [DMG]
[1770453049.264] [38622:38638] [DMG]            },
[1770453049.264] [38622:38638] [DMG]
[1770453049.264] [38622:38638] [DMG]    ],
[1770453049.264] [38622:38638] [DMG]
[1770453049.264] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453049.264] [38622:38638] [DMG] },
[1770453049.264] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770453049.264] [38622:38638] [CTL] Received ArmFailSafe response errorCode=0
[1770453049.264] [38622:38638] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1770453049.265] [38622:38638] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1770453049.265] [38622:38638] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1770453049.265] [38622:38638] [CTL] Setting Regulatory Config
[1770453049.265] [38622:38638] [CTL] Device does not support configurable regulatory location
[1770453049.265] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453049.265] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453049.265] [38622:38638] [EM] <<< [E:28670i S:42557 M:216523825] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1770453049.266] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453049.266] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453049.450] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453049.453] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453049.453] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453049.454] [38622:38638] [EM] >>> [E:28670i S:42557 M:9561280] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770453049.454] [38622:38638] [EM] Found matching exchange: 28670i, Delegate: 0xffffa400e0b8
[1770453049.454] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453049.454] [38622:38638] [DMG] InvokeResponseMessage =
[1770453049.454] [38622:38638] [DMG] {
[1770453049.454] [38622:38638] [DMG]    suppressResponse = false,
[1770453049.454] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453049.455] [38622:38638] [DMG]    [
[1770453049.455] [38622:38638] [DMG]            InvokeResponseIB =
[1770453049.455] [38622:38638] [DMG]            {
[1770453049.455] [38622:38638] [DMG]                    CommandDataIB =
[1770453049.455] [38622:38638] [DMG]                    {
[1770453049.455] [38622:38638] [DMG]                            CommandPathIB =
[1770453049.455] [38622:38638] [DMG]                            {
[1770453049.455] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453049.455] [38622:38638] [DMG]                                    ClusterId = 0x30,
[1770453049.455] [38622:38638] [DMG]                                    CommandId = 0x3,
[1770453049.456] [38622:38638] [DMG]                            },
[1770453049.456] [38622:38638] [DMG]
[1770453049.456] [38622:38638] [DMG]                            CommandFields =
[1770453049.456] [38622:38638] [DMG]                            {
[1770453049.456] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453049.456] [38622:38638] [DMG]                                    0x1 = "" (0 chars),
[1770453049.456] [38622:38638] [DMG]                            },
[1770453049.456] [38622:38638] [DMG]                    },
[1770453049.457] [38622:38638] [DMG]
[1770453049.457] [38622:38638] [DMG]            },
[1770453049.457] [38622:38638] [DMG]
[1770453049.457] [38622:38638] [DMG]    ],
[1770453049.457] [38622:38638] [DMG]
[1770453049.457] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453049.457] [38622:38638] [DMG] },
[1770453049.457] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1770453049.457] [38622:38638] [CTL] Received SetRegulatoryConfig response errorCode=0
[1770453049.458] [38622:38638] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1770453049.458] [38622:38638] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1770453049.458] [38622:38638] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1770453049.458] [38622:38638] [CTL] Setting Terms and Conditions
[1770453049.458] [38622:38638] [CTL] Setting Terms and Conditions: Skipped
[1770453049.458] [38622:38638] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'
[1770453049.458] [38622:38638] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1770453049.458] [38622:38638] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770453049.458] [38622:38638] [CTL] Sending request for PAI certificate
[1770453049.458] [38622:38638] [CTL] Sending Certificate Chain request to 0xffffa40217c0 device
[1770453049.458] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453049.459] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453049.459] [38622:38638] [EM] <<< [E:28671i S:42557 M:216523826] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770453049.460] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453049.460] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453049.645] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453049.747] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453049.747] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453050.231] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453050.232] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453050.427] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453050.427] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453050.428] [38622:38638] [EM] >>> [E:28671i S:42557 M:9561281] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[1770453050.428] [38622:38638] [EM] Found matching exchange: 28671i, Delegate: 0xffffa400db18
[1770453050.428] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453050.428] [38622:38638] [DMG] InvokeResponseMessage =
[1770453050.428] [38622:38638] [DMG] {
[1770453050.428] [38622:38638] [DMG]    suppressResponse = false,
[1770453050.428] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453050.428] [38622:38638] [DMG]    [
[1770453050.428] [38622:38638] [DMG]            InvokeResponseIB =
[1770453050.428] [38622:38638] [DMG]            {
[1770453050.429] [38622:38638] [DMG]                    CommandDataIB =
[1770453050.429] [38622:38638] [DMG]                    {
[1770453050.429] [38622:38638] [DMG]                            CommandPathIB =
[1770453050.429] [38622:38638] [DMG]                            {
[1770453050.429] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453050.429] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453050.429] [38622:38638] [DMG]                                    CommandId = 0x3,
[1770453050.429] [38622:38638] [DMG]                            },
[1770453050.430] [38622:38638] [DMG]
[1770453050.430] [38622:38638] [DMG]                            CommandFields =
[1770453050.430] [38622:38638] [DMG]                            {
[1770453050.430] [38622:38638] [DMG]                                    0x0 = [
[1770453050.430] [38622:38638] [DMG]                                                    0x30, 0x82, 0x01, 0xcb, 0x30, 0x82, 0x01, 0x71, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x56, 0xad, 0x82, 0x22, 0xad, 0x94, 0x5b, 0x64, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x30, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x0f, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x54, 0x65, 0x73, 0x74, 0x20, 0x50, 0x41, 0x41, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x41, 0x9a, 0x93, 0x15, 0xc2, 0x17, 0x3e, 0x0c, 0x8c, 0x87, 0x6d, 0x03, 0xcc, 0xfc, 0x94, 0x48, 0x52, 0x64, 0x7f, 0x7f, 0xec, 0x5e, 0x50, 0x82, 0xf4, 0x05, 0x99, 0x28, 0xec, 0xa8, 0x94, 0xc5, 0x94, 0x15, 0x13, 0x09, 0xac, 0x63, 0x1e, 0x4c, 0xb0, 0x33, 0x92, 0xaf, 0x68, 0x4b, 0x0b, 0xaf, 0xb7, 0xe6, 0x5b, 0x3b, 0x81, 0x62, 0xc2, 0xf5, 0x2b, 0xf9, 0x31, 0xb8, 0xe7, 0x7a, 0xaa, 0x82, 0xa3, 0x66, 0x30, 0x64, 0x30, 0x12, 0x06, 0x03, 0x55, 0x1d, 0x
[1770453050.431] [38622:38638] [DMG]                                    ] (463 bytes)
[1770453050.431] [38622:38638] [DMG]                            },
[1770453050.431] [38622:38638] [DMG]                    },
[1770453050.431] [38622:38638] [DMG]
[1770453050.431] [38622:38638] [DMG]            },
[1770453050.431] [38622:38638] [DMG]
[1770453050.431] [38622:38638] [DMG]    ],
[1770453050.431] [38622:38638] [DMG]
[1770453050.432] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453050.432] [38622:38638] [DMG] },
[1770453050.432] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770453050.432] [38622:38638] [CTL] Received certificate chain from the device
[1770453050.432] [38622:38638] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1770453050.432] [38622:38638] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1770453050.432] [38622:38638] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1770453050.432] [38622:38638] [CTL] Sending request for DAC certificate
[1770453050.432] [38622:38638] [CTL] Sending Certificate Chain request to 0xffffa40217c0 device
[1770453050.433] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453050.433] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453050.433] [38622:38638] [EM] <<< [E:28672i S:42557 M:216523827] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770453050.434] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453050.434] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453050.620] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453050.819] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453050.820] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453051.112] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453051.113] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453051.306] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453051.306] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453051.307] [38622:38638] [EM] >>> [E:28672i S:42557 M:9561282] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[1770453051.307] [38622:38638] [EM] Found matching exchange: 28672i, Delegate: 0xffffa400e0b8
[1770453051.307] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453051.307] [38622:38638] [DMG] InvokeResponseMessage =
[1770453051.307] [38622:38638] [DMG] {
[1770453051.307] [38622:38638] [DMG]    suppressResponse = false,
[1770453051.307] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453051.307] [38622:38638] [DMG]    [
[1770453051.308] [38622:38638] [DMG]            InvokeResponseIB =
[1770453051.308] [38622:38638] [DMG]            {
[1770453051.308] [38622:38638] [DMG]                    CommandDataIB =
[1770453051.308] [38622:38638] [DMG]                    {
[1770453051.308] [38622:38638] [DMG]                            CommandPathIB =
[1770453051.308] [38622:38638] [DMG]                            {
[1770453051.308] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453051.309] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453051.309] [38622:38638] [DMG]                                    CommandId = 0x3,
[1770453051.309] [38622:38638] [DMG]                            },
[1770453051.309] [38622:38638] [DMG]
[1770453051.309] [38622:38638] [DMG]                            CommandFields =
[1770453051.310] [38622:38638] [DMG]                            {
[1770453051.310] [38622:38638] [DMG]                                    0x0 = [
[1770453051.310] [38622:38638] [DMG]                                                    0x30, 0x82, 0x01, 0xe7, 0x30, 0x82, 0x01, 0x8e, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x46, 0x7f, 0x57, 0x62, 0xc8, 0xdc, 0x90, 0xd5, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x33, 0x33, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x53, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x44, 0x41, 0x43, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x2f, 0x30, 0x78, 0x38, 0x30, 0x31, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x31, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x39, 0xef, 0x6c, 0x9d, 0x9c, 0x99, 0x7b, 0xa2, 0xc7, 0x31, 0x9a, 0x4c, 0x73, 0xc9, 0xbf, 0x47, 0xdb, 0xcd, 0xbc, 0x42, 0xc5, 0x41, 0x3e, 0xec, 0x14, 0x52, 0x75, 0xb8, 0x8f, 0xc1, 0x1a, 0xb1, 0xad, 0x0b, 0xc3, 0x3e, 0xf1, 0x4c, 0x27, 0x
[1770453051.310] [38622:38638] [DMG]                                    ] (491 bytes)
[1770453051.310] [38622:38638] [DMG]                            },
[1770453051.310] [38622:38638] [DMG]                    },
[1770453051.310] [38622:38638] [DMG]
[1770453051.311] [38622:38638] [DMG]            },
[1770453051.311] [38622:38638] [DMG]
[1770453051.311] [38622:38638] [DMG]    ],
[1770453051.311] [38622:38638] [DMG]
[1770453051.311] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453051.311] [38622:38638] [DMG] },
[1770453051.311] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770453051.311] [38622:38638] [CTL] Received certificate chain from the device
[1770453051.311] [38622:38638] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1770453051.311] [38622:38638] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1770453051.311] [38622:38638] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1770453051.311] [38622:38638] [CTL] Sending Attestation Request to the device.
[1770453051.312] [38622:38638] [CTL] Sending Attestation request to 0xffffa40217c0 device
[1770453051.312] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453051.312] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453051.312] [38622:38638] [EM] <<< [E:28673i S:42557 M:216523828] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770453051.313] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453051.313] [38622:38638] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770453051.314] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453051.497] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453051.697] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453051.697] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453052.087] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453052.087] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453052.379] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453052.380] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453052.380] [38622:38638] [EM] >>> [E:28673i S:42557 M:9561283] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[1770453052.380] [38622:38638] [EM] Found matching exchange: 28673i, Delegate: 0xffffa400db18
[1770453052.380] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453052.381] [38622:38638] [DMG] InvokeResponseMessage =
[1770453052.381] [38622:38638] [DMG] {
[1770453052.381] [38622:38638] [DMG]    suppressResponse = false,
[1770453052.381] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453052.381] [38622:38638] [DMG]    [
[1770453052.381] [38622:38638] [DMG]            InvokeResponseIB =
[1770453052.381] [38622:38638] [DMG]            {
[1770453052.381] [38622:38638] [DMG]                    CommandDataIB =
[1770453052.381] [38622:38638] [DMG]                    {
[1770453052.381] [38622:38638] [DMG]                            CommandPathIB =
[1770453052.382] [38622:38638] [DMG]                            {
[1770453052.382] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453052.382] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453052.382] [38622:38638] [DMG]                                    CommandId = 0x1,
[1770453052.382] [38622:38638] [DMG]                            },
[1770453052.383] [38622:38638] [DMG]
[1770453052.383] [38622:38638] [DMG]                            CommandFields =
[1770453052.383] [38622:38638] [DMG]                            {
[1770453052.383] [38622:38638] [DMG]                                    0x0 = [
[1770453052.384] [38622:38638] [DMG]                                                    0x15, 0x31, 0x01, 0x1b, 0x02, 0x30, 0x82, 0x02, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x02, 0x08, 0x30, 0x82, 0x02, 0x04, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x82, 0x01, 0x70, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x01, 0x61, 0x04, 0x82, 0x01, 0x5d, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0xf1, 0xff, 0x36, 0x02, 0x05, 0x00, 0x80, 0x05, 0x01, 0x80, 0x05, 0x02, 0x80, 0x05, 0x03, 0x80, 0x05, 0x04, 0x80, 0x05, 0x05, 0x80, 0x05, 0x06, 0x80, 0x05, 0x07, 0x80, 0x05, 0x08, 0x80, 0x05, 0x09, 0x80, 0x05, 0x0a, 0x80, 0x05, 0x0b, 0x80, 0x05, 0x0c, 0x80, 0x05, 0x0d, 0x80, 0x05, 0x0e, 0x80, 0x05, 0x0f, 0x80, 0x05, 0x10, 0x80, 0x05, 0x11, 0x80, 0x05, 0x12, 0x80, 0x05, 0x13, 0x80, 0x05, 0x14, 0x80, 0x05, 0x15, 0x80, 0x05, 0x16, 0x80, 0x05, 0x17, 0x80, 0x05, 0x18, 0x80, 0x05, 0x19, 0x80, 0x05, 0x1a, 0x80, 0x05, 0x1b, 0x80, 0x05, 0x1c, 0x80, 0x05, 0x1d, 0x80, 0x05, 0x1e, 0x80, 0x05, 0x1f, 0x80, 0x05, 0x20, 0x80, 0x05, 0x21, 0x80, 0x05, 0x22, 0x80, 0x05, 0x23, 0x80, 0x05, 0x24, 0x80, 0x05, 0x25, 0x80, 0x05, 0x26, 0x80, 0x05, 0x27, 0x80, 0x05, 0x28, 0x80, 0x05, 0x29, 0x80, 0x05, 0x2a, 0x80, 0x05, 0x2b, 0x80, 0x05, 0x2c, 0x80, 0x05, 0x2d, 0x80, 0x05, 0x2e, 0x80, 0x05, 0x2f, 0x80, 0x05, 0x30, 0x80, 0x05, 0x31, 0x80, 0x05, 0x32, 0x80, 0x05, 0x33, 0x80, 0x05, 0x34, 0x80, 0x05, 0x35, 0x80, 0x05, 0x36, 0x80, 0x05, 0x37, 0x80, 0x05, 0x38, 0x80, 0x05, 0x39, 0x80, 0x05, 0x3a, 0x80, 0x05, 0x3b, 0x80, 0x05, 0x3c, 0x80, 0x05, 0x3d, 0x80, 0x05, 0x3e, 0x80, 0x05, 0x3f, 0x80, 0x05, 0x40, 0x80, 0x05, 0x41, 0x80, 0x05, 0x42, 0x80, 0x05, 0x43, 0x80, 0x
[1770453052.384] [38622:38638] [DMG]                                    ] (583 bytes)
[1770453052.384] [38622:38638] [DMG]                                    0x1 = [
[1770453052.384] [38622:38638] [DMG]                                                    0xc3, 0xa6, 0xad, 0x86, 0xa4, 0xab, 0x27, 0x00, 0x8f, 0x05, 0x35, 0x55, 0x62, 0x55, 0xec, 0xd8, 0x18, 0x8b, 0x5e, 0xe0, 0xfd, 0xd7, 0x10, 0x9a, 0xbb, 0x47, 0xb0, 0xa7, 0xd8, 0xa1, 0x38, 0xc8, 0xa2, 0x51, 0xba, 0x96, 0x5d, 0x15, 0x1f, 0x3d, 0xb7, 0xda, 0x7a, 0x36, 0x8a, 0xde, 0x4e, 0x28, 0xc3, 0x9e, 0x6a, 0x6b, 0xda, 0x8e, 0x24, 0xb6, 0x07, 0xbf, 0x66, 0xfb, 0x35, 0xbb, 0x11, 0x7a,
[1770453052.384] [38622:38638] [DMG]                                    ] (64 bytes)
[1770453052.385] [38622:38638] [DMG]                            },
[1770453052.385] [38622:38638] [DMG]                    },
[1770453052.385] [38622:38638] [DMG]
[1770453052.385] [38622:38638] [DMG]            },
[1770453052.385] [38622:38638] [DMG]
[1770453052.385] [38622:38638] [DMG]    ],
[1770453052.385] [38622:38638] [DMG]
[1770453052.385] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453052.385] [38622:38638] [DMG] },
[1770453052.385] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1770453052.386] [38622:38638] [CTL] Received Attestation Information from the device
[1770453052.386] [38622:38638] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1770453052.386] [38622:38638] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[1770453052.386] [38622:38638] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1770453052.386] [38622:38638] [CTL] Performing next commissioning step 'AttestationVerification'
[1770453052.386] [38622:38638] [CTL] Verifying Device Attestation information received from the device
[1770453052.412] [38622:38638] [-] Device candidate DAC chain details:
[1770453052.412] [38622:38638] [-] --> DAC's VID: 0xFFF1, PID: 0x8010
[1770453052.412] [38622:38638] [-] ==== DAC certificate considered (491 bytes) ====
[1770453052.412] [38622:38638] [-] -----BEGIN CERTIFICATE-----
[1770453052.412] [38622:38638] [-] MIIB5zCCAY6gAwIBAgIIRn9XYsjckNUwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770453052.412] [38622:38638] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
[1770453052.412] [38622:38638] [-] RjEwIBcNMjIwMzMxMDAwMDAwWhgPOTk5OTEyMzEyMzU5NTlaMFMxJTAjBgNVBAMM
[1770453052.412] [38622:38638] [-] HE1hdHRlciBEZXYgREFDIDB4RkZGMS8weDgwMTAxFDASBgorBgEEAYKifAIBDARG
[1770453052.412] [38622:38638] [-] RkYxMRQwEgYKKwYBBAGConwCAgwEODAxMDBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770453052.412] [38622:38638] [-] A0IABDnvbJ2cmXuixzGaTHPJv0fbzbxCxUE+7BRSdbiPwRqxrQvDPvFMJ5QEQp8v
[1770453052.412] [38622:38638] [-] XucKBRty5se55zVO2vkqtP/4hC+jYDBeMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/
[1770453052.413] [38622:38638] [-] BAQDAgeAMB0GA1UdDgQWBBQy/CfR71NDovNk8Cz0cMtnR4DlqjAfBgNVHSMEGDAW
[1770453052.413] [38622:38638] [-] gBRjVA5H9kscONE4hKRi0WwZXY/7PDAKBggqhkjOPQQDAgNHADBEAiBvEbIFC9PS
[1770453052.413] [38622:38638] [-] 42wkYTAIbCIBsIz5nVp3sjqQBQD77wkTsgIgE2q2oLuL1PSt+AoSNM/vtn8K+3NV
[1770453052.413] [38622:38638] [-] 8dykctoWrEo2ZOU=
[1770453052.413] [38622:38638] [-] -----END CERTIFICATE-----
[1770453052.415] [38622:38638] [-] --> DAC certificate SKID: 32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
[1770453052.418] [38622:38638] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770453052.418] [38622:38638] [-] ==== PAI certificate considered (463 bytes) ====
[1770453052.418] [38622:38638] [-] -----BEGIN CERTIFICATE-----
[1770453052.418] [38622:38638] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770453052.418] [38622:38638] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMjAyMDUw
[1770453052.418] [38622:38638] [-] MDAwMDBaGA85OTk5MTIzMTIzNTk1OVowPTElMCMGA1UEAwwcTWF0dGVyIERldiBQ
[1770453052.418] [38622:38638] [-] QUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZGRjEwWTATBgcqhkjO
[1770453052.418] [38622:38638] [-] PQIBBggqhkjOPQMBBwNCAARBmpMVwhc+DIyHbQPM/JRIUmR/f+xeUIL0BZko7KiU
[1770453052.418] [38622:38638] [-] xZQVEwmsYx5MsDOSr2hLC6+35ls7gWLC9Sv5MbjneqqCo2YwZDASBgNVHRMBAf8E
[1770453052.418] [38622:38638] [-] CDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUY1QOR/ZLHDjROISk
[1770453052.418] [38622:38638] [-] YtFsGV2P+zwwHwYDVR0jBBgwFoAUav0idx9RH+y/FkGXZxDc3DGhcX4wCgYIKoZI
[1770453052.418] [38622:38638] [-] zj0EAwIDSAAwRQIhALLvJ/Sa6bUPuR7qyUxNC9u415KcbLiPrOUpNo0SBUwMAiBl
[1770453052.418] [38622:38638] [-] Xckrhr2QmIKmxiF3uCXX0F7b58Ivn+pxIg5+pwP4kQ==
[1770453052.418] [38622:38638] [-] -----END CERTIFICATE-----
[1770453052.421] [38622:38638] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770453052.423] [38622:38638] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770453052.434] [38622:38638] [-] ==== PAA certificate considered (449 bytes) ====
[1770453052.434] [38622:38638] [-] -----BEGIN CERTIFICATE-----
[1770453052.434] [38622:38638] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770453052.434] [38622:38638] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMTA2Mjgx
[1770453052.434] [38622:38638] [-] NDIzNDNaGA85OTk5MTIzMTIzNTk1OVowMDEYMBYGA1UEAwwPTWF0dGVyIFRlc3Qg
[1770453052.434] [38622:38638] [-] UEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770453052.434] [38622:38638] [-] A0IABLbLY3KIfyko9brIGqnZOuJDHK2p154kL2UXfvnO2TKijs0Duq9qj8oYShpQ
[1770453052.434] [38622:38638] [-] NUKWDUU/MD8fGUIddR6Pjxqam3WjZjBkMBIGA1UdEwEB/wQIMAYBAf8CAQEwDgYD
[1770453052.434] [38622:38638] [-] VR0PAQH/BAQDAgEGMB0GA1UdDgQWBBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAfBgNV
[1770453052.434] [38622:38638] [-] HSMEGDAWgBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAKBggqhkjOPQQDAgNHADBEAiBQ
[1770453052.434] [38622:38638] [-] qoAC9NkyqaAFOPZTaK0P/8jvu8m+t9pWmDXPmqdRDgIgI7rI/g8j51RFtlM5CBpH
[1770453052.434] [38622:38638] [-] mUkpxyqvChVI1A0DTVFLJd4=
[1770453052.434] [38622:38638] [-] -----END CERTIFICATE-----
[1770453052.437] [38622:38638] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770453052.439] [38622:38638] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770453052.453] [38622:38638] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770453052.455] [38622:38638] [-] Device certification declaration details:
[1770453052.455] [38622:38638] [-] --> VID: 0xFFF1
[1770453052.455] [38622:38638] [-] --> Device type ID: 0x0000_0016
[1770453052.455] [38622:38638] [-] --> Certification type: 0 (Development and testing)
[1770453052.455] [38622:38638] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1770453052.455] [38622:38638] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1770453052.455] [38622:38638] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1770453052.455] [38622:38638] [CTL] Verifying the device's DAC chain revocation status
[1770453052.455] [38622:38638] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770453052.456] [38622:38638] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1770453052.456] [38622:38638] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1770453052.456] [38622:38638] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1770453052.456] [38622:38638] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1770453052.456] [38622:38638] [CTL] Sending CSR request to 0xffffa40217c0 device
[1770453052.456] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453052.456] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453052.456] [38622:38638] [EM] <<< [E:28674i S:42557 M:216523829] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770453052.457] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453052.457] [38622:38638] [CTL] Sent CSR request, waiting for the CSR
[1770453052.457] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453052.569] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453052.770] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453052.770] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453053.060] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453053.060] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453053.061] [38622:38638] [EM] >>> [E:28674i S:42557 M:9561284] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:391)
[1770453053.061] [38622:38638] [EM] Found matching exchange: 28674i, Delegate: 0xffffa400e0b8
[1770453053.061] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453053.061] [38622:38638] [DMG] InvokeResponseMessage =
[1770453053.061] [38622:38638] [DMG] {
[1770453053.061] [38622:38638] [DMG]    suppressResponse = false,
[1770453053.061] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453053.062] [38622:38638] [DMG]    [
[1770453053.062] [38622:38638] [DMG]            InvokeResponseIB =
[1770453053.062] [38622:38638] [DMG]            {
[1770453053.062] [38622:38638] [DMG]                    CommandDataIB =
[1770453053.062] [38622:38638] [DMG]                    {
[1770453053.062] [38622:38638] [DMG]                            CommandPathIB =
[1770453053.062] [38622:38638] [DMG]                            {
[1770453053.062] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453053.063] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453053.063] [38622:38638] [DMG]                                    CommandId = 0x5,
[1770453053.063] [38622:38638] [DMG]                            },
[1770453053.063] [38622:38638] [DMG]
[1770453053.063] [38622:38638] [DMG]                            CommandFields =
[1770453053.063] [38622:38638] [DMG]                            {
[1770453053.063] [38622:38638] [DMG]                                    0x0 = [
[1770453053.064] [38622:38638] [DMG]                                                    0x15, 0x30, 0x01, 0xdc, 0x30, 0x81, 0xd9, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x1e, 0x1f, 0x32, 0xbb, 0x4e, 0x4c, 0x03, 0x9e, 0x0b, 0x34, 0xbc, 0x14, 0xf8, 0x6b, 0xa7, 0x61, 0xb5, 0xc2, 0x0b, 0x9b, 0xc8, 0x0f, 0xac, 0x6d, 0x02, 0xd2, 0x61, 0x9e, 0xa0, 0x29, 0x13, 0x12, 0xf9, 0xb2, 0x9b, 0x95, 0xe3, 0x6e, 0x0a, 0x5c, 0x96, 0x84, 0xb4, 0x83, 0xd5, 0xe4, 0xea, 0x95, 0xb7, 0xab, 0xfd, 0x13, 0x33, 0xeb, 0xb9, 0xbf, 0x8c, 0x89, 0x3f, 0x93, 0xbb, 0x4f, 0xae, 0x32, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x47, 0x00, 0x30, 0x44, 0x02, 0x20, 0x4a, 0xf9, 0x66, 0xfc, 0x5f, 0xb6, 0x51, 0xa8, 0x11, 0xf6, 0x23, 0xb9, 0x55, 0xbe, 0x6e, 0x42, 0x7e, 0xeb, 0xaf, 0x8e, 0x83, 0xfc, 0x56, 0x79, 0xa9, 0xb6, 0x91, 0x5c, 0x6f, 0x2f, 0x00, 0xe7, 0x02, 0x20, 0x6f, 0x3b, 0xf5, 0x6d, 0xfc, 0x24, 0x21, 0x81, 0x1f, 0x7c, 0xd0, 0x4c, 0xb2, 0xb4, 0x4f, 0xfc, 0x8d, 0x2b, 0x13, 0x9e, 0x85, 0x22, 0xc1, 0xb9, 0xaf, 0xc8, 0xa5, 0xba, 0xfb, 0x9c, 0x43, 0x0c, 0x30, 0x02, 0x20, 0xc6, 0x85, 0x6d, 0xdc, 0x34, 0x30, 0xad, 0x6a, 0x21, 0x15, 0x81, 0x88, 0xf7, 0xea, 0x99, 0x8c, 0x66, 0x11, 0x3f, 0xf5, 0x22, 0x99, 0x67, 0x1e, 0x66, 0x03, 0xe7, 0x99, 0x11, 0xcc, 0x0f, 0x6f, 0x18,
[1770453053.064] [38622:38638] [DMG]                                    ] (260 bytes)
[1770453053.065] [38622:38638] [DMG]                                    0x1 = [
[1770453053.065] [38622:38638] [DMG]                                                    0xb9, 0xc2, 0xbd, 0xe6, 0x87, 0xb2, 0x75, 0xc6, 0x59, 0x85, 0xf1, 0xf7, 0xf6, 0xa5, 0x32, 0x00, 0x4f, 0x86, 0x3f, 0x5e, 0x9e, 0x56, 0x7e, 0x64, 0x64, 0x9c, 0x08, 0x0c, 0x70, 0x45, 0x51, 0x40, 0x6c, 0x5d, 0x95, 0x73, 0xfd, 0xad, 0x7e, 0x77, 0xb2, 0x33, 0xd2, 0x4b, 0x32, 0x49, 0x66, 0x30, 0xef, 0x31, 0x0f, 0x5a, 0x2c, 0x12, 0x3c, 0x5c, 0x36, 0xb1, 0x61, 0x66, 0x38, 0xf1, 0x9c, 0x56,
[1770453053.065] [38622:38638] [DMG]                                    ] (64 bytes)
[1770453053.065] [38622:38638] [DMG]                            },
[1770453053.065] [38622:38638] [DMG]                    },
[1770453053.065] [38622:38638] [DMG]
[1770453053.066] [38622:38638] [DMG]            },
[1770453053.066] [38622:38638] [DMG]
[1770453053.066] [38622:38638] [DMG]    ],
[1770453053.066] [38622:38638] [DMG]
[1770453053.066] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453053.066] [38622:38638] [DMG] },
[1770453053.066] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1770453053.067] [38622:38638] [CTL] Received certificate signing request from the device
[1770453053.067] [38622:38638] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1770453053.067] [38622:38638] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1770453053.067] [38622:38638] [CTL] Performing next commissioning step 'ValidateCSR'
[1770453053.075] [38622:38638] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1770453053.075] [38622:38638] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1770453053.075] [38622:38638] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1770453053.075] [38622:38638] [CTL] Getting certificate chain for the device from the issuer
[1770453053.081] [38622:38638] [CTL] Verifying Certificate Signing Request
[1770453053.085] [38622:38638] [CTL] Generating NOC
[1770453053.085] [38622:38638] [CTL] Providing certificate chain to the commissioner
[1770453053.085] [38622:38638] [CTL] Received callback from the CA for NOC Chain generation. Status src/controller/ExampleOperationalCredentialsIssuer.cpp:409: Success
[1770453053.086] [38622:38638] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1770453053.086] [38622:38638] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1770453053.086] [38622:38638] [CTL] Sending root certificate to the device
[1770453053.086] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453053.087] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453053.087] [38622:38638] [EM] <<< [E:28675i S:42557 M:216523830] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1770453053.088] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453053.088] [38622:38638] [CTL] Sent root certificate to the device
[1770453053.089] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453053.642] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453053.838] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453053.841] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453053.841] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453053.842] [38622:38638] [EM] >>> [E:28675i S:42557 M:9561285] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770453053.842] [38622:38638] [EM] Found matching exchange: 28675i, Delegate: 0xffffa400db18
[1770453053.842] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453053.842] [38622:38638] [DMG] InvokeResponseMessage =
[1770453053.842] [38622:38638] [DMG] {
[1770453053.842] [38622:38638] [DMG]    suppressResponse = false,
[1770453053.842] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453053.842] [38622:38638] [DMG]    [
[1770453053.842] [38622:38638] [DMG]            InvokeResponseIB =
[1770453053.842] [38622:38638] [DMG]            {
[1770453053.843] [38622:38638] [DMG]                    CommandStatusIB =
[1770453053.843] [38622:38638] [DMG]                    {
[1770453053.843] [38622:38638] [DMG]                            CommandPathIB =
[1770453053.843] [38622:38638] [DMG]                            {
[1770453053.843] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453053.843] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453053.843] [38622:38638] [DMG]                                    CommandId = 0xb,
[1770453053.843] [38622:38638] [DMG]                            },
[1770453053.843] [38622:38638] [DMG]
[1770453053.844] [38622:38638] [DMG]                            StatusIB =
[1770453053.844] [38622:38638] [DMG]                            {
[1770453053.844] [38622:38638] [DMG]                                    status = 0x00 (SUCCESS),
[1770453053.844] [38622:38638] [DMG]                            },
[1770453053.844] [38622:38638] [DMG]
[1770453053.844] [38622:38638] [DMG]                    },
[1770453053.844] [38622:38638] [DMG]
[1770453053.844] [38622:38638] [DMG]            },
[1770453053.845] [38622:38638] [DMG]
[1770453053.845] [38622:38638] [DMG]    ],
[1770453053.845] [38622:38638] [DMG]
[1770453053.845] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453053.845] [38622:38638] [DMG] },
[1770453053.845] [38622:38638] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1770453053.845] [38622:38638] [CTL] Device confirmed that it has received the root certificate
[1770453053.846] [38622:38638] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1770453053.846] [38622:38638] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1770453053.846] [38622:38638] [CTL] Performing next commissioning step 'SendNOC'
[1770453053.846] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453053.846] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453053.846] [38622:38638] [EM] <<< [E:28676i S:42557 M:216523831] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1770453053.848] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453053.848] [38622:38638] [CTL] Sent operational certificate to the device
[1770453053.848] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453054.228] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453054.520] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453054.714] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453054.815] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453054.816] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453054.816] [38622:38638] [EM] >>> [E:28676i S:42557 M:9561286] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770453054.816] [38622:38638] [EM] Found matching exchange: 28676i, Delegate: 0xffffa400e0b8
[1770453054.816] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453054.817] [38622:38638] [DMG] InvokeResponseMessage =
[1770453054.817] [38622:38638] [DMG] {
[1770453054.817] [38622:38638] [DMG]    suppressResponse = false,
[1770453054.817] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453054.817] [38622:38638] [DMG]    [
[1770453054.817] [38622:38638] [DMG]            InvokeResponseIB =
[1770453054.817] [38622:38638] [DMG]            {
[1770453054.817] [38622:38638] [DMG]                    CommandDataIB =
[1770453054.817] [38622:38638] [DMG]                    {
[1770453054.818] [38622:38638] [DMG]                            CommandPathIB =
[1770453054.818] [38622:38638] [DMG]                            {
[1770453054.818] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453054.818] [38622:38638] [DMG]                                    ClusterId = 0x3e,
[1770453054.818] [38622:38638] [DMG]                                    CommandId = 0x8,
[1770453054.818] [38622:38638] [DMG]                            },
[1770453054.818] [38622:38638] [DMG]
[1770453054.819] [38622:38638] [DMG]                            CommandFields =
[1770453054.819] [38622:38638] [DMG]                            {
[1770453054.819] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453054.819] [38622:38638] [DMG]                                    0x1 = 1 (unsigned),
[1770453054.819] [38622:38638] [DMG]                            },
[1770453054.819] [38622:38638] [DMG]                    },
[1770453054.819] [38622:38638] [DMG]
[1770453054.820] [38622:38638] [DMG]            },
[1770453054.820] [38622:38638] [DMG]
[1770453054.820] [38622:38638] [DMG]    ],
[1770453054.820] [38622:38638] [DMG]
[1770453054.820] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453054.820] [38622:38638] [DMG] },
[1770453054.821] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1770453054.821] [38622:38638] [CTL] Device returned status 0 on receiving the NOC
[1770453054.821] [38622:38638] [CTL] Operational credentials provisioned on device 0xffffa40217c0
[1770453054.821] [38622:38638] [TOO] Secure Pairing Success
[1770453054.821] [38622:38638] [TOO] CASE establishment successful
[1770453054.821] [38622:38638] [CTL] Successfully finished commissioning step 'SendNOC'
[1770453054.821] [38622:38638] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1770453054.821] [38622:38638] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1770453054.821] [38622:38638] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1770453054.822] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453054.822] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453054.822] [38622:38638] [EM] <<< [E:28677i S:42557 M:216523832] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[1770453054.823] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453054.823] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453055.203] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453055.303] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453055.303] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453055.304] [38622:38638] [EM] >>> [E:28677i S:42557 M:9561287] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770453055.304] [38622:38638] [EM] Found matching exchange: 28677i, Delegate: 0xffffa400db18
[1770453055.304] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453055.304] [38622:38638] [DMG] InvokeResponseMessage =
[1770453055.304] [38622:38638] [DMG] {
[1770453055.304] [38622:38638] [DMG]    suppressResponse = false,
[1770453055.304] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453055.304] [38622:38638] [DMG]    [
[1770453055.304] [38622:38638] [DMG]            InvokeResponseIB =
[1770453055.304] [38622:38638] [DMG]            {
[1770453055.304] [38622:38638] [DMG]                    CommandDataIB =
[1770453055.305] [38622:38638] [DMG]                    {
[1770453055.305] [38622:38638] [DMG]                            CommandPathIB =
[1770453055.305] [38622:38638] [DMG]                            {
[1770453055.305] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453055.305] [38622:38638] [DMG]                                    ClusterId = 0x31,
[1770453055.305] [38622:38638] [DMG]                                    CommandId = 0x5,
[1770453055.305] [38622:38638] [DMG]                            },
[1770453055.306] [38622:38638] [DMG]
[1770453055.306] [38622:38638] [DMG]                            CommandFields =
[1770453055.306] [38622:38638] [DMG]                            {
[1770453055.306] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453055.306] [38622:38638] [DMG]                                    0x2 = 0 (unsigned),
[1770453055.306] [38622:38638] [DMG]                            },
[1770453055.306] [38622:38638] [DMG]                    },
[1770453055.306] [38622:38638] [DMG]
[1770453055.306] [38622:38638] [DMG]            },
[1770453055.306] [38622:38638] [DMG]
[1770453055.307] [38622:38638] [DMG]    ],
[1770453055.307] [38622:38638] [DMG]
[1770453055.307] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453055.307] [38622:38638] [DMG] },
[1770453055.307] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1770453055.307] [38622:38638] [CTL] Received NetworkConfig response, networkingStatus=0
[1770453055.307] [38622:38638] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1770453055.307] [38622:38638] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1770453055.307] [38622:38638] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1770453055.308] [38622:38638] [CTL] Arming failsafe (108 seconds)
[1770453055.308] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453055.308] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453055.308] [38622:38638] [EM] <<< [E:28678i S:42557 M:216523833] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770453055.309] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453055.309] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453055.495] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453055.499] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453055.499] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453055.500] [38622:38638] [EM] >>> [E:28678i S:42557 M:9561288] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770453055.500] [38622:38638] [EM] Found matching exchange: 28678i, Delegate: 0xffffa400e0b8
[1770453055.500] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453055.500] [38622:38638] [DMG] InvokeResponseMessage =
[1770453055.500] [38622:38638] [DMG] {
[1770453055.500] [38622:38638] [DMG]    suppressResponse = false,
[1770453055.500] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453055.500] [38622:38638] [DMG]    [
[1770453055.501] [38622:38638] [DMG]            InvokeResponseIB =
[1770453055.501] [38622:38638] [DMG]            {
[1770453055.501] [38622:38638] [DMG]                    CommandDataIB =
[1770453055.501] [38622:38638] [DMG]                    {
[1770453055.501] [38622:38638] [DMG]                            CommandPathIB =
[1770453055.501] [38622:38638] [DMG]                            {
[1770453055.501] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453055.502] [38622:38638] [DMG]                                    ClusterId = 0x30,
[1770453055.502] [38622:38638] [DMG]                                    CommandId = 0x1,
[1770453055.502] [38622:38638] [DMG]                            },
[1770453055.502] [38622:38638] [DMG]
[1770453055.502] [38622:38638] [DMG]                            CommandFields =
[1770453055.502] [38622:38638] [DMG]                            {
[1770453055.503] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453055.503] [38622:38638] [DMG]                                    0x1 = "" (0 chars),
[1770453055.503] [38622:38638] [DMG]                            },
[1770453055.503] [38622:38638] [DMG]                    },
[1770453055.503] [38622:38638] [DMG]
[1770453055.503] [38622:38638] [DMG]            },
[1770453055.504] [38622:38638] [DMG]
[1770453055.504] [38622:38638] [DMG]    ],
[1770453055.504] [38622:38638] [DMG]
[1770453055.504] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453055.504] [38622:38638] [DMG] },
[1770453055.505] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770453055.505] [38622:38638] [CTL] Received ArmFailSafe response errorCode=0
[1770453055.505] [38622:38638] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1770453055.505] [38622:38638] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1770453055.505] [38622:38638] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1770453055.505] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453055.505] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453055.506] [38622:38638] [EM] <<< [E:28679i S:42557 M:216523834] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1770453055.507] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453055.507] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453055.690] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453056.571] [38622:38629] [DL] Indication received, conn = 0xffffac023710
[1770453056.571] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16391
[1770453056.571] [38622:38638] [EM] >>> [E:28679i S:42557 M:9561289] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1770453056.572] [38622:38638] [EM] Found matching exchange: 28679i, Delegate: 0xffffa400db18
[1770453056.572] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453056.572] [38622:38638] [DMG] InvokeResponseMessage =
[1770453056.572] [38622:38638] [DMG] {
[1770453056.572] [38622:38638] [DMG]    suppressResponse = false,
[1770453056.572] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453056.572] [38622:38638] [DMG]    [
[1770453056.572] [38622:38638] [DMG]            InvokeResponseIB =
[1770453056.572] [38622:38638] [DMG]            {
[1770453056.572] [38622:38638] [DMG]                    CommandDataIB =
[1770453056.572] [38622:38638] [DMG]                    {
[1770453056.573] [38622:38638] [DMG]                            CommandPathIB =
[1770453056.573] [38622:38638] [DMG]                            {
[1770453056.573] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453056.573] [38622:38638] [DMG]                                    ClusterId = 0x31,
[1770453056.573] [38622:38638] [DMG]                                    CommandId = 0x7,
[1770453056.573] [38622:38638] [DMG]                            },
[1770453056.574] [38622:38638] [DMG]
[1770453056.574] [38622:38638] [DMG]                            CommandFields =
[1770453056.574] [38622:38638] [DMG]                            {
[1770453056.574] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453056.574] [38622:38638] [DMG]                                    0x2 = NULL
[1770453056.574] [38622:38638] [DMG]                            },
[1770453056.574] [38622:38638] [DMG]                    },
[1770453056.574] [38622:38638] [DMG]
[1770453056.574] [38622:38638] [DMG]            },
[1770453056.574] [38622:38638] [DMG]
[1770453056.575] [38622:38638] [DMG]    ],
[1770453056.575] [38622:38638] [DMG]
[1770453056.575] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453056.575] [38622:38638] [DMG] },
[1770453056.575] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1770453056.575] [38622:38638] [CTL] Received ConnectNetwork response, networkingStatus=0
[1770453056.575] [38622:38638] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1770453056.575] [38622:38638] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'
[1770453056.575] [38622:38638] [CTL] Performing next commissioning step 'kEvictPreviousCaseSessions'
[1770453056.575] [38622:38638] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1770453056.576] [38622:38638] [CTL] Successfully finished commissioning step 'kEvictPreviousCaseSessions'
[1770453056.576] [38622:38638] [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'
[1770453056.576] [38622:38638] [CTL] Performing next commissioning step 'kFindOperationalForStayActive'
[1770453056.576] [38622:38638] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770453056.576] [38622:38638] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770453056.576] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1770453056.577] [38622:38638] [DIS] Lookup started for 9BB8A0DFD2A8507B-00000000000008CA
[1770453056.577] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453056.777] [38622:38638] [DIS] Checking node lookup status for 9BB8A0DFD2A8507B-00000000000008CA after 201 ms
[1770453058.695] [38622:38638] [DIS] SRV record already actively processed.
[1770453058.700] [38622:38638] [DIS] Lookup clearing interface for non LL address
[1770453058.700] [38622:38638] [DIS] UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195%eth0]:5540: new best score: 5 (for 9BB8A0DFD2A8507B-00000000000008CA)
[1770453058.700] [38622:38638] [DIS] Checking node lookup status for 9BB8A0DFD2A8507B-00000000000008CA after 2123 ms
[1770453058.700] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540 while in state 2
[1770453058.700] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1770453058.701] [38622:38638] [IN] SecureSession[0xffffac04b600]: Allocated Type:2 LSID:42558
[1770453058.701] [38622:38638] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1770453058.704] [38622:38638] [EM] <<< [E:28680i S:0 M:35572785] (U) Msg TX from D62791A8431B9F85 to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1770453058.705] [38622:38638] [EM] ??1 [E:28680i S:0 M:35572785] (U) Msg Retransmission to 0:0000000000000000 scheduled for 4032ms from now [State:Idle II:3000 AI:2500 AT:4000]
[1770453058.705] [38622:38638] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1770453058.705] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1770453059.200] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16389
[1770453059.244] [38622:38638] [EM] >>> [E:28680i S:0 M:137509413 (Ack:35572785)] (U) Msg RX from 0:0000000000000000 [0000] to D62791A8431B9F85 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770453059.244] [38622:38638] [EM] Found matching exchange: 28680i, Delegate: 0xffffa4024e98
[1770453059.244] [38622:38638] [EM] Rxd Ack; Removing MessageCounter:35572785 from Retrans Table on exchange 28680i
[1770453059.317] [38622:38638] [EM] >>> [E:28680i S:0 M:137509414 (Ack:35572785)] (U) Msg RX from 0:0000000000000000 [0000] to D62791A8431B9F85 --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[1770453059.317] [38622:38638] [EM] Found matching exchange: 28680i, Delegate: 0xffffa4024e98
[1770453059.317] [38622:38638] [EM] CHIP MessageCounter:35572785 not in RetransTable on exchange 28680i
[1770453059.317] [38622:38638] [SC] Received Sigma2 msg
[1770453059.317] [38622:38638] [SC] Found MRP parameters in the message
[1770453059.331] [38622:38638] [SC] Peer <00000000000008CA, 1> assigned session ID 8046
[1770453059.331] [38622:38638] [SC] Sending Sigma3
[1770453059.332] [38622:38638] [EM] <<< [E:28680i S:0 M:35572786 (Ack:137509414)] (U) Msg TX from D62791A8431B9F85 to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1770453059.333] [38622:38638] [EM] ??1 [E:28680i S:0 M:35572786] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2845ms from now [State:Idle II:3000 AI:2500 AT:0]
[1770453059.333] [38622:38638] [SC] Sent Sigma3 msg
[1770453059.930] [38622:38638] [EM] >>> [E:28680i S:0 M:137509415 (Ack:35572786)] (U) Msg RX from 0:0000000000000000 [0000] to D62791A8431B9F85 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770453059.930] [38622:38638] [EM] Found matching exchange: 28680i, Delegate: 0xffffa4024e98
[1770453059.930] [38622:38638] [EM] Rxd Ack; Removing MessageCounter:35572786 from Retrans Table on exchange 28680i
[1770453059.935] [38622:38638] [EM] >>> [E:28680i S:0 M:137509416 (Ack:35572786)] (U) Msg RX from 0:0000000000000000 [0000] to D62791A8431B9F85 --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1770453059.935] [38622:38638] [EM] Found matching exchange: 28680i, Delegate: 0xffffa4024e98
[1770453059.935] [38622:38638] [EM] CHIP MessageCounter:35572786 not in RetransTable on exchange 28680i
[1770453059.935] [38622:38638] [SC] Success status report received. Session was established
[1770453059.943] [38622:38638] [SC] SecureSession[0xffffac04b600, LSID:42558]: State change 'kEstablishing' --> 'kActive'
[1770453059.943] [38622:38638] [IN] SecureSession[0xffffac04b600]: Activated - Type:2 LSID:42558
[1770453059.943] [38622:38638] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:42558 PSID:8046!
[1770453059.943] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1770453059.943] [38622:38638] [CTL] Successfully finished commissioning step 'kFindOperationalForStayActive'
[1770453059.943] [38622:38638] [CTL] Commissioning stage next step: 'kFindOperationalForStayActive' -> 'ICDSendStayActive'
[1770453059.943] [38622:38638] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1770453059.943] [38622:38638] [CTL] Skipping kICDSendStayActive
[1770453059.943] [38622:38638] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1770453059.943] [38622:38638] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'kFindOperationalForCommissioningComplete'
[1770453059.943] [38622:38638] [CTL] Performing next commissioning step 'kFindOperationalForCommissioningComplete'
[1770453059.943] [38622:38638] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770453059.943] [38622:38638] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770453059.944] [38622:38638] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1770453059.944] [38622:38638] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1770453059.944] [38622:38638] [CTL] Successfully finished commissioning step 'kFindOperationalForCommissioningComplete'
[1770453059.944] [38622:38638] [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'
[1770453059.944] [38622:38638] [CTL] Performing next commissioning step 'SendComplete'
[1770453059.944] [38622:38638] [DMG] ICR moving to [AddingComm]
[1770453059.944] [38622:38638] [DMG] ICR moving to [AddedComma]
[1770453059.944] [38622:38638] [EM] <<< [E:28681i S:42558 M:53663149] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [507B] [UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1770453059.945] [38622:38638] [EM] ??1 [E:28681i S:42558 M:53663149] (S) Msg Retransmission to 1:00000000000008CA scheduled for 4058ms from now [State:Idle II:3000 AI:2500 AT:0]
[1770453059.945] [38622:38638] [DMG] ICR moving to [AwaitingRe]
[1770453059.945] [38622:38638] [EM] <<< [E:28680i S:0 M:35572787 (Ack:137509416)] (U) Msg TX from D62791A8431B9F85 to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770453059.945] [38622:38638] [EM] Flushed pending ack for MessageCounter:137509416 on exchange 28680i
[1770453059.945] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 32792
[1770453060.514] [38622:38638] [EM] >>> [E:28681i S:42558 M:103191473 (Ack:53663149)] (S) Msg RX from 1:00000000000008CA [507B] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1770453060.514] [38622:38638] [EM] Found matching exchange: 28681i, Delegate: 0xffffa400e0b8
[1770453060.514] [38622:38638] [EM] Rxd Ack; Removing MessageCounter:53663149 from Retrans Table on exchange 28681i
[1770453060.514] [38622:38638] [DMG] ICR moving to [ResponseRe]
[1770453060.514] [38622:38638] [DMG] InvokeResponseMessage =
[1770453060.515] [38622:38638] [DMG] {
[1770453060.515] [38622:38638] [DMG]    suppressResponse = false,
[1770453060.515] [38622:38638] [DMG]    InvokeResponseIBs =
[1770453060.515] [38622:38638] [DMG]    [
[1770453060.515] [38622:38638] [DMG]            InvokeResponseIB =
[1770453060.515] [38622:38638] [DMG]            {
[1770453060.515] [38622:38638] [DMG]                    CommandDataIB =
[1770453060.515] [38622:38638] [DMG]                    {
[1770453060.515] [38622:38638] [DMG]                            CommandPathIB =
[1770453060.515] [38622:38638] [DMG]                            {
[1770453060.516] [38622:38638] [DMG]                                    EndpointId = 0x0,
[1770453060.516] [38622:38638] [DMG]                                    ClusterId = 0x30,
[1770453060.516] [38622:38638] [DMG]                                    CommandId = 0x5,
[1770453060.516] [38622:38638] [DMG]                            },
[1770453060.516] [38622:38638] [DMG]
[1770453060.517] [38622:38638] [DMG]                            CommandFields =
[1770453060.517] [38622:38638] [DMG]                            {
[1770453060.517] [38622:38638] [DMG]                                    0x0 = 0 (unsigned),
[1770453060.517] [38622:38638] [DMG]                                    0x1 = "" (0 chars),
[1770453060.517] [38622:38638] [DMG]                            },
[1770453060.517] [38622:38638] [DMG]                    },
[1770453060.517] [38622:38638] [DMG]
[1770453060.517] [38622:38638] [DMG]            },
[1770453060.517] [38622:38638] [DMG]
[1770453060.517] [38622:38638] [DMG]    ],
[1770453060.517] [38622:38638] [DMG]
[1770453060.517] [38622:38638] [DMG]    InteractionModelRevision = 11
[1770453060.518] [38622:38638] [DMG] },
[1770453060.518] [38622:38638] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1770453060.518] [38622:38638] [CTL] Received CommissioningComplete response, errorCode=0
[1770453060.518] [38622:38638] [CTL] Successfully finished commissioning step 'SendComplete'
[1770453060.518] [38622:38638] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1770453060.518] [38622:38638] [CTL] Performing next commissioning step 'Cleanup'
[1770453060.518] [38622:38638] [CTL] Successfully finished commissioning step 'Cleanup'
[1770453060.519] [38622:38638] [DIS] Closing all BLE connections
[1770453060.519] [38622:38638] [IN] Clearing BLE pending packets.
[1770453060.520] [38622:38638] [BLE] Auto-closing end point's BLE connection.
[1770453060.520] [38622:38638] [DL] Closing BLE GATT connection (con 0xffffac023710)
[1770453060.520] [38622:38629] [DL] Close BLE connection: peer=EF:47:1A:8D:E4:BC
[1770453060.665] [38622:38638] [IN] SecureSession[0xffffa4022cb0]: MarkForEviction Type:1 LSID:42557
[1770453060.666] [38622:38638] [SC] SecureSession[0xffffa4022cb0, LSID:42557]: State change 'kActive' --> 'kPendingEviction'
[1770453060.666] [38622:38638] [IN] SecureSession[0xffffa4022cb0]: Released - Type:1 LSID:42557
[1770453060.666] [38622:38638] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1770453060.666] [38622:38638] [TOO] Device commissioning completed with success
[1770453060.666] [38622:38638] [DMG] ICR moving to [AwaitingDe]
[1770453060.667] [38622:38638] [EM] <<< [E:28681i S:42558 M:53663150 (Ack:103191473)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [507B] [UDP:[fd98:42ee:f6b4:1:b8af:f97:7b89:6195]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1770453060.667] [38622:38629] [DL] BLE connection closed: conn=0xffffac023710
[1770453060.668] [38622:38638] [EM] Flushed pending ack for MessageCounter:103191473 on exchange 28681i
[1770453060.668] [38622:38638] [DL] HandlePlatformSpecificBLEEvent 16390
[1770453060.668] [38622:38638] [BLE] No endpoint for unsubscribe complete
[1770453060.668] [38622:38638] [BLE] No endpoint for connection error
[1770453060.669] [38622:38622] [CTL] Shutting down the commissioner
[1770453060.669] [38622:38622] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770453060.670] [38622:38622] [CTL] Shutting down the controller
[1770453060.670] [38622:38622] [IN] Expiring all sessions for fabric 0x1!!
[1770453060.670] [38622:38622] [IN] SecureSession[0xffffac04b600]: MarkForEviction Type:2 LSID:42558
[1770453060.670] [38622:38622] [SC] SecureSession[0xffffac04b600, LSID:42558]: State change 'kActive' --> 'kPendingEviction'
[1770453060.670] [38622:38622] [IN] SecureSession[0xffffac04b600]: Released - Type:2 LSID:42558
[1770453060.670] [38622:38622] [FP] Forgetting fabric 0x1
[1770453060.670] [38622:38622] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770453060.671] [38622:38622] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770453060.671] [38622:38622] [TS] Reverted Last Known Good Time to previous value
[1770453060.671] [38622:38622] [CTL] Shutting down the commissioner
[1770453060.671] [38622:38622] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770453060.671] [38622:38622] [CTL] Shutting down the controller
[1770453060.671] [38622:38622] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770453060.672] [38622:38622] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770453060.672] [38622:38622] [FP] Shutting down FabricTable
[1770453060.672] [38622:38622] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770453060.672] [38622:38622] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770453060.672] [38622:38622] [TS] Reverted Last Known Good Time to previous value
[1770453060.684] [38622:38622] [DL] Wrote settings to /tmp/chip_counters.ini
[1770453060.684] [38622:38622] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770453060.684] [38622:38622] [DL] Inet Layer shutdown
[1770453060.684] [38622:38622] [DL] BLE Layer shutdown
[1770453060.688] [38622:38622] [DL] WiFi-PAF Layer shutdown
[1770453060.689] [38622:38622] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770453060.689] [38622:38622] [DL] NFCCommissioningMgr shutdown
[1770453060.690] [38622:38622] [DL] System Layer shutdown

```