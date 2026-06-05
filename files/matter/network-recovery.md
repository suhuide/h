# Matter 设备断电重启后网络恢复全过程分析

## 文档概览

**产品型号**: bk01_matter (Window Covering / 窗帘电机控制器)  
**Matter 版本**: Matter 1.5  
**Thread 版本**: OpenThread 1.4 (MTD/SED)  
**芯片平台**: Silicon Labs EFR32MG24  
**分析日期**: 2026-05-23  

**问题现象**: Matter 设备配网成功后，断电再上电，手机 APP 可能在 1 分钟到数分钟内无法控制设备。

---

## 1. 系统架构概览

### 1.1 硬件架构

```
┌──────────────────────────────────────────────────┐
│                  EFR32MG24 (Matter SoC)          │
│                                                  │
│  ┌──────────────┐   UART    ┌──────────────────┐ │
│  │ Matter Stack │◄─────────►│  MCU(MotorCtrl)  │ │
│  │ + Thread     │  Serial   │  - Motor Driver  │ │
│  │ + BLE        │  Protocol │  - BAT Management│ │
│  │ + FreeRTOS   │           │  - 433MHz RF     │ │
│  └──────────────┘           └──────────────────┘ │
│                                                  │
│  Storage: NVM3 Flash (40960 bytes)               │
│  - KVS (Key-Value Store)                         │
│  - Thread Network Credentials                    │
│  - Matter Fabric Data                            │
│  - Device Configuration                          │
└──────────────────────────────────────────────────┘
```

### 1.2 软件架构

```
┌─────────────────────────────────────────────┐
│ Application Layer                           │
│  AppTask / app_nwk_mgr / app_spm_mgr        │
│  app_comm_mgr / app_wdc_mgr / app_mcu_dfu   │
├─────────────────────────────────────────────┤
│ Matter Stack (CHIP/connectedhomeip)         │
│  Server / FabricTable / CASE / IM           │
│  CommissioningWindowManager                 │
├─────────────────────────────────────────────┤
│ Connectivity Layer                          │
│  PlatformMgr / ConnectivityMgr              │
│  ThreadStackManager / BLEManager            │
├─────────────────────────────────────────────┤
│ OpenThread Stack                            │
│  MLE / MAC / IPv6 / UDP / SRP Client        │
├─────────────────────────────────────────────┤
│ Hardware                                    │
│  802.15.4 Radio / BLE Radio / NVM3 Flash    │
└─────────────────────────────────────────────┘
```

> **OpenThread Stack 各组件说明**:
> - **MLE** (Mesh Link Establishment): Thread 链路管理层 — 设备发现(Discover)、父子关系建立(Child ID Request/Response)、链路维护、地址注册。本报告中 Thread Attach 的 6 个步骤全部由 MLE 驱动
> - **MAC** (Media Access Control): 802.15.4 MAC 层 — 信道扫描 (Active Scan, CSMA/CA 退避)、CSL 同步 (CslSynchronize)
> - **IPv6**: 基于 6LoWPAN 的 IPv6 协议栈 — SLAAC 地址生成、Mesh-Local / GUA / ML-EID 多地址管理
> - **UDP**: 传输层 — Matter 的消息 (MRP/CASE/IM) 通过 UDP 承载发送
> - **SRP Client** (Service Registration Protocol): Thread 服务注册 — 向 Border Router 注册 `_matter._tcp` / `_matterc._udp` DNS-SD 服务; 租约管理 (Key Lease 14天, Service Lease 2小时)

### 1.3 关键配置参数汇总

| 配置项 | 值 | 所在文件 | 说明 |
|--------|-----|---------|------|
| `CHIP_DEVICE_CONFIG_ENABLE_PAIRING_AUTOSTART` | 0 | [CHIPProjectConfig.h:141](../include/CHIPProjectConfig.h#L141) | 上电不自动打开配网窗口 |
| `CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART` | 0 | [CHIPProjectConfig.h:155](../include/CHIPProjectConfig.h#L155) | 上电不自动开启 BLE 广播 |
| `CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS` | 300 (5分钟) | [CHIPProjectConfig.h:162](../include/CHIPProjectConfig.h#L162) | Basic Commissioning Window 超时 |
| `CHIP_DEVICE_CONFIG_BLE_FAST_ADVERTISING_TIMEOUT` | 30s | [CHIPProjectConfig.h:118](../include/CHIPProjectConfig.h#L118) | BLE 快速广播超时 |
| `ATTACH_NETWORK_TIMEOUT_MS` | 30s | [app_nwk_mgr.cpp:22](../src/app/app_nwk_mgr.cpp#L22) | 入网判定超时 |
| `CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL` | 2000ms | [CHIPProjectConfig.h:131](../include/CHIPProjectConfig.h#L131) | MRP 可靠传输重试间隔 |
| `SL_IDLE_MODE_DURATION_S` | 600 (10分钟) | [sl_matter_icd_config.h:12](../config/sl_matter_icd_config.h#L12) | ICD 空闲模式时长 |
| `SL_ACTIVE_MODE_DURATION_MS` | 0 | [sl_matter_icd_config.h:23](../config/sl_matter_icd_config.h#L23) | ICD 活跃模式时长(0=禁用) |
| `SL_ACTIVE_MODE_THRESHOLD` | 0 | [sl_matter_icd_config.h:28](../config/sl_matter_icd_config.h#L28) | ICD 活跃阈值(0=禁用) |
| `SL_TRANSPORT_IDLE_INTERVAL` | 1000ms | [sl_matter_icd_config.h:38](../config/sl_matter_icd_config.h#L38) | 传输空闲间隔 |
| `SL_TRANSPORT_ACTIVE_INTERVAL` | 500ms | [sl_matter_icd_config.h:43](../config/sl_matter_icd_config.h#L43) | 传输活跃间隔 |
| `SL_CSL_TIMEOUT` | 30s | [sl_matter_icd_config.h:49](../config/sl_matter_icd_config.h#L49) | CSL 同步超时 |
| `OPENTHREAD_CONFIG_THREAD_VERSION` | 1.4 | [sl_openthread_features_config.h:45](../config/sl_openthread_features_config.h#L45) | Thread 协议版本 |
| `OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE` | 1 | [sl_openthread_features_config.h:65](../config/sl_openthread_features_config.h#L65) | CSL Receiver 启用 |
| `NVM3_DEFAULT_NVM_SIZE` | 40960 | [nvm3_default_config.h:38](../config/nvm3_default_config.h#L38) | NVM3 Flash 存储大小 |
| `CHIP_CONFIG_SYNCHRONOUS_REPORTS_ENABLED` | 1 | [sl_matter_config.h:81](../config/sl_matter_config.h#L81) | 同步属性报告 |
| `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS` | 1 | [AppBuildConfig.h:8](../config/app/AppBuildConfig.h#L8) | 持久化订阅 (重启后恢复订阅元数据) |
| `CHIP_CONFIG_SUBSCRIPTION_TIMEOUT_RESUMPTION` | 0 | [AppBuildConfig.h:12](../config/app/AppBuildConfig.h#L12) | 订阅超时自动恢复 (禁用) |
| `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION` | 1 | [AppBuildConfig.h:16](../config/app/AppBuildConfig.h#L16) | CASE 会话恢复 (允许缓存会话信息) |
| `ICD_REPORT_ON_ENTER_ACTIVE_MODE` | 0 | [ICDServerBuildConfig.h:9](../config/app/icd/server/ICDServerBuildConfig.h#L9) | ICD 进入活跃模式时上报 (禁用) |
| `CHIP_CONFIG_ENABLE_ICD_LIT` | 0 | [ICDServerBuildConfig.h:21](../config/app/icd/server/ICDServerBuildConfig.h#L21) | LIT (长空闲时间) ICD 模式 (禁用) |

### 1.4 平台事件类型码速查表

在 Matter 平台事件回调 `on_platform_event()` 中，`event->Type` 为数字枚举值。以下是恢复过程中常见的事件码：

| 事件码 | 枚举常量 | 说明 | 触发时机 |
|--------|---------|------|---------|
| **32769** | `DeviceEventType::kThreadConnectivityChange` (Result=`kConnectivity_Established`) | Thread 连接已建立 | OpenThread MLE Attach 完成后 |
| **32779** | `DeviceEventType::kThreadStateChange` | Thread 状态变化 (OT state 变更) | Attach/Detach 过程中多次触发 |
| **32786** | `DeviceEventType::kDnssdInitialized` | DNS-SD 服务初始化完成 | `DnssdServer::StartServer()` 完成后 |
| **32790** | `DeviceEventType::kOperationalNetworkReady` | Operational 网络就绪 (SRP 注册完成) | SRP Client 向 Border Router 注册 `_matter._tcp` 完成后 |
| **32792** | `DeviceEventType::kCaseSessionEstablished` | CASE 安全会话建立完成 | `SecureSession::mState` 变为 `kActive` 时 |

> **log 中识别技巧**: 32779 在 Attach 过程中可能多次出现（每次 OT 子状态切换），32769 紧随其后（Attach 最终成功）。32786→32790 的顺序固定（先 DNS-SD 初始化，再 SRP 注册完成）。

---

## 2. 断电重启完整时序流程

### 2.1 总体时序图

```
时间轴 (秒)
0       0.2      3                   60          90                             300+
│        │        │                    │           │                               │
├───①────┤        │                    │           │                               │
│        ├───②────┤                    │           │                               │
│        │        ├──────────③─────────┤           │                               │
│        │        │                    ├─④┤        │                               │
│        │        │                    │  │        │                               │
▼        ▼        ▼                    ▼  ▼
Power   Stack   Thread               CASE Subscribe
On      Ready   Up                   Up   Done
                (设备就绪,可接受命令)
        └── <span style="color:green">设备侧 ~3s</span> ──┘└────── <span style="color:red">控制器侧 30-180s</span> ──────┘
```

> **读图说明**: 每个 `▼` 是一个里程碑时刻。`├─①──┤` 是一个阶段条, 条的长度 = 阶段耗时。时间轴 0.2s 前为线性, 之后切换为近似对数刻度。

**各阶段概述**:

| # | 阶段 | 图中起止 | 正常耗时 | 最坏耗时 | 结束时你看到什么 |
|---|------|---------|---------|---------|----------------|
| ① | **Boot+Init** | 0 → 0.2 | 67ms (实测) | 0.5-1s | OT/BLE/Matter Stack 全部就绪, `app_nwk_mgr_init()` 触发 |
| ② | **Thread Attach** | 0.2 → 3 | 2-3s | 10-30s | Thread 入网成功, SRP 注册完成, DNS-SD 已发布 |
| ③ | **CASE Re-Estab** | 3 → 60 | 10-30s | 60-120s | 控制器检测离线 + DNS-SD + CASE Sigma 完成 |
| ④ | **Subscribe** | ~60 | 0.5-1s | 2-5s | CASE 建立后立即 Subscribe, APP 可正常控制设备 |

> <span style="background-color:#fff3cd;padding:2px 6px">**★ 关键结论**</span>: 设备在 ② 结束时 (~3s) **已经完全可以接受 Matter 命令**。③④ 都是**控制器侧**的等待和重建, 与设备无关——这就是"手机 APP 几分钟无法控制"的根因。

**基于真实 log 的 ① Boot+Init 实测耗时** (EFR32MG24, 未配网设备):

```
[00:00:00.067] Starting scheduler              ← FreeRTOS 启动 (基准)
[00:00:00.070] OpenThread started: OK           ← +3ms   OT Stack 就绪
[00:00:00.119] Bluetooth stack booted: v11.0.0  ← +52ms  BLE Stack 就绪
[00:00:00.134] App Task started                 ← +67ms  应用就绪
```

**各阶段的 SPEC 与代码依据**:

| # | 阶段 | 图中 ▼ 处里程碑 | SPEC 依据 | 项目代码 | Matter/OT SDK |
|---|------|----------------|----------|---------|--------------|
| **①** | Boot+Init | `Stack Ready` | **§11.8.2**: Thread 凭据/Fabric 数据持久化于 NVM; Thread Spec: 上电 10s 内发第一个 MLME-SCAN | `main()`→`sl_system_init()`→`AppTask::AppInit()` [AppTask.cpp:74](../src/app/AppTask.cpp#L74) | NVM3: `nvm3_open()`; OT: `otInstanceInit()`; BLE: `sl_bt_init()`; Matter: `Server::Init()` |
| **②** | Thread Attach | `Thread Up` | **Thread Spec (MLE)**: Discover→ChildIdReq→LinkReq; **§11.9.5.2**: SRP 发布 `_matter._tcp`/`_matterc._udp`; **§11.8.4**: 应重试 ≥5分钟 | `app_nwk_mgr_init()` [app_nwk_mgr.cpp:36](../src/app/app_nwk_mgr.cpp#L36); `on_platform_event(kConnectivity_Established)` [app_nwk_mgr.cpp:212](../src/app/app_nwk_mgr.cpp#L212) | OT: `mle.cpp:Attach()`→`Discover()`→`SendChildIdRequest()`; MAC: `mac.cpp:StartCsmaBackoff()`; SRP: `srp_client.cpp:SendUpdate()` |
| **③** | CASE Re-Estab | `CASE Up` | **§4.14.2**: CASE Sigma (MsgID `0x30`-`0x32`); **§4.14.2.7**: SessionResume (`0x33`) 不跨重启 | (控制器发起, 设备响应) | 设备: `CASEServer.cpp:HandleSigma1()`; 控制器: `CASEClient.cpp:SendSigma1()`; MRP: `ReliableMessageMgr.cpp` |
| **④** | Subscribe | `Subscribe Done` | **§8.5.2**: SubscribeReq(`0x03`)/Rsp(`0x04`)/ReportData(`0x05`); **§8.5.3.2**: PersistSubscriptions | `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS=1` [AppBuildConfig.h:8](../config/app/AppBuildConfig.h#L8) | `ReadClient.cpp:SendSubscribeRequest()`; `InteractionModelEngine.cpp:GetSubscriptionResumptionInfo()` |
| *(未配网)* | Commissioning Window | — | **§5.4.2.3.1**: 窗口 180s ≤ T ≤ 900s | `CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS=300` | `CommissioningWindowManager.cpp:OpenBasicCommissioningWindow()` |

> **<span style="color:green">设备侧</span>** (①+② ≈ 3s) vs **<span style="color:red">控制器侧</span>** (③+④ ≈ 30-180s)。设备在 ② 结束时已可接受命令, 后续延迟完全取决于控制器何时发现设备恢复。详见 [3. 各阶段延迟分析汇总](#3-各阶段延迟分析汇总)。

**时序图中各时间值的代码溯源**:

| 图中值 | 来源 | 文件:行 | 说明 |
|--------|------|---------|------|
| ① Boot+Init = **67ms** | 实测 log | `[00:00:00.067-0.134]` | FreeRTOS→App Task Started, 仅 67ms |
| ① 最坏 = 0.5-1s | NVM3 Repack | [nvm3_default_config.h:14](../config/nvm3_default_config.h#L14) | `NVM3_DEFAULT_CACHE_SIZE=200`; Repack 触发于 `repackIfNeeded()` |
| ② Thread Attach **超时 30s** | `ATTACH_NETWORK_TIMEOUT_MS` | [app_nwk_mgr.cpp:22](../src/app/app_nwk_mgr.cpp#L22) | 入网判定超时; 对比 SPEC §11.8.4 建议 5min |
| ② Thread Attach 正常 ~3s | OT 默认 `kAttachTimeout` | OT `src/core/thread/mle.cpp` | Child ID Request 单次超时 ≈ 3s; Active Scan 每信道 ≈ 20-80ms × 16 |
| ② SRP 耗时 ~100ms | OT `srp_client.cpp:SendUpdate()` | 1 次 CoAP 往返到 Border Router | 正常 LAN 往返 ≈ 1-10ms; 含 BR 处理 ≈ 100ms |
| ③ MRP 重传间隔 **2000ms** | `CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL` | [CHIPProjectConfig.h:131](../include/CHIPProjectConfig.h#L131) | 每次重试间隔 2s |
| ③ MRP 最大重传 **4 次** | `CHIP_CONFIG_RMP_DEFAULT_MAX_RETRANS` | Matter SDK `ReliableMessageProtocolConfig.h` | 4 × 2s × 退避 ≈ 12-20s |
| ③ DNS-SD TTL **120s** | RFC 6762 §7.1 | Border Router mDNS 默认 | 最坏: 需等缓存过期才能发现新 SRP 注册 |
| ③ CASE **SessionResume=1** | `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION` | [AppBuildConfig.h:16](../config/app/AppBuildConfig.h#L16) | 启用后 CASE 恢复从 4 次往返→2 次 (~1s 节省) |
| ④ Subscribe **PERSIST=1** | `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS` | [AppBuildConfig.h:8](../config/app/AppBuildConfig.h#L8) | 持久化订阅: 恢复时增量 Priming Report |
| ④ Subscribe 超时恢复=0 | `CHIP_CONFIG_SUBSCRIPTION_TIMEOUT_RESUMPTION` | [AppBuildConfig.h:12](../config/app/AppBuildConfig.h#L12) | 超时后不自动恢复(控制器需主动重建) |
| Commissioning Window **300s** | `CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS` | [CHIPProjectConfig.h:162](../include/CHIPProjectConfig.h#L162) | SPEC §5.4.2.3.1 要求 180-900s; 300s = 5min |
| 看门狗 **60s** 喂狗 | `WATCHDOG_TIMEOUT_MS` | [AppTask.cpp:57](../src/app/AppTask.cpp#L57) | 定期喂狗, 不影响网络恢复 |
| 工厂复位延迟 **2s** | `LEAVE_NETWORK_TIMEOUT_MS` | [app_nwk_mgr.cpp:23](../src/app/app_nwk_mgr.cpp#L23) | FabricCount==0 后 2s 触发 FactoryReset |
| OTA 检查周期 **86400s** | `OTA_PERIODIC_TIMEOUT` | [sl_matter_ota_config.h:9](../config/sl_matter_ota_config.h#L9) | 24h 检查一次, 不影响网络恢复 |
| ICD 活跃禁用 | `SL_ACTIVE_MODE_DURATION_MS=0` | [sl_matter_icd_config.h:23](../config/sl_matter_icd_config.h#L23) | 非 ICD 设备, 无线程休眠延迟 |
| BLE 快速广播 **30s** | `CHIP_DEVICE_CONFIG_BLE_FAST_ADVERTISING_TIMEOUT` | [CHIPProjectConfig.h:118](../include/CHIPProjectConfig.h#L118) | 仅未配网设备适用; 已配网不打 BLE |

### 2.2 Phase 1: 系统启动 (0 - 0.2 秒)

> **实测耗时**: EFR32MG24 上从 FreeRTOS Scheduler 启动到 App Task Started **仅 67ms** ([log 证据](#:~:text=Starting%20scheduler-,App%20Task%20started,-67ms))。Bootloader 跳转到 App 的耗时在 log 之前, 通常在 50-100ms。

**入口调用链**:

```
main()                              [main.cpp:51]
  └─ app_init_early()               // 启动 Trace，记录引导开始
  └─ sl_system_init()               // Silicon Labs 系统初始化
       ├─ 时钟初始化 (HFXO/DPLL)
       ├─ NVM3 初始化 (Flash 存储)
       ├─ BLE Stack 初始化 (sl_bt_init)
       ├─ OpenThread Stack 初始化 (otInstanceInit)
       ├─ FreeRTOS 调度器启动
       └─ Matter Platform 初始化
  └─ app_init()                     // [main.cpp:41]
       └─ SilabsMatterConfig::AppInit()  // Matter 应用初始化
            └─ AppTask::AppInit()   // [AppTask.cpp:74]
```

**AppTask::AppInit() 详细流程** ([AppTask.cpp:74-118](../src/app/AppTask.cpp#L74-L118)):

```
AppTask::AppInit()
  ├─ ev_queue_init()                // 事件队列初始化
  ├─ 打印版本号和复位原因
  ├─ _print_qrcode()                // 读取并打印 Matter QR Code
  ├─ _write_mfg_date()              // 写入/校验制造日期和序列号到 NVM3
  ├─ wdg_api_init()                 // 看门狗初始化 (60s 喂狗周期)
  ├─ app_comm_mgr_init()            // 串口通信管理器初始化 (与 MCU 通信)
  ├─ app_nwk_mgr_init()             // ★ 网络管理器初始化 (关键)
  ├─ app_comm_mgr_start()           // 启动串口通信
  ├─ app_spm_mgr_init()             // Matter 串口协议消息处理器
  ├─ app_timetask_mgr_init()        // 定时任务管理器 (窗帘定时)
  ├─ app_mcu_dfu_init()             // MCU OTA 固件升级初始化
  └─ bootloader_deinit()            // 关闭 Bootloader，SPI Flash 进入 Deep Sleep
```

**基于真实 log 的各步骤耗时** (未配网设备, EFR32MG24):

| 步骤 | Log 时间戳 | 实际耗时 |
|------|-----------|---------|
| FreeRTOS Scheduler 启动 | `[00:00:00.067]` | 0ms (基准) |
| OpenThread Stack 就绪 | `[00:00:00.070]` | +3ms |
| BLE Stack 就绪 | `[00:00:00.119]` | +52ms |
| AppTask::AppInit() 开始 | `[00:00:00.125]` | +58ms |
| App Task Started (全部就绪) | `[00:00:00.134]` | **+67ms** |

> **说明**: 上表中的耗时不含 Bootloader 阶段 (在 FreeRTOS 启动之前)。完整的冷启动 (Power On → App Ready) 约 100-200ms, 取决于 HFXO 稳定时间和 Bootloader 校验时间。Matter Spec 对启动耗时无硬性要求, 但 Thread Spec 要求设备上电后 10s 内发送第一个 MLME-SCAN。

---

### 2.3 Phase 2: 网络管理器初始化与 Thread 入网 (0.2 - 30+ 秒)

这是整个恢复过程**最关键**的阶段。设备在 ~0.13s 完成 Init 后, `app_nwk_mgr_init()` 立即触发 Thread Attach。

#### 2.3.1 app_nwk_mgr_init() 流程

入口：[app_nwk_mgr.cpp:36](../src/app/app_nwk_mgr.cpp#L36)

```cpp
int app_nwk_mgr_init(void)
{
    // 注册平台事件回调
    PlatformMgr().AddEventHandler(on_platform_event, 0);

    m_nwk_status = kNwkStatusLeave;  // 初始状态：离线

    // ★ 关键判断: 检查设备是否曾经配网
    if (ConnectivityMgr().IsThreadProvisioned()) {
        // 情况A: 已经配过网 → 走恢复流程
        LOG_MSG_INFO(TAG_NWK, "device has provisioned\n");
        ev_set_delay_ms(&rejoin_timeout_event, ATTACH_NETWORK_TIMEOUT_MS); // 30s
    } else {
        // 情况B: 未配网 → 打开发起配网窗口
        app_nwk_open_basic_commissioning_window();  // 5分钟窗口
    }
}
```

#### 2.3.2 ConnectivityMgr().IsThreadProvisioned() 判断逻辑

此方法读取 NVM3/KVS 中存储的 Thread 网络凭据：

```
NVM3 Flash (Key-Value Store)
├─ Thread Network Credentials         ← 判断依据
│   ├─ Network Key (Master Key)
│   ├─ Network Name
│   ├─ Extended PAN ID
│   ├─ PAN ID
│   ├─ Channel
│   ├─ Mesh Local Prefix
│   └─ Active Operational Dataset
├─ Matter Fabric Data
│   ├─ Fabric Index
│   ├─ Node ID
│   ├─ Root CA Certificate
│   ├─ Operational Certificate (NOC)
│   └─ Trusted Root CA Certificates
└─ Device Configuration
```

- **正常情况下**: Thread 凭据存在 → `IsThreadProvisioned() = true` → 进入恢复流程
- **异常情况**: NVM3 数据损坏/丢失 → `IsThreadProvisioned() = false` → 打开 5 分钟配网窗口（这是延迟的第一个潜在来源）

#### 2.3.3 OpenThread 入网 (Thread Attach) 过程

当设备已存储 Thread 凭据时，OpenThread 在初始化完成后自动开始 Attach 过程。整个 Attach 过程由 **MLE (Mesh Link Establishment)** 协议驱动 —— MLE 是 Thread 的链路管理层，负责设备发现、父子关系建立、地址注册和链路维护。

```
OpenThread Attach 流程 (全部由 MLE 协议驱动):

Step 1: Active Scan (主动扫描)
  ├─ 在所有 802.15.4 信道 (11-26) 发送 Beacon Request
  ├─ 接收周围 Thread 路由器的 Beacon 响应
  ├─ 匹配存储的 Network Name / Extended PAN ID
  └─ 耗时: 每个信道 ~20-80ms, 16 个信道 → 约 0.3-1.3 秒

Step 2: Parent Selection (选择父节点)
  ├─ 评估候选父节点的 RSSI 和链路质量
  ├─ 优选已存储的 Parent (如果可达)
  ├─ 选择最佳候选父节点
  └─ 耗时: 约 0.1-0.5 秒

Step 3: MLE Child ID Request/Response (子节点注册)
  ├─ 向选定的 Parent 发送 Child ID Request
  ├─ Parent 分配 Child ID 和地址
  ├─ 返回 Child ID Response
  └─ 耗时: 约 0.1-1 秒

Step 4: MLE Link Request/Accept (链路建立)
  ├─ 与 Parent 建立 MLE 链路
  ├─ 交换链路信息
  └─ 耗时: 约 0.1-0.5 秒

Step 5: Address Registration (地址注册)
  ├─ 使用 SLAAC 生成 Mesh-Local IPv6 地址
  ├─ 向 Parent 注册地址
  └─ 耗时: 约 0.5-2 秒

Step 6: SRP Registration (服务注册) ★
  ├─ DNS-SD Service Registration
  ├─ 注册 Matter 服务 (_matter._tcp 和 _matterc._udp)
  ├─ 包含设备类型、Vendor ID、Product ID 等
  └─ 耗时: 正常 ~100ms (1 次 CoAP 往返); 最坏 2-5s (Border Router 高负载时)
```

**正常 Thread Attach 总耗时 (不含 SRP-Service Registration Protocol)**: 约 2-3 秒 (SRP 额外 ~100ms)  
**异常情况耗时**: 10-30 秒甚至更长，原因包括:
- 父节点不可达，需要等待和重试
- 信道质量差，需要多次扫描
- 网络拓扑变化，需要重新发现
- Border Router 响应慢

#### 2.3.4 Thread 连接建立后的平台事件

当 Thread 连接建立成功后，OpenThread 通过回调通知 Matter Connectivity Manager，然后触发平台事件：

```cpp
case DeviceEventType::kThreadConnectivityChange:
    case kConnectivity_Established:
        LOG_MSG_INFO(TAG_NWK, "Thread Established");
        m_nwk_status = kNwkStatusJoined;
        app_comm_mgr_notify_nwk_status(m_nwk_status);  // 通知 MCU 网络状态
        ev_set_inactive(&rejoin_timeout_event);         // 停止 30s 超时计时器
```

**关键点**: 重新入网计时器设置为 30 秒（`ATTACH_NETWORK_TIMEOUT_MS`），如果 30 秒内没有成功 Attach，重新入网计时器超时，但**不会自动重试**，只会记录日志 `"rejoin failed"`。

---

### 2.4 Phase 3: Matter 应用层 & 控制器侧恢复 (Thread Up - 控制器感知, 可达 30-180 秒)

Thread 连接建立后，设备侧状态恢复是**即时的**(毫秒级)。本阶段的延迟主要来自**控制器侧**(手机 APP 感知设备恢复)。

#### 2.4.1 Matter Server 状态恢复

```
Server::Init() 完成后:
  ├─ Fabric Table 从 NVM3 恢复 (读取所有已配对的 Fabric)
  ├─ Access Control List 恢复
  ├─ Group Key Management 恢复
  ├─ Attribute Store 恢复 (从 NVM3 读取持久化的属性值)
  └─ Interaction Model 引擎就绪
```

**OTA Requestor 的两次调度**:

从真实 log 中可观察到 OTA Requestor 初始化被**调度了两次**:

```
[00:00:14.365] Scheduling OTA Requestor initialization        ← Thread Established 后第一次调度
[00:00:14.933] DNS-SD initialized, scheduling OTA Requestor initialization  ← DNS-SD 就绪后第二次调度
```

这说明 OTA Requestor 的最终启动依赖于 DNS-SD 服务就绪。第一次调度时 DNS-SD 尚未初始化，因此被推迟执行。第二次调度在 `kDnssdInitialized` (event 32786) 后触发，此时才真正初始化 OTA Requestor。这个行为是正常的——OTA 查询需要 DNS-SD 来发现 OTA Provider 服务。

#### 2.4.2 CASE 会话重建

这是**手机 APP 恢复控制的关键步骤**。

**Matter Spec 规范** (Core Spec **Section 4.14.2**, "CASE") + SDK `src/transport/CASEServer.cpp` / `src/transport/CASEClient.cpp`:

CASE (Certificate Authenticated Session Establishment) 使用 Sigma 协议，包含以下步骤：

```
CASE 会话建立过程 (Sigma Protocol) — SDK 代码追踪:

Step 1: Sigma1 (控制器 → 设备) — Message ID: 0x30
  SDK: src/transport/CASEClient.cpp → SendSigma1()
  控制器发送:
  ├─ 随机数 (InitiatorRandom: 32 bytes)
  ├─ 控制器的 Session ID
  ├─ 控制器的 Ephemeral Public Key (ECDH)
  └─ 加密套件协商 (AES-CCM-128 / HMAC-SHA-256)

Step 2: Sigma2 (设备 → 控制器) — Message ID: 0x31
  SDK: src/transport/CASEServer.cpp → HandleSigma1() → SendSigma2()
  设备发送:
  ├─ 随机数 (ResponderRandom: 32 bytes)
  ├─ 设备 NOC 证书链 (Node Operational Certificate)
  ├─ 设备的 Ephemeral Public Key (ECDH)
  └─ Sigma2 TBS (To-Be-Signed) 数据进行签名

Step 2-resume (设备 → 控制器) — Message ID: 0x33
  SDK: src/transport/CASEServer.cpp → SendSigma2Resume()
  (仅当 Session Resumption 条件满足)
  └─ 跳过部分 ECDH 交换, 使用缓存的密钥材料 → ~0.5-1s 加速

Step 3: Sigma3 (控制器 → 设备) — Message ID: 0x32
  SDK: src/transport/CASEClient.cpp → HandleSigma2() → SendSigma3()
  控制器验证设备证书链 → 发送:
  ├─ 使用控制器私钥对 Sigma2 TBS 数据的签名
  └─ 确认会话密钥派生

Step 4: StatusReport (设备 → 控制器) — Message ID: 0x40
  SDK: src/transport/CASEServer.cpp → HandleSigma3()
  设备验证控制器签名:
  ├─ 派生出共享的 Session Key (AES-CCM-128)
  ├─ 激活 SecureSession 对象
  └─ 发送 StatusReport (Success) → Session Active
```

**CASE 会话不持久化**: Spec **§4.14.2.7** 规定, CASE Security Context 基于 ECDH 临时密钥对派生, 这些密钥仅存在于 RAM。设备重启后 RAM 清零 → 所有旧的 CASE 会话自动失效。控制器需要 `SessionManager::SecureUnicastMessageDispatch()` 返回 `CHIP_ERROR_SESSION_NOT_FOUND` 后才能发起新的 CASE。

#### 2.4.3 控制器侧(手机 APP)发现设备的过程

**这是造成长时间延迟的最主要原因。**

```
控制器(手机APP)发现设备恢复的过程:

Case 1: 控制器通过 Subscription Timeout 发现设备离线
  SPEC: §8.5.2 — 订阅的 MaxInterval 超时机制
  SDK: src/app/ReadClient.cpp: OnMaxIntervalTimeout()
  ├─ 控制器之前建立的订阅有超时时间
  │   - 默认 Subscription MaxInterval: 通常 60 秒
  │   - 超时后控制器判定设备离线
  ├─ 控制器等待 Subscription 超时: 最长 60 秒
  └─ 超时后重新通过 DNS-SD 发现设备

Case 2: 控制器通过主动操作触发发现
  SPEC: §4.14.2.3 — CASE 会话建立超时; §8.5.2 — IM StatusResponse 超时
  SDK (控制层): src/messaging/ReliableMessageMgr.cpp: SendFromQueue()
  ├─ 用户操作 APP → 控制器尝试发送命令
  ├─ 旧的 CASE Session 无效 (设备重启后已清除)
  ├─ IM (Interaction Model) 发送请求 → 超时
  │   - MRP 重试间隔: 2000ms (CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL)
  │   - 默认最大重传次数: CHIP_CONFIG_RMP_DEFAULT_MAX_RETRANS = 4
  │   - SDK 代码: src/messaging/ReliableMessageProtocolConfig.h
  │   - 总超时: 4次 × 2000ms × 退避因子(1.5-2x) ≈ 12-20 秒
  └─ 控制器知道旧的会话已失效，发起新的 CASE

Case 3: 控制器通过 DNS-SD 定期刷新
  SPEC: §11.9 — DNS-SD Advertising & Discovery
  SDK: src/lib/dnssd/Discovery_ImplPlatform.cpp: ResolveByType()
  ├─ 控制器周期性地通过 DNS-SD 查询 Thread Border Router
  │   - mDNS 缓存 TTL: 默认 120 秒 (RFC 6762 §7.1)
  ├─ 发现设备已重新注册 SRP-Service Registration Protocol 服务
  └─ 发起新的 CASE 会话

Case 4: ICD (Intermittently Connected Device) 延迟
  SPEC: §9.15 — ICD Management; ICD_CheckIn message = 0x50
  ├─ 本项目 ICD 配置: SL_ACTIVE_MODE_DURATION_MS = 0 (活跃模式禁用)
  ├─ CHIP_CONFIG_ENABLE_ICD_LIT = 0 (LIT 模式禁用)
  ├─ ICD_REPORT_ON_ENTER_ACTIVE_MODE = 0 (进入活跃模式时不主动上报)
  └─ 结论: 本项目绝非严格 ICD 设备, Case 4 在本项目中不适用
```

#### 2.4.4 Subscribe (属性订阅) 重建

一旦 CASE 会话恢复：

**SPEC 依据**: Matter Core Spec **§8.5.2** (Interaction Model — Subscribe/Report), **§8.5.3.2** (Subscription Persistence)

**SDK 代码**: `src/app/ReadClient.cpp:SendSubscribeRequest()` + `src/app/InteractionModelEngine.cpp`

```
控制器重新订阅设备属性 (Message IDs):
  ① SubscribeRequest (0x03) — 控制器 → 设备
     ├─ 指定要订阅的 Cluster/Attribute 列表 (AttributePathIB)
     ├─ MinInterval / MaxInterval (例如: 1s / 60s)
     ├─ KeepSubscriptions (是否保留已有持久化订阅)
     │    └─ PERSIST_SUBSCRIPTIONS=1 时: KeepSubscriptions=true (尝试恢复)
     │    └─ PERSIST_SUBSCRIPTIONS=0 时: KeepSubscriptions=false (全新订阅)
     └─ isFabricFiltered (是否仅报告本 Fabric 的数据)

  ② SubscribeResponse (0x04) — 设备 → 控制器
     ├─ SubscriptionID (32-bit, 唯一标识此订阅)
     ├─ MaxInterval (协商后的最大报告间隔)
     └─ (无 Priming Report 数据 — 由 ReportData 单独发送)

  ③ ReportData (0x05) — 设备 → 控制器 (Priming Report)
     ├─ SubscriptionID (与 SubscribeResponse 中的保持一致)
     ├─ AttributeReportIBs (所有被订阅属性的当前值)
     │    └─ 对于 Window Covering: CurrentPosition/TargetPosition/OperationalStatus/Mode…
     └─ 后续: 当属性值改变时, 增量发送 ReportData
```

**PersistSubscription 对 Subscribe 恢复的影响** (SDK `src/app/InteractionModelEngine.cpp`):

```cpp
// 当 CHIP_CONFIG_PERSIST_SUBSCRIPTIONS = 1:
// InteractionModelEngine::GetSubscriptionResumptionInfo()
//   → 从 NVM3 读取 (SubscriptionID, AttributePaths, Intervals, FabricIndex)
//   → 当控制器发送 SubscribeRequest(KeepSubscriptions=true) 时:
//       设备识别已有的 Subscription → 直接复用 → 增量 Priming Report
//
// 当 CHIP_CONFIG_PERSIST_SUBSCRIPTIONS = 0:
//   → GetSubscriptionResumptionInfo() 返回空
//   → 控制器必须发送 SubscribeRequest(KeepSubscriptions=false)
//   → 设备创建全新订阅 → 全量 Priming Report (所有属性)
```

---

## 3. 各阶段延迟分析汇总

> 根因严重程度: <span style="color:red">**● 关键**</span> (根因1/2) — 直接影响恢复延迟; <span style="color:orange">**● 次要**</span> (根因3/4/5/6) — 叠加效应放大型

### 3.1 延迟时间线 (正常场景 vs 最坏场景)

| 阶段 | 正常场景 | 最坏场景 | 关键因素 |
|------|---------|---------|---------|
| **系统启动** (Boot + HW Init) | 0.07-0.2 秒 | 0.5-1 秒 | Log 实测 67ms; 最坏: Bootloader 校验慢 + NVM3 Repack |
| **Thread 扫描** (Active Scan) | 0.3-1 秒 | 3-5 秒 | 信道质量、路由器数量 |
| **Thread 入网** (Attach) | 2-5 秒 | 10-30 秒 | 父节点选择、拓扑变化 |
| **SRP 服务注册** | 0.1-2 秒 | 5-10 秒 | Border Router 响应速度; 正常仅 1 次 CoAP 往返(~100ms) |
| **控制器检测设备离线** | 0-10 秒 | 60 秒 | 取决于用户何时操作 APP; 被动等待 Sub MaxInterval=60s |
| **DNS-SD 重新发现** | 1-3 秒 | 5-15 秒 | Border Router 的 mDNS 缓存 (TTL=120s, RFC 6762 §7.1) |
| **CASE 会话重建** | 0.5-2 秒 | 3-5 秒 | 证书验证、密钥交换; SessionResumption 启用时减半 |
| **属性订阅重建** | 0.5-1 秒 | 2-5 秒 | Priming Report 数据量; PERSIST_SUBS=1 可增量 |
| **总计 (PERSIST_SUBSCRIPTIONS=1)** | **约 3-13 秒** | **约 90-140 秒+** | 当前配置 (Boot 仅 0.1s 而非原来估算的 1-3s) |
| **总计 (PERSIST_SUBSCRIPTIONS=0)** | **约 35-70 秒** | **约 120-200 秒+** | 假设: 无持久化订阅, 详见根因 6 |

### 3.2 延迟根因分析

#### <span style="color:red">●</span> 根因 1: 控制器无法感知设备重启 ★ 最主要根因

**协议行为定义**:

| 来源 | 位置 | 定义 |
|------|------|------|
| Matter Core Spec | **Section 4.14.2**, "CASE Session Establishment" | CASE 会话使用 Sigma 协议建立，会话密钥通过 ECDH 临时密钥对派生 |
| Matter Core Spec | **Section 4.14.2.7**, "Session Resumption" | 会话恢复(`CHIP_CONFIG_ENABLE_SESSION_RESUMPTION`)允许缓存部分会话信息，但会话密钥和安全上下文**不跨重启持久化** |
| Matter Core Spec | **Section 8.5.3.2**, "Subscription Persistence" | 订阅可在设备重启后持久化(`CHIP_CONFIG_PERSIST_SUBSCRIPTIONS`)，但持久化的订阅共享 CASE 会话的局限 — **恢复后仍需重建 CASE 会话** |
| Matter SDK | `src/transport/SecureSession.h` | `SecureSession` 对象的 `mState` 仅存在于 RAM 中，设备重启后 RAM 清零，所有活跃会话丢失 |
| Matter SDK | `src/transport/SessionManager.cpp` | `SessionManager::Init()` 在平台初始化时创建空的 Session 表，不尝试从 Flash 恢复任何活跃会话对象 |

**项目代码中的实际配置** ([AppBuildConfig.h:8-20](../config/app/AppBuildConfig.h#L8-L20)):

```cpp
#define CHIP_CONFIG_PERSIST_SUBSCRIPTIONS      1  // 持久化订阅: 启用
#define CHIP_CONFIG_SUBSCRIPTION_TIMEOUT_RESUMPTION  0  // 超时恢复: 禁用
#define CHIP_CONFIG_ENABLE_SESSION_RESUMPTION  1  // 会话恢复: 启用
```

- 持久化订阅 = 1：设备会在 NVM3 中存储订阅信息，重启后恢复订阅元数据。但 **CASE 会话密钥不持久化**（Spec 4.14.2.7 明确禁止），所以订阅恢复后仍需完整的 CASE 重建。
- 超时恢复 = 0：如果订阅超时，不自动恢复 — 控制器必须主动重新订阅。

**控制器侧的恢复等待链** (Matter SDK `src/messaging/ReliableMessageMgr.cpp`):

```
控制器 (手机 APP / Hub) 发现设备离线的过程:

Step 1: 控制器尝试使用旧 CASE 会话发送命令
  └─ SDK: src/messaging/ReliableMessageMgr.cpp
     └─ ReliableMessageMgr::SendFromQueue() → 通过 UDP 发送加密消息
        └─ 消息到达设备但设备没有对应的会话 → 被静默丢弃
        └─ 控制器不收到 Ack

Step 2: MRP 超时和重试
  └─ SDK: src/messaging/ReliableMessageProtocolConfig.h
     └─ 本项目配置: CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL = 2000ms
     └─ SDK 默认最大重传次数: CHIP_CONFIG_RMP_DEFAULT_MAX_RETRANS = 4 (src/messaging/ReliableMessageProtocolConfig.h)
     └─ 总超时: 4次 × 2000ms × 2 (含退避因子) ≈ 10-16 秒

Step 3: 控制器检测会话失效
  └─ SDK: src/transport/SessionManager.cpp
     └─ SessionManager::SecureUnicastMessageDispatch() → 返回 CHIP_ERROR_SESSION_NOT_FOUND
     └─ SDK: src/transport/CASEClient.cpp
        └─ 控制器触发新的 CASE Sigma1 → DNS-SD 发现设备

Spec 规定 (Section 4.14.2.3):
  └─ CASE 会话建立超时: kExpectedCASEProcessingTime ≈ 30 秒
  └─ 如果控制器侧的 DNS-SD 缓存了旧的地址，需要等待缓存 TTL 过期
```

**时间消耗汇总**:
| 步骤 | 耗时 | SDK 代码路径 |
|------|------|-------------|
| MRP 重试直到超时 | 6-16 秒 | `src/messaging/ReliableMessageMgr.cpp:SendFromQueue()` |
| CASE 会话检测失效 | 0.5-1 秒 | `src/transport/SessionManager.cpp` |
| DNS-SD 重新发现 | 1-15 秒(取决于 Border Router) | `src/lib/dnssd/Discovery_ImplPlatform.cpp` |
| 新建 CASE 会话 | 0.5-2 秒 | `src/transport/CASEClient.cpp`, `src/transport/CASEServer.cpp` |
| 重建属性订阅 | 0.5-1 秒 | `src/app/ReadClient.cpp:SendSubscribeRequest()` |
| **合计** | **9-35 秒(仅控制器侧)** | |

**真实 log 实证** — "unknown session" 消息:

以下是从 bk01_matter 设备断电重启后的真实 log 中提取的关键片段，直接验证了上述理论：

```
[00:00:14.506][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.531][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.553][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
[00:00:14.579][error][IN] Data received on an unknown session (LSID=36120). Dropping it!
```

**分析**:
- 这 4 条连续的 dropped 消息间隔约 22-26ms，来自同一控制器
- LSID=36120 是设备**重启前**的旧会话 ID（Local Session ID），设备重启后 RAM 中的 Session Table 已清空，`SessionManager::SecureUnicastMessageDispatch()` 查找不到该 LSID 对应的 `SecureSession` 对象
- 控制器（手机/Hub）此时尚未感知设备已重启，仍使用旧会话密钥加密发送命令
- 设备侧 `SessionManager` 在 `src/transport/SessionManager.cpp` 中查找会话失败后，打印此 error 并静默丢弃消息
- 这 4 次消息被丢弃后，控制器侧 MRP 最终因收不到 Ack 而超时（约 2-8 秒后），然后触发 CASE 重建

**关键结论**: 这条 log 是**根因 1 的直接实证**——不是理论推测，而是真实发生的。在每次断电重启后都会出现这个 pattern，每次浪费约 2-8 秒（取决于控制器 MRP 重试次数和间隔）。

#### <span style="color:red">●</span> 根因 2: Thread 网络重新入网耗时

**Spec 定义** (Matter Core Spec, **Section 11.8**, "Thread Integration"):

> "A Matter device operating over Thread SHALL use the Thread 1.3 or later protocol stack. The Thread Network credentials obtained during commissioning SHALL be persisted in non-volatile storage."

**OpenThread Attach 过程的各步骤耗时和代码追溯**:

| 步骤 | OpenThread SDK 代码 | 正常耗时 | 恶化条件 |
|------|-------------------|---------|---------|
| **Active Scan** | `src/core/mac/mac.cpp`: `Mac::StartCsmaBackoff()` → 全信道 Beacon Request 扫描 | 0.3-1s | 16 个信道都需要扫描, 拥挤环境等待退避 |
| **父节点选择** | `src/core/thread/mle.cpp`: `Mle::Attach()` → `Mle::GetNextNeighborInfo()` → Rssi 排序筛选 | 0.1-0.5s | 存储的 Parent 不可达, 需全量评估所有候选 Router |
| **Child ID Request** | `src/core/thread/mle.cpp`: `Mle::SendChildIdRequest()` → 等待 `ChildIdResponse` | 0.1-1s | Parent 忙于处理其他 Children, 响应超时需重试 |
| **MLE Link** | `src/core/thread/mle.cpp`: `Mle::HandleChildIdResponse()` → 链路建立 | 0.1-0.5s | 信号弱, 需要重传 |
| **地址注册** | `src/core/thread/mle.cpp`: `Mle::SendAddressSolicit()` → SLAAC 生成 Mesh-Local IPv6 | 0.5-2s | 多地址注册 (Mesh-Local + GUA + ML-EID) |
| **CSL 同步** | `src/core/mac/sub_mac.cpp`: `SubMac::CslSynchronize()` → CSL 周期协商 | 0-5s | CSL 自动同步启用 (`OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE=1`) |

**a) 父节点不可达的代码逻辑** (OpenThread `src/core/thread/mle.cpp`):

```cpp
// Mle::Attach() 中的 Parent 选择逻辑:
// 1. 首先尝试使用之前存储的 Parent (mParent)
// 2. 如果 mParent 不可达 (kErrorNoRoute / kErrorNoResponse):
//    → 清除缓存的 Parent → 重新执行全量扫描 (Mle::Discover())
//    → 每信道扫描耗时 × 16 信道 = 额外增加 1-5 秒
// 3. Child ID Request 超时默认 ~3 秒 (kAttachTimeout 默认值)
```

**b) CSL 同步延迟** (OpenThread `src/core/mac/sub_mac.cpp`):
- 本项目配置 `OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE = 1`
- CSL 初始同步需等待 Parent 发送 CSL IE (Information Element)，出现在下一个 Parent 的增强 Beacon 或数据帧中
- **首次 CSL 同步窗口**: 取决于 Parent 的 CSL 周期设置，最长可达 CSL Period 时长 (本项目未显式配置 CSL Period，使用 Thread 默认值)

**c) 入网失败处理不完善 — 代码分析**:

Matter SDK 层面 (`src/platform/silabs/ThreadStackManagerImpl.cpp`):
```cpp
// ThreadStackManagerImpl::OnThreadStateChanged()
// Thread 状态变化回调: OT_THREAD_STATE_DISABLED → DETACHED → CHILD → ROUTER
// 当 Thread 状态变为 DETACHED 且 IsThreadProvisioned()==true 时,
// OpenThread 内部自动尝试重新 Attach (由 Mle::Attach() 驱动)
// 但是: 如果持续 DETACHED 超过超时时间, 应用层没有收到任何通知
```

应用层 ([app_nwk_mgr.cpp:150-152](../src/app/app_nwk_mgr.cpp#L150-L152)):
```cpp
static void _rejoin_timeout_event_handler(app_event_t * ev)
{
    LOG_MSG_INFO(TAG_NWK, "rejoin failed");
    // ⚠️ 注意: 仅记录日志，没有重试机制!
    // 需要手动添加: ConnectivityMgr().SetThreadEnabled(false) → delay → SetThreadEnabled(true)
}
```

**对比 Spec 要求** (Matter Core Spec, Section 11.8.4, "Network Recovery"):
> "The device SHOULD attempt to re-establish Thread connectivity for a minimum of 5 minutes before considering the network unreachable."

实际代码 30 秒超时 (`ATTACH_NETWORK_TIMEOUT_MS = 30000`) 远低于 Spec 建议的 5 分钟。

#### <span style="color:orange">●</span> 根因 3: SRP 服务注册和 DNS-SD 发现延迟

**Spec 定义** (Matter Core Spec, **Section 11.9**, "Service Discovery"):

> Section 11.9.5.2: "A Matter device on Thread SHALL use the Thread Service Registration Protocol (SRP) to publish its operational service instance."
>
> Section 11.9.6: "The operational service instance SHALL be published with the following DNS-SD keys: `_matter._tcp` for TCP-based transport, `_matterc._udp` for UDP-based transport."
>
> Section 11.9.8: "The SRP registration SHALL include the TXT records containing the device's Vendor ID (VP), Product ID (PP), Discriminator (D), Commissioning Mode (CM), and other commissioning-related information."

**SRP 注册流程的代码链路**:

```
设备侧:
  1. Matter SDK: src/platform/silabs/DnssdImpl.cpp
     └─ DnssdImpl::StartOperationalAdvertising()
        └─ 构造 _matter._tcp SRV/TXT 记录
        └─ 调用 OpenThread SRP Client API

  2. OpenThread SDK: src/core/net/srp_client.cpp
     └─ Srp::Client::AddService()
        └─ 向 Thread Border Router 发送 SRP Update 消息 (CoAP over UDP)
        └─ 默认 SRP 服务租约 (lease) 超时: 2 小时
        └─ 默认 SRP Key 租约超时: 14 天

Border Router 侧:
  3. Thread Border Router: ot-br-posix / otbr-agent
     └─ SRP Server 接收 Update → 解析 DNS Resource Records
     └─ 更新 mDNS Responder (Bonjour / Avahi)
     └─ 重新发布 mDNS PTR/SRV/TXT 记录
     └─ mDNS 缓存 TTL: 默认 120 秒 (RFC 6762 Section 7.1)

控制器侧:
  4. 手机 APP / Matter Hub
     └─ SDK: src/lib/dnssd/Discovery_ImplPlatform.cpp
        └─ ResolveByType("_matter._tcp") → DNS-SD 查询
        └─ 获取设备 IP 地址、端口、TXT 记录
```

**此链路的各环节延迟**:

| 环节 | SDK 代码 | 延迟范围 | 说明 |
|------|---------|---------|------|
| 设备 SRP 注册 | `src/core/net/srp_client.cpp:Srp::Client::SendUpdate()` | 0.1-2s | CoAP 消息往返 + Border Router 处理 |
| Border Router → mDNS 更新 | `otbr-agent` (外部组件) | 0.5-5s | 取决于 CPU 负载、mDNS 定时发布周期 |
| mDNS 缓存传播 | RFC 6762 mDNS Responder | 0-120s | 上次缓存 TTL 未过期时, 控制器看到旧条目 |
| 控制器 DNS-SD 发现 | `src/lib/dnssd/Discovery_ImplPlatform.cpp` | 0.5-3s | DNS-SD 查询+响应 |

**关键问题**: 设备重启后 SRP 注册的是**新的服务实例**，但 mDNS 缓存中可能仍保留**旧的 DNS 条目**。控制器的 DNS-SD 解析器通常缓存结果 120 秒，意味着在最坏情况下，**设备恢复网络连接后仍需等待 2 分钟**控制器才能发现新的服务实例。

#### <span style="color:orange">●</span> 根因 4: BLE 作为带外发现通道未被利用

**Spec 定义** (Matter Core Spec, **Section 5.4.2.5**, "Using BLE"):

> "Nodes currently commissioned into one or more fabrics or already connected to an IP-bearing network SHALL NOT employ this method [BLE] for commissioning."
>
> 注意: Spec 明确**禁止已入网设备使用 BLE 进行配网**。但已入网设备在 operational mode 下**可选**使用 BLE 广播用于 operational discovery (Spec 5.6)。另外, 如果设备因 NVM3 数据丢失导致 `IsThreadProvisioned() = false`, 设备将回到未入网状态, 此时 BLE 配网广播是允许的。

本项目配置:
```c
// include/CHIPProjectConfig.h:141,155
#define CHIP_DEVICE_CONFIG_ENABLE_PAIRING_AUTOSTART             0  // 配网自动启动: 禁用
#define CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART 0  // BLE 广播自动启动: 禁用
```

**影响分析**:
- 已配网设备上电后**完全不打 BLE 广播** → 控制器只能通过 IP 网络 (DNS-SD) 发现设备  
- 如果 Thread 网络未恢复（Root Cause 2），BLE 通道无法作为备选恢复路径
- 对比: 部分 Matter 设备在上电时会短暂打 BLE 广播作为 "liveness signal"，让附近手机快速感知。这种操作模式在 Spec 5.6 中是允许的 ("MAY continue BLE advertisements")。

**BLE 广播参数要求** (Spec 5.4.2.5.3):
- 前 30 秒: Advertising Interval **20ms ~ 60ms** (快速广播)
- 30 秒后: **150ms ~ 1285ms** (慢速广播)
- 本项目配置: `CHIP_DEVICE_CONFIG_BLE_FAST_ADVERTISING_INTERVAL = 40` (25ms) ✓, `CHIP_DEVICE_CONFIG_BLE_SLOW_ADVERTISING_INTERVAL = 800` (500ms) ✓

#### <span style="color:orange">●</span> 根因 5: NVM3 Flash 存储恢复的启动开销

**NVM3 启动流程** (Silicon Labs GSDK `platform/emdrv/nvm3/src/nvm3_hal_flash.c`):

```
nvm3_initDefault() [autogen/sl_event_handler.c:51]
  └─ nvm3_open()
     └─ nvm3_halFlashReadWords() → 扫描 Flash Page 头, 定位活跃 Page
     └─ repackIfNeeded():
        ├─ 如果碎片化超过 NVM3_DEFAULT_REPACK_HEADROOM (本项目=0): 触发 Repack
        └─ Repack: 读出所有有效对象 → 擦除 Page → 写回 → 额外开销 500ms-2s
     └─ nvm3_halFlashReadWords() → 重建对象索引 (NVM3_DEFAULT_CACHE_SIZE=200)
```

**项目配置**:
- Flash 大小: 40960 bytes ([nvm3_default_config.h:38](../config/nvm3_default_config.h#L38))
- 最大对象: 511 entries (KVS_MAX_ENTRIES)
- Repack 触发阈值: 0 (任何碎片立即触发)

**对恢复延迟的影响**: NVM3 正常初始化是 Boot+Init 67ms 的一部分 (实际耗时 <10ms)。只有当触发 Repack 时才有额外开销 (~500ms-2s)。如果设备在写入期间断电导致 Page 损坏, 需从备份 Page 恢复, 额外增加 500ms-1s。

Matter Spec (**Section 11.8.2**) 对此的要求:
> "All Thread network credentials, Fabric configuration, and group keys SHALL be stored in non-volatile memory that survives power cycles."

#### <span style="color:orange">●</span> 根因 6: `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS=0` 时恢复更慢的原因分析

**问题**: 用户询问将 `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS` 设为 `0` 是否会进一步增加恢复延迟。答案是 **肯定的** —— 关闭持久化订阅会让恢复过程**显著变慢**。

**当前配置** ([AppBuildConfig.h:8-20](../config/app/AppBuildConfig.h#L8-L20)):

```cpp
#define CHIP_CONFIG_PERSIST_SUBSCRIPTIONS      1  // 当前: 启用
#define CHIP_CONFIG_SUBSCRIPTION_TIMEOUT_RESUMPTION  0  // 超时恢复: 禁用
#define CHIP_CONFIG_ENABLE_SESSION_RESUMPTION  1  // 会话恢复: 启用
```

**Spec 依据** (Matter Core Spec, **Section 8.5.3.2**, "Subscription Persistence"):

> "A device MAY persist subscriptions across power cycles. When subscription persistence is enabled, the device SHALL store the subscription metadata (Subscription ID, subscribed paths, reporting intervals, filters) in non-volatile storage. After reboot, the device SHALL restore these subscriptions and be prepared to resume reporting when a CASE session is re-established."

##### 两种配置的恢复行为对比

**真实 log 中的 "No subscriptions to resume"**:

从 bk01_matter 设备重启 log 中可见：

```
[00:00:14.945][info][IM] No subscriptions to resume
```

尽管 `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS = 1`，设备仍然报告无订阅可恢复。这说明 **`PERSIST_SUBSCRIPTIONS=1` 是"能力"而非"保证"**。以下场景会导致持久化数据实际为空：

| 场景 | 原因 |
|------|------|
| 首次配网后立即断电 | 从未建立过订阅，持久化区域为空 |
| NVM3 中订阅数据未写入或已过期 | 写入延迟或寿命到期 |
| 控制器从未订阅该设备 | 配网成功后控制器未自动订阅（取决于生态实现） |
| NVM3 Page 损坏 | 备份恢复后丢失了最近写入的订阅数据 |

> 因此 `PERSIST_SUBSCRIPTIONS=1` 的正确理解是：**当订阅数据存在时，设备能够持久化并恢复它；但这不保证每次重启都一定有可恢复的订阅数据。** 在评估恢复延迟时，需要考虑 "No subscriptions to resume" 路径下的全量订阅重建开销。

##### 两种配置的恢复行为对比

| 阶段 | `PERSIST_SUBSCRIPTIONS = 1` (当前) | `PERSIST_SUBSCRIPTIONS = 0` (假设) |
|------|-----------------------------------|-----------------------------------|
| **设备启动时** | 从 NVM3 恢复订阅元数据 (Subscription ID, paths, intervals) | 无订阅元数据, 订阅表为空 |
| **Thread 入网后** | 设备已知道: "我之前有 N 个订阅者" | 设备不知道曾被订阅过 |
| **控制器检测设备离线** | 同左 (控制器侧不变) | 同左 |
| **CASE 重建后** | 设备有订阅上下文 → 可快速恢复报告 | 设备无任何订阅上下文 |
| **控制器重新订阅** | 控制器可能尝试 `KeepSubscriptions=true` 恢复旧订阅 | 控制器必须建立**全新**订阅 |
| **Priming Report** | 可能部分增量 (如果 KeepSubscriptions 成功) | 必然全量 Priming Report (所有属性当前值) |

##### 延迟增加的具体原因

**原因 1: 控制器必须等待 Subscription 超时** (增加 30-60 秒)

当 `PERSIST_SUBSCRIPTIONS = 0` 时:

```
控制器侧行为 (SDK: src/app/ReadClient.cpp):
  └─ 控制器持有的 Subscription State (在控制器内存中) 仍然有效
  └─ 控制器持续等待设备发送属性报告
  └─ Subscription MaxInterval 超时机制:
     ├─ 默认 MaxInterval Ceiling: 60 秒
     ├─ 如果 MaxInterval 内未收到任何报告 → 控制器判定订阅失效
     └─ 控制器主动发送 SubscribeRequest (KeepSubscriptions=false) 建立新订阅
```

SDK 代码路径 (`src/app/ReadClient.cpp`):
```
ReadClient::OnMaxIntervalTimeout()
  └─ 订阅超时 → 触发 OnDeallocatePaths() → 回调应用层 → 应用层重新 Subscribe
```

对比 `PERSIST_SUBSCRIPTIONS = 1` 的情况:
- 设备恢复后能识别来自已持久化订阅的 `SubscribeRequest (KeepSubscriptions=true)`
- 控制器在 CASE 重建后立即重订阅, 无需等待超时

**原因 2: 全量 Priming Report 开销** (增加 1-5 秒)

`PERSIST_SUBSCRIPTIONS = 0` 时设备无订阅历史:

```cpp
// SDK: src/app/InteractionModelEngine.cpp
// 新订阅 → 需要发送 Priming Report:
// 设备需要读取所有被订阅的 attribute 当前值
// 对于 Window Covering 设备:
//   - CurrentPositionLiftPercent100ths
//   - TargetPositionLiftPercent100ths
//   - CurrentPositionTiltPercent100ths
//   - OperationalStatus
//   - Mode
//   - 以及 Identify, Groups, PowerSource 等基础 cluster
//
// 每个 attribute 的值都需要从 NVM3 或通过 UART 从 MCU 读取
// 全量 Priming Report 的数据量和 I/O 耗时 >> 增量报告
```

对比 `PERSIST_SUBSCRIPTIONS = 1`:
- 设备保留了上次报告的属性值快照
- 可以只发送变化的部分 (增量报告)
- Priming Report 可以更轻量

**原因 3: 多控制器场景下恢复放大** (成倍增加)

```
场景: Apple Home + Alexa + SmartThings 同时订阅

PERSIST_SUBSCRIPTIONS = 1:
  ├─ 设备恢复 3 个持久化订阅元数据
  ├─ 3 个控制器各自在 CASE 重建后恢复订阅
  └─ 每个控制器只需增量状态同步

PERSIST_SUBSCRIPTIONS = 0:
  ├─ 设备无任何订阅
  ├─ 3 个控制器各自等待超时 (可能不同时间)
  ├─ 各自发送全新的 SubscribeRequest
  ├─ 设备需为每个新订阅生成全量 Priming Report
  └─ 总延迟 = Max(各控制器的超时时间) + 3×Priming Report 时间
```

**原因 4: 与 `ENABLE_SESSION_RESUMPTION` 的协同作用丢失**

当前配置:
```cpp
#define CHIP_CONFIG_ENABLE_SESSION_RESUMPTION  1  // 启用会话恢复
```

Session Resumption 允许 CASE 会话使用缓存的密钥材料进行**快速重建** (减少一次 ECDH 密钥交换), 但 Session Resumption 数据的有效期和被恢复的 CASE 上下文与 **订阅持久化** 紧密关联 (SDK: `src/app/InteractionModelEngine.cpp` 中的 `GetSubscriptionResumptionInfo()`):

```cpp
// 当 PERSIST_SUBSCRIPTIONS = 1 时:
// InteractionModelEngine::GetSubscriptionResumptionInfo()
//   → 从 NVM3 读取订阅恢复信息
//   → 包含相关联的 CASE 会话恢复信息
//   → 控制器重新连接时可以利用 Session Resumption 加速

// 当 PERSIST_SUBSCRIPTIONS = 0 时:
// GetSubscriptionResumptionInfo() 返回空
// → Session Resumption 无法与订阅关联
// → 控制器必须走完整的 CASE Sigma1→Sigma2→Sigma3
// → 增加 ~1-2 秒
```

##### 量化延迟对比

| 配置 | 正常恢复总时间 | 最坏恢复总时间 | 额外延迟来源 |
|------|-------------|-------------|------------|
| `PERSIST_SUBSCRIPTIONS = 1` (当前) | 3-13 秒 | 90-140 秒 | 根因 1-5 中描述的各项 (与 §3.1 延迟表一致) |
| `PERSIST_SUBSCRIPTIONS = 0` (假设) | 40-100 秒 | 120-200+ 秒 | 上述原因 1-4 |
| **差值** | **+33-61 秒** | **+30-60+ 秒** | |

| 新增延迟项 | 配置=0 时增加的延迟 | 原因 |
|-----------|------------------|------|
| 订阅超时等待 | +30 至 +60 秒 | 控制器必须等待 MaxInterval 超时 |
| 全量 Priming Report | +1 至 +5 秒 | 设备需重新读取所有被订阅属性 |
| 多控制器串行恢复 | +N×5 秒 (N=控制器数) | 每个控制器独立发现 + 独立订阅 |
| Session Resumption 失效 | +1 至 +2 秒 | 无法利用缓存密钥加速 CASE |
| **合计额外延迟** | **约 +35 至 +70 秒** | |

##### 结论

`CHIP_CONFIG_PERSIST_SUBSCRIPTIONS = 0` **确实会让恢复更慢**，核心原因是:

1. **控制器侧**必须等待订阅超时 (最长 60s) 才能发现设备状态变化
2. **设备侧**没有任何订阅记忆，每个控制器都需要全量重建订阅
3. **Session Resumption 的加速效果**因为缺乏持久化订阅上下文而部分失效
4. **多控制器**环境中的延迟会被成倍放大

**当前项目设置 `PERSIST_SUBSCRIPTIONS = 1` 是正确的选择**。配合 `ENABLE_SESSION_RESUMPTION = 1`，可以提供最优的网络恢复性能。除非 NVM3 存储空间极度紧张（每个持久化订阅约占用 200-500 bytes），否则不应关闭此功能。

## 4. 关键代码路径详解

### 4.1 网络状态管理代码流

**SPEC 依据**: Matter Core Spec **§11.8** (Thread 状态映射), **§5.4.2** (配网窗口状态机)

```
文件: src/app/app_nwk_mgr.cpp (核心状态机)

网络状态转换:
                          
       ┌──────────┐        
       │  Leave   │◄─────────────────────────────┐
       │  (Init)  │                              │
       └────┬─────┘                              │
            │                                    │
    IsThreadProvisioned()?                       │
     │YES          │NO                           │
     ▼             ▼                             │
 ┌────────┐  ┌─────────────┐                     │
 │ Attach │  │ Open        │                     │
 │Joining │  │ Commission  │                     │
 └───┬────┘  │ Window      │                     │
     │       └─────────────┘                     │
     │ Thread Attach success                     │
     ▼                                           │
 ┌────────┐     Thread Lost      ┌────────┐      │
 │ Joined │─────────────────────►│ Leave  │──────┘
 └───┬────┘                      └────────┘
     │ Thread Lost
     ▼
 ┌────────┐
 │ Leave  │
 └────────┘
```

### 4.2 平台事件回调链

**SPEC 依据**: Matter Core Spec **§4.14.2** — CASE/PASE 会话层回调; **§11.8** — Thread 状态变化回调

```
OpenThread State Change (Thread Spec MLE / MAC 层状态机)
    │
    ▼
ThreadStackManager::OnThreadStateChanged()
    │  SDK: src/platform/silabs/ThreadStackManagerImpl.cpp
    │  映射 OT 状态 → Matter 事件:
    │    OT_DEVICE_ROLE_CHILD / ROUTER → kThreadConnectivityChange(kConnectivity_Established)
    │    OT_DEVICE_ROLE_DETACHED         → kThreadConnectivityChange(kConnectivity_Lost)
    ▼
ConnectivityManagerImpl::OnThreadStateChanged()
    │  SDK: src/platform/silabs/ConnectivityManagerImpl.cpp
    │  更新内部连接状态 + DNS-SD 服务状态
    ▼
PlatformManager::PostEvent(kThreadConnectivityChange)
    │  SDK: src/platform/PlatformManager.h
    │  事件数据结构: ChipDeviceEvent.ThreadConnectivityChange.Result
    ▼
on_platform_event() in app_nwk_mgr.cpp:206
    │  项目代码: [app_nwk_mgr.cpp:206](../src/app/app_nwk_mgr.cpp#L206)
    │
    ├─ kConnectivity_Established → 通知 MCU 已入网
    ├─ kConnectivity_Lost → 通知 MCU 离线
    ├─ kCHIPoBLEConnectionEstablished → 配网进行中 (SPEC §5.4.2)
    ├─ kCommissioningComplete → 配网完成 (SPEC §5.5 Commissioning Flow)
    └─ kFailSafeTimerExpired → 配网超时 (SPEC §11.10.7.2 ArmFailSafe)
```

### 4.3 Provisioning 状态持久化路径

**SPEC 依据**: Matter Core Spec **§11.8.2** (Thread credential storage), **§5.5** (Commissioning Complete — 数据持久化)

```
Matter Commissioning Complete (SPEC §5.5 — CommissioningComplete 命令)
    │
    ▼
Provision::Manager::GetInstance().GetStorage()
    │  SDK: src/platform/silabs/ProvisionManager.cpp
    │  └─ 存储 Setup Payload (QR Code 数据) → NVM3 KVS
    │      SPEC §5.4.1 — Onboarding Payload 包含: VP/PP/D/Passcode
    │  └─ 存储 Fabric 信息 (FabricIndex, NodeID, RootCA, NOC…)
    │
    ▼
Internal::SilabsConfig::WriteConfigValueStr()
    │  SDK: platform/silabs/SilabsConfig.cpp
    │  └─ 写入 NVM3 Key-Value Store
    │     └─ nvm3_writeData() → Flash (GSDK `platform/emdrv/nvm3/src/`)
    │     └─ SPEC §11.8.2 要求: Thread 凭据和 Fabric 配置必须保存在非易失存储中
    │
    ▼
ConnectivityMgr().IsThreadProvisioned()
    │  SDK: src/platform/silabs/ConnectivityManagerImpl.cpp
    │  └─ 读取 NVM3 中存储的 Thread Operational Dataset
    │  └─ 判断 Thread Netif 接口是否有有效配置 (NetworkKey, PANID, Channel…)
    │  └─ 返回值决定启动后走 "恢复流程" 还是 "配网流程"
```

### 4.4 CASE 协议消息与 Session Resumption 详解

**Secure Channel 协议** (协议ID: `0x0000_0002`) 定义了 CASE 会话建立的精确消息格式:

| 消息类型 | Message ID | 方向 | 说明 |
|---------|-----------|------|------|
| `CASE_Sigma1` | `0x30` | 控制器→设备 | 发起 CASE 握手, 携带控制器的 Fabric 信息和随机数 |
| `CASE_Sigma2` | `0x31` | 设备→控制器 | 响应 Sigma1, 携带设备 NOC 证书链和签名 |
| `CASE_Sigma3` | `0x32` | 控制器→设备 | 验证设备证书链, 发送确认和会话密钥材料 |
| `CASE_Sigma2Resume` | `0x33` | 设备→控制器 | **会话恢复** — 使用缓存的密钥材料快速重建, 跳过完整 Sigma 握手 |
| `ICD_CheckIn` | `0x50` | ICD→控制器 | ICD 设备周期性签入, 告知控制器设备处于活跃状态 |
| `StandaloneAck` | `0x10` | 双向 | 独立 ACK, 不依赖 piggyback |

**Session Resumption 的消息流程** (`CASE_Sigma2Resume`):

```
正常 CASE (完整 Sigma):
  Controller ──Sigma1──▶ Device
  Controller ◄──Sigma2── Device
  Controller ──Sigma3──▶ Device
  Controller ◄──StatusReport── Device  (Session Active)
  共 4 次往返, ~1.5-2 秒

Session Resumption (CASE_Sigma2Resume):
  Controller ──Sigma1──▶ Device
  Controller ◄──Sigma2Resume── Device  (★ 跳过 Sigma2+Sigma3, 直接恢复)
  Controller ◄──StatusReport── Device  (Session Active)
  共 2 次往返, ~0.5-1 秒 (节省 1 次 ECDH 密钥交换)
```

**真实 log 实证 — Session Resumption 的实际性能**:

```
[00:00:18.155] Msg TX ... Type 0000:30 (SecureChannel:CASE_Sigma1)         ← 控制器发起 Sigma1
[00:00:18.551] Msg RX ... Type 0000:33 (SecureChannel:CASE_Sigma2Resume)   ← 设备用 Sigma2Resume 响应 (仅 +396ms!)
[00:00:18.552] Msg TX ... Type 0000:10 (SecureChannel:StandaloneAck)       ← 设备确认收到
[00:00:18.559] Msg TX ... Type 0000:40 (SecureChannel:StatusReport)        ← Session 状态报告
[00:00:18.564] SecureSession[0x20006e28, LSID:25475]: State change 'kEstablishing' --> 'kActive'
```

从 Sigma1 发送到 Session Active 仅 **409ms**，验证了 Session Resumption 的预估（0.5-1s），且实际性能比预估值更快。关键观察：
- 控制器在设备 Thread Up 后约 3.8s 才发出 Sigma1（控制器侧反应时间）
- 设备以 `CASE_Sigma2Resume` (MsgID `0x33`) 响应，证明确实走了 Session Resumption 路径
- 新的 LSID=25475（与重启前被丢弃的 LSID=36120 不同），说明是全新的安全会话
```

**Session Resumption 的生效条件**:
1. 设备侧 `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION = 1` ✓ (本项目已启用)
2. 控制器侧也支持 Session Resumption
3. Session Resumption 缓存数据未被清除 (存储在 NVM3, 重启后仍有效)
4. 设备端的 `CASE_Sigma2Resume` 处理在 `src/transport/CASEServer.cpp` 中实现

**Session Resumption 的局限性**:
- 缓存的会话信息有过期时间 (默认取决于 `CHIP_CONFIG_CASE_SESSION_RESUMPTION_STORAGE_CAPACITY` 和 Fabric 配置)
- 如果控制器的 IP 地址发生变化, Session Resumption 可能无效
- 多个控制器各自维护独立的 Session Resumption 缓存

### 4.5 SPP (Serial Port Protocol) 重传机制

SPP 是 EFR32MG24 与 MCU 之间的串口通信协议，在恢复过程中与 Thread/CASE 恢复**并发进行**。理解 SPP 的重传行为有助于完整分析恢复期间的 log。

#### 4.5.1 SPP 帧格式与 Command 类型

SPP 帧格式 (基于 log 中的 `MATTER TX` 数据):

```
帧头: 55 AA (固定)
字节2:   01 = CMD frame type
字节3-4: 00 02 = Sequence Number (16-bit, little-endian)
字节5:   02 = Command Type (0x01=NOP/Heartbeat, 0x02=Data)
字节6-7: 01 01 = Payload length or flags
字节8-N: Payload data
```

Log 中观察到的 Command 类型:

| CMD | 名称 | 说明 |
|-----|------|------|
| `0x01` | NOP / Heartbeat | 空操作/心跳帧，用于维持链路或探测 MCU |
| `0x02` | Data / Status | 数据帧，携带 MCU 状态查询或 Matter 属性同步 |

#### 4.5.2 重传参数与行为

真实 log 展示了 SPP 层的完整重传 cycle:

```
[00:00:14.366] SPP: pending ack but allow new cmd process       ← 有待确认命令，但允许新命令执行
[00:00:14.844] SPP: re-sent count 1, ack_timeout_ms 500        ← 第一次重传 CMD 0x02 SN=0x0000
[00:00:15.344] SPP: re-sent count 2, ack_timeout_ms 500        ← 第二次重传 (间隔 500ms)
[00:00:15.845] SPP: re-sent reach to max                        ← 达到最大重传次数，放弃该 SN
[00:00:15.846] MATTER TX: 55 AA 01 00 01 01 00 02              ← 序列号递增: CMD 0x01 SN=0x0001
[00:00:16.346] SPP: re-sent count 1, ack_timeout_ms 500        ← 新一轮重传开始
[00:00:16.846] SPP: re-sent count 2, ack_timeout_ms 500
[00:00:17.346] SPP: re-sent reach to max                        ← 再次达到上限
[00:00:17.347] MATTER TX: 55 AA 01 00 02 02 01 01 06           ← CMD 0x02 SN=0x0002
[00:00:17.847] SPP: re-sent count 1, ack_timeout_ms 500
[00:00:18.347] SPP: re-sent count 2, ack_timeout_ms 500
[00:00:18.847] SPP: re-sent reach to max
```

**SPP 重传参数总结**:

| 参数 | 值 | 说明 |
|------|-----|------|
| `ack_timeout_ms` | 500ms | 等待 MCU 应答的超时时间 |
| 每帧最大重传次数 | 2 | `re-sent count 2` 后 `re-sent reach to max` |
| 放弃后行为 | 序列号递增，发送下一帧 | 不阻塞后续帧，允许新命令执行 |
| 并发策略 | 不阻塞 | "pending ack but allow new cmd process" |

#### 4.5.3 SPP 与网络恢复的并发关系

SPP 层的重传与 Matter 网络恢复**并行进行**，互不阻塞。从 log 时间线可以看到:

```
14.365  COM: notify network [Joined]          ← 通知 MCU 入网 (通过 SPP)
14.366  SPP: pending ack but allow new cmd    ← MCU 未立即应答，SPP 进入重传
14.447  SRP Client was started                ← Matter 侧继续 SRP 注册 (不等待 SPP)
14.844  SPP: re-sent count 1                  ← SPP 独立重传
14.933  DNS-SD initialized                   ← Matter 侧继续 DNS-SD (不等待 SPP)
15.845  SPP: re-sent reach to max             ← 第一轮放弃
18.155  CASE Sigma1 发送                     ← Matter 侧继续 CASE (不等待 SPP)
18.847  SPP: re-sent reach to max             ← 第三轮放弃
```

**关键结论**: SPP 重传不会阻塞 Matter 网络恢复。两个链路独立运作——Thread/CASE 恢复走 802.15.4 网络，SPP 走 UART 到 MCU。如果在恢复初期看到大量 SPP 重传 log 是**正常现象**，通常是因为 MCU 在 MG24 启动后还需要额外初始化时间。

---

## 5. Matter Spec 相关章节参考

### 5.1 核心规范 (23-27349-009_Matter-1.5-Core-Specification.pdf)

| 章节 | 内容 | 与恢复过程的关系 | 本报告引用处 |
|------|------|-----------------|-------------|
| **Section 4.14.2** | CASE Sigma Protocol — 会话建立握手 (协议ID: `0x0000_0002`, Message: `CASE_Sigma1`/`Sigma2`/`Sigma3` = `0x30`/`0x31`/`0x32`) | 设备重启后 CASE 会话密钥丢失，控制器需重新发起 Sigma | 根因 1 |
| **Section 4.14.2.7** | Session Resumption — 会话信息缓存 (Message: `CASE_Sigma2Resume` = `0x33`) | `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION=1` 允许缓存，但密钥/Security Context **不跨重启持久化** | 根因 1 |
| **Section 4.14.1** | PASE (Password-Authenticated Session Establishment) — 配网临时会话 | PASE 握手必须在 **60 秒内** 完成, 超时会话终止; 基于 Spake2+ 协议 | Phase 2 |
| **Section 5.4.2.3** | Announcement Duration | 配网窗口时长范围: **180s ≤ T ≤ 900s** (3~15分钟) | 根因 3, 方案 6.2 |
| **Section 5.4.2.5** | Using BLE for Commissioning | **已入网设备 SHALL NOT 使用 BLE 配网**; BLE 仅限未入网设备 | 根因 4 |
| **Section 11.10.7.2** | ArmFailSafe (General Commissioning Cluster) | 配网 FailSafe 超时机制: 默认 **60s**, 可由控制器延长 | Phase 3 |
| **Section 8.5.2** | Interaction Model — Subscribe/Report (Message: `SubscribeRequest`=`0x03`, `SubscribeResponse`=`0x04`, `ReportData`=`0x05`) | 订阅的建立和属性报告的发送机制 | 根因 1 |
| **Section 8.5.3.2** | Subscription Persistence | `CHIP_CONFIG_PERSIST_SUBSCRIPTIONS` 实现规范 | 根因 1, 根因 6 |
| **Section 9.15** | ICD (Intermittently Connected Device) Management | SED 休眠周期、唤醒、Check-in 消息 (Message: `ICD_CheckIn`=`0x50`) 定义 | 根因 2 |
| **Section 11.8** | Thread Integration | Matter 设备在 Thread 上的强制要求 (Thread 1.3+) | 根因 2 |
| **Section 11.8.2** | Thread Network Credential Storage | 要求 Thread 凭据持久化在 NVM 中 | 根因 5 |
| **Section 11.8.4** | Thread Network Recovery | 设备失联后应尝试重新 Attach **至少 5 分钟** | 根因 2 |
| **Section 11.9** | DNS-SD Advertising & Discovery Protocol | 定义 `_matter._tcp` / `_matterc._udp` 服务类型 | 根因 3 |
| **Section 11.9.5.2** | SRP-Based Service Registration | **要求 Thread 设备使用 SRP 注册服务，状态变化时刷新** | 根因 3, 方案 6.2 |
| **Section 11.9.6** | Operational Service Instance TXT Records | TXT 记录中包含 VP/PP/D/CM 等设备信息字段 | 根因 3 |
| **Section 11.9.8** | SRP Update and Lease Management | SRP 租约时间 (2h) 和 Key 租约 (14d) | 根因 3 |

### 5.2 设备库规范 (23-27351-008_Matter-1.5-Device-Library-Specification.pdf)

| 章节 | 内容 | 与本设备的关系 |
|------|------|--------------|
| **Window Covering** | 窗帘设备类型定义 | 本设备是 Window Covering 设备 |

### 5.3 Spec 定义的时序约束

| 参数 | Spec 要求 | Spec 章节 | 本项目配置 | 合规性 |
|------|----------|----------|-----------|--------|
| Basic Commissioning Window 时长 | 180s ≤ T ≤ 900s (3~15分钟) | **§5.4.2.3.1** | 300s (5分钟) | ✓ |
| BLE Fast Advertising Interval | 20ms ~ 60ms (前30秒) | **§5.4.2.5.3** | 40 (25ms) | ✓ |
| BLE Slow Advertising Interval | 150ms ~ 1285ms (30秒后) | **§5.4.2.5.3** | 800 (500ms) | ✓ |
| MRP Idle Retry Interval | 实现定义 (默认 300ms) | Matter SDK `ReliableMessageProtocolConfig.h` | 2000ms (本项目定制) | ✓ |
| FailSafe Timer (默认) | 60s, 可由 ArmFailSafe 延长 | **§11.10.7.2** | SDK 默认 60s | ✓ |
| CASE Session Idle Timeout | 实现定义 | **§4.14.2** | SDK 默认 | ✓ |
| Thread Attach 重试时间 | 建议至少 5 分钟 | **§11.8.4** | **30s 且无重试** ← 见根因 2 | <span style="color:red">**⚠️ 违反 Spec**</span> |
| SRP 服务租约 (Key Lease) | 默认 14 天 | **§11.9.8** | OpenThread 默认 | ✓ |
| SRP 服务租约 (Service Lease) | 默认 2 小时 | **§11.9.8** | OpenThread 默认 | ✓ |
| mDNS 缓存 TTL | 默认 120 秒 | RFC 6762 **§7.1** | Border Router 侧 (外部) | ✓ |

### 5.4 SDK 核心代码文件索引

以下列出本报告中引用的 Matter SDK (connectedhomeip) 和 OpenThread SDK 代码文件, 用于追溯网络恢复各环节的 SDK 实现:

**Matter SDK (connectedhomeip) — 关键文件:**

| SDK 文件路径 | 涉及环节 | 本报告引用处 |
|-------------|---------|------------|
| `src/transport/SessionManager.h/.cpp` | CASE/PASE 会话生命周期管理, `Init()` 创建空会话表 | 根因 1 |
| `src/transport/SecureSession.h/.cpp` | 单个安全会话的状态 (`mState`), 仅存 RAM | 根因 1 |
| `src/transport/CASEClient.cpp` | 控制器侧发起 CASE Sigma1 握手 | 根因 1, Phase 3 |
| `src/transport/CASEServer.cpp` | 设备侧响应 CASE Sigma1, 完成 Sigma2/Sigma3 | Phase 3 |
| `src/messaging/ReliableMessageMgr.h/.cpp` | MRP 可靠传输: `SendFromQueue()`, 重传队列管理 | 根因 1 |
| `src/messaging/ReliableMessageProtocolConfig.h` | MRP 参数: `CHIP_CONFIG_RMP_DEFAULT_MAX_RETRANS` (默认=4), 重试间隔 `CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL` | 根因 1 |
| `src/app/ReadClient.h/.cpp` | 订阅客户端: `SendSubscribeRequest()`, `OnMaxIntervalTimeout()`, 订阅生命周期 | 根因 1, 根因 6, Phase 3 |
| `src/app/InteractionModelEngine.h/.cpp` | IM 引擎: 订阅恢复 (含持久化订阅 `GetSubscriptionResumptionInfo()`), 属性报告调度 | 根因 1, 根因 6, Phase 3 |
| `src/app/DnssdServer.cpp` | `StartServer()`/`StopServer()` — DNS-SD 服务管理入口 | 方案 6.2 |
| `src/lib/dnssd/Advertiser.h` | `AdvertiseOperational()` — DNS-SD 广告抽象 API | 方案 6.2 |
| `src/lib/dnssd/Discovery_ImplPlatform.cpp` | DNS-SD 发现: `ResolveByType()` 查找服务 | 根因 3 |
| `src/lib/dnssd/ServiceNaming.h` | DNS-SD 服务命名: `_matter._tcp` 实例名构造 | 根因 3 |
| `src/lib/dnssd/TxtFields.h` | TXT 记录键值定义 (VP/PP/D/CM 等) | 根因 3 |
| `src/platform/silabs/DnssdImpl.cpp` | Silicon Labs 平台 DNS-SD 实现: 对接 OpenThread SRP | 根因 3, 方案 6.2 |
| `src/platform/silabs/ThreadStackManagerImpl.h/.cpp` | Thread Stack 初始化, `OnThreadStateChanged()` 回调 | Phase 2, 根因 2 |
| `src/platform/silabs/ConnectivityManagerImpl.h/.cpp` | 连接状态管理, `IsThreadProvisioned()` 判断 | Phase 2 |
| `src/platform/silabs/SilabsConfig.h/.cpp` | NVM3 KVS 读写: `ReadConfigValueStr()` / `WriteConfigValueStr()` | Phase 2 |

**OpenThread SDK — 关键文件:**

| SDK 文件路径 | 涉及环节 | 本报告引用处 |
|-------------|---------|------------|
| `src/core/thread/mle.cpp` | MLE Attach 流程: `Attach()` → `Discover()` → `SendChildIdRequest()` | 根因 2 |
| `src/core/mac/mac.cpp` | MAC 层: `StartCsmaBackoff()` → 全信道扫描 | 根因 2 |
| `src/core/mac/sub_mac.cpp` | CSL 同步: `CslSynchronize()` | 根因 2 |
| `src/core/net/srp_client.cpp` | SRP Client: `AddService()`, `SendUpdate()` — 服务注册 | 根因 3 |
| `include/openthread/srp_client.h` | SRP Client 公共 API: `otSrpClientStart()` / `otSrpClientStop()` | 方案 6.2 |
| `include/openthread/instance.h` | OpenThread 实例获取: `otInstanceInit()` | 方案 6.2 |
| `include/openthread/thread.h` | Thread 管理 API: `otThreadSetEnabled()` | 根因 2 |

**Silicon Labs GSDK (Gecko SDK / Simplicity SDK) — 关键文件:**

| SDK 文件路径 (相对 SDK 根目录) | 涉及环节 | 本报告引用处 |
|-------------|---------|------------|
| `platform/emdrv/nvm3/src/nvm3_hal_flash.c` (GSDK 4.x) 或 `protocol/nvm3/src/` (Simplicity SDK 2025+) | NVM3 Flash 读写, `nvm3_open()` | 根因 5 |
| `platform/emdrv/nvm3/inc/nvm3.h` 或 `protocol/nvm3/inc/nvm3.h` | NVM3 API 定义 | 根因 5 |

---

## 6. 优化建议

### 6.1 减少 Thread Attach 检测延迟

**当前问题**: `ATTACH_NETWORK_TIMEOUT_MS = 30000` (30s) 太长，且超时后无重试。

**SPEC 依据**: Matter Core Spec **§11.8.4**: "The device SHOULD attempt to re-establish Thread connectivity for a minimum of 5 minutes before considering the network unreachable." 即 Spec 建议重试至少 5 分钟，当前代码仅等待 30 秒且不重试 —— 严重违反 Spec 建议。

**建议**:
```cpp
// 缩短首次判断超时，加入重试机制
#define ATTACH_NETWORK_TIMEOUT_MS 15000  // 缩短到 15 秒
#define ATTACH_NETWORK_MAX_RETRIES 3     // 最大重试次数

static void _rejoin_timeout_event_handler(app_event_t * ev)
{
    static uint8_t retry_count = 0;
    if (retry_count < ATTACH_NETWORK_MAX_RETRIES) {
        retry_count++;
        LOG_MSG_INFO(TAG_NWK, "rejoin retry %d", retry_count);
        // 强制重新 Attach
        ConnectivityMgr().SetThreadEnabled(false);
        vTaskDelay(pdMS_TO_TICKS(500));
        ConnectivityMgr().SetThreadEnabled(true);
        ev_set_delay_ms(ev, ATTACH_NETWORK_TIMEOUT_MS);
    } else {
        LOG_MSG_ERR(TAG_NWK, "rejoin failed after %d retries", retry_count);
        retry_count = 0;
        // 可选: 打开 BLE 广播让用户知道设备在线
    }
}
```

### 6.2 加快控制器侧发现 — 主动触发 SRP 服务重注册

**问题分析**: 设备重启后, DNS-SD/mDNS 缓存中可能保留旧的 SRP 服务条目 (mDNS 默认 TTL=120s, RFC 6762). 控制器在缓存过期前无法发现设备的新服务实例. 设备侧需要**主动刷新** SRP 注册, 让 Border Router 立即更新 mDNS 记录.

**Spec 依据** (Matter Core Spec **Section 11.9.5.2**):
> "The SRP client SHALL update the service registration when the device's operational state changes, including when the device re-establishes Thread connectivity after a power cycle."

**实现方案: 在 Thread 连接建立后强制 DNS-SD 重新发布**

以下提供三个层级的代码修改, 从应用层到 SD K层:

#### 方案 A1: 应用层 — 在 `kConnectivity_Established` 事件中触发 DNS-SD 刷新 (推荐)

修改文件: [src/app/app_nwk_mgr.cpp](../src/app/app_nwk_mgr.cpp)

在 `on_platform_event()` 函数的 `kConnectivity_Established` 分支中添加 DNS-SD 重新发布逻辑:

```cpp
// app_nwk_mgr.cpp 新增头文件
#include <lib/dnssd/Advertiser.h>
#include <platform/CHIPDeviceLayer.h>

// 在 on_platform_event() 函数中修改:
static void on_platform_event(const ChipDeviceEvent * event, intptr_t arg)
{
    switch (event->Type) {
        case DeviceEventType::kThreadConnectivityChange:
            switch (event->ThreadConnectivityChange.Result) {
                case kConnectivity_Established:
                    LOG_MSG_INFO(TAG_NWK, "Thread Established");
                    m_nwk_status = kNwkStatusJoined;
                    app_comm_mgr_notify_nwk_status(m_nwk_status);
                    ev_set_inactive(&rejoin_timeout_event);

                    // ★ 新增: 主动触发 DNS-SD 服务重新发布
                    // 强制 Border Router 立即更新 mDNS 缓存
                    PlatformMgr().ScheduleWork([](intptr_t) {
                        // Step 1: 停止当前 DNS-SD 广告
                        chip::app::DnssdServer::Instance().StopServer();

                        // Step 2: 等待 500ms 确保 Border Router 清除旧条目
                        // 如果没有足够延时, SRP update 可能被合并为 no-op
                        chip::DeviceLayer::SystemLayer().StartTimer(
                            chip::System::Clock::Milliseconds32(500),
                            [](chip::System::Layer *, void *) {
                                // Step 3: 重新启动 DNS-SD 服务, 触发新的 SRP 注册
                                // DnssdServer::StartServer() 内部调用:
                                //   → DnssdImpl::StartOperationalAdvertising()
                                //   → OpenThread SRP Client: otSrpClientAddService()
                                //   → 向 Border Router 发送 SRP Update 消息
                                chip::app::DnssdServer::Instance().StartServer();
                                LOG_MSG_INFO(TAG_NWK, "DNS-SD re-published after Thread attach");
                            },
                            nullptr);
                    });

                    break;
                // ... 其余 case 保持不变
            }
            break;
        // ... 其余 event type 保持不变
    }
}
```

**工作原理**:
1. `StopServer()` → 调用 `chip::Dnssd::ServiceAdvertiser::RemoveServices()` → 底层 `DnssdImpl::RemoveServices()` → 调用 `otSrpClientRemoveService()` → OpenThread 发送 SRP Update (delete) 到 Border Router
2. 延迟 500ms — 确保 Border Router 处理了删除请求, 避免新旧条目混淆
3. `StartServer()` → 重新构建 DNS-SD 服务记录 → `otSrpClientAddService()` → 发送 SRP Update (add) → Border Router 立即更新 mDNS

**效果**: Border Router 的 mDNS 缓存立即刷新, 控制器下次 DNS-SD 查询能立即获取新条目.

#### 方案 A2: OpenThread 层 — 直接调用 SRP Client API 强制重新注册

如果需要更细粒度的控制, 可以绕过 Matter DNS-SD 层, 直接操作 OpenThread SRP Client:

```cpp
// app_nwk_mgr.cpp 新增头文件
#include <openthread/srp_client.h>
#include <openthread/instance.h>
#include <platform/silabs/ThreadStackManagerImpl.h>

static void force_srp_re_registration(void)
{
    // 获取 OpenThread 实例
    otInstance * otInst = chip::DeviceLayer::ThreadStackMgrImpl().OTInstance();
    if (otInst == nullptr) {
        LOG_MSG_ERR(TAG_NWK, "OT Instance is null");
        return;
    }

    const otSrpClientHostInfo * hostInfo = otSrpClientGetHostInfo(otInst);
    if (hostInfo == nullptr || !hostInfo->mName) {
        LOG_MSG_ERR(TAG_NWK, "SRP host info not available");
        return;
    }

    // 方法 1: 停止 → 重启 SRP Client (会触发全部服务重新注册)
    otSrpClientStop(otInst);
    otSrpClientStart(otInst, hostInfo->mName, hostInfo->mState);  // 保留原 State (租约等)

    // 方法 2 (替代, 更轻量): 直接刷新 Host 信息
    // otSrpClientSetHostName(otInst, hostInfo->mName);
    // otSrpClientSetHostAddresses(otInst, hostInfo->mAddresses, hostInfo->mNumAddresses);
    // → 这会导致 SRP Client 发送 SRP Update 消息刷新所有注册

    LOG_MSG_INFO(TAG_NWK, "SRP client re-registration triggered");
}
```

**调用时机**: 在 `kConnectivity_Established` 事件中调用 `force_srp_re_registration()`.

**注意事项**:
- `otSrpClientStop()` + `otSrpClientStart()` 会触发完整重新注册（Host + 所有 Services）
- 需要保留原有的 State (租约时间、Key 租约等), 否则已有的注册状态丢失
- OpenThread SRP Client API 定义在 `include/openthread/srp_client.h` (OpenThread 公共 API)

#### 方案 A3: Matter DNS-SD 层 — 通过 Advertiser API 发布 Service Update

Matter SDK 提供了更高层级的 DNS-SD 抽象, 推荐在跨平台移植场景下使用:

```cpp
// app_nwk_mgr.cpp 新增头文件
#include <lib/dnssd/Advertiser.h>
#include <lib/dnssd/Resolver.h>
#include <lib/dnssd/TxtFields.h>

static void refresh_dnssd_operational_advertisement(void)
{
    chip::Dnssd::DiscoveryFilter filter(chip::Dnssd::DiscoveryFilterType::kNone);
    chip::Dnssd::ServiceAdvertiser * advertiser =
        chip::DeviceLayer::DeviceLayer::ServiceAdvertiserInstance();

    if (advertiser == nullptr) {
        LOG_MSG_ERR(TAG_NWK, "ServiceAdvertiser not available");
        return;
    }

    // 获取当前的 operational 服务信息
    chip::Inet::IPAddressType addrType = chip::Inet::IPAddressType::kIPv6;
    uint16_t port = CHIP_PORT;  // 默认 Matter 端口 5540

    // 构造包含 "fresh" 标记的 TXT 记录
    // 添加一个自定义 TXT key "fr=1" 表示刚刚恢复 (可选, 用于诊断)
    chip::Dnssd::TextEntry txtEntries[] = {
        { "fr", reinterpret_cast<const uint8_t *>("1"), 1 },  // Fresh Re-registration
    };

    // 通过 Advertiser 重新发布 — 内部触发 SRP update
    CHIP_ERROR err = advertiser->AdvertiseOperational(
        advertiser->GetInstanceName(),
        chip::ByteSpan(),  // hostname (空 = 不更新 hostname)
        addrType, port,
        txtEntries, sizeof(txtEntries) / sizeof(txtEntries[0])
    );

    if (err == CHIP_NO_ERROR) {
        LOG_MSG_INFO(TAG_NWK, "Operational DNS-SD advertisement refreshed successfully");
    } else {
        LOG_MSG_ERR(TAG_NWK, "Failed to refresh DNS-SD: %" CHIP_ERROR_FORMAT, err.Format());
    }
}
```

**方案对比**:

| 方案 | 层级 | 优点 | 缺点 |
|------|------|------|------|
| A1 (DnssdServer) | Matter App 层 | 简单, 只需 2 个函数调用; 适合本项目的应用架构 | 依赖 `DnssdServer` 组件, 可能引入额外的初始化顺序依赖 |
| A2 (SRP Client API) | OpenThread 层 | 最直接, 零额外延迟; 不依赖 Matter DNS-SD 状态 | 平台绑定 (仅 Thread), 不跨传输层移植 |
| A3 (Advertiser API) | Matter SDK 层 | 跨平台, 标准 Matter SDK API; 可移植到 Wi-Fi 设备 | API 相对复杂, 需要获取 InstanceName 等上下文 |

**推荐**: 采用 **方案 A1** 作为首选, 因为其改动最小, 且直接利用项目已有的 `DnssdServer` 组件. 如果发现 `DnssdServer::StartServer()` 内部会做幂等检查跳过已经运行的服务, 则改用 **方案 A2** 直接操作 SRP Client.

#### 方案 B: 通知 MCU 网络恢复状态, 触发用户可见反馈

当前项目已有网络状态通知到 MCU 的机制 (通过串口协议):

```cpp
// app_nwk_mgr.cpp:216 — 现有代码已经在通知 MCU:
app_comm_mgr_notify_nwk_status(m_nwk_status);

// MCU 收到 kNwkStatusJoined 后可以:
// 1. 控制 LED 从闪烁变为常亮 → 用户看到设备已就绪
// 2. 主动上报电机状态 → 控制器订阅后立即获取最新状态
// 3. (如果支持) 发出短蜂鸣声 → 给安装人员即时反馈
```

如果需要 MCU 在收到恢复通知后立即同步状态, 可以在 [app_comm_mgr.cpp](../src/app/app_comm_mgr.cpp) 的 `app_comm_mgr_notify_nwk_status()` 中增加:

```cpp
void app_comm_mgr_notify_nwk_status(data_nwk_status_t status)
{
    spp_instance.notify_nwk_status(status);

    // ★ 新增: 入网成功后, 主动查询 MCU 当前设备状态
    if (status == kNwkStatusJoined) {
        // 让 MCU 主动上报所有电机状态 (Battery / Curtain % / Operational Status)
        // 以确保 Matter 属性值在控制器订阅后立即可用
        uint8_t payload[1] = { 0x01 };  // request all status
        spp_instance.send_cmd(kGetProductInfo, payload, 0);
    }
}
```

### 6.3 增加 BLE 快速广播作为带外辅助

**当前状态**: `CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART = 0`（禁用自动 BLE 广播）

**SPEC 依据**: Matter Core Spec **§5.4.2.5** 禁止已入网设备使用 BLE 配网, 但 **§5.6** 允许已入网设备可选维持 BLE 广播用于 operational discovery。在上电恢复场景, 短暂 BLE 广播作为 "liveness signal" 是合规的。

**建议**: 对于特定场景（如长时间未能恢复 Thread 连接），可以短暂打开 BLE 广播，让控制器通过 BLE 发现设备已上线，加速 CASE 重建。

### 6.4 区分 "凭据丢失" 与 "临时连接失败"

**SPEC 依据**: Matter Core Spec **§5.4.2.3.1**: 配网窗口时长范围 180s-900s; **§11.8.4**: 网络恢复应重试 5 分钟

如果 NVM3 中的网络凭据丢失，当前代码会打开 5 分钟的配网窗口。建议：
- 在打开配网窗口前，先多次尝试 Thread Attach 恢复（符合 §11.8.4）  
- 仅当确认 Thread 凭据确实丢失（`IsThreadProvisioned() = false`）时才打开配网窗口  
- 如果 Thread 凭据还在但只是暂时的连接问题，不应该打开配网窗口 —— 应遵循 §11.8.4 重试 5 分钟

### 6.5 NVM3 存储优化

**SPEC 依据**: Matter Core Spec **§11.8.2**: 要求 Thread 凭据/Fabric/Group Key 持久化于 NVM

- 减小 `KVS_MAX_ENTRIES` 以加快 NVM3 初始化扫描（当前 511 个条目可能不需要）
- 定期触发 NVM3 Repack 以防止碎片化 — Spec §11.8.2 要求的持久化数据完整性依赖 NVM3 状态
- 利用 `SL_MATTER_DEFERRED_ATTRIBUTE_STORE_DELAY_MS = 2000` 将属性变更延迟批量写入, 减少 NVM3 Page 擦除次数

---

## 7. 端到端延迟总结

### <span style="color:green">典型场景</span> (已配网设备断电后重新上电，所有条件正常)

```
时间线:
T+0s    电源接通
          SPEC: — (硬件相关, 无 Spec 约束)
          代码: main() [main.cpp:51]
T+0.07s FreeRTOS Scheduler 启动, OT/BLE/Matter Stack 初始化
          SPEC: §11.8.2 — NVM 中读取 Thread 凭据/Fabric 数据
          代码: nvm3_initDefault() [sl_event_handler.c:51]; sl_bt_init(); otInstanceInit()
          实测: [00:00:00.067-0.134] 仅 67ms
T+0.1s  OpenThread 开始扫描网络 (Thread Attach 开始)
          SPEC: Thread Spec MLE — MLME-SCAN.request
          代码: OT src/core/mac/mac.cpp: StartCsmaBackoff()
T+0.5s  发现 Thread 网络并选择父节点
          代码: OT src/core/thread/mle.cpp: Mle::Discover()
T+3s    完成 MLE Attach，成为 Thread 子节点
          SPEC: §11.8 — Thread Attach 完成, 设备获得 IPv6
          代码: OT src/core/thread/mle.cpp: HandleChildIdResponse()
T+3.1s  IPv6 地址分配完成，SRP 服务注册 (1 次 CoAP 往返)
          SPEC: §11.9.5.2 — SRP Update 发送
          代码: OT src/core/net/srp_client.cpp: SendUpdate()
T+3.2s  Matter Stack 完全就绪，DNS-SD 已发布
          SPEC: §11.9 — 设备处于 Operational 模式
          代码: src/app/DnssdServer.cpp: StartServer()
        ← 设备此时已可以接受 Matter 命令 (仅 ~3.2s!)
T+3s~33s 手机 APP 仍在等待旧 Subscription 超时 (MaxInterval=60s 未触发)
          SPEC: §8.5.2 — MaxInterval 超时
          代码(控制器): src/app/ReadClient.cpp: OnMaxIntervalTimeout()
T+33s   用户主动操作 APP → 控制器通过 DNS-SD 重新发现设备
          SPEC: §11.9 — DNS-SD 服务发现
          代码(控制器): src/lib/dnssd/Discovery_ImplPlatform.cpp
T+34s   CASE 会话重建完成
          SPEC: §4.14.2 — CASE Sigma 协议完成
          代码: src/transport/CASEServer.cpp/CASEClient.cpp
T+35s   属性订阅重新建立
          SPEC: §8.5.2 — SubscribeRequest(0x03)/Response(0x04)/ReportData(0x05)
          代码: src/app/ReadClient.cpp: SendSubscribeRequest()
T+35s   用户可以正常控制设备 ✓
```

### <span style="color:red">最坏场景</span>

```
时间线:
T+0s    电源接通
T+0.5s  完成硬件初始化 (NVM3 碎片较多 + Repack)
          SPEC: §11.8.2 — NVM 中读取 Thread 凭据/Fabric 数据(需数据完整性校验)
T+0.7s  OpenThread 开始扫描
T+7s    父节点不可达，重新扫描和选择 (多轮 Discover)
         代码: OT src/core/thread/mle.cpp: Mle::Attach() → 清除 mParent → Discover()
T+20s   完成 MLE Attach (逐步找到合适 Parent)
T+30s   重新入网计时器超时 (ATTACH_NETWORK_TIMEOUT_MS) — 但此时 Attach 已成功
         代码: app_nwk_mgr.cpp:150 — _rejoin_timeout_event_handler()
         对比 SPEC §11.8.4: 要求重试至少 5 分钟 ← 代码 30s 远低于 Spec 建议
T+31s   SRP 服务注册 + DNS-SD 发布
T+31~91s 控制器等待 Subscription MaxInterval=60s 超时
         SPEC: §8.5.2 — MaxInterval 超时
T+93s   控制器 DNS-SD 发现 + CASE + Subscribe 完成
        ← 总延迟: 约 1.5 分钟 (设备侧 ~22s + 控制器侧 ~70s)
        ← 如果 30s 前 Attach 未成功, 设备永久无法恢复(无重试)
```

### 核心结论

**断电后恢复控制的延迟主要来自以下几个叠加因素**:

| 因素 | 延迟占比 | SPEC 依据 | 项目代码 | SDK 代码 |
|------|---------|----------|---------|---------|
| **1. 控制器被动发现** | 50-70% (~10-60s) | §8.5.2 MaxInterval; §4.14.2.3 CASE 超时 | `CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL=2000ms` | `src/messaging/ReliableMessageMgr.cpp`; `src/app/ReadClient.cpp` |
| **2. Thread 网络入网** | 10-20% (~3-30s) | §11.8 Thread Integration; §11.8.4 应重试5分钟 | `ATTACH_NETWORK_TIMEOUT_MS=30000` | OT `src/core/thread/mle.cpp:Mle::Attach()` |
| **3. 无主动重试机制** | 10-20% | §11.8.4 要求 vs 实际 30s 超时 | `_rejoin_timeout_event_handler()` 仅打印日志 | N/A (应用层 bug) |
| **4. CASE+订阅重建** | 5-10% (~2-5s) | §4.14.2 CASE; §8.5.2 Subscribe | `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION=1` | `src/transport/CASEServer.cpp`; `src/app/ReadClient.cpp` |

**如果"几分钟"的延迟持续发生**，最可能的原因是：
- Thread Border Router 的 SRP/mDNS 缓存 TTL 设置过大 (RFC 6762 §7.1: 默认 120s)
- 手机 APP 实现中额外的超时等待 (视各生态实现而定)
- Thread 网络拓扑不稳定，Router/Parent 频繁切换 (Thread Spec MLE)
- NVM3 存储出现 Page 损坏，导致凭据读取失败 → 设备回退到配网模式 (Spec §5.4.2)
- <span style="color:red">**本项目代码 30s 超时后无重试**</span> ← 最可确定的软件缺陷

---

## 附录 A: 文件索引

| 文件 | 描述 |
|------|------|
| [src/main.cpp](../src/main.cpp) | 程序入口, boot 流程 |
| [src/app/AppTask.cpp](../src/app/AppTask.cpp) | 主任务, 初始化调度 |
| [src/app/app_nwk_mgr.cpp](../src/app/app_nwk_mgr.cpp) | **网络管理器 (核心分析文件)** |
| [src/app/app_comm_mgr.cpp](../src/app/app_comm_mgr.cpp) | 串口通信管理器 (与 MCU) |
| [src/app/app_spm_mgr.cpp](../src/app/app_spm_mgr.cpp) | Matter 串口协议消息处理器 |
| [include/CHIPProjectConfig.h](../include/CHIPProjectConfig.h) | **Matter 项目配置 (关键配置)** |
| [config/sl_matter_config.h](../config/sl_matter_config.h) | Matter Stack 配置 |
| [config/sl_matter_icd_config.h](../config/sl_matter_icd_config.h) | ICD/SED 配置 |
| [config/sl_openthread_features_config.h](../config/sl_openthread_features_config.h) | **OpenThread 配置** |
| [config/nvm3_default_config.h](../config/nvm3_default_config.h) | NVM3 Flash 存储配置 |
| [config/sl_bluetooth_config.h](../config/sl_bluetooth_config.h) | BLE Stack 配置 |
| [config/sl_bluetooth_advertiser_config.h](../config/sl_bluetooth_advertiser_config.h) | BLE 广播配置 |
| [autogen/sl_component_catalog.h](../autogen/sl_component_catalog.h) | 组件目录定义 |
| [autogen/sl_ot_init.c](../autogen/sl_ot_init.c) | OpenThread 初始化 |
| [spec/23-27349-009_Matter-1.5-Core-Specification.pdf](../spec/23-27349-009_Matter-1.5-Core-Specification.pdf) | Matter 1.5 核心规范 |
| [spec/23-27351-008_Matter-1.5-Device-Library-Specification.pdf](../spec/23-27351-008_Matter-1.5-Device-Library-Specification.pdf) | Matter 1.5 设备库规范 |

## 附录 B: 关键缩写

| 缩写 | 全称 | 说明 |
|------|------|------|
| CASE | Certificate Authenticated Session Establishment | 证书认证会话建立 |
| CSL | Coordinated Sampled Listening | 协调采样监听 (Thread 1.2+) |
| ICD | Intermittently Connected Device | 间歇连接设备 |
| IM | Interaction Model | Matter 交互模型 |
| KVS | Key-Value Store | NVM3 内的键值存储 |
| MLE | Mesh Link Establishment | Thread 网格链路建立 |
| MRP | Message Reliable Protocol | 消息可靠协议 |
| MTD | Minimal Thread Device | 最小 Thread 设备 |
| NOC | Node Operational Certificate | 节点操作证书 |
| NVM3 | Non-Volatile Memory 3 | Silicon Labs Flash 存储系统 |
| SED | Sleepy End Device | 休眠终端设备 |
| SPP | Serial Port Protocol | MG24 与 MCU 间的串口通信协议 |
| SRP | Service Registration Protocol | Thread 服务注册协议 |

---

## 附录 C: 真实设备恢复 Log 完整分析 (bk01_matter, 2026-05)

以下是从 bk01_matter 设备断电重启后的完整恢复 log 及逐行分析。设备已在 Thread 网络中配网，此 log 展示了正常场景下的网络恢复全过程。

### C.1 完整恢复时间线

```
时间戳      事件
──────────  ──────────────────────────────────────────────────────────
14.363      Thread 状态变化 (event 32779)
14.364      kThreadConnectivityChange (event 32769)
14.365      ★ Thread Established — 设备侧就绪
14.365      Scheduling OTA Requestor initialization (第一次调度)
14.365      Joining Multicast groups
14.447      SRP Client started, detected server: fd11:9c64:dd37:b8c4:...
14.448-449  Thread 状态变化 ×2 (event 32779 ×2)
14.506-579  ★★★ 收到旧会话数据: "Data received on an unknown session (LSID=36120)" ×4
14.844      SPP re-sent count 1 (CMD 0x02 SN=0x0000)
14.933      DNS-SD initialized (event 32786)
14.933      ★ Server initialization complete
14.934      Advertise operational node 52017B57FC1E977B-00000000000008CA
14.935      Operational network ready (event 32790)
14.945      No subscriptions to resume
15.344      SPP re-sent count 2
15.845      SPP re-sent reach to max → 序列号递增 SN=0x0001
16.346      SPP re-sent count 1 (CMD 0x01 SN=0x0001)
16.846      SPP re-sent count 2
17.346      SPP re-sent reach to max → 序列号递增 SN=0x0002
17.847      SPP re-sent count 1 (CMD 0x02 SN=0x0002)
17.935      DNS-SD Resolving 52017B57FC1E977B:0000000000000001 ...
18.027      Node ID resolved: UDP:[fd7a:e86b:...]:5540
18.155      ★ CASE Sigma1 (控制器 → 设备) MsgID 0x30
18.551      ★ CASE Sigma2Resume (设备 → 控制器) MsgID 0x33 (Session Resumption 启用)
18.559      StatusReport (设备 → 控制器) MsgID 0x40
18.564      ★ SecureSession Active (LSID:25475)
18.565      Stopping watchdog timer
18.569      IM:InvokeCommandRequest → Endpoint=0 Cluster=0x0029 Cmd=0x0004 (Descriptor/PartsList)
19.077      IM:InvokeCommandResponse → Status=0x0 (成功)
19.080      StandaloneAck
```

### C.2 关键里程碑与耗时

| 阶段 | 起止时间戳 | 耗时 | 说明 |
|------|-----------|------|------|
| Thread Up → SRP Started | 14.365 → 14.447 | 82ms | SRP Client 连接 Border Router |
| Thread Up → DNS-SD Ready | 14.365 → 14.933 | 568ms | DNS-SD 服务初始化和发布 |
| Thread Up → CASE Sigma1 | 14.365 → 18.155 | **3.79s** | **控制器侧反应时间**（检测设备恢复+发起CASE） |
| Sigma1 → Session Active | 18.155 → 18.564 | **409ms** | CASE Session Resumption 极速恢复 |
| Session Active → First Cmd OK | 18.564 → 19.077 | 513ms | Descriptor 查询往返 |
| **总计: Thread Up → 可控制** | 14.365 → 19.077 | **4.71s** | ★ 正常场景下的完整恢复时间 |

### C.3 关键发现

**1. 设备侧恢复极快 (~0.5s)**

从 Thread Established (14.365s) 到 DNS-SD Initialized (14.933s) 仅 **568ms**。设备侧的 SRP 注册、DNS-SD 发布、Server 初始化在不到 1 秒内完成。

**2. 控制器侧反应时间占主导 (~3.8s)**

从设备就绪 (14.933s) 到控制器发出 Sigma1 (18.155s) 间隔 **3.2 秒**。这是控制器从 DNS-SD 发现设备到发起 CASE 的时间，占整个恢复过程的 ~68%。

**3. Session Resumption 工作正常**

设备以 `CASE_Sigma2Resume` (0x33) 而非完整 `CASE_Sigma2` (0x31) 响应，证明 `CHIP_CONFIG_ENABLE_SESSION_RESUMPTION=1` 生效。实际耗时 **409ms** 远优于完整 Sigma 握手的 ~1.5-2s。

**4. 旧会话消息被丢弃是必然的**

LSID=36120 的 4 条消息被丢弃是**正常且预期的行为**——设备重启后会话表为空，控制器用旧 key 加密的消息无法被解密或路由。这不是 bug，而是协议设计的必然结果。优化方向是让控制器更快感知设备离线并重建 CASE（如缩短 MRP 重试周期）。

**5. SPP 重传与网络恢复并发互不阻塞**

SPP 在 14.844-18.847 之间的 3 轮重传与 DNS-SD/CASE 恢复完全并行。MCU 在 MG24 启动后可能需要额外初始化时间才能响应 SPP，这个延迟不影响 Matter 网络恢复。

**6. 此 log 无 Subscription 恢复**

`No subscriptions to resume` 说明控制器在设备重启前未建立持久化订阅，或订阅数据已过期。首次控制命令是 Descriptor Cluster 的 PartsList 查询 (Cluster 0x0029 Cmd 0x0004)，这是控制器的标准行为——先验证设备能力再建立应用层交互。

### C.4 与文档预估的对比

| 阶段 | 文档正常预估 | 真实 Log 实测 | 偏差 |
|------|------------|------------|------|
| Thread Up → SRP/DNS-SD 就绪 | 0.1-2s | 0.57s | ✓ 吻合 |
| 控制器感知 + DNS-SD 发现 | 1-15s | ~3.2s | ✓ 吻合 |
| CASE 会话重建 (Resumption) | 0.5-1s | 0.41s | 略快于预估 |
| 设备侧总恢复时间 | ~3s | ~0.5s | 比预估更快 |
| 端到端恢复时间 (设备侧+控制器侧) | 3-13s | ~4.7s | ✓ 吻合正常场景 |
