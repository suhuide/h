```c
[17:03:29.310]  [00:00:00.064][info  ][DL] Starting scheduler
[17:03:29.310]  [00:00:00.064][info  ][DL] ==================================================
[17:03:29.312]  [00:00:00.065][info  ][DL]  starting
[17:03:29.312]  [00:00:00.065][info  ][DL] ==================================================
[17:03:29.313]  [00:00:00.065][info  ][DL] Init CHIP Stack
[17:03:29.313]  [00:00:00.067][info  ][DL] Provision mode disabled
[17:03:29.313]  [00:00:00.067][info  ][DL] Initializing OpenThread stack
[17:03:29.315]  [00:00:00.068][info  ][DL] OpenThread ifconfig up and thread start
[17:03:29.315]  [00:00:00.068][info  ][DL] OpenThread started: OK
[17:03:29.319]  [00:00:00.103][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[17:03:29.319]  [00:00:00.103][info  ][DL] RAIL version:, v3.0.3-b0
[17:03:29.321]  [00:00:00.104][info  ][SVR] Current Software Version String: 0.0.12
[17:03:29.321]  [00:00:00.106][info  ][SVR] Current Software Version: 12
[17:03:29.322]  [00:00:00.107][info  ][DL] Device Configuration:
[17:03:29.322]  [00:00:00.107][info  ][DL]   Serial Number: 18F949E0A735AF92
[17:03:29.324]  [00:00:00.108][info  ][DL]   Vendor Id: 5232 (0x1470)
[17:03:29.324]  [00:00:00.108][info  ][DL]   Product Id: 65281 (0xFF01)
[17:03:29.324]  [00:00:00.108][info  ][DL]   Product Name: Window Covering
[17:03:29.325]  [00:00:00.109][info  ][DL]   Hardware Version: 1
[17:03:29.325]  [00:00:00.110][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[17:03:29.326]  [00:00:00.110][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 1064 (0x428)
[17:03:29.327]  [00:00:00.110][info  ][DL]   Manufacturing Date: 2026-10-19
[17:03:29.327]  [00:00:00.112][info  ][DL]   Device Type: 65535 (0xFFFF)
[17:03:29.327]  [00:00:00.113][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:03:29.331]  [00:00:00.116][info  ][SVR] SetupQRCode: [MT:K2CA0WSC00J19D1LX00]
[17:03:29.331]  [00:00:00.116][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[17:03:29.332]  [00:00:00.116][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0WSC00J19D1LX00
[17:03:29.336]  matterCli> [00:00:00.121][silabs ]CTM: Ver: 12 Build:  # Time:Oct 19 2026 16:35:17
[17:03:29.341]  [00:00:00.125][silabs ]CTM: Btl Ver: core: v3.2 user: v2
[17:03:29.346]  [00:00:00.130][silabs ]CTM: ResetCause: 0x80000080 (bit: WDOG0=0 LOCKUP=0 SYSREQ=0 PIN=0 POR=0)
[17:03:29.352]  [00:00:00.135][silabs ] Tx power 10dBm
[17:03:29.355]  [00:00:00.140][silabs ]SetupQRCode: [MT:K2CA0WSC00J19D1LX00]
[17:03:29.355]  [00:00:00.141][silabs ]COM: Init done
[17:03:29.355]  [00:00:00.141][silabs ]app_mcu_dfu_init: spawning async init thread
[17:03:29.356]  [00:00:00.142][silabs ]mcu_dfu_init_thread_func start
[17:03:29.356]  [00:00:00.142][silabs ]waiting for MCU version...
[17:03:29.358]  [00:00:00.142][silabs ]NWK: device has provisioned
[17:03:29.358]  
[17:03:29.358]  [00:00:00.142][silabs ]COM: notify network [Leave]
[17:03:29.358]  [00:00:00.142][silabs ]CLS: register device: dev 0x2002a226 endpoint 1 type 0 idx 1
[17:03:29.383]  [00:00:00.167][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:03:29.383]  [00:00:00.168][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[17:03:29.385]  [00:00:00.169][silabs ]App Task started
[17:03:29.385]  [00:00:00.169][silabs ]MATTER TX[0-8]: 55 AA 01 00 00 02 01 00 03 
[17:03:29.385]  [00:00:00.169][silabs ]COM: CMD: 0x02, SN: 0x0000, LEN: 9
[17:03:29.386]  
[17:03:29.386]  [00:00:00.170][silabs ]SPP: ack_timeout_ms 500
[17:03:29.386]  [00:00:00.170][silabs ]SPP: pending ack but allow new cmd process
[17:03:29.437]  [00:00:00.222][silabs ]MATTER RX[0-7]: 55 AA 01 00 00 02 00 02 
[17:03:29.437]  [00:00:00.222][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:03:29.449]  [00:00:00.234][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:03:29.449]  [00:00:00.235][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[17:03:29.450]  [00:00:00.235][silabs ]NWK: platform event type 32779
[17:03:29.450]  [00:00:00.236][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[17:03:29.452]  [00:00:00.236][silabs ]NWK: kThreadConnectivityChange,32769
[17:03:29.452]  [00:00:00.236][silabs ]NWK: Thread Established
[17:03:29.453]  [00:00:00.236][silabs ]COM: notify network [Joined]
[17:03:29.453]  [00:00:00.237][info  ][SVR] Scheduling OTA Requestor initialization
[17:03:29.456]  [00:00:00.237][info  ][SVR] Joining Multicast groups
[17:03:29.537]  [00:00:00.323][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[17:03:29.537]  [00:00:00.323][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[17:03:29.537]  
[17:03:29.537]  [00:00:00.323][silabs ]SPP: ack_timeout_ms 500
[17:03:29.585]  [00:00:00.370][info  ][DL] SRP Client was started, detected server: fd73:b61e:a621:d88a:a909:9947:78dc:224d
[17:03:29.585]  [00:00:00.370][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:03:29.587]  [00:00:00.371][silabs ]NWK: platform event type 32779
[17:03:29.587]  [00:00:00.372][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[17:03:29.589]  [00:00:00.372][silabs ]NWK: platform event type 32779
[17:03:29.613]  [00:00:00.398][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 31 2E 32 2E 36 7D 99 
[17:03:29.614]  [00:00:00.399][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"1.2.6}
[17:03:29.614]  [00:00:00.399][silabs ]COM: Failed to extract version from product info
[17:03:29.616]  [00:00:00.399][silabs ]COM: Fallback extracted version: 1.2.6
[17:03:29.616]  [00:00:00.399][silabs ]Current MCU version set to: 1.2.6
[17:03:29.652]  [00:00:00.436][silabs ]got MCU version 1.2.6
[17:03:29.652]  [00:00:00.436][silabs ]mcu_dfu: init done, waiting for Matter OTA trigger...
[17:03:29.715]  [00:00:00.500][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 01 00 03 
[17:03:29.715]  [00:00:00.500][silabs ]COM: CMD: 0x01, SN: 0x0002, LEN: 8
[17:03:29.715]  
[17:03:29.715]  [00:00:00.500][silabs ]SPP: ack_timeout_ms 500
[17:03:29.763]  [00:00:00.547][silabs ]MATTER RX[0-31]: 55 AA 01 00 02 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 31 2E 32 2E 36 7D 9A 
[17:03:29.764]  [00:00:00.548][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"1.2.6}
[17:03:29.764]  [00:00:00.548][silabs ]COM: Failed to extract version from product info
[17:03:29.765]  [00:00:00.548][silabs ]COM: Fallback extracted version: 1.2.6
[17:03:29.765]  [00:00:00.548][silabs ]Current MCU version set to: 1.2.6
[17:03:29.864]  [00:00:00.649][silabs ]MATTER TX[0-8]: 55 AA 01 00 03 02 01 01 07 
[17:03:29.864]  [00:00:00.649][silabs ]COM: CMD: 0x02, SN: 0x0003, LEN: 9
[17:03:29.864]  
[17:03:29.866]  [00:00:00.649][silabs ]SPP: ack_timeout_ms 500
[17:03:29.888]  [00:00:00.673][silabs ]MATTER RX[0-7]: 55 AA 01 00 03 02 00 05 
[17:03:29.888]  [00:00:00.673][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[17:03:29.993]  [00:00:00.778][silabs ]MATTER RX[0-11]: 55 AA 01 00 00 12 04 00 00 00 00 16 
[17:03:29.993]  [00:00:00.778][silabs ]MATTER TX[0-7]: 55 AA 01 00 00 12 00 12 
[17:03:29.994]  [00:00:00.778][silabs ]COM: CMD: 0x12, SN: 0x0000, LEN: 8
[17:03:29.994]  
[17:03:29.994]  [00:00:00.778][silabs ]WDC: report Active percent 0 dev_index 1
[17:03:29.996]  [00:00:00.779][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:03:29.996]  
[17:03:29.996]  [00:00:00.779][info  ][ZCL] Lift[1] Position Set: 10000
[17:03:29.998]  [00:00:00.779][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:03:30.285]  [00:00:01.071][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[17:03:30.285]  [00:00:01.071][silabs ]NWK: platform event type 32786
[17:03:30.287]  [00:00:01.071][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[17:03:30.287]  [00:00:01.071][info  ][SVR] Server initialization complete
[17:03:30.288]  [00:00:01.071][info  ][DIS] Updating services using commissioning mode 0
[17:03:30.288]  [00:00:01.071][info  ][DIS] Advertise operational node 52F66E6CB259E4E8-00000000000008D0
[17:03:30.290]  [00:00:01.072][info  ][DL] advertising srp service: 52F66E6CB259E4E8-00000000000008D0._matter._tcp
[17:03:30.291]  [00:00:01.072][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[17:03:30.291]  [00:00:01.073][silabs ]NWK: platform event type 32790
[17:03:30.298]  [00:00:01.083][info  ][IM] No subscriptions to resume
[17:03:30.493]  [00:00:01.278][silabs ]MATTER RX[0-11]: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:03:30.493]  [00:00:01.279][silabs ]MATTER TX[0-7]: 55 AA 01 01 00 12 00 13 
[17:03:30.495]  [00:00:01.279][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:03:30.495]  
[17:03:30.495]  [00:00:01.279][silabs ]WDC: report Active percent 0 dev_index 1
[17:03:30.496]  [00:00:01.279][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:03:30.496]  
[17:03:30.496]  [00:00:01.280][info  ][ZCL] Lift[1] Position Set: 10000
[17:03:30.499]  [00:00:01.280][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:03:30.994]  [00:00:01.779][silabs ]MATTER RX[0-11]: 55 AA 01 01 00 12 04 00 00 00 00 17 
[17:03:30.994]  [00:00:01.779][silabs ]MATTER TX[0-7]: 55 AA 01 01 00 12 00 13 
[17:03:30.995]  [00:00:01.780][silabs ]COM: CMD: 0x12, SN: 0x0100, LEN: 8
[17:03:30.995]  
[17:03:30.995]  [00:00:01.780][silabs ]WDC: report Active percent 0 dev_index 1
[17:03:30.997]  [00:00:01.780][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[17:03:30.997]  
[17:03:30.997]  [00:00:01.780][info  ][ZCL] Lift[1] Position Set: 10000
[17:03:30.999]  [00:00:01.780][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:03:31.541]  [00:00:02.327][silabs ]MATTER RX[0-8]: 55 AA 01 00 01 06 01 4E 56 
[17:03:31.541]  [00:00:02.327][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0001,len:1
[17:03:31.543]  [00:00:02.327][silabs ]payload[0-0]: 4E 
[17:03:31.543]  [00:00:02.327][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 06 00 07 
[17:03:31.543]  [00:00:02.328][silabs ]COM: CMD: 0x06, SN: 0x0001, LEN: 8
[17:03:31.546]  
[17:03:31.546]  [00:00:02.328][silabs ]PWR: report Battery Percent 78
[17:03:31.546]  
[17:03:31.641]  [00:00:02.426][silabs ]MATTER RX[0-8]: 55 AA 01 00 02 07 01 03 0D 
[17:03:31.641]  [00:00:02.426][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 07 00 09 
[17:03:31.642]  [00:00:02.426][silabs ]COM: CMD: 0x07, SN: 0x0002, LEN: 8
[17:03:31.642]  
[17:03:31.642]  [00:00:02.426][silabs ]PWR: report Battery Charge State 3
[17:03:31.645]  
[17:03:31.741]  [00:00:02.527][silabs ]MATTER RX[0-8]: 55 AA 01 00 03 08 01 00 0C 
[17:03:31.741]  [00:00:02.527][silabs ]MATTER TX[0-7]: 55 AA 01 00 03 08 00 0B 
[17:03:31.745]  [00:00:02.527][silabs ]COM: CMD: 0x08, SN: 0x0003, LEN: 8
[17:03:31.745]  
[17:03:31.745]  [00:00:02.528][silabs ]PWR: report Battery Charge Level 0
[17:03:31.746]  
[17:03:32.242]  [00:00:03.027][silabs ]MATTER RX[0-8]: 55 AA 01 01 03 08 01 00 0D 
[17:03:32.242]  [00:00:03.028][silabs ]MATTER TX[0-7]: 55 AA 01 01 03 08 00 0C 
[17:03:32.246]  [00:00:03.028][silabs ]COM: CMD: 0x08, SN: 0x0103, LEN: 8
[17:03:32.246]  
[17:03:32.246]  [00:00:03.028][silabs ]PWR: report Battery Charge Level 0
[17:03:32.246]  
[17:03:33.287]  [00:00:04.073][info  ][SWU] Stopping the watchdog timer
[17:03:33.287]  [00:00:04.073][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[17:21:12.662]  [00:17:43.458][silabs ]MATTER RX[0-11]: 55 AA 01 00 04 12 04 00 00 00 41 5B 
[17:21:12.662]  [00:17:43.458][silabs ]MATTER TX[0-7]: 55 AA 01 00 04 12 00 16 
[17:21:12.664]  [00:17:43.458][silabs ]COM: CMD: 0x12, SN: 0x0004, LEN: 8
[17:21:12.664]  
[17:21:12.664]  [00:17:43.458][silabs ]WDC: report Active percent 65 dev_index 1
[17:21:12.665]  [00:17:43.458][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 3500
[17:21:12.665]  
[17:21:12.665]  [00:17:43.458][info  ][ZCL] Lift[1] Position Set: 3500
[17:21:12.668]  [00:17:43.458][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:21:13.163]  [00:17:43.958][silabs ]MATTER RX[0-11]: 55 AA 01 01 04 12 04 00 00 00 41 5C 
[17:21:13.163]  [00:17:43.958][silabs ]MATTER TX[0-7]: 55 AA 01 01 04 12 00 17 
[17:21:13.164]  [00:17:43.958][silabs ]COM: CMD: 0x12, SN: 0x0104, LEN: 8
[17:21:13.164]  
[17:21:13.164]  [00:17:43.958][silabs ]WDC: report Active percent 65 dev_index 1
[17:21:13.166]  [00:17:43.959][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 3500
[17:21:13.166]  
[17:21:13.166]  [00:17:43.959][info  ][ZCL] Lift[1] Position Set: 3500
[17:21:13.169]  [00:17:43.959][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:21:27.642]  [00:17:58.437][silabs ]MATTER RX[0-11]: 55 AA 01 00 05 12 04 00 00 00 48 63 
[17:21:27.642]  [00:17:58.437][silabs ]MATTER TX[0-7]: 55 AA 01 00 05 12 00 17 
[17:21:27.644]  [00:17:58.438][silabs ]COM: CMD: 0x12, SN: 0x0005, LEN: 8
[17:21:27.644]  
[17:21:27.644]  [00:17:58.438][silabs ]WDC: report Active percent 72 dev_index 1
[17:21:27.645]  [00:17:58.438][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2800
[17:21:27.645]  
[17:21:27.645]  [00:17:58.438][info  ][ZCL] Lift[1] Position Set: 2800
[17:21:27.647]  [00:17:58.438][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:21:28.142]  [00:17:58.938][silabs ]MATTER RX[0-11]: 55 AA 01 01 05 12 04 00 00 00 48 64 
[17:21:28.142]  [00:17:58.938][silabs ]MATTER TX[0-7]: 55 AA 01 01 05 12 00 18 
[17:21:28.144]  [00:17:58.938][silabs ]COM: CMD: 0x12, SN: 0x0105, LEN: 8
[17:21:28.144]  
[17:21:28.144]  [00:17:58.938][silabs ]WDC: report Active percent 72 dev_index 1
[17:21:28.145]  [00:17:58.938][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2800
[17:21:28.145]  
[17:21:28.145]  [00:17:58.939][info  ][ZCL] Lift[1] Position Set: 2800
[17:21:28.149]  [00:17:58.939][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:13.608]  [00:18:44.404][info  ][EM] >>> [E:32951r S:0 M:46408845] (U) Msg RX from 0:0D7637E31CA2637A [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[17:22:13.609]  [00:18:44.404][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[17:22:13.610]  [00:18:44.405][info  ][EM] <<< [E:32951r S:0 M:242887501 (Ack:46408845)] (U) Msg TX from 0000000000000000 to 0:0D7637E31CA2637A [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:55436] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:13.613]  [00:18:44.406][info  ][SC] Received Sigma1 msg
[17:22:13.619]  [00:18:44.415][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008D0
[17:22:13.648]  [00:18:44.445][info  ][EM] <<< [E:32951r S:0 M:242887502 (Ack:46408845)] (U) Msg TX from 0000000000000000 to 0:0D7637E31CA2637A [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:55436] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[17:22:13.649]  [00:18:44.446][info  ][EM] ??1 [E:32951r S:0 M:242887502] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3366ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:13.655]  [00:18:44.446][info  ][SC] Sent Sigma2 msg
[17:22:14.297]  [00:18:45.093][info  ][EM] >>> [E:32951r S:0 M:46408846 (Ack:242887502)] (U) Msg RX from 0:0D7637E31CA2637A [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[17:22:14.298]  [00:18:45.094][info  ][EM] <<< [E:32951r S:0 M:242887503 (Ack:46408846)] (U) Msg TX from 0000000000000000 to 0:0D7637E31CA2637A [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:55436] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:14.301]  [00:18:45.094][info  ][SC] Received Sigma3 msg
[17:22:14.347]  [00:18:45.143][info  ][EM] <<< [E:32951r S:0 M:242887504 (Ack:46408846)] (U) Msg TX from 0000000000000000 to 0:0D7637E31CA2637A [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:55436] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[17:22:14.348]  [00:18:45.144][info  ][EM] ??1 [E:32951r S:0 M:242887504] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3359ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:14.351]  [00:18:45.148][info  ][SC] SecureSession[0x20006d50, LSID:58690]: State change 'kEstablishing' --> 'kActive'
[17:22:14.353]  [00:18:45.148][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[17:22:14.353]  [00:18:45.149][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[17:22:14.355]  [00:18:45.149][silabs ]NWK: platform event type 32792
[17:22:14.807]  [00:18:45.605][info  ][EM] >>> [E:32952r S:58690 M:44418917] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0001:08 (IM:InvokeCommandRequest) (B:64)
[17:22:14.810]  [00:18:45.606][info  ][ZCL] GoToLiftPercentage 6000 command received
[17:22:14.812]  [00:18:45.609][info  ][EM] <<< [E:32952r S:58690 M:57029687 (Ack:44418917)] (S) Msg TX from 00000000000008D0 to 1:000000000001B669 [E4E8] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:55436] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[17:22:14.815]  [00:18:45.610][info  ][EM] ??1 [E:32952r S:58690 M:57029687] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3332ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:14.819]  [00:18:45.610][silabs ]EP[1] startup coalesce: defer TargetPosition 6000
[17:22:14.830]  [00:18:45.626][info  ][EM] >>> [E:32951r S:0 M:46408847 (Ack:242887504)] (U) Msg RX from 0:0D7637E31CA2637A [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:15.338]  [00:18:46.134][info  ][EM] >>> [E:32952r S:58690 M:44418918 (Ack:57029687)] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[17:22:16.813]  [00:18:47.611][silabs ]WDC: EP[1] update operational status to Closed
[17:22:16.813]  
[17:22:16.813]  [00:18:47.611][info  ][ZCL] Lift[1] Position Set: 2900
[17:22:16.815]  [00:18:47.611][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:16.815]  [00:18:47.613][silabs ]EP[1] startup flush: send deferred TargetPosition 40
[17:22:16.817]  [00:18:47.614][silabs ]MATTER TX[0-11]: 55 AA 01 00 04 11 04 00 00 01 28 42 
[17:22:16.817]  [00:18:47.614][silabs ]COM: CMD: 0x11, SN: 0x0004, LEN: 12
[17:22:16.820]  
[17:22:16.820]  [00:18:47.614][silabs ]SPP: ack_timeout_ms 500
[17:22:17.318]  [00:18:48.115][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:22:17.318]  [00:18:48.115][silabs ]MATTER TX[0-11]: 55 AA 01 00 04 11 04 00 00 01 28 42 
[17:22:17.319]  [00:18:48.115][silabs ]COM: CMD: 0x11, SN: 0x0004, LEN: 12
[17:22:17.323]  
[17:22:17.388]  [00:18:48.184][silabs ]MATTER RX[0-11]: 55 AA 01 00 04 11 04 00 00 01 28 42 
[17:22:17.388]  [00:18:48.184][silabs ]COM: MCU TX spp_app_event_CurtainPercentCtrl (echo, sn:0x0004)
[17:22:24.998]  [00:18:55.794][silabs ]MATTER RX[0-11]: 55 AA 01 00 06 12 04 00 00 00 28 44 
[17:22:24.998]  [00:18:55.795][silabs ]MATTER TX[0-7]: 55 AA 01 00 06 12 00 18 
[17:22:24.999]  [00:18:55.795][silabs ]COM: CMD: 0x12, SN: 0x0006, LEN: 8
[17:22:24.999]  
[17:22:24.999]  [00:18:55.795][silabs ]WDC: report Active percent 40 dev_index 1
[17:22:25.000]  [00:18:55.795][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 6000
[17:22:25.000]  
[17:22:25.000]  [00:18:55.796][info  ][ZCL] Lift[1] Position Set: 6000
[17:22:25.003]  [00:18:55.796][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:25.498]  [00:18:56.295][silabs ]MATTER RX[0-11]: 55 AA 01 01 06 12 04 00 00 00 28 45 
[17:22:25.498]  [00:18:56.295][silabs ]MATTER TX[0-7]: 55 AA 01 01 06 12 00 19 
[17:22:25.499]  [00:18:56.295][silabs ]COM: CMD: 0x12, SN: 0x0106, LEN: 8
[17:22:25.499]  
[17:22:25.499]  [00:18:56.296][silabs ]WDC: report Active percent 40 dev_index 1
[17:22:25.501]  [00:18:56.296][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 6000
[17:22:25.501]  
[17:22:25.501]  [00:18:56.296][info  ][ZCL] Lift[1] Position Set: 6000
[17:22:25.504]  [00:18:56.296][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:39.413]  [00:19:10.211][info  ][EM] >>> [E:16918r S:0 M:91110439] (U) Msg RX from 0:70E913BDE4D0EEB1 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[17:22:39.414]  [00:19:10.211][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[17:22:39.416]  [00:19:10.212][info  ][EM] <<< [E:16918r S:0 M:242887505 (Ack:91110439)] (U) Msg TX from 0000000000000000 to 0:70E913BDE4D0EEB1 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:41921] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:39.420]  [00:19:10.212][info  ][SC] Received Sigma1 msg
[17:22:39.425]  [00:19:10.222][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008D0
[17:22:39.449]  [00:19:10.247][info  ][EM] <<< [E:16918r S:0 M:242887506 (Ack:91110439)] (U) Msg TX from 0000000000000000 to 0:70E913BDE4D0EEB1 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:41921] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[17:22:39.451]  [00:19:10.248][info  ][EM] ??1 [E:16918r S:0 M:242887506] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3377ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:39.454]  [00:19:10.248][info  ][SC] Sent Sigma2 msg
[17:22:40.311]  [00:19:11.109][info  ][EM] >>> [E:16918r S:0 M:91110440 (Ack:242887506)] (U) Msg RX from 0:70E913BDE4D0EEB1 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[17:22:40.312]  [00:19:11.110][info  ][EM] <<< [E:16918r S:0 M:242887507 (Ack:91110440)] (U) Msg TX from 0000000000000000 to 0:70E913BDE4D0EEB1 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:41921] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:40.317]  [00:19:11.110][info  ][SC] Received Sigma3 msg
[17:22:40.362]  [00:19:11.160][info  ][EM] <<< [E:16918r S:0 M:242887508 (Ack:91110440)] (U) Msg TX from 0000000000000000 to 0:70E913BDE4D0EEB1 [0000] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:41921] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[17:22:40.364]  [00:19:11.161][info  ][EM] ??1 [E:16918r S:0 M:242887508] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3367ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:40.366]  [00:19:11.164][info  ][SC] SecureSession[0x20006e28, LSID:58691]: State change 'kEstablishing' --> 'kActive'
[17:22:40.368]  [00:19:11.164][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[17:22:40.368]  [00:19:11.165][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[17:22:40.371]  [00:19:11.165][silabs ]NWK: platform event type 32792
[17:22:40.822]  [00:19:11.619][info  ][EM] >>> [E:16919r S:58691 M:240943519] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0001:08 (IM:InvokeCommandRequest) (B:64)
[17:22:40.824]  [00:19:11.621][info  ][ZCL] GoToLiftPercentage 1000 command received
[17:22:40.826]  [00:19:11.624][info  ][EM] <<< [E:16919r S:58691 M:179646922 (Ack:240943519)] (S) Msg TX from 00000000000008D0 to 1:000000000001B669 [E4E8] [UDP:[fdd8:ad7b:70a6:1:a1db:26f3:aa6c:1dd4]:41921] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[17:22:40.828]  [00:19:11.624][info  ][EM] ??1 [E:16919r S:58691 M:179646922] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3393ms from now [State:Active II:500 AI:300 AT:4000]
[17:22:40.830]  [00:19:11.625][silabs ]WDC: EP[1] Attr TargetPositionLiftPercent100ths 1000
[17:22:40.831]  [00:19:11.625][silabs ]WDC: EP[1] update operational status to Open
[17:22:40.831]  
[17:22:40.831]  [00:19:11.625][info  ][ZCL] Lift[1] Position Set: 5900
[17:22:40.832]  [00:19:11.625][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:40.832]  [00:19:11.627][silabs ]MATTER TX[0-11]: 55 AA 01 00 05 11 04 00 00 01 5A 75 
[17:22:40.833]  [00:19:11.628][silabs ]COM: CMD: 0x11, SN: 0x0005, LEN: 12
[17:22:40.833]  
[17:22:40.833]  [00:19:11.628][silabs ]SPP: ack_timeout_ms 500
[17:22:40.844]  [00:19:11.641][info  ][EM] >>> [E:16918r S:0 M:91110441 (Ack:242887508)] (U) Msg RX from 0:70E913BDE4D0EEB1 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[17:22:41.330]  [00:19:12.128][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[17:22:41.330]  [00:19:12.128][silabs ]MATTER TX[0-11]: 55 AA 01 00 05 11 04 00 00 01 5A 75 
[17:22:41.333]  [00:19:12.128][silabs ]COM: CMD: 0x11, SN: 0x0005, LEN: 12
[17:22:41.333]  
[17:22:41.345]  [00:19:12.142][info  ][EM] >>> [E:16919r S:58691 M:240943520 (Ack:179646922)] (S) Msg RX from 1:000000000001B669 [E4E8] to 00000000000008D0 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[17:22:41.833]  [00:19:12.629][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[17:22:41.833]  [00:19:12.629][silabs ]MATTER TX[0-11]: 55 AA 01 00 05 11 04 00 00 01 5A 75 
[17:22:41.833]  [00:19:12.629][silabs ]COM: CMD: 0x11, SN: 0x0005, LEN: 12
[17:22:41.837]  
[17:22:41.901]  [00:19:12.699][silabs ]MATTER RX[0-11]: 55 AA 01 00 05 11 04 00 00 01 5A 75 
[17:22:41.901]  [00:19:12.700][silabs ]COM: MCU TX spp_app_event_CurtainPercentCtrl (echo, sn:0x0005)
[17:22:46.760]  [00:19:17.558][silabs ]MATTER RX[0-11]: 55 AA 01 00 07 12 04 00 00 00 38 55 
[17:22:46.760]  [00:19:17.558][silabs ]MATTER TX[0-7]: 55 AA 01 00 07 12 00 19 
[17:22:46.761]  [00:19:17.559][silabs ]COM: CMD: 0x12, SN: 0x0007, LEN: 8
[17:22:46.761]  
[17:22:46.761]  [00:19:17.559][silabs ]WDC: report Active percent 56 dev_index 1
[17:22:46.763]  [00:19:17.559][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 1000
[17:22:46.763]  
[17:22:46.763]  [00:19:17.559][info  ][ZCL] Lift[1] Position Set: 1000
[17:22:46.766]  [00:19:17.559][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:47.261]  [00:19:18.059][silabs ]MATTER RX[0-11]: 55 AA 01 01 07 12 04 00 00 00 38 56 
[17:22:47.261]  [00:19:18.059][silabs ]MATTER TX[0-7]: 55 AA 01 01 07 12 00 1A 
[17:22:47.262]  [00:19:18.059][silabs ]COM: CMD: 0x12, SN: 0x0107, LEN: 8
[17:22:47.262]  
[17:22:47.262]  [00:19:18.059][silabs ]WDC: report Active percent 56 dev_index 1
[17:22:47.264]  [00:19:18.060][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 4400
[17:22:47.264]  
[17:22:47.264]  [00:19:18.060][info  ][ZCL] Lift[1] Position Set: 4400
[17:22:47.266]  [00:19:18.060][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:59.050]  [00:19:29.848][silabs ]MATTER RX[0-11]: 55 AA 01 00 08 12 04 00 00 00 47 65 
[17:22:59.050]  [00:19:29.848][silabs ]MATTER TX[0-7]: 55 AA 01 00 08 12 00 1A 
[17:22:59.052]  [00:19:29.848][silabs ]COM: CMD: 0x12, SN: 0x0008, LEN: 8
[17:22:59.052]  
[17:22:59.052]  [00:19:29.849][silabs ]WDC: report Active percent 71 dev_index 1
[17:22:59.053]  [00:19:29.849][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2900
[17:22:59.053]  
[17:22:59.053]  [00:19:29.849][info  ][ZCL] Lift[1] Position Set: 2900
[17:22:59.056]  [00:19:29.849][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
[17:22:59.551]  [00:19:30.348][silabs ]MATTER RX[0-11]: 55 AA 01 01 08 12 04 00 00 00 47 66 
[17:22:59.551]  [00:19:30.349][silabs ]MATTER TX[0-7]: 55 AA 01 01 08 12 00 1B 
[17:22:59.552]  [00:19:30.349][silabs ]COM: CMD: 0x12, SN: 0x0108, LEN: 8
[17:22:59.552]  
[17:22:59.552]  [00:19:30.349][silabs ]WDC: report Active percent 71 dev_index 1
[17:22:59.553]  [00:19:30.349][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 2900
[17:22:59.553]  
[17:22:59.553]  [00:19:30.350][info  ][ZCL] Lift[1] Position Set: 2900
[17:22:59.556]  [00:19:30.350][info  ][ZCL] WRITE ERR: ep 1 clus 0x0000_0102 attr 0x0000_0003 not supported
```
