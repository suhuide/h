```c
//SW version
software_string
```
```c
> 
Missed Logs: 3
[00:00:00.108][silabs ]FSH: storage info: page_size=4096 page_num=384
[00:00:00.549][silabs ]FSH: scan all_page=384: head_page=0 wirte_page=0 wirte_offset=293 idle_page=383 log_date_len=293 got_head=0
[00:00:00.550][silabs ]FSH: storage info: page_size=4096 page_num=32
[00:00:00.598][silabs ]FSH: scan all_page=32: head_page=0 wirte_page=0 wirte_offset=0 idle_page=32 log_date_len=0 got_head=0
[00:00:00.599][silabs ]LOG: app log mgmt init success(item_num=39).
[00:00:00.604][error ][DL] Initializing OpenThread Stack Success.
[00:00:00.605][error ][DL] Starting OpenThread Success.
[00:00:00.605][error ][DL] Open Thread Success.
[00:00:00.644][error ][DIS] Failed to remove advertised services: 3

[00:00:00.952][silabs ]MET: systerm reset reason=0x00000003.
[00:00:00.953][silabs ]APP: AppVer: 07.00.02(0x00070002) BtlVer: 0x03000004 Time:Jan  4 2026 17:17:25

[00:00:00.953][silabs ]APP: default transmit power 10dBm
[00:00:00.953][silabs ]WDG: Reset Reason: 0x00000000
[00:00:00.958][silabs ]DCIRCUIT: app dynamic circuit initialization start...
[00:00:00.958][silabs ]CTCFG: get factory_reset_count(buf_len=4, len=0).
[00:00:00.960][silabs ]DEV: Get GW_EAddress=(00000000:00000000) from nvm3

[00:00:00.963][silabs ]NFC: Using default commissioning type: BLE
matterCli> 
[00:00:01.459][silabs ]NWK: Use The Production QR Code.
[00:00:01.461][silabs ]NWK: SetupQRCode: [MT:6FCJ142C00KA0648G00]
[00:00:01.462][silabs ]NWK: Copy/paste the below URL in a browser to see the QR Code:
[00:00:01.462][silabs ]NWK: https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A6FCJ142C00KA0648G00
[00:00:01.462][silabs ]IDTIFY: Dev Application Init...
[00:00:01.464][silabs ]APP: App Task started
[00:00:01.465][silabs ]DEV: Status Change: Send Status = 1 To Meter.
[00:00:01.495][silabs ]: Set Matter_Status=Booting ACK=0 and Meter Ready OK...

[00:00:01.587][silabs ]MET: Meter Report sn=00000000 old_sn=00000000 status=0.
[00:00:01.587][silabs ]MET: Meter Report Hardware Version=0x0000.
[00:00:01.588][silabs ]MET: Meter Report software version=0x00000000.
[00:00:01.589][silabs ]ZCL: CTShorted Event: EndPointId=10, EventNumber=65539 Value=0
[00:00:01.590][silabs ]MET: ct_presence new_bitmap=0x0000 old_bitmap=0x0000.
[00:00:01.591][silabs ]ZCL: CTPresence Event: EndPointId=10, EventNumber=65540 Value=0
[00:00:01.591][silabs ]MET: Report Meter Phase is Normal.
[00:00:01.592][silabs ]ZCL: PhaseLoss Event: EndPointId=10, EventNumber=65541 Value=0
[00:00:01.593][silabs ]NWK: Key event 0
[00:00:01.593][silabs ]NWK: Received btn_event=0.
[00:00:01.595][silabs ]MET: EP[1] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.596][silabs ]MET: EP[2] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.596][silabs ]MET: EP[3] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.597][silabs ]MET: EP[4] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.598][silabs ]MET: EP[5] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.598][silabs ]MET: EP[6] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.599][silabs ]MET: EP[7] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.599][silabs ]MET: EP[8] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.600][silabs ]MET: EP[9] RMSVoltage Report:(0:0)-->(0:0).
[00:00:01.620][silabs ]MET: Report Test Channel Number=0.

[00:00:01.868][silabs ]NFC: kNfcCommissioningStatusKey (0x255) saved in persistent storage

[00:00:01.961][silabs ]DEV: Communicating with the meter by Modbus Success.


[00:00:02.363][silabs ]NFC: NFC RFMode ret=1

[00:00:04.011][silabs ]MET: Meter Report Manufacturing date=2025-12-01 old_date=2025-12-01 status=0.
[00:00:04.012][silabs ]MET: Meter Report Hardware Version=0x0103 old_version=0x0103 status=0.
[00:00:04.013][silabs ]MET: Meter Report hardware_string=MA_ME_1.3 old_hardware_string=MA_ME_1.3 status=0
[00:00:04.014][silabs ]MET: Meter Report: merer_version=0x00050100 matter_version=0x00070002 config_version=0x00070002.
[00:00:04.017][silabs ]MET: software_string=MA_7.0.2_ME_5.1.0 old_software_string=MA_7.0.2_ME_5.1.0.

[00:00:04.062][silabs ]NWK: network status timer, join_mode(1) nwk_status(0) dev_status(1) after_booting(0).

[00:00:04.062][silabs ]NWK: FabricCount 0, IsThreadProvisioned 0, NFC 0 536987936

[00:00:04.063][silabs ]NWK: May Joining by APP in the future and Timer Start for Commissioning.

[00:00:04.063][silabs ]NWK: set_dev_status-->kDevStatusReadyPairing.

[00:00:04.067][error ][DIS] Failed to remove advertised services: 3
[00:00:04.069][error ][DIS] Failed to advertise commissionable node: 3
[00:00:04.069][error ][DIS] Failed to finalize service update: 3
[00:00:04.069][silabs ]NWK: Open the Basic Commissioning Window Success
[00:00:04.070][silabs ]DEV: Status Change: Send Status = 2 To Meter.
[00:00:04.072][silabs ]NWK: Do After Booting Event.
[00:00:04.074][silabs ]TIMESYNC: Matter date time synchronization Success.

[00:00:04.126][silabs ]: Set Matter Status=2 ADDR=2017 ACK=0
[00:00:04.139][silabs ]: Set UTC Time=(2000-1-1 0:0:3000) ADDR=2012 ACK=0

[00:00:07.020][silabs ]MET: Report CT=01 is Normal.
[00:00:07.020][silabs ]MET: Report CT=02 is Normal.
[00:00:07.020][silabs ]MET: Report CT=03 is Normal.
[00:00:07.021][silabs ]MET: Report CT=04 is Normal.
[00:00:07.022][silabs ]MET: Report CT=05 is Normal.
[00:00:07.022][silabs ]MET: Report CT=06 is Normal.
[00:00:07.022][silabs ]MET: Report CT=07 is Normal.
[00:00:07.023][silabs ]MET: Report CT=08 is Normal.
[00:00:07.023][silabs ]MET: Report CT=09 is Normal.
[00:00:07.024][silabs ]ZCL: CTShorted Event: EndPointId=10, EventNumber=65551 Value=511

[00:03:04.066][error ][DIS] Failed to remove advertised services: 3
[00:03:04.066][error ][DIS] Failed to finalize service update: 3
[00:03:04.068][error ][DL] Failed to stop BledAdv timeout timer
[00:03:04.068][silabs ]NWK: platform_event(800d) join_mode(1) nwk_status(0) dev_status(2) mjoin_status(0) after_boot(1) joined_nwk(0)

[00:03:06.070][silabs ]NWK: network status timer, join_mode(1) nwk_status(0) dev_status(2) after_booting(1).

[00:03:06.071][silabs ]NWK: Timeout for Waiting Commissioning, Close Commissioning and set_dev_status-->kDevStatusIdle.
[00:03:06.071][silabs ]DEV: Status Change: Send Status = 5 To Meter.
[00:03:06.079][silabs ]: Set Matter Status=5 ADDR=2017 ACK=0

[00:15:04.968][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=1.
[00:15:06.968][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=2.
[00:15:08.968][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=3.
[00:15:10.967][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=4.
[00:15:12.967][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=5.
[00:15:14.966][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=6.
[00:15:16.967][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=7.
[00:15:18.966][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=8.
[00:15:20.967][silabs ]MET: Power_Range_Event: ret=0 for fixed_endpoint=9.
```