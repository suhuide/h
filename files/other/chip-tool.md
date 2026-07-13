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
ubuntu@ubuntu:~$ sudo ./chip-tool payload parse-setup-payload MT:K2CA0Q1814EZX083N00
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
sudo ./chip-tool onoff on 2250 3
sudo ./chip-tool onoff off 2250 3
sudo ./chip-tool levelcontrol move-to-level 128 0 0 0 2250 3
sudo ./chip-tool levelcontrol read min-level 2250 3
sudo ./chip-tool levelcontrol read max-level 2250 3
sudo ./chip-tool levelcontrol read current-level 2250 3
sudo ./chip-tool levelcontrol read all 2250 3
sudo ./chip-tool onoff read on-off 2250 6
sudo ./chip-tool onoff read start-up-on-off 2250 6
sudo ./chip-tool onoff write start-up-on-off 0 2250 6


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
# CD
```c
ubuntu@ubuntu:~$ sudo chmod +x chip-cert
ubuntu@ubuntu:~$ ./chip-cert print-cd ./csa25d65mat4831124.der
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
ubuntu@ubuntu:~$ ./chip-cert print-cd ./cd-0x149A-0x3005-0x1470-0x8006.der
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

## XY color control
🔵 蓝色	
```c
sudo ./chip-tool colorcontrol move-to-color 9831 3932 0 0 0 2250 3
```
🔴 红色	
```c
sudo ./chip-tool colorcontrol move-to-color 41947 21624 0 0 0 2250 3
```
🟢 绿色	
```c
sudo ./chip-tool colorcontrol move-to-color 0 19660 39320 0 0 2250 3
```
🟣 紫色	
```c
sudo ./chip-tool colorcontrol move-to-color 20971 9830 0 0 0 2250 3
```

```c
sudo ./chip-tool colorcontrol move-to-color <colorX> <colorY> <transitionTime> <optionsMask> <optionsOverride> <nodeId> <endpointId>
<colorX> <colorY>：XY 色坐标值（0–65535）

<transitionTime>：渐变秒数，0 瞬切

<optionsMask> <optionsOverride>：固定填 0

<nodeId>：2250（放在 endpoint 前面）

<endpointId>：3
```
### Read
```c
sudo ./chip-tool colorcontrol read color-mode 2250 3
sudo ./chip-tool colorcontrol read current-x 2250 3
sudo ./chip-tool colorcontrol read current-y 2250 3
```

## HSV color control
🔵 蓝色	
```c
sudo ./chip-tool colorcontrol move-to-hue 170 0 0 0 0 2250 3
```
🔴 红色	
```c
sudo ./chip-tool colorcontrol move-to-hue 0 0 0 0 0 2250 3
```
🟢 绿色	
```c
sudo ./chip-tool colorcontrol move-to-hue 85 0 0 0 0 2250 3
```
🟣 紫色	
```c
//Hue 模式下，紫色 ≈ 270°，对应 Hue 值 254 * 270/360 ≈ 191
sudo ./chip-tool colorcontrol move-to-hue 191 0 0 0 0 2250 3
```

Chip-Tool 测试指令
以下指令中 <node-id> 替换为实际入网后的节点 ID（例如 1），<endpoint> 替换为灯的端点号（例如 1）。

1. XY 模式 — 下发测试（Matter → MCU）
设置紫色 (RGB: 255, 0, 255)，用 XY 色坐标下发：


# 紫色 XY 坐标: x≈0.32, y≈0.15
# CurrentX = 0.32 * 65535 ≈ 21000
# CurrentY = 0.15 * 65535 ≈  9830
sudo ./chip-tool colorcontrol move-to-color <node-id> <endpoint> 21000 9830 10 0 0
此指令会：

触发 ColorControlAttributeChangedEventHandler → CurrentX/CurrentY case
调用 ConvertColor2RGB() 读取 XY → 转换 RGB → 通过串口 fLightColor 下发 MCU
验证点：MCU 端灯光应变紫色，串口日志应显示 Attr XY changed 及对应的 RGB 值。

2. HSV 模式 — 下发测试（Matter → MCU）
设置紫色 (H≈300°，映射到 Matter H≈212)：


# Hue 0-254: 300/360 * 254 ≈ 212
# Saturation: 254 (100%)
sudo ./chip-tool colorcontrol move-to-hue-and-saturation <node-id> <endpoint> 212 254 10 0 0
验证点：串口日志应显示 Attr CurrentHue 和 Attr CurrentSaturation，MCU 收到 RGB 转换后的 fLightColor。

3. XY 模式 — 上报验证（MCU → Matter）
MCU 上报颜色后，用以下指令读取 Matter 端属性确认 XY 值已更新：


# 读取 CurrentX
sudo ./chip-tool colorcontrol read current-x <node-id> <endpoint>

# 读取 CurrentY
sudo ./chip-tool colorcontrol read current-y <node-id> <endpoint>

# 读取 ColorMode，确认为 XY 模式 (1 = kCurrentXAndCurrentY)
sudo ./chip-tool colorcontrol read color-mode <node-id> <endpoint>
4. HSV 模式 — 上报验证（MCU → Matter）

# 读取 CurrentHue
sudo ./chip-tool colorcontrol read current-hue <node-id> <endpoint>

# 读取 CurrentSaturation
sudo ./chip-tool colorcontrol read current-saturation <node-id> <endpoint>

# 读取 CurrentLevel (亮度)
sudo ./chip-tool levelcontrol read current-level <node-id> <endpoint>
5. 完整测试流程

# ==== 第一步：测试 XY 下发 ====
# 设为红色 (XY: x≈0.64, y≈0.33)
sudo ./chip-tool colorcontrol move-to-color <node-id> <endpoint> 41942 21626 10 0 0
# 确认 MCU 收到，读取回来验证
sudo ./chip-tool colorcontrol read current-x <node-id> <endpoint>
sudo ./chip-tool colorcontrol read current-y <node-id> <endpoint>

# ==== 第二步：测试 XY→HSV 上报 ====
# 通过 MCU 物理改变颜色（如按键），然后读取 HSV 属性
sudo ./chip-tool colorcontrol read current-hue <node-id> <endpoint>
sudo ./chip-tool colorcontrol read current-saturation <node-id> <endpoint>
# ★ 重点验证：MCU 上报后 CurrentX/CurrentY 是否也同步更新了（之前的 bug）
sudo ./chip-tool colorcontrol read current-x <node-id> <endpoint>
sudo ./chip-tool colorcontrol read current-y <node-id> <endpoint>

# ==== 第三步：测试 HSV 下发 ====
# 设为蓝色 (H≈170/360*254≈120, S=254)
sudo ./chip-tool colorcontrol move-to-hue-and-saturation <node-id> <endpoint> 120 254 10 0 0

# ==== 第四步：测试 HSV→XY 上报 ====
# 再次通过 MCU 改变颜色，验证 XY 也同步
sudo ./chip-tool colorcontrol read current-x <node-id> <endpoint>
sudo ./chip-tool colorcontrol read current-y <node-id> <endpoint>
sudo ./chip-tool colorcontrol read color-mode <node-id> <endpoint>
常用颜色参考值
颜色	RGB	CurrentX (0-65535)	CurrentY (0-65535)	CurrentHue (0-254)	CurrentSaturation
红	(255,0,0)	41942	21626	0	254
绿	(0,255,0)	19660	46660	85	254
蓝	(0,0,255)	11796	3958	170	254
紫	(255,0,255)	20971	9830	212	254
黄	(255,255,0)	31480	37350	43	254
白	(255,255,255)	20468	21156	0	0
关键验证点总结
#	测试项	下发指令	读取验证
1	XY 下发→MCU	move-to-color	观察串口 Attr XY changed 日志
2	HSV 下发→MCU	move-to-hue-and-saturation	观察串口 Attr CurrentHue 日志
3	MCU上报→XY属性	MCU本地变色	read current-x/y （修复重点）
4	MCU上报→HSV属性	MCU本地变色	read current-hue/saturation
5	Level变化→XY转换	move-to-level	read current-x/y（验证 ConvertColor2RGB 对XY模式的处理）
特别注意第3项：这是本次修复的核心验证点——MCU 上报 RGB 后，CurrentX/CurrentY 是否真的被更新了。修复前只更新 HSV，XY 属性会保持旧值不变。


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