```c
[17:32:17.329]  [00:00:00.068][info  ][DL] Starting scheduler
[17:32:17.329]  [00:00:00.068][info  ][DL] ==================================================
[17:32:17.331]  [00:00:00.068][info  ][DL]  starting
[17:32:17.331]  [00:00:00.068][info  ][DL] ==================================================
[17:32:17.332]  [00:00:00.068][info  ][DL] Init CHIP Stack
[17:32:17.332]  [00:00:00.070][info  ][DL] Provision mode disabled
[17:32:17.332]  [00:00:00.070][info  ][DL] Initializing OpenThread stack
[17:32:17.334]  [00:00:00.072][info  ][DL] OpenThread ifconfig up and thread start
[17:32:17.334]  [00:00:00.072][info  ][DL] OpenThread started: OK
[17:32:17.337]  [00:00:00.107][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[17:32:17.337]  [00:00:00.107][info  ][DL] RAIL version:, v3.0.3-b0
[17:32:17.338]  [00:00:00.108][info  ][SVR] Current Software Version String: 0.0.3
[17:32:17.338]  [00:00:00.109][info  ][SVR] Current Software Version: 3
[17:32:17.339]  [00:00:00.110][info  ][DL] Device Configuration:
[17:32:17.339]  [00:00:00.110][info  ][DL]   Serial Number: 847227B0D1B99AF2
[17:32:17.339]  [00:00:00.111][info  ][DL]   Vendor Id: 5232 (0x1470)
[17:32:17.341]  [00:00:00.111][info  ][DL]   Product Id: 65281 (0xFF01)
[17:32:17.341]  [00:00:00.111][info  ][DL]   Product Name: Window Covering
[17:32:17.342]  [00:00:00.112][info  ][DL]   Hardware Version: 1
[17:32:17.342]  [00:00:00.113][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[17:32:17.344]  [00:00:00.113][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 3526 (0xDC6)
[17:32:17.344]  [00:00:00.113][info  ][DL]   Manufacturing Date: (not set)
[17:32:17.345]  [00:00:00.115][info  ][DL]   Device Type: 65535 (0xFFFF)
[17:32:17.345]  [00:00:00.115][info  ][SVR] SetupQRCode: [MT:K2CA04QO16GMBR1T310]
[17:32:17.347]  [00:00:00.115][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[17:32:17.348]  [00:00:00.115][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA04QO16GMBR1T310
[17:32:17.348]  [00:00:00.118][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:32:17.349]  [00:00:00.121][silabs ]Ver: 3 Btl: 0x03020002 Time:May 21 2026 19:24:17
[17:32:17.351]  [00:00:00.121][silabs ]Reset Reason: 0x00000000
[17:32:17.351]  [00:00:00.121][silabs ]SetupQRCode: [MT:K2CA04QO16GMBR1T310]
[17:32:17.352]  [00:00:00.122][silabs ]COM: Init done
[17:32:17.352]  [00:00:00.123][silabs ]NWK: device has provisioned
[17:32:17.352]  
[17:32:17.352]  [00:00:00.123][silabs ]COM: notify network [Leave]
[17:32:17.354]  [00:00:00.123][silabs ]CLS: register device: dev 0x2002c92e endpoint 1 type 0 idx 1
[17:32:17.354]  [00:00:00.124][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:32:17.355]  [00:00:00.125][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:32:17.355]  [00:00:00.125][silabs ]app_mcu_dfu_init
[17:32:17.356]  [00:00:00.126][silabs ]bootloader_init() OK, calling cache_entire_metadata()
[17:32:17.356]  [00:00:00.126][silabs ]cache_entire_metadata: starting ONE verify pass...
[17:32:17.358]  [00:00:00.126][silabs ]cache_entire_metadata: slot 0 length=2088960
[17:32:17.358]  [00:00:00.127][silabs ]cache_entire_metadata: initVerify OK, starting continueVerify loop...
[17:32:31.587]  [00:00:14.358][silabs ]cache_entire_metadata: continueVerify loop done, ret=515, iter=4731, bytes=45686
[17:32:31.587]  [00:00:14.359][silabs ]cache_entire_metadata: Header OK - magic=0x55AA, size=45676, ver=3.0.0
[17:32:31.595]  [00:00:14.367][silabs ]parse_metadata_header: Magic=0x55AA, Size=45676, Checksum=0x25, Version=3.0.0
[17:32:31.596]  [00:00:14.367][silabs ]cache_entire_metadata: DONE, cached 45686 bytes, header_valid=1
[17:32:31.596]  [00:00:14.367][silabs ]cache_entire_metadata() returned: true
[17:32:31.597]  [00:00:14.367][silabs ]app_mcu_dfu_init: done, cache_valid=1, header_valid=1
[17:32:31.597]  [00:00:14.367][silabs ]App Task started
[17:32:31.599]  [00:00:14.368][silabs ]MATTER TX: 55 AA 01 00 00 02 01 00 03 
[17:32:31.599]  [00:00:14.368][silabs ]COM: CMD: 0x02, SN: 0x0000, LEN: 9
[17:32:31.600]  
[17:32:31.600]  [00:00:14.368][silabs ]SPP: ack_timeout_ms 500
[17:32:31.600]  [00:00:14.368][silabs ]SPP: pending ack but allow new cmd process
[17:32:31.600]  matterCli> [00:00:14.386][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:32:31.614]  [00:00:14.386][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[17:32:31.616]  [00:00:14.386][silabs ]NWK: platform event type 32779
[17:32:31.616]  [00:00:14.387][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[17:32:31.617]  [00:00:14.387][silabs ]NWK: kThreadConnectivityChange,32769
[17:32:31.617]  [00:00:14.387][silabs ]NWK: Thread Established
[17:32:31.619]  [00:00:14.388][silabs ]COM: notify network [Joined]
[17:32:31.619]  [00:00:14.388][info  ][SVR] Scheduling OTA Requestor initialization
[17:32:31.624]  [00:00:14.388][info  ][SVR] Joining Multicast groups
[17:32:31.624]  [00:00:14.389][silabs ]SPP: pending ack but allow new cmd process
[17:32:31.656]  [00:00:14.424][silabs ]MATTER RX: 55 AA 01 00 00 02 00 02 
[17:32:31.656]  [00:00:14.424][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:32:31.755]  [00:00:14.525][silabs ]MATTER TX: 55 AA 01 00 01 01 00 02 
[17:32:31.755]  [00:00:14.525][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[17:32:31.755]  
[17:32:31.755]  [00:00:14.528][silabs ]SPP: ack_timeout_ms 500
[17:32:31.760]  [00:00:14.532][info  ][DL] SRP Client was started, detected server: fd11:9c64:dd37:b8c4:6397:7d5e:9e7b:227a
[17:32:31.760]  [00:00:14.532][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:32:31.762]  [00:00:14.532][silabs ]NWK: platform event type 32779
[17:32:31.762]  [00:00:14.533][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:32:31.765]  [00:00:14.534][silabs ]NWK: platform event type 32779
[17:32:31.829]  [00:00:14.600][silabs ]MATTER RX: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 31 2E 31 2E 30 7D 92 
[17:32:31.830]  [00:00:14.600][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"1.1.0}
[17:32:31.830]  [00:00:14.600][silabs ]COM: Failed to extract version from product info
[17:32:31.831]  [00:00:14.601][silabs ]COM: Fallback extracted version: 1.1.0
[17:32:31.831]  [00:00:14.601][silabs ]Current MCU version set to: 1.1.0
[17:32:31.833]  [00:00:14.601][silabs ]COM: Boot OTA check - MCU: 1.1.0, Metadata: 3.0.0
[17:32:31.833]  [00:00:14.601][silabs ]COM: Notify MCU OTA upgrade: cmd=0xE1, PID=0x0001, Ver=3.0.0, size=45676, checksum=0x25
[17:32:31.931]  [00:00:14.703][silabs ]MATTER TX: 55 AA 01 00 02 02 01 01 06 
[17:32:31.931]  [00:00:14.703][silabs ]COM: CMD: 0x02, SN: 0x0002, LEN: 9
[17:32:31.931]  
[17:32:31.931]  [00:00:14.703][silabs ]SPP: ack_timeout_ms 500
[17:32:31.955]  [00:00:14.724][silabs ]MATTER RX: 55 AA 01 00 02 02 00 04 
[17:32:31.955]  [00:00:14.724][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:32:32.055]  [00:00:14.826][silabs ]MATTER TX: 55 AA 01 00 03 E1 0A 00 01 33 2E 30 2E 30 B2 6C 25 21 
[17:32:32.055]  [00:00:14.826][silabs ]COM: CMD: 0xE1, SN: 0x0003, LEN: 18
[17:32:32.060]  
[17:32:32.060]  [00:00:14.826][silabs ]SPP: ack_timeout_ms 500
[17:32:32.076]  [00:00:14.847][silabs ]MATTER RX: 55 AA 01 00 00 12 04 00 00 00 00 16 
[17:32:32.076]  [00:00:14.847][silabs ]WDC: report Active percent 0 dev_index 1
[17:32:32.078]  [00:00:14.848][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:32:32.078]  
[17:32:32.078]  [00:00:14.848][info  ][ZCL] Lift[1] Position Set: 10000
[17:32:32.081]  [00:00:14.848][silabs ]SPP: pending ack but allow new cmd process
[17:32:32.556]  [00:00:15.327][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:32.556]  [00:00:15.329][silabs ]MATTER TX: 55 AA 01 00 03 E1 0A 00 01 33 2E 30 2E 30 B2 6C 25 21 
[17:32:32.559]  [00:00:15.330][silabs ]COM: CMD: 0xE1, SN: 0x0003, LEN: 18
[17:32:32.559]  
[17:32:32.559]  [00:00:15.332][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[17:32:32.561]  [00:00:15.332][silabs ]NWK: platform event type 32786
[17:32:32.561]  [00:00:15.332][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[17:32:32.562]  [00:00:15.332][info  ][SVR] Server initialization complete
[17:32:32.562]  [00:00:15.333][info  ][DIS] Updating services using commissioning mode 0
[17:32:32.564]  [00:00:15.333][info  ][DIS] Advertise operational node 62D8D539418A9054-00000000000008CA
[17:32:32.565]  [00:00:15.333][info  ][DL] advertising srp service: 62D8D539418A9054-00000000000008CA._matter._tcp
[17:32:32.565]  [00:00:15.333][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[17:32:32.569]  [00:00:15.333][silabs ]NWK: platform event type 32790
[17:32:32.574]  [00:00:15.343][info  ][IM] No subscriptions to resume
[17:32:33.060]  [00:00:15.832][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:33.060]  [00:00:15.832][silabs ]MATTER TX: 55 AA 01 00 03 E1 0A 00 01 33 2E 30 2E 30 B2 6C 25 21 
[17:32:33.065]  [00:00:15.832][silabs ]COM: CMD: 0xE1, SN: 0x0003, LEN: 18
[17:32:33.065]  
[17:32:33.561]  [00:00:16.333][silabs ]SPP: re-sent reach to max
[17:32:33.561]  [00:00:16.333][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:32:33.561]  [00:00:16.333][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:32:33.565]  
[17:32:33.565]  [00:00:16.333][silabs ]SPP: ack_timeout_ms 500
[17:32:33.781]  [00:00:16.552][silabs ]MATTER RX: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:32:33.781]  [00:00:16.552][silabs ]WDC: report Active percent 0 dev_index 1
[17:32:33.782]  [00:00:16.552][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:32:33.782]  
[17:32:33.782]  [00:00:16.552][info  ][ZCL] Lift[1] Position Set: 10000
[17:32:33.785]  [00:00:16.553][silabs ]SPP: pending ack but allow new cmd process
[17:32:34.063]  [00:00:16.834][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:34.063]  [00:00:16.834][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:32:34.063]  [00:00:16.834][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:32:34.069]  
[17:32:34.280]  [00:00:17.051][silabs ]MATTER RX: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:32:34.280]  [00:00:17.051][silabs ]WDC: report Active percent 0 dev_index 1
[17:32:34.282]  [00:00:17.052][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:32:34.282]  
[17:32:34.282]  [00:00:17.052][info  ][ZCL] Lift[1] Position Set: 10000
[17:32:34.285]  [00:00:17.052][silabs ]SPP: pending ack but allow new cmd process
[17:32:34.563]  [00:00:17.335][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:34.563]  [00:00:17.335][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:32:34.563]  [00:00:17.335][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:32:34.570]  
[17:32:34.829]  [00:00:17.597][silabs ]MATTER RX: 55 AA 01 00 03 E1 00 E4 
[17:32:34.926]  [00:00:17.696][silabs ]MATTER RX: 55 AA 01 00 03 E1 00 E4 
[17:32:34.926]  [00:00:17.698][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:32:34.926]  [00:00:17.698][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:32:34.930]  
[17:32:34.930]  [00:00:17.698][silabs ]SPP: ack_timeout_ms 500
[17:32:35.030]  [00:00:17.796][silabs ]MATTER RX: 55 AA 01 00 03 E1 00 E4 
[17:32:35.125]  [00:00:17.897][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:32:35.125]  [00:00:17.897][silabs ]MATTER RX: 55 AA 01 00 01 06 01 00 08 
[17:32:35.125]  [00:00:17.897][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:32:35.127]  
[17:32:35.127]  [00:00:17.898][silabs ]SPP: ack_timeout_ms 500
[17:32:35.127]  [00:00:17.898][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0001,len:1
[17:32:35.128]  [00:00:17.898][silabs ]payload: 00 
[17:32:35.128]  [00:00:17.898][silabs ]PWR: report Battery Percent 0
[17:32:35.131]  
[17:32:35.131]  [00:00:17.898][silabs ]SPP: pending ack but allow new cmd process
[17:32:35.564]  [00:00:18.333][info  ][SWU] Stopping the watchdog timer
[17:32:35.564]  [00:00:18.333][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[17:32:35.625]  [00:00:18.397][silabs ]MATTER RX: 55 AA 01 01 01 06 01 00 09 
[17:32:35.625]  [00:00:18.398][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:35.627]  [00:00:18.398][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:32:35.627]  [00:00:18.398][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:32:35.627]  
[17:32:35.627]  [00:00:18.398][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0101,len:1
[17:32:35.629]  [00:00:18.398][silabs ]payload: 00 
[17:32:35.629]  [00:00:18.399][silabs ]PWR: report Battery Percent 0
[17:32:35.634]  
[17:32:35.634]  [00:00:18.399][silabs ]SPP: pending ack but allow new cmd process
[17:32:36.125]  [00:00:18.897][silabs ]MATTER RX: 55 AA 01 01 01 06 01 00 09 
[17:32:36.125]  [00:00:18.897][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0101,len:1
[17:32:36.127]  [00:00:18.897][silabs ]payload: 00 
[17:32:36.127]  [00:00:18.897][silabs ]PWR: report Battery Percent 0
[17:32:36.127]  
[17:32:36.127]  [00:00:18.898][silabs ]SPP: pending ack but allow new cmd process
[17:32:36.128]  [00:00:18.898][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:36.128]  [00:00:18.898][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:32:36.131]  [00:00:18.898][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:32:36.134]  
[17:32:36.627]  [00:00:19.398][silabs ]SPP: re-sent reach to max
[17:32:36.627]  [00:00:19.399][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:32:36.627]  [00:00:19.399][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:32:36.630]  
[17:32:36.630]  [00:00:19.399][silabs ]SPP: ack_timeout_ms 500
[17:32:36.675]  [00:00:19.446][silabs ]MATTER RX: 55 AA 01 00 02 07 01 03 0D 
[17:32:36.675]  [00:00:19.447][silabs ]PWR: report Battery Charge State 3
[17:32:36.675]  
[17:32:36.675]  [00:00:19.447][silabs ]SPP: pending ack but allow new cmd process
[17:32:37.127]  [00:00:19.899][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:37.127]  [00:00:19.899][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:32:37.127]  [00:00:19.899][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:32:37.135]  
[17:32:37.174]  [00:00:19.946][silabs ]MATTER RX: 55 AA 01 01 02 07 01 03 0E 
[17:32:37.174]  [00:00:19.946][silabs ]PWR: report Battery Charge State 3
[17:32:37.174]  
[17:32:37.174]  [00:00:19.946][silabs ]SPP: pending ack but allow new cmd process
[17:32:37.628]  [00:00:20.399][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:37.628]  [00:00:20.399][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:32:37.628]  [00:00:20.399][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:32:37.635]  
[17:32:37.674]  [00:00:20.445][silabs ]MATTER RX: 55 AA 01 01 02 07 01 03 0E 
[17:32:37.674]  [00:00:20.445][silabs ]PWR: report Battery Charge State 3
[17:32:37.674]  
[17:32:37.674]  [00:00:20.446][silabs ]SPP: pending ack but allow new cmd process
[17:32:38.128]  [00:00:20.899][silabs ]SPP: re-sent reach to max
[17:32:38.128]  [00:00:20.900][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:38.128]  [00:00:20.900][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:38.131]  
[17:32:38.131]  [00:00:20.900][silabs ]SPP: ack_timeout_ms 500
[17:32:38.223]  [00:00:20.995][silabs ]MATTER RX: 55 AA 01 00 03 08 01 01 0D 
[17:32:38.223]  [00:00:20.995][silabs ]PWR: report Battery Charge Level 1
[17:32:38.223]  
[17:32:38.223]  [00:00:20.995][silabs ]SPP: pending ack but allow new cmd process
[17:32:38.628]  [00:00:21.400][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:38.628]  [00:00:21.400][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:38.628]  [00:00:21.400][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:38.634]  
[17:32:38.722]  [00:00:21.494][silabs ]MATTER RX: 55 AA 01 01 03 08 01 01 0E 
[17:32:38.722]  [00:00:21.495][silabs ]PWR: report Battery Charge Level 1
[17:32:38.722]  
[17:32:38.722]  [00:00:21.495][silabs ]SPP: pending ack but allow new cmd process
[17:32:39.128]  [00:00:21.900][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:39.128]  [00:00:21.900][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:39.128]  [00:00:21.900][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:39.134]  
[17:32:39.222]  [00:00:21.994][silabs ]MATTER RX: 55 AA 01 01 03 08 01 01 0E 
[17:32:39.222]  [00:00:21.994][silabs ]PWR: report Battery Charge Level 1
[17:32:39.222]  
[17:32:39.222]  [00:00:21.994][silabs ]SPP: pending ack but allow new cmd process
[17:32:39.629]  [00:00:22.400][silabs ]SPP: re-sent reach to max
[17:32:39.629]  [00:00:22.401][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:39.629]  [00:00:22.401][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:39.634]  
[17:32:39.634]  [00:00:22.401][silabs ]SPP: ack_timeout_ms 500
[17:32:39.771]  [00:00:22.542][silabs ]MATTER RX: 55 AA 01 00 04 08 01 02 0F 
[17:32:39.771]  [00:00:22.543][silabs ]PWR: report Battery Charge Level 2
[17:32:39.771]  
[17:32:39.771]  [00:00:22.543][silabs ]SPP: pending ack but allow new cmd process
[17:32:40.129]  [00:00:22.901][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:32:40.129]  [00:00:22.901][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:40.129]  [00:00:22.901][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:40.134]  
[17:32:40.271]  [00:00:23.042][silabs ]MATTER RX: 55 AA 01 01 04 08 01 02 10 
[17:32:40.271]  [00:00:23.042][silabs ]PWR: report Battery Charge Level 2
[17:32:40.271]  
[17:32:40.271]  [00:00:23.042][silabs ]SPP: pending ack but allow new cmd process
[17:32:40.629]  [00:00:23.401][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:32:40.629]  [00:00:23.401][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:32:40.629]  [00:00:23.401][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:32:40.634]  
[17:32:40.771]  [00:00:23.541][silabs ]MATTER RX: 55 AA 01 01 04 08 01 02 10 
[17:32:40.771]  [00:00:23.542][silabs ]SPP: tx_queue full!
[17:32:40.771]  [00:00:23.542][silabs ]PWR: report Battery Charge Level 2
[17:32:40.774]  
[17:32:41.129]  [00:00:23.901][silabs ]SPP: re-sent reach to max
[17:32:41.129]  [00:00:23.902][silabs ]MATTER TX: 55 AA 01 00 02 07 00 09 
[17:32:41.129]  [00:00:23.902][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:32:41.134]  
[17:32:41.134]  [00:00:23.902][silabs ]SPP: ack_timeout_ms 500
[17:32:41.320]  [00:00:24.091][silabs ]MATTER RX: 55 AA 01 00 05 E2 01 F0 D8 
[17:32:41.320]  [00:00:24.091][silabs ]payload: F0 
[17:32:41.320]  [00:00:24.091][silabs ]COM: OTAData request without offset, using state offset=0
[17:32:41.326]  [00:00:24.097][silabs ]Firmware checksum: calc=0x25, expected=0x25, PASS
[17:32:41.326]  [00:00:24.097][silabs ]COM: spp_app_event_OTAData, req_offset=0, read_len=240
[17:32:41.427]  [00:00:24.199][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:32:41.427]  [00:00:24.199][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:32:41.427]  
[17:32:41.427]  [00:00:24.199][silabs ]SPP: ack_timeout_ms 500
[17:32:41.819]  [00:00:24.590][silabs ]MATTER RX: 55 AA 01 01 05 E2 01 F0 D9 
[17:32:41.819]  [00:00:24.591][silabs ]payload: F0 
[17:32:41.819]  [00:00:24.591][silabs ]COM: OTAData request without offset, using state offset=240
[17:32:41.820]  [00:00:24.591][silabs ]COM: spp_app_event_OTAData, req_offset=240, read_len=240
[17:32:41.920]  [00:00:24.692][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:32:41.920]  [00:00:24.692][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:32:41.920]  
[17:32:41.920]  [00:00:24.692][silabs ]SPP: ack_timeout_ms 500
[17:32:42.318]  [00:00:25.090][silabs ]MATTER RX: 55 AA 01 01 05 E2 01 F0 D9 
[17:32:42.318]  [00:00:25.090][silabs ]payload: F0 
[17:32:42.318]  [00:00:25.090][silabs ]COM: OTAData request without offset, using state offset=480
[17:32:42.320]  [00:00:25.090][silabs ]COM: spp_app_event_OTAData, req_offset=480, read_len=240
[17:32:42.419]  [00:00:25.191][silabs ]MATTER TX: 55 AA 01 00 03 08 00 0B 
[17:32:42.419]  [00:00:25.191][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:32:42.419]  
[17:32:42.419]  [00:00:25.191][silabs ]SPP: ack_timeout_ms 500
[17:32:42.868]  [00:00:25.640][silabs ]MATTER RX: 55 AA 01 00 06 E2 01 F0 D9 
[17:32:42.868]  [00:00:25.640][silabs ]payload: F0 
[17:32:42.868]  [00:00:25.640][silabs ]COM: OTAData request without offset, using state offset=720
[17:32:42.869]  [00:00:25.640][silabs ]COM: spp_app_event_OTAData, req_offset=720, read_len=240
[17:32:42.970]  [00:00:25.742][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:32:42.970]  [00:00:25.742][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:32:42.970]  
[17:32:42.970]  [00:00:25.742][silabs ]SPP: ack_timeout_ms 500
[17:32:43.367]  [00:00:26.139][silabs ]MATTER RX: 55 AA 01 01 06 E2 01 F0 DA 
[17:32:43.367]  [00:00:26.139][silabs ]payload: F0 
[17:32:43.367]  [00:00:26.139][silabs ]COM: OTAData request without offset, using state offset=960
[17:32:43.369]  [00:00:26.140][silabs ]COM: spp_app_event_OTAData, req_offset=960, read_len=240
[17:32:43.468]  [00:00:26.241][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:32:43.468]  [00:00:26.241][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:32:43.468]  
[17:32:43.468]  [00:00:26.241][silabs ]SPP: ack_timeout_ms 500
[17:32:43.867]  [00:00:26.639][silabs ]MATTER RX: 55 AA 01 01 06 E2 01 F0 DA 
[17:32:43.867]  [00:00:26.639][silabs ]payload: F0 
[17:32:43.867]  [00:00:26.639][silabs ]COM: OTAData request without offset, using state offset=1200
[17:32:43.871]  [00:00:26.639][silabs ]COM: spp_app_event_OTAData, req_offset=1200, read_len=240
[17:32:43.968]  [00:00:26.741][silabs ]MATTER TX: 55 AA 01 00 04 08 00 0C 
[17:32:43.968]  [00:00:26.741][silabs ]COM: CMD: 0x08, SN: 0x0004, LEN: 8
[17:32:43.968]  
[17:32:43.968]  [00:00:26.741][silabs ]SPP: ack_timeout_ms 500
[17:32:44.417]  [00:00:27.188][silabs ]MATTER RX: 55 AA 01 00 07 E2 01 F0 DA 
[17:32:44.417]  [00:00:27.189][silabs ]payload: F0 
[17:32:44.417]  [00:00:27.189][silabs ]COM: OTAData request without offset, using state offset=1440
[17:32:44.420]  [00:00:27.189][silabs ]COM: spp_app_event_OTAData, req_offset=1440, read_len=240
[17:32:44.517]  [00:00:27.290][silabs ]MATTER TX: 55 AA 01 01 04 08 00 0D 
[17:32:44.517]  [00:00:27.290][silabs ]COM: CMD: 0x08, SN: 0x0104, LEN: 8
[17:32:44.517]  
[17:32:44.517]  [00:00:27.290][silabs ]SPP: ack_timeout_ms 500
[17:32:44.916]  [00:00:27.688][silabs ]MATTER RX: 55 AA 01 01 07 E2 01 F0 DB 
[17:32:44.916]  [00:00:27.688][silabs ]payload: F0 
[17:32:44.916]  [00:00:27.688][silabs ]COM: OTAData request without offset, using state offset=1680
[17:32:44.917]  [00:00:27.688][silabs ]COM: spp_app_event_OTAData, req_offset=1680, read_len=240
[17:32:45.017]  [00:00:27.790][silabs ]MATTER TX: 55 AA 01 00 04 E2 F0 48 1B 00 20 99 22 00 00 D9 BB 00 00 95 53 00 00 00 00 00 00 00 00 00 00 00 00 
[17:32:45.023]  [00:00:27.790][silabs ]COM: CMD: 0xE2, SN: 0x0004, LEN: 248
[17:32:45.023]  
[17:32:45.023]  [00:00:27.790][silabs ]SPP: ack_timeout_ms 500
[17:32:45.365]  [00:00:28.137][silabs ]MATTER RX: 55 AA 01 00 08 E2 01 F0 DB 
[17:32:45.365]  [00:00:28.137][silabs ]payload: F0 
[17:32:45.365]  [00:00:28.138][silabs ]COM: OTAData request without offset, using state offset=1920
[17:32:45.370]  [00:00:28.138][silabs ]COM: spp_app_event_OTAData, req_offset=1920, read_len=240
[17:32:45.468]  [00:00:28.239][silabs ]MATTER TX: 55 AA 01 00 05 E2 F0 00 D0 FB 1A 33 43 A2 46 AB 46 18 47 0C B0 00 00 2C B0 00 00 10 3A 02 D3 78 C8 
[17:32:45.471]  [00:00:28.239][silabs ]COM: CMD: 0xE2, SN: 0x0005, LEN: 248
[17:32:45.471]  
[17:32:45.471]  [00:00:28.239][silabs ]SPP: ack_timeout_ms 500
[17:32:45.815]  [00:00:28.586][silabs ]MATTER RX: 55 AA 01 00 09 E2 01 F0 DC 
[17:32:45.815]  [00:00:28.587][silabs ]payload: F0 
[17:32:45.815]  [00:00:28.587][silabs ]COM: OTAData request without offset, using state offset=2160
[17:32:45.819]  [00:00:28.587][silabs ]COM: spp_app_event_OTAData, req_offset=2160, read_len=240
[17:32:45.916]  [00:00:28.688][silabs ]MATTER TX: 55 AA 01 00 06 E2 F0 02 D1 01 F0 B9 FA 10 BD 03 68 DB 09 01 D3 80 23 19 43 63 29 02 D1 01 F0 B8 FF 
[17:32:45.920]  [00:00:28.688][silabs ]COM: CMD: 0xE2, SN: 0x0006, LEN: 248
[17:32:45.920]  
[17:32:45.920]  [00:00:28.688][silabs ]SPP: ack_timeout_ms 500
[17:32:46.265]  [00:00:29.037][silabs ]MATTER RX: 55 AA 01 00 0A E2 01 F0 DD 
[17:32:46.265]  [00:00:29.037][silabs ]payload: F0 
[17:32:46.265]  [00:00:29.037][silabs ]COM: OTAData request without offset, using state offset=2400
[17:32:46.267]  [00:00:29.037][silabs ]COM: spp_app_event_OTAData, req_offset=2400, read_len=240
[17:32:46.366]  [00:00:29.138][silabs ]MATTER TX: 55 AA 01 00 07 E2 F0 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 FE E7 
[17:32:46.370]  [00:00:29.138][silabs ]COM: CMD: 0xE2, SN: 0x0007, LEN: 248
[17:32:46.370]  
[17:32:46.370]  [00:00:29.138][silabs ]SPP: ack_timeout_ms 500
[17:32:46.714]  [00:00:29.486][silabs ]MATTER RX: 55 AA 01 00 0B E2 01 F0 DE 
[17:32:46.714]  [00:00:29.487][silabs ]payload: F0 
[17:32:46.714]  [00:00:29.487][silabs ]COM: OTAData request without offset, using state offset=2640
[17:32:46.715]  [00:00:29.487][silabs ]COM: spp_app_event_OTAData, req_offset=2640, read_len=240
[17:32:46.816]  [00:00:29.587][silabs ]MATTER TX: 55 AA 01 00 08 E2 F0 00 00 00 10 08 ED 00 E0 B4 00 00 20 A0 0A 00 20 0F B4 05 49 10 B5 03 AA 02 98 
[17:32:46.820]  [00:00:29.587][silabs ]COM: CMD: 0xE2, SN: 0x0008, LEN: 248
[17:32:46.820]  
[17:32:46.820]  [00:00:29.587][silabs ]SPP: ack_timeout_ms 500
[17:32:47.164]  [00:00:29.936][silabs ]MATTER RX: 55 AA 01 00 0C E2 01 F0 DF 
[17:32:47.164]  [00:00:29.936][silabs ]payload: F0 
[17:32:47.164]  [00:00:29.936][silabs ]COM: OTAData request without offset, using state offset=2880
[17:32:47.165]  [00:00:29.936][silabs ]COM: spp_app_event_OTAData, req_offset=2880, read_len=240
[17:32:47.266]  [00:00:30.038][silabs ]MATTER TX: 55 AA 01 00 09 E2 F0 EE E7 00 22 DF E7 00 00 00 22 03 09 8B 42 2C D3 03 0A 8B 42 11 D3 00 23 9C 46 
[17:32:47.270]  [00:00:30.038][silabs ]COM: CMD: 0xE2, SN: 0x0009, LEN: 248
[17:32:47.270]  
[17:32:47.270]  [00:00:30.038][silabs ]SPP: ack_timeout_ms 500
[17:32:47.614]  [00:00:30.385][silabs ]MATTER RX: 55 AA 01 00 0D E2 01 F0 E0 
[17:32:47.614]  [00:00:30.385][silabs ]payload: F0 
[17:32:47.614]  [00:00:30.385][silabs ]COM: OTAData request without offset, using state offset=3120
[17:32:47.615]  [00:00:30.386][silabs ]COM: spp_app_event_OTAData, req_offset=3120, read_len=240
[17:32:47.714]  [00:00:30.486][silabs ]MATTER TX: 55 AA 01 00 0A E2 F0 01 D3 8B 01 C0 1A 52 41 43 09 8B 42 01 D3 4B 01 C0 1A 52 41 03 09 8B 42 01 D3 
[17:32:47.718]  [00:00:30.486][silabs ]COM: CMD: 0xE2, SN: 0x000A, LEN: 248
[17:32:47.718]  
[17:32:47.718]  [00:00:30.486][silabs ]SPP: ack_timeout_ms 500
[17:32:48.063]  [00:00:30.834][silabs ]MATTER RX: 55 AA 01 00 0E E2 01 F0 E1 
[17:32:48.063]  [00:00:30.835][silabs ]payload: F0 
[17:32:48.063]  [00:00:30.835][silabs ]COM: OTAData request without offset, using state offset=3360
[17:32:48.064]  [00:00:30.835][silabs ]COM: spp_app_event_OTAData, req_offset=3360, read_len=240
[17:32:48.164]  [00:00:30.936][silabs ]MATTER TX: 55 AA 01 00 0B E2 F0 30 BD FF 21 C9 05 08 43 30 BD 08 46 07 21 09 05 88 43 30 BD 00 00 C0 7F F0 B5 
[17:32:48.168]  [00:00:30.936][silabs ]COM: CMD: 0xE2, SN: 0x000B, LEN: 248
[17:32:48.168]  
[17:32:48.168]  [00:00:30.936][silabs ]SPP: ack_timeout_ms 500
[17:32:48.512]  [00:00:31.285][silabs ]MATTER RX: 55 AA 01 00 0F E2 01 F0 E2 
[17:32:48.512]  [00:00:31.285][silabs ]payload: F0 
[17:32:48.512]  [00:00:31.285][silabs ]COM: OTAData request without offset, using state offset=3600
[17:32:48.514]  [00:00:31.285][silabs ]COM: spp_app_event_OTAData, req_offset=3600, read_len=240
[17:32:48.613]  [00:00:31.385][silabs ]MATTER TX: 55 AA 01 00 0C E2 F0 C9 0F C9 07 D5 E7 9C 4D 4E 00 00 28 01 D0 01 24 00 E0 00 24 34 19 5F 00 00 2A 
[17:32:48.618]  [00:00:31.385][silabs ]COM: CMD: 0xE2, SN: 0x000C, LEN: 248
[17:32:48.618]  
[17:32:48.618]  [00:00:31.385][silabs ]SPP: ack_timeout_ms 500
[17:32:48.962]  [00:00:31.734][silabs ]MATTER RX: 55 AA 01 00 10 E2 01 F0 E3 
[17:32:48.962]  [00:00:31.734][silabs ]payload: F0 
[17:32:48.962]  [00:00:31.735][silabs ]COM: OTAData request without offset, using state offset=3840
[17:32:48.964]  [00:00:31.735][silabs ]COM: spp_app_event_OTAData, req_offset=3840, read_len=240
[17:32:49.063]  [00:00:31.835][silabs ]MATTER TX: 55 AA 01 00 0D E2 F0 4B 05 F3 18 15 24 E3 40 10 D3 00 2B 52 D0 71 46 71 18 D3 0F C0 18 02 D3 49 1C 
[17:32:49.068]  [00:00:31.835][silabs ]COM: CMD: 0xE2, SN: 0x000D, LEN: 248
[17:32:49.068]  
[17:32:49.068]  [00:00:31.835][silabs ]SPP: ack_timeout_ms 500
[17:32:49.412]  [00:00:32.184][silabs ]MATTER RX: 55 AA 01 00 11 E2 01 F0 E4 
[17:32:49.412]  [00:00:32.184][silabs ]payload: F0 
[17:32:49.412]  [00:00:32.184][silabs ]COM: OTAData request without offset, using state offset=4080
[17:32:49.416]  [00:00:32.184][silabs ]COM: spp_app_event_OTAData, req_offset=4080, read_len=240
[17:32:49.514]  [00:00:32.286][silabs ]MATTER TX: 55 AA 01 00 0E E2 F0 00 21 71 18 5F 00 00 2A 01 D0 01 26 00 E0 00 26 BE 19 22 4F A9 42 10 D8 AE 42 
[17:32:49.518]  [00:00:32.286][silabs ]COM: CMD: 0xE2, SN: 0x000E, LEN: 248
[17:32:49.518]  
[17:32:49.518]  [00:00:32.286][silabs ]SPP: ack_timeout_ms 500
[17:32:49.862]  [00:00:32.633][silabs ]MATTER RX: 55 AA 01 00 12 E2 01 F0 E5 
[17:32:49.862]  [00:00:32.633][silabs ]payload: F0 
[17:32:49.862]  [00:00:32.633][silabs ]COM: OTAData request without offset, using state offset=4320
[17:32:49.866]  [00:00:32.634][silabs ]COM: spp_app_event_OTAData, req_offset=4320, read_len=240
[17:32:49.961]  [00:00:32.734][silabs ]MATTER TX: 55 AA 01 00 0F E2 F0 00 95 8C 46 01 04 23 46 8B 43 0A 91 61 46 09 04 E2 4D 8A 43 09 91 01 0A 7D 44 
[17:32:49.965]  [00:00:32.734][silabs ]COM: CMD: 0xE2, SN: 0x000F, LEN: 248
[17:32:49.965]  
[17:32:49.965]  [00:00:32.734][silabs ]SPP: ack_timeout_ms 500
[17:32:50.311]  [00:00:33.083][silabs ]MATTER RX: 55 AA 01 00 13 E2 01 F0 E6 
[17:32:50.311]  [00:00:33.083][silabs ]payload: F0 
[17:32:50.311]  [00:00:33.083][silabs ]COM: OTAData request without offset, using state offset=4560
[17:32:50.314]  [00:00:33.083][silabs ]COM: spp_app_event_OTAData, req_offset=4560, read_len=240
[17:32:50.412]  [00:00:33.184][silabs ]MATTER TX: 55 AA 01 00 10 E2 F0 04 9D E4 04 2C 1B 04 94 06 D2 02 9C 03 9D 64 1C 00 26 75 41 03 95 02 94 01 AC 
[17:32:50.415]  [00:00:33.184][silabs ]COM: CMD: 0xE2, SN: 0x0010, LEN: 248
[17:32:50.415]  
[17:32:50.415]  [00:00:33.184][silabs ]SPP: ack_timeout_ms 500
[17:32:50.761]  [00:00:33.533][silabs ]MATTER RX: 55 AA 01 00 14 E2 01 F0 E7 
[17:32:50.761]  [00:00:33.533][silabs ]payload: F0 
[17:32:50.761]  [00:00:33.533][silabs ]COM: OTAData request without offset, using state offset=4800
[17:32:50.764]  [00:00:33.533][silabs ]COM: spp_app_event_OTAData, req_offset=4800, read_len=240
[17:32:50.862]  [00:00:33.634][silabs ]MATTER TX: 55 AA 01 00 11 E2 F0 0D 46 45 43 68 0B EF 04 0D 46 64 46 65 43 6C 0B 3C 43 04 9F ED 04 7D 1B AC 46 
[17:32:50.866]  [00:00:33.634][silabs ]COM: CMD: 0xE2, SN: 0x0011, LEN: 248
[17:32:50.866]  
[17:32:50.866]  [00:00:33.634][silabs ]SPP: ack_timeout_ms 500
[17:32:51.210]  [00:00:33.982][silabs ]MATTER RX: 55 AA 01 00 15 E2 01 F0 E8 
[17:32:51.210]  [00:00:33.983][silabs ]payload: F0 
[17:32:51.210]  [00:00:33.983][silabs ]COM: OTAData request without offset, using state offset=5040
[17:32:51.211]  [00:00:33.983][silabs ]COM: spp_app_event_OTAData, req_offset=5040, read_len=240
[17:32:51.311]  [00:00:34.083][silabs ]MATTER TX: 55 AA 01 00 12 E2 F0 A8 42 02 D9 28 46 1A 46 64 1C 10 43 01 22 00 28 00 D0 16 43 61 02 00 20 07 9B 
[17:32:51.315]  [00:00:34.083][silabs ]COM: CMD: 0xE2, SN: 0x0012, LEN: 248
[17:32:51.315]  
[17:32:51.315]  [00:00:34.083][silabs ]SPP: ack_timeout_ms 500
[17:32:51.659]  [00:00:34.432][silabs ]MATTER RX: 55 AA 01 00 16 E2 01 F0 E9 
[17:32:51.659]  [00:00:34.432][silabs ]payload: F0 
[17:32:51.659]  [00:00:34.432][silabs ]COM: OTAData request without offset, using state offset=5280
[17:32:51.661]  [00:00:34.432][silabs ]COM: spp_app_event_OTAData, req_offset=5280, read_len=240
[17:32:51.762]  [00:00:34.534][silabs ]MATTER TX: 55 AA 01 00 13 E2 F0 9A 42 05 DC 03 22 52 07 89 18 C9 0F C9 07 B5 E7 05 22 52 07 89 18 07 4A 11 43 
[17:32:51.765]  [00:00:34.534][silabs ]COM: CMD: 0xE2, SN: 0x0013, LEN: 248
[17:32:51.765]  
[17:32:51.765]  [00:00:34.534][silabs ]SPP: ack_timeout_ms 500
[17:32:52.109]  [00:00:34.881][silabs ]MATTER RX: 55 AA 01 00 17 E2 01 F0 EA 
[17:32:52.109]  [00:00:34.881][silabs ]payload: F0 
[17:32:52.109]  [00:00:34.881][silabs ]COM: OTAData request without offset, using state offset=5520
[17:32:52.110]  [00:00:34.882][silabs ]COM: spp_app_event_OTAData, req_offset=5520, read_len=240
[17:32:52.210]  [00:00:34.983][silabs ]MATTER TX: 55 AA 01 00 14 E2 F0 92 07 11 43 D6 E7 01 21 89 07 D3 E7 F0 B5 8B 4C 0F 09 25 46 89 B0 BD 43 7B D0 
[17:32:52.214]  [00:00:34.983][silabs ]COM: CMD: 0xE2, SN: 0x0014, LEN: 248
[17:32:52.214]  
[17:32:52.214]  [00:00:34.983][silabs ]SPP: ack_timeout_ms 500
[17:32:52.559]  [00:00:35.332][silabs ]MATTER RX: 55 AA 01 00 18 E2 01 F0 EB 
[17:32:52.559]  [00:00:35.332][silabs ]payload: F0 
[17:32:52.559]  [00:00:35.332][silabs ]COM: OTAData request without offset, using state offset=5760
[17:32:52.560]  [00:00:35.332][silabs ]COM: spp_app_event_OTAData, req_offset=5760, read_len=240
[17:32:52.660]  [00:00:35.432][silabs ]MATTER TX: 55 AA 01 00 15 E2 F0 08 91 69 1A 01 91 04 9E 01 46 51 43 A4 1B 04 91 61 1A 00 9C 07 91 E1 06 05 D0 
[17:32:52.664]  [00:00:35.432][silabs ]COM: CMD: 0xE2, SN: 0x0015, LEN: 248
[17:32:52.664]  
[17:32:52.664]  [00:00:35.432][silabs ]SPP: ack_timeout_ms 500
[17:32:53.008]  [00:00:35.781][silabs ]MATTER RX: 55 AA 01 00 19 E2 01 F0 EC 
[17:32:53.008]  [00:00:35.781][silabs ]payload: F0 
[17:32:53.008]  [00:00:35.781][silabs ]COM: OTAData request without offset, using state offset=6000
[17:32:53.009]  [00:00:35.781][silabs ]COM: spp_app_event_OTAData, req_offset=6000, read_len=240
[17:32:53.110]  [00:00:35.882][silabs ]MATTER TX: 55 AA 01 00 16 E2 F0 41 40 04 E0 03 20 40 07 08 18 C1 0F C9 07 00 20 09 B0 F0 BD 00 20 F1 07 FA E7 
[17:32:53.114]  [00:00:35.882][silabs ]COM: CMD: 0xE2, SN: 0x0016, LEN: 248
[17:32:53.114]  
[17:32:53.114]  [00:00:35.882][silabs ]SPP: ack_timeout_ms 500
[17:32:53.458]  [00:00:36.230][silabs ]MATTER RX: 55 AA 01 00 1A E2 01 F0 ED 
[17:32:53.458]  [00:00:36.231][silabs ]payload: F0 
[17:32:53.458]  [00:00:36.231][silabs ]COM: OTAData request without offset, using state offset=6240
[17:32:53.459]  [00:00:36.231][silabs ]COM: spp_app_event_OTAData, req_offset=6240, read_len=240
[17:32:53.559]  [00:00:36.332][silabs ]MATTER TX: 55 AA 01 00 17 E2 F0 67 D0 AB 42 65 D0 00 28 00 DA 32 46 01 25 ED 05 29 43 2C 43 09 02 20 02 09 0A 
[17:32:53.563]  [00:00:36.332][silabs ]COM: CMD: 0xE2, SN: 0x0017, LEN: 248
[17:32:53.563]  
[17:32:53.563]  [00:00:36.332][silabs ]SPP: ack_timeout_ms 500
[17:32:53.908]  [00:00:36.680][silabs ]MATTER RX: 55 AA 01 00 1B E2 01 F0 EE 
[17:32:53.908]  [00:00:36.680][silabs ]payload: F0 
[17:32:53.908]  [00:00:36.680][silabs ]COM: OTAData request without offset, using state offset=6480
[17:32:53.909]  [00:00:36.680][silabs ]COM: spp_app_event_OTAData, req_offset=6480, read_len=240
[17:32:54.010]  [00:00:36.782][silabs ]MATTER TX: 55 AA 01 00 18 E2 F0 63 00 2D 06 AB 42 F9 D8 49 00 A9 42 F6 D8 AB 42 01 D1 A9 42 F2 D0 A9 42 01 D1 
[17:32:54.014]  [00:00:36.782][silabs ]COM: CMD: 0xE2, SN: 0x0018, LEN: 248
[17:32:54.014]  
[17:32:54.014]  [00:00:36.782][silabs ]SPP: ack_timeout_ms 500
[17:32:54.358]  [00:00:37.129][silabs ]MATTER RX: 55 AA 01 00 1C E2 01 F0 EF 
[17:32:54.358]  [00:00:37.129][silabs ]payload: F0 
[17:32:54.358]  [00:00:37.130][silabs ]COM: OTAData request without offset, using state offset=6720
[17:32:54.359]  [00:00:37.130][silabs ]COM: spp_app_event_OTAData, req_offset=6720, read_len=240
[17:32:54.459]  [00:00:37.231][silabs ]MATTER TX: 55 AA 01 00 19 E2 F0 D0 E7 10 B5 00 F0 A6 FA 00 68 10 BD 10 B5 04 46 00 F0 A0 FA 04 60 10 BD 70 B5 
[17:32:54.463]  [00:00:37.231][silabs ]COM: CMD: 0xE2, SN: 0x0019, LEN: 248
[17:32:54.463]  
[17:32:54.463]  [00:00:37.231][silabs ]SPP: ack_timeout_ms 500
[17:32:54.807]  [00:00:37.580][silabs ]MATTER RX: 55 AA 01 00 1D E2 01 F0 F0 
[17:32:54.807]  [00:00:37.580][silabs ]payload: F0 
[17:32:54.807]  [00:00:37.580][silabs ]COM: OTAData request without offset, using state offset=6960
[17:32:54.809]  [00:00:37.580][silabs ]COM: spp_app_event_OTAData, req_offset=6960, read_len=240
[17:32:54.908]  [00:00:37.680][silabs ]MATTER TX: 55 AA 01 00 1A E2 F0 02 DA 40 42 11 A6 08 E0 00 99 09 68 8A 07 01 D5 0F A6 02 E0 49 07 04 D5 0E A6 
[17:32:54.913]  [00:00:37.680][silabs ]COM: CMD: 0xE2, SN: 0x001A, LEN: 248
[17:32:54.913]  
[17:32:54.913]  [00:00:37.680][silabs ]SPP: ack_timeout_ms 500
[17:32:55.257]  [00:00:38.029][silabs ]MATTER RX: 55 AA 01 00 1E E2 01 F0 F1 
[17:32:55.257]  [00:00:38.029][silabs ]payload: F0 
[17:32:55.257]  [00:00:38.029][silabs ]COM: OTAData request without offset, using state offset=7200
[17:32:55.259]  [00:00:38.030][silabs ]COM: spp_app_event_OTAData, req_offset=7200, read_len=240
[17:32:55.358]  [00:00:38.130][silabs ]MATTER TX: 55 AA 01 00 1B E2 F0 AE 42 E5 DB 07 98 71 00 40 5A 00 28 E0 D1 A0 69 C0 1B A0 61 20 46 FF F7 0F FF 
[17:32:55.363]  [00:00:38.130][silabs ]COM: CMD: 0xE2, SN: 0x001B, LEN: 248
[17:32:55.363]  
[17:32:55.363]  [00:00:38.130][silabs ]SPP: ack_timeout_ms 500
[17:32:55.706]  [00:00:38.478][silabs ]MATTER RX: 55 AA 01 00 1F E2 01 F0 F2 
[17:32:55.706]  [00:00:38.479][silabs ]payload: F0 
[17:32:55.706]  [00:00:38.479][silabs ]COM: OTAData request without offset, using state offset=7440
[17:32:55.707]  [00:00:38.479][silabs ]COM: spp_app_event_OTAData, req_offset=7440, read_len=240
[17:32:55.809]  [00:00:38.581][silabs ]MATTER TX: 55 AA 01 00 1C E2 F0 D2 08 6D 0F 30 35 65 54 5D 07 2A 43 DB 08 49 1C 15 46 1D 43 F3 D1 04 68 00 23 
[17:32:55.813]  [00:00:38.581][silabs ]COM: CMD: 0xE2, SN: 0x001C, LEN: 248
[17:32:55.813]  
[17:32:55.813]  [00:00:38.581][silabs ]SPP: ack_timeout_ms 500
[17:32:56.156]  [00:00:38.928][silabs ]MATTER RX: 55 AA 01 00 20 E2 01 F0 F3 
[17:32:56.156]  [00:00:38.928][silabs ]payload: F0 
[17:32:56.156]  [00:00:38.928][silabs ]COM: OTAData request without offset, using state offset=7680
[17:32:56.159]  [00:00:38.928][silabs ]COM: spp_app_event_OTAData, req_offset=7680, read_len=240
[17:32:56.257]  [00:00:39.029][silabs ]MATTER TX: 55 AA 01 00 1D E2 F0 C3 61 30 BC 00 23 B5 E7 90 94 00 00 F3 B5 04 46 00 20 81 B0 20 62 20 46 E1 68 
[17:32:56.260]  [00:00:39.029][silabs ]COM: CMD: 0xE2, SN: 0x001D, LEN: 248
[17:32:56.260]  
[17:32:56.260]  [00:00:39.029][silabs ]SPP: ack_timeout_ms 500
[17:32:56.606]  [00:00:39.377][silabs ]MATTER RX: 55 AA 01 00 21 E2 01 F0 F4 
[17:32:56.606]  [00:00:39.378][silabs ]payload: F0 
[17:32:56.606]  [00:00:39.378][silabs ]COM: OTAData request without offset, using state offset=7920
[17:32:56.609]  [00:00:39.378][silabs ]COM: spp_app_event_OTAData, req_offset=7920, read_len=240
[17:32:56.707]  [00:00:39.479][silabs ]MATTER TX: 55 AA 01 00 1E E2 F0 68 2D 09 D0 4C 2D 3C D0 6A 2D 38 D0 74 2D 38 D0 7A 2D 36 D0 16 E0 40 E0 E1 68 
[17:32:56.710]  [00:00:39.479][silabs ]COM: CMD: 0xE2, SN: 0x001E, LEN: 248
[17:32:56.710]  
[17:32:56.710]  [00:00:39.479][silabs ]SPP: ack_timeout_ms 500
[17:32:57.055]  [00:00:39.828][silabs ]MATTER RX: 55 AA 01 00 22 E2 01 F0 F5 
[17:32:57.055]  [00:00:39.828][silabs ]payload: F0 
[17:32:57.055]  [00:00:39.828][silabs ]COM: OTAData request without offset, using state offset=8160
[17:32:57.059]  [00:00:39.828][silabs ]COM: spp_app_event_OTAData, req_offset=8160, read_len=240
[17:32:57.156]  [00:00:39.928][silabs ]MATTER TX: 55 AA 01 00 1F E2 F0 E9 08 84 0F 8D 00 25 43 84 00 24 18 4D 41 24 19 6D 41 12 1B AB 41 07 E0 09 25 
[17:32:57.159]  [00:00:39.928][silabs ]COM: CMD: 0xE2, SN: 0x001F, LEN: 248
[17:32:57.159]  
[17:32:57.159]  [00:00:39.928][silabs ]SPP: ack_timeout_ms 500
[17:32:57.504]  [00:00:40.277][silabs ]MATTER RX: 55 AA 01 00 23 E2 01 F0 F6 
[17:32:57.504]  [00:00:40.277][silabs ]payload: F0 
[17:32:57.504]  [00:00:40.277][silabs ]COM: OTAData request without offset, using state offset=8400
[17:32:57.508]  [00:00:40.278][silabs ]COM: spp_app_event_OTAData, req_offset=8400, read_len=240
[17:32:57.606]  [00:00:40.378][silabs ]MATTER TX: 55 AA 01 00 20 E2 F0 03 CA 08 90 09 91 4F 00 7D 0D 00 D1 6D 1E 00 21 08 46 00 20 C0 46 03 21 09 9A 
[17:32:57.610]  [00:00:40.378][silabs ]COM: CMD: 0xE2, SN: 0x0020, LEN: 248
[17:32:57.610]  
[17:32:57.610]  [00:00:40.378][silabs ]SPP: ack_timeout_ms 500
[17:32:57.954]  [00:00:40.727][silabs ]MATTER RX: 55 AA 01 00 24 E2 01 F0 F7 
[17:32:57.954]  [00:00:40.727][silabs ]payload: F0 
[17:32:57.954]  [00:00:40.727][silabs ]COM: OTAData request without offset, using state offset=8640
[17:32:57.958]  [00:00:40.727][silabs ]COM: spp_app_event_OTAData, req_offset=8640, read_len=240
[17:32:58.057]  [00:00:40.829][silabs ]MATTER TX: 55 AA 01 00 21 E2 F0 03 D0 00 20 C0 43 41 08 00 E0 10 46 18 9A 00 2A 03 D0 00 22 00 92 15 46 1E E0 
[17:32:58.060]  [00:00:40.829][silabs ]COM: CMD: 0xE2, SN: 0x0021, LEN: 248
[17:32:58.060]  
[17:32:58.060]  [00:00:40.829][silabs ]SPP: ack_timeout_ms 500
[17:32:58.403]  [00:00:41.176][silabs ]MATTER RX: 55 AA 01 00 25 E2 01 F0 F8 
[17:32:58.403]  [00:00:41.176][silabs ]payload: F0 
[17:32:58.403]  [00:00:41.176][silabs ]COM: OTAData request without offset, using state offset=8880
[17:32:58.408]  [00:00:41.176][silabs ]COM: spp_app_event_OTAData, req_offset=8880, read_len=240
[17:32:58.504]  [00:00:41.277][silabs ]MATTER TX: 55 AA 01 00 22 E2 F0 80 06 01 D5 E7 69 00 E0 06 27 28 46 65 2D 04 D0 66 28 14 D0 67 2D 69 D1 2D E0 
[17:32:58.508]  [00:00:41.277][silabs ]COM: CMD: 0xE2, SN: 0x0022, LEN: 248
[17:32:58.508]  
[17:32:58.508]  [00:00:41.277][silabs ]SPP: ack_timeout_ms 500
[17:32:58.853]  [00:00:41.625][silabs ]MATTER RX: 55 AA 01 00 26 E2 01 F0 F9 
[17:32:58.853]  [00:00:41.625][silabs ]payload: F0 
[17:32:58.853]  [00:00:41.626][silabs ]COM: OTAData request without offset, using state offset=9120
[17:32:58.855]  [00:00:41.626][silabs ]COM: spp_app_event_OTAData, req_offset=9120, read_len=240
[17:32:58.954]  [00:00:41.727][silabs ]MATTER TX: 55 AA 01 00 23 E2 F0 05 D4 00 98 A8 42 02 DB 00 20 C0 43 00 90 69 46 00 20 C8 72 0B 98 01 21 02 AF 
[17:32:58.957]  [00:00:41.727][silabs ]COM: CMD: 0xE2, SN: 0x0023, LEN: 248
[17:32:58.957]  
[17:32:58.957]  [00:00:41.727][silabs ]SPP: ack_timeout_ms 500
[17:32:59.303]  [00:00:42.076][silabs ]MATTER RX: 55 AA 01 00 27 E2 01 F0 FA 
[17:32:59.303]  [00:00:42.076][silabs ]payload: F0 
[17:32:59.303]  [00:00:42.076][silabs ]COM: OTAData request without offset, using state offset=9360
[17:32:59.304]  [00:00:42.076][silabs ]COM: spp_app_event_OTAData, req_offset=9360, read_len=240
[17:32:59.404]  [00:00:42.176][silabs ]MATTER TX: 55 AA 01 00 24 E2 F0 C0 68 62 68 01 68 40 5C A1 68 90 47 20 6A 40 1C 20 62 28 46 6D 1E 00 28 D9 DC 
[17:32:59.408]  [00:00:42.176][silabs ]COM: CMD: 0xE2, SN: 0x0024, LEN: 248
[17:32:59.408]  
[17:32:59.408]  [00:00:42.176][silabs ]SPP: ack_timeout_ms 500
[17:32:59.753]  [00:00:42.525][silabs ]MATTER RX: 55 AA 01 00 28 E2 01 F0 FB 
[17:32:59.753]  [00:00:42.525][silabs ]payload: F0 
[17:32:59.753]  [00:00:42.525][silabs ]COM: OTAData request without offset, using state offset=9600
[17:32:59.754]  [00:00:42.525][silabs ]COM: spp_app_event_OTAData, req_offset=9600, read_len=240
[17:32:59.854]  [00:00:42.626][silabs ]MATTER TX: 55 AA 01 00 25 E2 F0 01 23 18 3A 1B 07 D3 40 03 E0 01 22 12 05 CA 40 94 46 0C 31 20 29 02 D3 3A 46 
[17:32:59.858]  [00:00:42.626][silabs ]COM: CMD: 0xE2, SN: 0x0025, LEN: 248
[17:32:59.858]  
[17:32:59.858]  [00:00:42.626][silabs ]SPP: ack_timeout_ms 500
[17:33:00.202]  [00:00:42.974][silabs ]MATTER RX: 55 AA 01 00 29 E2 01 F0 FC 
[17:33:00.202]  [00:00:42.974][silabs ]payload: F0 
[17:33:00.202]  [00:00:42.975][silabs ]COM: OTAData request without offset, using state offset=9840
[17:33:00.203]  [00:00:42.975][silabs ]COM: spp_app_event_OTAData, req_offset=9840, read_len=240
[17:33:00.303]  [00:00:43.076][silabs ]MATTER TX: 55 AA 01 00 26 E2 F0 CB 5C 52 1C 6D 1E 33 54 40 1C 08 2A 01 DA 00 2D F4 DC 23 68 9A 06 01 D5 11 E0 
[17:33:00.308]  [00:00:43.076][silabs ]COM: CMD: 0xE2, SN: 0x0026, LEN: 248
[17:33:00.308]  
[17:33:00.308]  [00:00:43.076][silabs ]SPP: ack_timeout_ms 500
[17:33:00.651]  [00:00:43.424][silabs ]MATTER RX: 55 AA 01 00 2A E2 01 F0 FD 
[17:33:00.651]  [00:00:43.424][silabs ]payload: F0 
[17:33:00.651]  [00:00:43.424][silabs ]COM: OTAData request without offset, using state offset=10080
[17:33:00.653]  [00:00:43.424][silabs ]COM: spp_app_event_OTAData, req_offset=10080, read_len=240
[17:33:00.752]  [00:00:43.525][silabs ]MATTER TX: 55 AA 01 00 27 E2 F0 20 78 C0 06 02 D5 20 46 FF F7 76 F9 02 AE 09 E0 30 78 76 1C 3E 28 0D D0 62 68 
[17:33:00.758]  [00:00:43.525][silabs ]COM: CMD: 0xE2, SN: 0x0027, LEN: 248
[17:33:00.758]  
[17:33:00.758]  [00:00:43.525][silabs ]SPP: ack_timeout_ms 500
[17:33:01.101]  [00:00:43.874][silabs ]MATTER RX: 55 AA 01 00 2B E2 01 F0 FE 
[17:33:01.101]  [00:00:43.874][silabs ]payload: F0 
[17:33:01.101]  [00:00:43.874][silabs ]COM: OTAData request without offset, using state offset=10320
[17:33:01.102]  [00:00:43.874][silabs ]COM: spp_app_event_OTAData, req_offset=10320, read_len=240
[17:33:01.202]  [00:00:43.975][silabs ]MATTER TX: 55 AA 01 00 28 E2 F0 02 30 C0 5C 01 28 07 D0 FF 2C 0F D8 18 5D 00 28 0C D0 01 20 2C 70 F8 BD FF 33 
[17:33:01.207]  [00:00:43.975][silabs ]COM: CMD: 0xE2, SN: 0x0028, LEN: 248
[17:33:01.207]  
[17:33:01.207]  [00:00:43.975][silabs ]SPP: ack_timeout_ms 500
[17:33:01.550]  [00:00:44.323][silabs ]MATTER RX: 55 AA 01 00 2C E2 01 F0 FF 
[17:33:01.550]  [00:00:44.323][silabs ]payload: F0 
[17:33:01.550]  [00:00:44.324][silabs ]COM: OTAData request without offset, using state offset=10560
[17:33:01.554]  [00:00:44.324][silabs ]COM: spp_app_event_OTAData, req_offset=10560, read_len=240
[17:33:01.651]  [00:00:44.424][silabs ]MATTER TX: 55 AA 01 00 29 E2 F0 05 E0 EF F3 00 80 01 21 90 43 C9 07 08 43 80 F3 00 88 10 BD 0D 23 1B 04 1A 42 
[17:33:01.654]  [00:00:44.424][silabs ]COM: CMD: 0xE2, SN: 0x0029, LEN: 248
[17:33:01.654]  
[17:33:01.654]  [00:00:44.424][silabs ]SPP: ack_timeout_ms 500
[17:33:02.001]  [00:00:44.773][silabs ]MATTER RX: 55 AA 01 00 2D E2 01 F0 00 
[17:33:02.001]  [00:00:44.773][silabs ]payload: F0 
[17:33:02.001]  [00:00:44.773][silabs ]COM: OTAData request without offset, using state offset=10800
[17:33:02.001]  [00:00:44.773][silabs ]COM: spp_app_event_OTAData, req_offset=10800, read_len=240
[17:33:02.102]  [00:00:44.875][silabs ]MATTER TX: 55 AA 01 00 2A E2 F0 FA E7 62 68 28 78 A1 68 6D 1C 90 47 76 1E F8 D2 20 46 FF F7 1F F8 F8 BD 4E 41 
[17:33:02.107]  [00:00:44.875][silabs ]COM: CMD: 0xE2, SN: 0x002A, LEN: 248
[17:33:02.107]  
[17:33:02.107]  [00:00:44.875][silabs ]SPP: ack_timeout_ms 500
[17:33:02.449]  [00:00:45.222][silabs ]MATTER RX: 55 AA 01 00 2E E2 01 F0 01 
[17:33:02.449]  [00:00:45.222][silabs ]payload: F0 
[17:33:02.449]  [00:00:45.222][silabs ]COM: OTAData request without offset, using state offset=11040
[17:33:02.452]  [00:00:45.222][silabs ]COM: spp_app_event_OTAData, req_offset=11040, read_len=240
[17:33:02.552]  [00:00:45.324][silabs ]MATTER TX: 55 AA 01 00 2B E2 F0 21 FA 0A 9B 07 C3 0D B0 F0 BD 00 00 3C 89 00 00 03 46 40 00 0A 46 10 B5 40 0D 
[17:33:02.555]  [00:00:45.324][silabs ]COM: CMD: 0xE2, SN: 0x002B, LEN: 248
[17:33:02.555]  
[17:33:02.555]  [00:00:45.324][silabs ]SPP: ack_timeout_ms 500
[17:33:02.899]  [00:00:45.671][silabs ]MATTER RX: 55 AA 01 00 2F E2 01 F0 02 
[17:33:02.899]  [00:00:45.671][silabs ]payload: F0 
[17:33:02.899]  [00:00:45.672][silabs ]COM: OTAData request without offset, using state offset=11280
[17:33:02.902]  [00:00:45.672][silabs ]COM: spp_app_event_OTAData, req_offset=11280, read_len=240
[17:33:03.000]  [00:00:45.773][silabs ]MATTER TX: 55 AA 01 00 2C E2 F0 40 18 FA 49 47 18 14 E0 01 99 40 00 C9 0F 08 43 00 90 01 98 02 99 40 00 C9 0F 
[17:33:03.003]  [00:00:45.773][silabs ]COM: CMD: 0xE2, SN: 0x002C, LEN: 248
[17:33:03.003]  
[17:33:03.003]  [00:00:45.773][silabs ]SPP: ack_timeout_ms 500
[17:33:03.348]  [00:00:46.121][silabs ]MATTER RX: 55 AA 01 00 30 E2 01 F0 03 
[17:33:03.348]  [00:00:46.122][silabs ]payload: F0 
[17:33:03.348]  [00:00:46.122][silabs ]COM: OTAData request without offset, using state offset=11520
[17:33:03.350]  [00:00:46.122][silabs ]COM: spp_app_event_OTAData, req_offset=11520, read_len=240
[17:33:03.450]  [00:00:46.222][silabs ]MATTER TX: 55 AA 01 00 2D E2 F0 20 E0 90 42 04 D8 90 42 0C D1 01 9B 0B 42 09 D0 01 9B 59 18 01 91 05 D1 00 99 
[17:33:03.453]  [00:00:46.222][silabs ]COM: CMD: 0xE2, SN: 0x002D, LEN: 248
[17:33:03.453]  
[17:33:03.453]  [00:00:46.222][silabs ]SPP: ack_timeout_ms 500
[17:33:03.797]  [00:00:46.571][silabs ]MATTER RX: 55 AA 01 00 31 E2 01 F0 04 
[17:33:03.797]  [00:00:46.571][silabs ]payload: F0 
[17:33:03.797]  [00:00:46.571][silabs ]COM: OTAData request without offset, using state offset=11760
[17:33:03.799]  [00:00:46.571][silabs ]COM: spp_app_event_OTAData, req_offset=11760, read_len=240
[17:33:03.900]  [00:00:46.672][silabs ]MATTER TX: 55 AA 01 00 2E E2 F0 40 41 52 1C 06 9B 9A 42 D7 DB 00 2D 04 D1 75 46 03 9A 6B 1A 82 41 01 D2 03 20 
[17:33:03.904]  [00:00:46.672][silabs ]COM: CMD: 0xE2, SN: 0x002E, LEN: 248
[17:33:03.904]  
[17:33:03.904]  [00:00:46.672][silabs ]SPP: ack_timeout_ms 500
[17:33:04.248]  [00:00:47.020][silabs ]MATTER RX: 55 AA 01 00 32 E2 01 F0 05 
[17:33:04.248]  [00:00:47.020][silabs ]payload: F0 
[17:33:04.248]  [00:00:47.020][silabs ]COM: OTAData request without offset, using state offset=12000
[17:33:04.249]  [00:00:47.021][silabs ]COM: spp_app_event_OTAData, req_offset=12000, read_len=240
[17:33:04.349]  [00:00:47.122][silabs ]MATTER TX: 55 AA 01 00 2F E2 F0 08 43 01 21 D2 0A C9 02 D2 02 01 92 00 E0 01 21 10 9B 01 22 D2 07 01 2B 02 D0 
[17:33:04.352]  [00:00:47.122][silabs ]COM: CMD: 0xE2, SN: 0x002F, LEN: 248
[17:33:04.352]  
[17:33:04.352]  [00:00:47.122][silabs ]SPP: ack_timeout_ms 500
[17:33:04.697]  [00:00:47.469][silabs ]MATTER RX: 55 AA 01 00 33 E2 01 F0 06 
[17:33:04.697]  [00:00:47.470][silabs ]payload: F0 
[17:33:04.697]  [00:00:47.470][silabs ]COM: OTAData request without offset, using state offset=12240
[17:33:04.699]  [00:00:47.470][silabs ]COM: spp_app_event_OTAData, req_offset=12240, read_len=240
[17:33:04.799]  [00:00:47.572][silabs ]MATTER TX: 55 AA 01 00 30 E2 F0 04 46 0D 46 0E 46 10 21 08 46 00 20 C0 46 00 2F 03 D0 04 21 08 46 00 20 C0 46 
[17:33:04.803]  [00:00:47.572][silabs ]COM: CMD: 0xE2, SN: 0x0030, LEN: 248
[17:33:04.803]  
[17:33:04.803]  [00:00:47.572][silabs ]SPP: ack_timeout_ms 500
[17:33:05.146]  [00:00:47.919][silabs ]MATTER RX: 55 AA 01 00 34 E2 01 F0 07 
[17:33:05.146]  [00:00:47.919][silabs ]payload: F0 
[17:33:05.146]  [00:00:47.919][silabs ]COM: OTAData request without offset, using state offset=12480
[17:33:05.147]  [00:00:47.919][silabs ]COM: spp_app_event_OTAData, req_offset=12480, read_len=240
[17:33:05.247]  [00:00:48.020][silabs ]MATTER TX: 55 AA 01 00 31 E2 F0 C8 02 12 D5 48 03 40 0F 00 28 04 D0 C8 03 C0 43 01 21 88 40 70 47 EF F3 00 80 
[17:33:05.252]  [00:00:48.020][silabs ]COM: CMD: 0xE2, SN: 0x0031, LEN: 248
[17:33:05.252]  
[17:33:05.252]  [00:00:48.020][silabs ]SPP: ack_timeout_ms 500
[17:33:05.596]  [00:00:48.369][silabs ]MATTER RX: 55 AA 01 00 35 E2 01 F0 08 
[17:33:05.596]  [00:00:48.369][silabs ]payload: F0 
[17:33:05.596]  [00:00:48.369][silabs ]COM: OTAData request without offset, using state offset=12720
[17:33:05.600]  [00:00:48.370][silabs ]COM: spp_app_event_OTAData, req_offset=12720, read_len=240
[17:33:05.697]  [00:00:48.470][silabs ]MATTER TX: 55 AA 01 00 32 E2 F0 01 D5 01 20 C0 07 21 46 10 BD D1 06 07 D5 01 01 09 09 CC 08 49 07 00 0E 00 06 
[17:33:05.703]  [00:00:48.470][silabs ]COM: CMD: 0xE2, SN: 0x0032, LEN: 248
[17:33:05.703]  
[17:33:05.703]  [00:00:48.470][silabs ]SPP: ack_timeout_ms 500
[17:33:06.045]  [00:00:48.818][silabs ]MATTER RX: 55 AA 01 00 36 E2 01 F0 09 
[17:33:06.045]  [00:00:48.819][silabs ]payload: F0 
[17:33:06.045]  [00:00:48.819][silabs ]COM: OTAData request without offset, using state offset=12960
[17:33:06.046]  [00:00:48.819][silabs ]COM: spp_app_event_OTAData, req_offset=12960, read_len=240
[17:33:06.147]  [00:00:48.919][silabs ]MATTER TX: 55 AA 01 00 33 E2 F0 25 4A 03 92 00 21 02 91 11 70 00 F0 D9 FB 01 98 02 F0 E4 FD 02 98 03 99 28 22 
[17:33:06.150]  [00:00:48.919][silabs ]COM: CMD: 0xE2, SN: 0x0033, LEN: 248
[17:33:06.150]  
[17:33:06.150]  [00:00:48.919][silabs ]SPP: ack_timeout_ms 500
[17:33:06.495]  [00:00:49.268][silabs ]MATTER RX: 55 AA 01 00 37 E2 01 F0 0A 
[17:33:06.495]  [00:00:49.268][silabs ]payload: F0 
[17:33:06.495]  [00:00:49.268][silabs ]COM: OTAData request without offset, using state offset=13200
[17:33:06.498]  [00:00:49.268][silabs ]COM: spp_app_event_OTAData, req_offset=13200, read_len=240
[17:33:06.597]  [00:00:49.370][silabs ]MATTER TX: 55 AA 01 00 34 E2 F0 51 49 40 20 08 70 FF E7 02 A8 00 78 03 28 07 D1 FF E7 10 49 01 20 08 70 4B 49 
[17:33:06.603]  [00:00:49.370][silabs ]COM: CMD: 0xE2, SN: 0x0034, LEN: 248
[17:33:06.603]  
[17:33:06.603]  [00:00:49.370][silabs ]SPP: ack_timeout_ms 500
[17:33:06.944]  [00:00:49.717][silabs ]MATTER RX: 55 AA 01 00 38 E2 01 F0 0B 
[17:33:06.944]  [00:00:49.717][silabs ]payload: F0 
[17:33:06.944]  [00:00:49.717][silabs ]COM: OTAData request without offset, using state offset=13440
[17:33:06.948]  [00:00:49.717][silabs ]COM: spp_app_event_OTAData, req_offset=13440, read_len=240
[17:33:07.045]  [00:00:49.818][silabs ]MATTER TX: 55 AA 01 00 35 E2 F0 FF E7 16 48 00 78 40 07 81 0F 68 46 01 70 00 78 00 28 05 D1 FF E7 00 98 40 1C 
[17:33:07.048]  [00:00:49.818][silabs ]COM: CMD: 0xE2, SN: 0x0035, LEN: 248
[17:33:07.048]  
[17:33:07.048]  [00:00:49.818][silabs ]SPP: ack_timeout_ms 500
[17:33:07.393]  [00:00:50.166][silabs ]MATTER RX: 55 AA 01 00 39 E2 01 F0 0C 
[17:33:07.393]  [00:00:50.167][silabs ]payload: F0 
[17:33:07.393]  [00:00:50.167][silabs ]COM: OTAData request without offset, using state offset=13680
[17:33:07.395]  [00:00:50.167][silabs ]COM: spp_app_event_OTAData, req_offset=13680, read_len=240
[17:33:07.495]  [00:00:50.268][silabs ]MATTER TX: 55 AA 01 00 36 E2 F0 35 4F 00 00 35 4F 00 00 ED 4E 00 00 20 48 02 90 23 E0 1E 48 02 90 20 E0 1B 48 
[17:33:07.498]  [00:00:50.268][silabs ]COM: CMD: 0xE2, SN: 0x0036, LEN: 248
[17:33:07.498]  
[17:33:07.498]  [00:00:50.268][silabs ]SPP: ack_timeout_ms 500
[17:33:07.843]  [00:00:50.617][silabs ]MATTER RX: 55 AA 01 00 3A E2 01 F0 0D 
[17:33:07.843]  [00:00:50.617][silabs ]payload: F0 
[17:33:07.843]  [00:00:50.617][silabs ]COM: OTAData request without offset, using state offset=13920
[17:33:07.845]  [00:00:50.617][silabs ]COM: spp_app_event_OTAData, req_offset=13920, read_len=240
[17:33:07.945]  [00:00:50.717][silabs ]MATTER TX: 55 AA 01 00 37 E2 F0 1B 48 80 8D 00 28 05 D0 FF E7 19 49 28 22 01 20 88 54 1A E0 16 48 40 8D 00 28 
[17:33:07.949]  [00:00:50.717][silabs ]COM: CMD: 0xE2, SN: 0x0037, LEN: 248
[17:33:07.949]  
[17:33:07.949]  [00:00:50.717][silabs ]SPP: ack_timeout_ms 500
[17:33:08.293]  [00:00:51.066][silabs ]MATTER RX: 55 AA 01 00 3B E2 01 F0 0E 
[17:33:08.293]  [00:00:51.066][silabs ]payload: F0 
[17:33:08.293]  [00:00:51.066][silabs ]COM: OTAData request without offset, using state offset=14160
[17:33:08.295]  [00:00:51.066][silabs ]COM: spp_app_event_OTAData, req_offset=14160, read_len=240
[17:33:08.395]  [00:00:51.167][silabs ]MATTER TX: 55 AA 01 00 38 E2 F0 01 F0 E6 FD 01 A8 00 90 80 78 01 F0 E1 FD 00 98 40 78 01 F0 DD FD 00 98 00 78 
[17:33:08.399]  [00:00:51.167][silabs ]COM: CMD: 0xE2, SN: 0x0038, LEN: 248
[17:33:08.399]  
[17:33:08.399]  [00:00:51.167][silabs ]SPP: ack_timeout_ms 500
[17:33:08.743]  [00:00:51.515][silabs ]MATTER RX: 55 AA 01 00 3C E2 01 F0 0F 
[17:33:08.743]  [00:00:51.515][silabs ]payload: F0 
[17:33:08.743]  [00:00:51.516][silabs ]COM: OTAData request without offset, using state offset=14400
[17:33:08.744]  [00:00:51.516][silabs ]COM: spp_app_event_OTAData, req_offset=14400, read_len=240
[17:33:08.844]  [00:00:51.617][silabs ]MATTER TX: 55 AA 01 00 39 E2 F0 06 20 01 F0 6D FD FF E7 03 49 01 20 08 70 FF E7 80 BD C0 46 75 00 04 40 15 00 
[17:33:08.848]  [00:00:51.617][silabs ]COM: CMD: 0xE2, SN: 0x0039, LEN: 248
[17:33:08.848]  
[17:33:08.848]  [00:00:51.617][silabs ]SPP: ack_timeout_ms 500
[17:33:09.192]  [00:00:51.965][silabs ]MATTER RX: 55 AA 01 00 3D E2 01 F0 10 
[17:33:09.192]  [00:00:51.965][silabs ]payload: F0 
[17:33:09.192]  [00:00:51.965][silabs ]COM: OTAData request without offset, using state offset=14640
[17:33:09.193]  [00:00:51.965][silabs ]COM: spp_app_event_OTAData, req_offset=14640, read_len=240
[17:33:09.292]  [00:00:52.066][silabs ]MATTER TX: 55 AA 01 00 3A E2 F0 01 A8 00 78 08 49 41 43 08 48 40 18 00 90 00 98 02 88 24 21 51 43 40 18 C0 88 
[17:33:09.297]  [00:00:52.066][silabs ]COM: CMD: 0xE2, SN: 0x003A, LEN: 248
[17:33:09.297]  
[17:33:09.297]  [00:00:52.066][silabs ]SPP: ack_timeout_ms 500
[17:33:09.642]  [00:00:52.415][silabs ]MATTER RX: 55 AA 01 00 3E E2 01 F0 11 
[17:33:09.642]  [00:00:52.415][silabs ]payload: F0 
[17:33:09.642]  [00:00:52.415][silabs ]COM: OTAData request without offset, using state offset=14880
[17:33:09.643]  [00:00:52.415][silabs ]COM: spp_app_event_OTAData, req_offset=14880, read_len=240
[17:33:09.743]  [00:00:52.516][silabs ]MATTER TX: 55 AA 01 00 3B E2 F0 B8 0A 00 20 70 46 04 21 08 42 02 D0 EF F3 09 80 01 E0 EF F3 08 80 71 46 01 4A 
[17:33:09.748]  [00:00:52.516][silabs ]COM: CMD: 0xE2, SN: 0x003B, LEN: 248
[17:33:09.748]  
[17:33:09.748]  [00:00:52.516][silabs ]SPP: ack_timeout_ms 500
[17:33:10.091]  [00:00:52.864][silabs ]MATTER RX: 55 AA 01 00 3F E2 01 F0 12 
[17:33:10.091]  [00:00:52.864][silabs ]payload: F0 
[17:33:10.091]  [00:00:52.865][silabs ]COM: OTAData request without offset, using state offset=15120
[17:33:10.093]  [00:00:52.865][silabs ]COM: spp_app_event_OTAData, req_offset=15120, read_len=240
[17:33:10.192]  [00:00:52.965][silabs ]MATTER TX: 55 AA 01 00 3C E2 F0 00 78 40 B2 81 00 63 4A 00 20 88 54 01 B0 70 47 81 B0 01 46 68 46 01 70 00 78 
[17:33:10.197]  [00:00:52.965][silabs ]COM: CMD: 0xE2, SN: 0x003C, LEN: 248
[17:33:10.197]  
[17:33:10.197]  [00:00:52.965][silabs ]SPP: ack_timeout_ms 500
[17:33:10.541]  [00:00:53.314][silabs ]MATTER RX: 55 AA 01 00 40 E2 01 F0 13 
[17:33:10.541]  [00:00:53.314][silabs ]payload: F0 
[17:33:10.541]  [00:00:53.314][silabs ]COM: OTAData request without offset, using state offset=15360
[17:33:10.544]  [00:00:53.314][silabs ]COM: spp_app_event_OTAData, req_offset=15360, read_len=240
[17:33:10.642]  [00:00:53.416][silabs ]MATTER TX: 55 AA 01 00 3D E2 F0 00 78 40 B2 81 00 20 4A 01 20 88 54 01 B0 70 47 81 B0 01 46 68 46 01 70 00 78 
[17:33:10.647]  [00:00:53.416][silabs ]COM: CMD: 0xE2, SN: 0x003D, LEN: 248
[17:33:10.647]  
[17:33:10.647]  [00:00:53.416][silabs ]SPP: ack_timeout_ms 500
[17:33:10.990]  [00:00:53.763][silabs ]MATTER RX: 55 AA 01 00 41 E2 01 F0 14 
[17:33:10.990]  [00:00:53.763][silabs ]payload: F0 
[17:33:10.990]  [00:00:53.763][silabs ]COM: OTAData request without offset, using state offset=15600
[17:33:10.992]  [00:00:53.763][silabs ]COM: spp_app_event_OTAData, req_offset=15600, read_len=240
[17:33:11.091]  [00:00:53.865][silabs ]MATTER TX: 55 AA 01 00 3E E2 F0 02 22 10 40 42 08 08 78 10 43 08 70 FF E7 07 A8 00 88 80 07 00 28 1E D5 FF E7 
[17:33:11.098]  [00:00:53.865][silabs ]COM: CMD: 0xE2, SN: 0x003E, LEN: 248
[17:33:11.098]  
[17:33:11.098]  [00:00:53.865][silabs ]SPP: ack_timeout_ms 500
[17:33:11.440]  [00:00:54.212][silabs ]MATTER RX: 55 AA 01 00 42 E2 01 F0 15 
[17:33:11.440]  [00:00:54.212][silabs ]payload: F0 
[17:33:11.440]  [00:00:54.213][silabs ]COM: OTAData request without offset, using state offset=15840
[17:33:11.443]  [00:00:54.213][silabs ]COM: spp_app_event_OTAData, req_offset=15840, read_len=240
[17:33:11.541]  [00:00:54.314][silabs ]MATTER TX: 55 AA 01 00 3F E2 F0 FF E7 05 A8 00 78 01 28 07 D8 FF E7 00 BF FF E7 05 98 40 1C 05 A9 08 70 F3 E7 
[17:33:11.544]  [00:00:54.314][silabs ]COM: CMD: 0xE2, SN: 0x003F, LEN: 248
[17:33:11.544]  
[17:33:11.544]  [00:00:54.314][silabs ]SPP: ack_timeout_ms 500
[17:33:11.889]  [00:00:54.663][silabs ]MATTER RX: 55 AA 01 00 43 E2 01 F0 16 
[17:33:11.889]  [00:00:54.663][silabs ]payload: F0 
[17:33:11.889]  [00:00:54.663][silabs ]COM: OTAData request without offset, using state offset=16080
[17:33:11.893]  [00:00:54.663][silabs ]COM: spp_app_event_OTAData, req_offset=16080, read_len=240
[17:33:11.991]  [00:00:54.763][silabs ]MATTER TX: 55 AA 01 00 40 E2 F0 03 20 02 90 FF F7 9C FE 02 98 FF F7 FD FD FF E7 05 A8 00 88 00 07 00 28 08 D5 
[17:33:11.994]  [00:00:54.763][silabs ]COM: CMD: 0xE2, SN: 0x0040, LEN: 248
[17:33:11.994]  
[17:33:11.994]  [00:00:54.763][silabs ]SPP: ack_timeout_ms 500
[17:33:12.339]  [00:00:55.112][silabs ]MATTER RX: 55 AA 01 00 44 E2 01 F0 17 
[17:33:12.339]  [00:00:55.112][silabs ]payload: F0 
[17:33:12.339]  [00:00:55.112][silabs ]COM: OTAData request without offset, using state offset=16320
[17:33:12.340]  [00:00:55.113][silabs ]COM: spp_app_event_OTAData, req_offset=16320, read_len=240
[17:33:12.440]  [00:00:55.213][silabs ]MATTER TX: 55 AA 01 00 41 E2 F0 FF E7 00 20 03 F0 90 FE 01 20 04 21 E9 4A 03 F0 DD FD FF E7 09 E0 FF E7 00 20 
[17:33:12.444]  [00:00:55.213][silabs ]COM: CMD: 0xE2, SN: 0x0041, LEN: 248
[17:33:12.444]  
[17:33:12.444]  [00:00:55.213][silabs ]SPP: ack_timeout_ms 500
[17:33:12.788]  [00:00:55.561][silabs ]MATTER RX: 55 AA 01 00 45 E2 01 F0 18 
[17:33:12.788]  [00:00:55.562][silabs ]payload: F0 
[17:33:12.788]  [00:00:55.562][silabs ]COM: OTAData request without offset, using state offset=16560
[17:33:12.789]  [00:00:55.562][silabs ]COM: spp_app_event_OTAData, req_offset=16560, read_len=240
[17:33:12.890]  [00:00:55.663][silabs ]MATTER TX: 55 AA 01 00 42 E2 F0 03 20 00 90 01 20 FA 22 11 46 03 F0 A5 FD FF E7 04 20 02 F0 93 FC 04 48 12 21 
[17:33:12.893]  [00:00:55.663][silabs ]COM: CMD: 0xE2, SN: 0x0042, LEN: 248
[17:33:12.893]  
[17:33:12.893]  [00:00:55.663][silabs ]SPP: ack_timeout_ms 500
[17:33:13.238]  [00:00:56.011][silabs ]MATTER RX: 55 AA 01 00 46 E2 01 F0 19 
[17:33:13.238]  [00:00:56.011][silabs ]payload: F0 
[17:33:13.238]  [00:00:56.011][silabs ]COM: OTAData request without offset, using state offset=16800
[17:33:13.239]  [00:00:56.011][silabs ]COM: spp_app_event_OTAData, req_offset=16800, read_len=240
[17:33:13.339]  [00:00:56.112][silabs ]MATTER TX: 55 AA 01 00 43 E2 F0 06 20 00 90 01 20 FA 22 11 46 03 F0 2D FD FF E7 01 20 05 F0 B1 FB 04 48 12 21 
[17:33:13.342]  [00:00:56.112][silabs ]COM: CMD: 0xE2, SN: 0x0043, LEN: 248
[17:33:13.342]  
[17:33:13.342]  [00:00:56.112][silabs ]SPP: ack_timeout_ms 500
[17:33:13.687]  [00:00:56.460][silabs ]MATTER RX: 55 AA 01 00 47 E2 01 F0 1A 
[17:33:13.687]  [00:00:56.460][silabs ]payload: F0 
[17:33:13.687]  [00:00:56.460][silabs ]COM: OTAData request without offset, using state offset=17040
[17:33:13.689]  [00:00:56.461][silabs ]COM: spp_app_event_OTAData, req_offset=17040, read_len=240
[17:33:13.789]  [00:00:56.562][silabs ]MATTER TX: 55 AA 01 00 44 E2 F0 7D 20 C0 00 1C 21 00 23 1A 46 01 F0 D3 F9 04 B0 80 BD C0 46 18 14 00 20 81 B0 
[17:33:13.793]  [00:00:56.562][silabs ]COM: CMD: 0xE2, SN: 0x0044, LEN: 248
[17:33:13.793]  
[17:33:13.793]  [00:00:56.562][silabs ]SPP: ack_timeout_ms 500
[17:33:14.138]  [00:00:56.910][silabs ]MATTER RX: 55 AA 01 00 48 E2 01 F0 1B 
[17:33:14.138]  [00:00:56.911][silabs ]payload: F0 
[17:33:14.138]  [00:00:56.911][silabs ]COM: OTAData request without offset, using state offset=17280
[17:33:14.139]  [00:00:56.911][silabs ]COM: spp_app_event_OTAData, req_offset=17280, read_len=240
[17:33:14.238]  [00:00:57.011][silabs ]MATTER TX: 55 AA 01 00 45 E2 F0 80 BD 00 00 80 B5 82 B0 01 90 03 48 E6 49 00 F0 1F FB 02 B0 80 BD C0 46 E4 CE 
[17:33:14.242]  [00:00:57.011][silabs ]COM: CMD: 0xE2, SN: 0x0045, LEN: 248
[17:33:14.242]  
[17:33:14.242]  [00:00:57.011][silabs ]SPP: ack_timeout_ms 500
[17:33:14.586]  [00:00:57.360][silabs ]MATTER RX: 55 AA 01 00 49 E2 01 F0 1C 
[17:33:14.586]  [00:00:57.360][silabs ]payload: F0 
[17:33:14.586]  [00:00:57.360][silabs ]COM: OTAData request without offset, using state offset=17520
[17:33:14.588]  [00:00:57.360][silabs ]COM: spp_app_event_OTAData, req_offset=17520, read_len=240
[17:33:14.688]  [00:00:57.461][silabs ]MATTER TX: 55 AA 01 00 46 E2 F0 08 81 C8 80 88 80 48 80 08 80 FF E7 01 20 03 F0 33 FC 00 20 08 21 03 F0 53 FC 
[17:33:14.692]  [00:00:57.461][silabs ]COM: CMD: 0xE2, SN: 0x0046, LEN: 248
[17:33:14.692]  
[17:33:14.692]  [00:00:57.461][silabs ]SPP: ack_timeout_ms 500
[17:33:15.036]  [00:00:57.809][silabs ]MATTER RX: 55 AA 01 00 4A E2 01 F0 1D 
[17:33:15.036]  [00:00:57.810][silabs ]payload: F0 
[17:33:15.036]  [00:00:57.810][silabs ]COM: OTAData request without offset, using state offset=17760
[17:33:15.037]  [00:00:57.810][silabs ]COM: spp_app_event_OTAData, req_offset=17760, read_len=240
[17:33:15.137]  [00:00:57.911][silabs ]MATTER TX: 55 AA 01 00 47 E2 F0 01 20 02 F0 85 FB FF E7 FF E7 FF E7 04 B0 80 BD 18 14 00 20 10 27 00 00 80 B5 
[17:33:15.142]  [00:00:57.911][silabs ]COM: CMD: 0xE2, SN: 0x0047, LEN: 248
[17:33:15.142]  
[17:33:15.142]  [00:00:57.911][silabs ]SPP: ack_timeout_ms 500
[17:33:15.486]  [00:00:58.259][silabs ]MATTER RX: 55 AA 01 00 4B E2 01 F0 1E 
[17:33:15.486]  [00:00:58.259][silabs ]payload: F0 
[17:33:15.486]  [00:00:58.259][silabs ]COM: OTAData request without offset, using state offset=18000
[17:33:15.487]  [00:00:58.259][silabs ]COM: spp_app_event_OTAData, req_offset=18000, read_len=240
[17:33:15.587]  [00:00:58.360][silabs ]MATTER TX: 55 AA 01 00 48 E2 F0 01 90 D8 48 00 21 C1 70 80 79 07 28 1B D1 FF E7 D4 48 00 79 63 28 0B DC FF E7 
[17:33:15.592]  [00:00:58.360][silabs ]COM: CMD: 0xE2, SN: 0x0048, LEN: 248
[17:33:15.592]  
[17:33:15.592]  [00:00:58.360][silabs ]SPP: ack_timeout_ms 500
[17:33:15.935]  [00:00:58.708][silabs ]MATTER RX: 55 AA 01 00 4C E2 01 F0 1F 
[17:33:15.935]  [00:00:58.708][silabs ]payload: F0 
[17:33:15.935]  [00:00:58.709][silabs ]COM: OTAData request without offset, using state offset=18240
[17:33:15.939]  [00:00:58.709][silabs ]COM: spp_app_event_OTAData, req_offset=18240, read_len=240
[17:33:16.036]  [00:00:58.810][silabs ]MATTER TX: 55 AA 01 00 49 E2 F0 00 F0 46 F9 80 BD C0 46 24 14 00 20 2C 14 00 20 48 CF 00 00 80 B5 82 B0 01 90 
[17:33:16.042]  [00:00:58.810][silabs ]COM: CMD: 0xE2, SN: 0x0049, LEN: 248
[17:33:16.042]  
[17:33:16.042]  [00:00:58.810][silabs ]SPP: ack_timeout_ms 500
[17:33:16.385]  [00:00:59.159][silabs ]MATTER RX: 55 AA 01 00 4D E2 01 F0 20 
[17:33:16.385]  [00:00:59.159][silabs ]payload: F0 
[17:33:16.385]  [00:00:59.159][silabs ]COM: OTAData request without offset, using state offset=18480
[17:33:16.389]  [00:00:59.159][silabs ]COM: spp_app_event_OTAData, req_offset=18480, read_len=240
[17:33:16.486]  [00:00:59.259][silabs ]MATTER TX: 55 AA 01 00 4A E2 F0 02 21 00 23 05 F0 B4 FA 02 B0 80 BD 18 14 00 20 80 B5 82 B0 01 90 01 98 40 68 
[17:33:16.490]  [00:00:59.259][silabs ]COM: CMD: 0xE2, SN: 0x004A, LEN: 248
[17:33:16.490]  
[17:33:16.490]  [00:00:59.259][silabs ]SPP: ack_timeout_ms 500
[17:33:16.835]  [00:00:59.608][silabs ]MATTER RX: 55 AA 01 00 4E E2 01 F0 21 
[17:33:16.835]  [00:00:59.608][silabs ]payload: F0 
[17:33:16.835]  [00:00:59.608][silabs ]COM: OTAData request without offset, using state offset=18720
[17:33:16.838]  [00:00:59.609][silabs ]COM: spp_app_event_OTAData, req_offset=18720, read_len=240
[17:33:16.936]  [00:00:59.709][silabs ]MATTER TX: 55 AA 01 00 4B E2 F0 A9 62 00 00 B7 62 00 00 C5 62 00 00 D3 62 00 00 E1 62 00 00 EF 62 00 00 01 20 
[17:33:16.942]  [00:00:59.709][silabs ]COM: CMD: 0xE2, SN: 0x004B, LEN: 248
[17:33:16.942]  
[17:33:16.942]  [00:00:59.709][silabs ]SPP: ack_timeout_ms 500
[17:33:17.284]  [00:01:00.057][silabs ]MATTER RX: 55 AA 01 00 4F E2 01 F0 22 
[17:33:17.284]  [00:01:00.058][silabs ]payload: F0 
[17:33:17.284]  [00:01:00.058][silabs ]COM: OTAData request without offset, using state offset=18960
[17:33:17.288]  [00:01:00.058][silabs ]COM: spp_app_event_OTAData, req_offset=18960, read_len=240
[17:33:17.386]  [00:01:00.160][silabs ]MATTER TX: 55 AA 01 00 4C E2 F0 0C D0 FF E7 14 48 00 68 80 68 00 28 05 D0 FF E7 11 48 00 68 80 68 80 47 FF E7 
[17:33:17.391]  [00:01:00.160][silabs ]COM: CMD: 0xE2, SN: 0x004C, LEN: 248
[17:33:17.391]  
[17:33:17.391]  [00:01:00.160][silabs ]SPP: ack_timeout_ms 500
[17:33:17.734]  [00:01:00.507][silabs ]MATTER RX: 55 AA 01 00 50 E2 01 F0 23 
[17:33:17.734]  [00:01:00.507][silabs ]payload: F0 
[17:33:17.734]  [00:01:00.507][silabs ]COM: OTAData request without offset, using state offset=19200
[17:33:17.738]  [00:01:00.507][silabs ]COM: spp_app_event_OTAData, req_offset=19200, read_len=240
[17:33:17.835]  [00:01:00.608][silabs ]MATTER TX: 55 AA 01 00 4D E2 F0 2A 49 88 69 09 6A 88 42 0E DB FF E7 27 49 02 91 88 69 08 62 08 6A 32 38 08 62 
[17:33:17.838]  [00:01:00.608][silabs ]COM: CMD: 0xE2, SN: 0x004D, LEN: 248
[17:33:17.838]  
[17:33:17.838]  [00:01:00.608][silabs ]SPP: ack_timeout_ms 500
[17:33:18.184]  [00:01:00.957][silabs ]MATTER RX: 55 AA 01 00 51 E2 01 F0 24 
[17:33:18.184]  [00:01:00.958][silabs ]payload: F0 
[17:33:18.184]  [00:01:00.958][silabs ]COM: OTAData request without offset, using state offset=19440
[17:33:18.185]  [00:01:00.958][silabs ]COM: spp_app_event_OTAData, req_offset=19440, read_len=240
[17:33:18.285]  [00:01:01.058][silabs ]MATTER TX: 55 AA 01 00 4E E2 F0 86 B0 05 90 04 A8 01 70 BD 49 49 69 03 91 03 99 09 09 02 91 05 99 09 01 00 78 
[17:33:18.288]  [00:01:01.058][silabs ]COM: CMD: 0xE2, SN: 0x004E, LEN: 248
[17:33:18.288]  
[17:33:18.288]  [00:01:01.058][silabs ]SPP: ack_timeout_ms 500
[17:33:18.633]  [00:01:01.407][silabs ]MATTER RX: 55 AA 01 00 52 E2 01 F0 25 
[17:33:18.633]  [00:01:01.407][silabs ]payload: F0 
[17:33:18.633]  [00:01:01.407][silabs ]COM: OTAData request without offset, using state offset=19680
[17:33:18.635]  [00:01:01.407][silabs ]COM: spp_app_event_OTAData, req_offset=19680, read_len=240
[17:33:18.733]  [00:01:01.507][silabs ]MATTER TX: 55 AA 01 00 4F E2 F0 D1 E0 05 99 83 48 81 62 18 30 7D 21 89 00 03 F0 D3 FB 07 A8 00 78 00 28 0A D1 
[17:33:18.738]  [00:01:01.507][silabs ]COM: CMD: 0xE2, SN: 0x004F, LEN: 248
[17:33:18.738]  
[17:33:18.738]  [00:01:01.507][silabs ]SPP: ack_timeout_ms 500
[17:33:19.082]  [00:01:01.856][silabs ]MATTER RX: 55 AA 01 00 53 E2 01 F0 26 
[17:33:19.082]  [00:01:01.856][silabs ]payload: F0 
[17:33:19.082]  [00:01:01.856][silabs ]COM: OTAData request without offset, using state offset=19920
[17:33:19.084]  [00:01:01.857][silabs ]COM: spp_app_event_OTAData, req_offset=19920, read_len=240
[17:33:19.184]  [00:01:01.958][silabs ]MATTER TX: 55 AA 01 00 50 E2 F0 08 70 04 98 FF 21 FE 31 88 42 09 D3 FF E7 04 98 2A 49 88 42 04 D8 FF E7 03 A9 
[17:33:19.187]  [00:01:01.958][silabs ]COM: CMD: 0xE2, SN: 0x0050, LEN: 248
[17:33:19.187]  
[17:33:19.187]  [00:01:01.958][silabs ]SPP: ack_timeout_ms 500
[17:33:19.532]  [00:01:02.305][silabs ]MATTER RX: 55 AA 01 00 54 E2 01 F0 27 
[17:33:19.532]  [00:01:02.306][silabs ]payload: F0 
[17:33:19.532]  [00:01:02.306][silabs ]COM: OTAData request without offset, using state offset=20160
[17:33:19.533]  [00:01:02.306][silabs ]COM: spp_app_event_OTAData, req_offset=20160, read_len=240
[17:33:19.634]  [00:01:02.408][silabs ]MATTER TX: 55 AA 01 00 51 E2 F0 13 D0 FF E7 01 98 0A 49 48 61 00 20 00 90 18 22 04 F0 F2 FA 00 9B 35 21 18 46 
[17:33:19.638]  [00:01:02.408][silabs ]COM: CMD: 0xE2, SN: 0x0051, LEN: 248
[17:33:19.638]  
[17:33:19.638]  [00:01:02.408][silabs ]SPP: ack_timeout_ms 500
[17:33:19.982]  [00:01:02.755][silabs ]MATTER RX: 55 AA 01 00 55 E2 01 F0 28 
[17:33:19.982]  [00:01:02.755][silabs ]payload: F0 
[17:33:19.982]  [00:01:02.755][silabs ]COM: OTAData request without offset, using state offset=20400
[17:33:19.984]  [00:01:02.755][silabs ]COM: spp_app_event_OTAData, req_offset=20400, read_len=240
[17:33:20.083]  [00:01:02.856][silabs ]MATTER TX: 55 AA 01 00 52 E2 F0 02 9C 06 A8 02 78 57 4B D1 5C A1 43 D1 54 02 9C 02 78 55 4B D1 5C 21 43 D1 54 
[17:33:20.087]  [00:01:02.856][silabs ]COM: CMD: 0xE2, SN: 0x0052, LEN: 248
[17:33:20.087]  
[17:33:20.087]  [00:01:02.856][silabs ]SPP: ack_timeout_ms 500
[17:33:20.432]  [00:01:03.205][silabs ]MATTER RX: 55 AA 01 00 56 E2 01 F0 29 
[17:33:20.432]  [00:01:03.205][silabs ]payload: F0 
[17:33:20.432]  [00:01:03.206][silabs ]COM: OTAData request without offset, using state offset=20640
[17:33:20.433]  [00:01:03.206][silabs ]COM: spp_app_event_OTAData, req_offset=20640, read_len=240
[17:33:20.533]  [00:01:03.306][silabs ]MATTER TX: 55 AA 01 00 53 E2 F0 88 5C 98 43 88 54 33 E0 02 9C 06 A8 02 78 19 4B D1 5C A1 43 D1 54 02 9C 02 78 
[17:33:20.537]  [00:01:03.306][silabs ]COM: CMD: 0xE2, SN: 0x0053, LEN: 248
[17:33:20.537]  
[17:33:20.537]  [00:01:03.306][silabs ]SPP: ack_timeout_ms 500
[17:33:20.880]  [00:01:03.655][silabs ]MATTER RX: 55 AA 01 00 57 E2 01 F0 2A 
[17:33:20.880]  [00:01:03.655][silabs ]payload: F0 
[17:33:20.880]  [00:01:03.655][silabs ]COM: OTAData request without offset, using state offset=20880
[17:33:20.882]  [00:01:03.655][silabs ]COM: spp_app_event_OTAData, req_offset=20880, read_len=240
[17:33:20.982]  [00:01:03.755][silabs ]MATTER TX: 55 AA 01 00 54 E2 F0 1C 48 40 18 00 90 00 98 80 88 00 28 04 D0 FF E7 02 A9 01 20 08 70 03 E0 02 A9 
[17:33:20.987]  [00:01:03.755][silabs ]COM: CMD: 0xE2, SN: 0x0054, LEN: 248
[17:33:20.987]  
[17:33:20.987]  [00:01:03.755][silabs ]SPP: ack_timeout_ms 500
[17:33:21.331]  [00:01:04.104][silabs ]MATTER RX: 55 AA 01 00 58 E2 01 F0 2B 
[17:33:21.331]  [00:01:04.104][silabs ]payload: F0 
[17:33:21.331]  [00:01:04.104][silabs ]COM: OTAData request without offset, using state offset=21120
[17:33:21.332]  [00:01:04.105][silabs ]COM: spp_app_event_OTAData, req_offset=21120, read_len=240
[17:33:21.432]  [00:01:04.206][silabs ]MATTER TX: 55 AA 01 00 55 E2 F0 25 6C 00 00 31 6C 00 00 3D 6C 00 00 4B 6C 00 00 03 99 FF 20 08 70 29 E0 02 99 
[17:33:21.437]  [00:01:04.206][silabs ]COM: CMD: 0xE2, SN: 0x0055, LEN: 248
[17:33:21.437]  
[17:33:21.437]  [00:01:04.206][silabs ]SPP: ack_timeout_ms 500
[17:33:21.780]  [00:01:04.553][silabs ]MATTER RX: 55 AA 01 00 59 E2 01 F0 2C 
[17:33:21.780]  [00:01:04.554][silabs ]payload: F0 
[17:33:21.780]  [00:01:04.554][silabs ]COM: OTAData request without offset, using state offset=21360
[17:33:21.784]  [00:01:04.554][silabs ]COM: spp_app_event_OTAData, req_offset=21360, read_len=240
[17:33:21.882]  [00:01:04.656][silabs ]MATTER TX: 55 AA 01 00 56 E2 F0 10 60 10 68 84 23 18 43 10 60 60 4A 10 68 08 23 18 43 10 60 22 4A 0C 20 10 70 
[17:33:21.886]  [00:01:04.656][silabs ]COM: CMD: 0xE2, SN: 0x0056, LEN: 248
[17:33:21.886]  
[17:33:21.886]  [00:01:04.656][silabs ]SPP: ack_timeout_ms 500
[17:33:22.229]  [00:01:05.003][silabs ]MATTER RX: 55 AA 01 00 5A E2 01 F0 2D 
[17:33:22.229]  [00:01:05.003][silabs ]payload: F0 
[17:33:22.229]  [00:01:05.003][silabs ]COM: OTAData request without offset, using state offset=21600
[17:33:22.230]  [00:01:05.003][silabs ]COM: spp_app_event_OTAData, req_offset=21600, read_len=240
[17:33:22.331]  [00:01:05.104][silabs ]MATTER TX: 55 AA 01 00 57 E2 F0 FF E7 27 49 08 78 01 22 10 43 08 70 25 49 08 78 FE 22 10 40 08 70 24 49 08 78 
[17:33:22.334]  [00:01:05.104][silabs ]COM: CMD: 0xE2, SN: 0x0057, LEN: 248
[17:33:22.334]  
[17:33:22.334]  [00:01:05.104][silabs ]SPP: ack_timeout_ms 500
[17:33:22.679]  [00:01:05.453][silabs ]MATTER RX: 55 AA 01 00 5B E2 01 F0 2E 
[17:33:22.679]  [00:01:05.453][silabs ]payload: F0 
[17:33:22.679]  [00:01:05.453][silabs ]COM: OTAData request without offset, using state offset=21840
[17:33:22.681]  [00:01:05.454][silabs ]COM: spp_app_event_OTAData, req_offset=21840, read_len=240
[17:33:22.781]  [00:01:05.554][silabs ]MATTER TX: 55 AA 01 00 58 E2 F0 01 98 00 F0 CF FC 02 B0 80 BD C0 46 15 00 04 40 00 24 04 40 80 B5 82 B0 17 48 
[17:33:22.784]  [00:01:05.554][silabs ]COM: CMD: 0xE2, SN: 0x0058, LEN: 248
[17:33:22.784]  
[17:33:22.784]  [00:01:05.554][silabs ]SPP: ack_timeout_ms 500
[17:33:23.129]  [00:01:05.902][silabs ]MATTER RX: 55 AA 01 00 5C E2 01 F0 2F 
[17:33:23.129]  [00:01:05.903][silabs ]payload: F0 
[17:33:23.129]  [00:01:05.903][silabs ]COM: OTAData request without offset, using state offset=22080
[17:33:23.133]  [00:01:05.903][silabs ]COM: spp_app_event_OTAData, req_offset=22080, read_len=240
[17:33:23.230]  [00:01:06.003][silabs ]MATTER TX: 55 AA 01 00 59 E2 F0 00 80 45 44 10 B5 88 B0 07 90 06 A8 01 80 05 92 04 93 00 20 02 90 FF E7 FB F7 
[17:33:23.233]  [00:01:06.003][silabs ]COM: CMD: 0xE2, SN: 0x0059, LEN: 248
[17:33:23.233]  
[17:33:23.233]  [00:01:06.003][silabs ]SPP: ack_timeout_ms 500
[17:33:23.578]  [00:01:06.352][silabs ]MATTER RX: 55 AA 01 00 5D E2 01 F0 30 
[17:33:23.578]  [00:01:06.352][silabs ]payload: F0 
[17:33:23.578]  [00:01:06.352][silabs ]COM: OTAData request without offset, using state offset=22320
[17:33:23.581]  [00:01:06.352][silabs ]COM: spp_app_event_OTAData, req_offset=22320, read_len=240
[17:33:23.680]  [00:01:06.454][silabs ]MATTER TX: 55 AA 01 00 5A E2 F0 06 A8 00 88 04 F0 F8 FA FF E7 07 98 35 49 49 68 88 42 04 D2 FF E7 07 98 32 49 
[17:33:23.683]  [00:01:06.454][silabs ]COM: CMD: 0xE2, SN: 0x005A, LEN: 248
[17:33:23.683]  
[17:33:23.683]  [00:01:06.454][silabs ]SPP: ack_timeout_ms 500
[17:33:24.028]  [00:01:06.801][silabs ]MATTER RX: 55 AA 01 00 5E E2 01 F0 31 
[17:33:24.028]  [00:01:06.801][silabs ]payload: F0 
[17:33:24.028]  [00:01:06.802][silabs ]COM: OTAData request without offset, using state offset=22560
[17:33:24.032]  [00:01:06.802][silabs ]COM: spp_app_event_OTAData, req_offset=22560, read_len=240
[17:33:24.128]  [00:01:06.902][silabs ]MATTER TX: 55 AA 01 00 5B E2 F0 38 0E 00 20 80 B5 84 B0 02 90 02 98 40 1E 00 0E 00 28 03 D0 FF E7 01 20 03 90 
[17:33:24.131]  [00:01:06.902][silabs ]COM: CMD: 0xE2, SN: 0x005B, LEN: 248
[17:33:24.131]  
[17:33:24.131]  [00:01:06.902][silabs ]SPP: ack_timeout_ms 500
[17:33:24.477]  [00:01:07.250][silabs ]MATTER RX: 55 AA 01 00 5F E2 01 F0 32 
[17:33:24.477]  [00:01:07.251][silabs ]payload: F0 
[17:33:24.477]  [00:01:07.251][silabs ]COM: OTAData request without offset, using state offset=22800
[17:33:24.478]  [00:01:07.251][silabs ]COM: spp_app_event_OTAData, req_offset=22800, read_len=240
[17:33:24.578]  [00:01:07.352][silabs ]MATTER TX: 55 AA 01 00 5C E2 F0 04 B0 01 40 08 04 02 40 09 04 02 40 0A 04 02 40 0B 04 02 40 B4 0A 00 20 80 E2 
[17:33:24.581]  [00:01:07.352][silabs ]COM: CMD: 0xE2, SN: 0x005C, LEN: 248
[17:33:24.581]  
[17:33:24.581]  [00:01:07.352][silabs ]SPP: ack_timeout_ms 500
[17:33:24.927]  [00:01:07.701][silabs ]MATTER RX: 55 AA 01 00 60 E2 01 F0 33 
[17:33:24.927]  [00:01:07.701][silabs ]payload: F0 
[17:33:24.927]  [00:01:07.701][silabs ]COM: OTAData request without offset, using state offset=23040
[17:33:24.928]  [00:01:07.701][silabs ]COM: spp_app_event_OTAData, req_offset=23040, read_len=240
[17:33:25.028]  [00:01:07.802][silabs ]MATTER TX: 55 AA 01 00 5D E2 F0 08 78 10 40 08 70 42 49 08 78 10 40 08 70 FF E7 40 49 37 48 08 80 01 98 3F 49 
[17:33:25.032]  [00:01:07.802][silabs ]COM: CMD: 0xE2, SN: 0x005D, LEN: 248
[17:33:25.032]  
[17:33:25.032]  [00:01:07.802][silabs ]SPP: ack_timeout_ms 500
[17:33:25.376]  [00:01:08.150][silabs ]MATTER RX: 55 AA 01 00 61 E2 01 F0 34 
[17:33:25.376]  [00:01:08.150][silabs ]payload: F0 
[17:33:25.376]  [00:01:08.151][silabs ]COM: OTAData request without offset, using state offset=23280
[17:33:25.377]  [00:01:08.151][silabs ]COM: spp_app_event_OTAData, req_offset=23280, read_len=240
[17:33:25.478]  [00:01:08.251][silabs ]MATTER TX: 55 AA 01 00 5E E2 F0 09 84 00 00 12 23 04 40 BE 21 04 40 BC 21 04 40 57 08 04 40 0E 00 04 40 2E 00 
[17:33:25.481]  [00:01:08.251][silabs ]COM: CMD: 0xE2, SN: 0x005E, LEN: 248
[17:33:25.481]  
[17:33:25.481]  [00:01:08.251][silabs ]SPP: ack_timeout_ms 500
[17:33:25.826]  [00:01:08.600][silabs ]MATTER RX: 55 AA 01 00 62 E2 01 F0 35 
[17:33:25.826]  [00:01:08.600][silabs ]payload: F0 
[17:33:25.826]  [00:01:08.600][silabs ]COM: OTAData request without offset, using state offset=23520
[17:33:25.827]  [00:01:08.600][silabs ]COM: spp_app_event_OTAData, req_offset=23520, read_len=240
[17:33:25.928]  [00:01:08.702][silabs ]MATTER TX: 55 AA 01 00 5F E2 F0 23 F8 02 98 FE F7 20 F8 09 20 03 90 FE F7 1C F8 04 98 FD F7 A1 FF 02 98 FD F7 
[17:33:25.933]  [00:01:08.702][silabs ]COM: CMD: 0xE2, SN: 0x005F, LEN: 248
[17:33:25.933]  
[17:33:25.933]  [00:01:08.702][silabs ]SPP: ack_timeout_ms 500
[17:33:26.276]  [00:01:09.049][silabs ]MATTER RX: 55 AA 01 00 63 E2 01 F0 36 
[17:33:26.276]  [00:01:09.049][silabs ]payload: F0 
[17:33:26.276]  [00:01:09.049][silabs ]COM: OTAData request without offset, using state offset=23760
[17:33:26.277]  [00:01:09.049][silabs ]COM: spp_app_event_OTAData, req_offset=23760, read_len=240
[17:33:26.376]  [00:01:09.150][silabs ]MATTER TX: 55 AA 01 00 60 E2 F0 4A 15 04 40 52 15 04 40 5A 15 04 40 97 40 00 00 4A 17 04 40 74 15 04 40 08 08 
[17:33:26.381]  [00:01:09.150][silabs ]COM: CMD: 0xE2, SN: 0x0060, LEN: 248
[17:33:26.381]  
[17:33:26.381]  [00:01:09.150][silabs ]SPP: ack_timeout_ms 500
[17:33:26.725]  [00:01:09.499][silabs ]MATTER RX: 55 AA 01 00 64 E2 01 F0 37 
[17:33:26.725]  [00:01:09.500][silabs ]payload: F0 
[17:33:26.725]  [00:01:09.500][silabs ]COM: OTAData request without offset, using state offset=24000
[17:33:26.726]  [00:01:09.500][silabs ]COM: spp_app_event_OTAData, req_offset=24000, read_len=240
[17:33:26.826]  [00:01:09.600][silabs ]MATTER TX: 55 AA 01 00 61 E2 F0 08 70 FF E7 01 A8 00 78 0F 28 42 DC FF E7 08 98 01 A9 09 78 4A 00 23 49 89 5A 
[17:33:26.831]  [00:01:09.600][silabs ]COM: CMD: 0xE2, SN: 0x0061, LEN: 248
[17:33:26.831]  
[17:33:26.831]  [00:01:09.600][silabs ]SPP: ack_timeout_ms 500
[17:33:27.175]  [00:01:09.949][silabs ]MATTER RX: 55 AA 01 00 65 E2 01 F0 38 
[17:33:27.175]  [00:01:09.949][silabs ]payload: F0 
[17:33:27.175]  [00:01:09.949][silabs ]COM: OTAData request without offset, using state offset=24240
[17:33:27.179]  [00:01:09.949][silabs ]COM: spp_app_event_OTAData, req_offset=24240, read_len=240
[17:33:27.276]  [00:01:10.049][silabs ]MATTER TX: 55 AA 01 00 62 E2 F0 00 28 09 D4 FF E7 68 46 01 78 1F 20 01 40 01 20 88 40 16 49 08 60 FF E7 01 B0 
[17:33:27.282]  [00:01:10.049][silabs ]COM: CMD: 0xE2, SN: 0x0062, LEN: 248
[17:33:27.282]  
[17:33:27.282]  [00:01:10.049][silabs ]SPP: ack_timeout_ms 500
[17:33:27.624]  [00:01:10.398][silabs ]MATTER RX: 55 AA 01 00 66 E2 01 F0 39 
[17:33:27.624]  [00:01:10.398][silabs ]payload: F0 
[17:33:27.624]  [00:01:10.398][silabs ]COM: OTAData request without offset, using state offset=24480
[17:33:27.628]  [00:01:10.399][silabs ]COM: spp_app_event_OTAData, req_offset=24480, read_len=240
[17:33:27.725]  [00:01:10.500][silabs ]MATTER TX: 55 AA 01 00 63 E2 F0 08 38 03 22 D3 43 18 40 0A 4A 80 58 09 78 49 B2 8D 07 EE 0E FF 25 B5 40 A8 43 
[17:33:27.732]  [00:01:10.500][silabs ]COM: CMD: 0xE2, SN: 0x0063, LEN: 248
[17:33:27.732]  
[17:33:27.732]  [00:01:10.500][silabs ]SPP: ack_timeout_ms 500
[17:33:28.074]  [00:01:10.848][silabs ]MATTER RX: 55 AA 01 00 67 E2 01 F0 3A 
[17:33:28.074]  [00:01:10.848][silabs ]payload: F0 
[17:33:28.074]  [00:01:10.848][silabs ]COM: OTAData request without offset, using state offset=24720
[17:33:28.078]  [00:01:10.848][silabs ]COM: spp_app_event_OTAData, req_offset=24720, read_len=240
[17:33:28.176]  [00:01:10.950][silabs ]MATTER TX: 55 AA 01 00 64 E2 F0 FF F7 C6 FF 06 49 08 80 10 BD C0 46 0F 50 04 40 C8 0E 00 20 0E 50 04 40 CC 0E 
[17:33:28.181]  [00:01:10.950][silabs ]COM: CMD: 0xE2, SN: 0x0064, LEN: 248
[17:33:28.181]  
[17:33:28.181]  [00:01:10.950][silabs ]SPP: ack_timeout_ms 500
[17:33:28.524]  [00:01:11.297][silabs ]MATTER RX: 55 AA 01 00 68 E2 01 F0 3B 
[17:33:28.524]  [00:01:11.297][silabs ]payload: F0 
[17:33:28.524]  [00:01:11.297][silabs ]COM: OTAData request without offset, using state offset=24960
[17:33:28.525]  [00:01:11.297][silabs ]COM: spp_app_event_OTAData, req_offset=24960, read_len=240
[17:33:28.625]  [00:01:11.398][silabs ]MATTER TX: 55 AA 01 00 65 E2 F0 08 9A FE F7 E9 FE 03 99 06 98 FE F7 B5 FE 04 98 05 99 08 9A FE F7 E0 FE 04 98 
[17:33:28.628]  [00:01:11.398][silabs ]COM: CMD: 0xE2, SN: 0x0065, LEN: 248
[17:33:28.628]  
[17:33:28.628]  [00:01:11.398][silabs ]SPP: ack_timeout_ms 500
[17:33:28.973]  [00:01:11.747][silabs ]MATTER RX: 55 AA 01 00 69 E2 01 F0 3C 
[17:33:28.973]  [00:01:11.748][silabs ]payload: F0 
[17:33:28.973]  [00:01:11.748][silabs ]COM: OTAData request without offset, using state offset=25200
[17:33:28.975]  [00:01:11.748][silabs ]COM: spp_app_event_OTAData, req_offset=25200, read_len=240
[17:33:29.075]  [00:01:11.848][silabs ]MATTER TX: 55 AA 01 00 66 E2 F0 08 70 57 49 08 68 90 43 08 60 FD F7 43 F8 FD F7 47 F8 02 9B 03 99 04 98 1A 78 
[17:33:29.079]  [00:01:11.848][silabs ]COM: CMD: 0xE2, SN: 0x0066, LEN: 248
[17:33:29.079]  
[17:33:29.079]  [00:01:11.848][silabs ]SPP: ack_timeout_ms 500
[17:33:29.423]  [00:01:12.197][silabs ]MATTER RX: 55 AA 01 00 6A E2 01 F0 3D 
[17:33:29.423]  [00:01:12.197][silabs ]payload: F0 
[17:33:29.423]  [00:01:12.197][silabs ]COM: OTAData request without offset, using state offset=25440
[17:33:29.426]  [00:01:12.197][silabs ]COM: spp_app_event_OTAData, req_offset=25440, read_len=240
[17:33:29.524]  [00:01:12.297][silabs ]MATTER TX: 55 AA 01 00 67 E2 F0 FE F7 DE FD 00 28 06 D1 FF E7 1B 49 08 68 01 22 10 43 08 60 FF E7 00 20 01 21 
[17:33:29.527]  [00:01:12.297][silabs ]COM: CMD: 0xE2, SN: 0x0067, LEN: 248
[17:33:29.527]  
[17:33:29.527]  [00:01:12.297][silabs ]SPP: ack_timeout_ms 500
[17:33:29.872]  [00:01:12.646][silabs ]MATTER RX: 55 AA 01 00 6B E2 01 F0 3E 
[17:33:29.872]  [00:01:12.646][silabs ]payload: F0 
[17:33:29.872]  [00:01:12.646][silabs ]COM: OTAData request without offset, using state offset=25680
[17:33:29.876]  [00:01:12.647][silabs ]COM: spp_app_event_OTAData, req_offset=25680, read_len=240
[17:33:29.974]  [00:01:12.748][silabs ]MATTER TX: 55 AA 01 00 68 E2 F0 08 70 FF E7 00 98 40 1C 69 46 08 80 EA E7 01 A8 00 78 04 B0 70 47 80 B5 86 B0 
[17:33:29.978]  [00:01:12.748][silabs ]COM: CMD: 0xE2, SN: 0x0068, LEN: 248
[17:33:29.978]  
[17:33:29.978]  [00:01:12.748][silabs ]SPP: ack_timeout_ms 500
[17:33:30.322]  [00:01:13.095][silabs ]MATTER RX: 55 AA 01 00 6C E2 01 F0 3F 
[17:33:30.322]  [00:01:13.096][silabs ]payload: F0 
[17:33:30.322]  [00:01:13.096][silabs ]COM: OTAData request without offset, using state offset=25920
[17:33:30.324]  [00:01:13.096][silabs ]COM: spp_app_event_OTAData, req_offset=25920, read_len=240
[17:33:30.424]  [00:01:13.198][silabs ]MATTER TX: 55 AA 01 00 69 E2 F0 0C D1 FF E7 00 20 05 90 00 F0 DE F8 05 98 7F 49 24 22 88 54 32 22 03 20 88 54 
[17:33:30.428]  [00:01:13.198][silabs ]COM: CMD: 0xE2, SN: 0x0069, LEN: 248
[17:33:30.428]  
[17:33:30.428]  [00:01:13.198][silabs ]SPP: ack_timeout_ms 500
[17:33:30.771]  [00:01:13.545][silabs ]MATTER RX: 55 AA 01 00 6D E2 01 F0 40 
[17:33:30.771]  [00:01:13.545][silabs ]payload: F0 
[17:33:30.771]  [00:01:13.545][silabs ]COM: OTAData request without offset, using state offset=26160
[17:33:30.773]  [00:01:13.545][silabs ]COM: spp_app_event_OTAData, req_offset=26160, read_len=240
[17:33:30.872]  [00:01:13.646][silabs ]MATTER TX: 55 AA 01 00 6A E2 F0 46 48 00 7F 63 28 1C DC FF E7 44 48 00 6A 30 49 04 F0 DB F9 00 28 14 D1 FF E7 
[17:33:30.876]  [00:01:13.646][silabs ]COM: CMD: 0xE2, SN: 0x006A, LEN: 248
[17:33:30.876]  
[17:33:30.876]  [00:01:13.646][silabs ]SPP: ack_timeout_ms 500
[17:33:31.221]  [00:01:13.995][silabs ]MATTER RX: 55 AA 01 00 6E E2 01 F0 41 
[17:33:31.221]  [00:01:13.995][silabs ]payload: F0 
[17:33:31.221]  [00:01:13.995][silabs ]COM: OTAData request without offset, using state offset=26400
[17:33:31.222]  [00:01:13.996][silabs ]COM: spp_app_event_OTAData, req_offset=26400, read_len=240
[17:33:31.322]  [00:01:14.096][silabs ]MATTER TX: 55 AA 01 00 6B E2 F0 00 21 FE F7 E9 FB FF E7 08 49 36 22 01 20 88 54 0A E0 FF E7 0C 20 00 21 FE F7 
[17:33:31.326]  [00:01:14.096][silabs ]COM: CMD: 0xE2, SN: 0x006B, LEN: 248
[17:33:31.326]  
[17:33:31.326]  [00:01:14.096][silabs ]SPP: ack_timeout_ms 500
[17:33:31.671]  [00:01:14.444][silabs ]MATTER RX: 55 AA 01 00 6F E2 01 F0 42 
[17:33:31.671]  [00:01:14.445][silabs ]payload: F0 
[17:33:31.671]  [00:01:14.445][silabs ]COM: OTAData request without offset, using state offset=26640
[17:33:31.672]  [00:01:14.445][silabs ]COM: spp_app_event_OTAData, req_offset=26640, read_len=240
[17:33:31.772]  [00:01:14.545][silabs ]MATTER TX: 55 AA 01 00 6C E2 F0 80 B5 86 B0 05 90 05 98 00 79 04 A9 08 80 03 F0 01 F8 01 28 05 DC FF E7 03 F0 
[17:33:31.776]  [00:01:14.545][silabs ]COM: CMD: 0xE2, SN: 0x006C, LEN: 248
[17:33:31.776]  
[17:33:31.776]  [00:01:14.545][silabs ]SPP: ack_timeout_ms 500
[17:33:32.120]  [00:01:14.894][silabs ]MATTER RX: 55 AA 01 00 70 E2 01 F0 43 
[17:33:32.120]  [00:01:14.894][silabs ]payload: F0 
[17:33:32.120]  [00:01:14.894][silabs ]COM: OTAData request without offset, using state offset=26880
[17:33:32.121]  [00:01:14.894][silabs ]COM: spp_app_event_OTAData, req_offset=26880, read_len=240
[17:33:32.222]  [00:01:14.996][silabs ]MATTER TX: 55 AA 01 00 6D E2 F0 02 20 01 F0 91 FA FF E7 07 E0 2A 49 00 20 08 74 01 20 01 F0 89 FA 00 E0 FF E7 
[17:33:32.226]  [00:01:14.996][silabs ]COM: CMD: 0xE2, SN: 0x006D, LEN: 248
[17:33:32.226]  
[17:33:32.226]  [00:01:14.996][silabs ]SPP: ack_timeout_ms 500
[17:33:32.569]  [00:01:15.343][silabs ]MATTER RX: 55 AA 01 00 71 E2 01 F0 44 
[17:33:32.569]  [00:01:15.343][silabs ]payload: F0 
[17:33:32.569]  [00:01:15.344][silabs ]COM: OTAData request without offset, using state offset=27120
[17:33:32.571]  [00:01:15.344][silabs ]COM: spp_app_event_OTAData, req_offset=27120, read_len=240
[17:33:32.670]  [00:01:15.444][silabs ]MATTER TX: 55 AA 01 00 6E E2 F0 01 AB 18 70 DA 48 01 88 49 1C 01 80 01 88 01 20 00 90 00 20 04 22 02 F0 1B FE 
[17:33:32.673]  [00:01:15.444][silabs ]COM: CMD: 0xE2, SN: 0x006E, LEN: 248
[17:33:32.673]  
[17:33:32.673]  [00:01:15.444][silabs ]SPP: ack_timeout_ms 500
[17:33:33.019]  [00:01:15.793][silabs ]MATTER RX: 55 AA 01 00 72 E2 01 F0 45 
[17:33:33.019]  [00:01:15.793][silabs ]payload: F0 
[17:33:33.019]  [00:01:15.793][silabs ]COM: OTAData request without offset, using state offset=27360
[17:33:33.021]  [00:01:15.793][silabs ]COM: spp_app_event_OTAData, req_offset=27360, read_len=240
[17:33:33.121]  [00:01:15.894][silabs ]MATTER TX: 55 AA 01 00 6F E2 F0 01 28 09 D1 FF E7 05 9B 41 49 9A 22 88 5C C0 18 88 54 03 20 08 74 03 E0 3D 49 
[17:33:33.126]  [00:01:15.894][silabs ]COM: CMD: 0xE2, SN: 0x006F, LEN: 248
[17:33:33.126]  
[17:33:33.126]  [00:01:15.894][silabs ]SPP: ack_timeout_ms 500
[17:33:33.469]  [00:01:16.243][silabs ]MATTER RX: 55 AA 01 00 73 E2 01 F0 46 
[17:33:33.469]  [00:01:16.243][silabs ]payload: F0 
[17:33:33.469]  [00:01:16.243][silabs ]COM: OTAData request without offset, using state offset=27600
[17:33:33.472]  [00:01:16.243][silabs ]COM: spp_app_event_OTAData, req_offset=27600, read_len=240
[17:33:33.571]  [00:01:16.344][silabs ]MATTER TX: 55 AA 01 00 70 E2 F0 FF E7 04 A9 01 20 08 70 FF E7 05 49 00 20 08 74 00 E0 FF E7 04 A8 00 78 01 21 
[17:33:33.576]  [00:01:16.344][silabs ]COM: CMD: 0xE2, SN: 0x0070, LEN: 248
[17:33:33.576]  
[17:33:33.576]  [00:01:16.344][silabs ]SPP: ack_timeout_ms 500
[17:33:33.918]  [00:01:16.692][silabs ]MATTER RX: 55 AA 01 00 74 E2 01 F0 47 
[17:33:33.918]  [00:01:16.693][silabs ]payload: F0 
[17:33:33.918]  [00:01:16.693][silabs ]COM: OTAData request without offset, using state offset=27840
[17:33:33.921]  [00:01:16.693][silabs ]COM: spp_app_event_OTAData, req_offset=27840, read_len=240
[17:33:34.019]  [00:01:16.793][silabs ]MATTER TX: 55 AA 01 00 71 E2 F0 02 AB 00 20 18 70 58 70 98 70 03 99 D9 70 BA 49 0A 88 52 1C 0A 80 09 88 04 22 
[17:33:34.023]  [00:01:16.793][silabs ]COM: CMD: 0xE2, SN: 0x0071, LEN: 248
[17:33:34.023]  
[17:33:34.023]  [00:01:16.793][silabs ]SPP: ack_timeout_ms 500
[17:33:34.368]  [00:01:17.142][silabs ]MATTER RX: 55 AA 01 00 75 E2 01 F0 48 
[17:33:34.368]  [00:01:17.142][silabs ]payload: F0 
[17:33:34.368]  [00:01:17.142][silabs ]COM: OTAData request without offset, using state offset=28080
[17:33:34.370]  [00:01:17.142][silabs ]COM: spp_app_event_OTAData, req_offset=28080, read_len=240
[17:33:34.470]  [00:01:17.244][silabs ]MATTER TX: 55 AA 01 00 72 E2 F0 04 98 00 28 15 D0 FF E7 06 99 48 08 00 90 01 20 01 40 01 91 0B 48 00 29 02 90 
[17:33:34.473]  [00:01:17.244][silabs ]COM: CMD: 0xE2, SN: 0x0072, LEN: 248
[17:33:34.473]  
[17:33:34.473]  [00:01:17.244][silabs ]SPP: ack_timeout_ms 500
[17:33:34.817]  [00:01:17.591][silabs ]MATTER RX: 55 AA 01 00 76 E2 01 F0 49 
[17:33:34.817]  [00:01:17.592][silabs ]payload: F0 
[17:33:34.817]  [00:01:17.592][silabs ]COM: OTAData request without offset, using state offset=28320
[17:33:34.819]  [00:01:17.592][silabs ]COM: spp_app_event_OTAData, req_offset=28320, read_len=240
[17:33:34.919]  [00:01:17.693][silabs ]MATTER TX: 55 AA 01 00 73 E2 F0 01 A9 0A 80 00 88 A6 49 89 7D 88 42 03 D1 FF E7 01 F0 6E F9 FF E7 04 B0 80 BD 
[17:33:34.923]  [00:01:17.693][silabs ]COM: CMD: 0xE2, SN: 0x0073, LEN: 248
[17:33:34.923]  
[17:33:34.923]  [00:01:17.693][silabs ]SPP: ack_timeout_ms 500
[17:33:35.267]  [00:01:18.041][silabs ]MATTER RX: 55 AA 01 00 77 E2 01 F0 4A 
[17:33:35.267]  [00:01:18.041][silabs ]payload: F0 
[17:33:35.267]  [00:01:18.041][silabs ]COM: OTAData request without offset, using state offset=28560
[17:33:35.269]  [00:01:18.041][silabs ]COM: spp_app_event_OTAData, req_offset=28560, read_len=240
[17:33:35.368]  [00:01:18.142][silabs ]MATTER TX: 55 AA 01 00 74 E2 F0 80 B5 84 B0 03 46 03 A8 03 80 02 91 01 A9 0A 80 00 88 BB 49 09 88 88 42 03 D1 
[17:33:35.372]  [00:01:18.142][silabs ]COM: CMD: 0xE2, SN: 0x0074, LEN: 248
[17:33:35.372]  
[17:33:35.372]  [00:01:18.142][silabs ]SPP: ack_timeout_ms 500
[17:33:35.717]  [00:01:18.491][silabs ]MATTER RX: 55 AA 01 00 78 E2 01 F0 4B 
[17:33:35.717]  [00:01:18.491][silabs ]payload: F0 
[17:33:35.717]  [00:01:18.491][silabs ]COM: OTAData request without offset, using state offset=28800
[17:33:35.721]  [00:01:18.492][silabs ]COM: spp_app_event_OTAData, req_offset=28800, read_len=240
[17:33:35.818]  [00:01:18.592][silabs ]MATTER TX: 55 AA 01 00 75 E2 F0 0B 88 90 68 C0 18 90 60 06 98 09 88 FF F7 C8 F9 03 99 02 46 48 68 80 18 48 60 
[17:33:35.822]  [00:01:18.592][silabs ]COM: CMD: 0xE2, SN: 0x0075, LEN: 248
[17:33:35.822]  
[17:33:35.822]  [00:01:18.592][silabs ]SPP: ack_timeout_ms 500
[17:33:36.167]  [00:01:18.940][silabs ]MATTER RX: 55 AA 01 00 79 E2 01 F0 4C 
[17:33:36.167]  [00:01:18.941][silabs ]payload: F0 
[17:33:36.167]  [00:01:18.941][silabs ]COM: OTAData request without offset, using state offset=29040
[17:33:36.168]  [00:01:18.941][silabs ]COM: spp_app_event_OTAData, req_offset=29040, read_len=240
[17:33:36.268]  [00:01:19.041][silabs ]MATTER TX: 55 AA 01 00 76 E2 F0 0C 90 02 F0 11 FD 01 46 0D 98 01 70 00 78 03 90 23 48 04 90 01 F0 E6 FE 03 99 
[17:33:36.271]  [00:01:19.041][silabs ]COM: CMD: 0xE2, SN: 0x0076, LEN: 248
[17:33:36.271]  
[17:33:36.271]  [00:01:19.041][silabs ]SPP: ack_timeout_ms 500
[17:33:36.616]  [00:01:19.390][silabs ]MATTER RX: 55 AA 01 00 7A E2 01 F0 4D 
[17:33:36.616]  [00:01:19.390][silabs ]payload: F0 
[17:33:36.616]  [00:01:19.390][silabs ]COM: OTAData request without offset, using state offset=29280
[17:33:36.618]  [00:01:19.390][silabs ]COM: spp_app_event_OTAData, req_offset=29280, read_len=240
[17:33:36.718]  [00:01:19.492][silabs ]MATTER TX: 55 AA 01 00 77 E2 F0 02 F0 EE F9 04 B0 80 BD 80 B5 84 B0 03 46 03 A8 03 80 02 91 01 A9 0A 80 00 88 
[17:33:36.722]  [00:01:19.492][silabs ]COM: CMD: 0xE2, SN: 0x0077, LEN: 248
[17:33:36.722]  
[17:33:36.722]  [00:01:19.492][silabs ]SPP: ack_timeout_ms 500
[17:33:37.065]  [00:01:19.839][silabs ]MATTER RX: 55 AA 01 00 7B E2 01 F0 4E 
[17:33:37.065]  [00:01:19.840][silabs ]payload: F0 
[17:33:37.065]  [00:01:19.840][silabs ]COM: OTAData request without offset, using state offset=29520
[17:33:37.067]  [00:01:19.840][silabs ]COM: spp_app_event_OTAData, req_offset=29520, read_len=240
[17:33:37.167]  [00:01:19.941][silabs ]MATTER TX: 55 AA 01 00 78 E2 F0 02 F0 EC F9 00 99 02 46 01 98 03 AB 1A 70 40 5C C0 07 00 28 1D D0 FF E7 03 A8 
[17:33:37.171]  [00:01:19.941][silabs ]COM: CMD: 0xE2, SN: 0x0078, LEN: 248
[17:33:37.171]  
[17:33:37.171]  [00:01:19.941][silabs ]SPP: ack_timeout_ms 500
[17:33:37.515]  [00:01:20.289][silabs ]MATTER RX: 55 AA 01 00 7C E2 01 F0 4F 
[17:33:37.515]  [00:01:20.289][silabs ]payload: F0 
[17:33:37.515]  [00:01:20.289][silabs ]COM: OTAData request without offset, using state offset=29760
[17:33:37.516]  [00:01:20.290][silabs ]COM: spp_app_event_OTAData, req_offset=29760, read_len=240
[17:33:37.616]  [00:01:20.390][silabs ]MATTER TX: 55 AA 01 00 79 E2 F0 80 BD C0 46 7C 00 00 20 71 8D 00 00 10 B5 94 B0 95 48 40 7C 0F 90 00 28 09 D0 
[17:33:37.621]  [00:01:20.390][silabs ]COM: CMD: 0xE2, SN: 0x0079, LEN: 248
[17:33:37.621]  
[17:33:37.621]  [00:01:20.390][silabs ]SPP: ack_timeout_ms 500
[17:33:37.965]  [00:01:20.739][silabs ]MATTER RX: 55 AA 01 00 7D E2 01 F0 50 
[17:33:37.965]  [00:01:20.740][silabs ]payload: F0 
[17:33:37.965]  [00:01:20.740][silabs ]COM: OTAData request without offset, using state offset=30000
[17:33:37.967]  [00:01:20.740][silabs ]COM: spp_app_event_OTAData, req_offset=30000, read_len=240
[17:33:38.066]  [00:01:20.840][silabs ]MATTER TX: 55 AA 01 00 7A E2 F0 49 1C 81 61 80 69 14 28 06 D3 FF E7 39 49 08 68 10 22 90 43 08 60 FF E7 FF E7 
[17:33:38.071]  [00:01:20.840][silabs ]COM: CMD: 0xE2, SN: 0x007A, LEN: 248
[17:33:38.071]  
[17:33:38.071]  [00:01:20.840][silabs ]SPP: ack_timeout_ms 500
[17:33:38.415]  [00:01:21.189][silabs ]MATTER RX: 55 AA 01 00 7E E2 01 F0 51 
[17:33:38.415]  [00:01:21.189][silabs ]payload: F0 
[17:33:38.415]  [00:01:21.189][silabs ]COM: OTAData request without offset, using state offset=30240
[17:33:38.416]  [00:01:21.189][silabs ]COM: spp_app_event_OTAData, req_offset=30240, read_len=240
[17:33:38.516]  [00:01:21.291][silabs ]MATTER TX: 55 AA 01 00 7B E2 F0 44 16 00 20 3C 0E 00 20 80 B5 82 B0 0F 48 01 A9 01 22 02 F0 9A F9 01 28 10 DB 
[17:33:38.520]  [00:01:21.291][silabs ]COM: CMD: 0xE2, SN: 0x007B, LEN: 248
[17:33:38.520]  
[17:33:38.520]  [00:01:21.291][silabs ]SPP: ack_timeout_ms 500
[17:33:38.864]  [00:01:21.638][silabs ]MATTER RX: 55 AA 01 00 7F E2 01 F0 52 
[17:33:38.864]  [00:01:21.638][silabs ]payload: F0 
[17:33:38.864]  [00:01:21.639][silabs ]COM: OTAData request without offset, using state offset=30480
[17:33:38.866]  [00:01:21.639][silabs ]COM: spp_app_event_OTAData, req_offset=30480, read_len=240
[17:33:38.966]  [00:01:21.740][silabs ]MATTER TX: 55 AA 01 00 7C E2 F0 81 00 01 A0 40 58 87 46 99 90 00 00 B7 90 00 00 DF 90 00 00 47 91 00 00 84 49 
[17:33:38.971]  [00:01:21.740][silabs ]COM: CMD: 0xE2, SN: 0x007C, LEN: 248
[17:33:38.971]  
[17:33:38.971]  [00:01:21.740][silabs ]SPP: ack_timeout_ms 500
[17:33:39.314]  [00:01:22.088][silabs ]MATTER RX: 55 AA 01 00 80 E2 01 F0 53 
[17:33:39.314]  [00:01:22.088][silabs ]payload: F0 
[17:33:39.314]  [00:01:22.088][silabs ]COM: OTAData request without offset, using state offset=30720
[17:33:39.318]  [00:01:22.088][silabs ]COM: spp_app_event_OTAData, req_offset=30720, read_len=240
[17:33:39.415]  [00:01:22.189][silabs ]MATTER TX: 55 AA 01 00 7D E2 F0 00 28 08 D0 FF E7 4E 48 01 79 00 23 18 46 1A 46 02 F0 C6 FA FF E7 C8 49 08 68 
[17:33:39.421]  [00:01:22.189][silabs ]COM: CMD: 0xE2, SN: 0x007D, LEN: 248
[17:33:39.421]  
[17:33:39.421]  [00:01:22.189][silabs ]SPP: ack_timeout_ms 500
[17:33:39.764]  [00:01:22.538][silabs ]MATTER RX: 55 AA 01 00 81 E2 01 F0 54 
[17:33:39.764]  [00:01:22.538][silabs ]payload: F0 
[17:33:39.764]  [00:01:22.538][silabs ]COM: OTAData request without offset, using state offset=30960
[17:33:39.768]  [00:01:22.538][silabs ]COM: spp_app_event_OTAData, req_offset=30960, read_len=240
[17:33:39.865]  [00:01:22.639][silabs ]MATTER TX: 55 AA 01 00 7E E2 F0 00 28 08 D0 FF E7 12 48 C1 78 00 23 18 46 1A 46 02 F0 4E FA FF E7 FF E7 FF E7 
[17:33:39.871]  [00:01:22.639][silabs ]COM: CMD: 0xE2, SN: 0x007E, LEN: 248
[17:33:39.871]  
[17:33:39.871]  [00:01:22.639][silabs ]SPP: ack_timeout_ms 500
[17:33:40.214]  [00:01:22.987][silabs ]MATTER RX: 55 AA 01 00 82 E2 01 F0 55 
[17:33:40.214]  [00:01:22.988][silabs ]payload: F0 
[17:33:40.214]  [00:01:22.988][silabs ]COM: OTAData request without offset, using state offset=31200
[17:33:40.217]  [00:01:22.988][silabs ]COM: spp_app_event_OTAData, req_offset=31200, read_len=240
[17:33:40.314]  [00:01:23.088][silabs ]MATTER TX: 55 AA 01 00 7F E2 F0 14 21 41 43 E5 48 40 18 00 1D 06 90 06 99 88 88 40 1C 88 80 06 99 88 88 49 89 
[17:33:40.317]  [00:01:23.088][silabs ]COM: CMD: 0xE2, SN: 0x007F, LEN: 248
[17:33:40.317]  
[17:33:40.317]  [00:01:23.088][silabs ]SPP: ack_timeout_ms 500
[17:33:40.663]  [00:01:23.437][silabs ]MATTER RX: 55 AA 01 00 83 E2 01 F0 56 
[17:33:40.663]  [00:01:23.437][silabs ]payload: F0 
[17:33:40.663]  [00:01:23.437][silabs ]COM: OTAData request without offset, using state offset=31440
[17:33:40.667]  [00:01:23.437][silabs ]COM: spp_app_event_OTAData, req_offset=31440, read_len=240
[17:33:40.765]  [00:01:23.539][silabs ]MATTER TX: 55 AA 01 00 80 E2 F0 88 88 09 89 88 42 2C DB FF E7 02 99 00 20 88 80 02 98 80 89 00 28 06 D0 FF E7 
[17:33:40.768]  [00:01:23.539][silabs ]COM: CMD: 0xE2, SN: 0x0080, LEN: 248
[17:33:40.768]  
[17:33:40.768]  [00:01:23.539][silabs ]SPP: ack_timeout_ms 500
[17:33:41.112]  [00:01:23.886][silabs ]MATTER RX: 55 AA 01 00 84 E2 01 F0 57 
[17:33:41.112]  [00:01:23.887][silabs ]payload: F0 
[17:33:41.112]  [00:01:23.887][silabs ]COM: OTAData request without offset, using state offset=31680
[17:33:41.117]  [00:01:23.887][silabs ]COM: spp_app_event_OTAData, req_offset=31680, read_len=240
[17:33:41.214]  [00:01:23.989][silabs ]MATTER TX: 55 AA 01 00 81 E2 F0 04 98 1B 78 5A 43 89 18 48 70 03 A8 00 88 0A 21 F8 F7 BA FF 00 9B 01 9A 01 46 
[17:33:41.220]  [00:01:23.989][silabs ]COM: CMD: 0xE2, SN: 0x0081, LEN: 248
[17:33:41.220]  
[17:33:41.220]  [00:01:23.989][silabs ]SPP: ack_timeout_ms 500
[17:33:41.562]  [00:01:24.336][silabs ]MATTER RX: 55 AA 01 00 85 E2 01 F0 58 
[17:33:41.562]  [00:01:24.336][silabs ]payload: F0 
[17:33:41.562]  [00:01:24.336][silabs ]COM: OTAData request without offset, using state offset=31920
[17:33:41.564]  [00:01:24.336][silabs ]COM: spp_app_event_OTAData, req_offset=31920, read_len=240
[17:33:41.664]  [00:01:24.437][silabs ]MATTER TX: 55 AA 01 00 82 E2 F0 06 9C 16 78 0D 46 75 43 45 19 AC 81 15 78 0C 46 6C 43 04 19 E3 81 12 78 51 43 
[17:33:41.667]  [00:01:24.437][silabs ]COM: CMD: 0xE2, SN: 0x0082, LEN: 248
[17:33:41.667]  
[17:33:41.667]  [00:01:24.437][silabs ]SPP: ack_timeout_ms 500
[17:33:42.012]  [00:01:24.786][silabs ]MATTER RX: 55 AA 01 00 86 E2 01 F0 59 
[17:33:42.012]  [00:01:24.787][silabs ]payload: F0 
[17:33:42.012]  [00:01:24.787][silabs ]COM: OTAData request without offset, using state offset=32160
[17:33:42.013]  [00:01:24.787][silabs ]COM: spp_app_event_OTAData, req_offset=32160, read_len=240
[17:33:42.113]  [00:01:24.887][silabs ]MATTER TX: 55 AA 01 00 83 E2 F0 07 D0 0B E0 FD F7 12 FC FD F7 DC FB 00 F0 18 FA 05 E0 FD F7 0B FC FC F7 97 FE 
[17:33:42.117]  [00:01:24.887][silabs ]COM: CMD: 0xE2, SN: 0x0083, LEN: 248
[17:33:42.117]  
[17:33:42.117]  [00:01:24.887][silabs ]SPP: ack_timeout_ms 500
[17:33:42.461]  [00:01:25.236][silabs ]MATTER RX: 55 AA 01 00 87 E2 01 F0 5A 
[17:33:42.461]  [00:01:25.236][silabs ]payload: F0 
[17:33:42.461]  [00:01:25.236][silabs ]COM: OTAData request without offset, using state offset=32400
[17:33:42.463]  [00:01:25.236][silabs ]COM: spp_app_event_OTAData, req_offset=32400, read_len=240
[17:33:42.563]  [00:01:25.337][silabs ]MATTER TX: 55 AA 01 00 84 E2 F0 00 78 01 28 09 D1 FF E7 FC F7 70 FE 01 F0 6E FE 01 F0 00 FD FE F7 02 FF FF E7 
[17:33:42.566]  [00:01:25.337][silabs ]COM: CMD: 0xE2, SN: 0x0084, LEN: 248
[17:33:42.566]  
[17:33:42.566]  [00:01:25.337][silabs ]SPP: ack_timeout_ms 500
[17:33:42.911]  [00:01:25.685][silabs ]MATTER RX: 55 AA 01 00 88 E2 01 F0 5B 
[17:33:42.911]  [00:01:25.685][silabs ]payload: F0 
[17:33:42.911]  [00:01:25.686][silabs ]COM: OTAData request without offset, using state offset=32640
[17:33:42.912]  [00:01:25.686][silabs ]COM: spp_app_event_OTAData, req_offset=32640, read_len=240
[17:33:43.012]  [00:01:25.787][silabs ]MATTER TX: 55 AA 01 00 85 E2 F0 00 28 16 D0 FF E7 35 48 18 30 00 F0 71 FA 00 28 0E D0 FF E7 1D 49 08 68 40 1C 
[17:33:43.016]  [00:01:25.787][silabs ]COM: CMD: 0xE2, SN: 0x0085, LEN: 248
[17:33:43.016]  
[17:33:43.016]  [00:01:25.787][silabs ]SPP: ack_timeout_ms 500
[17:33:43.362]  [00:01:26.135][silabs ]MATTER RX: 55 AA 01 00 89 E2 01 F0 5C 
[17:33:43.362]  [00:01:26.135][silabs ]payload: F0 
[17:33:43.362]  [00:01:26.135][silabs ]COM: OTAData request without offset, using state offset=32880
[17:33:43.363]  [00:01:26.135][silabs ]COM: spp_app_event_OTAData, req_offset=32880, read_len=240
[17:33:43.462]  [00:01:26.236][silabs ]MATTER TX: 55 AA 01 00 86 E2 F0 00 92 11 80 00 78 07 A9 01 91 06 AC 02 94 05 AB 03 93 22 46 FD F7 DA F8 00 98 
[17:33:43.466]  [00:01:26.236][silabs ]COM: CMD: 0xE2, SN: 0x0086, LEN: 248
[17:33:43.466]  
[17:33:43.466]  [00:01:26.236][silabs ]SPP: ack_timeout_ms 500
[17:33:43.810]  [00:01:26.584][silabs ]MATTER RX: 55 AA 01 00 8A E2 01 F0 5D 
[17:33:43.810]  [00:01:26.584][silabs ]payload: F0 
[17:33:43.810]  [00:01:26.584][silabs ]COM: OTAData request without offset, using state offset=33120
[17:33:43.812]  [00:01:26.585][silabs ]COM: spp_app_event_OTAData, req_offset=33120, read_len=240
[17:33:43.912]  [00:01:26.686][silabs ]MATTER TX: 55 AA 01 00 87 E2 F0 01 F0 E8 FB 08 48 00 90 08 49 01 22 01 92 FF F7 9F FA 00 98 01 99 00 F0 11 F8 
[17:33:43.915]  [00:01:26.686][silabs ]COM: CMD: 0xE2, SN: 0x0087, LEN: 248
[17:33:43.915]  
[17:33:43.915]  [00:01:26.686][silabs ]SPP: ack_timeout_ms 500
[17:33:44.261]  [00:01:27.034][silabs ]MATTER RX: 55 AA 01 00 8B E2 01 F0 5E 
[17:33:44.261]  [00:01:27.035][silabs ]payload: F0 
[17:33:44.261]  [00:01:27.035][silabs ]COM: OTAData request without offset, using state offset=33360
[17:33:44.262]  [00:01:27.035][silabs ]COM: spp_app_event_OTAData, req_offset=33360, read_len=240
[17:33:44.361]  [00:01:27.135][silabs ]MATTER TX: 55 AA 01 00 88 E2 F0 0C 0A 00 20 3C 0E 00 20 80 B5 84 B0 35 48 00 7C 03 90 00 28 08 D0 FF E7 03 98 
[17:33:44.365]  [00:01:27.135][silabs ]COM: CMD: 0xE2, SN: 0x0088, LEN: 248
[17:33:44.365]  
[17:33:44.365]  [00:01:27.135][silabs ]SPP: ack_timeout_ms 500
[17:33:44.710]  [00:01:27.484][silabs ]MATTER RX: 55 AA 01 00 8C E2 01 F0 5F 
[17:33:44.710]  [00:01:27.484][silabs ]payload: F0 
[17:33:44.710]  [00:01:27.484][silabs ]COM: OTAData request without offset, using state offset=33600
[17:33:44.711]  [00:01:27.484][silabs ]COM: spp_app_event_OTAData, req_offset=33600, read_len=240
[17:33:44.811]  [00:01:27.585][silabs ]MATTER TX: 55 AA 01 00 89 E2 F0 68 46 01 80 00 88 01 28 05 DB FF E7 02 20 01 21 FC F7 FA FE 04 E0 02 20 01 21 
[17:33:44.815]  [00:01:27.585][silabs ]COM: CMD: 0xE2, SN: 0x0089, LEN: 248
[17:33:44.815]  
[17:33:44.815]  [00:01:27.585][silabs ]SPP: ack_timeout_ms 500
[17:33:45.159]  [00:01:27.933][silabs ]MATTER RX: 55 AA 01 00 8D E2 01 F0 60 
[17:33:45.159]  [00:01:27.934][silabs ]payload: F0 
[17:33:45.159]  [00:01:27.934][silabs ]COM: OTAData request without offset, using state offset=33840
[17:33:45.161]  [00:01:27.934][silabs ]COM: spp_app_event_OTAData, req_offset=33840, read_len=240
[17:33:45.262]  [00:01:28.036][silabs ]MATTER TX: 55 AA 01 00 8A E2 F0 18 E0 00 E0 B4 0A 00 20 40 42 0F 00 E9 03 00 00 E7 03 00 00 81 B0 00 90 00 9A 
[17:33:45.265]  [00:01:28.036][silabs ]COM: CMD: 0xE2, SN: 0x008A, LEN: 248
[17:33:45.265]  
[17:33:45.265]  [00:01:28.036][silabs ]SPP: ack_timeout_ms 500
[17:33:45.609]  [00:01:28.383][silabs ]MATTER RX: 55 AA 01 00 8E E2 01 F0 61 
[17:33:45.609]  [00:01:28.383][silabs ]payload: F0 
[17:33:45.609]  [00:01:28.383][silabs ]COM: OTAData request without offset, using state offset=34080
[17:33:45.611]  [00:01:28.383][silabs ]COM: spp_app_event_OTAData, req_offset=34080, read_len=240
[17:33:45.710]  [00:01:28.484][silabs ]MATTER TX: 55 AA 01 00 8B E2 F0 0E 48 F8 F7 9D FA 01 99 0D 48 F8 F7 99 FA 00 99 0C 48 F8 F7 95 FA 08 99 0B 48 
[17:33:45.716]  [00:01:28.484][silabs ]COM: CMD: 0xE2, SN: 0x008B, LEN: 248
[17:33:45.716]  
[17:33:45.716]  [00:01:28.484][silabs ]SPP: ack_timeout_ms 500
[17:33:46.059]  [00:01:28.833][silabs ]MATTER RX: 55 AA 01 00 8F E2 01 F0 62 
[17:33:46.059]  [00:01:28.833][silabs ]payload: F0 
[17:33:46.059]  [00:01:28.833][silabs ]COM: OTAData request without offset, using state offset=34320
[17:33:46.060]  [00:01:28.833][silabs ]COM: spp_app_event_OTAData, req_offset=34320, read_len=240
[17:33:46.160]  [00:01:28.934][silabs ]MATTER TX: 55 AA 01 00 8C E2 F0 80 BD C0 46 80 B5 5B 48 00 78 40 06 00 28 09 D4 FF E7 D7 48 00 88 00 28 04 D0 
[17:33:46.165]  [00:01:28.934][silabs ]COM: CMD: 0xE2, SN: 0x008C, LEN: 248
[17:33:46.165]  
[17:33:46.165]  [00:01:28.934][silabs ]SPP: ack_timeout_ms 500
[17:33:46.509]  [00:01:29.283][silabs ]MATTER RX: 55 AA 01 00 90 E2 01 F0 63 
[17:33:46.509]  [00:01:29.283][silabs ]payload: F0 
[17:33:46.509]  [00:01:29.283][silabs ]COM: OTAData request without offset, using state offset=34560
[17:33:46.512]  [00:01:29.283][silabs ]COM: spp_app_event_OTAData, req_offset=34560, read_len=240
[17:33:46.610]  [00:01:29.384][silabs ]MATTER TX: 55 AA 01 00 8D E2 F0 40 1C 08 60 9E 49 08 88 40 1E 08 80 02 E0 FF F7 45 FF FF E7 FF E7 31 E0 94 48 
[17:33:46.616]  [00:01:29.384][silabs ]COM: CMD: 0xE2, SN: 0x008D, LEN: 248
[17:33:46.616]  
[17:33:46.616]  [00:01:29.384][silabs ]SPP: ack_timeout_ms 500
[17:33:46.958]  [00:01:29.732][silabs ]MATTER RX: 55 AA 01 00 91 E2 01 F0 64 
[17:33:46.958]  [00:01:29.733][silabs ]payload: F0 
[17:33:46.958]  [00:01:29.733][silabs ]COM: OTAData request without offset, using state offset=34800
[17:33:46.963]  [00:01:29.733][silabs ]COM: spp_app_event_OTAData, req_offset=34800, read_len=240
[17:33:47.059]  [00:01:29.833][silabs ]MATTER TX: 55 AA 01 00 8E E2 F0 FF E7 5C 48 00 78 C0 06 00 28 3D D5 FF E7 5D 49 08 78 10 22 10 43 08 70 57 49 
[17:33:47.065]  [00:01:29.833][silabs ]COM: CMD: 0xE2, SN: 0x008E, LEN: 248
[17:33:47.065]  
[17:33:47.065]  [00:01:29.833][silabs ]SPP: ack_timeout_ms 500
[17:33:47.408]  [00:01:30.182][silabs ]MATTER RX: 55 AA 01 00 92 E2 01 F0 65 
[17:33:47.408]  [00:01:30.182][silabs ]payload: F0 
[17:33:47.408]  [00:01:30.182][silabs ]COM: OTAData request without offset, using state offset=35040
[17:33:47.411]  [00:01:30.182][silabs ]COM: spp_app_event_OTAData, req_offset=35040, read_len=240
[17:33:47.509]  [00:01:30.284][silabs ]MATTER TX: 55 AA 01 00 8F E2 F0 08 78 20 22 10 43 08 70 FF E7 FF E7 37 E0 1E 49 08 78 02 22 10 43 08 70 1C 48 
[17:33:47.515]  [00:01:30.284][silabs ]COM: CMD: 0xE2, SN: 0x008F, LEN: 248
[17:33:47.515]  
[17:33:47.515]  [00:01:30.284][silabs ]SPP: ack_timeout_ms 500
[17:33:47.858]  [00:01:30.631][silabs ]MATTER RX: 55 AA 01 00 93 E2 01 F0 66 
[17:33:47.858]  [00:01:30.631][silabs ]payload: F0 
[17:33:47.858]  [00:01:30.631][silabs ]COM: OTAData request without offset, using state offset=35280
[17:33:47.861]  [00:01:30.632][silabs ]COM: spp_app_event_OTAData, req_offset=35280, read_len=240
[17:33:47.959]  [00:01:30.733][silabs ]MATTER TX: 55 AA 01 00 90 E2 F0 00 28 06 D0 FF E7 03 98 02 A9 09 78 FC F7 64 FA 1C E0 03 98 02 A9 09 78 FC F7 
[17:33:47.962]  [00:01:30.733][silabs ]COM: CMD: 0xE2, SN: 0x0090, LEN: 248
[17:33:47.962]  
[17:33:47.962]  [00:01:30.733][silabs ]SPP: ack_timeout_ms 500
[17:33:48.307]  [00:01:31.081][silabs ]MATTER RX: 55 AA 01 00 94 E2 01 F0 67 
[17:33:48.307]  [00:01:31.082][silabs ]payload: F0 
[17:33:48.307]  [00:01:31.082][silabs ]COM: OTAData request without offset, using state offset=35520
[17:33:48.309]  [00:01:31.082][silabs ]COM: spp_app_event_OTAData, req_offset=35520, read_len=240
[17:33:48.409]  [00:01:31.182][silabs ]MATTER TX: 55 AA 01 00 91 E2 F0 2A 49 88 69 40 1C 88 61 FF E7 FF E7 02 20 FB F7 63 F8 FF E7 04 B0 80 BD 80 B5 
[17:33:48.412]  [00:01:31.182][silabs ]COM: CMD: 0xE2, SN: 0x0091, LEN: 248
[17:33:48.412]  
[17:33:48.412]  [00:01:31.182][silabs ]SPP: ack_timeout_ms 500
[17:33:48.757]  [00:01:31.531][silabs ]MATTER RX: 55 AA 01 00 95 E2 01 F0 68 
[17:33:48.757]  [00:01:31.531][silabs ]payload: F0 
[17:33:48.757]  [00:01:31.531][silabs ]COM: OTAData request without offset, using state offset=35760
[17:33:48.758]  [00:01:31.531][silabs ]COM: spp_app_event_OTAData, req_offset=35760, read_len=240
[17:33:48.859]  [00:01:31.632][silabs ]MATTER TX: 55 AA 01 00 92 E2 F0 01 22 10 43 08 70 FF E7 02 B0 80 BD 80 B5 84 B0 03 90 02 91 03 98 02 99 00 F0 
[17:33:48.862]  [00:01:31.632][silabs ]COM: CMD: 0xE2, SN: 0x0092, LEN: 248
[17:33:48.862]  
[17:33:48.862]  [00:01:31.632][silabs ]SPP: ack_timeout_ms 500
[17:33:49.206]  [00:01:31.980][silabs ]MATTER RX: 55 AA 01 00 96 E2 01 F0 69 
[17:33:49.206]  [00:01:31.981][silabs ]payload: F0 
[17:33:49.206]  [00:01:31.981][silabs ]COM: OTAData request without offset, using state offset=36000
[17:33:49.207]  [00:01:31.981][silabs ]COM: spp_app_event_OTAData, req_offset=36000, read_len=240
[17:33:49.308]  [00:01:32.082][silabs ]MATTER TX: 55 AA 01 00 93 E2 F0 01 99 00 20 08 60 06 E0 01 98 00 90 FF E7 01 98 00 68 01 90 DD E7 04 B0 70 47 
[17:33:49.311]  [00:01:32.082][silabs ]COM: CMD: 0xE2, SN: 0x0093, LEN: 248
[17:33:49.311]  
[17:33:49.311]  [00:01:32.082][silabs ]SPP: ack_timeout_ms 500
[17:33:49.656]  [00:01:32.430][silabs ]MATTER RX: 55 AA 01 00 97 E2 01 F0 6A 
[17:33:49.656]  [00:01:32.430][silabs ]payload: F0 
[17:33:49.656]  [00:01:32.430][silabs ]COM: OTAData request without offset, using state offset=36240
[17:33:49.657]  [00:01:32.430][silabs ]COM: spp_app_event_OTAData, req_offset=36240, read_len=240
[17:33:49.758]  [00:01:32.532][silabs ]MATTER TX: 55 AA 01 00 94 E2 F0 FF E7 0D 49 08 68 04 22 10 43 08 60 30 BF FF E7 00 BF AA 20 FF F7 4E FB FD F7 
[17:33:49.761]  [00:01:32.532][silabs ]COM: CMD: 0xE2, SN: 0x0094, LEN: 248
[17:33:49.761]  
[17:33:49.761]  [00:01:32.532][silabs ]SPP: ack_timeout_ms 500
[17:33:50.105]  [00:01:32.879][silabs ]MATTER RX: 55 AA 01 00 98 E2 01 F0 6B 
[17:33:50.105]  [00:01:32.879][silabs ]payload: F0 
[17:33:50.105]  [00:01:32.879][silabs ]COM: OTAData request without offset, using state offset=36480
[17:33:50.107]  [00:01:32.880][silabs ]COM: spp_app_event_OTAData, req_offset=36480, read_len=240
[17:33:50.206]  [00:01:32.981][silabs ]MATTER TX: 55 AA 01 00 95 E2 F0 40 1C 00 90 ED E7 00 20 05 B0 70 47 80 B5 84 B0 03 90 02 91 01 92 03 98 01 99 
[17:33:50.210]  [00:01:32.981][silabs ]COM: CMD: 0xE2, SN: 0x0095, LEN: 248
[17:33:50.210]  
[17:33:50.210]  [00:01:32.981][silabs ]SPP: ack_timeout_ms 500
[17:33:50.555]  [00:01:33.329][silabs ]MATTER RX: 55 AA 01 00 99 E2 01 F0 6C 
[17:33:50.555]  [00:01:33.330][silabs ]payload: F0 
[17:33:50.555]  [00:01:33.330][silabs ]COM: OTAData request without offset, using state offset=36720
[17:33:50.556]  [00:01:33.330][silabs ]COM: spp_app_event_OTAData, req_offset=36720, read_len=240
[17:33:50.656]  [00:01:33.430][silabs ]MATTER TX: 55 AA 01 00 96 E2 F0 00 20 08 80 FF E7 01 98 41 1C 01 91 00 78 00 28 05 D0 FF E7 00 98 40 1C 69 46 
[17:33:50.660]  [00:01:33.430][silabs ]COM: CMD: 0xE2, SN: 0x0096, LEN: 248
[17:33:50.660]  
[17:33:50.660]  [00:01:33.430][silabs ]SPP: ack_timeout_ms 500
[17:33:51.004]  [00:01:33.779][silabs ]MATTER RX: 55 AA 01 00 9A E2 01 F0 6D 
[17:33:51.004]  [00:01:33.779][silabs ]payload: F0 
[17:33:51.004]  [00:01:33.779][silabs ]COM: OTAData request without offset, using state offset=36960
[17:33:51.006]  [00:01:33.779][silabs ]COM: spp_app_event_OTAData, req_offset=36960, read_len=240
[17:33:51.106]  [00:01:33.880][silabs ]MATTER TX: 55 AA 01 00 97 E2 F0 10 B5 88 B0 00 F0 9E F8 06 A9 00 20 08 70 FF E7 4B 49 00 20 18 22 00 F0 4F F9 
[17:33:51.110]  [00:01:33.880][silabs ]COM: CMD: 0xE2, SN: 0x0097, LEN: 248
[17:33:51.110]  
[17:33:51.110]  [00:01:33.880][silabs ]SPP: ack_timeout_ms 500
[17:33:51.454]  [00:01:34.228][silabs ]MATTER RX: 55 AA 01 00 9B E2 01 F0 6E 
[17:33:51.454]  [00:01:34.228][silabs ]payload: F0 
[17:33:51.454]  [00:01:34.229][silabs ]COM: OTAData request without offset, using state offset=37200
[17:33:51.455]  [00:01:34.229][silabs ]COM: spp_app_event_OTAData, req_offset=37200, read_len=240
[17:33:51.555]  [00:01:34.330][silabs ]MATTER TX: 55 AA 01 00 98 E2 F0 07 A8 00 78 40 B2 00 28 07 D1 FF E7 D5 48 80 88 01 21 09 02 88 42 15 D0 FF E7 
[17:33:51.560]  [00:01:34.330][silabs ]COM: CMD: 0xE2, SN: 0x0098, LEN: 248
[17:33:51.560]  
[17:33:51.560]  [00:01:34.330][silabs ]SPP: ack_timeout_ms 500
[17:33:51.904]  [00:01:34.678][silabs ]MATTER RX: 55 AA 01 00 9C E2 01 F0 6F 
[17:33:51.904]  [00:01:34.678][silabs ]payload: F0 
[17:33:51.904]  [00:01:34.678][silabs ]COM: OTAData request without offset, using state offset=37440
[17:33:51.906]  [00:01:34.678][silabs ]COM: spp_app_event_OTAData, req_offset=37440, read_len=240
[17:33:52.005]  [00:01:34.779][silabs ]MATTER TX: 55 AA 01 00 99 E2 F0 43 68 03 98 02 99 01 9A 98 47 00 90 68 46 00 78 40 B2 04 B0 80 BD C0 46 00 0A 
[17:33:52.010]  [00:01:34.779][silabs ]COM: CMD: 0xE2, SN: 0x0099, LEN: 248
[17:33:52.010]  
[17:33:52.010]  [00:01:34.779][silabs ]SPP: ack_timeout_ms 500
[17:33:52.353]  [00:01:35.127][silabs ]MATTER RX: 55 AA 01 00 9D E2 01 F0 70 
[17:33:52.353]  [00:01:35.127][silabs ]payload: F0 
[17:33:52.353]  [00:01:35.127][silabs ]COM: OTAData request without offset, using state offset=37680
[17:33:52.357]  [00:01:35.128][silabs ]COM: spp_app_event_OTAData, req_offset=37680, read_len=240
[17:33:52.456]  [00:01:35.229][silabs ]MATTER TX: 55 AA 01 00 9A E2 F0 00 78 81 00 7F 48 40 58 00 90 00 98 03 A9 FF F7 83 FE 03 98 1D 49 88 42 2E D1 
[17:33:52.460]  [00:01:35.229][silabs ]COM: CMD: 0xE2, SN: 0x009A, LEN: 248
[17:33:52.460]  
[17:33:52.460]  [00:01:35.229][silabs ]SPP: ack_timeout_ms 500
[17:33:52.803]  [00:01:35.577][silabs ]MATTER RX: 55 AA 01 00 9E E2 01 F0 71 
[17:33:52.803]  [00:01:35.578][silabs ]payload: F0 
[17:33:52.803]  [00:01:35.578][silabs ]COM: OTAData request without offset, using state offset=37920
[17:33:52.805]  [00:01:35.578][silabs ]COM: spp_app_event_OTAData, req_offset=37920, read_len=240
[17:33:52.904]  [00:01:35.678][silabs ]MATTER TX: 55 AA 01 00 9B E2 F0 DE E7 02 98 01 99 88 42 04 D9 FF E7 07 A9 FC 20 08 70 0B E0 02 98 00 1D 02 90 
[17:33:52.910]  [00:01:35.678][silabs ]COM: CMD: 0xE2, SN: 0x009B, LEN: 248
[17:33:52.910]  
[17:33:52.910]  [00:01:35.678][silabs ]SPP: ack_timeout_ms 500
[17:33:53.253]  [00:01:36.027][silabs ]MATTER RX: 55 AA 01 00 9F E2 01 F0 72 
[17:33:53.253]  [00:01:36.027][silabs ]payload: F0 
[17:33:53.253]  [00:01:36.027][silabs ]COM: OTAData request without offset, using state offset=38160
[17:33:53.256]  [00:01:36.027][silabs ]COM: spp_app_event_OTAData, req_offset=38160, read_len=240
[17:33:53.354]  [00:01:36.128][silabs ]MATTER TX: 55 AA 01 00 9C E2 F0 04 98 49 02 40 18 03 90 04 98 03 99 12 88 0A 9B 00 F0 0A F8 01 46 02 98 01 70 
[17:33:53.360]  [00:01:36.128][silabs ]COM: CMD: 0xE2, SN: 0x009C, LEN: 248
[17:33:53.360]  
[17:33:53.360]  [00:01:36.128][silabs ]SPP: ack_timeout_ms 500
[17:33:53.703]  [00:01:36.476][silabs ]MATTER RX: 55 AA 01 00 A0 E2 01 F0 73 
[17:33:53.703]  [00:01:36.477][silabs ]payload: F0 
[17:33:53.703]  [00:01:36.477][silabs ]COM: OTAData request without offset, using state offset=38400
[17:33:53.706]  [00:01:36.477][silabs ]COM: spp_app_event_OTAData, req_offset=38400, read_len=240
[17:33:53.804]  [00:01:36.578][silabs ]MATTER TX: 55 AA 01 00 9D E2 F0 41 43 49 48 40 18 00 90 00 98 80 88 00 28 11 D0 FF E7 00 99 88 88 40 1E 88 80 
[17:33:53.807]  [00:01:36.578][silabs ]COM: CMD: 0xE2, SN: 0x009D, LEN: 248
[17:33:53.807]  
[17:33:53.807]  [00:01:36.578][silabs ]SPP: ack_timeout_ms 500
[17:33:54.152]  [00:01:36.926][silabs ]MATTER RX: 55 AA 01 00 A1 E2 01 F0 74 
[17:33:54.152]  [00:01:36.926][silabs ]payload: F0 
[17:33:54.152]  [00:01:36.926][silabs ]COM: OTAData request without offset, using state offset=38640
[17:33:54.156]  [00:01:36.926][silabs ]COM: spp_app_event_OTAData, req_offset=38640, read_len=240
[17:33:54.254]  [00:01:37.027][silabs ]MATTER TX: 55 AA 01 00 9E E2 F0 FF E7 01 99 48 88 40 1C 48 80 80 B2 20 28 04 DB FF E7 01 99 00 20 48 80 FF E7 
[17:33:54.256]  [00:01:37.027][silabs ]COM: CMD: 0xE2, SN: 0x009E, LEN: 248
[17:33:54.256]  
[17:33:54.256]  [00:01:37.027][silabs ]SPP: ack_timeout_ms 500
[17:33:54.601]  [00:01:37.375][silabs ]MATTER RX: 55 AA 01 00 A2 E2 01 F0 75 
[17:33:54.601]  [00:01:37.375][silabs ]payload: F0 
[17:33:54.601]  [00:01:37.376][silabs ]COM: OTAData request without offset, using state offset=38880
[17:33:54.605]  [00:01:37.376][silabs ]COM: spp_app_event_OTAData, req_offset=38880, read_len=240
[17:33:54.703]  [00:01:37.477][silabs ]MATTER TX: 55 AA 01 00 9F E2 F0 0F 49 F8 F7 29 F8 F8 F7 D7 F8 01 46 01 A8 01 70 00 78 64 28 04 DB FF E7 01 A9 
[17:33:54.707]  [00:01:37.477][silabs ]COM: CMD: 0xE2, SN: 0x009F, LEN: 248
[17:33:54.707]  
[17:33:54.707]  [00:01:37.477][silabs ]SPP: ack_timeout_ms 500
[17:33:55.051]  [00:01:37.826][silabs ]MATTER RX: 55 AA 01 00 A3 E2 01 F0 76 
[17:33:55.051]  [00:01:37.826][silabs ]payload: F0 
[17:33:55.051]  [00:01:37.826][silabs ]COM: OTAData request without offset, using state offset=39120
[17:33:55.053]  [00:01:37.826][silabs ]COM: spp_app_event_OTAData, req_offset=39120, read_len=240
[17:33:55.152]  [00:01:37.926][silabs ]MATTER TX: 55 AA 01 00 A0 E2 F0 58 43 C9 68 89 1A F7 F7 41 F9 69 46 08 70 00 98 01 A9 08 70 FF E7 01 A8 00 78 
[17:33:55.156]  [00:01:37.926][silabs ]COM: CMD: 0xE2, SN: 0x00A0, LEN: 248
[17:33:55.156]  
[17:33:55.156]  [00:01:37.926][silabs ]SPP: ack_timeout_ms 500
[17:33:55.501]  [00:01:38.275][silabs ]MATTER RX: 55 AA 01 00 A4 E2 01 F0 77 
[17:33:55.501]  [00:01:38.275][silabs ]payload: F0 
[17:33:55.501]  [00:01:38.275][silabs ]COM: OTAData request without offset, using state offset=39360
[17:33:55.502]  [00:01:38.276][silabs ]COM: spp_app_event_OTAData, req_offset=39360, read_len=240
[17:33:55.602]  [00:01:38.376][silabs ]MATTER TX: 55 AA 01 00 A1 E2 F0 48 60 FF E7 03 99 C8 68 49 68 40 5C 02 99 00 9A 88 54 FF E7 FF E7 00 98 40 1C 
[17:33:55.606]  [00:01:38.376][silabs ]COM: CMD: 0xE2, SN: 0x00A1, LEN: 248
[17:33:55.606]  
[17:33:55.606]  [00:01:38.376][silabs ]SPP: ack_timeout_ms 500
[17:33:55.950]  [00:01:38.724][silabs ]MATTER RX: 55 AA 01 00 A5 E2 01 F0 78 
[17:33:55.950]  [00:01:38.725][silabs ]payload: F0 
[17:33:55.950]  [00:01:38.725][silabs ]COM: OTAData request without offset, using state offset=39600
[17:33:55.952]  [00:01:38.725][silabs ]COM: spp_app_event_OTAData, req_offset=39600, read_len=240
[17:33:56.052]  [00:01:38.827][silabs ]MATTER TX: 55 AA 01 00 A2 E2 F0 16 20 FA F7 35 F8 FF F7 E5 FF FF E7 08 48 00 78 00 07 00 28 0B D5 FF E7 05 49 
[17:33:56.056]  [00:01:38.827][silabs ]COM: CMD: 0xE2, SN: 0x00A2, LEN: 248
[17:33:56.056]  
[17:33:56.056]  [00:01:38.827][silabs ]SPP: ack_timeout_ms 500
[17:33:56.400]  [00:01:39.174][silabs ]MATTER RX: 55 AA 01 00 A6 E2 01 F0 79 
[17:33:56.400]  [00:01:39.174][silabs ]payload: F0 
[17:33:56.400]  [00:01:39.174][silabs ]COM: OTAData request without offset, using state offset=39840
[17:33:56.401]  [00:01:39.174][silabs ]COM: spp_app_event_OTAData, req_offset=39840, read_len=240
[17:33:56.501]  [00:01:39.275][silabs ]MATTER TX: 55 AA 01 00 A3 E2 F0 01 98 07 91 06 A9 02 91 08 80 05 92 04 AA 13 80 07 98 09 88 40 18 03 90 03 98 
[17:33:56.505]  [00:01:39.275][silabs ]COM: CMD: 0xE2, SN: 0x00A3, LEN: 248
[17:33:56.505]  
[17:33:56.505]  [00:01:39.275][silabs ]SPP: ack_timeout_ms 500
[17:33:56.850]  [00:01:39.624][silabs ]MATTER RX: 55 AA 01 00 A7 E2 01 F0 7A 
[17:33:56.850]  [00:01:39.625][silabs ]payload: F0 
[17:33:56.850]  [00:01:39.625][silabs ]COM: OTAData request without offset, using state offset=40080
[17:33:56.851]  [00:01:39.625][silabs ]COM: spp_app_event_OTAData, req_offset=40080, read_len=240
[17:33:56.951]  [00:01:39.725][silabs ]MATTER TX: 55 AA 01 00 A4 E2 F0 15 49 08 88 40 1E 08 80 04 E0 16 48 00 68 01 A9 08 70 FF E7 FF E7 12 48 00 68 
[17:33:56.955]  [00:01:39.725][silabs ]COM: CMD: 0xE2, SN: 0x00A4, LEN: 248
[17:33:56.955]  
[17:33:56.955]  [00:01:39.725][silabs ]SPP: ack_timeout_ms 500
[17:33:57.300]  [00:01:40.074][silabs ]MATTER RX: 55 AA 01 00 A8 E2 01 F0 7B 
[17:33:57.300]  [00:01:40.074][silabs ]payload: F0 
[17:33:57.300]  [00:01:40.074][silabs ]COM: OTAData request without offset, using state offset=40320
[17:33:57.301]  [00:01:40.074][silabs ]COM: spp_app_event_OTAData, req_offset=40320, read_len=240
[17:33:57.401]  [00:01:40.175][silabs ]MATTER TX: 55 AA 01 00 A5 E2 F0 FF E7 02 98 FE F7 44 FF 02 90 DC E7 FF E7 01 98 F6 F7 0E FE FF E7 04 B0 80 BD 
[17:33:57.405]  [00:01:40.175][silabs ]COM: CMD: 0xE2, SN: 0x00A5, LEN: 248
[17:33:57.405]  
[17:33:57.405]  [00:01:40.175][silabs ]SPP: ack_timeout_ms 500
[17:33:57.749]  [00:01:40.523][silabs ]MATTER RX: 55 AA 01 00 A9 E2 01 F0 7C 
[17:33:57.749]  [00:01:40.524][silabs ]payload: F0 
[17:33:57.749]  [00:01:40.524][silabs ]COM: OTAData request without offset, using state offset=40560
[17:33:57.751]  [00:01:40.524][silabs ]COM: spp_app_event_OTAData, req_offset=40560, read_len=240
[17:33:57.850]  [00:01:40.625][silabs ]MATTER TX: 55 AA 01 00 A6 E2 F0 01 A8 00 88 4F 28 0D DC FF E7 01 A8 00 88 01 01 08 48 41 18 00 20 48 71 FF E7 
[17:33:57.855]  [00:01:40.625][silabs ]COM: CMD: 0xE2, SN: 0x00A6, LEN: 248
[17:33:57.855]  
[17:33:57.855]  [00:01:40.625][silabs ]SPP: ack_timeout_ms 500
[17:33:58.199]  [00:01:40.973][silabs ]MATTER RX: 55 AA 01 00 AA E2 01 F0 7D 
[17:33:58.199]  [00:01:40.973][silabs ]payload: F0 
[17:33:58.199]  [00:01:40.973][silabs ]COM: OTAData request without offset, using state offset=40800
[17:33:58.200]  [00:01:40.973][silabs ]COM: spp_app_event_OTAData, req_offset=40800, read_len=240
[17:33:58.300]  [00:01:41.075][silabs ]MATTER TX: 55 AA 01 00 A7 E2 F0 01 A8 00 78 C1 00 08 48 40 18 41 68 05 48 88 47 06 E0 FF E7 FF E7 01 98 40 1C 
[17:33:58.305]  [00:01:41.075][silabs ]COM: CMD: 0xE2, SN: 0x00A7, LEN: 248
[17:33:58.305]  
[17:33:58.305]  [00:01:41.075][silabs ]SPP: ack_timeout_ms 500
[17:33:58.649]  [00:01:41.422][silabs ]MATTER RX: 55 AA 01 00 AB E2 01 F0 7E 
[17:33:58.649]  [00:01:41.422][silabs ]payload: F0 
[17:33:58.649]  [00:01:41.423][silabs ]COM: OTAData request without offset, using state offset=41040
[17:33:58.650]  [00:01:41.423][silabs ]COM: spp_app_event_OTAData, req_offset=41040, read_len=240
[17:33:58.750]  [00:01:41.524][silabs ]MATTER TX: 55 AA 01 00 A8 E2 F0 FF E7 80 BD 74 0E 00 20 A4 1D 04 40 14 1F 04 40 9C 0E 00 20 80 B5 14 20 F9 F7 
[17:33:58.755]  [00:01:41.524][silabs ]COM: CMD: 0xE2, SN: 0x00A8, LEN: 248
[17:33:58.755]  
[17:33:58.755]  [00:01:41.524][silabs ]SPP: ack_timeout_ms 500
[17:33:59.098]  [00:01:41.873][silabs ]MATTER RX: 55 AA 01 00 AC E2 01 F0 7F 
[17:33:59.098]  [00:01:41.873][silabs ]payload: F0 
[17:33:59.098]  [00:01:41.873][silabs ]COM: OTAData request without offset, using state offset=41280
[17:33:59.099]  [00:01:41.873][silabs ]COM: spp_app_event_OTAData, req_offset=41280, read_len=240
[17:33:59.198]  [00:01:41.973][silabs ]MATTER TX: 55 AA 01 00 A9 E2 F0 F9 F7 1E FD 0B 49 08 68 40 1C 08 60 0A 48 00 88 C0 07 00 28 07 D0 FF E7 08 48 
[17:33:59.204]  [00:01:41.973][silabs ]COM: CMD: 0xE2, SN: 0x00A9, LEN: 248
[17:33:59.204]  
[17:33:59.204]  [00:01:41.973][silabs ]SPP: ack_timeout_ms 500
[17:33:59.548]  [00:01:42.322][silabs ]MATTER RX: 55 AA 01 00 AD E2 01 F0 80 
[17:33:59.548]  [00:01:42.322][silabs ]payload: F0 
[17:33:59.548]  [00:01:42.323][silabs ]COM: OTAData request without offset, using state offset=41520
[17:33:59.552]  [00:01:42.323][silabs ]COM: spp_app_event_OTAData, req_offset=41520, read_len=240
[17:33:59.649]  [00:01:42.423][silabs ]MATTER TX: 55 AA 01 00 AA E2 F0 FF E7 0B 49 08 68 00 78 0A 4A 10 70 08 68 40 1C 08 60 06 49 08 88 40 1E 08 80 
[17:33:59.655]  [00:01:42.423][silabs ]COM: CMD: 0xE2, SN: 0x00AA, LEN: 248
[17:33:59.655]  
[17:33:59.655]  [00:01:42.423][silabs ]SPP: ack_timeout_ms 500
[17:33:59.998]  [00:01:42.772][silabs ]MATTER RX: 55 AA 01 00 AE E2 01 F0 81 
[17:33:59.998]  [00:01:42.772][silabs ]payload: F0 
[17:33:59.998]  [00:01:42.772][silabs ]COM: OTAData request without offset, using state offset=41760
[17:34:00.001]  [00:01:42.772][silabs ]COM: spp_app_event_OTAData, req_offset=41760, read_len=240
[17:34:00.100]  [00:01:42.874][silabs ]MATTER TX: 55 AA 01 00 AB E2 F0 EF FC 0A B0 10 BD C0 46 24 16 00 20 44 16 00 20 F8 B5 04 0C 8B B2 26 46 82 B2 
[17:34:00.105]  [00:01:42.874][silabs ]COM: CMD: 0xE2, SN: 0x00AB, LEN: 248
[17:34:00.105]  
[17:34:00.105]  [00:01:42.874][silabs ]SPP: ack_timeout_ms 500
[17:34:00.448]  [00:01:43.221][silabs ]MATTER RX: 55 AA 01 00 AF E2 01 F0 82 
[17:34:00.448]  [00:01:43.221][silabs ]payload: F0 
[17:34:00.448]  [00:01:43.222][silabs ]COM: OTAData request without offset, using state offset=42000
[17:34:00.451]  [00:01:43.222][silabs ]COM: spp_app_event_OTAData, req_offset=42000, read_len=240
[17:34:00.548]  [00:01:43.322][silabs ]MATTER TX: 55 AA 01 00 AC E2 F0 3A 46 B5 4B F6 F7 0C FE B4 4A B5 4B F6 F7 08 FE 61 60 20 60 00 20 C0 43 19 B0 
[17:34:00.552]  [00:01:43.322][silabs ]COM: CMD: 0xE2, SN: 0x00AC, LEN: 248
[17:34:00.552]  
[17:34:00.552]  [00:01:43.322][silabs ]SPP: ack_timeout_ms 500
[17:34:00.897]  [00:01:43.671][silabs ]MATTER RX: 55 AA 01 00 B0 E2 01 F0 83 
[17:34:00.897]  [00:01:43.671][silabs ]payload: F0 
[17:34:00.897]  [00:01:43.671][silabs ]COM: OTAData request without offset, using state offset=42240
[17:34:00.898]  [00:01:43.671][silabs ]COM: spp_app_event_OTAData, req_offset=42240, read_len=240
[17:34:00.998]  [00:01:43.772][silabs ]MATTER TX: 55 AA 01 00 AD E2 F0 6D 1C BD E7 09 98 00 28 09 DA 01 22 60 68 D2 07 50 40 60 60 0A 98 19 B0 40 42 
[17:34:01.002]  [00:01:43.772][silabs ]COM: CMD: 0xE2, SN: 0x00AD, LEN: 248
[17:34:01.002]  
[17:34:01.002]  [00:01:43.772][silabs ]SPP: ack_timeout_ms 500
[17:34:01.346]  [00:01:44.121][silabs ]MATTER RX: 55 AA 01 00 B1 E2 01 F0 84 
[17:34:01.346]  [00:01:44.122][silabs ]payload: F0 
[17:34:01.346]  [00:01:44.122][silabs ]COM: OTAData request without offset, using state offset=42480
[17:34:01.350]  [00:01:44.122][silabs ]COM: spp_app_event_OTAData, req_offset=42480, read_len=240
[17:34:01.448]  [00:01:44.222][silabs ]MATTER TX: 55 AA 01 00 AE E2 F0 80 0F 13 90 02 98 05 99 80 00 03 9E 04 9D 0B 91 F6 F7 C1 FF 07 46 30 46 08 91 
[17:34:01.452]  [00:01:44.222][silabs ]COM: CMD: 0xE2, SN: 0x00AE, LEN: 248
[17:34:01.452]  
[17:34:01.452]  [00:01:44.222][silabs ]SPP: ack_timeout_ms 500
[17:34:01.796]  [00:01:44.571][silabs ]MATTER RX: 55 AA 01 00 B2 E2 01 F0 85 
[17:34:01.796]  [00:01:44.571][silabs ]payload: F0 
[17:34:01.796]  [00:01:44.571][silabs ]COM: OTAData request without offset, using state offset=42720
[17:34:01.801]  [00:01:44.571][silabs ]COM: spp_app_event_OTAData, req_offset=42720, read_len=240
[17:34:01.898]  [00:01:44.672][silabs ]MATTER TX: 55 AA 01 00 AF E2 F0 00 00 40 54 31 63 62 1A 61 B4 D0 3D 73 70 03 2E 8A 19 A3 3B FB 21 39 41 83 C8 
[17:34:01.902]  [00:01:44.672][silabs ]COM: CMD: 0xE2, SN: 0x00AF, LEN: 248
[17:34:01.902]  
[17:34:01.902]  [00:01:44.672][silabs ]SPP: ack_timeout_ms 500
[17:34:02.246]  [00:01:45.020][silabs ]MATTER RX: 55 AA 01 00 B3 E2 01 F0 86 
[17:34:02.246]  [00:01:45.020][silabs ]payload: F0 
[17:34:02.246]  [00:01:45.021][silabs ]COM: OTAData request without offset, using state offset=42960
[17:34:02.249]  [00:01:45.021][silabs ]COM: spp_app_event_OTAData, req_offset=42960, read_len=240
[17:34:02.347]  [00:01:45.122][silabs ]MATTER TX: 55 AA 01 00 B0 E2 F0 B5 1A 00 24 22 46 2B 46 F6 F7 37 FC 06 46 01 91 22 46 2B 46 00 20 0A 49 F6 F7 
[17:34:02.350]  [00:01:45.122][silabs ]COM: CMD: 0xE2, SN: 0x00B0, LEN: 248
[17:34:02.350]  
[17:34:02.350]  [00:01:45.122][silabs ]SPP: ack_timeout_ms 500
[17:34:02.695]  [00:01:45.470][silabs ]MATTER RX: 55 AA 01 00 B4 E2 01 F0 87 
[17:34:02.695]  [00:01:45.470][silabs ]payload: F0 
[17:34:02.695]  [00:01:45.470][silabs ]COM: OTAData request without offset, using state offset=43200
[17:34:02.699]  [00:01:45.470][silabs ]COM: spp_app_event_OTAData, req_offset=43200, read_len=240
[17:34:02.797]  [00:01:45.571][silabs ]MATTER TX: 55 AA 01 00 B1 E2 F0 22 68 F6 F7 B5 FB F8 BD F0 B5 1F B4 05 46 48 00 0C 46 F9 21 40 08 89 05 86 B0 
[17:34:02.800]  [00:01:45.571][silabs ]COM: CMD: 0xE2, SN: 0x00B1, LEN: 248
[17:34:02.800]  
[17:34:02.800]  [00:01:45.571][silabs ]SPP: ack_timeout_ms 500
[17:34:03.145]  [00:01:45.919][silabs ]MATTER RX: 55 AA 01 00 B5 E2 01 F0 88 
[17:34:03.145]  [00:01:45.919][silabs ]payload: F0 
[17:34:03.145]  [00:01:45.919][silabs ]COM: OTAData request without offset, using state offset=43440
[17:34:03.150]  [00:01:45.920][silabs ]COM: spp_app_event_OTAData, req_offset=43440, read_len=240
[17:34:03.247]  [00:01:46.021][silabs ]MATTER TX: 55 AA 01 00 B2 E2 F0 55 55 C5 BF 10 B5 01 22 F7 F7 78 FF 10 BD 00 22 10 B5 13 46 10 46 11 46 F6 F7 
[17:34:03.251]  [00:01:46.021][silabs ]COM: CMD: 0xE2, SN: 0x00B2, LEN: 248
[17:34:03.251]  
[17:34:03.251]  [00:01:46.021][silabs ]SPP: ack_timeout_ms 500
[17:34:03.595]  [00:01:46.370][silabs ]MATTER RX: 55 AA 01 00 B6 E2 01 F0 89 
[17:34:03.595]  [00:01:46.370][silabs ]payload: F0 
[17:34:03.595]  [00:01:46.370][silabs ]COM: OTAData request without offset, using state offset=43680
[17:34:03.596]  [00:01:46.370][silabs ]COM: spp_app_event_OTAData, req_offset=43680, read_len=240
[17:34:03.696]  [00:01:46.470][silabs ]MATTER TX: 55 AA 01 00 B3 E2 F0 0F C8 FF F7 11 FF 07 B0 00 BD 02 A8 0F C8 FF F7 3B FE 07 B0 00 BD 00 90 02 A8 
[17:34:03.699]  [00:01:46.470][silabs ]COM: CMD: 0xE2, SN: 0x00B3, LEN: 248
[17:34:03.699]  
[17:34:03.699]  [00:01:46.470][silabs ]SPP: ack_timeout_ms 500
[17:34:04.044]  [00:01:46.819][silabs ]MATTER RX: 55 AA 01 00 B7 E2 01 F0 8A 
[17:34:04.044]  [00:01:46.819][silabs ]payload: F0 
[17:34:04.044]  [00:01:46.819][silabs ]COM: OTAData request without offset, using state offset=43920
[17:34:04.045]  [00:01:46.820][silabs ]COM: spp_app_event_OTAData, req_offset=43920, read_len=240
[17:34:04.146]  [00:01:46.920][silabs ]MATTER TX: 55 AA 01 00 B4 E2 F0 82 B0 00 90 72 B6 1A 49 10 20 08 60 19 49 F1 20 08 60 19 49 55 20 08 60 18 49 
[17:34:04.150]  [00:01:46.920][silabs ]COM: CMD: 0xE2, SN: 0x00B4, LEN: 248
[17:34:04.150]  
[17:34:04.150]  [00:01:46.920][silabs ]SPP: ack_timeout_ms 500
[17:34:04.495]  [00:01:47.268][silabs ]MATTER RX: 55 AA 01 00 B8 E2 01 F0 8B 
[17:34:04.495]  [00:01:47.269][silabs ]payload: F0 
[17:34:04.495]  [00:01:47.269][silabs ]COM: OTAData request without offset, using state offset=44160
[17:34:04.496]  [00:01:47.269][silabs ]COM: spp_app_event_OTAData, req_offset=44160, read_len=240
[17:34:04.595]  [00:01:47.370][silabs ]MATTER TX: 55 AA 01 00 B5 E2 F0 70 47 C0 46 20 00 02 40 04 00 02 40 08 00 02 40 00 00 02 40 80 B5 1F 20 F8 F7 
[17:34:04.599]  [00:01:47.370][silabs ]COM: CMD: 0xE2, SN: 0x00B5, LEN: 248
[17:34:04.599]  
[17:34:04.599]  [00:01:47.370][silabs ]SPP: ack_timeout_ms 500
[17:34:04.944]  [00:01:47.718][silabs ]MATTER RX: 55 AA 01 00 B9 E2 01 F0 8C 
[17:34:04.944]  [00:01:47.718][silabs ]payload: F0 
[17:34:04.944]  [00:01:47.718][silabs ]COM: OTAData request without offset, using state offset=44400
[17:34:04.945]  [00:01:47.718][silabs ]COM: spp_app_event_OTAData, req_offset=44400, read_len=240
[17:34:05.044]  [00:01:47.819][silabs ]MATTER TX: 55 AA 01 00 B6 E2 F0 00 20 08 80 FF E7 02 A8 00 88 3E 49 88 42 0E DC FF E7 04 98 41 1C 04 91 00 78 
[17:34:05.049]  [00:01:47.819][silabs ]COM: CMD: 0xE2, SN: 0x00B6, LEN: 248
[17:34:05.049]  
[17:34:05.049]  [00:01:47.819][silabs ]SPP: ack_timeout_ms 500
[17:34:05.393]  [00:01:48.167][silabs ]MATTER RX: 55 AA 01 00 BA E2 01 F0 8D 
[17:34:05.393]  [00:01:48.167][silabs ]payload: F0 
[17:34:05.393]  [00:01:48.168][silabs ]COM: OTAData request without offset, using state offset=44640
[17:34:05.395]  [00:01:48.168][silabs ]COM: spp_app_event_OTAData, req_offset=44640, read_len=240
[17:34:05.495]  [00:01:48.269][silabs ]MATTER TX: 55 AA 01 00 B7 E2 F0 7F B0 0F B0 10 BD C0 46 01 02 00 00 00 FE FF FF FF 01 00 00 FF 03 00 00 70 B5 
[17:34:05.499]  [00:01:48.269][silabs ]COM: CMD: 0xE2, SN: 0x00B7, LEN: 248
[17:34:05.499]  
[17:34:05.499]  [00:01:48.269][silabs ]SPP: ack_timeout_ms 500
[17:34:05.843]  [00:01:48.618][silabs ]MATTER RX: 55 AA 01 00 BB E2 01 F0 8E 
[17:34:05.843]  [00:01:48.618][silabs ]payload: F0 
[17:34:05.843]  [00:01:48.618][silabs ]COM: OTAData request without offset, using state offset=44880
[17:34:05.844]  [00:01:48.618][silabs ]COM: spp_app_event_OTAData, req_offset=44880, read_len=240
[17:34:05.944]  [00:01:48.718][silabs ]MATTER TX: 55 AA 01 00 B8 E2 F0 10 BD 00 BF 09 00 13 04 01 23 DB 05 02 00 0A 43 0D D4 DA 42 03 D4 9A 42 07 D4 
[17:34:05.949]  [00:01:48.718][silabs ]COM: CMD: 0xE2, SN: 0x00B8, LEN: 248
[17:34:05.949]  
[17:34:05.949]  [00:01:48.718][silabs ]SPP: ack_timeout_ms 500
[17:34:06.292]  [00:01:49.067][silabs ]MATTER RX: 55 AA 01 00 BC E2 01 F0 8F 
[17:34:06.292]  [00:01:49.067][silabs ]payload: F0 
[17:34:06.292]  [00:01:49.068][silabs ]COM: OTAData request without offset, using state offset=45120
[17:34:06.294]  [00:01:49.068][silabs ]COM: spp_app_event_OTAData, req_offset=45120, read_len=240
[17:34:06.394]  [00:01:49.168][silabs ]MATTER TX: 55 AA 01 00 B9 E2 F0 45 00 B5 42 06 D8 4D 00 B5 42 03 D8 D2 18 FF 2A 00 D0 E7 E7 00 48 70 BD 00 00 
[17:34:06.399]  [00:01:49.168][silabs ]COM: CMD: 0xE2, SN: 0x00B9, LEN: 248
[17:34:06.399]  
[17:34:06.399]  [00:01:49.168][silabs ]SPP: ack_timeout_ms 500
[17:34:06.742]  [00:01:49.517][silabs ]MATTER RX: 55 AA 01 00 BD E2 01 F0 90 
[17:34:06.742]  [00:01:49.517][silabs ]payload: F0 
[17:34:06.742]  [00:01:49.517][silabs ]COM: OTAData request without offset, using state offset=45360
[17:34:06.746]  [00:01:49.517][silabs ]COM: spp_app_event_OTAData, req_offset=45360, read_len=240
[17:34:06.845]  [00:01:49.619][silabs ]MATTER TX: 55 AA 01 00 BA E2 F0 78 44 84 46 03 BC 60 47 31 71 FF FF 03 B4 02 48 78 44 84 46 03 BC 60 47 99 73 
[17:34:06.850]  [00:01:49.619][silabs ]COM: CMD: 0xE2, SN: 0x00BA, LEN: 248
[17:34:06.850]  
[17:34:06.850]  [00:01:49.619][silabs ]SPP: ack_timeout_ms 500
[17:34:07.192]  [00:01:49.966][silabs ]MATTER RX: 55 AA 01 00 BE E2 01 F0 91 
[17:34:07.192]  [00:01:49.966][silabs ]payload: F0 
[17:34:07.192]  [00:01:49.967][silabs ]COM: OTAData request without offset, using state offset=45600
[17:34:07.193]  [00:01:49.967][silabs ]COM: spp_app_event_OTAData, req_offset=45600, read_len=76
[17:34:07.293]  [00:01:50.068][silabs ]MATTER TX: 55 AA 01 00 BB E2 F0 43 44 45 46 40 30 58 00 30 31 32 33 34 35 36 37 38 39 61 62 63 64 65 66 40 30 
[17:34:07.299]  [00:01:50.068][silabs ]COM: CMD: 0xE2, SN: 0x00BB, LEN: 248
[17:34:07.299]  
[17:34:07.299]  [00:01:50.068][silabs ]SPP: ack_timeout_ms 500
[17:34:07.642]  [00:01:50.416][silabs ]MATTER RX: 55 AA 01 00 BF E2 01 F0 92 
[17:34:07.642]  [00:01:50.416][silabs ]payload: F0 
[17:34:07.642]  [00:01:50.416][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:07.643]  [00:01:50.416][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:07.646]  [00:01:50.417][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:07.743]  [00:01:50.517][silabs ]MATTER TX: 55 AA 01 00 BC E2 F0 FF 97 F8 1F 0F 98 05 DE 8B 11 2F EF 1F 6D 0A 5A CF 7E 36 6D B7 09 CB 27 66 3F 
[17:34:07.746]  [00:01:50.517][silabs ]COM: CMD: 0xE2, SN: 0x00BC, LEN: 248
[17:34:07.746]  
[17:34:07.746]  [00:01:50.517][silabs ]SPP: ack_timeout_ms 500
[17:34:08.092]  [00:01:50.866][silabs ]MATTER RX: 55 AA 01 00 C0 E2 01 F0 93 
[17:34:08.092]  [00:01:50.866][silabs ]payload: F0 
[17:34:08.092]  [00:01:50.867][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:08.093]  [00:01:50.867][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:08.096]  [00:01:50.867][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:08.193]  [00:01:50.967][silabs ]MATTER TX: 55 AA 01 00 BD E2 F0 DC B5 A0 E2 3A 30 1F 97 FF FF FF FF B4 45 00 00 FD 25 A0 C8 E9 A3 C1 4F FF FF 
[17:34:08.196]  [00:01:50.967][silabs ]COM: CMD: 0xE2, SN: 0x00BD, LEN: 248
[17:34:08.196]  
[17:34:08.196]  [00:01:50.967][silabs ]SPP: ack_timeout_ms 500
[17:34:08.541]  [00:01:51.316][silabs ]MATTER RX: 55 AA 01 00 C1 E2 01 F0 94 
[17:34:08.541]  [00:01:51.316][silabs ]payload: F0 
[17:34:08.541]  [00:01:51.316][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:08.543]  [00:01:51.316][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:08.546]  [00:01:51.317][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:08.643]  [00:01:51.417][silabs ]MATTER TX: 55 AA 01 00 BE E2 F0 FF FF 00 00 35 5E 00 00 40 CE 00 00 75 59 00 00 BD 59 00 00 24 00 00 00 69 5A 
[17:34:08.649]  [00:01:51.417][silabs ]COM: CMD: 0xE2, SN: 0x00BE, LEN: 248
[17:34:08.649]  
[17:34:08.649]  [00:01:51.417][silabs ]SPP: ack_timeout_ms 500
[17:34:08.992]  [00:01:51.765][silabs ]MATTER RX: 55 AA 01 00 C2 E2 01 F0 95 
[17:34:08.992]  [00:01:51.765][silabs ]payload: F0 
[17:34:08.992]  [00:01:51.766][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:08.992]  [00:01:51.766][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:08.996]  [00:01:51.766][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:09.092]  [00:01:51.867][silabs ]MATTER TX: 55 AA 01 00 BF E2 F0 19 5E 00 00 19 00 00 00 E1 63 00 00 01 00 00 00 35 5E 00 00 FF FF 00 00 35 5E 
[17:34:09.096]  [00:01:51.867][silabs ]COM: CMD: 0xE2, SN: 0x00BF, LEN: 248
[17:34:09.096]  
[17:34:09.096]  [00:01:51.867][silabs ]SPP: ack_timeout_ms 500
[17:34:09.440]  [00:01:52.215][silabs ]MATTER RX: 55 AA 01 00 C3 E2 01 F0 96 
[17:34:09.440]  [00:01:52.215][silabs ]payload: F0 
[17:34:09.440]  [00:01:52.215][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:09.442]  [00:01:52.215][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:09.445]  [00:01:52.216][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:09.542]  [00:01:52.316][silabs ]MATTER TX: 55 AA 01 00 C0 E2 F0 72 64 20 66 61 75 6C 74 20 68 61 6E 64 6C 65 72 5D 0D 0A 00 52 30 20 3D 20 25 
[17:34:09.545]  [00:01:52.316][silabs ]COM: CMD: 0xE2, SN: 0x00C0, LEN: 248
[17:34:09.545]  
[17:34:09.545]  [00:01:52.316][silabs ]SPP: ack_timeout_ms 500
[17:34:09.890]  [00:01:52.665][silabs ]MATTER RX: 55 AA 01 00 C4 E2 01 F0 97 
[17:34:09.890]  [00:01:52.666][silabs ]payload: F0 
[17:34:09.890]  [00:01:52.666][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:09.892]  [00:01:52.666][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:09.895]  [00:01:52.666][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:09.992]  [00:01:52.766][silabs ]MATTER TX: 55 AA 01 00 C1 E2 F0 F8 FF FF FF 0C 00 00 00 0E 00 00 00 0F 00 00 00 2E 00 00 00 10 01 00 00 43 00 
[17:34:09.995]  [00:01:52.766][silabs ]COM: CMD: 0xE2, SN: 0x00C1, LEN: 248
[17:34:09.995]  
[17:34:09.995]  [00:01:52.766][silabs ]SPP: ack_timeout_ms 500
[17:34:10.340]  [00:01:53.115][silabs ]MATTER RX: 55 AA 01 00 C5 E2 01 4C F4 
[17:34:10.340]  [00:01:53.115][silabs ]payload: 4C 
[17:34:10.340]  [00:01:53.115][silabs ]COM: OTAData request without offset, using state offset=45676
[17:34:10.342]  [00:01:53.115][silabs ]COM: spp_app_event_OTAData, req_offset=45676, read_len=0
[17:34:10.345]  [00:01:53.116][silabs ]COM: Failed to read firmware data at offset 45676
[17:34:10.442]  [00:01:53.216][silabs ]MATTER TX: 55 AA 01 00 C2 E2 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
[17:34:10.446]  [00:01:53.216][silabs ]COM: CMD: 0xE2, SN: 0x00C2, LEN: 84
[17:34:10.446]  
[17:34:10.446]  [00:01:53.216][silabs ]SPP: ack_timeout_ms 500
[17:34:10.942]  [00:01:53.717][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:10.942]  [00:01:53.717][silabs ]MATTER TX: 55 AA 01 00 C2 E2 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
[17:34:10.944]  [00:01:53.718][silabs ]COM: CMD: 0xE2, SN: 0x00C2, LEN: 84
[17:34:10.949]  
[17:34:11.121]  [00:01:53.896][silabs ]MATTER RX: 55 AA 01 00 C6 E3 01 00 AA 
[17:34:11.121]  [00:01:53.896][silabs ]COM: MCU OTA result: Success
[17:34:11.121]  [00:01:53.897][silabs ]SPP: pending ack but allow new cmd process
[17:34:11.444]  [00:01:54.218][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:11.444]  [00:01:54.218][silabs ]MATTER TX: 55 AA 01 00 C2 E2 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
[17:34:11.445]  [00:01:54.218][silabs ]COM: CMD: 0xE2, SN: 0x00C2, LEN: 84
[17:34:11.449]  
[17:34:11.945]  [00:01:54.719][silabs ]SPP: re-sent reach to max
[17:34:11.945]  [00:01:54.720][silabs ]MATTER TX: 55 AA 01 00 C6 E3 00 A9 
[17:34:11.945]  [00:01:54.720][silabs ]COM: CMD: 0xE3, SN: 0x00C6, LEN: 8
[17:34:11.949]  
[17:34:11.949]  [00:01:54.720][silabs ]SPP: ack_timeout_ms 500
[17:34:12.446]  [00:01:55.220][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:12.446]  [00:01:55.220][silabs ]MATTER TX: 55 AA 01 00 C6 E3 00 A9 
[17:34:12.446]  [00:01:55.220][silabs ]COM: CMD: 0xE3, SN: 0x00C6, LEN: 8
[17:34:12.454]  
[17:34:12.945]  [00:01:55.720][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:12.945]  [00:01:55.720][silabs ]MATTER TX: 55 AA 01 00 C6 E3 00 A9 
[17:34:12.945]  [00:01:55.720][silabs ]COM: CMD: 0xE3, SN: 0x00C6, LEN: 8
[17:34:12.954]  
[17:34:13.449]  [00:01:56.220][silabs ]SPP: re-sent reach to max
[17:34:31.993]  \FF\D1"\04` R\88\93\104\AETbq\03\03p\02N\99!\00&:\00D\02	\04a@\02\04T\01\88\02\08\A4\01(\00D\00$A\08\0CB8\10\08\01\9C\00\C0\18\130K\80\00\00\E0 0?\00@\14\05\02`0 \04\10@X\00 
[17:34:32.000]  \0B\04\80&\10\82\00\0B\80\02"\82\00\16`\14\83\08\00H\00@\06\90@\00\03!A\00\00\00 \01\00\02\04 \80\A0\00 \01\08\10	\00@\00!\10\00\80\08@\04D\00@\00\A1\00 \00\10\00\00\B0\00\0C"\00"@\02\06\94$\00@\06\80\0C4\00\01\00\A0\00HT$\02\01IK@\00\19\00\00b\C0@\B0\80\08\84\10\0C\18\02\00E\08
[17:34:32.002]  \00\AAHD\04\01\B1\80\91\02P\00\08\96\00"\80l\0E\12\8A`\00t\000x\18\04\18\00\01\12J\A0 \0C\00\80\84$\10\18@\08\02\08\B1A@H@\00\DA\00\80\00\84@\08\00\01\00\06\00\01\00r\08\80\BC\A6\84\00 0@F	\01\80\00\90\80D\01A@d"\00\00\02\00\00H\00\84\A8\08 \84\00\88\84\01P\00
[17:34:32.004]  \04\10@\08$\82\00\031 (\00	\08\00\00\C8\00P\00
[17:34:32.004]   \90\00 \10\18P\80\10\00& \86\08@\08\00 \85\0C\80\82\14(@\00\01\84\05\82\81
[17:34:32.004]  <\00\00\00\90(`\10\81'\02\80\02\90!\08 \C4E\180\149\08\00\07\A8\84\19 \H\00)\16\96B9\9C\F2(G\A1 \A5J\11\15\02H	DZ\B2$\93\91Q\05\82\03&\94\10\02@"`\11\88\08\00\10\128\00\80\00@\00\00\00`J\00\04\16@\A0@\10\06\02@  B(\00\00H\02\80\00U(\80
[17:34:32.020]  @\81 $\11\10d\80\80\00\00\04\00\02\02\18)\08\82\84\18\1A#\81\82@\A0\02D \16\80\B0\02 @\00B\81\14\00\08\18\08\08\8C\12\01\04\10\00\08 \00\C0\02\03\0C\0C\C0\00\02\02\06\90\00\00( \00P\01\80\00\13\00"\A3\04\A1@\84\05\A0 \00@h(\1A\80\00\00\00\10>\00!\11B\00(\00@\18$\12\12\C2\07\10\06\A0d\04\80@H	U5\FE\D8\F9! \07\88\00\1A\85\15hM\10\95\84	\0C\00R\08\10\08!\00\05e\00\1A\E0\80\C4`@\90 \08\00\00`\00\00\08	\05\00@\00\00\02\00\10\01\00\004\00\80"0\11 H\10$\9A8@HK8@\08\00\12@\81\04\00\00@@\84a\01\00\13P\00\00\00\00$D @\00R\01\10\85\81@ \04 H\00\04\080\00\08\08@ \00\00\00\00\00\00\C0\12\00 \B0\10 PH`\0E\08
[17:34:32.050]  \00\01\8CP`\02\04\00"+\8C\9DIS\E8\12'\06\152\C0RfPVIY\C9\0C\1Ex\07\82 \C0\AB*\86U\1E\02\00)U\00\06\00D(\01\12\02\92H\80#\11\05$\E2 \9D\00\00\00\00@\FF\12\02\C0\14$$\04\00d\00\00P\00*@D@$P\81\08\C8\04\00`\00\01\10c\04\10\80\00\15\84\C0\03\E0@\C0LN\10`
[17:34:32.063]  8`\0Bx\08P\00\10\82!\00\08\80\11D\05\029\06\98\12,\00\C4\9B\06\00\01D\13\02\0E\07D	\04@ %\12\80\02$\10\00@\00\16\00A\00\01@\02\94\00\00\00\10\00\00\00\10\00\00\00\C0\80\10\00\02\98\00\00\10\00\00\14\01\00\00\0C"H	\00$!\81\08 \A8\88\08\00\10\89\05\02\02\08\00\01@\80
[17:34:32.071]  d  \00\12\00\10@P\00\00\08\01\90\00\10\00 @&!\80\01\85\00\80\0C\00\00\00a\04\10@\10`\18\04 \02\04\02@\F0\0C\A0\80\02\06\C0H\000\00\00\10\00d\00d\00\00E\00t\00\00\00\C0\11\18\16\80`x08\00\00\00\00@\E0\00\00\00\00\00\80\C0\06\00\00\00\00\C0\00\00\00\804 \00 \00\1C\80D\04@a(\CC\C0}\00\04$\0C\00\14\16\07\04C\DC\12\01\08\10\1A\0F[\16\08	F\86a\02 Q##\06\03D\19\16\06 \04\00s\03\03\C3\08\01\08E\13\00\01\01\18\04#\D0	\19!\04!\81\18\82\80\08Bd\1A\00\A0\02\9E\D1\08\00@\84\A2\04\03\80$D\07\00\1C\00\00\00\00\88\00\00\00\00#\10\800\A0 \14\01\98\10\00 \04\81\80P@\08\90@\01P8\80\00@\08\C1\00\00L\81\8C\00\02\00\19\01x\01,\C0\00\02\050\10\00\A8\08\02\00@hP\01\04\10\00\08\A0\E5\19`\86\08\00 D\03$@\00\04\00> 
[17:34:32.235]  Missed Logs: 25
[17:34:32.235]  [00:00:00.068][info  ][DL] Starting scheduler
[17:34:32.235]  [00:00:00.068][info  ][DL] ==================================================
[17:34:32.236]  [00:00:00.068][info  ][DL]  starting
[17:34:32.236]  [00:00:00.069][info  ][DL] ==================================================
[17:34:32.238]  [00:00:00.069][info  ][DL] Init CHIP Stack
[17:34:32.238]  [00:00:00.070][info  ][DL] Provision mode disabled
[17:34:32.238]  [00:00:00.070][info  ][DL] Initializing OpenThread stack
[17:34:32.239]  [00:00:00.072][info  ][DL] OpenThread ifconfig up and thread start
[17:34:32.239]  [00:00:00.072][info  ][DL] OpenThread started: OK
[17:34:32.243]  [00:00:00.107][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[17:34:32.243]  [00:00:00.107][info  ][DL] RAIL version:, v3.0.3-b0
[17:34:32.246]  [00:00:00.110][info  ][SVR] Current Software Version String: 0.0.3
[17:34:32.246]  [00:00:00.110][info  ][SVR] Current Software Version: 3
[17:34:32.248]  [00:00:00.112][info  ][DL] Device Configuration:
[17:34:32.248]  [00:00:00.114][info  ][DL]   Serial Number: 847227B0D1B99AF2
[17:34:32.248]  [00:00:00.114][info  ][DL]   Vendor Id: 5232 (0x1470)
[17:34:32.250]  [00:00:00.115][info  ][DL]   Product Id: 65281 (0xFF01)
[17:34:32.250]  [00:00:00.116][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:34:32.253]  [00:00:00.118][info  ][DL]   Product Name: Window Covering
[17:34:32.253]  [00:00:00.118][info  ][DL]   Hardware Version: 1
[17:34:32.253]  [00:00:00.118][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[17:34:32.253]  [00:00:00.119][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 3526 (0xDC6)
[17:34:32.255]  [00:00:00.119][info  ][DL]   Manufacturing Date: (not set)
[17:34:32.256]  [00:00:00.119][info  ][DL]   Device Type: 65535 (0xFFFF)
[17:34:32.256]  [00:00:00.120][info  ][SVR] SetupQRCode: [MT:K2CA04QO16GMBR1T310]
[17:34:32.256]  [00:00:00.120][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[17:34:32.258]  [00:00:00.120][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA04QO16GMBR1T310
[17:34:32.259]  [00:00:00.120][silabs ]Ver: 3 Btl: 0x03020002 Time:May 21 2026 19:24:17
[17:34:32.261]  [00:00:00.121][silabs ]Reset Reason: 0x00000000
[17:34:32.261]  
[17:34:32.261]  Missed Logs: 1
[17:34:32.261]  [00:00:00.121][silabs ]SetupQRCode: [MT:K2CA04QO16GMBR1T310]
[17:34:32.262]  [00:00:00.122][silabs ]COM: Init done
[17:34:32.262]  [00:00:00.123][silabs ]NWK: device has provisioned
[17:34:32.262]  
[17:34:32.262]  [00:00:00.123][silabs ]COM: notify network [Leave]
[17:34:32.264]  [00:00:00.123][silabs ]CLS: register device: dev 0x2002c92e endpoint 1 type 0 idx 1
[17:34:32.264]  [00:00:00.124][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:34:32.264]  [00:00:00.125][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:34:32.266]  [00:00:00.125][silabs ]app_mcu_dfu_init
[17:34:32.266]  [00:00:00.125][silabs ]bootloader_init() OK, calling cache_entire_metadata()
[17:34:32.266]  [00:00:00.125][silabs ]cache_entire_metadata: starting ONE verify pass...
[17:34:32.267]  [00:00:00.127][silabs ]cache_entire_metadata: initVerify OK, starting continueVerify loop...
[17:34:46.493]  [00:00:14.358][silabs ]cache_entire_metadata: continueVerify loop done, ret=515, iter=4731, bytes=45686
[17:34:46.493]  [00:00:14.359][silabs ]cache_entire_metadata: Header OK - magic=0x55AA, size=45676, ver=3.0.0
[17:34:46.501]  [00:00:14.366][silabs ]parse_metadata_header: Magic=0x55AA, Size=45676, Checksum=0x25, Version=3.0.0
[17:34:46.501]  [00:00:14.367][silabs ]cache_entire_metadata: DONE, cached 45686 bytes, header_valid=1
[17:34:46.503]  [00:00:14.367][silabs ]cache_entire_metadata() returned: true
[17:34:46.503]  [00:00:14.367][silabs ]app_mcu_dfu_init: done, cache_valid=1, header_valid=1
[17:34:46.504]  [00:00:14.367][silabs ]App Task started
[17:34:46.504]  [00:00:14.367][silabs ]MATTER TX: 55 AA 01 00 00 02 01 00 03 
[17:34:46.506]  [00:00:14.367][silabs ]COM: CMD: 0x02, SN: 0x0000, LEN: 9
[17:34:46.506]  
[17:34:46.506]  [00:00:14.368][silabs ]SPP: ack_timeout_ms 500
[17:34:46.509]  [00:00:14.368][silabs ]SPP: pending ack but allow new cmd process
[17:34:46.512]  matterCli> [00:00:14.386][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:34:46.521]  [00:00:14.386][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[17:34:46.522]  [00:00:14.386][silabs ]NWK: platform event type 32779
[17:34:46.522]  [00:00:14.387][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[17:34:46.524]  [00:00:14.388][silabs ]NWK: kThreadConnectivityChange,32769
[17:34:46.524]  [00:00:14.388][silabs ]NWK: Thread Established
[17:34:46.525]  [00:00:14.388][silabs ]COM: notify network [Joined]
[17:34:46.525]  [00:00:14.388][info  ][SVR] Scheduling OTA Requestor initialization
[17:34:46.528]  [00:00:14.388][info  ][SVR] Joining Multicast groups
[17:34:46.528]  [00:00:14.389][silabs ]SPP: pending ack but allow new cmd process
[17:34:46.532]  [00:00:14.395][silabs ]MATTER RX: 55 AA 01 00 00 02 00 02 
[17:34:46.532]  [00:00:14.396][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:34:46.632]  [00:00:14.497][silabs ]MATTER TX: 55 AA 01 00 01 01 00 02 
[17:34:46.632]  [00:00:14.497][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[17:34:46.632]  
[17:34:46.632]  [00:00:14.500][silabs ]SPP: ack_timeout_ms 500
[17:34:46.689]  [00:00:14.554][info  ][DL] SRP Client was started, detected server: fd11:9c64:dd37:b8c4:6397:7d5e:9e7b:227a
[17:34:46.689]  [00:00:14.554][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:34:46.690]  [00:00:14.555][silabs ]NWK: platform event type 32779
[17:34:46.690]  [00:00:14.556][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:34:46.694]  [00:00:14.556][silabs ]NWK: platform event type 32779
[17:34:46.704]  [00:00:14.570][silabs ]MATTER RX: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[17:34:46.706]  [00:00:14.570][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[17:34:46.706]  [00:00:14.570][silabs ]COM: Failed to extract version from product info
[17:34:46.707]  [00:00:14.571][silabs ]COM: Fallback extracted version: 3.0.0
[17:34:46.707]  [00:00:14.571][silabs ]Current MCU version set to: 3.0.0
[17:34:46.708]  [00:00:14.571][silabs ]COM: Boot OTA check - MCU: 3.0.0, Metadata: 3.0.0
[17:34:46.708]  [00:00:14.571][silabs ]COM: No MCU upgrade needed (metadata version not greater)
[17:34:46.805]  [00:00:14.671][silabs ]MATTER TX: 55 AA 01 00 02 02 01 01 06 
[17:34:46.805]  [00:00:14.671][silabs ]COM: CMD: 0x02, SN: 0x0002, LEN: 9
[17:34:46.805]  
[17:34:46.805]  [00:00:14.671][silabs ]SPP: ack_timeout_ms 500
[17:34:46.832]  [00:00:14.695][silabs ]MATTER RX: 55 AA 01 00 02 02 00 04 
[17:34:46.832]  [00:00:14.695][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:34:46.934]  [00:00:14.799][silabs ]MATTER RX: 55 AA 01 00 00 12 04 00 00 00 00 16 
[17:34:46.934]  [00:00:14.799][silabs ]WDC: report Active percent 0 dev_index 1
[17:34:46.936]  [00:00:14.799][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:34:46.936]  
[17:34:46.936]  [00:00:14.799][info  ][ZCL] Lift[1] Position Set: 10000
[17:34:46.937]  [00:00:14.800][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:34:46.937]  [00:00:14.800][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:34:46.939]  
[17:34:46.939]  [00:00:14.801][silabs ]SPP: ack_timeout_ms 500
[17:34:47.433]  [00:00:15.299][silabs ]MATTER RX: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:34:47.433]  [00:00:15.299][silabs ]WDC: report Active percent 0 dev_index 1
[17:34:47.435]  [00:00:15.299][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:34:47.435]  
[17:34:47.435]  [00:00:15.299][info  ][ZCL] Lift[1] Position Set: 10000
[17:34:47.436]  [00:00:15.300][silabs ]SPP: pending ack but allow new cmd process
[17:34:47.436]  [00:00:15.301][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:47.439]  [00:00:15.301][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:34:47.439]  [00:00:15.301][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:34:47.442]  
[17:34:47.630]  [00:00:15.495][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[17:34:47.630]  [00:00:15.496][silabs ]NWK: platform event type 32786
[17:34:47.631]  [00:00:15.496][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[17:34:47.631]  [00:00:15.496][info  ][SVR] Server initialization complete
[17:34:47.633]  [00:00:15.496][info  ][DIS] Updating services using commissioning mode 0
[17:34:47.633]  [00:00:15.496][info  ][DIS] Advertise operational node 62D8D539418A9054-00000000000008CA
[17:34:47.634]  [00:00:15.497][info  ][DL] advertising srp service: 62D8D539418A9054-00000000000008CA._matter._tcp
[17:34:47.635]  [00:00:15.497][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[17:34:47.635]  [00:00:15.497][silabs ]NWK: platform event type 32790
[17:34:47.643]  [00:00:15.507][info  ][IM] No subscriptions to resume
[17:34:47.933]  [00:00:15.798][silabs ]MATTER RX: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:34:47.933]  [00:00:15.798][silabs ]WDC: report Active percent 0 dev_index 1
[17:34:47.935]  [00:00:15.799][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:34:47.935]  
[17:34:47.935]  [00:00:15.799][info  ][ZCL] Lift[1] Position Set: 10000
[17:34:47.936]  [00:00:15.799][silabs ]SPP: pending ack but allow new cmd process
[17:34:47.936]  [00:00:15.802][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:47.937]  [00:00:15.802][silabs ]MATTER TX: 55 AA 01 00 00 12 00 12 
[17:34:47.937]  [00:00:15.802][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:34:47.942]  
[17:34:48.438]  [00:00:16.303][silabs ]SPP: re-sent reach to max
[17:34:48.438]  [00:00:16.304][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:48.438]  [00:00:16.304][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:48.442]  
[17:34:48.442]  [00:00:16.304][silabs ]SPP: ack_timeout_ms 500
[17:34:48.480]  [00:00:16.345][silabs ]MATTER RX: 55 AA 01 00 01 06 01 00 08 
[17:34:48.480]  [00:00:16.345][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0001,len:1
[17:34:48.481]  [00:00:16.345][silabs ]payload: 00 
[17:34:48.481]  [00:00:16.345][silabs ]PWR: report Battery Percent 0
[17:34:48.481]  
[17:34:48.481]  [00:00:16.346][silabs ]SPP: pending ack but allow new cmd process
[17:34:48.938]  [00:00:16.804][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:48.938]  [00:00:16.804][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:48.938]  [00:00:16.804][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:48.942]  
[17:34:48.979]  [00:00:16.844][silabs ]MATTER RX: 55 AA 01 01 01 06 01 00 09 
[17:34:48.979]  [00:00:16.845][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0101,len:1
[17:34:48.981]  [00:00:16.845][silabs ]payload: 00 
[17:34:48.981]  [00:00:16.845][silabs ]PWR: report Battery Percent 0
[17:34:48.981]  
[17:34:48.981]  [00:00:16.845][silabs ]SPP: pending ack but allow new cmd process
[17:34:49.438]  [00:00:17.304][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:49.438]  [00:00:17.304][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:49.438]  [00:00:17.304][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:49.441]  
[17:34:49.478]  [00:00:17.344][silabs ]MATTER RX: 55 AA 01 01 01 06 01 00 09 
[17:34:49.478]  [00:00:17.344][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0101,len:1
[17:34:49.479]  [00:00:17.344][silabs ]payload: 00 
[17:34:49.479]  [00:00:17.344][silabs ]PWR: report Battery Percent 0
[17:34:49.479]  
[17:34:49.479]  [00:00:17.345][silabs ]SPP: pending ack but allow new cmd process
[17:34:49.939]  [00:00:17.804][silabs ]SPP: re-sent reach to max
[17:34:49.939]  [00:00:17.805][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:49.939]  [00:00:17.805][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:49.943]  
[17:34:49.943]  [00:00:17.805][silabs ]SPP: ack_timeout_ms 500
[17:34:50.028]  [00:00:17.894][silabs ]MATTER RX: 55 AA 01 00 02 07 01 03 0D 
[17:34:50.028]  [00:00:17.894][silabs ]PWR: report Battery Charge State 3
[17:34:50.028]  
[17:34:50.028]  [00:00:17.894][silabs ]SPP: pending ack but allow new cmd process
[17:34:50.439]  [00:00:18.305][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:50.439]  [00:00:18.305][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:50.439]  [00:00:18.305][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:50.447]  
[17:34:50.528]  [00:00:18.393][silabs ]MATTER RX: 55 AA 01 01 02 07 01 03 0E 
[17:34:50.528]  [00:00:18.394][silabs ]PWR: report Battery Charge State 3
[17:34:50.528]  
[17:34:50.528]  [00:00:18.394][silabs ]SPP: pending ack but allow new cmd process
[17:34:50.632]  [00:00:18.498][info  ][SWU] Stopping the watchdog timer
[17:34:50.632]  [00:00:18.498][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[17:34:50.939]  [00:00:18.805][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:50.939]  [00:00:18.805][silabs ]MATTER TX: 55 AA 01 01 00 12 00 13 
[17:34:50.939]  [00:00:18.805][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:34:50.947]  
[17:34:51.027]  [00:00:18.893][silabs ]MATTER RX: 55 AA 01 01 02 07 01 03 0E 
[17:34:51.027]  [00:00:18.893][silabs ]PWR: report Battery Charge State 3
[17:34:51.027]  
[17:34:51.027]  [00:00:18.893][silabs ]SPP: pending ack but allow new cmd process
[17:34:51.440]  [00:00:19.305][silabs ]SPP: re-sent reach to max
[17:34:51.440]  [00:00:19.306][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:34:51.440]  [00:00:19.306][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:34:51.443]  
[17:34:51.443]  [00:00:19.306][silabs ]SPP: ack_timeout_ms 500
[17:34:51.576]  [00:00:19.442][silabs ]MATTER RX: 55 AA 01 00 03 08 01 01 0D 
[17:34:51.576]  [00:00:19.443][silabs ]PWR: report Battery Charge Level 1
[17:34:51.576]  
[17:34:51.576]  [00:00:19.443][silabs ]SPP: pending ack but allow new cmd process
[17:34:51.940]  [00:00:19.806][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:51.940]  [00:00:19.806][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:34:51.940]  [00:00:19.806][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:34:51.947]  
[17:34:52.076]  [00:00:19.942][silabs ]MATTER RX: 55 AA 01 01 03 08 01 01 0E 
[17:34:52.076]  [00:00:19.942][silabs ]PWR: report Battery Charge Level 1
[17:34:52.076]  
[17:34:52.076]  [00:00:19.943][silabs ]SPP: pending ack but allow new cmd process
[17:34:52.440]  [00:00:20.306][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:52.440]  [00:00:20.306][silabs ]MATTER TX: 55 AA 01 00 01 06 00 07 
[17:34:52.440]  [00:00:20.306][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:34:52.446]  
[17:34:52.576]  [00:00:20.442][silabs ]MATTER RX: 55 AA 01 01 03 08 01 01 0E 
[17:34:52.576]  [00:00:20.442][silabs ]PWR: report Battery Charge Level 1
[17:34:52.576]  
[17:34:52.576]  [00:00:20.442][silabs ]SPP: pending ack but allow new cmd process
[17:34:52.941]  [00:00:20.806][silabs ]SPP: re-sent reach to max
[17:34:52.941]  [00:00:20.807][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:52.941]  [00:00:20.807][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:52.944]  
[17:34:52.944]  [00:00:20.807][silabs ]SPP: ack_timeout_ms 500
[17:34:53.125]  [00:00:20.991][silabs ]MATTER RX: 55 AA 01 00 04 08 01 02 0F 
[17:34:53.125]  [00:00:20.992][silabs ]PWR: report Battery Charge Level 2
[17:34:53.125]  
[17:34:53.125]  [00:00:20.992][silabs ]SPP: pending ack but allow new cmd process
[17:34:53.441]  [00:00:21.307][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:53.441]  [00:00:21.307][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:53.441]  [00:00:21.307][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:53.447]  
[17:34:53.625]  [00:00:21.491][silabs ]MATTER RX: 55 AA 01 01 04 08 01 02 10 
[17:34:53.625]  [00:00:21.491][silabs ]SPP: tx_queue full!
[17:34:53.625]  [00:00:21.491][silabs ]PWR: report Battery Charge Level 2
[17:34:53.632]  
[17:34:53.941]  [00:00:21.807][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:53.941]  [00:00:21.807][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:53.941]  [00:00:21.807][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:53.946]  
[17:34:54.125]  [00:00:21.991][silabs ]MATTER RX: 55 AA 01 01 04 08 01 02 10 
[17:34:54.125]  [00:00:21.991][silabs ]SPP: tx_queue full!
[17:34:54.125]  [00:00:21.991][silabs ]PWR: report Battery Charge Level 2
[17:34:54.132]  
[17:34:54.442]  [00:00:22.307][silabs ]SPP: re-sent reach to max
[17:34:54.442]  [00:00:22.308][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:54.442]  [00:00:22.308][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:54.447]  
[17:34:54.447]  [00:00:22.308][silabs ]SPP: ack_timeout_ms 500
[17:34:54.942]  [00:00:22.808][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:54.942]  [00:00:22.808][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:54.942]  [00:00:22.808][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:54.946]  
[17:34:55.441]  [00:00:23.308][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:55.441]  [00:00:23.308][silabs ]MATTER TX: 55 AA 01 01 01 06 00 08 
[17:34:55.441]  [00:00:23.308][silabs ]COM: CMD: 0x06, SN: 0x0101, LEN: 8
[17:34:55.446]  
[17:34:55.942]  [00:00:23.808][silabs ]SPP: re-sent reach to max
[17:34:55.942]  [00:00:23.809][silabs ]MATTER TX: 55 AA 01 00 02 07 00 09 
[17:34:55.942]  [00:00:23.809][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:34:55.946]  
[17:34:55.946]  [00:00:23.809][silabs ]SPP: ack_timeout_ms 500
[17:34:56.443]  [00:00:24.309][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:56.443]  [00:00:24.309][silabs ]MATTER TX: 55 AA 01 00 02 07 00 09 
[17:34:56.443]  [00:00:24.309][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:34:56.446]  
[17:34:56.943]  [00:00:24.809][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:56.943]  [00:00:24.809][silabs ]MATTER TX: 55 AA 01 00 02 07 00 09 
[17:34:56.943]  [00:00:24.809][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:34:56.947]  
[17:34:57.444]  [00:00:25.309][silabs ]SPP: re-sent reach to max
[17:34:57.444]  [00:00:25.310][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:57.444]  [00:00:25.310][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:57.447]  
[17:34:57.447]  [00:00:25.310][silabs ]SPP: ack_timeout_ms 500
[17:34:57.943]  [00:00:25.810][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:57.943]  [00:00:25.810][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:57.943]  [00:00:25.810][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:57.952]  
[17:34:58.444]  [00:00:26.310][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:58.444]  [00:00:26.310][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:58.444]  [00:00:26.310][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:58.451]  
[17:34:58.944]  [00:00:26.810][silabs ]SPP: re-sent reach to max
[17:34:58.944]  [00:00:26.811][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:58.944]  [00:00:26.811][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:58.948]  
[17:34:58.948]  [00:00:26.811][silabs ]SPP: ack_timeout_ms 500
[17:34:59.445]  [00:00:27.311][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:34:59.445]  [00:00:27.311][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:59.445]  [00:00:27.311][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:59.451]  
[17:34:59.945]  [00:00:27.811][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:34:59.945]  [00:00:27.811][silabs ]MATTER TX: 55 AA 01 01 02 07 00 0A 
[17:34:59.945]  [00:00:27.811][silabs ]COM: CMD: 0x07, SN: 0x0102, LEN: 8
[17:34:59.952]  
[17:35:00.445]  [00:00:28.311][silabs ]SPP: re-sent reach to max
[17:35:00.445]  [00:00:28.312][silabs ]MATTER TX: 55 AA 01 00 03 08 00 0B 
[17:35:00.445]  [00:00:28.312][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:35:00.448]  
[17:35:00.448]  [00:00:28.312][silabs ]SPP: ack_timeout_ms 500
[17:35:00.945]  [00:00:28.812][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:35:00.945]  [00:00:28.812][silabs ]MATTER TX: 55 AA 01 00 03 08 00 0B 
[17:35:00.945]  [00:00:28.812][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:35:00.951]  
[17:35:01.446]  [00:00:29.312][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:35:01.446]  [00:00:29.312][silabs ]MATTER TX: 55 AA 01 00 03 08 00 0B 
[17:35:01.446]  [00:00:29.312][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:35:01.452]  
[17:35:01.946]  [00:00:29.812][silabs ]SPP: re-sent reach to max
[17:35:01.946]  [00:00:29.813][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:01.946]  [00:00:29.813][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:01.951]  
[17:35:01.951]  [00:00:29.813][silabs ]SPP: ack_timeout_ms 500
[17:35:02.446]  [00:00:30.313][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:35:02.446]  [00:00:30.313][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:02.446]  [00:00:30.313][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:02.451]  
[17:35:02.946]  [00:00:30.813][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:35:02.946]  [00:00:30.813][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:02.946]  [00:00:30.813][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:02.951]  
[17:35:03.447]  [00:00:31.313][silabs ]SPP: re-sent reach to max
[17:35:03.447]  [00:00:31.314][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:03.447]  [00:00:31.314][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:03.451]  
[17:35:03.451]  [00:00:31.314][silabs ]SPP: ack_timeout_ms 500
[17:35:03.947]  [00:00:31.814][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:35:03.947]  [00:00:31.814][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:03.947]  [00:00:31.814][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:03.951]  
[17:35:04.447]  [00:00:32.314][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:35:04.447]  [00:00:32.314][silabs ]MATTER TX: 55 AA 01 01 03 08 00 0C 
[17:35:04.447]  [00:00:32.314][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:35:04.451]  
[17:35:04.947]  [00:00:32.814][silabs ]SPP: re-sent reach to max
[17:35:04.947]  [00:00:32.815][silabs ]MATTER TX: 55 AA 01 00 04 08 00 0C 
[17:35:04.947]  [00:00:32.815][silabs ]COM: CMD: 0x08, SN: 0x0004, LEN: 8
[17:35:04.951]  
[17:35:04.951]  [00:00:32.815][silabs ]SPP: ack_timeout_ms 500
[17:35:05.448]  [00:00:33.315][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:35:05.448]  [00:00:33.315][silabs ]MATTER TX: 55 AA 01 00 04 08 00 0C 
[17:35:05.448]  [00:00:33.315][silabs ]COM: CMD: 0x08, SN: 0x0004, LEN: 8
[17:35:05.456]  
[17:35:05.948]  [00:00:33.815][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:35:05.948]  [00:00:33.815][silabs ]MATTER TX: 55 AA 01 00 04 08 00 0C 
[17:35:05.948]  [00:00:33.815][silabs ]COM: CMD: 0x08, SN: 0x0004, LEN: 8
[17:35:05.956]  
[17:35:06.451]  [00:00:34.315][silabs ]SPP: re-sent reach to max
```