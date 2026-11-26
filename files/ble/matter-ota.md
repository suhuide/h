# Matter 设备 BLE OTA（DFU over BLE）实现总结

> 项目：`C:\Si\v6\aok02_matter_ota`（EFR32MG24A410F1536，SiSDK 2025.12.3 + Matter 扩展 2.8.1）
> 状态：**已全链路验证成功**（658KB 签名+加密 GBL，verify OK → 安装 → 0.0.1→0.0.2）

---

## 1. 架构与结论

- **只走 side-channel BLE**（custom_adv），不占用 chip BLE（Matter 配网通道）——用户实测结论：OTA 服务放 chip BLE 侧会出问题，side-channel 独立可控。
- **手写接收端**（`app_ble_ota_mgr`），不使用 SiSDK 官方 `app_ota_dfu` 组件（其 boot 期 RTA 任务触发 `bootloader_init()` 导致挂死，已回退该方案）。
- GATT 服务用 **Silabs OTA UUID**（`1D14D6EE-FD63-4FA1-BFA4-8F47B42119F0`），Simplicity Connect/EFR Connect 开箱即用；接收代码按 gattdb 句柄匹配，与 UUID 无关。
- **单击完成**：BEGIN 的 write-with-response 挂起，整槽擦除（~1.3s）完成后才回 OK，SC 收到后才推流（ATT 事务超时 30s >> 擦除 1.34s）。
- **写入按 SPI flash 页大小 256B 切分**：bootloader 页编程跨页会回绕覆盖页首（见 §4 问题 3）。
- **校验分片跑 CHIP event task**（`PlatformMgr().ScheduleWork` 链式自排步进，与 Matter OTA 的 verify 同任务）：`initVerifyImage` + 每步 `continueVerifyImage`，串行化 SE 访问且系统不被冻结。
- **门禁**：只接受 side-channel(custom_adv) 连接；chip BLE 连接写 OTA 特征一律 ATT 0x80 拒绝。
- **安全边界**：bootloader 强制 GBL 签名+加密+secure boot——假镜像 verify 失败不安装、不变砖。
- 全部改动由 **`D_BLE_DFU` 宏门控**（SDK 零改动；宏未定义的工程编译结果不变）。
- 配套 bootloader 要求：**aok 系 SPI 存储型（v3.2.x / user v4）**。内部 flash 型 bootloader（v3.0/u3）不兼容，代码会主动拒绝（见 §4 问题 8）。

---

## 2. 移植清单

### 2.1 新增文件

**`common/app/app_ble_ota_mgr.h` + `common/app/app_ble_ota_mgr.cpp`** — OTA 接收端模块，整文件 `#if defined(D_BLE_DFU)` 包裹（未定义宏时为空 TU，其他工程零影响）。

对外接口：
```c
void app_ble_ota_mgr_init(void);                                  // 初始化事件（app_ble_mgr_init 里调用）
void app_ble_ota_mgr_set_connection(uint8_t connection);          // 标记 side-channel 连接
void app_ble_ota_mgr_on_connection_closed(uint8_t connection);    // 断链通知
void app_ble_ota_mgr_on_user_write(volatile sl_bt_msg_t * evt);   // OTA 特征写入分发
```

模块内部要点（移植后不需要改，理解用）：
- 状态机：`IDLE → PREPARING(整槽擦除,应答挂起) → DOWNLOAD(流式写) → WAIT_CLOSE → VERIFY(分片) → 安装重启`；ERROR 可重新 BEGIN。
- **上下文分工（实测教训）**：蓝牙栈任务只做轻活（状态/stage 缓冲/回响应）；擦除在 **AppTask** 事件执行；校验步进在 **CHIP event task**（`PlatformMgr().ScheduleWork` 链）；**所有 bootloader 接口调用必须包 `CORE_CRITICAL_SECTION`**（等同 Matter SDK 的 `WRAP_BL_DFU_CALL`），且校验必须与 Matter/Thread 的 SE 加密使用同任务串行——SE 非线程安全（见 §4 问题 12）。
- **stage 对齐写**：bootloader 存储接口要求长度 4 字节对齐，手机分包任意长 → 1KB stage 缓冲凑齐即写，END 残余补 0。
- **惰性初始化**：`bootloader_init()` 在 BEGIN 时才调（boot 期零 bootloader 访问，规避挂死）。
- 控制字（Silabs OTA 语义）：`0=BEGIN / 3=END(断链后校验+安装) / 4=请求断链`。
- 仅 `opcode == sl_bt_gatt_write_request(0x12)` 回 write response（write_no_response 不回）。
- 校验上下文：静态 `uint32_t ctx[179]`（713B，MG24 SEMAILBOX）。

### 2.2 修改文件

**① include 区**（`#include "app_ble_mgr.h"` 之后）：
```cpp
#if defined(D_BLE_DFU)
#include "app_ble_ota_mgr.h"
#endif
```

**② `app_ble_mgr_init()`**：`ev_init` 之后补 `app_ble_ota_mgr_init();`（同样门控）。

**③ 连接标记**（`ble_manager_gatt_server_connection_opened` 内，`return` 之前）：
```cpp
#if defined(D_BLE_DFU)
    if (advertiser == custom_adv_handle) {
        app_ble_ota_mgr_set_connection(conn_id);
    }
#endif
```

**④ 断链转发**（`ble_manager_gatt_server_connection_closed` 内，LOG 之后）：
```cpp
#if defined(D_BLE_DFU)
    app_ble_ota_mgr_on_connection_closed(conn_evt->connection);
#endif
```

**⑤ 写分发**（`ble_manager_gatt_server_user_write_request_event_callback` 内，`data` 取出后、`app2host` 分支前）：
```cpp
#if defined(D_BLE_DFU)
    if (gattdb_ota_control == data->characteristic || gattdb_ota_data == data->characteristic) {
        app_ble_ota_mgr_on_user_write(evt);   // 响应由模块按 opcode 决定是否回
        return;
    }
#endif
```

**注意**：`common/` 是多项目共享子模块——以上触点全部宏门控，未定义 `D_BLE_DFU` 的兄弟工程编译结果不变。

### 2.3 工程文件（`.slcp`）

- `define:` 块加：
  ```yaml
  - name: D_BLE_DFU
    value: '1'
  ```
- `source:` 列表加：`- path: common/app/app_ble_ota_mgr.cpp`
- **不需要任何新组件**（不要 `app_ota_dfu`、不要 `app_rta`）。依赖的 `bootloader_interface` / `bootloader_interface_s2` / `bootloader_app_properties` 工程原本就有。

### 2.4 GATT 服务（`config/btconf/gatt_configuration.btconf`）

**追加到文件末尾**（必须在文件尾：`app_spm_mgr.cpp` 有 `gattdb_remotectl_rx==39 / tx==42` 句柄静态断言，往前插会移动既有句柄导致编译错）：

```xml
  <!--Silicon Labs OTA (D_BLE_DFU): 手写接收端 common/app/app_ble_ota_mgr.cpp 按 gattdb 句柄匹配，
      只接受 side-channel(custom_adv) 连接发起的 OTA 会话，chip BLE 连接写入被 ATT 拒绝。-->
  <service advertise="false" id="ota" name="Silicon Labs OTA" requirement="mandatory" sourceId="com.silabs.service.ota" type="primary" uuid="1D14D6EE-FD63-4FA1-BFA4-8F47B42119F0">
    <characteristic const="false" id="ota_control" name="Silicon Labs OTA Control" sourceId="com.silabs.characteristic.ota_control" uuid="F7BF3564-FB6D-4E53-88A4-5E37E0326063">
      <value length="1" type="user" variable_length="false"/>
      <properties write="true">
        <write authenticated="false" bonded="false" encrypted="false"/>
      </properties>
    </characteristic>
    <characteristic const="false" id="ota_data" name="Silicon Labs OTA Data" sourceId="com.silabs.characteristic.ota_data" uuid="984227F3-34FC-4045-A5D0-2C581F81A153">
      <value length="1" type="user" variable_length="false"/>
      <properties write="true">
        <write authenticated="false" bonded="false" encrypted="false"/>
        <write_no_response authenticated="false" bonded="false" encrypted="false"/>
      </properties>
    </characteristic>
  </service>
</gatt>
```

说明：`encrypted="false"` 起步（A 产品变体的 SM 配对流程被 `#if 0` 禁用，强制加密会使 A 变体无法 OTA）；要收紧改 `true` 并同时恢复配对流程。安全硬边界 = bootloader 强制 GBL 签名+加密+secure boot。

---

## 3. slcp / 组件 / btconf 变更明细

| 项 | 变更 | 备注 |
|---|---|---|
| `.slcp` → `define:` | `D_BLE_DFU = '1'` | 功能总开关 |
| `.slcp` → `source:` | `common/app/app_ble_ota_mgr.cpp` | 新模块编译单元 |
| `config/btconf/gatt_configuration.btconf` | 文件尾追加 OTA 服务（XML 见 §2.4） | 单一来源，勿在别处重复定义 |
| `autogen/gatt_db.h` | 出现 `gattdb_ota / gattdb_ota_control / gattdb_ota_data` | slc generate 产物，作编译验证点 |
| `AppTask.cpp` 的 `bootloader_deinit()` | **保持不动** | 惰性 init 设计下 13µA 省电仍有效 |

---

## 4. 调试问题记录（现象 → 根因 → 解决）

### 问题 1：boot 挂死
- **现象**：装上官方 `app_ota_dfu` 组件后，boot 卡死在早期，版本日志都不打。
- **根因**：组件的 RTA 任务在 boot 期即 `bootloader_init()` 访问 SPI flash，与 Matter 启动并发冲突；栈加大无效。
- **解决**：移除该组件，改为**手写接收端 + 惰性 init**（BEGIN 才碰 bootloader），boot 期零 bootloader 访问。教训：**不要在 boot 期做任何 bootloader 存储访问**。

### 问题 2：SYSREQ 软复位（ResetCause 0x40，SYSREQ=1）★核心教训
- **现象**：裸调 `bootloader_init()` 等接口，设备立刻软复位（~0.04s 级，非看门狗——周期 128s；非 LOCKUP）。
- **根因**：**Series 2 的 bootloader 接口不是中断/任务安全的**。Matter SDK 的 `WRAP_BL_DFU_CALL`（OTAImageProcessorImpl.cpp:39）在 Series 2 上就是 `CORE_CRITICAL_SECTION(code;)`——官方所有调用都关中断执行；Series 3 才裸调。
- **解决**：本项目全部 bootloader 接口调用包 `CORE_CRITICAL_SECTION`。
- **宏形态坑**：`#define CORE_CRITICAL_SECTION(yourcode) { CORE_DECLARE_IRQ_STATE; CORE_ENTER_CRITICAL(); { yourcode } CORE_EXIT_CRITICAL(); }`（sl_core.h:210）——`yourcode` **不带尾分号**贴入，正确用法 `CORE_CRITICAL_SECTION(code;)`；头文件是 `sl_core.h` 不是 `em_core.h`。

### 问题 3：verify FAILED ret:0x1001（PARSER_UNEXPECTED）★核心教训
- **现象**：擦除 FF ✓、接收内容正确（stage dump 与文件逐字节一致 ✓）、写入后读回却完全不同——flash offset 244-255 与文件一致、**offset 256 起分叉**。
- **根因**：**bootloader 的 SPI 页编程不分割 256B 页边界**——SPI page program 跨页会回绕覆盖页首。244B 包从 offset 244 写，前 12 字节落 244-255，剩余 232 字节回绕覆盖 0-231，GBL 头被毁。
- **解决**：app 层 `_flush_aligned()` 按 256B 页边界切分 `bootloader_eraseWriteStorage` 调用（永不跨页，回绕物理上不再发生）。修复后 verify OK。
- **佐证方法**：`rx0 dump`（首包 RAM 内容）与 `hdr dump`（flash 读回）配对——rx0 对、hdr 错 → 写入/擦除层问题；rx0 就错 → 手机侧/接收层问题。
- **遗留**：同一 write 路径服务 Thread OTA（OTAImageProcessorImpl 写 >256B 块）——需确认 Thread OTA 在这版 bootloader（v3.2.4/u4）上是否真实验证过；bootloader 侧补分割是潜在共性修复。

### 问题 4：erase FAILED ret:1028（0x404 NEEDS_ALIGN）
- **现象**：`bootloader_eraseStorageSlot` 0.044s 即返回对齐错误（昨天同样调用 1.34s 成功）——跨 boot 非确定性。
- **分析**：入口对齐校验依赖 bootloader 本次 boot 对 flash 的 SFDP/JEDEC 探测结果（pageSize），探测结果跨 boot 不一致 → 强指向 **SPI flash 通信/探测不稳定（板级）**。
- **解决**：擦除自动重试 ×3 + 擦除时打印 `storage:` 参数行（pageSize/part 型号）供跨 boot 对比。若 `part` 型号跨 boot 变化或与本板实焊不符 → 板级排查（接线/WP#/供电）。（注：重试与参数日志的代码随后随快照回退移除，复现时按此加回。）

### 问题 5：读回 = 旧内容 & 新内容（4a 15 26 03…）
- **现象/根因**：slot 有旧数据时直接写入，NOR 型 flash 写只能 1→0，读回 = 旧 & 新。
- **解决**：**擦除是必须的**（BEGIN 先整槽擦 `bootloader_eraseStorageSlot`，实测 1.34s → FF）。"不擦除直接写"机理上不成立。

### 问题 6：slot 头 16 字节变 4a 15 26 03（bootload table）
- **现象**：`initVerifyImage` 后 slot 头 16B 被写成 `4a 15 26 03 08 00 00 00 00 00 00 00 01 00 00 00`。
- **结论**：这是 flashed bootloader（v3.2.4）在 initParse 阶段写入的 **bootload table**（覆盖 GBL 头 16B；解析器头部已缓存在 713B context 里，不影响其自身解析，但会干扰外部 dump 判读）。识别即可，无需处理。

### 问题 7：链接错误 undefined reference（C/C++ 链接）
- **根因**：`btl_interface.h`、`sl_bt_app_ota_dfu.h` 等 Silabs C 头**无 `__cplusplus` 护栏**，C++ TU 裸 include 产生修饰名引用。
- **解决**：`extern "C" { #include "btl_interface.h" }`（Matter SDK OTAImageProcessorImpl.cpp:30 同款）。遇到 Silabs 头的 undefined reference 先查这个。

### 问题 8：第二次 BEGIN 误判容量满
- **现象**：擦除完成后的第二次 BEGIN，首包即 ERROR。
- **根因**：`s_slot_size` 只在 INIT 路径赋值，ERASE 路径漏设（保持 0）→ 首包容量检查 `0 >= 0` 误判。
- **解决**：ERASE 完成分支补 `getStorageSlotInfo` 赋值 + BEGIN 分支兜底刷新。

### 问题 9：复位原因日志永远是 0
- **根因**：`wdg_api_get_reset_reason()` 返回的静态变量只在 `wdg_api_reset_check()` 里填充，无人调用。
- **解决**：直接读 `RMU_ResetCauseGet()`（em_rmu.h；Series 2 宏名为 `EMU_RSTCAUSE_*`）。另：`SILABS_LOG` 不出调试控制台（该口只见 `[DL]`/`[silabs ]BLE:` 标签日志），调试日志统一用 `LOG_MSG_*`。

### 问题 10：安装耗时 ~70s
- **说明**：`rebootAndInstall` 之后是 bootloader 安装流程（LZMA 解压 + 内部 flash 编程 ~1.5MB + ECDSA 校验 + secure boot 再验证 ~2.3s），全部在 bootloader 内部，与应用无关。属正常耗时；要缩短可去掉 GBL 的 LZMA 压缩（传输时间换安装时间）。

### 问题 11：板子被刷成内部 flash 型 bootloader
- **现象**：`storage: type:0 num:1 pageSize:0 part:?`，擦除空跑（读回不变）、写 0x401 INVALID_SLOT。
- **结论**：该板 bootloader（v3.0/u3）无 SPI 存储配置，**与接收端不兼容**。代码已有防护（见 §2.2/源码 ERASE 分支的 storage 检查）：storageType=0 / pageSize=0 时拒绝 OTA 并回错误码。**解决 = 该板刷 aok SPI 存储型 bootloader（v3.2.x/u4）**。

### 问题 12：verify 途中 HardFault（PC=LR=0xB39AC5AE，CFSR=0）★核心教训
- **现象**：已配网（Thread 在网）状态下 BLE OTA，verify 步进到 512~1024 步之间 HardFault：
```
[00:01:54.421][error][-] HardFault:  0x48415244
[00:01:54.421][error][-] SCB->CFSR   0x00000000
[00:01:54.421][error][-] SCB->HFSR   0x40000000   ← FORCED
[00:01:54.421][error][-] PC=LR=0xB39AC5AE          ← 调用无效函数指针（CFSR=0 → 跳转非法目标）
```
- **相关性（决定性）**：Matter OTA(Thread) 成功 → 接着 BLE OTA 两次 verify 失败（最后一次 HardFault）→ **factory reset 退到未配网后 BLE OTA 成功**——失败与"设备已配网"强相关。
- **根因**：**SE 加密硬件跨任务并发**。已配网时 Thread/Matter 持续使用 SE 加密；verify 原跑在 AppTask 与之并行，处理**加密 GBL** 的 ENC tag（SE 解密/签名）时撞车。与 Matter SDK 官方注释同源（MATTER-4155："SE access is not thread safe"）。
- **为什么 Matter OTA 配网状态能成功**：它的 verify 就在 CHIP event task 里执行，与所有 SE 使用天然串行（单任务事件循环不可能与自己并发）。
- **解决**：校验步进从 AppTask 事件链改为 **CHIP event task**（`PlatformMgr().ScheduleWork(_verify_step)` 链式自排）——与 Matter OTA 完全同任务、同串行化。
- **待复测**：未配网态的成功不能证明本修复生效（未配网本就无 SE 并发）；**需在已配网状态下复测一次 BLE OTA**。

### 其他已识别但未阻塞的点
- 版本日志（Ver/Btl Ver）本地构建不打：`GIT_COMMIT_HASH` 仅 Jenkins 注入。
- `_print_qrcode` unused 警告：调用点被注释，light 同款，无害。
- 官方 `app_ota_dfu`/`in_place_ota_dfu` 与本方案冲突，**组件列表里不要装**；`AppLoader OTA DFU` 系列是 NCP+AppLoader 架构用的，也不装。

---

## 5. Matter OTA 与 BLE OTA 流程对比

| 维度 | Matter OTA（Thread） | BLE OTA（本方案） |
|---|---|---|
| 传输通道 | Thread（BDX，OTA Requestor/Provider） | BLE side-channel（Silabs OTA 服务） |
| 接收位置 | CHIP event task，SDK `OTAImageProcessorImpl` | 蓝牙栈任务（传输/写入）+ AppTask（擦除）+ CHIP event task（校验，与 Matter OTA 同任务），我们的 `app_ble_ota_mgr` |
| 写入调用 | `WRAP_BL_DFU_CALL(bootloader_eraseWriteStorage(...))`，BDX 块大小 | 同款（CORE_CRITICAL_SECTION），**256B 页边界切分** |
| 校验调用 | `bootloader_verifyImage(slot, NULL)` **一次同步阻塞 ~15s**（关中断全程） | `initVerifyImage` + `continueVerifyImage` **分片**（CHIP event task 经 `ScheduleWork` 链式步进，每次毫秒级关中断，系统全程活着，进度可见） |
| 校验耗时 | ~15.3s | ~15.8s（同一 bootloader 机制，本质相同） |
| 成功后 | `ForceKeyMapSave` → `setImageToBootload` → 写 MatterUpdateReboot 标记 → 重启安装 | `setImageToBootload` → `rebootAndInstall`（无 Matter 专属步骤） |
| 失败后 | `CancelImageUpdate`，留旧版本 | ERROR + flash deinit，留旧版本 |
| 安装段 | 相同：bootloader 内 LZMA 解压 + 内部 flash 编程 + 签名校验，~70s | 相同 |
| 客户端 | 生态 Matter App / chip-tool | Simplicity Connect / nRF Connect（手工）/ 自研 App |
| 触发 | Provider 24h 查询或 App 发起 | 用户点 update（单击） |

---

## 6. [Log](matter-ota-log.md)

### 6.1 成功链路（BLE OTA，本次验证）
```
BLE OTA control cmd=0 (opcode=0x12, state=IDLE)
BLE OTA state IDLE -> PREPARING
BLE OTA preparing: erasing slot (single-click flow)
BLE OTA erasing slot 0 (may take a while)...
BLE OTA flash@erase: ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
BLE OTA state PREPARING -> DOWNLOAD
BLE OTA ready - streaming can start
BLE OTA rx0: eb 17 a6 03 08 00 00 00 00 00 00 03 01 01 00 00
BLE OTA rx 244 / 2088960 bytes          ← 每 8KB 一条
…
BLE OTA control cmd=3 (opcode=0x12, state=DOWNLOAD)
BLE OTA state DOWNLOAD -> WAIT_CLOSE
BLE OTA download DONE (658788 bytes), waiting disconnect
（断链）
BLE OTA conn 1 closed, state=WAIT_CLOSE pos=658788
BLE OTA verify start (658788 bytes)
BLE OTA verifying... steps:512 / 1024 / …（每 512 步一条）
BLE OTA verify OK (5149 steps)
BLE OTA reboot to install
（~70s 安装：LZMA 解压+编程+签名校验+secure boot，属正常）
重启后 Current Software Version 变为新版本
```

### 6.2 chip BLE 通道全链路成功实拍（2026-10-09）
```
[00:00:29.101] BLE OTA control cmd=0 (opcode=0x12, conn=2, state=IDLE)     ← chip BLE 连接发起
[00:00:29.101] BLE OTA state IDLE -> PREPARING
[00:00:29.101] BLE OTA preparing: erasing slot (single-click flow)
[00:00:29.101] BLE OTA erasing slot 0 ...
[00:00:29.235] BLE OTA flash@erase: ff …（整槽擦除 1.25s）
[00:00:29.235] BLE OTA state PREPARING -> DOWNLOAD
[00:00:29.235] BLE OTA deferred resp sent ret:0x0000 conn:2                 ← 延迟应答送达
[00:00:29.235] BLE OTA ready - streaming can start
[00:00:29.670] BLE OTA rx0: eb 17 a6 03 …                                  ← GBL 头正确
…rx 进度（每 8KB）…
[00:04:44.934] BLE OTA download DONE (659912 bytes), verifying
[00:04:44.937] BLE OTA hdr0 / hdr244 dump                                  ← flash 读回与文件一致
[00:04:44.938] BLE OTA verify start (659912 bytes)
…verifying… steps:512 … 4608 …
[00:05:00.916] BLE OTA verify OK (5158 steps)
[00:05:00.xxx] BLE OTA reboot to install → 重启后 0.0.2                    ← 全链路成功
```
（注：该次传输速率 ~2.6KB/s，瓶颈为 CHIPoBLE 连接被 Matter 重协商到 90ms 连接间隔，见 §9）

---

## 9. 速度瓶颈：CHIPoBLE 连接被 Matter 重协商到 90ms ★

- **现象**：chip BLE 通道 OTA 吞吐 ~2.6KB/s；write-with-response 与 write-without-response（speed OTA）**同速**——瓶颈不在响应等待。
- **根因**：**Matter ConnectivityManager 对 CHIPoBLE 连接的省电参数管理**：连接建立时 fast（30ms），稳定/idle 后重协商到 **90ms**（日志 `i:72`）——90ms 间隔 × 每连接事件 ~1 包 ≈ 2.6KB/s 上限。side-channel 连接不受 Matter 参数管理，参数由手机（central）决定——**实测两条通道速率相同（~2.6KB/s）**，side-channel 并不更快（其参数同样是手机侧的默认值）。
- **修复**：OTA 会话期间由设备（peripheral）发 L2CAP 参数请求：BEGIN 成功进入 DOWNLOAD 后调用 `sl_bt_connection_set_parameters(conn, 16, 24, 0, 500, 0, 0)`（20-30ms）——central（手机）通常会接受。若实测仍被 Matter 降回，可在 rx 进度处周期性重申。
- 预期效果：30ms 间隔下吞吐 ~8-20KB/s（659KB 约 40-80s）。

---

## 7. 已知限制与遗留

1. **bootloader 侧 write 不做 256B 分割**（本方案在 app 层规避）