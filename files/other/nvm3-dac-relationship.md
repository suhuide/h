# NVM3 与 DAC 证书存储关系详解

## 目录
- [1. 概述](#1-概述)
- [2. NVM3 简介](#2-nvm3-简介)
  - [2.1 什么是 NVM3？](#21-什么是-nvm3)
  - [2.2 NVM3 特性](#22-nvm3-特性)
  - [2.3 NVM3 内存布局](#23-nvm3-内存布局)
- [3. DAC 证书存储架构](#3-dac-证书存储架构)
  - [3.1 两级间接寻址机制](#31-两级间接寻址机制)
  - [3.2 NVM3 Key 定义](#32-nvm3-key-定义)
  - [3.3 证书数据存储区](#33-证书数据存储区)
- [4. NVM3 Key 详解](#4-nvm3-key-详解)
  - [4.1 Key 范围定义](#41-key-范围定义)
  - [4.2 工厂凭证 Key 列表](#42-工厂凭证-key-列表)
  - [4.3 Key 值实际示例](#43-key-值实际示例)
- [5. 地址计算与证书定位](#5-地址计算与证书定位)
  - [5.1 地址计算公式](#51-地址计算公式)
  - [5.2 实际案例分析](#52-实际案例分析)
  - [5.3 Flash 数据布局](#53-flash-数据布局)
- [6. DAC 私钥管理](#6-dac-密钥管理)
  - [6.1 PSA Crypto 密钥存储](#61-psa-crypto-密钥存储)
  - [6.2 密钥槽位分配](#62-密钥槽位分配)
  - [6.3 密钥安全特性](#63-密钥安全特性)
- [7. NVM3 配置与初始化](#7-nvm3-配置与初始化)
  - [7.1 初始空状态](#71-初始空状态)
  - [7.2 配置流程](#72-配置流程)
  - [7.3 版本管理](#73-版本管理)
- [8. 实际操作指南](#8-实际操作指南)
  - [8.1 读取 NVM3 数据](#81-读取-nvm3-数据)
  - [8.2 解析 NVM3 内容](#82-解析-nvm3-内容)
  - [8.3 更新证书](#83-更新证书)
- [9. 常见问题与排错](#9-常见问题与排错)
  - [9.1 证书读取失败](#91-证书读取失败)
  - [9.2 地址计算错误](#92-地址计算错误)
  - [9.3 密钥丢失](#93-密钥丢失)
- [10. 最佳实践](#10-最佳实践)
- [11. 总结](#11-总结)

---

## 1. 概述

在 Silicon Labs EFR32 系列 MCU 上运行 Matter 协议时，**DAC (Device Attestation Certificate)** 证书和相关凭证需要安全地存储在非易失性存储器中。**NVM3 (Non-Volatile Memory 3)** 是 Silicon Labs 提供的第三代非易失性存储管理系统，负责管理 DAC 证书、PAI 证书、CD (Certification Declaration) 以及相关密钥的存储。

**本文档核心目标**：
- 理解 NVM3 如何存储 DAC 证书
- 掌握两级间接寻址机制
- 学会读取和管理 NVM3 中的凭证数据
- 了解密钥安全管理策略

---

## 2. NVM3 简介

### 2.1 什么是 NVM3？

NVM3 (Non-Volatile Memory 3) 是 Silicon Labs 开发的**第三代非易失性存储系统**，专为 EFR32 系列无线 MCU 设计。它提供了一个可靠的、磨损均衡的闪存管理方案，用于存储需要跨重启保持的配置数据、证书和密钥。

**关键特性**：
- 磨损均衡 (Wear Leveling)
- 掉电安全 (Power-Fail Safe)
- 动态对象管理
- 自动垃圾回收

### 2.2 NVM3 特性

| 特性 | 说明 |
|------|------|
| **磨损均衡** | 自动分配物理地址，延长闪存寿命 |
| **掉电安全** | 即使在写入过程中断电，数据也不会损坏 |
| **动态对象** | 支持可变大小的数据存储 |
| **最大对象大小** | 4096 字节 (4 KB) |
| **键值存储** | 使用 32-bit Key 标识数据对象 |
| **自动垃圾回收** | 自动回收删除对象的空间 |

### 2.3 NVM3 内存布局

在典型的 Matter 设备配置中，NVM3 占据特定的 Flash 区域：

```
┌─────────────────────────────────────────────────────────┐
│              Flash Memory Map (EFR32)                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  0x08174000 ────────────────────────────┐               │
│         │                                │               │
│         ▼                                │               │
│  ┌──────────────────────────────────┐   │               │
│  │   NVM3 Data Area                 │   │               │
│  │   (24 KB total)                  │   │               │
│  │                                  │   │               │
│  │  • Network config                │   │               │
│  │  • Thread dataset                │   │               │
│  │  • Fabric data                   │   │               │
│  │  • Serial numbers                │   │               │
│  │  • Credential metadata (keys)    │   │               │
│  │  • PSA Crypto keys               │   │               │
│  └──────────────────────────────────┘   │               │
│                                         │               │
│  0x0817E000 ────────────────────────────┤               │
│         │                                │               │
│         ▼                                │               │
│  ┌──────────────────────────────────┐   │               │
│  │   Last Page (Certificate Data)   │◄──┘               │
│  │   0x0817E000 - 0x0817FFFF        │                   │
│  │   (8 KB)                         │                   │
│  │                                  │                   │
│  │  • DAC Certificate (DER)         │                   │
│  │  • PAI Certificate (DER)         │                   │
│  │  • CD (Certification Declaration)│                   │
│  └──────────────────────────────────┘                   │
│                                                         │
│  0x0817FFFF                                             │
└─────────────────────────────────────────────────────────┘
```

**关键地址**：
- **NVM3 数据区**: `0x08174000` - `0x0817E000` (24 KB)
- **最后一页 (证书区)**: `0x0817E000` - `0x0817FFFF` (8 KB)

---

## 3. DAC 证书存储架构

### 3.1 两级间接寻址机制

Matter SDK 使用**两级间接寻址**来管理 NVM3 中的证书存储：

```
┌──────────────────────────────────────────────────────────┐
│                  Level 1: NVM3 Keys                       │
│              (存储在 NVM3 数据区)                          │
│                                                          │
│  Key 0x87221: Base Address  ──────────────────┐          │
│  Key 0x87222: DAC Offset    ──┐               │          │
│  Key 0x87223: DAC Size      ──┤               │          │
│  Key 0x87224: PAI Offset     ─┤               │          │
│  Key 0x87225: PAI Size       ─┤               │          │
│  Key 0x87226: CD Offset      ─┘               │          │
│  Key 0x87227: CD Size                         │          │
└───────────────────────────────────────────────┼──────────┘
                                                │
                                                ▼
┌──────────────────────────────────────────────────────────┐
│              Level 2: Certificate Data                    │
│            (存储在最后一页 Flash)                          │
│                                                          │
│  Actual Address = Base Address + Offset                  │
│                                                          │
│  DAC Address = 0x0817E000 + 0x00001000 = 0x0817F000     │
│  PAI Address = 0x0817E000 + 0x00001200 = 0x0817F200     │
│  CD  Address = 0x0817E000 + 0x00001400 = 0x0817F400     │
│                                                          │
│  ┌────────────────────────────────────────────┐          │
│  │ 0x0817F000: DAC Certificate (DER encoded) │          │
│  │ 0x0817F200: PAI Certificate (DER encoded) │          │
│  │ 0x0817F400: CD Data (CMS signed)          │          │
│  └────────────────────────────────────────────┘          │
└──────────────────────────────────────────────────────────┘
```

**为什么使用两级间接寻址？**

1. **灵活性**: 证书大小可以变化，无需固定位置
2. **可维护性**: 只需更新 NVM3 Keys，无需移动证书数据
3. **磨损均衡**: NVM3 自动管理物理存储位置
4. **扩展性**: 可以轻松添加新证书类型

### 3.2 NVM3 Key 定义

所有 Key 定义位于 Matter SDK 头文件中：

**文件路径**: `third_party/matter_sdk/src/platform/silabs/SilabsConfig.h`

```c
// NVM3 Key 范围限制 (未经 Silabs SiSDK 团队批准不得修改)
inline constexpr uint32_t kMatterNvm3KeyLoLimit = 0x087200U;
inline constexpr uint32_t kMatterNvm3KeyHiLimit = 0x087FFFU;

// 工厂凭证 Key 基址
static constexpr Key kMatterFactory_KeyBase = 0x087200U;
```

### 3.3 证书数据存储区

证书数据以 **DER 编码的 X.509 格式**存储在 Flash 最后一页：

**DER 编码特征**：
- 以 `30 82` 开头 (ASN.1 SEQUENCE 标记)
- 包含 Subject、Issuer、公钥等信息
- 可被标准 X.509 解析器读取

**实际示例** (来自 `last_page.s37`):

```
地址 0x0817F000:
  30 82 01 XX ...  ← DER SEQUENCE 标记
  Subject: "HOPERF Matter DAC"
  VID: 0x1470, PID: 0x8006
  Signed by: "HOPERF Matter PAI 01"

地址 0x0817F200:
  30 82 01 XX ...  ← DER SEQUENCE 标记
  Subject: "HOPERF Matter PAI 01"
  VID: 0x1470
  Signed by: "HOPERF Matter PAA 01"

地址 0x0817F400:
  30 82 00 XX ...  ← DER SEQUENCE 标记
  CMS Signed Data (Certification Declaration)
  VID: 0x1470, PID: 0x8006
```

---

## 4. NVM3 Key 详解

### 4.1 Key 范围定义

NVM3 Key 使用 32-bit 值，分为不同的功能区域：

| Key 范围 | 用途 |
|---------|------|
| `0x087200` - `0x087FFF` | Matter 工厂凭证 (不可随意修改) |
| `0x00000` - `0x0EFFF` | 通用 NVM3 数据 |
| `0x0F000` - `0x0FFFF` | 配置和状态数据 |
| `0x87500` - `0x87FFF` | Fabric/Operational 数据 |

### 4.2 工厂凭证 Key 列表

以下是 Matter SDK 定义的完整工厂凭证 Key 列表：

```c
// ═══════════════════════════════════════════════════════════
// 工厂凭证 Key 定义 (SilabsConfig.h)
// ═══════════════════════════════════════════════════════════

// 持久化唯一 ID
static constexpr Key kConfigKey_PersistentUniqueId = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x1F);
// → Key: 0x8721F
// → 用途: 设备唯一标识符，用于生成密钥

// 密钥 ID
static constexpr Key kConfigKey_Creds_KeyId = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x20);
// → Key: 0x87220
// → 用途: 标识密钥版本

// 基地址
static constexpr Key kConfigKey_Creds_Base_Addr = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x21);
// → Key: 0x87221
// → 用途: 证书数据存储区的基地址

// DAC 偏移
static constexpr Key kConfigKey_Creds_DAC_Offset = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x22);
// → Key: 0x87222
// → 用途: DAC 证书相对于基地址的偏移

// DAC 大小
static constexpr Key kConfigKey_Creds_DAC_Size = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x23);
// → Key: 0x87223
// → 用途: DAC 证书的字节大小

// PAI 偏移
static constexpr Key kConfigKey_Creds_PAI_Offset = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x24);
// → Key: 0x87224
// → 用途: PAI 证书相对于基地址的偏移

// PAI 大小
static constexpr Key kConfigKey_Creds_PAI_Size = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x25);
// → Key: 0x87225
// → 用途: PAI 证书的字节大小

// CD 偏移
static constexpr Key kConfigKey_Creds_CD_Offset = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x26);
// → Key: 0x87226
// → 用途: CD 数据相对于基地址的偏移

// CD 大小
static constexpr Key kConfigKey_Creds_CD_Size = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x27);
// → Key: 0x87227
// → 用途: CD 数据的字节大小

// 配置请求状态
static constexpr Key kConfigKey_Provision_Request = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x28);
// → Key: 0x87228
// → 用途: 跟踪配置请求状态

// 配置版本
static constexpr Key kConfigKey_Provision_Version = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x29);
// → Key: 0x87229
// → 用途: 配置数据版本号

// OTA TLV 加密密钥 ID
static constexpr Key kOtaTlvEncryption_KeyId = 
    SilabsConfigKey(kMatterFactory_KeyBase, 0x30);
// → Key: 0x87230
// → 用途: OTA 更新加密密钥
```

### 4.3 Key 值实际示例

从实际设备 (`nvm3-new.md`) 中提取的 Key 值：

| Key | 类型 | 大小 | 值 | 说明 |
|-----|------|------|-----|------|
| `0x0ef00` | Data | 32 B | - | 持久化唯一 ID |
| `0x0f00f` | Data | 10 B | - | 配置状态 |
| `0x87200` | Data | 16 B | "0C1777D6..." | 序列号 |
| `0x87204` | Data | 10 B | "2026-03-" | 日期字符串 |
| `0x87205` | Data | 11 B | - | 唯一设备 ID |
| `0x87209` | Data | 24 B | - | 厂商标识字符串 |
| `0x8720a` | Data | 132 B | Base64 | Base64 编码的 DAC 证书 |
| `0x8720d` | Data | 4 B | "A-OK" | 状态标记 |
| `0x8720e` | Data | 18 B | "Curtain Controller" | 产品名称 |
| `0x8720f` | Data | 4 B | "V1.0" | 固件版本 |
| `0x87211` | Data | 21 B | "https://..." | 厂商 URL |
| `0x8721f` | Data | 32 B | - | 哈希/标识符 |
| **`0x87220`** | Data | 4 B | `02 00 00 00` | 版本 = 2 |
| **`0x87221`** | Data | 4 B | `00 E0 17 08` | 基地址 = `0x0817E000` |
| **`0x87222`** | Data | 4 B | `00 10 00 00` | DAC 偏移 = `0x00001000` |
| **`0x87223`** | Data | 4 B | `E0 01 00 00` | DAC 大小 = `0x1E0` (480 字节) |
| **`0x87224`** | Data | 4 B | `00 12 00 00` | PAI 偏移 = `0x00001200` |
| **`0x87225`** | Data | 4 B | `D6 01 00 00` | PAI 大小 = `0x1D6` (470 字节) |
| **`0x87226`** | Data | 4 B | `00 14 00 00` | CD 偏移 = `0x00001400` |
| **`0x87227`** | Data | 4 B | `F5 00 00 00` | CD 大小 = `0xF5` (245 字节) |
| `0x87500` | Data | 800 B | - | Fabric/Operational 数据 |

---

## 5. 地址计算与证书定位

### 5.1 地址计算公式

证书在 Flash 中的实际地址通过以下公式计算：

```
实际地址 = 基地址 + 偏移量

其中：
  基地址 = NVM3 Key 0x87221 的值
  偏移量 = 对应证书的 Offset Key 值
```

**完整计算示例**：

```
从 NVM3 读取:
  Key 0x87221 (Base Addr): 0x0817E000
  Key 0x87222 (DAC Offset): 0x00001000
  Key 0x87223 (DAC Size):   0x000001E0
  Key 0x87224 (PAI Offset): 0x00001200
  Key 0x87225 (PAI Size):   0x000001D6
  Key 0x87226 (CD Offset):  0x00001400
  Key 0x87227 (CD Size):    0x000000F5

计算:
  DAC 地址 = 0x0817E000 + 0x00001000 = 0x0817F000
  PAI 地址 = 0x0817E000 + 0x00001200 = 0x0817F200
  CD  地址 = 0x0817E000 + 0x00001400 = 0x0817F400

验证:
  DAC 范围: 0x0817F000 - 0x0817F1DF (480 字节)
  PAI 范围: 0x0817F200 - 0x0817F3D5 (470 字节)
  CD  范围: 0x0817F400 - 0x0817F4F4 (245 字节)
```

### 5.2 实际案例分析

**案例 1: 成功读取证书**

从 `nvm3-new.md`:
```
Key 0x87221: 00 E0 17 08 → Base = 0x0817E000
Key 0x87222: 00 10 00 00 → DAC Offset = 0x1000
Key 0x87223: E0 01 00 00 → DAC Size = 0x1E0 (480)

计算: 0x0817E000 + 0x1000 = 0x0817F000

验证 Flash 0x0817F000:
  30 82 01 XX ... ✓ 有效的 DER 编码证书
  Subject: "HOPERF Matter DAC"
```

**案例 2: 偏移量为零 (未配置)**

从 `nvm3-old.md` (空状态):
```
Key 0x87221: 00 E0 17 08 → Base = 0x0817E000
Key 0x87222: 00 00 00 00 → DAC Offset = 0x0000
Key 0x87223: 00 00 00 00 → DAC Size = 0x000

计算: 0x0817E000 + 0x0000 = 0x0817E000

验证 Flash 0x0817E000:
  空数据或无效证书 ✗
  → 结论: 证书未配置
```

### 5.3 Flash 数据布局

最后一页 (`0x0817E000` - `0x0817FFFF`) 的完整布局：

```
┌─────────────────────────────────────────────────────────┐
│           Last Page (0x0817E000 - 0x0817FFFF)           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  0x0817E000 ──────────────────────────┐                │
│         │                              │                │
│         ▼                              │                │
│  ┌────────────────────────────────┐   │                │
│  │  未使用 / 填充区域              │   │                │
│  │  (0x000 - 0xFFF = 4KB)        │   │                │
│  └────────────────────────────────┘   │                │
│                                       │                │
│  0x0817F000 ──────────────────────────┤                │
│         │                              │                │
│         ▼                              │                │
│  ┌────────────────────────────────┐   │                │
│  │  DAC Certificate               │◄───┘               │
│  │  Size: 0x1E0 (480 bytes)      │  Offset: 0x1000    │
│  │  Subject: "HOPERF Matter DAC" │                    │
│  │  Format: DER-encoded X.509    │                    │
│  └────────────────────────────────┘                    │
│                                                         │
│  0x0817F200 ──────────────────────────┐                │
│         │                              │                │
│         ▼                              │                │
│  ┌────────────────────────────────┐   │                │
│  │  PAI Certificate               │◄───┘               │
│  │  Size: 0x1D6 (470 bytes)      │  Offset: 0x1200    │
│  │  Subject: "HOPERF Matter PAI 01"                   │
│  │  Format: DER-encoded X.509    │                    │
│  └────────────────────────────────┘                    │
│                                                         │
│  0x0817F400 ──────────────────────────┐                │
│         │                              │                │
│         ▼                              │                │
│  ┌────────────────────────────────┐   │                │
│  │  CD (Certification Declaration)│◄───┘               │
│  │  Size: 0xF5 (245 bytes)       │  Offset: 0x1400    │
│  │  Format: CMS Signed Data      │                    │
│  │  VID: 0x1470, PID: 0x8006     │                    │
│  └────────────────────────────────┘                    │
│                                                         │
│  0x0817F4F5 - 0x0817FFFF: 未使用区域                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 6. DAC 密钥管理

### 6.1 PSA Crypto 密钥存储

DAC 私钥使用 **PSA Crypto** (Platform Security Architecture Crypto) 格式存储在 NVM3 中：

**PSA Key 标识符**：
```
Flash 地址 0x08175050: "PSA_KEY" 标记
Flash 地址 0x08175D40: "PSA_KEY" 标记
```

**PSA Key 结构**：
```
┌──────────────────────────────────────────┐
│           PSA Key Entry                  │
├──────────────────────────────────────────┤
│  Header: "PSA_KEY" (7 bytes)            │
│  Key ID:   (2 bytes)                    │
│  Key Type: (2 bytes) - ECC P-256        │
│  Key Size: (2 bytes) - 256 bits         │
│  Key Data: (32 bytes) - 私钥材料         │
│  Metadata: (variable)                   │
└──────────────────────────────────────────┘
```

### 6.2 密钥槽位分配

从实际设备观察到的密钥槽位：

| 槽位 ID | 用途 | 密钥类型 | 大小 | 说明 |
|---------|------|---------|------|------|
| **0x01** | **DAC 私钥** | ECC P-256 | 32 B | 用于 Attestation 签名 |
| **0x02** | **Operational/NOCA 密钥** | ECC P-256 | 32 B | 用于 NOC 操作通信 |
| **0x07** | **Fabric 相关密钥** | ECC P-256 | 32 B | 用于 Fabric 管理 |

**DAC 私钥特征**：
- **密钥 ID**: `0x01`
- **密钥类型**: ECC P-256 (ECDSA)
- **密钥大小**: 256 位 (32 字节)
- **用途**: 配网时 Attestation 签名
- **安全性**: 绝不应导出或暴露

### 6.3 密钥安全特性

| 安全特性 | 实现方式 |
|---------|---------|
| **不可导出** | PSA Crypto 硬件保护，私钥不可读 |
| **安全元件** | 密钥存储在安全区域，防止物理攻击 |
| **唯一性** | 每个设备使用不同的 DAC 私钥 |
| **访问控制** | 仅 Matter 协议栈可访问 |
| **防重放** | Attestation 签名包含 Nonce 挑战 |

---

## 7. NVM3 配置与初始化

### 7.1 初始空状态

从 `aaa_empty.s37` 观察到的初始/空 NVM3 状态：

```
┌─────────────────────────────────────────────────────────┐
│              初始空状态 (aaa_empty.s37)                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  已配置的字段:                                           │
│  • 序列号占位符                                          │
│  • 厂商名称: "Curtain Controller"                       │
│  • 厂商 URL: "https://www.aoksx.com"                    │
│  • 固件版本: "V1.0"                                    │
│                                                         │
│  未配置的字段:                                           │
│  ✗ DAC 偏移/大小: 0x0000                                │
│  ✗ PAI 偏移/大小: 0x0000                                │
│  ✗ CD  偏移/大小: 0x0000                                │
│  ✗ DAC 私钥: 未生成                                     │
│                                                         │
│  状态: 等待工厂配置                                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 7.2 配置流程

完整的 NVM3 配置流程：

```
┌──────────────────────────────────────────────────────────┐
│               NVM3 工厂配置流程                           │
└──────────────────────────────────────────────────────────┘

1. 烧录固件
   └─> Flash 包含空 NVM3 状态

2. 生成证书和密钥
   ├─> 生成 DAC 私钥 (PSA Key ID 0x01)
   ├─> 生成 DAC 证书 (使用 PAI 签名)
   ├─> 获取 PAI 证书 (由 PAA 签名)
   └─> 获取 CD (Certification Declaration)

3. 写入证书数据
   ├─> 将 DAC 证书写入 Flash (例如 0x0817F000)
   ├─> 将 PAI 证书写入 Flash (例如 0x0817F200)
   └─> 将 CD 数据写入 Flash (例如 0x0817F400)

4. 更新 NVM3 Keys
   ├─> Key 0x87221: 写入基地址 (0x0817E000)
   ├─> Key 0x87222: 写入 DAC 偏移 (0x1000)
   ├─> Key 0x87223: 写入 DAC 大小 (0x1E0)
   ├─> Key 0x87224: 写入 PAI 偏移 (0x1200)
   ├─> Key 0x87225: 写入 PAI 大小 (0x1D6)
   ├─> Key 0x87226: 写入 CD 偏移 (0x1400)
   └─> Key 0x87227: 写入 CD 大小 (0xF5)

5. 验证配置
   ├─> 读取 NVM3 Keys
   ├─> 计算证书地址
   ├─> 验证 DER 编码格式
   └─> 测试 Attestation 签名

6. 配置完成
   └─> 设备准备好配网
```

### 7.3 版本管理

NVM3 使用版本号跟踪配置状态：

```
Key 0x87220: 版本号

02 00 00 00 → Version 2 (当前版本)
01 00 00 00 → Version 1 (旧版本)
00 00 00 00 → Version 0 (未配置)
```

**版本变更示例** (从 `nvm3-old.md` 到 `nvm3-new.md`):
```
旧版本:
  kConfigKey_Creds_DAC_Offset = 0x00000000
  kConfigKey_Creds_PAI_Offset = 0x00000200
  擦除计数: 1

新版本:
  kConfigKey_Creds_DAC_Offset = 0x00001000  ← 变更
  kConfigKey_Creds_PAI_Offset = 0x00001200  ← 变更
  擦除计数: 2  ← 增加 (NVM3 磨损均衡回收)
```

---

## 8. 实际操作指南

### 8.1 读取 NVM3 数据

使用 Silicon Labs Commander 工具读取 NVM3 数据：

```bash
# 读取 NVM3 数据区域
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000

# 读取最后一页 (证书数据)
commander nvm3 read -o last_page.s37 --device efr32mg24 --range 0x817e000:0x8180000

# 解析 NVM3 内容
commander nvm3 parse nvm3.s37
```

### 8.2 解析 NVM3 内容

解析输出示例：

```
NVM3 Parse Result:
═══════════════════════════════════════════════════════════

Key: 0x087221
Type: Data
Size: 4 bytes
Value: 00 E0 17 08
Interpretation: Base Address = 0x0817E000
───────────────────────────────────────────────────────────

Key: 0x087222
Type: Data
Size: 4 bytes
Value: 00 10 00 00
Interpretation: DAC Offset = 0x00001000
───────────────────────────────────────────────────────────

Key: 0x087223
Type: Data
Size: 4 bytes
Value: E0 01 00 00
Interpretation: DAC Size = 0x000001E0 (480 bytes)
───────────────────────────────────────────────────────────

Key: 0x087224
Type: Data
Size: 4 bytes
Value: 00 12 00 00
Interpretation: PAI Offset = 0x00001200
───────────────────────────────────────────────────────────

Key: 0x087225
Type: Data
Size: 4 bytes
Value: D6 01 00 00
Interpretation: PAI Size = 0x000001D6 (470 bytes)
───────────────────────────────────────────────────────────

Key: 0x087226
Type: Data
Size: 4 bytes
Value: 00 14 00 00
Interpretation: CD Offset = 0x00001400
───────────────────────────────────────────────────────────

Key: 0x087227
Type: Data
Size: 4 bytes
Value: F5 00 00 00
Interpretation: CD Size = 0x000000F5 (245 bytes)

═══════════════════════════════════════════════════════════
```

### 8.3 更新证书

更新 NVM3 中证书的步骤：

```bash
# 步骤 1: 备份当前 NVM3
commander nvm3 read -o backup.s37 --device efr32mg24 --range 0x8174000:0x8180000

# 步骤 2: 计算新地址
新 DAC 地址 = 基地址 + 新偏移
例如: 0x0817E000 + 0x00001000 = 0x0817F000

# 步骤 3: 写入新证书到 Flash
# (使用编程器或自定义脚本)

# 步骤 4: 更新 NVM3 Keys
commander nvm3 write --device efr32mg24 --key 0x87222 --value 00100000
commander nvm3 write --device efr32mg24 --key 0x87223 --value E0010000

# 步骤 5: 验证
commander nvm3 parse --device efr32mg24
```

---

## 9. 常见问题与排错

### 9.1 证书读取失败

**症状**: 配网失败，日志显示无法读取 DAC 证书

**可能原因**:
1. NVM3 Keys 未配置 (偏移量/大小为 0)
2. Flash 地址计算错误
3. 证书数据损坏

**排错步骤**:
```
1. 检查 NVM3 Keys:
   commander nvm3 parse nvm3.s37

2. 验证 Key 0x87221-0x87227 是否有有效值

3. 计算证书地址并验证 Flash 内容:
   地址 = 基地址 + 偏移量

4. 检查 DER 编码 (应以 30 82 开头)
```

### 9.2 地址计算错误

**症状**: 读取到错误或无效的证书数据

**常见错误**:
```c
// 错误: 字节序处理不当
Base Address: 00 E0 17 08
错误解析: 0x00E01708 ✗
正确解析: 0x0817E000 ✓ (小端字节序)

// 错误: 偏移量单位错误
DAC Offset: 00 10 00 00
错误解析: 0x00100000 (1 MB) ✗
正确解析: 0x00001000 (4 KB) ✓
```

**正确解析代码**:
```c
// 读取 4-byte 小端值
uint32_t base_addr = read_nvm3_key(0x87221);  // 返回 0x0817E000
uint32_t dac_offset = read_nvm3_key(0x87222);  // 返回 0x00001000

// 计算实际地址
uint32_t dac_address = base_addr + dac_offset;  // 0x0817F000
```

### 9.3 密钥丢失

**症状**: Attestation 签名失败

**可能原因**:
1. PSA Key ID 0x01 被擦除
2. NVM3 垃圾回收误删除
3. Flash 损坏

**恢复步骤**:
```
1. 检查 PSA Key 是否存在:
   commander nvm3 parse last_page.s37

2. 搜索 "PSA_KEY" 标记和 Key ID 0x01

3. 如果丢失，需要重新生成:
   - 生成新的 DAC 私钥
   - 使用 PAI 重新签名 DAC 证书
   - 更新 NVM3 Keys
```

---

## 10. 最佳实践

### 工厂配置

| 实践 | 说明 |
|------|------|
| **预烧录证书** | 在工厂生产时预烧录 DAC/PAI/CD 证书 |
| **安全存储私钥** | DAC 私钥使用 PSA Crypto 硬件保护 |
| **验证配置** | 出厂前验证完整的证书链和 Attestation 流程 |
| **备份 NVM3** | 保存 NVM3 镜像用于恢复 |

### 开发调试

| 实践 | 说明 |
|------|------|
| **使用 Commander 工具** | 定期解析和验证 NVM3 内容 |
| **保持日志** | 记录 NVM3 变更历史 |
| **版本控制** | 使用 Provision Version 跟踪配置 |
| **测试空状态** | 验证设备从未配置到配置的转换 |

### 生产部署

| 实践 | 说明 |
|------|------|
| **禁用调试接口** | 防止 NVM3 数据被读取 |
| **启用安全启动** | 保护固件和 NVM3 完整性 |
| **监控擦除计数** | 检测异常 NVM3 活动 |
| **定期更新 PAA 信任库** | 确保吊销检查有效 |

---

## 11. 总结

### 核心要点

1. **NVM3 是 Silicon Labs 的非易失性存储系统**
   - 提供磨损均衡和掉电安全
   - 管理 Matter 设备的证书和密钥

2. **两级间接寻址机制**
   ```
   NVM3 Keys (0x87221-0x87227)
      ↓ (存储基地址和偏移)
   Flash 最后一页 (0x0817E000-0x0817FFFF)
      ↓ (实际证书数据)
   DAC/PAI/CD 证书 (DER 编码)
   ```

3. **关键 NVM3 Keys**
   | Key | 用途 |
   |-----|------|
   | 0x87221 | 基地址 |
   | 0x87222/0x87223 | DAC 偏移/大小 |
   | 0x87224/0x87225 | PAI 偏移/大小 |
   | 0x87226/0x87227 | CD 偏移/大小 |

4. **DAC 私钥安全**
   - 使用 PSA Crypto 格式存储
   - Key ID 0x01
   - ECC P-256 密钥对
   - 绝不应导出

5. **地址计算**
   ```
   证书地址 = 基地址 (0x87221) + 偏移量 (0x87222/0x87224/0x87226)
   ```

### 快速参考

**读取 NVM3**:
```bash
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000
commander nvm3 parse nvm3.s37
```

**计算证书地址**:
```
DAC = 0x0817E000 + 0x00001000 = 0x0817F000
PAI = 0x0817E000 + 0x00001200 = 0x0817F200
CD  = 0x0817E000 + 0x00001400 = 0x0817F400
```

**验证 DER 编码**:
```
证书应以 30 82 开头 (ASN.1 SEQUENCE)
```

---

## 附录：参考资源

| 资源 | 路径/链接 |
|------|----------|
| Silabs Application Note | [AN1135](https://www.silabs.com/documents/public/application-notes/an1135-using-third-generation-nonvolatile-memory.pdf) |
| SDK 头文件 | `third_party/matter_sdk/src/platform/silabs/SilabsConfig.h` |
| NVM3 数据文件 | `D:\hrf\h\files\matter\dac\nvm3-new.md` |
| 最后一页证书 | `D:\hrf\h\files\matter\dac\last_page.s37` |
| 空状态模板 | `D:\hrf\h\files\matter\dac\aaa_empty.s37` |
| DAC 文档 | `D:\hrf\h\files\matter\dac\dac.md` |

---

*本文档基于 Silicon Labs Matter SDK 实现及实际 NVM3 数据编写*
