# Matter RDI(轮换设备标识)机制分析
---

## 1. 总结

**RDI = 用"每台设备唯一的秘密(PUI) + 一个会变化的 Counter"算出来的 16 字节哈希值,  
设备在 BLE 配网广播期间通过 GATT 特征值 C3 对外提供;  
产线/售后拿扫描器读出它,与量产 CSV 里预登记的 PUI 逐一重算比对,  
即可反查出这台"没有标签的设备"对应的配网二维码(discriminator/passcode)。**  

它解决的问题是:设备贴纸掉了、或设备被退回翻新时,你不知道它当初是用哪套  
配网信息(discriminator + passcode)出厂的——扫一下蓝牙,就能查回来。  

---

## 2. 机制分三层看

### 2.1 广播层:怎么知道"这台设备可以读附加数据"?

Matter BLE 配网广播里,FFF6 服务数据(8 字节)布局固定:

```c
字节0      字节1-2        字节3-4     字节5-6     字节7
opcode    discriminator   VID         PID         flags
=0x00     (12bit,LE)      (LE)        (LE)        bit0=1 表示"C3 里有附加数据"
```

对应扫描器 `advertisement_group()` 的校验:  
`data[0]==0, data[7]==1`(只接受"普通配网广播 + Additional Data 标志")。  
这就是编译宏 `CHIP_ENABLE_ADDITIONAL_DATA_ADVERTISING=1` 的作用——  
由 Silabs BLEManagerImpl 在组装广播时置位。  

这个标志告诉扫描器:连上来读 C3 有意义,不用白连。  

### 2.2 GATT 层:C3 里到底放了什么

Matter 服务 `0xFFF6` 下的 C3 特征值(`64630238-8772-45F2-B87D-748A83218F04`)  
以 USER 类型提供,读出来的 23 字节是Matter TLV 编码的 Additional Data Payload:  
```c
15 30 00 12  [counter 2 bytes] [hash 16 bytes] 18
│  │  │  │   └─────────── 18-byte RDI ─────────┘│
│  │  │  └─ Length = 18 (0x12)                  │
│  │  └─ Context tag 0 (kRotatingDeviceIdTag)   │
│  └─ Header: tag 0 + 18Bytes string (0x30)     |
└─ Structure start (0x15)       Structure end ──┘
```

18 字节 RDI 的内部布局:

```
counter (2字节, 小端)  +  hash (16字节)
```

扫描器 `parse_c3()` 做了严格校验:长度必须 23、头必须是 `15 30 00 12`、尾 `18`——  
这也解释了文档里那个坑:**C3 若保留 HEX 类型,读出来是静态 `00`,  
不是 SDK 生成的 TLV**,必须改成 USER 类型(SDK 生成 `datatype=0x07`、动态数据),  
读取请求才会走到 `BLEManagerImpl::HandleC3ReadRequest()`,  
把启动时 `EncodeAdditionalDataTlv()` 生成好的 TLV 发出来。  

### 2.3 算法层:PUI + Counter → hash

三个输入:

| 名字 | 是什么 | 从哪来 |
|---|---|---|
| **PUI**(PersistentUniqueId) | 32 个 HEX 字符的 **ASCII 文本**(32 个原始字节,不再 hex 解码!) | 产线烧录进工厂数据,键 `0x08721F`(`SilabsConfig.h: kConfigKey_PersistentUniqueId = kMatterFactory_KeyBase\|0x1F`),运行时由 DeviceInstanceInfoProvider 的 `GetRotatingDeviceIdUniqueId()` 读出 |
| **Counter**(Lifetime Counter) | 2 字节轮换计数 | `ConfigurationMgr().GetLifetimeCounter()` → Silabs 实现即 NVM3 里的 **BootCount**(`kConfigKey_BootCount`,开机 +1)。所以:断连/重广播 Counter 不变,**复位后才变**——与实测 log 一致 |
| 算法选择 | MATTER_V0(原版) / MATTER_V1(公司补丁新增,默认) | 补丁宏 `ROTATING_DEVICE_ID_USE_MATTER_V1` |

**MATTER_V0(SDK 原版)** —— SHA256 截尾:

```
hash = SHA256( PUI_bytes ‖ counter_LE(2字节) ) 的最后16字节
RDI  = counter_LE ‖ hash
```

**MATTER_V1(补丁新增,即标准 HKDF-SHA256 / RFC5869,只取第一块)**:

```c
PRK  = HMAC-SHA256( salt = counter_LE(2字节),  IKM = PUI(32字节) )   # HKDF-Extract
hash = HMAC-SHA256( PRK, info="RotatingDeviceID" ‖ 0x01 ) 的前16字节  # HKDF-Expand
RDI  = counter_LE ‖ hash
```

⚠️ 字节序细节(对拍时最容易错的地方):counter 在**盐和 RDI 输出里都是小端**
(SDK `BufferWriter::Put16` 默认小端,扫描器 `counter.to_bytes(2,'little')` 与之一致)。

**为什么这样设计就"轮换"且"查得到"?**

- Counter 变 → hash 全变 → 跟踪者无法用固定 ID 长期追踪同一台设备(隐私);
- HKDF/SHA256 单向 → 广播里只有 RDI,拿不到 PUI 本身(PUI 永远不出芯片);
- 产线手里有全部设备的 PUI(CSV)→ 重算一遍就能唯一反查——**安全性和可查性来自
  "秘密在产线侧,不在空气里"**。

---

## 3. 全链路数据流

```c
┌─ 量产 (mfg_tool v2.6.8) ─────────────────────────────┐
│ 生成 PUI + discriminator/passcode/VID/PID             │
│ 写入芯片工厂数据 (PUI → 键 0x08721F)                   │
│ 导出 rdi_data.csv:                                    │
│   date,device_id,vendor_id,product_id,               │
│   discriminator,unique_id(PUI),qr_code,manualcode    │
└──────────────────────┬───────────────────────────────┘
                       ▼
┌─  设备   ─────────────────────────────────────────────┐
│ 配网广播: FFF6 服务数据, flags bit0=1                  │
│ C3(USER): 15 30 00 12 ‖ counter ‖ HKDF(PUI,cnt) ‖ 18 │
│ counter = BootCount(NVM3, 每次复位 +1)                 │
└──────────────────────┬───────────────────────────────┘
                       ▼
┌─ 扫描器 (tools/rdi_scan_match.py, bleak) ────────────┐
│ 1. 扫广播 → FFF6 服务数据 → 解出 VID/PID/discriminator│
│ 2. 用三元组在 CSV 里缩小候选(只看,不凭它定身份)        │
│ 3. 连接读 C3 → 校验 TLV → 取 counter + RDI            │
│ 4. 对每条候选用其 PUI + 同算法算期望 RDI               │
│ 5. 唯一命中 → 打印该设备二维码 (JSON 行输出)           │
└───────────────────────────────────────────────────────┘
```

扫描器设计里两个值得点名的严谨之处:  
- **身份判定只认 RDI**。discriminator 只是"筛候选",就算多台设备 discriminator  
  相撞,也能靠 RDI 区分;命中数 ≠1 时直接拒绝,不猜。  
- CSV 校验时解码 `MT:` 二维码(Base38 → 版本/VID/PID/流程/发现方式/disc/passcode),  
  确认**二维码本身与该行 VID/PID/discriminator 一致**,防量产记录录错。  

实测样例(log.log):  
`MT:K2CA0YDG158HO34RB10` → Base38 解码 = VID 5232(0x1470), PID 65281(0xFF01),  
discriminator 2485 —— 与 `HM-MT2401-RDI/mfg_config.json` 里  
`vendor_id: 5232, product_id: 65281` 完全吻合,自洽。  

---

## 4. 名词辨析(容易混)

| 名词 | 层面 | 变化规律 | 本方案角色 |
|---|---|---|---|
| **BLE 地址 (含 RPA)** | 链路层 | 可解析私有地址,每 ~15min 轮换 | 与 RDI 无关;扫描按地址去重只是防重复读 |
| **discriminator** | 配网发现 | 每台固定(产线随机生成) | 广播里明文,只用于筛候选 |
| **PUI** | 应用层秘密 | 永不变、永不出芯片 | RDI 的密钥材料,CSV 里登记 |
| **RDI** | 应用层公开 | Counter 变则变 | 空气里的"轮换身份证" |
| **Counter** | NVM3 BootCount | 每次复位 +1 | RDI 的轮换因子 |

另注:Matter 规范里 Additional Data/RDI 的原始用途(见 SDK  
`AdditionalDataPayload.h` 头注释)正是①客服协助配网/确认设备来源,  
②程序化获取 Setup PIN 简化配网——Amazon MSS 等生态用它做回收设备识别;  
本方案是同一机制 + 产线 CSV 反查的具体落地。规范也明确:  
获取 PIN 的具体机制不在规范内,所以"用 CSV 反查"属于厂商自选实现,合规。  

---

## 5. 怎么验证

### 5.1 端到端验证(已有,最省事)

```bash
cd C:\Si\v6\bk01_matter
python -m pip install -r tools/requirements-rdi.txt
python tools/rdi_scan_match.py --scan-seconds 15
```

设备进入配网广播即可。通过标准(已实测):读到 **23 字节 C3**、
`unique match` 且打印的二维码与该设备身份一致(可用 §6.3 独立复算交叉验证)。

### 5.2 手动分步验证(nRF Connect / 任意 BLE 工具)

1. **广播层**:扫描设备 → Service Data 0xFFF6 共 8 字节,
   检查 `byte[0]=0x00`、`byte[7]=0x01`(Additional Data 标志),
   中间 6 字节 = discriminator(小端12bit)+VID+PID(小端)
2. **GATT 层**:连接 → 读 C3 → 应为 23 字节,以 `15 30 00 12` 开头、`18` 结尾
3. 读出 `counter = bytes[4:6] 小端`,`RDI = bytes[6:22]`

### 5.3 独立复算(不依赖扫描器,密码学层验证)

```python
import hmac, hashlib, struct
def rdi_v1(pui_ascii32: str, counter: int) -> bytes:
    pui  = pui_ascii32.encode('ascii')            # 32字节 ASCII, 保留大小写!
    salt = struct.pack('<H', counter)             # 小端!
    prk  = hmac.new(salt, pui, hashlib.sha256).digest()
    okm  = hmac.new(prk, b'RotatingDeviceID\x01', hashlib.sha256).digest()[:16]
    return salt + okm                              # 18字节: counter_LE + hash

def rdi_v0(pui_ascii32: str, counter: int) -> bytes:
    salt = struct.pack('<H', counter)
    return salt + hashlib.sha256(pui_ascii32.encode('ascii') + salt).digest()[-16:]

# 例: 取 CSV 某行 unique_id + 设备 C3 里的 counter, 与 C3 里的 16 字节比对
print(rdi_v1("0123ABCDEF0123456789ABCDEF012345", 3).hex())
```

比对一致 ⇒ 算法、PUI 字节、Counter 三者全部正确——这是最硬的证据。

### 5.4 行为验证(验证 Counter 语义)

| 操作 | 预期 | 已实测 |
|---|---|---|
| 断连后重新读 C3 | counter/RDI 不变 | ✔ (log 2026-09-20) |
| 整机复位后再读 | counter +1,RDI 随之改变 | ✔ |
| 重烧镜像(不整片擦除) | BootCount 保留,counter 连续 | ✔ (烧录须知:保留 Bootloader/工厂数据/Counter) |
| 整片擦除(erase chip) | BootCount 清零 → counter 回到小值,与量产记录时间线脱钩 | ⚠ 避免在 RDI 设备上做 |

### 5.5 负面用例(验证"不是碰巧匹配")

1. CSV 里把某行 `unique_id` 改一个字符(如 `A`→`B`)→ 该设备应变为 no RDI match
2. 两台设备故意配同一 discriminator → 扫描仍能各自唯一匹配(RDI 区分)
3. `--algorithm MATTER_V0` 跑 V1 固件 → 应全部不匹配(算法隔离正确)

### 5.6 边界(文档已声明未覆盖,验证时注意)

MTU=23 长读(GATT 长读需要连接参数支持)、完整 Thread 配网联动、
Amazon MSS 生态侧验证——这三项当前工程"Windows + MTU=247"结论未包含。

---

## 6. 坑与注意事项

1. **C3 类型必须 USER,不能 HEX**——HEX 类型下读出静态 `00`,SDK 的 TLV 根本没发出去
2. **PUI 大小写是身份字节**——CSV 必须与写入芯片的大小写逐字符一致(32 ASCII 字节参与哈希)
3. **算法无自动回退**——V1 固件配 V0 扫描(或反之)只会静默不匹配;CSV 不含算法列,新文件默认 V1
4. **Counter 小端、盐小端**——对拍代码最常见的错就是写了大端
5. **整片擦除毁 Counter 连续性**(§6.4)
6. **量产工具版本**——须 mfg_tool ≥ 2.6.8 烧 DAC;`rdi_data.csv` 导出为量产工具后续新增功能
7. 补丁改在共享 SDK 的 `extension/matter_extension` 里,**共用该 SDK 的其他工程也会默认 V1**
8. RDI 是**明文可读**(文档明确:读取不要求加密/认证/绑定)——安全性完全建立在
   HKDF 单向性 + PUI 不出芯片上;不要往 C3 里放任何秘密

---

## 7. 涉及的关键代码位置

| 位置 | 作用 |
|---|---|
| `matter_sdk/src/setup_payload/AdditionalDataPayloadGenerator.cpp` | RDI 生成(V0 原版/V1 补丁分支) |
| `matter_sdk/src/setup_payload/AdditionalDataPayload.h` | 18 字节定义、标签 0x00、规范用途注释 |
| `matter_sdk/src/platform/silabs/efr32/BLEManagerImpl.cpp` `EncodeAdditionalDataTlv/HandleC3ReadRequest` | TLV 生成 + C3 读请求响应 |
| `matter_sdk/src/platform/silabs/ConfigurationManagerImpl.cpp` `GetRebootCount/IncreaseBootCount` | Counter = NVM3 BootCount |
| `matter_sdk/src/platform/silabs/SilabsConfig.h:150` | PUI 工厂键 `kConfigKey_PersistentUniqueId`(0x08721F) |
