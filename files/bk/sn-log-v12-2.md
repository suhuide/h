```c
[17:44:26.240]  [00:00:00.066][info  ][DL] Starting scheduler
[17:44:26.240]  [00:00:00.066][info  ][DL] ==================================================
[17:44:26.241]  [00:00:00.066][info  ][DL]  starting
[17:44:26.241]  [00:00:00.066][info  ][DL] ==================================================
[17:44:26.243]  [00:00:00.066][info  ][DL] Init CHIP Stack
[17:44:26.243]  [00:00:00.068][info  ][DL] Provision mode disabled
[17:44:26.243]  [00:00:00.068][info  ][DL] Initializing OpenThread stack
[17:44:26.245]  [00:00:00.069][info  ][DL] OpenThread ifconfig up and thread start
[17:44:26.245]  [00:00:00.070][info  ][DL] OpenThread started: OK
[17:44:26.247]  [00:00:00.104][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[17:44:26.247]  [00:00:00.104][info  ][DL] RAIL version:, v3.0.3-b0
[17:44:26.249]  [00:00:00.106][info  ][SVR] Current Software Version String: 0.0.12
[17:44:26.249]  [00:00:00.107][info  ][SVR] Current Software Version: 12
[17:44:26.250]  [00:00:00.107][info  ][DL] Device Configuration:
[17:44:26.250]  [00:00:00.108][info  ][DL]   Serial Number: 18F949E0A735AF92
[17:44:26.250]  [00:00:00.109][info  ][DL]   Vendor Id: 5232 (0x1470)
[17:44:26.254]  [00:00:00.110][info  ][DL]   Product Id: 65281 (0xFF01)
[17:44:26.254]  [00:00:00.110][info  ][DL]   Product Name: Window Covering
[17:44:26.256]  [00:00:00.113][info  ][DL]   Hardware Version: 1
[17:44:26.256]  [00:00:00.113][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[17:44:26.258]  [00:00:00.114][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:44:26.258]  [00:00:00.116][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 1064 (0x428)
[17:44:26.259]  [00:00:00.116][info  ][DL]   Manufacturing Date: 2026-10-19
[17:44:26.261]  [00:00:00.116][info  ][DL]   Device Type: 65535 (0xFFFF)
[17:44:26.261]  [00:00:00.117][info  ][SVR] SetupQRCode: [MT:K2CA0WSC00J19D1LX00]
[17:44:26.262]  [00:00:00.117][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[17:44:26.262]  [00:00:00.117][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0WSC00J19D1LX00
[17:44:26.265]  matterCli> [00:00:00.123][silabs ]CTM: Ver: 12 Build:  # Time:Oct 19 2026 16:35:17
[17:44:26.271]  [00:00:00.127][silabs ]CTM: Btl Ver: core: v3.2 user: v2
[17:44:26.276]  [00:00:00.132][silabs ]CTM: ResetCause: 0x00000003 (bit: WDOG0=0 LOCKUP=0 SYSREQ=0 PIN=1 POR=1)
[17:44:26.280]  [00:00:00.137][silabs ] Tx power 10dBm
[17:44:26.286]  [00:00:00.142][silabs ]SetupQRCode: [MT:K2CA0WSC00J19D1LX00]
[17:44:26.286]  [00:00:00.143][silabs ]COM: Init done
[17:44:26.286]  [00:00:00.143][silabs ]app_mcu_dfu_init: spawning async init thread
[17:44:26.287]  [00:00:00.144][silabs ]mcu_dfu_init_thread_func start
[17:44:26.287]  [00:00:00.144][silabs ]waiting for MCU version...
[17:44:26.289]  [00:00:00.144][silabs ]NWK: device has provisioned
[17:44:26.289]  
[17:44:26.289]  [00:00:00.144][silabs ]COM: notify network [Leave]
[17:44:26.290]  [00:00:00.144][silabs ]CLS: register device: dev 0x2002a226 endpoint 1 type 0 idx 1
[17:44:26.290]  [00:00:00.146][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:44:26.290]  [00:00:00.147][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:44:26.290]  [00:00:00.148][silabs ]App Task started
[17:44:26.293]  [00:00:00.148][silabs ]MATTER TX[0-8]: 55 AA 01 00 00 02 01 00 03 
[17:44:26.293]  [00:00:00.148][silabs ]COM: CMD: 0x02, SN: 0x0000, LEN: 9
[17:44:26.295]  
[17:44:26.295]  [00:00:00.148][silabs ]SPP: ack_timeout_ms 500
[17:44:26.295]  [00:00:00.149][silabs ]SPP: pending ack but allow new cmd process
[17:44:26.315]  [00:00:00.170][silabs ]MATTER RX[0-7]: 55 AA 01 00 00 02 00 02 
[17:44:26.315]  [00:00:00.170][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:44:26.413]  [00:00:00.271][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[17:44:26.413]  [00:00:00.271][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[17:44:26.413]  
[17:44:26.413]  [00:00:00.271][silabs ]SPP: ack_timeout_ms 500
[17:44:26.488]  [00:00:00.345][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 31 2E 32 2E 36 7D 99 
[17:44:26.490]  [00:00:00.345][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"1.2.6}
[17:44:26.490]  [00:00:00.346][silabs ]COM: Failed to extract version from product info
[17:44:26.491]  [00:00:00.346][silabs ]COM: Fallback extracted version: 1.2.6
[17:44:26.491]  [00:00:00.346][silabs ]Current MCU version set to: 1.2.6
[17:44:26.504]  [00:00:00.361][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:44:26.504]  [00:00:00.361][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[17:44:26.505]  [00:00:00.362][silabs ]NWK: platform event type 32779
[17:44:26.505]  [00:00:00.363][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[17:44:26.507]  [00:00:00.363][silabs ]NWK: kThreadConnectivityChange,32769
[17:44:26.507]  [00:00:00.363][silabs ]NWK: Thread Established
[17:44:26.508]  [00:00:00.363][silabs ]COM: notify network [Joined]
[17:44:26.508]  [00:00:00.363][info  ][SVR] Scheduling OTA Requestor initialization
[17:44:26.511]  [00:00:00.363][info  ][SVR] Joining Multicast groups
[17:44:26.582]  [00:00:00.438][silabs ]got MCU version 1.2.6
[17:44:26.582]  [00:00:00.438][silabs ]mcu_dfu: init done, waiting for Matter OTA trigger...
[17:44:26.589]  [00:00:00.446][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 01 00 03 
[17:44:26.589]  [00:00:00.446][silabs ]COM: CMD: 0x01, SN: 0x0002, LEN: 8
[17:44:26.589]  
[17:44:26.589]  [00:00:00.446][silabs ]SPP: ack_timeout_ms 500
[17:44:26.638]  [00:00:00.495][info  ][DL] SRP Client was started, detected server: fd73:b61e:a621:d88a:a909:9947:78dc:224d
[17:44:26.638]  [00:00:00.495][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:44:26.639]  [00:00:00.495][silabs ]NWK: platform event type 32779
[17:44:26.639]  [00:00:00.497][silabs ]MATTER RX[0-31]: 55 AA 01 00 02 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 31 2E 32 2E 36 7D 9A 
[17:44:26.640]  [00:00:00.497][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:44:26.642]  [00:00:00.497][silabs ]NWK: platform event type 32779
[17:44:26.642]  [00:00:00.498][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"1.2.6}
[17:44:26.643]  [00:00:00.498][silabs ]COM: Failed to extract version from product info
[17:44:26.644]  [00:00:00.498][silabs ]COM: Fallback extracted version: 1.2.6
[17:44:26.644]  [00:00:00.499][silabs ]Current MCU version set to: 1.2.6
[17:44:26.742]  [00:00:00.599][silabs ]MATTER TX[0-8]: 55 AA 01 00 03 02 01 01 07 
[17:44:26.742]  [00:00:00.600][silabs ]COM: CMD: 0x02, SN: 0x0003, LEN: 9
[17:44:26.742]  
[17:44:26.745]  [00:00:00.600][silabs ]SPP: ack_timeout_ms 500
[17:44:26.813]  [00:00:00.670][silabs ]MATTER RX[0-7]: 55 AA 01 00 03 02 00 05 
[17:44:26.813]  [00:00:00.670][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:44:26.918]  [00:00:00.775][silabs ]MATTER RX[0-11]: 55 AA 01 00 00 12 04 00 00 00 47 5D 
[17:44:26.918]  [00:00:00.776][silabs ]MATTER TX[0-7]: 55 AA 01 00 00 12 00 12 
[17:44:26.920]  [00:00:00.776][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:44:26.920]  
[17:44:26.920]  [00:00:00.776][silabs ]WDC: report Active percent 71 dev_index 1
[17:44:26.921]  [00:00:00.776][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2900
[17:44:26.921]  
[17:44:26.921]  [00:00:00.777][info  ][ZCL] Lift[1] Position Set: 2900
[17:44:26.924]  [00:00:00.777][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:44:27.334]  [00:00:01.190][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[17:44:27.334]  [00:00:01.191][silabs ]NWK: platform event type 32786
[17:44:27.335]  [00:00:01.191][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[17:44:27.335]  [00:00:01.191][info  ][SVR] Server initialization complete
[17:44:27.336]  [00:00:01.191][info  ][DIS] Updating services using commissioning mode 0
[17:44:27.336]  [00:00:01.191][info  ][DIS] Advertise operational node 52F66E6CB259E4E8-00000000000008D0
[17:44:27.338]  [00:00:01.192][info  ][DL] advertising srp service: 52F66E6CB259E4E8-00000000000008D0._matter._tcp
[17:44:27.340]  [00:00:01.192][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[17:44:27.340]  [00:00:01.192][silabs ]NWK: platform event type 32790
[17:44:27.345]  [00:00:01.202][info  ][IM] No subscriptions to resume
[17:44:27.419]  [00:00:01.276][silabs ]MATTER RX[0-11]: 55 AA 01 01 00 12 04 00 00 00 47 5E 
[17:44:27.419]  [00:00:01.276][silabs ]MATTER TX[0-7]: 55 AA 01 01 00 12 00 13 
[17:44:27.420]  [00:00:01.277][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:44:27.420]  
[17:44:27.420]  [00:00:01.277][silabs ]WDC: report Active percent 71 dev_index 1
[17:44:27.421]  [00:00:01.277][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2900
[17:44:27.421]  
[17:44:27.421]  [00:00:01.277][info  ][ZCL] Lift[1] Position Set: 2900
[17:44:27.425]  [00:00:01.277][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:44:27.920]  [00:00:01.777][silabs ]MATTER RX[0-11]: 55 AA 01 01 00 12 04 00 00 00 47 5E 
[17:44:27.920]  [00:00:01.777][silabs ]MATTER TX[0-7]: 55 AA 01 01 00 12 00 13 
[17:44:27.921]  [00:00:01.777][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:44:27.921]  
[17:44:27.921]  [00:00:01.777][silabs ]WDC: report Active percent 71 dev_index 1
[17:44:27.922]  [00:00:01.778][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2900
[17:44:27.922]  
[17:44:27.922]  [00:00:01.778][info  ][ZCL] Lift[1] Position Set: 2900
[17:44:27.925]  [00:00:01.778][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:44:28.467]  [00:00:02.324][silabs ]MATTER RX[0-8]: 55 AA 01 00 01 06 01 64 6C 
[17:44:28.467]  [00:00:02.325][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0001,len:1
[17:44:28.469]  [00:00:02.325][silabs ]payload[0-0]: 64 
[17:44:28.469]  [00:00:02.325][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 06 00 07 
[17:44:28.469]  [00:00:02.325][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:44:28.471]  
[17:44:28.471]  [00:00:02.326][silabs ]PWR: report Battery Percent 100
[17:44:28.475]  
[17:44:28.567]  [00:00:02.424][silabs ]MATTER RX[0-8]: 55 AA 01 00 02 07 01 03 0D 
[17:44:28.567]  [00:00:02.424][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 07 00 09 
[17:44:28.570]  [00:00:02.424][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:44:28.570]  
[17:44:28.570]  [00:00:02.425][silabs ]PWR: report Battery Charge State 3
[17:44:28.574]  
[17:44:28.669]  [00:00:02.524][silabs ]MATTER RX[0-8]: 55 AA 01 00 03 08 01 00 0C 
[17:44:28.669]  [00:00:02.525][silabs ]MATTER TX[0-7]: 55 AA 01 00 03 08 00 0B 
[17:44:28.671]  [00:00:02.525][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:44:28.671]  
[17:44:28.671]  [00:00:02.525][silabs ]PWR: report Battery Charge Level 0
[17:44:28.671]  
[17:44:29.168]  [00:00:03.025][silabs ]MATTER RX[0-8]: 55 AA 01 01 03 08 01 00 0D 
[17:44:29.168]  [00:00:03.025][silabs ]MATTER TX[0-7]: 55 AA 01 01 03 08 00 0C 
[17:44:29.170]  [00:00:03.026][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:44:29.170]  
[17:44:29.170]  [00:00:03.026][silabs ]PWR: report Battery Charge Level 0
[17:44:29.174]  
[17:44:30.336]  [00:00:04.193][info  ][SWU] Stopping the watchdog timer
[17:44:30.336]  [00:00:04.193][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[17:44:44.101]  [00:00:17.958][silabs ]MATTER RX[0-8]: 55 AA 01 00 04 06 01 63 6E 
[17:44:44.101]  [00:00:17.958][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0004,len:1
[17:44:44.103]  [00:00:17.958][silabs ]payload[0-0]: 63 
[17:44:44.103]  [00:00:17.958][silabs ]MATTER TX[0-7]: 55 AA 01 00 04 06 00 0A 
[17:44:44.103]  [00:00:17.959][silabs ]COM: CMD: 0x06, SN: 0x0004, LEN: 8
[17:44:44.104]  
[17:44:44.104]  [00:00:17.959][silabs ]PWR: report Battery Percent 99
[17:44:44.108]  
[17:44:44.805]  [00:00:18.663][silabs ]MATTER RX[0-11]: 55 AA 01 00 05 12 04 00 00 00 54 6F 
[17:44:44.805]  [00:00:18.663][silabs ]MATTER TX[0-7]: 55 AA 01 00 05 12 00 17 
[17:44:44.806]  [00:00:18.663][silabs ]COM: CMD: 0x12, SN: 0x0005, LEN: 8
[17:44:44.806]  
[17:44:44.806]  [00:00:18.663][silabs ]WDC: report Active percent 84 dev_index 1
[17:44:44.808]  [00:00:18.664][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1600
[17:44:44.808]  
[17:44:44.808]  [00:00:18.664][info  ][ZCL] Lift[1] Position Set: 1600
[17:44:44.809]  [00:00:18.664][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:44:45.305]  [00:00:19.163][silabs ]MATTER RX[0-11]: 55 AA 01 01 05 12 04 00 00 00 54 70 
[17:44:45.305]  [00:00:19.164][silabs ]MATTER TX[0-7]: 55 AA 01 01 05 12 00 18 
[17:44:45.307]  [00:00:19.164][silabs ]COM: CMD: 0x12, SN: 0x0105, LEN: 8
[17:44:45.307]  
[17:44:45.307]  [00:00:19.164][silabs ]WDC: report Active percent 84 dev_index 1
[17:44:45.308]  [00:00:19.164][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1600
[17:44:45.308]  
[17:44:45.308]  [00:00:19.165][info  ][ZCL] Lift[1] Position Set: 1600
[17:44:45.311]  [00:00:19.165][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:45:46.098]  [00:01:19.958][silabs ]MATTER RX[0-11]: 55 AA 01 00 06 12 04 00 00 00 60 7C 
[17:45:46.098]  [00:01:19.959][silabs ]MATTER TX[0-7]: 55 AA 01 00 06 12 00 18 
[17:45:46.100]  [00:01:19.959][silabs ]COM: CMD: 0x12, SN: 0x0006, LEN: 8
[17:45:46.100]  
[17:45:46.100]  [00:01:19.959][silabs ]WDC: report Active percent 96 dev_index 1
[17:45:46.101]  [00:01:19.959][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 400
[17:45:46.101]  
[17:45:46.101]  [00:01:19.960][info  ][ZCL] Lift[1] Position Set: 400
[17:45:46.103]  [00:01:19.960][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:45:46.599]  [00:01:20.459][silabs ]MATTER RX[0-11]: 55 AA 01 01 06 12 04 00 00 00 60 7D 
[17:45:46.599]  [00:01:20.459][silabs ]MATTER TX[0-7]: 55 AA 01 01 06 12 00 19 
[17:45:46.600]  [00:01:20.459][silabs ]COM: CMD: 0x12, SN: 0x0106, LEN: 8
[17:45:46.600]  
[17:45:46.600]  [00:01:20.460][silabs ]WDC: report Active percent 96 dev_index 1
[17:45:46.602]  [00:01:20.460][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 400
[17:45:46.602]  
[17:45:46.602]  [00:01:20.460][info  ][ZCL] Lift[1] Position Set: 400
[17:45:46.605]  [00:01:20.460][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:04.216]  [00:01:38.078][info  ][EM] >>> [E:44400r S:0 M:9630211] (U) Msg RX from 0:4DB4BB8A6C3955A7 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[17:46:04.219]  [00:01:38.079][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[17:46:04.220]  [00:01:38.079][info  ][EM] <<< [E:44400r S:0 M:67243587 (Ack:9630211)] (U) Msg TX from 0000000000000000 to 0:4DB4BB8A6C3955A7 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:34045] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:04.221]  [00:01:38.080][info  ][SC] Received Sigma1 msg
[17:46:04.229]  [00:01:38.088][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008D0
[17:46:04.258]  [00:01:38.119][info  ][EM] <<< [E:44400r S:0 M:67243588 (Ack:9630211)] (U) Msg TX from 0000000000000000 to 0:4DB4BB8A6C3955A7 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:34045] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[17:46:04.260]  [00:01:38.120][info  ][EM] ??1 [E:44400r S:0 M:67243588] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3375ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:04.264]  [00:01:38.121][info  ][SC] Sent Sigma2 msg
[17:46:04.902]  [00:01:38.763][info  ][EM] >>> [E:44400r S:0 M:9630212 (Ack:67243588)] (U) Msg RX from 0:4DB4BB8A6C3955A7 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[17:46:04.903]  [00:01:38.764][info  ][EM] <<< [E:44400r S:0 M:67243589 (Ack:9630212)] (U) Msg TX from 0000000000000000 to 0:4DB4BB8A6C3955A7 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:34045] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:04.907]  [00:01:38.764][info  ][SC] Received Sigma3 msg
[17:46:04.953]  [00:01:38.814][info  ][EM] <<< [E:44400r S:0 M:67243590 (Ack:9630212)] (U) Msg TX from 0000000000000000 to 0:4DB4BB8A6C3955A7 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:34045] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[17:46:04.954]  [00:01:38.815][info  ][EM] ??1 [E:44400r S:0 M:67243590] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3352ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:04.957]  [00:01:38.818][info  ][SC] SecureSession[0x20006d50, LSID:13918]: State change 'kEstablishing' --> 'kActive'
[17:46:04.958]  [00:01:38.818][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[17:46:04.958]  [00:01:38.819][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[17:46:04.961]  [00:01:38.819][silabs ]NWK: platform event type 32792
[17:46:05.511]  [00:01:39.372][info  ][EM] >>> [E:44401r S:13918 M:209289452] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0001:08 (IM:InvokeCommandRequest) (B:64)
[17:46:05.514]  [00:01:39.374][info  ][ZCL] GoToLiftPercentage 1000 command received
[17:46:05.514]  [00:01:39.376][info  ][EM] <<< [E:44401r S:13918 M:109349185 (Ack:209289452)] (S) Msg TX from 00000000000008D0 to 1:000000000001B669 [E4E8] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:34045] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[17:46:05.517]  [00:01:39.376][info  ][EM] ??1 [E:44401r S:13918 M:109349185] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3342ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:05.521]  [00:01:39.377][silabs ]EP[1] startup coalesce: defer TargetPosition 1000
[17:46:05.543]  [00:01:39.404][info  ][EM] >>> [E:44400r S:0 M:9630213 (Ack:67243590)] (U) Msg RX from 0:4DB4BB8A6C3955A7 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:06.071]  [00:01:39.932][info  ][EM] >>> [E:44401r S:13918 M:209289453 (Ack:109349185)] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[17:46:07.517]  [00:01:41.378][silabs ]WDC: EP[1] update operational status to Closed
[17:46:07.517]  
[17:46:07.517]  [00:01:41.378][info  ][ZCL] Lift[1] Position Set: 500
[17:46:07.517]  [00:01:41.378][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:07.520]  [00:01:41.380][silabs ]EP[1] startup flush: send deferred TargetPosition 90
[17:46:07.520]  [00:01:41.381][silabs ]MATTER TX[0-11]: 55 AA 01 00 04 11 04 00 00 01 5A 74 
[17:46:07.520]  [00:01:41.381][silabs ]COM: CMD: 0x11, SN: 0x0004, LEN: 12
[17:46:07.524]  
[17:46:07.524]  [00:01:41.381][silabs ]SPP: ack_timeout_ms 500
[17:46:08.021]  [00:01:41.882][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:46:08.021]  [00:01:41.882][silabs ]MATTER TX[0-11]: 55 AA 01 00 04 11 04 00 00 01 5A 74 
[17:46:08.024]  [00:01:41.882][silabs ]COM: CMD: 0x11, SN: 0x0004, LEN: 12
[17:46:08.024]  
[17:46:08.090]  [00:01:41.952][silabs ]MATTER RX[0-11]: 55 AA 01 00 04 11 04 00 00 01 5A 74 
[17:46:08.090]  [00:01:41.952][silabs ]COM: MCU TX spp_app_event_CurtainPercentCtrl (echo, sn:0x0004)
[17:46:11.195]  [00:01:45.056][silabs ]MATTER RX[0-11]: 55 AA 01 00 07 12 04 00 00 00 5A 77 
[17:46:11.195]  [00:01:45.056][silabs ]MATTER TX[0-7]: 55 AA 01 00 07 12 00 19 
[17:46:11.196]  [00:01:45.056][silabs ]COM: CMD: 0x12, SN: 0x0007, LEN: 8
[17:46:11.196]  
[17:46:11.196]  [00:01:45.056][silabs ]WDC: report Active percent 90 dev_index 1
[17:46:11.197]  [00:01:45.057][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1000
[17:46:11.197]  
[17:46:11.197]  [00:01:45.057][info  ][ZCL] Lift[1] Position Set: 1000
[17:46:11.200]  [00:01:45.057][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:11.695]  [00:01:45.556][silabs ]MATTER RX[0-11]: 55 AA 01 01 07 12 04 00 00 00 5A 78 
[17:46:11.695]  [00:01:45.557][silabs ]MATTER TX[0-7]: 55 AA 01 01 07 12 00 1A 
[17:46:11.696]  [00:01:45.557][silabs ]COM: CMD: 0x12, SN: 0x0107, LEN: 8
[17:46:11.696]  
[17:46:11.696]  [00:01:45.557][silabs ]WDC: report Active percent 90 dev_index 1
[17:46:11.698]  [00:01:45.557][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1000
[17:46:11.698]  
[17:46:11.698]  [00:01:45.557][info  ][ZCL] Lift[1] Position Set: 1000
[17:46:11.700]  [00:01:45.557][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:16.120]  [00:01:49.981][info  ][EM] >>> [E:4162r S:0 M:1854113] (U) Msg RX from 0:C1821BCEF2BF91BC [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[17:46:16.121]  [00:01:49.982][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[17:46:16.123]  [00:01:49.983][info  ][EM] <<< [E:4162r S:0 M:67243591 (Ack:1854113)] (U) Msg TX from 0000000000000000 to 0:C1821BCEF2BF91BC [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:48679] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:16.124]  [00:01:49.983][info  ][SC] Received Sigma1 msg
[17:46:16.134]  [00:01:49.992][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008D0
[17:46:16.155]  [00:01:50.016][info  ][EM] <<< [E:4162r S:0 M:67243592 (Ack:1854113)] (U) Msg TX from 0000000000000000 to 0:C1821BCEF2BF91BC [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:48679] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[17:46:16.156]  [00:01:50.017][info  ][EM] ??1 [E:4162r S:0 M:67243592] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3382ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:16.160]  [00:01:50.017][info  ][SC] Sent Sigma2 msg
[17:46:16.854]  [00:01:50.715][info  ][EM] >>> [E:4162r S:0 M:1854114 (Ack:67243592)] (U) Msg RX from 0:C1821BCEF2BF91BC [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[17:46:16.855]  [00:01:50.716][info  ][EM] <<< [E:4162r S:0 M:67243593 (Ack:1854114)] (U) Msg TX from 0000000000000000 to 0:C1821BCEF2BF91BC [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:48679] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:16.859]  [00:01:50.716][info  ][SC] Received Sigma3 msg
[17:46:16.905]  [00:01:50.765][info  ][EM] <<< [E:4162r S:0 M:67243594 (Ack:1854114)] (U) Msg TX from 0000000000000000 to 0:C1821BCEF2BF91BC [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:48679] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[17:46:16.906]  [00:01:50.766][info  ][EM] ??1 [E:4162r S:0 M:67243594] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3356ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:16.909]  [00:01:50.770][info  ][SC] SecureSession[0x20006e28, LSID:13919]: State change 'kEstablishing' --> 'kActive'
[17:46:16.910]  [00:01:50.770][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[17:46:16.910]  [00:01:50.771][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[17:46:16.913]  [00:01:50.771][silabs ]NWK: platform event type 32792
[17:46:17.364]  [00:01:51.225][info  ][EM] >>> [E:4163r S:13919 M:109446507] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0001:08 (IM:InvokeCommandRequest) (B:64)
[17:46:17.366]  [00:01:51.226][info  ][ZCL] GoToLiftPercentage 1500 command received
[17:46:17.368]  [00:01:51.229][info  ][EM] <<< [E:4163r S:13919 M:48879868 (Ack:109446507)] (S) Msg TX from 00000000000008D0 to 1:000000000001B669 [E4E8] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:48679] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[17:46:17.371]  [00:01:51.230][info  ][EM] ??1 [E:4163r S:13919 M:48879868] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:17.372]  [00:01:51.230][silabs ]WDC: EP[1] Attr TargetPositionLiftPercent100ths 1500
[17:46:17.372]  [00:01:51.230][silabs ]WDC: EP[1] update operational status to Closed
[17:46:17.373]  
[17:46:17.373]  [00:01:51.231][info  ][ZCL] Lift[1] Position Set: 1100
[17:46:17.373]  [00:01:51.231][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:17.374]  [00:01:51.233][silabs ]MATTER TX[0-11]: 55 AA 01 00 05 11 04 00 00 01 55 70 
[17:46:17.376]  [00:01:51.233][silabs ]COM: CMD: 0x11, SN: 0x0005, LEN: 12
[17:46:17.376]  
[17:46:17.376]  [00:01:51.233][silabs ]SPP: ack_timeout_ms 500
[17:46:17.388]  [00:01:51.249][info  ][EM] >>> [E:4162r S:0 M:1854115 (Ack:67243594)] (U) Msg RX from 0:C1821BCEF2BF91BC [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:17.872]  [00:01:51.733][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:46:17.872]  [00:01:51.733][silabs ]MATTER TX[0-11]: 55 AA 01 00 05 11 04 00 00 01 55 70 
[17:46:17.873]  [00:01:51.733][silabs ]COM: CMD: 0x11, SN: 0x0005, LEN: 12
[17:46:17.878]  
[17:46:17.883]  [00:01:51.744][info  ][EM] >>> [E:4163r S:13919 M:109446508 (Ack:48879868)] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[17:46:17.943]  [00:01:51.803][silabs ]MATTER RX[0-11]: 55 AA 01 00 05 11 04 00 00 01 55 70 
[17:46:17.943]  [00:01:51.804][silabs ]COM: MCU TX spp_app_event_CurtainPercentCtrl (echo, sn:0x0005)
[17:46:20.795]  [00:01:54.657][silabs ]MATTER RX[0-11]: 55 AA 01 00 08 12 04 00 00 00 55 73 
[17:46:20.795]  [00:01:54.657][silabs ]MATTER TX[0-7]: 55 AA 01 00 08 12 00 1A 
[17:46:20.797]  [00:01:54.657][silabs ]COM: CMD: 0x12, SN: 0x0008, LEN: 8
[17:46:20.797]  
[17:46:20.797]  [00:01:54.658][silabs ]WDC: report Active percent 85 dev_index 1
[17:46:20.798]  [00:01:54.658][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1500
[17:46:20.798]  
[17:46:20.798]  [00:01:54.658][info  ][ZCL] Lift[1] Position Set: 1500
[17:46:20.801]  [00:01:54.658][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:21.296]  [00:01:55.158][silabs ]MATTER RX[0-11]: 55 AA 01 01 08 12 04 00 00 00 55 74 
[17:46:21.296]  [00:01:55.158][silabs ]MATTER TX[0-7]: 55 AA 01 01 08 12 00 1B 
[17:46:21.299]  [00:01:55.158][silabs ]COM: CMD: 0x12, SN: 0x0108, LEN: 8
[17:46:21.299]  
[17:46:21.299]  [00:01:55.158][silabs ]WDC: report Active percent 85 dev_index 1
[17:46:21.299]  [00:01:55.159][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1500
[17:46:21.299]  
[17:46:21.299]  [00:01:55.159][info  ][ZCL] Lift[1] Position Set: 1500
[17:46:21.302]  [00:01:55.159][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:35.966]  [00:02:09.828][info  ][EM] >>> [E:11115r S:0 M:216056954] (U) Msg RX from 0:C8D05BAC1936ABF5 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[17:46:35.968]  [00:02:09.829][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[17:46:35.969]  [00:02:09.829][info  ][EM] <<< [E:11115r S:0 M:67243595 (Ack:216056954)] (U) Msg TX from 0000000000000000 to 0:C8D05BAC1936ABF5 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:35925] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:35.972]  [00:02:09.830][info  ][SC] Received Sigma1 msg
[17:46:35.978]  [00:02:09.838][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008D0
[17:46:36.001]  [00:02:09.863][info  ][EM] <<< [E:11115r S:0 M:67243596 (Ack:216056954)] (U) Msg TX from 0000000000000000 to 0:C8D05BAC1936ABF5 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:35925] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[17:46:36.003]  [00:02:09.864][info  ][EM] ??1 [E:11115r S:0 M:67243596] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3388ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:36.007]  [00:02:09.864][info  ][SC] Sent Sigma2 msg
[17:46:36.689]  [00:02:10.551][info  ][EM] >>> [E:11115r S:0 M:216056955 (Ack:67243596)] (U) Msg RX from 0:C8D05BAC1936ABF5 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[17:46:36.691]  [00:02:10.552][info  ][EM] <<< [E:11115r S:0 M:67243597 (Ack:216056955)] (U) Msg TX from 0000000000000000 to 0:C8D05BAC1936ABF5 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:35925] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:36.695]  [00:02:10.552][info  ][SC] Received Sigma3 msg
[17:46:36.741]  [00:02:10.602][info  ][EM] <<< [E:11115r S:0 M:67243598 (Ack:216056955)] (U) Msg TX from 0000000000000000 to 0:C8D05BAC1936ABF5 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:35925] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[17:46:36.742]  [00:02:10.603][info  ][EM] ??1 [E:11115r S:0 M:67243598] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3378ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:36.745]  [00:02:10.606][info  ][SC] SecureSession[0x20006f00, LSID:13920]: State change 'kEstablishing' --> 'kActive'
[17:46:36.746]  [00:02:10.606][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[17:46:36.746]  [00:02:10.607][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[17:46:36.748]  [00:02:10.607][silabs ]NWK: platform event type 32792
[17:46:37.211]  [00:02:11.072][info  ][EM] >>> [E:11116r S:13920 M:118152253] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0001:08 (IM:InvokeCommandRequest) (B:64)
[17:46:37.213]  [00:02:11.073][info  ][ZCL] GoToLiftPercentage 6000 command received
[17:46:37.214]  [00:02:11.076][info  ][EM] <<< [E:11116r S:13920 M:187542453 (Ack:118152253)] (S) Msg TX from 00000000000008D0 to 1:000000000001B669 [E4E8] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:35925] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[17:46:37.217]  [00:02:11.077][info  ][EM] ??1 [E:11116r S:13920 M:187542453] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3363ms from now [State:Active II:500 AI:300 AT:4000]
[17:46:37.219]  [00:02:11.078][silabs ]WDC: EP[1] Attr TargetPositionLiftPercent100ths 6000
[17:46:37.220]  [00:02:11.078][silabs ]WDC: EP[1] update operational status to Closed
[17:46:37.220]  
[17:46:37.220]  [00:02:11.078][info  ][ZCL] Lift[1] Position Set: 1600
[17:46:37.221]  [00:02:11.078][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:37.221]  [00:02:11.080][silabs ]MATTER TX[0-11]: 55 AA 01 00 06 11 04 00 00 01 28 44 
[17:46:37.223]  [00:02:11.081][silabs ]COM: CMD: 0x11, SN: 0x0006, LEN: 12
[17:46:37.223]  
[17:46:37.223]  [00:02:11.081][silabs ]SPP: ack_timeout_ms 500
[17:46:37.227]  [00:02:11.088][info  ][EM] >>> [E:11115r S:0 M:216056956 (Ack:67243598)] (U) Msg RX from 0:C8D05BAC1936ABF5 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:46:37.720]  [00:02:11.582][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:46:37.720]  [00:02:11.582][silabs ]MATTER TX[0-11]: 55 AA 01 00 06 11 04 00 00 01 28 44 
[17:46:37.722]  [00:02:11.582][silabs ]COM: CMD: 0x11, SN: 0x0006, LEN: 12
[17:46:37.727]  
[17:46:37.733]  [00:02:11.594][info  ][EM] >>> [E:11116r S:13920 M:118152254 (Ack:187542453)] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[17:46:37.789]  [00:02:11.651][silabs ]MATTER RX[0-11]: 55 AA 01 00 06 11 04 00 00 01 28 44 
[17:46:37.789]  [00:02:11.651][silabs ]COM: MCU TX spp_app_event_CurtainPercentCtrl (echo, sn:0x0006)
[17:46:45.597]  [00:02:19.458][silabs ]MATTER RX[0-8]: 55 AA 01 00 09 06 01 62 72 
[17:46:45.597]  [00:02:19.458][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0009,len:1
[17:46:45.599]  [00:02:19.458][silabs ]payload[0-0]: 62 
[17:46:45.599]  [00:02:19.459][silabs ]MATTER TX[0-7]: 55 AA 01 00 09 06 00 0F 
[17:46:45.599]  [00:02:19.459][silabs ]COM: CMD: 0x06, SN: 0x0009, LEN: 8
[17:46:45.602]  
[17:46:45.602]  [00:02:19.459][silabs ]PWR: report Battery Percent 98
[17:46:45.602]  
[17:46:47.553]  [00:02:21.414][silabs ]MATTER RX[0-11]: 55 AA 01 00 0A 12 04 00 00 00 28 48 
[17:46:47.553]  [00:02:21.415][silabs ]MATTER TX[0-7]: 55 AA 01 00 0A 12 00 1C 
[17:46:47.554]  [00:02:21.415][silabs ]COM: CMD: 0x12, SN: 0x000A, LEN: 8
[17:46:47.554]  
[17:46:47.554]  [00:02:21.415][silabs ]WDC: report Active percent 40 dev_index 1
[17:46:47.556]  [00:02:21.415][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 6000
[17:46:47.556]  
[17:46:47.556]  [00:02:21.416][info  ][ZCL] Lift[1] Position Set: 6000
[17:46:47.558]  [00:02:21.416][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:46:48.054]  [00:02:21.915][silabs ]MATTER RX[0-11]: 55 AA 01 01 0A 12 04 00 00 00 28 49 
[17:46:48.054]  [00:02:21.915][silabs ]MATTER TX[0-7]: 55 AA 01 01 0A 12 00 1D 
[17:46:48.055]  [00:02:21.916][silabs ]COM: CMD: 0x12, SN: 0x010A, LEN: 8
[17:46:48.055]  
[17:46:48.055]  [00:02:21.916][silabs ]WDC: report Active percent 40 dev_index 1
[17:46:48.056]  [00:02:21.916][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 6000
[17:46:48.056]  
[17:46:48.056]  [00:02:21.916][info  ][ZCL] Lift[1] Position Set: 6000
[17:46:48.058]  [00:02:21.916][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:48:03.639]  [00:03:37.501][silabs ]MATTER RX[0-11]: 55 AA 01 00 0B 12 04 00 00 00 3D 5E 
[17:48:03.639]  [00:03:37.501][silabs ]MATTER TX[0-7]: 55 AA 01 00 0B 12 00 1D 
[17:48:03.641]  [00:03:37.501][silabs ]COM: CMD: 0x12, SN: 0x000B, LEN: 8
[17:48:03.641]  
[17:48:03.641]  [00:03:37.501][silabs ]WDC: report Active percent 61 dev_index 1
[17:48:03.643]  [00:03:37.502][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 3900
[17:48:03.643]  
[17:48:03.643]  [00:03:37.502][info  ][ZCL] Lift[1] Position Set: 3900
[17:48:03.646]  [00:03:37.502][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:48:04.140]  [00:03:38.001][silabs ]MATTER RX[0-11]: 55 AA 01 01 0B 12 04 00 00 00 3D 5F 
[17:48:04.140]  [00:03:38.002][silabs ]MATTER TX[0-7]: 55 AA 01 01 0B 12 00 1E 
[17:48:04.142]  [00:03:38.002][silabs ]COM: CMD: 0x12, SN: 0x010B, LEN: 8
[17:48:04.142]  
[17:48:04.142]  [00:03:38.002][silabs ]WDC: report Active percent 61 dev_index 1
[17:48:04.143]  [00:03:38.002][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 3900
[17:48:04.143]  
[17:48:04.143]  [00:03:38.002][info  ][ZCL] Lift[1] Position Set: 3900
[17:48:04.145]  [00:03:38.003][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported

```
