# MSP 串口通信协议规范
## 1. 物理层与低功耗唤醒

### 1.1 串口物理参数

| 项目 | 参数 |
| --- | --- |
| 波特率 | 9600 bps |
| 数据格式 | 8N1(8 位数据位，无校验，1 位停止位) |
| 流控 | 无 |
| 字节序 | 大端(Big-Endian，高字节在前) |
| **断帧超时** | **字节间空闲超时(gap)**。帧内字节连续，若 **20 ms** 内未收到下一个字节，判定断帧，清空缓冲并寻找帧头。 |
| **帧间隔** | 收到对方 ACK 应答后，可立即发下一帧。无 ACK 的主动上报，间隔建议 ≥ 20 ms。 |

### 1.2 低功耗唤醒机制

- **Matter 唤醒 MCU**：Matter 发数据前，拉低 Wakeup 引脚保持 **5 ms** 唤醒 MCU，再发数据。
- **MCU 唤醒 Matter**：MCU 发数据前，先发送 3 个 `0x00` 作为前导码，再发送正式数据帧。

---

## 2. 协议帧结构
<div style="display: flex; gap: 10px;">
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: sans-serif; font-size: 14px;">
  <thead>
    <tr style="background-color: #d9d9d9;">
      <th style="border: 1px solid #000; padding: 5px;background-color: #d9d9d9;font-weight: bold;">帧头</th>
      <th style="border: 1px solid #000; padding: 5px;background-color: #d9d9d9;font-weight: bold;">SN(序列号)</th>
      <th style="border: 1px solid #000; padding: 5px;background-color: #d9d9d9;font-weight: bold;">Type</th>
      <th colspan="2" style="border: 1px solid #000; padding: 5px;background-color: #d9d9d9;font-weight: bold;">PDU(n+1)</th>
      <th style="border: 1px solid #000; padding: 5px;background-color: #d9d9d9;font-weight: bold;">CRC16</th>
    </tr>
  </thead>
  <tbody>
    <!-- Line1 -->
    <tr>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px;">2 bytes<br>(55 AA)</td>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px;">1 byte</td>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px;">1 byte</td>
      <td style="border: 1px solid #000; padding: 5px; background-color: #d9d9d9; font-weight: bold;">Len</td>
      <td style="border: 1px solid #000; padding: 5px; background-color: #d9d9d9; font-weight: bold;">Payload(0-248)</td>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px;">2 bytes</td>
    </tr>
    <!-- Line2 -->
    <tr>
      <td style="border: 1px solid #000; padding: 5px;">1 byte</td>
      <td style="border: 1px solid #000; padding: 5px;">n bytes</td>
    </tr>
  </tbody>
</table>
</div>

**字段说明：**

- **SN**：序列号(0~255 循环)，发送方递增，应答方回显。
- **Type**：消息类型，见第 3 节。
- **Len**：**Payload** 的字节数(不包含帧头及帧尾)。
- **Payload**：业务数据区，最大 248 字节。
- **CRC16**：覆盖范围从 `SN` 到 `Payload` 末尾。

**校验算法：**

- 固定使用 **CRC-16/CCITT-FALSE**(Poly 0x1021，Init 0xFFFF，无反转)。
- 计算范围：不包含帧头 `55 AA`，不包含 `CRC16` 自身。
- 标准测试：字符串 `"123456789"` 算出的 CRC 应为 `0x29B1`。

**帧接收状态机：**

- 全包总长度 = **`Len + 7`** 字节。
- 找 `55 AA` → 收 3 字节(SN+Type+Len)→ 收 `Len` 字节 → 收 2 字节 CRC16。

---

## 3. 消息类型与 Payload 结构

根据 `Type` 的不同，Payload 结构如下：

| Type | 帧类型 | 方向 | 说明 |
| --- | --- | --- | --- |
| `0x01` | **CMD** | 模块 ➔ MCU | 业务控制/查询 |
| `0x02` | **ACK** | MCU ➔ 模块 | 对 CMD 的应答 |
| `0x03` | **EVENT** | MCU ➔ 模块 | 业务状态主动上报 |
| `0x04` | **ACK_EVT** | 模块 ➔ MCU | 对 EVENT 的确认 |
| `0x05` | **SYS_CMD** | 双向 | 系统级配置/OTA 请求 |
| `0x06` | **SYS_ACK** | 双向 | 系统级配置/OTA 应答 |

### 3.1 业务帧 Payload(Type 01/02/03/04)

用于设备的具体功能控制(如开关、调光、上报温度等)；具体 `DevType`/`Opcode`/`Data` 见第 4 节，其他品类由子规范定义。

| 帧类型 | Payload 结构 | 长度 (Len) | 说明 |
| --- | --- | --- | --- |
| CMD / EVENT | `Channel(1) + DevType(1) + Opcode(1) + Data(N)` | **3 + N** | 发起控制或上报 |
| ACK 纯确认 | 无 | **0** | 执行成功，无数据返回 |
| ACK 合一应答 | `Channel(1) + DevType(1) + Opcode(1) + Status(1) + Data(N)` | **4 + N** | 执行成功，附带当前值 |
| ACK 错误应答 | `Channel(1) + DevType(1) + Opcode(1) + Status(1)` | **4** | 执行失败，附带错误码 |
| ACK_EVT | 无 | **0** | 模块对 MCU 上报的确认 |

- `Status` 错误码：`0x00` 成功，`0x01` 不支持，`0x02` 越界，`0x03` 忙，`0x04` 故障，`0x05` 未入网/未就绪。
- 记录型设备(门锁等)整条记录上报仍使用 EVENT，可在 Data 中携带 `0x20` 同步的 UTC 时间戳；离线缓存与补报策略由品类子规范定义，通用层不设 DP 缓存命令。

### 3.2 系统帧 Payload(Type 05/06)

用于链路管理、系统配置与固件升级。

| 帧类型 | Payload 结构 | 长度 (Len) | 说明 |
| --- | --- | --- | --- |
| SYS_CMD 请求 | `Cmd(1) + Data(N)` | **1 + N** | 发起系统指令 |
| SYS_ACK 应答 | `Cmd(1) + Status(1) + Data(N)` | **2 + N** | 系统指令应答(Status=0 成功) |

- `SYS_ACK` 的 `Status` 与业务帧共用同一错误码表；`Status≠0` 时 `Data` 为空。

---

## 4. 业务帧(DevType)

业务帧的通用 Payload 结构见 3.1；本节按 `DevType` 定义各品类的 `Opcode` 与 `Data`。

- **Channel**：实例号。`0x00` 表示整机级，`0x01` 起为具体设备实例。
- **DevType**：品类。`0x00`=电池、`0x01`=灯、`0x02`=开关、`0x03`=插座、`0x04`=窗帘、`0x05`=传感器；其他品类由子规范定义。
- **Opcode**：按 DevType 定义，不同品类可复用相同编号。
- **Opcode 分区**：`0x00~0x09` 命令/上报，`0x0A~0x0F` 属性/控制，`0x10~0x1F` 设置。
- 控制/查询用 CMD，状态上报用 EVENT；成功回 ACK 合一应答(带当前值)，上报回 ACK_EVT。

### 4.1 电池(DevType=0x00)

`Channel=0x00` 表示整机级电池信息。

| Opcode | 功能 | CMD / EVENT Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | 电池电量 | 查询：无；EVENT：`1B` 0~100 | `1B` 当前值 | 模块映射 Matter `BatPercentRemaining`(×2) |
| `0x01` | 充电状态 | 查询：无；EVENT：`1B` 0=Unknown，1=Charging，2=Full，3=NotCharging | `1B` 当前值 | 对应 Matter `BatChargeState` |
| `0x02` | 低电量状态 | 查询：无；EVENT：`1B` 0=OK，1=Warning，2=Critical | `1B` 当前值 | 对应 Matter `BatChargeLevel` |

- 电池是整机级虚拟设备，`Channel` 固定 `0x00`；是否列入通道能力清单由实现决定。
- 电池上报由 MCU 发 EVENT，模块回 ACK_EVT；查询由模块发 CMD，MCU 回当前值。
- 电池电量按 0~100% 上报；模块 ×2 后写入 Matter `BatPercentRemaining`(0~200，单位 0.5%)。MCU 必须保证 0~100，避免 ×2 后 uint8 溢出。
- 电压/温度等电池诊断可按需扩展 Opcode。

**电池示例(仅 Payload)：**

- 模块查询电量：`00 00 00`(Ch=0，DevType=0，Opcode=0)；MCU 回 ACK 合一 `00 00 00 00 32`(Status=0，当前值=50)
- MCU 上报电量 50%：`00 00 00 32`；模块回 ACK_EVT

### 4.2 灯(DevType=0x01)

`Channel` 为灯的实例号(从 1 开始)，`DevType=0x01` 表示灯。

**命令类(无 Data)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | On | 无 | `1B` 当前 OnOff | 对应 Matter `On` 命令 |
| `0x01` | Off | 无 | `1B` 当前 OnOff | 对应 Matter `Off` 命令 |
| `0x02` | Toggle | 无 | `1B` 翻转后的值 | 对应 Matter `Toggle`；MCU 翻转后回报 |

**属性类(设置/查询)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x0A` | OnOff 设置 / 查询 | 设置：`1B`(0 关 / 1 开)；查询：无 | `1B` 当前值 | 无 Data 的 CMD 视为查询 |
| `0x0B` | 亮度设置 / 查询 | 设置：`2B`(0~5000)；查询：无 | `2B` 当前值 | 0 最暗、5000 最亮 |
| `0x0C` | 色温设置 / 查询 | 设置：`2B` mireds；查询：无 | `2B` 当前值 | 范围 `0x0001~0xFEFF` |
| `0x0D` | 颜色 XY 设置 / 查询 | 设置：`4B`(X 2B + Y 2B)；查询：无 | `4B` 当前值 | `x/y × 65536`，两坐标同帧 |

**设置类：**

| Opcode | 功能 | 设置 Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x10` | 颜色模式 | `1B`：0=CT，1=XY | `1B` 当前模式 | 模块映射 Matter ColorMode；非法值回 `Status=0x02`，不支持的模式回 `Status=0x01` |
| `0x11` | 渐变时间 | `2B`：0.1s 单位，0=立即 | `2B` 当前值 | 作用于 OnOff/亮度/色温/XY |
| `0x12` | 开灯亮度 OnLevel | `2B`：0~5000，0xFFFF=当前亮度 | `2B` 当前值 | 无亮度参数的 On 使用该值 |
| `0x13` | 开机状态 StartUpOnOff | `1B`：0=关，1=开，2=翻转，0xFF=断电前 | `1B` 当前值 | 掉电恢复后的 OnOff 状态 |
| `0x14` | 开机亮度 StartUpCurrentLevel | `2B`：0~5000，0xFFFF=断电前 | `2B` 当前值 | 掉电恢复后的亮度 |
| `0x15` | 最小/最大亮度 | `4B`：Min(2)+Max(2)，各 0~5000 | `4B` 当前值 | Min ≤ Max；越界回 `Status=0x02` |
| `0x16` | 识别/闪烁 | `2B`：秒数，0=停止 | `2B` 剩余秒数 | Identify 用，安装/找灯 |

- `0x00~0x02` 为无参数命令；`0x0A~0x0D` 为属性式设置/查询。
- 状态上报用属性 Opcode(`0x0A~0x0D`)；命令 Opcode(`0x00~0x02`)不用于 EVENT。
- 设置/查询同样走 CMD/ACK 合一应答；查询时 CMD 不带 Data，MCU 回当前配置值。
- `OnLevel` 是“开灯时使用的亮度”，`StartUpCurrentLevel` 是“掉电恢复后的亮度”，两者不要混用。
- 渐变时间 `0` 表示立即到位；Matter 的 0.1s 单位由模块换算。
- 颜色模式只定义 CT/XY；HS 由模块内部换算，不下发给 MCU。
- 多字节数值大端；亮度 `0x0000~0x1388`(0~5000)为协议缩放，Matter `currentLevel`(0~254)由模块换算。
- 颜色 XY 由模块完成 XY↔HS/CT 换算，MCU 只需按 XY 实现。
- 控制/查询成功回 ACK 合一应答(带当前值)；失败回 ACK 错误应答。
- 状态变化时 MCU 用 EVENT(同属性 Opcode + Data)主动上报，模块回 ACK_EVT。
- OnOff 的 Toggle 由 MCU 翻转，ACK 返回翻转后的值；如需主动同步，再发 EVENT(Opcode `0x0A`)。

**灯控制示例(仅 Payload)：**

- 模块发 On 命令：`01 01 00`(Ch=1，DevType=1，Opcode=0，无 Data)
- MCU ACK：`01 01 00 00 01`(Status=0，当前 OnOff=1)
- MCU 主动上报 OnOff：`01 01 0A 01`；模块回 ACK_EVT(无 Payload)

### 4.3 开关(DevType=0x02)

`Channel` 为开关实例号(从 1 开始)，`DevType=0x02` 表示墙面开关/继电器开关(默认 OnOff)。

**命令类(无 Data)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | On | 无 | `1B` 当前 OnOff | 对应 Matter `On` 命令 |
| `0x01` | Off | 无 | `1B` 当前 OnOff | 对应 Matter `Off` 命令 |
| `0x02` | Toggle | 无 | `1B` 翻转后的值 | 对应 Matter `Toggle`；MCU 翻转后回报 |

**属性类(设置/查询)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x0A` | OnOff 设置 / 查询 | 设置：`1B`(0 关 / 1 开)；查询：无 | `1B` 当前值 | 无 Data 的 CMD 视为查询 |

**设置类：**

| Opcode | 功能 | 设置 Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x10` | 按键模式 | `1B`：0=自锁/翻转，1=点动，2=场景 | `1B` 当前值 | 默认 0；点动/场景由 MCU 本地处理 |
| `0x11` | 上电状态 | `1B`：0=关，1=开，2=翻转，0xFF=断电前 | `1B` 当前值 | 对应 Matter `StartUpOnOff` |

- 开关默认按 OnOff 处理；点动/场景按键模式只影响 MCU 本地按键逻辑，状态仍用 OnOff 上报。
- 场景按键如需上报单击/双击/长按，可在子规范扩展按键 EVENT Opcode。
- 多路开关的每一路是独立 On/Off 实例：`Channel=1/2/3` 分别对应第 1/2/3 路，每路独立控制和上报；单路只用 `Channel=1`。模块按 `Channel` 映射到 Matter 的不同 endpoint。
- 纯开关只做通断，不测功率/电量；带计量硬件的插座才扩展功率/电量 Opcode。

**开关示例(仅 Payload)：**

- 模块发 On 命令：`01 02 00`(Ch=1，DevType=2，Opcode=0，无 Data)
- MCU ACK：`01 02 00 00 01`(Status=0，当前 OnOff=1)
- MCU 主动上报 OnOff：`01 02 0A 01`；模块回 ACK_EVT(无 Payload)
- 设置上电状态=断电前：`01 02 11 FF`；MCU ACK `01 02 11 00 FF`

### 4.4 插座(DevType=0x03)

`Channel` 为插座实例号(从 1 开始)，`DevType=0x03` 表示插座(纯 OnOff 设备)。

**命令类(无 Data)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | On | 无 | `1B` 当前 OnOff | 对应 Matter `On` 命令 |
| `0x01` | Off | 无 | `1B` 当前 OnOff | 对应 Matter `Off` 命令 |
| `0x02` | Toggle | 无 | `1B` 翻转后的值 | 对应 Matter `Toggle`；MCU 翻转后回报 |

**属性类(设置/查询)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x0A` | OnOff 设置 / 查询 | 设置：`1B`(0 关 / 1 开)；查询：无 | `1B` 当前值 | 无 Data 的 CMD 视为查询 |

- `0x00~0x02` 为无参数命令；`0x0A` 为属性式设置/查询。
- 状态上报用 Opcode `0x0A`；命令 Opcode(`0x00~0x02`)不用于 EVENT。
- 带计量硬件的插座由子规范扩展功率/电量 Opcode；纯开关不适用；不实现回 `Status=0x01`。

**插座示例(仅 Payload)：**

- 模块发 On 命令：`01 03 00`(Ch=1，DevType=3，Opcode=0，无 Data)
- MCU ACK：`01 03 00 00 01`(Status=0，当前 OnOff=1)
- MCU 主动上报 OnOff：`01 03 0A 01`；模块回 ACK_EVT(无 Payload)

### 4.5 窗帘(DevType=0x04)

`Channel` 为窗帘实例号(从 1 开始)，`DevType=0x04` 表示窗帘。位置/倾斜统一用 `1B` `0~100`(0=全关，100=全开)；模块负责与 Matter `Percent100ths`(0=全开，10000=全关)换算。电池信息见 4.1(`DevType=0x00`)。

**命令类(无 Data)：**

| Opcode | 功能 | CMD Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | UpOrOpen | 无 | `1B` 当前运行状态 | 对应 Matter `UpOrOpen` |
| `0x01` | DownOrClose | 无 | `1B` 当前运行状态 | 对应 Matter `DownOrClose` |
| `0x02` | StopMotion | 无 | `1B` 当前运行状态 | 对应 Matter `StopMotion` |

**控制/上报类：**

| Opcode | 功能 | CMD / EVENT Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x0A` | 目标位置 | `1B`：0~100 | `1B` 当前位置 | 对应 Matter `GoToLiftPercentage`；0=全关，100=全开 |
| `0x0B` | 当前位置上报 | `1B`：0~100 | — | EVENT；模块回 ACK_EVT |
| `0x0C` | 运行状态上报 | `1B`：0=停止，1=正在开，2=正在关 | — | EVENT；对应 Matter OperationalStatus |
| `0x0D` | 目标倾斜 | `1B`：0~100(可选) | `1B` 当前倾斜 | 仅百叶帘/可调帘 |
| `0x0E` | 倾斜位置上报 | `1B`：0~100(可选) | — | EVENT |
| `0x0F` | 安全状态上报 | `1B` bitfield：bit0 障碍、bit1 过温、bit2 电机故障、bit3 限位异常 | — | EVENT；模块映射 Matter SafetyStatus |

**设置类：**

| Opcode | 功能 | 设置 Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x10` | 方向反转 | `1B`：0=正转，1=反转 | `1B` 当前值 | 对应 Matter `Mode.MotorDirectionReversed` |
| `0x11` | 校准/行程 | `1B`：0=进入校准，1=设全开限位，2=设全关限位，3=保存退出，4=取消 | `1B` 当前步骤 | 产测/安装用；模块同步 Matter 限位 |
| `0x12` | 运行速度 | `1B`：0~100(可选) | `1B` 当前值 | 厂商扩展 |
| `0x13` | 软启停 | `1B`：0=关，1=开(可选) | `1B` 当前值 | 厂商扩展 |
| `0x14` | 常用位置 | `1B`：0~100(可选) | `1B` 当前值 | 厂商扩展，一键到常用位置 |

- `0x00~0x02` 为无参数命令，对应 Matter 的三个窗帘命令；`0x0A` 为目标位置(带百分比参数)。
- 位置 `0=全关、100=全开` 为 MCU 语义；模块换算 Matter `CurrentPositionLiftPercent100ths`/`TargetPositionLiftPercent100ths`(Matter `0=全开、10000=全关`)。
- 位置/倾斜精度为 1%；如需 0.01% 精度，可将字段扩展为 `2B` `0~10000`(当前代码为 `1B` `0~100`)。
- 运行状态上报 `0x0C` 的 `0/1/2` 是“停/正在开/正在关”，对应 Matter `OperationalStatus`；命令本身无参数。
- 上报类 Opcode(`0x0B/0x0C/0x0E/0x0F`)由 MCU 发 EVENT，模块回 ACK_EVT(无 Payload)。
- 倾斜仅对支持 tilt 的产品开放；不支持的 Opcode 回 `Status=0x01`。
- 方向反转后 MCU 的开/关输出对调；模块同步 Matter `Mode.MotorDirectionReversed`。
- 校准流程由 MCU 执行电机行程学习，模块只负责同步 Matter 的限位/模式。
- 速度、软启停、常用位置为厂商扩展，按电机能力选配；不实现时回 `Status=0x01`。

**窗帘控制示例(仅 Payload)：**

- 模块发 UpOrOpen 命令：`01 04 00`(Ch=1，DevType=4，Opcode=0，无 Data)
- MCU ACK：`01 04 00 00 01`(Status=0，当前运行状态=正在开)
- 模块设置目标位置 50%：`01 04 0A 32`(Opcode=0x0A，Data=50)
- MCU ACK：`01 04 0A 00 32`(Status=0，当前值=50)
- MCU 当前位置上报 50%：`01 04 0B 32`；模块回 ACK_EVT

### 4.6 传感器(DevType=0x05)

`Channel` 为传感器实例号(从 1 开始)；一个多合一传感器使用同一 `Channel`，通过不同 `Opcode` 上报不同测量值。所有测量值支持查询(CMD)和主动上报(EVENT)，EVENT 由模块回 ACK_EVT。

**上报/命令类：**

| Opcode | 功能 | CMD / EVENT Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x00` | 温度 | 查询：无；EVENT：`2B` int16 ×0.01°C | `2B` 当前值 | Matter 0x0402；25.36°C=0x09E8 |
| `0x01` | 湿度 | 查询：无；EVENT：`2B` uint16 ×0.01%RH | `2B` 当前值 | Matter 0x0403；80.00%=0x1F40 |
| `0x02` | 光照 | 查询：无；EVENT：`2B` uint16 lux | `2B` 当前值 | Matter 0x0400 |
| `0x03` | 占空/人体存在 | 查询：无；EVENT：`1B` bit0(0 无人/1 占用) | `1B` 当前值 | Matter 0x0406 |
| `0x04` | 门窗磁 | 查询：无；EVENT：`1B`(0 关闭/1 打开) | `1B` 当前值 | Matter 0x0045 |
| `0x05` | 烟感状态 | 查询：无；EVENT：`1B` 0=正常，1=预警，2=报警 | `1B` 当前值 | Matter Smoke CO Alarm `SmokeState` |
| `0x06` | 烟感设备状态 | 查询：无；EVENT：`1B` bitfield：bit0 硬件故障、bit1 传感器污染、bit2 寿命到期、bit3 自检中 | `1B` 当前值 | 对应 Matter `HardwareFaultAlert`/`ContaminationState`/`EndOfServiceAlert`/`TestInProgress` |
| `0x07` | CO 状态 | 查询：无；EVENT：`1B` 0=正常，1=预警，2=报警 | `1B` 当前值 | 可选；Matter `COState`；烟感/CO 一体机用 |
| `0x08` | 烟感自检 | 无 | `1B`：0=通过，1=失败，2=进行中 | Matter `SelfTestRequest`；MCU 执行后回结果 |

**设置类：**

| Opcode | 功能 | 设置 Data | ACK 合一 Data | 说明 |
| --- | --- | --- | --- | --- |
| `0x10` | 温度校准 | `2B` int16 ×0.01°C | `2B` 当前值 | 可选；偏移量 |
| `0x11` | 湿度校准 | `2B` int16 ×0.01%RH | `2B` 当前值 | 可选；偏移量 |
| `0x12` | 上报间隔 | `2B` 秒，0=关闭周期上报 | `2B` 当前值 | 可选；MCU 主动上报周期 |

- 温度用 int16 二进制补码，湿度用 uint16；多字节大端。
- `0x10/0x11` 为校准偏移量，MCU 在原始测量值上叠加；不实现回 `Status=0x01`。
- `0x12` 为 MCU 主动上报周期，模块只保存/查询，不代替 MCU 定时。
- 传感器电池信息走 4.1(`DevType=0x00`)，不在本 DevType 内重复。
- 烟感/CO 对应 Matter Smoke CO Alarm cluster(0x005C)；报警用 EVENT 立即上报，模块可同时触发 Matter 告警事件。
- 自检 `0x08` 为无 Data 命令，MCU 执行后 ACK 返回结果；设备状态 `0x06` 按位映射 Matter alerts。

**传感器示例(仅 Payload)：**

- MCU 上报温度 25.36°C：`01 05 00 09 E8`(Ch=1，DevType=5，Opcode=0，Data=0x09E8)；模块回 ACK_EVT
- MCU 上报湿度 80.00%：`01 05 01 1F 40`(Data=0x1F40)；模块回 ACK_EVT
- MCU 上报门窗磁打开：`01 05 04 01`；模块回 ACK_EVT
- MCU 上报烟感报警：`01 05 05 02`；模块回 ACK_EVT
- 模块请求自检：`01 05 08`；MCU 回 ACK 合一 `01 05 08 00 00`(Status=0，结果=通过)
- MCU 上报硬件故障：`01 05 06 01`；可选 CO 报警：`01 05 07 02`
- 模块查询温度：`01 05 00`；MCU 回 ACK 合一 `01 05 00 00 09 E8`

---

## 5. 系统帧(SYS_CMD / SYS_ACK)

所有系统级操作均通过 `Type=0x05/0x06` 交互，Payload 首字节为 `Cmd`。  

**命令号分区：**

| Cmd 范围 | 用途 |
| --- | --- |
| `0x00` | 保留 |
| `0x01~0x0F` | 5.1 版本与设备信息 |
| `0x10~0x1F` | 5.2 网络状态、控制与诊断 |
| `0x20~0x2F` | 5.3 时间与链路参数 |
| `0x30~0x3F` | 5.4 产测 |
| `0x40~0xDF` | 保留 |
| `0xE0~0xEF` | 5.5 MCU OTA |
| `0xF0~0xFF` | 保留 |

> 下表“请求 Data / 应答 Data”均**不含** Payload 首字节 `Cmd` 与应答帧的 `Status`；完整结构见 3.2。

### 5.1 版本与设备信息(0x01~0x0F)

| Cmd | 功能 | 方向 | 请求 Data(Type=05) | 应答 Data(Type=06，Status=0) | 备注 |
| --- | --- | --- | --- | --- | --- |
| `0x01` | 查版本 | 模块 ➔ MCU | 无 | 变长 ASCII：版本号 | 模块查询 MCU 版本；上电链路确认、OTA 版本比较用，如 `"v1.0.1"`(格式 `vX.Y.Z`) |
| `0x02` | 查询模组信息 | MCU ➔ 模块 | 无 | ASCII JSON | MCU 查询模组自身信息：`{"fw":"模组固件","hw":"硬件型号","mv":"Matter SDK 版本","bl":"Bootloader 版本"}`；诊断与兼容性核对用，与 0x01 不重复 |
| `0x03` | 通道能力上报 | MCU ➔ 模块 | `Ch(1B)+DevType(1B)` 循环 | 无 | MCU 上电时主动上报自身硬件清单 |
| `0x04` | 查询通道能力 | 模块 ➔ MCU | 无 | `[Ch(1B)+DevType(1B)]...` | 模块单独重启、未收到 `0x03` 时补查；无通道时 Data 为空 |

> `0x01` 只取 MCU 版本(模块查询)；`0x02` 取模组自身的 fw/hw/mv/bl(MCU 查询)。方向不同、用途不同，不合并。
>
> `0x05~0x0F` 预留：模组硬件信息、序列号、生产批次等设备信息类命令。

### 5.2 网络状态、控制与诊断(0x10~0x1F)

| Cmd | 功能 | 方向 | 请求 Data(Type=05) | 应答 Data(Type=06，Status=0) | 备注 |
| --- | --- | --- | --- | --- | --- |
| `0x10` | 网络状态上报 | 模块 ➔ MCU | `状态(1B)` | 无 | 模块状态变化时主动通知，取值见下表 |
| `0x11` | 查询网络状态 | MCU ➔ 模块 | 无 | `状态(1B)` | 枚举同 `0x10`；上电、配网后核对用 |
| `0x12` | 网络控制 | MCU ➔ 模块 | `动作(1B)` | 无 | 动作见下表；OTA 期间回 `Status=0x03` 忙 |
| `0x14` | 查询网络质量 | MCU ➔ 模块 | 无 | `RSSI(1)+LQI(1)` | 已入网时有效；Thread 链路 RSSI(int8，dBm)与 LQI(0~255)；未入网回 `Status=0x05` |
| `0x15` | 查询 Thread 网络信息 | MCU ➔ 模块 | 无 | `信道(1B)+PANID(2B)` | 产测/诊断用；Thread 2.4G 信道 11~26，PANID 高字节在前 |

> `0x13`、`0x16~0x1F` 预留：父节点信息、网络诊断统计、配网窗口查询等网络类命令。

**网络状态值(0x10 / 0x11)：**

| 值 | 状态 |
| --- | --- |
| `0x00` | 未配网(BLE 广播等待配网) |
| `0x01` | 配网中(BLE 已连 + Commissioning) |
| `0x02` | Thread 附加中(凭证已下发，未入网) |
| `0x03` | 在网(Thread 附加 + Matter fabric 已加入) |
| `0x04` | 异常 |

**网络控制动作(0x12)：**

| 值 | 动作 | 说明 |
| --- | --- | --- |
| `0x00` | 软复位 | 先回应答再复位，保留配置 |
| `0x01` | 进入配网 | 打开 BLE 广播配网窗口，默认 **180 s**；重复下发可延长 |
| `0x02` | 停止配网 | 关闭 BLE 广播 |
| `0x03` | 离网 | 仅离开 Thread 网络，保留 Matter Fabric；用于换网/重新入网 |
| `0x04` | 恢复出厂 | Thread Leave + Matter Fabric 移除 + 模块本地配置清除；先回应答再执行 |

### 5.3 时间与链路参数(0x20~0x2F)

| Cmd | 功能 | 方向 | 请求 Data(Type=05) | 应答 Data(Type=06，Status=0) | 备注 |
| --- | --- | --- | --- | --- | --- |
| `0x20` | 时间同步 | MCU ➔ 模块 | 无 | `UTC(4)+星期(1)` | 记录型设备(门锁)本地时间戳用；星期 1~7(1=周一)；对齐 Matter Time 同步 |
| `0x21` | 配置链路参数 | 双向 | `使能(1B)+ACK超时(2B,ms)` | 无 | 默认 `1 / 500 ms`；超时范围 200~2000 ms；重试次数固定 2 次；掉电不保存；接收方按新参数更新本端重发策略，从下一条事务生效 |

> `0x22~0x2F` 预留：时区/夏令时、SN 窗口、链路统计等时间与链路类命令。

### 5.4 产测(0x30~0x3F)

| Cmd | 功能 | 方向 | 请求 Data(Type=05) | 应答 Data(Type=06，Status=0) | 备注 |
| --- | --- | --- | --- | --- | --- |
| `0x30` | RF 产测 | MCU ➔ 模块 | 无 | `RSSI(1)+LQI(1)` | 模组初始化完成后执行；未入网也可测 |

> `0x31~0x3F` 预留：发射功率、误包率、信道扫描、GPIO/按键自检等产测命令。

### 5.5 OTA(0xE0~0xEF)

> 以 `bk01_matter` 现有代码为准，OTA 流程与 `serial.md` 对齐；帧封装仍按本规范第 2 节。

| Cmd | 功能 | 方向 | 请求 Data(Type=05) | 应答 Data(Type=06，Status=0) | 备注 |
| --- | --- | --- | --- | --- | --- |
| `0xE1` | OTA 通知 | 模块 ➔ MCU | `产品ID(2)+版本(5 ASCII)+大小(2)+校验和(1)`，共 10B | 无 | 新版本高于 MCU 当前版本时发送；MCU 回 ACK=接受并擦除升级区；版本如 `0.0.1`，产品ID/大小为高字节在前；产品ID 来自 OTA metadata，与 MCU 版本无关 |
| `0xE2` | OTA 拉数据 | MCU ➔ 模块 | `最大读取长度(1B)`，建议 240 | `固件数据(N B)`，N ≤ 请求长度 | 无 Offset，模块内部维护偏移；首次自动跳过 10B metadata 头 |
| `0xE3` | OTA 结果 | MCU ➔ 模块 | `结果(1B)`：0 成功 / 1 失败 | 无 | MCU 收满并校验后上报；模块回 ACK |

**OTA 约定：**

1. **metadata 头(10B)**：`magic(2, 0x55AA) + size(2) + checksum(1) + version(5)`，由 Matter OTA 镜像携带；MCU 不解析该头，`0xE2` 只传头之后的固件数据。
2. **校验和**：`checksum = 固件数据逐字节累加和 & 0xFF`(不含 10B metadata 头)；MCU 收满 `size` 字节后校验大小与校验和。
3. **版本比较**：模块读取 metadata 版本，与 MCU 当前版本(`0x01` 查询)比较；仅当新版本更高时才发 `0xE1`，否则直接应用 Matter 镜像；MCU 版本未知时跳过 MCU 升级。
4. **超时与收尾**：模块发出 `0xE1` 后等待 MCU 完成，最长 **150 s**；MCU 成功(`0xE3=0`)后模块应用 Matter 镜像并重启；超时或失败则放弃本次升级，Matter OTA 状态复位。
5. **`0xE2` 流控**：MCU 每收到一包数据后，用下一包 `0xE2` 请求(1B 最大长度)继续；模块按内部偏移返回下一段，直到累计 `size` 字节。
6. **`0xE0`**：现有代码曾用作 MCU 产品信息上报入口；本规范不定义该命令，版本统一由 `0x01`(纯 `vX.Y.Z`)获取。

> `0xE4~0xEF` 预留：断点续传、分片校验、升级进度查询等 OTA 命令。

---

## 6. 通信机制与可靠性

1. **超时与重发**：发送请求(Type 01/03/05)后，必须在 **500 ms**(默认，可由 `0x21` 配置)内收到对应应答。超时则以相同 SN 重发，最多重发 2 次(共 3 次)；重发内容与首发完全一致，**SN 不递增**。Type 02/04/06 为应答帧，不单独重发。
2. **去重防误**：接收方维护最近 8 个已处理的 SN 缓存。重复 SN 只回应答，不重复执行动作；CRC 校验失败静默丢弃，由发送方超时重发兜底。
3. **上电/重连交互流程**：
   - MCU 上电后，发送 `SYS_CMD 0x03` 上报硬件通道清单。
   - MCU 紧接着发 `EVENT` 全量上报所有通道的初始状态。
   - 模块就绪后，发送 `SYS_CMD 0x01` 查询 MCU 版本，确认链路畅通。
   - 模块单独重启、未收到 `0x03` 时，用 `SYS_CMD 0x04` 补查通道能力。
   - 网络状态变化时模块主动 `0x10` 上报；MCU 需要核实时用 `0x11` 查询。
4. **双向并发**：一方正在等待应答时收到对方新请求，应先处理并回应对应 ACK(无法立即执行可回 `Status=0x03` 忙)，再继续等待自己的应答；不得静默丢弃对方请求。
5. **恢复出厂**：MCU 发 `0x12`(动作=`0x04`)→ 模块先回 ACK → 模块执行 Thread Leave + Fabric 移除并复位。MCU 侧配置由 MCU 自行清除，模块不做通知。

---

## 7. 报文结构示例
### 7.1 通用示例

**示例 1：查版本(请求与应答)**
```c
模块→MCU: 55 AA 01 05 01 01 3A 94    (SYS_CMD, SN=0x01, Cmd=0x01)
MCU→模块: 55 AA 01 06 08 01 00 76 31 2E 30 2E 31 2C 3D    (SYS_ACK, SN=0x01, Cmd=0x01, Status=0, Data="v1.0.1")
```

**示例 2：网络状态上报(模块通知 MCU)**
```c
模块→MCU: 55 AA 02 05 02 10 01 94 F8    (SYS_CMD, SN=0x02, Cmd=0x10, Data=1 在网)
MCU→模块: 55 AA 02 06 02 10 00 1F 05    (SYS_ACK, SN=0x02, Cmd=0x10, Status=0)
```

**示例 3：MCU 上电上报通道能力**
```c
MCU→模块: 55 AA 03 05 05 03 01 01 02 03 3A BA    (SYS_CMD, SN=0x03, Cmd=0x03, Ch1=灯, Ch2=插座)
```

**示例 4：MCU 拉取 OTA 数据**
```c
MCU→模块: 55 AA 04 05 02 E2 04 7C 7B    (SYS_CMD, SN=0x04, Cmd=0xE2, 最大读取长度=4B)
模块→MCU: 55 AA 04 06 06 E2 00 D4 D3 D2 D1 53 24    (SYS_ACK, SN=0x04, Cmd=0xE2, Status=0, 4B 固件数据)
```
> 示例 4 为缩短展示只取 4B；实际常用 240B(Len=0xF2)。

### 7.2 网络/配置/产测示例
**示例 5：查询网络状态**
```c
模块→MCU: 55 AA 05 05 01 11 E2 54    (SYS_CMD, SN=0x05, Cmd=0x11)
MCU→模块: 55 AA 05 06 03 11 00 03 5F 78    (SYS_ACK, SN=0x05, Cmd=0x11, Status=0, 当前状态=3 在网)
```

**示例 6：网络控制(进入配网)**
```c
模块→MCU: 55 AA 06 05 02 12 01 7B 9C    (SYS_CMD, SN=0x06, Cmd=0x12, 动作=1)
MCU→模块: 55 AA 06 06 02 12 00 F0 61    (SYS_ACK, SN=0x06, Cmd=0x12, Status=0)
```

**示例 7：查询通道能力**
```c
模块→MCU: 55 AA 07 05 01 04 4D A8    (SYS_CMD, SN=0x07, Cmd=0x04)
MCU→模块: 55 AA 07 06 06 04 00 01 01 02 03 99 13    (SYS_ACK, SN=0x07, Cmd=0x04, Status=0, Ch1=灯, Ch2=插座)
```

**示例 8：配置链路参数(500 ms)**
```c
模块→MCU: 55 AA 08 05 04 21 01 01 F4 42 04    (SYS_CMD, SN=0x08, Cmd=0x21, 使能=1, 超时=0x01F4)
MCU→模块: 55 AA 08 06 02 21 00 6F 0F    (SYS_ACK, SN=0x08, Cmd=0x21, Status=0)
```

**示例 9：RF 产测**
```c
模块→MCU: 55 AA 09 05 01 30 99 25    (SYS_CMD, SN=0x09, Cmd=0x30)
MCU→模块: 55 AA 09 06 04 30 00 C4 8C 78 98    (SYS_ACK, SN=0x09, Cmd=0x30, Status=0, RSSI=-60dBm, LQI=140)
```

### 7.3 业务帧示例
**灯 On 命令与 ACK**
```c
模块→MCU: 55 AA 0A 01 03 01 01 00 BD 9E    (CMD, SN=0x0A, Len=3)
MCU→模块: 55 AA 0A 02 05 01 01 00 00 01 4F 64    (ACK, Status=0, 当前 OnOff=1)
```

**灯 OnOff 上报与 ACK_EVT**
```c
MCU→模块: 55 AA 0B 03 04 01 01 0A 01 43 69    (EVENT, Opcode=0x0A, Data=1)
模块→MCU: 55 AA 0B 04 00 F0 A9    (ACK_EVT)
```

**开关 On 命令与 ACK**

```c
模块→MCU: 55 AA 11 01 03 01 02 00 31 EB    (CMD, SN=0x11, Opcode=0)
MCU→模块: 55 AA 11 02 05 01 02 00 00 01 3F A3    (ACK, Status=0, 当前 OnOff=1)
```

**插座 On 命令与 ACK**

```c
模块→MCU: 55 AA 12 01 03 01 03 00 CC 3A    (CMD, SN=0x12, Opcode=0)
MCU→模块: 55 AA 12 02 05 01 03 00 00 01 81 62    (ACK, Status=0, 当前 OnOff=1)
```

**窗帘 UpOrOpen 与 ACK**
```c
模块→MCU: 55 AA 0C 01 03 01 04 00 CF 8A    (CMD, Opcode=0)
MCU→模块: 55 AA 0C 02 05 01 04 00 00 01 73 EA    (ACK, 当前状态=正在开)
```

**窗帘位置上报**
```c
MCU→模块: 55 AA 0D 03 04 01 04 0B 32 3C BD    (EVENT, 当前位置=50%)
```

**温度上报与 ACK_EVT**
```c
MCU→模块: 55 AA 0E 03 05 01 05 00 09 E8 E4 06    (EVENT, 25.36°C)
模块→MCU: 55 AA 0E 04 00 1B 59    (ACK_EVT)
```

**温度查询与 ACK**
```c
模块→MCU: 55 AA 0F 01 03 01 05 00 32 5B    (CMD, 查询温度)
MCU→模块: 55 AA 0F 02 06 01 05 00 00 09 E8 0E EC    (ACK, Status=0, 25.36°C)
```

**烟感报警上报**
```c
MCU→模块: 55 AA 10 03 04 01 05 05 02 C3 A0    (EVENT, 烟感报警)
模块→MCU: 55 AA 10 04 00 43 3B    (ACK_EVT)
```

---

## 8. 开发对接备忘

1. **收包解析**：找 `55 AA`，读取 `Len`，收满 `Len+7` 字节整帧(帧头 2B + SN/Type/Len 3B + Payload Len + CRC16 2B)，校验 CRC 后按 `Type` 分发。
2. **高低字节**：SN、Data 中的多字节数值(如 uint16/uint32/Size)、CRC16，全部遵循**高字节在前**。
3. **命令配对**：`0x10`↔`0x11`(状态上报/查询)、`0x03`↔`0x04`(能力上报/查询)、`0xE1`→`0xE2`→`0xE3`(OTA 通知/拉取/结果)；应答 SN 必须回显。
