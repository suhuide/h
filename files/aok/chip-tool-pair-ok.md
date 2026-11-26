```c
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840
[1770357714.669] [47502:47502] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770357714.672] [47502:47502] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770357714.685] [47502:47502] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770357714.685] [47502:47502] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770357714.686] [47502:47502] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770357714.699] [47502:47502] [DL] Wrote settings to /tmp/chip_counters.ini
[1770357714.699] [47502:47502] [DL] NVS set: chip-counters/reboot-count = 2 (0x2)
[1770357714.701] [47502:47502] [DL] Got Ethernet interface: eth0
[1770357714.702] [47502:47502] [DL] Found the primary Ethernet interface:eth0
[1770357714.704] [47502:47502] [DL] Got WiFi interface: wlan0
[1770357714.704] [47502:47502] [DL] Failed to reset WiFi statistic counts
[1770357714.704] [47502:47502] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770357714.733] [47502:47502] [IN] UDP::Init bind&listen port=0
[1770357714.733] [47502:47502] [IN] UDP::Init bound to port=43718
[1770357714.733] [47502:47502] [IN] BLEBase::Init - setting/overriding transport
[1770357714.733] [47502:47502] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770357714.733] [47502:47502] [CTL] NFCBase::Init
[1770357714.733] [47502:47502] [IN] TransportMgr initialized
[1770357714.733] [47502:47502] [FP] Initializing FabricTable from persistent storage
[1770357714.734] [47502:47502] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770357714.738] [47502:47502] [FP] Fabric index 0x1 was retrieved from storage. Compressed FabricId 0xC10D5CDE8EFEE20A, FabricId 0x0000000000000001, NodeId 0x000000000001B669, VendorId 0xFFF1
[1770357714.743] [47502:47502] [DMG] Ember attribute persistence requires setting up
[1770357714.743] [47502:47502] [ZCL] Using ZAP configuration...
[1770357714.749] [47502:47502] [CTL] System State Initialized...
[1770357714.750] [47502:47502] [CTL] Setting attestation nonce to random value
[1770357714.750] [47502:47502] [CTL] Setting CSR nonce to random value
[1770357714.750] [47502:47502] [IN] UDP::Init bind&listen port=5550
[1770357714.750] [47502:47502] [IN] UDP::Init bound to port=5550
[1770357714.750] [47502:47502] [IN] TransportMgr initialized
[1770357714.751] [47502:47512] [DL] CHIP task running
[1770357714.751] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 32786
[1770357714.753] [47502:47512] [CTL] Setting attestation nonce to random value
[1770357714.753] [47502:47512] [CTL] Setting CSR nonce to random value
[1770357714.756] [47502:47512] [CTL] Generating NOC
[1770357714.758] [47502:47512] [FP] Validating NOC chain
[1770357714.763] [47502:47512] [FP] NOC chain validation successful
[1770357714.764] [47502:47512] [FP] Updated fabric at index: 0x1, Node ID: 0x000000000001B669
[1770357714.764] [47502:47512] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770357714.764] [47502:47512] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770357714.764] [47502:47512] [TS] Retaining current Last Known Good Time
[1770357714.768] [47502:47512] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770357714.772] [47502:47512] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770357714.775] [47502:47512] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: C10D5CDE8EFEE20A)
[1770357714.775] [47502:47512] [IN] UDP::Init bind&listen port=5551
[1770357714.776] [47502:47512] [IN] UDP::Init bound to port=5551
[1770357714.776] [47502:47512] [IN] TransportMgr initialized
[1770357714.812] [47502:47512] [CTL] Setting thread operational dataset from parameters
[1770357714.812] [47502:47512] [CTL] Setting attestation nonce to random value
[1770357714.812] [47502:47512] [CTL] Setting CSR nonce to random value
[1770357714.812] [47502:47512] [CTL] Commission called for node ID 0x00000000000008CA
[1770357714.863] [47502:47509] [BLE] BLE removing known devices
[1770357717.587] [47502:47509] [BLE] BLE initiating scan
[1770357717.595] [47502:47512] [BLE] ChipDeviceScanner has started scanning!
[1770357717.595] [47502:47512] [DL] Long dispatch time: 2783 ms, for event type 3
[1770357717.603] [47502:47509] [BLE] Device 03:F4:4E:2E:31:C4 does not look like a CHIP device.
[1770357717.626] [47502:47509] [BLE] Device 90:EF:4A:67:A8:7B does not look like a CHIP device.
[1770357717.639] [47502:47509] [BLE] Device 54:AA:F1:19:F7:5A does not look like a CHIP device.
[1770357717.641] [47502:47509] [BLE] Device 0F:15:1A:2E:FA:12 does not look like a CHIP device.
[1770357717.689] [47502:47509] [BLE] New device scanned: D2:88:D5:4D:90:CA
[1770357717.690] [47502:47509] [BLE] Device discriminator match. Attempting to connect.
[1770357717.696] [47502:47509] [BLE] ChipDeviceScanner has stopped scanning!
[1770357718.639] [47502:47509] [DL] ConnectDevice complete
[1770357718.639] [47502:47509] [BLE] New device connected: D2:88:D5:4D:90:CA
[1770357721.337] [47502:47509] [DL] CHIP service found
[1770357721.337] [47502:47509] [DL] Valid C1 characteristic found
[1770357721.337] [47502:47509] [DL] Valid C2 characteristic found
[1770357721.337] [47502:47509] [DL] New BLE connection: conn=0xffff7c028da0 device=D2:88:D5:4D:90:CA path=/org/bluez/hci0/dev_D2_88_D5_4D_90_CA
[1770357721.337] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16387
[1770357721.337] [47502:47512] [DIS] Closing all BLE connections
[1770357721.338] [47502:47512] [IN] BleConnectionComplete: endPoint 0xaaaacdeb6fd0
[1770357721.339] [47502:47512] [IN] SecureSession[0xffff74003cf0]: Allocated Type:1 LSID:47210
[1770357721.339] [47502:47512] [SC] Assigned local session key ID 47210
[1770357721.339] [47502:47512] [EM] <<< [E:55088i S:0 M:206666171] (U) Msg TX from 7030A929FDCA1259 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770357721.339] [47502:47512] [IN] Message appended to BLE send queue
[1770357721.340] [47502:47512] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770357722.466] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357722.663] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16390
[1770357722.663] [47502:47512] [BLE] subscribe complete, ep = 0xaaaacdeb6fd0
[1770357722.663] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357722.664] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357722.664] [47502:47512] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770357722.664] [47502:47512] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770357722.664] [47502:47512] [BLE] local and remote recv window size = 5
[1770357722.665] [47502:47512] [IN] BLE EndPoint 0xaaaacdeb6fd0 Connection Complete
[1770357723.050] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357723.149] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357723.149] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357723.149] [47502:47512] [EM] >>> [E:55088i S:0 M:157823077] (U) Msg RX from 0:0000000000000000 [0000] to 7030A929FDCA1259 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:154)
[1770357723.149] [47502:47512] [EM] Found matching exchange: 55088i, Delegate: 0xffff7400f6d8
[1770357723.150] [47502:47512] [SC] Received PBKDF param response
[1770357723.150] [47502:47512] [SC] Peer assigned session ID 554
[1770357723.150] [47502:47512] [SC] Found MRP parameters in the message
[1770357723.170] [47502:47512] [EM] <<< [E:55088i S:0 M:206666172] (U) Msg TX from 7030A929FDCA1259 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770357723.170] [47502:47512] [SC] Sent spake2p msg1
[1770357723.344] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357723.637] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357723.637] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357723.638] [47502:47512] [EM] >>> [E:55088i S:0 M:157823078] (U) Msg RX from 0:0000000000000000 [0000] to 7030A929FDCA1259 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770357723.638] [47502:47512] [EM] Found matching exchange: 55088i, Delegate: 0xffff7400f6d8
[1770357723.638] [47502:47512] [SC] Received spake2p msg2
[1770357723.643] [47502:47512] [EM] <<< [E:55088i S:0 M:206666173] (U) Msg TX from 7030A929FDCA1259 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770357723.645] [47502:47512] [SC] Sent spake2p msg3
[1770357723.928] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357723.930] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357723.931] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357723.931] [47502:47512] [EM] >>> [E:55088i S:0 M:157823079] (U) Msg RX from 0:0000000000000000 [0000] to 7030A929FDCA1259 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770357723.931] [47502:47512] [EM] Found matching exchange: 55088i, Delegate: 0xffff7400f6d8
[1770357723.932] [47502:47512] [SC] SecureSession[0xffff74003cf0, LSID:47210]: State change 'kEstablishing' --> 'kActive'
[1770357723.932] [47502:47512] [IN] SecureSession[0xffff74003cf0]: Activated - Type:1 LSID:47210
[1770357723.932] [47502:47512] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:47210 PSID:554!
[1770357723.932] [47502:47512] [CTL] Remote device completed SPAKE2+ handshake
[1770357723.932] [47502:47512] [TOO] Pairing Success
[1770357723.932] [47502:47512] [TOO] PASE establishment successful
[1770357723.933] [47502:47512] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770357723.933] [47502:47512] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770357723.933] [47502:47512] [CTL] Sending read requests for commissioning information
[1770357723.933] [47502:47512] [DMG] SendReadRequest ReadClient[0xffff74010cf0]: Sending Read Request
[1770357723.933] [47502:47512] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770357723.934] [47502:47512] [EM] <<< [E:55089i S:47210 M:200676516] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770357723.935] [47502:47512] [DMG] MoveToState ReadClient[0xffff74010cf0]: Moving to [AwaitingIn]
[1770357723.935] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 32792
[1770357724.221] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357724.322] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357724.323] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357724.615] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357724.616] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357725.099] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357725.100] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357725.101] [47502:47512] [EM] >>> [E:55089i S:47210 M:201358431] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:673)
[1770357725.101] [47502:47512] [EM] Found matching exchange: 55089i, Delegate: 0xffff74010d00
[1770357725.101] [47502:47512] [DMG] ReportDataMessage =
[1770357725.101] [47502:47512] [DMG] {
[1770357725.101] [47502:47512] [DMG]    AttributeReportIBs =
[1770357725.102] [47502:47512] [DMG]    [
[1770357725.102] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.102] [47502:47512] [DMG]            {
[1770357725.102] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.102] [47502:47512] [DMG]                    {
[1770357725.102] [47502:47512] [DMG]                            DataVersion = 0x6e0f98bf,
[1770357725.102] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.102] [47502:47512] [DMG]                            {
[1770357725.102] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.102] [47502:47512] [DMG]                                    Cluster = 0x31,
[1770357725.102] [47502:47512] [DMG]                                    Attribute = 0x0000_FFFC,
[1770357725.102] [47502:47512] [DMG]                            }
[1770357725.103] [47502:47512] [DMG]
[1770357725.103] [47502:47512] [DMG]                            Data = 2 (unsigned),
[1770357725.103] [47502:47512] [DMG]                    },
[1770357725.103] [47502:47512] [DMG]
[1770357725.103] [47502:47512] [DMG]            },
[1770357725.103] [47502:47512] [DMG]
[1770357725.103] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.103] [47502:47512] [DMG]            {
[1770357725.103] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.103] [47502:47512] [DMG]                    {
[1770357725.104] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.104] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.104] [47502:47512] [DMG]                            {
[1770357725.104] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.104] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.104] [47502:47512] [DMG]                                    Attribute = 0x0000_0000,
[1770357725.104] [47502:47512] [DMG]                            }
[1770357725.104] [47502:47512] [DMG]
[1770357725.105] [47502:47512] [DMG]                            Data = NULL
[1770357725.105] [47502:47512] [DMG]                    },
[1770357725.105] [47502:47512] [DMG]
[1770357725.105] [47502:47512] [DMG]            },
[1770357725.105] [47502:47512] [DMG]
[1770357725.105] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.105] [47502:47512] [DMG]            {
[1770357725.105] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.105] [47502:47512] [DMG]                    {
[1770357725.105] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.106] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.106] [47502:47512] [DMG]                            {
[1770357725.106] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.106] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.106] [47502:47512] [DMG]                                    Attribute = 0x0000_0001,
[1770357725.106] [47502:47512] [DMG]                            }
[1770357725.106] [47502:47512] [DMG]
[1770357725.106] [47502:47512] [DMG]                            Data = 0 (unsigned),
[1770357725.106] [47502:47512] [DMG]                    },
[1770357725.106] [47502:47512] [DMG]
[1770357725.106] [47502:47512] [DMG]            },
[1770357725.107] [47502:47512] [DMG]
[1770357725.107] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.107] [47502:47512] [DMG]            {
[1770357725.107] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.107] [47502:47512] [DMG]                    {
[1770357725.107] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.107] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.107] [47502:47512] [DMG]                            {
[1770357725.107] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.108] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.108] [47502:47512] [DMG]                                    Attribute = 0x0000_0002,
[1770357725.108] [47502:47512] [DMG]                            }
[1770357725.108] [47502:47512] [DMG]
[1770357725.108] [47502:47512] [DMG]                            Data = 0 (unsigned),
[1770357725.108] [47502:47512] [DMG]                    },
[1770357725.108] [47502:47512] [DMG]
[1770357725.108] [47502:47512] [DMG]            },
[1770357725.108] [47502:47512] [DMG]
[1770357725.108] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.109] [47502:47512] [DMG]            {
[1770357725.109] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.109] [47502:47512] [DMG]                    {
[1770357725.109] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.109] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.109] [47502:47512] [DMG]                            {
[1770357725.109] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.109] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.109] [47502:47512] [DMG]                                    Attribute = 0x0000_0005,
[1770357725.109] [47502:47512] [DMG]                            }
[1770357725.109] [47502:47512] [DMG]
[1770357725.110] [47502:47512] [DMG]                            Data = [
[1770357725.110] [47502:47512] [DMG]
[1770357725.110] [47502:47512] [DMG]                                    {
[1770357725.110] [47502:47512] [DMG]                                            0x0 = 0 (signed),
[1770357725.110] [47502:47512] [DMG]                                            0x1 = 0 (unsigned),
[1770357725.110] [47502:47512] [DMG]                                    },
[1770357725.110] [47502:47512] [DMG]                            ],
[1770357725.110] [47502:47512] [DMG]                    },
[1770357725.110] [47502:47512] [DMG]
[1770357725.110] [47502:47512] [DMG]            },
[1770357725.110] [47502:47512] [DMG]
[1770357725.110] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.110] [47502:47512] [DMG]            {
[1770357725.111] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.111] [47502:47512] [DMG]                    {
[1770357725.111] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.111] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.111] [47502:47512] [DMG]                            {
[1770357725.111] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.111] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.111] [47502:47512] [DMG]                                    Attribute = 0x0000_0006,
[1770357725.111] [47502:47512] [DMG]                            }
[1770357725.111] [47502:47512] [DMG]
[1770357725.111] [47502:47512] [DMG]                            Data = [
[1770357725.111] [47502:47512] [DMG]
[1770357725.111] [47502:47512] [DMG]                            ],
[1770357725.111] [47502:47512] [DMG]                    },
[1770357725.112] [47502:47512] [DMG]
[1770357725.112] [47502:47512] [DMG]            },
[1770357725.112] [47502:47512] [DMG]
[1770357725.112] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.112] [47502:47512] [DMG]            {
[1770357725.112] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.112] [47502:47512] [DMG]                    {
[1770357725.112] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.112] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.112] [47502:47512] [DMG]                            {
[1770357725.112] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.112] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.112] [47502:47512] [DMG]                                    Attribute = 0x0000_0007,
[1770357725.112] [47502:47512] [DMG]                            }
[1770357725.112] [47502:47512] [DMG]
[1770357725.113] [47502:47512] [DMG]                            Data = NULL
[1770357725.113] [47502:47512] [DMG]                    },
[1770357725.113] [47502:47512] [DMG]
[1770357725.113] [47502:47512] [DMG]            },
[1770357725.113] [47502:47512] [DMG]
[1770357725.113] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.113] [47502:47512] [DMG]            {
[1770357725.113] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.113] [47502:47512] [DMG]                    {
[1770357725.113] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.113] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.113] [47502:47512] [DMG]                            {
[1770357725.113] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.113] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.113] [47502:47512] [DMG]                                    Attribute = 0x0000_0008,
[1770357725.113] [47502:47512] [DMG]                            }
[1770357725.114] [47502:47512] [DMG]
[1770357725.114] [47502:47512] [DMG]                            Data = 2 (unsigned),
[1770357725.114] [47502:47512] [DMG]                    },
[1770357725.114] [47502:47512] [DMG]
[1770357725.114] [47502:47512] [DMG]            },
[1770357725.114] [47502:47512] [DMG]
[1770357725.114] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.114] [47502:47512] [DMG]            {
[1770357725.114] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.114] [47502:47512] [DMG]                    {
[1770357725.114] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.114] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.114] [47502:47512] [DMG]                            {
[1770357725.114] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.115] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.115] [47502:47512] [DMG]                                    Attribute = 0x0000_000A,
[1770357725.115] [47502:47512] [DMG]                            }
[1770357725.115] [47502:47512] [DMG]
[1770357725.115] [47502:47512] [DMG]                            Data = 2 (unsigned),
[1770357725.115] [47502:47512] [DMG]                    },
[1770357725.115] [47502:47512] [DMG]
[1770357725.115] [47502:47512] [DMG]            },
[1770357725.115] [47502:47512] [DMG]
[1770357725.115] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.115] [47502:47512] [DMG]            {
[1770357725.115] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.116] [47502:47512] [DMG]                    {
[1770357725.116] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.116] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.116] [47502:47512] [DMG]                            {
[1770357725.116] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.116] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.116] [47502:47512] [DMG]                                    Attribute = 0x0000_000B,
[1770357725.116] [47502:47512] [DMG]                            }
[1770357725.116] [47502:47512] [DMG]
[1770357725.116] [47502:47512] [DMG]                            Data = 2 (unsigned),
[1770357725.116] [47502:47512] [DMG]                    },
[1770357725.116] [47502:47512] [DMG]
[1770357725.116] [47502:47512] [DMG]            },
[1770357725.116] [47502:47512] [DMG]
[1770357725.116] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.116] [47502:47512] [DMG]            {
[1770357725.116] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.117] [47502:47512] [DMG]                    {
[1770357725.117] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.117] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.117] [47502:47512] [DMG]                            {
[1770357725.117] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.117] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.117] [47502:47512] [DMG]                                    Attribute = 0x0000_FFFC,
[1770357725.117] [47502:47512] [DMG]                            }
[1770357725.117] [47502:47512] [DMG]
[1770357725.117] [47502:47512] [DMG]                            Data = 1 (unsigned),
[1770357725.117] [47502:47512] [DMG]                    },
[1770357725.117] [47502:47512] [DMG]
[1770357725.117] [47502:47512] [DMG]            },
[1770357725.117] [47502:47512] [DMG]
[1770357725.117] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.117] [47502:47512] [DMG]            {
[1770357725.117] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.117] [47502:47512] [DMG]                    {
[1770357725.118] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.118] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.118] [47502:47512] [DMG]                            {
[1770357725.118] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.118] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.118] [47502:47512] [DMG]                                    Attribute = 0x0000_FFFD,
[1770357725.118] [47502:47512] [DMG]                            }
[1770357725.118] [47502:47512] [DMG]
[1770357725.118] [47502:47512] [DMG]                            Data = 2 (unsigned),
[1770357725.118] [47502:47512] [DMG]                    },
[1770357725.118] [47502:47512] [DMG]
[1770357725.118] [47502:47512] [DMG]            },
[1770357725.118] [47502:47512] [DMG]
[1770357725.118] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.118] [47502:47512] [DMG]            {
[1770357725.118] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.118] [47502:47512] [DMG]                    {
[1770357725.119] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.119] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.119] [47502:47512] [DMG]                            {
[1770357725.119] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.119] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.119] [47502:47512] [DMG]                                    Attribute = 0x0000_FFF8,
[1770357725.119] [47502:47512] [DMG]                            }
[1770357725.119] [47502:47512] [DMG]
[1770357725.119] [47502:47512] [DMG]                            Data = [
[1770357725.119] [47502:47512] [DMG]                                            3 (unsigned),
[1770357725.119] [47502:47512] [DMG]                            ],
[1770357725.119] [47502:47512] [DMG]                    },
[1770357725.119] [47502:47512] [DMG]
[1770357725.119] [47502:47512] [DMG]            },
[1770357725.119] [47502:47512] [DMG]
[1770357725.119] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.119] [47502:47512] [DMG]            {
[1770357725.119] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.120] [47502:47512] [DMG]                    {
[1770357725.120] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.120] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.120] [47502:47512] [DMG]                            {
[1770357725.120] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.120] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.120] [47502:47512] [DMG]                                    Attribute = 0x0000_FFF9,
[1770357725.120] [47502:47512] [DMG]                            }
[1770357725.120] [47502:47512] [DMG]
[1770357725.120] [47502:47512] [DMG]                            Data = [
[1770357725.120] [47502:47512] [DMG]                                            0 (unsigned), 2 (unsigned), 4 (unsigned),
[1770357725.120] [47502:47512] [DMG]                            ],
[1770357725.120] [47502:47512] [DMG]                    },
[1770357725.120] [47502:47512] [DMG]
[1770357725.120] [47502:47512] [DMG]            },
[1770357725.120] [47502:47512] [DMG]
[1770357725.120] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.121] [47502:47512] [DMG]            {
[1770357725.121] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.121] [47502:47512] [DMG]                    {
[1770357725.121] [47502:47512] [DMG]                            DataVersion = 0xbe3bec84,
[1770357725.121] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.121] [47502:47512] [DMG]                            {
[1770357725.121] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.121] [47502:47512] [DMG]                                    Cluster = 0x38,
[1770357725.121] [47502:47512] [DMG]                                    Attribute = 0x0000_FFFB,
[1770357725.121] [47502:47512] [DMG]                            }
[1770357725.121] [47502:47512] [DMG]
[1770357725.121] [47502:47512] [DMG]                            Data = [
[1770357725.121] [47502:47512] [DMG]                                            0 (unsigned), 1 (unsigned), 2 (unsigned), 5 (unsigned), 6 (unsigned), 7 (unsigned), 8 (unsigned), 10 (unsigned), 11 (unsigned), 65532 (unsigned), 65533 (unsigned), 65528 (unsigned), 65529 (unsigned), 65531 (unsigned),
[1770357725.121] [47502:47512] [DMG]                            ],
[1770357725.121] [47502:47512] [DMG]                    },
[1770357725.121] [47502:47512] [DMG]
[1770357725.122] [47502:47512] [DMG]            },
[1770357725.122] [47502:47512] [DMG]
[1770357725.122] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.122] [47502:47512] [DMG]            {
[1770357725.122] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.122] [47502:47512] [DMG]                    {
[1770357725.122] [47502:47512] [DMG]                            DataVersion = 0x3b37612e,
[1770357725.122] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.122] [47502:47512] [DMG]                            {
[1770357725.122] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.122] [47502:47512] [DMG]                                    Cluster = 0x28,
[1770357725.122] [47502:47512] [DMG]                                    Attribute = 0x0000_0004,
[1770357725.122] [47502:47512] [DMG]                            }
[1770357725.122] [47502:47512] [DMG]
[1770357725.122] [47502:47512] [DMG]                            Data = 32772 (unsigned),
[1770357725.122] [47502:47512] [DMG]                    },
[1770357725.122] [47502:47512] [DMG]
[1770357725.122] [47502:47512] [DMG]            },
[1770357725.123] [47502:47512] [DMG]
[1770357725.123] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.123] [47502:47512] [DMG]            {
[1770357725.123] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.123] [47502:47512] [DMG]                    {
[1770357725.123] [47502:47512] [DMG]                            DataVersion = 0x3b37612e,
[1770357725.123] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.123] [47502:47512] [DMG]                            {
[1770357725.123] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.123] [47502:47512] [DMG]                                    Cluster = 0x28,
[1770357725.123] [47502:47512] [DMG]                                    Attribute = 0x0000_0002,
[1770357725.123] [47502:47512] [DMG]                            }
[1770357725.123] [47502:47512] [DMG]
[1770357725.123] [47502:47512] [DMG]                            Data = 65521 (unsigned),
[1770357725.123] [47502:47512] [DMG]                    },
[1770357725.123] [47502:47512] [DMG]
[1770357725.123] [47502:47512] [DMG]            },
[1770357725.123] [47502:47512] [DMG]
[1770357725.124] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.124] [47502:47512] [DMG]            {
[1770357725.124] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.124] [47502:47512] [DMG]                    {
[1770357725.124] [47502:47512] [DMG]                            DataVersion = 0xa9823854,
[1770357725.124] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.124] [47502:47512] [DMG]                            {
[1770357725.124] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.124] [47502:47512] [DMG]                                    Cluster = 0x30,
[1770357725.124] [47502:47512] [DMG]                                    Attribute = 0x0000_0003,
[1770357725.124] [47502:47512] [DMG]                            }
[1770357725.124] [47502:47512] [DMG]
[1770357725.124] [47502:47512] [DMG]                            Data = 0 (unsigned),
[1770357725.124] [47502:47512] [DMG]                    },
[1770357725.124] [47502:47512] [DMG]
[1770357725.124] [47502:47512] [DMG]            },
[1770357725.124] [47502:47512] [DMG]
[1770357725.125] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.125] [47502:47512] [DMG]            {
[1770357725.125] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.125] [47502:47512] [DMG]                    {
[1770357725.125] [47502:47512] [DMG]                            DataVersion = 0xa9823854,
[1770357725.125] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.125] [47502:47512] [DMG]                            {
[1770357725.125] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.125] [47502:47512] [DMG]                                    Cluster = 0x30,
[1770357725.125] [47502:47512] [DMG]                                    Attribute = 0x0000_0002,
[1770357725.125] [47502:47512] [DMG]                            }
[1770357725.125] [47502:47512] [DMG]
[1770357725.125] [47502:47512] [DMG]                            Data = 0 (unsigned),
[1770357725.125] [47502:47512] [DMG]                    },
[1770357725.125] [47502:47512] [DMG]
[1770357725.125] [47502:47512] [DMG]            },
[1770357725.125] [47502:47512] [DMG]
[1770357725.125] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.126] [47502:47512] [DMG]            {
[1770357725.126] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.126] [47502:47512] [DMG]                    {
[1770357725.126] [47502:47512] [DMG]                            DataVersion = 0xa9823854,
[1770357725.126] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.126] [47502:47512] [DMG]                            {
[1770357725.126] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.126] [47502:47512] [DMG]                                    Cluster = 0x30,
[1770357725.126] [47502:47512] [DMG]                                    Attribute = 0x0000_0001,
[1770357725.126] [47502:47512] [DMG]                            }
[1770357725.126] [47502:47512] [DMG]
[1770357725.126] [47502:47512] [DMG]                            Data =
[1770357725.126] [47502:47512] [DMG]                            {
[1770357725.126] [47502:47512] [DMG]                                    0x0 = 60 (unsigned),
[1770357725.126] [47502:47512] [DMG]                                    0x1 = 900 (unsigned),
[1770357725.126] [47502:47512] [DMG]                            },
[1770357725.126] [47502:47512] [DMG]                    },
[1770357725.127] [47502:47512] [DMG]
[1770357725.127] [47502:47512] [DMG]            },
[1770357725.127] [47502:47512] [DMG]
[1770357725.127] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.127] [47502:47512] [DMG]            {
[1770357725.127] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.127] [47502:47512] [DMG]                    {
[1770357725.127] [47502:47512] [DMG]                            DataVersion = 0xa9823854,
[1770357725.127] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.127] [47502:47512] [DMG]                            {
[1770357725.127] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.127] [47502:47512] [DMG]                                    Cluster = 0x30,
[1770357725.127] [47502:47512] [DMG]                                    Attribute = 0x0000_0000,
[1770357725.127] [47502:47512] [DMG]                            }
[1770357725.127] [47502:47512] [DMG]
[1770357725.127] [47502:47512] [DMG]                            Data = 0 (unsigned),
[1770357725.127] [47502:47512] [DMG]                    },
[1770357725.127] [47502:47512] [DMG]
[1770357725.128] [47502:47512] [DMG]            },
[1770357725.128] [47502:47512] [DMG]
[1770357725.128] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.128] [47502:47512] [DMG]            {
[1770357725.128] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.128] [47502:47512] [DMG]                    {
[1770357725.128] [47502:47512] [DMG]                            DataVersion = 0xa9823854,
[1770357725.128] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.128] [47502:47512] [DMG]                            {
[1770357725.128] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.128] [47502:47512] [DMG]                                    Cluster = 0x30,
[1770357725.128] [47502:47512] [DMG]                                    Attribute = 0x0000_0004,
[1770357725.128] [47502:47512] [DMG]                            }
[1770357725.128] [47502:47512] [DMG]
[1770357725.128] [47502:47512] [DMG]                            Data = true,
[1770357725.128] [47502:47512] [DMG]                    },
[1770357725.128] [47502:47512] [DMG]
[1770357725.128] [47502:47512] [DMG]            },
[1770357725.129] [47502:47512] [DMG]
[1770357725.129] [47502:47512] [DMG]    ],
[1770357725.129] [47502:47512] [DMG]
[1770357725.129] [47502:47512] [DMG]    SuppressResponse = true,
[1770357725.129] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357725.129] [47502:47512] [DMG] }
[1770357725.133] [47502:47512] [DMG] SendReadRequest ReadClient[0xffff74010cf0]: Sending Read Request
[1770357725.134] [47502:47512] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770357725.134] [47502:47512] [EM] <<< [E:55090i S:47210 M:200676517] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770357725.135] [47502:47512] [DMG] MoveToState ReadClient[0xffff74010cf0]: Moving to [AwaitingIn]
[1770357725.488] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357725.588] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357725.588] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357725.589] [47502:47512] [EM] >>> [E:55090i S:47210 M:201358432] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:181)
[1770357725.589] [47502:47512] [EM] Found matching exchange: 55090i, Delegate: 0xffff74010d00
[1770357725.589] [47502:47512] [DMG] ReportDataMessage =
[1770357725.589] [47502:47512] [DMG] {
[1770357725.589] [47502:47512] [DMG]    AttributeReportIBs =
[1770357725.589] [47502:47512] [DMG]    [
[1770357725.590] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.590] [47502:47512] [DMG]            {
[1770357725.590] [47502:47512] [DMG]                    AttributeStatusIB =
[1770357725.590] [47502:47512] [DMG]                    {
[1770357725.590] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.590] [47502:47512] [DMG]                            {
[1770357725.590] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.590] [47502:47512] [DMG]                                    Cluster = 0x46,
[1770357725.590] [47502:47512] [DMG]                                    Attribute = 0x0000_0002,
[1770357725.591] [47502:47512] [DMG]                            }
[1770357725.591] [47502:47512] [DMG]
[1770357725.591] [47502:47512] [DMG]                            StatusIB =
[1770357725.591] [47502:47512] [DMG]                            {
[1770357725.591] [47502:47512] [DMG]                                    status = 0xc3 (UNSUPPORTED_CLUSTER),
[1770357725.591] [47502:47512] [DMG]                            },
[1770357725.591] [47502:47512] [DMG]
[1770357725.591] [47502:47512] [DMG]                    },
[1770357725.591] [47502:47512] [DMG]
[1770357725.592] [47502:47512] [DMG]            },
[1770357725.592] [47502:47512] [DMG]
[1770357725.592] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.592] [47502:47512] [DMG]            {
[1770357725.592] [47502:47512] [DMG]                    AttributeStatusIB =
[1770357725.592] [47502:47512] [DMG]                    {
[1770357725.592] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.592] [47502:47512] [DMG]                            {
[1770357725.592] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.593] [47502:47512] [DMG]                                    Cluster = 0x46,
[1770357725.593] [47502:47512] [DMG]                                    Attribute = 0x0000_0001,
[1770357725.593] [47502:47512] [DMG]                            }
[1770357725.593] [47502:47512] [DMG]
[1770357725.593] [47502:47512] [DMG]                            StatusIB =
[1770357725.593] [47502:47512] [DMG]                            {
[1770357725.594] [47502:47512] [DMG]                                    status = 0xc3 (UNSUPPORTED_CLUSTER),
[1770357725.594] [47502:47512] [DMG]                            },
[1770357725.594] [47502:47512] [DMG]
[1770357725.594] [47502:47512] [DMG]                    },
[1770357725.594] [47502:47512] [DMG]
[1770357725.594] [47502:47512] [DMG]            },
[1770357725.594] [47502:47512] [DMG]
[1770357725.594] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.594] [47502:47512] [DMG]            {
[1770357725.594] [47502:47512] [DMG]                    AttributeStatusIB =
[1770357725.594] [47502:47512] [DMG]                    {
[1770357725.594] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.595] [47502:47512] [DMG]                            {
[1770357725.595] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.595] [47502:47512] [DMG]                                    Cluster = 0x46,
[1770357725.595] [47502:47512] [DMG]                                    Attribute = 0x0000_0000,
[1770357725.595] [47502:47512] [DMG]                            }
[1770357725.595] [47502:47512] [DMG]
[1770357725.595] [47502:47512] [DMG]                            StatusIB =
[1770357725.595] [47502:47512] [DMG]                            {
[1770357725.595] [47502:47512] [DMG]                                    status = 0xc3 (UNSUPPORTED_CLUSTER),
[1770357725.595] [47502:47512] [DMG]                            },
[1770357725.595] [47502:47512] [DMG]
[1770357725.595] [47502:47512] [DMG]                    },
[1770357725.596] [47502:47512] [DMG]
[1770357725.596] [47502:47512] [DMG]            },
[1770357725.596] [47502:47512] [DMG]
[1770357725.596] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.596] [47502:47512] [DMG]            {
[1770357725.596] [47502:47512] [DMG]                    AttributeStatusIB =
[1770357725.596] [47502:47512] [DMG]                    {
[1770357725.596] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.596] [47502:47512] [DMG]                            {
[1770357725.596] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.596] [47502:47512] [DMG]                                    Cluster = 0x46,
[1770357725.596] [47502:47512] [DMG]                                    Attribute = 0x0000_0007,
[1770357725.597] [47502:47512] [DMG]                            }
[1770357725.597] [47502:47512] [DMG]
[1770357725.597] [47502:47512] [DMG]                            StatusIB =
[1770357725.597] [47502:47512] [DMG]                            {
[1770357725.597] [47502:47512] [DMG]                                    status = 0xc3 (UNSUPPORTED_CLUSTER),
[1770357725.597] [47502:47512] [DMG]                            },
[1770357725.597] [47502:47512] [DMG]
[1770357725.597] [47502:47512] [DMG]                    },
[1770357725.597] [47502:47512] [DMG]
[1770357725.597] [47502:47512] [DMG]            },
[1770357725.598] [47502:47512] [DMG]
[1770357725.598] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.598] [47502:47512] [DMG]            {
[1770357725.598] [47502:47512] [DMG]                    AttributeStatusIB =
[1770357725.598] [47502:47512] [DMG]                    {
[1770357725.598] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.598] [47502:47512] [DMG]                            {
[1770357725.598] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.598] [47502:47512] [DMG]                                    Cluster = 0x46,
[1770357725.598] [47502:47512] [DMG]                                    Attribute = 0x0000_0006,
[1770357725.599] [47502:47512] [DMG]                            }
[1770357725.599] [47502:47512] [DMG]
[1770357725.599] [47502:47512] [DMG]                            StatusIB =
[1770357725.599] [47502:47512] [DMG]                            {
[1770357725.599] [47502:47512] [DMG]                                    status = 0xc3 (UNSUPPORTED_CLUSTER),
[1770357725.599] [47502:47512] [DMG]                            },
[1770357725.599] [47502:47512] [DMG]
[1770357725.599] [47502:47512] [DMG]                    },
[1770357725.599] [47502:47512] [DMG]
[1770357725.599] [47502:47512] [DMG]            },
[1770357725.599] [47502:47512] [DMG]
[1770357725.600] [47502:47512] [DMG]            AttributeReportIB =
[1770357725.600] [47502:47512] [DMG]            {
[1770357725.600] [47502:47512] [DMG]                    AttributeDataIB =
[1770357725.600] [47502:47512] [DMG]                    {
[1770357725.600] [47502:47512] [DMG]                            DataVersion = 0x6e0f98bf,
[1770357725.600] [47502:47512] [DMG]                            AttributePathIB =
[1770357725.600] [47502:47512] [DMG]                            {
[1770357725.600] [47502:47512] [DMG]                                    Endpoint = 0x0,
[1770357725.600] [47502:47512] [DMG]                                    Cluster = 0x31,
[1770357725.600] [47502:47512] [DMG]                                    Attribute = 0x0000_0003,
[1770357725.600] [47502:47512] [DMG]                            }
[1770357725.601] [47502:47512] [DMG]
[1770357725.601] [47502:47512] [DMG]                            Data = 20 (unsigned),
[1770357725.601] [47502:47512] [DMG]                    },
[1770357725.601] [47502:47512] [DMG]
[1770357725.601] [47502:47512] [DMG]            },
[1770357725.601] [47502:47512] [DMG]
[1770357725.601] [47502:47512] [DMG]    ],
[1770357725.601] [47502:47512] [DMG]
[1770357725.601] [47502:47512] [DMG]    SuppressResponse = true,
[1770357725.602] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357725.602] [47502:47512] [DMG] }
[1770357725.603] [47502:47512] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1770357725.603] [47502:47512] [SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8004
[1770357725.603] [47502:47512] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1770357725.604] [47502:47512] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1770357725.604] [47502:47512] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1770357725.604] [47502:47512] [CTL] Performing next commissioning step 'ArmFailSafe'
[1770357725.604] [47502:47512] [CTL] Arming failsafe (60 seconds)
[1770357725.604] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357725.604] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357725.604] [47502:47512] [EM] <<< [E:55091i S:47210 M:200676518] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770357725.605] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357725.781] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357725.784] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357725.785] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357725.785] [47502:47512] [EM] >>> [E:55091i S:47210 M:201358433] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770357725.785] [47502:47512] [EM] Found matching exchange: 55091i, Delegate: 0xffff74008ae8
[1770357725.785] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357725.786] [47502:47512] [DMG] InvokeResponseMessage =
[1770357725.786] [47502:47512] [DMG] {
[1770357725.786] [47502:47512] [DMG]    suppressResponse = false,
[1770357725.786] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357725.786] [47502:47512] [DMG]    [
[1770357725.786] [47502:47512] [DMG]            InvokeResponseIB =
[1770357725.786] [47502:47512] [DMG]            {
[1770357725.786] [47502:47512] [DMG]                    CommandDataIB =
[1770357725.787] [47502:47512] [DMG]                    {
[1770357725.787] [47502:47512] [DMG]                            CommandPathIB =
[1770357725.787] [47502:47512] [DMG]                            {
[1770357725.787] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357725.787] [47502:47512] [DMG]                                    ClusterId = 0x30,
[1770357725.787] [47502:47512] [DMG]                                    CommandId = 0x1,
[1770357725.787] [47502:47512] [DMG]                            },
[1770357725.788] [47502:47512] [DMG]
[1770357725.788] [47502:47512] [DMG]                            CommandFields =
[1770357725.788] [47502:47512] [DMG]                            {
[1770357725.788] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357725.788] [47502:47512] [DMG]                                    0x1 = "" (0 chars),
[1770357725.788] [47502:47512] [DMG]                            },
[1770357725.789] [47502:47512] [DMG]                    },
[1770357725.789] [47502:47512] [DMG]
[1770357725.789] [47502:47512] [DMG]            },
[1770357725.789] [47502:47512] [DMG]
[1770357725.789] [47502:47512] [DMG]    ],
[1770357725.789] [47502:47512] [DMG]
[1770357725.790] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357725.790] [47502:47512] [DMG] },
[1770357725.790] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770357725.790] [47502:47512] [CTL] Received ArmFailSafe response errorCode=0
[1770357725.790] [47502:47512] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1770357725.791] [47502:47512] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1770357725.791] [47502:47512] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1770357725.791] [47502:47512] [CTL] Setting Regulatory Config
[1770357725.791] [47502:47512] [CTL] Device does not support configurable regulatory location
[1770357725.791] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357725.791] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357725.791] [47502:47512] [EM] <<< [E:55092i S:47210 M:200676519] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1770357725.792] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357725.793] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357725.976] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357725.979] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357725.980] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357725.980] [47502:47512] [EM] >>> [E:55092i S:47210 M:201358434] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770357725.980] [47502:47512] [EM] Found matching exchange: 55092i, Delegate: 0xffff7400aae8
[1770357725.981] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357725.981] [47502:47512] [DMG] InvokeResponseMessage =
[1770357725.981] [47502:47512] [DMG] {
[1770357725.981] [47502:47512] [DMG]    suppressResponse = false,
[1770357725.981] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357725.981] [47502:47512] [DMG]    [
[1770357725.981] [47502:47512] [DMG]            InvokeResponseIB =
[1770357725.981] [47502:47512] [DMG]            {
[1770357725.981] [47502:47512] [DMG]                    CommandDataIB =
[1770357725.982] [47502:47512] [DMG]                    {
[1770357725.982] [47502:47512] [DMG]                            CommandPathIB =
[1770357725.982] [47502:47512] [DMG]                            {
[1770357725.982] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357725.982] [47502:47512] [DMG]                                    ClusterId = 0x30,
[1770357725.982] [47502:47512] [DMG]                                    CommandId = 0x3,
[1770357725.982] [47502:47512] [DMG]                            },
[1770357725.983] [47502:47512] [DMG]
[1770357725.983] [47502:47512] [DMG]                            CommandFields =
[1770357725.983] [47502:47512] [DMG]                            {
[1770357725.983] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357725.983] [47502:47512] [DMG]                                    0x1 = "" (0 chars),
[1770357725.983] [47502:47512] [DMG]                            },
[1770357725.984] [47502:47512] [DMG]                    },
[1770357725.984] [47502:47512] [DMG]
[1770357725.984] [47502:47512] [DMG]            },
[1770357725.984] [47502:47512] [DMG]
[1770357725.984] [47502:47512] [DMG]    ],
[1770357725.984] [47502:47512] [DMG]
[1770357725.984] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357725.984] [47502:47512] [DMG] },
[1770357725.984] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1770357725.984] [47502:47512] [CTL] Received SetRegulatoryConfig response errorCode=0
[1770357725.984] [47502:47512] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1770357725.985] [47502:47512] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1770357725.985] [47502:47512] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1770357725.985] [47502:47512] [CTL] Setting Terms and Conditions
[1770357725.985] [47502:47512] [CTL] Setting Terms and Conditions: Skipped
[1770357725.985] [47502:47512] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'

[1770357725.985] [47502:47512] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'ConfigureUTCTime'
[1770357725.985] [47502:47512] [CTL] Performing next commissioning step 'ConfigureUTCTime'
[1770357725.985] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357725.985] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357725.986] [47502:47512] [EM] <<< [E:55093i S:47210 M:200676520] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:72)
[1770357725.987] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357725.987] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357726.171] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357726.367] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357726.367] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357726.368] [47502:47512] [EM] >>> [E:55093i S:47210 M:201358435] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770357726.368] [47502:47512] [EM] Found matching exchange: 55093i, Delegate: 0xffff74008ae8
[1770357726.368] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357726.368] [47502:47512] [DMG] InvokeResponseMessage =
[1770357726.368] [47502:47512] [DMG] {
[1770357726.368] [47502:47512] [DMG]    suppressResponse = false,
[1770357726.369] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357726.369] [47502:47512] [DMG]    [
[1770357726.369] [47502:47512] [DMG]            InvokeResponseIB =
[1770357726.369] [47502:47512] [DMG]            {
[1770357726.369] [47502:47512] [DMG]                    CommandStatusIB =
[1770357726.369] [47502:47512] [DMG]                    {
[1770357726.369] [47502:47512] [DMG]                            CommandPathIB =
[1770357726.369] [47502:47512] [DMG]                            {
[1770357726.370] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357726.370] [47502:47512] [DMG]                                    ClusterId = 0x38,
[1770357726.370] [47502:47512] [DMG]                                    CommandId = 0x0,
[1770357726.370] [47502:47512] [DMG]                            },
[1770357726.370] [47502:47512] [DMG]
[1770357726.370] [47502:47512] [DMG]                            StatusIB =
[1770357726.370] [47502:47512] [DMG]                            {
[1770357726.371] [47502:47512] [DMG]                                    status = 0x00 (SUCCESS),
[1770357726.371] [47502:47512] [DMG]                            },
[1770357726.371] [47502:47512] [DMG]
[1770357726.371] [47502:47512] [DMG]                    },
[1770357726.371] [47502:47512] [DMG]
[1770357726.371] [47502:47512] [DMG]            },
[1770357726.371] [47502:47512] [DMG]
[1770357726.371] [47502:47512] [DMG]    ],
[1770357726.372] [47502:47512] [DMG]
[1770357726.372] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357726.372] [47502:47512] [DMG] },
[1770357726.372] [47502:47512] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_0038 Command=0x0000_0000 Status=0x0
[1770357726.372] [47502:47512] [CTL] Successfully finished commissioning step 'ConfigureUTCTime'
[1770357726.372] [47502:47512] [CTL] Commissioning stage next step: 'ConfigureUTCTime' -> 'SendPAICertificateRequest'
[1770357726.372] [47502:47512] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770357726.372] [47502:47512] [CTL] Sending request for PAI certificate
[1770357726.373] [47502:47512] [CTL] Sending Certificate Chain request to 0xffff7400f680 device
[1770357726.373] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357726.373] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357726.373] [47502:47512] [EM] <<< [E:55094i S:47210 M:200676521] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770357726.375] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357726.375] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357726.658] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357727.246] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357727.247] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357727.638] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357727.638] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357727.831] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357727.831] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357727.832] [47502:47512] [EM] >>> [E:55094i S:47210 M:201358436] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[1770357727.832] [47502:47512] [EM] Found matching exchange: 55094i, Delegate: 0xffff7400aae8
[1770357727.832] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357727.832] [47502:47512] [DMG] InvokeResponseMessage =
[1770357727.832] [47502:47512] [DMG] {
[1770357727.832] [47502:47512] [DMG]    suppressResponse = false,
[1770357727.832] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357727.833] [47502:47512] [DMG]    [
[1770357727.833] [47502:47512] [DMG]            InvokeResponseIB =
[1770357727.833] [47502:47512] [DMG]            {
[1770357727.833] [47502:47512] [DMG]                    CommandDataIB =
[1770357727.833] [47502:47512] [DMG]                    {
[1770357727.833] [47502:47512] [DMG]                            CommandPathIB =
[1770357727.833] [47502:47512] [DMG]                            {
[1770357727.833] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357727.834] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357727.834] [47502:47512] [DMG]                                    CommandId = 0x3,
[1770357727.834] [47502:47512] [DMG]                            },
[1770357727.834] [47502:47512] [DMG]
[1770357727.834] [47502:47512] [DMG]                            CommandFields =
[1770357727.834] [47502:47512] [DMG]                            {
[1770357727.835] [47502:47512] [DMG]                                    0x0 = [
[1770357727.835] [47502:47512] [DMG]                                                    0x30, 0x82, 0x01, 0xcb, 0x30, 0x82, 0x01, 0x71, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x56, 0xad, 0x82, 0x22, 0xad, 0x94, 0x5b, 0x64, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x30, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x0f, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x54, 0x65, 0x73, 0x74, 0x20, 0x50, 0x41, 0x41, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x41, 0x9a, 0x93, 0x15, 0xc2, 0x17, 0x3e, 0x0c, 0x8c, 0x87, 0x6d, 0x03, 0xcc, 0xfc, 0x94, 0x48, 0x52, 0x64, 0x7f, 0x7f, 0xec, 0x5e, 0x50, 0x82, 0xf4, 0x05, 0x99, 0x28, 0xec, 0xa8, 0x94, 0xc5, 0x94, 0x15, 0x13, 0x09, 0xac, 0x63, 0x1e, 0x4c, 0xb0, 0x33, 0x92, 0xaf, 0x68, 0x4b, 0x0b, 0xaf, 0xb7, 0xe6, 0x5b, 0x3b, 0x81, 0x62, 0xc2, 0xf5, 0x2b, 0xf9, 0x31, 0xb8, 0xe7, 0x7a, 0xaa, 0x82, 0xa3, 0x66, 0x30, 0x64, 0x30, 0x12, 0x06, 0x03, 0x55, 0x1d, 0x
[1770357727.835] [47502:47512] [DMG]                                    ] (463 bytes)
[1770357727.835] [47502:47512] [DMG]                            },
[1770357727.836] [47502:47512] [DMG]                    },
[1770357727.836] [47502:47512] [DMG]
[1770357727.836] [47502:47512] [DMG]            },
[1770357727.836] [47502:47512] [DMG]
[1770357727.836] [47502:47512] [DMG]    ],
[1770357727.836] [47502:47512] [DMG]
[1770357727.836] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357727.836] [47502:47512] [DMG] },
[1770357727.837] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770357727.837] [47502:47512] [CTL] Received certificate chain from the device
[1770357727.837] [47502:47512] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1770357727.837] [47502:47512] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1770357727.837] [47502:47512] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1770357727.837] [47502:47512] [CTL] Sending request for DAC certificate
[1770357727.837] [47502:47512] [CTL] Sending Certificate Chain request to 0xffff7400f680 device
[1770357727.837] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357727.837] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357727.838] [47502:47512] [EM] <<< [E:55095i S:47210 M:200676522] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770357727.839] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357727.839] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357728.023] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357728.413] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357728.414] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357728.806] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357728.807] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357729.002] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357729.003] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357729.003] [47502:47512] [EM] >>> [E:55095i S:47210 M:201358437] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:557)
[1770357729.003] [47502:47512] [EM] Found matching exchange: 55095i, Delegate: 0xffff74008ae8
[1770357729.003] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357729.003] [47502:47512] [DMG] InvokeResponseMessage =
[1770357729.004] [47502:47512] [DMG] {
[1770357729.004] [47502:47512] [DMG]    suppressResponse = false,
[1770357729.004] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357729.004] [47502:47512] [DMG]    [
[1770357729.004] [47502:47512] [DMG]            InvokeResponseIB =
[1770357729.004] [47502:47512] [DMG]            {
[1770357729.004] [47502:47512] [DMG]                    CommandDataIB =
[1770357729.004] [47502:47512] [DMG]                    {
[1770357729.004] [47502:47512] [DMG]                            CommandPathIB =
[1770357729.005] [47502:47512] [DMG]                            {
[1770357729.005] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357729.005] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357729.005] [47502:47512] [DMG]                                    CommandId = 0x3,
[1770357729.005] [47502:47512] [DMG]                            },
[1770357729.005] [47502:47512] [DMG]
[1770357729.005] [47502:47512] [DMG]                            CommandFields =
[1770357729.006] [47502:47512] [DMG]                            {
[1770357729.006] [47502:47512] [DMG]                                    0x0 = [
[1770357729.006] [47502:47512] [DMG]                                                    0x30, 0x82, 0x01, 0xe9, 0x30, 0x82, 0x01, 0x8e, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x1e, 0x06, 0x7f, 0x3b, 0xfe, 0xcd, 0xd8, 0x13, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x53, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x44, 0x41, 0x43, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x2f, 0x30, 0x78, 0x38, 0x30, 0x30, 0x34, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x30, 0x34, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x50, 0x41, 0x38, 0xef, 0x31, 0xc9, 0xdd, 0x16, 0x0e, 0xb4, 0x6c, 0x6c, 0x17, 0x11, 0x4f, 0x9d, 0x72, 0x88, 0x40, 0x80, 0x1f, 0x73, 0xbb, 0x9b, 0x5a, 0x2c, 0x51, 0x91, 0xc9, 0xb2, 0x06, 0x63, 0x01, 0x9d, 0x94, 0x76, 0xd1, 0x93, 0x1b, 0x
[1770357729.007] [47502:47512] [DMG]                                    ] (493 bytes)
[1770357729.007] [47502:47512] [DMG]                            },
[1770357729.007] [47502:47512] [DMG]                    },
[1770357729.007] [47502:47512] [DMG]
[1770357729.007] [47502:47512] [DMG]            },
[1770357729.007] [47502:47512] [DMG]
[1770357729.008] [47502:47512] [DMG]    ],
[1770357729.008] [47502:47512] [DMG]
[1770357729.008] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357729.008] [47502:47512] [DMG] },
[1770357729.008] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770357729.008] [47502:47512] [CTL] Received certificate chain from the device
[1770357729.009] [47502:47512] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1770357729.009] [47502:47512] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1770357729.009] [47502:47512] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1770357729.009] [47502:47512] [CTL] Sending Attestation Request to the device.
[1770357729.009] [47502:47512] [CTL] Sending Attestation request to 0xffff7400f680 device
[1770357729.009] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357729.009] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357729.010] [47502:47512] [EM] <<< [E:55096i S:47210 M:200676523] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770357729.011] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357729.011] [47502:47512] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770357729.011] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357729.292] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357729.783] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357729.783] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357730.076] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357730.076] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357730.368] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357730.369] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357730.369] [47502:47512] [EM] >>> [E:55096i S:47210 M:201358438] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[1770357730.369] [47502:47512] [EM] Found matching exchange: 55096i, Delegate: 0xffff7400aae8
[1770357730.369] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357730.370] [47502:47512] [DMG] InvokeResponseMessage =
[1770357730.370] [47502:47512] [DMG] {
[1770357730.370] [47502:47512] [DMG]    suppressResponse = false,
[1770357730.370] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357730.370] [47502:47512] [DMG]    [
[1770357730.370] [47502:47512] [DMG]            InvokeResponseIB =
[1770357730.370] [47502:47512] [DMG]            {
[1770357730.370] [47502:47512] [DMG]                    CommandDataIB =
[1770357730.370] [47502:47512] [DMG]                    {
[1770357730.370] [47502:47512] [DMG]                            CommandPathIB =
[1770357730.371] [47502:47512] [DMG]                            {
[1770357730.371] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357730.371] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357730.371] [47502:47512] [DMG]                                    CommandId = 0x1,
[1770357730.371] [47502:47512] [DMG]                            },
[1770357730.371] [47502:47512] [DMG]
[1770357730.371] [47502:47512] [DMG]                            CommandFields =
[1770357730.372] [47502:47512] [DMG]                            {
[1770357730.372] [47502:47512] [DMG]                                    0x0 = [
[1770357730.372] [47502:47512] [DMG]                                                    0x15, 0x31, 0x01, 0x1b, 0x02, 0x30, 0x82, 0x02, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x02, 0x08, 0x30, 0x82, 0x02, 0x04, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x82, 0x01, 0x70, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x01, 0x61, 0x04, 0x82, 0x01, 0x5d, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0xf1, 0xff, 0x36, 0x02, 0x05, 0x00, 0x80, 0x05, 0x01, 0x80, 0x05, 0x02, 0x80, 0x05, 0x03, 0x80, 0x05, 0x04, 0x80, 0x05, 0x05, 0x80, 0x05, 0x06, 0x80, 0x05, 0x07, 0x80, 0x05, 0x08, 0x80, 0x05, 0x09, 0x80, 0x05, 0x0a, 0x80, 0x05, 0x0b, 0x80, 0x05, 0x0c, 0x80, 0x05, 0x0d, 0x80, 0x05, 0x0e, 0x80, 0x05, 0x0f, 0x80, 0x05, 0x10, 0x80, 0x05, 0x11, 0x80, 0x05, 0x12, 0x80, 0x05, 0x13, 0x80, 0x05, 0x14, 0x80, 0x05, 0x15, 0x80, 0x05, 0x16, 0x80, 0x05, 0x17, 0x80, 0x05, 0x18, 0x80, 0x05, 0x19, 0x80, 0x05, 0x1a, 0x80, 0x05, 0x1b, 0x80, 0x05, 0x1c, 0x80, 0x05, 0x1d, 0x80, 0x05, 0x1e, 0x80, 0x05, 0x1f, 0x80, 0x05, 0x20, 0x80, 0x05, 0x21, 0x80, 0x05, 0x22, 0x80, 0x05, 0x23, 0x80, 0x05, 0x24, 0x80, 0x05, 0x25, 0x80, 0x05, 0x26, 0x80, 0x05, 0x27, 0x80, 0x05, 0x28, 0x80, 0x05, 0x29, 0x80, 0x05, 0x2a, 0x80, 0x05, 0x2b, 0x80, 0x05, 0x2c, 0x80, 0x05, 0x2d, 0x80, 0x05, 0x2e, 0x80, 0x05, 0x2f, 0x80, 0x05, 0x30, 0x80, 0x05, 0x31, 0x80, 0x05, 0x32, 0x80, 0x05, 0x33, 0x80, 0x05, 0x34, 0x80, 0x05, 0x35, 0x80, 0x05, 0x36, 0x80, 0x05, 0x37, 0x80, 0x05, 0x38, 0x80, 0x05, 0x39, 0x80, 0x05, 0x3a, 0x80, 0x05, 0x3b, 0x80, 0x05, 0x3c, 0x80, 0x05, 0x3d, 0x80, 0x05, 0x3e, 0x80, 0x05, 0x3f, 0x80, 0x05, 0x40, 0x80, 0x05, 0x41, 0x80, 0x05, 0x42, 0x80, 0x05, 0x43, 0x80, 0x
[1770357730.372] [47502:47512] [DMG]                                    ] (583 bytes)
[1770357730.372] [47502:47512] [DMG]                                    0x1 = [
[1770357730.372] [47502:47512] [DMG]                                                    0x8f, 0xd2, 0x76, 0x26, 0xe3, 0x78, 0x69, 0x4b, 0x00, 0xeb, 0xe7, 0xd2, 0xbe, 0xee, 0x5b, 0xb1, 0x27, 0x63, 0x35, 0x3f, 0x94, 0xda, 0x5b, 0x18, 0xa9, 0x68, 0x0f, 0x95, 0xfa, 0x70, 0x04, 0xf3, 0x29, 0x9a, 0x91, 0xf0, 0x48, 0x6a, 0xd6, 0x59, 0x89, 0xbd, 0xb7, 0x9d, 0x5a, 0x4b, 0x87, 0x8d, 0x83, 0x19, 0x4a, 0x4c, 0xf7, 0xbe, 0x10, 0xbf, 0x6a, 0x92, 0x6e, 0xd4, 0xc8, 0x19, 0xc5, 0x2a,
[1770357730.373] [47502:47512] [DMG]                                    ] (64 bytes)
[1770357730.373] [47502:47512] [DMG]                            },
[1770357730.373] [47502:47512] [DMG]                    },
[1770357730.373] [47502:47512] [DMG]
[1770357730.373] [47502:47512] [DMG]            },
[1770357730.373] [47502:47512] [DMG]
[1770357730.373] [47502:47512] [DMG]    ],
[1770357730.373] [47502:47512] [DMG]
[1770357730.373] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357730.373] [47502:47512] [DMG] },
[1770357730.373] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1770357730.374] [47502:47512] [CTL] Received Attestation Information from the device
[1770357730.374] [47502:47512] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1770357730.374] [47502:47512] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[1770357730.374] [47502:47512] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1770357730.374] [47502:47512] [CTL] Performing next commissioning step 'AttestationVerification'
[1770357730.374] [47502:47512] [CTL] Verifying Device Attestation information received from the device
[1770357730.401] [47502:47512] [-] Device candidate DAC chain details:
[1770357730.401] [47502:47512] [-] --> DAC's VID: 0xFFF1, PID: 0x8004
[1770357730.401] [47502:47512] [-] ==== DAC certificate considered (493 bytes) ====
[1770357730.401] [47502:47512] [-] -----BEGIN CERTIFICATE-----
[1770357730.401] [47502:47512] [-] MIIB6TCCAY6gAwIBAgIIHgZ/O/7N2BMwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770357730.401] [47502:47512] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
[1770357730.401] [47502:47512] [-] RjEwIBcNMjIwMjA1MDAwMDAwWhgPOTk5OTEyMzEyMzU5NTlaMFMxJTAjBgNVBAMM
[1770357730.401] [47502:47512] [-] HE1hdHRlciBEZXYgREFDIDB4RkZGMS8weDgwMDQxFDASBgorBgEEAYKifAIBDARG
[1770357730.401] [47502:47512] [-] RkYxMRQwEgYKKwYBBAGConwCAgwEODAwNDBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770357730.401] [47502:47512] [-] A0IABFBBOO8xyd0WDrRsbBcRT51yiECAH3O7m1osUZHJsgZjAZ2UdtGTG5P/R/Qy
[1770357730.401] [47502:47512] [-] VjeQNdIpYgt+IQ5ZLyZDfS1XYgWjYDBeMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/
[1770357730.401] [47502:47512] [-] BAQDAgeAMB0GA1UdDgQWBBSgpxwqX3RFIFsSpijKtxZFui1ecjAfBgNVHSMEGDAW
[1770357730.401] [47502:47512] [-] gBRjVA5H9kscONE4hKRi0WwZXY/7PDAKBggqhkjOPQQDAgNJADBGAiEA53nri7vY
[1770357730.401] [47502:47512] [-] uiho03v8Og4zhwPb5FxUCYyK5KOETvXIK1sCIQCQ52srg3OSqylAORBA9k3HjFMB
[1770357730.401] [47502:47512] [-] rJ0IZk/20BBK/pj8gA==
[1770357730.401] [47502:47512] [-] -----END CERTIFICATE-----
[1770357730.404] [47502:47512] [-] --> DAC certificate SKID: A0:A7:1C:2A:5F:74:45:20:5B:12:A6:28:CA:B7:16:45:BA:2D:5E:72
[1770357730.406] [47502:47512] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770357730.406] [47502:47512] [-] ==== PAI certificate considered (463 bytes) ====
[1770357730.406] [47502:47512] [-] -----BEGIN CERTIFICATE-----
[1770357730.406] [47502:47512] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770357730.406] [47502:47512] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMjAyMDUw
[1770357730.406] [47502:47512] [-] MDAwMDBaGA85OTk5MTIzMTIzNTk1OVowPTElMCMGA1UEAwwcTWF0dGVyIERldiBQ
[1770357730.407] [47502:47512] [-] QUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZGRjEwWTATBgcqhkjO
[1770357730.407] [47502:47512] [-] PQIBBggqhkjOPQMBBwNCAARBmpMVwhc+DIyHbQPM/JRIUmR/f+xeUIL0BZko7KiU
[1770357730.407] [47502:47512] [-] xZQVEwmsYx5MsDOSr2hLC6+35ls7gWLC9Sv5MbjneqqCo2YwZDASBgNVHRMBAf8E
[1770357730.407] [47502:47512] [-] CDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUY1QOR/ZLHDjROISk
[1770357730.407] [47502:47512] [-] YtFsGV2P+zwwHwYDVR0jBBgwFoAUav0idx9RH+y/FkGXZxDc3DGhcX4wCgYIKoZI
[1770357730.407] [47502:47512] [-] zj0EAwIDSAAwRQIhALLvJ/Sa6bUPuR7qyUxNC9u415KcbLiPrOUpNo0SBUwMAiBl
[1770357730.407] [47502:47512] [-] Xckrhr2QmIKmxiF3uCXX0F7b58Ivn+pxIg5+pwP4kQ==
[1770357730.407] [47502:47512] [-] -----END CERTIFICATE-----
[1770357730.409] [47502:47512] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770357730.411] [47502:47512] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770357730.422] [47502:47512] [-] ==== PAA certificate considered (449 bytes) ====
[1770357730.422] [47502:47512] [-] -----BEGIN CERTIFICATE-----
[1770357730.422] [47502:47512] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770357730.422] [47502:47512] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMTA2Mjgx
[1770357730.423] [47502:47512] [-] NDIzNDNaGA85OTk5MTIzMTIzNTk1OVowMDEYMBYGA1UEAwwPTWF0dGVyIFRlc3Qg
[1770357730.423] [47502:47512] [-] UEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770357730.423] [47502:47512] [-] A0IABLbLY3KIfyko9brIGqnZOuJDHK2p154kL2UXfvnO2TKijs0Duq9qj8oYShpQ
[1770357730.423] [47502:47512] [-] NUKWDUU/MD8fGUIddR6Pjxqam3WjZjBkMBIGA1UdEwEB/wQIMAYBAf8CAQEwDgYD
[1770357730.423] [47502:47512] [-] VR0PAQH/BAQDAgEGMB0GA1UdDgQWBBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAfBgNV
[1770357730.423] [47502:47512] [-] HSMEGDAWgBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAKBggqhkjOPQQDAgNHADBEAiBQ
[1770357730.423] [47502:47512] [-] qoAC9NkyqaAFOPZTaK0P/8jvu8m+t9pWmDXPmqdRDgIgI7rI/g8j51RFtlM5CBpH
[1770357730.423] [47502:47512] [-] mUkpxyqvChVI1A0DTVFLJd4=
[1770357730.423] [47502:47512] [-] -----END CERTIFICATE-----
[1770357730.425] [47502:47512] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770357730.428] [47502:47512] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770357730.442] [47502:47512] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770357730.444] [47502:47512] [-] Device certification declaration details:
[1770357730.444] [47502:47512] [-] --> VID: 0xFFF1
[1770357730.444] [47502:47512] [-] --> Device type ID: 0x0000_0016
[1770357730.444] [47502:47512] [-] --> Certification type: 0 (Development and testing)
[1770357730.444] [47502:47512] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1770357730.444] [47502:47512] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1770357730.444] [47502:47512] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1770357730.444] [47502:47512] [CTL] Verifying the device's DAC chain revocation status
[1770357730.444] [47502:47512] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770357730.444] [47502:47512] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1770357730.444] [47502:47512] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1770357730.444] [47502:47512] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1770357730.444] [47502:47512] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1770357730.445] [47502:47512] [CTL] Sending CSR request to 0xffff7400f680 device
[1770357730.445] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357730.445] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357730.445] [47502:47512] [EM] <<< [E:55097i S:47210 M:200676524] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770357730.446] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357730.446] [47502:47512] [CTL] Sent CSR request, waiting for the CSR
[1770357730.446] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357730.754] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357731.051] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357731.051] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357731.341] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357731.341] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357731.342] [47502:47512] [EM] >>> [E:55097i S:47210 M:201358439] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1770357731.342] [47502:47512] [EM] Found matching exchange: 55097i, Delegate: 0xffff74008ae8
[1770357731.342] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357731.342] [47502:47512] [DMG] InvokeResponseMessage =
[1770357731.342] [47502:47512] [DMG] {
[1770357731.342] [47502:47512] [DMG]    suppressResponse = false,
[1770357731.342] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357731.343] [47502:47512] [DMG]    [
[1770357731.343] [47502:47512] [DMG]            InvokeResponseIB =
[1770357731.343] [47502:47512] [DMG]            {
[1770357731.343] [47502:47512] [DMG]                    CommandDataIB =
[1770357731.343] [47502:47512] [DMG]                    {
[1770357731.343] [47502:47512] [DMG]                            CommandPathIB =
[1770357731.343] [47502:47512] [DMG]                            {
[1770357731.343] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357731.343] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357731.343] [47502:47512] [DMG]                                    CommandId = 0x5,
[1770357731.344] [47502:47512] [DMG]                            },
[1770357731.344] [47502:47512] [DMG]
[1770357731.344] [47502:47512] [DMG]                            CommandFields =
[1770357731.344] [47502:47512] [DMG]                            {
[1770357731.344] [47502:47512] [DMG]                                    0x0 = [
[1770357731.344] [47502:47512] [DMG]                                                    0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xab, 0x25, 0xe0, 0xf8, 0x13, 0xb1, 0xb3, 0xe0, 0x49, 0xff, 0x83, 0x2e, 0x08, 0xd1, 0xc5, 0x86, 0x69, 0x82, 0x92, 0x32, 0xdd, 0xb7, 0xeb, 0x3a, 0x96, 0x64, 0x34, 0xcc, 0x68, 0x5f, 0x7e, 0x63, 0x19, 0x15, 0x0f, 0x6a, 0xd7, 0xcb, 0x73, 0xd2, 0xab, 0x72, 0x1a, 0xc0, 0x41, 0x29, 0xcd, 0x29, 0x23, 0x8c, 0x28, 0xd4, 0x31, 0xb7, 0x84, 0xae, 0x5b, 0x34, 0xc9, 0x08, 0x0c, 0x52, 0xa0, 0x19, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x21, 0x00, 0xee, 0x64, 0x44, 0x64, 0x91, 0x41, 0xbb, 0xb8, 0x45, 0x48, 0x0c, 0x25, 0x98, 0x19, 0x15, 0x86, 0x05, 0x64, 0x70, 0x5b, 0xd9, 0x49, 0xcb, 0x3d, 0x46, 0x8c, 0xa1, 0x41, 0x6b, 0x14, 0xe7, 0x08, 0x02, 0x20, 0x18, 0xc3, 0x89, 0x78, 0x48, 0x44, 0x8b, 0xc9, 0x8e, 0x55, 0xe3, 0x2b, 0x7d, 0xcb, 0x6a, 0xb6, 0xda, 0x29, 0x6c, 0x8e, 0xd5, 0x86, 0x00, 0xfd, 0xc4, 0x57, 0x44, 0x59, 0xab, 0x54, 0xae, 0x24, 0x30, 0x02, 0x20, 0x9a, 0xed, 0xd7, 0x02, 0x2d, 0xa3, 0x35, 0xda, 0x44, 0x41, 0x48, 0x7a, 0xe9, 0x0d, 0xf4, 0x64, 0x48, 0xfd, 0x9c, 0xa1, 0x94, 0x38, 0x29, 0x5f, 0x76, 0x08, 0x49, 0xde, 0x88, 0x41, 0xd4, 0x13, 0x18,
[1770357731.345] [47502:47512] [DMG]                                    ] (261 bytes)
[1770357731.345] [47502:47512] [DMG]                                    0x1 = [
[1770357731.345] [47502:47512] [DMG]                                                    0xc4, 0x69, 0x2d, 0xb9, 0x03, 0x7a, 0xb7, 0xdc, 0xe0, 0xdc, 0x01, 0x0d, 0xa2, 0x12, 0x88, 0x16, 0xcd, 0xa0, 0x07, 0x97, 0xc5, 0x35, 0x53, 0xb0, 0xc8, 0xf7, 0x71, 0xdd, 0x67, 0xe3, 0x17, 0xfa, 0x87, 0x76, 0xb1, 0x33, 0x26, 0x06, 0x14, 0xe1, 0x61, 0x54, 0x2b, 0x43, 0x54, 0xf3, 0xb6, 0x71, 0xa4, 0xca, 0xb4, 0x0d, 0x6c, 0xf4, 0x11, 0x4e, 0xa2, 0x13, 0x5d, 0x2a, 0x77, 0x30, 0xdd, 0x2a,
[1770357731.345] [47502:47512] [DMG]                                    ] (64 bytes)
[1770357731.345] [47502:47512] [DMG]                            },
[1770357731.345] [47502:47512] [DMG]                    },
[1770357731.346] [47502:47512] [DMG]
[1770357731.346] [47502:47512] [DMG]            },
[1770357731.346] [47502:47512] [DMG]
[1770357731.346] [47502:47512] [DMG]    ],
[1770357731.346] [47502:47512] [DMG]
[1770357731.346] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357731.346] [47502:47512] [DMG] },
[1770357731.346] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1770357731.346] [47502:47512] [CTL] Received certificate signing request from the device
[1770357731.346] [47502:47512] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1770357731.346] [47502:47512] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1770357731.347] [47502:47512] [CTL] Performing next commissioning step 'ValidateCSR'
[1770357731.356] [47502:47512] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1770357731.356] [47502:47512] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1770357731.357] [47502:47512] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1770357731.357] [47502:47512] [CTL] Getting certificate chain for the device from the issuer
[1770357731.362] [47502:47512] [CTL] Verifying Certificate Signing Request
[1770357731.366] [47502:47512] [CTL] Generating NOC
[1770357731.367] [47502:47512] [CTL] Providing certificate chain to the commissioner
[1770357731.367] [47502:47512] [CTL] Received callback from the CA for NOC Chain generation. Status src/controller/ExampleOperationalCredentialsIssuer.cpp:409: Success
[1770357731.367] [47502:47512] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1770357731.367] [47502:47512] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1770357731.367] [47502:47512] [CTL] Sending root certificate to the device
[1770357731.368] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357731.368] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357731.368] [47502:47512] [EM] <<< [E:55098i S:47210 M:200676525] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1770357731.369] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357731.369] [47502:47512] [CTL] Sent root certificate to the device
[1770357731.370] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357731.729] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357731.924] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357731.927] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357731.928] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357731.928] [47502:47512] [EM] >>> [E:55098i S:47210 M:201358440] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770357731.928] [47502:47512] [EM] Found matching exchange: 55098i, Delegate: 0xffff7400aae8
[1770357731.928] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357731.929] [47502:47512] [DMG] InvokeResponseMessage =
[1770357731.929] [47502:47512] [DMG] {
[1770357731.929] [47502:47512] [DMG]    suppressResponse = false,
[1770357731.929] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357731.929] [47502:47512] [DMG]    [
[1770357731.929] [47502:47512] [DMG]            InvokeResponseIB =
[1770357731.929] [47502:47512] [DMG]            {
[1770357731.930] [47502:47512] [DMG]                    CommandStatusIB =
[1770357731.930] [47502:47512] [DMG]                    {
[1770357731.930] [47502:47512] [DMG]                            CommandPathIB =
[1770357731.930] [47502:47512] [DMG]                            {
[1770357731.930] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357731.930] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357731.930] [47502:47512] [DMG]                                    CommandId = 0xb,
[1770357731.931] [47502:47512] [DMG]                            },
[1770357731.931] [47502:47512] [DMG]
[1770357731.931] [47502:47512] [DMG]                            StatusIB =
[1770357731.931] [47502:47512] [DMG]                            {
[1770357731.931] [47502:47512] [DMG]                                    status = 0x00 (SUCCESS),
[1770357731.932] [47502:47512] [DMG]                            },
[1770357731.932] [47502:47512] [DMG]
[1770357731.932] [47502:47512] [DMG]                    },
[1770357731.932] [47502:47512] [DMG]
[1770357731.932] [47502:47512] [DMG]            },
[1770357731.932] [47502:47512] [DMG]
[1770357731.932] [47502:47512] [DMG]    ],
[1770357731.932] [47502:47512] [DMG]
[1770357731.932] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357731.933] [47502:47512] [DMG] },
[1770357731.933] [47502:47512] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1770357731.933] [47502:47512] [CTL] Device confirmed that it has received the root certificate
[1770357731.933] [47502:47512] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1770357731.933] [47502:47512] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1770357731.933] [47502:47512] [CTL] Performing next commissioning step 'SendNOC'
[1770357731.933] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357731.933] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357731.934] [47502:47512] [EM] <<< [E:55099i S:47210 M:200676526] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1770357731.934] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357731.935] [47502:47512] [CTL] Sent operational certificate to the device
[1770357731.935] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357732.314] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357732.606] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357732.801] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357732.805] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357732.805] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357732.806] [47502:47512] [EM] >>> [E:55099i S:47210 M:201358441] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770357732.806] [47502:47512] [EM] Found matching exchange: 55099i, Delegate: 0xffff74008ae8
[1770357732.806] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357732.806] [47502:47512] [DMG] InvokeResponseMessage =
[1770357732.806] [47502:47512] [DMG] {
[1770357732.807] [47502:47512] [DMG]    suppressResponse = false,
[1770357732.807] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357732.807] [47502:47512] [DMG]    [
[1770357732.807] [47502:47512] [DMG]            InvokeResponseIB =
[1770357732.807] [47502:47512] [DMG]            {
[1770357732.807] [47502:47512] [DMG]                    CommandDataIB =
[1770357732.807] [47502:47512] [DMG]                    {
[1770357732.808] [47502:47512] [DMG]                            CommandPathIB =
[1770357732.808] [47502:47512] [DMG]                            {
[1770357732.808] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357732.808] [47502:47512] [DMG]                                    ClusterId = 0x3e,
[1770357732.808] [47502:47512] [DMG]                                    CommandId = 0x8,
[1770357732.809] [47502:47512] [DMG]                            },
[1770357732.809] [47502:47512] [DMG]
[1770357732.809] [47502:47512] [DMG]                            CommandFields =
[1770357732.809] [47502:47512] [DMG]                            {
[1770357732.809] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357732.809] [47502:47512] [DMG]                                    0x1 = 1 (unsigned),
[1770357732.809] [47502:47512] [DMG]                            },
[1770357732.810] [47502:47512] [DMG]                    },
[1770357732.810] [47502:47512] [DMG]
[1770357732.810] [47502:47512] [DMG]            },
[1770357732.810] [47502:47512] [DMG]
[1770357732.810] [47502:47512] [DMG]    ],
[1770357732.810] [47502:47512] [DMG]
[1770357732.810] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357732.810] [47502:47512] [DMG] },
[1770357732.811] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1770357732.811] [47502:47512] [CTL] Device returned status 0 on receiving the NOC
[1770357732.811] [47502:47512] [CTL] Operational credentials provisioned on device 0xffff7400f680
[1770357732.811] [47502:47512] [TOO] Secure Pairing Success
[1770357732.811] [47502:47512] [TOO] CASE establishment successful
[1770357732.811] [47502:47512] [CTL] Successfully finished commissioning step 'SendNOC'
[1770357732.811] [47502:47512] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1770357732.812] [47502:47512] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1770357732.812] [47502:47512] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1770357732.812] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357732.812] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357732.812] [47502:47512] [EM] <<< [E:55100i S:47210 M:200676527] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[1770357732.813] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357732.814] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357733.093] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357733.291] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357733.291] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357733.292] [47502:47512] [EM] >>> [E:55100i S:47210 M:201358442] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770357733.292] [47502:47512] [EM] Found matching exchange: 55100i, Delegate: 0xffff7400aae8
[1770357733.292] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357733.292] [47502:47512] [DMG] InvokeResponseMessage =
[1770357733.292] [47502:47512] [DMG] {
[1770357733.292] [47502:47512] [DMG]    suppressResponse = false,
[1770357733.292] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357733.292] [47502:47512] [DMG]    [
[1770357733.292] [47502:47512] [DMG]            InvokeResponseIB =
[1770357733.293] [47502:47512] [DMG]            {
[1770357733.293] [47502:47512] [DMG]                    CommandDataIB =
[1770357733.293] [47502:47512] [DMG]                    {
[1770357733.293] [47502:47512] [DMG]                            CommandPathIB =
[1770357733.293] [47502:47512] [DMG]                            {
[1770357733.293] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357733.293] [47502:47512] [DMG]                                    ClusterId = 0x31,
[1770357733.293] [47502:47512] [DMG]                                    CommandId = 0x5,
[1770357733.293] [47502:47512] [DMG]                            },
[1770357733.294] [47502:47512] [DMG]
[1770357733.294] [47502:47512] [DMG]                            CommandFields =
[1770357733.294] [47502:47512] [DMG]                            {
[1770357733.294] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357733.294] [47502:47512] [DMG]                                    0x2 = 0 (unsigned),
[1770357733.294] [47502:47512] [DMG]                            },
[1770357733.294] [47502:47512] [DMG]                    },
[1770357733.294] [47502:47512] [DMG]
[1770357733.294] [47502:47512] [DMG]            },
[1770357733.295] [47502:47512] [DMG]
[1770357733.295] [47502:47512] [DMG]    ],
[1770357733.295] [47502:47512] [DMG]
[1770357733.295] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357733.295] [47502:47512] [DMG] },
[1770357733.295] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1770357733.296] [47502:47512] [CTL] Received NetworkConfig response, networkingStatus=0
[1770357733.296] [47502:47512] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1770357733.296] [47502:47512] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1770357733.296] [47502:47512] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1770357733.296] [47502:47512] [CTL] Arming failsafe (94 seconds)
[1770357733.296] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357733.296] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357733.297] [47502:47512] [EM] <<< [E:55101i S:47210 M:200676528] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770357733.298] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357733.298] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357733.679] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357733.682] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357733.683] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357733.683] [47502:47512] [EM] >>> [E:55101i S:47210 M:201358443] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770357733.683] [47502:47512] [EM] Found matching exchange: 55101i, Delegate: 0xffff74008ae8
[1770357733.684] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357733.684] [47502:47512] [DMG] InvokeResponseMessage =
[1770357733.684] [47502:47512] [DMG] {
[1770357733.684] [47502:47512] [DMG]    suppressResponse = false,
[1770357733.684] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357733.684] [47502:47512] [DMG]    [
[1770357733.684] [47502:47512] [DMG]            InvokeResponseIB =
[1770357733.684] [47502:47512] [DMG]            {
[1770357733.684] [47502:47512] [DMG]                    CommandDataIB =
[1770357733.684] [47502:47512] [DMG]                    {
[1770357733.684] [47502:47512] [DMG]                            CommandPathIB =
[1770357733.685] [47502:47512] [DMG]                            {
[1770357733.685] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357733.685] [47502:47512] [DMG]                                    ClusterId = 0x30,
[1770357733.685] [47502:47512] [DMG]                                    CommandId = 0x1,
[1770357733.685] [47502:47512] [DMG]                            },
[1770357733.685] [47502:47512] [DMG]
[1770357733.685] [47502:47512] [DMG]                            CommandFields =
[1770357733.685] [47502:47512] [DMG]                            {
[1770357733.685] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357733.685] [47502:47512] [DMG]                                    0x1 = "" (0 chars),
[1770357733.685] [47502:47512] [DMG]                            },
[1770357733.686] [47502:47512] [DMG]                    },
[1770357733.686] [47502:47512] [DMG]
[1770357733.686] [47502:47512] [DMG]            },
[1770357733.686] [47502:47512] [DMG]
[1770357733.686] [47502:47512] [DMG]    ],
[1770357733.686] [47502:47512] [DMG]
[1770357733.686] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357733.686] [47502:47512] [DMG] },
[1770357733.686] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770357733.686] [47502:47512] [CTL] Received ArmFailSafe response errorCode=0
[1770357733.686] [47502:47512] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1770357733.687] [47502:47512] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1770357733.687] [47502:47512] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1770357733.687] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357733.687] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357733.687] [47502:47512] [EM] <<< [E:55102i S:47210 M:200676529] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1770357733.688] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357733.689] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357733.972] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16389
[1770357735.145] [47502:47509] [DL] Indication received, conn = 0xffff7c028da0
[1770357735.146] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16391
[1770357735.146] [47502:47512] [EM] >>> [E:55102i S:47210 M:201358444] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1770357735.146] [47502:47512] [EM] Found matching exchange: 55102i, Delegate: 0xffff7400aae8
[1770357735.146] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357735.146] [47502:47512] [DMG] InvokeResponseMessage =
[1770357735.147] [47502:47512] [DMG] {
[1770357735.147] [47502:47512] [DMG]    suppressResponse = false,
[1770357735.147] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357735.147] [47502:47512] [DMG]    [
[1770357735.147] [47502:47512] [DMG]            InvokeResponseIB =
[1770357735.147] [47502:47512] [DMG]            {
[1770357735.147] [47502:47512] [DMG]                    CommandDataIB =
[1770357735.147] [47502:47512] [DMG]                    {
[1770357735.147] [47502:47512] [DMG]                            CommandPathIB =
[1770357735.148] [47502:47512] [DMG]                            {
[1770357735.148] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357735.148] [47502:47512] [DMG]                                    ClusterId = 0x31,
[1770357735.148] [47502:47512] [DMG]                                    CommandId = 0x7,
[1770357735.148] [47502:47512] [DMG]                            },
[1770357735.149] [47502:47512] [DMG]
[1770357735.149] [47502:47512] [DMG]                            CommandFields =
[1770357735.149] [47502:47512] [DMG]                            {
[1770357735.149] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357735.149] [47502:47512] [DMG]                                    0x2 = NULL
[1770357735.149] [47502:47512] [DMG]                            },
[1770357735.149] [47502:47512] [DMG]                    },
[1770357735.150] [47502:47512] [DMG]
[1770357735.150] [47502:47512] [DMG]            },
[1770357735.150] [47502:47512] [DMG]
[1770357735.150] [47502:47512] [DMG]    ],
[1770357735.150] [47502:47512] [DMG]
[1770357735.150] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357735.150] [47502:47512] [DMG] },
[1770357735.150] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1770357735.150] [47502:47512] [CTL] Received ConnectNetwork response, networkingStatus=0
[1770357735.150] [47502:47512] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1770357735.150] [47502:47512] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'
[1770357735.151] [47502:47512] [CTL] Performing next commissioning step 'kEvictPreviousCaseSessions'
[1770357735.151] [47502:47512] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1770357735.151] [47502:47512] [CTL] Successfully finished commissioning step 'kEvictPreviousCaseSessions'
[1770357735.151] [47502:47512] [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'
[1770357735.151] [47502:47512] [CTL] Performing next commissioning step 'kFindOperationalForStayActive'
[1770357735.151] [47502:47512] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770357735.151] [47502:47512] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770357735.151] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1770357735.152] [47502:47512] [DIS] Lookup started for C10D5CDE8EFEE20A-00000000000008CA
[1770357735.153] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357735.352] [47502:47512] [DIS] Checking node lookup status for C10D5CDE8EFEE20A-00000000000008CA after 200 ms
[1770357736.670] [47502:47512] [DIS] SRV record already actively processed.
[1770357736.673] [47502:47512] [DIS] Lookup clearing interface for non LL address
[1770357736.674] [47502:47512] [DIS] UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e%eth0]:5540: new best score: 5 (for C10D5CDE8EFEE20A-00000000000008CA)
[1770357736.674] [47502:47512] [DIS] Checking node lookup status for C10D5CDE8EFEE20A-00000000000008CA after 1523 ms
[1770357736.674] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540 while in state 2
[1770357736.674] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1770357736.675] [47502:47512] [IN] SecureSession[0xffff7402ad50]: Allocated Type:2 LSID:47211
[1770357736.675] [47502:47512] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1770357736.679] [47502:47512] [EM] <<< [E:55103i S:0 M:206666174] (U) Msg TX from B2F2CCFB722D7E9F to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1770357736.679] [47502:47512] [EM] ??1 [E:55103i S:0 M:206666174] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2205ms from now [State:Idle II:2000 AI:2000 AT:4000]
[1770357736.680] [47502:47512] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1770357736.680] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1770357736.874] [47502:47512] [EM] >>> [E:55103i S:0 M:157823080 (Ack:206666174)] (U) Msg RX from 0:0000000000000000 [0000] to B2F2CCFB722D7E9F --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770357736.874] [47502:47512] [EM] Found matching exchange: 55103i, Delegate: 0xffff74013fb8
[1770357736.874] [47502:47512] [EM] Rxd Ack; Removing MessageCounter:206666174 from Retrans Table on exchange 55103i
[1770357736.966] [47502:47512] [EM] >>> [E:55103i S:0 M:157823081 (Ack:206666174)] (U) Msg RX from 0:0000000000000000 [0000] to B2F2CCFB722D7E9F --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:752)
[1770357736.966] [47502:47512] [EM] Found matching exchange: 55103i, Delegate: 0xffff74013fb8
[1770357736.966] [47502:47512] [EM] CHIP MessageCounter:206666174 not in RetransTable on exchange 55103i
[1770357736.966] [47502:47512] [SC] Received Sigma2 msg
[1770357736.966] [47502:47512] [SC] Found MRP parameters in the message
[1770357736.979] [47502:47512] [SC] Peer <00000000000008CA, 1> assigned session ID 553
[1770357736.979] [47502:47512] [SC] Sending Sigma3
[1770357736.981] [47502:47512] [EM] <<< [E:55103i S:0 M:206666175 (Ack:157823081)] (U) Msg TX from B2F2CCFB722D7E9F to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1770357736.982] [47502:47512] [EM] ??1 [E:55103i S:0 M:206666175] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2566ms from now [State:Active II:2000 AI:2000 AT:4000]
[1770357736.982] [47502:47512] [SC] Sent Sigma3 msg
[1770357737.217] [47502:47512] [EM] >>> [E:55103i S:0 M:157823082 (Ack:206666175)] (U) Msg RX from 0:0000000000000000 [0000] to B2F2CCFB722D7E9F --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770357737.217] [47502:47512] [EM] Found matching exchange: 55103i, Delegate: 0xffff74013fb8
[1770357737.218] [47502:47512] [EM] Rxd Ack; Removing MessageCounter:206666175 from Retrans Table on exchange 55103i
[1770357737.238] [47502:47512] [EM] >>> [E:55103i S:0 M:157823083 (Ack:206666175)] (U) Msg RX from 0:0000000000000000 [0000] to B2F2CCFB722D7E9F --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1770357737.238] [47502:47512] [EM] Found matching exchange: 55103i, Delegate: 0xffff74013fb8
[1770357737.238] [47502:47512] [EM] CHIP MessageCounter:206666175 not in RetransTable on exchange 55103i
[1770357737.238] [47502:47512] [SC] Success status report received. Session was established
[1770357737.244] [47502:47512] [SC] SecureSession[0xffff7402ad50, LSID:47211]: State change 'kEstablishing' --> 'kActive'
[1770357737.245] [47502:47512] [IN] SecureSession[0xffff7402ad50]: Activated - Type:2 LSID:47211
[1770357737.245] [47502:47512] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:47211 PSID:553!
[1770357737.245] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1770357737.245] [47502:47512] [CTL] Successfully finished commissioning step 'kFindOperationalForStayActive'
[1770357737.245] [47502:47512] [CTL] Commissioning stage next step: 'kFindOperationalForStayActive' -> 'ICDSendStayActive'
[1770357737.245] [47502:47512] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1770357737.245] [47502:47512] [CTL] Skipping kICDSendStayActive
[1770357737.245] [47502:47512] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1770357737.245] [47502:47512] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'kFindOperationalForCommissioningComplete'
[1770357737.245] [47502:47512] [CTL] Performing next commissioning step 'kFindOperationalForCommissioningComplete'
[1770357737.245] [47502:47512] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1770357737.245] [47502:47512] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770357737.245] [47502:47512] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1770357737.245] [47502:47512] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1770357737.245] [47502:47512] [CTL] Successfully finished commissioning step 'kFindOperationalForCommissioningComplete'
[1770357737.245] [47502:47512] [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'
[1770357737.246] [47502:47512] [CTL] Performing next commissioning step 'SendComplete'
[1770357737.246] [47502:47512] [DMG] ICR moving to [AddingComm]
[1770357737.246] [47502:47512] [DMG] ICR moving to [AddedComma]
[1770357737.246] [47502:47512] [EM] <<< [E:55104i S:47211 M:177032213] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [E20A] [UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1770357737.246] [47502:47512] [EM] ??1 [E:55104i S:47211 M:177032213] (S) Msg Retransmission to 1:00000000000008CA scheduled for 2686ms from now [State:Active II:2000 AI:2000 AT:4000]
[1770357737.247] [47502:47512] [DMG] ICR moving to [AwaitingRe]
[1770357737.247] [47502:47512] [EM] <<< [E:55103i S:0 M:206666176 (Ack:157823083)] (U) Msg TX from B2F2CCFB722D7E9F to 0:0000000000000000 [0000] [UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1770357737.247] [47502:47512] [EM] Flushed pending ack for MessageCounter:157823083 on exchange 55103i
[1770357737.248] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 32792
[1770357737.381] [47502:47512] [EM] >>> [E:55104i S:47211 M:226020702 (Ack:177032213)] (S) Msg RX from 1:00000000000008CA [E20A] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1770357737.381] [47502:47512] [EM] Found matching exchange: 55104i, Delegate: 0xffff74008ae8
[1770357737.382] [47502:47512] [EM] Rxd Ack; Removing MessageCounter:177032213 from Retrans Table on exchange 55104i
[1770357737.382] [47502:47512] [DMG] ICR moving to [ResponseRe]
[1770357737.382] [47502:47512] [DMG] InvokeResponseMessage =
[1770357737.382] [47502:47512] [DMG] {
[1770357737.382] [47502:47512] [DMG]    suppressResponse = false,
[1770357737.382] [47502:47512] [DMG]    InvokeResponseIBs =
[1770357737.382] [47502:47512] [DMG]    [
[1770357737.382] [47502:47512] [DMG]            InvokeResponseIB =
[1770357737.383] [47502:47512] [DMG]            {
[1770357737.383] [47502:47512] [DMG]                    CommandDataIB =
[1770357737.383] [47502:47512] [DMG]                    {
[1770357737.383] [47502:47512] [DMG]                            CommandPathIB =
[1770357737.383] [47502:47512] [DMG]                            {
[1770357737.383] [47502:47512] [DMG]                                    EndpointId = 0x0,
[1770357737.384] [47502:47512] [DMG]                                    ClusterId = 0x30,
[1770357737.384] [47502:47512] [DMG]                                    CommandId = 0x5,
[1770357737.384] [47502:47512] [DMG]                            },
[1770357737.384] [47502:47512] [DMG]
[1770357737.384] [47502:47512] [DMG]                            CommandFields =
[1770357737.384] [47502:47512] [DMG]                            {
[1770357737.384] [47502:47512] [DMG]                                    0x0 = 0 (unsigned),
[1770357737.385] [47502:47512] [DMG]                                    0x1 = "" (0 chars),
[1770357737.385] [47502:47512] [DMG]                            },
[1770357737.385] [47502:47512] [DMG]                    },
[1770357737.385] [47502:47512] [DMG]
[1770357737.385] [47502:47512] [DMG]            },
[1770357737.385] [47502:47512] [DMG]
[1770357737.385] [47502:47512] [DMG]    ],
[1770357737.386] [47502:47512] [DMG]
[1770357737.386] [47502:47512] [DMG]    InteractionModelRevision = 12
[1770357737.386] [47502:47512] [DMG] },
[1770357737.386] [47502:47512] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1770357737.386] [47502:47512] [CTL] Received CommissioningComplete response, errorCode=0
[1770357737.386] [47502:47512] [CTL] Successfully finished commissioning step 'SendComplete'
[1770357737.386] [47502:47512] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1770357737.386] [47502:47512] [CTL] Performing next commissioning step 'Cleanup'
[1770357737.387] [47502:47512] [CTL] Successfully finished commissioning step 'Cleanup'
[1770357737.387] [47502:47512] [DIS] Closing all BLE connections
[1770357737.387] [47502:47512] [IN] Clearing BLE pending packets.
[1770357737.388] [47502:47512] [BLE] Auto-closing end point's BLE connection.
[1770357737.388] [47502:47512] [DL] Closing BLE GATT connection (con 0xffff7c028da0)
[1770357737.388] [47502:47509] [DL] Close BLE connection: peer=D2:88:D5:4D:90:CA
[1770357737.485] [47502:47512] [IN] SecureSession[0xffff74003cf0]: MarkForEviction Type:1 LSID:47210
[1770357737.485] [47502:47512] [SC] SecureSession[0xffff74003cf0, LSID:47210]: State change 'kActive' --> 'kPendingEviction'
[1770357737.485] [47502:47512] [IN] SecureSession[0xffff74003cf0]: Released - Type:1 LSID:47210
[1770357737.486] [47502:47512] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1770357737.486] [47502:47512] [TOO] Device commissioning completed with success
[1770357737.486] [47502:47512] [DMG] ICR moving to [AwaitingDe]
[1770357737.487] [47502:47512] [EM] <<< [E:55104i S:47211 M:177032214 (Ack:226020702)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [E20A] [UDP:[fd98:42ee:f6b4:1:2fc8:95d5:4f3e:447e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1770357737.487] [47502:47512] [EM] Flushed pending ack for MessageCounter:226020702 on exchange 55104i
[1770357737.487] [47502:47512] [DL] HandlePlatformSpecificBLEEvent 16390
[1770357737.487] [47502:47512] [BLE] No endpoint for unsubscribe complete
[1770357737.487] [47502:47509] [DL] BLE connection closed: conn=0xffff7c028da0
[1770357737.489] [47502:47502] [CTL] Shutting down the commissioner
[1770357737.489] [47502:47502] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770357737.490] [47502:47502] [CTL] Shutting down the controller
[1770357737.490] [47502:47502] [IN] Expiring all sessions for fabric 0x1!!
[1770357737.490] [47502:47502] [IN] SecureSession[0xffff7402ad50]: MarkForEviction Type:2 LSID:47211
[1770357737.490] [47502:47502] [SC] SecureSession[0xffff7402ad50, LSID:47211]: State change 'kActive' --> 'kPendingEviction'
[1770357737.490] [47502:47502] [IN] SecureSession[0xffff7402ad50]: Released - Type:2 LSID:47211
[1770357737.490] [47502:47502] [FP] Forgetting fabric 0x1
[1770357737.490] [47502:47502] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770357737.491] [47502:47502] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770357737.491] [47502:47502] [TS] Reverted Last Known Good Time to previous value
[1770357737.491] [47502:47502] [CTL] Shutting down the commissioner
[1770357737.491] [47502:47502] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770357737.491] [47502:47502] [CTL] Shutting down the controller
[1770357737.491] [47502:47502] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770357737.492] [47502:47502] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770357737.492] [47502:47502] [FP] Shutting down FabricTable
[1770357737.492] [47502:47502] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770357737.493] [47502:47502] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770357737.493] [47502:47502] [TS] Reverted Last Known Good Time to previous value
[1770357737.505] [47502:47502] [DL] Wrote settings to /tmp/chip_counters.ini
[1770357737.505] [47502:47502] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770357737.505] [47502:47502] [DL] Inet Layer shutdown
[1770357737.505] [47502:47502] [DL] BLE Layer shutdown
[1770357737.509] [47502:47502] [DL] WiFi-PAF Layer shutdown
[1770357737.509] [47502:47502] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770357737.509] [47502:47502] [DL] NFCCommissioningMgr shutdown
[1770357737.509] [47502:47502] [DL] System Layer shutdown
```