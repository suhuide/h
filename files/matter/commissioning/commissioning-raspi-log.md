```c
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 77822335 3087 --paa-trust-store-path /home/ubuntu/paa-root-certs
[1788155573.246] [547289:547289] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1788155573.247] [547289:547289] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1788155573.253] [547289:547289] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1788155573.253] [547289:547289] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1788155573.254] [547289:547289] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1788155573.259] [547289:547289] [DL] Wrote settings to /tmp/chip_counters.ini
[1788155573.259] [547289:547289] [DL] NVS set: chip-counters/reboot-count = 2 (0x2)
[1788155573.260] [547289:547289] [DL] Got Ethernet interface: eth0
[1788155573.260] [547289:547289] [DL] Found the primary Ethernet interface:eth0
[1788155573.261] [547289:547289] [DL] Got WiFi interface: wlan0
[1788155573.261] [547289:547289] [DL] Failed to reset WiFi statistic counts
[1788155573.261] [547289:547289] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1788155573.261] [547289:547289] [IN] UDP::Init bind&listen port=0
[1788155573.261] [547289:547289] [IN] UDP::Init bound to port=39701
[1788155573.261] [547289:547289] [IN] UDP::Init bind&listen port=0
[1788155573.262] [547289:547289] [IN] UDP::Init bound to port=49703
[1788155573.262] [547289:547289] [IN] BLEBase::Init - setting/overriding transport
[1788155573.262] [547289:547289] [IN] WiFiPAFBase::Init - setting/overriding transport
[1788155573.262] [547289:547289] [IN] TransportMgr initialized
[1788155573.262] [547289:547289] [FP] Initializing FabricTable from persistent storage
[1788155573.262] [547289:547289] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1788155573.264] [547289:547289] [FP] Fabric index 0x1 was retrieved from storage. Compressed FabricId 0x30230980DA7DCAF4, FabricId 0x0000000000000001, NodeId 0x000000000001B669, VendorId 0xFFF1
[1788155573.268] [547289:547289] [DMG] Ember attribute persistence requires setting up
[1788155573.268] [547289:547289] [ZCL] Using ZAP configuration...
[1788155573.272] [547289:547289] [CTL] System State Initialized...
[1788155573.583] [547289:547289] [CTL] Setting attestation nonce to random value
[1788155573.583] [547289:547289] [CTL] Setting CSR nonce to random value
[1788155573.583] [547289:547289] [IN] UDP::Init bind&listen port=5550
[1788155573.583] [547289:547289] [IN] UDP::Init bound to port=5550
[1788155573.583] [547289:547289] [IN] UDP::Init bind&listen port=5550
[1788155573.583] [547289:547289] [IN] UDP::Init bound to port=5550
[1788155573.583] [547289:547289] [IN] TransportMgr initialized
[1788155573.584] [547289:547373] [DL] CHIP task running
[1788155573.584] [547289:547373] [CTL] Setting attestation nonce to random value
[1788155573.585] [547289:547373] [CTL] Setting CSR nonce to random value
[1788155573.586] [547289:547373] [CTL] Generating NOC
[1788155573.587] [547289:547373] [FP] Validating NOC chain
[1788155573.589] [547289:547373] [FP] NOC chain validation successful
[1788155573.589] [547289:547373] [FP] Updated fabric at index: 0x1, Node ID: 0x000000000001B669
[1788155573.589] [547289:547373] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1788155573.589] [547289:547373] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1788155573.589] [547289:547373] [TS] Retaining current Last Known Good Time
[1788155573.591] [547289:547373] [FP] Metadata for Fabric 0x1 persisted to storage.
[1788155573.594] [547289:547373] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1788155573.597] [547289:547373] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 30230980DA7DCAF4)
[1788155573.597] [547289:547373] [IN] UDP::Init bind&listen port=5551
[1788155573.597] [547289:547373] [IN] UDP::Init bound to port=5551
[1788155573.597] [547289:547373] [IN] UDP::Init bind&listen port=5551
[1788155573.597] [547289:547373] [IN] UDP::Init bound to port=5551
[1788155573.597] [547289:547373] [IN] TransportMgr initialized
[1788155573.620] [547289:547373] [CTL] Setting thread operational dataset from parameters
[1788155573.620] [547289:547373] [CTL] Setting attestation nonce to random value
[1788155573.620] [547289:547373] [CTL] Setting CSR nonce to random value
[1788155573.620] [547289:547373] [CTL] Commission called for node ID 0x00000000000008CA
[1788155573.667] [547289:547313] [BLE] BLE removing known devices
[1788155575.497] [547289:547313] [BLE] BLE initiating scan
[1788155575.549] [547289:547373] [BLE] ChipDeviceScanner has started scanning!
[1788155575.549] [547289:547373] [DL] Long dispatch time: 1930 ms, for event type 3
[1788155575.556] [547289:547313] [BLE] Device 2E:34:41:02:30:3D does not look like a CHIP device.
[1788155575.559] [547289:547313] [BLE] Device 15:8A:66:3C:20:AA does not look like a CHIP device.
[1788155575.561] [547289:547313] [BLE] Device 15:63:6D:97:84:0D does not look like a CHIP device.
[1788155575.564] [547289:547313] [BLE] Device 23:0A:AE:8C:EA:F3 does not look like a CHIP device.
[1788155575.566] [547289:547313] [BLE] Device 73:27:ED:76:E1:FE does not look like a CHIP device.
[1788155575.569] [547289:547313] [BLE] Device 41:42:D7:87:B6:45 does not look like a CHIP device.
[1788155575.586] [547289:547313] [BLE] Device 4C:3C:09:4C:FF:46 does not look like a CHIP device.
[1788155575.593] [547289:547313] [BLE] Device 5F:64:49:99:54:7C does not look like a CHIP device.
[1788155575.602] [547289:547313] [BLE] Device 10:05:A6:29:0A:8C does not look like a CHIP device.
[1788155575.604] [547289:547313] [BLE] New device scanned: CD:3A:AA:3B:8B:66
[1788155575.604] [547289:547313] [BLE] Device discriminator match. Attempting to connect.
[1788155575.611] [547289:547313] [BLE] ChipDeviceScanner has stopped scanning!
[1788155575.817] [547289:547313] [DL] ConnectDevice complete
[1788155575.817] [547289:547313] [BLE] New device connected: CD:3A:AA:3B:8B:66
[1788155577.588] [547289:547313] [DL] CHIP service found
[1788155577.588] [547289:547313] [DL] Valid C1 characteristic found
[1788155577.588] [547289:547313] [DL] Valid C2 characteristic found
[1788155577.588] [547289:547313] [DL] New BLE connection: conn=0xffff8405ef20 device=CD:3A:AA:3B:8B:66 path=/org/bluez/hci0/dev_CD_3A_AA_3B_8B_66
[1788155577.588] [547289:547373] [DIS] Closing all BLE connections
[1788155577.589] [547289:547373] [IN] BleConnectionComplete: endPoint 0xaaaad9174f80
[1788155577.590] [547289:547373] [IN] SecureSession[0xffff90002c60]: Allocated Type:1 LSID:44800
[1788155577.590] [547289:547373] [SC] Assigned local session key ID 44800
[1788155577.590] [547289:547373] [EM] <<< [E:850i S:0 M:111788296] (U) Msg TX from C33AEEA911976EF6 to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1788155577.590] [547289:547373] [IN] Message appended to BLE send queue
[1788155577.590] [547289:547373] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1788155578.546] [547289:547373] [BLE] subscribe complete, ep = 0xaaaad9174f80
[1788155578.547] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155578.547] [547289:547373] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1788155578.547] [547289:547373] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1788155578.547] [547289:547373] [BLE] local and remote recv window size = 5
[1788155578.548] [547289:547373] [IN] BLE EndPoint 0xaaaad9174f80 Connection Complete
[1788155578.743] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155578.743] [547289:547373] [EM] >>> [E:850i S:0 M:52138051] (U) Msg RX from 0:0000000000000000 [0000] to C33AEEA911976EF6 --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:154)
[1788155578.744] [547289:547373] [EM] Found matching exchange: 850i, Delegate: 0xffff9000de80
[1788155578.744] [547289:547373] [SC] Received PBKDF param response
[1788155578.744] [547289:547373] [SC] Peer assigned session ID 61772
[1788155578.744] [547289:547373] [SC] Found MRP parameters in the message
[1788155578.756] [547289:547373] [EM] <<< [E:850i S:0 M:111788297] (U) Msg TX from C33AEEA911976EF6 to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1788155578.757] [547289:547373] [SC] Sent spake2p msg1
[1788155578.937] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155578.938] [547289:547373] [EM] >>> [E:850i S:0 M:52138052] (U) Msg RX from 0:0000000000000000 [0000] to C33AEEA911976EF6 --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1788155578.938] [547289:547373] [EM] Found matching exchange: 850i, Delegate: 0xffff9000de80
[1788155578.938] [547289:547373] [SC] Received spake2p msg2
[1788155578.940] [547289:547373] [EM] <<< [E:850i S:0 M:111788298] (U) Msg TX from C33AEEA911976EF6 to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1788155578.941] [547289:547373] [SC] Sent spake2p msg3
[1788155579.132] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155579.132] [547289:547373] [EM] >>> [E:850i S:0 M:52138053] (U) Msg RX from 0:0000000000000000 [0000] to C33AEEA911976EF6 --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1788155579.132] [547289:547373] [EM] Found matching exchange: 850i, Delegate: 0xffff9000de80
[1788155579.133] [547289:547373] [SC] SecureSession[0xffff90002c60, LSID:44800]: State change 'kEstablishing' --> 'kActive'
[1788155579.133] [547289:547373] [IN] SecureSession[0xffff90002c60]: Activated - Type:1 LSID:44800
[1788155579.133] [547289:547373] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:44800 PSID:61772!
[1788155579.133] [547289:547373] [CTL] Remote device completed SPAKE2+ handshake
[1788155579.133] [547289:547373] [TOO] Pairing Success
[1788155579.133] [547289:547373] [TOO] PASE establishment successful
[1788155579.133] [547289:547373] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1788155579.133] [547289:547373] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1788155579.133] [547289:547373] [TOO] Starting commissioning stage 'ReadCommissioningInfo'
[1788155579.133] [547289:547373] [CTL] Sending read requests for commissioning information
[1788155579.134] [547289:547373] [DMG] SendReadRequest ReadClient[0xffff9000fe90]: Sending Read Request
[1788155579.134] [547289:547373] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1788155579.134] [547289:547373] [EM] <<< [E:851i S:44800 M:103044093] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:136)
[1788155579.135] [547289:547373] [DMG] MoveToState ReadClient[0xffff9000fe90]: Moving to [AwaitingIn]
[1788155579.329] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155579.521] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155579.522] [547289:547373] [EM] >>> [E:851i S:44800 M:162761933] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:253)
[1788155579.522] [547289:547373] [EM] Found matching exchange: 851i, Delegate: 0xffff9000fea0
[1788155579.522] [547289:547373] [DMG] ReportDataMessage =
[1788155579.522] [547289:547373] [DMG] {
[1788155579.522] [547289:547373] [DMG]  AttributeReportIBs =
[1788155579.523] [547289:547373] [DMG]  [
[1788155579.523] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.523] [547289:547373] [DMG]          {
[1788155579.523] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.523] [547289:547373] [DMG]                  {
[1788155579.523] [547289:547373] [DMG]                          DataVersion = 0xdb74ef94,
[1788155579.523] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.523] [547289:547373] [DMG]                          {
[1788155579.524] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.524] [547289:547373] [DMG]                                  Cluster = 0x28,
[1788155579.524] [547289:547373] [DMG]                                  Attribute = 0x0000_0004,
[1788155579.524] [547289:547373] [DMG]                          }
[1788155579.524] [547289:547373] [DMG]
[1788155579.524] [547289:547373] [DMG]                          Data = 12293 (unsigned),
[1788155579.524] [547289:547373] [DMG]                  },
[1788155579.524] [547289:547373] [DMG]
[1788155579.524] [547289:547373] [DMG]          },
[1788155579.525] [547289:547373] [DMG]
[1788155579.525] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.525] [547289:547373] [DMG]          {
[1788155579.525] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.525] [547289:547373] [DMG]                  {
[1788155579.525] [547289:547373] [DMG]                          DataVersion = 0xdb74ef94,
[1788155579.525] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.525] [547289:547373] [DMG]                          {
[1788155579.525] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.525] [547289:547373] [DMG]                                  Cluster = 0x28,
[1788155579.526] [547289:547373] [DMG]                                  Attribute = 0x0000_0002,
[1788155579.526] [547289:547373] [DMG]                          }
[1788155579.526] [547289:547373] [DMG]
[1788155579.526] [547289:547373] [DMG]                          Data = 5274 (unsigned),
[1788155579.526] [547289:547373] [DMG]                  },
[1788155579.526] [547289:547373] [DMG]
[1788155579.526] [547289:547373] [DMG]          },
[1788155579.526] [547289:547373] [DMG]
[1788155579.526] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.526] [547289:547373] [DMG]          {
[1788155579.526] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.527] [547289:547373] [DMG]                  {
[1788155579.527] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.527] [547289:547373] [DMG]                          {
[1788155579.527] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.527] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.527] [547289:547373] [DMG]                                  Attribute = 0x0000_000C,
[1788155579.527] [547289:547373] [DMG]                          }
[1788155579.527] [547289:547373] [DMG]
[1788155579.527] [547289:547373] [DMG]                          StatusIB =
[1788155579.527] [547289:547373] [DMG]                          {
[1788155579.528] [547289:547373] [DMG]                                  status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1788155579.528] [547289:547373] [DMG]                          },
[1788155579.528] [547289:547373] [DMG]
[1788155579.528] [547289:547373] [DMG]                  },
[1788155579.528] [547289:547373] [DMG]
[1788155579.528] [547289:547373] [DMG]          },
[1788155579.528] [547289:547373] [DMG]
[1788155579.528] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.528] [547289:547373] [DMG]          {
[1788155579.528] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.528] [547289:547373] [DMG]                  {
[1788155579.528] [547289:547373] [DMG]                          DataVersion = 0xb887987a,
[1788155579.528] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.528] [547289:547373] [DMG]                          {
[1788155579.529] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.529] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.529] [547289:547373] [DMG]                                  Attribute = 0x0000_0003,
[1788155579.529] [547289:547373] [DMG]                          }
[1788155579.529] [547289:547373] [DMG]
[1788155579.529] [547289:547373] [DMG]                          Data = 0 (unsigned),
[1788155579.529] [547289:547373] [DMG]                  },
[1788155579.529] [547289:547373] [DMG]
[1788155579.529] [547289:547373] [DMG]          },
[1788155579.529] [547289:547373] [DMG]
[1788155579.529] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.529] [547289:547373] [DMG]          {
[1788155579.529] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.530] [547289:547373] [DMG]                  {
[1788155579.530] [547289:547373] [DMG]                          DataVersion = 0xb887987a,
[1788155579.530] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.530] [547289:547373] [DMG]                          {
[1788155579.530] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.530] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.530] [547289:547373] [DMG]                                  Attribute = 0x0000_0002,
[1788155579.530] [547289:547373] [DMG]                          }
[1788155579.530] [547289:547373] [DMG]
[1788155579.530] [547289:547373] [DMG]                          Data = 0 (unsigned),
[1788155579.530] [547289:547373] [DMG]                  },
[1788155579.530] [547289:547373] [DMG]
[1788155579.530] [547289:547373] [DMG]          },
[1788155579.530] [547289:547373] [DMG]
[1788155579.531] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.531] [547289:547373] [DMG]          {
[1788155579.531] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.531] [547289:547373] [DMG]                  {
[1788155579.531] [547289:547373] [DMG]                          DataVersion = 0xb887987a,
[1788155579.531] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.531] [547289:547373] [DMG]                          {
[1788155579.531] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.531] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.531] [547289:547373] [DMG]                                  Attribute = 0x0000_0001,
[1788155579.531] [547289:547373] [DMG]                          }
[1788155579.531] [547289:547373] [DMG]
[1788155579.531] [547289:547373] [DMG]                          Data =
[1788155579.532] [547289:547373] [DMG]                          {
[1788155579.532] [547289:547373] [DMG]                                  0x0 = 60 (unsigned),
[1788155579.532] [547289:547373] [DMG]                                  0x1 = 900 (unsigned),
[1788155579.532] [547289:547373] [DMG]                          },
[1788155579.532] [547289:547373] [DMG]                  },
[1788155579.532] [547289:547373] [DMG]
[1788155579.532] [547289:547373] [DMG]          },
[1788155579.532] [547289:547373] [DMG]
[1788155579.532] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.532] [547289:547373] [DMG]          {
[1788155579.532] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.532] [547289:547373] [DMG]                  {
[1788155579.533] [547289:547373] [DMG]                          DataVersion = 0xb887987a,
[1788155579.533] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.533] [547289:547373] [DMG]                          {
[1788155579.533] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.533] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.533] [547289:547373] [DMG]                                  Attribute = 0x0000_0000,
[1788155579.533] [547289:547373] [DMG]                          }
[1788155579.533] [547289:547373] [DMG]
[1788155579.533] [547289:547373] [DMG]                          Data = 0 (unsigned),
[1788155579.533] [547289:547373] [DMG]                  },
[1788155579.533] [547289:547373] [DMG]
[1788155579.533] [547289:547373] [DMG]          },
[1788155579.534] [547289:547373] [DMG]
[1788155579.534] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.534] [547289:547373] [DMG]          {
[1788155579.534] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.534] [547289:547373] [DMG]                  {
[1788155579.534] [547289:547373] [DMG]                          DataVersion = 0xb887987a,
[1788155579.534] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.534] [547289:547373] [DMG]                          {
[1788155579.534] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.534] [547289:547373] [DMG]                                  Cluster = 0x30,
[1788155579.534] [547289:547373] [DMG]                                  Attribute = 0x0000_0004,
[1788155579.534] [547289:547373] [DMG]                          }
[1788155579.534] [547289:547373] [DMG]
[1788155579.534] [547289:547373] [DMG]                          Data = true,
[1788155579.534] [547289:547373] [DMG]                  },
[1788155579.534] [547289:547373] [DMG]
[1788155579.534] [547289:547373] [DMG]          },
[1788155579.534] [547289:547373] [DMG]
[1788155579.534] [547289:547373] [DMG]  ],
[1788155579.534] [547289:547373] [DMG]
[1788155579.534] [547289:547373] [DMG]  SuppressResponse = true,
[1788155579.534] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155579.534] [547289:547373] [DMG] }
[1788155579.535] [547289:547373] [DMG] SendReadRequest ReadClient[0xffff9000fe90]: Sending Read Request
[1788155579.535] [547289:547373] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1788155579.535] [547289:547373] [EM] <<< [E:852i S:44800 M:103044094] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:112)
[1788155579.536] [547289:547373] [DMG] MoveToState ReadClient[0xffff9000fe90]: Moving to [AwaitingIn]
[1788155579.719] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155579.720] [547289:547373] [EM] >>> [E:852i S:44800 M:162761934] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:208)
[1788155579.720] [547289:547373] [EM] Found matching exchange: 852i, Delegate: 0xffff9000fea0
[1788155579.720] [547289:547373] [DMG] ReportDataMessage =
[1788155579.720] [547289:547373] [DMG] {
[1788155579.720] [547289:547373] [DMG]  AttributeReportIBs =
[1788155579.720] [547289:547373] [DMG]  [
[1788155579.720] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.720] [547289:547373] [DMG]          {
[1788155579.720] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.720] [547289:547373] [DMG]                  {
[1788155579.720] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.721] [547289:547373] [DMG]                          {
[1788155579.721] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.721] [547289:547373] [DMG]                                  Cluster = 0x46,
[1788155579.721] [547289:547373] [DMG]                                  Attribute = 0x0000_0002,
[1788155579.721] [547289:547373] [DMG]                          }
[1788155579.721] [547289:547373] [DMG]
[1788155579.721] [547289:547373] [DMG]                          StatusIB =
[1788155579.721] [547289:547373] [DMG]                          {
[1788155579.721] [547289:547373] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788155579.721] [547289:547373] [DMG]                          },
[1788155579.721] [547289:547373] [DMG]
[1788155579.721] [547289:547373] [DMG]                  },
[1788155579.722] [547289:547373] [DMG]
[1788155579.722] [547289:547373] [DMG]          },
[1788155579.722] [547289:547373] [DMG]
[1788155579.722] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.722] [547289:547373] [DMG]          {
[1788155579.722] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.722] [547289:547373] [DMG]                  {
[1788155579.722] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.722] [547289:547373] [DMG]                          {
[1788155579.722] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.722] [547289:547373] [DMG]                                  Cluster = 0x46,
[1788155579.722] [547289:547373] [DMG]                                  Attribute = 0x0000_0001,
[1788155579.723] [547289:547373] [DMG]                          }
[1788155579.723] [547289:547373] [DMG]
[1788155579.723] [547289:547373] [DMG]                          StatusIB =
[1788155579.723] [547289:547373] [DMG]                          {
[1788155579.723] [547289:547373] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788155579.723] [547289:547373] [DMG]                          },
[1788155579.723] [547289:547373] [DMG]
[1788155579.723] [547289:547373] [DMG]                  },
[1788155579.723] [547289:547373] [DMG]
[1788155579.723] [547289:547373] [DMG]          },
[1788155579.723] [547289:547373] [DMG]
[1788155579.724] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.724] [547289:547373] [DMG]          {
[1788155579.724] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.724] [547289:547373] [DMG]                  {
[1788155579.724] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.724] [547289:547373] [DMG]                          {
[1788155579.724] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.724] [547289:547373] [DMG]                                  Cluster = 0x46,
[1788155579.724] [547289:547373] [DMG]                                  Attribute = 0x0000_0000,
[1788155579.724] [547289:547373] [DMG]                          }
[1788155579.724] [547289:547373] [DMG]
[1788155579.724] [547289:547373] [DMG]                          StatusIB =
[1788155579.725] [547289:547373] [DMG]                          {
[1788155579.725] [547289:547373] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788155579.725] [547289:547373] [DMG]                          },
[1788155579.725] [547289:547373] [DMG]
[1788155579.725] [547289:547373] [DMG]                  },
[1788155579.725] [547289:547373] [DMG]
[1788155579.725] [547289:547373] [DMG]          },
[1788155579.725] [547289:547373] [DMG]
[1788155579.725] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.725] [547289:547373] [DMG]          {
[1788155579.725] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.725] [547289:547373] [DMG]                  {
[1788155579.725] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.726] [547289:547373] [DMG]                          {
[1788155579.726] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.726] [547289:547373] [DMG]                                  Cluster = 0x46,
[1788155579.726] [547289:547373] [DMG]                                  Attribute = 0x0000_0007,
[1788155579.726] [547289:547373] [DMG]                          }
[1788155579.726] [547289:547373] [DMG]
[1788155579.726] [547289:547373] [DMG]                          StatusIB =
[1788155579.726] [547289:547373] [DMG]                          {
[1788155579.726] [547289:547373] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788155579.726] [547289:547373] [DMG]                          },
[1788155579.726] [547289:547373] [DMG]
[1788155579.726] [547289:547373] [DMG]                  },
[1788155579.726] [547289:547373] [DMG]
[1788155579.726] [547289:547373] [DMG]          },
[1788155579.727] [547289:547373] [DMG]
[1788155579.727] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.727] [547289:547373] [DMG]          {
[1788155579.727] [547289:547373] [DMG]                  AttributeStatusIB =
[1788155579.727] [547289:547373] [DMG]                  {
[1788155579.727] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.727] [547289:547373] [DMG]                          {
[1788155579.727] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.727] [547289:547373] [DMG]                                  Cluster = 0x46,
[1788155579.727] [547289:547373] [DMG]                                  Attribute = 0x0000_0006,
[1788155579.727] [547289:547373] [DMG]                          }
[1788155579.727] [547289:547373] [DMG]
[1788155579.727] [547289:547373] [DMG]                          StatusIB =
[1788155579.727] [547289:547373] [DMG]                          {
[1788155579.727] [547289:547373] [DMG]                                  status = 0xc3 (UNSUPPORTED_CLUSTER),
[1788155579.727] [547289:547373] [DMG]                          },
[1788155579.727] [547289:547373] [DMG]
[1788155579.727] [547289:547373] [DMG]                  },
[1788155579.727] [547289:547373] [DMG]
[1788155579.727] [547289:547373] [DMG]          },
[1788155579.727] [547289:547373] [DMG]
[1788155579.727] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.727] [547289:547373] [DMG]          {
[1788155579.727] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.727] [547289:547373] [DMG]                  {
[1788155579.727] [547289:547373] [DMG]                          DataVersion = 0xaaeb83ec,
[1788155579.727] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.727] [547289:547373] [DMG]                          {
[1788155579.727] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.728] [547289:547373] [DMG]                                  Cluster = 0x31,
[1788155579.728] [547289:547373] [DMG]                                  Attribute = 0x0000_0003,
[1788155579.728] [547289:547373] [DMG]                          }
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]                          Data = 20 (unsigned),
[1788155579.728] [547289:547373] [DMG]                  },
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]          },
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]          AttributeReportIB =
[1788155579.728] [547289:547373] [DMG]          {
[1788155579.728] [547289:547373] [DMG]                  AttributeDataIB =
[1788155579.728] [547289:547373] [DMG]                  {
[1788155579.728] [547289:547373] [DMG]                          DataVersion = 0xaaeb83ec,
[1788155579.728] [547289:547373] [DMG]                          AttributePathIB =
[1788155579.728] [547289:547373] [DMG]                          {
[1788155579.728] [547289:547373] [DMG]                                  Endpoint = 0x0,
[1788155579.728] [547289:547373] [DMG]                                  Cluster = 0x31,
[1788155579.728] [547289:547373] [DMG]                                  Attribute = 0x0000_FFFC,
[1788155579.728] [547289:547373] [DMG]                          }
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]                          Data = 2 (unsigned),
[1788155579.728] [547289:547373] [DMG]                  },
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]          },
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]  ],
[1788155579.728] [547289:547373] [DMG]
[1788155579.728] [547289:547373] [DMG]  SuppressResponse = true,
[1788155579.728] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155579.729] [547289:547373] [DMG] }
[1788155579.729] [547289:547373] [CTL] Ignoring failure to read IsCommissioningWithoutPower: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1788155579.729] [547289:547373] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1788155579.730] [547289:547373] [SVR] OnReadCommissioningInfo - vendorId=0x149A productId=0x3005
[1788155579.730] [547289:547373] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1788155579.730] [547289:547373] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1788155579.730] [547289:547373] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1788155579.730] [547289:547373] [CTL] Performing next commissioning step 'ArmFailSafe'
[1788155579.730] [547289:547373] [TOO] Starting commissioning stage 'ArmFailSafe'
[1788155579.730] [547289:547373] [CTL] Arming failsafe (60 seconds)
[1788155579.730] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155579.730] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155579.730] [547289:547373] [EM] <<< [E:853i S:44800 M:103044095] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1788155579.730] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155580.010] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155580.010] [547289:547373] [EM] >>> [E:853i S:44800 M:162761935] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788155580.010] [547289:547373] [EM] Found matching exchange: 853i, Delegate: 0xffff90014458
[1788155580.010] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155580.011] [547289:547373] [DMG] InvokeResponseMessage =
[1788155580.011] [547289:547373] [DMG] {
[1788155580.011] [547289:547373] [DMG]  suppressResponse = false,
[1788155580.011] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155580.011] [547289:547373] [DMG]  [
[1788155580.011] [547289:547373] [DMG]          InvokeResponseIB =
[1788155580.011] [547289:547373] [DMG]          {
[1788155580.011] [547289:547373] [DMG]                  CommandDataIB =
[1788155580.011] [547289:547373] [DMG]                  {
[1788155580.011] [547289:547373] [DMG]                          CommandPathIB =
[1788155580.011] [547289:547373] [DMG]                          {
[1788155580.011] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155580.011] [547289:547373] [DMG]                                  ClusterId = 0x30,
[1788155580.012] [547289:547373] [DMG]                                  CommandId = 0x1,
[1788155580.012] [547289:547373] [DMG]                          },
[1788155580.012] [547289:547373] [DMG]
[1788155580.012] [547289:547373] [DMG]                          CommandFields =
[1788155580.012] [547289:547373] [DMG]                          {
[1788155580.012] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155580.012] [547289:547373] [DMG]                                  0x1 = "" (0 chars),
[1788155580.012] [547289:547373] [DMG]                          },
[1788155580.012] [547289:547373] [DMG]                  },
[1788155580.012] [547289:547373] [DMG]
[1788155580.012] [547289:547373] [DMG]          },
[1788155580.012] [547289:547373] [DMG]
[1788155580.012] [547289:547373] [DMG]  ],
[1788155580.012] [547289:547373] [DMG]
[1788155580.012] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155580.012] [547289:547373] [DMG] },
[1788155580.013] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1788155580.013] [547289:547373] [CTL] Received ArmFailSafe response errorCode=0
[1788155580.013] [547289:547373] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1788155580.013] [547289:547373] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1788155580.013] [547289:547373] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1788155580.013] [547289:547373] [TOO] Starting commissioning stage 'ConfigRegulatory'
[1788155580.013] [547289:547373] [CTL] Setting Regulatory Config
[1788155580.013] [547289:547373] [CTL] Device does not support configurable regulatory location
[1788155580.013] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155580.013] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155580.013] [547289:547373] [EM] <<< [E:854i S:44800 M:103044096] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1788155580.014] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155580.014] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155580.205] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155580.205] [547289:547373] [EM] >>> [E:854i S:44800 M:162761936] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788155580.206] [547289:547373] [EM] Found matching exchange: 854i, Delegate: 0xffff90011e08
[1788155580.206] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155580.206] [547289:547373] [DMG] InvokeResponseMessage =
[1788155580.206] [547289:547373] [DMG] {
[1788155580.206] [547289:547373] [DMG]  suppressResponse = false,
[1788155580.206] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155580.206] [547289:547373] [DMG]  [
[1788155580.206] [547289:547373] [DMG]          InvokeResponseIB =
[1788155580.206] [547289:547373] [DMG]          {
[1788155580.206] [547289:547373] [DMG]                  CommandDataIB =
[1788155580.206] [547289:547373] [DMG]                  {
[1788155580.206] [547289:547373] [DMG]                          CommandPathIB =
[1788155580.207] [547289:547373] [DMG]                          {
[1788155580.207] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155580.207] [547289:547373] [DMG]                                  ClusterId = 0x30,
[1788155580.207] [547289:547373] [DMG]                                  CommandId = 0x3,
[1788155580.207] [547289:547373] [DMG]                          },
[1788155580.207] [547289:547373] [DMG]
[1788155580.207] [547289:547373] [DMG]                          CommandFields =
[1788155580.207] [547289:547373] [DMG]                          {
[1788155580.207] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155580.207] [547289:547373] [DMG]                                  0x1 = "" (0 chars),
[1788155580.207] [547289:547373] [DMG]                          },
[1788155580.208] [547289:547373] [DMG]                  },
[1788155580.208] [547289:547373] [DMG]
[1788155580.208] [547289:547373] [DMG]          },
[1788155580.208] [547289:547373] [DMG]
[1788155580.208] [547289:547373] [DMG]  ],
[1788155580.208] [547289:547373] [DMG]
[1788155580.208] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155580.208] [547289:547373] [DMG] },
[1788155580.208] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1788155580.208] [547289:547373] [CTL] Received SetRegulatoryConfig response errorCode=0
[1788155580.208] [547289:547373] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1788155580.209] [547289:547373] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1788155580.209] [547289:547373] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1788155580.209] [547289:547373] [TOO] Starting commissioning stage 'ConfigureTCAcknowledgments'
[1788155580.209] [547289:547373] [CTL] Setting Terms and Conditions
[1788155580.209] [547289:547373] [CTL] Setting Terms and Conditions: Skipped
[1788155580.209] [547289:547373] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'
[1788155580.209] [547289:547373] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1788155580.209] [547289:547373] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1788155580.209] [547289:547373] [TOO] Starting commissioning stage 'SendPAICertificateRequest'
[1788155580.209] [547289:547373] [CTL] Sending request for PAI certificate
[1788155580.209] [547289:547373] [CTL] Sending Certificate Chain request to 0xffff9000de20 device
[1788155580.209] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155580.209] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155580.210] [547289:547373] [EM] <<< [E:855i S:44800 M:103044097] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1788155580.211] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155580.211] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155580.401] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155580.596] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155580.789] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155580.790] [547289:547373] [EM] >>> [E:855i S:44800 M:162761937] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:534)
[1788155580.790] [547289:547373] [EM] Found matching exchange: 855i, Delegate: 0xffff90014458
[1788155580.790] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155580.790] [547289:547373] [DMG] InvokeResponseMessage =
[1788155580.790] [547289:547373] [DMG] {
[1788155580.790] [547289:547373] [DMG]  suppressResponse = false,
[1788155580.790] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155580.790] [547289:547373] [DMG]  [
[1788155580.790] [547289:547373] [DMG]          InvokeResponseIB =
[1788155580.790] [547289:547373] [DMG]          {
[1788155580.791] [547289:547373] [DMG]                  CommandDataIB =
[1788155580.791] [547289:547373] [DMG]                  {
[1788155580.791] [547289:547373] [DMG]                          CommandPathIB =
[1788155580.791] [547289:547373] [DMG]                          {
[1788155580.791] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155580.791] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155580.791] [547289:547373] [DMG]                                  CommandId = 0x3,
[1788155580.791] [547289:547373] [DMG]                          },
[1788155580.791] [547289:547373] [DMG]
[1788155580.791] [547289:547373] [DMG]                          CommandFields =
[1788155580.791] [547289:547373] [DMG]                          {
[1788155580.792] [547289:547373] [DMG]                                  0x0 = [
[1788155580.792] [547289:547373] [DMG]                                                  0x30, 0x82, 0x01, 0xd2, 0x30, 0x82, 0x01, 0x77, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x11, 0x00, 0xeb, 0x49, 0xbf, 0xaa, 0x73, 0x8f, 0xa5, 0x5d, 0xa8, 0xeb, 0x1b, 0x36, 0x94, 0x58, 0x3f, 0xec, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x41, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x33, 0x30, 0x39, 0x30, 0x35, 0x30, 0x30, 0x31, 0x39, 0x34, 0x30, 0x5a, 0x18, 0x0f, 0x32, 0x32, 0x32, 0x30, 0x31, 0x30, 0x32, 0x32, 0x30, 0x31, 0x31, 0x39, 0x34, 0x30, 0x5a, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x02, 0x37, 0xc9, 0x8e, 0xc5, 0xfb, 0xfc, 0x70, 0x3b, 0x9c, 0x17, 0x63, 0x4a, 0x94, 0x4a, 0xe1, 0x0e, 0x06, 0x22, 0x2e, 0xab, 0x58, 0x8e, 0x60, 0xe4, 0xc8, 0x8c, 0x71, 0x07, 0xbe, 0xe9, 0xeb, 0xb6, 0x43, 0x36, 0xe5, 0xea, 0x19, 0xf3, 0x4f, 0x69, 0x16, 0x42, 0x63, 0xca, 0xe2, 0x09, 0x7e, 0x65, 0xa5, 0x16, 0xf8, 0xa0, 0x5f, 0xb3, 0x6d, 0x0c, 0x45, 0x1f, 0x3c, 0xa6, 0x50, 0x88, 0x24, 0xa3, 0x66, 0x30, 0x64, 0x
[1788155580.792] [547289:547373] [DMG]                                  ] (470 bytes)
[1788155580.792] [547289:547373] [DMG]                          },
[1788155580.792] [547289:547373] [DMG]                  },
[1788155580.792] [547289:547373] [DMG]
[1788155580.792] [547289:547373] [DMG]          },
[1788155580.793] [547289:547373] [DMG]
[1788155580.793] [547289:547373] [DMG]  ],
[1788155580.793] [547289:547373] [DMG]
[1788155580.793] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155580.793] [547289:547373] [DMG] },
[1788155580.793] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1788155580.793] [547289:547373] [CTL] Received certificate chain from the device
[1788155580.793] [547289:547373] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1788155580.793] [547289:547373] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1788155580.793] [547289:547373] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1788155580.793] [547289:547373] [TOO] Starting commissioning stage 'SendDACCertificateRequest'
[1788155580.793] [547289:547373] [CTL] Sending request for DAC certificate
[1788155580.793] [547289:547373] [CTL] Sending Certificate Chain request to 0xffff9000de20 device
[1788155580.794] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155580.794] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155580.794] [547289:547373] [EM] <<< [E:856i S:44800 M:103044098] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1788155580.795] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155580.795] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155580.986] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155581.279] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155581.569] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155581.570] [547289:547373] [EM] >>> [E:856i S:44800 M:162761938] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:545)
[1788155581.570] [547289:547373] [EM] Found matching exchange: 856i, Delegate: 0xffff90011e08
[1788155581.570] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155581.570] [547289:547373] [DMG] InvokeResponseMessage =
[1788155581.570] [547289:547373] [DMG] {
[1788155581.570] [547289:547373] [DMG]  suppressResponse = false,
[1788155581.570] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155581.570] [547289:547373] [DMG]  [
[1788155581.570] [547289:547373] [DMG]          InvokeResponseIB =
[1788155581.570] [547289:547373] [DMG]          {
[1788155581.570] [547289:547373] [DMG]                  CommandDataIB =
[1788155581.571] [547289:547373] [DMG]                  {
[1788155581.571] [547289:547373] [DMG]                          CommandPathIB =
[1788155581.571] [547289:547373] [DMG]                          {
[1788155581.571] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155581.571] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155581.571] [547289:547373] [DMG]                                  CommandId = 0x3,
[1788155581.571] [547289:547373] [DMG]                          },
[1788155581.571] [547289:547373] [DMG]
[1788155581.571] [547289:547373] [DMG]                          CommandFields =
[1788155581.572] [547289:547373] [DMG]                          {
[1788155581.572] [547289:547373] [DMG]                                  0x0 = [
[1788155581.572] [547289:547373] [DMG]                                                  0x30, 0x82, 0x01, 0xdd, 0x30, 0x82, 0x01, 0x83, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x10, 0x0e, 0xcb, 0x29, 0xb3, 0x32, 0x16, 0xa9, 0x9d, 0x31, 0x83, 0xfc, 0x5d, 0xfe, 0xc9, 0x24, 0xf9, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x35, 0x31, 0x1d, 0x30, 0x1b, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x14, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x34, 0x31, 0x30, 0x32, 0x31, 0x30, 0x35, 0x31, 0x30, 0x32, 0x38, 0x5a, 0x18, 0x0f, 0x32, 0x31, 0x32, 0x34, 0x30, 0x39, 0x32, 0x37, 0x30, 0x36, 0x31, 0x30, 0x32, 0x38, 0x5a, 0x30, 0x48, 0x31, 0x1a, 0x30, 0x18, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x11, 0x48, 0x4f, 0x50, 0x45, 0x52, 0x46, 0x20, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x41, 0x43, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x31, 0x34, 0x37, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x30, 0x36, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xe9, 0x56, 0x79, 0x4b, 0x3d, 0x63, 0xe4, 0xe6, 0x32, 0xb1, 0x60, 0xac, 0xb2, 0x3d, 0xe6, 0x50, 0x47, 0x76, 0x1f, 0xe6, 0xdc, 0x20, 0xe2, 0x16, 0x11, 0xd1, 0x7e, 0x9e, 0x7b, 0x3d, 0x73, 0x5c, 0xa9, 0xf7, 0x3a, 0x60, 0x84, 0xca, 0x2d, 0x61, 0x07, 0x29, 0x4b, 0xbb, 0x0a, 0xf9, 0xbd, 0xeb, 0x92, 0x98, 0x
[1788155581.572] [547289:547373] [DMG]                                  ] (481 bytes)
[1788155581.572] [547289:547373] [DMG]                          },
[1788155581.572] [547289:547373] [DMG]                  },
[1788155581.572] [547289:547373] [DMG]
[1788155581.573] [547289:547373] [DMG]          },
[1788155581.573] [547289:547373] [DMG]
[1788155581.573] [547289:547373] [DMG]  ],
[1788155581.573] [547289:547373] [DMG]
[1788155581.573] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155581.573] [547289:547373] [DMG] },
[1788155581.573] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1788155581.573] [547289:547373] [CTL] Received certificate chain from the device
[1788155581.573] [547289:547373] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1788155581.573] [547289:547373] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1788155581.573] [547289:547373] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1788155581.573] [547289:547373] [TOO] Starting commissioning stage 'SendAttestationRequest'
[1788155581.574] [547289:547373] [CTL] Sending Attestation Request to the device.
[1788155581.574] [547289:547373] [CTL] Sending Attestation request to 0xffff9000de20 device
[1788155581.574] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155581.574] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155581.574] [547289:547373] [EM] <<< [E:857i S:44800 M:103044099] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1788155581.575] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155581.575] [547289:547373] [CTL] Sent Attestation request, waiting for the Attestation Information
[1788155581.575] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155581.864] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155582.058] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155582.252] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155582.253] [547289:547373] [EM] >>> [E:857i S:44800 M:162761939] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:554)
[1788155582.253] [547289:547373] [EM] Found matching exchange: 857i, Delegate: 0xffff90014458
[1788155582.253] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155582.253] [547289:547373] [DMG] InvokeResponseMessage =
[1788155582.253] [547289:547373] [DMG] {
[1788155582.253] [547289:547373] [DMG]  suppressResponse = false,
[1788155582.253] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155582.253] [547289:547373] [DMG]  [
[1788155582.253] [547289:547373] [DMG]          InvokeResponseIB =
[1788155582.253] [547289:547373] [DMG]          {
[1788155582.253] [547289:547373] [DMG]                  CommandDataIB =
[1788155582.254] [547289:547373] [DMG]                  {
[1788155582.254] [547289:547373] [DMG]                          CommandPathIB =
[1788155582.254] [547289:547373] [DMG]                          {
[1788155582.254] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155582.254] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155582.254] [547289:547373] [DMG]                                  CommandId = 0x1,
[1788155582.254] [547289:547373] [DMG]                          },
[1788155582.254] [547289:547373] [DMG]
[1788155582.255] [547289:547373] [DMG]                          CommandFields =
[1788155582.255] [547289:547373] [DMG]                          {
[1788155582.255] [547289:547373] [DMG]                                  0x0 = [
[1788155582.255] [547289:547373] [DMG]                                                  0x15, 0x31, 0x01, 0x7b, 0x01, 0x30, 0x82, 0x01, 0x77, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x01, 0x68, 0x30, 0x82, 0x01, 0x64, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x81, 0xd0, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x81, 0xc2, 0x04, 0x81, 0xbf, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0x9a, 0x14, 0x36, 0x02, 0x05, 0x05, 0x30, 0x05, 0x15, 0x30, 0x05, 0x25, 0x30, 0x05, 0x35, 0x30, 0x05, 0x45, 0x30, 0x05, 0x55, 0x30, 0x05, 0x65, 0x30, 0x05, 0x75, 0x30, 0x05, 0x85, 0x30, 0x05, 0x95, 0x30, 0x05, 0xa5, 0x30, 0x05, 0xb5, 0x30, 0x05, 0xc5, 0x30, 0x05, 0xd5, 0x30, 0x05, 0xe5, 0x30, 0x05, 0xf5, 0x30, 0x05, 0x05, 0x40, 0x05, 0x15, 0x40, 0x05, 0x25, 0x40, 0x05, 0x35, 0x40, 0x05, 0x45, 0x40, 0x05, 0x55, 0x40, 0x05, 0x65, 0x40, 0x05, 0x75, 0x40, 0x05, 0x85, 0x40, 0x05, 0x95, 0x40, 0x05, 0xa5, 0x40, 0x05, 0xb5, 0x40, 0x05, 0xc5, 0x40, 0x05, 0xd5, 0x40, 0x05, 0xe5, 0x40, 0x05, 0xf5, 0x40, 0x05, 0x05, 0x42, 0x05, 0x15, 0x42, 0x05, 0x25, 0x42, 0x05, 0x35, 0x42, 0x18, 0x25, 0x03, 0x02, 0x02, 0x2c, 0x04, 0x13, 0x46, 0x41, 0x4d, 0x32, 0x32, 0x36, 0x34, 0x39, 0x37, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x24, 0x05, 0x00, 0x24, 0x06, 0x00, 0x24, 0x07, 0x01, 0x24, 0x08, 0x02, 0x25, 0x09, 0x70, 0x14, 0x25, 0x0a, 0x06, 0x80, 0x36, 0x0b, 0x10, 0x14, 0xe9, 0x16, 0x0d, 0xc4, 0x17, 0xf7, 0x41, 0x9c, 0x95, 0x32, 0x0b, 0xbf, 0x36, 0x56, 0x71, 0x93, 0x3f, 0xf3, 0x12, 0x22, 0x18, 0x18, 0x31, 0x7d, 0x30, 0x7b, 0x02, 0x01, 0x03, 0x80, 0x14, 0xfe, 0x34, 0x3f, 0x95, 0x99, 0x47, 0x76, 0x3b, 0x61, 0xee, 0x45, 0x39, 0x13, 0x13, 0x38, 0x49, 0x4f, 0x
[1788155582.255] [547289:547373] [DMG]                                  ] (423 bytes)
[1788155582.255] [547289:547373] [DMG]                                  0x1 = [
[1788155582.256] [547289:547373] [DMG]                                                  0xb0, 0xb8, 0x29, 0xd1, 0x07, 0xa9, 0x2e, 0xc0, 0xc7, 0xdd, 0xeb, 0xa0, 0xcb, 0x6e, 0x6e, 0x29, 0xf3, 0x2a, 0x17, 0x55, 0x10, 0x0d, 0xbf, 0xe5, 0x1a, 0xbb, 0xad, 0xdc, 0xd1, 0x07, 0x11, 0x17, 0x33, 0xe0, 0xa9, 0xad, 0xc1, 0xfb, 0xbc, 0x73, 0x76, 0x85, 0xae, 0x9b, 0x81, 0x33, 0x7b, 0xe9, 0x97, 0x82, 0x51, 0xc8, 0x9b, 0xc2, 0xdc, 0x03, 0xeb, 0x4d, 0xd3, 0xd0, 0xe6, 0xa0, 0x8e, 0x8f,
[1788155582.256] [547289:547373] [DMG]                                  ] (64 bytes)
[1788155582.256] [547289:547373] [DMG]                          },
[1788155582.256] [547289:547373] [DMG]                  },
[1788155582.256] [547289:547373] [DMG]
[1788155582.256] [547289:547373] [DMG]          },
[1788155582.256] [547289:547373] [DMG]
[1788155582.256] [547289:547373] [DMG]  ],
[1788155582.256] [547289:547373] [DMG]
[1788155582.256] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155582.257] [547289:547373] [DMG] },
[1788155582.257] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1788155582.257] [547289:547373] [CTL] Received Attestation Information from the device
[1788155582.257] [547289:547373] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1788155582.257] [547289:547373] [CTL] AutoCommissioner setting attestationElements buffer size 423/423
[1788155582.257] [547289:547373] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1788155582.257] [547289:547373] [CTL] Performing next commissioning step 'AttestationVerification'
[1788155582.257] [547289:547373] [TOO] Starting commissioning stage 'AttestationVerification'
[1788155582.257] [547289:547373] [CTL] Verifying Device Attestation information received from the device
[1788155582.271] [547289:547373] [-] Device candidate DAC chain details:
[1788155582.271] [547289:547373] [-] --> DAC's VID: 0x1470, PID: 0x8006
[1788155582.271] [547289:547373] [-] ==== DAC certificate considered (481 bytes) ====
[1788155582.271] [547289:547373] [-] -----BEGIN CERTIFICATE-----
[1788155582.271] [547289:547373] [-] MIIB3TCCAYOgAwIBAgIQDsspszIWqZ0xg/xd/skk+TAKBggqhkjOPQQDAjA1MR0w
[1788155582.271] [547289:547373] [-] GwYDVQQDDBRIT1BFUkYgTWF0dGVyIFBBSSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0
[1788155582.271] [547289:547373] [-] NzAwIBcNMjQxMDIxMDUxMDI4WhgPMjEyNDA5MjcwNjEwMjhaMEgxGjAYBgNVBAMM
[1788155582.271] [547289:547373] [-] EUhPUEVSRiBNYXR0ZXIgREFDMRQwEgYKKwYBBAGConwCAQwEMTQ3MDEUMBIGCisG
[1788155582.271] [547289:547373] [-] AQQBgqJ8AgIMBDgwMDYwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATpVnlLPWPk
[1788155582.271] [547289:547373] [-] 5jKxYKyyPeZQR3Yf5twg4hYR0X6eez1zXKn3OmCEyi1hBylLuwr5veuSmLR/fBFz
[1788155582.271] [547289:547373] [-] ADmydjbJoqCOo2AwXjAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaAFOu0mvEt1SNX
[1788155582.271] [547289:547373] [-] vT5a0j1vRwbQv5+aMB0GA1UdDgQWBBScROSpadKqznYFUcvoTNvpaDk8vDAOBgNV
[1788155582.271] [547289:547373] [-] HQ8BAf8EBAMCB4AwCgYIKoZIzj0EAwIDSAAwRQIhAPd+rIia1s69ZfGEi/Q1eYUJ
[1788155582.271] [547289:547373] [-] w9O4F6M6vf5wrTWCulbUAiAC9YZTeZWzo3vmoh8zdbCkIaiEmtPjgQ9ybO0Optbx
[1788155582.271] [547289:547373] [-] Lg==
[1788155582.271] [547289:547373] [-] -----END CERTIFICATE-----
[1788155582.273] [547289:547373] [-] --> DAC certificate SKID: 9C:44:E4:A9:69:D2:AA:CE:76:05:51:CB:E8:4C:DB:E9:68:39:3C:BC
[1788155582.274] [547289:547373] [-] --> DAC certificate AKID: EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
[1788155582.274] [547289:547373] [-] ==== PAI certificate considered (470 bytes) ====
[1788155582.274] [547289:547373] [-] -----BEGIN CERTIFICATE-----
[1788155582.274] [547289:547373] [-] MIIB0jCCAXegAwIBAgIRAOtJv6pzj6VdqOsbNpRYP+wwCgYIKoZIzj0EAwIwNTEd
[1788155582.274] [547289:547373] [-] MBsGA1UEAwwUSE9QRVJGIE1hdHRlciBQQUEgMDExFDASBgorBgEEAYKifAIBDAQx
[1788155582.274] [547289:547373] [-] NDcwMCAXDTIzMDkwNTAwMTk0MFoYDzIyMjAxMDIyMDExOTQwWjA1MR0wGwYDVQQD
[1788155582.274] [547289:547373] [-] DBRIT1BFUkYgTWF0dGVyIFBBSSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0NzAwWTAT
[1788155582.274] [547289:547373] [-] BgcqhkjOPQIBBggqhkjOPQMBBwNCAAQCN8mOxfv8cDucF2NKlErhDgYiLqtYjmDk
[1788155582.274] [547289:547373] [-] yIxxB77p67ZDNuXqGfNPaRZCY8riCX5lpRb4oF+zbQxFHzymUIgko2YwZDASBgNV
[1788155582.274] [547289:547373] [-] HRMBAf8ECDAGAQH/AgEAMB8GA1UdIwQYMBaAFOkWDcQX90GclTILvzZWcZM/8xIi
[1788155582.274] [547289:547373] [-] MB0GA1UdDgQWBBTrtJrxLdUjV70+WtI9b0cG0L+fmjAOBgNVHQ8BAf8EBAMCAQYw
[1788155582.274] [547289:547373] [-] CgYIKoZIzj0EAwIDSQAwRgIhAJmF3MWaAB3+WFav89D3a0KoDZ+7c4SGmJtjDdyz
[1788155582.274] [547289:547373] [-] CPaCAiEA8DfnzFMaVz8QaDyI/ygdCGEPMBbpvHxx9KNEiJs7gcE=
[1788155582.274] [547289:547373] [-] -----END CERTIFICATE-----
[1788155582.275] [547289:547373] [-] --> PAI certificate SKID: EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
[1788155582.276] [547289:547373] [-] --> PAI certificate AKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788155582.282] [547289:547373] [-] ==== PAA certificate considered (466 bytes) ====
[1788155582.282] [547289:547373] [-] -----BEGIN CERTIFICATE-----
[1788155582.282] [547289:547373] [-] MIIBzjCCAXSgAwIBAgIRAMB+YpaZQeu05JIuF/AMsiYwCgYIKoZIzj0EAwIwNTEd
[1788155582.282] [547289:547373] [-] MBsGA1UEAwwUSE9QRVJGIE1hdHRlciBQQUEgMDExFDASBgorBgEEAYKifAIBDAQx
[1788155582.282] [547289:547373] [-] NDcwMCAXDTIzMDgyNTA1Mjk1N1oYDzIyMjMwNzA4MDYyOTU3WjA1MR0wGwYDVQQD
[1788155582.282] [547289:547373] [-] DBRIT1BFUkYgTWF0dGVyIFBBQSAwMTEUMBIGCisGAQQBgqJ8AgEMBDE0NzAwWTAT
[1788155582.282] [547289:547373] [-] BgcqhkjOPQIBBggqhkjOPQMBBwNCAATVxJPVN3fr7vg9sOX24AO3WyMLWN/O9u5Z
[1788155582.282] [547289:547373] [-] pjjquJNYiPXVziNj1Yq7o1fFT+JJ/V8gEkq3az3CMfTgr5A3DhHko2MwYTAPBgNV
[1788155582.282] [547289:547373] [-] HRMBAf8EBTADAQH/MB0GA1UdDgQWBBTpFg3EF/dBnJUyC782VnGTP/MSIjAOBgNV
[1788155582.282] [547289:547373] [-] HQ8BAf8EBAMCAYYwHwYDVR0jBBgwFoAU6RYNxBf3QZyVMgu/NlZxkz/zEiIwCgYI
[1788155582.282] [547289:547373] [-] KoZIzj0EAwIDSAAwRQIhAMghj3vry4WnuZhyPK8ZGqyFG2aNdKkJCqwy/4SkcHT7
[1788155582.282] [547289:547373] [-] AiBxxCLcAC5bDcze/6tJcCuLX5vWaVQYw6IVwBwciEo+rw==
[1788155582.282] [547289:547373] [-] -----END CERTIFICATE-----
[1788155582.283] [547289:547373] [-] --> PAA certificate SKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788155582.284] [547289:547373] [-] --> PAA certificate AKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1788155582.291] [547289:547373] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1788155582.292] [547289:547373] [-] Device certification declaration details:
[1788155582.292] [547289:547373] [-] --> VID: 0x149A
[1788155582.292] [547289:547373] [-] --> Device type ID: 0x0000_0202
[1788155582.292] [547289:547373] [-] --> Certification type: 2 (Certified device)
[1788155582.292] [547289:547373] [-] --> DAC origin VID: 0x1470, PID: 0x8006
[1788155582.292] [547289:547373] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1788155582.292] [547289:547373] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1788155582.292] [547289:547373] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1788155582.292] [547289:547373] [TOO] Starting commissioning stage 'AttestationRevocationCheck'
[1788155582.292] [547289:547373] [CTL] Verifying the device's DAC chain revocation status
[1788155582.292] [547289:547373] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1788155582.292] [547289:547373] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1788155582.292] [547289:547373] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1788155582.292] [547289:547373] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1788155582.292] [547289:547373] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1788155582.292] [547289:547373] [TOO] Starting commissioning stage 'SendOpCertSigningRequest'
[1788155582.292] [547289:547373] [CTL] Sending CSR request to 0xffff9000de20 device
[1788155582.292] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155582.292] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155582.293] [547289:547373] [EM] <<< [E:858i S:44800 M:103044100] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1788155582.293] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155582.293] [547289:547373] [CTL] Sent CSR request, waiting for the CSR
[1788155582.293] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155582.449] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155582.642] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155582.642] [547289:547373] [EM] >>> [E:858i S:44800 M:162761940] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1788155582.642] [547289:547373] [EM] Found matching exchange: 858i, Delegate: 0xffff90011e08
[1788155582.642] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155582.642] [547289:547373] [DMG] InvokeResponseMessage =
[1788155582.642] [547289:547373] [DMG] {
[1788155582.642] [547289:547373] [DMG]  suppressResponse = false,
[1788155582.642] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155582.642] [547289:547373] [DMG]  [
[1788155582.642] [547289:547373] [DMG]          InvokeResponseIB =
[1788155582.642] [547289:547373] [DMG]          {
[1788155582.642] [547289:547373] [DMG]                  CommandDataIB =
[1788155582.642] [547289:547373] [DMG]                  {
[1788155582.642] [547289:547373] [DMG]                          CommandPathIB =
[1788155582.642] [547289:547373] [DMG]                          {
[1788155582.643] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155582.643] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155582.643] [547289:547373] [DMG]                                  CommandId = 0x5,
[1788155582.643] [547289:547373] [DMG]                          },
[1788155582.643] [547289:547373] [DMG]
[1788155582.643] [547289:547373] [DMG]                          CommandFields =
[1788155582.643] [547289:547373] [DMG]                          {
[1788155582.643] [547289:547373] [DMG]                                  0x0 = [
[1788155582.643] [547289:547373] [DMG]                                                  0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xcc, 0x36, 0x1b, 0x29, 0x50, 0x8e, 0x22, 0x4e, 0x59, 0xdf, 0xb1, 0xce, 0xdb, 0x9b, 0xd0, 0xde, 0xa9, 0xcd, 0x2f, 0x77, 0xa4, 0x75, 0xfb, 0x8e, 0x38, 0x3e, 0x0d, 0x48, 0x44, 0x66, 0xbf, 0x58, 0x3e, 0x6f, 0xf6, 0x81, 0x56, 0xd4, 0xba, 0xec, 0xfb, 0x6b, 0x19, 0xd5, 0x91, 0x79, 0x2e, 0x35, 0x14, 0x4d, 0x84, 0x51, 0x57, 0x13, 0xd1, 0x0f, 0x38, 0xc0, 0x46, 0x04, 0x37, 0x11, 0x92, 0xf1, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x20, 0x65, 0x7a, 0x23, 0x84, 0x25, 0xe8, 0x86, 0xf1, 0x5b, 0x81, 0x6b, 0x33, 0x18, 0x23, 0x38, 0x91, 0xf2, 0x69, 0x22, 0x13, 0x75, 0x0f, 0xaa, 0x60, 0x48, 0x93, 0xe0, 0xc1, 0xcd, 0x94, 0x46, 0x45, 0x02, 0x21, 0x00, 0x83, 0x0b, 0x5b, 0xb3, 0x8b, 0x2c, 0xaa, 0x4f, 0x32, 0xd7, 0xfe, 0x6e, 0x8f, 0x97, 0xb8, 0xda, 0x24, 0xa7, 0x58, 0x6e, 0xdb, 0x16, 0x9b, 0x03, 0xb3, 0x46, 0x7d, 0x0c, 0x58, 0x08, 0xa6, 0xfe, 0x30, 0x02, 0x20, 0xda, 0x4f, 0x90, 0x13, 0x09, 0x93, 0x4b, 0xa0, 0x5f, 0xa5, 0x0f, 0xb9, 0x95, 0x83, 0x90, 0xe8, 0x25, 0x7d, 0x83, 0x9c, 0x11, 0xf7, 0xe7, 0x99, 0x37, 0x6a, 0xea, 0x52, 0x58, 0xeb, 0xea, 0xff, 0x18,
[1788155582.643] [547289:547373] [DMG]                                  ] (261 bytes)
[1788155582.643] [547289:547373] [DMG]                                  0x1 = [
[1788155582.643] [547289:547373] [DMG]                                                  0x8c, 0xd8, 0x07, 0x34, 0xb6, 0xe1, 0x89, 0x31, 0xe1, 0xc5, 0xf4, 0x60, 0x9a, 0x2a, 0x75, 0x94, 0x0a, 0x1b, 0x5d, 0xe6, 0x91, 0x16, 0xa8, 0x4e, 0x2e, 0xce, 0xcb, 0xab, 0xdf, 0x17, 0x49, 0xb3, 0x48, 0xf0, 0xb1, 0xd6, 0xdb, 0x8a, 0x93, 0x1d, 0xc1, 0xbd, 0x06, 0xc6, 0x33, 0x24, 0x4e, 0x9d, 0xb5, 0x82, 0x77, 0xaa, 0x21, 0xf1, 0x5e, 0x31, 0xe1, 0x5f, 0x98, 0xe3, 0xc2, 0xc8, 0x5f, 0xfa,
[1788155582.643] [547289:547373] [DMG]                                  ] (64 bytes)
[1788155582.643] [547289:547373] [DMG]                          },
[1788155582.643] [547289:547373] [DMG]                  },
[1788155582.643] [547289:547373] [DMG]
[1788155582.643] [547289:547373] [DMG]          },
[1788155582.643] [547289:547373] [DMG]
[1788155582.643] [547289:547373] [DMG]  ],
[1788155582.643] [547289:547373] [DMG]
[1788155582.644] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155582.644] [547289:547373] [DMG] },
[1788155582.644] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1788155582.644] [547289:547373] [CTL] Received certificate signing request from the device
[1788155582.644] [547289:547373] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1788155582.644] [547289:547373] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1788155582.644] [547289:547373] [CTL] Performing next commissioning step 'ValidateCSR'
[1788155582.644] [547289:547373] [TOO] Starting commissioning stage 'ValidateCSR'
[1788155582.648] [547289:547373] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1788155582.648] [547289:547373] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1788155582.648] [547289:547373] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1788155582.648] [547289:547373] [TOO] Starting commissioning stage 'GenerateNOCChain'
[1788155582.648] [547289:547373] [CTL] Getting certificate chain for the device from the issuer
[1788155582.650] [547289:547373] [CTL] Verifying Certificate Signing Request
[1788155582.653] [547289:547373] [CTL] Generating NOC
[1788155582.653] [547289:547373] [CTL] Providing certificate chain to the commissioner
[1788155582.653] [547289:547373] [CTL] Received callback from the CA for NOC Chain generation. Status: Success
[1788155582.653] [547289:547373] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1788155582.654] [547289:547373] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1788155582.654] [547289:547373] [TOO] Starting commissioning stage 'SendTrustedRootCert'
[1788155582.654] [547289:547373] [CTL] Sending root certificate to the device
[1788155582.654] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155582.654] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155582.654] [547289:547373] [EM] <<< [E:859i S:44800 M:103044101] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1788155582.655] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155582.655] [547289:547373] [CTL] Sent root certificate to the device
[1788155582.656] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155583.032] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155583.032] [547289:547373] [EM] >>> [E:859i S:44800 M:162761941] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1788155583.032] [547289:547373] [EM] Found matching exchange: 859i, Delegate: 0xffff90014458
[1788155583.032] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155583.032] [547289:547373] [DMG] InvokeResponseMessage =
[1788155583.032] [547289:547373] [DMG] {
[1788155583.032] [547289:547373] [DMG]  suppressResponse = false,
[1788155583.032] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155583.032] [547289:547373] [DMG]  [
[1788155583.032] [547289:547373] [DMG]          InvokeResponseIB =
[1788155583.033] [547289:547373] [DMG]          {
[1788155583.033] [547289:547373] [DMG]                  CommandStatusIB =
[1788155583.033] [547289:547373] [DMG]                  {
[1788155583.033] [547289:547373] [DMG]                          CommandPathIB =
[1788155583.033] [547289:547373] [DMG]                          {
[1788155583.033] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155583.033] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155583.033] [547289:547373] [DMG]                                  CommandId = 0xb,
[1788155583.033] [547289:547373] [DMG]                          },
[1788155583.033] [547289:547373] [DMG]
[1788155583.033] [547289:547373] [DMG]                          StatusIB =
[1788155583.033] [547289:547373] [DMG]                          {
[1788155583.033] [547289:547373] [DMG]                                  status = 0x00 (SUCCESS),
[1788155583.033] [547289:547373] [DMG]                          },
[1788155583.033] [547289:547373] [DMG]
[1788155583.033] [547289:547373] [DMG]                  },
[1788155583.033] [547289:547373] [DMG]
[1788155583.033] [547289:547373] [DMG]          },
[1788155583.033] [547289:547373] [DMG]
[1788155583.033] [547289:547373] [DMG]  ],
[1788155583.033] [547289:547373] [DMG]
[1788155583.033] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155583.033] [547289:547373] [DMG] },
[1788155583.034] [547289:547373] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1788155583.034] [547289:547373] [CTL] Device confirmed that it has received the root certificate
[1788155583.034] [547289:547373] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1788155583.034] [547289:547373] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1788155583.034] [547289:547373] [CTL] Performing next commissioning step 'SendNOC'
[1788155583.034] [547289:547373] [TOO] Starting commissioning stage 'SendNOC'
[1788155583.034] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155583.034] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155583.034] [547289:547373] [EM] <<< [E:860i S:44800 M:103044102] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1788155583.035] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155583.035] [547289:547373] [CTL] Sent operational certificate to the device
[1788155583.035] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155583.617] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155583.617] [547289:547373] [EM] >>> [E:860i S:44800 M:162761942] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788155583.617] [547289:547373] [EM] Found matching exchange: 860i, Delegate: 0xffff90011e08
[1788155583.617] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155583.617] [547289:547373] [DMG] InvokeResponseMessage =
[1788155583.617] [547289:547373] [DMG] {
[1788155583.617] [547289:547373] [DMG]  suppressResponse = false,
[1788155583.617] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155583.618] [547289:547373] [DMG]  [
[1788155583.618] [547289:547373] [DMG]          InvokeResponseIB =
[1788155583.618] [547289:547373] [DMG]          {
[1788155583.618] [547289:547373] [DMG]                  CommandDataIB =
[1788155583.618] [547289:547373] [DMG]                  {
[1788155583.618] [547289:547373] [DMG]                          CommandPathIB =
[1788155583.618] [547289:547373] [DMG]                          {
[1788155583.618] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155583.618] [547289:547373] [DMG]                                  ClusterId = 0x3e,
[1788155583.618] [547289:547373] [DMG]                                  CommandId = 0x8,
[1788155583.618] [547289:547373] [DMG]                          },
[1788155583.618] [547289:547373] [DMG]
[1788155583.618] [547289:547373] [DMG]                          CommandFields =
[1788155583.618] [547289:547373] [DMG]                          {
[1788155583.618] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155583.618] [547289:547373] [DMG]                                  0x1 = 1 (unsigned),
[1788155583.618] [547289:547373] [DMG]                          },
[1788155583.618] [547289:547373] [DMG]                  },
[1788155583.618] [547289:547373] [DMG]
[1788155583.618] [547289:547373] [DMG]          },
[1788155583.618] [547289:547373] [DMG]
[1788155583.618] [547289:547373] [DMG]  ],
[1788155583.618] [547289:547373] [DMG]
[1788155583.618] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155583.618] [547289:547373] [DMG] },
[1788155583.618] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1788155583.618] [547289:547373] [CTL] Device returned status 0 on receiving the NOC
[1788155583.618] [547289:547373] [CTL] Operational credentials provisioned on device 0xffff9000de20
[1788155583.618] [547289:547373] [TOO] Secure Pairing Success
[1788155583.618] [547289:547373] [TOO] CASE establishment successful
[1788155583.618] [547289:547373] [CTL] Successfully finished commissioning step 'SendNOC'
[1788155583.618] [547289:547373] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1788155583.618] [547289:547373] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1788155583.618] [547289:547373] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1788155583.618] [547289:547373] [TOO] Starting commissioning stage 'ThreadNetworkSetup'
[1788155583.619] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155583.619] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155583.619] [547289:547373] [EM] <<< [E:861i S:44800 M:103044103] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:176)
[1788155583.620] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155583.620] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155583.812] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155583.812] [547289:547373] [EM] >>> [E:861i S:44800 M:162761943] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788155583.812] [547289:547373] [EM] Found matching exchange: 861i, Delegate: 0xffff90014458
[1788155583.813] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155583.813] [547289:547373] [DMG] InvokeResponseMessage =
[1788155583.813] [547289:547373] [DMG] {
[1788155583.813] [547289:547373] [DMG]  suppressResponse = false,
[1788155583.813] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155583.813] [547289:547373] [DMG]  [
[1788155583.813] [547289:547373] [DMG]          InvokeResponseIB =
[1788155583.813] [547289:547373] [DMG]          {
[1788155583.813] [547289:547373] [DMG]                  CommandDataIB =
[1788155583.813] [547289:547373] [DMG]                  {
[1788155583.813] [547289:547373] [DMG]                          CommandPathIB =
[1788155583.813] [547289:547373] [DMG]                          {
[1788155583.813] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155583.813] [547289:547373] [DMG]                                  ClusterId = 0x31,
[1788155583.813] [547289:547373] [DMG]                                  CommandId = 0x5,
[1788155583.813] [547289:547373] [DMG]                          },
[1788155583.813] [547289:547373] [DMG]
[1788155583.813] [547289:547373] [DMG]                          CommandFields =
[1788155583.813] [547289:547373] [DMG]                          {
[1788155583.813] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155583.813] [547289:547373] [DMG]                                  0x2 = 0 (unsigned),
[1788155583.813] [547289:547373] [DMG]                          },
[1788155583.813] [547289:547373] [DMG]                  },
[1788155583.813] [547289:547373] [DMG]
[1788155583.813] [547289:547373] [DMG]          },
[1788155583.813] [547289:547373] [DMG]
[1788155583.813] [547289:547373] [DMG]  ],
[1788155583.813] [547289:547373] [DMG]
[1788155583.813] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155583.813] [547289:547373] [DMG] },
[1788155583.813] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1788155583.813] [547289:547373] [CTL] Received NetworkConfig response, networkingStatus=0
[1788155583.814] [547289:547373] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1788155583.814] [547289:547373] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1788155583.814] [547289:547373] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1788155583.814] [547289:547373] [TOO] Starting commissioning stage 'FailsafeBeforeThreadEnable'
[1788155583.814] [547289:547373] [CTL] Arming failsafe (94 seconds)
[1788155583.814] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155583.814] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155583.814] [547289:547373] [EM] <<< [E:862i S:44800 M:103044104] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1788155583.815] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155583.815] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155584.006] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155584.007] [547289:547373] [EM] >>> [E:862i S:44800 M:162761944] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1788155584.007] [547289:547373] [EM] Found matching exchange: 862i, Delegate: 0xffff90011e08
[1788155584.007] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155584.007] [547289:547373] [DMG] InvokeResponseMessage =
[1788155584.007] [547289:547373] [DMG] {
[1788155584.007] [547289:547373] [DMG]  suppressResponse = false,
[1788155584.007] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155584.007] [547289:547373] [DMG]  [
[1788155584.007] [547289:547373] [DMG]          InvokeResponseIB =
[1788155584.007] [547289:547373] [DMG]          {
[1788155584.007] [547289:547373] [DMG]                  CommandDataIB =
[1788155584.007] [547289:547373] [DMG]                  {
[1788155584.007] [547289:547373] [DMG]                          CommandPathIB =
[1788155584.007] [547289:547373] [DMG]                          {
[1788155584.007] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155584.007] [547289:547373] [DMG]                                  ClusterId = 0x30,
[1788155584.007] [547289:547373] [DMG]                                  CommandId = 0x1,
[1788155584.007] [547289:547373] [DMG]                          },
[1788155584.007] [547289:547373] [DMG]
[1788155584.007] [547289:547373] [DMG]                          CommandFields =
[1788155584.007] [547289:547373] [DMG]                          {
[1788155584.008] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155584.008] [547289:547373] [DMG]                                  0x1 = "" (0 chars),
[1788155584.008] [547289:547373] [DMG]                          },
[1788155584.008] [547289:547373] [DMG]                  },
[1788155584.008] [547289:547373] [DMG]
[1788155584.008] [547289:547373] [DMG]          },
[1788155584.008] [547289:547373] [DMG]
[1788155584.008] [547289:547373] [DMG]  ],
[1788155584.008] [547289:547373] [DMG]
[1788155584.008] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155584.008] [547289:547373] [DMG] },
[1788155584.008] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1788155584.008] [547289:547373] [CTL] Received ArmFailSafe response errorCode=0
[1788155584.008] [547289:547373] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1788155584.008] [547289:547373] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1788155584.008] [547289:547373] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1788155584.008] [547289:547373] [TOO] Starting commissioning stage 'ThreadNetworkEnable'
[1788155584.008] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155584.008] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155584.008] [547289:547373] [EM] <<< [E:863i S:44800 M:103044105] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1788155584.009] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155584.009] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155585.468] [547289:547313] [DL] Indication received: conn=0xffff8405ef20
[1788155585.469] [547289:547373] [EM] >>> [E:863i S:44800 M:162761945] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1788155585.469] [547289:547373] [EM] Found matching exchange: 863i, Delegate: 0xffff90014458
[1788155585.469] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155585.469] [547289:547373] [DMG] InvokeResponseMessage =
[1788155585.469] [547289:547373] [DMG] {
[1788155585.469] [547289:547373] [DMG]  suppressResponse = false,
[1788155585.469] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155585.469] [547289:547373] [DMG]  [
[1788155585.469] [547289:547373] [DMG]          InvokeResponseIB =
[1788155585.469] [547289:547373] [DMG]          {
[1788155585.469] [547289:547373] [DMG]                  CommandDataIB =
[1788155585.469] [547289:547373] [DMG]                  {
[1788155585.469] [547289:547373] [DMG]                          CommandPathIB =
[1788155585.469] [547289:547373] [DMG]                          {
[1788155585.469] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155585.469] [547289:547373] [DMG]                                  ClusterId = 0x31,
[1788155585.469] [547289:547373] [DMG]                                  CommandId = 0x7,
[1788155585.469] [547289:547373] [DMG]                          },
[1788155585.469] [547289:547373] [DMG]
[1788155585.469] [547289:547373] [DMG]                          CommandFields =
[1788155585.469] [547289:547373] [DMG]                          {
[1788155585.469] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155585.469] [547289:547373] [DMG]                                  0x2 = NULL
[1788155585.469] [547289:547373] [DMG]                          },
[1788155585.469] [547289:547373] [DMG]                  },
[1788155585.469] [547289:547373] [DMG]
[1788155585.469] [547289:547373] [DMG]          },
[1788155585.469] [547289:547373] [DMG]
[1788155585.469] [547289:547373] [DMG]  ],
[1788155585.469] [547289:547373] [DMG]
[1788155585.469] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155585.469] [547289:547373] [DMG] },
[1788155585.470] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1788155585.470] [547289:547373] [CTL] Received ConnectNetwork response, networkingStatus=0
[1788155585.470] [547289:547373] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1788155585.470] [547289:547373] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'EvictPreviousCaseSessions'
[1788155585.470] [547289:547373] [CTL] Performing next commissioning step 'EvictPreviousCaseSessions'
[1788155585.470] [547289:547373] [TOO] Starting commissioning stage 'EvictPreviousCaseSessions'
[1788155585.470] [547289:547373] [IN] Expiring all sessions for node <00000000000008CA, 1>!!
[1788155585.470] [547289:547373] [CTL] Successfully finished commissioning step 'EvictPreviousCaseSessions'
[1788155585.470] [547289:547373] [CTL] Commissioning stage next step: 'EvictPreviousCaseSessions' -> 'FindOperationalForStayActive'
[1788155585.470] [547289:547373] [CTL] Performing next commissioning step 'FindOperationalForStayActive'
[1788155585.470] [547289:547373] [TOO] Starting commissioning stage 'FindOperationalForStayActive'
[1788155585.470] [547289:547373] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1788155585.470] [547289:547373] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1788155585.470] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 2
[1788155585.470] [547289:547373] [DIS] Lookup started for 30230980DA7DCAF4-00000000000008CA
[1788155585.471] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155585.669] [547289:547373] [DIS] Checking node lookup status for 30230980DA7DCAF4-00000000000008CA after 200 ms
[1788155587.031] [547289:547373] [DIS] SRV record already actively processed.
[1788155587.031] [547289:547373] [DIS] SRV record already actively processed.
[1788155587.036] [547289:547373] [DIS] Lookup clearing interface for non LL address
[1788155587.036] [547289:547373] [DIS] UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9%eth0]:5540: new best score: 5 (for 30230980DA7DCAF4-00000000000008CA)
[1788155587.036] [547289:547373] [DIS] Checking node lookup status for 30230980DA7DCAF4-00000000000008CA after 1566 ms
[1788155587.036] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: Updating device address to UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540 while in state 2
[1788155587.036] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 2 --> 3
[1788155587.036] [547289:547373] [IN] SecureSession[0xffff90019f20]: Allocated Type:2 LSID:44801
[1788155587.036] [547289:547373] [SC] Initiating session on local FabricIndex 1 from 0x000000000001B669 -> 0x00000000000008CA
[1788155587.037] [547289:547373] [EM] <<< [E:864i S:0 M:111788299] (U) Msg TX from C48046684CDB7D27 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[1788155587.037] [547289:547373] [EM] ??1 [E:864i S:0 M:111788299] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2504ms from now [State:Idle II:2000 AI:2000 AT:4000]
[1788155587.037] [547289:547373] [SC] Sent Sigma1 msg to <00000000000008CA, 1> [II:500ms AI:300ms AT:4000ms]
[1788155587.037] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 3 --> 4
[1788155587.156] [547289:547373] [EM] >>> [E:864i S:0 M:52138054 (Ack:111788299)] (U) Msg RX from 0:0000000000000000 [0000] to C48046684CDB7D27 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788155587.156] [547289:547373] [EM] Found matching exchange: 864i, Delegate: 0xffff90015f78
[1788155587.157] [547289:547373] [EM] Rxd Ack; Removing MessageCounter:111788299 from Retrans Table on exchange 864i
[1788155587.214] [547289:547373] [EM] >>> [E:864i S:0 M:52138055 (Ack:111788299)] (U) Msg RX from 0:0000000000000000 [0000] to C48046684CDB7D27 --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:752)
[1788155587.214] [547289:547373] [EM] Found matching exchange: 864i, Delegate: 0xffff90015f78
[1788155587.214] [547289:547373] [EM] CHIP MessageCounter:111788299 not in RetransTable on exchange 864i
[1788155587.214] [547289:547373] [SC] Received Sigma2 msg
[1788155587.214] [547289:547373] [SC] Found MRP parameters in the message
[1788155587.219] [547289:547373] [SC] Peer <00000000000008CA, 1> assigned session ID 61771
[1788155587.219] [547289:547373] [SC] Sending Sigma3
[1788155587.228] [547289:547373] [EM] <<< [E:864i S:0 M:111788300 (Ack:52138055)] (U) Msg TX from C48046684CDB7D27 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[1788155587.228] [547289:547373] [EM] ??1 [E:864i S:0 M:111788300] (U) Msg Retransmission to 0:0000000000000000 scheduled for 2265ms from now [State:Active II:2000 AI:2000 AT:4000]
[1788155587.228] [547289:547373] [SC] Sent Sigma3 msg
[1788155587.401] [547289:547373] [EM] >>> [E:864i S:0 M:52138056 (Ack:111788300)] (U) Msg RX from 0:0000000000000000 [0000] to C48046684CDB7D27 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788155587.401] [547289:547373] [EM] Found matching exchange: 864i, Delegate: 0xffff90015f78
[1788155587.401] [547289:547373] [EM] Rxd Ack; Removing MessageCounter:111788300 from Retrans Table on exchange 864i
[1788155587.406] [547289:547373] [EM] >>> [E:864i S:0 M:52138057 (Ack:111788300)] (U) Msg RX from 0:0000000000000000 [0000] to C48046684CDB7D27 --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[1788155587.406] [547289:547373] [EM] Found matching exchange: 864i, Delegate: 0xffff90015f78
[1788155587.406] [547289:547373] [EM] CHIP MessageCounter:111788300 not in RetransTable on exchange 864i
[1788155587.407] [547289:547373] [SC] Success status report received. Session was established
[1788155587.410] [547289:547373] [SC] SecureSession[0xffff90019f20, LSID:44801]: State change 'kEstablishing' --> 'kActive'
[1788155587.410] [547289:547373] [IN] SecureSession[0xffff90019f20]: Activated - Type:2 LSID:44801
[1788155587.410] [547289:547373] [IN] New secure session activated for device <00000000000008CA, 1>, LSID:44801 PSID:61771!
[1788155587.410] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 4 --> 5
[1788155587.410] [547289:547373] [CTL] Successfully finished commissioning step 'FindOperationalForStayActive'
[1788155587.410] [547289:547373] [CTL] Commissioning stage next step: 'FindOperationalForStayActive' -> 'ICDSendStayActive'
[1788155587.410] [547289:547373] [CTL] Performing next commissioning step 'ICDSendStayActive'
[1788155587.410] [547289:547373] [TOO] Starting commissioning stage 'ICDSendStayActive'
[1788155587.410] [547289:547373] [CTL] Skipping kICDSendStayActive
[1788155587.410] [547289:547373] [CTL] Successfully finished commissioning step 'ICDSendStayActive'
[1788155587.410] [547289:547373] [CTL] Commissioning stage next step: 'ICDSendStayActive' -> 'FindOperationalForCommissioningComplete'
[1788155587.410] [547289:547373] [CTL] Performing next commissioning step 'FindOperationalForCommissioningComplete'
[1788155587.410] [547289:547373] [TOO] Starting commissioning stage 'FindOperationalForCommissioningComplete'
[1788155587.410] [547289:547373] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CA]
[1788155587.410] [547289:547373] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1788155587.410] [547289:547373] [DIS] Found an existing secure session to [1:00000000000008CA]!
[1788155587.410] [547289:547373] [DIS] OperationalSessionSetup[1:00000000000008CA]: State change 1 --> 5
[1788155587.410] [547289:547373] [CTL] Successfully finished commissioning step 'FindOperationalForCommissioningComplete'
[1788155587.410] [547289:547373] [CTL] Commissioning stage next step: 'FindOperationalForCommissioningComplete' -> 'SendComplete'
[1788155587.410] [547289:547373] [CTL] Performing next commissioning step 'SendComplete'
[1788155587.410] [547289:547373] [TOO] Starting commissioning stage 'SendComplete'
[1788155587.410] [547289:547373] [DMG] ICR moving to [AddingComm]
[1788155587.410] [547289:547373] [DMG] ICR moving to [AddedComma]
[1788155587.411] [547289:547373] [EM] <<< [E:865i S:44801 M:86523146] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [CAF4] [UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[1788155587.411] [547289:547373] [EM] ??1 [E:865i S:44801 M:86523146] (S) Msg Retransmission to 1:00000000000008CA scheduled for 2463ms from now [State:Active II:2000 AI:2000 AT:4000]
[1788155587.411] [547289:547373] [DMG] ICR moving to [AwaitingRe]
[1788155587.411] [547289:547373] [EM] <<< [E:864i S:0 M:111788301 (Ack:52138057)] (U) Msg TX from C48046684CDB7D27 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[1788155587.411] [547289:547373] [EM] Flushed pending ack for MessageCounter:52138057 on exchange 864i
[1788155587.474] [547289:547373] [EM] >>> [E:865i S:44801 M:247742570 (Ack:86523146)] (S) Msg RX from 1:00000000000008CA [CAF4] to 000000000001B669 --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1788155587.474] [547289:547373] [EM] Found matching exchange: 865i, Delegate: 0xffff90014458
[1788155587.474] [547289:547373] [EM] Rxd Ack; Removing MessageCounter:86523146 from Retrans Table on exchange 865i
[1788155587.474] [547289:547373] [DMG] ICR moving to [ResponseRe]
[1788155587.474] [547289:547373] [DMG] InvokeResponseMessage =
[1788155587.474] [547289:547373] [DMG] {
[1788155587.474] [547289:547373] [DMG]  suppressResponse = false,
[1788155587.474] [547289:547373] [DMG]  InvokeResponseIBs =
[1788155587.474] [547289:547373] [DMG]  [
[1788155587.474] [547289:547373] [DMG]          InvokeResponseIB =
[1788155587.474] [547289:547373] [DMG]          {
[1788155587.474] [547289:547373] [DMG]                  CommandDataIB =
[1788155587.474] [547289:547373] [DMG]                  {
[1788155587.474] [547289:547373] [DMG]                          CommandPathIB =
[1788155587.474] [547289:547373] [DMG]                          {
[1788155587.474] [547289:547373] [DMG]                                  EndpointId = 0x0,
[1788155587.474] [547289:547373] [DMG]                                  ClusterId = 0x30,
[1788155587.474] [547289:547373] [DMG]                                  CommandId = 0x5,
[1788155587.474] [547289:547373] [DMG]                          },
[1788155587.474] [547289:547373] [DMG]
[1788155587.474] [547289:547373] [DMG]                          CommandFields =
[1788155587.474] [547289:547373] [DMG]                          {
[1788155587.474] [547289:547373] [DMG]                                  0x0 = 0 (unsigned),
[1788155587.474] [547289:547373] [DMG]                                  0x1 = "" (0 chars),
[1788155587.474] [547289:547373] [DMG]                          },
[1788155587.475] [547289:547373] [DMG]                  },
[1788155587.475] [547289:547373] [DMG]
[1788155587.475] [547289:547373] [DMG]          },
[1788155587.475] [547289:547373] [DMG]
[1788155587.475] [547289:547373] [DMG]  ],
[1788155587.475] [547289:547373] [DMG]
[1788155587.475] [547289:547373] [DMG]  InteractionModelRevision = 12
[1788155587.475] [547289:547373] [DMG] },
[1788155587.475] [547289:547373] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0005
[1788155587.475] [547289:547373] [CTL] Received CommissioningComplete response, errorCode=0
[1788155587.475] [547289:547373] [CTL] Successfully finished commissioning step 'SendComplete'
[1788155587.475] [547289:547373] [CTL] Commissioning stage next step: 'SendComplete' -> 'Cleanup'
[1788155587.475] [547289:547373] [CTL] Performing next commissioning step 'Cleanup'
[1788155587.475] [547289:547373] [TOO] Starting commissioning stage 'Cleanup'
[1788155587.475] [547289:547373] [CTL] Successfully finished commissioning step 'Cleanup'
[1788155587.475] [547289:547373] [DIS] Closing all BLE connections
[1788155587.475] [547289:547373] [IN] Clearing BLE pending packets.
[1788155587.476] [547289:547373] [BLE] Auto-closing end point's BLE connection.
[1788155587.476] [547289:547373] [DL] Closing BLE GATT connection (con 0xffff8405ef20)
[1788155587.476] [547289:547313] [DL] Close BLE connection: peer=CD:3A:AA:3B:8B:66
[1788155588.004] [547289:547313] [DL] BLE connection closed: conn=0xffff8405ef20
[1788155588.004] [547289:547373] [IN] SecureSession[0xffff90002c60]: MarkForEviction Type:1 LSID:44800
[1788155588.004] [547289:547373] [SC] SecureSession[0xffff90002c60, LSID:44800]: State change 'kActive' --> 'kPendingEviction'
[1788155588.005] [547289:547373] [IN] SecureSession[0xffff90002c60]: Released - Type:1 LSID:44800
[1788155588.005] [547289:547373] [CTL] Commissioning complete for node ID 0x00000000000008CA: success
[1788155588.005] [547289:547373] [TOO] Device commissioning completed with success
[1788155588.005] [547289:547373] [DMG] ICR moving to [AwaitingDe]
[1788155588.005] [547289:547373] [EM] <<< [E:865i S:44801 M:86523147 (Ack:247742570)] (S) Msg TX from 000000000001B669 to 1:00000000000008CA [CAF4] [UDP:[fd00:dcff:665f:1:42d6:136b:a2e1:6bb9]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[1788155588.005] [547289:547373] [EM] Flushed pending ack for MessageCounter:247742570 on exchange 865i
[1788155588.005] [547289:547373] [BLE] No endpoint for unsubscribe complete
[1788155588.005] [547289:547373] [BLE] No endpoint for connection error
[1788155588.005] [547289:547373] [DL] Freeing BLE connection: conn=0xffff8405ef20
[1788155588.006] [547289:547289] [CTL] Shutting down the commissioner
[1788155588.006] [547289:547289] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788155588.006] [547289:547289] [CTL] Shutting down the controller
[1788155588.006] [547289:547289] [IN] Expiring all sessions for fabric 0x1!!
[1788155588.006] [547289:547289] [IN] SecureSession[0xffff90019f20]: MarkForEviction Type:2 LSID:44801
[1788155588.006] [547289:547289] [SC] SecureSession[0xffff90019f20, LSID:44801]: State change 'kActive' --> 'kPendingEviction'
[1788155588.006] [547289:547289] [IN] SecureSession[0xffff90019f20]: Released - Type:2 LSID:44801
[1788155588.006] [547289:547289] [FP] Forgetting fabric 0x1
[1788155588.006] [547289:547289] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1788155588.006] [547289:547289] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1788155588.006] [547289:547289] [TS] Reverted Last Known Good Time to previous value
[1788155588.006] [547289:547289] [CTL] Shutting down the commissioner
[1788155588.007] [547289:547289] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788155588.007] [547289:547289] [CTL] Shutting down the controller
[1788155588.007] [547289:547289] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1788155588.007] [547289:547289] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1788155588.007] [547289:547289] [FP] Shutting down FabricTable
[1788155588.007] [547289:547289] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1788155588.008] [547289:547289] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1788155588.008] [547289:547289] [TS] Reverted Last Known Good Time to previous value
[1788155588.014] [547289:547289] [DL] Wrote settings to /tmp/chip_counters.ini
[1788155588.014] [547289:547289] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1788155588.014] [547289:547289] [DL] Inet Layer shutdown
[1788155588.014] [547289:547289] [DL] BLE Layer shutdown
[1788155588.017] [547289:547289] [DL] WiFi-PAF Layer shutdown
[1788155588.017] [547289:547289] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1788155588.017] [547289:547289] [DL] System Layer shutdown
```