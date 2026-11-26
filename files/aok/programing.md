
```c
2026-08-31 09:19:23,051 root INFO ****************************************
2026-08-31 09:19:23,052 root INFO 读取QR码: MT:MNKA1KKN16G7UO3.Y10
2026-08-31 09:19:23,052 root INFO Jlink Speed=8000 KHz
2026-08-31 09:19:26,067 root INFO 芯片信息：
  ∙ part: 'efr32mg24a410f1536im40'
  ∙ family: 'efr32mg24'
  ∙ version: '10'
  ∙ revision: 'A1'
  ∙ flash_addr: 0x08000000
  ∙ flash_size: 0x00180000

2026-08-31 09:19:26,070 root INFO 芯片SE: 
  ∙ SE Firmware version: '2.2.5'
  ∙ Serial number: '000000000000000038398ffffe536e4b'
  ∙ Debug lock: 'False'
  ∙ Device erase: 'True'
  ∙ Secure debug unlock: False
  ∙ Secure boot: True
  ∙ Boot status: 0x20 OK
  ∙ Command key installed: True
  ∙ Sign key installed: True

2026-08-31 09:19:26,071 root INFO 生成 manufacturing_date: 20260831091926
2026-08-31 09:19:28,682 root INFO ****************************************
2026-08-31 09:19:28,685 root INFO 读取QR码: MT:MNKA1KKN16G7UO3.Y10
2026-08-31 09:19:28,686 root INFO 正在运行中...
2026-08-31 09:19:33,630 root CRITICAL ⛔️ Command 'commander-cli device masserase --device EFR32MG24 --serialno 440045640' returned non-zero exit status 4294967294. code=b'Resetting device...\r\nERROR: Could not halt the device when connecting.\r\nDONE\r\n'
2026-08-31 09:19:33,631 root ERROR Command 'commander-cli device masserase --device EFR32MG24 --serialno 440045640' returned non-zero exit status 4294967294. code=b'Resetting device...\r\nERROR: Could not halt the device when connecting.\r\nDONE\r\n'
Traceback (most recent call last):
  File "D:\hrf\mfg\matter_mfg_tool\modules\util.py", line 22, in execute
  File "D:\hrf\mfg\matter_mfg_tool\subprocess.py", line 421, in check_output
  File "D:\hrf\mfg\matter_mfg_tool\subprocess.py", line 526, in run
subprocess.CalledProcessError: Command 'commander-cli device masserase --device EFR32MG24 --serialno 440045640' returned non-zero exit status 4294967294.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 993, in run
  File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 763, in start_flash
  File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 223, in workflow_erase_all
  File "D:\hrf\mfg\matter_mfg_tool\writer_efr32.py", line 273, in erase_chip
  File "D:\hrf\mfg\matter_mfg_tool\modules\efr32_commander.py", line 405, in masserase
  File "D:\hrf\mfg\matter_mfg_tool\modules\efr32_commander.py", line 245, in execute
  File "D:\hrf\mfg\matter_mfg_tool\modules\util.py", line 24, in execute
  File "D:\hrf\mfg\matter_mfg_tool\modules\util.py", line 53, in fail
modules.util.UtilException: Command 'commander-cli device masserase --device EFR32MG24 --serialno 440045640' returned non-zero exit status 4294967294. code=b'Resetting device...\r\nERROR: Could not halt the device when connecting.\r\nDONE\r\n'
2026-08-31 09:19:33,631 root ERROR Closing all connection
2026-08-31 09:19:33,631 root ERROR All connection Closed
2026-08-31 09:19:46,520 root ERROR 输入的二维码为空
2026-08-31 09:19:49,388 root INFO 正在读取配置 D:/hrf/mfg/HM-MT2401BR-IPEX-AOK02AC-v1.0.0-20260825182657/debug.json
2026-08-31 09:19:49,390 root INFO Lockout code enabled
2026-08-31 09:19:49,390 root INFO 配置读取成功!
2026-08-31 09:19:49,390 root INFO ERF32 Matter SDK版本: 1.2 证书偏移地址: 4096
2026-08-31 09:19:49,392 root INFO 使用配置文件指定的CD文件 D:\hrf\mfg\HM-MT2401BR-IPEX-AOK02AC-v1.0.0-20260825182657\cert\fam226497.der
2026-08-31 09:19:49,396 root INFO 重新检测下载器接口
2026-08-31 09:19:49,510 root INFO extension_dac=0
2026-08-31 09:19:49,510 root INFO origin_vendor_id=0x1470 origin_product_id=0x8006 vendor_id=0x149A product_id=0x3215 avaliable_dac=200, used_dac=116
2026-08-31 09:19:49,510 root INFO 使用配置文件的生产参数！！！
```
## Time
```c
09:19:49
09:19:23
```

## 2
```c
2026-09-07 13:57:15,622 root INFO **************************************** 
2026-09-07 13:57:15,623 root INFO 读取QR码: MT:MNKA1SWV175I8O7IO10 
2026-09-07 13:57:21,291 root INFO **************************************** 
2026-09-07 13:57:21,292 root INFO 读取QR码: MT:MNKA1SWV175I8O7IO10 
2026-09-07 13:57:21,405 root INFO Jlink Speed=8000 KHz 
2026-09-07 13:57:23,674 root INFO 芯片信息： ∙ part: 'efr32mg24a410f1536im40' ∙ family: 'efr32mg24' ∙ version: '10' ∙ revision: 'A1' ∙ flash_addr: 0x08000000 ∙ flash_size: 0x00180000 
2026-09-07 13:57:23,675 root INFO 芯片SE: ∙ SE Firmware version: '2.2.5' ∙ Serial number: '000000000000000038398ffffe538f77' ∙ Debug lock: 'False' ∙ Device erase: 'True' ∙ Secure debug unlock: False ∙ Secure boot: True ∙ Boot status: 0x20 OK ∙ Command key installed: True ∙ Sign key installed: True 
2026-09-07 13:57:23,677 root INFO 生成 manufacturing_date: 20260907135723 
2026-09-07 13:57:28,955 root INFO 复位芯片 
2026-09-07 13:57:29,335 root INFO 下载GFW固件 
2026-09-07 13:57:33,049 root INFO 连接Jlink 
2026-09-07 13:57:33,250 root INFO 初始化芯片 
2026-09-07 13:57:33,378 root INFO 读取DAC信息, device_id=38398ffffe538f77 
2026-09-07 13:57:34,526 root INFO write lockout: 2d64887a1ec3e607af418cf024c06a61453ce63d88d8080bc07423a78e2b7a60 
2026-09-07 13:57:35,693 root INFO 获取BLE_ADV_UUID值 [a816d99b264d4a2ebafd54504b3ba414] 
2026-09-07 13:57:35,693 root INFO 正在生成配网参数 
2026-09-07 13:57:35,700 root INFO 正在写入Verifier 
2026-09-07 13:57:51,889 root INFO 正在使能Secure Boot 
2026-09-07 13:57:51,916 root INFO 正在写入Pub Sign Key 
2026-09-07 13:57:52,653 root WARNING Key已被写入过, 忽略本次操作 
2026-09-07 13:57:52,653 root INFO 正在写入Secure Boot配置 
2026-09-07 13:57:53,240 root WARNING Secure Boot已被写入过, 忽略本次操作 
2026-09-07 13:57:53,248 root INFO Secure Boot配置完成 
2026-09-07 13:57:53,248 root INFO 正在写入GBL Decrypt Key到SE中 
2026-09-07 13:57:53,248 root INFO 正在写入AES Key 
2026-09-07 13:57:53,683 root WARNING AES Key已被写入过, 忽略本次操作 
2026-09-07 13:57:54,690 root INFO 读取STWE01启动日志, port=COM6, baudrate=921600 
2026-09-07 13:57:55,003 root ERROR CompletedProcess(args='commander-cli vcom config --baudrate 921600 --identifybyserialport COM6', returncode=4294967294) 
2026-09-07 13:57:55,004 root CRITICAL ⛔️ Command failed with code -2 code=-2 
2026-09-07 13:57:55,004 root ERROR Command failed with code -2 code=-2 Traceback (most recent call last): File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 993, in run File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 905, in start_flash File "D:\hrf\mfg\matter_mfg_tool\mfg_worker.py", line 559, in workflow_collect_stwe01_firmware_info File "D:\hrf\mfg\matter_mfg_tool\modules\stwe01_version_reader.py", line 166, in read_stwe01_startup_versions File "D:\hrf\mfg\matter_mfg_tool\modules\stwe01_version_reader.py", line 83, in open_serial_with_recovery File "D:\hrf\mfg\matter_mfg_tool\modules\efr32_commander.py", line 286, in configure_vcom File "D:\hrf\mfg\matter_mfg_tool\modules\efr32_commander.py", line 282, in File "D:\hrf\mfg\matter_mfg_tool\modules\efr32_commander.py", line 277, in execute_by_serial_port File "D:\hrf\mfg\matter_mfg_tool\modules\util.py", line 31, in execute File "D:\hrf\mfg\matter_mfg_tool\modules\util.py", line 53, in fail modules.util.UtilException: Command failed with code -2 code=-2 
2026-09-07 13:57:55,004 root ERROR Closing all connection 
2026-09-07 13:57:55,004 root ERROR All connection Closed 
2026-09-07 13:58:01,020 root ERROR 输入的二维码为空 
```
## Time
```c
13:57:54
13:57:15
```