```c
//SW version
software_string
```
```c
> 
Missed Logs: 4
[00:00:00.129][silabs ]FSH: storage info: page_size=4096 page_num=384
[00:00:00.572][silabs ]FSH: scan all_page=384: head_page=0 wirte_page=0 wirte_offset=876 idle_page=383 log_date_len=876 got_head=0
[00:00:00.573][silabs ]FSH: storage info: page_size=4096 page_num=32
[00:00:00.622][silabs ]FSH: scan all_page=32: head_page=0 wirte_page=0 wirte_offset=38 idle_page=31 log_date_len=38 got_head=0
[00:00:00.622][silabs ]LOG: app log mgmt init success(item_num=39).
[00:00:00.638][error ][DL] Initializing OpenThread Stack Success.
[00:00:00.643][error ][DL] Starting OpenThread Success.
[00:00:00.643][error ][DL] Open Thread Success.
[00:00:00.702][error ][DIS] Failed to remove advertised services: 3

[00:00:01.018][silabs ]MET: systerm reset reason=0x00000003.
[00:00:01.019][silabs ]APP: AppVer: 07.00.02(0x00070002) BtlVer: 0x03000004 Time:Jan  4 2026 17:17:25

[00:00:01.019][silabs ]APP: default transmit power 10dBm
[00:00:01.020][silabs ]WDG: Reset Reason: 0x00000000
[00:00:01.024][silabs ]DCIRCUIT: app dynamic circuit initialization start...
[00:00:01.025][silabs ]CTCFG: get factory_reset_count(buf_len=4, len=0).
[00:00:01.028][silabs ]DEV: Get GW_EAddress=(00000000:00000000) from nvm3

[00:00:01.032][silabs ]NFC: Using commissioning type: BLE
[00:00:01.036][silabs ]NWK: Use The Production QR Code.
[00:00:01.037][silabs ]NWK: SetupQRCode: [MT:6FCJ142C00KA0648G00]
[00:00:01.038][silabs ]NWK: Copy/paste the below URL in a browser to see the QR Code:
[00:00:01.038][silabs ]NWK: https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A6FCJ142C00KA0648G00
[00:00:01.039][silabs ]IDTIFY: Dev Application Init...
[00:00:01.040][silabs ]APP: App Task started
matterCli> 
[00:00:01.432][silabs ]NFC: kNfcCommissioningStatusKey (0x255) saved in persistent storage

[00:00:01.531][silabs ]DEV: Status Change: Send Status = 1 To Meter.

[00:00:01.557][silabs ]: Set Matter_Status=Booting ACK=0 and Meter Ready OK...

[00:00:01.662][silabs ]MET: Meter Report sn=00000000 old_sn=00000000 status=0.
[00:00:01.662][silabs ]MET: Meter Report Hardware Version=0x0000.
[00:00:01.663][silabs ]MET: Meter Report software version=0x00000000.
[00:00:01.664][silabs ]ZCL: CTShorted Event: EndPointId=10, EventNumber=131074 Value=0
[00:00:01.665][silabs ]MET: ct_presence new_bitmap=0x0000 old_bitmap=0x0000.
[00:00:01.666][silabs ]ZCL: CTPresence Event: EndPointId=10, EventNumber=131075 Value=0
[00:00:01.666][silabs ]MET: Report Meter Phase Loss L1.
[00:00:01.667][silabs ]ZCL: PhaseLoss Event: EndPointId=10, EventNumber=131076 Value=1
[00:00:01.668][silabs ]NWK: Key event 0
[00:00:01.668][silabs ]NWK: Received btn_event=0.
[00:00:01.670][silabs ]MET: EP[1] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.671][silabs ]MET: EP[2] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.671][silabs ]MET: EP[3] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.672][silabs ]MET: EP[4] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.672][silabs ]MET: EP[5] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.673][silabs ]MET: EP[6] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.674][silabs ]MET: EP[7] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.674][silabs ]MET: EP[8] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.675][silabs ]MET: EP[9] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.693][silabs ]MET: Report Test Channel Number=0.

[00:00:01.938][silabs ]NFC: NFC RFMode ret=1

[00:00:02.031][silabs ]DEV: Communicating with the meter by Modbus Success.


[00:00:04.086][silabs ]MET: Meter Report Manufacturing date=2025-12-01 old_date=2025-12-01 status=0.
[00:00:04.087][silabs ]MET: Meter Report Hardware Version=0x0103 old_version=0x0103 status=0.
[00:00:04.088][silabs ]MET: Meter Report hardware_string=MA_ME_1.3 old_hardware_string=MA_ME_1.3 status=0
[00:00:04.089][silabs ]MET: Meter Report: merer_version=0x00050100 matter_version=0x00070002 config_version=0x00070002.
[00:00:04.092][silabs ]MET: software_string=MA_7.0.2_ME_5.1.0 old_software_string=MA_7.0.2_ME_5.1.0.
[00:00:04.094][silabs ]CTCFG: circuit_config_from meter: index=0 (2 1 3) is_different=0

[00:00:04.131][silabs ]NWK: network status timer, join_mode(3) nwk_status(1) dev_status(1) after_booting(0).

[00:00:04.131][silabs ]NWK: FabricCount 2, IsThreadProvisioned 0, NFC 0 536987936

[00:00:04.131][silabs ]NWK: Only Joining by Multiply in the future and Timer Start for Session Established.

[00:00:04.132][silabs ]DEV: Status Change: Send Status = 11 To Meter.
[00:00:04.133][silabs ]NWK: Do After Booting Event.
[00:00:04.137][silabs ]TIMESYNC: Matter date time synchronization Success.
[00:00:04.137][silabs ]DCIRCUIT: Base BrDevice[circuit00]: ONLINE
[00:00:04.150][silabs ]DCIRCUIT: Added device=circuit00 for dynamic_endpoint=11(index=0, ch_bitmap=0003) success.
[00:00:04.150][silabs ]CTCFG: save circuit_config to nvm3 status = 0

[00:00:04.207][silabs ]: Set Matter Status=11 ADDR=2017 ACK=0
[00:00:04.213][silabs ]: Set UTC Time=(2000-1-1 0:0:3000) ADDR=2012 ACK=0
[00:00:04.237][silabs ]: Set CH=1 Voltage Input=1 ADDR=2047 ACK=0
[00:00:04.247][silabs ]: Set CH=2 Voltage Input=2 ADDR=2048 ACK=0
[00:00:04.253][silabs ]: Set CH=1 Circuit: circuit_type=2 channels=3 equipment=1 ADDR=2056 ACK=0
[00:00:04.260][silabs ]: Set CH=2 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2060 ACK=0
[00:00:04.267][silabs ]: Set CH=3 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2064 ACK=0
[00:00:04.274][silabs ]: Set CH=4 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2068 ACK=0
[00:00:04.281][silabs ]: Set CH=5 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2072 ACK=0
[00:00:04.288][silabs ]: Set CH=6 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2076 ACK=0
[00:00:04.294][silabs ]: Set CH=7 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2080 ACK=0
[00:00:04.301][silabs ]: Set CH=8 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2084 ACK=0
[00:00:04.308][silabs ]: Set CH=9 Circuit: circuit_type=0 channels=0 equipment=0 ADDR=2088 ACK=0

[00:00:07.078][silabs ]MET: Report CT=01 is Normal.
[00:00:07.078][silabs ]MET: Report CT=02 is Normal.
[00:00:07.078][silabs ]MET: Report CT=03 is Normal.
[00:00:07.079][silabs ]MET: Report CT=04 is Normal.
[00:00:07.079][silabs ]MET: Report CT=05 is Normal.
[00:00:07.080][silabs ]MET: Report CT=06 is Normal.
[00:00:07.080][silabs ]MET: Report CT=07 is Normal.
[00:00:07.081][silabs ]MET: Report CT=08 is Normal.
[00:00:07.081][silabs ]MET: Report CT=09 is Normal.
[00:00:07.082][silabs ]ZCL: CTShorted Event: EndPointId=10, EventNumber=131087 Value=511

[00:00:11.282][silabs ]NWK: platform_event(800b) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:11.282][silabs ]NWK: platform_event: kThreadStateChange RoleChanged=1 AddressChanged=0 NetDataChanged=0 ChildNodesChanged=0 Flags=00001084.
[00:00:11.287][silabs ]NWK: platform_event(8001) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:11.288][silabs ]NWK: platform_event: ThreadConnectivity Established.

[00:00:11.404][silabs ]NWK: platform_event(800b) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:11.405][silabs ]NWK: platform_event: kThreadStateChange RoleChanged=0 AddressChanged=0 NetDataChanged=1 ChildNodesChanged=0 Flags=00000200.
[00:00:11.411][silabs ]NWK: platform_event(800b) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:11.411][silabs ]NWK: platform_event: kThreadStateChange RoleChanged=0 AddressChanged=1 NetDataChanged=0 ChildNodesChanged=0 Flags=00000001.

[00:00:11.663][silabs ]NWK: platform_event(8012) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:11.663][silabs ]NWK: platform_event: kDnssdInitialized.
[00:00:11.666][silabs ]NWK: platform_event(8016) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)

[00:00:12.026][silabs ]NWK: platform_event(8018) join_mode(3) nwk_status(1) dev_status(11) mjoin_status(0) after_boot(1) joined_nwk(1)
[00:00:12.027][silabs ]NWK: Session Connect OK-->kSecureSessionEstablished PeerNodeId=1 FabricIndex=2783524976 SecureSessionType=0 TransportType=1 LocalSessionId=2
[00:00:12.027][silabs ]NWK: platform_event: kSecureSessionEstablished-->kNwkSessionEstablished.
[00:00:12.028][silabs ]NWK: Session Established and Stop Waiting Timer and set_dev_status-->kDevStatusOperation.

[00:00:12.083][silabs ]DEV: Status Change: Send Status = 6 To Meter.
[00:00:12.084][silabs ]DEV: Start Timer to check GW(00000000:00000000) status.

[00:00:12.164][silabs ]: Set Matter Status=6 ADDR=2017 ACK=0

[00:00:14.666][silabs ]CLS: Unknown Attribute: EId=0x00 CId=0x002a AId==0x0002 Type=48 Size=1 Value=0x1
[00:00:14.666][silabs ]CLS: Unknown Attribute: EId=0x00 CId=0x002a AId==0x0003 Type=32 Size=1 Value=0xff

[00:00:56.686][error ][DIS] OperationalSessionSetup[1:0000000036E47752]: operational discovery failed: 32
[00:00:56.686][error ][DMG] Failed to establish CASE for subscription-resumption with error '32'
```