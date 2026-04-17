# [OT](ot.md)

```c
sudo ot-ctl dataset active -x
0e0800000000000100004a0300000d35060004001fffe002080ba8c26939f226680708fdd0a8de45a382e40510e9405e254d6075c62bac56ebbd930ecd030f4f70656e5468726561642d3533343601025346041013957463af0d2b6e844136e1f3fbf0300c0402a0f7f8000300000f
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
```
```c
ubuntu@ubuntu:~$ sudo ./chip-tool payload parse-setup-payload MT:GYFB5KY61495TG11V10
[1773207925.100] [2635626:2635626] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1773207925.100] [2635626:2635626] [SPL] Parsing base38Representation: MT:GYFB5KY61495TG11V10
[1773207925.100] [2635626:2635626] [SPL] Version:             0
[1773207925.100] [2635626:2635626] [SPL] VendorID:            5274
[1773207925.100] [2635626:2635626] [SPL] ProductID:           12821
[1773207925.100] [2635626:2635626] [SPL] Custom flow:         0    (STANDARD)
[1773207925.100] [2635626:2635626] [SPL] Discovery Bitmask:   0x02 (BLE)
[1773207925.100] [2635626:2635626] [SPL] Long discriminator:  1884   (0x75c)
[1773207925.100] [2635626:2635626] [SPL] Passcode:            85956333
```
```c
sudo rm -rf /tmp/chip_*
```
```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000d35060004001fffe002080ba8c26939f226680708fdd0a8de45a382e40510e9405e254d6075c62bac56ebbd930ecd030f4f70656e5468726561642d3533343601025346041013957463af0d2b6e844136e1f3fbf0300c0402a0f7f8000300000f 20202021 3840 
```

```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000d35060004001fffe002080ba8c26939f226680708fdd0a8de45a382e40510e9405e254d6075c62bac56ebbd930ecd030f4f70656e5468726561642d3533343601025346041013957463af0d2b6e844136e1f3fbf0300c0402a0f7f8000300000f 20202021 3840
```

```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000d35060004001fffe002080ba8c26939f226680708fdd0a8de45a382e40510e9405e254d6075c62bac56ebbd930ecd030f4f70656e5468726561642d3533343601025346041013957463af0d2b6e844136e1f3fbf0300c0402a0f7f8000300000f 85956333 1884 --paa-trust-store-path ~/paa-root-certs
```
```c
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
sudo ./chip-tool basicinformation read specification-version 2250 0
[1773207413.406] [2596661:2596663] [TOO]   SpecificationVersion: 17039360(0x01040000)
//inline constexpr uint32_t kSpecificationVersion = 0x01040000;
//inline constexpr uint32_t kSpecificationVersion = 0x01050000;
```
|Bits |Name |Summary|
| -- | -- | -- |
|31 .. 24 |Major | Major version of specification.|
|23 .. 16 |Minor | Minor version of specification.|
|15 .. 8 |Dot | Dot version of the specification.|
|7 .. 0 |Reserved1 | Future reserved version field 1,set to 0 until defined.|

```c
sudo ./chip-tool descriptor read parts-list 2250 0
[1773133102.269] [2893471:2893473] [TOO]   PartsList: 6 entries
[1773133102.269] [2893471:2893473] [TOO]     [1]: 1
[1773133102.269] [2893471:2893473] [TOO]     [2]: 2
[1773133102.269] [2893471:2893473] [TOO]     [3]: 3
[1773133102.269] [2893471:2893473] [TOO]     [4]: 4
[1773133102.269] [2893471:2893473] [TOO]     [5]: 5
[1773133102.269] [2893471:2893473] [TOO]     [6]: 6
```
```c
sudo ./chip-tool descriptor read device-type-list 2250 6
[1773134080.593] [2957410:2957438] [TOO]   DeviceTypeList: 1 entries
[1773134080.593] [2957410:2957438] [TOO]     [1]: {
[1773134080.593] [2957410:2957438] [TOO]       DeviceType: 266 (On/Off Plug-in Unit)
[1773134080.593] [2957410:2957438] [TOO]       Revision: 1
[1773134080.593] [2957410:2957438] [TOO]      }
```
```c
sudo ./chip-tool descriptor read server-list 2250 6
[1773134113.437] [2959503:2959505] [TOO]   ServerList: 5 entries
[1773134113.437] [2959503:2959505] [TOO]     [1]: 29 (Descriptor)
[1773134113.437] [2959503:2959505] [TOO]     [2]: 3 (Identify)
[1773134113.437] [2959503:2959505] [TOO]     [3]: 4 (Groups)
[1773134113.437] [2959503:2959505] [TOO]     [4]: 6 (OnOff)
[1773134113.437] [2959503:2959505] [TOO]     [5]: 98 (ScenesManagement)

```

```c
sudo ./chip-tool levelcontrol move-to-level 128 0 0 0 2250 1
sudo ./chip-tool colorcontrol move-to-color-temperature 4000 0 0 0 2250 1
```

```c
sudo ./chip-tool interactive start
any subscribe-by-id 0xffffffff 0xffffffff 0 1 2250 0xffff
```
