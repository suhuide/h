# 串口下发 PID → 更新 Basic Info + 重新生成二维码（实施总结）

> 产品: aok02_matter_ac（EFR32MG24） ｜ 状态: **已实施并通过编译**（2026-08-25）

## 一、背景：PID 的存储与消费点

- 编译期宏 `CHIP_DEVICE_CONFIG_DEVICE_PRODUCT_ID = 0x8010`（`include/CHIPProjectConfig.h`）只是**回退默认值**。
- 运行时 PID 经 `Provision::Manager::GetInstance().GetStorage().GetProductId()` 读取（NVM3 工厂区 key `kConfigKey_ProductId`）。
- PID 消费点（**实时读取，无 RAM 缓存问题**）：
  - Basic Info 集群 `ProductID(0x0004)` → 写 NVM3 后自动更新
  - CHIPoBLE 配网广播中的 PID → 自动更新
- 二维码 base38 由**闭源库** `libProvision_efr32mg24.a` 的 `GetSetupPayload()` 生成；passcode 明文不存（只有 SPAKE2+ verifier），原始 11 字节 setup payload bit-set 存于工厂区。

## 二、关键发现：二维码不随 PID 变化（推翻最初反汇编结论）

最初通过反汇编推断"闭源 getter 实时读 PID，写 NVM3 后二维码自动变"。**实测推翻**：两个不同 PID 写 NVM3 后，闭源库打出的 base38 完全一样（`MT:MNKA1C8F153FUC7-Z10` 不变）。

真实机制：闭源库 `GetSetupPayload` 使用**内部缓存的 setup payload bitset**（工厂烧录时固化，含旧 PID），写 PID 不会刷新该缓存。且 RAM 成员 `mProductId` 同样无法从外部直接写（`Set` 为 private override）。

**解决方案**：应用层用 SDK 生成器自行重建二维码——从闭源库的旧二维码中解析出 passcode/discriminator 等不可直读字段，覆盖 PID 后重新编码（见 §3.2）。

## 三、实施改动

### 3.1 接收与更新 PID

**文件**: `common/app/app_spm_mgr.cpp`（`case kGetProductInfo`，新增 `#include "AppTask.h"`）

```cpp
case kGetProductInfo:
{
    LOG_MSG_INFO(TAG_COM, "MCU Respond Product Info");
    if (payload_size >= 2) {
        uint16_t pid = SPProtocol::get_uint16_from_network(payload); // 大端
        LOG_MSG_INFO(TAG_COM, "MCU Product ID: 0x%04X", (unsigned int) pid);
        app_task_update_pid(pid);
    }
    break;
}
```

**文件**: `common/app/AppTask.h` — 新增声明：

```cpp
void app_task_update_pid(uint16_t pid);
bool app_task_is_pid_updated(void);
```

**文件**: `common/app/AppTask.cpp` — `app_task_update_pid()`：

```cpp
static bool g_pid_updated = false;

bool app_task_is_pid_updated(void) { return g_pid_updated; }

void app_task_update_pid(uint16_t pid)
{
    g_pid_updated = true;          // 收到过 PID 应答（供查询重试判断）

    uint16_t cur_pid = 0;
    CHIP_ERROR err = Provision::Manager::GetInstance().GetStorage().GetProductId(cur_pid);
    if (err == CHIP_NO_ERROR && cur_pid == pid) {
        _print_qrcode();           // PID 未变：只重打二维码，避免无谓写 flash
        return;
    }

    LOG_MSG_INFO(TAG_COM, "Update PID: 0x%04X -> 0x%04X", (unsigned int) cur_pid, (unsigned int) pid);

    // 经 GenericStorage::Set 写 Provision 存储（Basic Info / BLE 广播实时读此处）
    // Set() 在 Storage 里是 private override，通过 GenericStorage 基类引用可访问
    Provision::GenericStorage & store = Provision::Manager::GetInstance().GetStorage();
    store.Set(Provision::Parameters::kProductId, &pid);

    _print_qrcode();               // 串口输出新二维码
}
```

### 3.2 二维码重建（核心修复）

**文件**: `common/app/AppTask.cpp` — 新增 `_generate_setup_payload_with_current_pid()`，`_print_qrcode()` 与 `app_task_read_qrcode()` 均改走它：

```cpp
static CHIP_ERROR _generate_setup_payload_with_current_pid(chip::MutableCharSpan & out)
{
    // ① 取闭源库当前二维码（含 passcode/discriminator 等不可直读字段）
    char oldBuffer[chip::QRCodeBasicSetupPayloadGenerator::kMaxQRCodeBase38RepresentationLength + 1];
    chip::MutableCharSpan oldPayload(oldBuffer);
    CHIP_ERROR err = Provision::Manager::GetInstance().GetStorage().GetSetupPayload(oldPayload);
    if (err != CHIP_NO_ERROR) return err;

    // ② base38 → SetupPayload 结构
    SetupPayload payload;
    err = QRCodeSetupPayloadParser(std::string(oldPayload.data())).populatePayload(payload);
    if (err != CHIP_NO_ERROR) return err;

    // ③ 覆盖为当前实时 PID（GetProductId 实时读 NVM3，实测可靠）
    uint16_t pid = 0;
    err = Provision::Manager::GetInstance().GetStorage().GetProductId(pid);
    if (err != CHIP_NO_ERROR) return err;
    payload.productID = pid;

    // ④ SDK 生成器重新编码
    return QRCodeBasicSetupPayloadGenerator(payload).payloadBase38Representation(out);
}
```

新增 include：`<setup_payload/QRCodeSetupPayloadParser.h>`。

消费点覆盖：

| 消费点 | 位置 | 效果 |
|---|---|---|
| 上电打印 | `_print_qrcode()` | 打印当前 PID 的二维码 |
| PID 更新后重打 | `app_task_update_pid()` 末尾 | 新 PID 二维码 |
| 手机 App 客户定制 BLE 取码 | `app_task_read_qrcode()` | 返回新 PID 二维码 |

### 3.3 查询时机与重试

**文件**: `common/app/app_comm_mgr.h` — 新增 `void app_comm_mgr_query_product_info(void);`

**文件**: `common/app/app_comm_mgr.cpp`：

```cpp
#define PRODUCT_QUERY_RETRY_MAX 3            /* 无应答时的最大重试次数 */
#define PRODUCT_QUERY_RETRY_INTERVAL_MS 500  /* 重试间隔（半秒） */

void app_comm_mgr_query_product_info(void)
{
    if (app_task_is_pid_updated()) return;   // 已收到过 PID，不再打扰 MCU
    s_product_query_retry_count = 0;
    spp_instance.send_cmd(kGetProductInfo, NULL, 0);
    ev_set_delay_ms(&product_query_event, PRODUCT_QUERY_RETRY_INTERVAL_MS);
}

static void _product_query_event_handler(app_event_t * ev)
{
    if (app_task_is_pid_updated()) return;   // 已收到 → 停止
    if (s_product_query_retry_count < PRODUCT_QUERY_RETRY_MAX) {
        s_product_query_retry_count++;
        LOG_MSG_INFO(TAG_COM, "query product info retry %u", s_product_query_retry_count);
        spp_instance.send_cmd(kGetProductInfo, NULL, 0);
        ev_set_delay_ms(&product_query_event, PRODUCT_QUERY_RETRY_INTERVAL_MS);
    } else {
        LOG_MSG_ERR(TAG_COM, "query product info failed after %u retries", PRODUCT_QUERY_RETRY_MAX);
    }
}
```

**两个触发点**：

1. `app_comm_mgr_start()`（UART 初始化完成即发，**不依赖 dev_info**）：
```cpp
    comm_state = COMM_STATE_INIT;
    ev_set_delay_ms(&query_device_event, 0);
    app_comm_mgr_query_product_info();   // ← UART ready 后第一时间查询
```
2. `app_spm_mgr.cpp` 的 `dev_info_report_process()`（`g_dev_status = true` 之后补查，带守卫；覆盖 MCU 慢启动、首轮查询失败后 dev_info 才到的场景）：
```cpp
    g_dev_status = true;
    app_comm_mgr_query_product_info();
```

**原架构不受影响**：`_query_device_event_handler` 已恢复为原始的每 2 秒发 `fDevTypeInfo` 查询 dev_info 的逻辑。

### 3.4 未改动/回退项

- SDK `BaseApplication.cpp` 的 `OutputQrCode(true)`：**未屏蔽**（保留上电打印）
- `AppInit()` 里的 `_print_qrcode()`：**未屏蔽**（保留上电打印；反正 `_generate_setup_payload_with_current_pid` 已保证打印的是当前 NVM3 PID）

## 四、数据流与时序

```
上电
 ├─ UART ready（app_comm_mgr_start）
 │    ├─ notify Leave（原逻辑）
 │    ├─ fDevTypeInfo 每 2s 循环查询 dev_info（原架构不变）
 │    └─ 立即发 kGetProductInfo ──┐
 ├─ MCU 回 dev_info              │
 │    └─ g_dev_status=true        │
 │         └─ 补查 kGetProductInfo（已收到 PID 则跳过）
 └─ MCU 回 PID ───────────────────┘
      └─ app_task_update_pid(pid)
           ├─ g_pid_updated = true
           ├─ PID 未变 → 仅重打二维码
           └─ PID 变化 → GenericStorage::Set(kProductId)（Basic Info/BLE 自动更新）
                        → _generate_setup_payload_with_current_pid()
                          （旧二维码解析 → 覆盖 PID → SDK 生成器重编码）
                        → 打印新二维码
无应答：500ms 间隔重试 ×3 → 仍无应答则停止（等 dev_info 到达再补查）
```

## 五、需与 MCU 端确认

- `kGetProductInfo` 响应 payload 格式：当前按**纯 2 字节大端 PID** 解析（`SPProtocol::get_uint16_from_network`）。若带长度/类型头，在 `case kGetProductInfo` 调整偏移即可。

## 六、验证清单

1. 正常场景：UART ready 后日志立即出现 kGetProductInfo 帧 → `MCU Product ID: 0xXXXX` → （PID 变化时）`Update PID: 旧 -> 新` → `SetupQRCode: [MT:...]` 的 base38 变化
2. base38 解码校验：PID=新值、VID/passcode/discriminator 不变
3. chip-tool 读 Basic Info `ProductID(0x0004)` = 新值
4. 手机 App 客户定制 BLE 取二维码 → 新 PID
5. MCU 静默场景：`query product info retry 1/2/3`（间隔 500ms）→ `query product info failed after 3 retries`
6. 断电重启：PID 从 NVM3 恢复、二维码仍为新 PID（MCU 每次上电再下发，幂等）

## 七、遗留注意事项

- Provision 闭源库的二维码缓存不随 PID 更新，**所有二维码出口必须走 `_generate_setup_payload_with_current_pid`**，不要再直接使用 `GetSetupPayload()` 的返回值对外输出。
- 若将来 SDK 升级或 provision 库更新，需回归验证二维码行为。


<div align="center">
  <img src="pid.png" width="1080">
</div>

```c
[09:06:12.263]  [00:00:00.088][info  ][DL] Starting scheduler
[09:06:12.263]  [00:00:00.088][info  ][DL] ==================================================
[09:06:12.264]  [00:00:00.088][info  ][DL]  starting
[09:06:12.264]  [00:00:00.088][info  ][DL] ==================================================
[09:06:12.266]  [00:00:00.088][info  ][DL] Init CHIP Stack
[09:06:12.266]  [00:00:00.090][info  ][DL] Provision mode disabled
[09:06:12.266]  [00:00:00.090][info  ][DL] Initializing OpenThread stack
[09:06:12.267]  [00:00:00.090][info  ][DL] OpenThread started: OK
[09:06:12.267]  [00:00:00.091][info  ][DL] Setting OpenThread device type to ROUTER
[09:06:12.275]  [00:00:00.154][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[09:06:12.275]  [00:00:00.154][info  ][DL] RAIL version:, v3.0.3-b0
[09:06:12.275]  [00:00:00.154][silabs ]BLE: Verify 'ret == CONFIG_STATUS_OK' failed
[09:06:12.277]  [00:00:00.154][silabs ]BLE: [E: 0x0001] Failed to read product type
[09:06:12.277]  
[09:06:12.277]  [00:00:00.155][silabs ]BLE: product type [A-OK]
[09:06:12.296]  [00:00:00.173][silabs ]BLE: identify addr: FE:97:2E:2B:F7:2B type=1
[09:06:12.296]  [00:00:00.174][silabs ]BLE: MTU size 249
[09:06:12.296]  [00:00:00.174][detail][DL] CHIP event task running
[09:06:12.297]  [00:00:00.175][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[09:06:12.297]  [00:00:00.176][detail][DL] OpenThread State Changed (Flags: 0x00038210)
[09:06:12.299]  [00:00:00.176][detail][DL]    Network Name: OpenThread
[09:06:12.299]  [00:00:00.176][detail][DL]    PAN Id: 0xFFFF
[09:06:12.300]  [00:00:00.176][detail][DL]    Extended PAN Id: 0xDEAD00BEEF00CAFE
[09:06:12.300]  [00:00:00.176][detail][DL]    Channel: 11
[09:06:12.301]  [00:00:00.177][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64
[09:06:12.301]  
[09:06:12.301]  Missed Logs: 2
[09:06:12.301]  [00:00:00.177][info  ][SVR] Current Software Version String: 1.0.0
[09:06:12.302]  
[09:06:12.302]  Missed Logs: 2
[09:06:12.302]  [00:00:00.177][info  ][SVR] Current Software Version: 10000
[09:06:12.302]  [00:00:00.177][info  ][DL] Device Configuration:
[09:06:12.304]  [00:00:00.178][info  ][DL]   Serial Number: 757BCD44FC429F5F
[09:06:12.304]  [00:00:00.178][info  ][DL]   Vendor Id: 5274 (0x149A)
[09:06:12.305]  [00:00:00.178][info  ][DL]   Product Id: 12293 (0x3005)
[09:06:12.305]  [00:00:00.179][info  ][DL]   Product Name: Window Covering
[09:06:12.308]  [00:00:00.179][info  ][DL]   Hardware Version: 1
[09:06:12.308]  [00:00:00.179][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[09:06:12.309]  [00:00:00.179][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 2093 (0x82D)
[09:06:12.309]  [00:00:00.180][info  ][SVR] SetupQRCode: [MT:MNKA1C8F153FUC7-Z10]
[09:06:12.312]  matterCli> [00:00:00.186][silabs ]CTM: Ver: 10000 Build:  # Time:Aug 24 2026 17:50:31
[09:06:12.316]  [00:00:00.191][silabs ]CTM: Btl Ver: core: v3.0 user: v3
[09:06:12.321]  [00:00:00.196][silabs ] Reset Reason: 0x00000000
[09:06:12.326]  [00:00:00.201][silabs ] Tx power 10dBm
[09:06:12.327]  [00:00:00.206][silabs ]SetupQRCode: [MT:MNKA1C8F153FUC7-Z10]
[09:06:12.327]  [00:00:00.207][info  ][DL] Configuring BLE Channel
[09:06:12.327]  [00:00:00.207][detail][DL] BLE Static Device Address F8:28:A9:A8:FD:6C
[09:06:12.330]  [00:00:00.208][silabs ]BLE: _create_second_adv, adv Handle = 0, interval 320/400 (units of 0.625ms)
[09:06:12.331]  [00:00:00.208][silabs ]BLE: advertiser start without white list
[09:06:12.331]  [00:00:00.209][silabs ]COM: Init done
[09:06:12.333]  [00:00:00.209][silabs ]NWK: open basic commissioning window time 300 sec
[09:06:12.333]  [00:00:00.211][detail][IN] SecureSession[0x20007be8]: Allocated Type:1 LSID:36686
[09:06:12.334]  [00:00:00.211][detail][SC] Assigned local session key ID 36686
[09:06:12.334]  [00:00:00.211][detail][SC] Waiting for PBKDF param request
[09:06:12.335]  [00:00:00.211][info  ][DIS] Updating services using commissioning mode 1
[09:06:12.335]  [00:00:00.211][error ][DIS] Failed to remove advertised services: 3
[09:06:12.337]  [00:00:00.212][detail][DL] Using Thread extended MAC for hostname.
[09:06:12.337]  [00:00:00.212][detail][DIS] DNS-SD Pairing Instruction not set
[09:06:12.338]  [00:00:00.212][info  ][DIS] Advertise commission parameter vendorID=5274 productID=12293 discriminator=2093/08 cm=1 cp=0 jf=0
[09:06:12.339]  [00:00:00.213][error ][DIS] Failed to advertise commissionable node: 3
[09:06:12.339]  [00:00:00.213][error ][DIS] Failed to finalize service update: 3
[09:06:12.341]  [00:00:00.213][detail][DL] Start BLE advertisement
[09:06:12.341]  [00:00:00.214][info  ][DL] BLE Static Device Address EA:49:0C:D9:EA:B6
[09:06:12.342]  [00:00:00.214][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[09:06:12.343]  [00:00:00.215][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[09:06:12.343]  [00:00:00.216][silabs ]NWK: platform event type 800d
```
```c
[10:01:33.670]  [00:00:40.470][silabs ] MATTER RX: : 55 aa 02 00 27 01 00 02 30 25 80 
[10:01:33.670]  [00:00:40.470][silabs ]COM: MCU Respond Product Info
[10:01:33.670]  [00:00:40.470][silabs ]COM: MCU Product ID: 0x3025
[10:01:33.672]  [00:00:40.471][silabs ]COM: Update PID: 0x3005 -> 0x3025
[10:01:33.672]  [00:00:40.472][silabs ]SetupQRCode: [MT:MNKA1D8F153FUC7-Z10]
```
```c
[12:04:31.374]  [00:00:00.091][info  ][DL] Starting scheduler
[12:04:31.374]  [00:00:00.091][info  ][DL] ==================================================
[12:04:31.375]  [00:00:00.092][info  ][DL]  starting
[12:04:31.375]  [00:00:00.092][info  ][DL] ==================================================
[12:04:31.376]  [00:00:00.092][info  ][DL] Init CHIP Stack
[12:04:31.376]  [00:00:00.093][info  ][DL] Provision mode disabled
[12:04:31.376]  [00:00:00.093][info  ][DL] Initializing OpenThread stack
[12:04:31.377]  [00:00:00.095][info  ][DL] OpenThread ifconfig up and thread start
[12:04:31.377]  [00:00:00.095][info  ][DL] OpenThread started: OK
[12:04:31.385]  [00:00:00.198][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[12:04:31.385]  [00:00:00.198][info  ][DL] RAIL version:, v3.0.3-b0
[12:04:31.385]  [00:00:00.198][silabs ]BLE: Verify 'ret == CONFIG_STATUS_OK' failed
[12:04:31.387]  [00:00:00.198][silabs ]BLE: [E: 0x0001] Failed to read product type
[12:04:31.387]  
[12:04:31.387]  [00:00:00.199][silabs ]BLE: product type [A-OK]
[12:04:31.406]  [00:00:00.217][silabs ]BLE: identify addr: E5:13:DB:0E:18:14 type=1
[12:04:31.406]  [00:00:00.218][silabs ]BLE: MTU size 249
[12:04:31.406]  [00:00:00.218][detail][DL] CHIP event task running
[12:04:31.407]  [00:00:00.219][info  ][SVR] Current Software Version String: 1.0.0
[12:04:31.407]  [00:00:00.220][info  ][SVR] Current Software Version: 10000
[12:04:31.409]  [00:00:00.220][info  ][DL] Device Configuration:
[12:04:31.409]  [00:00:00.220][info  ][DL]   Serial Number: 757BCD44FC429F5F
[12:04:31.410]  [00:00:00.221][info  ][DL]   Vendor Id: 5274 (0x149A)
[12:04:31.410]  [00:00:00.221][info  ][DL]   Product Id: 12325 (0x3025)
[12:04:31.412]  [00:00:00.222][info  ][DL]   Product Name: Window Covering
[12:04:31.412]  [00:00:00.222][info  ][DL]   Hardware Version: 1
[12:04:31.412]  [00:00:00.223][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[12:04:31.413]  [00:00:00.223][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 2093 (0x82D)
[12:04:31.414]  [00:00:00.224][info  ][DL]   Manufacturing Date: 2026-08-21
[12:04:31.414]  [00:00:00.224][info  ][DL]   Device Type: 65535 (0xFFFF)
[12:04:31.416]  [00:00:00.225][info  ][SVR] SetupQRCode: [MT:MNKA1C8F153FUC7-Z10]
[12:04:31.416]  [00:00:00.225][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[12:04:31.417]  [00:00:00.225][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AMNKA1C8F153FUC7-Z10
[12:04:31.418]  [00:00:00.230][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[12:04:31.418]  [00:00:00.230][detail][DL] OpenThread State Changed (Flags: 0x111fd33d)
[12:04:31.421]  [00:00:00.230][detail][DL]    Device Role: DETACHED
[12:04:31.421]  [00:00:00.230][detail][DL]    Network Name: OpenThread-225f
[12:04:31.422]  [00:00:00.230][detail][DL]    PAN Id: 0x225F
[12:04:31.422]  [00:00:00.231][detail][DL]    Extended PAN Id: 0xD66AA42E602782D7
[12:04:31.423]  [00:00:00.231][detail][DL]    Channel: 15
[12:04:31.423]  [00:00:00.231][detail][DL]    Mesh Prefix: fd11:9c64:dd37:b8c4:0:0:0:0/64
[12:04:31.425]  [00:00:00.231][detail][DL]    Thread Unicast Addresses:
[12:04:31.425]  [00:00:00.232][detail][DL]         fd11:9c64:dd37:b8c4:0:ff:fe00:5400/64 valid preferred rloc
[12:04:31.425]  [00:00:00.232][detail][DL]         fd11:9c64:dd37:b8c4:72fd:58d7:77fb:bc4d/64 valid preferred
[12:04:31.425]  [00:00:00.232][detail][DL]         fe80:0:0:0:4803:53b5:c197:b056/64 valid preferred
[12:04:31.427]  matterCli> [00:00:00.240][silabs ]CTM: Ver: 10000 Build:  # Time:Aug 25 2026 12:01:42
[12:04:31.434]  [00:00:00.245][silabs ]CTM: Btl Ver: core: v3.0 user: v3
[12:04:31.439]  [00:00:00.250][silabs ] Reset Reason: 0x00000000
[12:04:31.444]  [00:00:00.254][silabs ] Tx power 10dBm
[12:04:31.448]  [00:00:00.259][silabs ]SetupQRCode: [MT:MNKA1D8F153FUC7-Z10]
[12:04:31.448]  [00:00:00.260][info  ][DL] Configuring BLE Channel
[12:04:31.448]  [00:00:00.261][detail][DL] BLE Static Device Address DE:34:25:19:F0:CD
[12:04:31.450]  [00:00:00.261][silabs ]BLE: _create_second_adv, adv Handle = 0, interval 320/400 (units of 0.625ms)
[12:04:31.452]  [00:00:00.261][silabs ]BLE: advertiser start without white list
[12:04:31.452]  [00:00:00.263][silabs ]COM: Init done
```
```c
[12:04:32.108]  [00:08:41.931][silabs ] MATTER RX: : 55 aa 02 00 27 01 00 02 30 05 60 
[12:04:32.108]  [00:08:41.931][silabs ]COM: MCU Respond Product Info
[12:04:32.108]  [00:08:41.931][silabs ]COM: MCU Product ID: 0x3005
[12:04:32.110]  [00:08:41.931][silabs ]COM: Update PID: 0x3025 -> 0x3005
[12:04:32.110]  [00:08:41.932][silabs ]SetupQRCode: [MT:MNKA1C8F153FUC7-Z10]
```