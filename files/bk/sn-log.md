```c
[16:16:27.956]  [00:00:00.067][info  ][DL] Starting scheduler
[16:16:27.956]  [00:00:00.067][info  ][DL] ==================================================
[16:16:27.957]  [00:00:00.067][info  ][DL]  starting
[16:16:27.957]  [00:00:00.068][info  ][DL] ==================================================
[16:16:27.960]  [00:00:00.068][info  ][DL] Init CHIP Stack
[16:16:27.960]  [00:00:00.069][info  ][DL] Provision mode disabled
[16:16:27.960]  [00:00:00.069][info  ][DL] Initializing OpenThread stack
[16:16:27.961]  [00:00:00.071][info  ][DL] OpenThread ifconfig up and thread start
[16:16:27.961]  [00:00:00.071][info  ][DL] OpenThread started: OK
[16:16:27.964]  [00:00:00.106][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[16:16:27.964]  [00:00:00.106][info  ][DL] RAIL version:, v3.0.3-b0
[16:16:27.967]  [00:00:00.107][info  ][SVR] Current Software Version String: 0.0.4
[16:16:27.967]  [00:00:00.109][info  ][SVR] Current Software Version: 4
[16:16:27.968]  [00:00:00.110][info  ][DL] Device Configuration:
[16:16:27.968]  [00:00:00.110][info  ][DL]   Serial Number: 36DF4B3B8F54A56D
[16:16:27.968]  [00:00:00.111][info  ][DL]   Vendor Id: 5232 (0x1470)
[16:16:27.969]  [00:00:00.111][info  ][DL]   Product Id: 65281 (0xFF01)
[16:16:27.969]  [00:00:00.111][info  ][DL]   Product Name: Window Covering
[16:16:27.971]  [00:00:00.112][info  ][DL]   Hardware Version: 1
[16:16:27.971]  [00:00:00.112][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[16:16:27.972]  [00:00:00.113][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 2485 (0x9B5)
[16:16:27.972]  [00:00:00.113][info  ][DL]   Manufacturing Date: 2026-06-08
[16:16:27.973]  [00:00:00.115][info  ][DL]   Device Type: 65535 (0xFFFF)
[16:16:27.973]  [00:00:00.115][info  ][SVR] SetupQRCode: [MT:K2CA0YDG158HO34RB10]
[16:16:27.975]  [00:00:00.115][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[16:16:27.977]  [00:00:00.115][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0YDG158HO34RB10
[16:16:27.978]  [00:00:00.116][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:16:27.978]  [00:00:00.119][silabs ]Ver: 4 Btl: 0x03020002 Time:Jun 18 2026 16:15:16 Reset Reason: 0x00000000
[16:16:27.979]  [00:00:00.119][silabs ]SetupQRCode: [MT:K2CA0YDG158HO34RB10]
[16:16:27.979]  [00:00:00.120][silabs ]COM: Init done
[16:16:27.980]  [00:00:00.120][silabs ]app_mcu_dfu_init: spawning async init thread
[16:16:27.980]  [00:00:00.121][silabs ]NWK: device has provisioned
[16:16:27.981]  
[16:16:27.981]  [00:00:00.121][silabs ]COM: notify network [Leave]
[16:16:27.981]  [00:00:00.122][silabs ]mcu_dfu_init_thread_func start
[16:16:27.981]  [00:00:00.122][silabs ]CLS: register device: dev 0x2002e386 endpoint 1 type 0 idx 1
[16:16:27.982]  [00:00:00.122][silabs ]waiting for MCU version...
[16:16:27.982]  [00:00:00.123][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[16:16:27.985]  [00:00:00.124][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[16:16:27.986]  [00:00:00.125][silabs ]App Task started
[16:16:27.986]  [00:00:00.125][silabs ]MATTER TX[0-8]: 55 AA 01 00 00 02 01 00 03 
[16:16:27.986]  [00:00:00.125][silabs ]COM: CMD: 0x02, SN: 0x0000, LEN: 9
[16:16:27.987]  
[16:16:27.987]  [00:00:00.125][silabs ]SPP: ack_timeout_ms 500
[16:16:27.987]  [00:00:00.125][silabs ]SPP: pending ack but allow new cmd process
[16:16:27.992]  matterCli> [00:00:00.238][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:16:28.095]  [00:00:00.239][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[16:16:28.097]  [00:00:00.239][silabs ]NWK: platform event type 32779
[16:16:28.097]  [00:00:00.240][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[16:16:28.098]  [00:00:00.240][silabs ]NWK: kThreadConnectivityChange,32769
[16:16:28.098]  [00:00:00.240][silabs ]NWK: Thread Established
[16:16:28.100]  [00:00:00.240][silabs ]COM: notify network [Joined]
[16:16:28.100]  [00:00:00.240][info  ][SVR] Scheduling OTA Requestor initialization
[16:16:28.103]  [00:00:00.241][info  ][SVR] Joining Multicast groups
[16:16:28.103]  [00:00:00.242][silabs ]SPP: pending ack but allow new cmd process
[16:16:28.227]  [00:00:00.369][info  ][DL] SRP Client was started, detected server: fd11:9c64:dd37:b8c4:6397:7d5e:9e7b:227a
[16:16:28.227]  [00:00:00.370][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:16:28.228]  [00:00:00.370][silabs ]NWK: platform event type 32779
[16:16:28.228]  [00:00:00.371][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:16:28.232]  [00:00:00.371][silabs ]NWK: platform event type 32779
[16:16:28.331]  [00:00:00.473][silabs ]MATTER RX[0-31]: 55 AA 01 00 00 02 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:16:28.334]  [00:00:00.473][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[16:16:28.410]  [00:00:00.552][silabs ]MATTER RX[0-11]: 55 AA 01 00 1B 12 04 00 00 00 00 31 
[16:16:28.410]  [00:00:00.552][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:28.411]  [00:00:00.552][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:28.411]  
[16:16:28.411]  [00:00:00.552][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:28.432]  [00:00:00.575][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[16:16:28.432]  [00:00:00.575][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[16:16:28.432]  
[16:16:28.432]  [00:00:00.575][silabs ]SPP: ack_timeout_ms 500
[16:16:28.910]  [00:00:01.052][silabs ]MATTER RX[0-11]: 55 AA 01 09 1B 12 04 00 00 00 00 3A 
[16:16:28.910]  [00:00:01.052][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:28.911]  [00:00:01.052][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:28.911]  
[16:16:28.911]  [00:00:01.052][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:28.918]  [00:00:01.053][silabs ]SPP: pending ack but allow new cmd process
[16:16:28.933]  [00:00:01.076][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:28.933]  [00:00:01.076][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[16:16:28.937]  [00:00:01.076][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[16:16:28.937]  
[16:16:29.014]  [00:00:01.156][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[16:16:29.014]  [00:00:01.156][silabs ]NWK: platform event type 32786
[16:16:29.015]  [00:00:01.156][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[16:16:29.015]  [00:00:01.156][info  ][SVR] Server initialization complete
[16:16:29.016]  [00:00:01.156][info  ][DIS] Updating services using commissioning mode 0
[16:16:29.016]  [00:00:01.157][info  ][DIS] Advertise operational node 66AC7364E726C344-00000000000008CA
[16:16:29.017]  [00:00:01.157][info  ][DL] advertising srp service: 66AC7364E726C344-00000000000008CA._matter._tcp
[16:16:29.018]  [00:00:01.158][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[16:16:29.018]  [00:00:01.158][silabs ]NWK: platform event type 32790
[16:16:29.027]  [00:00:01.167][info  ][IM] No subscriptions to resume
[16:16:29.410]  [00:00:01.551][silabs ]MATTER RX[0-11]: 55 AA 01 09 1B 12 04 00 00 00 00 3A 
[16:16:29.410]  [00:00:01.552][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:29.411]  [00:00:01.552][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:29.411]  
[16:16:29.411]  [00:00:01.552][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:29.414]  [00:00:01.553][silabs ]SPP: pending ack but allow new cmd process
[16:16:29.433]  [00:00:01.577][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:29.433]  [00:00:01.577][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[16:16:29.437]  [00:00:01.577][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[16:16:29.442]  
[16:16:29.935]  [00:00:02.078][silabs ]SPP: re-sent reach to max
[16:16:29.935]  [00:00:02.078][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 01 00 03 
[16:16:29.935]  [00:00:02.079][silabs ]COM: CMD: 0x01, SN: 0x0002, LEN: 8
[16:16:29.938]  
[16:16:29.938]  [00:00:02.079][silabs ]SPP: ack_timeout_ms 500
[16:16:29.980]  [00:00:02.123][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:16:29.982]  [00:00:02.123][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:16:29.982]  [00:00:02.123][silabs ]COM: Failed to extract version from product info
[16:16:29.983]  [00:00:02.124][silabs ]COM: Fallback extracted version: 3.0.0
[16:16:29.983]  [00:00:02.124][silabs ]Current MCU version set to: 3.0.0
[16:16:30.033]  [00:00:02.173][silabs ]got MCU version 3.0.0
[16:16:30.033]  [00:00:02.173][silabs ]mcu_dfu: init done, waiting for Matter OTA trigger...
[16:16:30.080]  [00:00:02.222][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:16:30.082]  [00:00:02.223][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:16:30.082]  [00:00:02.223][silabs ]COM: Failed to extract version from product info
[16:16:30.083]  [00:00:02.223][silabs ]COM: Fallback extracted version: 3.0.0
[16:16:30.083]  [00:00:02.223][silabs ]Current MCU version set to: 3.0.0
[16:16:30.085]  [00:00:02.224][silabs ]MATTER TX[0-8]: 55 AA 01 00 03 02 01 01 07 
[16:16:30.085]  [00:00:02.224][silabs ]COM: CMD: 0x02, SN: 0x0003, LEN: 9
[16:16:30.088]  
[16:16:30.088]  [00:00:02.224][silabs ]SPP: ack_timeout_ms 500
[16:16:30.181]  [00:00:02.323][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:16:30.182]  [00:00:02.323][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:16:30.182]  [00:00:02.323][silabs ]COM: Failed to extract version from product info
[16:16:30.183]  [00:00:02.323][silabs ]COM: Fallback extracted version: 3.0.0
[16:16:30.183]  [00:00:02.323][silabs ]Current MCU version set to: 3.0.0
[16:16:30.281]  [00:00:02.422][silabs ]MATTER RX[0-31]: 55 AA 01 00 02 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 94 
[16:16:30.282]  [00:00:02.422][silabs ]MATTER TX[0-7]: 55 AA 01 00 1B 12 00 2D 
[16:16:30.282]  [00:00:02.422][silabs ]COM: CMD: 0x12, SN: 0x001B, LEN: 8
[16:16:30.283]  
[16:16:30.283]  [00:00:02.423][silabs ]SPP: ack_timeout_ms 500
[16:16:30.283]  [00:00:02.423][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:16:30.284]  [00:00:02.423][silabs ]COM: Failed to extract version from product info
[16:16:30.284]  [00:00:02.423][silabs ]COM: Fallback extracted version: 3.0.0
[16:16:30.288]  [00:00:02.423][silabs ]Current MCU version set to: 3.0.0
[16:16:30.380]  [00:00:02.522][silabs ]MATTER RX[0-31]: 55 AA 01 00 03 02 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 96 
[16:16:30.381]  [00:00:02.523][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[16:16:30.381]  [00:00:02.524][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:30.387]  [00:00:02.524][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:30.387]  
[16:16:30.387]  [00:00:02.524][silabs ]SPP: ack_timeout_ms 500
[16:16:30.455]  [00:00:02.598][silabs ]MATTER RX[0-8]: 55 AA 01 00 1C 06 01 00 23 
[16:16:30.455]  [00:00:02.598][silabs ]COM: spp_app_event_BatteryLevel,sn:0x001C,len:1
[16:16:30.457]  [00:00:02.598][silabs ]payload[0-0]: 00 
[16:16:30.457]  [00:00:02.598][silabs ]PWR: report Battery Percent 0
[16:16:30.457]  
[16:16:30.457]  [00:00:02.599][silabs ]SPP: pending ack but allow new cmd process
[16:16:30.881]  [00:00:03.024][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:30.881]  [00:00:03.024][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:30.886]  [00:00:03.024][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:30.886]  
[16:16:30.955]  [00:00:03.097][silabs ]MATTER RX[0-8]: 55 AA 01 09 1C 06 01 00 2C 
[16:16:30.955]  [00:00:03.098][silabs ]COM: spp_app_event_BatteryLevel,sn:0x091C,len:1
[16:16:30.956]  [00:00:03.098][silabs ]payload[0-0]: 00 
[16:16:30.956]  [00:00:03.098][silabs ]PWR: report Battery Percent 0
[16:16:30.956]  
[16:16:30.956]  [00:00:03.098][silabs ]SPP: pending ack but allow new cmd process
[16:16:31.381]  [00:00:03.524][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:31.381]  [00:00:03.524][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:31.383]  [00:00:03.524][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:31.387]  
[16:16:31.455]  [00:00:03.597][silabs ]MATTER RX[0-8]: 55 AA 01 09 1C 06 01 00 2C 
[16:16:31.455]  [00:00:03.597][silabs ]COM: spp_app_event_BatteryLevel,sn:0x091C,len:1
[16:16:31.456]  [00:00:03.597][silabs ]payload[0-0]: 00 
[16:16:31.456]  [00:00:03.598][silabs ]PWR: report Battery Percent 0
[16:16:31.456]  
[16:16:31.456]  [00:00:03.598][silabs ]SPP: pending ack but allow new cmd process
[16:16:31.882]  [00:00:04.024][silabs ]SPP: re-sent reach to max
[16:16:31.882]  [00:00:04.025][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:31.882]  [00:00:04.025][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:31.887]  
[16:16:31.887]  [00:00:04.025][silabs ]SPP: ack_timeout_ms 500
[16:16:32.004]  [00:00:04.147][silabs ]MATTER RX[0-8]: 55 AA 01 00 1D 07 01 03 28 
[16:16:32.004]  [00:00:04.147][silabs ]PWR: report Battery Charge State 3
[16:16:32.004]  
[16:16:32.008]  [00:00:04.147][silabs ]SPP: pending ack but allow new cmd process
[16:16:32.017]  [00:00:04.158][info  ][SWU] Stopping the watchdog timer
[16:16:32.017]  [00:00:04.158][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:16:32.382]  [00:00:04.525][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:32.382]  [00:00:04.525][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:32.386]  [00:00:04.525][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:32.386]  
[16:16:32.504]  [00:00:04.646][silabs ]MATTER RX[0-8]: 55 AA 01 09 1D 07 01 03 31 
[16:16:32.504]  [00:00:04.647][silabs ]PWR: report Battery Charge State 3
[16:16:32.504]  
[16:16:32.506]  [00:00:04.647][silabs ]SPP: pending ack but allow new cmd process
[16:16:32.882]  [00:00:05.025][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:32.882]  [00:00:05.025][silabs ]MATTER TX[0-7]: 55 AA 01 09 1B 12 00 36 
[16:16:32.887]  [00:00:05.025][silabs ]COM: CMD: 0x12, SN: 0x091B, LEN: 8
[16:16:32.887]  
[16:16:33.004]  [00:00:05.146][silabs ]MATTER RX[0-8]: 55 AA 01 09 1D 07 01 03 31 
[16:16:33.004]  [00:00:05.146][silabs ]PWR: report Battery Charge State 3
[16:16:33.004]  
[16:16:33.006]  [00:00:05.147][silabs ]SPP: pending ack but allow new cmd process
[16:16:33.382]  [00:00:05.525][silabs ]SPP: re-sent reach to max
[16:16:33.382]  [00:00:05.526][silabs ]MATTER TX[0-7]: 55 AA 01 00 1C 06 00 22 
[16:16:33.382]  [00:00:05.526][silabs ]COM: CMD: 0x06, SN: 0x001C, LEN: 8
[16:16:33.387]  
[16:16:33.387]  [00:00:05.526][silabs ]SPP: ack_timeout_ms 500
[16:16:33.556]  [00:00:05.699][silabs ]MATTER RX[0-11]: 55 AA 01 00 20 12 04 00 00 00 00 36 
[16:16:33.556]  [00:00:05.699][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:33.557]  [00:00:05.700][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:33.557]  
[16:16:33.557]  [00:00:05.700][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:33.562]  [00:00:05.700][silabs ]SPP: pending ack but allow new cmd process
[16:16:33.883]  [00:00:06.026][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:33.883]  [00:00:06.026][silabs ]MATTER TX[0-7]: 55 AA 01 00 1C 06 00 22 
[16:16:33.886]  [00:00:06.026][silabs ]COM: CMD: 0x06, SN: 0x001C, LEN: 8
[16:16:33.886]  
[16:16:34.056]  [00:00:06.199][silabs ]MATTER RX[0-11]: 55 AA 01 09 20 12 04 00 00 00 00 3F 
[16:16:34.056]  [00:00:06.199][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:34.058]  [00:00:06.199][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:34.058]  
[16:16:34.058]  [00:00:06.199][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:34.062]  [00:00:06.200][silabs ]SPP: pending ack but allow new cmd process
[16:16:34.383]  [00:00:06.526][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:34.383]  [00:00:06.526][silabs ]MATTER TX[0-7]: 55 AA 01 00 1C 06 00 22 
[16:16:34.387]  [00:00:06.526][silabs ]COM: CMD: 0x06, SN: 0x001C, LEN: 8
[16:16:34.387]  
[16:16:34.556]  [00:00:06.698][silabs ]MATTER RX[0-11]: 55 AA 01 09 20 12 04 00 00 00 00 3F 
[16:16:34.556]  [00:00:06.699][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:34.557]  [00:00:06.699][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:34.557]  
[16:16:34.557]  [00:00:06.699][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:34.562]  [00:00:06.699][silabs ]SPP: pending ack but allow new cmd process
[16:16:34.884]  [00:00:07.026][silabs ]SPP: re-sent reach to max
[16:16:34.884]  [00:00:07.027][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:34.884]  [00:00:07.027][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:34.887]  
[16:16:34.887]  [00:00:07.027][silabs ]SPP: ack_timeout_ms 500
[16:16:35.106]  [00:00:07.248][silabs ]MATTER RX[0-11]: 55 AA 01 00 2F 12 04 00 00 00 00 45 
[16:16:35.106]  [00:00:07.249][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:35.107]  [00:00:07.249][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:35.107]  
[16:16:35.107]  [00:00:07.249][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:35.113]  [00:00:07.249][silabs ]SPP: pending ack but allow new cmd process
[16:16:35.384]  [00:00:07.527][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:35.384]  [00:00:07.527][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:35.386]  [00:00:07.527][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:35.392]  
[16:16:35.605]  [00:00:07.748][silabs ]MATTER RX[0-11]: 55 AA 01 09 2F 12 04 00 00 00 00 4E 
[16:16:35.605]  [00:00:07.748][silabs ]SPP: tx_queue full!
[16:16:35.605]  [00:00:07.748][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:35.606]  [00:00:07.749][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:35.610]  
[16:16:35.610]  [00:00:07.749][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:35.884]  [00:00:08.027][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:35.884]  [00:00:08.027][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:35.886]  [00:00:08.027][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:35.891]  
[16:16:36.104]  [00:00:08.248][silabs ]MATTER RX[0-11]: 55 AA 01 09 2F 12 04 00 00 00 00 4E 
[16:16:36.104]  [00:00:08.248][silabs ]SPP: tx_queue full!
[16:16:36.104]  [00:00:08.248][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:36.106]  [00:00:08.248][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:36.110]  
[16:16:36.110]  [00:00:08.248][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:36.384]  [00:00:08.527][silabs ]SPP: re-sent reach to max
[16:16:36.384]  [00:00:08.528][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:36.384]  [00:00:08.528][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:36.389]  
[16:16:36.389]  [00:00:08.528][silabs ]SPP: ack_timeout_ms 500
[16:16:36.655]  [00:00:08.797][silabs ]MATTER RX[0-11]: 55 AA 01 00 34 12 04 00 00 00 00 4A 
[16:16:36.655]  [00:00:08.797][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:36.656]  [00:00:08.797][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:36.656]  
[16:16:36.656]  [00:00:08.797][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:36.660]  [00:00:08.798][silabs ]SPP: pending ack but allow new cmd process
[16:16:36.884]  [00:00:09.028][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:36.884]  [00:00:09.028][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:36.888]  [00:00:09.028][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:36.892]  
[16:16:37.155]  [00:00:09.296][silabs ]MATTER RX[0-11]: 55 AA 01 09 34 12 04 00 00 00 00 53 
[16:16:37.155]  [00:00:09.297][silabs ]SPP: tx_queue full!
[16:16:37.155]  [00:00:09.297][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:37.156]  [00:00:09.297][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:37.158]  
[16:16:37.158]  [00:00:09.297][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:37.384]  [00:00:09.528][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:37.384]  [00:00:09.528][silabs ]MATTER TX[0-7]: 55 AA 01 09 1C 06 00 2B 
[16:16:37.388]  [00:00:09.528][silabs ]COM: CMD: 0x06, SN: 0x091C, LEN: 8
[16:16:37.391]  
[16:16:37.654]  [00:00:09.796][silabs ]MATTER RX[0-11]: 55 AA 01 09 34 12 04 00 00 00 00 53 
[16:16:37.654]  [00:00:09.796][silabs ]SPP: tx_queue full!
[16:16:37.654]  [00:00:09.796][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:37.655]  [00:00:09.796][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:37.658]  
[16:16:37.658]  [00:00:09.797][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:37.886]  [00:00:10.028][silabs ]SPP: re-sent reach to max
[16:16:37.886]  [00:00:10.030][silabs ]MATTER TX[0-7]: 55 AA 01 00 1D 07 00 24 
[16:16:37.886]  [00:00:10.030][silabs ]COM: CMD: 0x07, SN: 0x001D, LEN: 8
[16:16:37.892]  
[16:16:37.892]  [00:00:10.030][silabs ]SPP: ack_timeout_ms 500
[16:16:38.200]  [00:00:10.342][silabs ]MATTER RX[0-8]: 55 AA 01 00 35 06 01 00 3C 
[16:16:38.200]  [00:00:10.343][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0035,len:1
[16:16:38.201]  [00:00:10.343][silabs ]payload[0-0]: 00 
[16:16:38.201]  [00:00:10.343][silabs ]PWR: report Battery Percent 0
[16:16:38.201]  
[16:16:38.201]  [00:00:10.343][silabs ]SPP: pending ack but allow new cmd process
[16:16:38.387]  [00:00:10.531][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:38.387]  [00:00:10.531][silabs ]MATTER TX[0-7]: 55 AA 01 00 1D 07 00 24 
[16:16:38.392]  [00:00:10.531][silabs ]COM: CMD: 0x07, SN: 0x001D, LEN: 8
[16:16:38.392]  
[16:16:38.700]  [00:00:10.842][silabs ]MATTER RX[0-8]: 55 AA 01 09 35 06 01 00 45 
[16:16:38.700]  [00:00:10.842][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0935,len:1
[16:16:38.701]  [00:00:10.843][silabs ]payload[0-0]: 00 
[16:16:38.701]  [00:00:10.843][silabs ]SPP: tx_queue full!
[16:16:38.701]  [00:00:10.843][silabs ]PWR: report Battery Percent 0
[16:16:38.706]  
[16:16:38.889]  [00:00:11.032][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:38.889]  [00:00:11.032][silabs ]MATTER TX[0-7]: 55 AA 01 00 1D 07 00 24 
[16:16:38.891]  [00:00:11.032][silabs ]COM: CMD: 0x07, SN: 0x001D, LEN: 8
[16:16:38.897]  
[16:16:39.200]  [00:00:11.342][silabs ]MATTER RX[0-8]: 55 AA 01 09 35 06 01 00 45 
[16:16:39.200]  [00:00:11.342][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0935,len:1
[16:16:39.201]  [00:00:11.342][silabs ]payload[0-0]: 00 
[16:16:39.201]  [00:00:11.342][silabs ]SPP: tx_queue full!
[16:16:39.201]  [00:00:11.342][silabs ]PWR: report Battery Percent 0
[16:16:39.207]  
[16:16:39.390]  [00:00:11.533][silabs ]SPP: re-sent reach to max
[16:16:39.390]  [00:00:11.533][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:39.390]  [00:00:11.533][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:39.393]  
[16:16:39.393]  [00:00:11.533][silabs ]SPP: ack_timeout_ms 500
[16:16:39.749]  [00:00:11.891][silabs ]MATTER RX[0-8]: 55 AA 01 00 36 07 01 03 41 
[16:16:39.749]  [00:00:11.892][silabs ]PWR: report Battery Charge State 3
[16:16:39.749]  
[16:16:39.753]  [00:00:11.892][silabs ]SPP: pending ack but allow new cmd process
[16:16:39.891]  [00:00:12.034][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:39.891]  [00:00:12.034][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:39.894]  [00:00:12.034][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:39.896]  
[16:16:40.249]  [00:00:12.391][silabs ]MATTER RX[0-8]: 55 AA 01 09 36 07 01 03 4A 
[16:16:40.249]  [00:00:12.391][silabs ]SPP: tx_queue full!
[16:16:40.249]  [00:00:12.392][silabs ]PWR: report Battery Charge State 3
[16:16:40.256]  
[16:16:40.391]  [00:00:12.535][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:40.391]  [00:00:12.535][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:40.397]  [00:00:12.535][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:40.397]  
[16:16:40.748]  [00:00:12.891][silabs ]MATTER RX[0-8]: 55 AA 01 09 36 07 01 03 4A 
[16:16:40.748]  [00:00:12.891][silabs ]SPP: tx_queue full!
[16:16:40.748]  [00:00:12.891][silabs ]PWR: report Battery Charge State 3
[16:16:40.756]  
[16:16:40.892]  [00:00:13.036][silabs ]SPP: re-sent reach to max
[16:16:40.892]  [00:00:13.036][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:40.892]  [00:00:13.036][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:40.896]  
[16:16:40.896]  [00:00:13.036][silabs ]SPP: ack_timeout_ms 500
[16:16:41.301]  [00:00:13.444][silabs ]MATTER RX[0-11]: 55 AA 01 00 39 12 04 00 00 00 00 4F 
[16:16:41.301]  [00:00:13.444][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:41.302]  [00:00:13.444][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:41.302]  
[16:16:41.302]  [00:00:13.445][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:41.306]  [00:00:13.445][silabs ]SPP: pending ack but allow new cmd process
[16:16:41.394]  [00:00:13.537][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:41.394]  [00:00:13.537][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:41.396]  [00:00:13.537][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:41.401]  
[16:16:41.800]  [00:00:13.943][silabs ]MATTER RX[0-11]: 55 AA 01 09 39 12 04 00 00 00 00 58 
[16:16:41.800]  [00:00:13.944][silabs ]SPP: tx_queue full!
[16:16:41.800]  [00:00:13.944][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:41.802]  [00:00:13.944][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:41.805]  
[16:16:41.805]  [00:00:13.944][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:41.894]  [00:00:14.038][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:41.894]  [00:00:14.038][silabs ]MATTER TX[0-7]: 55 AA 01 09 1D 07 00 2D 
[16:16:41.897]  [00:00:14.038][silabs ]COM: CMD: 0x07, SN: 0x091D, LEN: 8
[16:16:41.901]  
[16:16:42.300]  [00:00:14.443][silabs ]MATTER RX[0-11]: 55 AA 01 09 39 12 04 00 00 00 00 58 
[16:16:42.300]  [00:00:14.444][silabs ]SPP: tx_queue full!
[16:16:42.300]  [00:00:14.444][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:42.302]  [00:00:14.444][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:42.305]  
[16:16:42.305]  [00:00:14.444][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:42.396]  [00:00:14.539][silabs ]SPP: re-sent reach to max
[16:16:42.396]  [00:00:14.540][silabs ]MATTER TX[0-7]: 55 AA 01 00 20 12 00 32 
[16:16:42.396]  [00:00:14.540][silabs ]COM: CMD: 0x12, SN: 0x0020, LEN: 8
[16:16:42.401]  
[16:16:42.401]  [00:00:14.540][silabs ]SPP: ack_timeout_ms 500
[16:16:42.850]  [00:00:14.993][silabs ]MATTER RX[0-11]: 55 AA 01 00 48 12 04 00 00 00 00 5E 
[16:16:42.850]  [00:00:14.993][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:42.852]  [00:00:14.994][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:42.852]  
[16:16:42.852]  [00:00:14.994][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:42.856]  [00:00:14.994][silabs ]SPP: pending ack but allow new cmd process
[16:16:42.897]  [00:00:15.041][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:42.897]  [00:00:15.041][silabs ]MATTER TX[0-7]: 55 AA 01 00 20 12 00 32 
[16:16:42.902]  [00:00:15.041][silabs ]COM: CMD: 0x12, SN: 0x0020, LEN: 8
[16:16:42.902]  
[16:16:43.350]  [00:00:15.493][silabs ]MATTER RX[0-11]: 55 AA 01 09 48 12 04 00 00 00 00 67 
[16:16:43.350]  [00:00:15.493][silabs ]SPP: tx_queue full!
[16:16:43.350]  [00:00:15.493][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:43.351]  [00:00:15.493][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:43.356]  
[16:16:43.356]  [00:00:15.493][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:43.399]  [00:00:15.541][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:43.399]  [00:00:15.541][silabs ]MATTER TX[0-7]: 55 AA 01 00 20 12 00 32 
[16:16:43.401]  [00:00:15.541][silabs ]COM: CMD: 0x12, SN: 0x0020, LEN: 8
[16:16:43.406]  
[16:16:43.850]  [00:00:15.992][silabs ]MATTER RX[0-11]: 55 AA 01 09 48 12 04 00 00 00 00 67 
[16:16:43.850]  [00:00:15.993][silabs ]SPP: tx_queue full!
[16:16:43.850]  [00:00:15.993][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:43.851]  [00:00:15.993][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:43.856]  
[16:16:43.856]  [00:00:15.993][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:43.900]  [00:00:16.042][silabs ]SPP: re-sent reach to max
[16:16:43.900]  [00:00:16.043][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:43.900]  [00:00:16.043][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:43.903]  
[16:16:43.903]  [00:00:16.043][silabs ]SPP: ack_timeout_ms 500
[16:16:44.396]  [00:00:16.539][silabs ]MATTER RX[0-8]: 55 AA 01 00 49 06 01 00 50 
[16:16:44.396]  [00:00:16.539][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0049,len:1
[16:16:44.397]  [00:00:16.539][silabs ]payload[0-0]: 00 
[16:16:44.397]  [00:00:16.540][silabs ]PWR: report Battery Percent 0
[16:16:44.397]  
[16:16:44.397]  [00:00:16.540][silabs ]SPP: pending ack but allow new cmd process
[16:16:44.401]  [00:00:16.544][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:44.401]  [00:00:16.544][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:44.406]  [00:00:16.544][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:44.406]  
[16:16:44.895]  [00:00:17.039][silabs ]MATTER RX[0-8]: 55 AA 01 09 49 06 01 00 59 
[16:16:44.895]  [00:00:17.039][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0949,len:1
[16:16:44.897]  [00:00:17.039][silabs ]payload[0-0]: 00 
[16:16:44.897]  [00:00:17.039][silabs ]SPP: tx_queue full!
[16:16:44.897]  [00:00:17.039][silabs ]PWR: report Battery Percent 0
[16:16:44.902]  
[16:16:44.902]  [00:00:17.045][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:44.902]  [00:00:17.045][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:44.906]  [00:00:17.045][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:44.906]  
[16:16:45.395]  [00:00:17.538][silabs ]MATTER RX[0-8]: 55 AA 01 09 49 06 01 00 59 
[16:16:45.395]  [00:00:17.539][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0949,len:1
[16:16:45.396]  [00:00:17.539][silabs ]payload[0-0]: 00 
[16:16:45.396]  [00:00:17.539][silabs ]SPP: tx_queue full!
[16:16:45.396]  [00:00:17.539][silabs ]PWR: report Battery Percent 0
[16:16:45.401]  
[16:16:45.404]  [00:00:17.546][silabs ]SPP: re-sent reach to max
[16:16:45.404]  [00:00:17.547][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:45.404]  [00:00:17.547][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:45.407]  
[16:16:45.407]  [00:00:17.547][silabs ]SPP: ack_timeout_ms 500
[16:16:45.905]  [00:00:18.048][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:45.905]  [00:00:18.048][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:45.908]  [00:00:18.048][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:45.911]  
[16:16:45.945]  [00:00:18.087][silabs ]MATTER RX[0-8]: 55 AA 01 00 4A 07 01 03 55 
[16:16:45.945]  [00:00:18.088][silabs ]PWR: report Battery Charge State 3
[16:16:45.945]  
[16:16:45.948]  [00:00:18.088][silabs ]SPP: pending ack but allow new cmd process
[16:16:46.405]  [00:00:18.549][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:46.405]  [00:00:18.549][silabs ]MATTER TX[0-7]: 55 AA 01 09 20 12 00 3B 
[16:16:46.411]  [00:00:18.549][silabs ]COM: CMD: 0x12, SN: 0x0920, LEN: 8
[16:16:46.411]  
[16:16:46.445]  [00:00:18.587][silabs ]MATTER RX[0-8]: 55 AA 01 09 4A 07 01 03 5E 
[16:16:46.445]  [00:00:18.587][silabs ]SPP: tx_queue full!
[16:16:46.445]  [00:00:18.587][silabs ]PWR: report Battery Charge State 3
[16:16:46.451]  
[16:16:46.907]  [00:00:19.050][silabs ]SPP: re-sent reach to max
[16:16:46.907]  [00:00:19.051][silabs ]MATTER TX[0-7]: 55 AA 01 00 2F 12 00 41 
[16:16:46.907]  [00:00:19.051][silabs ]COM: CMD: 0x12, SN: 0x002F, LEN: 8
[16:16:46.911]  
[16:16:46.911]  [00:00:19.051][silabs ]SPP: ack_timeout_ms 500
[16:16:46.944]  [00:00:19.087][silabs ]MATTER RX[0-8]: 55 AA 01 09 4A 07 01 03 5E 
[16:16:46.944]  [00:00:19.087][silabs ]PWR: report Battery Charge State 3
[16:16:46.944]  
[16:16:46.948]  [00:00:19.087][silabs ]SPP: pending ack but allow new cmd process
[16:16:47.409]  [00:00:19.552][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:47.409]  [00:00:19.552][silabs ]MATTER TX[0-7]: 55 AA 01 00 2F 12 00 41 
[16:16:47.412]  [00:00:19.552][silabs ]COM: CMD: 0x12, SN: 0x002F, LEN: 8
[16:16:47.416]  
[16:16:47.497]  [00:00:19.640][silabs ]MATTER RX[0-11]: 55 AA 01 00 4D 12 04 00 00 00 00 63 
[16:16:47.497]  [00:00:19.640][silabs ]SPP: tx_queue full!
[16:16:47.497]  [00:00:19.640][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:47.498]  [00:00:19.640][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:47.501]  
[16:16:47.501]  [00:00:19.641][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:47.909]  [00:00:20.052][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:47.909]  [00:00:20.052][silabs ]MATTER TX[0-7]: 55 AA 01 00 2F 12 00 41 
[16:16:47.912]  [00:00:20.052][silabs ]COM: CMD: 0x12, SN: 0x002F, LEN: 8
[16:16:47.916]  
[16:16:47.997]  [00:00:20.139][silabs ]MATTER RX[0-11]: 55 AA 01 09 4D 12 04 00 00 00 00 6C 
[16:16:47.997]  [00:00:20.140][silabs ]SPP: tx_queue full!
[16:16:47.997]  [00:00:20.140][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:47.998]  [00:00:20.140][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:48.002]  
[16:16:48.002]  [00:00:20.140][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:48.409]  [00:00:20.552][silabs ]SPP: re-sent reach to max
[16:16:48.409]  [00:00:20.553][silabs ]MATTER TX[0-7]: 55 AA 01 00 34 12 00 46 
[16:16:48.409]  [00:00:20.553][silabs ]COM: CMD: 0x12, SN: 0x0034, LEN: 8
[16:16:48.412]  
[16:16:48.412]  [00:00:20.553][silabs ]SPP: ack_timeout_ms 500
[16:16:48.496]  [00:00:20.639][silabs ]MATTER RX[0-11]: 55 AA 01 09 4D 12 04 00 00 00 00 6C 
[16:16:48.496]  [00:00:20.640][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:48.498]  [00:00:20.640][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:48.498]  
[16:16:48.498]  [00:00:20.640][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:48.501]  [00:00:20.640][silabs ]SPP: pending ack but allow new cmd process
[16:16:48.910]  [00:00:21.053][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:48.910]  [00:00:21.053][silabs ]MATTER TX[0-7]: 55 AA 01 00 34 12 00 46 
[16:16:48.913]  [00:00:21.053][silabs ]COM: CMD: 0x12, SN: 0x0034, LEN: 8
[16:16:48.916]  
[16:16:49.046]  [00:00:21.189][silabs ]MATTER RX[0-11]: 55 AA 01 00 61 12 04 00 00 00 00 77 
[16:16:49.046]  [00:00:21.189][silabs ]SPP: tx_queue full!
[16:16:49.046]  [00:00:21.190][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:49.047]  [00:00:21.190][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:49.050]  
[16:16:49.050]  [00:00:21.190][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:49.410]  [00:00:21.554][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:49.410]  [00:00:21.554][silabs ]MATTER TX[0-7]: 55 AA 01 00 34 12 00 46 
[16:16:49.416]  [00:00:21.554][silabs ]COM: CMD: 0x12, SN: 0x0034, LEN: 8
[16:16:49.416]  
[16:16:49.546]  [00:00:21.689][silabs ]MATTER RX[0-11]: 55 AA 01 09 61 12 04 00 00 00 00 80 
[16:16:49.546]  [00:00:21.689][silabs ]SPP: tx_queue full!
[16:16:49.546]  [00:00:21.689][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:49.547]  [00:00:21.689][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:49.550]  
[16:16:49.550]  [00:00:21.690][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:49.911]  [00:00:22.054][silabs ]SPP: re-sent reach to max
[16:16:49.911]  [00:00:22.055][silabs ]MATTER TX[0-7]: 55 AA 01 00 35 06 00 3B 
[16:16:49.911]  [00:00:22.055][silabs ]COM: CMD: 0x06, SN: 0x0035, LEN: 8
[16:16:49.915]  
[16:16:49.915]  [00:00:22.055][silabs ]SPP: ack_timeout_ms 500
[16:16:50.046]  [00:00:22.189][silabs ]MATTER RX[0-11]: 55 AA 01 09 61 12 04 00 00 00 00 80 
[16:16:50.046]  [00:00:22.189][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:50.047]  [00:00:22.189][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:50.047]  
[16:16:50.047]  [00:00:22.189][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:50.050]  [00:00:22.190][silabs ]SPP: pending ack but allow new cmd process
[16:16:50.412]  [00:00:22.555][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:50.412]  [00:00:22.555][silabs ]MATTER TX[0-7]: 55 AA 01 00 35 06 00 3B 
[16:16:50.415]  [00:00:22.555][silabs ]COM: CMD: 0x06, SN: 0x0035, LEN: 8
[16:16:50.415]  
[16:16:50.592]  [00:00:22.735][silabs ]MATTER RX[0-8]: 55 AA 01 00 62 06 01 00 69 
[16:16:50.592]  [00:00:22.735][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0062,len:1
[16:16:50.593]  [00:00:22.736][silabs ]payload[0-0]: 00 
[16:16:50.593]  [00:00:22.736][silabs ]SPP: tx_queue full!
[16:16:50.593]  [00:00:22.736][silabs ]PWR: report Battery Percent 0
[16:16:50.601]  
[16:16:50.911]  [00:00:23.055][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:50.911]  [00:00:23.055][silabs ]MATTER TX[0-7]: 55 AA 01 00 35 06 00 3B 
[16:16:50.916]  [00:00:23.055][silabs ]COM: CMD: 0x06, SN: 0x0035, LEN: 8
[16:16:50.916]  
[16:16:51.092]  [00:00:23.235][silabs ]MATTER RX[0-8]: 55 AA 01 09 62 06 01 00 72 
[16:16:51.092]  [00:00:23.235][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0962,len:1
[16:16:51.093]  [00:00:23.235][silabs ]payload[0-0]: 00 
[16:16:51.093]  [00:00:23.235][silabs ]SPP: tx_queue full!
[16:16:51.093]  [00:00:23.236][silabs ]PWR: report Battery Percent 0
[16:16:51.100]  
[16:16:51.412]  [00:00:23.555][silabs ]SPP: re-sent reach to max
[16:16:51.412]  [00:00:23.556][silabs ]MATTER TX[0-7]: 55 AA 01 00 36 07 00 3D 
[16:16:51.412]  [00:00:23.556][silabs ]COM: CMD: 0x07, SN: 0x0036, LEN: 8
[16:16:51.416]  
[16:16:51.416]  [00:00:23.556][silabs ]SPP: ack_timeout_ms 500
[16:16:51.591]  [00:00:23.734][silabs ]MATTER RX[0-8]: 55 AA 01 09 62 06 01 00 72 
[16:16:51.591]  [00:00:23.735][silabs ]COM: spp_app_event_BatteryLevel,sn:0x0962,len:1
[16:16:51.592]  [00:00:23.735][silabs ]payload[0-0]: 00 
[16:16:51.592]  [00:00:23.735][silabs ]PWR: report Battery Percent 0
[16:16:51.592]  
[16:16:51.592]  [00:00:23.735][silabs ]SPP: pending ack but allow new cmd process
[16:16:51.913]  [00:00:24.056][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:51.913]  [00:00:24.056][silabs ]MATTER TX[0-7]: 55 AA 01 00 36 07 00 3D 
[16:16:51.916]  [00:00:24.056][silabs ]COM: CMD: 0x07, SN: 0x0036, LEN: 8
[16:16:51.921]  
[16:16:52.141]  [00:00:24.284][silabs ]MATTER RX[0-8]: 55 AA 01 00 63 07 01 03 6E 
[16:16:52.141]  [00:00:24.285][silabs ]SPP: tx_queue full!
[16:16:52.141]  [00:00:24.285][silabs ]PWR: report Battery Charge State 3
[16:16:52.146]  
[16:16:52.412]  [00:00:24.556][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:52.412]  [00:00:24.556][silabs ]MATTER TX[0-7]: 55 AA 01 00 36 07 00 3D 
[16:16:52.416]  [00:00:24.556][silabs ]COM: CMD: 0x07, SN: 0x0036, LEN: 8
[16:16:52.421]  
[16:16:52.640]  [00:00:24.784][silabs ]MATTER RX[0-8]: 55 AA 01 09 63 07 01 03 77 
[16:16:52.640]  [00:00:24.784][silabs ]SPP: tx_queue full!
[16:16:52.640]  [00:00:24.785][silabs ]PWR: report Battery Charge State 3
[16:16:52.646]  
[16:16:52.913]  [00:00:25.056][silabs ]SPP: re-sent reach to max
[16:16:52.913]  [00:00:25.057][silabs ]MATTER TX[0-7]: 55 AA 01 00 39 12 00 4B 
[16:16:52.913]  [00:00:25.057][silabs ]COM: CMD: 0x12, SN: 0x0039, LEN: 8
[16:16:52.916]  
[16:16:52.916]  [00:00:25.057][silabs ]SPP: ack_timeout_ms 500
[16:16:53.140]  [00:00:25.284][silabs ]MATTER RX[0-8]: 55 AA 01 09 63 07 01 03 77 
[16:16:53.140]  [00:00:25.284][silabs ]PWR: report Battery Charge State 3
[16:16:53.140]  
[16:16:53.146]  [00:00:25.284][silabs ]SPP: pending ack but allow new cmd process
[16:16:53.414]  [00:00:25.557][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:53.414]  [00:00:25.557][silabs ]MATTER TX[0-7]: 55 AA 01 00 39 12 00 4B 
[16:16:53.417]  [00:00:25.557][silabs ]COM: CMD: 0x12, SN: 0x0039, LEN: 8
[16:16:53.420]  
[16:16:53.694]  [00:00:25.836][silabs ]MATTER RX[0-11]: 55 AA 01 00 66 12 04 00 00 00 00 7C 
[16:16:53.694]  [00:00:25.836][silabs ]SPP: tx_queue full!
[16:16:53.694]  [00:00:25.836][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:53.695]  [00:00:25.837][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:53.698]  
[16:16:53.698]  [00:00:25.837][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:53.913]  [00:00:26.057][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:53.913]  [00:00:26.057][silabs ]MATTER TX[0-7]: 55 AA 01 00 39 12 00 4B 
[16:16:53.917]  [00:00:26.057][silabs ]COM: CMD: 0x12, SN: 0x0039, LEN: 8
[16:16:53.920]  
[16:16:54.193]  [00:00:26.336][silabs ]MATTER RX[0-11]: 55 AA 01 09 66 12 04 00 00 00 00 85 
[16:16:54.193]  [00:00:26.336][silabs ]SPP: tx_queue full!
[16:16:54.193]  [00:00:26.336][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:54.194]  [00:00:26.336][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:54.198]  
[16:16:54.198]  [00:00:26.337][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:54.414]  [00:00:26.557][silabs ]SPP: re-sent reach to max
[16:16:54.414]  [00:00:26.558][silabs ]MATTER TX[0-7]: 55 AA 01 00 48 12 00 5A 
[16:16:54.414]  [00:00:26.558][silabs ]COM: CMD: 0x12, SN: 0x0048, LEN: 8
[16:16:54.417]  
[16:16:54.417]  [00:00:26.558][silabs ]SPP: ack_timeout_ms 500
[16:16:54.693]  [00:00:26.836][silabs ]MATTER RX[0-11]: 55 AA 01 09 66 12 04 00 00 00 00 85 
[16:16:54.693]  [00:00:26.836][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:54.695]  [00:00:26.836][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:54.695]  
[16:16:54.695]  [00:00:26.836][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:54.697]  [00:00:26.837][silabs ]SPP: pending ack but allow new cmd process
[16:16:54.914]  [00:00:27.058][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:54.914]  [00:00:27.058][silabs ]MATTER TX[0-7]: 55 AA 01 00 48 12 00 5A 
[16:16:54.918]  [00:00:27.058][silabs ]COM: CMD: 0x12, SN: 0x0048, LEN: 8
[16:16:54.921]  
[16:16:55.243]  [00:00:27.386][silabs ]MATTER RX[0-11]: 55 AA 01 00 7A 12 04 00 00 00 00 90 
[16:16:55.243]  [00:00:27.386][silabs ]SPP: tx_queue full!
[16:16:55.243]  [00:00:27.386][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:55.244]  [00:00:27.386][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:55.247]  
[16:16:55.247]  [00:00:27.386][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:55.414]  [00:00:27.558][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:55.414]  [00:00:27.558][silabs ]MATTER TX[0-7]: 55 AA 01 00 48 12 00 5A 
[16:16:55.418]  [00:00:27.558][silabs ]COM: CMD: 0x12, SN: 0x0048, LEN: 8
[16:16:55.421]  
[16:16:55.742]  [00:00:27.885][silabs ]MATTER RX[0-11]: 55 AA 01 09 7A 12 04 00 00 00 00 99 
[16:16:55.742]  [00:00:27.886][silabs ]SPP: tx_queue full!
[16:16:55.742]  [00:00:27.886][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:55.744]  [00:00:27.886][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:55.747]  
[16:16:55.747]  [00:00:27.886][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:55.914]  [00:00:28.058][silabs ]SPP: re-sent reach to max
[16:16:55.914]  [00:00:28.059][silabs ]MATTER TX[0-7]: 55 AA 01 00 49 06 00 4F 
[16:16:55.914]  [00:00:28.059][silabs ]COM: CMD: 0x06, SN: 0x0049, LEN: 8
[16:16:55.921]  
[16:16:55.921]  [00:00:28.059][silabs ]SPP: ack_timeout_ms 500
[16:16:56.242]  [00:00:28.385][silabs ]MATTER RX[0-11]: 55 AA 01 09 7A 12 04 00 00 00 00 99 
[16:16:56.242]  [00:00:28.386][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:56.243]  [00:00:28.386][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:56.243]  
[16:16:56.243]  [00:00:28.386][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:56.247]  [00:00:28.386][silabs ]SPP: pending ack but allow new cmd process
[16:16:56.415]  [00:00:28.559][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:56.415]  [00:00:28.559][silabs ]MATTER TX[0-7]: 55 AA 01 00 49 06 00 4F 
[16:16:56.421]  [00:00:28.559][silabs ]COM: CMD: 0x06, SN: 0x0049, LEN: 8
[16:16:56.421]  
[16:16:56.789]  [00:00:28.932][silabs ]MATTER RX[0-8]: 55 AA 01 00 7B 06 01 00 82 
[16:16:56.789]  [00:00:28.932][silabs ]COM: spp_app_event_BatteryLevel,sn:0x007B,len:1
[16:16:56.790]  [00:00:28.932][silabs ]payload[0-0]: 00 
[16:16:56.790]  [00:00:28.932][silabs ]SPP: tx_queue full!
[16:16:56.790]  [00:00:28.933][silabs ]PWR: report Battery Percent 0
[16:16:56.796]  
[16:16:56.915]  [00:00:29.059][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:56.915]  [00:00:29.059][silabs ]MATTER TX[0-7]: 55 AA 01 00 49 06 00 4F 
[16:16:56.920]  [00:00:29.059][silabs ]COM: CMD: 0x06, SN: 0x0049, LEN: 8
[16:16:56.920]  
[16:16:57.288]  [00:00:29.432][silabs ]MATTER RX[0-8]: 55 AA 01 09 7B 06 01 00 8B 
[16:16:57.288]  [00:00:29.432][silabs ]COM: spp_app_event_BatteryLevel,sn:0x097B,len:1
[16:16:57.290]  [00:00:29.432][silabs ]payload[0-0]: 00 
[16:16:57.290]  [00:00:29.432][silabs ]SPP: tx_queue full!
[16:16:57.290]  [00:00:29.432][silabs ]PWR: report Battery Percent 0
[16:16:57.295]  
[16:16:57.415]  [00:00:29.559][silabs ]SPP: re-sent reach to max
[16:16:57.415]  [00:00:29.560][silabs ]MATTER TX[0-7]: 55 AA 01 00 4A 07 00 51 
[16:16:57.415]  [00:00:29.560][silabs ]COM: CMD: 0x07, SN: 0x004A, LEN: 8
[16:16:57.420]  
[16:16:57.420]  [00:00:29.560][silabs ]SPP: ack_timeout_ms 500
[16:16:57.788]  [00:00:29.931][silabs ]MATTER RX[0-8]: 55 AA 01 09 7B 06 01 00 8B 
[16:16:57.788]  [00:00:29.932][silabs ]COM: spp_app_event_BatteryLevel,sn:0x097B,len:1
[16:16:57.789]  [00:00:29.932][silabs ]payload[0-0]: 00 
[16:16:57.789]  [00:00:29.932][silabs ]PWR: report Battery Percent 0
[16:16:57.789]  
[16:16:57.789]  [00:00:29.932][silabs ]SPP: pending ack but allow new cmd process
[16:16:57.916]  [00:00:30.060][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:57.916]  [00:00:30.060][silabs ]MATTER TX[0-7]: 55 AA 01 00 4A 07 00 51 
[16:16:57.920]  [00:00:30.060][silabs ]COM: CMD: 0x07, SN: 0x004A, LEN: 8
[16:16:57.920]  
[16:16:58.341]  [00:00:30.485][silabs ]MATTER RX[0-11]: 55 AA 01 00 7F 12 04 00 00 00 00 95 
[16:16:58.341]  [00:00:30.485][silabs ]SPP: tx_queue full!
[16:16:58.341]  [00:00:30.485][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:58.343]  [00:00:30.485][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:58.345]  
[16:16:58.345]  [00:00:30.485][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:58.416]  [00:00:30.560][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:58.416]  [00:00:30.560][silabs ]MATTER TX[0-7]: 55 AA 01 00 4A 07 00 51 
[16:16:58.421]  [00:00:30.560][silabs ]COM: CMD: 0x07, SN: 0x004A, LEN: 8
[16:16:58.421]  
[16:16:58.840]  [00:00:30.984][silabs ]MATTER RX[0-11]: 55 AA 01 09 7F 12 04 00 00 00 00 9E 
[16:16:58.840]  [00:00:30.985][silabs ]SPP: tx_queue full!
[16:16:58.840]  [00:00:30.985][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:58.843]  [00:00:30.985][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:58.846]  
[16:16:58.846]  [00:00:30.985][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:58.917]  [00:00:31.060][silabs ]SPP: re-sent reach to max
[16:16:58.917]  [00:00:31.061][silabs ]MATTER TX[0-7]: 55 AA 01 09 4A 07 00 5A 
[16:16:58.917]  [00:00:31.061][silabs ]COM: CMD: 0x07, SN: 0x094A, LEN: 8
[16:16:58.920]  
[16:16:58.920]  [00:00:31.061][silabs ]SPP: ack_timeout_ms 500
[16:16:59.340]  [00:00:31.484][silabs ]MATTER RX[0-11]: 55 AA 01 09 7F 12 04 00 00 00 00 9E 
[16:16:59.340]  [00:00:31.485][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:59.342]  [00:00:31.485][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:59.342]  
[16:16:59.342]  [00:00:31.485][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:59.345]  [00:00:31.485][silabs ]SPP: pending ack but allow new cmd process
[16:16:59.416]  [00:00:31.561][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:16:59.416]  [00:00:31.561][silabs ]MATTER TX[0-7]: 55 AA 01 09 4A 07 00 5A 
[16:16:59.420]  [00:00:31.561][silabs ]COM: CMD: 0x07, SN: 0x094A, LEN: 8
[16:16:59.425]  
[16:16:59.890]  [00:00:32.034][silabs ]MATTER RX[0-11]: 55 AA 01 00 8E 12 04 00 00 00 00 A4 
[16:16:59.890]  [00:00:32.034][silabs ]SPP: tx_queue full!
[16:16:59.890]  [00:00:32.035][silabs ]WDC: report Active percent 0 dev_index 1
[16:16:59.892]  [00:00:32.035][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:16:59.895]  
[16:16:59.895]  [00:00:32.035][info  ][ZCL] Lift[1] Position Set: 10000
[16:16:59.918]  [00:00:32.061][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:16:59.918]  [00:00:32.061][silabs ]MATTER TX[0-7]: 55 AA 01 09 4A 07 00 5A 
[16:16:59.920]  [00:00:32.061][silabs ]COM: CMD: 0x07, SN: 0x094A, LEN: 8
[16:16:59.925]  
[16:17:00.390]  [00:00:32.534][silabs ]MATTER RX[0-11]: 55 AA 01 09 8E 12 04 00 00 00 00 AD 
[16:17:00.390]  [00:00:32.534][silabs ]SPP: tx_queue full!
[16:17:00.390]  [00:00:32.534][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:00.391]  [00:00:32.534][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:00.394]  
[16:17:00.394]  [00:00:32.535][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:00.417]  [00:00:32.561][silabs ]SPP: re-sent reach to max
[16:17:00.417]  [00:00:32.562][silabs ]MATTER TX[0-7]: 55 AA 01 09 4D 12 00 68 
[16:17:00.417]  [00:00:32.562][silabs ]COM: CMD: 0x12, SN: 0x094D, LEN: 8
[16:17:00.421]  
[16:17:00.421]  [00:00:32.562][silabs ]SPP: ack_timeout_ms 500
[16:17:00.890]  [00:00:33.034][silabs ]MATTER RX[0-11]: 55 AA 01 09 8E 12 04 00 00 00 00 AD 
[16:17:00.890]  [00:00:33.034][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:00.892]  [00:00:33.034][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:00.892]  
[16:17:00.892]  [00:00:33.034][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:00.895]  [00:00:33.035][silabs ]SPP: pending ack but allow new cmd process
[16:17:00.918]  [00:00:33.062][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:00.918]  [00:00:33.062][silabs ]MATTER TX[0-7]: 55 AA 01 09 4D 12 00 68 
[16:17:00.921]  [00:00:33.062][silabs ]COM: CMD: 0x12, SN: 0x094D, LEN: 8
[16:17:00.925]  
[16:17:01.418]  [00:00:33.562][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:01.418]  [00:00:33.562][silabs ]MATTER TX[0-7]: 55 AA 01 09 4D 12 00 68 
[16:17:01.421]  [00:00:33.562][silabs ]COM: CMD: 0x12, SN: 0x094D, LEN: 8
[16:17:01.425]  
[16:17:01.440]  [00:00:33.583][silabs ]MATTER RX[0-11]: 55 AA 01 00 A2 12 04 00 00 00 00 B8 
[16:17:01.440]  [00:00:33.583][silabs ]SPP: tx_queue full!
[16:17:01.440]  [00:00:33.583][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:01.441]  [00:00:33.583][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:01.444]  
[16:17:01.444]  [00:00:33.583][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:01.918]  [00:00:34.062][silabs ]SPP: re-sent reach to max
[16:17:01.918]  [00:00:34.063][silabs ]MATTER TX[0-7]: 55 AA 01 09 61 12 00 7C 
[16:17:01.918]  [00:00:34.063][silabs ]COM: CMD: 0x12, SN: 0x0961, LEN: 8
[16:17:01.922]  
[16:17:01.922]  [00:00:34.063][silabs ]SPP: ack_timeout_ms 500
[16:17:01.940]  [00:00:34.083][silabs ]MATTER RX[0-11]: 55 AA 01 09 A2 12 04 00 00 00 00 C1 
[16:17:01.940]  [00:00:34.083][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:01.940]  [00:00:34.083][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:01.940]  
[16:17:01.940]  [00:00:34.083][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:01.945]  [00:00:34.083][silabs ]SPP: pending ack but allow new cmd process
[16:17:02.419]  [00:00:34.563][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:02.419]  [00:00:34.563][silabs ]MATTER TX[0-7]: 55 AA 01 09 61 12 00 7C 
[16:17:02.422]  [00:00:34.563][silabs ]COM: CMD: 0x12, SN: 0x0961, LEN: 8
[16:17:02.425]  
[16:17:02.439]  [00:00:34.583][silabs ]MATTER RX[0-11]: 55 AA 01 09 A2 12 04 00 00 00 00 C1 
[16:17:02.439]  [00:00:34.583][silabs ]SPP: tx_queue full!
[16:17:02.439]  [00:00:34.583][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:02.441]  [00:00:34.583][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:02.444]  
[16:17:02.444]  [00:00:34.583][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:02.919]  [00:00:35.063][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:02.919]  [00:00:35.063][silabs ]MATTER TX[0-7]: 55 AA 01 09 61 12 00 7C 
[16:17:02.922]  [00:00:35.063][silabs ]COM: CMD: 0x12, SN: 0x0961, LEN: 8
[16:17:02.925]  
[16:17:02.985]  [00:00:35.129][silabs ]MATTER RX[0-8]: 55 AA 01 00 A3 06 01 00 AA 
[16:17:02.985]  [00:00:35.129][silabs ]COM: spp_app_event_BatteryLevel,sn:0x00A3,len:1
[16:17:02.987]  [00:00:35.129][silabs ]payload[0-0]: 00 
[16:17:02.987]  [00:00:35.129][silabs ]SPP: tx_queue full!
[16:17:02.987]  [00:00:35.130][silabs ]PWR: report Battery Percent 0
[16:17:02.995]  
[16:17:03.420]  [00:00:35.563][silabs ]SPP: re-sent reach to max
[16:17:03.420]  [00:00:35.564][silabs ]MATTER TX[0-7]: 55 AA 01 09 62 06 00 71 
[16:17:03.420]  [00:00:35.564][silabs ]COM: CMD: 0x06, SN: 0x0962, LEN: 8
[16:17:03.425]  
[16:17:03.425]  [00:00:35.564][silabs ]SPP: ack_timeout_ms 500
[16:17:03.486]  [00:00:35.629][silabs ]MATTER RX[0-8]: 55 AA 01 09 A3 06 01 00 B3 
[16:17:03.486]  [00:00:35.629][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09A3,len:1
[16:17:03.486]  [00:00:35.629][silabs ]payload[0-0]: 00 
[16:17:03.486]  [00:00:35.629][silabs ]PWR: report Battery Percent 0
[16:17:03.486]  
[16:17:03.486]  [00:00:35.630][silabs ]SPP: pending ack but allow new cmd process
[16:17:03.920]  [00:00:36.064][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:03.920]  [00:00:36.064][silabs ]MATTER TX[0-7]: 55 AA 01 09 62 06 00 71 
[16:17:03.925]  [00:00:36.064][silabs ]COM: CMD: 0x06, SN: 0x0962, LEN: 8
[16:17:03.925]  
[16:17:03.985]  [00:00:36.128][silabs ]MATTER RX[0-8]: 55 AA 01 09 A3 06 01 00 B3 
[16:17:03.985]  [00:00:36.129][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09A3,len:1
[16:17:03.986]  [00:00:36.129][silabs ]payload[0-0]: 00 
[16:17:03.986]  [00:00:36.129][silabs ]SPP: tx_queue full!
[16:17:03.986]  [00:00:36.129][silabs ]PWR: report Battery Percent 0
[16:17:03.990]  
[16:17:04.419]  [00:00:36.564][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:04.419]  [00:00:36.564][silabs ]MATTER TX[0-7]: 55 AA 01 09 62 06 00 71 
[16:17:04.425]  [00:00:36.564][silabs ]COM: CMD: 0x06, SN: 0x0962, LEN: 8
[16:17:04.425]  
[16:17:04.535]  [00:00:36.678][silabs ]MATTER RX[0-8]: 55 AA 01 00 A4 07 01 03 AF 
[16:17:04.535]  [00:00:36.679][silabs ]SPP: tx_queue full!
[16:17:04.535]  [00:00:36.679][silabs ]PWR: report Battery Charge State 3
[16:17:04.540]  
[16:17:04.920]  [00:00:37.064][silabs ]SPP: re-sent reach to max
[16:17:04.920]  [00:00:37.065][silabs ]MATTER TX[0-7]: 55 AA 01 09 63 07 00 73 
[16:17:04.920]  [00:00:37.065][silabs ]COM: CMD: 0x07, SN: 0x0963, LEN: 8
[16:17:04.925]  
[16:17:04.925]  [00:00:37.065][silabs ]SPP: ack_timeout_ms 500
[16:17:05.034]  [00:00:37.178][silabs ]MATTER RX[0-8]: 55 AA 01 09 A4 07 01 03 B8 
[16:17:05.034]  [00:00:37.178][silabs ]PWR: report Battery Charge State 3
[16:17:05.034]  
[16:17:05.040]  [00:00:37.179][silabs ]SPP: pending ack but allow new cmd process
[16:17:05.421]  [00:00:37.565][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:05.421]  [00:00:37.565][silabs ]MATTER TX[0-7]: 55 AA 01 09 63 07 00 73 
[16:17:05.425]  [00:00:37.565][silabs ]COM: CMD: 0x07, SN: 0x0963, LEN: 8
[16:17:05.425]  
[16:17:05.534]  [00:00:37.678][silabs ]MATTER RX[0-8]: 55 AA 01 09 A4 07 01 03 B8 
[16:17:05.534]  [00:00:37.678][silabs ]SPP: tx_queue full!
[16:17:05.534]  [00:00:37.678][silabs ]PWR: report Battery Charge State 3
[16:17:05.540]  
[16:17:05.920]  [00:00:38.065][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:05.920]  [00:00:38.065][silabs ]MATTER TX[0-7]: 55 AA 01 09 63 07 00 73 
[16:17:05.924]  [00:00:38.065][silabs ]COM: CMD: 0x07, SN: 0x0963, LEN: 8
[16:17:05.924]  
[16:17:06.088]  [00:00:38.231][silabs ]MATTER RX[0-11]: 55 AA 01 00 A7 12 04 00 00 00 00 BD 
[16:17:06.088]  [00:00:38.231][silabs ]SPP: tx_queue full!
[16:17:06.088]  [00:00:38.231][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:06.089]  [00:00:38.232][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:06.092]  
[16:17:06.092]  [00:00:38.232][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:06.421]  [00:00:38.565][silabs ]SPP: re-sent reach to max
[16:17:06.421]  [00:00:38.566][silabs ]MATTER TX[0-7]: 55 AA 01 09 66 12 00 81 
[16:17:06.421]  [00:00:38.566][silabs ]COM: CMD: 0x12, SN: 0x0966, LEN: 8
[16:17:06.424]  
[16:17:06.424]  [00:00:38.566][silabs ]SPP: ack_timeout_ms 500
[16:17:06.587]  [00:00:38.731][silabs ]MATTER RX[0-11]: 55 AA 01 09 A7 12 04 00 00 00 00 C6 
[16:17:06.587]  [00:00:38.731][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:06.589]  [00:00:38.731][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:06.589]  
[16:17:06.589]  [00:00:38.731][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:06.592]  [00:00:38.732][silabs ]SPP: pending ack but allow new cmd process
[16:17:06.921]  [00:00:39.066][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:06.921]  [00:00:39.066][silabs ]MATTER TX[0-7]: 55 AA 01 09 66 12 00 81 
[16:17:06.925]  [00:00:39.066][silabs ]COM: CMD: 0x12, SN: 0x0966, LEN: 8
[16:17:06.930]  
[16:17:07.086]  [00:00:39.230][silabs ]MATTER RX[0-11]: 55 AA 01 09 A7 12 04 00 00 00 00 C6 
[16:17:07.086]  [00:00:39.231][silabs ]SPP: tx_queue full!
[16:17:07.086]  [00:00:39.231][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:07.087]  [00:00:39.231][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:07.091]  
[16:17:07.091]  [00:00:39.231][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:07.422]  [00:00:39.566][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:07.422]  [00:00:39.566][silabs ]MATTER TX[0-7]: 55 AA 01 09 66 12 00 81 
[16:17:07.425]  [00:00:39.566][silabs ]COM: CMD: 0x12, SN: 0x0966, LEN: 8
[16:17:07.430]  
[16:17:07.636]  [00:00:39.780][silabs ]MATTER RX[0-11]: 55 AA 01 00 B6 12 04 00 00 00 00 CC 
[16:17:07.636]  [00:00:39.780][silabs ]SPP: tx_queue full!
[16:17:07.636]  [00:00:39.780][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:07.637]  [00:00:39.781][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:07.641]  
[16:17:07.641]  [00:00:39.781][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:07.923]  [00:00:40.066][silabs ]SPP: re-sent reach to max
[16:17:07.923]  [00:00:40.067][silabs ]MATTER TX[0-7]: 55 AA 01 09 7A 12 00 95 
[16:17:07.923]  [00:00:40.067][silabs ]COM: CMD: 0x12, SN: 0x097A, LEN: 8
[16:17:07.926]  
[16:17:07.926]  [00:00:40.067][silabs ]SPP: ack_timeout_ms 500
[16:17:08.136]  [00:00:40.280][silabs ]MATTER RX[0-11]: 55 AA 01 09 B6 12 04 00 00 00 00 D5 
[16:17:08.136]  [00:00:40.280][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:08.137]  [00:00:40.280][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:08.137]  
[16:17:08.137]  [00:00:40.280][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:08.141]  [00:00:40.281][silabs ]SPP: pending ack but allow new cmd process
[16:17:08.423]  [00:00:40.567][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:08.423]  [00:00:40.567][silabs ]MATTER TX[0-7]: 55 AA 01 09 7A 12 00 95 
[16:17:08.425]  [00:00:40.567][silabs ]COM: CMD: 0x12, SN: 0x097A, LEN: 8
[16:17:08.425]  
[16:17:08.635]  [00:00:40.779][silabs ]MATTER RX[0-11]: 55 AA 01 09 B6 12 04 00 00 00 00 D5 
[16:17:08.635]  [00:00:40.780][silabs ]SPP: tx_queue full!
[16:17:08.635]  [00:00:40.780][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:08.636]  [00:00:40.780][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:08.640]  
[16:17:08.640]  [00:00:40.780][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:08.923]  [00:00:41.067][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:08.923]  [00:00:41.067][silabs ]MATTER TX[0-7]: 55 AA 01 09 7A 12 00 95 
[16:17:08.926]  [00:00:41.067][silabs ]COM: CMD: 0x12, SN: 0x097A, LEN: 8
[16:17:08.926]  
[16:17:09.185]  [00:00:41.329][silabs ]MATTER RX[0-11]: 55 AA 01 00 CA 12 04 00 00 00 00 E0 
[16:17:09.185]  [00:00:41.330][silabs ]SPP: tx_queue full!
[16:17:09.185]  [00:00:41.330][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:09.186]  [00:00:41.330][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:09.189]  
[16:17:09.189]  [00:00:41.330][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:09.423]  [00:00:41.567][silabs ]SPP: re-sent reach to max
[16:17:09.423]  [00:00:41.568][silabs ]MATTER TX[0-7]: 55 AA 01 09 7B 06 00 8A 
[16:17:09.423]  [00:00:41.568][silabs ]COM: CMD: 0x06, SN: 0x097B, LEN: 8
[16:17:09.426]  
[16:17:09.426]  [00:00:41.568][silabs ]SPP: ack_timeout_ms 500
[16:17:09.684]  [00:00:41.829][silabs ]MATTER RX[0-11]: 55 AA 01 09 CA 12 04 00 00 00 00 E9 
[16:17:09.684]  [00:00:41.829][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:09.686]  [00:00:41.829][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:09.686]  
[16:17:09.686]  [00:00:41.830][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:09.690]  [00:00:41.830][silabs ]SPP: pending ack but allow new cmd process
[16:17:09.924]  [00:00:42.068][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:09.924]  [00:00:42.068][silabs ]MATTER TX[0-7]: 55 AA 01 09 7B 06 00 8A 
[16:17:09.927]  [00:00:42.068][silabs ]COM: CMD: 0x06, SN: 0x097B, LEN: 8
[16:17:09.930]  
[16:17:10.184]  [00:00:42.329][silabs ]MATTER RX[0-11]: 55 AA 01 09 CA 12 04 00 00 00 00 E9 
[16:17:10.184]  [00:00:42.329][silabs ]SPP: tx_queue full!
[16:17:10.184]  [00:00:42.329][silabs ]WDC: report Active percent 0 dev_index 1
[16:17:10.186]  [00:00:42.329][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:17:10.189]  
[16:17:10.189]  [00:00:42.329][info  ][ZCL] Lift[1] Position Set: 10000
[16:17:10.424]  [00:00:42.568][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:10.424]  [00:00:42.568][silabs ]MATTER TX[0-7]: 55 AA 01 09 7B 06 00 8A 
[16:17:10.427]  [00:00:42.568][silabs ]COM: CMD: 0x06, SN: 0x097B, LEN: 8
[16:17:10.429]  
[16:17:10.731]  [00:00:42.875][silabs ]MATTER RX[0-8]: 55 AA 01 00 CB 06 01 00 D2 
[16:17:10.731]  [00:00:42.875][silabs ]COM: spp_app_event_BatteryLevel,sn:0x00CB,len:1
[16:17:10.732]  [00:00:42.875][silabs ]payload[0-0]: 00 
[16:17:10.732]  [00:00:42.875][silabs ]SPP: tx_queue full!
[16:17:10.732]  [00:00:42.875][silabs ]PWR: report Battery Percent 0
[16:17:10.740]  
[16:17:10.924]  [00:00:43.068][silabs ]SPP: re-sent reach to max
[16:17:10.924]  [00:00:43.069][silabs ]MATTER TX[0-7]: 55 AA 01 09 7F 12 00 9A 
[16:17:10.924]  [00:00:43.069][silabs ]COM: CMD: 0x12, SN: 0x097F, LEN: 8
[16:17:10.927]  
[16:17:10.927]  [00:00:43.069][silabs ]SPP: ack_timeout_ms 500
[16:17:11.231]  [00:00:43.375][silabs ]MATTER RX[0-8]: 55 AA 01 09 CB 06 01 00 DB 
[16:17:11.231]  [00:00:43.375][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09CB,len:1
[16:17:11.232]  [00:00:43.375][silabs ]payload[0-0]: 00 
[16:17:11.232]  [00:00:43.375][silabs ]PWR: report Battery Percent 0
[16:17:11.232]  
[16:17:11.232]  [00:00:43.375][silabs ]SPP: pending ack but allow new cmd process
[16:17:11.425]  [00:00:43.569][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:11.425]  [00:00:43.569][silabs ]MATTER TX[0-7]: 55 AA 01 09 7F 12 00 9A 
[16:17:11.430]  [00:00:43.569][silabs ]COM: CMD: 0x12, SN: 0x097F, LEN: 8
[16:17:11.430]  
[16:17:11.730]  [00:00:43.875][silabs ]MATTER RX[0-8]: 55 AA 01 09 CB 06 01 00 DB 
[16:17:11.730]  [00:00:43.875][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09CB,len:1
[16:17:11.732]  [00:00:43.875][silabs ]payload[0-0]: 00 
[16:17:11.732]  [00:00:43.875][silabs ]SPP: tx_queue full!
[16:17:11.732]  [00:00:43.875][silabs ]PWR: report Battery Percent 0
[16:17:11.739]  
[16:17:11.925]  [00:00:44.069][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:11.925]  [00:00:44.069][silabs ]MATTER TX[0-7]: 55 AA 01 09 7F 12 00 9A 
[16:17:11.930]  [00:00:44.069][silabs ]COM: CMD: 0x12, SN: 0x097F, LEN: 8
[16:17:11.930]  
[16:17:12.279]  [00:00:44.423][silabs ]MATTER RX[0-8]: 55 AA 01 00 CC 07 01 03 D7 
[16:17:12.279]  [00:00:44.424][silabs ]SPP: tx_queue full!
[16:17:12.279]  [00:00:44.424][silabs ]PWR: report Battery Charge State 3
[16:17:12.285]  
[16:17:12.426]  [00:00:44.569][silabs ]SPP: re-sent reach to max
[16:17:12.426]  [00:00:44.571][silabs ]MATTER TX[0-7]: 55 AA 01 09 8E 12 00 A9 
[16:17:12.426]  [00:00:44.571][silabs ]COM: CMD: 0x12, SN: 0x098E, LEN: 8
[16:17:12.430]  
[16:17:12.430]  [00:00:44.571][silabs ]SPP: ack_timeout_ms 500
[16:17:12.779]  [00:00:44.923][silabs ]MATTER RX[0-8]: 55 AA 01 09 CC 07 01 03 E0 
[16:17:12.779]  [00:00:44.924][silabs ]PWR: report Battery Charge State 3
[16:17:12.779]  
[16:17:12.784]  [00:00:44.924][silabs ]SPP: pending ack but allow new cmd process
[16:17:12.926]  [00:00:45.071][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:12.926]  [00:00:45.071][silabs ]MATTER TX[0-7]: 55 AA 01 09 8E 12 00 A9 
[16:17:12.929]  [00:00:45.071][silabs ]COM: CMD: 0x12, SN: 0x098E, LEN: 8
[16:17:12.934]  
[16:17:13.279]  [00:00:45.423][silabs ]MATTER RX[0-8]: 55 AA 01 09 CC 07 01 03 E0 
[16:17:13.279]  [00:00:45.423][silabs ]SPP: tx_queue full!
[16:17:13.279]  [00:00:45.423][silabs ]PWR: report Battery Charge State 3
[16:17:13.285]  
[16:17:13.427]  [00:00:45.572][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:13.427]  [00:00:45.572][silabs ]MATTER TX[0-7]: 55 AA 01 09 8E 12 00 A9 
[16:17:13.430]  [00:00:45.572][silabs ]COM: CMD: 0x12, SN: 0x098E, LEN: 8
[16:17:13.434]  
[16:17:13.829]  [00:00:45.973][silabs ]MATTER RX[0-8]: 55 AA 01 00 CD 08 01 01 D7 
[16:17:13.829]  [00:00:45.973][silabs ]SPP: tx_queue full!
[16:17:13.829]  [00:00:45.973][silabs ]PWR: report Battery Charge Level 1
[16:17:13.835]  
[16:17:13.928]  [00:00:46.073][silabs ]SPP: re-sent reach to max
[16:17:13.928]  [00:00:46.073][silabs ]MATTER TX[0-7]: 55 AA 01 09 A2 12 00 BD 
[16:17:13.928]  [00:00:46.073][silabs ]COM: CMD: 0x12, SN: 0x09A2, LEN: 8
[16:17:13.932]  
[16:17:13.932]  [00:00:46.073][silabs ]SPP: ack_timeout_ms 500
[16:17:14.329]  [00:00:46.473][silabs ]MATTER RX[0-8]: 55 AA 01 09 CD 08 01 01 E0 
[16:17:14.329]  [00:00:46.473][silabs ]PWR: report Battery Charge Level 1
[16:17:14.329]  
[16:17:14.332]  [00:00:46.473][silabs ]SPP: pending ack but allow new cmd process
[16:17:14.429]  [00:00:46.574][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:14.429]  [00:00:46.574][silabs ]MATTER TX[0-7]: 55 AA 01 09 A2 12 00 BD 
[16:17:14.435]  [00:00:46.574][silabs ]COM: CMD: 0x12, SN: 0x09A2, LEN: 8
[16:17:14.435]  
[16:17:14.828]  [00:00:46.972][silabs ]MATTER RX[0-8]: 55 AA 01 09 CD 08 01 01 E0 
[16:17:14.828]  [00:00:46.972][silabs ]SPP: tx_queue full!
[16:17:14.828]  [00:00:46.973][silabs ]PWR: report Battery Charge Level 1
[16:17:14.834]  
[16:17:14.930]  [00:00:47.075][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:14.930]  [00:00:47.075][silabs ]MATTER TX[0-7]: 55 AA 01 09 A2 12 00 BD 
[16:17:14.934]  [00:00:47.075][silabs ]COM: CMD: 0x12, SN: 0x09A2, LEN: 8
[16:17:14.934]  
[16:17:15.378]  [00:00:47.522][silabs ]MATTER RX[0-8]: 55 AA 01 00 CE 08 01 02 D9 
[16:17:15.378]  [00:00:47.522][silabs ]SPP: tx_queue full!
[16:17:15.378]  [00:00:47.523][silabs ]PWR: report Battery Charge Level 2
[16:17:15.385]  
[16:17:15.430]  [00:00:47.576][silabs ]SPP: re-sent reach to max
[16:17:15.430]  [00:00:47.576][silabs ]MATTER TX[0-7]: 55 AA 01 09 A3 06 00 B2 
[16:17:15.430]  [00:00:47.576][silabs ]COM: CMD: 0x06, SN: 0x09A3, LEN: 8
[16:17:15.434]  
[16:17:15.434]  [00:00:47.576][silabs ]SPP: ack_timeout_ms 500
[16:17:15.878]  [00:00:48.022][silabs ]MATTER RX[0-8]: 55 AA 01 09 CE 08 01 02 E2 
[16:17:15.878]  [00:00:48.022][silabs ]PWR: report Battery Charge Level 2
[16:17:15.878]  
[16:17:15.880]  [00:00:48.022][silabs ]SPP: pending ack but allow new cmd process
[16:17:15.932]  [00:00:48.077][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:15.932]  [00:00:48.077][silabs ]MATTER TX[0-7]: 55 AA 01 09 A3 06 00 B2 
[16:17:15.935]  [00:00:48.077][silabs ]COM: CMD: 0x06, SN: 0x09A3, LEN: 8
[16:17:15.940]  
[16:17:16.377]  [00:00:48.522][silabs ]MATTER RX[0-8]: 55 AA 01 09 CE 08 01 02 E2 
[16:17:16.377]  [00:00:48.522][silabs ]SPP: tx_queue full!
[16:17:16.377]  [00:00:48.522][silabs ]PWR: report Battery Charge Level 2
[16:17:16.384]  
[16:17:16.432]  [00:00:48.578][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:16.432]  [00:00:48.578][silabs ]MATTER TX[0-7]: 55 AA 01 09 A3 06 00 B2 
[16:17:16.436]  [00:00:48.578][silabs ]COM: CMD: 0x06, SN: 0x09A3, LEN: 8
[16:17:16.439]  
[16:17:16.933]  [00:00:49.079][silabs ]SPP: re-sent reach to max
[16:17:16.933]  [00:00:49.079][silabs ]MATTER TX[0-7]: 55 AA 01 09 A4 07 00 B4 
[16:17:16.933]  [00:00:49.079][silabs ]COM: CMD: 0x07, SN: 0x09A4, LEN: 8
[16:17:16.939]  
[16:17:16.939]  [00:00:49.079][silabs ]SPP: ack_timeout_ms 500
[16:17:17.434]  [00:00:49.580][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:17.434]  [00:00:49.580][silabs ]MATTER TX[0-7]: 55 AA 01 09 A4 07 00 B4 
[16:17:17.439]  [00:00:49.580][silabs ]COM: CMD: 0x07, SN: 0x09A4, LEN: 8
[16:17:17.439]  
[16:17:17.936]  [00:00:50.081][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:17.936]  [00:00:50.081][silabs ]MATTER TX[0-7]: 55 AA 01 09 A4 07 00 B4 
[16:17:17.939]  [00:00:50.081][silabs ]COM: CMD: 0x07, SN: 0x09A4, LEN: 8
[16:17:17.944]  
[16:17:18.437]  [00:00:50.582][silabs ]SPP: re-sent reach to max
[16:17:18.437]  [00:00:50.583][silabs ]MATTER TX[0-7]: 55 AA 01 09 A7 12 00 C2 
[16:17:18.437]  [00:00:50.583][silabs ]COM: CMD: 0x12, SN: 0x09A7, LEN: 8
[16:17:18.441]  
[16:17:18.441]  [00:00:50.583][silabs ]SPP: ack_timeout_ms 500
[16:17:18.939]  [00:00:51.083][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:18.939]  [00:00:51.083][silabs ]MATTER TX[0-7]: 55 AA 01 09 A7 12 00 C2 
[16:17:18.941]  [00:00:51.083][silabs ]COM: CMD: 0x12, SN: 0x09A7, LEN: 8
[16:17:18.945]  
[16:17:19.439]  [00:00:51.584][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:19.439]  [00:00:51.584][silabs ]MATTER TX[0-7]: 55 AA 01 09 A7 12 00 C2 
[16:17:19.445]  [00:00:51.584][silabs ]COM: CMD: 0x12, SN: 0x09A7, LEN: 8
[16:17:19.445]  
[16:17:19.941]  [00:00:52.085][silabs ]SPP: re-sent reach to max
[16:17:19.941]  [00:00:52.086][silabs ]MATTER TX[0-7]: 55 AA 01 09 B6 12 00 D1 
[16:17:19.941]  [00:00:52.086][silabs ]COM: CMD: 0x12, SN: 0x09B6, LEN: 8
[16:17:19.944]  
[16:17:19.944]  [00:00:52.086][silabs ]SPP: ack_timeout_ms 500
[16:17:20.442]  [00:00:52.587][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:20.442]  [00:00:52.587][silabs ]MATTER TX[0-7]: 55 AA 01 09 B6 12 00 D1 
[16:17:20.445]  [00:00:52.587][silabs ]COM: CMD: 0x12, SN: 0x09B6, LEN: 8
[16:17:20.449]  
[16:17:20.943]  [00:00:53.088][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:20.943]  [00:00:53.088][silabs ]MATTER TX[0-7]: 55 AA 01 09 B6 12 00 D1 
[16:17:20.946]  [00:00:53.088][silabs ]COM: CMD: 0x12, SN: 0x09B6, LEN: 8
[16:17:20.949]  
[16:17:21.445]  [00:00:53.589][silabs ]SPP: re-sent reach to max
[16:17:21.445]  [00:00:53.590][silabs ]MATTER TX[0-7]: 55 AA 01 09 CA 12 00 E5 
[16:17:21.445]  [00:00:53.590][silabs ]COM: CMD: 0x12, SN: 0x09CA, LEN: 8
[16:17:21.449]  
[16:17:21.449]  [00:00:53.590][silabs ]SPP: ack_timeout_ms 500
[16:17:21.946]  [00:00:54.091][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:21.946]  [00:00:54.091][silabs ]MATTER TX[0-7]: 55 AA 01 09 CA 12 00 E5 
[16:17:21.949]  [00:00:54.091][silabs ]COM: CMD: 0x12, SN: 0x09CA, LEN: 8
[16:17:21.954]  
[16:17:22.447]  [00:00:54.592][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:22.447]  [00:00:54.592][silabs ]MATTER TX[0-7]: 55 AA 01 09 CA 12 00 E5 
[16:17:22.451]  [00:00:54.592][silabs ]COM: CMD: 0x12, SN: 0x09CA, LEN: 8
[16:17:22.454]  
[16:17:22.949]  [00:00:55.093][silabs ]SPP: re-sent reach to max
[16:17:22.949]  [00:00:55.094][silabs ]MATTER TX[0-7]: 55 AA 01 09 CB 06 00 DA 
[16:17:22.949]  [00:00:55.094][silabs ]COM: CMD: 0x06, SN: 0x09CB, LEN: 8
[16:17:22.954]  
[16:17:22.954]  [00:00:55.094][silabs ]SPP: ack_timeout_ms 500
[16:17:23.449]  [00:00:55.594][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:23.449]  [00:00:55.594][silabs ]MATTER TX[0-7]: 55 AA 01 09 CB 06 00 DA 
[16:17:23.454]  [00:00:55.594][silabs ]COM: CMD: 0x06, SN: 0x09CB, LEN: 8
[16:17:23.454]  
[16:17:23.951]  [00:00:56.095][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:23.951]  [00:00:56.095][silabs ]MATTER TX[0-7]: 55 AA 01 09 CB 06 00 DA 
[16:17:23.954]  [00:00:56.095][silabs ]COM: CMD: 0x06, SN: 0x09CB, LEN: 8
[16:17:23.954]  
[16:17:24.451]  [00:00:56.595][silabs ]SPP: re-sent reach to max
[16:17:24.451]  [00:00:56.596][silabs ]MATTER TX[0-7]: 55 AA 01 09 CC 07 00 DC 
[16:17:24.451]  [00:00:56.596][silabs ]COM: CMD: 0x07, SN: 0x09CC, LEN: 8
[16:17:24.455]  
[16:17:24.455]  [00:00:56.596][silabs ]SPP: ack_timeout_ms 500
[16:17:24.951]  [00:00:57.096][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:24.951]  [00:00:57.096][silabs ]MATTER TX[0-7]: 55 AA 01 09 CC 07 00 DC 
[16:17:24.953]  [00:00:57.096][silabs ]COM: CMD: 0x07, SN: 0x09CC, LEN: 8
[16:17:24.959]  
[16:17:25.451]  [00:00:57.596][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:25.451]  [00:00:57.596][silabs ]MATTER TX[0-7]: 55 AA 01 09 CC 07 00 DC 
[16:17:25.453]  [00:00:57.596][silabs ]COM: CMD: 0x07, SN: 0x09CC, LEN: 8
[16:17:25.459]  
[16:17:25.951]  [00:00:58.096][silabs ]SPP: re-sent reach to max
[16:17:25.951]  [00:00:58.097][silabs ]MATTER TX[0-7]: 55 AA 01 09 CD 08 00 DE 
[16:17:25.951]  [00:00:58.097][silabs ]COM: CMD: 0x08, SN: 0x09CD, LEN: 8
[16:17:25.955]  
[16:17:25.955]  [00:00:58.097][silabs ]SPP: ack_timeout_ms 500
[16:17:26.453]  [00:00:58.597][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:26.453]  [00:00:58.597][silabs ]MATTER TX[0-7]: 55 AA 01 09 CD 08 00 DE 
[16:17:26.455]  [00:00:58.597][silabs ]COM: CMD: 0x08, SN: 0x09CD, LEN: 8
[16:17:26.459]  
[16:17:26.953]  [00:00:59.097][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:26.953]  [00:00:59.097][silabs ]MATTER TX[0-7]: 55 AA 01 09 CD 08 00 DE 
[16:17:26.955]  [00:00:59.097][silabs ]COM: CMD: 0x08, SN: 0x09CD, LEN: 8
[16:17:26.959]  
[16:17:27.452]  [00:00:59.597][silabs ]SPP: re-sent reach to max
[16:17:27.452]  [00:00:59.598][silabs ]MATTER TX[0-7]: 55 AA 01 09 CE 08 00 DF 
[16:17:27.452]  [00:00:59.598][silabs ]COM: CMD: 0x08, SN: 0x09CE, LEN: 8
[16:17:27.455]  
[16:17:27.455]  [00:00:59.598][silabs ]SPP: ack_timeout_ms 500
[16:17:27.953]  [00:01:00.098][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:17:27.953]  [00:01:00.098][silabs ]MATTER TX[0-7]: 55 AA 01 09 CE 08 00 DF 
[16:17:27.955]  [00:01:00.098][silabs ]COM: CMD: 0x08, SN: 0x09CE, LEN: 8
[16:17:27.959]  
[16:17:28.453]  [00:01:00.598][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:17:28.453]  [00:01:00.598][silabs ]MATTER TX[0-7]: 55 AA 01 09 CE 08 00 DF 
[16:17:28.456]  [00:01:00.598][silabs ]COM: CMD: 0x08, SN: 0x09CE, LEN: 8
[16:17:28.459]  
[16:17:28.954]  [00:01:01.098][silabs ]SPP: re-sent reach to max
[16:22:53.300]  [00:06:25.453][info  ][EM] >>> [E:8055r S:0 M:12589915] (U) Msg RX from 0:D77C78803D908713 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[16:22:53.301]  [00:06:25.454][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[16:22:53.303]  [00:06:25.454][info  ][EM] <<< [E:8055r S:0 M:104101962 (Ack:12589915)] (U) Msg TX from 0000000000000000 to 0:D77C78803D908713 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:54930] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:22:53.306]  [00:06:25.455][info  ][SC] Received Sigma1 msg
[16:22:53.313]  [00:06:25.463][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[16:22:53.340]  [00:06:25.494][info  ][EM] <<< [E:8055r S:0 M:104101963 (Ack:12589915)] (U) Msg TX from 0000000000000000 to 0:D77C78803D908713 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:54930] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[16:22:53.342]  [00:06:25.495][info  ][EM] ??1 [E:8055r S:0 M:104101963] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3350ms from now [State:Active II:500 AI:300 AT:4000]
[16:22:53.347]  [00:06:25.495][info  ][SC] Sent Sigma2 msg
[16:22:53.944]  [00:06:26.097][info  ][EM] >>> [E:8055r S:0 M:12589916 (Ack:104101963)] (U) Msg RX from 0:D77C78803D908713 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[16:22:53.945]  [00:06:26.098][info  ][EM] <<< [E:8055r S:0 M:104101964 (Ack:12589916)] (U) Msg TX from 0000000000000000 to 0:D77C78803D908713 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:54930] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:22:53.951]  [00:06:26.099][info  ][SC] Received Sigma3 msg
[16:22:53.996]  [00:06:26.149][info  ][EM] <<< [E:8055r S:0 M:104101965 (Ack:12589916)] (U) Msg TX from 0000000000000000 to 0:D77C78803D908713 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:54930] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:22:53.997]  [00:06:26.149][info  ][EM] ??1 [E:8055r S:0 M:104101965] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3386ms from now [State:Active II:500 AI:300 AT:4000]
[16:22:54.000]  [00:06:26.153][info  ][SC] SecureSession[0x20006d50, LSID:7469]: State change 'kEstablishing' --> 'kActive'
[16:22:54.001]  [00:06:26.153][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[16:22:54.001]  [00:06:26.154][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:22:54.006]  [00:06:26.154][silabs ]NWK: platform event type 32792
[16:22:54.453]  [00:06:26.606][info  ][EM] >>> [E:8056r S:7469 M:20295420] (S) Msg RX from 1:000000000001B669 [C344] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:71)
[16:22:54.456]  [00:06:26.608][info  ][SWU] OTA Requestor received AnnounceOTAProvider
[16:22:54.456]  [00:06:26.610][info  ][EM] <<< [E:8056r S:7469 M:221181327 (Ack:20295420)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:54930] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[16:22:54.459]  [00:06:26.611][info  ][EM] ??1 [E:8056r S:7469 M:221181327] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3332ms from now [State:Active II:500 AI:300 AT:4000]
[16:22:54.461]  [00:06:26.612][info  ][SWU] Stopping the Periodic Query timer
[16:22:54.461]  [00:06:26.612][info  ][SWU] Starting the watchdog timer, timeout: 21600 seconds
[16:22:54.463]  [00:06:26.612][info  ][DIS] Resolving 66AC7364E726C344:0000000000000001 ...
[16:22:54.463]  [00:06:26.613][info  ][DIS] Lookup started for 66AC7364E726C344-0000000000000001
[16:22:54.470]  [00:06:26.624][info  ][EM] >>> [E:8055r S:0 M:12589917 (Ack:104101965)] (U) Msg RX from 0:D77C78803D908713 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:22:54.515]  [00:06:26.668][info  ][EM] >>> [E:8056r S:7469 M:20295421 (Ack:221181327)] (S) Msg RX from 1:000000000001B669 [C344] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:22:54.661]  [00:06:26.812][info  ][DIS] Checking node lookup status for 66AC7364E726C344-0000000000000001 after 200 ms
[16:22:55.557]  [00:06:27.710][info  ][DIS] Node ID resolved for 66AC7364E726C344-0000000000000001
[16:22:55.557]  [00:06:27.710][info  ][DIS] UDP:[fdd9:d33f:e8ea:b55e:8aa2:9eff:fe1d:c2c2]:5540: new best score: 3 (for 66AC7364E726C344-0000000000000001)
[16:22:55.558]  [00:06:27.711][info  ][DIS] Checking node lookup status for 66AC7364E726C344-0000000000000001 after 1099 ms
[16:22:55.560]  [00:06:27.712][info  ][SC] Initiating session on local FabricIndex 1 from 0x00000000000008CA -> 0x0000000000000001
[16:22:55.578]  [00:06:27.731][info  ][EM] <<< [E:60953i S:0 M:104101966] (U) Msg TX from 0D6A4AFFDFBEF588 to 0:0000000000000000 [0000] [UDP:[fdd9:d33f:e8ea:b55e:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:233)
[16:22:55.579]  [00:06:27.732][info  ][EM] ??1 [E:60953i S:0 M:104101966] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3582ms from now [State:Idle II:500 AI:2000 AT:4000]
[16:22:55.585]  [00:06:27.732][info  ][SC] Sent Sigma1 msg to <0000000000000001, 1> [II:3000ms AI:2500ms AT:0ms]
[16:22:56.088]  [00:06:28.241][info  ][EM] >>> [E:60953i S:0 M:258783730 (Ack:104101966)] (U) Msg RX from 0:0000000000000000 [0000] to 0D6A4AFFDFBEF588 --- Type 0000:33 (SecureChannel:CASE_Sigma2Resume) (B:100)
[16:22:56.089]  [00:06:28.242][info  ][EM] <<< [E:60953i S:0 M:104101967 (Ack:258783730)] (U) Msg TX from 0D6A4AFFDFBEF588 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:22:56.095]  [00:06:28.250][info  ][EM] <<< [E:60953i S:0 M:104101968 (Ack:258783730)] (U) Msg TX from 0D6A4AFFDFBEF588 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:22:56.099]  [00:06:28.250][info  ][EM] ??1 [E:60953i S:0 M:104101968] (U) Msg Retransmission to 0:0000000000000000 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:56.100]  [00:06:28.253][info  ][SC] SecureSession[0x20006f00, LSID:7471]: State change 'kEstablishing' --> 'kActive'
[16:22:56.102]  [00:06:28.256][info  ][EM] <<< [E:60954i S:7471 M:3253010] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[16:22:56.105]  [00:06:28.257][info  ][EM] ??1 [E:60954i S:7471 M:3253010] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5564ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:56.106]  [00:06:28.257][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:22:56.111]  [00:06:28.257][silabs ]NWK: platform event type 32792
[16:22:56.591]  [00:06:28.744][info  ][EM] >>> [E:60953i S:0 M:258783731 (Ack:104101968)] (U) Msg RX from 0:0000000000000000 [0000] to 0D6A4AFFDFBEF588 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:22:56.659]  [00:06:28.813][info  ][EM] >>> [E:60954i S:7471 M:8703164 (Ack:3253010)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:198)
[16:22:56.661]  [00:06:28.814][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[16:22:56.663]  [00:06:28.814][info  ][SWU] Update available from version 4 to 5
[16:22:56.663]  [00:06:28.816][info  ][EM] <<< [E:60954i S:7471 M:3253011 (Ack:8703164)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:22:56.706]  [00:06:28.817][info  ][DIS] Found an existing secure session to [1:0000000000000001]!
[16:22:56.706]  [00:06:28.818][info  ][SWU] HandlePrepareDownload: started
[16:22:56.708]  [00:06:28.861][info  ][EM] <<< [E:60955i S:7471 M:3253012] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:04 (BDX:ReceiveInit) (B:90)
[16:22:56.709]  [00:06:28.862][info  ][EM] ??1 [E:60955i S:7471 M:3253012] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5321ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:57.162]  [00:06:29.316][info  ][EM] >>> [E:60955i S:7471 M:8703165 (Ack:3253012)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:05 (BDX:ReceiveAccept) (B:38)
[16:22:57.164]  [00:06:29.318][info  ][EM] <<< [E:60955i S:7471 M:3253013 (Ack:8703165)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:22:57.167]  [00:06:29.319][info  ][EM] ??1 [E:60955i S:7471 M:3253013] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:57.933]  [00:06:30.086][info  ][EM] >>> [E:60955i S:7471 M:8703166 (Ack:3253013)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:22:57.965]  [00:06:30.087][info  ][SWU] Image Header software version: 5 payload size: 608904
[16:22:57.988]  [00:06:30.141][info  ][EM] <<< [E:60955i S:7471 M:3253014 (Ack:8703166)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:22:57.989]  [00:06:30.141][info  ][EM] ??1 [E:60955i S:7471 M:3253014] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:58.695]  [00:06:30.848][info  ][EM] >>> [E:60955i S:7471 M:8703167 (Ack:3253014)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:22:58.724]  [00:06:30.877][info  ][EM] <<< [E:60955i S:7471 M:3253015 (Ack:8703167)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:22:58.726]  [00:06:30.878][info  ][EM] ??1 [E:60955i S:7471 M:3253015] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[16:22:59.465]  [00:06:31.619][info  ][EM] >>> [E:60955i S:7471 M:8703168 (Ack:3253015)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:22:59.495]  [00:06:31.648][info  ][EM] <<< [E:60955i S:7471 M:3253016 (Ack:8703168)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:22:59.496]  [00:06:31.649][info  ][EM] ??1 [E:60955i S:7471 M:3253016] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:00.455]  [00:06:32.608][info  ][EM] >>> [E:60955i S:7471 M:8703169 (Ack:3253016)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:00.485]  [00:06:32.638][info  ][EM] <<< [E:60955i S:7471 M:3253017 (Ack:8703169)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:00.486]  [00:06:32.638][info  ][EM] ??1 [E:60955i S:7471 M:3253017] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:01.446]  [00:06:33.600][info  ][EM] >>> [E:60955i S:7471 M:8703170 (Ack:3253017)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:01.511]  [00:06:33.666][info  ][EM] <<< [E:60955i S:7471 M:3253018 (Ack:8703170)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:01.514]  [00:06:33.666][info  ][EM] ??1 [E:60955i S:7471 M:3253018] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5284ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:02.336]  [00:06:34.490][info  ][EM] >>> [E:60955i S:7471 M:8703171 (Ack:3253018)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:02.367]  [00:06:34.520][info  ][EM] <<< [E:60955i S:7471 M:3253019 (Ack:8703171)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:02.368]  [00:06:34.520][info  ][EM] ??1 [E:60955i S:7471 M:3253019] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:03.214]  [00:06:35.368][info  ][EM] >>> [E:60955i S:7471 M:8703172 (Ack:3253019)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:03.244]  [00:06:35.398][info  ][EM] <<< [E:60955i S:7471 M:3253020 (Ack:8703172)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:03.246]  [00:06:35.398][info  ][EM] ??1 [E:60955i S:7471 M:3253020] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:04.079]  [00:06:36.232][info  ][EM] >>> [E:60955i S:7471 M:8703173 (Ack:3253020)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:04.109]  [00:06:36.262][info  ][EM] <<< [E:60955i S:7471 M:3253021 (Ack:8703173)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:04.110]  [00:06:36.263][info  ][EM] ??1 [E:60955i S:7471 M:3253021] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:04.849]  [00:06:37.002][info  ][EM] >>> [E:60955i S:7471 M:8703174 (Ack:3253021)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:04.905]  [00:06:37.058][info  ][EM] <<< [E:60955i S:7471 M:3253022 (Ack:8703174)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:04.906]  [00:06:37.059][info  ][EM] ??1 [E:60955i S:7471 M:3253022] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:05.717]  [00:06:37.871][info  ][EM] >>> [E:60955i S:7471 M:8703175 (Ack:3253022)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:05.747]  [00:06:37.901][info  ][EM] <<< [E:60955i S:7471 M:3253023 (Ack:8703175)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:05.748]  [00:06:37.902][info  ][EM] ??1 [E:60955i S:7471 M:3253023] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:06.589]  [00:06:38.743][info  ][EM] >>> [E:60955i S:7471 M:8703176 (Ack:3253023)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:06.618]  [00:06:38.772][info  ][EM] <<< [E:60955i S:7471 M:3253024 (Ack:8703176)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:06.620]  [00:06:38.773][info  ][EM] ??1 [E:60955i S:7471 M:3253024] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:07.479]  [00:06:39.633][info  ][EM] >>> [E:60955i S:7471 M:8703177 (Ack:3253024)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:07.509]  [00:06:39.663][info  ][EM] <<< [E:60955i S:7471 M:3253025 (Ack:8703177)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:07.511]  [00:06:39.664][info  ][EM] ??1 [E:60955i S:7471 M:3253025] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:08.350]  [00:06:40.503][info  ][EM] >>> [E:60955i S:7471 M:8703178 (Ack:3253025)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:08.415]  [00:06:40.569][info  ][EM] <<< [E:60955i S:7471 M:3253026 (Ack:8703178)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:08.416]  [00:06:40.569][info  ][EM] ??1 [E:60955i S:7471 M:3253026] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:09.321]  [00:06:41.474][info  ][EM] >>> [E:60955i S:7471 M:8703179 (Ack:3253026)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:09.351]  [00:06:41.504][info  ][EM] <<< [E:60955i S:7471 M:3253027 (Ack:8703179)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:09.353]  [00:06:41.505][info  ][EM] ??1 [E:60955i S:7471 M:3253027] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:10.085]  [00:06:42.238][info  ][EM] >>> [E:60955i S:7471 M:8703180 (Ack:3253027)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:10.114]  [00:06:42.268][info  ][EM] <<< [E:60955i S:7471 M:3253028 (Ack:8703180)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:10.116]  [00:06:42.268][info  ][EM] ??1 [E:60955i S:7471 M:3253028] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:10.992]  [00:06:43.146][info  ][EM] >>> [E:60955i S:7471 M:8703181 (Ack:3253028)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:11.022]  [00:06:43.175][info  ][EM] <<< [E:60955i S:7471 M:3253029 (Ack:8703181)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:11.024]  [00:06:43.176][info  ][EM] ??1 [E:60955i S:7471 M:3253029] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:11.774]  [00:06:43.927][info  ][EM] >>> [E:60955i S:7471 M:8703182 (Ack:3253029)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:11.829]  [00:06:43.982][info  ][EM] <<< [E:60955i S:7471 M:3253030 (Ack:8703182)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:11.831]  [00:06:43.983][info  ][EM] ??1 [E:60955i S:7471 M:3253030] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5220ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:12.752]  [00:06:44.905][info  ][EM] >>> [E:60955i S:7471 M:8703183 (Ack:3253030)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:12.781]  [00:06:44.935][info  ][EM] <<< [E:60955i S:7471 M:3253031 (Ack:8703183)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:12.783]  [00:06:44.935][info  ][EM] ??1 [E:60955i S:7471 M:3253031] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5454ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:13.521]  [00:06:45.675][info  ][EM] >>> [E:60955i S:7471 M:8703184 (Ack:3253031)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:13.551]  [00:06:45.705][info  ][EM] <<< [E:60955i S:7471 M:3253032 (Ack:8703184)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:13.554]  [00:06:45.706][info  ][EM] ??1 [E:60955i S:7471 M:3253032] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5246ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:14.508]  [00:06:46.661][info  ][EM] >>> [E:60955i S:7471 M:8703185 (Ack:3253032)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:14.538]  [00:06:46.691][info  ][EM] <<< [E:60955i S:7471 M:3253033 (Ack:8703185)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:14.539]  [00:06:46.692][info  ][EM] ??1 [E:60955i S:7471 M:3253033] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:18.508]  [00:06:50.662][info  ][EM] >>> [E:60955i S:7471 M:8703186 (Ack:3253033)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:18.573]  [00:06:50.727][info  ][EM] <<< [E:60955i S:7471 M:3253034 (Ack:8703186)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:18.574]  [00:06:50.728][info  ][EM] ??1 [E:60955i S:7471 M:3253034] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5280ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:19.474]  [00:06:51.627][info  ][EM] >>> [E:60955i S:7471 M:8703187 (Ack:3253034)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:19.503]  [00:06:51.657][info  ][EM] <<< [E:60955i S:7471 M:3253035 (Ack:8703187)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:19.504]  [00:06:51.658][info  ][EM] ??1 [E:60955i S:7471 M:3253035] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:20.241]  [00:06:52.394][info  ][EM] >>> [E:60955i S:7471 M:8703188 (Ack:3253035)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:20.270]  [00:06:52.423][info  ][EM] <<< [E:60955i S:7471 M:3253036 (Ack:8703188)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:20.271]  [00:06:52.424][info  ][EM] ??1 [E:60955i S:7471 M:3253036] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:21.327]  [00:06:53.480][info  ][EM] >>> [E:60955i S:7471 M:8703189 (Ack:3253036)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:21.355]  [00:06:53.509][info  ][EM] <<< [E:60955i S:7471 M:3253037 (Ack:8703189)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:21.358]  [00:06:53.510][info  ][EM] ??1 [E:60955i S:7471 M:3253037] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:22.091]  [00:06:54.245][info  ][EM] >>> [E:60955i S:7471 M:8703190 (Ack:3253037)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:22.148]  [00:06:54.302][info  ][EM] <<< [E:60955i S:7471 M:3253038 (Ack:8703190)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:22.149]  [00:06:54.303][info  ][EM] ??1 [E:60955i S:7471 M:3253038] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:22.872]  [00:06:55.026][info  ][EM] >>> [E:60955i S:7471 M:8703191 (Ack:3253038)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:22.902]  [00:06:55.055][info  ][EM] <<< [E:60955i S:7471 M:3253039 (Ack:8703191)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:22.903]  [00:06:55.056][info  ][EM] ??1 [E:60955i S:7471 M:3253039] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:23.639]  [00:06:55.792][info  ][EM] >>> [E:60955i S:7471 M:8703192 (Ack:3253039)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:23.669]  [00:06:55.823][info  ][EM] <<< [E:60955i S:7471 M:3253040 (Ack:8703192)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:23.670]  [00:06:55.823][info  ][EM] ??1 [E:60955i S:7471 M:3253040] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5615ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:24.619]  [00:06:56.772][info  ][EM] >>> [E:60955i S:7471 M:8703193 (Ack:3253040)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:24.649]  [00:06:56.802][info  ][EM] <<< [E:60955i S:7471 M:3253041 (Ack:8703193)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:24.650]  [00:06:56.803][info  ][EM] ??1 [E:60955i S:7471 M:3253041] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:25.490]  [00:06:57.644][info  ][EM] >>> [E:60955i S:7471 M:8703194 (Ack:3253041)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:25.556]  [00:06:57.709][info  ][EM] <<< [E:60955i S:7471 M:3253042 (Ack:8703194)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:25.558]  [00:06:57.710][info  ][EM] ??1 [E:60955i S:7471 M:3253042] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:26.465]  [00:06:58.620][info  ][EM] >>> [E:60955i S:7471 M:8703195 (Ack:3253042)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:26.495]  [00:06:58.649][info  ][EM] <<< [E:60955i S:7471 M:3253043 (Ack:8703195)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:26.497]  [00:06:58.650][info  ][EM] ??1 [E:60955i S:7471 M:3253043] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:27.357]  [00:06:59.511][info  ][EM] >>> [E:60955i S:7471 M:8703196 (Ack:3253043)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:27.387]  [00:06:59.541][info  ][EM] <<< [E:60955i S:7471 M:3253044 (Ack:8703196)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:27.389]  [00:06:59.541][info  ][EM] ??1 [E:60955i S:7471 M:3253044] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5321ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:28.256]  [00:07:00.410][info  ][EM] >>> [E:60955i S:7471 M:8703197 (Ack:3253044)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:28.285]  [00:07:00.439][info  ][EM] <<< [E:60955i S:7471 M:3253045 (Ack:8703197)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:28.286]  [00:07:00.440][info  ][EM] ??1 [E:60955i S:7471 M:3253045] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:29.044]  [00:07:01.193][info  ][EM] >>> [E:60955i S:7471 M:8703198 (Ack:3253045)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:29.111]  [00:07:01.250][info  ][EM] <<< [E:60955i S:7471 M:3253046 (Ack:8703198)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:29.111]  [00:07:01.250][info  ][EM] ??1 [E:60955i S:7471 M:3253046] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:29.825]  [00:07:01.966][info  ][EM] >>> [E:60955i S:7471 M:8703199 (Ack:3253046)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:29.855]  [00:07:01.997][info  ][EM] <<< [E:60955i S:7471 M:3253047 (Ack:8703199)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:29.855]  [00:07:01.997][info  ][EM] ??1 [E:60955i S:7471 M:3253047] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5643ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:30.603]  [00:07:02.752][info  ][EM] >>> [E:60955i S:7471 M:8703200 (Ack:3253047)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:30.635]  [00:07:02.782][info  ][EM] <<< [E:60955i S:7471 M:3253048 (Ack:8703200)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:30.635]  [00:07:02.783][info  ][EM] ??1 [E:60955i S:7471 M:3253048] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:31.488]  [00:07:03.628][info  ][EM] >>> [E:60955i S:7471 M:8703201 (Ack:3253048)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:31.518]  [00:07:03.659][info  ][EM] <<< [E:60955i S:7471 M:3253049 (Ack:8703201)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:31.518]  [00:07:03.659][info  ][EM] ??1 [E:60955i S:7471 M:3253049] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:32.361]  [00:07:04.512][info  ][EM] >>> [E:60955i S:7471 M:8703202 (Ack:3253049)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:32.427]  [00:07:04.576][info  ][EM] <<< [E:60955i S:7471 M:3253050 (Ack:8703202)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:32.427]  [00:07:04.577][info  ][EM] ??1 [E:60955i S:7471 M:3253050] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5658ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:33.230]  [00:07:05.381][info  ][EM] >>> [E:60955i S:7471 M:8703203 (Ack:3253050)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:33.261]  [00:07:05.411][info  ][EM] <<< [E:60955i S:7471 M:3253051 (Ack:8703203)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:33.261]  [00:07:05.412][info  ][EM] ??1 [E:60955i S:7471 M:3253051] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:34.009]  [00:07:06.163][info  ][EM] >>> [E:60955i S:7471 M:8703204 (Ack:3253051)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:34.041]  [00:07:06.193][info  ][EM] <<< [E:60955i S:7471 M:3253052 (Ack:8703204)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:34.041]  [00:07:06.193][info  ][EM] ??1 [E:60955i S:7471 M:3253052] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:34.951]  [00:07:07.101][info  ][EM] >>> [E:60955i S:7471 M:8703205 (Ack:3253052)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:34.983]  [00:07:07.131][info  ][EM] <<< [E:60955i S:7471 M:3253053 (Ack:8703205)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:34.983]  [00:07:07.131][info  ][EM] ??1 [E:60955i S:7471 M:3253053] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:35.932]  [00:07:08.079][info  ][EM] >>> [E:60955i S:7471 M:8703206 (Ack:3253053)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:35.986]  [00:07:08.133][info  ][EM] <<< [E:60955i S:7471 M:3253054 (Ack:8703206)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:35.986]  [00:07:08.134][info  ][EM] ??1 [E:60955i S:7471 M:3253054] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:36.915]  [00:07:09.057][info  ][EM] >>> [E:60955i S:7471 M:8703207 (Ack:3253054)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:36.941]  [00:07:09.087][info  ][EM] <<< [E:60955i S:7471 M:3253055 (Ack:8703207)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:36.941]  [00:07:09.087][info  ][EM] ??1 [E:60955i S:7471 M:3253055] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:37.671]  [00:07:09.818][info  ][EM] >>> [E:60955i S:7471 M:8703208 (Ack:3253055)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:37.702]  [00:07:09.848][info  ][EM] <<< [E:60955i S:7471 M:3253056 (Ack:8703208)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:37.702]  [00:07:09.849][info  ][EM] ??1 [E:60955i S:7471 M:3253056] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:38.535]  [00:07:10.678][info  ][EM] >>> [E:60955i S:7471 M:8703209 (Ack:3253056)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:38.566]  [00:07:10.708][info  ][EM] <<< [E:60955i S:7471 M:3253057 (Ack:8703209)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:38.566]  [00:07:10.708][info  ][EM] ??1 [E:60955i S:7471 M:3253057] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5615ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:39.618]  [00:07:11.758][info  ][EM] >>> [E:60955i S:7471 M:8703210 (Ack:3253057)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:39.678]  [00:07:11.826][info  ][EM] <<< [E:60955i S:7471 M:3253058 (Ack:8703210)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:39.678]  [00:07:11.827][info  ][EM] ??1 [E:60955i S:7471 M:3253058] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5209ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:40.708]  [00:07:12.863][info  ][EM] >>> [E:60955i S:7471 M:8703211 (Ack:3253058)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:40.738]  [00:07:12.893][info  ][EM] <<< [E:60955i S:7471 M:3253059 (Ack:8703211)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:40.752]  [00:07:12.893][info  ][EM] ??1 [E:60955i S:7471 M:3253059] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5734ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:42.038]  [00:07:14.183][info  ][EM] >>> [E:60955i S:7471 M:8703212 (Ack:3253059)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:42.068]  [00:07:14.213][info  ][EM] <<< [E:60955i S:7471 M:3253060 (Ack:8703212)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:42.068]  [00:07:14.214][info  ][EM] ??1 [E:60955i S:7471 M:3253060] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5555ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:42.915]  [00:07:15.067][info  ][EM] >>> [E:60955i S:7471 M:8703213 (Ack:3253060)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:42.945]  [00:07:15.097][info  ][EM] <<< [E:60955i S:7471 M:3253061 (Ack:8703213)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:42.945]  [00:07:15.098][info  ][EM] ??1 [E:60955i S:7471 M:3253061] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:43.714]  [00:07:15.861][info  ][EM] >>> [E:60955i S:7471 M:8703214 (Ack:3253061)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:43.771]  [00:07:15.918][info  ][EM] <<< [E:60955i S:7471 M:3253062 (Ack:8703214)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:43.771]  [00:07:15.919][info  ][EM] ??1 [E:60955i S:7471 M:3253062] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:47.632]  [00:07:19.773][info  ][EM] >>> [E:60955i S:7471 M:8703215 (Ack:3253062)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:47.663]  [00:07:19.803][info  ][EM] <<< [E:60955i S:7471 M:3253063 (Ack:8703215)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:47.663]  [00:07:19.803][info  ][EM] ??1 [E:60955i S:7471 M:3253063] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5435ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:48.603]  [00:07:20.758][info  ][EM] >>> [E:60955i S:7471 M:8703216 (Ack:3253063)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:48.633]  [00:07:20.788][info  ][EM] <<< [E:60955i S:7471 M:3253064 (Ack:8703216)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:48.648]  [00:07:20.789][info  ][EM] ??1 [E:60955i S:7471 M:3253064] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:49.367]  [00:07:21.512][info  ][EM] >>> [E:60955i S:7471 M:8703217 (Ack:3253064)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:49.397]  [00:07:21.541][info  ][EM] <<< [E:60955i S:7471 M:3253065 (Ack:8703217)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:49.397]  [00:07:21.542][info  ][EM] ??1 [E:60955i S:7471 M:3253065] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:50.133]  [00:07:22.284][info  ][EM] >>> [E:60955i S:7471 M:8703218 (Ack:3253065)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:50.194]  [00:07:22.348][info  ][EM] <<< [E:60955i S:7471 M:3253066 (Ack:8703218)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:50.210]  [00:07:22.349][info  ][EM] ??1 [E:60955i S:7471 M:3253066] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:50.901]  [00:07:23.051][info  ][EM] >>> [E:60955i S:7471 M:8703219 (Ack:3253066)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:50.933]  [00:07:23.081][info  ][EM] <<< [E:60955i S:7471 M:3253067 (Ack:8703219)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:50.933]  [00:07:23.082][info  ][EM] ??1 [E:60955i S:7471 M:3253067] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:51.777]  [00:07:23.922][info  ][EM] >>> [E:60955i S:7471 M:8703220 (Ack:3253067)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:51.803]  [00:07:23.953][info  ][EM] <<< [E:60955i S:7471 M:3253068 (Ack:8703220)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:51.803]  [00:07:23.954][info  ][EM] ??1 [E:60955i S:7471 M:3253068] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5424ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:52.550]  [00:07:24.698][info  ][EM] >>> [E:60955i S:7471 M:8703221 (Ack:3253068)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:52.577]  [00:07:24.728][info  ][EM] <<< [E:60955i S:7471 M:3253069 (Ack:8703221)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:52.577]  [00:07:24.729][info  ][EM] ??1 [E:60955i S:7471 M:3253069] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5572ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:53.444]  [00:07:25.587][info  ][EM] >>> [E:60955i S:7471 M:8703222 (Ack:3253069)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:53.502]  [00:07:25.645][info  ][EM] <<< [E:60955i S:7471 M:3253070 (Ack:8703222)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:53.502]  [00:07:25.646][info  ][EM] ??1 [E:60955i S:7471 M:3253070] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5293ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:54.211]  [00:07:26.354][info  ][EM] >>> [E:60955i S:7471 M:8703223 (Ack:3253070)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:54.242]  [00:07:26.383][info  ][EM] <<< [E:60955i S:7471 M:3253071 (Ack:8703223)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:54.242]  [00:07:26.384][info  ][EM] ??1 [E:60955i S:7471 M:3253071] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:54.993]  [00:07:27.141][info  ][EM] >>> [E:60955i S:7471 M:8703224 (Ack:3253071)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:55.024]  [00:07:27.170][info  ][EM] <<< [E:60955i S:7471 M:3253072 (Ack:8703224)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:55.024]  [00:07:27.171][info  ][EM] ??1 [E:60955i S:7471 M:3253072] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:55.981]  [00:07:28.127][info  ][EM] >>> [E:60955i S:7471 M:8703225 (Ack:3253072)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:56.012]  [00:07:28.158][info  ][EM] <<< [E:60955i S:7471 M:3253073 (Ack:8703225)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:56.012]  [00:07:28.158][info  ][EM] ??1 [E:60955i S:7471 M:3253073] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:56.738]  [00:07:28.884][info  ][EM] >>> [E:60955i S:7471 M:8703226 (Ack:3253073)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:56.799]  [00:07:28.952][info  ][EM] <<< [E:60955i S:7471 M:3253074 (Ack:8703226)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:56.799]  [00:07:28.953][info  ][EM] ??1 [E:60955i S:7471 M:3253074] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5572ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:57.614]  [00:07:29.761][info  ][EM] >>> [E:60955i S:7471 M:8703227 (Ack:3253074)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:57.643]  [00:07:29.791][info  ][EM] <<< [E:60955i S:7471 M:3253075 (Ack:8703227)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:57.643]  [00:07:29.791][info  ][EM] ??1 [E:60955i S:7471 M:3253075] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5654ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:58.399]  [00:07:30.541][info  ][EM] >>> [E:60955i S:7471 M:8703228 (Ack:3253075)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:58.429]  [00:07:30.572][info  ][EM] <<< [E:60955i S:7471 M:3253076 (Ack:8703228)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:58.429]  [00:07:30.573][info  ][EM] ??1 [E:60955i S:7471 M:3253076] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[16:23:59.180]  [00:07:31.333][info  ][EM] >>> [E:60955i S:7471 M:8703229 (Ack:3253076)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:23:59.212]  [00:07:31.362][info  ][EM] <<< [E:60955i S:7471 M:3253077 (Ack:8703229)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:23:59.212]  [00:07:31.363][info  ][EM] ??1 [E:60955i S:7471 M:3253077] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5398ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:00.074]  [00:07:32.220][info  ][EM] >>> [E:60955i S:7471 M:8703230 (Ack:3253077)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:00.123]  [00:07:32.278][info  ][EM] <<< [E:60955i S:7471 M:3253078 (Ack:8703230)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:00.137]  [00:07:32.279][info  ][EM] ??1 [E:60955i S:7471 M:3253078] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:00.882]  [00:07:33.024][info  ][EM] >>> [E:60955i S:7471 M:8703231 (Ack:3253078)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:00.907]  [00:07:33.053][info  ][EM] <<< [E:60955i S:7471 M:3253079 (Ack:8703231)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:00.907]  [00:07:33.054][info  ][EM] ??1 [E:60955i S:7471 M:3253079] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5643ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:01.638]  [00:07:33.791][info  ][EM] >>> [E:60955i S:7471 M:8703232 (Ack:3253079)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:01.666]  [00:07:33.821][info  ][EM] <<< [E:60955i S:7471 M:3253080 (Ack:8703232)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:01.680]  [00:07:33.822][info  ][EM] ??1 [E:60955i S:7471 M:3253080] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:02.816]  [00:07:34.963][info  ][EM] >>> [E:60955i S:7471 M:8703233 (Ack:3253080)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:02.841]  [00:07:34.993][info  ][EM] <<< [E:60955i S:7471 M:3253081 (Ack:8703233)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:02.841]  [00:07:34.994][info  ][EM] ??1 [E:60955i S:7471 M:3253081] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5559ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:03.586]  [00:07:35.729][info  ][EM] >>> [E:60955i S:7471 M:8703234 (Ack:3253081)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:03.656]  [00:07:35.799][info  ][EM] <<< [E:60955i S:7471 M:3253082 (Ack:8703234)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:03.656]  [00:07:35.800][info  ][EM] ??1 [E:60955i S:7471 M:3253082] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:04.486]  [00:07:36.626][info  ][EM] >>> [E:60955i S:7471 M:8703235 (Ack:3253082)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:04.502]  [00:07:36.657][info  ][EM] <<< [E:60955i S:7471 M:3253083 (Ack:8703235)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:04.517]  [00:07:36.658][info  ][EM] ??1 [E:60955i S:7471 M:3253083] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5495ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:05.237]  [00:07:37.391][info  ][EM] >>> [E:60955i S:7471 M:8703236 (Ack:3253083)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:05.269]  [00:07:37.421][info  ][EM] <<< [E:60955i S:7471 M:3253084 (Ack:8703236)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:05.269]  [00:07:37.421][info  ][EM] ??1 [E:60955i S:7471 M:3253084] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:06.030]  [00:07:38.171][info  ][EM] >>> [E:60955i S:7471 M:8703237 (Ack:3253084)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:06.061]  [00:07:38.202][info  ][EM] <<< [E:60955i S:7471 M:3253085 (Ack:8703237)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:06.061]  [00:07:38.202][info  ][EM] ??1 [E:60955i S:7471 M:3253085] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5280ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:06.829]  [00:07:38.981][info  ][EM] >>> [E:60955i S:7471 M:8703238 (Ack:3253085)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:06.891]  [00:07:39.038][info  ][EM] <<< [E:60955i S:7471 M:3253086 (Ack:8703238)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:06.891]  [00:07:39.039][info  ][EM] ??1 [E:60955i S:7471 M:3253086] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:07.754]  [00:07:39.908][info  ][EM] >>> [E:60955i S:7471 M:8703239 (Ack:3253086)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:07.796]  [00:07:39.938][info  ][EM] <<< [E:60955i S:7471 M:3253087 (Ack:8703239)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:07.796]  [00:07:39.938][info  ][EM] ??1 [E:60955i S:7471 M:3253087] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:08.539]  [00:07:40.687][info  ][EM] >>> [E:60955i S:7471 M:8703240 (Ack:3253087)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:08.570]  [00:07:40.717][info  ][EM] <<< [E:60955i S:7471 M:3253088 (Ack:8703240)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:08.570]  [00:07:40.717][info  ][EM] ??1 [E:60955i S:7471 M:3253088] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:09.432]  [00:07:41.580][info  ][EM] >>> [E:60955i S:7471 M:8703241 (Ack:3253088)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:09.463]  [00:07:41.610][info  ][EM] <<< [E:60955i S:7471 M:3253089 (Ack:8703241)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:09.463]  [00:07:41.610][info  ][EM] ??1 [E:60955i S:7471 M:3253089] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5559ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:10.306]  [00:07:42.458][info  ][EM] >>> [E:60955i S:7471 M:8703242 (Ack:3253089)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:10.383]  [00:07:42.523][info  ][EM] <<< [E:60955i S:7471 M:3253090 (Ack:8703242)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:10.383]  [00:07:42.524][info  ][EM] ??1 [E:60955i S:7471 M:3253090] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5484ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:11.105]  [00:07:43.250][info  ][EM] >>> [E:60955i S:7471 M:8703243 (Ack:3253090)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:11.131]  [00:07:43.280][info  ][EM] <<< [E:60955i S:7471 M:3253091 (Ack:8703243)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:11.131]  [00:07:43.281][info  ][EM] ??1 [E:60955i S:7471 M:3253091] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:11.984]  [00:07:44.124][info  ][EM] >>> [E:60955i S:7471 M:8703244 (Ack:3253091)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:11.999]  [00:07:44.154][info  ][EM] <<< [E:60955i S:7471 M:3253092 (Ack:8703244)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:12.014]  [00:07:44.154][info  ][EM] ??1 [E:60955i S:7471 M:3253092] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:12.740]  [00:07:44.891][info  ][EM] >>> [E:60955i S:7471 M:8703245 (Ack:3253092)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:12.770]  [00:07:44.921][info  ][EM] <<< [E:60955i S:7471 M:3253093 (Ack:8703245)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:12.770]  [00:07:44.922][info  ][EM] ??1 [E:60955i S:7471 M:3253093] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5738ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:13.501]  [00:07:45.648][info  ][EM] >>> [E:60955i S:7471 M:8703246 (Ack:3253093)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:13.562]  [00:07:45.706][info  ][EM] <<< [E:60955i S:7471 M:3253094 (Ack:8703246)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:13.562]  [00:07:45.706][info  ][EM] ??1 [E:60955i S:7471 M:3253094] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:14.303]  [00:07:46.445][info  ][EM] >>> [E:60955i S:7471 M:8703247 (Ack:3253094)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:14.319]  [00:07:46.474][info  ][EM] <<< [E:60955i S:7471 M:3253095 (Ack:8703247)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:14.334]  [00:07:46.475][info  ][EM] ??1 [E:60955i S:7471 M:3253095] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:15.277]  [00:07:47.424][info  ][EM] >>> [E:60955i S:7471 M:8703248 (Ack:3253095)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:15.306]  [00:07:47.455][info  ][EM] <<< [E:60955i S:7471 M:3253096 (Ack:8703248)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:15.306]  [00:07:47.456][info  ][EM] ??1 [E:60955i S:7471 M:3253096] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:16.176]  [00:07:48.332][info  ][EM] >>> [E:60955i S:7471 M:8703249 (Ack:3253096)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:16.207]  [00:07:48.361][info  ][EM] <<< [E:60955i S:7471 M:3253097 (Ack:8703249)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:16.207]  [00:07:48.362][info  ][EM] ??1 [E:60955i S:7471 M:3253097] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:17.272]  [00:07:49.422][info  ][EM] >>> [E:60955i S:7471 M:8703250 (Ack:3253097)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:17.348]  [00:07:49.489][info  ][EM] <<< [E:60955i S:7471 M:3253098 (Ack:8703250)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:17.348]  [00:07:49.489][info  ][EM] ??1 [E:60955i S:7471 M:3253098] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:18.156]  [00:07:50.310][info  ][EM] >>> [E:60955i S:7471 M:8703251 (Ack:3253098)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:18.187]  [00:07:50.339][info  ][EM] <<< [E:60955i S:7471 M:3253099 (Ack:8703251)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:18.187]  [00:07:50.340][info  ][EM] ??1 [E:60955i S:7471 M:3253099] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:19.024]  [00:07:51.168][info  ][EM] >>> [E:60955i S:7471 M:8703252 (Ack:3253099)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:19.054]  [00:07:51.199][info  ][EM] <<< [E:60955i S:7471 M:3253100 (Ack:8703252)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:19.054]  [00:07:51.199][info  ][EM] ??1 [E:60955i S:7471 M:3253100] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:19.819]  [00:07:51.970][info  ][EM] >>> [E:60955i S:7471 M:8703253 (Ack:3253100)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:19.850]  [00:07:52.000][info  ][EM] <<< [E:60955i S:7471 M:3253101 (Ack:8703253)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:19.850]  [00:07:52.001][info  ][EM] ??1 [E:60955i S:7471 M:3253101] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5654ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:20.610]  [00:07:52.761][info  ][EM] >>> [E:60955i S:7471 M:8703254 (Ack:3253101)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:20.672]  [00:07:52.820][info  ][EM] <<< [E:60955i S:7471 M:3253102 (Ack:8703254)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:20.672]  [00:07:52.820][info  ][EM] ??1 [E:60955i S:7471 M:3253102] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5501ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:21.379]  [00:07:53.535][info  ][EM] >>> [E:60955i S:7471 M:8703255 (Ack:3253102)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:21.411]  [00:07:53.564][info  ][EM] <<< [E:60955i S:7471 M:3253103 (Ack:8703255)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:21.411]  [00:07:53.565][info  ][EM] ??1 [E:60955i S:7471 M:3253103] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:22.188]  [00:07:54.338][info  ][EM] >>> [E:60955i S:7471 M:8703256 (Ack:3253103)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:22.218]  [00:07:54.369][info  ][EM] <<< [E:60955i S:7471 M:3253104 (Ack:8703256)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:22.218]  [00:07:54.370][info  ][EM] ??1 [E:60955i S:7471 M:3253104] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:22.963]  [00:07:55.115][info  ][EM] >>> [E:60955i S:7471 M:8703257 (Ack:3253104)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:23.000]  [00:07:55.145][info  ][EM] <<< [E:60955i S:7471 M:3253105 (Ack:8703257)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:23.000]  [00:07:55.145][info  ][EM] ??1 [E:60955i S:7471 M:3253105] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5501ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:23.852]  [00:07:55.996][info  ][EM] >>> [E:60955i S:7471 M:8703258 (Ack:3253105)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:23.915]  [00:07:56.062][info  ][EM] <<< [E:60955i S:7471 M:3253106 (Ack:8703258)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:23.915]  [00:07:56.063][info  ][EM] ??1 [E:60955i S:7471 M:3253106] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5577ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:24.916]  [00:07:57.062][info  ][EM] >>> [E:60955i S:7471 M:8703259 (Ack:3253106)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:24.946]  [00:07:57.092][info  ][EM] <<< [E:60955i S:7471 M:3253107 (Ack:8703259)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:24.946]  [00:07:57.092][info  ][EM] ??1 [E:60955i S:7471 M:3253107] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:25.892]  [00:07:58.043][info  ][EM] >>> [E:60955i S:7471 M:8703260 (Ack:3253107)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:25.922]  [00:07:58.074][info  ][EM] <<< [E:60955i S:7471 M:3253108 (Ack:8703260)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:25.922]  [00:07:58.075][info  ][EM] ??1 [E:60955i S:7471 M:3253108] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:26.656]  [00:07:58.804][info  ][EM] >>> [E:60955i S:7471 M:8703261 (Ack:3253108)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:26.687]  [00:07:58.834][info  ][EM] <<< [E:60955i S:7471 M:3253109 (Ack:8703261)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:26.687]  [00:07:58.834][info  ][EM] ??1 [E:60955i S:7471 M:3253109] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:27.453]  [00:07:59.601][info  ][EM] >>> [E:60955i S:7471 M:8703262 (Ack:3253109)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:27.514]  [00:07:59.661][info  ][EM] <<< [E:60955i S:7471 M:3253110 (Ack:8703262)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:27.514]  [00:07:59.662][info  ][EM] ??1 [E:60955i S:7471 M:3253110] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:28.230]  [00:08:00.374][info  ][EM] >>> [E:60955i S:7471 M:8703263 (Ack:3253110)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:28.256]  [00:08:00.403][info  ][EM] <<< [E:60955i S:7471 M:3253111 (Ack:8703263)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:28.256]  [00:08:00.404][info  ][EM] ??1 [E:60955i S:7471 M:3253111] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5592ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:28.989]  [00:08:01.143][info  ][EM] >>> [E:60955i S:7471 M:8703264 (Ack:3253111)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:29.030]  [00:08:01.173][info  ][EM] <<< [E:60955i S:7471 M:3253112 (Ack:8703264)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:29.030]  [00:08:01.174][info  ][EM] ??1 [E:60955i S:7471 M:3253112] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:29.756]  [00:08:01.911][info  ][EM] >>> [E:60955i S:7471 M:8703265 (Ack:3253112)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:29.787]  [00:08:01.941][info  ][EM] <<< [E:60955i S:7471 M:3253113 (Ack:8703265)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:29.787]  [00:08:01.942][info  ][EM] ??1 [E:60955i S:7471 M:3253113] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:30.553]  [00:08:02.706][info  ][EM] >>> [E:60955i S:7471 M:8703266 (Ack:3253113)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:30.623]  [00:08:02.773][info  ][EM] <<< [E:60955i S:7471 M:3253114 (Ack:8703266)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:30.623]  [00:08:02.774][info  ][EM] ??1 [E:60955i S:7471 M:3253114] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5736ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:31.345]  [00:08:03.486][info  ][EM] >>> [E:60955i S:7471 M:8703267 (Ack:3253114)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:31.360]  [00:08:03.516][info  ][EM] <<< [E:60955i S:7471 M:3253115 (Ack:8703267)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:31.376]  [00:08:03.517][info  ][EM] ??1 [E:60955i S:7471 M:3253115] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:32.230]  [00:08:04.372][info  ][EM] >>> [E:60955i S:7471 M:8703268 (Ack:3253115)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:32.246]  [00:08:04.402][info  ][EM] <<< [E:60955i S:7471 M:3253116 (Ack:8703268)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:32.262]  [00:08:04.403][info  ][EM] ??1 [E:60955i S:7471 M:3253116] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:33.218]  [00:08:05.363][info  ][EM] >>> [E:60955i S:7471 M:8703269 (Ack:3253116)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:33.249]  [00:08:05.393][info  ][EM] <<< [E:60955i S:7471 M:3253117 (Ack:8703269)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:33.249]  [00:08:05.394][info  ][EM] ??1 [E:60955i S:7471 M:3253117] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5443ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:34.198]  [00:08:06.353][info  ][EM] >>> [E:60955i S:7471 M:8703270 (Ack:3253117)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:34.256]  [00:08:06.409][info  ][EM] <<< [E:60955i S:7471 M:3253118 (Ack:8703270)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:34.256]  [00:08:06.410][info  ][EM] ??1 [E:60955i S:7471 M:3253118] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:35.181]  [00:08:07.330][info  ][EM] >>> [E:60955i S:7471 M:8703271 (Ack:3253118)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:35.213]  [00:08:07.359][info  ][EM] <<< [E:60955i S:7471 M:3253119 (Ack:8703271)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:35.213]  [00:08:07.360][info  ][EM] ??1 [E:60955i S:7471 M:3253119] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5248ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:35.972]  [00:08:08.119][info  ][EM] >>> [E:60955i S:7471 M:8703272 (Ack:3253119)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:36.002]  [00:08:08.148][info  ][EM] <<< [E:60955i S:7471 M:3253120 (Ack:8703272)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:36.002]  [00:08:08.149][info  ][EM] ??1 [E:60955i S:7471 M:3253120] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:36.836]  [00:08:08.992][info  ][EM] >>> [E:60955i S:7471 M:8703273 (Ack:3253120)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:36.868]  [00:08:09.022][info  ][EM] <<< [E:60955i S:7471 M:3253121 (Ack:8703273)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:36.868]  [00:08:09.023][info  ][EM] ??1 [E:60955i S:7471 M:3253121] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5284ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:37.604]  [00:08:09.757][info  ][EM] >>> [E:60955i S:7471 M:8703274 (Ack:3253121)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:37.673]  [00:08:09.824][info  ][EM] <<< [E:60955i S:7471 M:3253122 (Ack:8703274)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:37.673]  [00:08:09.825][info  ][EM] ??1 [E:60955i S:7471 M:3253122] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:38.370]  [00:08:10.522][info  ][EM] >>> [E:60955i S:7471 M:8703275 (Ack:3253122)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:38.402]  [00:08:10.551][info  ][EM] <<< [E:60955i S:7471 M:3253123 (Ack:8703275)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:38.402]  [00:08:10.552][info  ][EM] ??1 [E:60955i S:7471 M:3253123] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5321ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:39.273]  [00:08:11.420][info  ][EM] >>> [E:60955i S:7471 M:8703276 (Ack:3253123)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:39.304]  [00:08:11.450][info  ][EM] <<< [E:60955i S:7471 M:3253124 (Ack:8703276)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:39.304]  [00:08:11.451][info  ][EM] ??1 [E:60955i S:7471 M:3253124] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:40.055]  [00:08:12.196][info  ][EM] >>> [E:60955i S:7471 M:8703277 (Ack:3253124)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:40.070]  [00:08:12.226][info  ][EM] <<< [E:60955i S:7471 M:3253125 (Ack:8703277)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:40.086]  [00:08:12.226][info  ][EM] ??1 [E:60955i S:7471 M:3253125] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:40.830]  [00:08:12.981][info  ][EM] >>> [E:60955i S:7471 M:8703278 (Ack:3253125)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:40.887]  [00:08:13.038][info  ][EM] <<< [E:60955i S:7471 M:3253126 (Ack:8703278)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:40.887]  [00:08:13.039][info  ][EM] ??1 [E:60955i S:7471 M:3253126] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:41.613]  [00:08:13.764][info  ][EM] >>> [E:60955i S:7471 M:8703279 (Ack:3253126)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:41.644]  [00:08:13.794][info  ][EM] <<< [E:60955i S:7471 M:3253127 (Ack:8703279)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:41.644]  [00:08:13.795][info  ][EM] ??1 [E:60955i S:7471 M:3253127] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:42.387]  [00:08:14.530][info  ][EM] >>> [E:60955i S:7471 M:8703280 (Ack:3253127)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:42.418]  [00:08:14.559][info  ][EM] <<< [E:60955i S:7471 M:3253128 (Ack:8703280)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:42.418]  [00:08:14.560][info  ][EM] ??1 [E:60955i S:7471 M:3253128] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:43.140]  [00:08:15.294][info  ][EM] >>> [E:60955i S:7471 M:8703281 (Ack:3253128)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:43.177]  [00:08:15.324][info  ][EM] <<< [E:60955i S:7471 M:3253129 (Ack:8703281)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:43.177]  [00:08:15.325][info  ][EM] ??1 [E:60955i S:7471 M:3253129] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:43.918]  [00:08:16.069][info  ][EM] >>> [E:60955i S:7471 M:8703282 (Ack:3253129)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:43.989]  [00:08:16.133][info  ][EM] <<< [E:60955i S:7471 M:3253130 (Ack:8703282)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:43.989]  [00:08:16.134][info  ][EM] ??1 [E:60955i S:7471 M:3253130] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:44.686]  [00:08:16.842][info  ][EM] >>> [E:60955i S:7471 M:8703283 (Ack:3253130)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:44.718]  [00:08:16.872][info  ][EM] <<< [E:60955i S:7471 M:3253131 (Ack:8703283)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:44.718]  [00:08:16.873][info  ][EM] ??1 [E:60955i S:7471 M:3253131] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:45.502]  [00:08:17.647][info  ][EM] >>> [E:60955i S:7471 M:8703284 (Ack:3253131)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:45.528]  [00:08:17.676][info  ][EM] <<< [E:60955i S:7471 M:3253132 (Ack:8703284)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:45.528]  [00:08:17.677][info  ][EM] ??1 [E:60955i S:7471 M:3253132] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:46.490]  [00:08:18.632][info  ][EM] >>> [E:60955i S:7471 M:8703285 (Ack:3253132)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:46.521]  [00:08:18.662][info  ][EM] <<< [E:60955i S:7471 M:3253133 (Ack:8703285)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:46.521]  [00:08:18.663][info  ][EM] ??1 [E:60955i S:7471 M:3253133] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:47.350]  [00:08:19.498][info  ][EM] >>> [E:60955i S:7471 M:8703286 (Ack:3253133)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:47.406]  [00:08:19.558][info  ][EM] <<< [E:60955i S:7471 M:3253134 (Ack:8703286)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:47.406]  [00:08:19.559][info  ][EM] ??1 [E:60955i S:7471 M:3253134] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:48.232]  [00:08:20.387][info  ][EM] >>> [E:60955i S:7471 M:8703287 (Ack:3253134)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:48.263]  [00:08:20.417][info  ][EM] <<< [E:60955i S:7471 M:3253135 (Ack:8703287)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:48.263]  [00:08:20.418][info  ][EM] ??1 [E:60955i S:7471 M:3253135] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:49.017]  [00:08:21.172][info  ][EM] >>> [E:60955i S:7471 M:8703288 (Ack:3253135)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:49.048]  [00:08:21.202][info  ][EM] <<< [E:60955i S:7471 M:3253136 (Ack:8703288)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:49.048]  [00:08:21.203][info  ][EM] ??1 [E:60955i S:7471 M:3253136] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5701ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:49.950]  [00:08:22.102][info  ][EM] >>> [E:60955i S:7471 M:8703289 (Ack:3253136)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:49.981]  [00:08:22.132][info  ][EM] <<< [E:60955i S:7471 M:3253137 (Ack:8703289)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:49.981]  [00:08:22.133][info  ][EM] ??1 [E:60955i S:7471 M:3253137] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:50.780]  [00:08:22.924][info  ][EM] >>> [E:60955i S:7471 M:8703290 (Ack:3253137)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:50.850]  [00:08:22.991][info  ][EM] <<< [E:60955i S:7471 M:3253138 (Ack:8703290)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:50.850]  [00:08:22.992][info  ][EM] ??1 [E:60955i S:7471 M:3253138] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:51.545]  [00:08:23.694][info  ][EM] >>> [E:60955i S:7471 M:8703291 (Ack:3253138)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:51.576]  [00:08:23.724][info  ][EM] <<< [E:60955i S:7471 M:3253139 (Ack:8703291)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:51.576]  [00:08:23.725][info  ][EM] ??1 [E:60955i S:7471 M:3253139] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5598ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:52.434]  [00:08:24.576][info  ][EM] >>> [E:60955i S:7471 M:8703292 (Ack:3253139)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:52.449]  [00:08:24.605][info  ][EM] <<< [E:60955i S:7471 M:3253140 (Ack:8703292)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:52.465]  [00:08:24.606][info  ][EM] ??1 [E:60955i S:7471 M:3253140] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:53.219]  [00:08:25.362][info  ][EM] >>> [E:60955i S:7471 M:8703293 (Ack:3253140)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:53.249]  [00:08:25.391][info  ][EM] <<< [E:60955i S:7471 M:3253141 (Ack:8703293)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:53.249]  [00:08:25.392][info  ][EM] ??1 [E:60955i S:7471 M:3253141] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:54.093]  [00:08:26.245][info  ][EM] >>> [E:60955i S:7471 M:8703294 (Ack:3253141)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:54.150]  [00:08:26.302][info  ][EM] <<< [E:60955i S:7471 M:3253142 (Ack:8703294)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:54.150]  [00:08:26.303][info  ][EM] ??1 [E:60955i S:7471 M:3253142] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:54.995]  [00:08:27.140][info  ][EM] >>> [E:60955i S:7471 M:8703295 (Ack:3253142)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:55.023]  [00:08:27.169][info  ][EM] <<< [E:60955i S:7471 M:3253143 (Ack:8703295)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:55.023]  [00:08:27.170][info  ][EM] ??1 [E:60955i S:7471 M:3253143] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5390ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:55.776]  [00:08:27.927][info  ][EM] >>> [E:60955i S:7471 M:8703296 (Ack:3253143)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:55.802]  [00:08:27.958][info  ][EM] <<< [E:60955i S:7471 M:3253144 (Ack:8703296)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:55.815]  [00:08:27.958][info  ][EM] ??1 [E:60955i S:7471 M:3253144] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:56.675]  [00:08:28.828][info  ][EM] >>> [E:60955i S:7471 M:8703297 (Ack:3253144)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:56.703]  [00:08:28.858][info  ][EM] <<< [E:60955i S:7471 M:3253145 (Ack:8703297)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:56.713]  [00:08:28.859][info  ][EM] ??1 [E:60955i S:7471 M:3253145] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5489ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:57.473]  [00:08:29.617][info  ][EM] >>> [E:60955i S:7471 M:8703298 (Ack:3253145)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:57.528]  [00:08:29.682][info  ][EM] <<< [E:60955i S:7471 M:3253146 (Ack:8703298)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:57.528]  [00:08:29.683][info  ][EM] ??1 [E:60955i S:7471 M:3253146] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:58.232]  [00:08:30.386][info  ][EM] >>> [E:60955i S:7471 M:8703299 (Ack:3253146)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:58.276]  [00:08:30.416][info  ][EM] <<< [E:60955i S:7471 M:3253147 (Ack:8703299)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:58.276]  [00:08:30.416][info  ][EM] ??1 [E:60955i S:7471 M:3253147] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:59.013]  [00:08:31.162][info  ][EM] >>> [E:60955i S:7471 M:8703300 (Ack:3253147)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:59.044]  [00:08:31.191][info  ][EM] <<< [E:60955i S:7471 M:3253148 (Ack:8703300)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:59.044]  [00:08:31.192][info  ][EM] ??1 [E:60955i S:7471 M:3253148] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[16:24:59.775]  [00:08:31.917][info  ][EM] >>> [E:60955i S:7471 M:8703301 (Ack:3253148)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:24:59.791]  [00:08:31.947][info  ][EM] <<< [E:60955i S:7471 M:3253149 (Ack:8703301)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:24:59.802]  [00:08:31.948][info  ][EM] ??1 [E:60955i S:7471 M:3253149] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:00.552]  [00:08:32.704][info  ][EM] >>> [E:60955i S:7471 M:8703302 (Ack:3253149)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:00.610]  [00:08:32.761][info  ][EM] <<< [E:60955i S:7471 M:3253150 (Ack:8703302)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:00.610]  [00:08:32.761][info  ][EM] ??1 [E:60955i S:7471 M:3253150] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:01.357]  [00:08:33.509][info  ][EM] >>> [E:60955i S:7471 M:8703303 (Ack:3253150)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:01.389]  [00:08:33.540][info  ][EM] <<< [E:60955i S:7471 M:3253151 (Ack:8703303)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:01.389]  [00:08:33.541][info  ][EM] ??1 [E:60955i S:7471 M:3253151] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:02.138]  [00:08:34.283][info  ][EM] >>> [E:60955i S:7471 M:8703304 (Ack:3253151)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:02.169]  [00:08:34.313][info  ][EM] <<< [E:60955i S:7471 M:3253152 (Ack:8703304)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:02.169]  [00:08:34.314][info  ][EM] ??1 [E:60955i S:7471 M:3253152] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5671ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:03.027]  [00:08:35.169][info  ][EM] >>> [E:60955i S:7471 M:8703305 (Ack:3253152)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:03.044]  [00:08:35.200][info  ][EM] <<< [E:60955i S:7471 M:3253153 (Ack:8703305)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:03.059]  [00:08:35.201][info  ][EM] ??1 [E:60955i S:7471 M:3253153] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5353ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:03.790]  [00:08:35.931][info  ][EM] >>> [E:60955i S:7471 M:8703306 (Ack:3253153)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:03.843]  [00:08:35.997][info  ][EM] <<< [E:60955i S:7471 M:3253154 (Ack:8703306)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:03.843]  [00:08:35.998][info  ][EM] ??1 [E:60955i S:7471 M:3253154] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5407ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:04.576]  [00:08:36.721][info  ][EM] >>> [E:60955i S:7471 M:8703307 (Ack:3253154)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:04.609]  [00:08:36.751][info  ][EM] <<< [E:60955i S:7471 M:3253155 (Ack:8703307)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:04.609]  [00:08:36.751][info  ][EM] ??1 [E:60955i S:7471 M:3253155] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:05.591]  [00:08:37.739][info  ][EM] >>> [E:60955i S:7471 M:8703308 (Ack:3253155)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:05.623]  [00:08:37.769][info  ][EM] <<< [E:60955i S:7471 M:3253156 (Ack:8703308)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:05.623]  [00:08:37.770][info  ][EM] ??1 [E:60955i S:7471 M:3253156] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:06.460]  [00:08:38.612][info  ][EM] >>> [E:60955i S:7471 M:8703309 (Ack:3253156)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:06.495]  [00:08:38.642][info  ][EM] <<< [E:60955i S:7471 M:3253157 (Ack:8703309)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:06.495]  [00:08:38.643][info  ][EM] ??1 [E:60955i S:7471 M:3253157] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:07.261]  [00:08:39.410][info  ][EM] >>> [E:60955i S:7471 M:8703310 (Ack:3253157)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:07.311]  [00:08:39.466][info  ][EM] <<< [E:60955i S:7471 M:3253158 (Ack:8703310)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:07.311]  [00:08:39.467][info  ][EM] ??1 [E:60955i S:7471 M:3253158] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:08.044]  [00:08:40.193][info  ][EM] >>> [E:60955i S:7471 M:8703311 (Ack:3253158)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:08.075]  [00:08:40.223][info  ][EM] <<< [E:60955i S:7471 M:3253159 (Ack:8703311)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:08.075]  [00:08:40.224][info  ][EM] ??1 [E:60955i S:7471 M:3253159] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:08.811]  [00:08:40.965][info  ][EM] >>> [E:60955i S:7471 M:8703312 (Ack:3253159)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:08.843]  [00:08:40.996][info  ][EM] <<< [E:60955i S:7471 M:3253160 (Ack:8703312)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:08.843]  [00:08:40.996][info  ][EM] ??1 [E:60955i S:7471 M:3253160] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5246ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:09.692]  [00:08:41.837][info  ][EM] >>> [E:60955i S:7471 M:8703313 (Ack:3253160)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:09.724]  [00:08:41.867][info  ][EM] <<< [E:60955i S:7471 M:3253161 (Ack:8703313)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:09.724]  [00:08:41.868][info  ][EM] ??1 [E:60955i S:7471 M:3253161] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:10.491]  [00:08:42.646][info  ][EM] >>> [E:60955i S:7471 M:8703314 (Ack:3253161)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:10.563]  [00:08:42.712][info  ][EM] <<< [E:60955i S:7471 M:3253162 (Ack:8703314)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:10.563]  [00:08:42.713][info  ][EM] ??1 [E:60955i S:7471 M:3253162] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:11.493]  [00:08:43.643][info  ][EM] >>> [E:60955i S:7471 M:8703315 (Ack:3253162)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:11.526]  [00:08:43.672][info  ][EM] <<< [E:60955i S:7471 M:3253163 (Ack:8703315)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:11.526]  [00:08:43.673][info  ][EM] ??1 [E:60955i S:7471 M:3253163] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5583ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:12.275]  [00:08:44.430][info  ][EM] >>> [E:60955i S:7471 M:8703316 (Ack:3253163)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:12.306]  [00:08:44.459][info  ][EM] <<< [E:60955i S:7471 M:3253164 (Ack:8703316)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:12.306]  [00:08:44.460][info  ][EM] ??1 [E:60955i S:7471 M:3253164] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:13.164]  [00:08:45.311][info  ][EM] >>> [E:60955i S:7471 M:8703317 (Ack:3253164)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:13.209]  [00:08:45.340][info  ][EM] <<< [E:60955i S:7471 M:3253165 (Ack:8703317)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:13.209]  [00:08:45.341][info  ][EM] ??1 [E:60955i S:7471 M:3253165] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:13.968]  [00:08:46.120][info  ][EM] >>> [E:60955i S:7471 M:8703318 (Ack:3253165)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:14.030]  [00:08:46.177][info  ][EM] <<< [E:60955i S:7471 M:3253166 (Ack:8703318)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:14.030]  [00:08:46.178][info  ][EM] ??1 [E:60955i S:7471 M:3253166] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:14.743]  [00:08:46.900][info  ][EM] >>> [E:60955i S:7471 M:8703319 (Ack:3253166)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:14.777]  [00:08:46.930][info  ][EM] <<< [E:60955i S:7471 M:3253167 (Ack:8703319)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:14.777]  [00:08:46.930][info  ][EM] ??1 [E:60955i S:7471 M:3253167] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:15.739]  [00:08:47.888][info  ][EM] >>> [E:60955i S:7471 M:8703320 (Ack:3253167)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:15.776]  [00:08:47.918][info  ][EM] <<< [E:60955i S:7471 M:3253168 (Ack:8703320)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:15.776]  [00:08:47.918][info  ][EM] ??1 [E:60955i S:7471 M:3253168] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:16.549]  [00:08:48.694][info  ][EM] >>> [E:60955i S:7471 M:8703321 (Ack:3253168)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:16.576]  [00:08:48.724][info  ][EM] <<< [E:60955i S:7471 M:3253169 (Ack:8703321)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:16.576]  [00:08:48.724][info  ][EM] ??1 [E:60955i S:7471 M:3253169] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:17.326]  [00:08:49.475][info  ][EM] >>> [E:60955i S:7471 M:8703322 (Ack:3253169)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:17.393]  [00:08:49.541][info  ][EM] <<< [E:60955i S:7471 M:3253170 (Ack:8703322)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:17.393]  [00:08:49.541][info  ][EM] ??1 [E:60955i S:7471 M:3253170] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:18.188]  [00:08:50.343][info  ][EM] >>> [E:60955i S:7471 M:8703323 (Ack:3253170)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:18.220]  [00:08:50.373][info  ][EM] <<< [E:60955i S:7471 M:3253171 (Ack:8703323)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:18.220]  [00:08:50.374][info  ][EM] ??1 [E:60955i S:7471 M:3253171] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:18.976]  [00:08:51.119][info  ][EM] >>> [E:60955i S:7471 M:8703324 (Ack:3253171)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:18.994]  [00:08:51.148][info  ][EM] <<< [E:60955i S:7471 M:3253172 (Ack:8703324)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:18.994]  [00:08:51.149][info  ][EM] ??1 [E:60955i S:7471 M:3253172] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:19.836]  [00:08:51.988][info  ][EM] >>> [E:60955i S:7471 M:8703325 (Ack:3253172)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:19.868]  [00:08:52.017][info  ][EM] <<< [E:60955i S:7471 M:3253173 (Ack:8703325)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:19.868]  [00:08:52.018][info  ][EM] ??1 [E:60955i S:7471 M:3253173] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5641ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:20.605]  [00:08:52.757][info  ][EM] >>> [E:60955i S:7471 M:8703326 (Ack:3253173)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:20.661]  [00:08:52.815][info  ][EM] <<< [E:60955i S:7471 M:3253174 (Ack:8703326)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:20.661]  [00:08:52.815][info  ][EM] ??1 [E:60955i S:7471 M:3253174] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:21.378]  [00:08:53.521][info  ][EM] >>> [E:60955i S:7471 M:8703327 (Ack:3253174)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:21.411]  [00:08:53.551][info  ][EM] <<< [E:60955i S:7471 M:3253175 (Ack:8703327)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:21.411]  [00:08:53.552][info  ][EM] ??1 [E:60955i S:7471 M:3253175] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:22.243]  [00:08:54.393][info  ][EM] >>> [E:60955i S:7471 M:8703328 (Ack:3253175)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:22.272]  [00:08:54.422][info  ][EM] <<< [E:60955i S:7471 M:3253176 (Ack:8703328)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:22.272]  [00:08:54.423][info  ][EM] ??1 [E:60955i S:7471 M:3253176] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:23.109]  [00:08:55.263][info  ][EM] >>> [E:60955i S:7471 M:8703329 (Ack:3253176)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:23.145]  [00:08:55.292][info  ][EM] <<< [E:60955i S:7471 M:3253177 (Ack:8703329)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:23.145]  [00:08:55.293][info  ][EM] ??1 [E:60955i S:7471 M:3253177] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:23.893]  [00:08:56.041][info  ][EM] >>> [E:60955i S:7471 M:8703330 (Ack:3253177)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:23.960]  [00:08:56.105][info  ][EM] <<< [E:60955i S:7471 M:3253178 (Ack:8703330)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:23.960]  [00:08:56.106][info  ][EM] ??1 [E:60955i S:7471 M:3253178] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:24.659]  [00:08:56.809][info  ][EM] >>> [E:60955i S:7471 M:8703331 (Ack:3253178)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:24.694]  [00:08:56.838][info  ][EM] <<< [E:60955i S:7471 M:3253179 (Ack:8703331)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:24.694]  [00:08:56.839][info  ][EM] ??1 [E:60955i S:7471 M:3253179] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:25.542]  [00:08:57.698][info  ][EM] >>> [E:60955i S:7471 M:8703332 (Ack:3253179)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:25.572]  [00:08:57.727][info  ][EM] <<< [E:60955i S:7471 M:3253180 (Ack:8703332)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:25.572]  [00:08:57.728][info  ][EM] ??1 [E:60955i S:7471 M:3253180] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:26.344]  [00:08:58.488][info  ][EM] >>> [E:60955i S:7471 M:8703333 (Ack:3253180)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:26.361]  [00:08:58.517][info  ][EM] <<< [E:60955i S:7471 M:3253181 (Ack:8703333)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:26.377]  [00:08:58.518][info  ][EM] ??1 [E:60955i S:7471 M:3253181] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:27.420]  [00:08:59.565][info  ][EM] >>> [E:60955i S:7471 M:8703334 (Ack:3253181)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:27.466]  [00:08:59.624][info  ][EM] <<< [E:60955i S:7471 M:3253182 (Ack:8703334)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:27.480]  [00:08:59.625][info  ][EM] ??1 [E:60955i S:7471 M:3253182] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:28.312]  [00:09:00.469][info  ][EM] >>> [E:60955i S:7471 M:8703335 (Ack:3253182)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:28.344]  [00:09:00.499][info  ][EM] <<< [E:60955i S:7471 M:3253183 (Ack:8703335)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:28.344]  [00:09:00.500][info  ][EM] ??1 [E:60955i S:7471 M:3253183] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:29.081]  [00:09:01.230][info  ][EM] >>> [E:60955i S:7471 M:8703336 (Ack:3253183)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:29.113]  [00:09:01.260][info  ][EM] <<< [E:60955i S:7471 M:3253184 (Ack:8703336)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:29.113]  [00:09:01.260][info  ][EM] ??1 [E:60955i S:7471 M:3253184] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:29.841]  [00:09:01.994][info  ][EM] >>> [E:60955i S:7471 M:8703337 (Ack:3253184)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:29.868]  [00:09:02.023][info  ][EM] <<< [E:60955i S:7471 M:3253185 (Ack:8703337)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:29.868]  [00:09:02.024][info  ][EM] ??1 [E:60955i S:7471 M:3253185] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:30.711]  [00:09:02.866][info  ][EM] >>> [E:60955i S:7471 M:8703338 (Ack:3253185)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:30.778]  [00:09:02.931][info  ][EM] <<< [E:60955i S:7471 M:3253186 (Ack:8703338)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:30.778]  [00:09:02.932][info  ][EM] ??1 [E:60955i S:7471 M:3253186] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:31.494]  [00:09:03.643][info  ][EM] >>> [E:60955i S:7471 M:8703339 (Ack:3253186)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:31.527]  [00:09:03.673][info  ][EM] <<< [E:60955i S:7471 M:3253187 (Ack:8703339)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:31.527]  [00:09:03.673][info  ][EM] ??1 [E:60955i S:7471 M:3253187] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:32.283]  [00:09:04.432][info  ][EM] >>> [E:60955i S:7471 M:8703340 (Ack:3253187)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:32.313]  [00:09:04.461][info  ][EM] <<< [E:60955i S:7471 M:3253188 (Ack:8703340)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:32.313]  [00:09:04.462][info  ][EM] ??1 [E:60955i S:7471 M:3253188] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5293ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:33.159]  [00:09:05.314][info  ][EM] >>> [E:60955i S:7471 M:8703341 (Ack:3253188)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:33.192]  [00:09:05.343][info  ][EM] <<< [E:60955i S:7471 M:3253189 (Ack:8703341)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:33.192]  [00:09:05.344][info  ][EM] ??1 [E:60955i S:7471 M:3253189] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:33.954]  [00:09:06.101][info  ][EM] >>> [E:60955i S:7471 M:8703342 (Ack:3253189)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:34.013]  [00:09:06.158][info  ][EM] <<< [E:60955i S:7471 M:3253190 (Ack:8703342)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:34.013]  [00:09:06.159][info  ][EM] ??1 [E:60955i S:7471 M:3253190] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:34.727]  [00:09:06.869][info  ][EM] >>> [E:60955i S:7471 M:8703343 (Ack:3253190)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:34.743]  [00:09:06.898][info  ][EM] <<< [E:60955i S:7471 M:3253191 (Ack:8703343)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:34.743]  [00:09:06.899][info  ][EM] ??1 [E:60955i S:7471 M:3253191] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:35.595]  [00:09:07.744][info  ][EM] >>> [E:60955i S:7471 M:8703344 (Ack:3253191)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:35.625]  [00:09:07.773][info  ][EM] <<< [E:60955i S:7471 M:3253192 (Ack:8703344)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:35.625]  [00:09:07.774][info  ][EM] ??1 [E:60955i S:7471 M:3253192] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:36.577]  [00:09:08.729][info  ][EM] >>> [E:60955i S:7471 M:8703345 (Ack:3253192)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:36.611]  [00:09:08.759][info  ][EM] <<< [E:60955i S:7471 M:3253193 (Ack:8703345)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:36.611]  [00:09:08.760][info  ][EM] ??1 [E:60955i S:7471 M:3253193] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:37.344]  [00:09:09.500][info  ][EM] >>> [E:60955i S:7471 M:8703346 (Ack:3253193)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:37.426]  [00:09:09.570][info  ][EM] <<< [E:60955i S:7471 M:3253194 (Ack:8703346)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:37.426]  [00:09:09.571][info  ][EM] ??1 [E:60955i S:7471 M:3253194] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5583ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:38.161]  [00:09:10.305][info  ][EM] >>> [E:60955i S:7471 M:8703347 (Ack:3253194)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:38.178]  [00:09:10.335][info  ][EM] <<< [E:60955i S:7471 M:3253195 (Ack:8703347)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:38.194]  [00:09:10.335][info  ][EM] ??1 [E:60955i S:7471 M:3253195] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:38.927]  [00:09:11.079][info  ][EM] >>> [E:60955i S:7471 M:8703348 (Ack:3253195)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:38.961]  [00:09:11.109][info  ][EM] <<< [E:60955i S:7471 M:3253196 (Ack:8703348)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:38.961]  [00:09:11.110][info  ][EM] ??1 [E:60955i S:7471 M:3253196] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:39.795]  [00:09:11.949][info  ][EM] >>> [E:60955i S:7471 M:8703349 (Ack:3253196)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:39.826]  [00:09:11.979][info  ][EM] <<< [E:60955i S:7471 M:3253197 (Ack:8703349)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:39.826]  [00:09:11.980][info  ][EM] ??1 [E:60955i S:7471 M:3253197] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5351ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:40.679]  [00:09:12.828][info  ][EM] >>> [E:60955i S:7471 M:8703350 (Ack:3253197)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:40.735]  [00:09:12.883][info  ][EM] <<< [E:60955i S:7471 M:3253198 (Ack:8703350)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:40.735]  [00:09:12.884][info  ][EM] ??1 [E:60955i S:7471 M:3253198] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5458ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:41.559]  [00:09:13.703][info  ][EM] >>> [E:60955i S:7471 M:8703351 (Ack:3253198)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:41.589]  [00:09:13.733][info  ][EM] <<< [E:60955i S:7471 M:3253199 (Ack:8703351)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:41.589]  [00:09:13.733][info  ][EM] ??1 [E:60955i S:7471 M:3253199] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5738ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:42.342]  [00:09:14.486][info  ][EM] >>> [E:60955i S:7471 M:8703352 (Ack:3253199)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:42.358]  [00:09:14.515][info  ][EM] <<< [E:60955i S:7471 M:3253200 (Ack:8703352)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:42.369]  [00:09:14.516][info  ][EM] ??1 [E:60955i S:7471 M:3253200] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5654ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:43.120]  [00:09:15.267][info  ][EM] >>> [E:60955i S:7471 M:8703353 (Ack:3253200)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:43.151]  [00:09:15.296][info  ][EM] <<< [E:60955i S:7471 M:3253201 (Ack:8703353)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:43.151]  [00:09:15.297][info  ][EM] ??1 [E:60955i S:7471 M:3253201] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:43.902]  [00:09:16.052][info  ][EM] >>> [E:60955i S:7471 M:8703354 (Ack:3253201)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:43.973]  [00:09:16.119][info  ][EM] <<< [E:60955i S:7471 M:3253202 (Ack:8703354)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:43.973]  [00:09:16.120][info  ][EM] ??1 [E:60955i S:7471 M:3253202] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:44.781]  [00:09:16.936][info  ][EM] >>> [E:60955i S:7471 M:8703355 (Ack:3253202)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:44.811]  [00:09:16.965][info  ][EM] <<< [E:60955i S:7471 M:3253203 (Ack:8703355)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:44.811]  [00:09:16.966][info  ][EM] ??1 [E:60955i S:7471 M:3253203] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:45.583]  [00:09:17.733][info  ][EM] >>> [E:60955i S:7471 M:8703356 (Ack:3253203)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:45.613]  [00:09:17.763][info  ][EM] <<< [E:60955i S:7471 M:3253204 (Ack:8703356)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:45.613]  [00:09:17.764][info  ][EM] ??1 [E:60955i S:7471 M:3253204] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:46.485]  [00:09:18.639][info  ][EM] >>> [E:60955i S:7471 M:8703357 (Ack:3253204)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:46.516]  [00:09:18.668][info  ][EM] <<< [E:60955i S:7471 M:3253205 (Ack:8703357)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:46.516]  [00:09:18.669][info  ][EM] ??1 [E:60955i S:7471 M:3253205] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:47.259]  [00:09:19.404][info  ][EM] >>> [E:60955i S:7471 M:8703358 (Ack:3253205)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:47.319]  [00:09:19.464][info  ][EM] <<< [E:60955i S:7471 M:3253206 (Ack:8703358)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:47.319]  [00:09:19.465][info  ][EM] ??1 [E:60955i S:7471 M:3253206] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:48.030]  [00:09:20.186][info  ][EM] >>> [E:60955i S:7471 M:8703359 (Ack:3253206)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:48.061]  [00:09:20.215][info  ][EM] <<< [E:60955i S:7471 M:3253207 (Ack:8703359)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:48.061]  [00:09:20.216][info  ][EM] ??1 [E:60955i S:7471 M:3253207] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:49.018]  [00:09:21.175][info  ][EM] >>> [E:60955i S:7471 M:8703360 (Ack:3253207)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:49.057]  [00:09:21.206][info  ][EM] <<< [E:60955i S:7471 M:3253208 (Ack:8703360)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:49.057]  [00:09:21.206][info  ][EM] ??1 [E:60955i S:7471 M:3253208] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:49.900]  [00:09:22.054][info  ][EM] >>> [E:60955i S:7471 M:8703361 (Ack:3253208)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:49.929]  [00:09:22.084][info  ][EM] <<< [E:60955i S:7471 M:3253209 (Ack:8703361)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:49.929]  [00:09:22.084][info  ][EM] ??1 [E:60955i S:7471 M:3253209] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:50.672]  [00:09:22.828][info  ][EM] >>> [E:60955i S:7471 M:8703362 (Ack:3253209)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:50.741]  [00:09:22.897][info  ][EM] <<< [E:60955i S:7471 M:3253210 (Ack:8703362)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:50.741]  [00:09:22.898][info  ][EM] ??1 [E:60955i S:7471 M:3253210] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5261ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:51.460]  [00:09:23.607][info  ][EM] >>> [E:60955i S:7471 M:8703363 (Ack:3253210)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:51.491]  [00:09:23.636][info  ][EM] <<< [E:60955i S:7471 M:3253211 (Ack:8703363)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:51.491]  [00:09:23.637][info  ][EM] ??1 [E:60955i S:7471 M:3253211] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:52.238]  [00:09:24.381][info  ][EM] >>> [E:60955i S:7471 M:8703364 (Ack:3253211)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:52.253]  [00:09:24.411][info  ][EM] <<< [E:60955i S:7471 M:3253212 (Ack:8703364)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:52.264]  [00:09:24.412][info  ][EM] ??1 [E:60955i S:7471 M:3253212] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:53.001]  [00:09:25.160][info  ][EM] >>> [E:60955i S:7471 M:8703365 (Ack:3253212)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:53.043]  [00:09:25.189][info  ][EM] <<< [E:60955i S:7471 M:3253213 (Ack:8703365)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:53.043]  [00:09:25.190][info  ][EM] ??1 [E:60955i S:7471 M:3253213] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:53.880]  [00:09:26.032][info  ][EM] >>> [E:60955i S:7471 M:8703366 (Ack:3253213)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:53.938]  [00:09:26.088][info  ][EM] <<< [E:60955i S:7471 M:3253214 (Ack:8703366)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:53.938]  [00:09:26.089][info  ][EM] ??1 [E:60955i S:7471 M:3253214] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5433ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:54.654]  [00:09:26.809][info  ][EM] >>> [E:60955i S:7471 M:8703367 (Ack:3253214)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:54.683]  [00:09:26.839][info  ][EM] <<< [E:60955i S:7471 M:3253215 (Ack:8703367)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:54.683]  [00:09:26.840][info  ][EM] ??1 [E:60955i S:7471 M:3253215] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5699ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:55.427]  [00:09:27.574][info  ][EM] >>> [E:60955i S:7471 M:8703368 (Ack:3253215)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:55.456]  [00:09:27.603][info  ][EM] <<< [E:60955i S:7471 M:3253216 (Ack:8703368)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:55.456]  [00:09:27.604][info  ][EM] ??1 [E:60955i S:7471 M:3253216] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5261ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:56.283]  [00:09:28.436][info  ][EM] >>> [E:60955i S:7471 M:8703369 (Ack:3253216)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:56.314]  [00:09:28.466][info  ][EM] <<< [E:60955i S:7471 M:3253217 (Ack:8703369)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:56.314]  [00:09:28.467][info  ][EM] ??1 [E:60955i S:7471 M:3253217] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5269ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:57.163]  [00:09:29.313][info  ][EM] >>> [E:60955i S:7471 M:8703370 (Ack:3253217)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:57.231]  [00:09:29.381][info  ][EM] <<< [E:60955i S:7471 M:3253218 (Ack:8703370)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:57.231]  [00:09:29.381][info  ][EM] ??1 [E:60955i S:7471 M:3253218] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:58.258]  [00:09:30.416][info  ][EM] >>> [E:60955i S:7471 M:8703371 (Ack:3253218)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:58.299]  [00:09:30.445][info  ][EM] <<< [E:60955i S:7471 M:3253219 (Ack:8703371)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:58.299]  [00:09:30.446][info  ][EM] ??1 [E:60955i S:7471 M:3253219] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[16:25:59.372]  [00:09:31.521][info  ][EM] >>> [E:60955i S:7471 M:8703372 (Ack:3253219)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:25:59.398]  [00:09:31.551][info  ][EM] <<< [E:60955i S:7471 M:3253220 (Ack:8703372)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:25:59.398]  [00:09:31.552][info  ][EM] ??1 [E:60955i S:7471 M:3253220] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:00.672]  [00:09:32.815][info  ][EM] >>> [E:60955i S:7471 M:8703373 (Ack:3253220)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:00.688]  [00:09:32.844][info  ][EM] <<< [E:60955i S:7471 M:3253221 (Ack:8703373)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:00.688]  [00:09:32.845][info  ][EM] ??1 [E:60955i S:7471 M:3253221] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:01.529]  [00:09:33.683][info  ][EM] >>> [E:60955i S:7471 M:8703374 (Ack:3253221)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:01.593]  [00:09:33.740][info  ][EM] <<< [E:60955i S:7471 M:3253222 (Ack:8703374)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:01.593]  [00:09:33.741][info  ][EM] ??1 [E:60955i S:7471 M:3253222] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:02.421]  [00:09:34.571][info  ][EM] >>> [E:60955i S:7471 M:8703375 (Ack:3253222)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:02.452]  [00:09:34.600][info  ][EM] <<< [E:60955i S:7471 M:3253223 (Ack:8703375)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:02.452]  [00:09:34.601][info  ][EM] ??1 [E:60955i S:7471 M:3253223] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:03.214]  [00:09:35.359][info  ][EM] >>> [E:60955i S:7471 M:8703376 (Ack:3253223)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:03.246]  [00:09:35.389][info  ][EM] <<< [E:60955i S:7471 M:3253224 (Ack:8703376)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:03.246]  [00:09:35.389][info  ][EM] ??1 [E:60955i S:7471 M:3253224] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5525ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:03.978]  [00:09:36.126][info  ][EM] >>> [E:60955i S:7471 M:8703377 (Ack:3253224)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:04.010]  [00:09:36.157][info  ][EM] <<< [E:60955i S:7471 M:3253225 (Ack:8703377)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:04.010]  [00:09:36.157][info  ][EM] ??1 [E:60955i S:7471 M:3253225] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:04.759]  [00:09:36.903][info  ][EM] >>> [E:60955i S:7471 M:8703378 (Ack:3253225)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:04.823]  [00:09:36.968][info  ][EM] <<< [E:60955i S:7471 M:3253226 (Ack:8703378)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:04.823]  [00:09:36.969][info  ][EM] ??1 [E:60955i S:7471 M:3253226] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:05.508]  [00:09:37.659][info  ][EM] >>> [E:60955i S:7471 M:8703379 (Ack:3253226)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:05.540]  [00:09:37.688][info  ][EM] <<< [E:60955i S:7471 M:3253227 (Ack:8703379)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:05.540]  [00:09:37.689][info  ][EM] ??1 [E:60955i S:7471 M:3253227] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:06.494]  [00:09:38.649][info  ][EM] >>> [E:60955i S:7471 M:8703380 (Ack:3253227)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:06.526]  [00:09:38.679][info  ][EM] <<< [E:60955i S:7471 M:3253228 (Ack:8703380)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:06.526]  [00:09:38.680][info  ][EM] ??1 [E:60955i S:7471 M:3253228] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:07.289]  [00:09:39.445][info  ][EM] >>> [E:60955i S:7471 M:8703381 (Ack:3253228)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:07.321]  [00:09:39.475][info  ][EM] <<< [E:60955i S:7471 M:3253229 (Ack:8703381)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:07.321]  [00:09:39.476][info  ][EM] ??1 [E:60955i S:7471 M:3253229] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:08.259]  [00:09:40.416][info  ][EM] >>> [E:60955i S:7471 M:8703382 (Ack:3253229)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:08.322]  [00:09:40.473][info  ][EM] <<< [E:60955i S:7471 M:3253230 (Ack:8703382)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:08.322]  [00:09:40.474][info  ][EM] ??1 [E:60955i S:7471 M:3253230] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:09.039]  [00:09:41.184][info  ][EM] >>> [E:60955i S:7471 M:8703383 (Ack:3253230)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:09.071]  [00:09:41.214][info  ][EM] <<< [E:60955i S:7471 M:3253231 (Ack:8703383)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:09.071]  [00:09:41.214][info  ][EM] ??1 [E:60955i S:7471 M:3253231] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:09.820]  [00:09:41.973][info  ][EM] >>> [E:60955i S:7471 M:8703384 (Ack:3253231)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:09.852]  [00:09:42.002][info  ][EM] <<< [E:60955i S:7471 M:3253232 (Ack:8703384)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:09.852]  [00:09:42.003][info  ][EM] ??1 [E:60955i S:7471 M:3253232] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:10.947]  [00:09:43.092][info  ][EM] >>> [E:60955i S:7471 M:8703385 (Ack:3253232)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:10.979]  [00:09:43.123][info  ][EM] <<< [E:60955i S:7471 M:3253233 (Ack:8703385)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:10.979]  [00:09:43.123][info  ][EM] ??1 [E:60955i S:7471 M:3253233] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5691ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:11.726]  [00:09:43.876][info  ][EM] >>> [E:60955i S:7471 M:8703386 (Ack:3253233)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:11.790]  [00:09:43.943][info  ][EM] <<< [E:60955i S:7471 M:3253234 (Ack:8703386)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:11.790]  [00:09:43.943][info  ][EM] ??1 [E:60955i S:7471 M:3253234] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:12.618]  [00:09:44.765][info  ][EM] >>> [E:60955i S:7471 M:8703387 (Ack:3253234)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:12.650]  [00:09:44.795][info  ][EM] <<< [E:60955i S:7471 M:3253235 (Ack:8703387)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:12.650]  [00:09:44.796][info  ][EM] ??1 [E:60955i S:7471 M:3253235] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:13.494]  [00:09:45.648][info  ][EM] >>> [E:60955i S:7471 M:8703388 (Ack:3253235)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:13.525]  [00:09:45.678][info  ][EM] <<< [E:60955i S:7471 M:3253236 (Ack:8703388)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:13.525]  [00:09:45.679][info  ][EM] ??1 [E:60955i S:7471 M:3253236] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:14.478]  [00:09:46.633][info  ][EM] >>> [E:60955i S:7471 M:8703389 (Ack:3253236)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:14.510]  [00:09:46.664][info  ][EM] <<< [E:60955i S:7471 M:3253237 (Ack:8703389)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:14.510]  [00:09:46.664][info  ][EM] ??1 [E:60955i S:7471 M:3253237] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:15.275]  [00:09:47.419][info  ][EM] >>> [E:60955i S:7471 M:8703390 (Ack:3253237)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:15.322]  [00:09:47.477][info  ][EM] <<< [E:60955i S:7471 M:3253238 (Ack:8703390)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:15.322]  [00:09:47.478][info  ][EM] ??1 [E:60955i S:7471 M:3253238] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:16.053]  [00:09:48.198][info  ][EM] >>> [E:60955i S:7471 M:8703391 (Ack:3253238)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:16.069]  [00:09:48.228][info  ][EM] <<< [E:60955i S:7471 M:3253239 (Ack:8703391)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:16.085]  [00:09:48.229][info  ][EM] ??1 [E:60955i S:7471 M:3253239] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5430ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:16.849]  [00:09:48.998][info  ][EM] >>> [E:60955i S:7471 M:8703392 (Ack:3253239)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:16.880]  [00:09:49.027][info  ][EM] <<< [E:60955i S:7471 M:3253240 (Ack:8703392)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:16.880]  [00:09:49.028][info  ][EM] ??1 [E:60955i S:7471 M:3253240] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:17.851]  [00:09:49.998][info  ][EM] >>> [E:60955i S:7471 M:8703393 (Ack:3253240)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:17.883]  [00:09:50.028][info  ][EM] <<< [E:60955i S:7471 M:3253241 (Ack:8703393)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:17.883]  [00:09:50.028][info  ][EM] ??1 [E:60955i S:7471 M:3253241] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:18.725]  [00:09:50.876][info  ][EM] >>> [E:60955i S:7471 M:8703394 (Ack:3253241)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:18.788]  [00:09:50.943][info  ][EM] <<< [E:60955i S:7471 M:3253242 (Ack:8703394)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:18.788]  [00:09:50.944][info  ][EM] ??1 [E:60955i S:7471 M:3253242] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5682ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:19.535]  [00:09:51.686][info  ][EM] >>> [E:60955i S:7471 M:8703395 (Ack:3253242)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:19.567]  [00:09:51.715][info  ][EM] <<< [E:60955i S:7471 M:3253243 (Ack:8703395)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:19.567]  [00:09:51.716][info  ][EM] ??1 [E:60955i S:7471 M:3253243] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:20.457]  [00:09:52.606][info  ][EM] >>> [E:60955i S:7471 M:8703396 (Ack:3253243)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:20.489]  [00:09:52.635][info  ][EM] <<< [E:60955i S:7471 M:3253244 (Ack:8703396)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:20.489]  [00:09:52.636][info  ][EM] ??1 [E:60955i S:7471 M:3253244] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:21.238]  [00:09:53.393][info  ][EM] >>> [E:60955i S:7471 M:8703397 (Ack:3253244)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:21.270]  [00:09:53.423][info  ][EM] <<< [E:60955i S:7471 M:3253245 (Ack:8703397)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:21.270]  [00:09:53.423][info  ][EM] ??1 [E:60955i S:7471 M:3253245] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5699ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:22.115]  [00:09:54.267][info  ][EM] >>> [E:60955i S:7471 M:8703398 (Ack:3253245)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:22.178]  [00:09:54.326][info  ][EM] <<< [E:60955i S:7471 M:3253246 (Ack:8703398)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:22.178]  [00:09:54.327][info  ][EM] ??1 [E:60955i S:7471 M:3253246] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:23.004]  [00:09:55.154][info  ][EM] >>> [E:60955i S:7471 M:8703399 (Ack:3253246)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:23.036]  [00:09:55.184][info  ][EM] <<< [E:60955i S:7471 M:3253247 (Ack:8703399)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:23.036]  [00:09:55.185][info  ][EM] ??1 [E:60955i S:7471 M:3253247] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:23.896]  [00:09:56.053][info  ][EM] >>> [E:60955i S:7471 M:8703400 (Ack:3253247)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:23.928]  [00:09:56.083][info  ][EM] <<< [E:60955i S:7471 M:3253248 (Ack:8703400)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:23.928]  [00:09:56.083][info  ][EM] ??1 [E:60955i S:7471 M:3253248] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:24.775]  [00:09:56.924][info  ][EM] >>> [E:60955i S:7471 M:8703401 (Ack:3253248)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:24.807]  [00:09:56.955][info  ][EM] <<< [E:60955i S:7471 M:3253249 (Ack:8703401)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:24.807]  [00:09:56.956][info  ][EM] ??1 [E:60955i S:7471 M:3253249] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:25.669]  [00:09:57.818][info  ][EM] >>> [E:60955i S:7471 M:8703402 (Ack:3253249)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:25.732]  [00:09:57.888][info  ][EM] <<< [E:60955i S:7471 M:3253250 (Ack:8703402)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:25.732]  [00:09:57.888][info  ][EM] ??1 [E:60955i S:7471 M:3253250] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5622ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:26.540]  [00:09:58.684][info  ][EM] >>> [E:60955i S:7471 M:8703403 (Ack:3253250)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:26.555]  [00:09:58.714][info  ][EM] <<< [E:60955i S:7471 M:3253251 (Ack:8703403)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:26.570]  [00:09:58.714][info  ][EM] ??1 [E:60955i S:7471 M:3253251] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5263ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:27.292]  [00:09:59.448][info  ][EM] >>> [E:60955i S:7471 M:8703404 (Ack:3253251)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:27.324]  [00:09:59.478][info  ][EM] <<< [E:60955i S:7471 M:3253252 (Ack:8703404)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:27.324]  [00:09:59.478][info  ][EM] ??1 [E:60955i S:7471 M:3253252] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5263ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:28.271]  [00:10:00.429][info  ][EM] >>> [E:60955i S:7471 M:8703405 (Ack:3253252)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:28.302]  [00:10:00.458][info  ][EM] <<< [E:60955i S:7471 M:3253253 (Ack:8703405)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:28.302]  [00:10:00.459][info  ][EM] ??1 [E:60955i S:7471 M:3253253] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5299ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:29.051]  [00:10:01.208][info  ][EM] >>> [E:60955i S:7471 M:8703406 (Ack:3253253)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:29.114]  [00:10:01.266][info  ][EM] <<< [E:60955i S:7471 M:3253254 (Ack:8703406)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:29.114]  [00:10:01.267][info  ][EM] ??1 [E:60955i S:7471 M:3253254] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:29.834]  [00:10:01.986][info  ][EM] >>> [E:60955i S:7471 M:8703407 (Ack:3253254)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:29.866]  [00:10:02.016][info  ][EM] <<< [E:60955i S:7471 M:3253255 (Ack:8703407)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:29.866]  [00:10:02.016][info  ][EM] ??1 [E:60955i S:7471 M:3253255] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:30.601]  [00:10:02.752][info  ][EM] >>> [E:60955i S:7471 M:8703408 (Ack:3253255)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:30.633]  [00:10:02.783][info  ][EM] <<< [E:60955i S:7471 M:3253256 (Ack:8703408)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:30.633]  [00:10:02.784][info  ][EM] ??1 [E:60955i S:7471 M:3253256] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5471ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:31.374]  [00:10:03.527][info  ][EM] >>> [E:60955i S:7471 M:8703409 (Ack:3253256)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:31.406]  [00:10:03.556][info  ][EM] <<< [E:60955i S:7471 M:3253257 (Ack:8703409)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:31.406]  [00:10:03.557][info  ][EM] ??1 [E:60955i S:7471 M:3253257] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:32.250]  [00:10:04.395][info  ][EM] >>> [E:60955i S:7471 M:8703410 (Ack:3253257)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:32.314]  [00:10:04.463][info  ][EM] <<< [E:60955i S:7471 M:3253258 (Ack:8703410)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:32.314]  [00:10:04.463][info  ][EM] ??1 [E:60955i S:7471 M:3253258] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:33.126]  [00:10:05.285][info  ][EM] >>> [E:60955i S:7471 M:8703411 (Ack:3253258)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:33.158]  [00:10:05.315][info  ][EM] <<< [E:60955i S:7471 M:3253259 (Ack:8703411)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:33.158]  [00:10:05.316][info  ][EM] ??1 [E:60955i S:7471 M:3253259] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:33.907]  [00:10:06.053][info  ][EM] >>> [E:60955i S:7471 M:8703412 (Ack:3253259)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:33.938]  [00:10:06.083][info  ][EM] <<< [E:60955i S:7471 M:3253260 (Ack:8703412)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:33.938]  [00:10:06.083][info  ][EM] ??1 [E:60955i S:7471 M:3253260] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:34.765]  [00:10:06.923][info  ][EM] >>> [E:60955i S:7471 M:8703413 (Ack:3253260)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:34.797]  [00:10:06.954][info  ][EM] <<< [E:60955i S:7471 M:3253261 (Ack:8703413)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:34.797]  [00:10:06.955][info  ][EM] ??1 [E:60955i S:7471 M:3253261] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:35.561]  [00:10:07.709][info  ][EM] >>> [E:60955i S:7471 M:8703414 (Ack:3253261)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:35.608]  [00:10:07.765][info  ][EM] <<< [E:60955i S:7471 M:3253262 (Ack:8703414)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:35.608]  [00:10:07.766][info  ][EM] ??1 [E:60955i S:7471 M:3253262] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:36.435]  [00:10:08.592][info  ][EM] >>> [E:60955i S:7471 M:8703415 (Ack:3253262)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:36.467]  [00:10:08.622][info  ][EM] <<< [E:60955i S:7471 M:3253263 (Ack:8703415)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:36.467]  [00:10:08.623][info  ][EM] ??1 [E:60955i S:7471 M:3253263] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:37.201]  [00:10:09.360][info  ][EM] >>> [E:60955i S:7471 M:8703416 (Ack:3253263)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:37.232]  [00:10:09.389][info  ][EM] <<< [E:60955i S:7471 M:3253264 (Ack:8703416)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:37.232]  [00:10:09.390][info  ][EM] ??1 [E:60955i S:7471 M:3253264] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:37.988]  [00:10:10.133][info  ][EM] >>> [E:60955i S:7471 M:8703417 (Ack:3253264)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:38.004]  [00:10:10.163][info  ][EM] <<< [E:60955i S:7471 M:3253265 (Ack:8703417)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:38.019]  [00:10:10.164][info  ][EM] ??1 [E:60955i S:7471 M:3253265] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:38.758]  [00:10:10.916][info  ][EM] >>> [E:60955i S:7471 M:8703418 (Ack:3253265)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:38.825]  [00:10:10.982][info  ][EM] <<< [E:60955i S:7471 M:3253266 (Ack:8703418)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:38.825]  [00:10:10.983][info  ][EM] ??1 [E:60955i S:7471 M:3253266] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:39.521]  [00:10:11.679][info  ][EM] >>> [E:60955i S:7471 M:8703419 (Ack:3253266)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:39.550]  [00:10:11.708][info  ][EM] <<< [E:60955i S:7471 M:3253267 (Ack:8703419)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:39.551]  [00:10:11.709][info  ][EM] ??1 [E:60955i S:7471 M:3253267] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5261ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:40.299]  [00:10:12.458][info  ][EM] >>> [E:60955i S:7471 M:8703420 (Ack:3253267)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:40.329]  [00:10:12.488][info  ][EM] <<< [E:60955i S:7471 M:3253268 (Ack:8703420)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:40.330]  [00:10:12.488][info  ][EM] ??1 [E:60955i S:7471 M:3253268] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:41.173]  [00:10:13.332][info  ][EM] >>> [E:60955i S:7471 M:8703421 (Ack:3253268)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:41.203]  [00:10:13.362][info  ][EM] <<< [E:60955i S:7471 M:3253269 (Ack:8703421)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:41.204]  [00:10:13.363][info  ][EM] ??1 [E:60955i S:7471 M:3253269] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:41.954]  [00:10:14.113][info  ][EM] >>> [E:60955i S:7471 M:8703422 (Ack:3253269)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:42.012]  [00:10:14.170][info  ][EM] <<< [E:60955i S:7471 M:3253270 (Ack:8703422)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:42.014]  [00:10:14.171][info  ][EM] ??1 [E:60955i S:7471 M:3253270] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:42.828]  [00:10:14.987][info  ][EM] >>> [E:60955i S:7471 M:8703423 (Ack:3253270)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:42.858]  [00:10:15.017][info  ][EM] <<< [E:60955i S:7471 M:3253271 (Ack:8703423)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:42.860]  [00:10:15.018][info  ][EM] ??1 [E:60955i S:7471 M:3253271] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:43.622]  [00:10:15.782][info  ][EM] >>> [E:60955i S:7471 M:8703424 (Ack:3253271)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:43.652]  [00:10:15.811][info  ][EM] <<< [E:60955i S:7471 M:3253272 (Ack:8703424)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:43.654]  [00:10:15.812][info  ][EM] ??1 [E:60955i S:7471 M:3253272] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5231ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:44.396]  [00:10:16.554][info  ][EM] >>> [E:60955i S:7471 M:8703425 (Ack:3253272)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:44.426]  [00:10:16.584][info  ][EM] <<< [E:60955i S:7471 M:3253273 (Ack:8703425)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:44.427]  [00:10:16.585][info  ][EM] ??1 [E:60955i S:7471 M:3253273] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:45.169]  [00:10:17.328][info  ][EM] >>> [E:60955i S:7471 M:8703426 (Ack:3253273)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:45.237]  [00:10:17.396][info  ][EM] <<< [E:60955i S:7471 M:3253274 (Ack:8703426)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:45.238]  [00:10:17.397][info  ][EM] ??1 [E:60955i S:7471 M:3253274] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:45.946]  [00:10:18.106][info  ][EM] >>> [E:60955i S:7471 M:8703427 (Ack:3253274)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:45.976]  [00:10:18.135][info  ][EM] <<< [E:60955i S:7471 M:3253275 (Ack:8703427)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:45.979]  [00:10:18.136][info  ][EM] ??1 [E:60955i S:7471 M:3253275] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:46.711]  [00:10:18.870][info  ][EM] >>> [E:60955i S:7471 M:8703428 (Ack:3253275)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:46.741]  [00:10:18.900][info  ][EM] <<< [E:60955i S:7471 M:3253276 (Ack:8703428)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:46.742]  [00:10:18.901][info  ][EM] ??1 [E:60955i S:7471 M:3253276] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:47.471]  [00:10:19.629][info  ][EM] >>> [E:60955i S:7471 M:8703429 (Ack:3253276)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:47.500]  [00:10:19.660][info  ][EM] <<< [E:60955i S:7471 M:3253277 (Ack:8703429)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:47.502]  [00:10:19.661][info  ][EM] ??1 [E:60955i S:7471 M:3253277] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5246ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:48.274]  [00:10:20.433][info  ][EM] >>> [E:60955i S:7471 M:8703430 (Ack:3253277)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:48.331]  [00:10:20.490][info  ][EM] <<< [E:60955i S:7471 M:3253278 (Ack:8703430)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:48.332]  [00:10:20.491][info  ][EM] ??1 [E:60955i S:7471 M:3253278] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5248ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:49.043]  [00:10:21.202][info  ][EM] >>> [E:60955i S:7471 M:8703431 (Ack:3253278)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:49.072]  [00:10:21.231][info  ][EM] <<< [E:60955i S:7471 M:3253279 (Ack:8703431)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:49.073]  [00:10:21.232][info  ][EM] ??1 [E:60955i S:7471 M:3253279] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:49.809]  [00:10:21.967][info  ][EM] >>> [E:60955i S:7471 M:8703432 (Ack:3253279)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:49.838]  [00:10:21.998][info  ][EM] <<< [E:60955i S:7471 M:3253280 (Ack:8703432)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:49.840]  [00:10:21.998][info  ][EM] ??1 [E:60955i S:7471 M:3253280] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5375ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:50.572]  [00:10:22.732][info  ][EM] >>> [E:60955i S:7471 M:8703433 (Ack:3253280)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:50.603]  [00:10:22.761][info  ][EM] <<< [E:60955i S:7471 M:3253281 (Ack:8703433)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:50.604]  [00:10:22.762][info  ][EM] ??1 [E:60955i S:7471 M:3253281] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:51.345]  [00:10:23.504][info  ][EM] >>> [E:60955i S:7471 M:8703434 (Ack:3253281)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:51.410]  [00:10:23.569][info  ][EM] <<< [E:60955i S:7471 M:3253282 (Ack:8703434)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:51.412]  [00:10:23.570][info  ][EM] ??1 [E:60955i S:7471 M:3253282] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:52.138]  [00:10:24.297][info  ][EM] >>> [E:60955i S:7471 M:8703435 (Ack:3253282)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:52.168]  [00:10:24.327][info  ][EM] <<< [E:60955i S:7471 M:3253283 (Ack:8703435)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:52.169]  [00:10:24.328][info  ][EM] ??1 [E:60955i S:7471 M:3253283] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5701ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:53.213]  [00:10:25.372][info  ][EM] >>> [E:60955i S:7471 M:8703436 (Ack:3253283)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:53.242]  [00:10:25.402][info  ][EM] <<< [E:60955i S:7471 M:3253284 (Ack:8703436)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:53.243]  [00:10:25.402][info  ][EM] ??1 [E:60955i S:7471 M:3253284] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5284ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:53.999]  [00:10:26.158][info  ][EM] >>> [E:60955i S:7471 M:8703437 (Ack:3253284)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:54.028]  [00:10:26.187][info  ][EM] <<< [E:60955i S:7471 M:3253285 (Ack:8703437)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:54.030]  [00:10:26.188][info  ][EM] ??1 [E:60955i S:7471 M:3253285] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5407ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:54.865]  [00:10:27.025][info  ][EM] >>> [E:60955i S:7471 M:8703438 (Ack:3253285)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:54.923]  [00:10:27.083][info  ][EM] <<< [E:60955i S:7471 M:3253286 (Ack:8703438)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:54.925]  [00:10:27.083][info  ][EM] ??1 [E:60955i S:7471 M:3253286] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:55.629]  [00:10:27.788][info  ][EM] >>> [E:60955i S:7471 M:8703439 (Ack:3253286)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:55.658]  [00:10:27.818][info  ][EM] <<< [E:60955i S:7471 M:3253287 (Ack:8703439)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:55.659]  [00:10:27.818][info  ][EM] ??1 [E:60955i S:7471 M:3253287] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:56.416]  [00:10:28.576][info  ][EM] >>> [E:60955i S:7471 M:8703440 (Ack:3253287)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:56.446]  [00:10:28.605][info  ][EM] <<< [E:60955i S:7471 M:3253288 (Ack:8703440)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:56.447]  [00:10:28.606][info  ][EM] ??1 [E:60955i S:7471 M:3253288] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:57.184]  [00:10:29.342][info  ][EM] >>> [E:60955i S:7471 M:8703441 (Ack:3253288)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:57.213]  [00:10:29.373][info  ][EM] <<< [E:60955i S:7471 M:3253289 (Ack:8703441)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:57.215]  [00:10:29.374][info  ][EM] ??1 [E:60955i S:7471 M:3253289] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:57.952]  [00:10:30.112][info  ][EM] >>> [E:60955i S:7471 M:8703442 (Ack:3253289)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:58.018]  [00:10:30.177][info  ][EM] <<< [E:60955i S:7471 M:3253290 (Ack:8703442)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:58.019]  [00:10:30.178][info  ][EM] ??1 [E:60955i S:7471 M:3253290] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:58.726]  [00:10:30.885][info  ][EM] >>> [E:60955i S:7471 M:8703443 (Ack:3253290)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:58.756]  [00:10:30.915][info  ][EM] <<< [E:60955i S:7471 M:3253291 (Ack:8703443)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:58.758]  [00:10:30.916][info  ][EM] ??1 [E:60955i S:7471 M:3253291] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5577ms from now [State:Active II:500 AI:2000 AT:4000]
[16:26:59.494]  [00:10:31.654][info  ][EM] >>> [E:60955i S:7471 M:8703444 (Ack:3253291)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:26:59.524]  [00:10:31.683][info  ][EM] <<< [E:60955i S:7471 M:3253292 (Ack:8703444)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:26:59.525]  [00:10:31.684][info  ][EM] ??1 [E:60955i S:7471 M:3253292] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:00.259]  [00:10:32.418][info  ][EM] >>> [E:60955i S:7471 M:8703445 (Ack:3253292)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:00.289]  [00:10:32.449][info  ][EM] <<< [E:60955i S:7471 M:3253293 (Ack:8703445)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:00.291]  [00:10:32.449][info  ][EM] ??1 [E:60955i S:7471 M:3253293] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:01.051]  [00:10:33.210][info  ][EM] >>> [E:60955i S:7471 M:8703446 (Ack:3253293)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:01.111]  [00:10:33.271][info  ][EM] <<< [E:60955i S:7471 M:3253294 (Ack:8703446)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:01.112]  [00:10:33.271][info  ][EM] ??1 [E:60955i S:7471 M:3253294] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:01.859]  [00:10:34.019][info  ][EM] >>> [E:60955i S:7471 M:8703447 (Ack:3253294)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:01.889]  [00:10:34.048][info  ][EM] <<< [E:60955i S:7471 M:3253295 (Ack:8703447)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:01.891]  [00:10:34.049][info  ][EM] ??1 [E:60955i S:7471 M:3253295] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:02.652]  [00:10:34.811][info  ][EM] >>> [E:60955i S:7471 M:8703448 (Ack:3253295)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:02.682]  [00:10:34.840][info  ][EM] <<< [E:60955i S:7471 M:3253296 (Ack:8703448)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:02.683]  [00:10:34.841][info  ][EM] ??1 [E:60955i S:7471 M:3253296] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5366ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:03.419]  [00:10:35.579][info  ][EM] >>> [E:60955i S:7471 M:8703449 (Ack:3253296)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:03.449]  [00:10:35.608][info  ][EM] <<< [E:60955i S:7471 M:3253297 (Ack:8703449)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:03.450]  [00:10:35.609][info  ][EM] ??1 [E:60955i S:7471 M:3253297] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:04.204]  [00:10:36.364][info  ][EM] >>> [E:60955i S:7471 M:8703450 (Ack:3253297)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:04.270]  [00:10:36.429][info  ][EM] <<< [E:60955i S:7471 M:3253298 (Ack:8703450)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:04.272]  [00:10:36.430][info  ][EM] ??1 [E:60955i S:7471 M:3253298] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:04.957]  [00:10:37.117][info  ][EM] >>> [E:60955i S:7471 M:8703451 (Ack:3253298)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:04.988]  [00:10:37.147][info  ][EM] <<< [E:60955i S:7471 M:3253299 (Ack:8703451)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:04.989]  [00:10:37.147][info  ][EM] ??1 [E:60955i S:7471 M:3253299] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5291ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:05.723]  [00:10:37.882][info  ][EM] >>> [E:60955i S:7471 M:8703452 (Ack:3253299)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:05.752]  [00:10:37.912][info  ][EM] <<< [E:60955i S:7471 M:3253300 (Ack:8703452)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:05.754]  [00:10:37.913][info  ][EM] ??1 [E:60955i S:7471 M:3253300] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:06.483]  [00:10:38.643][info  ][EM] >>> [E:60955i S:7471 M:8703453 (Ack:3253300)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:06.513]  [00:10:38.672][info  ][EM] <<< [E:60955i S:7471 M:3253301 (Ack:8703453)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:06.514]  [00:10:38.673][info  ][EM] ??1 [E:60955i S:7471 M:3253301] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:07.250]  [00:10:39.410][info  ][EM] >>> [E:60955i S:7471 M:8703454 (Ack:3253301)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:07.305]  [00:10:39.464][info  ][EM] <<< [E:60955i S:7471 M:3253302 (Ack:8703454)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:07.306]  [00:10:39.465][info  ][EM] ??1 [E:60955i S:7471 M:3253302] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:08.127]  [00:10:40.287][info  ][EM] >>> [E:60955i S:7471 M:8703455 (Ack:3253302)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:08.157]  [00:10:40.316][info  ][EM] <<< [E:60955i S:7471 M:3253303 (Ack:8703455)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:08.158]  [00:10:40.317][info  ][EM] ??1 [E:60955i S:7471 M:3253303] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:08.929]  [00:10:41.089][info  ][EM] >>> [E:60955i S:7471 M:8703456 (Ack:3253303)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:08.959]  [00:10:41.119][info  ][EM] <<< [E:60955i S:7471 M:3253304 (Ack:8703456)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:08.961]  [00:10:41.120][info  ][EM] ??1 [E:60955i S:7471 M:3253304] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:09.803]  [00:10:41.963][info  ][EM] >>> [E:60955i S:7471 M:8703457 (Ack:3253304)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:09.833]  [00:10:41.993][info  ][EM] <<< [E:60955i S:7471 M:3253305 (Ack:8703457)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:09.835]  [00:10:41.994][info  ][EM] ??1 [E:60955i S:7471 M:3253305] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:10.678]  [00:10:42.837][info  ][EM] >>> [E:60955i S:7471 M:8703458 (Ack:3253305)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:10.743]  [00:10:42.902][info  ][EM] <<< [E:60955i S:7471 M:3253306 (Ack:8703458)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:10.744]  [00:10:42.903][info  ][EM] ??1 [E:60955i S:7471 M:3253306] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:11.453]  [00:10:43.612][info  ][EM] >>> [E:60955i S:7471 M:8703459 (Ack:3253306)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:11.482]  [00:10:43.642][info  ][EM] <<< [E:60955i S:7471 M:3253307 (Ack:8703459)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:11.485]  [00:10:43.643][info  ][EM] ??1 [E:60955i S:7471 M:3253307] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:12.223]  [00:10:44.382][info  ][EM] >>> [E:60955i S:7471 M:8703460 (Ack:3253307)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:12.252]  [00:10:44.413][info  ][EM] <<< [E:60955i S:7471 M:3253308 (Ack:8703460)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:12.254]  [00:10:44.413][info  ][EM] ??1 [E:60955i S:7471 M:3253308] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:12.991]  [00:10:45.151][info  ][EM] >>> [E:60955i S:7471 M:8703461 (Ack:3253308)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:13.020]  [00:10:45.180][info  ][EM] <<< [E:60955i S:7471 M:3253309 (Ack:8703461)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:13.023]  [00:10:45.181][info  ][EM] ??1 [E:60955i S:7471 M:3253309] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:13.866]  [00:10:46.026][info  ][EM] >>> [E:60955i S:7471 M:8703462 (Ack:3253309)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:13.923]  [00:10:46.083][info  ][EM] <<< [E:60955i S:7471 M:3253310 (Ack:8703462)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:13.925]  [00:10:46.083][info  ][EM] ??1 [E:60955i S:7471 M:3253310] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5592ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:14.637]  [00:10:46.797][info  ][EM] >>> [E:60955i S:7471 M:8703463 (Ack:3253310)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:14.667]  [00:10:46.827][info  ][EM] <<< [E:60955i S:7471 M:3253311 (Ack:8703463)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:14.669]  [00:10:46.828][info  ][EM] ??1 [E:60955i S:7471 M:3253311] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:15.417]  [00:10:47.577][info  ][EM] >>> [E:60955i S:7471 M:8703464 (Ack:3253311)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:15.446]  [00:10:47.607][info  ][EM] <<< [E:60955i S:7471 M:3253312 (Ack:8703464)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:15.448]  [00:10:47.607][info  ][EM] ??1 [E:60955i S:7471 M:3253312] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:16.401]  [00:10:48.560][info  ][EM] >>> [E:60955i S:7471 M:8703465 (Ack:3253312)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:16.430]  [00:10:48.589][info  ][EM] <<< [E:60955i S:7471 M:3253313 (Ack:8703465)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:16.431]  [00:10:48.590][info  ][EM] ??1 [E:60955i S:7471 M:3253313] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:17.381]  [00:10:49.541][info  ][EM] >>> [E:60955i S:7471 M:8703466 (Ack:3253313)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:17.446]  [00:10:49.606][info  ][EM] <<< [E:60955i S:7471 M:3253314 (Ack:8703466)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:17.447]  [00:10:49.607][info  ][EM] ??1 [E:60955i S:7471 M:3253314] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:18.138]  [00:10:50.298][info  ][EM] >>> [E:60955i S:7471 M:8703467 (Ack:3253314)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:18.168]  [00:10:50.328][info  ][EM] <<< [E:60955i S:7471 M:3253315 (Ack:8703467)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:18.170]  [00:10:50.329][info  ][EM] ??1 [E:60955i S:7471 M:3253315] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:18.924]  [00:10:51.083][info  ][EM] >>> [E:60955i S:7471 M:8703468 (Ack:3253315)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:18.953]  [00:10:51.113][info  ][EM] <<< [E:60955i S:7471 M:3253316 (Ack:8703468)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:18.955]  [00:10:51.114][info  ][EM] ??1 [E:60955i S:7471 M:3253316] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:20.028]  [00:10:52.187][info  ][EM] >>> [E:60955i S:7471 M:8703469 (Ack:3253316)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:20.058]  [00:10:52.217][info  ][EM] <<< [E:60955i S:7471 M:3253317 (Ack:8703469)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:20.059]  [00:10:52.218][info  ][EM] ??1 [E:60955i S:7471 M:3253317] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5203ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:21.241]  [00:10:53.401][info  ][EM] >>> [E:60955i S:7471 M:8703470 (Ack:3253317)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:21.300]  [00:10:53.459][info  ][EM] <<< [E:60955i S:7471 M:3253318 (Ack:8703470)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:21.301]  [00:10:53.460][info  ][EM] ??1 [E:60955i S:7471 M:3253318] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:22.072]  [00:10:54.231][info  ][EM] >>> [E:60955i S:7471 M:8703471 (Ack:3253318)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:22.101]  [00:10:54.261][info  ][EM] <<< [E:60955i S:7471 M:3253319 (Ack:8703471)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:22.102]  [00:10:54.261][info  ][EM] ??1 [E:60955i S:7471 M:3253319] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:22.930]  [00:10:55.089][info  ][EM] >>> [E:60955i S:7471 M:8703472 (Ack:3253319)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:22.959]  [00:10:55.119][info  ][EM] <<< [E:60955i S:7471 M:3253320 (Ack:8703472)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:22.961]  [00:10:55.120][info  ][EM] ??1 [E:60955i S:7471 M:3253320] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:23.714]  [00:10:55.875][info  ][EM] >>> [E:60955i S:7471 M:8703473 (Ack:3253320)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:23.744]  [00:10:55.904][info  ][EM] <<< [E:60955i S:7471 M:3253321 (Ack:8703473)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:23.745]  [00:10:55.905][info  ][EM] ??1 [E:60955i S:7471 M:3253321] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:24.485]  [00:10:56.645][info  ][EM] >>> [E:60955i S:7471 M:8703474 (Ack:3253321)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:24.551]  [00:10:56.710][info  ][EM] <<< [E:60955i S:7471 M:3253322 (Ack:8703474)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:24.552]  [00:10:56.711][info  ][EM] ??1 [E:60955i S:7471 M:3253322] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:25.259]  [00:10:57.419][info  ][EM] >>> [E:60955i S:7471 M:8703475 (Ack:3253322)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:25.290]  [00:10:57.449][info  ][EM] <<< [E:60955i S:7471 M:3253323 (Ack:8703475)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:25.291]  [00:10:57.450][info  ][EM] ??1 [E:60955i S:7471 M:3253323] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:26.023]  [00:10:58.183][info  ][EM] >>> [E:60955i S:7471 M:8703476 (Ack:3253323)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:26.052]  [00:10:58.212][info  ][EM] <<< [E:60955i S:7471 M:3253324 (Ack:8703476)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:26.054]  [00:10:58.213][info  ][EM] ??1 [E:60955i S:7471 M:3253324] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:26.820]  [00:10:58.980][info  ][EM] >>> [E:60955i S:7471 M:8703477 (Ack:3253324)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:26.850]  [00:10:59.009][info  ][EM] <<< [E:60955i S:7471 M:3253325 (Ack:8703477)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:26.851]  [00:10:59.010][info  ][EM] ??1 [E:60955i S:7471 M:3253325] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:27.586]  [00:10:59.746][info  ][EM] >>> [E:60955i S:7471 M:8703478 (Ack:3253325)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:27.643]  [00:10:59.803][info  ][EM] <<< [E:60955i S:7471 M:3253326 (Ack:8703478)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:27.645]  [00:10:59.804][info  ][EM] ??1 [E:60955i S:7471 M:3253326] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:28.338]  [00:11:00.499][info  ][EM] >>> [E:60955i S:7471 M:8703479 (Ack:3253326)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:28.369]  [00:11:00.529][info  ][EM] <<< [E:60955i S:7471 M:3253327 (Ack:8703479)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:28.370]  [00:11:00.529][info  ][EM] ??1 [E:60955i S:7471 M:3253327] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:29.132]  [00:11:01.291][info  ][EM] >>> [E:60955i S:7471 M:8703480 (Ack:3253327)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:29.161]  [00:11:01.321][info  ][EM] <<< [E:60955i S:7471 M:3253328 (Ack:8703480)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:29.163]  [00:11:01.322][info  ][EM] ??1 [E:60955i S:7471 M:3253328] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:30.024]  [00:11:02.184][info  ][EM] >>> [E:60955i S:7471 M:8703481 (Ack:3253328)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:30.054]  [00:11:02.213][info  ][EM] <<< [E:60955i S:7471 M:3253329 (Ack:8703481)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:30.055]  [00:11:02.214][info  ][EM] ??1 [E:60955i S:7471 M:3253329] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:30.790]  [00:11:02.950][info  ][EM] >>> [E:60955i S:7471 M:8703482 (Ack:3253329)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:30.856]  [00:11:03.016][info  ][EM] <<< [E:60955i S:7471 M:3253330 (Ack:8703482)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:30.857]  [00:11:03.016][info  ][EM] ??1 [E:60955i S:7471 M:3253330] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5572ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:31.556]  [00:11:03.716][info  ][EM] >>> [E:60955i S:7471 M:8703483 (Ack:3253330)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:31.586]  [00:11:03.747][info  ][EM] <<< [E:60955i S:7471 M:3253331 (Ack:8703483)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:31.588]  [00:11:03.747][info  ][EM] ??1 [E:60955i S:7471 M:3253331] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5592ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:32.543]  [00:11:04.703][info  ][EM] >>> [E:60955i S:7471 M:8703484 (Ack:3253331)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:32.573]  [00:11:04.733][info  ][EM] <<< [E:60955i S:7471 M:3253332 (Ack:8703484)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:32.574]  [00:11:04.733][info  ][EM] ??1 [E:60955i S:7471 M:3253332] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:33.424]  [00:11:05.583][info  ][EM] >>> [E:60955i S:7471 M:8703485 (Ack:3253332)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:33.453]  [00:11:05.613][info  ][EM] <<< [E:60955i S:7471 M:3253333 (Ack:8703485)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:33.454]  [00:11:05.614][info  ][EM] ??1 [E:60955i S:7471 M:3253333] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5682ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:34.513]  [00:11:06.672][info  ][EM] >>> [E:60955i S:7471 M:8703486 (Ack:3253333)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:34.571]  [00:11:06.732][info  ][EM] <<< [E:60955i S:7471 M:3253334 (Ack:8703486)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:34.573]  [00:11:06.732][info  ][EM] ??1 [E:60955i S:7471 M:3253334] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:35.288]  [00:11:07.448][info  ][EM] >>> [E:60955i S:7471 M:8703487 (Ack:3253334)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:35.318]  [00:11:07.477][info  ][EM] <<< [E:60955i S:7471 M:3253335 (Ack:8703487)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:35.319]  [00:11:07.478][info  ][EM] ??1 [E:60955i S:7471 M:3253335] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:36.048]  [00:11:08.208][info  ][EM] >>> [E:60955i S:7471 M:8703488 (Ack:3253335)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:36.078]  [00:11:08.238][info  ][EM] <<< [E:60955i S:7471 M:3253336 (Ack:8703488)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:36.079]  [00:11:08.239][info  ][EM] ??1 [E:60955i S:7471 M:3253336] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:36.818]  [00:11:08.978][info  ][EM] >>> [E:60955i S:7471 M:8703489 (Ack:3253336)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:36.848]  [00:11:09.008][info  ][EM] <<< [E:60955i S:7471 M:3253337 (Ack:8703489)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:36.849]  [00:11:09.008][info  ][EM] ??1 [E:60955i S:7471 M:3253337] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5555ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:37.587]  [00:11:09.748][info  ][EM] >>> [E:60955i S:7471 M:8703490 (Ack:3253337)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:37.655]  [00:11:09.815][info  ][EM] <<< [E:60955i S:7471 M:3253338 (Ack:8703490)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:37.656]  [00:11:09.816][info  ][EM] ??1 [E:60955i S:7471 M:3253338] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:38.358]  [00:11:10.518][info  ][EM] >>> [E:60955i S:7471 M:8703491 (Ack:3253338)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:38.388]  [00:11:10.548][info  ][EM] <<< [E:60955i S:7471 M:3253339 (Ack:8703491)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:38.389]  [00:11:10.548][info  ][EM] ??1 [E:60955i S:7471 M:3253339] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:39.126]  [00:11:11.287][info  ][EM] >>> [E:60955i S:7471 M:8703492 (Ack:3253339)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:39.156]  [00:11:11.316][info  ][EM] <<< [E:60955i S:7471 M:3253340 (Ack:8703492)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:39.158]  [00:11:11.317][info  ][EM] ??1 [E:60955i S:7471 M:3253340] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:39.898]  [00:11:12.057][info  ][EM] >>> [E:60955i S:7471 M:8703493 (Ack:3253340)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:39.927]  [00:11:12.087][info  ][EM] <<< [E:60955i S:7471 M:3253341 (Ack:8703493)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:39.929]  [00:11:12.088][info  ][EM] ??1 [E:60955i S:7471 M:3253341] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:40.672]  [00:11:12.833][info  ][EM] >>> [E:60955i S:7471 M:8703494 (Ack:3253341)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:40.729]  [00:11:12.889][info  ][EM] <<< [E:60955i S:7471 M:3253342 (Ack:8703494)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:40.730]  [00:11:12.890][info  ][EM] ??1 [E:60955i S:7471 M:3253342] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:41.465]  [00:11:13.625][info  ][EM] >>> [E:60955i S:7471 M:8703495 (Ack:3253342)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:41.494]  [00:11:13.655][info  ][EM] <<< [E:60955i S:7471 M:3253343 (Ack:8703495)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:41.495]  [00:11:13.655][info  ][EM] ??1 [E:60955i S:7471 M:3253343] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:42.236]  [00:11:14.396][info  ][EM] >>> [E:60955i S:7471 M:8703496 (Ack:3253343)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:42.265]  [00:11:14.425][info  ][EM] <<< [E:60955i S:7471 M:3253344 (Ack:8703496)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:42.266]  [00:11:14.426][info  ][EM] ??1 [E:60955i S:7471 M:3253344] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:43.104]  [00:11:15.264][info  ][EM] >>> [E:60955i S:7471 M:8703497 (Ack:3253344)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:43.134]  [00:11:15.294][info  ][EM] <<< [E:60955i S:7471 M:3253345 (Ack:8703497)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:43.136]  [00:11:15.294][info  ][EM] ??1 [E:60955i S:7471 M:3253345] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:43.884]  [00:11:16.044][info  ][EM] >>> [E:60955i S:7471 M:8703498 (Ack:3253345)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:43.951]  [00:11:16.111][info  ][EM] <<< [E:60955i S:7471 M:3253346 (Ack:8703498)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:43.953]  [00:11:16.112][info  ][EM] ??1 [E:60955i S:7471 M:3253346] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:44.669]  [00:11:16.829][info  ][EM] >>> [E:60955i S:7471 M:8703499 (Ack:3253346)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:44.699]  [00:11:16.858][info  ][EM] <<< [E:60955i S:7471 M:3253347 (Ack:8703499)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:44.700]  [00:11:16.859][info  ][EM] ??1 [E:60955i S:7471 M:3253347] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:45.439]  [00:11:17.599][info  ][EM] >>> [E:60955i S:7471 M:8703500 (Ack:3253347)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:45.470]  [00:11:17.629][info  ][EM] <<< [E:60955i S:7471 M:3253348 (Ack:8703500)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:45.471]  [00:11:17.630][info  ][EM] ??1 [E:60955i S:7471 M:3253348] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:46.310]  [00:11:18.469][info  ][EM] >>> [E:60955i S:7471 M:8703501 (Ack:3253348)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:46.340]  [00:11:18.500][info  ][EM] <<< [E:60955i S:7471 M:3253349 (Ack:8703501)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:46.341]  [00:11:18.500][info  ][EM] ??1 [E:60955i S:7471 M:3253349] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:47.196]  [00:11:19.355][info  ][EM] >>> [E:60955i S:7471 M:8703502 (Ack:3253349)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:47.252]  [00:11:19.412][info  ][EM] <<< [E:60955i S:7471 M:3253350 (Ack:8703502)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:47.253]  [00:11:19.413][info  ][EM] ??1 [E:60955i S:7471 M:3253350] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:47.964]  [00:11:20.125][info  ][EM] >>> [E:60955i S:7471 M:8703503 (Ack:3253350)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:47.993]  [00:11:20.154][info  ][EM] <<< [E:60955i S:7471 M:3253351 (Ack:8703503)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:47.995]  [00:11:20.155][info  ][EM] ??1 [E:60955i S:7471 M:3253351] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5246ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:48.833]  [00:11:20.993][info  ][EM] >>> [E:60955i S:7471 M:8703504 (Ack:3253351)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:48.862]  [00:11:21.022][info  ][EM] <<< [E:60955i S:7471 M:3253352 (Ack:8703504)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:48.863]  [00:11:21.023][info  ][EM] ??1 [E:60955i S:7471 M:3253352] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5295ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:49.618]  [00:11:21.779][info  ][EM] >>> [E:60955i S:7471 M:8703505 (Ack:3253352)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:49.648]  [00:11:21.808][info  ][EM] <<< [E:60955i S:7471 M:3253353 (Ack:8703505)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:49.649]  [00:11:21.809][info  ][EM] ??1 [E:60955i S:7471 M:3253353] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:50.590]  [00:11:22.750][info  ][EM] >>> [E:60955i S:7471 M:8703506 (Ack:3253353)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:50.656]  [00:11:22.816][info  ][EM] <<< [E:60955i S:7471 M:3253354 (Ack:8703506)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:50.658]  [00:11:22.817][info  ][EM] ??1 [E:60955i S:7471 M:3253354] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:51.363]  [00:11:23.523][info  ][EM] >>> [E:60955i S:7471 M:8703507 (Ack:3253354)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:51.392]  [00:11:23.552][info  ][EM] <<< [E:60955i S:7471 M:3253355 (Ack:8703507)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:51.393]  [00:11:23.553][info  ][EM] ??1 [E:60955i S:7471 M:3253355] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5433ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:52.131]  [00:11:24.291][info  ][EM] >>> [E:60955i S:7471 M:8703508 (Ack:3253355)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:52.162]  [00:11:24.322][info  ][EM] <<< [E:60955i S:7471 M:3253356 (Ack:8703508)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:52.164]  [00:11:24.323][info  ][EM] ??1 [E:60955i S:7471 M:3253356] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:53.009]  [00:11:25.169][info  ][EM] >>> [E:60955i S:7471 M:8703509 (Ack:3253356)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:53.039]  [00:11:25.200][info  ][EM] <<< [E:60955i S:7471 M:3253357 (Ack:8703509)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:53.041]  [00:11:25.200][info  ][EM] ??1 [E:60955i S:7471 M:3253357] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:53.777]  [00:11:25.937][info  ][EM] >>> [E:60955i S:7471 M:8703510 (Ack:3253357)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:53.834]  [00:11:25.994][info  ][EM] <<< [E:60955i S:7471 M:3253358 (Ack:8703510)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:53.835]  [00:11:25.995][info  ][EM] ??1 [E:60955i S:7471 M:3253358] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:54.763]  [00:11:26.923][info  ][EM] >>> [E:60955i S:7471 M:8703511 (Ack:3253358)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:54.793]  [00:11:26.954][info  ][EM] <<< [E:60955i S:7471 M:3253359 (Ack:8703511)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:54.794]  [00:11:26.955][info  ][EM] ??1 [E:60955i S:7471 M:3253359] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5622ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:55.524]  [00:11:27.683][info  ][EM] >>> [E:60955i S:7471 M:8703512 (Ack:3253359)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:55.553]  [00:11:27.713][info  ][EM] <<< [E:60955i S:7471 M:3253360 (Ack:8703512)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:55.554]  [00:11:27.714][info  ][EM] ??1 [E:60955i S:7471 M:3253360] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:56.403]  [00:11:28.563][info  ][EM] >>> [E:60955i S:7471 M:8703513 (Ack:3253360)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:56.433]  [00:11:28.592][info  ][EM] <<< [E:60955i S:7471 M:3253361 (Ack:8703513)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:56.434]  [00:11:28.593][info  ][EM] ??1 [E:60955i S:7471 M:3253361] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:57.170]  [00:11:29.330][info  ][EM] >>> [E:60955i S:7471 M:8703514 (Ack:3253361)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:57.234]  [00:11:29.395][info  ][EM] <<< [E:60955i S:7471 M:3253362 (Ack:8703514)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:57.237]  [00:11:29.396][info  ][EM] ??1 [E:60955i S:7471 M:3253362] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5577ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:58.045]  [00:11:30.206][info  ][EM] >>> [E:60955i S:7471 M:8703515 (Ack:3253362)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:58.075]  [00:11:30.235][info  ][EM] <<< [E:60955i S:7471 M:3253363 (Ack:8703515)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:58.076]  [00:11:30.236][info  ][EM] ??1 [E:60955i S:7471 M:3253363] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:58.913]  [00:11:31.074][info  ][EM] >>> [E:60955i S:7471 M:8703516 (Ack:3253363)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:58.943]  [00:11:31.104][info  ][EM] <<< [E:60955i S:7471 M:3253364 (Ack:8703516)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:58.945]  [00:11:31.104][info  ][EM] ??1 [E:60955i S:7471 M:3253364] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[16:27:59.670]  [00:11:31.830][info  ][EM] >>> [E:60955i S:7471 M:8703517 (Ack:3253364)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:27:59.700]  [00:11:31.860][info  ][EM] <<< [E:60955i S:7471 M:3253365 (Ack:8703517)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:27:59.701]  [00:11:31.860][info  ][EM] ??1 [E:60955i S:7471 M:3253365] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:00.581]  [00:11:32.741][info  ][EM] >>> [E:60955i S:7471 M:8703518 (Ack:3253365)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:00.638]  [00:11:32.799][info  ][EM] <<< [E:60955i S:7471 M:3253366 (Ack:8703518)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:00.640]  [00:11:32.799][info  ][EM] ??1 [E:60955i S:7471 M:3253366] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:01.476]  [00:11:33.636][info  ][EM] >>> [E:60955i S:7471 M:8703519 (Ack:3253366)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:01.506]  [00:11:33.666][info  ][EM] <<< [E:60955i S:7471 M:3253367 (Ack:8703519)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:01.507]  [00:11:33.666][info  ][EM] ??1 [E:60955i S:7471 M:3253367] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:02.268]  [00:11:34.427][info  ][EM] >>> [E:60955i S:7471 M:8703520 (Ack:3253367)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:02.297]  [00:11:34.458][info  ][EM] <<< [E:60955i S:7471 M:3253368 (Ack:8703520)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:02.299]  [00:11:34.458][info  ][EM] ??1 [E:60955i S:7471 M:3253368] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:03.136]  [00:11:35.297][info  ][EM] >>> [E:60955i S:7471 M:8703521 (Ack:3253368)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:03.166]  [00:11:35.327][info  ][EM] <<< [E:60955i S:7471 M:3253369 (Ack:8703521)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:03.168]  [00:11:35.328][info  ][EM] ??1 [E:60955i S:7471 M:3253369] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5734ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:03.924]  [00:11:36.084][info  ][EM] >>> [E:60955i S:7471 M:8703522 (Ack:3253369)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:03.989]  [00:11:36.149][info  ][EM] <<< [E:60955i S:7471 M:3253370 (Ack:8703522)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:03.991]  [00:11:36.150][info  ][EM] ??1 [E:60955i S:7471 M:3253370] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:04.786]  [00:11:36.946][info  ][EM] >>> [E:60955i S:7471 M:8703523 (Ack:3253370)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:04.815]  [00:11:36.975][info  ][EM] <<< [E:60955i S:7471 M:3253371 (Ack:8703523)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:04.816]  [00:11:36.976][info  ][EM] ??1 [E:60955i S:7471 M:3253371] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:05.556]  [00:11:37.716][info  ][EM] >>> [E:60955i S:7471 M:8703524 (Ack:3253371)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:05.586]  [00:11:37.746][info  ][EM] <<< [E:60955i S:7471 M:3253372 (Ack:8703524)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:05.587]  [00:11:37.747][info  ][EM] ??1 [E:60955i S:7471 M:3253372] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:06.331]  [00:11:38.491][info  ][EM] >>> [E:60955i S:7471 M:8703525 (Ack:3253372)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:06.360]  [00:11:38.521][info  ][EM] <<< [E:60955i S:7471 M:3253373 (Ack:8703525)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:06.361]  [00:11:38.521][info  ][EM] ??1 [E:60955i S:7471 M:3253373] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:07.202]  [00:11:39.362][info  ][EM] >>> [E:60955i S:7471 M:8703526 (Ack:3253373)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:07.257]  [00:11:39.417][info  ][EM] <<< [E:60955i S:7471 M:3253374 (Ack:8703526)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:07.259]  [00:11:39.417][info  ][EM] ??1 [E:60955i S:7471 M:3253374] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5454ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:08.270]  [00:11:40.430][info  ][EM] >>> [E:60955i S:7471 M:8703527 (Ack:3253374)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:08.300]  [00:11:40.459][info  ][EM] <<< [E:60955i S:7471 M:3253375 (Ack:8703527)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:08.301]  [00:11:40.460][info  ][EM] ??1 [E:60955i S:7471 M:3253375] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5489ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:09.054]  [00:11:41.214][info  ][EM] >>> [E:60955i S:7471 M:8703528 (Ack:3253375)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:09.084]  [00:11:41.244][info  ][EM] <<< [E:60955i S:7471 M:3253376 (Ack:8703528)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:09.085]  [00:11:41.245][info  ][EM] ??1 [E:60955i S:7471 M:3253376] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5671ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:09.868]  [00:11:42.029][info  ][EM] >>> [E:60955i S:7471 M:8703529 (Ack:3253376)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:09.898]  [00:11:42.058][info  ][EM] <<< [E:60955i S:7471 M:3253377 (Ack:8703529)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:09.900]  [00:11:42.059][info  ][EM] ??1 [E:60955i S:7471 M:3253377] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:10.747]  [00:11:42.908][info  ][EM] >>> [E:60955i S:7471 M:8703530 (Ack:3253377)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:10.813]  [00:11:42.973][info  ][EM] <<< [E:60955i S:7471 M:3253378 (Ack:8703530)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:10.814]  [00:11:42.974][info  ][EM] ??1 [E:60955i S:7471 M:3253378] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:11.515]  [00:11:43.676][info  ][EM] >>> [E:60955i S:7471 M:8703531 (Ack:3253378)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:11.546]  [00:11:43.706][info  ][EM] <<< [E:60955i S:7471 M:3253379 (Ack:8703531)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:11.547]  [00:11:43.707][info  ][EM] ??1 [E:60955i S:7471 M:3253379] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:12.294]  [00:11:44.454][info  ][EM] >>> [E:60955i S:7471 M:8703532 (Ack:3253379)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:12.323]  [00:11:44.483][info  ][EM] <<< [E:60955i S:7471 M:3253380 (Ack:8703532)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:12.324]  [00:11:44.484][info  ][EM] ??1 [E:60955i S:7471 M:3253380] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:13.060]  [00:11:45.220][info  ][EM] >>> [E:60955i S:7471 M:8703533 (Ack:3253380)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:13.090]  [00:11:45.250][info  ][EM] <<< [E:60955i S:7471 M:3253381 (Ack:8703533)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:13.092]  [00:11:45.250][info  ][EM] ??1 [E:60955i S:7471 M:3253381] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:13.834]  [00:11:45.995][info  ][EM] >>> [E:60955i S:7471 M:8703534 (Ack:3253381)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:13.892]  [00:11:46.052][info  ][EM] <<< [E:60955i S:7471 M:3253382 (Ack:8703534)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:13.894]  [00:11:46.053][info  ][EM] ??1 [E:60955i S:7471 M:3253382] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:14.605]  [00:11:46.765][info  ][EM] >>> [E:60955i S:7471 M:8703535 (Ack:3253382)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:14.635]  [00:11:46.794][info  ][EM] <<< [E:60955i S:7471 M:3253383 (Ack:8703535)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:14.636]  [00:11:46.795][info  ][EM] ??1 [E:60955i S:7471 M:3253383] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5615ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:15.386]  [00:11:47.545][info  ][EM] >>> [E:60955i S:7471 M:8703536 (Ack:3253383)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:15.416]  [00:11:47.576][info  ][EM] <<< [E:60955i S:7471 M:3253384 (Ack:8703536)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:15.417]  [00:11:47.576][info  ][EM] ??1 [E:60955i S:7471 M:3253384] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:16.148]  [00:11:48.308][info  ][EM] >>> [E:60955i S:7471 M:8703537 (Ack:3253384)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:16.178]  [00:11:48.337][info  ][EM] <<< [E:60955i S:7471 M:3253385 (Ack:8703537)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:16.179]  [00:11:48.338][info  ][EM] ??1 [E:60955i S:7471 M:3253385] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:16.923]  [00:11:49.083][info  ][EM] >>> [E:60955i S:7471 M:8703538 (Ack:3253385)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:16.988]  [00:11:49.148][info  ][EM] <<< [E:60955i S:7471 M:3253386 (Ack:8703538)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:16.990]  [00:11:49.149][info  ][EM] ??1 [E:60955i S:7471 M:3253386] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:17.707]  [00:11:49.868][info  ][EM] >>> [E:60955i S:7471 M:8703539 (Ack:3253386)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:17.736]  [00:11:49.897][info  ][EM] <<< [E:60955i S:7471 M:3253387 (Ack:8703539)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:17.738]  [00:11:49.898][info  ][EM] ??1 [E:60955i S:7471 M:3253387] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:18.459]  [00:11:50.620][info  ][EM] >>> [E:60955i S:7471 M:8703540 (Ack:3253387)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:18.488]  [00:11:50.649][info  ][EM] <<< [E:60955i S:7471 M:3253388 (Ack:8703540)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:18.490]  [00:11:50.650][info  ][EM] ??1 [E:60955i S:7471 M:3253388] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:19.244]  [00:11:51.405][info  ][EM] >>> [E:60955i S:7471 M:8703541 (Ack:3253388)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:19.274]  [00:11:51.434][info  ][EM] <<< [E:60955i S:7471 M:3253389 (Ack:8703541)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:19.275]  [00:11:51.435][info  ][EM] ??1 [E:60955i S:7471 M:3253389] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:20.115]  [00:11:52.275][info  ][EM] >>> [E:60955i S:7471 M:8703542 (Ack:3253389)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:20.171]  [00:11:52.332][info  ][EM] <<< [E:60955i S:7471 M:3253390 (Ack:8703542)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:20.172]  [00:11:52.333][info  ][EM] ??1 [E:60955i S:7471 M:3253390] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:20.898]  [00:11:53.059][info  ][EM] >>> [E:60955i S:7471 M:8703543 (Ack:3253390)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:20.928]  [00:11:53.088][info  ][EM] <<< [E:60955i S:7471 M:3253391 (Ack:8703543)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:20.930]  [00:11:53.089][info  ][EM] ??1 [E:60955i S:7471 M:3253391] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:21.671]  [00:11:53.832][info  ][EM] >>> [E:60955i S:7471 M:8703544 (Ack:3253391)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:21.700]  [00:11:53.861][info  ][EM] <<< [E:60955i S:7471 M:3253392 (Ack:8703544)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:21.702]  [00:11:53.862][info  ][EM] ??1 [E:60955i S:7471 M:3253392] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:22.429]  [00:11:54.589][info  ][EM] >>> [E:60955i S:7471 M:8703545 (Ack:3253392)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:22.459]  [00:11:54.620][info  ][EM] <<< [E:60955i S:7471 M:3253393 (Ack:8703545)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:22.461]  [00:11:54.621][info  ][EM] ??1 [E:60955i S:7471 M:3253393] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5538ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:23.203]  [00:11:55.363][info  ][EM] >>> [E:60955i S:7471 M:8703546 (Ack:3253393)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:23.268]  [00:11:55.428][info  ][EM] <<< [E:60955i S:7471 M:3253394 (Ack:8703546)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:23.269]  [00:11:55.428][info  ][EM] ??1 [E:60955i S:7471 M:3253394] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:23.997]  [00:11:56.158][info  ][EM] >>> [E:60955i S:7471 M:8703547 (Ack:3253394)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:24.027]  [00:11:56.188][info  ][EM] <<< [E:60955i S:7471 M:3253395 (Ack:8703547)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:24.029]  [00:11:56.188][info  ][EM] ??1 [E:60955i S:7471 M:3253395] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:24.768]  [00:11:56.929][info  ][EM] >>> [E:60955i S:7471 M:8703548 (Ack:3253395)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:24.799]  [00:11:56.958][info  ][EM] <<< [E:60955i S:7471 M:3253396 (Ack:8703548)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:24.800]  [00:11:56.959][info  ][EM] ??1 [E:60955i S:7471 M:3253396] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:25.652]  [00:11:57.812][info  ][EM] >>> [E:60955i S:7471 M:8703549 (Ack:3253396)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:25.682]  [00:11:57.842][info  ][EM] <<< [E:60955i S:7471 M:3253397 (Ack:8703549)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:25.683]  [00:11:57.842][info  ][EM] ??1 [E:60955i S:7471 M:3253397] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:26.506]  [00:11:58.667][info  ][EM] >>> [E:60955i S:7471 M:8703550 (Ack:3253397)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:26.564]  [00:11:58.724][info  ][EM] <<< [E:60955i S:7471 M:3253398 (Ack:8703550)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:26.565]  [00:11:58.725][info  ][EM] ??1 [E:60955i S:7471 M:3253398] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:27.292]  [00:11:59.453][info  ][EM] >>> [E:60955i S:7471 M:8703551 (Ack:3253398)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:27.322]  [00:11:59.482][info  ][EM] <<< [E:60955i S:7471 M:3253399 (Ack:8703551)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:27.323]  [00:11:59.483][info  ][EM] ??1 [E:60955i S:7471 M:3253399] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:28.075]  [00:12:00.235][info  ][EM] >>> [E:60955i S:7471 M:8703552 (Ack:3253399)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:28.104]  [00:12:00.265][info  ][EM] <<< [E:60955i S:7471 M:3253400 (Ack:8703552)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:28.107]  [00:12:00.266][info  ][EM] ??1 [E:60955i S:7471 M:3253400] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:28.948]  [00:12:01.109][info  ][EM] >>> [E:60955i S:7471 M:8703553 (Ack:3253400)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:28.979]  [00:12:01.139][info  ][EM] <<< [E:60955i S:7471 M:3253401 (Ack:8703553)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:28.980]  [00:12:01.139][info  ][EM] ??1 [E:60955i S:7471 M:3253401] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:29.708]  [00:12:01.869][info  ][EM] >>> [E:60955i S:7471 M:8703554 (Ack:3253401)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:29.774]  [00:12:01.934][info  ][EM] <<< [E:60955i S:7471 M:3253402 (Ack:8703554)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:29.775]  [00:12:01.935][info  ][EM] ??1 [E:60955i S:7471 M:3253402] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:30.474]  [00:12:02.634][info  ][EM] >>> [E:60955i S:7471 M:8703555 (Ack:3253402)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:30.504]  [00:12:02.664][info  ][EM] <<< [E:60955i S:7471 M:3253403 (Ack:8703555)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:30.505]  [00:12:02.665][info  ][EM] ??1 [E:60955i S:7471 M:3253403] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5559ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:31.556]  [00:12:03.716][info  ][EM] >>> [E:60955i S:7471 M:8703556 (Ack:3253403)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:31.586]  [00:12:03.747][info  ][EM] <<< [E:60955i S:7471 M:3253404 (Ack:8703556)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:31.588]  [00:12:03.748][info  ][EM] ??1 [E:60955i S:7471 M:3253404] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:32.433]  [00:12:04.594][info  ][EM] >>> [E:60955i S:7471 M:8703557 (Ack:3253404)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:32.464]  [00:12:04.624][info  ][EM] <<< [E:60955i S:7471 M:3253405 (Ack:8703557)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:32.465]  [00:12:04.625][info  ][EM] ??1 [E:60955i S:7471 M:3253405] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5428ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:33.303]  [00:12:05.464][info  ][EM] >>> [E:60955i S:7471 M:8703558 (Ack:3253405)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:33.360]  [00:12:05.521][info  ][EM] <<< [E:60955i S:7471 M:3253406 (Ack:8703558)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:33.361]  [00:12:05.522][info  ][EM] ??1 [E:60955i S:7471 M:3253406] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:34.186]  [00:12:06.347][info  ][EM] >>> [E:60955i S:7471 M:8703559 (Ack:3253406)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:34.216]  [00:12:06.376][info  ][EM] <<< [E:60955i S:7471 M:3253407 (Ack:8703559)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:34.217]  [00:12:06.377][info  ][EM] ??1 [E:60955i S:7471 M:3253407] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:35.376]  [00:12:07.538][info  ][EM] >>> [E:60955i S:7471 M:8703560 (Ack:3253407)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:35.406]  [00:12:07.567][info  ][EM] <<< [E:60955i S:7471 M:3253408 (Ack:8703560)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:35.408]  [00:12:07.568][info  ][EM] ??1 [E:60955i S:7471 M:3253408] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:39.255]  [00:12:11.416][info  ][EM] >>> [E:60955i S:7471 M:8703561 (Ack:3253408)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:39.284]  [00:12:11.445][info  ][EM] <<< [E:60955i S:7471 M:3253409 (Ack:8703561)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:39.286]  [00:12:11.446][info  ][EM] ??1 [E:60955i S:7471 M:3253409] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:40.278]  [00:12:12.438][info  ][EM] >>> [E:60955i S:7471 M:8703562 (Ack:3253409)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:40.346]  [00:12:12.507][info  ][EM] <<< [E:60955i S:7471 M:3253410 (Ack:8703562)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:40.348]  [00:12:12.508][info  ][EM] ??1 [E:60955i S:7471 M:3253410] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5261ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:41.147]  [00:12:13.307][info  ][EM] >>> [E:60955i S:7471 M:8703563 (Ack:3253410)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:41.176]  [00:12:13.336][info  ][EM] <<< [E:60955i S:7471 M:3253411 (Ack:8703563)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:41.177]  [00:12:13.337][info  ][EM] ??1 [E:60955i S:7471 M:3253411] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:41.919]  [00:12:14.080][info  ][EM] >>> [E:60955i S:7471 M:8703564 (Ack:3253411)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:41.949]  [00:12:14.110][info  ][EM] <<< [E:60955i S:7471 M:3253412 (Ack:8703564)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:41.951]  [00:12:14.110][info  ][EM] ??1 [E:60955i S:7471 M:3253412] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5536ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:42.710]  [00:12:14.871][info  ][EM] >>> [E:60955i S:7471 M:8703565 (Ack:3253412)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:42.740]  [00:12:14.901][info  ][EM] <<< [E:60955i S:7471 M:3253413 (Ack:8703565)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:42.741]  [00:12:14.901][info  ][EM] ??1 [E:60955i S:7471 M:3253413] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:43.725]  [00:12:15.886][info  ][EM] >>> [E:60955i S:7471 M:8703566 (Ack:3253413)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:43.787]  [00:12:15.948][info  ][EM] <<< [E:60955i S:7471 M:3253414 (Ack:8703566)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:43.789]  [00:12:15.949][info  ][EM] ??1 [E:60955i S:7471 M:3253414] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:44.491]  [00:12:16.652][info  ][EM] >>> [E:60955i S:7471 M:8703567 (Ack:3253414)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:44.521]  [00:12:16.681][info  ][EM] <<< [E:60955i S:7471 M:3253415 (Ack:8703567)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:44.522]  [00:12:16.682][info  ][EM] ??1 [E:60955i S:7471 M:3253415] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:45.528]  [00:12:17.689][info  ][EM] >>> [E:60955i S:7471 M:8703568 (Ack:3253415)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:45.559]  [00:12:17.719][info  ][EM] <<< [E:60955i S:7471 M:3253416 (Ack:8703568)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:45.560]  [00:12:17.719][info  ][EM] ??1 [E:60955i S:7471 M:3253416] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:46.404]  [00:12:18.565][info  ][EM] >>> [E:60955i S:7471 M:8703569 (Ack:3253416)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:46.434]  [00:12:18.595][info  ][EM] <<< [E:60955i S:7471 M:3253417 (Ack:8703569)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:46.436]  [00:12:18.595][info  ][EM] ??1 [E:60955i S:7471 M:3253417] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5263ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:47.379]  [00:12:19.541][info  ][EM] >>> [E:60955i S:7471 M:8703570 (Ack:3253417)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:47.449]  [00:12:19.609][info  ][EM] <<< [E:60955i S:7471 M:3253418 (Ack:8703570)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:47.450]  [00:12:19.610][info  ][EM] ??1 [E:60955i S:7471 M:3253418] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:48.251]  [00:12:20.412][info  ][EM] >>> [E:60955i S:7471 M:8703571 (Ack:3253418)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:48.281]  [00:12:20.442][info  ][EM] <<< [E:60955i S:7471 M:3253419 (Ack:8703571)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:48.282]  [00:12:20.443][info  ][EM] ??1 [E:60955i S:7471 M:3253419] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:49.338]  [00:12:21.500][info  ][EM] >>> [E:60955i S:7471 M:8703572 (Ack:3253419)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:49.368]  [00:12:21.529][info  ][EM] <<< [E:60955i S:7471 M:3253420 (Ack:8703572)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:49.369]  [00:12:21.530][info  ][EM] ??1 [E:60955i S:7471 M:3253420] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:50.106]  [00:12:22.267][info  ][EM] >>> [E:60955i S:7471 M:8703573 (Ack:3253420)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:50.136]  [00:12:22.296][info  ][EM] <<< [E:60955i S:7471 M:3253421 (Ack:8703573)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:50.137]  [00:12:22.297][info  ][EM] ??1 [E:60955i S:7471 M:3253421] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:50.969]  [00:12:23.128][info  ][EM] >>> [E:60955i S:7471 M:8703574 (Ack:3253421)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:51.029]  [00:12:23.189][info  ][EM] <<< [E:60955i S:7471 M:3253422 (Ack:8703574)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:51.030]  [00:12:23.190][info  ][EM] ??1 [E:60955i S:7471 M:3253422] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:51.738]  [00:12:23.899][info  ][EM] >>> [E:60955i S:7471 M:8703575 (Ack:3253422)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:51.768]  [00:12:23.929][info  ][EM] <<< [E:60955i S:7471 M:3253423 (Ack:8703575)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:51.769]  [00:12:23.930][info  ][EM] ??1 [E:60955i S:7471 M:3253423] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:52.937]  [00:12:25.098][info  ][EM] >>> [E:60955i S:7471 M:8703576 (Ack:3253423)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:52.967]  [00:12:25.127][info  ][EM] <<< [E:60955i S:7471 M:3253424 (Ack:8703576)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:52.969]  [00:12:25.128][info  ][EM] ??1 [E:60955i S:7471 M:3253424] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:54.040]  [00:12:26.201][info  ][EM] >>> [E:60955i S:7471 M:8703577 (Ack:3253424)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:54.071]  [00:12:26.231][info  ][EM] <<< [E:60955i S:7471 M:3253425 (Ack:8703577)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:54.072]  [00:12:26.232][info  ][EM] ??1 [E:60955i S:7471 M:3253425] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:54.806]  [00:12:26.967][info  ][EM] >>> [E:60955i S:7471 M:8703578 (Ack:3253425)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:54.872]  [00:12:27.033][info  ][EM] <<< [E:60955i S:7471 M:3253426 (Ack:8703578)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:54.873]  [00:12:27.034][info  ][EM] ??1 [E:60955i S:7471 M:3253426] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:56.114]  [00:12:28.275][info  ][EM] >>> [E:60955i S:7471 M:8703579 (Ack:3253426)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:56.143]  [00:12:28.304][info  ][EM] <<< [E:60955i S:7471 M:3253427 (Ack:8703579)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:56.146]  [00:12:28.305][info  ][EM] ??1 [E:60955i S:7471 M:3253427] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:56.988]  [00:12:29.149][info  ][EM] >>> [E:60955i S:7471 M:8703580 (Ack:3253427)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:57.017]  [00:12:29.178][info  ][EM] <<< [E:60955i S:7471 M:3253428 (Ack:8703580)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:57.020]  [00:12:29.179][info  ][EM] ??1 [E:60955i S:7471 M:3253428] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:57.754]  [00:12:29.916][info  ][EM] >>> [E:60955i S:7471 M:8703581 (Ack:3253428)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:57.784]  [00:12:29.945][info  ][EM] <<< [E:60955i S:7471 M:3253429 (Ack:8703581)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:57.785]  [00:12:29.946][info  ][EM] ??1 [E:60955i S:7471 M:3253429] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:58.781]  [00:12:30.941][info  ][EM] >>> [E:60955i S:7471 M:8703582 (Ack:3253429)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:58.837]  [00:12:30.999][info  ][EM] <<< [E:60955i S:7471 M:3253430 (Ack:8703582)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:58.839]  [00:12:30.999][info  ][EM] ??1 [E:60955i S:7471 M:3253430] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[16:28:59.553]  [00:12:31.713][info  ][EM] >>> [E:60955i S:7471 M:8703583 (Ack:3253430)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:28:59.583]  [00:12:31.744][info  ][EM] <<< [E:60955i S:7471 M:3253431 (Ack:8703583)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:28:59.584]  [00:12:31.744][info  ][EM] ??1 [E:60955i S:7471 M:3253431] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:00.358]  [00:12:32.520][info  ][EM] >>> [E:60955i S:7471 M:8703584 (Ack:3253431)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:00.389]  [00:12:32.549][info  ][EM] <<< [E:60955i S:7471 M:3253432 (Ack:8703584)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:00.390]  [00:12:32.550][info  ][EM] ??1 [E:60955i S:7471 M:3253432] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:01.141]  [00:12:33.302][info  ][EM] >>> [E:60955i S:7471 M:8703585 (Ack:3253432)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:01.171]  [00:12:33.333][info  ][EM] <<< [E:60955i S:7471 M:3253433 (Ack:8703585)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:01.173]  [00:12:33.333][info  ][EM] ??1 [E:60955i S:7471 M:3253433] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:01.944]  [00:12:34.106][info  ][EM] >>> [E:60955i S:7471 M:8703586 (Ack:3253433)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:02.010]  [00:12:34.171][info  ][EM] <<< [E:60955i S:7471 M:3253434 (Ack:8703586)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:02.011]  [00:12:34.171][info  ][EM] ??1 [E:60955i S:7471 M:3253434] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:02.717]  [00:12:34.877][info  ][EM] >>> [E:60955i S:7471 M:8703587 (Ack:3253434)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:02.746]  [00:12:34.908][info  ][EM] <<< [E:60955i S:7471 M:3253435 (Ack:8703587)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:02.747]  [00:12:34.908][info  ][EM] ??1 [E:60955i S:7471 M:3253435] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:03.808]  [00:12:35.968][info  ][EM] >>> [E:60955i S:7471 M:8703588 (Ack:3253435)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:03.837]  [00:12:35.999][info  ][EM] <<< [E:60955i S:7471 M:3253436 (Ack:8703588)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:03.839]  [00:12:36.000][info  ][EM] ??1 [E:60955i S:7471 M:3253436] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5351ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:04.601]  [00:12:36.762][info  ][EM] >>> [E:60955i S:7471 M:8703589 (Ack:3253436)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:04.631]  [00:12:36.792][info  ][EM] <<< [E:60955i S:7471 M:3253437 (Ack:8703589)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:04.632]  [00:12:36.792][info  ][EM] ??1 [E:60955i S:7471 M:3253437] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:05.397]  [00:12:37.557][info  ][EM] >>> [E:60955i S:7471 M:8703590 (Ack:3253437)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:05.453]  [00:12:37.614][info  ][EM] <<< [E:60955i S:7471 M:3253438 (Ack:8703590)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:05.454]  [00:12:37.615][info  ][EM] ??1 [E:60955i S:7471 M:3253438] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:06.271]  [00:12:38.432][info  ][EM] >>> [E:60955i S:7471 M:8703591 (Ack:3253438)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:06.301]  [00:12:38.461][info  ][EM] <<< [E:60955i S:7471 M:3253439 (Ack:8703591)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:06.302]  [00:12:38.462][info  ][EM] ??1 [E:60955i S:7471 M:3253439] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:07.051]  [00:12:39.211][info  ][EM] >>> [E:60955i S:7471 M:8703592 (Ack:3253439)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:07.080]  [00:12:39.242][info  ][EM] <<< [E:60955i S:7471 M:3253440 (Ack:8703592)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:07.082]  [00:12:39.242][info  ][EM] ??1 [E:60955i S:7471 M:3253440] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5622ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:07.819]  [00:12:39.980][info  ][EM] >>> [E:60955i S:7471 M:8703593 (Ack:3253440)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:07.849]  [00:12:40.010][info  ][EM] <<< [E:60955i S:7471 M:3253441 (Ack:8703593)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:07.850]  [00:12:40.010][info  ][EM] ??1 [E:60955i S:7471 M:3253441] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:08.591]  [00:12:40.751][info  ][EM] >>> [E:60955i S:7471 M:8703594 (Ack:3253441)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:08.657]  [00:12:40.818][info  ][EM] <<< [E:60955i S:7471 M:3253442 (Ack:8703594)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:08.658]  [00:12:40.818][info  ][EM] ??1 [E:60955i S:7471 M:3253442] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:09.364]  [00:12:41.525][info  ][EM] >>> [E:60955i S:7471 M:8703595 (Ack:3253442)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:09.394]  [00:12:41.555][info  ][EM] <<< [E:60955i S:7471 M:3253443 (Ack:8703595)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:09.396]  [00:12:41.556][info  ][EM] ??1 [E:60955i S:7471 M:3253443] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:10.128]  [00:12:42.289][info  ][EM] >>> [E:60955i S:7471 M:8703596 (Ack:3253443)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:10.157]  [00:12:42.318][info  ][EM] <<< [E:60955i S:7471 M:3253444 (Ack:8703596)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:10.158]  [00:12:42.319][info  ][EM] ??1 [E:60955i S:7471 M:3253444] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:11.099]  [00:12:43.259][info  ][EM] >>> [E:60955i S:7471 M:8703597 (Ack:3253444)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:11.128]  [00:12:43.290][info  ][EM] <<< [E:60955i S:7471 M:3253445 (Ack:8703597)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:11.129]  [00:12:43.291][info  ][EM] ??1 [E:60955i S:7471 M:3253445] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:11.876]  [00:12:44.037][info  ][EM] >>> [E:60955i S:7471 M:8703598 (Ack:3253445)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:11.933]  [00:12:44.093][info  ][EM] <<< [E:60955i S:7471 M:3253446 (Ack:8703598)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:11.934]  [00:12:44.094][info  ][EM] ??1 [E:60955i S:7471 M:3253446] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:12.633]  [00:12:44.793][info  ][EM] >>> [E:60955i S:7471 M:8703599 (Ack:3253446)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:12.663]  [00:12:44.824][info  ][EM] <<< [E:60955i S:7471 M:3253447 (Ack:8703599)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:12.664]  [00:12:44.824][info  ][EM] ??1 [E:60955i S:7471 M:3253447] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5375ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:13.413]  [00:12:45.575][info  ][EM] >>> [E:60955i S:7471 M:8703600 (Ack:3253447)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:13.444]  [00:12:45.604][info  ][EM] <<< [E:60955i S:7471 M:3253448 (Ack:8703600)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:13.445]  [00:12:45.605][info  ][EM] ??1 [E:60955i S:7471 M:3253448] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5248ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:14.510]  [00:12:46.671][info  ][EM] >>> [E:60955i S:7471 M:8703601 (Ack:3253448)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:14.540]  [00:12:46.702][info  ][EM] <<< [E:60955i S:7471 M:3253449 (Ack:8703601)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:14.541]  [00:12:46.702][info  ][EM] ??1 [E:60955i S:7471 M:3253449] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5622ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:15.270]  [00:12:47.431][info  ][EM] >>> [E:60955i S:7471 M:8703602 (Ack:3253449)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:15.335]  [00:12:47.497][info  ][EM] <<< [E:60955i S:7471 M:3253450 (Ack:8703602)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:15.338]  [00:12:47.498][info  ][EM] ??1 [E:60955i S:7471 M:3253450] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5213ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:16.194]  [00:12:48.355][info  ][EM] >>> [E:60955i S:7471 M:8703603 (Ack:3253450)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:16.224]  [00:12:48.385][info  ][EM] <<< [E:60955i S:7471 M:3253451 (Ack:8703603)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:16.225]  [00:12:48.386][info  ][EM] ??1 [E:60955i S:7471 M:3253451] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:16.959]  [00:12:49.120][info  ][EM] >>> [E:60955i S:7471 M:8703604 (Ack:3253451)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:16.988]  [00:12:49.149][info  ][EM] <<< [E:60955i S:7471 M:3253452 (Ack:8703604)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:16.989]  [00:12:49.150][info  ][EM] ??1 [E:60955i S:7471 M:3253452] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:17.942]  [00:12:50.103][info  ][EM] >>> [E:60955i S:7471 M:8703605 (Ack:3253452)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:17.971]  [00:12:50.132][info  ][EM] <<< [E:60955i S:7471 M:3253453 (Ack:8703605)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:17.973]  [00:12:50.133][info  ][EM] ??1 [E:60955i S:7471 M:3253453] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:18.731]  [00:12:50.892][info  ][EM] >>> [E:60955i S:7471 M:8703606 (Ack:3253453)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:18.788]  [00:12:50.949][info  ][EM] <<< [E:60955i S:7471 M:3253454 (Ack:8703606)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:18.789]  [00:12:50.950][info  ][EM] ??1 [E:60955i S:7471 M:3253454] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:19.493]  [00:12:51.655][info  ][EM] >>> [E:60955i S:7471 M:8703607 (Ack:3253454)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:19.523]  [00:12:51.685][info  ][EM] <<< [E:60955i S:7471 M:3253455 (Ack:8703607)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:19.524]  [00:12:51.685][info  ][EM] ??1 [E:60955i S:7471 M:3253455] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5508ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:20.292]  [00:12:52.454][info  ][EM] >>> [E:60955i S:7471 M:8703608 (Ack:3253455)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:20.323]  [00:12:52.483][info  ][EM] <<< [E:60955i S:7471 M:3253456 (Ack:8703608)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:20.324]  [00:12:52.484][info  ][EM] ??1 [E:60955i S:7471 M:3253456] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5368ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:21.073]  [00:12:53.234][info  ][EM] >>> [E:60955i S:7471 M:8703609 (Ack:3253456)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:21.103]  [00:12:53.264][info  ][EM] <<< [E:60955i S:7471 M:3253457 (Ack:8703609)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:21.104]  [00:12:53.264][info  ][EM] ??1 [E:60955i S:7471 M:3253457] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:21.946]  [00:12:54.107][info  ][EM] >>> [E:60955i S:7471 M:8703610 (Ack:3253457)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:22.011]  [00:12:54.172][info  ][EM] <<< [E:60955i S:7471 M:3253458 (Ack:8703610)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:22.013]  [00:12:54.173][info  ][EM] ??1 [E:60955i S:7471 M:3253458] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:22.717]  [00:12:54.877][info  ][EM] >>> [E:60955i S:7471 M:8703611 (Ack:3253458)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:22.746]  [00:12:54.908][info  ][EM] <<< [E:60955i S:7471 M:3253459 (Ack:8703611)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:22.747]  [00:12:54.909][info  ][EM] ??1 [E:60955i S:7471 M:3253459] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:23.506]  [00:12:55.666][info  ][EM] >>> [E:60955i S:7471 M:8703612 (Ack:3253459)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:23.536]  [00:12:55.697][info  ][EM] <<< [E:60955i S:7471 M:3253460 (Ack:8703612)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:23.537]  [00:12:55.697][info  ][EM] ??1 [E:60955i S:7471 M:3253460] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:24.381]  [00:12:56.542][info  ][EM] >>> [E:60955i S:7471 M:8703613 (Ack:3253460)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:24.411]  [00:12:56.573][info  ][EM] <<< [E:60955i S:7471 M:3253461 (Ack:8703613)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:24.413]  [00:12:56.574][info  ][EM] ??1 [E:60955i S:7471 M:3253461] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:25.147]  [00:12:57.308][info  ][EM] >>> [E:60955i S:7471 M:8703614 (Ack:3253461)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:25.203]  [00:12:57.365][info  ][EM] <<< [E:60955i S:7471 M:3253462 (Ack:8703614)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:25.205]  [00:12:57.366][info  ][EM] ??1 [E:60955i S:7471 M:3253462] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:25.934]  [00:12:58.095][info  ][EM] >>> [E:60955i S:7471 M:8703615 (Ack:3253462)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:25.964]  [00:12:58.125][info  ][EM] <<< [E:60955i S:7471 M:3253463 (Ack:8703615)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:25.965]  [00:12:58.125][info  ][EM] ??1 [E:60955i S:7471 M:3253463] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5450ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:26.703]  [00:12:58.864][info  ][EM] >>> [E:60955i S:7471 M:8703616 (Ack:3253463)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:26.732]  [00:12:58.894][info  ][EM] <<< [E:60955i S:7471 M:3253464 (Ack:8703616)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:26.734]  [00:12:58.894][info  ][EM] ??1 [E:60955i S:7471 M:3253464] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5691ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:27.584]  [00:12:59.745][info  ][EM] >>> [E:60955i S:7471 M:8703617 (Ack:3253464)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:27.613]  [00:12:59.775][info  ][EM] <<< [E:60955i S:7471 M:3253465 (Ack:8703617)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:27.614]  [00:12:59.776][info  ][EM] ??1 [E:60955i S:7471 M:3253465] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:28.451]  [00:13:00.613][info  ][EM] >>> [E:60955i S:7471 M:8703618 (Ack:3253465)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:28.517]  [00:13:00.678][info  ][EM] <<< [E:60955i S:7471 M:3253466 (Ack:8703618)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:28.519]  [00:13:00.679][info  ][EM] ??1 [E:60955i S:7471 M:3253466] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:29.216]  [00:13:01.377][info  ][EM] >>> [E:60955i S:7471 M:8703619 (Ack:3253466)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:29.246]  [00:13:01.407][info  ][EM] <<< [E:60955i S:7471 M:3253467 (Ack:8703619)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:29.247]  [00:13:01.408][info  ][EM] ??1 [E:60955i S:7471 M:3253467] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5407ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:29.994]  [00:13:02.155][info  ][EM] >>> [E:60955i S:7471 M:8703620 (Ack:3253467)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:30.022]  [00:13:02.184][info  ][EM] <<< [E:60955i S:7471 M:3253468 (Ack:8703620)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:30.024]  [00:13:02.185][info  ][EM] ??1 [E:60955i S:7471 M:3253468] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:30.959]  [00:13:03.120][info  ][EM] >>> [E:60955i S:7471 M:8703621 (Ack:3253468)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:30.988]  [00:13:03.150][info  ][EM] <<< [E:60955i S:7471 M:3253469 (Ack:8703621)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:30.989]  [00:13:03.150][info  ][EM] ??1 [E:60955i S:7471 M:3253469] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:31.740]  [00:13:03.902][info  ][EM] >>> [E:60955i S:7471 M:8703622 (Ack:3253469)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:31.797]  [00:13:03.958][info  ][EM] <<< [E:60955i S:7471 M:3253470 (Ack:8703622)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:31.799]  [00:13:03.958][info  ][EM] ??1 [E:60955i S:7471 M:3253470] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:32.638]  [00:13:04.798][info  ][EM] >>> [E:60955i S:7471 M:8703623 (Ack:3253470)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:32.667]  [00:13:04.829][info  ][EM] <<< [E:60955i S:7471 M:3253471 (Ack:8703623)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:32.669]  [00:13:04.830][info  ][EM] ??1 [E:60955i S:7471 M:3253471] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:33.406]  [00:13:05.567][info  ][EM] >>> [E:60955i S:7471 M:8703624 (Ack:3253471)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:33.436]  [00:13:05.596][info  ][EM] <<< [E:60955i S:7471 M:3253472 (Ack:8703624)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:33.437]  [00:13:05.597][info  ][EM] ??1 [E:60955i S:7471 M:3253472] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:34.289]  [00:13:06.451][info  ][EM] >>> [E:60955i S:7471 M:8703625 (Ack:3253472)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:34.318]  [00:13:06.480][info  ][EM] <<< [E:60955i S:7471 M:3253473 (Ack:8703625)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:34.319]  [00:13:06.481][info  ][EM] ??1 [E:60955i S:7471 M:3253473] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:35.064]  [00:13:07.225][info  ][EM] >>> [E:60955i S:7471 M:8703626 (Ack:3253473)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:35.130]  [00:13:07.291][info  ][EM] <<< [E:60955i S:7471 M:3253474 (Ack:8703626)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:35.131]  [00:13:07.291][info  ][EM] ??1 [E:60955i S:7471 M:3253474] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:35.848]  [00:13:08.010][info  ][EM] >>> [E:60955i S:7471 M:8703627 (Ack:3253474)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:35.878]  [00:13:08.040][info  ][EM] <<< [E:60955i S:7471 M:3253475 (Ack:8703627)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:35.880]  [00:13:08.041][info  ][EM] ??1 [E:60955i S:7471 M:3253475] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:36.720]  [00:13:08.881][info  ][EM] >>> [E:60955i S:7471 M:8703628 (Ack:3253475)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:36.751]  [00:13:08.912][info  ][EM] <<< [E:60955i S:7471 M:3253476 (Ack:8703628)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:36.752]  [00:13:08.913][info  ][EM] ??1 [E:60955i S:7471 M:3253476] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:37.506]  [00:13:09.668][info  ][EM] >>> [E:60955i S:7471 M:8703629 (Ack:3253476)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:37.536]  [00:13:09.698][info  ][EM] <<< [E:60955i S:7471 M:3253477 (Ack:8703629)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:37.538]  [00:13:09.699][info  ][EM] ??1 [E:60955i S:7471 M:3253477] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:38.582]  [00:13:10.744][info  ][EM] >>> [E:60955i S:7471 M:8703630 (Ack:3253477)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:38.638]  [00:13:10.800][info  ][EM] <<< [E:60955i S:7471 M:3253478 (Ack:8703630)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:38.640]  [00:13:10.801][info  ][EM] ??1 [E:60955i S:7471 M:3253478] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:39.347]  [00:13:11.509][info  ][EM] >>> [E:60955i S:7471 M:8703631 (Ack:3253478)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:39.377]  [00:13:11.539][info  ][EM] <<< [E:60955i S:7471 M:3253479 (Ack:8703631)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:39.378]  [00:13:11.540][info  ][EM] ??1 [E:60955i S:7471 M:3253479] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5368ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:40.236]  [00:13:12.398][info  ][EM] >>> [E:60955i S:7471 M:8703632 (Ack:3253479)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:40.266]  [00:13:12.427][info  ][EM] <<< [E:60955i S:7471 M:3253480 (Ack:8703632)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:40.267]  [00:13:12.428][info  ][EM] ??1 [E:60955i S:7471 M:3253480] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:41.039]  [00:13:13.200][info  ][EM] >>> [E:60955i S:7471 M:8703633 (Ack:3253480)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:41.068]  [00:13:13.230][info  ][EM] <<< [E:60955i S:7471 M:3253481 (Ack:8703633)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:41.070]  [00:13:13.231][info  ][EM] ??1 [E:60955i S:7471 M:3253481] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:41.963]  [00:13:14.125][info  ][EM] >>> [E:60955i S:7471 M:8703634 (Ack:3253481)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:42.029]  [00:13:14.190][info  ][EM] <<< [E:60955i S:7471 M:3253482 (Ack:8703634)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:42.030]  [00:13:14.191][info  ][EM] ??1 [E:60955i S:7471 M:3253482] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5540ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:42.830]  [00:13:14.992][info  ][EM] >>> [E:60955i S:7471 M:8703635 (Ack:3253482)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:42.860]  [00:13:15.022][info  ][EM] <<< [E:60955i S:7471 M:3253483 (Ack:8703635)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:42.862]  [00:13:15.022][info  ][EM] ??1 [E:60955i S:7471 M:3253483] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:43.591]  [00:13:15.753][info  ][EM] >>> [E:60955i S:7471 M:8703636 (Ack:3253483)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:43.622]  [00:13:15.783][info  ][EM] <<< [E:60955i S:7471 M:3253484 (Ack:8703636)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:43.623]  [00:13:15.784][info  ][EM] ??1 [E:60955i S:7471 M:3253484] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:44.456]  [00:13:16.618][info  ][EM] >>> [E:60955i S:7471 M:8703637 (Ack:3253484)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:44.485]  [00:13:16.647][info  ][EM] <<< [E:60955i S:7471 M:3253485 (Ack:8703637)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:44.487]  [00:13:16.648][info  ][EM] ??1 [E:60955i S:7471 M:3253485] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:45.247]  [00:13:17.409][info  ][EM] >>> [E:60955i S:7471 M:8703638 (Ack:3253485)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:45.306]  [00:13:17.467][info  ][EM] <<< [E:60955i S:7471 M:3253486 (Ack:8703638)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:45.307]  [00:13:17.468][info  ][EM] ??1 [E:60955i S:7471 M:3253486] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:46.017]  [00:13:18.178][info  ][EM] >>> [E:60955i S:7471 M:8703639 (Ack:3253486)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:46.047]  [00:13:18.208][info  ][EM] <<< [E:60955i S:7471 M:3253487 (Ack:8703639)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:46.048]  [00:13:18.208][info  ][EM] ??1 [E:60955i S:7471 M:3253487] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:46.785]  [00:13:18.947][info  ][EM] >>> [E:60955i S:7471 M:8703640 (Ack:3253487)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:46.815]  [00:13:18.976][info  ][EM] <<< [E:60955i S:7471 M:3253488 (Ack:8703640)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:46.816]  [00:13:18.977][info  ][EM] ??1 [E:60955i S:7471 M:3253488] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:47.559]  [00:13:19.720][info  ][EM] >>> [E:60955i S:7471 M:8703641 (Ack:3253488)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:47.589]  [00:13:19.750][info  ][EM] <<< [E:60955i S:7471 M:3253489 (Ack:8703641)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:47.590]  [00:13:19.751][info  ][EM] ??1 [E:60955i S:7471 M:3253489] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:48.346]  [00:13:20.507][info  ][EM] >>> [E:60955i S:7471 M:8703642 (Ack:3253489)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:48.414]  [00:13:20.575][info  ][EM] <<< [E:60955i S:7471 M:3253490 (Ack:8703642)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:48.415]  [00:13:20.576][info  ][EM] ??1 [E:60955i S:7471 M:3253490] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:49.123]  [00:13:21.285][info  ][EM] >>> [E:60955i S:7471 M:8703643 (Ack:3253490)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:49.153]  [00:13:21.315][info  ][EM] <<< [E:60955i S:7471 M:3253491 (Ack:8703643)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:49.155]  [00:13:21.316][info  ][EM] ??1 [E:60955i S:7471 M:3253491] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:49.893]  [00:13:22.054][info  ][EM] >>> [E:60955i S:7471 M:8703644 (Ack:3253491)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:49.922]  [00:13:22.084][info  ][EM] <<< [E:60955i S:7471 M:3253492 (Ack:8703644)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:49.924]  [00:13:22.084][info  ][EM] ??1 [E:60955i S:7471 M:3253492] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:50.687]  [00:13:22.848][info  ][EM] >>> [E:60955i S:7471 M:8703645 (Ack:3253492)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:50.717]  [00:13:22.878][info  ][EM] <<< [E:60955i S:7471 M:3253493 (Ack:8703645)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:50.718]  [00:13:22.879][info  ][EM] ??1 [E:60955i S:7471 M:3253493] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:51.462]  [00:13:23.625][info  ][EM] >>> [E:60955i S:7471 M:8703646 (Ack:3253493)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:51.520]  [00:13:23.681][info  ][EM] <<< [E:60955i S:7471 M:3253494 (Ack:8703646)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:51.522]  [00:13:23.682][info  ][EM] ??1 [E:60955i S:7471 M:3253494] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:52.235]  [00:13:24.396][info  ][EM] >>> [E:60955i S:7471 M:8703647 (Ack:3253494)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:52.264]  [00:13:24.426][info  ][EM] <<< [E:60955i S:7471 M:3253495 (Ack:8703647)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:52.266]  [00:13:24.427][info  ][EM] ??1 [E:60955i S:7471 M:3253495] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:53.105]  [00:13:25.266][info  ][EM] >>> [E:60955i S:7471 M:8703648 (Ack:3253495)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:53.135]  [00:13:25.296][info  ][EM] <<< [E:60955i S:7471 M:3253496 (Ack:8703648)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:53.136]  [00:13:25.297][info  ][EM] ??1 [E:60955i S:7471 M:3253496] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:53.883]  [00:13:26.044][info  ][EM] >>> [E:60955i S:7471 M:8703649 (Ack:3253496)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:53.912]  [00:13:26.074][info  ][EM] <<< [E:60955i S:7471 M:3253497 (Ack:8703649)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:53.914]  [00:13:26.075][info  ][EM] ??1 [E:60955i S:7471 M:3253497] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:54.659]  [00:13:26.821][info  ][EM] >>> [E:60955i S:7471 M:8703650 (Ack:3253497)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:54.725]  [00:13:26.886][info  ][EM] <<< [E:60955i S:7471 M:3253498 (Ack:8703650)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:54.726]  [00:13:26.887][info  ][EM] ??1 [E:60955i S:7471 M:3253498] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:55.643]  [00:13:27.805][info  ][EM] >>> [E:60955i S:7471 M:8703651 (Ack:3253498)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:55.673]  [00:13:27.834][info  ][EM] <<< [E:60955i S:7471 M:3253499 (Ack:8703651)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:55.674]  [00:13:27.835][info  ][EM] ??1 [E:60955i S:7471 M:3253499] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:56.427]  [00:13:28.589][info  ][EM] >>> [E:60955i S:7471 M:8703652 (Ack:3253499)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:56.458]  [00:13:28.619][info  ][EM] <<< [E:60955i S:7471 M:3253500 (Ack:8703652)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:56.459]  [00:13:28.620][info  ][EM] ??1 [E:60955i S:7471 M:3253500] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:57.312]  [00:13:29.473][info  ][EM] >>> [E:60955i S:7471 M:8703653 (Ack:3253500)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:57.341]  [00:13:29.503][info  ][EM] <<< [E:60955i S:7471 M:3253501 (Ack:8703653)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:57.343]  [00:13:29.504][info  ][EM] ??1 [E:60955i S:7471 M:3253501] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:58.097]  [00:13:30.258][info  ][EM] >>> [E:60955i S:7471 M:8703654 (Ack:3253501)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:58.152]  [00:13:30.315][info  ][EM] <<< [E:60955i S:7471 M:3253502 (Ack:8703654)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:58.155]  [00:13:30.315][info  ][EM] ??1 [E:60955i S:7471 M:3253502] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:58.867]  [00:13:31.029][info  ][EM] >>> [E:60955i S:7471 M:8703655 (Ack:3253502)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:58.897]  [00:13:31.058][info  ][EM] <<< [E:60955i S:7471 M:3253503 (Ack:8703655)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:58.898]  [00:13:31.059][info  ][EM] ??1 [E:60955i S:7471 M:3253503] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[16:29:59.631]  [00:13:31.791][info  ][EM] >>> [E:60955i S:7471 M:8703656 (Ack:3253503)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:29:59.660]  [00:13:31.822][info  ][EM] <<< [E:60955i S:7471 M:3253504 (Ack:8703656)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:29:59.661]  [00:13:31.822][info  ][EM] ??1 [E:60955i S:7471 M:3253504] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:00.403]  [00:13:32.565][info  ][EM] >>> [E:60955i S:7471 M:8703657 (Ack:3253504)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:00.433]  [00:13:32.594][info  ][EM] <<< [E:60955i S:7471 M:3253505 (Ack:8703657)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:00.434]  [00:13:32.595][info  ][EM] ??1 [E:60955i S:7471 M:3253505] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:01.177]  [00:13:33.338][info  ][EM] >>> [E:60955i S:7471 M:8703658 (Ack:3253505)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:01.241]  [00:13:33.403][info  ][EM] <<< [E:60955i S:7471 M:3253506 (Ack:8703658)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:01.243]  [00:13:33.404][info  ][EM] ??1 [E:60955i S:7471 M:3253506] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:01.965]  [00:13:34.126][info  ][EM] >>> [E:60955i S:7471 M:8703659 (Ack:3253506)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:01.995]  [00:13:34.157][info  ][EM] <<< [E:60955i S:7471 M:3253507 (Ack:8703659)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:01.996]  [00:13:34.157][info  ][EM] ??1 [E:60955i S:7471 M:3253507] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5544ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:02.740]  [00:13:34.901][info  ][EM] >>> [E:60955i S:7471 M:8703660 (Ack:3253507)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:02.769]  [00:13:34.931][info  ][EM] <<< [E:60955i S:7471 M:3253508 (Ack:8703660)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:02.770]  [00:13:34.931][info  ][EM] ??1 [E:60955i S:7471 M:3253508] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:03.509]  [00:13:35.670][info  ][EM] >>> [E:60955i S:7471 M:8703661 (Ack:3253508)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:03.539]  [00:13:35.701][info  ][EM] <<< [E:60955i S:7471 M:3253509 (Ack:8703661)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:03.540]  [00:13:35.701][info  ][EM] ??1 [E:60955i S:7471 M:3253509] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:04.282]  [00:13:36.443][info  ][EM] >>> [E:60955i S:7471 M:8703662 (Ack:3253509)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:04.341]  [00:13:36.502][info  ][EM] <<< [E:60955i S:7471 M:3253510 (Ack:8703662)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:04.342]  [00:13:36.503][info  ][EM] ??1 [E:60955i S:7471 M:3253510] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:05.296]  [00:13:37.458][info  ][EM] >>> [E:60955i S:7471 M:8703663 (Ack:3253510)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:05.326]  [00:13:37.488][info  ][EM] <<< [E:60955i S:7471 M:3253511 (Ack:8703663)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:05.328]  [00:13:37.489][info  ][EM] ??1 [E:60955i S:7471 M:3253511] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5454ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:06.375]  [00:13:38.537][info  ][EM] >>> [E:60955i S:7471 M:8703664 (Ack:3253511)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:06.405]  [00:13:38.566][info  ][EM] <<< [E:60955i S:7471 M:3253512 (Ack:8703664)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:06.406]  [00:13:38.567][info  ][EM] ??1 [E:60955i S:7471 M:3253512] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5583ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:07.139]  [00:13:39.300][info  ][EM] >>> [E:60955i S:7471 M:8703665 (Ack:3253512)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:07.169]  [00:13:39.331][info  ][EM] <<< [E:60955i S:7471 M:3253513 (Ack:8703665)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:07.170]  [00:13:39.331][info  ][EM] ??1 [E:60955i S:7471 M:3253513] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5203ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:08.135]  [00:13:40.297][info  ][EM] >>> [E:60955i S:7471 M:8703666 (Ack:3253513)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:08.200]  [00:13:40.362][info  ][EM] <<< [E:60955i S:7471 M:3253514 (Ack:8703666)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:08.201]  [00:13:40.363][info  ][EM] ??1 [E:60955i S:7471 M:3253514] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:08.896]  [00:13:41.058][info  ][EM] >>> [E:60955i S:7471 M:8703667 (Ack:3253514)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:08.926]  [00:13:41.087][info  ][EM] <<< [E:60955i S:7471 M:3253515 (Ack:8703667)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:08.927]  [00:13:41.088][info  ][EM] ??1 [E:60955i S:7471 M:3253515] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:09.663]  [00:13:41.825][info  ][EM] >>> [E:60955i S:7471 M:8703668 (Ack:3253515)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:09.692]  [00:13:41.854][info  ][EM] <<< [E:60955i S:7471 M:3253516 (Ack:8703668)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:09.694]  [00:13:41.855][info  ][EM] ??1 [E:60955i S:7471 M:3253516] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:10.440]  [00:13:42.602][info  ][EM] >>> [E:60955i S:7471 M:8703669 (Ack:3253516)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:10.471]  [00:13:42.632][info  ][EM] <<< [E:60955i S:7471 M:3253517 (Ack:8703669)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:10.472]  [00:13:42.633][info  ][EM] ??1 [E:60955i S:7471 M:3253517] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:11.228]  [00:13:43.389][info  ][EM] >>> [E:60955i S:7471 M:8703670 (Ack:3253517)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:11.285]  [00:13:43.447][info  ][EM] <<< [E:60955i S:7471 M:3253518 (Ack:8703670)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:11.286]  [00:13:43.448][info  ][EM] ??1 [E:60955i S:7471 M:3253518] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5213ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:11.999]  [00:13:44.161][info  ][EM] >>> [E:60955i S:7471 M:8703671 (Ack:3253518)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:12.029]  [00:13:44.190][info  ][EM] <<< [E:60955i S:7471 M:3253519 (Ack:8703671)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:12.030]  [00:13:44.191][info  ][EM] ??1 [E:60955i S:7471 M:3253519] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:12.788]  [00:13:44.951][info  ][EM] >>> [E:60955i S:7471 M:8703672 (Ack:3253519)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:12.818]  [00:13:44.980][info  ][EM] <<< [E:60955i S:7471 M:3253520 (Ack:8703672)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:12.820]  [00:13:44.981][info  ][EM] ??1 [E:60955i S:7471 M:3253520] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:13.570]  [00:13:45.732][info  ][EM] >>> [E:60955i S:7471 M:8703673 (Ack:3253520)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:13.600]  [00:13:45.761][info  ][EM] <<< [E:60955i S:7471 M:3253521 (Ack:8703673)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:13.601]  [00:13:45.762][info  ][EM] ??1 [E:60955i S:7471 M:3253521] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:14.345]  [00:13:46.507][info  ][EM] >>> [E:60955i S:7471 M:8703674 (Ack:3253521)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:14.412]  [00:13:46.573][info  ][EM] <<< [E:60955i S:7471 M:3253522 (Ack:8703674)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:14.413]  [00:13:46.574][info  ][EM] ??1 [E:60955i S:7471 M:3253522] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:15.123]  [00:13:47.285][info  ][EM] >>> [E:60955i S:7471 M:8703675 (Ack:3253522)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:15.152]  [00:13:47.315][info  ][EM] <<< [E:60955i S:7471 M:3253523 (Ack:8703675)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:15.155]  [00:13:47.315][info  ][EM] ??1 [E:60955i S:7471 M:3253523] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:15.903]  [00:13:48.065][info  ][EM] >>> [E:60955i S:7471 M:8703676 (Ack:3253523)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:15.933]  [00:13:48.094][info  ][EM] <<< [E:60955i S:7471 M:3253524 (Ack:8703676)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:15.934]  [00:13:48.095][info  ][EM] ??1 [E:60955i S:7471 M:3253524] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:16.691]  [00:13:48.853][info  ][EM] >>> [E:60955i S:7471 M:8703677 (Ack:3253524)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:16.721]  [00:13:48.883][info  ][EM] <<< [E:60955i S:7471 M:3253525 (Ack:8703677)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:16.722]  [00:13:48.883][info  ][EM] ??1 [E:60955i S:7471 M:3253525] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:17.458]  [00:13:49.620][info  ][EM] >>> [E:60955i S:7471 M:8703678 (Ack:3253525)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:17.517]  [00:13:49.678][info  ][EM] <<< [E:60955i S:7471 M:3253526 (Ack:8703678)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:17.518]  [00:13:49.679][info  ][EM] ??1 [E:60955i S:7471 M:3253526] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:18.341]  [00:13:50.503][info  ][EM] >>> [E:60955i S:7471 M:8703679 (Ack:3253526)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:18.371]  [00:13:50.534][info  ][EM] <<< [E:60955i S:7471 M:3253527 (Ack:8703679)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:18.373]  [00:13:50.534][info  ][EM] ??1 [E:60955i S:7471 M:3253527] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:19.229]  [00:13:51.391][info  ][EM] >>> [E:60955i S:7471 M:8703680 (Ack:3253527)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:19.259]  [00:13:51.421][info  ][EM] <<< [E:60955i S:7471 M:3253528 (Ack:8703680)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:19.260]  [00:13:51.421][info  ][EM] ??1 [E:60955i S:7471 M:3253528] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:20.060]  [00:13:52.222][info  ][EM] >>> [E:60955i S:7471 M:8703681 (Ack:3253528)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:20.090]  [00:13:52.252][info  ][EM] <<< [E:60955i S:7471 M:3253529 (Ack:8703681)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:20.092]  [00:13:52.252][info  ][EM] ??1 [E:60955i S:7471 M:3253529] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5682ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:20.827]  [00:13:52.989][info  ][EM] >>> [E:60955i S:7471 M:8703682 (Ack:3253529)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:20.894]  [00:13:53.055][info  ][EM] <<< [E:60955i S:7471 M:3253530 (Ack:8703682)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:20.895]  [00:13:53.055][info  ][EM] ??1 [E:60955i S:7471 M:3253530] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:21.596]  [00:13:53.758][info  ][EM] >>> [E:60955i S:7471 M:8703683 (Ack:3253530)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:21.626]  [00:13:53.788][info  ][EM] <<< [E:60955i S:7471 M:3253531 (Ack:8703683)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:21.627]  [00:13:53.789][info  ][EM] ??1 [E:60955i S:7471 M:3253531] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:22.467]  [00:13:54.628][info  ][EM] >>> [E:60955i S:7471 M:8703684 (Ack:3253531)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:22.496]  [00:13:54.659][info  ][EM] <<< [E:60955i S:7471 M:3253532 (Ack:8703684)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:22.498]  [00:13:54.660][info  ][EM] ??1 [E:60955i S:7471 M:3253532] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:23.246]  [00:13:55.408][info  ][EM] >>> [E:60955i S:7471 M:8703685 (Ack:3253532)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:23.275]  [00:13:55.438][info  ][EM] <<< [E:60955i S:7471 M:3253533 (Ack:8703685)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:23.277]  [00:13:55.439][info  ][EM] ??1 [E:60955i S:7471 M:3253533] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:24.030]  [00:13:56.191][info  ][EM] >>> [E:60955i S:7471 M:8703686 (Ack:3253533)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:24.086]  [00:13:56.249][info  ][EM] <<< [E:60955i S:7471 M:3253534 (Ack:8703686)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:24.088]  [00:13:56.250][info  ][EM] ??1 [E:60955i S:7471 M:3253534] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:24.911]  [00:13:57.073][info  ][EM] >>> [E:60955i S:7471 M:8703687 (Ack:3253534)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:24.940]  [00:13:57.102][info  ][EM] <<< [E:60955i S:7471 M:3253535 (Ack:8703687)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:24.941]  [00:13:57.103][info  ][EM] ??1 [E:60955i S:7471 M:3253535] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5390ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:25.681]  [00:13:57.843][info  ][EM] >>> [E:60955i S:7471 M:8703688 (Ack:3253535)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:25.711]  [00:13:57.873][info  ][EM] <<< [E:60955i S:7471 M:3253536 (Ack:8703688)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:25.712]  [00:13:57.874][info  ][EM] ??1 [E:60955i S:7471 M:3253536] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:26.451]  [00:13:58.614][info  ][EM] >>> [E:60955i S:7471 M:8703689 (Ack:3253536)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:26.481]  [00:13:58.643][info  ][EM] <<< [E:60955i S:7471 M:3253537 (Ack:8703689)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:26.483]  [00:13:58.644][info  ][EM] ??1 [E:60955i S:7471 M:3253537] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5701ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:27.335]  [00:13:59.499][info  ][EM] >>> [E:60955i S:7471 M:8703690 (Ack:3253537)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:27.402]  [00:13:59.564][info  ][EM] <<< [E:60955i S:7471 M:3253538 (Ack:8703690)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:27.403]  [00:13:59.565][info  ][EM] ??1 [E:60955i S:7471 M:3253538] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5478ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:28.206]  [00:14:00.369][info  ][EM] >>> [E:60955i S:7471 M:8703691 (Ack:3253538)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:28.236]  [00:14:00.399][info  ][EM] <<< [E:60955i S:7471 M:3253539 (Ack:8703691)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:28.238]  [00:14:00.399][info  ][EM] ??1 [E:60955i S:7471 M:3253539] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:28.996]  [00:14:01.159][info  ][EM] >>> [E:60955i S:7471 M:8703692 (Ack:3253539)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:29.026]  [00:14:01.188][info  ][EM] <<< [E:60955i S:7471 M:3253540 (Ack:8703692)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:29.027]  [00:14:01.189][info  ][EM] ??1 [E:60955i S:7471 M:3253540] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:29.894]  [00:14:02.056][info  ][EM] >>> [E:60955i S:7471 M:8703693 (Ack:3253540)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:29.924]  [00:14:02.086][info  ][EM] <<< [E:60955i S:7471 M:3253541 (Ack:8703693)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:29.925]  [00:14:02.087][info  ][EM] ??1 [E:60955i S:7471 M:3253541] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:30.668]  [00:14:02.831][info  ][EM] >>> [E:60955i S:7471 M:8703694 (Ack:3253541)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:30.724]  [00:14:02.886][info  ][EM] <<< [E:60955i S:7471 M:3253542 (Ack:8703694)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:30.726]  [00:14:02.887][info  ][EM] ??1 [E:60955i S:7471 M:3253542] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:31.431]  [00:14:03.593][info  ][EM] >>> [E:60955i S:7471 M:8703695 (Ack:3253542)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:31.460]  [00:14:03.624][info  ][EM] <<< [E:60955i S:7471 M:3253543 (Ack:8703695)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:31.463]  [00:14:03.624][info  ][EM] ??1 [E:60955i S:7471 M:3253543] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:32.320]  [00:14:04.482][info  ][EM] >>> [E:60955i S:7471 M:8703696 (Ack:3253543)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:32.350]  [00:14:04.512][info  ][EM] <<< [E:60955i S:7471 M:3253544 (Ack:8703696)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:32.352]  [00:14:04.513][info  ][EM] ??1 [E:60955i S:7471 M:3253544] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:33.084]  [00:14:05.247][info  ][EM] >>> [E:60955i S:7471 M:8703697 (Ack:3253544)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:33.114]  [00:14:05.276][info  ][EM] <<< [E:60955i S:7471 M:3253545 (Ack:8703697)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:33.115]  [00:14:05.277][info  ][EM] ??1 [E:60955i S:7471 M:3253545] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:34.068]  [00:14:06.230][info  ][EM] >>> [E:60955i S:7471 M:8703698 (Ack:3253545)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:34.134]  [00:14:06.296][info  ][EM] <<< [E:60955i S:7471 M:3253546 (Ack:8703698)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:34.136]  [00:14:06.297][info  ][EM] ??1 [E:60955i S:7471 M:3253546] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:34.848]  [00:14:07.011][info  ][EM] >>> [E:60955i S:7471 M:8703699 (Ack:3253546)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:34.879]  [00:14:07.041][info  ][EM] <<< [E:60955i S:7471 M:3253547 (Ack:8703699)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:34.880]  [00:14:07.041][info  ][EM] ??1 [E:60955i S:7471 M:3253547] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:35.824]  [00:14:07.986][info  ][EM] >>> [E:60955i S:7471 M:8703700 (Ack:3253547)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:35.854]  [00:14:08.016][info  ][EM] <<< [E:60955i S:7471 M:3253548 (Ack:8703700)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:35.856]  [00:14:08.017][info  ][EM] ??1 [E:60955i S:7471 M:3253548] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:36.801]  [00:14:08.963][info  ][EM] >>> [E:60955i S:7471 M:8703701 (Ack:3253548)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:36.831]  [00:14:08.994][info  ][EM] <<< [E:60955i S:7471 M:3253549 (Ack:8703701)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:36.832]  [00:14:08.994][info  ][EM] ??1 [E:60955i S:7471 M:3253549] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:37.983]  [00:14:10.145][info  ][EM] >>> [E:60955i S:7471 M:8703702 (Ack:3253549)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:38.041]  [00:14:10.203][info  ][EM] <<< [E:60955i S:7471 M:3253550 (Ack:8703702)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:38.042]  [00:14:10.204][info  ][EM] ??1 [E:60955i S:7471 M:3253550] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:38.974]  [00:14:11.137][info  ][EM] >>> [E:60955i S:7471 M:8703703 (Ack:3253550)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:39.005]  [00:14:11.166][info  ][EM] <<< [E:60955i S:7471 M:3253551 (Ack:8703703)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:39.006]  [00:14:11.167][info  ][EM] ??1 [E:60955i S:7471 M:3253551] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:40.029]  [00:14:12.191][info  ][EM] >>> [E:60955i S:7471 M:8703704 (Ack:3253551)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:40.058]  [00:14:12.221][info  ][EM] <<< [E:60955i S:7471 M:3253552 (Ack:8703704)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:40.060]  [00:14:12.221][info  ][EM] ??1 [E:60955i S:7471 M:3253552] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:40.793]  [00:14:12.956][info  ][EM] >>> [E:60955i S:7471 M:8703705 (Ack:3253552)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:40.823]  [00:14:12.986][info  ][EM] <<< [E:60955i S:7471 M:3253553 (Ack:8703705)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:40.824]  [00:14:12.986][info  ][EM] ??1 [E:60955i S:7471 M:3253553] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:41.671]  [00:14:13.833][info  ][EM] >>> [E:60955i S:7471 M:8703706 (Ack:3253553)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:41.738]  [00:14:13.899][info  ][EM] <<< [E:60955i S:7471 M:3253554 (Ack:8703706)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:41.739]  [00:14:13.900][info  ][EM] ??1 [E:60955i S:7471 M:3253554] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:42.543]  [00:14:14.705][info  ][EM] >>> [E:60955i S:7471 M:8703707 (Ack:3253554)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:42.573]  [00:14:14.735][info  ][EM] <<< [E:60955i S:7471 M:3253555 (Ack:8703707)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:42.574]  [00:14:14.735][info  ][EM] ??1 [E:60955i S:7471 M:3253555] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:43.314]  [00:14:15.476][info  ][EM] >>> [E:60955i S:7471 M:8703708 (Ack:3253555)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:43.344]  [00:14:15.506][info  ][EM] <<< [E:60955i S:7471 M:3253556 (Ack:8703708)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:43.345]  [00:14:15.507][info  ][EM] ??1 [E:60955i S:7471 M:3253556] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:44.195]  [00:14:16.356][info  ][EM] >>> [E:60955i S:7471 M:8703709 (Ack:3253556)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:44.224]  [00:14:16.386][info  ][EM] <<< [E:60955i S:7471 M:3253557 (Ack:8703709)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:44.226]  [00:14:16.386][info  ][EM] ??1 [E:60955i S:7471 M:3253557] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:45.278]  [00:14:17.440][info  ][EM] >>> [E:60955i S:7471 M:8703710 (Ack:3253557)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:45.335]  [00:14:17.498][info  ][EM] <<< [E:60955i S:7471 M:3253558 (Ack:8703710)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:45.337]  [00:14:17.499][info  ][EM] ??1 [E:60955i S:7471 M:3253558] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:46.053]  [00:14:18.214][info  ][EM] >>> [E:60955i S:7471 M:8703711 (Ack:3253558)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:46.083]  [00:14:18.245][info  ][EM] <<< [E:60955i S:7471 M:3253559 (Ack:8703711)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:46.084]  [00:14:18.245][info  ][EM] ??1 [E:60955i S:7471 M:3253559] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:47.061]  [00:14:19.224][info  ][EM] >>> [E:60955i S:7471 M:8703712 (Ack:3253559)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:47.091]  [00:14:19.253][info  ][EM] <<< [E:60955i S:7471 M:3253560 (Ack:8703712)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:47.092]  [00:14:19.254][info  ][EM] ??1 [E:60955i S:7471 M:3253560] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:47.831]  [00:14:19.994][info  ][EM] >>> [E:60955i S:7471 M:8703713 (Ack:3253560)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:47.861]  [00:14:20.023][info  ][EM] <<< [E:60955i S:7471 M:3253561 (Ack:8703713)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:47.862]  [00:14:20.024][info  ][EM] ??1 [E:60955i S:7471 M:3253561] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:48.608]  [00:14:20.770][info  ][EM] >>> [E:60955i S:7471 M:8703714 (Ack:3253561)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:48.675]  [00:14:20.837][info  ][EM] <<< [E:60955i S:7471 M:3253562 (Ack:8703714)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:48.677]  [00:14:20.837][info  ][EM] ??1 [E:60955i S:7471 M:3253562] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:49.382]  [00:14:21.543][info  ][EM] >>> [E:60955i S:7471 M:8703715 (Ack:3253562)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:49.411]  [00:14:21.574][info  ][EM] <<< [E:60955i S:7471 M:3253563 (Ack:8703715)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:49.412]  [00:14:21.574][info  ][EM] ??1 [E:60955i S:7471 M:3253563] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:50.162]  [00:14:22.325][info  ][EM] >>> [E:60955i S:7471 M:8703716 (Ack:3253563)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:50.193]  [00:14:22.354][info  ][EM] <<< [E:60955i S:7471 M:3253564 (Ack:8703716)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:50.194]  [00:14:22.355][info  ][EM] ??1 [E:60955i S:7471 M:3253564] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:50.939]  [00:14:23.101][info  ][EM] >>> [E:60955i S:7471 M:8703717 (Ack:3253564)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:50.968]  [00:14:23.130][info  ][EM] <<< [E:60955i S:7471 M:3253565 (Ack:8703717)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:50.970]  [00:14:23.131][info  ][EM] ??1 [E:60955i S:7471 M:3253565] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:51.722]  [00:14:23.884][info  ][EM] >>> [E:60955i S:7471 M:8703718 (Ack:3253565)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:51.781]  [00:14:23.943][info  ][EM] <<< [E:60955i S:7471 M:3253566 (Ack:8703718)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:51.782]  [00:14:23.944][info  ][EM] ??1 [E:60955i S:7471 M:3253566] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:52.489]  [00:14:24.651][info  ][EM] >>> [E:60955i S:7471 M:8703719 (Ack:3253566)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:52.518]  [00:14:24.681][info  ][EM] <<< [E:60955i S:7471 M:3253567 (Ack:8703719)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:52.520]  [00:14:24.681][info  ][EM] ??1 [E:60955i S:7471 M:3253567] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5564ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:53.278]  [00:14:25.440][info  ][EM] >>> [E:60955i S:7471 M:8703720 (Ack:3253567)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:53.307]  [00:14:25.470][info  ][EM] <<< [E:60955i S:7471 M:3253568 (Ack:8703720)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:53.309]  [00:14:25.471][info  ][EM] ??1 [E:60955i S:7471 M:3253568] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:54.249]  [00:14:26.412][info  ][EM] >>> [E:60955i S:7471 M:8703721 (Ack:3253568)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:54.279]  [00:14:26.441][info  ][EM] <<< [E:60955i S:7471 M:3253569 (Ack:8703721)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:54.280]  [00:14:26.442][info  ][EM] ??1 [E:60955i S:7471 M:3253569] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5357ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:55.009]  [00:14:27.171][info  ][EM] >>> [E:60955i S:7471 M:8703722 (Ack:3253569)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:55.079]  [00:14:27.242][info  ][EM] <<< [E:60955i S:7471 M:3253570 (Ack:8703722)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:55.081]  [00:14:27.242][info  ][EM] ??1 [E:60955i S:7471 M:3253570] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:55.779]  [00:14:27.941][info  ][EM] >>> [E:60955i S:7471 M:8703723 (Ack:3253570)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:55.808]  [00:14:27.971][info  ][EM] <<< [E:60955i S:7471 M:3253571 (Ack:8703723)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:55.811]  [00:14:27.972][info  ][EM] ??1 [E:60955i S:7471 M:3253571] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:56.564]  [00:14:28.726][info  ][EM] >>> [E:60955i S:7471 M:8703724 (Ack:3253571)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:56.594]  [00:14:28.755][info  ][EM] <<< [E:60955i S:7471 M:3253572 (Ack:8703724)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:56.595]  [00:14:28.756][info  ][EM] ??1 [E:60955i S:7471 M:3253572] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:57.339]  [00:14:29.501][info  ][EM] >>> [E:60955i S:7471 M:8703725 (Ack:3253572)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:57.369]  [00:14:29.532][info  ][EM] <<< [E:60955i S:7471 M:3253573 (Ack:8703725)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:57.371]  [00:14:29.532][info  ][EM] ??1 [E:60955i S:7471 M:3253573] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5368ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:58.123]  [00:14:30.285][info  ][EM] >>> [E:60955i S:7471 M:8703726 (Ack:3253573)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:58.179]  [00:14:30.341][info  ][EM] <<< [E:60955i S:7471 M:3253574 (Ack:8703726)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:58.181]  [00:14:30.342][info  ][EM] ??1 [E:60955i S:7471 M:3253574] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:58.992]  [00:14:31.154][info  ][EM] >>> [E:60955i S:7471 M:8703727 (Ack:3253574)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:59.021]  [00:14:31.183][info  ][EM] <<< [E:60955i S:7471 M:3253575 (Ack:8703727)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:59.023]  [00:14:31.184][info  ][EM] ??1 [E:60955i S:7471 M:3253575] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[16:30:59.769]  [00:14:31.932][info  ][EM] >>> [E:60955i S:7471 M:8703728 (Ack:3253575)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:30:59.799]  [00:14:31.961][info  ][EM] <<< [E:60955i S:7471 M:3253576 (Ack:8703728)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:30:59.801]  [00:14:31.962][info  ][EM] ??1 [E:60955i S:7471 M:3253576] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5473ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:00.770]  [00:14:32.932][info  ][EM] >>> [E:60955i S:7471 M:8703729 (Ack:3253576)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:00.800]  [00:14:32.961][info  ][EM] <<< [E:60955i S:7471 M:3253577 (Ack:8703729)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:00.801]  [00:14:32.962][info  ][EM] ??1 [E:60955i S:7471 M:3253577] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5658ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:01.753]  [00:14:33.916][info  ][EM] >>> [E:60955i S:7471 M:8703730 (Ack:3253577)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:01.821]  [00:14:33.983][info  ][EM] <<< [E:60955i S:7471 M:3253578 (Ack:8703730)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:01.822]  [00:14:33.983][info  ][EM] ??1 [E:60955i S:7471 M:3253578] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:02.752]  [00:14:34.914][info  ][EM] >>> [E:60955i S:7471 M:8703731 (Ack:3253578)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:02.781]  [00:14:34.943][info  ][EM] <<< [E:60955i S:7471 M:3253579 (Ack:8703731)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:02.783]  [00:14:34.944][info  ][EM] ??1 [E:60955i S:7471 M:3253579] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:03.521]  [00:14:35.683][info  ][EM] >>> [E:60955i S:7471 M:8703732 (Ack:3253579)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:03.551]  [00:14:35.713][info  ][EM] <<< [E:60955i S:7471 M:3253580 (Ack:8703732)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:03.552]  [00:14:35.713][info  ][EM] ??1 [E:60955i S:7471 M:3253580] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5716ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:04.296]  [00:14:36.458][info  ][EM] >>> [E:60955i S:7471 M:8703733 (Ack:3253580)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:04.326]  [00:14:36.488][info  ][EM] <<< [E:60955i S:7471 M:3253581 (Ack:8703733)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:04.328]  [00:14:36.489][info  ][EM] ??1 [E:60955i S:7471 M:3253581] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5398ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:05.066]  [00:14:37.228][info  ][EM] >>> [E:60955i S:7471 M:8703734 (Ack:3253581)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:05.124]  [00:14:37.287][info  ][EM] <<< [E:60955i S:7471 M:3253582 (Ack:8703734)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:05.125]  [00:14:37.287][info  ][EM] ??1 [E:60955i S:7471 M:3253582] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:05.836]  [00:14:37.999][info  ][EM] >>> [E:60955i S:7471 M:8703735 (Ack:3253582)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:05.867]  [00:14:38.029][info  ][EM] <<< [E:60955i S:7471 M:3253583 (Ack:8703735)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:05.868]  [00:14:38.029][info  ][EM] ??1 [E:60955i S:7471 M:3253583] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5716ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:06.615]  [00:14:38.778][info  ][EM] >>> [E:60955i S:7471 M:8703736 (Ack:3253583)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:06.646]  [00:14:38.807][info  ][EM] <<< [E:60955i S:7471 M:3253584 (Ack:8703736)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:06.647]  [00:14:38.808][info  ][EM] ??1 [E:60955i S:7471 M:3253584] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:07.392]  [00:14:39.554][info  ][EM] >>> [E:60955i S:7471 M:8703737 (Ack:3253584)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:07.422]  [00:14:39.583][info  ][EM] <<< [E:60955i S:7471 M:3253585 (Ack:8703737)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:07.423]  [00:14:39.584][info  ][EM] ??1 [E:60955i S:7471 M:3253585] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:08.149]  [00:14:40.311][info  ][EM] >>> [E:60955i S:7471 M:8703738 (Ack:3253585)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:08.212]  [00:14:40.375][info  ][EM] <<< [E:60955i S:7471 M:3253586 (Ack:8703738)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:08.213]  [00:14:40.375][info  ][EM] ??1 [E:60955i S:7471 M:3253586] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5394ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:08.932]  [00:14:41.093][info  ][EM] >>> [E:60955i S:7471 M:8703739 (Ack:3253586)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:08.962]  [00:14:41.124][info  ][EM] <<< [E:60955i S:7471 M:3253587 (Ack:8703739)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:08.963]  [00:14:41.124][info  ][EM] ??1 [E:60955i S:7471 M:3253587] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5572ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:09.696]  [00:14:41.858][info  ][EM] >>> [E:60955i S:7471 M:8703740 (Ack:3253587)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:09.726]  [00:14:41.888][info  ][EM] <<< [E:60955i S:7471 M:3253588 (Ack:8703740)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:09.727]  [00:14:41.888][info  ][EM] ??1 [E:60955i S:7471 M:3253588] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:10.458]  [00:14:42.620][info  ][EM] >>> [E:60955i S:7471 M:8703741 (Ack:3253588)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:10.488]  [00:14:42.650][info  ][EM] <<< [E:60955i S:7471 M:3253589 (Ack:8703741)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:10.489]  [00:14:42.651][info  ][EM] ??1 [E:60955i S:7471 M:3253589] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5749ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:11.344]  [00:14:43.506][info  ][EM] >>> [E:60955i S:7471 M:8703742 (Ack:3253589)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:11.401]  [00:14:43.564][info  ][EM] <<< [E:60955i S:7471 M:3253590 (Ack:8703742)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:11.403]  [00:14:43.565][info  ][EM] ??1 [E:60955i S:7471 M:3253590] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:12.134]  [00:14:44.296][info  ][EM] >>> [E:60955i S:7471 M:8703743 (Ack:3253590)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:12.164]  [00:14:44.327][info  ][EM] <<< [E:60955i S:7471 M:3253591 (Ack:8703743)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:12.165]  [00:14:44.327][info  ][EM] ??1 [E:60955i S:7471 M:3253591] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5458ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:12.897]  [00:14:45.059][info  ][EM] >>> [E:60955i S:7471 M:8703744 (Ack:3253591)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:12.926]  [00:14:45.088][info  ][EM] <<< [E:60955i S:7471 M:3253592 (Ack:8703744)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:12.927]  [00:14:45.089][info  ][EM] ??1 [E:60955i S:7471 M:3253592] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:13.776]  [00:14:45.938][info  ][EM] >>> [E:60955i S:7471 M:8703745 (Ack:3253592)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:13.806]  [00:14:45.968][info  ][EM] <<< [E:60955i S:7471 M:3253593 (Ack:8703745)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:13.808]  [00:14:45.968][info  ][EM] ??1 [E:60955i S:7471 M:3253593] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:14.654]  [00:14:46.817][info  ][EM] >>> [E:60955i S:7471 M:8703746 (Ack:3253593)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:14.720]  [00:14:46.882][info  ][EM] <<< [E:60955i S:7471 M:3253594 (Ack:8703746)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:14.721]  [00:14:46.882][info  ][EM] ??1 [E:60955i S:7471 M:3253594] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:15.417]  [00:14:47.580][info  ][EM] >>> [E:60955i S:7471 M:8703747 (Ack:3253594)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:15.447]  [00:14:47.609][info  ][EM] <<< [E:60955i S:7471 M:3253595 (Ack:8703747)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:15.449]  [00:14:47.610][info  ][EM] ??1 [E:60955i S:7471 M:3253595] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:16.175]  [00:14:48.337][info  ][EM] >>> [E:60955i S:7471 M:8703748 (Ack:3253595)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:16.205]  [00:14:48.367][info  ][EM] <<< [E:60955i S:7471 M:3253596 (Ack:8703748)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:16.206]  [00:14:48.368][info  ][EM] ??1 [E:60955i S:7471 M:3253596] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:16.940]  [00:14:49.102][info  ][EM] >>> [E:60955i S:7471 M:8703749 (Ack:3253596)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:16.970]  [00:14:49.132][info  ][EM] <<< [E:60955i S:7471 M:3253597 (Ack:8703749)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:16.972]  [00:14:49.132][info  ][EM] ??1 [E:60955i S:7471 M:3253597] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:17.695]  [00:14:49.857][info  ][EM] >>> [E:60955i S:7471 M:8703750 (Ack:3253597)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:17.751]  [00:14:49.914][info  ][EM] <<< [E:60955i S:7471 M:3253598 (Ack:8703750)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:17.753]  [00:14:49.915][info  ][EM] ??1 [E:60955i S:7471 M:3253598] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5357ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:18.572]  [00:14:50.734][info  ][EM] >>> [E:60955i S:7471 M:8703751 (Ack:3253598)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:18.601]  [00:14:50.763][info  ][EM] <<< [E:60955i S:7471 M:3253599 (Ack:8703751)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:18.603]  [00:14:50.764][info  ][EM] ??1 [E:60955i S:7471 M:3253599] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:19.349]  [00:14:51.511][info  ][EM] >>> [E:60955i S:7471 M:8703752 (Ack:3253599)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:19.379]  [00:14:51.541][info  ][EM] <<< [E:60955i S:7471 M:3253600 (Ack:8703752)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:19.380]  [00:14:51.541][info  ][EM] ??1 [E:60955i S:7471 M:3253600] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:20.111]  [00:14:52.273][info  ][EM] >>> [E:60955i S:7471 M:8703753 (Ack:3253600)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:20.140]  [00:14:52.302][info  ][EM] <<< [E:60955i S:7471 M:3253601 (Ack:8703753)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:20.142]  [00:14:52.303][info  ][EM] ??1 [E:60955i S:7471 M:3253601] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5252ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:21.083]  [00:14:53.246][info  ][EM] >>> [E:60955i S:7471 M:8703754 (Ack:3253601)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:21.150]  [00:14:53.313][info  ][EM] <<< [E:60955i S:7471 M:3253602 (Ack:8703754)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:21.152]  [00:14:53.314][info  ][EM] ??1 [E:60955i S:7471 M:3253602] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:21.850]  [00:14:54.012][info  ][EM] >>> [E:60955i S:7471 M:8703755 (Ack:3253602)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:21.880]  [00:14:54.042][info  ][EM] <<< [E:60955i S:7471 M:3253603 (Ack:8703755)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:21.881]  [00:14:54.043][info  ][EM] ??1 [E:60955i S:7471 M:3253603] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:22.630]  [00:14:54.792][info  ][EM] >>> [E:60955i S:7471 M:8703756 (Ack:3253603)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:22.660]  [00:14:54.823][info  ][EM] <<< [E:60955i S:7471 M:3253604 (Ack:8703756)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:22.661]  [00:14:54.823][info  ][EM] ??1 [E:60955i S:7471 M:3253604] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:23.397]  [00:14:55.559][info  ][EM] >>> [E:60955i S:7471 M:8703757 (Ack:3253604)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:23.427]  [00:14:55.589][info  ][EM] <<< [E:60955i S:7471 M:3253605 (Ack:8703757)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:23.428]  [00:14:55.589][info  ][EM] ??1 [E:60955i S:7471 M:3253605] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:24.183]  [00:14:56.346][info  ][EM] >>> [E:60955i S:7471 M:8703758 (Ack:3253605)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:24.241]  [00:14:56.403][info  ][EM] <<< [E:60955i S:7471 M:3253606 (Ack:8703758)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:24.242]  [00:14:56.404][info  ][EM] ??1 [E:60955i S:7471 M:3253606] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:24.947]  [00:14:57.109][info  ][EM] >>> [E:60955i S:7471 M:8703759 (Ack:3253606)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[16:31:24.976]  [00:14:57.138][info  ][EM] <<< [E:60955i S:7471 M:3253607 (Ack:8703759)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[16:31:24.978]  [00:14:57.139][info  ][EM] ??1 [E:60955i S:7471 M:3253607] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:25.639]  [00:14:57.801][info  ][EM] >>> [E:60955i S:7471 M:8703760 (Ack:3253607)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0002:12 (BDX:BlockEOF) (B:767)
[16:31:25.641]  [00:14:57.803][info  ][EM] <<< [E:60955i S:7471 M:3253608 (Ack:8703760)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0002:14 (BDX:BlockAckEOF) (B:38)
[16:31:25.643]  [00:14:57.804][info  ][EM] ??1 [E:60955i S:7471 M:3253608] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:25.645]  [00:14:57.808][info  ][DIS] Found an existing secure session to [1:0000000000000001]!
[16:31:25.649]  [00:14:57.810][info  ][EM] <<< [E:60956i S:7471 M:3253609] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:97)
[16:31:25.650]  [00:14:57.811][info  ][EM] ??1 [E:60956i S:7471 M:3253609] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[16:31:25.673]  [00:14:57.834][info  ][SWU] OTA image downloaded successfully
[16:31:26.146]  [00:14:58.308][info  ][EM] >>> [E:60956i S:7471 M:8703761 (Ack:3253609)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[16:31:26.148]  [00:14:58.309][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0003
[16:31:26.150]  [00:14:58.312][info  ][EM] <<< [E:60956i S:7471 M:3253610 (Ack:8703761)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:31:26.154]  [00:14:58.312][silabs ]mcu_dfu: upgrade triggered
[16:31:26.164]  [00:14:58.327][info  ][EM] >>> [E:60955i S:7471 M:8703762 (Ack:3253608)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:31:26.263]  [00:14:58.421][silabs ]mcu_dfu: Matter OTA upgrade triggered!
[16:31:26.263]  [00:14:58.423][silabs ]app_read_metadata: seek back, restarting verify...
[16:31:39.163]  [00:15:11.326][silabs ]app_read_metadata: 4400 iters, ret=513, copied=10
[16:31:39.163]  [00:15:11.326][silabs ]mcu_dfu: header OK, magic=0x55AA, size=45676, ver=3.0.0
[16:31:39.167]  [00:15:11.326][silabs ]mcu_dfu: version compare \E2\80\94 cur=3.0.0 new=3.0.0
[16:31:52.821]  [00:15:11.326][silabs ]mcu_dfu: MCU version up-to-date, directly applying Matter image...
[16:31:52.821]  [00:1\05> 
[16:33:01.610]  Missed Logs: 25
[16:33:01.610]  [00:00:00.064][info  ][DL] Starting scheduler
[16:33:01.610]  [00:00:00.064][info  ][DL] ==================================================
[16:33:01.611]  [00:00:00.065][info  ][DL]  starting
[16:33:01.611]  [00:00:00.065][info  ][DL] ==================================================
[16:33:01.612]  [00:00:00.065][info  ][DL] Init CHIP Stack
[16:33:01.612]  [00:00:00.066][info  ][DL] Provision mode disabled
[16:33:01.612]  [00:00:00.066][info  ][DL] Initializing OpenThread stack
[16:33:01.614]  [00:00:00.068][info  ][DL] OpenThread ifconfig up and thread start
[16:33:01.614]  [00:00:00.068][info  ][DL] OpenThread started: OK
[16:33:01.617]  [00:00:00.103][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[16:33:01.617]  [00:00:00.103][info  ][DL] RAIL version:, v3.0.3-b0
[16:33:01.619]  [00:00:00.105][info  ][SVR] Current Software Version String: 0.0.5
[16:33:01.619]  [00:00:00.105][info  ][SVR] Current Software Version: 5
[16:33:01.621]  [00:00:00.107][info  ][DL] Device Configuration:
[16:33:01.621]  [00:00:00.108][info  ][DL]   Serial Number: 36DF4B3B8F54A56D
[16:33:01.621]  [00:00:00.109][info  ][DL]   Vendor Id: 5232 (0x1470)
[16:33:01.624]  [00:00:00.111][info  ][DL]   Product Id: 65281 (0xFF01)
[16:33:01.624]  [00:00:00.111][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:33:01.626]  [00:00:00.113][info  ][DL]   Product Name: Window Covering
[16:33:01.626]  [00:00:00.114][info  ][DL]   Hardware Version: 1
[16:33:01.629]  [00:00:00.114][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[16:33:01.629]  [00:00:00.114][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 2485 (0x9B5)
[16:33:01.630]  [00:00:00.114][info  ][DL]   Manufacturing Date: 2026-06-08
[16:33:01.631]  [00:00:00.115][info  ][DL]   Device Type: 65535 (0xFFFF)
[16:33:01.631]  [00:00:00.115][info  ][SVR] SetupQRCode: [MT:K2CA0YDG158HO34RB10]
[16:33:01.631]  [00:00:00.115][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[16:33:01.632]  [00:00:00.115][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0YDG158HO34RB10
[16:33:01.634]  [00:00:00.116][silabs ]Ver: 5 Btl: 0x03020002 Time:Jun 17 2026 17:12:58 Reset Reason: 0x00000000
[16:33:01.634]  [00:00:00.116][silabs ]SetupQRCode: [MT:K2CA0YDG158HO34RB10]
[16:33:01.634]  [00:00:00.117][silabs ]COM: Init done
[16:33:01.636]  
[16:33:01.636]  Missed Logs: 1
[16:33:01.636]  [00:00:00.117][silabs ]app_mcu_dfu_init: spawning async init thread
[16:33:01.636]  
[16:33:01.636]  Missed Logs: 1
[16:33:01.636]  [00:00:00.118][silabs ]NWK: device has provisioned
[16:33:01.638]  
[16:33:01.638]  [00:00:00.118][silabs ]COM: notify network [Leave]
[16:33:01.638]  [00:00:00.119][silabs ]CLS: register device: dev 0x2002e386 endpoint 1 type 0 idx 1
[16:33:01.639]  [00:00:00.119][silabs ]mcu_dfu_init_thread_func start
[16:33:01.639]  [00:00:00.120][silabs ]waiting for MCU version...
[16:33:01.640]  [00:00:00.121][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[16:33:01.640]  [00:00:00.122][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[16:33:01.641]  [00:00:00.122][silabs ]App Task started
[16:33:01.641]  [00:00:00.122][silabs ]MATTER TX[0-8]: 55 AA 01 00 00 02 01 00 03 
[16:33:01.647]  [00:00:00.123][silabs ]SPP: pending ack but allow new cmd process
[16:33:01.647]  matterCli> [00:00:00.171][silabs ]MATTER RX[0-31]: 55 AA 01 00 00 02 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:33:01.688]  [00:00:00.171][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[16:33:01.745]  [00:00:00.231][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:33:01.745]  [00:00:00.232][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[16:33:01.747]  [00:00:00.232][silabs ]NWK: platform event type 32779
[16:33:01.747]  [00:00:00.233][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[16:33:01.748]  [00:00:00.233][silabs ]NWK: kThreadConnectivityChange,32769
[16:33:01.748]  [00:00:00.233][silabs ]NWK: Thread Established
[16:33:01.749]  [00:00:00.233][silabs ]COM: notify network [Joined]
[16:33:01.749]  [00:00:00.234][info  ][SVR] Scheduling OTA Requestor initialization
[16:33:01.753]  [00:00:00.234][info  ][SVR] Joining Multicast groups
[16:33:01.785]  [00:00:00.272][silabs ]MATTER TX[0-7]: 55 AA 01 00 01 01 00 02 
[16:33:01.785]  [00:00:00.272][silabs ]COM: CMD: 0x01, SN: 0x0001, LEN: 8
[16:33:01.785]  
[16:33:01.785]  [00:00:00.272][silabs ]SPP: ack_timeout_ms 500
[16:33:01.834]  [00:00:00.320][silabs ]MATTER RX[0-31]: 55 AA 01 00 01 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 93 
[16:33:01.835]  [00:00:00.321][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:33:01.835]  [00:00:00.321][silabs ]COM: Failed to extract version from product info
[16:33:01.837]  [00:00:00.321][silabs ]COM: Fallback extracted version: 3.0.0
[16:33:01.837]  [00:00:00.321][silabs ]Current MCU version set to: 3.0.0
[16:33:01.927]  [00:00:00.413][silabs ]got MCU version 3.0.0
[16:33:01.927]  [00:00:00.413][silabs ]mcu_dfu: init done, waiting for Matter OTA trigger...
[16:33:01.935]  [00:00:00.421][silabs ]MATTER TX[0-7]: 55 AA 01 00 02 01 00 03 
[16:33:01.935]  [00:00:00.421][silabs ]COM: CMD: 0x01, SN: 0x0002, LEN: 8
[16:33:01.935]  
[16:33:01.935]  [00:00:00.421][silabs ]SPP: ack_timeout_ms 500
[16:33:01.984]  [00:00:00.470][silabs ]MATTER RX[0-31]: 55 AA 01 00 02 01 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 94 
[16:33:01.986]  [00:00:00.470][silabs ]COM: MCU TX spp_app_event_GetProductInfo - {"p":"BK001","v":"3.0.0}
[16:33:01.986]  [00:00:00.470][silabs ]COM: Failed to extract version from product info
[16:33:01.987]  [00:00:00.470][silabs ]COM: Fallback extracted version: 3.0.0
[16:33:01.987]  [00:00:00.471][silabs ]Current MCU version set to: 3.0.0
[16:33:02.001]  [00:00:00.487][info  ][DL] SRP Client was started, detected server: fd11:9c64:dd37:b8c4:6397:7d5e:9e7b:227a
[16:33:02.001]  [00:00:00.488][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:33:02.002]  [00:00:00.488][silabs ]NWK: platform event type 32779
[16:33:02.002]  [00:00:00.489][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[16:33:02.007]  [00:00:00.489][silabs ]NWK: platform event type 32779
[16:33:02.084]  [00:00:00.571][silabs ]MATTER TX[0-8]: 55 AA 01 00 03 02 01 01 07 
[16:33:02.084]  [00:00:00.571][silabs ]COM: CMD: 0x02, SN: 0x0003, LEN: 9
[16:33:02.084]  
[16:33:02.087]  [00:00:00.571][silabs ]SPP: ack_timeout_ms 500
[16:33:02.134]  [00:00:00.620][silabs ]MATTER RX[0-31]: 55 AA 01 00 03 02 18 7B 22 70 22 3A 22 42 4B 30 30 31 22 2C 22 76 22 3A 22 33 2E 30 2E 30 7D 96 
[16:33:02.136]  [00:00:00.621][silabs ]COM: MCU TX spp_app_event_NwkStatusNotify
[16:33:02.213]  [00:00:00.700][silabs ]MATTER RX[0-11]: 55 AA 01 00 CF 12 04 00 00 00 00 E5 
[16:33:02.213]  [00:00:00.700][silabs ]WDC: report Active percent 0 dev_index 1
[16:33:02.214]  [00:00:00.700][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:33:02.214]  
[16:33:02.214]  [00:00:00.700][info  ][ZCL] Lift[1] Position Set: 10000
[16:33:02.234]  [00:00:00.720][silabs ]MATTER TX[0-7]: 55 AA 01 00 CF 12 00 E1 
[16:33:02.234]  [00:00:00.720][silabs ]COM: CMD: 0x12, SN: 0x00CF, LEN: 8
[16:33:02.234]  
[16:33:02.234]  [00:00:00.720][silabs ]SPP: ack_timeout_ms 500
[16:33:02.712]  [00:00:01.199][silabs ]MATTER RX[0-11]: 55 AA 01 09 CF 12 04 00 00 00 00 EE 
[16:33:02.712]  [00:00:01.200][silabs ]WDC: report Active percent 0 dev_index 1
[16:33:02.715]  [00:00:01.200][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:33:02.715]  
[16:33:02.715]  [00:00:01.200][info  ][ZCL] Lift[1] Position Set: 10000
[16:33:02.718]  [00:00:01.200][silabs ]SPP: pending ack but allow new cmd process
[16:33:02.734]  [00:00:01.220][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:02.734]  [00:00:01.220][silabs ]MATTER TX[0-7]: 55 AA 01 00 CF 12 00 E1 
[16:33:02.736]  [00:00:01.220][silabs ]COM: CMD: 0x12, SN: 0x00CF, LEN: 8
[16:33:02.741]  
[16:33:02.747]  [00:00:01.234][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[16:33:02.747]  [00:00:01.234][silabs ]NWK: platform event type 32786
[16:33:02.748]  [00:00:01.234][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[16:33:02.748]  [00:00:01.234][info  ][SVR] Server initialization complete
[16:33:02.750]  [00:00:01.234][info  ][DIS] Updating services using commissioning mode 0
[16:33:02.750]  [00:00:01.235][info  ][DIS] Advertise operational node 66AC7364E726C344-00000000000008CA
[16:33:02.752]  [00:00:01.236][info  ][DL] advertising srp service: 66AC7364E726C344-00000000000008CA._matter._tcp
[16:33:02.753]  [00:00:01.236][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[16:33:02.753]  [00:00:01.236][silabs ]NWK: platform event type 32790
[16:33:02.762]  [00:00:01.246][info  ][IM] No subscriptions to resume
[16:33:03.212]  [00:00:01.699][silabs ]MATTER RX[0-11]: 55 AA 01 09 CF 12 04 00 00 00 00 EE 
[16:33:03.212]  [00:00:01.699][silabs ]WDC: report Active percent 0 dev_index 1
[16:33:03.214]  [00:00:01.699][silabs ]WDC: EP[1] set CurrentPositionLiftPercentage 10000
[16:33:03.214]  
[16:33:03.214]  [00:00:01.700][info  ][ZCL] Lift[1] Position Set: 10000
[16:33:03.217]  [00:00:01.700][silabs ]SPP: pending ack but allow new cmd process
[16:33:03.234]  [00:00:01.720][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:03.234]  [00:00:01.720][silabs ]MATTER TX[0-7]: 55 AA 01 00 CF 12 00 E1 
[16:33:03.237]  [00:00:01.720][silabs ]COM: CMD: 0x12, SN: 0x00CF, LEN: 8
[16:33:03.241]  
[16:33:03.734]  [00:00:02.220][silabs ]SPP: re-sent reach to max
[16:33:03.734]  [00:00:02.221][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:03.734]  [00:00:02.221][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:03.737]  
[16:33:03.737]  [00:00:02.221][silabs ]SPP: ack_timeout_ms 500
[16:33:03.759]  [00:00:02.245][silabs ]MATTER RX[0-8]: 55 AA 01 00 D0 06 01 00 D7 
[16:33:03.759]  [00:00:02.246][silabs ]COM: spp_app_event_BatteryLevel,sn:0x00D0,len:1
[16:33:03.760]  [00:00:02.246][silabs ]payload[0-0]: 00 
[16:33:03.760]  [00:00:02.246][silabs ]PWR: report Battery Percent 0
[16:33:03.760]  
[16:33:03.760]  [00:00:02.246][silabs ]SPP: pending ack but allow new cmd process
[16:33:04.235]  [00:00:02.721][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:04.235]  [00:00:02.721][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:04.238]  [00:00:02.721][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:04.242]  
[16:33:04.258]  [00:00:02.745][silabs ]MATTER RX[0-8]: 55 AA 01 09 D0 06 01 00 E0 
[16:33:04.258]  [00:00:02.745][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09D0,len:1
[16:33:04.261]  [00:00:02.746][silabs ]payload[0-0]: 00 
[16:33:04.261]  [00:00:02.746][silabs ]PWR: report Battery Percent 0
[16:33:04.261]  
[16:33:04.261]  [00:00:02.746][silabs ]SPP: pending ack but allow new cmd process
[16:33:04.734]  [00:00:03.221][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:04.734]  [00:00:03.221][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:04.737]  [00:00:03.221][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:04.742]  
[16:33:04.758]  [00:00:03.245][silabs ]MATTER RX[0-8]: 55 AA 01 09 D0 06 01 00 E0 
[16:33:04.758]  [00:00:03.245][silabs ]COM: spp_app_event_BatteryLevel,sn:0x09D0,len:1
[16:33:04.760]  [00:00:03.245][silabs ]payload[0-0]: 00 
[16:33:04.760]  [00:00:03.245][silabs ]PWR: report Battery Percent 0
[16:33:04.760]  
[16:33:04.760]  [00:00:03.246][silabs ]SPP: pending ack but allow new cmd process
[16:33:05.235]  [00:00:03.721][silabs ]SPP: re-sent reach to max
[16:33:05.235]  [00:00:03.722][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:05.235]  [00:00:03.722][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:05.239]  
[16:33:05.239]  [00:00:03.722][silabs ]SPP: ack_timeout_ms 500
[16:33:05.307]  [00:00:03.794][silabs ]MATTER RX[0-8]: 55 AA 01 00 D1 07 01 03 DC 
[16:33:05.307]  [00:00:03.794][silabs ]PWR: report Battery Charge State 3
[16:33:05.307]  
[16:33:05.311]  [00:00:03.794][silabs ]SPP: pending ack but allow new cmd process
[16:33:05.735]  [00:00:04.222][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:05.735]  [00:00:04.222][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:05.738]  [00:00:04.222][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:05.741]  
[16:33:05.750]  [00:00:04.236][info  ][DIS] Resolving 66AC7364E726C344:0000000000000001 ...
[16:33:05.750]  [00:00:04.237][info  ][DIS] Lookup started for 66AC7364E726C344-0000000000000001
[16:33:05.807]  [00:00:04.293][silabs ]MATTER RX[0-8]: 55 AA 01 09 D1 07 01 03 E5 
[16:33:05.807]  [00:00:04.294][silabs ]PWR: report Battery Charge State 3
[16:33:05.807]  
[16:33:05.811]  [00:00:04.294][silabs ]SPP: pending ack but allow new cmd process
[16:33:05.951]  [00:00:04.436][info  ][DIS] Checking node lookup status for 66AC7364E726C344-0000000000000001 after 200 ms
[16:33:05.995]  [00:00:04.482][info  ][DIS] Node ID resolved for 66AC7364E726C344-0000000000000001
[16:33:05.995]  [00:00:04.482][info  ][DIS] UDP:[fdd9:d33f:e8ea:b55e:8aa2:9eff:fe1d:c2c2]:5540: new best score: 3 (for 66AC7364E726C344-0000000000000001)
[16:33:05.996]  [00:00:04.482][info  ][DIS] Checking node lookup status for 66AC7364E726C344-0000000000000001 after 246 ms
[16:33:05.997]  [00:00:04.484][info  ][SC] Initiating session on local FabricIndex 1 from 0x00000000000008CA -> 0x0000000000000001
[16:33:06.015]  [00:00:04.502][info  ][EM] <<< [E:57093i S:0 M:265229010] (U) Msg TX from 7A5F92CB17C83FB8 to 0:0000000000000000 [0000] [UDP:[fdd9:d33f:e8ea:b55e:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:233)
[16:33:06.017]  [00:00:04.502][info  ][EM] ??1 [E:57093i S:0 M:265229010] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3637ms from now [State:Idle II:500 AI:2000 AT:4000]
[16:33:06.022]  [00:00:04.503][info  ][SC] Sent Sigma1 msg to <0000000000000001, 1> [II:3000ms AI:2500ms AT:0ms]
[16:33:06.235]  [00:00:04.722][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:06.235]  [00:00:04.722][silabs ]MATTER TX[0-7]: 55 AA 01 09 CF 12 00 EA 
[16:33:06.238]  [00:00:04.722][silabs ]COM: CMD: 0x12, SN: 0x09CF, LEN: 8
[16:33:06.241]  
[16:33:06.306]  [00:00:04.793][silabs ]MATTER RX[0-8]: 55 AA 01 09 D1 07 01 03 E5 
[16:33:06.306]  [00:00:04.793][silabs ]PWR: report Battery Charge State 3
[16:33:06.306]  
[16:33:06.311]  [00:00:04.793][silabs ]SPP: pending ack but allow new cmd process
[16:33:06.522]  [00:00:05.008][info  ][EM] >>> [E:57093i S:0 M:258783732 (Ack:265229010)] (U) Msg RX from 0:0000000000000000 [0000] to 7A5F92CB17C83FB8 --- Type 0000:33 (SecureChannel:CASE_Sigma2Resume) (B:100)
[16:33:06.523]  [00:00:05.009][info  ][EM] <<< [E:57093i S:0 M:265229011 (Ack:258783732)] (U) Msg TX from 7A5F92CB17C83FB8 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:33:06.552]  [00:00:05.039][info  ][EM] <<< [E:57093i S:0 M:265229012 (Ack:258783732)] (U) Msg TX from 7A5F92CB17C83FB8 to 0:0000000000000000 [0000] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[16:33:06.554]  [00:00:05.040][info  ][EM] ??1 [E:57093i S:0 M:265229012] (U) Msg Retransmission to 0:0000000000000000 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[16:33:06.556]  [00:00:05.043][info  ][SC] SecureSession[0x20006e28, LSID:23243]: State change 'kEstablishing' --> 'kActive'
[16:33:06.559]  [00:00:05.044][info  ][SWU] Stopping the watchdog timer
[16:33:06.559]  [00:00:05.044][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[16:33:06.562]  [00:00:05.048][info  ][EM] <<< [E:57094i S:23243 M:40793486] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:97)
[16:33:06.563]  [00:00:05.049][info  ][EM] ??1 [E:57094i S:23243 M:40793486] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[16:33:06.566]  [00:00:05.050][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[16:33:06.566]  [00:00:05.050][silabs ]NWK: platform event type 32792
[16:33:06.736]  [00:00:05.222][silabs ]SPP: re-sent reach to max
[16:33:06.736]  [00:00:05.223][silabs ]MATTER TX[0-7]: 55 AA 01 00 D0 06 00 D6 
[16:33:06.736]  [00:00:05.223][silabs ]COM: CMD: 0x06, SN: 0x00D0, LEN: 8
[16:33:06.738]  
[16:33:06.738]  [00:00:05.223][silabs ]SPP: ack_timeout_ms 500
[16:33:06.856]  [00:00:05.343][silabs ]MATTER RX[0-8]: 55 AA 01 00 D2 08 01 01 DC 
[16:33:06.856]  [00:00:05.343][silabs ]PWR: report Battery Charge Level 1
[16:33:06.856]  
[16:33:06.862]  [00:00:05.343][silabs ]SPP: pending ack but allow new cmd process
[16:33:07.031]  [00:00:05.517][info  ][EM] >>> [E:57093i S:0 M:258783733 (Ack:265229012)] (U) Msg RX from 0:0000000000000000 [0000] to 7A5F92CB17C83FB8 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[16:33:07.055]  [00:00:05.541][info  ][EM] >>> [E:57094i S:23243 M:201846615 (Ack:40793486)] (S) Msg RX from 1:0000000000000001 [C344] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[16:33:07.056]  [00:00:05.541][info  ][DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0004 Status=0x0
[16:33:07.057]  [00:00:05.543][info  ][EM] <<< [E:57094i S:23243 M:40793487 (Ack:201846615)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [C344] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[16:33:07.236]  [00:00:05.723][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:07.236]  [00:00:05.723][silabs ]MATTER TX[0-7]: 55 AA 01 00 D0 06 00 D6 
[16:33:07.241]  [00:00:05.723][silabs ]COM: CMD: 0x06, SN: 0x00D0, LEN: 8
[16:33:07.241]  
[16:33:07.355]  [00:00:05.842][silabs ]MATTER RX[0-8]: 55 AA 01 09 D2 08 01 01 E5 
[16:33:07.355]  [00:00:05.843][silabs ]PWR: report Battery Charge Level 1
[16:33:07.355]  
[16:33:07.362]  [00:00:05.843][silabs ]SPP: pending ack but allow new cmd process
[16:33:07.735]  [00:00:06.223][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:07.735]  [00:00:06.223][silabs ]MATTER TX[0-7]: 55 AA 01 00 D0 06 00 D6 
[16:33:07.742]  [00:00:06.223][silabs ]COM: CMD: 0x06, SN: 0x00D0, LEN: 8
[16:33:07.742]  
[16:33:07.856]  [00:00:06.342][silabs ]MATTER RX[0-8]: 55 AA 01 09 D2 08 01 01 E5 
[16:33:07.856]  [00:00:06.342][silabs ]PWR: report Battery Charge Level 1
[16:33:07.856]  
[16:33:07.861]  [00:00:06.343][silabs ]SPP: pending ack but allow new cmd process
[16:33:08.237]  [00:00:06.723][silabs ]SPP: re-sent reach to max
[16:33:08.237]  [00:00:06.724][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:08.237]  [00:00:06.724][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:08.241]  
[16:33:08.241]  [00:00:06.724][silabs ]SPP: ack_timeout_ms 500
[16:33:08.406]  [00:00:06.892][silabs ]MATTER RX[0-8]: 55 AA 01 00 D3 08 01 02 DE 
[16:33:08.406]  [00:00:06.892][silabs ]PWR: report Battery Charge Level 2
[16:33:08.406]  
[16:33:08.409]  [00:00:06.892][silabs ]SPP: pending ack but allow new cmd process
[16:33:08.737]  [00:00:07.224][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:08.737]  [00:00:07.224][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:08.741]  [00:00:07.224][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:08.741]  
[16:33:08.905]  [00:00:07.391][silabs ]MATTER RX[0-8]: 55 AA 01 09 D3 08 01 02 E7 
[16:33:08.905]  [00:00:07.392][silabs ]SPP: tx_queue full!
[16:33:08.905]  [00:00:07.392][silabs ]PWR: report Battery Charge Level 2
[16:33:08.911]  
[16:33:09.237]  [00:00:07.724][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:09.237]  [00:00:07.724][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:09.242]  [00:00:07.724][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:09.242]  
[16:33:09.404]  [00:00:07.891][silabs ]MATTER RX[0-8]: 55 AA 01 09 D3 08 01 02 E7 
[16:33:09.404]  [00:00:07.891][silabs ]SPP: tx_queue full!
[16:33:09.404]  [00:00:07.891][silabs ]PWR: report Battery Charge Level 2
[16:33:09.411]  
[16:33:09.737]  [00:00:08.224][silabs ]SPP: re-sent reach to max
[16:33:09.737]  [00:00:08.225][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:09.737]  [00:00:08.225][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:09.741]  
[16:33:09.741]  [00:00:08.225][silabs ]SPP: ack_timeout_ms 500
[16:33:10.238]  [00:00:08.725][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:10.238]  [00:00:08.725][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:10.241]  [00:00:08.725][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:10.246]  
[16:33:10.737]  [00:00:09.225][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:10.737]  [00:00:09.225][silabs ]MATTER TX[0-7]: 55 AA 01 09 D0 06 00 DF 
[16:33:10.741]  [00:00:09.225][silabs ]COM: CMD: 0x06, SN: 0x09D0, LEN: 8
[16:33:10.746]  
[16:33:11.238]  [00:00:09.725][silabs ]SPP: re-sent reach to max
[16:33:11.238]  [00:00:09.726][silabs ]MATTER TX[0-7]: 55 AA 01 00 D1 07 00 D8 
[16:33:11.238]  [00:00:09.726][silabs ]COM: CMD: 0x07, SN: 0x00D1, LEN: 8
[16:33:11.242]  
[16:33:11.242]  [00:00:09.726][silabs ]SPP: ack_timeout_ms 500
[16:33:11.738]  [00:00:10.226][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:11.738]  [00:00:10.226][silabs ]MATTER TX[0-7]: 55 AA 01 00 D1 07 00 D8 
[16:33:11.742]  [00:00:10.226][silabs ]COM: CMD: 0x07, SN: 0x00D1, LEN: 8
[16:33:11.746]  
[16:33:12.238]  [00:00:10.726][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:12.238]  [00:00:10.726][silabs ]MATTER TX[0-7]: 55 AA 01 00 D1 07 00 D8 
[16:33:12.241]  [00:00:10.726][silabs ]COM: CMD: 0x07, SN: 0x00D1, LEN: 8
[16:33:12.246]  
[16:33:12.739]  [00:00:11.226][silabs ]SPP: re-sent reach to max
[16:33:12.739]  [00:00:11.227][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:12.739]  [00:00:11.227][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:12.742]  
[16:33:12.742]  [00:00:11.227][silabs ]SPP: ack_timeout_ms 500
[16:33:13.240]  [00:00:11.727][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:13.240]  [00:00:11.727][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:13.242]  [00:00:11.727][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:13.246]  
[16:33:13.740]  [00:00:12.227][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:13.740]  [00:00:12.227][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:13.742]  [00:00:12.227][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:13.745]  
[16:33:14.240]  [00:00:12.727][silabs ]SPP: re-sent reach to max
[16:33:14.240]  [00:00:12.728][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:14.240]  [00:00:12.728][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:14.243]  
[16:33:14.243]  [00:00:12.728][silabs ]SPP: ack_timeout_ms 500
[16:33:14.741]  [00:00:13.228][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:14.741]  [00:00:13.228][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:14.743]  [00:00:13.228][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:14.746]  
[16:33:15.240]  [00:00:13.728][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:15.240]  [00:00:13.728][silabs ]MATTER TX[0-7]: 55 AA 01 09 D1 07 00 E1 
[16:33:15.242]  [00:00:13.728][silabs ]COM: CMD: 0x07, SN: 0x09D1, LEN: 8
[16:33:15.246]  
[16:33:15.740]  [00:00:14.228][silabs ]SPP: re-sent reach to max
[16:33:15.740]  [00:00:14.229][silabs ]MATTER TX[0-7]: 55 AA 01 00 D2 08 00 DA 
[16:33:15.740]  [00:00:14.229][silabs ]COM: CMD: 0x08, SN: 0x00D2, LEN: 8
[16:33:15.746]  
[16:33:15.746]  [00:00:14.229][silabs ]SPP: ack_timeout_ms 500
[16:33:16.241]  [00:00:14.729][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:16.241]  [00:00:14.729][silabs ]MATTER TX[0-7]: 55 AA 01 00 D2 08 00 DA 
[16:33:16.246]  [00:00:14.729][silabs ]COM: CMD: 0x08, SN: 0x00D2, LEN: 8
[16:33:16.246]  
[16:33:16.741]  [00:00:15.229][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:16.741]  [00:00:15.229][silabs ]MATTER TX[0-7]: 55 AA 01 00 D2 08 00 DA 
[16:33:16.747]  [00:00:15.229][silabs ]COM: CMD: 0x08, SN: 0x00D2, LEN: 8
[16:33:16.747]  
[16:33:17.242]  [00:00:15.729][silabs ]SPP: re-sent reach to max
[16:33:17.242]  [00:00:15.730][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:17.242]  [00:00:15.730][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:17.246]  
[16:33:17.246]  [00:00:15.730][silabs ]SPP: ack_timeout_ms 500
[16:33:17.742]  [00:00:16.230][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:17.742]  [00:00:16.230][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:17.745]  [00:00:16.230][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:17.745]  
[16:33:18.242]  [00:00:16.730][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:18.242]  [00:00:16.730][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:18.245]  [00:00:16.730][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:18.245]  
[16:33:18.742]  [00:00:17.230][silabs ]SPP: re-sent reach to max
[16:33:18.742]  [00:00:17.231][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:18.742]  [00:00:17.231][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:18.746]  
[16:33:18.746]  [00:00:17.231][silabs ]SPP: ack_timeout_ms 500
[16:33:19.243]  [00:00:17.731][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:19.243]  [00:00:17.731][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:19.245]  [00:00:17.731][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:19.250]  
[16:33:19.743]  [00:00:18.231][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:19.743]  [00:00:18.231][silabs ]MATTER TX[0-7]: 55 AA 01 09 D2 08 00 E3 
[16:33:19.746]  [00:00:18.231][silabs ]COM: CMD: 0x08, SN: 0x09D2, LEN: 8
[16:33:19.751]  
[16:33:20.243]  [00:00:18.731][silabs ]SPP: re-sent reach to max
[16:33:20.243]  [00:00:18.732][silabs ]MATTER TX[0-7]: 55 AA 01 00 D3 08 00 DB 
[16:33:20.243]  [00:00:18.732][silabs ]COM: CMD: 0x08, SN: 0x00D3, LEN: 8
[16:33:20.247]  
[16:33:20.247]  [00:00:18.732][silabs ]SPP: ack_timeout_ms 500
[16:33:20.744]  [00:00:19.232][silabs ]SPP: re-sent count 1, ack_timeout_ms 500
[16:33:20.744]  [00:00:19.232][silabs ]MATTER TX[0-7]: 55 AA 01 00 D3 08 00 DB 
[16:33:20.747]  [00:00:19.232][silabs ]COM: CMD: 0x08, SN: 0x00D3, LEN: 8
[16:33:20.750]  
[16:33:21.244]  [00:00:19.732][silabs ]SPP: re-sent count 2, ack_timeout_ms 500
[16:33:21.244]  [00:00:19.732][silabs ]MATTER TX[0-7]: 55 AA 01 00 D3 08 00 DB 
[16:33:21.247]  [00:00:19.732][silabs ]COM: CMD: 0x08, SN: 0x00D3, LEN: 8
[16:33:21.250]  
[16:33:21.746]  [00:00:20.232][silabs ]SPP: re-sent reach to max
```