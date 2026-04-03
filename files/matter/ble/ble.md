
# Matter 1.5

#### 5.4.2.5. Using BLE
This section provides details of how a device announces its commissionable status or how a device
requests fixes to the operational network configuration using BLE technology (see Bluetooth® Core
Specification 4.2 (amended) and Bluetooth® Core Specification Supplement 12). As required in Sec­
tion  5.4.2.2,  “Announcement  Commencement”,  Nodes  currently  commissioned  into  one  or  more
fabrics or already connected to an IP-bearing network SHALL NOT employ this method for commis­
sioning.
##### 5.4.2.5.1. Device Role
Commissionable devices SHALL implement the role of a Generic Access Profile (GAP) Peripheral.
##### 5.4.2.5.2. Channels
There are three advertising channels used by BLE. All three channels SHOULD be used by commis­
sionable devices for BLE advertising.
##### 5.4.2.5.3. Interval
Commissionable devices SHOULD use an Advertising Interval between 20 ms and 60 ms for the first
30  seconds  and  a  value  between  150  ms  to  1285  ms  for  the  rest  of  the  Announcement  duration.
Shorter intervals typically result in shorter discovery times.
If a device opts to use Extended Announcement, it SHALL switch to using an Advertising Interval
larger or equal to 1200 ms and SHOULD use a nominal Advertising Interval of 1285 ms. When using
Extended  Announcement,  the  device  SHALL  set  the  Extended  Announcement  Flag  in  the  Matter
Service  Data  in  the  BLE  Advertisement  (see  Table  70,  “Matter  BLE  Service  Data  payload  for­
mat — Commissionable OpCode”).
##### 5.4.2.5.4. Advertising Mode
Commissionable  devices  SHALL  use  the  GAP  General  Discoverable  mode,  sending  connectable
undirected advertising events.
##### 5.4.2.5.5. Advertising Address
To ensure privacy, commissionable devices SHALL use LE Random Device Address (see Bluetooth®
Core Specification 4.2 (amended) Vol 6, Part B, Section 1.3.2.1 "Static device address") for BLE Adver­
tising and SHALL change it at least on every boot.
##### 5.4.2.5.6. Advertising Data
In order to reduce 2.4 GHz spectrum congestion due to active BLE scanning, and to extend battery
life in battery-powered devices, all critical data used for device discovery is contained in the Adver­
tising Data rather than the Scan Response Data. This allows a BLE Commissioner to passively scan
(i.e., not issue Scan Requests upon receiving scannable advertisements) and still be able to receive
all information needed to commission a device.
Note  that  if  additional  vendor-specific  information  is  to  be  conveyed  and  does  not  fit  within  the
Advertising Data, it may be included in the Scan Response Data. See Section 5.4.2.8, “Manufacturer-
specific data” for details on including vendor-specific information.
Advertising data for Matter discovery uses "Service Data - 16 bit UUID" advertisement data type (see
Bluetooth® Core Specification Supplement 12 Section 1.11 "Service Data"), with 16-bit UUID value of
0xFFF6 (see Table 36, “SIG UUID assignment”).
All multi-byte values are encoded in little-endian byte order within the service data payload.

## Silabs 
```c
sl_btctrl_init_phy()
sl_bt_connection_set_default_preferred_phy()
sl_bt_connection_set_preferred_phy()

sl_bt_evt_connection_phy_status_id
```
## Supported BLE PHY for Matter Commissioning 
Matter commissioning over BLE typically utilizes the following PHY (Physical Layer) settings to ensure compatibility and reliability:   
LE 1M PHY (1 Mbps): This is the standard, most common, and required PHY for general Matter device discovery and commissionin.  
LE Coded PHY (125 kbps): Supported by many Silicon Labs/Nordic chipsets used for Matter to provide increased range, ensuring reliable commissioning even if the device is far from the phone.   

## Matter BLE
根据蓝牙核心规范（Bluetooth Core Specification），**信道 37、38、39 这三个主要广播信道（Primary Advertising Channels）不能使用 2M PHY**，但**可以使用 Coded PHY**（即 LE Long Range）。

---

### 广播信道分类与 PHY 支持情况

| 广播信道类型 | 信道编号 | 可用的 PHY | 说明 |
| :--- | :--- | :--- | :--- |
| **主要广播信道** | 37、38、39 | LE 1M PHY（强制）<br>LE Coded PHY（可选） | 固定三个信道，用于设备发现和连接建立 |
| **辅助广播信道** | 0-36（数据信道） | LE 1M PHY<br>LE 2M PHY<br>LE Coded PHY | 蓝牙 5.0 引入扩展广播后可用，需先通过主广播信道指示 |

---

### 规范依据（蓝牙 Core Spec）

#### 1. 主要广播信道只能用 1M 或 Coded PHY

根据 **蓝牙核心规范 Vol 6, Part B, Section 2.3** 中的 **Table 2.3**：

> ADV_EXT_IND 类型的 PDU 仅支持 LE 1M PHY 和 LE Coded PHY，不支持 LE 2M PHY。

ADV_EXT_IND 是在主要广播信道上发送的扩展广播指示包。这意味着：如果你想在主要广播信道上发送任何广播包，物理层只能是 **1M PHY** 或 **Coded PHY**，**2M PHY 不被允许**。

#### 2. 2M PHY 只能在辅助广播信道使用

2M PHY 是蓝牙 5.0 引入的高速物理层，但它**不能用于主要广播信道**。如果设备想使用 2M PHY 进行广播，必须：

1. 在主要广播信道（37/38/39）上使用 **1M PHY** 或 **Coded PHY** 发送 ADV_EXT_IND 包
2. 该包内包含指向辅助广播信道的指针（包含信道编号和时间偏移）
3. 然后在辅助广播信道上使用 **2M PHY** 发送实际的广播数据（AUX_ADV_IND）

#### 3. Coded PHY 在主要广播信道的使用条件

Coded PHY（125kbps / 500kbps）可以用于主要广播信道，但有一个关键限制：**广播类型不能是 "legacy" 属性**，且不能同时支持可连接和可扫描。 这意味着使用 Coded PHY 广播时，必须使用蓝牙 5.0 引入的扩展广播格式。

---

### 蓝牙 Core Spec 章节索引

如果你手上有蓝牙核心规范文档，可以查阅以下章节获取原文：

| 规范章节 | 内容说明 |
| :--- | :--- |
| **core 6.0 P2590,Vol 4, Part E, Section 7.8.53** | LE Set Extended Advertising Parameters 命令，定义主/辅广播信道的 PHY 选择  |
| **core 6.0 P2934,Vol 6, Part B, Section 2.1** | 定义 Uncoded PHY（1M/2M）的包结构  |
| **core 6.0 P2938,Vol 6, Part B, Section 2.2** | 定义 Coded PHY 的包结构  |
| **core 6.0 P2941,Vol 6, Part B, Section 2.3** | 定义广播物理信道 PDU，包含 Table 2.3（各 PDU 类型对 PHY 的支持） |
---

### 总结

回到你的问题：**BLE 广播使用的三个广播信道（37、38、39）可以用 2M PHY / Coded PHY 吗？**

- **2M PHY：不可以** — 规范明确禁止在主要广播信道上使用 2M PHY
- **Coded PHY：可以** — 但需要配合扩展广播（Extended Advertising）使用，且不能是 legacy 广播

这就是为什么 Matter 规范选择 BLE 配网时，物理层实际锁定在 **1M PHY**——因为 Coded PHY 虽可用于主要广播信道，但需要额外的扩展广播支持，而 Matter 为了兼容性优先，选择了所有 BLE 设备都强制支持的 1M PHY。