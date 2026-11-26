
```c
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2252 hex:0e080000000000010000000300001a35060004001fffe00208099471b525eb93d80708fda811a6aeb9b724051036fa5c3baff144a93e50b1e02118b44d030f4f70656e5468726561642d373938610102798a0410aaa3ba1a03fc3b75d05387a2cc81df5e0c0402a0f7f8 20202021 3840
[1770360080.106] [1704:1704] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770360080.121] [1704:1704] [DL] Wrote settings to /tmp/chip_tool_kvs
[1770360080.133] [1704:1704] [DL] ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs, IGNORING.
[1770360080.151] [1704:1704] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1770360080.158] [1704:1704] [DL] Wrote settings to /tmp/chip_factory.ini
[1770360080.158] [1704:1704] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1770360080.165] [1704:1704] [DL] Wrote settings to /tmp/chip_config.ini
[1770360080.165] [1704:1704] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters.ini
[1770360080.172] [1704:1704] [DL] Wrote settings to /tmp/chip_counters.ini
[1770360080.184] [1704:1704] [DL] Wrote settings to /tmp/chip_config.ini
[1770360080.184] [1704:1704] [DL] NVS set: chip-config/unique-id = "5B02D93668568806"
[1770360080.196] [1704:1704] [DL] Wrote settings to /tmp/chip_factory.ini
[1770360080.196] [1704:1704] [DL] NVS set: chip-factory/vendor-id = 65521 (0xFFF1)
[1770360080.205] [1704:1704] [DL] Wrote settings to /tmp/chip_factory.ini
[1770360080.205] [1704:1704] [DL] NVS set: chip-factory/product-id = 32769 (0x8001)
[1770360080.214] [1704:1704] [DL] Wrote settings to /tmp/chip_counters.ini
[1770360080.214] [1704:1704] [DL] NVS set: chip-counters/reboot-count = 1 (0x1)
[1770360080.224] [1704:1704] [DL] Wrote settings to /tmp/chip_counters.ini
[1770360080.224] [1704:1704] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770360080.234] [1704:1704] [DL] Wrote settings to /tmp/chip_counters.ini
[1770360080.234] [1704:1704] [DL] NVS set: chip-counters/boot-reason = 0 (0x0)
[1770360080.248] [1704:1704] [DL] Wrote settings to /tmp/chip_config.ini
[1770360080.248] [1704:1704] [DL] NVS set: chip-config/regulatory-location = 0 (0x0)
[1770360080.260] [1704:1704] [DL] Wrote settings to /tmp/chip_config.ini
[1770360080.261] [1704:1704] [DL] NVS set: chip-config/location-capability = 2 (0x2)
[1770360080.281] [1704:1704] [DL] Wrote settings to /tmp/chip_config.ini
[1770360080.281] [1704:1704] [DL] NVS set: chip-config/configuration-version = 1 (0x1)
[1770360080.283] [1704:1704] [DL] Got Ethernet interface: eth0
[1770360080.285] [1704:1704] [DL] Found the primary Ethernet interface:eth0
[1770360080.287] [1704:1704] [DL] Got WiFi interface: wlan0
[1770360080.287] [1704:1704] [DL] Failed to reset WiFi statistic counts
[1770360080.287] [1704:1704] [PAF] WiFiPAF: WiFiPAFLayer::Init()
[1770360080.475] [1704:1704] [IN] UDP::Init bind&listen port=0
[1770360080.475] [1704:1704] [IN] UDP::Init bound to port=56553
[1770360080.475] [1704:1704] [IN] BLEBase::Init - setting/overriding transport
[1770360080.475] [1704:1704] [IN] WiFiPAFBase::Init - setting/overriding transport
[1770360080.475] [1704:1704] [CTL] NFCBase::Init
[1770360080.475] [1704:1704] [IN] TransportMgr initialized
[1770360080.476] [1704:1704] [FP] Initializing FabricTable from persistent storage
[1770360080.476] [1704:1704] [TS] Last Known Good Time: [unknown]
[1770360080.476] [1704:1704] [TS] Setting Last Known Good Time to firmware build time 2023-10-14T01:16:48
[1770360080.486] [1704:1704] [DMG] Ember attribute persistence requires setting up
[1770360080.486] [1704:1704] [ZCL] Using ZAP configuration...
[1770360080.493] [1704:1704] [CTL] System State Initialized...
[1770360080.520] [1704:1704] [CTL] Setting attestation nonce to random value
[1770360080.520] [1704:1704] [CTL] Setting CSR nonce to random value
[1770360080.520] [1704:1704] [IN] UDP::Init bind&listen port=5550
[1770360080.521] [1704:1704] [IN] UDP::Init bound to port=5550
[1770360080.521] [1704:1704] [IN] TransportMgr initialized
[1770360080.524] [1704:1720] [DL] CHIP task running
[1770360080.525] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 32786
[1770360080.527] [1704:1720] [CTL] Setting attestation nonce to random value
[1770360080.527] [1704:1720] [CTL] Setting CSR nonce to random value
[1770360080.528] [1704:1720] [CTL] Couldn't get ExampleOpCredsCAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770360080.531] [1704:1720] [CTL] Couldn't get ExampleOpCredsICAKey from storage: src/controller/ExamplePersistentStorage.cpp:112: CHIP Error 0x000000A0: Value not found in the persisted storage
[1770360080.534] [1704:1720] [CTL] Generating RCAC
[1770360080.538] [1704:1720] [CTL] Generating ICAC
[1770360080.541] [1704:1720] [CTL] Generating NOC
[1770360080.542] [1704:1720] [FP] Validating NOC chain
[1770360080.547] [1704:1720] [FP] NOC chain validation successful
[1770360080.548] [1704:1720] [FP] Added new fabric at index: 0x1
[1770360080.548] [1704:1720] [FP] Assigned compressed fabric ID: 0x46E039287128F8B5, node ID: 0x000000000001B669
[1770360080.548] [1704:1720] [TS] Last Known Good Time: 2023-10-14T01:16:48
[1770360080.548] [1704:1720] [TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[1770360080.548] [1704:1720] [TS] Retaining current Last Known Good Time
[1770360080.551] [1704:1720] [FP] Metadata for Fabric 0x1 persisted to storage.
[1770360080.555] [1704:1720] [TS] Committing Last Known Good Time to storage: 2023-10-14T01:16:48
[1770360080.564] [1704:1720] [CTL] Joined the fabric at index 1. Fabric ID is 0x0000000000000001 (Compressed Fabric ID: 46E039287128F8B5)
[1770360080.564] [1704:1720] [IN] UDP::Init bind&listen port=5551
[1770360080.564] [1704:1720] [IN] UDP::Init bound to port=5551
[1770360080.564] [1704:1720] [IN] TransportMgr initialized
[1770360080.647] [1704:1720] [CTL] Setting thread operational dataset from parameters
[1770360080.647] [1704:1720] [CTL] Setting attestation nonce to random value
[1770360080.647] [1704:1720] [CTL] Setting CSR nonce to random value
[1770360080.647] [1704:1720] [CTL] Commission called for node ID 0x00000000000008CC
[1770360080.647] [1704:1720] [DL] Long dispatch time: 122 ms, for event type 2
[1770360080.687] [1704:1711] [BLE] BLE removing known devices
[1770360080.693] [1704:1711] [BLE] BLE initiating scan
[1770360080.700] [1704:1720] [BLE] ChipDeviceScanner has started scanning!
[1770360080.745] [1704:1711] [BLE] Device 08:12:87:DC:C8:5F does not look like a CHIP device.
[1770360080.752] [1704:1711] [BLE] Device D3:35:6C:9C:EF:2E does not look like a CHIP device.
[1770360080.763] [1704:1711] [BLE] Device 08:12:87:DC:C8:5F does not look like a CHIP device.
[1770360080.779] [1704:1711] [BLE] Device 5A:45:62:DB:34:22 does not look like a CHIP device.
[1770360080.781] [1704:1711] [BLE] Device 15:E1:86:C5:BA:A3 does not look like a CHIP device.
[1770360080.793] [1704:1711] [BLE] Device 08:12:87:DC:C8:5F does not look like a CHIP device.
[1770360080.806] [1704:1711] [BLE] Device 2C:BA:BA:99:E6:A0 does not look like a CHIP device.
[1770360080.818] [1704:1711] [BLE] New device scanned: E0:F0:A0:52:CD:52
[1770360080.818] [1704:1711] [BLE] Device discriminator match. Attempting to connect.
[1770360080.824] [1704:1711] [BLE] ChipDeviceScanner has stopped scanning!
[1770360081.372] [1704:1711] [DL] FAIL: ConnectDevice: GDBus.Error:org.bluez.Error.Failed: le-connection-abort-by-local (36)
[1770360081.372] [1704:1711] [DL] ConnectDevice retry: 1 out of 4
[1770360082.018] [1704:1711] [DL] FAIL: ConnectDevice: GDBus.Error:org.bluez.Error.Failed: le-connection-abort-by-local (36)
[1770360082.018] [1704:1711] [DL] ConnectDevice retry: 2 out of 4
[1770360082.789] [1704:1711] [DL] ConnectDevice complete
[1770360082.789] [1704:1711] [BLE] New device connected: E0:F0:A0:52:CD:52
[1770360086.111] [1704:1711] [DL] CHIP service found
[1770360086.111] [1704:1711] [DL] Valid C2 characteristic found
[1770360086.111] [1704:1711] [DL] Valid C1 characteristic found
[1770360086.112] [1704:1711] [DL] New BLE connection: conn=0xffff8802a540 device=E0:F0:A0:52:CD:52 path=/org/bluez/hci0/dev_E0_F0_A0_52_CD_52
[1770360086.112] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16387
[1770360086.112] [1704:1720] [DIS] Closing all BLE connections
[1770360086.112] [1704:1720] [IN] BleConnectionComplete: endPoint 0xaaaac70b6fd0
[1770360086.114] [1704:1720] [IN] SecureSession[0xffff80022cd0]: Allocated Type:1 LSID:26730
[1770360086.114] [1704:1720] [SC] Assigned local session key ID 26730
[1770360086.114] [1704:1720] [EM] <<< [E:28674i S:0 M:66215661] (U) Msg TX from 0EAEA12C5F55C41E to 0:0000000000000000 [0000] [BLE] --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[1770360086.114] [1704:1720] [IN] Message appended to BLE send queue
[1770360086.114] [1704:1720] [SC] Sent PBKDF param request [II:500ms AI:300ms AT:4000ms)
[1770360087.249] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360087.542] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16390
[1770360087.543] [1704:1720] [BLE] subscribe complete, ep = 0xaaaac70b6fd0
[1770360087.543] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360087.543] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360087.544] [1704:1720] [BLE] peripheral chose BTP version 4; central expected between 4 and 4
[1770360087.544] [1704:1720] [BLE] using BTP fragment sizes rx 244 / tx 244.
[1770360087.544] [1704:1720] [BLE] local and remote recv window size = 5
[1770360087.545] [1704:1720] [IN] BLE EndPoint 0xaaaac70b6fd0 Connection Complete
[1770360087.931] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360088.225] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360088.225] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360088.226] [1704:1720] [EM] >>> [E:28674i S:0 M:34986952] (U) Msg RX from 0:0000000000000000 [0000] to 0EAEA12C5F55C41E --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[1770360088.226] [1704:1720] [EM] Found matching exchange: 28674i, Delegate: 0xffff80021818
[1770360088.226] [1704:1720] [SC] Received PBKDF param response
[1770360088.226] [1704:1720] [SC] Peer assigned session ID 31156
[1770360088.226] [1704:1720] [SC] Found MRP parameters in the message
[1770360088.244] [1704:1720] [EM] <<< [E:28674i S:0 M:66215662] (U) Msg TX from 0EAEA12C5F55C41E to 0:0000000000000000 [0000] [BLE] --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[1770360088.245] [1704:1720] [SC] Sent spake2p msg1
[1770360088.418] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360088.517] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360088.517] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360088.517] [1704:1720] [EM] >>> [E:28674i S:0 M:34986953] (U) Msg RX from 0:0000000000000000 [0000] to 0EAEA12C5F55C41E --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[1770360088.517] [1704:1720] [EM] Found matching exchange: 28674i, Delegate: 0xffff80021818
[1770360088.518] [1704:1720] [SC] Received spake2p msg2
[1770360088.522] [1704:1720] [EM] <<< [E:28674i S:0 M:66215663] (U) Msg TX from 0EAEA12C5F55C41E to 0:0000000000000000 [0000] [BLE] --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[1770360088.524] [1704:1720] [SC] Sent spake2p msg3
[1770360088.906] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360089.004] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360089.005] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360089.005] [1704:1720] [EM] >>> [E:28674i S:0 M:34986954] (U) Msg RX from 0:0000000000000000 [0000] to 0EAEA12C5F55C41E --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[1770360089.005] [1704:1720] [EM] Found matching exchange: 28674i, Delegate: 0xffff80021818
[1770360089.006] [1704:1720] [SC] SecureSession[0xffff80022cd0, LSID:26730]: State change 'kEstablishing' --> 'kActive'
[1770360089.006] [1704:1720] [IN] SecureSession[0xffff80022cd0]: Activated - Type:1 LSID:26730
[1770360089.006] [1704:1720] [IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:26730 PSID:31156!
[1770360089.006] [1704:1720] [CTL] Remote device completed SPAKE2+ handshake
[1770360089.006] [1704:1720] [TOO] Pairing Success
[1770360089.006] [1704:1720] [TOO] PASE establishment successful
[1770360089.006] [1704:1720] [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'
[1770360089.007] [1704:1720] [CTL] Performing next commissioning step 'ReadCommissioningInfo'
[1770360089.007] [1704:1720] [CTL] Sending read requests for commissioning information
[1770360089.007] [1704:1720] [DMG] SendReadRequest ReadClient[0xffff80022ae0]: Sending Read Request
[1770360089.012] [1704:1720] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770360089.013] [1704:1720] [EM] <<< [E:28675i S:26730 M:214419314] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:134)
[1770360089.014] [1704:1720] [DMG] MoveToState ReadClient[0xffff80022ae0]: Moving to [AwaitingIn]
[1770360089.014] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 32792
[1770360089.393] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360089.979] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360089.980] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360090.370] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360090.370] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360090.371] [1704:1720] [EM] >>> [E:28675i S:26730 M:34177120] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:257)
[1770360090.371] [1704:1720] [EM] Found matching exchange: 28675i, Delegate: 0xffff80022af0
[1770360090.371] [1704:1720] [DMG] ReportDataMessage =
[1770360090.371] [1704:1720] [DMG] {
[1770360090.371] [1704:1720] [DMG]      AttributeReportIBs =
[1770360090.371] [1704:1720] [DMG]      [
[1770360090.371] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.372] [1704:1720] [DMG]              {
[1770360090.372] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.372] [1704:1720] [DMG]                      {
[1770360090.372] [1704:1720] [DMG]                              DataVersion = 0xfa4f5ffc,
[1770360090.372] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.372] [1704:1720] [DMG]                              {
[1770360090.373] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.373] [1704:1720] [DMG]                                      Cluster = 0x31,
[1770360090.374] [1704:1720] [DMG]                                      Attribute = 0x0000_FFFC,
[1770360090.374] [1704:1720] [DMG]                              }
[1770360090.374] [1704:1720] [DMG]
[1770360090.374] [1704:1720] [DMG]                              Data = 2 (unsigned),
[1770360090.374] [1704:1720] [DMG]                      },
[1770360090.374] [1704:1720] [DMG]
[1770360090.375] [1704:1720] [DMG]              },
[1770360090.375] [1704:1720] [DMG]
[1770360090.375] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.375] [1704:1720] [DMG]              {
[1770360090.375] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.375] [1704:1720] [DMG]                      {
[1770360090.375] [1704:1720] [DMG]                              DataVersion = 0x90efe910,
[1770360090.375] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.375] [1704:1720] [DMG]                              {
[1770360090.376] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.376] [1704:1720] [DMG]                                      Cluster = 0x28,
[1770360090.376] [1704:1720] [DMG]                                      Attribute = 0x0000_0004,
[1770360090.376] [1704:1720] [DMG]                              }
[1770360090.376] [1704:1720] [DMG]
[1770360090.376] [1704:1720] [DMG]                              Data = 32784 (unsigned),
[1770360090.376] [1704:1720] [DMG]                      },
[1770360090.377] [1704:1720] [DMG]
[1770360090.377] [1704:1720] [DMG]              },
[1770360090.377] [1704:1720] [DMG]
[1770360090.377] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.377] [1704:1720] [DMG]              {
[1770360090.377] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.377] [1704:1720] [DMG]                      {
[1770360090.377] [1704:1720] [DMG]                              DataVersion = 0x90efe910,
[1770360090.377] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.378] [1704:1720] [DMG]                              {
[1770360090.378] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.378] [1704:1720] [DMG]                                      Cluster = 0x28,
[1770360090.378] [1704:1720] [DMG]                                      Attribute = 0x0000_0002,
[1770360090.378] [1704:1720] [DMG]                              }
[1770360090.378] [1704:1720] [DMG]
[1770360090.378] [1704:1720] [DMG]                              Data = 65521 (unsigned),
[1770360090.378] [1704:1720] [DMG]                      },
[1770360090.378] [1704:1720] [DMG]
[1770360090.378] [1704:1720] [DMG]              },
[1770360090.378] [1704:1720] [DMG]
[1770360090.378] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.379] [1704:1720] [DMG]              {
[1770360090.379] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.379] [1704:1720] [DMG]                      {
[1770360090.379] [1704:1720] [DMG]                              DataVersion = 0xb127cfb,
[1770360090.379] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.379] [1704:1720] [DMG]                              {
[1770360090.379] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.379] [1704:1720] [DMG]                                      Cluster = 0x30,
[1770360090.379] [1704:1720] [DMG]                                      Attribute = 0x0000_0003,
[1770360090.379] [1704:1720] [DMG]                              }
[1770360090.379] [1704:1720] [DMG]
[1770360090.380] [1704:1720] [DMG]                              Data = 0 (unsigned),
[1770360090.380] [1704:1720] [DMG]                      },
[1770360090.380] [1704:1720] [DMG]
[1770360090.380] [1704:1720] [DMG]              },
[1770360090.380] [1704:1720] [DMG]
[1770360090.380] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.380] [1704:1720] [DMG]              {
[1770360090.380] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.380] [1704:1720] [DMG]                      {
[1770360090.380] [1704:1720] [DMG]                              DataVersion = 0xb127cfb,
[1770360090.380] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.380] [1704:1720] [DMG]                              {
[1770360090.380] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.380] [1704:1720] [DMG]                                      Cluster = 0x30,
[1770360090.381] [1704:1720] [DMG]                                      Attribute = 0x0000_0002,
[1770360090.381] [1704:1720] [DMG]                              }
[1770360090.381] [1704:1720] [DMG]
[1770360090.381] [1704:1720] [DMG]                              Data = 0 (unsigned),
[1770360090.381] [1704:1720] [DMG]                      },
[1770360090.381] [1704:1720] [DMG]
[1770360090.381] [1704:1720] [DMG]              },
[1770360090.382] [1704:1720] [DMG]
[1770360090.382] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.382] [1704:1720] [DMG]              {
[1770360090.382] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.382] [1704:1720] [DMG]                      {
[1770360090.382] [1704:1720] [DMG]                              DataVersion = 0xb127cfb,
[1770360090.383] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.383] [1704:1720] [DMG]                              {
[1770360090.383] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.384] [1704:1720] [DMG]                                      Cluster = 0x30,
[1770360090.384] [1704:1720] [DMG]                                      Attribute = 0x0000_0001,
[1770360090.384] [1704:1720] [DMG]                              }
[1770360090.385] [1704:1720] [DMG]
[1770360090.385] [1704:1720] [DMG]                              Data =
[1770360090.385] [1704:1720] [DMG]                              {
[1770360090.385] [1704:1720] [DMG]                                      0x0 = 60 (unsigned),
[1770360090.385] [1704:1720] [DMG]                                      0x1 = 900 (unsigned),
[1770360090.385] [1704:1720] [DMG]                              },
[1770360090.385] [1704:1720] [DMG]                      },
[1770360090.385] [1704:1720] [DMG]
[1770360090.385] [1704:1720] [DMG]              },
[1770360090.385] [1704:1720] [DMG]
[1770360090.385] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.385] [1704:1720] [DMG]              {
[1770360090.386] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.386] [1704:1720] [DMG]                      {
[1770360090.386] [1704:1720] [DMG]                              DataVersion = 0xb127cfb,
[1770360090.386] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.386] [1704:1720] [DMG]                              {
[1770360090.386] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.386] [1704:1720] [DMG]                                      Cluster = 0x30,
[1770360090.386] [1704:1720] [DMG]                                      Attribute = 0x0000_0000,
[1770360090.386] [1704:1720] [DMG]                              }
[1770360090.386] [1704:1720] [DMG]
[1770360090.386] [1704:1720] [DMG]                              Data = 0 (unsigned),
[1770360090.387] [1704:1720] [DMG]                      },
[1770360090.387] [1704:1720] [DMG]
[1770360090.387] [1704:1720] [DMG]              },
[1770360090.387] [1704:1720] [DMG]
[1770360090.387] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.387] [1704:1720] [DMG]              {
[1770360090.387] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.387] [1704:1720] [DMG]                      {
[1770360090.387] [1704:1720] [DMG]                              DataVersion = 0xb127cfb,
[1770360090.387] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.387] [1704:1720] [DMG]                              {
[1770360090.387] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.387] [1704:1720] [DMG]                                      Cluster = 0x30,
[1770360090.388] [1704:1720] [DMG]                                      Attribute = 0x0000_0004,
[1770360090.388] [1704:1720] [DMG]                              }
[1770360090.388] [1704:1720] [DMG]
[1770360090.388] [1704:1720] [DMG]                              Data = true,
[1770360090.388] [1704:1720] [DMG]                      },
[1770360090.388] [1704:1720] [DMG]
[1770360090.388] [1704:1720] [DMG]              },
[1770360090.388] [1704:1720] [DMG]
[1770360090.388] [1704:1720] [DMG]      ],
[1770360090.388] [1704:1720] [DMG]
[1770360090.388] [1704:1720] [DMG]      SuppressResponse = true,
[1770360090.388] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360090.388] [1704:1720] [DMG] }
[1770360090.390] [1704:1720] [DMG] SendReadRequest ReadClient[0xffff80022ae0]: Sending Read Request
[1770360090.391] [1704:1720] [DMG] 0 data version filters provided, 0 not relevant, 0 encoded, 0 skipped due to lack of space
[1770360090.391] [1704:1720] [EM] <<< [E:28676i S:26730 M:214419315] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:02 (IM:ReadRequest) (B:103)
[1770360090.392] [1704:1720] [DMG] MoveToState ReadClient[0xffff80022ae0]: Moving to [AwaitingIn]
[1770360090.659] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360090.860] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360090.860] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360090.861] [1704:1720] [EM] >>> [E:28676i S:26730 M:34177121] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:05 (IM:ReportData) (B:191)
[1770360090.861] [1704:1720] [EM] Found matching exchange: 28676i, Delegate: 0xffff80022af0
[1770360090.861] [1704:1720] [DMG] ReportDataMessage =
[1770360090.861] [1704:1720] [DMG] {
[1770360090.861] [1704:1720] [DMG]      AttributeReportIBs =
[1770360090.861] [1704:1720] [DMG]      [
[1770360090.862] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.862] [1704:1720] [DMG]              {
[1770360090.862] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.862] [1704:1720] [DMG]                      {
[1770360090.862] [1704:1720] [DMG]                              DataVersion = 0x12c36da4,
[1770360090.862] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.862] [1704:1720] [DMG]                              {
[1770360090.863] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.863] [1704:1720] [DMG]                                      Cluster = 0x46,
[1770360090.863] [1704:1720] [DMG]                                      Attribute = 0x0000_0002,
[1770360090.863] [1704:1720] [DMG]                              }
[1770360090.863] [1704:1720] [DMG]
[1770360090.863] [1704:1720] [DMG]                              Data = 0 (unsigned),
[1770360090.863] [1704:1720] [DMG]                      },
[1770360090.864] [1704:1720] [DMG]
[1770360090.864] [1704:1720] [DMG]              },
[1770360090.864] [1704:1720] [DMG]
[1770360090.864] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.864] [1704:1720] [DMG]              {
[1770360090.864] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.864] [1704:1720] [DMG]                      {
[1770360090.864] [1704:1720] [DMG]                              DataVersion = 0x12c36da4,
[1770360090.864] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.864] [1704:1720] [DMG]                              {
[1770360090.864] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.865] [1704:1720] [DMG]                                      Cluster = 0x46,
[1770360090.865] [1704:1720] [DMG]                                      Attribute = 0x0000_0001,
[1770360090.865] [1704:1720] [DMG]                              }
[1770360090.865] [1704:1720] [DMG]
[1770360090.865] [1704:1720] [DMG]                              Data = 0 (unsigned),
[1770360090.865] [1704:1720] [DMG]                      },
[1770360090.865] [1704:1720] [DMG]
[1770360090.865] [1704:1720] [DMG]              },
[1770360090.865] [1704:1720] [DMG]
[1770360090.866] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.866] [1704:1720] [DMG]              {
[1770360090.866] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.866] [1704:1720] [DMG]                      {
[1770360090.866] [1704:1720] [DMG]                              DataVersion = 0x12c36da4,
[1770360090.866] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.866] [1704:1720] [DMG]                              {
[1770360090.866] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.866] [1704:1720] [DMG]                                      Cluster = 0x46,
[1770360090.866] [1704:1720] [DMG]                                      Attribute = 0x0000_0000,
[1770360090.866] [1704:1720] [DMG]                              }
[1770360090.866] [1704:1720] [DMG]
[1770360090.867] [1704:1720] [DMG]                              Data = 600 (unsigned),
[1770360090.867] [1704:1720] [DMG]                      },
[1770360090.867] [1704:1720] [DMG]
[1770360090.867] [1704:1720] [DMG]              },
[1770360090.867] [1704:1720] [DMG]
[1770360090.867] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.867] [1704:1720] [DMG]              {
[1770360090.867] [1704:1720] [DMG]                      AttributeStatusIB =
[1770360090.867] [1704:1720] [DMG]                      {
[1770360090.867] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.867] [1704:1720] [DMG]                              {
[1770360090.868] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.868] [1704:1720] [DMG]                                      Cluster = 0x46,
[1770360090.868] [1704:1720] [DMG]                                      Attribute = 0x0000_0007,
[1770360090.868] [1704:1720] [DMG]                              }
[1770360090.868] [1704:1720] [DMG]
[1770360090.868] [1704:1720] [DMG]                              StatusIB =
[1770360090.868] [1704:1720] [DMG]                              {
[1770360090.868] [1704:1720] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770360090.869] [1704:1720] [DMG]                              },
[1770360090.869] [1704:1720] [DMG]
[1770360090.869] [1704:1720] [DMG]                      },
[1770360090.869] [1704:1720] [DMG]
[1770360090.869] [1704:1720] [DMG]              },
[1770360090.869] [1704:1720] [DMG]
[1770360090.869] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.869] [1704:1720] [DMG]              {
[1770360090.869] [1704:1720] [DMG]                      AttributeStatusIB =
[1770360090.869] [1704:1720] [DMG]                      {
[1770360090.870] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.870] [1704:1720] [DMG]                              {
[1770360090.870] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.870] [1704:1720] [DMG]                                      Cluster = 0x46,
[1770360090.870] [1704:1720] [DMG]                                      Attribute = 0x0000_0006,
[1770360090.870] [1704:1720] [DMG]                              }
[1770360090.870] [1704:1720] [DMG]
[1770360090.870] [1704:1720] [DMG]                              StatusIB =
[1770360090.870] [1704:1720] [DMG]                              {
[1770360090.871] [1704:1720] [DMG]                                      status = 0x86 (UNSUPPORTED_ATTRIBUTE),
[1770360090.871] [1704:1720] [DMG]                              },
[1770360090.871] [1704:1720] [DMG]
[1770360090.871] [1704:1720] [DMG]                      },
[1770360090.871] [1704:1720] [DMG]
[1770360090.871] [1704:1720] [DMG]              },
[1770360090.871] [1704:1720] [DMG]
[1770360090.871] [1704:1720] [DMG]              AttributeReportIB =
[1770360090.871] [1704:1720] [DMG]              {
[1770360090.871] [1704:1720] [DMG]                      AttributeDataIB =
[1770360090.871] [1704:1720] [DMG]                      {
[1770360090.871] [1704:1720] [DMG]                              DataVersion = 0xfa4f5ffc,
[1770360090.872] [1704:1720] [DMG]                              AttributePathIB =
[1770360090.872] [1704:1720] [DMG]                              {
[1770360090.872] [1704:1720] [DMG]                                      Endpoint = 0x0,
[1770360090.872] [1704:1720] [DMG]                                      Cluster = 0x31,
[1770360090.872] [1704:1720] [DMG]                                      Attribute = 0x0000_0003,
[1770360090.872] [1704:1720] [DMG]                              }
[1770360090.872] [1704:1720] [DMG]
[1770360090.872] [1704:1720] [DMG]                              Data = 20 (unsigned),
[1770360090.872] [1704:1720] [DMG]                      },
[1770360090.872] [1704:1720] [DMG]
[1770360090.872] [1704:1720] [DMG]              },
[1770360090.873] [1704:1720] [DMG]
[1770360090.873] [1704:1720] [DMG]      ],
[1770360090.873] [1704:1720] [DMG]
[1770360090.873] [1704:1720] [DMG]      SuppressResponse = true,
[1770360090.873] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360090.873] [1704:1720] [DMG] }
[1770360090.884] [1704:1720] [CTL] NetworkCommissioning Features: has Thread. endpointid = 0
[1770360090.884] [1704:1720] [SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010
[1770360090.884] [1704:1720] [SVR] OnReadCommissioningInfo ICD - IdleModeDuration=0 activeModeDuration=0 activeModeThreshold=0
[1770360090.884] [1704:1720] [CTL] Successfully finished commissioning step 'ReadCommissioningInfo'
[1770360090.884] [1704:1720] [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'
[1770360090.884] [1704:1720] [CTL] Performing next commissioning step 'ArmFailSafe'
[1770360090.884] [1704:1720] [CTL] Arming failsafe (60 seconds)
[1770360090.884] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360090.884] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360090.885] [1704:1720] [EM] <<< [E:28677i S:26730 M:214419316] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770360090.886] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360091.733] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360091.735] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360091.736] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360091.736] [1704:1720] [EM] >>> [E:28677i S:26730 M:34177122] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360091.736] [1704:1720] [EM] Found matching exchange: 28677i, Delegate: 0xffff8000db18
[1770360091.736] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360091.736] [1704:1720] [DMG] InvokeResponseMessage =
[1770360091.736] [1704:1720] [DMG] {
[1770360091.736] [1704:1720] [DMG]      suppressResponse = false,
[1770360091.737] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360091.737] [1704:1720] [DMG]      [
[1770360091.737] [1704:1720] [DMG]              InvokeResponseIB =
[1770360091.737] [1704:1720] [DMG]              {
[1770360091.737] [1704:1720] [DMG]                      CommandDataIB =
[1770360091.737] [1704:1720] [DMG]                      {
[1770360091.737] [1704:1720] [DMG]                              CommandPathIB =
[1770360091.737] [1704:1720] [DMG]                              {
[1770360091.737] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360091.738] [1704:1720] [DMG]                                      ClusterId = 0x30,
[1770360091.738] [1704:1720] [DMG]                                      CommandId = 0x1,
[1770360091.738] [1704:1720] [DMG]                              },
[1770360091.738] [1704:1720] [DMG]
[1770360091.738] [1704:1720] [DMG]                              CommandFields =
[1770360091.738] [1704:1720] [DMG]                              {
[1770360091.738] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360091.738] [1704:1720] [DMG]                                      0x1 = "" (0 chars),
[1770360091.739] [1704:1720] [DMG]                              },
[1770360091.739] [1704:1720] [DMG]                      },
[1770360091.739] [1704:1720] [DMG]
[1770360091.739] [1704:1720] [DMG]              },
[1770360091.739] [1704:1720] [DMG]
[1770360091.739] [1704:1720] [DMG]      ],
[1770360091.739] [1704:1720] [DMG]
[1770360091.740] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360091.740] [1704:1720] [DMG] },
[1770360091.740] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770360091.740] [1704:1720] [CTL] Received ArmFailSafe response errorCode=0
[1770360091.740] [1704:1720] [CTL] Successfully finished commissioning step 'ArmFailSafe'
[1770360091.740] [1704:1720] [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'
[1770360091.740] [1704:1720] [CTL] Performing next commissioning step 'ConfigRegulatory'
[1770360091.740] [1704:1720] [CTL] Setting Regulatory Config
[1770360091.741] [1704:1720] [CTL] Device does not support configurable regulatory location
[1770360091.741] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360091.741] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360091.741] [1704:1720] [EM] <<< [E:28678i S:26730 M:214419317] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[1770360091.742] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360091.743] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360092.220] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360092.319] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360092.319] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360092.320] [1704:1720] [EM] >>> [E:28678i S:26730 M:34177123] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360092.320] [1704:1720] [EM] Found matching exchange: 28678i, Delegate: 0xffff8000e0b8
[1770360092.320] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360092.320] [1704:1720] [DMG] InvokeResponseMessage =
[1770360092.320] [1704:1720] [DMG] {
[1770360092.320] [1704:1720] [DMG]      suppressResponse = false,
[1770360092.320] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360092.320] [1704:1720] [DMG]      [
[1770360092.320] [1704:1720] [DMG]              InvokeResponseIB =
[1770360092.321] [1704:1720] [DMG]              {
[1770360092.321] [1704:1720] [DMG]                      CommandDataIB =
[1770360092.321] [1704:1720] [DMG]                      {
[1770360092.321] [1704:1720] [DMG]                              CommandPathIB =
[1770360092.321] [1704:1720] [DMG]                              {
[1770360092.321] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360092.321] [1704:1720] [DMG]                                      ClusterId = 0x30,
[1770360092.321] [1704:1720] [DMG]                                      CommandId = 0x3,
[1770360092.322] [1704:1720] [DMG]                              },
[1770360092.322] [1704:1720] [DMG]
[1770360092.322] [1704:1720] [DMG]                              CommandFields =
[1770360092.322] [1704:1720] [DMG]                              {
[1770360092.322] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360092.322] [1704:1720] [DMG]                                      0x1 = "" (0 chars),
[1770360092.322] [1704:1720] [DMG]                              },
[1770360092.323] [1704:1720] [DMG]                      },
[1770360092.323] [1704:1720] [DMG]
[1770360092.323] [1704:1720] [DMG]              },
[1770360092.323] [1704:1720] [DMG]
[1770360092.323] [1704:1720] [DMG]      ],
[1770360092.323] [1704:1720] [DMG]
[1770360092.323] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360092.323] [1704:1720] [DMG] },
[1770360092.324] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0003
[1770360092.324] [1704:1720] [CTL] Received SetRegulatoryConfig response errorCode=0
[1770360092.324] [1704:1720] [CTL] Successfully finished commissioning step 'ConfigRegulatory'
[1770360092.324] [1704:1720] [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'ConfigureTCAcknowledgments'
[1770360092.324] [1704:1720] [CTL] Performing next commissioning step 'ConfigureTCAcknowledgments'
[1770360092.324] [1704:1720] [CTL] Setting Terms and Conditions
[1770360092.324] [1704:1720] [CTL] Setting Terms and Conditions: Skipped
[1770360092.324] [1704:1720] [CTL] Successfully finished commissioning step 'ConfigureTCAcknowledgments'

[1770360092.324] [1704:1720] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1770360092.325] [1704:1720] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770360092.325] [1704:1720] [CTL] Sending request for PAI certificate
[1770360092.325] [1704:1720] [CTL] Sending Certificate Chain request to 0xffff800217c0 device
[1770360092.325] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360092.332] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360092.332] [1704:1720] [EM] <<< [E:28679i S:26730 M:214419318] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770360092.333] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360092.333] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360092.805] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360093.293] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360093.293] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360094.170] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360094.170] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360094.561] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360094.561] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360094.561] [1704:1720] [EM] >>> [E:28679i S:26730 M:34177124] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[1770360094.561] [1704:1720] [EM] Found matching exchange: 28679i, Delegate: 0xffff8000db18
[1770360094.562] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360094.562] [1704:1720] [DMG] InvokeResponseMessage =
[1770360094.562] [1704:1720] [DMG] {
[1770360094.562] [1704:1720] [DMG]      suppressResponse = false,
[1770360094.562] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360094.562] [1704:1720] [DMG]      [
[1770360094.562] [1704:1720] [DMG]              InvokeResponseIB =
[1770360094.562] [1704:1720] [DMG]              {
[1770360094.563] [1704:1720] [DMG]                      CommandDataIB =
[1770360094.563] [1704:1720] [DMG]                      {
[1770360094.563] [1704:1720] [DMG]                              CommandPathIB =
[1770360094.563] [1704:1720] [DMG]                              {
[1770360094.563] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360094.563] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360094.563] [1704:1720] [DMG]                                      CommandId = 0x3,
[1770360094.563] [1704:1720] [DMG]                              },
[1770360094.564] [1704:1720] [DMG]
[1770360094.564] [1704:1720] [DMG]                              CommandFields =
[1770360094.564] [1704:1720] [DMG]                              {
[1770360094.564] [1704:1720] [DMG]                                      0x0 = [
[1770360094.565] [1704:1720] [DMG]                                                      0x30, 0x82, 0x01, 0xcb, 0x30, 0x82, 0x01, 0x71, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x56, 0xad, 0x82, 0x22, 0xad, 0x94, 0x5b, 0x64, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x30, 0x31, 0x18, 0x30, 0x16, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x0f, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x54, 0x65, 0x73, 0x74, 0x20, 0x50, 0x41, 0x41, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x32, 0x30, 0x35, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x41, 0x9a, 0x93, 0x15, 0xc2, 0x17, 0x3e, 0x0c, 0x8c, 0x87, 0x6d, 0x03, 0xcc, 0xfc, 0x94, 0x48, 0x52, 0x64, 0x7f, 0x7f, 0xec, 0x5e, 0x50, 0x82, 0xf4, 0x05, 0x99, 0x28, 0xec, 0xa8, 0x94, 0xc5, 0x94, 0x15, 0x13, 0x09, 0xac, 0x63, 0x1e, 0x4c, 0xb0, 0x33, 0x92, 0xaf, 0x68, 0x4b, 0x0b, 0xaf, 0xb7, 0xe6, 0x5b, 0x3b, 0x81, 0x62, 0xc2, 0xf5, 0x2b, 0xf9, 0x31, 0xb8, 0xe7, 0x7a, 0xaa, 0x82, 0xa3, 0x66, 0x30, 0x64, 0x30, 0x12, 0x06, 0x03, 0x55, 0x1d, 0x
[1770360094.565] [1704:1720] [DMG]                                      ] (463 bytes)
[1770360094.565] [1704:1720] [DMG]                              },
[1770360094.565] [1704:1720] [DMG]                      },
[1770360094.565] [1704:1720] [DMG]
[1770360094.565] [1704:1720] [DMG]              },
[1770360094.566] [1704:1720] [DMG]
[1770360094.566] [1704:1720] [DMG]      ],
[1770360094.566] [1704:1720] [DMG]
[1770360094.566] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360094.566] [1704:1720] [DMG] },
[1770360094.566] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770360094.567] [1704:1720] [CTL] Received certificate chain from the device
[1770360094.567] [1704:1720] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1770360094.567] [1704:1720] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1770360094.567] [1704:1720] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1770360094.567] [1704:1720] [CTL] Sending request for DAC certificate
[1770360094.567] [1704:1720] [CTL] Sending Certificate Chain request to 0xffff800217c0 device
[1770360094.567] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360094.567] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360094.568] [1704:1720] [EM] <<< [E:28680i S:26730 M:214419319] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1770360094.569] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360094.569] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360094.753] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360094.951] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360094.951] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360095.341] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360095.341] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360095.827] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360095.828] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360095.828] [1704:1720] [EM] >>> [E:28680i S:26730 M:34177125] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[1770360095.828] [1704:1720] [EM] Found matching exchange: 28680i, Delegate: 0xffff8000e0b8
[1770360095.828] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360095.828] [1704:1720] [DMG] InvokeResponseMessage =
[1770360095.828] [1704:1720] [DMG] {
[1770360095.828] [1704:1720] [DMG]      suppressResponse = false,
[1770360095.828] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360095.828] [1704:1720] [DMG]      [
[1770360095.828] [1704:1720] [DMG]              InvokeResponseIB =
[1770360095.829] [1704:1720] [DMG]              {
[1770360095.829] [1704:1720] [DMG]                      CommandDataIB =
[1770360095.829] [1704:1720] [DMG]                      {
[1770360095.829] [1704:1720] [DMG]                              CommandPathIB =
[1770360095.829] [1704:1720] [DMG]                              {
[1770360095.829] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360095.829] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360095.829] [1704:1720] [DMG]                                      CommandId = 0x3,
[1770360095.829] [1704:1720] [DMG]                              },
[1770360095.829] [1704:1720] [DMG]
[1770360095.829] [1704:1720] [DMG]                              CommandFields =
[1770360095.829] [1704:1720] [DMG]                              {
[1770360095.829] [1704:1720] [DMG]                                      0x0 = [
[1770360095.830] [1704:1720] [DMG]                                                      0x30, 0x82, 0x01, 0xe7, 0x30, 0x82, 0x01, 0x8e, 0xa0, 0x03, 0x02, 0x01, 0x02, 0x02, 0x08, 0x46, 0x7f, 0x57, 0x62, 0xc8, 0xdc, 0x90, 0xd5, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x30, 0x3d, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x50, 0x41, 0x49, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x20, 0x6e, 0x6f, 0x20, 0x50, 0x49, 0x44, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x30, 0x20, 0x17, 0x0d, 0x32, 0x32, 0x30, 0x33, 0x33, 0x31, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x5a, 0x18, 0x0f, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32, 0x33, 0x35, 0x39, 0x35, 0x39, 0x5a, 0x30, 0x53, 0x31, 0x25, 0x30, 0x23, 0x06, 0x03, 0x55, 0x04, 0x03, 0x0c, 0x1c, 0x4d, 0x61, 0x74, 0x74, 0x65, 0x72, 0x20, 0x44, 0x65, 0x76, 0x20, 0x44, 0x41, 0x43, 0x20, 0x30, 0x78, 0x46, 0x46, 0x46, 0x31, 0x2f, 0x30, 0x78, 0x38, 0x30, 0x31, 0x30, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x01, 0x0c, 0x04, 0x46, 0x46, 0x46, 0x31, 0x31, 0x14, 0x30, 0x12, 0x06, 0x0a, 0x2b, 0x06, 0x01, 0x04, 0x01, 0x82, 0xa2, 0x7c, 0x02, 0x02, 0x0c, 0x04, 0x38, 0x30, 0x31, 0x30, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0x39, 0xef, 0x6c, 0x9d, 0x9c, 0x99, 0x7b, 0xa2, 0xc7, 0x31, 0x9a, 0x4c, 0x73, 0xc9, 0xbf, 0x47, 0xdb, 0xcd, 0xbc, 0x42, 0xc5, 0x41, 0x3e, 0xec, 0x14, 0x52, 0x75, 0xb8, 0x8f, 0xc1, 0x1a, 0xb1, 0xad, 0x0b, 0xc3, 0x3e, 0xf1, 0x4c, 0x27, 0x
[1770360095.830] [1704:1720] [DMG]                                      ] (491 bytes)
[1770360095.830] [1704:1720] [DMG]                              },
[1770360095.830] [1704:1720] [DMG]                      },
[1770360095.830] [1704:1720] [DMG]
[1770360095.830] [1704:1720] [DMG]              },
[1770360095.830] [1704:1720] [DMG]
[1770360095.830] [1704:1720] [DMG]      ],
[1770360095.830] [1704:1720] [DMG]
[1770360095.830] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360095.830] [1704:1720] [DMG] },
[1770360095.830] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1770360095.831] [1704:1720] [CTL] Received certificate chain from the device
[1770360095.831] [1704:1720] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1770360095.831] [1704:1720] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1770360095.831] [1704:1720] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1770360095.831] [1704:1720] [CTL] Sending Attestation Request to the device.
[1770360095.831] [1704:1720] [CTL] Sending Attestation request to 0xffff800217c0 device
[1770360095.831] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360095.831] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360095.832] [1704:1720] [EM] <<< [E:28681i S:26730 M:214419320] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770360095.833] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360095.833] [1704:1720] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770360095.834] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360096.119] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360096.412] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360096.413] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360096.707] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360096.708] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360097.000] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360097.000] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360097.000] [1704:1720] [EM] >>> [E:28681i S:26730 M:34177126] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[1770360097.001] [1704:1720] [EM] Found matching exchange: 28681i, Delegate: 0xffff8000db18
[1770360097.001] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360097.001] [1704:1720] [DMG] InvokeResponseMessage =
[1770360097.001] [1704:1720] [DMG] {
[1770360097.001] [1704:1720] [DMG]      suppressResponse = false,
[1770360097.001] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360097.001] [1704:1720] [DMG]      [
[1770360097.001] [1704:1720] [DMG]              InvokeResponseIB =
[1770360097.002] [1704:1720] [DMG]              {
[1770360097.002] [1704:1720] [DMG]                      CommandDataIB =
[1770360097.002] [1704:1720] [DMG]                      {
[1770360097.002] [1704:1720] [DMG]                              CommandPathIB =
[1770360097.002] [1704:1720] [DMG]                              {
[1770360097.002] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360097.002] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360097.002] [1704:1720] [DMG]                                      CommandId = 0x1,
[1770360097.003] [1704:1720] [DMG]                              },
[1770360097.003] [1704:1720] [DMG]
[1770360097.003] [1704:1720] [DMG]                              CommandFields =
[1770360097.003] [1704:1720] [DMG]                              {
[1770360097.003] [1704:1720] [DMG]                                      0x0 = [
[1770360097.004] [1704:1720] [DMG]                                                      0x15, 0x31, 0x01, 0x1b, 0x02, 0x30, 0x82, 0x02, 0x17, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x02, 0xa0, 0x82, 0x02, 0x08, 0x30, 0x82, 0x02, 0x04, 0x02, 0x01, 0x03, 0x31, 0x0d, 0x30, 0x0b, 0x06, 0x09, 0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01, 0x30, 0x82, 0x01, 0x70, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x07, 0x01, 0xa0, 0x82, 0x01, 0x61, 0x04, 0x82, 0x01, 0x5d, 0x15, 0x24, 0x00, 0x01, 0x25, 0x01, 0xf1, 0xff, 0x36, 0x02, 0x05, 0x00, 0x80, 0x05, 0x01, 0x80, 0x05, 0x02, 0x80, 0x05, 0x03, 0x80, 0x05, 0x04, 0x80, 0x05, 0x05, 0x80, 0x05, 0x06, 0x80, 0x05, 0x07, 0x80, 0x05, 0x08, 0x80, 0x05, 0x09, 0x80, 0x05, 0x0a, 0x80, 0x05, 0x0b, 0x80, 0x05, 0x0c, 0x80, 0x05, 0x0d, 0x80, 0x05, 0x0e, 0x80, 0x05, 0x0f, 0x80, 0x05, 0x10, 0x80, 0x05, 0x11, 0x80, 0x05, 0x12, 0x80, 0x05, 0x13, 0x80, 0x05, 0x14, 0x80, 0x05, 0x15, 0x80, 0x05, 0x16, 0x80, 0x05, 0x17, 0x80, 0x05, 0x18, 0x80, 0x05, 0x19, 0x80, 0x05, 0x1a, 0x80, 0x05, 0x1b, 0x80, 0x05, 0x1c, 0x80, 0x05, 0x1d, 0x80, 0x05, 0x1e, 0x80, 0x05, 0x1f, 0x80, 0x05, 0x20, 0x80, 0x05, 0x21, 0x80, 0x05, 0x22, 0x80, 0x05, 0x23, 0x80, 0x05, 0x24, 0x80, 0x05, 0x25, 0x80, 0x05, 0x26, 0x80, 0x05, 0x27, 0x80, 0x05, 0x28, 0x80, 0x05, 0x29, 0x80, 0x05, 0x2a, 0x80, 0x05, 0x2b, 0x80, 0x05, 0x2c, 0x80, 0x05, 0x2d, 0x80, 0x05, 0x2e, 0x80, 0x05, 0x2f, 0x80, 0x05, 0x30, 0x80, 0x05, 0x31, 0x80, 0x05, 0x32, 0x80, 0x05, 0x33, 0x80, 0x05, 0x34, 0x80, 0x05, 0x35, 0x80, 0x05, 0x36, 0x80, 0x05, 0x37, 0x80, 0x05, 0x38, 0x80, 0x05, 0x39, 0x80, 0x05, 0x3a, 0x80, 0x05, 0x3b, 0x80, 0x05, 0x3c, 0x80, 0x05, 0x3d, 0x80, 0x05, 0x3e, 0x80, 0x05, 0x3f, 0x80, 0x05, 0x40, 0x80, 0x05, 0x41, 0x80, 0x05, 0x42, 0x80, 0x05, 0x43, 0x80, 0x
[1770360097.004] [1704:1720] [DMG]                                      ] (583 bytes)
[1770360097.004] [1704:1720] [DMG]                                      0x1 = [
[1770360097.004] [1704:1720] [DMG]                                                      0x36, 0x2a, 0xd6, 0xb7, 0x2a, 0x1f, 0x68, 0x0f, 0x26, 0x2f, 0xc7, 0x45, 0xc2, 0xf1, 0x5c, 0x54, 0x28, 0x6d, 0xeb, 0xfd, 0xae, 0x64, 0x0b, 0x73, 0x4d, 0x92, 0x22, 0x77, 0x5b, 0x08, 0xce, 0x42, 0xa7, 0xa9, 0xdb, 0xaa, 0xe1, 0xc6, 0xee, 0x7d, 0xf0, 0x70, 0x98, 0xb8, 0x0c, 0xd4, 0x27, 0x4d, 0x33, 0x5f, 0x92, 0x9f, 0xb8, 0x75, 0x0e, 0x7b, 0x22, 0xc7, 0x45, 0xdf, 0x08, 0x68, 0xdc, 0x84,
[1770360097.005] [1704:1720] [DMG]                                      ] (64 bytes)
[1770360097.005] [1704:1720] [DMG]                              },
[1770360097.005] [1704:1720] [DMG]                      },
[1770360097.005] [1704:1720] [DMG]
[1770360097.005] [1704:1720] [DMG]              },
[1770360097.005] [1704:1720] [DMG]
[1770360097.005] [1704:1720] [DMG]      ],
[1770360097.005] [1704:1720] [DMG]
[1770360097.005] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360097.005] [1704:1720] [DMG] },
[1770360097.006] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1770360097.006] [1704:1720] [CTL] Received Attestation Information from the device
[1770360097.006] [1704:1720] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1770360097.006] [1704:1720] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[1770360097.006] [1704:1720] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1770360097.006] [1704:1720] [CTL] Performing next commissioning step 'AttestationVerification'
[1770360097.006] [1704:1720] [CTL] Verifying Device Attestation information received from the device
[1770360097.032] [1704:1720] [-] Device candidate DAC chain details:
[1770360097.032] [1704:1720] [-] --> DAC's VID: 0xFFF1, PID: 0x8010
[1770360097.032] [1704:1720] [-] ==== DAC certificate considered (491 bytes) ====
[1770360097.032] [1704:1720] [-] -----BEGIN CERTIFICATE-----
[1770360097.032] [1704:1720] [-] MIIB5zCCAY6gAwIBAgIIRn9XYsjckNUwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770360097.032] [1704:1720] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
[1770360097.033] [1704:1720] [-] RjEwIBcNMjIwMzMxMDAwMDAwWhgPOTk5OTEyMzEyMzU5NTlaMFMxJTAjBgNVBAMM
[1770360097.033] [1704:1720] [-] HE1hdHRlciBEZXYgREFDIDB4RkZGMS8weDgwMTAxFDASBgorBgEEAYKifAIBDARG
[1770360097.033] [1704:1720] [-] RkYxMRQwEgYKKwYBBAGConwCAgwEODAxMDBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770360097.033] [1704:1720] [-] A0IABDnvbJ2cmXuixzGaTHPJv0fbzbxCxUE+7BRSdbiPwRqxrQvDPvFMJ5QEQp8v
[1770360097.033] [1704:1720] [-] XucKBRty5se55zVO2vkqtP/4hC+jYDBeMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/
[1770360097.033] [1704:1720] [-] BAQDAgeAMB0GA1UdDgQWBBQy/CfR71NDovNk8Cz0cMtnR4DlqjAfBgNVHSMEGDAW
[1770360097.033] [1704:1720] [-] gBRjVA5H9kscONE4hKRi0WwZXY/7PDAKBggqhkjOPQQDAgNHADBEAiBvEbIFC9PS
[1770360097.033] [1704:1720] [-] 42wkYTAIbCIBsIz5nVp3sjqQBQD77wkTsgIgE2q2oLuL1PSt+AoSNM/vtn8K+3NV
[1770360097.033] [1704:1720] [-] 8dykctoWrEo2ZOU=
[1770360097.033] [1704:1720] [-] -----END CERTIFICATE-----
[1770360097.035] [1704:1720] [-] --> DAC certificate SKID: 32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
[1770360097.038] [1704:1720] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770360097.038] [1704:1720] [-] ==== PAI certificate considered (463 bytes) ====
[1770360097.038] [1704:1720] [-] -----BEGIN CERTIFICATE-----
[1770360097.038] [1704:1720] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770360097.038] [1704:1720] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMjAyMDUw
[1770360097.038] [1704:1720] [-] MDAwMDBaGA85OTk5MTIzMTIzNTk1OVowPTElMCMGA1UEAwwcTWF0dGVyIERldiBQ
[1770360097.038] [1704:1720] [-] QUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZGRjEwWTATBgcqhkjO
[1770360097.038] [1704:1720] [-] PQIBBggqhkjOPQMBBwNCAARBmpMVwhc+DIyHbQPM/JRIUmR/f+xeUIL0BZko7KiU
[1770360097.038] [1704:1720] [-] xZQVEwmsYx5MsDOSr2hLC6+35ls7gWLC9Sv5MbjneqqCo2YwZDASBgNVHRMBAf8E
[1770360097.038] [1704:1720] [-] CDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUY1QOR/ZLHDjROISk
[1770360097.038] [1704:1720] [-] YtFsGV2P+zwwHwYDVR0jBBgwFoAUav0idx9RH+y/FkGXZxDc3DGhcX4wCgYIKoZI
[1770360097.038] [1704:1720] [-] zj0EAwIDSAAwRQIhALLvJ/Sa6bUPuR7qyUxNC9u415KcbLiPrOUpNo0SBUwMAiBl
[1770360097.039] [1704:1720] [-] Xckrhr2QmIKmxiF3uCXX0F7b58Ivn+pxIg5+pwP4kQ==
[1770360097.039] [1704:1720] [-] -----END CERTIFICATE-----
[1770360097.041] [1704:1720] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770360097.043] [1704:1720] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770360097.054] [1704:1720] [-] ==== PAA certificate considered (449 bytes) ====
[1770360097.054] [1704:1720] [-] -----BEGIN CERTIFICATE-----
[1770360097.054] [1704:1720] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
[1770360097.054] [1704:1720] [-] TWF0dGVyIFRlc3QgUEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTAgFw0yMTA2Mjgx
[1770360097.054] [1704:1720] [-] NDIzNDNaGA85OTk5MTIzMTIzNTk1OVowMDEYMBYGA1UEAwwPTWF0dGVyIFRlc3Qg
[1770360097.054] [1704:1720] [-] UEFBMRQwEgYKKwYBBAGConwCAQwERkZGMTBZMBMGByqGSM49AgEGCCqGSM49AwEH
[1770360097.054] [1704:1720] [-] A0IABLbLY3KIfyko9brIGqnZOuJDHK2p154kL2UXfvnO2TKijs0Duq9qj8oYShpQ
[1770360097.054] [1704:1720] [-] NUKWDUU/MD8fGUIddR6Pjxqam3WjZjBkMBIGA1UdEwEB/wQIMAYBAf8CAQEwDgYD
[1770360097.054] [1704:1720] [-] VR0PAQH/BAQDAgEGMB0GA1UdDgQWBBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAfBgNV
[1770360097.054] [1704:1720] [-] HSMEGDAWgBRq/SJ3H1Ef7L8WQZdnENzcMaFxfjAKBggqhkjOPQQDAgNHADBEAiBQ
[1770360097.055] [1704:1720] [-] qoAC9NkyqaAFOPZTaK0P/8jvu8m+t9pWmDXPmqdRDgIgI7rI/g8j51RFtlM5CBpH
[1770360097.055] [1704:1720] [-] mUkpxyqvChVI1A0DTVFLJd4=
[1770360097.055] [1704:1720] [-] -----END CERTIFICATE-----
[1770360097.057] [1704:1720] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770360097.059] [1704:1720] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770360097.073] [1704:1720] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770360097.075] [1704:1720] [-] Device certification declaration details:
[1770360097.075] [1704:1720] [-] --> VID: 0xFFF1
[1770360097.076] [1704:1720] [-] --> Device type ID: 0x0000_0016
[1770360097.076] [1704:1720] [-] --> Certification type: 0 (Development and testing)
[1770360097.076] [1704:1720] [CTL] Successfully finished commissioning step 'AttestationVerification'
[1770360097.076] [1704:1720] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1770360097.076] [1704:1720] [CTL] Performing next commissioning step 'AttestationRevocationCheck'
[1770360097.076] [1704:1720] [CTL] Verifying the device's DAC chain revocation status
[1770360097.076] [1704:1720] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770360097.076] [1704:1720] [CTL] Successfully validated 'Attestation Information' command received from the device.
[1770360097.076] [1704:1720] [CTL] Successfully finished commissioning step 'AttestationRevocationCheck'
[1770360097.076] [1704:1720] [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'
[1770360097.076] [1704:1720] [CTL] Performing next commissioning step 'SendOpCertSigningRequest'
[1770360097.076] [1704:1720] [CTL] Sending CSR request to 0xffff800217c0 device
[1770360097.076] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360097.077] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360097.077] [1704:1720] [EM] <<< [E:28682i S:26730 M:214419321] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1770360097.078] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360097.078] [1704:1720] [CTL] Sent CSR request, waiting for the CSR
[1770360097.078] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360097.288] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360097.487] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360097.487] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360098.070] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360098.071] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360098.071] [1704:1720] [EM] >>> [E:28682i S:26730 M:34177127] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[1770360098.071] [1704:1720] [EM] Found matching exchange: 28682i, Delegate: 0xffff8000e0b8
[1770360098.071] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360098.071] [1704:1720] [DMG] InvokeResponseMessage =
[1770360098.071] [1704:1720] [DMG] {
[1770360098.072] [1704:1720] [DMG]      suppressResponse = false,
[1770360098.072] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360098.072] [1704:1720] [DMG]      [
[1770360098.072] [1704:1720] [DMG]              InvokeResponseIB =
[1770360098.072] [1704:1720] [DMG]              {
[1770360098.072] [1704:1720] [DMG]                      CommandDataIB =
[1770360098.072] [1704:1720] [DMG]                      {
[1770360098.072] [1704:1720] [DMG]                              CommandPathIB =
[1770360098.072] [1704:1720] [DMG]                              {
[1770360098.073] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360098.073] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360098.073] [1704:1720] [DMG]                                      CommandId = 0x5,
[1770360098.073] [1704:1720] [DMG]                              },
[1770360098.073] [1704:1720] [DMG]
[1770360098.074] [1704:1720] [DMG]                              CommandFields =
[1770360098.074] [1704:1720] [DMG]                              {
[1770360098.074] [1704:1720] [DMG]                                      0x0 = [
[1770360098.074] [1704:1720] [DMG]                                                      0x15, 0x30, 0x01, 0xdd, 0x30, 0x81, 0xda, 0x30, 0x81, 0x81, 0x02, 0x01, 0x00, 0x30, 0x0e, 0x31, 0x0c, 0x30, 0x0a, 0x06, 0x03, 0x55, 0x04, 0x0b, 0x0c, 0x03, 0x43, 0x53, 0x41, 0x30, 0x59, 0x30, 0x13, 0x06, 0x07, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x02, 0x01, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x03, 0x01, 0x07, 0x03, 0x42, 0x00, 0x04, 0xc4, 0x9b, 0x7e, 0xf9, 0x01, 0x66, 0xb2, 0xae, 0x83, 0xcf, 0x1c, 0xda, 0x78, 0x70, 0xce, 0x1f, 0x23, 0xe4, 0x0e, 0xd9, 0x9c, 0xd2, 0x61, 0x6e, 0xdb, 0xd0, 0xb8, 0x2b, 0x15, 0x67, 0x07, 0x7d, 0x9d, 0xde, 0xf8, 0xf6, 0x8d, 0x91, 0x81, 0x9b, 0x86, 0x4d, 0x1d, 0xf4, 0x58, 0x66, 0x93, 0x5a, 0x53, 0x5b, 0x91, 0x04, 0xf6, 0xa9, 0x60, 0x48, 0x7a, 0xa3, 0xbf, 0xb1, 0xf0, 0x88, 0x55, 0xe8, 0xa0, 0x11, 0x30, 0x0f, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x09, 0x0e, 0x31, 0x02, 0x30, 0x00, 0x30, 0x0a, 0x06, 0x08, 0x2a, 0x86, 0x48, 0xce, 0x3d, 0x04, 0x03, 0x02, 0x03, 0x48, 0x00, 0x30, 0x45, 0x02, 0x21, 0x00, 0xb7, 0x7a, 0x7f, 0xf9, 0x3e, 0x27, 0x0e, 0x2e, 0xbc, 0xda, 0x22, 0xa5, 0x04, 0x73, 0x91, 0x7a, 0x2e, 0xb7, 0xd9, 0x89, 0x88, 0x40, 0x5b, 0x16, 0x51, 0x4b, 0x81, 0xdb, 0x01, 0x7f, 0xbf, 0xe4, 0x02, 0x20, 0x1f, 0x89, 0x4a, 0x5f, 0x18, 0x15, 0x52, 0x1f, 0xa8, 0xc6, 0xf2, 0xd8, 0xbb, 0xae, 0x16, 0x06, 0x76, 0x61, 0x38, 0xc4, 0x37, 0x10, 0xd4, 0xa1, 0x0e, 0x6a, 0x41, 0xce, 0xaf, 0x7b, 0x0e, 0x37, 0x30, 0x02, 0x20, 0x4e, 0x59, 0x5b, 0xd1, 0x1d, 0xc9, 0x5e, 0x66, 0x6e, 0x99, 0x8f, 0xa3, 0x16, 0xbd, 0xba, 0xc1, 0x1f, 0x7d, 0x63, 0x84, 0x35, 0x1e, 0x0e, 0x52, 0x26, 0xf5, 0xf3, 0x1f, 0xee, 0x6a, 0xa4, 0x9a, 0x18,
[1770360098.075] [1704:1720] [DMG]                                      ] (261 bytes)
[1770360098.075] [1704:1720] [DMG]                                      0x1 = [
[1770360098.075] [1704:1720] [DMG]                                                      0x3b, 0x65, 0x90, 0x19, 0x9a, 0x5e, 0xe6, 0xdd, 0x1e, 0xba, 0x8f, 0xcd, 0x9a, 0x75, 0x4a, 0x8a, 0x53, 0x7f, 0xd5, 0x89, 0xcc, 0xbe, 0xfc, 0x93, 0x65, 0x3c, 0x50, 0x91, 0x98, 0xcc, 0xc4, 0x9f, 0x86, 0x5d, 0xcd, 0x34, 0x04, 0xcb, 0xc1, 0x39, 0xca, 0x18, 0x19, 0x88, 0xf3, 0x3a, 0x62, 0x3a, 0x68, 0x6b, 0x68, 0x4a, 0xce, 0x2f, 0x01, 0x93, 0xf7, 0x72, 0xc8, 0x20, 0x51, 0xf4, 0xb3, 0x6c,
[1770360098.075] [1704:1720] [DMG]                                      ] (64 bytes)
[1770360098.075] [1704:1720] [DMG]                              },
[1770360098.075] [1704:1720] [DMG]                      },
[1770360098.076] [1704:1720] [DMG]
[1770360098.076] [1704:1720] [DMG]              },
[1770360098.076] [1704:1720] [DMG]
[1770360098.076] [1704:1720] [DMG]      ],
[1770360098.076] [1704:1720] [DMG]
[1770360098.076] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360098.076] [1704:1720] [DMG] },
[1770360098.077] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0005
[1770360098.077] [1704:1720] [CTL] Received certificate signing request from the device
[1770360098.077] [1704:1720] [CTL] Successfully finished commissioning step 'SendOpCertSigningRequest'
[1770360098.077] [1704:1720] [CTL] Commissioning stage next step: 'SendOpCertSigningRequest' -> 'ValidateCSR'
[1770360098.077] [1704:1720] [CTL] Performing next commissioning step 'ValidateCSR'
[1770360098.086] [1704:1720] [CTL] Successfully finished commissioning step 'ValidateCSR'
[1770360098.086] [1704:1720] [CTL] Commissioning stage next step: 'ValidateCSR' -> 'GenerateNOCChain'
[1770360098.086] [1704:1720] [CTL] Performing next commissioning step 'GenerateNOCChain'
[1770360098.086] [1704:1720] [CTL] Getting certificate chain for the device from the issuer
[1770360098.092] [1704:1720] [CTL] Verifying Certificate Signing Request
[1770360098.095] [1704:1720] [CTL] Generating NOC
[1770360098.096] [1704:1720] [CTL] Providing certificate chain to the commissioner
[1770360098.096] [1704:1720] [CTL] Received callback from the CA for NOC Chain generation. Status src/controller/ExampleOperationalCredentialsIssuer.cpp:409: Success
[1770360098.096] [1704:1720] [CTL] Successfully finished commissioning step 'GenerateNOCChain'
[1770360098.097] [1704:1720] [CTL] Performing next commissioning step 'SendTrustedRootCert'
[1770360098.097] [1704:1720] [CTL] Sending root certificate to the device
[1770360098.097] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360098.097] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360098.097] [1704:1720] [EM] <<< [E:28683i S:26730 M:214419322] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[1770360098.098] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360098.098] [1704:1720] [CTL] Sent root certificate to the device
[1770360098.099] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360098.556] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360098.751] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360098.754] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360098.754] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360098.755] [1704:1720] [EM] >>> [E:28683i S:26730 M:34177128] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[1770360098.755] [1704:1720] [EM] Found matching exchange: 28683i, Delegate: 0xffff8000db18
[1770360098.755] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360098.755] [1704:1720] [DMG] InvokeResponseMessage =
[1770360098.755] [1704:1720] [DMG] {
[1770360098.755] [1704:1720] [DMG]      suppressResponse = false,
[1770360098.755] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360098.755] [1704:1720] [DMG]      [
[1770360098.755] [1704:1720] [DMG]              InvokeResponseIB =
[1770360098.756] [1704:1720] [DMG]              {
[1770360098.756] [1704:1720] [DMG]                      CommandStatusIB =
[1770360098.756] [1704:1720] [DMG]                      {
[1770360098.756] [1704:1720] [DMG]                              CommandPathIB =
[1770360098.756] [1704:1720] [DMG]                              {
[1770360098.756] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360098.757] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360098.757] [1704:1720] [DMG]                                      CommandId = 0xb,
[1770360098.757] [1704:1720] [DMG]                              },
[1770360098.757] [1704:1720] [DMG]
[1770360098.757] [1704:1720] [DMG]                              StatusIB =
[1770360098.757] [1704:1720] [DMG]                              {
[1770360098.757] [1704:1720] [DMG]                                      status = 0x00 (SUCCESS),
[1770360098.757] [1704:1720] [DMG]                              },
[1770360098.757] [1704:1720] [DMG]
[1770360098.757] [1704:1720] [DMG]                      },
[1770360098.757] [1704:1720] [DMG]
[1770360098.757] [1704:1720] [DMG]              },
[1770360098.758] [1704:1720] [DMG]
[1770360098.758] [1704:1720] [DMG]      ],
[1770360098.758] [1704:1720] [DMG]
[1770360098.758] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360098.758] [1704:1720] [DMG] },
[1770360098.758] [1704:1720] [DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_003E Command=0x0000_000B Status=0x0
[1770360098.758] [1704:1720] [CTL] Device confirmed that it has received the root certificate
[1770360098.758] [1704:1720] [CTL] Successfully finished commissioning step 'SendTrustedRootCert'
[1770360098.758] [1704:1720] [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'
[1770360098.758] [1704:1720] [CTL] Performing next commissioning step 'SendNOC'
[1770360098.758] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360098.758] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360098.759] [1704:1720] [EM] <<< [E:28684i S:26730 M:214419323] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[1770360098.760] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360098.760] [1704:1720] [CTL] Sent operational certificate to the device
[1770360098.760] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360099.141] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360099.433] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360099.822] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360099.825] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360099.825] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360099.825] [1704:1720] [EM] >>> [E:28684i S:26730 M:34177129] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360099.826] [1704:1720] [EM] Found matching exchange: 28684i, Delegate: 0xffff8000e0b8
[1770360099.826] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360099.826] [1704:1720] [DMG] InvokeResponseMessage =
[1770360099.826] [1704:1720] [DMG] {
[1770360099.826] [1704:1720] [DMG]      suppressResponse = false,
[1770360099.826] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360099.826] [1704:1720] [DMG]      [
[1770360099.826] [1704:1720] [DMG]              InvokeResponseIB =
[1770360099.826] [1704:1720] [DMG]              {
[1770360099.826] [1704:1720] [DMG]                      CommandDataIB =
[1770360099.826] [1704:1720] [DMG]                      {
[1770360099.826] [1704:1720] [DMG]                              CommandPathIB =
[1770360099.827] [1704:1720] [DMG]                              {
[1770360099.827] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360099.827] [1704:1720] [DMG]                                      ClusterId = 0x3e,
[1770360099.827] [1704:1720] [DMG]                                      CommandId = 0x8,
[1770360099.827] [1704:1720] [DMG]                              },
[1770360099.827] [1704:1720] [DMG]
[1770360099.827] [1704:1720] [DMG]                              CommandFields =
[1770360099.827] [1704:1720] [DMG]                              {
[1770360099.827] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360099.828] [1704:1720] [DMG]                                      0x1 = 1 (unsigned),
[1770360099.828] [1704:1720] [DMG]                              },
[1770360099.828] [1704:1720] [DMG]                      },
[1770360099.828] [1704:1720] [DMG]
[1770360099.828] [1704:1720] [DMG]              },
[1770360099.828] [1704:1720] [DMG]
[1770360099.828] [1704:1720] [DMG]      ],
[1770360099.828] [1704:1720] [DMG]
[1770360099.828] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360099.828] [1704:1720] [DMG] },
[1770360099.829] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0008
[1770360099.829] [1704:1720] [CTL] Device returned status 0 on receiving the NOC
[1770360099.829] [1704:1720] [CTL] Operational credentials provisioned on device 0xffff800217c0
[1770360099.829] [1704:1720] [TOO] Secure Pairing Success
[1770360099.829] [1704:1720] [TOO] CASE establishment successful
[1770360099.829] [1704:1720] [CTL] Successfully finished commissioning step 'SendNOC'
[1770360099.829] [1704:1720] [CTL] No NetworkScan enabled or WiFi/Thread endpoint not specified, skipping ScanNetworks
[1770360099.829] [1704:1720] [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'
[1770360099.829] [1704:1720] [CTL] Performing next commissioning step 'ThreadNetworkSetup'
[1770360099.829] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360099.829] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360099.830] [1704:1720] [EM] <<< [E:28685i S:26730 M:214419324] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[1770360099.831] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360099.831] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360100.505] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360100.605] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360100.606] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360100.606] [1704:1720] [EM] >>> [E:28685i S:26730 M:34177130] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360100.606] [1704:1720] [EM] Found matching exchange: 28685i, Delegate: 0xffff8000db18
[1770360100.606] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360100.606] [1704:1720] [DMG] InvokeResponseMessage =
[1770360100.606] [1704:1720] [DMG] {
[1770360100.607] [1704:1720] [DMG]      suppressResponse = false,
[1770360100.607] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360100.607] [1704:1720] [DMG]      [
[1770360100.607] [1704:1720] [DMG]              InvokeResponseIB =
[1770360100.607] [1704:1720] [DMG]              {
[1770360100.607] [1704:1720] [DMG]                      CommandDataIB =
[1770360100.607] [1704:1720] [DMG]                      {
[1770360100.607] [1704:1720] [DMG]                              CommandPathIB =
[1770360100.608] [1704:1720] [DMG]                              {
[1770360100.608] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360100.608] [1704:1720] [DMG]                                      ClusterId = 0x31,
[1770360100.608] [1704:1720] [DMG]                                      CommandId = 0x5,
[1770360100.608] [1704:1720] [DMG]                              },
[1770360100.608] [1704:1720] [DMG]
[1770360100.608] [1704:1720] [DMG]                              CommandFields =
[1770360100.609] [1704:1720] [DMG]                              {
[1770360100.609] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360100.609] [1704:1720] [DMG]                                      0x2 = 0 (unsigned),
[1770360100.609] [1704:1720] [DMG]                              },
[1770360100.609] [1704:1720] [DMG]                      },
[1770360100.609] [1704:1720] [DMG]
[1770360100.609] [1704:1720] [DMG]              },
[1770360100.610] [1704:1720] [DMG]
[1770360100.610] [1704:1720] [DMG]      ],
[1770360100.610] [1704:1720] [DMG]
[1770360100.610] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360100.610] [1704:1720] [DMG] },
[1770360100.610] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0005
[1770360100.610] [1704:1720] [CTL] Received NetworkConfig response, networkingStatus=0
[1770360100.611] [1704:1720] [CTL] Successfully finished commissioning step 'ThreadNetworkSetup'
[1770360100.611] [1704:1720] [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'
[1770360100.611] [1704:1720] [CTL] Performing next commissioning step 'FailsafeBeforeThreadEnable'
[1770360100.611] [1704:1720] [CTL] Arming failsafe (164 seconds)
[1770360100.611] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360100.611] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360100.612] [1704:1720] [EM] <<< [E:28686i S:26730 M:214419325] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770360100.613] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360100.613] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360100.896] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360100.898] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360100.899] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360100.899] [1704:1720] [EM] >>> [E:28686i S:26730 M:34177131] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360100.899] [1704:1720] [EM] Found matching exchange: 28686i, Delegate: 0xffff8000e0b8
[1770360100.899] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360100.900] [1704:1720] [DMG] InvokeResponseMessage =
[1770360100.900] [1704:1720] [DMG] {
[1770360100.900] [1704:1720] [DMG]      suppressResponse = false,
[1770360100.900] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360100.900] [1704:1720] [DMG]      [
[1770360100.900] [1704:1720] [DMG]              InvokeResponseIB =
[1770360100.900] [1704:1720] [DMG]              {
[1770360100.900] [1704:1720] [DMG]                      CommandDataIB =
[1770360100.900] [1704:1720] [DMG]                      {
[1770360100.901] [1704:1720] [DMG]                              CommandPathIB =
[1770360100.901] [1704:1720] [DMG]                              {
[1770360100.901] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360100.901] [1704:1720] [DMG]                                      ClusterId = 0x30,
[1770360100.901] [1704:1720] [DMG]                                      CommandId = 0x1,
[1770360100.901] [1704:1720] [DMG]                              },
[1770360100.901] [1704:1720] [DMG]
[1770360100.902] [1704:1720] [DMG]                              CommandFields =
[1770360100.902] [1704:1720] [DMG]                              {
[1770360100.902] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360100.902] [1704:1720] [DMG]                                      0x1 = "" (0 chars),
[1770360100.902] [1704:1720] [DMG]                              },
[1770360100.902] [1704:1720] [DMG]                      },
[1770360100.902] [1704:1720] [DMG]
[1770360100.903] [1704:1720] [DMG]              },
[1770360100.903] [1704:1720] [DMG]
[1770360100.903] [1704:1720] [DMG]      ],
[1770360100.903] [1704:1720] [DMG]
[1770360100.903] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360100.903] [1704:1720] [DMG] },
[1770360100.903] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770360100.904] [1704:1720] [CTL] Received ArmFailSafe response errorCode=0
[1770360100.904] [1704:1720] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable'
[1770360100.904] [1704:1720] [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'
[1770360100.904] [1704:1720] [CTL] Performing next commissioning step 'ThreadNetworkEnable'
[1770360100.904] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360100.904] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360100.904] [1704:1720] [EM] <<< [E:28687i S:26730 M:214419326] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[1770360100.905] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360100.906] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360101.187] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360103.238] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360103.239] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360103.239] [1704:1720] [EM] >>> [E:28687i S:26730 M:34177132] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[1770360103.239] [1704:1720] [EM] Found matching exchange: 28687i, Delegate: 0xffff8000db18
[1770360103.239] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360103.239] [1704:1720] [DMG] InvokeResponseMessage =
[1770360103.239] [1704:1720] [DMG] {
[1770360103.240] [1704:1720] [DMG]      suppressResponse = false,
[1770360103.240] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360103.240] [1704:1720] [DMG]      [
[1770360103.240] [1704:1720] [DMG]              InvokeResponseIB =
[1770360103.240] [1704:1720] [DMG]              {
[1770360103.240] [1704:1720] [DMG]                      CommandDataIB =
[1770360103.240] [1704:1720] [DMG]                      {
[1770360103.241] [1704:1720] [DMG]                              CommandPathIB =
[1770360103.241] [1704:1720] [DMG]                              {
[1770360103.241] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360103.241] [1704:1720] [DMG]                                      ClusterId = 0x31,
[1770360103.241] [1704:1720] [DMG]                                      CommandId = 0x7,
[1770360103.241] [1704:1720] [DMG]                              },
[1770360103.241] [1704:1720] [DMG]
[1770360103.241] [1704:1720] [DMG]                              CommandFields =
[1770360103.242] [1704:1720] [DMG]                              {
[1770360103.242] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360103.242] [1704:1720] [DMG]                                      0x2 = NULL
[1770360103.242] [1704:1720] [DMG]                              },
[1770360103.242] [1704:1720] [DMG]                      },
[1770360103.242] [1704:1720] [DMG]
[1770360103.242] [1704:1720] [DMG]              },
[1770360103.243] [1704:1720] [DMG]
[1770360103.243] [1704:1720] [DMG]      ],
[1770360103.243] [1704:1720] [DMG]
[1770360103.243] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360103.243] [1704:1720] [DMG] },
[1770360103.243] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0031 Command=0x0000_0007
[1770360103.243] [1704:1720] [CTL] Received ConnectNetwork response, networkingStatus=0
[1770360103.243] [1704:1720] [CTL] Successfully finished commissioning step 'ThreadNetworkEnable'
[1770360103.243] [1704:1720] [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'
[1770360103.244] [1704:1720] [CTL] Performing next commissioning step 'kEvictPreviousCaseSessions'
[1770360103.244] [1704:1720] [IN] Expiring all sessions for node <00000000000008CC, 1>!!
[1770360103.244] [1704:1720] [CTL] Successfully finished commissioning step 'kEvictPreviousCaseSessions'
[1770360103.244] [1704:1720] [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'
[1770360103.244] [1704:1720] [CTL] Performing next commissioning step 'kFindOperationalForStayActive'
[1770360103.244] [1704:1720] [CSM] FindOrEstablishSession: PeerId = [1:00000000000008CC]
[1770360103.244] [1704:1720] [CSM] FindOrEstablishSession: No existing OperationalSessionSetup instance found
[1770360103.244] [1704:1720] [DIS] OperationalSessionSetup[1:00000000000008CC]: State change 1 --> 2
[1770360103.246] [1704:1720] [DIS] Lookup started for 46E039287128F8B5-00000000000008CC
[1770360103.246] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360103.444] [1704:1720] [DIS] Checking node lookup status for 46E039287128F8B5-00000000000008CC after 200 ms
[1770360106.160] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360108.403] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360108.403] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360111.620] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360113.863] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360113.863] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360116.787] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360119.030] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360119.030] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360121.662] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360124.100] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360124.100] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360126.731] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360129.170] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360129.170] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360131.899] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360134.240] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360134.241] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360134.248] [1704:1720] [DIS] Timeout waiting for mDNS resolution.
[1770360136.872] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360139.312] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360139.312] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360141.945] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360144.384] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360144.384] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360147.017] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360148.244] [1704:1720] [DIS] Checking node lookup status for 46E039287128F8B5-00000000000008CC after 45000 ms
[1770360148.245] [1704:1720] [DIS] OperationalSessionSetup[1:00000000000008CC]: operational discovery failed: src/lib/address_resolve/AddressResolve_DefaultImpl.cpp:124: CHIP Error 0x00000032: Timeout
[1770360148.245] [1704:1720] [DIS] Retrying operational DNS-SD discovery. Attempts remaining: 2
[1770360148.246] [1704:1720] [DIS] Lookup started for 46E039287128F8B5-00000000000008CC
[1770360148.246] [1704:1720] [CTL] Session establishment failed for <00000000000008CC, 1>, error: src/lib/address_resolve/AddressResolve_DefaultImpl.cpp:124: CHIP Error 0x00000032: Timeout.  Next retry expected to get a response to Sigma1 or fail within 60 seconds
[1770360148.246] [1704:1720] [CTL] Arming failsafe (120 seconds)
[1770360148.246] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360148.246] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360148.247] [1704:1720] [EM] <<< [E:28688i S:26730 M:214419327] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770360148.248] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360148.382] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360148.446] [1704:1720] [DIS] Checking node lookup status for 46E039287128F8B5-00000000000008CC after 201 ms
[1770360148.774] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360148.775] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360148.775] [1704:1720] [EM] >>> [E:28688i S:26730 M:34177133] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360148.775] [1704:1720] [EM] Found matching exchange: 28688i, Delegate: 0xffff8000db18
[1770360148.776] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360148.776] [1704:1720] [DMG] InvokeResponseMessage =
[1770360148.776] [1704:1720] [DMG] {
[1770360148.776] [1704:1720] [DMG]      suppressResponse = false,
[1770360148.776] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360148.776] [1704:1720] [DMG]      [
[1770360148.776] [1704:1720] [DMG]              InvokeResponseIB =
[1770360148.776] [1704:1720] [DMG]              {
[1770360148.777] [1704:1720] [DMG]                      CommandDataIB =
[1770360148.777] [1704:1720] [DMG]                      {
[1770360148.777] [1704:1720] [DMG]                              CommandPathIB =
[1770360148.777] [1704:1720] [DMG]                              {
[1770360148.777] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360148.777] [1704:1720] [DMG]                                      ClusterId = 0x30,
[1770360148.777] [1704:1720] [DMG]                                      CommandId = 0x1,
[1770360148.778] [1704:1720] [DMG]                              },
[1770360148.778] [1704:1720] [DMG]
[1770360148.778] [1704:1720] [DMG]                              CommandFields =
[1770360148.778] [1704:1720] [DMG]                              {
[1770360148.778] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360148.778] [1704:1720] [DMG]                                      0x1 = "" (0 chars),
[1770360148.779] [1704:1720] [DMG]                              },
[1770360148.779] [1704:1720] [DMG]                      },
[1770360148.779] [1704:1720] [DMG]
[1770360148.779] [1704:1720] [DMG]              },
[1770360148.779] [1704:1720] [DMG]
[1770360148.779] [1704:1720] [DMG]      ],
[1770360148.779] [1704:1720] [DMG]
[1770360148.779] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360148.779] [1704:1720] [DMG] },
[1770360148.780] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770360148.780] [1704:1720] [CTL] Status of extending fail-safe for CASE retry: 0
[1770360148.780] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360151.502] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360153.942] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360153.942] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360156.574] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360159.013] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360159.014] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360161.646] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360164.085] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360164.085] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360166.717] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360169.156] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360169.156] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360171.788] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360174.324] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360174.325] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360176.956] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360179.250] [1704:1720] [DIS] Timeout waiting for mDNS resolution.
[1770360179.394] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360179.394] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360182.027] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360184.466] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360184.466] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360187.195] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360189.634] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360189.634] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360192.266] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360193.245] [1704:1720] [DIS] Checking node lookup status for 46E039287128F8B5-00000000000008CC after 45001 ms
[1770360193.246] [1704:1720] [DIS] OperationalSessionSetup[1:00000000000008CC]: operational discovery failed: src/lib/address_resolve/AddressResolve_DefaultImpl.cpp:124: CHIP Error 0x00000032: Timeout
[1770360193.246] [1704:1720] [DIS] Retrying operational DNS-SD discovery. Attempts remaining: 1
[1770360193.247] [1704:1720] [DIS] Lookup started for 46E039287128F8B5-00000000000008CC
[1770360193.247] [1704:1720] [CTL] Session establishment failed for <00000000000008CC, 1>, error: src/lib/address_resolve/AddressResolve_DefaultImpl.cpp:124: CHIP Error 0x00000032: Timeout.  Next retry expected to get a response to Sigma1 or fail within 60 seconds
[1770360193.247] [1704:1720] [CTL] Arming failsafe (120 seconds)
[1770360193.247] [1704:1720] [DMG] ICR moving to [AddingComm]
[1770360193.247] [1704:1720] [DMG] ICR moving to [AddedComma]
[1770360193.248] [1704:1720] [EM] <<< [E:28689i S:26730 M:214419328] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1770360193.249] [1704:1720] [DMG] ICR moving to [AwaitingRe]
[1770360193.447] [1704:1720] [DIS] Checking node lookup status for 46E039287128F8B5-00000000000008CC after 201 ms
[1770360193.631] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360193.634] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360193.635] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360193.635] [1704:1720] [EM] >>> [E:28689i S:26730 M:34177134] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[1770360193.635] [1704:1720] [EM] Found matching exchange: 28689i, Delegate: 0xffff8000db18
[1770360193.635] [1704:1720] [DMG] ICR moving to [ResponseRe]
[1770360193.636] [1704:1720] [DMG] InvokeResponseMessage =
[1770360193.636] [1704:1720] [DMG] {
[1770360193.636] [1704:1720] [DMG]      suppressResponse = false,
[1770360193.636] [1704:1720] [DMG]      InvokeResponseIBs =
[1770360193.636] [1704:1720] [DMG]      [
[1770360193.636] [1704:1720] [DMG]              InvokeResponseIB =
[1770360193.636] [1704:1720] [DMG]              {
[1770360193.636] [1704:1720] [DMG]                      CommandDataIB =
[1770360193.636] [1704:1720] [DMG]                      {
[1770360193.637] [1704:1720] [DMG]                              CommandPathIB =
[1770360193.637] [1704:1720] [DMG]                              {
[1770360193.637] [1704:1720] [DMG]                                      EndpointId = 0x0,
[1770360193.637] [1704:1720] [DMG]                                      ClusterId = 0x30,
[1770360193.637] [1704:1720] [DMG]                                      CommandId = 0x1,
[1770360193.637] [1704:1720] [DMG]                              },
[1770360193.638] [1704:1720] [DMG]
[1770360193.638] [1704:1720] [DMG]                              CommandFields =
[1770360193.638] [1704:1720] [DMG]                              {
[1770360193.638] [1704:1720] [DMG]                                      0x0 = 0 (unsigned),
[1770360193.638] [1704:1720] [DMG]                                      0x1 = "" (0 chars),
[1770360193.638] [1704:1720] [DMG]                              },
[1770360193.638] [1704:1720] [DMG]                      },
[1770360193.639] [1704:1720] [DMG]
[1770360193.639] [1704:1720] [DMG]              },
[1770360193.639] [1704:1720] [DMG]
[1770360193.639] [1704:1720] [DMG]      ],
[1770360193.639] [1704:1720] [DMG]
[1770360193.639] [1704:1720] [DMG]      InteractionModelRevision = 12
[1770360193.639] [1704:1720] [DMG] },
[1770360193.639] [1704:1720] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001
[1770360193.640] [1704:1720] [CTL] Status of extending fail-safe for CASE retry: 0
[1770360193.640] [1704:1720] [DMG] ICR moving to [AwaitingDe]
[1770360196.362] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16389
[1770360198.800] [1704:1711] [DL] Indication received, conn = 0xffff8802a540
[1770360198.801] [1704:1720] [DL] HandlePlatformSpecificBLEEvent 16391
[1770360200.525] [1704:1704] [CTL] Shutting down the commissioner
[1770360200.525] [1704:1704] [CTL] Cancelling CASE setup for step 'kFindOperationalForStayActive'
[1770360200.525] [1704:1704] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770360200.526] [1704:1704] [DIS] Closing all BLE connections
[1770360200.526] [1704:1704] [IN] Clearing BLE pending packets.
[1770360200.527] [1704:1704] [BLE] Auto-closing end point's BLE connection.
[1770360200.527] [1704:1704] [DL] Closing BLE GATT connection (con 0xffff8802a540)
[1770360200.528] [1704:1711] [DL] Close BLE connection: peer=E0:F0:A0:52:CD:52
[1770360200.752] [1704:1704] [IN] SecureSession[0xffff80022cd0]: MarkForEviction Type:1 LSID:26730
[1770360200.752] [1704:1704] [SC] SecureSession[0xffff80022cd0, LSID:26730]: State change 'kActive' --> 'kPendingEviction'
[1770360200.752] [1704:1704] [IN] SecureSession[0xffff80022cd0]: Released - Type:1 LSID:26730
[1770360200.752] [1704:1704] [CTL] Shutting down the controller
[1770360200.752] [1704:1704] [DIS] OperationalSessionSetup[1:00000000000008CC]: Cancelling incomplete address resolution as device is being deleted.
[1770360200.752] [1704:1704] [IN] Expiring all sessions for fabric 0x1!!
[1770360200.753] [1704:1704] [FP] Forgetting fabric 0x1
[1770360200.753] [1704:1704] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770360200.753] [1704:1711] [DL] BLE connection closed: conn=0xffff8802a540
[1770360200.753] [1704:1704] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770360200.754] [1704:1704] [TS] Reverted Last Known Good Time to previous value
[1770360200.754] [1704:1704] [CTL] Shutting down the commissioner
[1770360200.754] [1704:1704] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770360200.754] [1704:1704] [CTL] Shutting down the controller
[1770360200.754] [1704:1704] [CTL] Shutting down the System State, this will teardown the CHIP Stack
[1770360200.755] [1704:1704] [DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[1770360200.755] [1704:1704] [FP] Shutting down FabricTable
[1770360200.755] [1704:1704] [TS] Pending Last Known Good Time: 2023-10-14T01:16:48
[1770360200.756] [1704:1704] [TS] Previous Last Known Good Time: 2023-10-14T01:16:48
[1770360200.756] [1704:1704] [TS] Reverted Last Known Good Time to previous value
[1770360200.768] [1704:1704] [DL] Wrote settings to /tmp/chip_counters.ini
[1770360200.768] [1704:1704] [DL] NVS set: chip-counters/total-operational-hours = 0 (0x0)
[1770360200.768] [1704:1704] [DL] Inet Layer shutdown
[1770360200.768] [1704:1704] [DL] BLE Layer shutdown
[1770360200.771] [1704:1704] [DL] WiFi-PAF Layer shutdown
[1770360200.771] [1704:1704] [PAF] WiFiPAF: Closing all WiFiPAF sessions to shutdown
[1770360200.771] [1704:1704] [DL] NFCCommissioningMgr shutdown
[1770360200.772] [1704:1704] [DL] System Layer shutdown
[1770360200.774] [1704:1704] [TOO] Run command failure: ../../examples/chip-tool/commands/common/CHIPCommand.cpp:645: CHIP Error 0x00000032: Timeout

```
