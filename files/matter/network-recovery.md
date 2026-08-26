# Matter 设备断电重启后网络恢复全过程分析
## 文档概览
| 项目 | 内容 |
|------|------|
| **产品型号** | bk01_matter (Window Covering / 窗帘电机控制器) |
| **补充实测** | aok02_matter_ac（订阅恢复失败路径实测，2026-08-20） |
| **Matter 版本** | Matter 1.5 |
| **Thread 版本** | OpenThread 1.4 (MTD/SED) |
| **芯片平台** | Silicon Labs EFR32MG24 |
| **问题现象** | Matter 设备配网成功后，断电再上电，手机 APP 可能在 1 分钟到数分钟内无法控制设备 |
> **修订说明（v2）**：本版修正了原报告中关于 CASE Session Resumption 持久化、
> KeepSubscriptions 语义、控制器侧感知机制（MRP 超时 vs SESSION_NOT_FOUND）、
> 以及 PERSIST_SUBSCRIPTIONS 与 Session Resumption 关系等技术性错误，
> 消除了原文内部矛盾（详见各处「修订说明」标注），并重构为
> 「摘要 → 流程 → 根因 → 建议 → 附录」的漏斗式结构。
> Spec 章节号沿用原报告，请以所用 Matter 1.5 正式版规范逐一核对。
---
## 0. 一页摘要（先看这里）
**核心结论：设备侧约 3 秒内就已完全就绪；"APP 几分钟控制不了"的延迟几乎全部来自控制器侧（手机 APP / Hub）的离线感知与会话/订阅重建流程。**
| 阶段 | 归属 | 正常耗时 | 最坏耗时 | 结束标志 |
|------|------|---------|---------|---------|
| ① Boot + 初始化 | 设备 | **67ms（实测）** | 0.5–1s | OT/BLE/Matter Stack 就绪 |
| ② Thread 入网 + SRP 注册 | 设备 | 2–3s | 10–30s | SRP 注册完成，DNS-SD 已发布 |
| ③ 控制器感知离线 + DNS-SD + CASE 重建 | **控制器** | 5–30s | 60–120s | 新 CASE 会话 Active |
| ④ 订阅重建（或设备主动恢复） | 双方 | 0.5–1s | 2–5s | priming report 确认，APP 可控制 |
| **端到端** | — | **3–13s** | **90–140s+** | |
**三大根因（按影响排序）**：
1. 🔴 **控制器只能被动感知设备重启**（MRP 重传超时 + 订阅 MaxInterval 超时 + mDNS 缓存 TTL）→ 占总延迟 50–70%
2. 🔴 **Thread 入网超时后无重试机制**（30s 超时只打日志，远低于 Spec §11.8.4 建议的 5 分钟）→ 10–20%，**已确认的代码缺陷**
3. 🟠 **DNS-SD / mDNS 缓存 TTL 120s**，控制器可能拿到旧服务记录 → 叠加放大
**已确认正确的关键配置**：`PERSIST_SUBSCRIPTIONS=1` + `ENABLE_SESSION_RESUMPTION=1`。
两者是**相互独立**的加速机制，同时开启性能最优（详见 §7 根因 6 辨析）。
**实测数据支撑**：
- bk01 正常场景端到端 **~4.7s**（Thread Up → 可控制，附录 D 完整 log）
- aok02 订阅恢复失败路径（0x7d）：设备侧 0.6s 完成，控制器 **19s 后**才重新连接（§6.4）
---
## 1. 系统架构与配置概览
### 1.1 硬件架构
```
┌──────────────────────────────────────────────────┐
│ EFR32MG24 (Matter SoC)                           │
│                                                  │
│  ┌──────────────┐  UART   ┌────────────────────┐ │
│  │ Matter Stack │◄───────►│ MCU (MotorCtrl)    │ │
│  │ + Thread     │  SPP    │ - Motor Driver     │ │
│  │ + BLE        │  协议   │ - BAT Management   │ │
│  │ + FreeRTOS   │         │ - 433MHz RF        │ │
│  └──────────────┘         └────────────────────┘ │
│                                                  │
│  NVM3 Flash (40960 bytes):                      │
│  - KVS (Key-Value Store)                        │
│  - Thread Network Credentials                   │
│  - Matter Fabric Data                           │
│  - 持久化订阅元数据                              │
│  - CASE 会话恢复记录 (Resumption Records)        │
│  - Device Configuration                         │
└──────────────────────────────────────────────────┘
```
### 1.2 软件架构
```
┌─────────────────────────────────────────────┐
│ Application Layer                            │
│ AppTask / app_nwk_mgr / app_spm_mgr          │
│ app_comm_mgr / app_wdc_mgr / app_mcu_dfu     │
├─────────────────────────────────────────────┤
│ Matter Stack (connectedhomeip)               │
│ Server / FabricTable / CASE / IM             │
│ CommissioningWindowManager                   │
├─────────────────────────────────────────────┤
│ Connectivity Layer                           │
│ PlatformMgr / ConnectivityMgr                │
│ ThreadStackManager / BLEManager              │
├─────────────────────────────────────────────┤
│ OpenThread Stack                             │
│ MLE / MAC / IPv6 / UDP / SRP Client          │
├─────────────────────────────────────────────┤
│ Hardware                                     │
│ 802.15.4 Radio / BLE Radio / NVM3 Flash      │
└─────────────────────────────────────────────┘
```
**各组件说明**：
- **MLE** (Mesh Link Establishment)：Thread 链路管理层 — 设备发现、父子关系建立（Child ID Request/Response）、链路维护、地址注册。Thread Attach 全过程由 MLE 驱动
- **MAC**：802.15.4 MAC 层 — 信道扫描（Active Scan、CSMA/CA 退避）、CSL 同步
- **IPv6**：基于 6LoWPAN — SLAAC 地址生成、Mesh-Local / GUA / ML-EID 多地址管理
- **SRP Client**：向 Border Router 注册 `_matter._tcp` / `_matterc._udp` DNS-SD 服务；租约管理（Key Lease 14 天、Service Lease 2 小时）
### 1.3 关键配置参数汇总
| 配置项 | 值 | 所在文件 | 与恢复的关系 |
|--------|-----|---------|------------|
| `ATTACH_NETWORK_TIMEOUT_MS` | 30s | app_nwk_mgr.cpp:22 | 入网判定超时（**超时后无重试，见根因 2**） |
| `CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL` | 2000ms | CHIPProjectConfig.h:131 | MRP 重传间隔（影响控制器侧感知时长） |
| `CHIP_CONFIG_RMP_DEFAULT_MAX_RETRANS` | 4（SDK 默认） | ReliableMessageProtocolConfig.h | 控制器侧总超时 ≈ 4 × 2s × 退避 ≈ 10–20s |
| `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS` | 1 | AppBuildConfig.h:8 | 持久化订阅（设备重启后**主动**恢复，见 §6.3） |
| `CHIP_CONFIG_SUBSCRIPTION_TIMEOUT_RESUMPTION` | 0 | AppBuildConfig.h:12 | 订阅超时不自动恢复（控制器需主动重建） |
| `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION` | 1 | AppBuildConfig.h:16 | CASE 会话恢复记录持久化（**与订阅持久化相互独立**） |
| `CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS` | 300s (5min) | CHIPProjectConfig.h:162 | Basic 配网窗口（Spec §5.4.2.3.1 要求 180–900s ✓） |
| `CHIP_DEVICE_CONFIG_ENABLE_PAIRING_AUTOSTART` | 0 | CHIPProjectConfig.h:141 | 上电不自动打开配网窗口 |
| `CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART` | 0 | CHIPProjectConfig.h:155 | 已配网设备上电不打 BLE 广播（见根因 4） |
| `CHIP_DEVICE_CONFIG_BLE_FAST_ADVERTISING_TIMEOUT` | 30s | CHIPProjectConfig.h:118 | 仅未配网设备适用 |
| `SL_IDLE_MODE_DURATION_S` | 600s | sl_matter_icd_config.h:12 | ICD 空闲模式时长 |
| `SL_ACTIVE_MODE_DURATION_MS` | 0 | sl_matter_icd_config.h:23 | 活跃模式禁用（非严格 ICD 行为） |
| `CHIP_CONFIG_ENABLE_ICD_LIT` | 0 | ICDServerBuildConfig.h:21 | LIT 模式禁用 → **Check-In (0x50) 机制不适用本设备** |
| `OPENTHREAD_CONFIG_THREAD_VERSION` | 1.4 | sl_openthread_features_config.h:45 | Thread 协议版本 |
| `OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE` | 1 | sl_openthread_features_config.h:65 | CSL Receiver 启用 |
| `NVM3_DEFAULT_NVM_SIZE` | 40960 | nvm3_default_config.h:38 | NVM3 Flash 大小 |
| `WATCHDOG_TIMEOUT_MS` | 60s | AppTask.cpp:57 | 看门狗喂狗周期，不影响恢复 |
| `OTA_PERIODIC_TIMEOUT` | 86400s | sl_matter_ota_config.h:9 | 24h 检查一次，不影响恢复 |
### 1.4 平台事件类型码速查表
在 Matter 平台事件回调 `on_platform_event()` 中，`event->Type` 为数字枚举值：
| 事件码 | 枚举常量 | 说明 | 触发时机 |
|--------|---------|------|---------|
| **32769** | `kThreadConnectivityChange` (Result=`kConnectivity_Established`) | Thread 连接已建立 | OpenThread MLE Attach 完成后 |
| **32779** | `kThreadStateChange` | Thread 状态变化 | Attach/Detach 过程中可能多次触发 |
| **32786** | `kDnssdInitialized` | DNS-SD 初始化完成 | `DnssdServer::StartServer()` 完成后 |
| **32790** | `kOperationalNetworkReady` | Operational 网络就绪 | SRP 注册完成后（32786 → 32790 顺序固定） |
| **32792** | `kCaseSessionEstablished` | CASE 安全会话建立 | `SecureSession::mState` 变为 `kActive` 时 |
**Log 识别技巧**：32779 在 Attach 过程中多次出现（OT 子状态切换），32769 紧随其后（Attach 最终成功）；32786 → 32790 顺序固定。
---
## 2. 断电重启完整时序总览
### 2.1 总体时序图
```
时间轴(秒)   0    0.2      3              60~90          300+
             │    │        │               │              │
             ├─①──┤        │               │              │
             │    ├─②──────┤               │              │
             │    │        ├──────③────────┤              │
             │    │        │          ├─④──┤              │
             ▼    ▼        ▼          ▼    ▼
            上电  栈就绪   Thread Up  CASE  订阅完成
                                (此时设备已可接受 Matter 命令!)
  └── 设备侧 ~3s ──┘└────── 控制器侧 30~180s ──────┘
```
> **读图要点**：每个 `▼` 是里程碑时刻；阶段条长度 = 阶段耗时。
> ② 结束时（~3s）设备已完全可接受 Matter 命令。③④ 是**控制器侧**的
> 等待与重建，与设备无关——这就是"手机 APP 几分钟无法控制"的根因。
### 2.2 各阶段一览
| # | 阶段 | 正常耗时 | 最坏耗时 | 结束时你看到什么 |
|---|------|---------|---------|----------------|
| ① | Boot + Init | 67ms（实测） | 0.5–1s | Stack 全部就绪，`app_nwk_mgr_init()` 触发 |
| ② | Thread Attach + SRP | 2–3s | 10–30s | Thread 入网成功，DNS-SD 已发布 |
| ③ | CASE Re-Estab（控制器侧） | 10–30s | 60–120s | 控制器检测离线 + DNS-SD + CASE 完成 |
| ④ | Subscribe | 0.5–1s | 2–5s | CASE 建立后订阅就绪，APP 可正常控制 |
### 2.3 各阶段依据速查
| # | 阶段 | Spec 依据 | 项目代码 | SDK 代码 |
|---|------|----------|---------|---------|
| ① | Boot+Init | §11.8.2（NVM 持久化） | `main()` → `AppTask::AppInit()` [AppTask.cpp:74] | NVM3 `nvm3_open()`; OT `otInstanceInit()`; `Server::Init()` |
| ② | Thread Attach | Thread Spec MLE（Discover→ChildIdReq→LinkReq）; §11.9.5.2（SRP 发布）; §11.8.4（应重试 ≥5min） | `app_nwk_mgr_init()` [app_nwk_mgr.cpp:36] | OT `mle.cpp:Attach()`; `srp_client.cpp:SendUpdate()` |
| ③ | CASE Re-Estab | §4.14.2（Sigma 0x30–0x32）; §4.14.2.7（Resumption 0x33） | （控制器发起，设备响应） | `CASEServer.cpp:HandleSigma1()`; `CASEClient.cpp:SendSigma1()` |
| ④ | Subscribe | §8.5.2（0x03/0x04/0x05）; §8.5.3（订阅持久化） | `PERSIST_SUBSCRIPTIONS=1` | `ReadClient.cpp:SendSubscribeRequest()`; `InteractionModelEngine.cpp` |
| 未配网 | Commissioning Window | §5.4.2.3.1（180–900s） | `DISCOVERY_TIMEOUT_SECS=300` | `CommissioningWindowManager.cpp` |
---
## 3. 阶段①：Boot 与初始化（0 – 0.2s）
### 3.1 调用链
```
main() [main.cpp:51]
└─ app_init_early()               // 启动 Trace
└─ sl_system_init()               // Silicon Labs 系统初始化
   ├─ 时钟初始化 (HFXO/DPLL)
   ├─ NVM3 初始化 (Flash 存储)
   ├─ BLE Stack 初始化 (sl_bt_init)
   ├─ OpenThread Stack 初始化 (otInstanceInit)
   ├─ FreeRTOS 调度器启动
   └─ Matter Platform 初始化
└─ app_init() → SilabsMatterConfig::AppInit()
   └─ AppTask::AppInit() [AppTask.cpp:74-118]
      ├─ ev_queue_init()          // 事件队列
      ├─ 打印版本号和复位原因
      ├─ _print_qrcode()          // 打印 Matter QR Code
      ├─ _write_mfg_date()        // 制造日期/序列号写入 NVM3
      ├─ wdg_api_init()           // 看门狗 (60s)
      ├─ app_comm_mgr_init()      // 串口通信管理器
      ├─ app_nwk_mgr_init()       // ★ 网络管理器（关键）
      ├─ app_comm_mgr_start()
      ├─ app_spm_mgr_init()       // Matter 串口协议处理器
      ├─ app_timetask_mgr_init()  // 定时任务（窗帘定时）
      ├─ app_mcu_dfu_init()       // MCU OTA
      └─ bootloader_deinit()      // SPI Flash 进入 Deep Sleep
```
### 3.2 实测耗时（bk01，EFR32MG24）
| 步骤 | Log 时间戳 | 实际耗时 |
|------|-----------|---------|
| FreeRTOS Scheduler 启动 | `[00:00:00.067]` | 0ms（基准） |
| OpenThread Stack 就绪 | `[00:00:00.070]` | +3ms |
| BLE Stack 就绪 | `[00:00:00.119]` | +52ms |
| AppTask::AppInit() 开始 | `[00:00:00.125]` | +58ms |
| **App Task Started（全部就绪）** | `[00:00:00.134]` | **+67ms** |
> 完整冷启动（Power On → App Ready）约 100–200ms（含 Bootloader 校验、
> HFXO 稳定时间）。**此阶段不是恢复延迟的瓶颈。**
### 3.3 关键分叉：配网状态判断
`app_nwk_mgr_init()` 读取 NVM3 中存储的 Thread 网络凭据（Network Key、
Extended PAN ID、PAN ID、Channel、Active Operational Dataset 等）：
```cpp
if (ConnectivityMgr().IsThreadProvisioned()) {
    // 情况A: 已配网 → 走恢复流程
    // 启动 30s 入网计时器 (ATTACH_NETWORK_TIMEOUT_MS)
} else {
    // 情况B: 凭据缺失（NVM3 损坏 / 首次）→ 打开 5 分钟配网窗口
    // ⚠️ 这是延迟的第一个潜在来源（异常路径）
}
```
---
## 4. 阶段②：Thread 入网（0.2 – 3s，最坏 10–30s+）
### 4.1 MLE 驱动的 Attach 流程
| 步骤 | 内容 | 正常耗时 | 恶化条件 | OT SDK 代码 |
|------|------|---------|---------|-------------|
| 1. Active Scan | 16 信道 Beacon Request 扫描 | 0.3–1s | 信道拥挤、退避等待 | `mac.cpp:StartCsmaBackoff()` |
| 2. Parent Selection | 按 RSSI 评估候选父节点 | 0.1–0.5s | 缓存 Parent 不可达 → 全量重扫（+1–5s） | `mle.cpp:Mle::Attach()` |
| 3. Child ID Req/Rsp | 向 Parent 注册为 Child | 0.1–1s | Parent 忙、响应超时重试 | `mle.cpp:SendChildIdRequest()` |
| 4. MLE Link 建立 | 链路信息交换 | 0.1–0.5s | 信号弱、重传 | `mle.cpp:HandleChildIdResponse()` |
| 5. 地址注册 | SLAAC 生成 Mesh-Local IPv6 并注册 | 0.5–2s | 多地址注册（ML + GUA + ML-EID） | `mle.cpp:SendAddressSolicit()` |
| 6. SRP 注册 ★ | 向 Border Router 注册 Matter 服务 | ~100ms（1 次 CoAP 往返） | Border Router 高负载时 2–5s | `srp_client.cpp:SendUpdate()` |
**正常总计约 2–3 秒；异常（父节点不可达/信道差/拓扑变化）10–30s 甚至更长。**
### 4.2 已确认的代码缺陷：入网失败无重试
```cpp
// app_nwk_mgr.cpp:150-152 — 当前 bk01 实现
static void _rejoin_timeout_event_handler(app_event_t * ev)
{
    LOG_MSG_INFO(TAG_NWK, "rejoin failed");
    // ⚠️ 仅打日志，无重试机制！
}
```
对比 Spec（Matter Core Spec §11.8.4）：
> "The device SHOULD attempt to re-establish Thread connectivity for a
> minimum of 5 minutes before considering the network unreachable."
当前实现 30 秒即放弃且不重试——**若 30s 内 Attach 失败而网络随后恢复，
设备将永久离线直到再次断电。** 修复方案见 §8.2。
> **aok02 已修复（2026-08-20）**：超时后重启 Thread 栈
> （`otThreadSetEnabled(false/true)`）并无限重试；
> `kConnectivity_Lost` 事件也纳入同一重试看门狗。
### 4.3 Attach 成功后的设备侧事件流
```
MLE Attach 完成
→ kThreadConnectivityChange(Established) (32769)
→ app_nwk_mgr: m_nwk_status = Joined; 通知 MCU; 停止 30s 计时器
→ SRP Client 启动 (连 Border Router)
→ kDnssdInitialized (32786)
→ SRP 注册完成 → kOperationalNetworkReady (32790)
← 设备此刻已可接受 Matter 命令
```
---
## 5. 设备侧 Matter 恢复（毫秒级，非瓶颈）
Thread Up 后设备侧恢复几乎瞬时完成（bk01 实测）：
```
14.365  Thread Established
14.447  SRP Client started, detected server: fd11:9c64:... (仅 +82ms)
14.933  DNS-SD initialized (+568ms)
14.934  Advertise operational node 52017B57FC1E977B-00000000000008CA
14.945  No subscriptions to resume（本次实测无持久化订阅数据）
```
### 5.1 Server 状态恢复
`Server::Init()` 完成后：Fabric Table / ACL / Group Key / Attribute Store
均从 NVM3 恢复，Interaction Model 引擎就绪。
**OTA Requestor 的两次调度**（log 实证，属正常行为）：
```
[00:00:14.365] Scheduling OTA Requestor initialization   ← 第一次调度
[00:00:14.933] DNS-SD initialized, scheduling OTA ...    ← DNS-SD 就绪后第二次
```
OTA 查询依赖 DNS-SD 发现 OTA Provider 服务，故首次调度被推迟到
`kDnssdInitialized` (32786) 之后才真正执行。
### 5.2 "unknown session" 日志——必然且正常的行为
```
[00:00:14.506][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.531][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.553][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.579][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
```
**逐条分析**：
- 4 条消息间隔 22–26ms，来自同一控制器
- 设备重启后 RAM 中的 Session Table 为空，`SessionManager` 查不到 LSID=36120
  对应的 `SecureSession` 对象 → 打印 error 并静默丢弃
- 控制器此时尚未感知设备重启，仍用**旧会话密钥**加密发命令
- **这是协议设计的必然结果，不是 bug**。丢弃后控制器因收不到 Ack 触发
  MRP 超时——这恰恰是控制器感知设备重启的第一信号源（见 §6.1）
### 5.3 SPP 串口重传——与网络恢复并发，互不阻塞
SPP 是 MG24 与 MCU 间的串口协议（帧头 `55 AA`，CMD 0x01=NOP/心跳，
0x02=Data/Status）。
**实测重传参数**：
| 参数 | 值 | 说明 |
|------|-----|------|
| `ack_timeout_ms` | 500ms | 等待 MCU 应答超时 |
| 每帧最大重传次数 | 2 | `re-sent count 2` 后 `reach to max` |
| 放弃后行为 | 序列号递增，发下一帧 | 不阻塞后续帧 |
| 并发策略 | 不阻塞 | "pending ack but allow new cmd process" |
**与网络恢复的并发关系**（log 时间线实证）：
```
14.365  COM: notify network [Joined]        ← 通过 SPP 通知 MCU
14.447  SRP Client started                  ← Matter 侧继续（不等 SPP）
14.844  SPP: re-sent count 1                ← SPP 独立重传
14.933  DNS-SD initialized                  ← Matter 侧继续
18.155  CASE Sigma1                         ← Matter 侧继续
18.847  SPP: re-sent reach to max           ← 第三轮放弃
```
**关键结论**：恢复初期大量 SPP 重传是**正常现象**——MCU 在 MG24 启动后
还需要额外初始化时间。SPP 走 UART，与 Thread/CASE（802.15.4）完全独立。
---
## 6. 阶段③④：控制器侧恢复（30 – 180s，延迟大头）
### 6.1 控制器如何感知"设备重启了"
控制器**没有任何主动通知机制**可用（设备不会广播"我重启了"），只能通过
三条被动路径：
| 路径 | 机制 | 耗时 | SDK 代码（控制器侧） |
|------|------|------|---------------------|
| **A. 被动超时** | 订阅 MaxInterval（通常 60s）内无报告 → 判定离线 | 最长 60s | `ReadClient.cpp:OnMaxIntervalTimeout()` |
| **B. 用户操作触发** | 用户点 APP → 旧会话发命令 → 设备静默丢弃 → 无 Ack → MRP 重传 4 次 × 2s（含退避）超时 → 触发重查 DNS-SD + 新 CASE | 10–20s | `ReliableMessageMgr.cpp:SendFromQueue()` |
| **C. 周期 DNS-SD 刷新** | 控制器定期查询 Border Router mDNS（缓存 TTL 120s, RFC 6762 §7.1） | 0–120s | `Discovery_ImplPlatform.cpp:ResolveByType()` |
> **修订说明**：原报告称"控制器收到 SESSION_NOT_FOUND 后重建 CASE"，
> 这混淆了设备侧逻辑——`SecureUnicastMessageDispatch()` 返回
> `SESSION_NOT_FOUND` 发生在**设备**上，控制器根本感知不到这个错误码。
> 控制器侧的真实感知信号是 **MRP 无 Ack 超时**。
**控制器侧重建各环节耗时**：
| 步骤 | 耗时 |
|------|------|
| MRP 重试直到超时 | 6–16s |
| DNS-SD 重新发现（受 mDNS 缓存影响） | 1–15s |
| 新建 CASE 会话（Resumption 生效时 0.4–1s） | 0.4–2s |
| 重建属性订阅 | 0.5–1s |
| **合计（仅控制器侧）** | **9–35s** |
### 6.2 CASE 会话重建
**基础事实（修正后）**：
1. RAM 中的 `SecureSession` 对象（含会话密钥）重启即全部丢失 → 所有旧会话失效
2. 但设备在 NVM 中持久化了 **CASE 会话恢复记录**（`ENABLE_SESSION_RESUMPTION=1`，
   Spec §4.14.2.7 定义的正是这套可持久化的加速恢复机制）
3. 控制器重新发起 Sigma1 时，设备用缓存的密钥材料以 **Sigma2Resume (0x33)**
   响应，跳过完整 ECDH 交换
> **修订说明**：原报告称"Spec §4.14.2.7 明确禁止会话密钥跨重启持久化"，
> 与自己的实测 log 矛盾——bk01 重启后设备正是用 Sigma2Resume 响应成功的。
> 正确理解：**活动会话不持久化，但恢复记录持久化**——这正是 Resumption 的设计意图。
**两种握手对比**：
```
完整 Sigma（4 报文，~1.5–2s）:           Session Resumption（2 报文，~0.4–1s）:
  Controller ──Sigma1(0x30)──▶ Device     Controller ──Sigma1(0x30)──▶ Device
  Controller ◄──Sigma2(0x31)── Device     Controller ◄──Sigma2Resume(0x33)── Device
  Controller ──Sigma3(0x32)──▶ Device     (Session Active)
  Controller ◄─StatusReport(0x40)─ Device
```
**bk01 实测（Session Resumption 生效实证）**：
```
[00:00:18.155] Msg TX Type 0000:30 (CASE_Sigma1)          ← 控制器发起
[00:00:18.551] Msg RX Type 0000:33 (CASE_Sigma2Resume)    ← 仅 +396ms！恢复路径
[00:00:18.552] Msg TX Type 0000:10 (StandaloneAck)
[00:00:18.559] Msg TX Type 0000:40 (StatusReport)
[00:00:18.564] SecureSession[LSID:25475]: kEstablishing → kActive
```
观察要点：
- Sigma1 → Session Active 仅 **409ms**，优于预估值
- 新 LSID=25475 ≠ 被丢弃的旧 LSID=36120，证明确实是全新会话
- 控制器在设备就绪后 **~3.2s** 才发出 Sigma1（控制器侧反应时间，占全程 ~68%）
**Resumption 生效条件**：① 设备侧 `ENABLE_SESSION_RESUMPTION=1` ✓；
② 控制器侧支持；③ 恢复记录未过期/未清除；④ 控制器 IP 未变化。
局限性：多个控制器各自维护独立缓存；缓存有容量与过期限制。

### 6.3 订阅重建：两条路径
#### 路径一：持久化订阅恢复（PERSIST_SUBSCRIPTIONS=1 时的标准机制）
设备重启后**主动**执行，无需控制器任何动作：
```
设备: "Resuming N subscriptions"
  → 设备主动对每个订阅者发起 CASE（此时设备是 Initiator）
  → CASE 恢复成功（Sigma2Resume）
  → 重建 ReadHandler
  → 发送 priming report（订阅属性的当前值）
  → 控制器确认 → 订阅恢复完成
```
SDK 依据：`InteractionModelEngine.cpp:GetSubscriptionResumptionInfo()` 从
NVM3 读取（SubscriptionID、AttributePaths、Intervals、FabricIndex）。
#### 路径二：控制器重新订阅（PERSIST=0，或恢复失败时）
控制器检测离线后发送全新 `SubscribeRequest (0x03)` → 设备回
`SubscribeResponse (0x04)` → 发送全量 priming `ReportData (0x05)`。
对 Window Covering 设备，全量 priming 需读取
CurrentPosition / TargetPosition / OperationalStatus / Mode 等所有被订阅属性
（部分需经 UART 从 MCU 读取），耗时 1–5s。
> **概念澄清（修订重点）**：
> - **KeepSubscriptions** 是 SubscribeRequest 中的一个字段，语义是
>   "建立这个新订阅时，是否**保留该订阅者在设备上的其他订阅**"
>   （叠加 vs 替换），它**不是**跨重启恢复的开关。
> - 跨重启恢复由 `PERSIST_SUBSCRIPTIONS` + SubscriptionID 匹配驱动，
>   与 KeepSubscriptions 字段无关。
> **补充说明**：`PERSIST_SUBSCRIPTIONS=1` 是"能力"而非"保证"——
> bk01 log 中的 "No subscriptions to resume" 表明持久化数据可能为空
> （首次配网即断电 / 控制器从未订阅 / NVM 损坏 / 数据过期），
> 此时自动退化为路径二。

### 6.4 订阅恢复失败路径：0x7d InvalidSubscription（aok02 实测，2026-08-20）
**CASE 恢复成功 ≠ 订阅恢复成功。** aok02_matter_ac 固件实测时间线：
```
00:00:14.547  Resuming 1 subscriptions          ← 设备主动恢复订阅
00:00:14.769  设备主动发 CASE_Sigma1（设备是 Initiator）
00:00:14.833  收到 Sigma2Resume               ← ✅ CASE 恢复成功（仅 0.3s）
00:00:14.848  Registered a ReadHandler
00:00:15.097  Status response = 0x7d           ← ❌ 控制器拒绝 priming report
00:00:15.108  Subscription torn down           ← 设备按 Spec §8.5.3 拆除
                                                 并删除持久化记录
──────（等待窗口：设备侧无任何动作可做）──────
00:00:33.442  控制器主动发 CASE_Sigma1         ← 用户点 APP 触发
00:00:33.649  新 CASE 会话 + 新订阅建立
00:00:38.810  priming reports 全部 0x00 确认   ← 恢复正常
```
**关键结论**：
1. **0x7d = 控制器侧丢失了订阅状态**（hub 重启 / 状态清理 / 多 hub 迁移）。
   设备按 Spec §8.5.3 拆除订阅并删除持久化记录后，双方都不再持有该订阅，
   无对象可恢复。
2. **订阅只能由控制器（订阅方）发起 SubscribeRequest 重建**。常电非 ICD
   设备没有任何协议消息可以"请求控制器来订阅我"——Check-In（0x50）是
   ICD 专属机制，本设备 `CHIP_CONFIG_ENABLE_ICD_LIT=0`、非严格 ICD，不适用。
3. **设备主动发起 CASE 并非"无意义"**（修订：原文表述过强）——在控制器
   保留状态时，它正是 §6.3 路径一的标准恢复机制；仅当控制器丢状态（回 0x7d）
   后才失效。失效后，"点一下 APP 才能恢复"的根因完全在**控制器侧**的
   发现/重订阅策略，设备端无协议内手段强制加速。
4. 对比同一设备：成功路径 0.6s 完成，失败路径等了 **19s**（直到用户操作触发
   控制器重连）——差异全部在控制器侧。
**责任边界判定表（用日志定位"卡住"在哪一侧）**：
| 设备侧日志表现 | 结论 |
|----------------|------|
| 重启后 1–3s 内：Resuming → Sigma2Resume → ReadHandler → priming report 0x00 确认 | 设备侧 100% 完成；APP 仍离线 = 控制器侧问题，设备代码无解 |
| priming report 收到 0x7d → torn down | 控制器侧丢订阅状态（本路径）；等待控制器重订阅，或做"温和助推"实验（§8.3） |
| `rejoin failed` 反复出现 | 网络层未恢复，检查入网重试机制（§4.2） |
| 某个 peer 的 DNS 解析挂起 / Sigma 无响应 | SDK 订阅恢复自带重试调度，观察 `Resuming N subscriptions` 重试日志即可 |
**设备端可选的间接助推**（均为网络层动作，非协议消息）：
| 方案 | 做法 | 风险 | 评价 |
|------|------|------|------|
| 温和助推 | 检测到订阅 torn down 后 N 秒内无新 CASE → Thread detach+reattach 一次，迫使 SRP 重注册 + mDNS 重公告，可能提前唤醒控制器 | 打断其他控制器既有会话/订阅；只能在"拆除后、重连前"窗口执行 | 可选实验，未实施（见 §8.3） |
| DNS-SD TXT boot counter | 每次重启 TXT 记录变化，逼 mDNS 立即重公告 | 非标准 vendor key、侵入大、对主动重查的控制器无感 | 不建议 |
| 等待自愈 | 不做任何事 | — | 控制器通常 30s–2min 内自发重连 |
---

## 7. 延迟根因汇总
> 严重程度：🔴 关键（直接决定恢复延迟）/ 🟠 次要（叠加放大）
### 延迟时间线（正常 vs 最坏）
| 阶段 | 正常场景 | 最坏场景 | 关键因素 |
|------|---------|---------|---------|
| 系统启动 | 0.07–0.2s | 0.5–1s | 实测 67ms；最坏为 Bootloader 慢 + NVM3 Repack |
| Thread 扫描 | 0.3–1s | 3–5s | 信道质量、路由器数量 |
| Thread 入网 | 2–5s | 10–30s | 父节点选择、拓扑变化 |
| SRP 服务注册 | 0.1–2s | 5–10s | Border Router 响应速度 |
| 控制器检测离线 | 0–10s | 60s | 用户是否操作 APP；被动等 MaxInterval=60s |
| DNS-SD 重新发现 | 1–3s | 5–15s | Border Router mDNS 缓存（TTL=120s） |
| CASE 重建 | 0.4–2s | 3–5s | Resumption 启用时减半 |
| 订阅重建 | 0.5–1s | 2–5s | priming report 数据量 |
| **总计（PERSIST=1）** | **约 3–13s** | **约 90–140s+** | |
| **总计（PERSIST=0，假设）** | **约 40–100s** | **约 120–200s+** | 见根因 6 |
### 🔴 根因 1：控制器只能被动感知设备重启（占延迟 50–70%，最主要根因）
**协议层面的必然性**：
| 来源 | 位置 | 定义 |
|------|------|------|
| Matter Core Spec | §4.14.2 | CASE 会话用 Sigma 协议建立，会话密钥由 ECDH 临时密钥派生 |
| Matter Core Spec | §4.14.2.7 | Session Resumption：恢复记录可持久化于 NVM，用于加速重建（修订后表述） |
| Matter Core Spec | §8.5.3.2 | 订阅可持久化，但恢复后仍需重建 CASE 会话 |
| Matter SDK | `SecureSession.h` | 会话对象 `mState` 仅存 RAM，重启即丢失 |
| Matter SDK | `SessionManager.cpp` | `Init()` 创建空会话表，不从 Flash 恢复活动会话 |
**设备没有任何"主动通知重启"的协议手段** → 控制器只能靠
MRP 无 Ack 超时（10–20s）或订阅超时（最长 60s）发现异常，再叠加
DNS-SD 重发现（mDNS TTL 120s）+ CASE + 订阅重建。
**实测**：bk01 上 "unknown session" 丢弃 4 条后，控制器约 3.8s 才发出
Sigma1（本次较快，因控制器恰在主动操作）；纯被动等待场景可拖到 60–120s。
### 🔴 根因 2：Thread 入网超时后无重试（已确认的代码缺陷）
- `ATTACH_NETWORK_TIMEOUT_MS = 30s`，超时后**仅打日志不重试**
- Spec §11.8.4 建议至少重试 5 分钟，当前实现 30s 即放弃 —— **违反 Spec 建议**
- 若 30s 内 Attach 失败而网络随后恢复 → 设备永久离线
- **aok02 已修复**（超时重启 Thread 栈 + 无限重试），bk01 建议同步合入（§8.2）
- 附带问题：若 NVM3 凭据损坏导致 `IsThreadProvisioned()=false`，设备直接
  打开 5 分钟配网窗口——建议先区分"凭据丢失"与"临时连接失败"（§8.4）
### 🟠 根因 3：SRP / DNS-SD / mDNS 链路延迟
**注册链路**：
```
设备 SRP 注册 (srp_client.cpp:SendUpdate, 0.1–2s)
→ Border Router 处理 (otbr-agent, 0.5–5s)
→ mDNS 记录更新（缓存 TTL 120s, RFC 6762 §7.1）
→ 控制器 DNS-SD 发现 (Discovery_ImplPlatform.cpp, 0.5–3s)
```
**关键问题**：设备重启后 SRP 注册的是新服务实例，但 mDNS 缓存可能仍保留
旧条目。最坏情况下控制器要等 TTL 过期（最长 2 分钟）才能发现新注册。
缓解方案见 §8.2（Thread Up 后强制 SRP 重注册）。
### 🟠 根因 4：BLE 未用作带外"存活信号"
- Spec §5.4.2.5 **禁止已入网设备用 BLE 配网**，但 §5.6 允许 operational
  状态下**可选**维持 BLE 广播
- 本项目 `CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART=0` → 已配网设备上电
  完全不打 BLE，附近的手机无法通过 BLE 快速感知设备在线
- 若 Thread 凭据丢失回到未入网状态，BLE 配网广播是允许的（且本项目
  广播参数合规：快速 25ms / 慢速 500ms，符合 §5.4.2.5.3）
- 建议：仅在 Thread 长时间恢复失败的场景下短暂开 BLE 广播作 liveness signal
### 🟠 根因 5：NVM3 存储开销（影响很小）
- 正常初始化 <10ms（含在 67ms Boot 内）
- 仅 Repack（碎片整理，+0.5–2s）或写入中断电导致 Page 损坏（备份恢复
  +0.5–1s）时有额外开销
- Spec §11.8.2 要求 Thread 凭据/Fabric/Group Key 持久化于 NVM——当前满足
- 优化空间：利用 `SL_MATTER_DEFERRED_ATTRIBUTE_STORE_DELAY_MS=2000`
  延迟批量写入，减少 Page 擦除
### 🟠 根因 6：`PERSIST_SUBSCRIPTIONS` 配置辨析（重写）
**修正后的机制对比**：
| 维度 | PERSIST=1（当前，正确选择） | PERSIST=0（假设） |
|------|---------------------------|------------------|
| 设备重启后 | 从 NVM 恢复订阅元数据，**主动**对订阅者发起 CASE + 推送 priming report | 无任何订阅记忆 |
| 控制器需要做什么 | **什么都不用做**（若其仍持有匹配状态） | 必须自行检测离线（等超时）→ 全新 SubscribeRequest |
| 订阅超时等待 | 无 | +30~60s（MaxInterval 超时） |
| priming report | 增量（设备保留上次报告快照） | 全量（所有被订阅属性现值，+1–5s） |
| 多控制器场景 | 各自独立恢复，互不阻塞 | 各自等超时 + 各自全量重建，成倍放大（+N×5s） |
| CASE Resumption | **不受影响**（独立机制） | **同样不受影响** |
> **修订说明**：原报告声称"Session Resumption 依赖订阅持久化、PERSIST=0
> 时必须走完整 Sigma、无法利用缓存密钥"——这是错误的。Session Resumption
> 记录存储在独立的 SessionResumptionStorage 中，与订阅持久化无关。
> PERSIST=0 真正多花的时间来自"控制器必须自己等超时 + 全量订阅重建"，
> 合计约 +30~70s。
**结论**：当前 `PERSIST_SUBSCRIPTIONS=1` 是正确配置。除非 NVM3 空间极度
紧张（每个持久化订阅约 200–500 bytes），否则不应关闭。
---

## 8. 优化建议
### 8.1 已落地（aok02_matter_ac，2026-08-20）
1. **入网失败重试**：`_rejoin_timeout_event_handler` 超时后重启 Thread 栈
   （`otThreadSetEnabled(false/true)`）并无限重试，满足 Spec §11.8.4 的
   5 分钟要求；`kConnectivity_Lost` 也启动同一看门狗
2. **上电标记关键属性 dirty**：Init 后调用
   `MatterReportingAttributeChangeCallback`（OnOff、CurrentLevel、
   RGB 的 Hue/Sat/X/Y），保证订阅恢复后 priming report 一次带全最新值，
   免控制器补一轮 Read
### 8.2 建议落地
**① 入网重试同步到 bk01**（对应根因 2）：
```cpp
#define ATTACH_NETWORK_TIMEOUT_MS   15000  // 缩短到 15s
#define ATTACH_NETWORK_MAX_RETRIES  3
static void _rejoin_timeout_event_handler(app_event_t * ev)
{
    static uint8_t retry_count = 0;
    if (retry_count < ATTACH_NETWORK_MAX_RETRIES) {
        retry_count++;
        LOG_MSG_INFO(TAG_NWK, "rejoin retry %d", retry_count);
        ConnectivityMgr().SetThreadEnabled(false);
        vTaskDelay(pdMS_TO_TICKS(500));
        ConnectivityMgr().SetThreadEnabled(true);
        ev_set_delay_ms(ev, ATTACH_NETWORK_TIMEOUT_MS);
    } else {
        LOG_MSG_ERR(TAG_NWK, "rejoin failed after %d retries", retry_count);
        retry_count = 0;
        // 可选: 短暂打开 BLE 广播，提示用户设备在线但未入网
    }
}
```
**② Thread 连接建立后强制 SRP 重注册**（对应根因 3，绕过 mDNS 缓存）：
思路：在 `kConnectivity_Established` 事件中
`DnssdServer::Instance().StopServer()` → 延时 500ms（确保 Border Router
处理删除请求，避免 Update 被合并为 no-op）→ `StartServer()`。
Stop/Start 内部触发 `otSrpClientRemoveService()` / `otSrpClientAddService()`
两次 SRP Update，迫使 Border Router 立即刷新 mDNS 记录。
层级选择：
| 方案 | 层级 | 优点 | 缺点 |
|------|------|------|------|
| DnssdServer Stop/Start | Matter App 层 | 改动最小（2 个函数调用） | 依赖 DnssdServer 组件初始化顺序；若内部幂等检查跳过已运行服务则失效 |
| 直接调 OT SRP Client API | OpenThread 层 | 最直接、零额外延迟 | 平台绑定（仅 Thread），不可移植到 Wi-Fi |
| Advertiser API 重发布 | Matter SDK 层 | 跨平台标准 API | API 较复杂，需实例名等上下文 |
推荐先用 DnssdServer 方案，若发现幂等跳过则改用 OT SRP Client 方案。
> ⚠️ **修订说明**：原报告方案 A2 代码中
> `otSrpClientStart(otInst, hostInfo->mName, hostInfo->mState)` 的 API
> 签名有误（实际为 `otSrpClientStart(otInstance*, const otSockAddr*)`），
> 方案 A3 中的 `advertiser->GetInstanceName()` 也非真实 SDK API。
> 本版不保留具体伪代码，落地时以所用 SDK 版本头文件为准。
**③ MCU 状态主动上报**（配合 §5.3）：
入网成功后（`app_comm_mgr_notify_nwk_status(kNwkStatusJoined)`）主动查询
MCU 全量状态（Battery / Curtain % / Operational Status），确保控制器订阅后
立即可用最新属性值。同时 MCU 可控制 LED 由闪烁变常亮，给用户/安装人员
即时反馈。
### 8.3 可选实验（未实施）
**"温和助推"**：检测到订阅 torn down（0x7d）后 N 秒内无新 CASE →
Thread detach + reattach 一次，迫使 SRP 重注册 + mDNS 重公告，可能提前
唤醒控制器发现监听。
- 风险：打断其他控制器的既有会话/订阅；只能限定在"拆除后、重连前"窗口执行
- **是否实施取决于实测自愈时长——若控制器通常 2 分钟内自发重连，无需任何代码**
### 8.4 其他建议
- **区分"凭据丢失"与"临时连接失败"**：打开配网窗口前先按 §11.8.4 多次
  尝试恢复；仅当 `IsThreadProvisioned()=false` 确认凭据丢失时才开窗口
- **NVM3 优化**：减小 `KVS_MAX_ENTRIES`（当前 511 可能过多）；定期触发
  Repack 防碎片化；利用延迟批量写入减少 Page 擦除
- **不建议**：DNS-SD TXT 自定义 boot counter（非标准、侵入大）；已入网
  设备常开 BLE 配网广播（违反 Spec §5.4.2.5）
---

## 9. 端到端延迟总结
### 9.1 典型场景（bk01 实测，Thread Up → 可控制 ~4.7s）
```
T+0s       电源接通
T+0.07s    FreeRTOS + OT/BLE/Matter Stack 就绪（实测 67ms）
           [读 NVM3: Thread 凭据 / Fabric / 订阅元数据 / Resumption 记录]
T+~14.3s*  Thread Attach 开始（*log 含前序启动段，Attach 本身 2-3s）
T+14.4s    SRP Client 启动（Thread Up 后 82ms）
T+14.9s    DNS-SD 发布完成（568ms）  ← 设备已可接受 Matter 命令
T+18.2s    控制器发 CASE Sigma1（感知延迟 ~3.2s，占全程 68%）
T+18.6s    Session Active（Sigma2Resume，仅 409ms）
T+19.1s    首条命令执行成功（Descriptor PartsList, Cluster 0x0029 Cmd 0x0004）
                                                        ✓ 用户可正常控制
```
### 9.2 最坏场景（~90–140s+）
```
T+0~1s     Boot（含 NVM3 Repack）
T+0.7~20s  Thread Attach（父节点不可达，多轮 Discover 重扫）
T+20~31s   SRP 注册 + DNS-SD 发布
T+31~91s   控制器纯被动等待（订阅 MaxInterval 60s + mDNS TTL 部分过期）
T+93s      控制器 DNS-SD + CASE + Subscribe 完成
设备侧 ~22s + 控制器侧 ~70s
若 30s 内 Attach 未成功且无重试 → 设备永久离线（bk01 当前缺陷，§4.2）
```
### 9.3 延迟因素占比
| 因素 | 延迟占比 | 对应根因 |
|------|---------|---------|
| 控制器被动发现（MRP 超时 + 订阅超时 + DNS-SD） | 50–70%（~10–60s） | 根因 1 |
| Thread 网络入网 | 10–20%（~3–30s） | 根因 2 |
| 入网失败无重试（缺陷场景） | 10–20% / 可致永久离线 | 根因 2 |
| CASE + 订阅重建 | 5–10%（~2–5s） | 根因 1 |
| SRP/mDNS 缓存 | 叠加放大（最长 120s） | 根因 3 |
### 9.4 如果"几分钟"延迟持续发生，排查顺序
1. 设备 log 是否反复出现 `rejoin failed` → 网络层问题 / 无重试缺陷（最可确定的软件缺陷）
2. Border Router 的 SRP/mDNS 缓存 TTL 是否过大（RFC 6762 §7.1 默认 120s）
3. 手机 APP 生态实现中的额外超时等待（各生态不同）
4. Thread 拓扑是否不稳定（Router/Parent 频繁切换）
5. NVM3 是否 Page 损坏导致凭据读取失败 → 设备回退配网模式（Spec §5.4.2）
6. 是否命中 0x7d 订阅恢复失败路径（控制器侧丢状态，§6.4）
---
## 10. 附录
### 附录 A：文件索引
| 文件 | 描述 |
|------|------|
| src/main.cpp | 程序入口，boot 流程 |
| src/app/AppTask.cpp | 主任务，初始化调度 |
| **src/app/app_nwk_mgr.cpp** | **网络管理器（核心分析文件）** |
| src/app/app_comm_mgr.cpp | 串口通信管理器（与 MCU） |
| src/app/app_spm_mgr.cpp | Matter 串口协议消息处理器 |
| include/CHIPProjectConfig.h | **Matter 项目配置（关键）** |
| config/app/AppBuildConfig.h | **订阅/会话恢复配置（关键）** |
| config/sl_matter_icd_config.h | ICD/SED 配置 |
| config/sl_openthread_features_config.h | **OpenThread 配置** |
| config/nvm3_default_config.h | NVM3 Flash 存储配置 |
| spec/23-27349-009_Matter-1.5-Core-Specification.pdf | Matter 1.5 核心规范 |
| spec/23-27351-008_Matter-1.5-Device-Library-Specification.pdf | Matter 1.5 设备库规范 |
| recovery/log-subscriptions-resume.md | aok02 订阅恢复完整日志 |
### 附录 B：Spec 章节索引（章节号请与 Matter 1.5 正式版核对）
| 章节 | 内容 | 关联章节 |
|------|------|---------|
| §4.14.1 | PASE（配网临时会话，Spake2+，60s 内完成） | §3 |
| §4.14.2 | CASE Sigma 协议（0x30/0x31/0x32） | §6.2 |
| §4.14.2.7 | Session Resumption（0x33）——**恢复记录可持久化** | §6.2（修正） |
| §5.4.2.3.1 | 配网窗口 180–900s（本项目 300s ✓） | §8.4 |
| §5.4.2.5 | 已入网设备禁用 BLE 配网 | 根因 4 |
| §5.6 | Operational 模式下可选维持 BLE 广播 | 根因 4 |
| §8.5.2 | Subscribe/Report（0x03/0x04/0x05），MaxInterval 超时 | §6.1/§6.3 |
| §8.5.3 | 订阅持久化与 InvalidSubscription 处理 | §6.3/§6.4/根因 6 |
| §9.15 | ICD Management（Check-In 0x50，仅 ICD 适用） | §6.4 |
| §11.8 | Thread 集成（Thread 1.3+ 强制） | §4 |
| §11.8.2 | Thread 凭据/Fabric/Group Key 持久化于 NVM | §3/根因 5 |
| §11.8.4 | 网络恢复应重试 ≥5 分钟（**当前 30s 无重试，违反建议**） | §4.2 |
| §11.9 | DNS-SD 广告与发现（`_matter._tcp` / `_matterc._udp`） | 根因 3 |
| §11.9.5.2 | Thread 设备用 SRP 注册服务（意译，非原文引用） | 根因 3/§8.2 |
| §11.9.6 | Operational TXT 记录（VP/PP/D/CM 等） | 根因 3 |
| §11.9.8 | SRP 租约（Service 2h / Key 14d） | 根因 3 |
| §11.10.7.2 | ArmFailSafe（默认 60s，可延长） | §3 |
| RFC 6762 §7.1 | mDNS 缓存 TTL 默认 120s | 根因 3 |
**Spec 合规性检查**：
| 参数 | Spec 要求 | 本项目 | 合规性 |
|------|----------|--------|--------|
| Basic Commissioning Window | 180–900s | 300s | ✓ |
| BLE Fast Advertising Interval | 20–60ms（前 30s） | 25ms | ✓ |
| BLE Slow Advertising Interval | 150–1285ms（30s 后） | 500ms | ✓ |
| Thread Attach 重试时间 | 建议至少 5 分钟 | **30s 且无重试** | **⚠️ 违反 Spec 建议（aok02 已修复）** |
| SRP 租约 | Service 2h / Key 14d | OT 默认 | ✓ |

### 附录 C：SDK 关键文件索引
**Matter SDK (connectedhomeip)**：
| 文件 | 涉及环节 |
|------|---------|
| `src/transport/SessionManager.*` | 会话生命周期，unknown session 丢弃逻辑 |
| `src/transport/SecureSession.*` | 会话状态（仅存 RAM） |
| `src/transport/CASEClient.cpp` / `CASEServer.cpp` | CASE 握手（Sigma1/2/3、Sigma2Resume） |
| `src/messaging/ReliableMessageMgr.cpp` | MRP 重传（控制器感知超时的来源） |
| `src/messaging/ReliableMessageProtocolConfig.h` | MRP 参数（MAX_RETRANS=4 等） |
| `src/app/ReadClient.cpp` | 订阅客户端（OnMaxIntervalTimeout 等） |
| `src/app/InteractionModelEngine.cpp` | 订阅恢复（GetSubscriptionResumptionInfo） |
| `src/app/DnssdServer.cpp` / `src/lib/dnssd/*` | DNS-SD 服务管理 |
| `src/platform/silabs/DnssdImpl.cpp` | 对接 OpenThread SRP |
| `src/platform/silabs/ThreadStackManagerImpl.cpp` | OT 状态回调映射 |
| `src/platform/silabs/ConnectivityManagerImpl.cpp` | IsThreadProvisioned() 判断 |
| `src/platform/silabs/SilabsConfig.*` | NVM3 KVS 读写 |
**OpenThread SDK**：
| 文件 | 涉及环节 |
|------|---------|
| `src/core/thread/mle.cpp` | MLE Attach（Discover / ChildIdRequest） |
| `src/core/mac/mac.cpp` / `sub_mac.cpp` | 信道扫描 / CSL 同步 |
| `src/core/net/srp_client.cpp` | SRP Client（AddService / SendUpdate） |
| `include/openthread/srp_client.h` / `thread.h` / `instance.h` | 公共 API |
**Silicon Labs GSDK**：
| 文件 | 涉及环节 |
|------|---------|
| `platform/emdrv/nvm3/`（GSDK 4.x）或 `protocol/nvm3/`（Simplicity SDK） | NVM3 Flash 读写 |
### 附录 D：bk01 真实恢复 Log 完整分析（2026-05）
**完整时间线**：
```
时间戳     事件
────────── ──────────────────────────────────────────────────────────
14.363     Thread 状态变化 (event 32779)
14.364     kThreadConnectivityChange (event 32769)
14.365   ★ Thread Established — 设备侧就绪
14.365     Scheduling OTA Requestor initialization（第一次调度）
14.365     Joining Multicast groups
14.447     SRP Client started, detected server: fd11:9c64:dd37:b8c4:...
14.448-449 Thread 状态变化 ×2 (event 32779 ×2)
14.506-579 ★★★ 旧会话数据被丢弃: "unknown session (LSID=36120)" ×4
14.844     SPP re-sent count 1 (CMD 0x02 SN=0x0000)
14.933     DNS-SD initialized (event 32786)
14.933   ★ Server initialization complete
14.934     Advertise operational node 52017B57FC1E977B-00000000000008CA
14.935     Operational network ready (event 32790)
14.945     No subscriptions to resume
15.344     SPP re-sent count 2
15.845     SPP re-sent reach to max → SN 递增为 0x0001
16.346-17.346  SPP 第二轮重传（count 1/2 → max）
17.935     DNS-SD Resolving 52017B57FC1E977B:0000000000000001
18.027     Node ID resolved: UDP:[fd7a:e86b:...]:5540
18.155   ★ CASE Sigma1（控制器 → 设备）MsgID 0x30
18.551   ★ CASE Sigma2Resume（设备 → 控制器）MsgID 0x33（Resumption 生效）
18.559     StatusReport (0x40)
18.564   ★ SecureSession Active (LSID:25475)
18.565     Stopping watchdog timer
18.569     IM:InvokeCommandRequest → Endpoint=0 Cluster=0x0029 Cmd=0x0004
           （Descriptor/PartsList — 控制器先验证设备能力的标准行为）
19.077     IM:InvokeCommandResponse → Status=0x0（成功）
19.080     StandaloneAck
17.847-18.847  SPP 第三轮重传（与 CASE 恢复完全并行）
```
**关键里程碑与耗时**：
| 阶段 | 起止时间戳 | 耗时 | 说明 |
|------|-----------|------|------|
| Thread Up → SRP Started | 14.365 → 14.447 | 82ms | SRP Client 连接 Border Router |
| Thread Up → DNS-SD Ready | 14.365 → 14.933 | 568ms | DNS-SD 初始化和发布 |
| Thread Up → CASE Sigma1 | 14.365 → 18.155 | **3.79s** | **控制器侧反应时间** |
| Sigma1 → Session Active | 18.155 → 18.564 | **409ms** | CASE Resumption 极速恢复 |
| Session Active → First Cmd OK | 18.564 → 19.077 | 513ms | Descriptor 查询往返 |
| **总计：Thread Up → 可控制** | 14.365 → 19.077 | **4.71s** | ★ 正常场景完整恢复时间 |
**六项关键发现**：
1. **设备侧恢复极快（~0.5s）**：Thread Established → DNS-SD 发布 <1s
2. **控制器侧反应时间占主导（~3.8s，68%）**：从设备就绪到控制器发 Sigma1
3. **Session Resumption 工作正常**：Sigma2Resume (0x33) 响应，409ms 完成
   （远优于完整 Sigma 的 1.5–2s）
4. **旧会话消息被丢弃是必然的**（§5.2，非 bug）
5. **SPP 重传与网络恢复并发互不阻塞**（§5.3）
6. **本次无 Subscription 恢复**：`No subscriptions to resume` 说明重启前
   无持久化订阅数据（首次配网即断电 / 控制器未订阅 / 数据过期）
**与文档预估对比**：
| 阶段 | 预估 | 实测 | 偏差 |
|------|------|------|------|
| Thread Up → SRP/DNS-SD 就绪 | 0.1–2s | 0.57s | ✓ 吻合 |
| 控制器感知 + DNS-SD 发现 | 1–15s | ~3.2s | ✓ 吻合 |
| CASE 重建 | 0.5–1s | 0.41s | 略快 |
| 设备侧总恢复 | ~3s | ~0.5s | 比预估更快 |
| 端到端 | 3–13s | ~4.7s | ✓ 吻合正常场景 |
### 附录 E：缩写表
| 缩写 | 全称 | 说明 |
|------|------|------|
| CASE | Certificate Authenticated Session Establishment | 证书认证会话建立 |
| CSL | Coordinated Sampled Listening | 协调采样监听（Thread 1.2+） |
| ICD | Intermittently Connected Device | 间歇连接设备 |
| IM | Interaction Model | Matter 交互模型 |
| KVS | Key-Value Store | NVM3 内的键值存储 |
| MLE | Mesh Link Establishment | Thread 网格链路建立 |
| MRP | Message Reliability Protocol | 消息可靠协议 |
| MTD | Minimal Thread Device | 最小 Thread 设备 |
| NOC | Node Operational Certificate | 节点操作证书 |
| NVM3 | Non-Volatile Memory 3 | Silicon Labs Flash 存储系统 |
| SED | Sleepy End Device | 休眠终端设备 |
| SPP | Serial Port Protocol | MG24 与 MCU 间的串口通信协议 |
| SRP | Service Registration Protocol | Thread 服务注册协议 |
### 附录 F：数据来源标注
| 数据 | 来源 |
|------|------|
| Boot 67ms / unknown session ×4 / Sigma2Resume 409ms / SPP 重传参数 | bk01_matter 实测 log（2026-05） |
| 0x7d InvalidSubscription / torn down / 19s 等待时间线 | aok02_matter_ac 实测 log（2026-08-20） |
| 其余耗时区间 | 基于 SDK 代码路径与 Spec 约束的推算，已标注代码出处 |
---
## 修订记录
| 版本 | 日期 | 修订内容 |
|------|------|---------|
| v1 | 2026-05-23 | 初版（bk01 分析） |
| v1.1 | 2026-08-20 | 补充 aok02 订阅恢复失败路径（0x7d）实测 |
| **v2** | 2026-08-20 | **技术修正**：① CASE Resumption 持久化语义（消除与实测 log 的矛盾）；② 控制器侧感知机制（MRP 超时，非 SESSION_NOT_FOUND）；③ KeepSubscriptions 字段语义；④ PERSIST_SUBSCRIPTIONS 与 Session Resumption 为独立机制；⑤ 标注原代码示例中的 API 签名错误；**结构重构**：摘要前置、根因去重、配置/事件/Spec/SDK 索引归入附录 |
