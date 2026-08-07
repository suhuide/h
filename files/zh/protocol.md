# Matter over Thread 数据帧标准 V26.07.24

## 1. 接口配置
* **接口类型:** UART
* **接口电平:** VCC-3.3V (1.8V <= VCC <= 3.3V)
* **波特率:** 9600
* **数据位:** 8
* **校验:** None
* **停止位:** 1
* **日志引脚:** IO3
* **UART引脚:** TX (IO8), RX (IO9)

## 2. 通信说明与校验规则
* **低功耗唤醒：** 低功耗设备在帧头前加 `0xFE` 唤醒字节，校验不包含 `0xFE`。  
  *示例：* `FE 55 AA AA 55 00 03 01 01 02 00 08 00 00 09`
* **异或校验 (XOR-8/BCC)：** D13 = XOR(D0..D12)。发送和接收数据帧的最后一位为前面所有数据位（D0-D12）异或的结果。

## 3. 帧结构

### 3.1 帧结构定义 (14 字节固定帧)

| D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **Frame**|| **Header** || **Version** | **Mode** | **Config / Endpoint** | **Cid H** | **Cid L** | **Aid H** | **Aid L** | **Value H** | **Value L** | **Check** |
| 55 | AA | AA | 55 | 00 | — | — | — | — | — | — | — | — | XOR(D0..D12) |

*Frame Header: 55 AA AA 55, Version: 00*

### 3.2 Mode (数据发送方向)

| Mode | 说明 |
|:---|:---|
| 0 | System 发消息 (MCU <- Matter模组) |
| 1 | System 收消息 (MCU -> Matter模组) |
| 2 | Control 发消息 (MCU <- Matter模组, APP功能) |
| 3 | Control 收消息 (MCU -> Matter模组, APP功能) |

### 3.3 Config / Endpoint (D6)

| Mode | Config | 说明 |
|:---|:---|:---|
| 1 (System, MCU->Matter) | 0 | 重启设备 |
| | 3 | 清除所有数据并重启 (恢复出厂) |
| 2, 3 (Control) | 0, 1, 2 | Matter Endpoint |

### 3.4 Cid / Aid (标准 Matter Cluster / Attribute ID)

* **Cid (D7-D8):** Matter Cluster ID (大端序)
* **Aid (D9-D10):** Matter Attribute ID (大端序)
* **Value (D11-D12):** 属性值 (大端序)

| 功能 | Cid | Aid | Value | 方向 |
|------|-----|-----|-------|------|
| System Ctrl | 0x0011 | 0x0000 | 0 | MCU->Matter |
| Curtain Percent | 0x0102 | 0x0008 | 0-100 | 双向 |
| Curtain Ctrl | 0x0102 | 0x0007 | 0=Open, 1=Stop, 2=Close | 双向 |
| LED OnOff | 0x0006 | 0x0000 | 0=关, 1=开 | 双向 |
| LED Level | 0x0008 | 0x0000 | 0x0000-0x1388 | 双向 |
| LED CurrentX | 0x0300 | 0x0003 | 0x0000-0xFEFF (x × 65536) | 双向 |
| LED CurrentY | 0x0300 | 0x0004 | 0x0000-0xFEFF (y × 65536) | 双向 |
| LED ColorTemperatureMireds | 0x0300 | 0x0007 | 0x0001-0xFEFF | 双向 |
| Battery | 0x002F | 0x0009 | 0-100 | MCU->Matter |


## 4 系统控制
### 4.1 重启
| Mode | Config | Cid | Aid | Value | Check | Packet |
|------|--------|-----|-----|-------|-------|-----|
| 1 (MCU->Matter) | 0x00 (重启) | 0x0011 | 0x0000 | 0x0000 | 10 | `55 AA AA 55 00 01 00 00 11 00 00 00 00 10` |
### 4.2 恢复出厂设置
| Mode | Config | Cid | Aid | Value | Check | Packet |
|------|--------|-----|-----|-------|-------|-----|
| 1 (MCU->Matter) | 0x03 (Reset) | 0x0011 | 0x0000 | 0x0000 | 10 | `55 AA AA 55 00 01 03 00 11 00 00 00 00 13` |

## 5. 窗帘功能 (Cid=0x0102)

*(低功耗设备帧头前加 `FE`，以下示例省略 `FE`)*

### 5.1 窗帘百分比 0% (关闭)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0008 | 0x0000 | 08 | `55 AA AA 55 00 02 01 01 02 00 08 00 00 08` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0008 | 0x0000 | 09 | `55 AA AA 55 00 03 01 01 02 00 08 00 00 09` |

### 5.2 窗帘百分比 100% (打开)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0008 | 0x0064 | 6C | `55 AA AA 55 00 02 01 01 02 00 08 00 64 6C` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0008 | 0x0064 | 6D | `55 AA AA 55 00 03 01 01 02 00 08 00 64 6D` |

### 5.3 窗帘百分比 50% (半开)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0008 | 0x0032 | 3A | `55 AA AA 55 00 02 01 01 02 00 08 00 32 3A` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0008 | 0x0032 | 3B | `55 AA AA 55 00 03 01 01 02 00 08 00 32 3B` |

### 5.4 窗帘停止

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0008 | 0x00FF | F7 | `55 AA AA 55 00 02 01 01 02 00 08 00 FF F7` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0008 | 当前% | — | MCU 收到停止命令后上报当前位置 |

### 5.5 窗帘控制 (Aid=0x0007)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0007 | 0x0000 (Open) | 07 | `55 AA AA 55 00 02 01 01 02 00 07 00 00 07` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0007 | 0x0000 (Open) | 06 | `55 AA AA 55 00 03 01 01 02 00 07 00 00 06` |
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0007 | 0x0001 (Stop) | 06 | `55 AA AA 55 00 02 01 01 02 00 07 00 01 06` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0007 | 0x0001 (Stop) | 07 | `55 AA AA 55 00 03 01 01 02 00 07 00 01 07` |
| 2 (Matter->MCU) | 0x01 | 0x0102 | 0x0007 | 0x0002 (Close) | 05 | `55 AA AA 55 00 02 01 01 02 00 07 00 02 05` |
| 3 (MCU->Matter) | 0x01 | 0x0102 | 0x0007 | 0x0002 (Close) | 04 | `55 AA AA 55 00 03 01 01 02 00 07 00 02 04` |

---

## 6. LED 功能

### 6.1 LED 关闭 (Cid=0x0006 OnOff)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x02 | 0x0006 | 0x0000 | 0x0000 | 06 | `55 AA AA 55 00 02 02 00 06 00 00 00 00 06` |
| 3 (MCU->Matter) | 0x02 | 0x0006 | 0x0000 | 0x0000 | 07 | `55 AA AA 55 00 03 02 00 06 00 00 00 00 07` |

### 6.2 LED 打开 (Cid=0x0006 OnOff)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x02 | 0x0006 | 0x0000 | 0x0001 | 07 | `55 AA AA 55 00 02 02 00 06 00 00 00 01 07` |
| 3 (MCU->Matter) | 0x02 | 0x0006 | 0x0000 | 0x0001 | 06 | `55 AA AA 55 00 03 02 00 06 00 00 00 01 06` |

### 6.3 LED 亮度 (Cid=0x0008 Level, 0x0000-0x1388)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter->MCU) | 0x02 | 0x0008 | 0x0000 | 0x1388 | 93 | `55 AA AA 55 00 02 02 00 08 00 00 13 88 93` |
| 3 (MCU->Matter) | 0x02 | 0x0008 | 0x0000 | 0x1388 | 92 | `55 AA AA 55 00 03 02 00 08 00 00 13 88 92` |
| 2 (Matter->MCU) | 0x02 | 0x0008 | 0x0000 | 0x0000 | 08 | `55 AA AA 55 00 02 02 00 08 00 00 00 00 08` |
| 3 (MCU->Matter) | 0x02 | 0x0008 | 0x0000 | 0x0000 | 09 | `55 AA AA 55 00 03 02 00 08 00 00 00 00 09` |

### 6.4 LED 色坐标 (Cid=0x0300, CurrentX Aid=0x0003, CurrentY Aid=0x0004)

*Value = x或y × 65536, 范围 0x0000-0xFEFF*

**红色 (x≈0.64, y≈0.33):**

| 属性 | Mode | Endpoint | Aid | Value | Check | Packet |
|------|------|----------|-----|-------|-------|-----|
| CurrentX | 2 (Matter->MCU) | 0x02 | 0x0003 | 0xA3D7 | 74 | `55 AA AA 55 00 02 02 03 00 00 03 A3 D7 74` |
| CurrentX | 3 (MCU->Matter) | 0x02 | 0x0003 | 0xA3D7 | 75 | `55 AA AA 55 00 03 02 03 00 00 03 A3 D7 75` |
| CurrentY | 2 (Matter->MCU) | 0x02 | 0x0004 | 0x547B | 28 | `55 AA AA 55 00 02 02 03 00 00 04 54 7B 28` |
| CurrentY | 3 (MCU->Matter) | 0x02 | 0x0004 | 0x547B | 29 | `55 AA AA 55 00 03 02 03 00 00 04 54 7B 29` |

**绿色 (x≈0.21, y≈0.71):**

| 属性 | Mode | Endpoint | Aid | Value | Check | Packet |
|------|------|----------|-----|-------|-------|-----|
| CurrentX | 2 (Matter→MCU) | 0x02 | 0x0003 | 0x35C3 | F6 | `55 AA AA 55 00 02 02 03 00 00 03 35 C3 F6` |
| CurrentY | 2 (Matter→MCU) | 0x02 | 0x0004 | 0xB5C3 | 71 | `55 AA AA 55 00 02 02 03 00 00 04 B5 C3 71` |
| CurrentX | 3 (MCU→Matter) | 0x02 | 0x0003 | 0x35C3 | F7 | `55 AA AA 55 00 03 02 03 00 00 03 35 C3 F7` |
| CurrentY | 3 (MCU→Matter) | 0x02 | 0x0004 | 0xB5C3 | 70 | `55 AA AA 55 00 03 02 03 00 00 04 B5 C3 70` |

**蓝色 (x≈0.15, y≈0.06):**

| 属性 | Mode | Endpoint | Aid | Value | Check | Packet |
|------|------|----------|-----|-------|-------|-----|
| CurrentX | 2 (Matter→MCU) | 0x02 | 0x0003 | 0x2666 | 40 | `55 AA AA 55 00 02 02 03 00 00 03 26 66 40` |
| CurrentY | 2 (Matter→MCU) | 0x02 | 0x0004 | 0x0F5C | 54 | `55 AA AA 55 00 02 02 03 00 00 04 0F 5C 54` |
| CurrentX | 3 (MCU→Matter) | 0x02 | 0x0003 | 0x2666 | 41 | `55 AA AA 55 00 03 02 03 00 00 03 26 66 41` |
| CurrentY | 3 (MCU→Matter) | 0x02 | 0x0004 | 0x0F5C | 55 | `55 AA AA 55 00 03 02 03 00 00 04 0F 5C 55` |

**紫色 (x≈0.32, y≈0.15):**

| 属性 | Mode | Endpoint | Aid | Value | Check | Packet |
|------|------|----------|-----|-------|-------|-----|
| CurrentX | 2 (Matter→MCU) | 0x02 | 0x0003 | 0x51EB | BA | `55 AA AA 55 00 02 02 03 00 00 03 51 EB BA` |
| CurrentY | 2 (Matter→MCU) | 0x02 | 0x0004 | 0x2666 | 47 | `55 AA AA 55 00 02 02 03 00 00 04 26 66 47` |
| CurrentX | 3 (MCU→Matter) | 0x02 | 0x0003 | 0x51EB | BB | `55 AA AA 55 00 03 02 03 00 00 03 51 EB BB` |
| CurrentY | 3 (MCU→Matter) | 0x02 | 0x0004 | 0x2666 | 46 | `55 AA AA 55 00 03 02 03 00 00 04 26 66 46` |

> **注意**: X/Y 各一帧，配对后应用。MCU/Matter模块 收到不成对的单帧应缓冲等待配对或超时丢弃。

### 6.5 LED 色温 (Cid=0x0300, Aid=0x0007 ColorTemperatureMireds, 0x0001-0xFEFF)

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 2 (Matter→MCU) | 0x02 | 0x0300 | 0x0007 | 0x0064 (100) | 60 | `55 AA AA 55 00 02 02 03 00 00 07 00 64 60` |
| 3 (MCU→Matter) | 0x02 | 0x0300 | 0x0007 | 0x0064 (100) | 61 | `55 AA AA 55 00 03 02 03 00 00 07 00 64 61` |
| 2 (Matter→MCU) | 0x02 | 0x0300 | 0x0007 | 0x0190 (400) | 95 | `55 AA AA 55 00 02 02 03 00 00 07 01 90 95` |
| 3 (MCU→Matter) | 0x02 | 0x0300 | 0x0007 | 0x0190 (400) | 94 | `55 AA AA 55 00 03 02 03 00 00 07 01 90 94` |
| 2 (Matter→MCU) | 0x02 | 0x0300 | 0x0007 | 0x028A (650) | 8C | `55 AA AA 55 00 02 02 03 00 00 07 02 8A 8C` |
| 3 (MCU→Matter) | 0x02 | 0x0300 | 0x0007 | 0x028A (650) | 8D | `55 AA AA 55 00 03 02 03 00 00 07 02 8A 8D` |

---

## 7. 低功耗电池设置 (Cid=0x002F, Aid=0x0009)

*(电池电量只有 MCU->Matter 方向)*

### 7.1 电池 100%

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 3 (MCU->Matter) | 0x01 | 0x002F | 0x0009 | 0x0064 | 40 | `55 AA AA 55 00 03 01 00 2F 00 09 00 64 40` |

### 7.2 电池 50%

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 3 (MCU->Matter) | 0x01 | 0x002F | 0x0009 | 0x0032 | 16 | `55 AA AA 55 00 03 01 00 2F 00 09 00 32 16` |

### 7.3 电池 0%

| Mode | Endpoint | Cid | Aid | Value | Check | Packet |
|------|----------|-----|-----|-------|-------|-----|
| 3 (MCU->Matter) | 0x01 | 0x002F | 0x0009 | 0x0000 | 24 | `55 AA AA 55 00 03 01 00 2F 00 09 00 00 24` |
