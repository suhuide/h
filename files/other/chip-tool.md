```c
sudo ot-ctl dataset active -x
0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8
Done

sudo ./chip-tool payload parse-setup-payload MT:SAGA442C00KA0648G00
[1770349320.167] [20645:20645] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1770349320.167] [20645:20645] [SPL] Parsing base38Representation: MT:SAGA442C00KA0648G00
[1770349320.168] [20645:20645] [SPL] Version:             0
[1770349320.168] [20645:20645] [SPL] VendorID:            65521
[1770349320.168] [20645:20645] [SPL] ProductID:           32784
[1770349320.168] [20645:20645] [SPL] Custom flow:         0    (STANDARD)
[1770349320.168] [20645:20645] [SPL] Discovery Bitmask:   0x02 (BLE)
[1770349320.168] [20645:20645] [SPL] Long discriminator:  3840   (0xf00)
[1770349320.168] [20645:20645] [SPL] Passcode:            20202021

sudo rm -rf /tmp/chip_*
sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840 --paa-trust-store-path ~/paa-root-certs

sudo ./chip-tool onoff on 2250 3
sudo ./chip-tool onoff off 2250 3
sudo ./chip-tool levelcontrol move-to-level 128 0 0 0 2250 3
sudo ./chip-tool levelcontrol read min-level 2250 3
sudo ./chip-tool levelcontrol read max-level 2250 3
sudo ./chip-tool levelcontrol read current-level 2250 3
sudo ./chip-tool levelcontrol read all 2250 3

sudo ./chip-tool basicinformation read software-version 2250 0
sudo ./chip-tool basicinformation read software-version-string 2250 0
```
```c
sudo ./chip-tool descriptor read parts-list 2250 0
[1773133102.269] [2893471:2893473] [TOO]   PartsList: 6 entries
[1773133102.269] [2893471:2893473] [TOO]     [1]: 1
[1773133102.269] [2893471:2893473] [TOO]     [2]: 2
[1773133102.269] [2893471:2893473] [TOO]     [3]: 3
[1773133102.269] [2893471:2893473] [TOO]     [4]: 4
[1773133102.269] [2893471:2893473] [TOO]     [5]: 5
[1773133102.269] [2893471:2893473] [TOO]     [6]: 6

sudo ./chip-tool descriptor read device-type-list 2250 6
[1773134080.593] [2957410:2957438] [TOO]   DeviceTypeList: 1 entries
[1773134080.593] [2957410:2957438] [TOO]     [1]: {
[1773134080.593] [2957410:2957438] [TOO]       DeviceType: 266 (On/Off Plug-in Unit)
[1773134080.593] [2957410:2957438] [TOO]       Revision: 1
[1773134080.593] [2957410:2957438] [TOO]      }

sudo ./chip-tool descriptor read server-list 2250 6
[1773134113.437] [2959503:2959505] [TOO]   ServerList: 5 entries
[1773134113.437] [2959503:2959505] [TOO]     [1]: 29 (Descriptor)
[1773134113.437] [2959503:2959505] [TOO]     [2]: 3 (Identify)
[1773134113.437] [2959503:2959505] [TOO]     [3]: 4 (Groups)
[1773134113.437] [2959503:2959505] [TOO]     [4]: 6 (OnOff)
[1773134113.437] [2959503:2959505] [TOO]     [5]: 98 (ScenesManagement)

```
2. 新起一个 独立的SSH窗口(不能关闭，也不要这个独立窗口执行其他命令), 使用chip-ota-provider-app工具加载打包固件
./chip-ota-provider-app --KVS /tmp/chip_kvs_provider -f pte9_wired_matter-v65.00.FF-signed_0xFFF1_0x8004.ota

3.入网和配置chip-ota-provider-app （只需要运行一次即可，后续OTA升级不需要运行 ）
sudo ./chip-tool pairing onnetwork 1 20202021 
sudo ./chip-tool accesscontrol write acl '[{"fabricIndex": 1, "privilege": 5, "authMode": 2, "subjects": [112233], "targets": null}, {"fabricIndex": 1, "privilege": 3, "authMode": 2, "subjects": null, "targets": null}]' 1 0 

4. 触发OTA升级; 启动升级后，设备白灯闪烁，升级的时间大约要2分钟
sudo ./chip-tool otasoftwareupdaterequestor announce-otaprovider 1 0 0 0 2252 0 

5. 升级成功后，设备重启，通过查看启动日志确认升级是否成功。
matter固件版本号：[TOO]   SoftwareVersionString: 

NOTE:
ps -ef | grep "ota" //查看进程
killall -9 sudo chip-ota-provider-app //杀掉进程的命令