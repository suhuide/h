# [OT](ot.md)
# [CERT](cert.md)  

```c
sudo ot-ctl dataset active -x
0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f
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
sudo ./chip-tool payload parse-setup-payload MT:GYFB5KY61495TG11V10
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
sudo ./chip-tool payload parse-setup-payload MT:K2CA0Q1814EZX083N00
[1779188027.854] [3269625:3269625] [DL] ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_tool_kvs
[1779188027.854] [3269625:3269625] [SPL] Parsing base38Representation: MT:K2CA0Q1814EZX083N00
[1779188027.858] [3269625:3269625] [SPL] Version:             0
[1779188027.858] [3269625:3269625] [SPL] VendorID:            5232
[1779188027.858] [3269625:3269625] [SPL] ProductID:           65281
[1779188027.858] [3269625:3269625] [SPL] Custom flow:         0    (STANDARD)
[1779188027.859] [3269625:3269625] [SPL] Discovery Bitmask:   0x02 (BLE)
[1779188027.859] [3269625:3269625] [SPL] Long discriminator:  3876   (0xf24)
[1779188027.859] [3269625:3269625] [SPL] Passcode:            28770211
```

```c
sudo rm -rf /tmp/chip_*
```
```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 20202021 3840 
```

```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 20202021 3840
```

```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 85956333 1884 --paa-trust-store-path ~/paa-root-certs
```
```c
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 28770211 3876 --paa-trust-store-path ~/paa-root-certs
```
```c
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
# OnOff
```c
sudo ./chip-tool onoff on 2250 2
sudo ./chip-tool onoff off 2250 2
sudo ./chip-tool onoff read on-off 2250 6
sudo ./chip-tool onoff read start-up-on-off 2250 6
sudo ./chip-tool onoff write start-up-on-off 0 2250 6
```
## Level
```c
sudo ./chip-tool levelcontrol move-to-level 0 0 0 0 2250 2
sudo ./chip-tool levelcontrol move-to-level 128 0 0 0 2250 2
sudo ./chip-tool levelcontrol move-to-level 254 0 0 0 2250 2

sudo ./chip-tool levelcontrol move-to-level 128 30 0 0 2250 2
sudo ./chip-tool levelcontrol read min-level 2250 2
sudo ./chip-tool levelcontrol read max-level 2250 2
sudo ./chip-tool levelcontrol read current-level 2250 2
sudo ./chip-tool levelcontrol read all 2250 2
```
## Color temperature
```c
sudo ./chip-tool colorcontrol move-to-color-temperature 4000 30 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color-temperature 100 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color-temperature 100 30 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color-temperature 650 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color-temperature 650 30 0 0 2250 2
```
## XY color control
🔵	
```c
sudo ./chip-tool colorcontrol move-to-color 9830 3931 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color 9830 3931 30 0 0 2250 2
```
🔴
```c
sudo ./chip-tool colorcontrol move-to-color 41947 21624 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color 41947 21624 30 0 0 2250 2
```
🟢
```c
sudo ./chip-tool colorcontrol move-to-color 19660 39320  0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color 19660 39320  30 0 0 2250 2
```
🟣
```c
sudo ./chip-tool colorcontrol move-to-color 20971 9830 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-color 20971 9830 30 0 0 2250 2
```
### Read
```c
sudo ./chip-tool colorcontrol read color-mode 2250 2
sudo ./chip-tool colorcontrol read current-x 2250 2
sudo ./chip-tool colorcontrol read current-y 2250 2
```
## HSV color control
🔵 色相角 240° → Hue = 254 * 240 / 360 ≈ 170
```c
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 170 254 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 170 254 30 0 0 2250 2
```
🔴 色相角 0° → Hue = 0
```c
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 0 254 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 0 254 30 0 0 2250 2
```
🟢 色相角 120° → Hue = 254 * 120 / 360 ≈ 85
```c
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 85 254 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 85 254 30 0 0 2250 2
```
🟣 色相角  270° → Hue = 254 * 270 / 360 ≈ 191
```c
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 191 254 0 0 0 2250 2
sudo ./chip-tool colorcontrol move-to-hue-and-saturation 191 254 30 0 0 2250 2
```

## Windowcovering
```c
sudo ./chip-tool windowcovering up-or-open 2250 1
sudo ./chip-tool windowcovering go-to-lift-percentage 6000 2250 1
sudo ./chip-tool windowcovering go-to-lift-percentage 3000 2250 1
sudo ./chip-tool windowcovering down-or-close 2250 1
```
## Groups
```c
sudo ./chip-tool groupkeymanagement read max-groups-per-fabric 2250 0
```
## descriptor
```c
sudo ./chip-tool descriptor read feature-map 2250 1
```

## Identify
### Identify
```c
sudo ./chip-tool identify identify 10 2250 1
sudo ./chip-tool identify identify 30 2250 1
sudo ./chip-tool identify identify 0 2250 1
sudo ./chip-tool identify identify 3600 2250 1
```
### TriggerEffect 
```c
sudo ./chip-tool identify trigger-effect 0 0 2250 1
sudo ./chip-tool identify trigger-effect 1 1 2250 1
```

## Other
```c
sudo ./chip-tool interactive start
any subscribe-by-id 0xffffffff 0xffffffff 0 1 2250 0xffff
```

# CD
```c
sudo chmod +x chip-cert
./chip-cert print-cd ./csa25d65mat4831124.der
SignerKeyId value: hex:FE343F959947763B61EE4539131338494FE67D8E
0x01, tag[Anonymous]: 0x100, type: Structure (0x15), container:
0x04,     tag[Context Specific]: 0x0, type: Unsigned Fixed Point (0x04), value: 1
0x08,     tag[Context Specific]: 0x1, type: Unsigned Fixed Point (0x04), value: 5274
0x0A,     tag[Context Specific]: 0x2, type: Array (0x16), container:
0x0D,         tag[Anonymous]: 0x100, type: Unsigned Fixed Point (0x04), value: 12821
0x12,     tag[Context Specific]: 0x3, type: Unsigned Fixed Point (0x04), value: 514
0x15,     tag[Context Specific]: 0x4, type: UTF-8 String (0x0c), length: 19, value: "CSA25D65MAT48311-24"
0x2B,     tag[Context Specific]: 0x5, type: Unsigned Fixed Point (0x04), value: 0
0x2E,     tag[Context Specific]: 0x6, type: Unsigned Fixed Point (0x04), value: 0
0x31,     tag[Context Specific]: 0x7, type: Unsigned Fixed Point (0x04), value: 1
0x34,     tag[Context Specific]: 0x8, type: Unsigned Fixed Point (0x04), value: 2
0x38,     tag[Context Specific]: 0x9, type: Unsigned Fixed Point (0x04), value: 5232
0x3C,     tag[Context Specific]: 0xa, type: Unsigned Fixed Point (0x04), value: 32774
0x3E,     tag[Context Specific]: 0xb, type: Array (0x16), container:
0x40,         tag[Anonymous]: 0x100, type: Octet String (0x10), length: 20, value: hex:E9160DC417F7419C95320BBF365671933FF31222
```
| TLV 项 | 字段含义 | 解析出的值 |
| :--- | :--- | :--- |
| **`SignerKeyId value`** | **签名者密钥标识符** | `FE343F959947763B61EE4539131338494FE67D8E` |
| **`tag[Anonymous]: 0x100`** | **结构体版本** | `1` |
| **`tag[Context Specific]: 0x1`** | **供应商ID (Vendor ID)** | `5274` (0x149A) |
| **`tag[Context Specific]: 0x2`** | **产品ID (Product ID)** | `12821` (0x3215) |
| **`tag[Context Specific]: 0x3`** | **设备类型ID (Device Type ID)** | `514` (0x202) |
| **`tag[Context Specific]: 0x4`** | **认证ID (Certification ID)** | `"CSA25D65MAT48311-24"` |
| **`tag[Context Specific]: 0x5`** | **安全策略 (Security Policy)** | `0` |
| **`tag[Context Specific]: 0x6`** | **RCD 版本号** | `0` |
| **`tag[Context Specific]: 0x7`** | **设备特征版本号** | `1` |
| **`tag[Context Specific]: 0x8`** | **认证类型 (Certification Type)** | `2` |
| **`tag[Context Specific]: 0x9`** | **认证设备类型ID** | `5232` (0x1470) |
| **`tag[Context Specific]: 0xa`** | **原始供应商ID (Origin Vendor ID)** | `32774` (0x8006) |
| **`tag[Context Specific]: 0xb`** | **产品外观 (Product Appearance)** | `E9160DC417F7419C95320BBF365671933FF31222` (hex) |

```c
./chip-cert print-cd ./cd-0x149A-0x3005-0x1470-0x8006.der
SignerKeyId value: hex:62FA823359ACFAA9963E1CFA140ADDF504F37160
0x01, tag[Anonymous]: 0x100, type: Structure (0x15), container:
0x04,     tag[Context Specific]: 0x0, type: Unsigned Fixed Point (0x04), value: 1
0x08,     tag[Context Specific]: 0x1, type: Unsigned Fixed Point (0x04), value: 5274
0x0A,     tag[Context Specific]: 0x2, type: Array (0x16), container:
0x0D,         tag[Anonymous]: 0x100, type: Unsigned Fixed Point (0x04), value: 12293
0x12,     tag[Context Specific]: 0x3, type: Unsigned Fixed Point (0x04), value: 514
0x15,     tag[Context Specific]: 0x4, type: UTF-8 String (0x0c), length: 19, value: "ZIG20142ZB330003-24"
0x2B,     tag[Context Specific]: 0x5, type: Unsigned Fixed Point (0x04), value: 0
0x2E,     tag[Context Specific]: 0x6, type: Unsigned Fixed Point (0x04), value: 0
0x32,     tag[Context Specific]: 0x7, type: Unsigned Fixed Point (0x04), value: 599
0x35,     tag[Context Specific]: 0x8, type: Unsigned Fixed Point (0x04), value: 1
0x39,     tag[Context Specific]: 0x9, type: Unsigned Fixed Point (0x04), value: 5232
0x3D,     tag[Context Specific]: 0xa, type: Unsigned Fixed Point (0x04), value: 32774
```

| TLV 项 | 字段含义 | 解析出的值 |
| :--- | :--- | :--- |
| **`tag[Anonymous]: 0x100`** | **结构体版本** | `1` |
| **`tag[Context Specific]: 0x1`** | **供应商ID (Vendor ID)** | `5274` (0x149A) |
| **`tag[Context Specific]: 0x2`** | **产品ID (Product ID)** | `12293` (0x3005) |
| **`tag[Context Specific]: 0x3`** | **设备类型ID (Device Type ID)** | `514` (0x202) |
| **`tag[Context Specific]: 0x4`** | **认证ID (Certification ID)** | `"ZIG20142ZB330003-24"` |
| **`tag[Context Specific]: 0x5`** | **安全策略 (Security Policy)** | `0` |
| **`tag[Context Specific]: 0x6`** | **RCD 版本号** | `0` |
| **`tag[Context Specific]: 0x7`** | **设备特征版本号** | `599` |
| **`tag[Context Specific]: 0x8`** | **认证类型 (Certification Type)** | `1` (设备认证) |
| **`tag[Context Specific]: 0x9`** | **认证设备类型ID** | `5232` (0x1470) |
| **`tag[Context Specific]: 0xa`** | **原始供应商ID (Origin Vendor ID)** | `32774` (0x8006) |
| **`SignerKeyId value`** | **签名者密钥标识符** | `62FA823359...` |
