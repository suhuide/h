# Matter 1.7 TE2 测试活动 
---

# 第一部分：邮件中文内容

## 1.1 活动概要

致 Matter 工作组成员：

这是 **Matter 1.7 TE2 报名的最后提醒**。报名通道现已开放，
将于 **9 月 21 日 AoE（Anywhere on Earth）当天结束**时关闭，
报名详情见邮件末尾。
如果你之前报过名、但还没有进入该活动的**保密 Slack 频道**：
说明你的报名并未完成。此时请按邮件收到的指引（亦见下文）补全流程。

**活动形式**：本次为 **Gated Virtual（受控线上）活动**，
无需差旅、免费参加。

**参与门槛（Gated 系列要求）**：如果你想参加 Matter 1.7 的 **SVE**
（Self-Verification Event，自验证活动），**必须同时参加 TE#1（上一次活动）
和 TE#2（本次活动）**。

**目标**：1.7 TE2 的首要目标是验证设备是否符合 **1.7 版本目标特性**
的合规要求。

**时间**：2026 年 9 月 28 日 – 10 月 2 日（线上）。

**报名截止**：2026 年 9 月 21 日 EoD AoE。

## 1.2 报名流程与注意事项

- 数据收集使用联盟提供的在线工具 **TEDS（Test Event Data Stockpile）**：
  <https://zigbeecertifiedproducts.knack.com/test-event-data-stockpile-teds#teds-for-matter>
- **ATL（认可测试实验室）**需在 ATL 专用入口注册：
  <https://zigbeecertifiedproducts.knack.com/test-event-data-stockpile-teds#test-house-review>
- 进入 TEDS 后用 Sign Up 注册，或使用以往参加测试活动时创建的账号登录，
  然后在仪表盘里报名 **Matter 1.7 TE#2**。
  （没有 TEDS 账号可用公司邮箱自行注册，约 1 小时～最多 1-2 个工作日确认。）
- **DUT 注册**：每家公司必须为本活动注册一台 DUT（被测设备）。
  每位参与者必须使用已注册的 DUT 工作。（多人共用一台 DUT 时，由其中一人
  注册 DUT；所有参与者仍需各自单独报名活动。）
- 请使用**最新 PICS** 注册 DUT，并确认上传过程无报错——该信息用于评估
  各测试用例的支持情况。活动期间发布新版 PICS 后仍可更新。
- 报名完成（个人报名 + 挂到已注册 DUT 上）后，参与者会被加入 Slack 频道。
- 报名期内会收到 `test-events@csa-iot.org` 的自动邮件，**需要处理的情形**
  包括：已报名但未挂到 DUT、被分配到 DUT 但本人未报名——这些情况下报名
  都算未完成。一般完成全部报名要求（含确认 DUT 参加过完整 gated 系列）
  后 1 小时～最多 1 个工作日会被拉入活动 Slack 频道。
- 疑问联系：`test-events@csa-iot.org`。

## 1.3 计划特性清单（1.7）

> 注意：此列表可能变化，部分特性可能按 TSG（技术规范组）决议从 1.7 中移除。

| 焦点领域 | 1.7 特性 |
|---|---|
| DMTT | Q-quality（质量等级）变更 |
| | Device location（设备位置） |
| | Wildcard Filtering（通配过滤） |
| TCR | Thermostat Mode（温控器模式） |
| | Smoke Concentration Measurement（烟雾浓度测量） |
| PQC | PQC Phase 1（后量子密码第一阶段） |
| Commissioning over Thread | Thread 配网 |
| Network Recovery | Network Recovery（网络恢复） |
| Networking Improvements | Invoke/Write 中的 "SuppressResponse" |
| | 订阅 DataReport 交错发送（Stagger Subscription DataReport） |
| Energy Management | 智能电气报警 [ESALM] |
| | 配电 [ELDIST] |
| | 智能配电盘：电气保护报警 [EPALM] |
| | 电力拓扑 [PWRTL] |
| | 外部电价（External Tariff） |
| | DEM PowerRangeAdjustment 特性 |
| HRAP | 服务注册代理（SRP） |
| | 配网代理（Commissioning Proxy, CP） |
| | 每设备凭证（Per Device Credentials, PDC） |
| | TBR 诊断（TBR Diagnostics） |
| HVAC | 温控器传感器 |
| | 温控器事件 |
| | 温控器关键保护（Critical Protection） |
| Ambient Sensing | 合并的环境感知特性 |
| Ambient Sensing | 空气质量 |
| | 湿度计（Humidistat） |
| Proximity Ranging | 接近测距 |
| Closures | 访问类闭合装置（Access Closures） |
| Cameras | AV 分析 cluster |
| | 区域灵敏度（Zone sensitivity） |
| | 远程区域（Remote zones） |
| Media clusters | 扬声器设备类型 |
| | 音频消息 |
| Home Appliances | 温控柜拓扑（Temperature Controlled Cabinet Topology） |
| Scenes | Color Control cluster |
| | Scenes 修复 |
| Groups | Groups 软弃用（soft deprecation） |
| NFC-based commissioning | NFC 配网测试改进 |

## 1.4 设备类型（Device Types）——新增/更新

| 设备类型 | Revision | 1.7 规格更新内容 |
|---|---|---|
| Ambient Context Sensor（环境上下文传感器） | 2 | 新增 |
| Arc Fault Circuit Interrupter（电弧故障断路器） | 1 | 新增 |
| Auxiliary Load Switch（辅助负载开关） | 1 | 新增 |
| AV Analysis Node（AV 分析节点） | 1 | 新增 |
| Casting Audio Player（投屏音频播放器） | 1 | 新增 |
| Commissioning By Proxy（配网代理） | 1 | 新增 |
| Electrical Circuit Breaker（电路断路器） | 1 | 新增 |
| Electrical Distribution Enclosure（配电箱） | 1 | 新增 |
| Electrical Surge Protector（电涌保护器） | 1 | 新增 |
| Humidity Conditioner（湿度调节器） | 1 | 新增 |
| Irrigation System（灌溉系统） | 1 | 新增 |
| Proximity Ranger（接近测距器） | 1 | 新增 |
| Residual Current Circuit Breaker（剩余电流断路器） | 1 | 新增 |
| Streaming Audio Player（流媒体音频播放器） | 1 | 新增 |
| Basic Video Player | 4 | 新 cluster——新媒体集群 |
| Camera | 2 | 新 cluster——AV 分析集群 |
| Casting Video Player | 3 | 新 cluster——媒体文件管理 |
| Closure | 2 | 新 condition——AccessDevice |
| Closure Panel | 2 | 新 condition——AccessDevice |
| Electrical Sensor | 2 | 新 cluster——电气报警 |
| Network Infrastructure Manager（网络基础设施管理器） | 3 | 新 cluster——NIM、TBRD、SRP、配网代理 |
| Oven（烤箱） | 3 | 新 cluster——柜内拓扑 |
| Refrigerator（冰箱） | 4 | 新 cluster——柜内拓扑 |
| Room Air Conditioner（房间空调） | 5 | 新 cluster——温控器模式 |
| Smoke CO Alarm（烟 CO 报警器） | 3 | 新 cluster——烟雾浓度 |
| Speaker | 2 | 新 cluster——音频控制 |

## 1.5 集群（Clusters）——新增/更新

**新增集群（除注明外均为 App 层 rev 1）：**

| 集群 | Revision |
|---|---|
| Ambient Context Sensing（环境上下文感知） | 2 |
| Ambient Sensing Union（环境感知联合） | 1 |
| Audio Control（音频控制） | 1 |
| AV Analysis（AV 分析） | 1 |
| Commissioning Proxy（配网代理） | 1 |
| Electrical Distribution（配电） | 1 |
| Electrical Alarm（电气报警） | 1 |
| Electrical Protection Alarm（电气保护报警） | 1 |
| Humidistat（湿度计） | 1 |
| Media File Management（媒体文件管理） | 1 |
| Network Identity Management（网络身份管理） | 1 |
| Proximity Ranging（接近测距） | 1 |
| Smoke Concentration Measurement（烟雾浓度测量） | 6 |
| Temperature Controlled Cabinet Topology（温控柜拓扑） | 1 |
| Thermostat Mode（温控器模式） | 1 |
| Thread Border Router Diagnostics（TBR 诊断） | 1 |
| Water Tank Level Monitoring（水箱水位监测） | 1 |

**更新集群：**

| 集群 | 层 | Revision | 1.7 更新原因 |
|---|---|---|---|
| Account Login | App | 3 | 媒体特性 |
| Content Launcher | App | 3 | 媒体特性 |
| Color Control | App | 10 | 新增可场景化属性（scenable attribute） |
| Device Energy Management | App | 5 | PowerRangeAdjustment 特性 |
| Messages | App | 4 | 媒体特性 |
| Media Playback | App | 3 | 媒体特性 |
| Power Source Configuration | Core | 2 | DMTT 编辑性修改（无功能变化） |
| Pump Configuration and Control | App | 6 | DMTT——Q quality |
| Basic Information | Core | 7 | DMTT——device location |
| Bridged Device Basic Information | Core | 7 | DMTT——device location |
| Closure Control | App | 2 | Access Closures |
| Closure Dimension | App | 2 | Access Closures |
| Commodity Tariff | App | 2 | 能源——电价外部 ID |
| Fan Control | App | 7 | DMTT——Q quality |
| General Diagnostics | Core | 4 | HRAP——SRP |
| Group Key Management | Core | 4 | Groups |
| Groups | App | 5 | Groups |
| Network Commissioning | Core | 3 | HRAP——PDC |
| Operational Credentials | Core | 3 | PQC |
| Occupancy Sensing | App | 8 | 环境感知 |
| On/Off | App | 7 | DMTT——Q quality |
| Power Source | Core | 4 | DMTT 编辑性修改（无功能变化） |
| Power Topology | Core | 2 | 能源——电气保护 |
| Flow Measurement | App | 5 | DMTT 编辑性修改（无功能变化） |
| Illuminance Measurement | App | 5 | DMTT 编辑性修改（无功能变化） |
| Push AV Stream Transport | App | 3 | Camera 更新 |
| Scenes Management | App | 2 | Scenes 修复 |
| Temperature Measurement | App | 6 | DMTT 编辑性修改（无功能变化） |
| Thermostat | App | 12 | HVAC 温控器工作 |
| Valve Configuration and Control | App | 2 | DMTT——Q quality |
| Zone Management | App | 2 | Camera 更新 |

**两条备注：**
1. **浓度测量类集群**：所有现有别名浓度测量集群（甲醛、PM2.5 等）revision
   统一 +1，但**无功能变化**——原因是基类为烟雾浓度新增了枚举值。
2. **Mode Base 派生集群**：所有 Mode Base 派生集群 revision +1，原因是新增
   CoreModes condition。该 condition 只在 thermostat mode 集群上受支持，
   因此其他集群的 +1 不代表功能变化。

**其余集群与 1.6.1 发布版保持一致。**

## 1.6 测试用例清单（按领域归类）

- **基础/数据模型**：TC-BINFO-2.1、TC-BRBINFO-2.1、TC-RR-1.1、TC-IDM-4.5、
  TC-IDM-10.1~10.7、TC-IDM-12.1
- **DMTT/Q 质量**：TC-OO-2.8、TC-FAN-3.5
- **温控模式（TCR）**：TC-TSTATM-1.2、2.1、3.2、3.4
- **设备认证 / PQC**：TC-DA-1.10~1.13、TC-OPCREDS-3.9
- **Thread 配网**：TC-SC-TC-1.1/1.2/2.1/2.2/3.1/3.2/4.1/4.2
- **通用调试**：TC-CGEN-2.12/2.13
- **NFC 配网**：TC-DD-2.3、2.4、3.23~3.27、4.1、4.2
- **能源管理**：TC-ESALM-2.1~2.4、3.1、TC-ELDIST-2.1、TC-EPALM-2.1~2.3、3.1、
  TC-PWRTL-2.1/2.2、TC-SETRF-2.1/3.1、TC-DEM-2.11
- **HRAP**：TC-SRP-1.1~1.2、2.1~2.3、3.1~3.3、4.1~4.4、TC-COMPRO-2.1~2.9、
  TC-NETIM-1.1~1.6、TC-TBRD-2.1
- **HVAC**：TC-TSTAT-2.1/2.2/2.3/4.4
- **环境感知**：TC-ASU-2.1/2.2/3.1、TC-ACS-2.1、3.1~3.3
- **湿度**：TC-HSTAT-2.1~2.6
- **接近测距**：TC-PROXR-2.1~2.4、3.1~3.3
- **闭合装置**：TC-CLCTRL-7.1~7.4、TC-CLDIM-5.1~5.3、6.1/6.2
- **相机/媒体**：TC-AVANALY-2.1~2.14、TC-ZONEMGMT-2.5、
  TC-MEDIAFILEMANAGEMENT-1.1/2.1/2.2/3.1/3.2、TC-AUDIOCONTROL-2.1~2.8、
  TC-ALOGIN-12.3、TC-CONTENTLAUNCHER-10.8~10.10、TC-MEDIAPLAYBACK-6.11/6.12、
  TC-MESS-1.1/3.1~3.3
- **家电**：TC-TCCTOPO-2.1
- **灯/Scenes/Groups**：TC-CC-10.1、TC-S-2.2、TC-G-2.2/2.3/2.4

---

# 第二部分：版本演进分析（1.5 → 1.6 → 1.7）

> 说明：1.5 / 1.6 的内容基于 CSA 公开发布信息整理（1.7 部分以本邮件为准），
> 细节以 CSA 官方 release notes 为准。

## 2.1 Matter 1.5（2025 年）要点回顾

- **能源管理深化**：Device Energy Management 集群与设备类型完善，
  面向电热水器、电池储能、EV 充电等需求响应场景；
- **水管理**：水阀、水泵、水箱水位（Water Tank Level）等引入；
- **Commodity Tariff（商品电价）集群进入 spec**：为能源调度提供价格信号
  （1.7 在此基础上补"电价外部 ID"）；
- **Mode Base 派生集群机制**：为后续"温控器模式"等派生集群打基础
  （1.7 的 CoreModes condition 即其延伸）。

## 2.2 Matter 1.6（2025 年末）要点回顾

- **Camera（摄像头）设备类型首次进入规范**：引入 `Push AV Stream Transport`
  集群（推流传输）、`Zone Management` 集群（移动侦测区域管理），
  摄像头作为原生 Matter 设备类型落地（此前只能桥接）；
- 在 1.5 能源/水管理基础上继续打磨。

> 佐证：1.7 邮件中 "Push AV Stream Transport rev 3 = Camera 更新"、
> "Zone Management rev 2 = Camera 更新"、"Camera rev 2 = 新增 AV 分析集群"
> —— 正是 1.6 摄像头主线在 1.7 的延续。

## 2.3 Matter 1.7 新增内容分析（相对 1.6）

按增量性质归纳为六类：

### A. 安全基线升级（影响所有设备）★最重要

- **PQC（后量子密码）Phase 1**：Operational Credentials rev 3。
  在现有 ECDSA/P256 基础上引入抗量子攻击密码套件（ML-DSA 类），
  对**所有设备型号的固件升级路径、证书链、烧录工具链都有影响**，
  是 1.7 中波及面最广的一项；
- 对应测试：TC-DA-1.10~1.13、TC-OPCREDS-3.9。

### B. 家庭网络基础设施（HRAP：Home Router Access Point）★新角色

1.7 引入"家庭路由接入点"方向，Matter 设备可承担部分网络基础设施职能：
- **SRP 服务注册代理**（General Diagnostics rev 4）；
- **配网代理 Commissioning Proxy**（新集群 + 新设备类型）——由已入网
  设备代理新设备配网；
- **每设备凭证 PDC**（Network Commissioning rev 3）——凭证粒度细化；
- **TBR 诊断**（新集群 Thread Border Router Diagnostics）；
- **Network Recovery**（网络恢复）；
- 新设备类型 **Network Infrastructure Manager**（rev 3）。

### C. 能源与配电（1.5 能源线的延伸）

- 智能电气报警 [ESALM]（新集群 Electrical Alarm）；
- 配电 [ELDIST]（新集群 Electrical Distribution + 配电箱/断路器/
  电涌保护器/剩余电流断路器一整套新设备类型）；
- 电气保护报警 [EPALM]（新集群）；
- 电力拓扑 [PWRTL]（Power Topology rev 2）；
- 外部电价（Commodity Tariff rev 2）；
- DEM 新特性 PowerRangeAdjustment（功率范围调整，需求响应细化）。

### D. 感知与家电扩展

- **环境感知**：合并 Ambient Sensing 特性，新增
  Ambient Context Sensing / Ambient Sensing Union 集群；Occupancy rev 8；
- **湿度调节器**（Humidistat 新集群 + Humidity Conditioner 设备类型）；
- **接近测距**（Proximity Ranging 新集群 + Proximity Ranger 设备类型）；
- **HVAC**：温控器模式（新集群 + CoreModes condition）、温控器传感器/
  事件/关键保护（Thermostat rev 12）；
- **家电**：温控柜拓扑（烤箱/冰箱 rev 更新）；
- **烟雾浓度测量**（Smoke CO Alarm rev 3）。

### E. 多媒体与闭合装置（1.6 相机线的延伸）

- **AV Analysis 集群**（相机端 AI 分析结果上报）；
- **媒体文件管理**、Audio Control 集群 + Speaker / Casting / Streaming
  音频设备类型（音频从"播放控制"扩展到"音频消息与文件"）；
- Account Login / Content Launcher / Media Playback / Messages rev 更新；
- **闭合装置**：Closure / Closure Panel rev 2 + AccessDevice condition
  （智能门锁/门禁类闭合装置的访问语义）。

### F. 数据模型质量与配套（DMTT Q-quality）

- **Q-quality**：On/Off rev 7、Fan Control rev 7、Pump rev 6、Valve rev 2
  等——对既有集群做规范质量修订（补齐一致性描述与测试），
  多数"无功能变化"，但**认证测试用例会更新**（如 TC-OO-2.8）；
- **Device location**：Basic Information / Bridged Device Basic Information
  rev 7，新增设备位置属性；
- **Groups 软弃用**：Groups rev 5 + Group Key Management rev 4——开始标注
  迁移方向，但未删除（现有控制器生态仍依赖）；
- **Scenes 修复**：Scenes Management rev 2 + Color Control rev 10
  （新增可场景化属性，场景与颜色联动修复）；
- 协议层：Invoke/Write 的 **SuppressResponse**、订阅报告交错发送
  （Stagger Subscription DataReport）——削平大订阅负载的报文突发；
- **Wildcard Filtering**（通配过滤）。

## 2.4 相对 1.5 / 1.6 的增量对照表

| 领域 | 1.5 | 1.6 | 1.7（新增） |
|---|---|---|---|
| 安全 | — | — | **PQC Phase 1**（后量子）★全员影响 |
| 配网 | — | — | **Thread 配网**、NFC 改进、**配网代理 CP/PDC** |
| 网络 | TBR 起步 | — | **HRAP 全家桶**（SRP/TBRD/Network Recovery/网络基础设施管理器） |
| 能源 | DEM/电价引入 | 打磨 | **电气报警/配电/配电盘/电力拓扑**、外部电价 ID、PowerRange 调整 |
| 相机/媒体 | — | **Camera + PushAV + Zone 引入** | **AV 分析、媒体文件管理、Audio Control、音频设备类型** |
| 感知 | — | — | **环境感知合并、空气质量、湿度调节、接近测距、烟雾浓度** |
| HVAC | — | — | **温控器模式/传感器/事件/关键保护** |
| 闭合 | 基础阀门等 | — | **Access Closures（门锁/门禁语义）** |
| 家电 | 水管理 | — | **温控柜拓扑**（烤箱/冰箱） |
| 数据模型 | Mode Base 机制 | 打磨 | **Q-quality 批量修订 + Device location + Groups 软弃用 + Scenes 修复** |
| 测试 | — | — | TE2 覆盖 150+ 用例（见 §1.6） |

**一总结**：
- **1.5 = 能源与水的"量"的扩张**；
- **1.6 = 摄像头/流媒体全新品类的引入**；
- **1.7 = 四条主线：①后量子安全（PQC）②家庭网络基础设施（HRAP）
  ③能源配电闭环 ④感知/AI/多媒体的纵深**，同时用 Q-quality 和
  Device location 对存量数据模型做质量收敛。

---

# 第三部分：对照明类产品的影响

我们的产品是可切型灯（ECL superset：On/Off/Dim/CT/ECL），
1.7 的直接影响集中在以下几点：

1. **Color Control rev 10**：新增可场景化属性 → ECL 的 ColorControl
   需要升级 spec revision，对应新测试 **TC-CC-10.1**；
2. **On/Off rev 7（Q-quality）**：对应 **TC-OO-2.8**——无大功能变化，
   但一致性/测试表述更新，认证须用新 PICS 与新用例；
3. **Scenes Management rev 2**：Scenes 修复，影响 **TC-S-2.2**
   （灯是场景的主要执行者之一）；
4. **Groups 软弃用（rev 5）**：TC-G-2.2~2.4。注意"软弃用"= 仍需支持
   （控制器生态依赖），但规范开始标注迁移方向；
5. **不直接涉及**：PQC（短期可选，长期是趋势）、HRAP、能源配电、HVAC、
   相机/媒体、环境感知、接近测距——这些是其他品类的 1.7 主线；
6. **工程侧注意**：
   - SDK 升级到含 1.7 数据模型的版本后，Color Control / On/Off /
     Scenes / Groups / Basic Information 等 cluster revision 会随 SDK
     上升，ZAP 需同步；
   - Device location（Basic Information rev 7）随 SDK 升级自带；
   - 认证报 PICS 用 1.7 版；**串口切型方案（EP1 灯类型在线切换）工作在
     数据模型之下，与 spec 版本升级正交，不受影响**——但切型时的
     FeatureMap/ColorCapabilities 重写值需与 1.7 PICS 声明保持一致。

---
