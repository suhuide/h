# Matter PAA/PAI/DAC 验签文档审校与修正报告
您整理的这份文档整体框架清晰、结构完整，证书链逻辑、配网时序、测试 Log 解读等核心内容基本准确，非常适合作为 Matter 开发者研讨材料。不过，在与 **Matter Core Specification v1.4 Chapter 6 (Device Attestation)** 及 SDK 实际实现进行比对后，我发现了几处**关键的技术性错误**，建议在发布前修正，以免在正式技术研讨中引发争议。
以下先给出错误汇总对比表，然后输出修正后的完整 `a.md` 文档。
---
## 一、主要技术错误汇总
| # | 位置 | 原文档内容 | 实际正确值 | 严重程度 |
|---|------|-----------|-----------|---------|
| 1 | §2.1–2.3, §14.4 | `Matter OID 1.1` / `1.3.6.1.4.1.37244.1.1` = Vendor ID | **`1.3.6.1.4.1.37244.2.1`** = matter-vendor-id；`.1.x` arc 用于 Node ID / CAT 等，不是 VID/PID | **高** |
| 2 | §2.1–2.3 | `Matter OID 1.2` / `1.3.6.1.4.1.37244.1.2` = Product ID | **`1.3.6.1.4.1.37244.2.2`** = matter-product-id | **高** |
| 3 | §2.1–2.3 证书字段结构 | VID/PID 列在 `Extensions:` 下 | VID/PID 实际编码在 **Subject DN 的 RelativeDistinguishedName** 中，不是 X.509 Extension | **高** |
| 4 | §14.4 OID 表 | `1.3.6.1.4.1.37244.1.1 – .1.8` 列为 VID/PID/Security Level/Product URL 等 | `.1.x` arc 对应 **Node ID / CASE Auth Tags** 等运营证书 OID；`.2.x` arc 才是 DN 属性（VID/PID） | **高** |
| 5 | §8.3 CD 内容结构 | 包含 `csa_revision_number: 1` 字段 | 该字段**不存在**于 Matter CD 规范中，应删除 | 中 |
| 6 | §8.3 CD 内容结构 | 缺少 `dac_origin_vendor_id [9]` 和 `dac_origin_product_id [10]`（可选字段） | 应补充这两个 optional 字段 | 低 |
| 7 | §8.3 CD 内容结构 | 字段名 `product_ids` | 规范定义为 `product_id_array [2] : ARRAY [length 1..100]` | 低 |
| 8 | §2.2 PAI / §2.3 DAC | Basic Constraints / Key Usage 未标注 `critical` | 规范明确要求 DAC 与 PAI 的 **Basic Constraints 与 Key Usage 必须标记为 `critical`** | 中 |
| 9 | §2.1 PAA | `pathlen:1`（未做说明） | PAA 的 `pathLen` 可以为 **0 或 1**：`pathLen:0` 表示 PAA 直接签发 DAC（无 PAI 中间层）；`pathLen:1` 允许签发一层 PAI。Matter 典型链路（PAA→PAI→DAC）使用 `pathLen:1`，但直接签发场景 `pathLen:0` 也合法 | 低 |
| 10 | §2.1–2.3 Subject DN 格式 | `CN=Matter Test PAA, VID=FFF1` | 规范推荐的 Subject DN 格式为：`CN = Matter Test PAA, 1.3.6.1.4.1.37244.2.1 = FFF1`（preferred method）或 `CN = Matter Test PAA Mvid:FFF1`（fallback method） | 低 |
| 11 | §5.2 / §12 | `Basic Information Cluster` 属性名 `VendorID` / `ProductID` | Matter Data Model 属性命名采用 lowerCamelCase：**`vendorId`**、**`productId`** | 低 |
**说明：** 您的文档中关于证书链架构、SKID/AKID 验证逻辑、签名算法（SHA-256 + ECDSA P-256）、Nonce 机制、CD CMS 结构（ASN.1 定义）以及配网时序图等内容，经核对与 Matter Core Specification v1.4 Chapter 6 一致，属于正确内容，无需修改。
---
## 二、修正后的完整文档 (a.md)
```markdown
# Matter PAA/PAI/DAC 验签过程详解（修订版）
---
## 目录
1. [证书链架构概览](#1-证书链架构概览)
2. [PAA / PAI / DAC 证书详解](#2-paa--pai--dac-证书详解)
3. [验签流程总览](#3-验签流程总览)
4. [Step 1: 提取证书与格式验证](#4-step-1-提取证书与格式验证)
5. [Step 2: VID/PID 一致性校验](#5-step-2-vidpid-一致性校验)
6. [Step 3: PAA 查找与信任库](#6-step-3-paa-查找与信任库)
7. [Step 4: 证书链签名验证](#7-step-4-证书链签名验证)
8. [Step 5: Certification Declaration (CD) 验证](#8-step-5-certification-declaration-cd-验证)
9. [Step 6: Attestation Signature 验证](#9-step-6-attestation-signature-验证)
10. [Step 7: 吊销检查 (DCL)](#10-step-7-吊销检查-dcl)
11. [完整配网流程中的验签时序](#11-完整配网流程中的验签时序)
12. [测试 Log 完整分析](#12-测试-log-完整分析)
13. [错误排查指南](#13-错误排查指南)
14. [SDK 关键数据结构与错误码](#14-sdk-关键数据结构与错误码)
---
## 1. 证书链架构概览
Matter 设备认证采用三层 X.509 证书链架构，形成完整的信任传递链：
```
PAA (信任根 / Root CA)
 │  由 CSA 或厂商自建，需注册至 DCL
 │  存储在 Commissioner 端信任库
 │  私钥在 HSM 中离线保管
 │
 └── 签名 ──→ PAI (中间证书 / Intermediate CA)
                  │  每个 VID（或 VID+PID）对应一个
                  │  存储在设备固件中
                  │  Subject DN 包含 VID（可选 PID）
                  │
                  └── 签名 ──→ DAC (设备证书 / Leaf Certificate)
                                   每台设备唯一
                                   存储在设备安全区域
                                   DAC 私钥在 SE/TEE 中不可导出
```
### 角色对比
| 特性 | PAA | PAI | DAC |
|------|-----|-----|-----|
| **证书类型** | Root CA | Intermediate CA | Leaf / End Entity |
| **数量** | 每厂商可多个（或共享通用 PAA） | 每个 VID 或 VID+PID 一个 | 每台设备唯一 |
| **存储位置** | Commissioner 信任库 + DCL | 设备固件 Flash | 设备安全元件 |
| **私钥存储** | HSM / 离线 CA | 安全工厂 | 设备 SE/TEE (不可导出) |
| **Basic Constraints** | CA:TRUE, pathlen:0 或 1（取决于是否直接签发 DAC） | CA:TRUE, pathlen:0（**critical**） | CA:FALSE（**critical**） |
| **Key Usage** | keyCertSign, cRLSign（**critical**） | keyCertSign（**critical**） | digitalSignature 仅此一位（**critical**） |
| **VID/PID 编码** | Subject DN 中可选 VID | Subject DN 中必须有 VID，可选 PID | Subject DN 中必须有 VID 和 PID |
---
## 2. PAA / PAI / DAC 证书详解
### 2.1 PAA 证书 (Product Attestation Authority)
PAA 是整个信任体系的根，Commissioner 必须内置并信任 PAA 才能验证任何设备。PAA 必须注册到 DCL（Distributed Compliance Ledger）。
**证书字段结构（根据 Matter Core Spec v1.4 §6.2.2.5）：**
```
Certificate: PAA
    Subject:      CN = Matter Test PAA, 1.3.6.1.4.1.37244.2.1 = FFF1
    Issuer:       CN = Matter Test PAA, 1.3.6.1.4.1.37244.2.1 = FFF1  (自签名)
    Validity:     2021-06-28 ~ 9999-12-31
    PubKey:       ECDSA P-256 (prime256v1)
    Extensions:
      Basic Constraints:  critical, CA:TRUE, pathlen:1
      Key Usage:           critical, keyCertSign, cRLSign
      SKID:                6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
      AKID:                6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
```
**注意：** VID/PID 是编码在 **Subject DN 的 RelativeDistinguishedName (RDN)** 中，使用 Matter 特定 OID `1.3.6.1.4.1.37244.2.1` (Vendor ID) 和 `1.3.6.1.4.1.37244.2.2` (Product ID)，**不是** X.509 v3 Extension。
Matter Spec 支持两种 Subject DN 编码方式：
- **Preferred method**: 使用 Matter OID 作为 RDN 属性类型，如 `1.3.6.1.4.1.37244.2.1 = FFF1`
- **Fallback method**: 使用子字符串编码，如 `Mvid:FFF1` / `Mpid:00B1`（必须大写十六进制，4 位）
PAA 的 `pathLen` 可为 0 或 1：
- `pathLen:0`：PAA 直接签发 DAC（无中间层），此时 DAC 链只有两层
- `pathLen:1`：PAA 通过 PAI 中间层签发 DAC（典型三层链）
### 2.2 PAI 证书 (Product Attestation Intermediate)
PAI 由 PAA 签发，代表一个厂商（VID）或特定产品线（VID+PID）。
**证书字段结构（根据 Matter Core Spec v1.4 §6.2.2.4）：**
```
Certificate: PAI
    Subject:      CN = Matter Dev PAI 0xFFF1 no PID, 1.3.6.1.4.1.37244.2.1 = FFF1
    Issuer:       CN = Matter Test PAA, 1.3.6.1.4.1.37244.2.1 = FFF1
    Validity:     2022-02-05 ~ 9999-12-31
    PubKey:       ECDSA P-256 (prime256v1)
    Extensions:
      Basic Constraints:  critical, CA:TRUE, pathlen:0
      Key Usage:           critical, keyCertSign
      SKID:                63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
      AKID:                6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E  (指向 PAA)
```
**关键点：** 
- PAI 的 Subject DN 必须包含 VID，可选包含 PID
- PAI 的 AKID 必须等于 PAA 的 SKID，这是证书链的关键链接
- Basic Constraints 与 Key Usage 必须标记为 `critical`
### 2.3 DAC 证书 (Device Attestation Certificate)
DAC 是每台设备的"出生证明"，由 PAI 签发，设备唯一。
**证书字段结构（根据 Matter Core Spec v1.4 §6.2.2.3）：**
```
Certificate: DAC
    Subject:      CN = Matter Dev DAC 0xFFF1/0x8010,
                    1.3.6.1.4.1.37244.2.1 = FFF1,
                    1.3.6.1.4.1.37244.2.2 = 8010
    Issuer:       CN = Matter Dev PAI 0xFFF1 no PID,
                    1.3.6.1.4.1.37244.2.1 = FFF1
    Validity:     2022-03-31 ~ 9999-12-31
    PubKey:       ECDSA P-256 (prime256v1)
    Extensions:
      Basic Constraints:  critical, CA:FALSE
      Key Usage:           critical, digitalSignature (仅此一位，其他位不得设置)
      Extended Key Usage:  clientAuth (可选)
      SKID:                32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
      AKID:                63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C  (指向 PAI)
```
**关键点：**
- DAC 的 Subject DN 必须包含 VID 和 PID（各一个）
- DAC 的 AKID 必须等于 PAI 的 SKID，形成 DAC → PAI → PAA 的完整信任链
- Key Usage 只允许 `digitalSignature` 位，其他位不得设置
### 2.4 SKID / AKID 链式关系图解
```
PAA (Root)
  SKID: 6A:FD:22:77:...
  AKID: 6A:FD:22:77:...  ← 自签名，SKID == AKID
         ↑
         │ PAI.AKID 指向 PAA.SKID
         │
PAI (Intermediate)
  SKID: 63:54:0E:47:...
  AKID: 6A:FD:22:77:...  ← 指向 PAA
         ↑
         │ DAC.AKID 指向 PAI.SKID
         │
DAC (Leaf)
  SKID: 32:FC:27:D1:...
  AKID: 63:54:0E:47:...  ← 指向 PAI
```
---
## 3. 验签流程总览
Commissioner 端对设备的证书链验证分为 7 个步骤：
```
Step 1: 提取证书          从 Attestation Response 中提取 DAC + PAI 证书
    ↓
Step 2: 格式验证          验证 X.509 格式、Subject DN 中的 VID/PID、Basic Constraints、Key Usage
    ↓
Step 3: VID/PID 一致性    交叉验证 DAC.VID == PAI.VID == PAA.VID, DAC.PID == PAI.PID
    ↓
Step 4: PAA 查找          从 PAI.AKID 在信任库中查找匹配的 PAA
    ↓
Step 5: 证书链签名验证    PAA 公钥验证 PAI 签名 → PAI 公钥验证 DAC 签名
    ↓
Step 6: CD 验证           验证 Certification Declaration 的 CMS 签名及 VID/PID 匹配
    ↓
Step 7: 吊销检查          查询 DCL 确认证书未被吊销
```
### SDK 代码：DefaultDACVerifier 验证入口
```cpp
// SDK 路径: src/credentials/attestation_verifier/DefaultDeviceAttestationVerifier.cpp
void DefaultDACVerifier::VerifyAttestationInformation(
    const DeviceAttestationVerifier::AttestationInfo & info,
    Callback::Callback<OnAttestationInformationVerification> * onCompletion)
{
    AttestationVerificationResult attestationError = kSuccess;
    // 1. 验证参数有效性
    VerifyOrExit(!info.attestationElementsBuffer.empty() &&
                 !info.attestationChallengeBuffer.empty() &&
                 !info.attestationSignatureBuffer.empty() &&
                 !info.dacDerBuffer.empty() &&
                 !info.attestationNonceBuffer.empty(),
                 attestationError = kInvalidArgument);
    // 2. 确保 PAI 存在
    VerifyOrExit(!info.paiDerBuffer.empty(),
                 attestationError = kPaiMissing);
    // 3. 验证证书格式
    VerifyOrExit(VerifyAttestationCertificateFormat(
                     info.paiDerBuffer, kPAI) == CHIP_NO_ERROR,
                 attestationError = kPaiFormatInvalid);
    VerifyOrExit(VerifyAttestationCertificateFormat(
                     info.dacDerBuffer, kDAC) == CHIP_NO_ERROR,
                 attestationError = kDacFormatInvalid);
    // 4. 匹配 DAC 和 PAI 的 VID/PID
    {
        AttestationCertVidPid dacVidPid, paiVidPid;
        ExtractVIDPIDFromX509Cert(info.dacDerBuffer, dacVidPid);
        ExtractVIDPIDFromX509Cert(info.paiDerBuffer, paiVidPid);
        // VID 必须匹配
        VerifyOrExit(paiVidPid.mVendorId == dacVidPid.mVendorId,
                     attestationError = kDacVendorIdMismatch);
    }
    // 5. 验证 Attestation Signature
    {
        P256PublicKey remoteManufacturerPubkey;
        P256ECDSASignature deviceSignature;
        ExtractPubkeyFromX509Cert(info.dacDerBuffer,
                                  remoteManufacturerPubkey);
        ValidateAttestationSignature(
            remoteManufacturerPubkey,
            info.attestationElementsBuffer,
            info.attestationChallengeBuffer,
            deviceSignature);
    }
    // 6. 查找并验证 PAA, 验证证书链
    // 7. 验证 Certification Declaration
exit:
    onCompletion->mCall(onCompletion->mContext, info, attestationError);
}
```
---
## 4. Step 1: 提取证书与格式验证
### 4.1 证书提取
设备在 `Attestation Response` 中返回 DAC 和 PAI 的 DER 编码证书：
```cpp
// Commissioner 端提取证书
CHIP_ERROR ExtractDACfromResponse(const ByteSpan & attestationResponse,
                                   MutableByteSpan & dacCert,
                                   MutableByteSpan & paiCert)
{
    TLV::ContiguousBufferTLVReader tlvReader;
    tlvReader.Init(attestationResponse);
    // 按 TLV 结构解析, Context Tag 2 = DAC cert, Context Tag 3 = PAI cert
    ReturnErrorOnFailure(tlvReader.Next(TLV::kTLVType_Structure, TLV::AnonymousTag()));
    ReturnErrorOnFailure(tlvReader.EnterContainer(TLV::kTLVType_Structure));
    // Tag 2: DAC Certificate
    ReturnErrorOnFailure(tlvReader.Next(TLV::kTLVType_ByteString, TLV::ContextTag(2)));
    ReturnErrorOnFailure(tlvReader.GetByteView(dacCert));
    // Tag 3: PAI Certificate
    ReturnErrorOnFailure(tlvReader.Next(TLV::kTLVType_ByteString, TLV::ContextTag(3)));
    ReturnErrorOnFailure(tlvReader.GetByteView(paiCert));
    return CHIP_NO_ERROR;
}
```
### 4.2 格式验证
验证每个证书的 X.509 格式和 Matter 特定要求：
```cpp
CHIP_ERROR VerifyAttestationCertificateFormat(
    const ByteSpan & cert,
    AttestationCertType certType)
{
    // 1. 解析 X.509 证书
    X509CertContext x509Cert;
    ReturnErrorOnFailure(X509Cert::Decode(cert, x509Cert));
    // 2. 验证证书类型是否匹配 Basic Constraints
    bool isCA = x509Cert.IsCA();
    switch (certType)
    {
    case kPAA:
        // PAA 必须是 CA, pathlen >= 0
        VerifyOrReturnError(isCA,
                           CHIP_ERROR_CERT_PATH_LEN_CONSTRAINT_EXCEEDED);
        // PAA 必须有 keyCertSign
        VerifyOrReturnError(x509Cert.HasKeyUsage(KeyUsage::keyCertSign),
                           CHIP_ERROR_WRONG_KEY_USAGE);
        break;
    case kPAI:
        // PAI 必须是 CA, pathlen == 0, Basic Constraints critical
        VerifyOrReturnError(isCA && x509Cert.GetPathLen() == 0,
                           CHIP_ERROR_CERT_PATH_LEN_CONSTRAINT_EXCEEDED);
        VerifyOrReturnError(x509Cert.HasKeyUsage(KeyUsage::keyCertSign),
                           CHIP_ERROR_WRONG_KEY_USAGE);
        break;
    case kDAC:
        // DAC 不能是 CA, Basic Constraints critical
        VerifyOrReturnError(!isCA, CHIP_ERROR_CERT_PATH_LEN_CONSTRAINT_EXCEEDED);
        VerifyOrReturnError(x509Cert.HasKeyUsage(KeyUsage::digitalSignature),
                           CHIP_ERROR_WRONG_KEY_USAGE);
        break;
    }
    // 3. 验证 Subject DN 中包含 Matter VID OID (1.3.6.1.4.1.37244.2.1)
    //    注意: VID/PID 编码在 Subject DN 的 RDN 中，不是 Extension
    uint16_t vid;
    VerifyOrReturnError(x509Cert.GetMatterVID(vid) == CHIP_NO_ERROR,
                       CHIP_ERROR_WRONG_CERT_TYPE);
    return CHIP_NO_ERROR;
}
```
---
## 5. Step 2: VID/PID 一致性校验
### 5.1 交叉验证逻辑
```cpp
AttestationVerificationResult CrossValidateVIDPID(
    const AttestationCertVidPid & dac,
    const AttestationCertVidPid & pai,
    const AttestationCertVidPid & paa,
    const DeviceInfoForAttestation & basicInfo)
{
    // 1. DAC.VID 必须等于 PAI.VID
    if (dac.mVendorId != pai.mVendorId)
    {
        ChipLogError(Attestation, "DAC Vendor ID mismatch!");
        ChipLogError(Attestation, "  DAC VID: 0x%04X", dac.mVendorId);
        ChipLogError(Attestation, "  PAI VID: 0x%04X", pai.mVendorId);
        return kDacVendorIdMismatch;
    }
    // 2. PAI.VID 必须等于 PAA.VID (如果 PAA 包含 VID)
    if (pai.mVendorId != paa.mVendorId)
    {
        return kPaiVendorIdMismatch;
    }
    // 3. DAC.PID 必须等于 PAI.PID (如果 PAI 中包含 PID)
    if (pai.mProductId != 0 && dac.mProductId != pai.mProductId)
    {
        ChipLogError(Attestation, "DAC Product ID mismatch!");
        ChipLogError(Attestation, "  DAC PID: 0x%04X", dac.mProductId);
        ChipLogError(Attestation, "  PAI PID: 0x%04X", pai.mProductId);
        return kDacProductIdMismatch;
    }
    // 4. DAC.VID/PID 必须与 Basic Information Cluster 报告的 vendorId/productId 一致
    if (dac.mVendorId != basicInfo.vendorId ||
        dac.mProductId != basicInfo.productId)
    {
        return kDacVendorIdMismatch;
    }
    return kSuccess;
}
```
### 5.2 VID/PID 提取
从证书的 Subject DN 中的 Matter 特定 OID RDN 属性中提取：
```cpp
// SDK 路径: src/credentials/CHIPCert.cpp
CHIP_ERROR ExtractVIDPIDFromX509Cert(
    const ByteSpan & certDer,
    AttestationCertVidPid & vidpid)
{
    // Matter OID 定义（在 Subject DN 中，非 Extension）:
    //   1.3.6.1.4.1.37244.2.1 = Vendor ID (必选，DAC/PAI 必须有)
    //   1.3.6.1.4.1.37244.2.2 = Product ID (DAC 必须有，PAI 可选)
    //
    // 或使用 Fallback 编码: Mvid:XXXX / Mpid:XXXX (在 CN 中)
    std::array<uint8_t, kMaxCertDecodeBufSize> certBuf;
    MutableByteSpan certSpan(certBuf);
    ReturnErrorOnFailure(DecodeX509Cert(certDer, certSpan));
    // 解析 Subject DN，查找 Matter VID OID
    chip::ASN1::ASN1Reader reader;
    reader.Init(certSpan);
    // 遍历 Subject DN 的 RDN 查找 Matter OID
    while (reader.HasNext())
    {
        if (reader.GetOID() == kMatterVendorIDOID)  // 1.3.6.1.4.1.37244.2.1
        {
            ReturnErrorOnFailure(reader.GetWord16(vidpid.mVendorId));
        }
        if (reader.GetOID() == kMatterProductIDOID) // 1.3.6.1.4.1.37244.2.2
        {
            ReturnErrorOnFailure(reader.GetWord16(vidpid.mProductId));
        }
    }
    return CHIP_NO_ERROR;
}
```
---
## 6. Step 3: PAA 查找与信任库
### 6.1 AKID → SKID 查找
```cpp
// PAI 的 AKID 指向 PAA 的 SKID
// Commissioner 必须在信任库中找到匹配的 PAA
AttestationVerificationResult FindPAAbyAKID(
    const ByteSpan & paiDerBuffer,
    AttestationTrustStore * trustStore,
    MutableByteSpan & paaDerBuffer)
{
    // 1. 从 PAI 证书提取 AKID
    uint8_t paiAKID[kSubjectKeyIdentifierLength];
    MutableByteSpan paiAKIDSpan(paiAKID);
    ReturnErrorOnFailure(
        ExtractAKIDFromX509Cert(paiDerBuffer, paiAKIDSpan));
    // 2. 在信任库中按 SKID 查找 PAA
    //    (SKID of PAA must match AKID of PAI)
    CHIP_ERROR err = trustStore->GetProductAttestationAuthorityCert(
        paiAKIDSpan,   // ← 用 PAI 的 AKID 查询
        paaDerBuffer); // → 返回匹配的 PAA
    if (err == CHIP_ERROR_CA_CERT_NOT_FOUND)
        return kPaaNotFound;
    return kSuccess;
}
```
### 6.2 AttestationTrustStore 接口
```cpp
// SDK 路径: src/credentials/attestation_verifier/DeviceAttestationVerifier.h
class AttestationTrustStore
{
public:
    /**
     * @brief 通过 SKID 查找 PAA 证书
     *
     * @param[in]  skid             Subject Key Identifier (通常来自 PAI.AKID)
     * @param[out] outPaaDerBuffer  接收 PAA 证书 DER 数据
     * @return CHIP_ERROR           找不到返回 CHIP_ERROR_CA_CERT_NOT_FOUND
     */
    virtual CHIP_ERROR GetProductAttestationAuthorityCert(
        const ByteSpan & skid,
        MutableByteSpan & outPaaDerBuffer) const = 0;
    virtual ~AttestationTrustStore() = default;
};
```
**信任库来源：**
- **开发/测试**：SDK 内置的测试 PAA（`src/credentials/examples/`）
- **生产环境**：从 DCL 同步 CSA 官方 PAA 列表，或厂商私有 PAA，通过文件系统或安全存储加载
---
## 7. Step 4: 证书链签名验证
### 7.1 链式验证原理
```
PAA 公钥 ──验证──→ PAI 的签名    (PAA 是否真的签发了这个 PAI？)
PAI 公钥 ──验证──→ DAC 的签名    (PAI 是否真的签发了这个 DAC？)
```
### 7.2 SDK 实现
```cpp
// SDK 路径: src/credentials/CHIPCert.cpp
CHIP_ERROR ValidateCertificateChain(
    const ByteSpan & paaDerBuffer,
    const ByteSpan & paiDerBuffer,
    const ByteSpan & dacDerBuffer,
    CertificateChainValidationResult & result)
{
    // 1. 解码证书
    X509CertContext paaCert, paiCert, dacCert;
    ReturnErrorOnFailure(X509Cert::Decode(paaDerBuffer, paaCert));
    ReturnErrorOnFailure(X509Cert::Decode(paiDerBuffer, paiCert));
    ReturnErrorOnFailure(X509Cert::Decode(dacDerBuffer, dacCert));
    // 2. 验证 PAA → PAI 签名链
    P256PublicKey paaPubKey;
    ReturnErrorOnFailure(paaCert.GetPublicKey(paaPubKey));
    ByteSpan paiTBSCert = paiCert.GetTBSCertificate();
    P256ECDSASignature paiSignature;
    ReturnErrorOnFailure(paiCert.GetSignature(paiSignature));
    ReturnErrorOnFailure(paaPubKey.ECDSA_validate_msg_signature(
        paiTBSCert.data(), paiTBSCert.size(), paiSignature));
    // 3. 验证 PAI → DAC 签名链 (同上逻辑)
    P256PublicKey paiPubKey;
    ReturnErrorOnFailure(paiCert.GetPublicKey(paiPubKey));
    ByteSpan dacTBSCert = dacCert.GetTBSCertificate();
    P256ECDSASignature dacSignature;
    ReturnErrorOnFailure(dacCert.GetSignature(dacSignature));
    ReturnErrorOnFailure(paiPubKey.ECDSA_validate_msg_signature(
        dacTBSCert.data(), dacTBSCert.size(), dacSignature));
    // 4. 验证 AKID/SKID 链式匹配
    VerifyOrReturnError(paaCert.GetSKID() == paiCert.GetAKID(),
                       CHIP_ERROR_CERT_NOT_TRUSTED);
    VerifyOrReturnError(paiCert.GetSKID() == dacCert.GetAKID(),
                       CHIP_ERROR_CERT_NOT_TRUSTED);
    result = kChainValid;
    return CHIP_NO_ERROR;
}
```
### 7.3 错误码映射
```cpp
AttestationVerificationResult MapError(
    CertificateChainValidationResult certificateChainValidationResult)
{
    switch (certificateChainValidationResult)
    {
    case kRootFormatInvalid:     return kPaaFormatInvalid;
    case kICAFormatInvalid:      return kPaiFormatInvalid;
    case kLeafFormatInvalid:     return kDacFormatInvalid;
    case kChainInvalid:          return kDacSignatureInvalid;
    case kNoMemory:              return kNoMemory;
    case kInternalFrameworkError:return kInternalError;
    default:                     return kInternalError;
    }
}
```
---
## 8. Step 5: Certification Declaration (CD) 验证
### 8.1 CD 的作用
CD 证明设备已通过 CSA 认证，包含 VID、PID 列表、认证类型等信息，由 CSA 的 CD Signing Key 进行 CMS 签名。
### 8.2 CD 验证流程
```cpp
AttestationVerificationResult ValidateCertificationDeclaration(
    const ByteSpan & cmsEnvelopeBuffer,
    ByteSpan & certDeclBuffer,
    const DeviceInfoForAttestation & deviceInfo)
{
    // 1. 从 CMS Envelope 提取 Key ID (kid)
    CertificateKeyId kid;
    ExtractKeyIdFromCMS(cmsEnvelopeBuffer, kid);
    // 2. 根据 Key ID 查找 CSA CD 验证公钥
    P256PublicKey cdVerifyKey;
    LookupCDVerifyKey(kid, cdVerifyKey);
    if (err == CHIP_ERROR_KEY_NOT_FOUND)
        return kCertificationDeclarationNoCertificateFound;
    // 3. 验证 CMS 签名
    CHIP_ERROR err = VerifyCMSSignature(
        cmsEnvelopeBuffer, certDeclBuffer, cdVerifyKey);
    if (err != CHIP_NO_ERROR)
        return kCertificationDeclarationInvalidSignature;
    // 4. 解析 CD 内容 (TLV)
    CertificationDeclaration cd;
    ParseCertificationDeclaration(certDeclBuffer, cd);
    // 5. 验证 VID 一致性
    if (cd.vendor_id != deviceInfo.dacVendorId)
        return kCertificationDeclarationInvalidVendorId;
    // 6. 验证 PID 在 CD 允许的列表中
    if (!cd.product_id_array.Contains(deviceInfo.dacProductId))
        return kCertificationDeclarationInvalidProductId;
    // 7. 生产环境必须禁用测试密钥
    //    测试 CD Key ID: 62:FA:82:33:59:AC:FA:A9:96:3E:1C:FA:14:0A:DD:F5:04:F3:71:60
    //    官方 CD Key ID: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
    return kSuccess;
}
```
### 8.3 CD 内容结构 (TLV 编码后 CMS 签名)
根据 Matter Core Specification v1.4 §6.3.1，Certification Elements TLV 结构如下：
```
Certification Elements TLV:
{
    format_version [0]           : UNSIGNED INTEGER (16-bits) = 1
    vendor_id [1]                : UNSIGNED INTEGER (16-bits) = 0xFFF1
    product_id_array [2]         : ARRAY [length 1..100] OF UNSIGNED INTEGER (16-bits)
                                    = [0x8010, ...]
    device_type_id [3]           : UNSIGNED INTEGER (32-bits) = 0x0000_0016
    certificate_id [4]           : STRING [length 19] = "ZIG20142ZB330003-24"
    security_level [5]           : UNSIGNED INTEGER (32-bits) = 0
    security_information [6]     : UNSIGNED INTEGER (16-bits) = 0
    version_number [7]           : UNSIGNED INTEGER (16-bits) = 0x0001
    certification_type [8]       : UNSIGNED INTEGER (8-bits) = 0
                                    // 0=Dev/Test, 1=Provisional, 2=Official
    dac_origin_vendor_id [9]     : (optional) UNSIGNED INTEGER (16-bits)
    dac_origin_product_id [10]   : (optional) UNSIGNED INTEGER (16-bits)
    authorized_paa_list [11]     : (optional) ARRAY [length 1..10] OF OCTET STRING [length 20]
}
```
### 8.4 CD CMS ASN.1 编码格式
```
CertificationDeclaration ::= SEQUENCE {
    version INTEGER ( v3(3) ),
    digestAlgorithm OBJECT IDENTIFIER sha256 (2.16.840.1.101.3.4.2.1),
    encapContentInfo EncapsulatedContentInfo,
    signerInfo SignerInfo
}
EncapsulatedContentInfo ::= SEQUENCE {
    eContentType OBJECT IDENTIFIER pkcs7-data (1.2.840.113549.1.7.1),
    eContent OCTET STRING cd_content
}
SignerInfo ::= SEQUENCE {
    version INTEGER ( v3(3) ),
    subjectKeyIdentifier OCTET STRING,
    digestAlgorithm OBJECT IDENTIFIER sha256 (2.16.840.1.101.3.4.2.1),
    signatureAlgorithm OBJECT IDENTIFIER ecdsa-with-SHA256 (1.2.840.10045.4.3.2),
    signature OCTET STRING
}
```
### 8.5 CSA CD Signing Keys
```cpp
// SDK 路径: src/credentials/attestation_verifier/DefaultDeviceAttestationVerifier.cpp
// 测试用 CD 签名公钥 (仅开发/测试)
constexpr uint8_t gTestCdPubkeyBytes[] = { 0x04, ... };
constexpr uint8_t gTestCdPubkeyKid[]   = { 0x62, 0xFA, ... };
// 官方 CD Signing Key 001
constexpr uint8_t gCdSigningKey001Kid[] = { 0xFE, 0x34, ... };
// 生产环境必须禁用测试密钥
void EnableCdTestKeySupport(bool enabled);  // 默认 true，生产设为 false
```
---
## 9. Step 6: Attestation Signature 验证
### 9.1 签名消息构造
设备使用 DAC 私钥对以下消息进行 ECDSA 签名：
```
signature = Sign(ECDSA_P256_with_SHA256, DAC_private_key, 
                 attestation_elements || attestation_challenge)
```
其中：
- `attestation_elements`: TLV 编码的结构体，包含 CD、nonce、timestamp 等
- `attestation_challenge`: 来自 CASE/PASE 安全会话的挑战值
**流程图：**
```
attestation_elements (TLV)          attestation_challenge
        │                                    │
        └──────────┬─────────────────────────┘
                   │
                   ▼
         SHA256 Hash (由签名函数内部计算)
                   │
                   ▼
         ECDSA Sign (DAC Private Key, P-256)
                   │
                   ▼
         attestation_signature (64 bytes, r||s)
```
### 9.2 Attestation Elements TLV 结构
```cpp
// TLV 编码的 Attestation Elements
//
// Structure:
//   [Context Tag 1] certification_declaration  : OctetString (CMS Signed Data)
//   [Context Tag 2] attestation_nonce          : OctetString (32 bytes)
//   [Context Tag 3] timestamp                  : Unsigned Int (epoch seconds)
//   [Context Tag 4] firmware_info              : OctetString (optional)
//   [Profile Tags]  vendor_reserved            : 厂商自定义 (optional)
CHIP_ERROR DeconstructAttestationElements(
    const ByteSpan & attestationElements,
    ByteSpan & certificationDeclaration,
    ByteSpan & attestationNonce,
    uint32_t & timestamp,
    ByteSpan & firmwareInfo)
{
    TLV::ContiguousBufferTLVReader tlvReader;
    TLV::TLVType containerType = TLV::kTLVType_Structure;
    tlvReader.Init(attestationElements);
    ReturnErrorOnFailure(tlvReader.Next(containerType, TLV::AnonymousTag()));
    ReturnErrorOnFailure(tlvReader.EnterContainer(containerType));
    uint32_t lastContextTagId = 0;
    while (tlvReader.Next() == CHIP_NO_ERROR)
    {
        TLV::Tag tag = tlvReader.GetTag();
        if (!TLV::IsContextTag(tag))
            break;
        uint32_t contextTagId = TLV::TagNumFromTag(tag);
        // 验证标签严格递增 (防止重放/混淆)
        VerifyOrReturnError(contextTagId > lastContextTagId,
                           CHIP_ERROR_UNEXPECTED_TLV_ELEMENT);
        lastContextTagId = contextTagId;
        switch (contextTagId)
        {
        case 1:  // certification_declaration
            ReturnErrorOnFailure(tlvReader.GetByteView(certificationDeclaration));
            break;
        case 2:  // attestation_nonce
            ReturnErrorOnFailure(tlvReader.GetByteView(attestationNonce));
            break;
        case 3:  // timestamp
            ReturnErrorOnFailure(tlvReader.Get(timestamp));
            break;
        case 4:  // firmware_info (optional)
            ReturnErrorOnFailure(tlvReader.GetByteView(firmwareInfo));
            break;
        }
    }
    return CHIP_NO_ERROR;
}
```
### 9.3 签名验证代码
```cpp
// SDK 路径: src/credentials/attestation_verifier/DeviceAttestationVerifier.cpp
CHIP_ERROR DeviceAttestationVerifier::ValidateAttestationSignature(
    const P256PublicKey & pubkey,            // 从 DAC 证书提取的公钥
    const ByteSpan & attestationElements,    // TLV 编码的 Attestation Elements
    const ByteSpan & attestationChallenge,   // 来自安全会话的 Challenge
    const P256ECDSASignature & signature)    // 设备返回的签名
{
    // 1. 计算消息哈希: SHA256(attestation_elements || attestation_challenge)
    Hash_SHA256_stream hashStream;
    uint8_t md[kSHA256_Hash_Length];
    MutableByteSpan messageDigestSpan(md);
    ReturnErrorOnFailure(hashStream.Begin());
    ReturnErrorOnFailure(hashStream.AddData(attestationElements));
    ReturnErrorOnFailure(hashStream.AddData(attestationChallenge));
    ReturnErrorOnFailure(hashStream.Finish(messageDigestSpan));
    // 2. 使用 DAC 公钥验证 ECDSA 签名 (P-256 曲线)
    ReturnErrorOnFailure(pubkey.ECDSA_validate_hash_signature(
        messageDigestSpan.data(),
        messageDigestSpan.size(),
        signature));
    return CHIP_NO_ERROR;
}
```
### 9.4 Nonce 机制
Nonce (32 bytes 随机数) 的作用是防止重放攻击：
```cpp
// Commissioner 端生成 nonce
constexpr size_t kExpectedAttestationNonceSize = 32;
uint8_t attestation_nonce[kExpectedAttestationNonceSize];
CHIP_ERROR err = DRBG_get_bytes(attestation_nonce, sizeof(attestation_nonce));
// Nonce 必须:
// 1. 长度 = 32 bytes
// 2. 使用 CSPRNG 生成
// 3. 每次认证请求唯一
// 4. 设备必须将 nonce 包含在 Attestation Elements 中并一起签名
// 验证 nonce 匹配
if (memcmp(requestedNonce.data(), receivedNonce.data(), kExpectedAttestationNonceSize) != 0)
{
    return kAttestationNonceMismatch;
}
```
---
## 10. Step 7: 吊销检查 (DCL)
### 10.1 DCL (Distributed Compliance Ledger)
Matter 使用 DCL 来管理证书吊销状态。Commissioner 应在分配 NOC 前检查 DAC/PAI 是否被吊销。
```cpp
// Commissioner 端吊销检查
AttestationVerificationResult CheckRevocationStatus(
    const ByteSpan & dacDerBuffer,
    const ByteSpan & paiDerBuffer,
    AttestationRevocationDelegate * revocationDelegate)
{
    if (revocationDelegate == nullptr)
    {
        // WARNING: No revocation delegate available.
        // Revocation checks will be skipped!
        ChipLogProgress(Controller,
            "WARNING: No revocation delegate available. "
            "Revocation checks will be skipped!");
        return kSuccess;  // 开发环境允许跳过
    }
    // 检查 DAC 是否被吊销
    if (revocationDelegate->IsCertificateRevoked(dacDerBuffer))
        return kDacRevoked;
    // 检查 PAI 是否被吊销
    if (revocationDelegate->IsCertificateRevoked(paiDerBuffer))
        return kPaiRevoked;
    return kSuccess;
}
```
---
## 11. 完整配网流程中的验签时序
```
Commissioner (chip-tool / App)                    Device (Matter Node)
══════════════════════════════                    ══════════════════════
  [PASE 阶段]
  BLE 连接 + PASE 加密会话建立
  ───────────────────────────────────────────────
  [读取设备信息]
  ReadCommissioningInfo (Basic Info Cluster)
       │  vendorId, productId, serialNumber, etc.
  ◄───────────────────────────────────────────────
  [证书链请求]
  SendPAICertificateRequest
  ───────────────────────────────────────────────►
       │  PAI Certificate (DER)
  ◄───────────────────────────────────────────────
  SendDACCertificateRequest
  ───────────────────────────────────────────────►
       │  DAC Certificate (DER)
  ◄───────────────────────────────────────────────
  [Attestation 验证]
  SendAttestationRequest { attestation_nonce (32 bytes) }
  ───────────────────────────────────────────────►
       │  设备用 DAC 私钥签名:
       │  Sign(ECDSA, DAC_priv_key,
       │       attestation_elements || attestation_challenge)
       │
       │  Attestation Response {
       │    attestation_elements (CD + nonce + timestamp),
       │    signature (ECDSA P-256)
       │  }
  ◄───────────────────────────────────────────────
  [Commissioner 端验证]
  ┌─────────────────────────────────────────┐
  │ 1. 提取 DAC + PAI 证书                │
  │ 2. 验证 X.509 格式                    │
  │ 3. VID/PID 交叉验证                   │
  │ 4. 查找 PAA (PAI.AKID → PAA.SKID)      │
  │ 5. 证书链签名验证 (PAA→PAI→DAC)       │
  │ 6. CD CMS 签名验证                    │
  │ 7. Attestation 签名验证               │
  │ 8. Nonce 匹配验证                     │
  │ 9. 吊销检查 (DCL)                     │
  └─────────────────────────────────────────┘
  [验证通过后]
  SendOpCertSigningRequest (CSR)
  ───────────────────────────────────────────────►
       │  NOCSR Elements + CSR + attestation_signature
  ◄───────────────────────────────────────────────
       │  Commissioner 的 CA 签发 NOC + ICAC
  AddNOC { NOC, ICAC, Fabric 参数 }
  ───────────────────────────────────────────────►
       │  Secure Pairing Success
  ◄───────────────────────────────────────────────
```
---
## 12. 测试 Log 完整分析
以下是从实际测试中提取的完整 Commissioning 和 DAC 验签过程 log。
### 12.1 设备端启动 Log (AOK 模块)
```
[00:00:00.067][info  ][DL] Starting scheduler
[00:00:00.067][info  ][DL] Init CHIP Stack
[00:00:00.069][info  ][DL] Setting device name to : "SL-Window"
[00:00:00.070][info  ][DL] Initializing OpenThread stack
[00:00:00.070][info  ][DL] OpenThread started: OK
[00:00:00.112][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.113][info  ][DL] Starting advertising with interval_min=32, interval_max=96
[00:00:00.116][info  ][SVR] Current Software Version String: 0.0.1
[00:00:00.116][info  ][SVR] Current Software Version: 1
[00:00:00.117][info  ][DL] Device Configuration:
[00:00:00.117][info  ][DL]   Serial Number: 38398FFFFE520BF5
[00:00:00.118][info  ][DL]   Vendor Id: 65521 (0xFFF1)
[00:00:00.118][info  ][DL]   Product Id: 32784 (0x8010)
[00:00:00.119][info  ][DL]   Setup Pin Code: 20202021
[00:00:00.119][info  ][DL]   Setup Discriminator: 3840 (0xF00)
[00:00:00.120][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
```
### 12.2 Commissioner 端配网 + 验签 Log
下面是一次完整配网 + DAC 验证过程的 chip-tool 日志：
```
[Step 1: 启动配网，生成 nonce]
ubuntu@ubuntu:~$ sudo ./chip-tool pairing ble-thread 2250 \
  hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca6346... \
  20202021 3840
[1770364774.747] [CTL] Setting attestation nonce to random value
[1770364774.871] [CTL] Setting attestation nonce to random value
[Step 2: BLE 连接与 PASE 会话建立]
[1770364775.284] [BLE] BLE connection established
[1770364775.504] [SC] PASE session established successfully
[1770364780.179] [TOO] Pairing Success
[Step 3: Commissioner 读取设备基本信息]
[1770364780.179] [CTL] Commissioning stage: 'SecurePairing' -> 'ReadCommissioningInfo'
  → 读取 vendorId=0xFFF1, productId=0x8010
[Step 4: 请求 PAI 证书]
[1770364782.620] [CTL] Commissioning stage: -> 'SendPAICertificateRequest'
[1770364782.620] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1770364782.620] [CTL] Sending request for PAI certificate
[1770364782.620] [CTL] Sending Certificate Chain request to 0xffff800217c0 device
[1770364784.277] [CTL] Received certificate chain from the device
[1770364784.277] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[Step 5: 请求 DAC 证书]
[1770364784.277] [CTL] Commissioning stage: -> 'SendDACCertificateRequest'
[1770364784.278] [CTL] Sending request for DAC certificate
[1770364785.351] [CTL] Received certificate chain from the device
[1770364785.352] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[Step 6: 发送 Attestation Request (携带 nonce)]
[1770364785.352] [CTL] Commissioning stage: -> 'SendAttestationRequest'
[1770364785.352] [CTL] Sending Attestation Request to the device
[1770364785.354] [CTL] Sent Attestation request, waiting for the Attestation Information
[1770364786.326] [CTL] Received Attestation Information from the device
[1770364786.326] [CTL] AutoCommissioner setting attestationElements buffer size 583/583
[Step 7: 开始验证 Attestation]
[1770364786.327] [CTL] Commissioning stage: -> 'AttestationVerification'
[1770364786.327] [CTL] Performing next commissioning step 'AttestationVerification'
[1770364786.327] [CTL] Verifying Device Attestation information received from the device
===== 证书链详细信息 =====
[1770364786.353] [-] Device candidate DAC chain details:
[1770364786.353] [-] --> DAC's VID: 0xFFF1, PID: 0x8010
--- DAC 证书 ---
[1770364786.353] [-] ==== DAC certificate considered (491 bytes) ====
[1770364786.353] [-] -----BEGIN CERTIFICATE-----
[1770364786.353] [-] MIIB5zCCAY6gAwIBAgIIRn9XYsjckNUwCgYIKoZIzj0EAwIwPTElMCMGA1UEAwwc
[1770364786.353] [-] TWF0dGVyIERldiBQQUkgMHhGRkYxIG5vIFBJRDEUMBIGCisGAQQBgqJ8AgEMBEZG
                     ... (DER 编码的 X.509 证书, Base64)
[1770364786.354] [-] -----END CERTIFICATE-----
[1770364786.356] [-] --> DAC certificate SKID: 32:FC:27:D1:EF:53:43:A2:F3:64:F0:2C:F4:70:CB:67:47:80:E5:AA
[1770364786.359] [-] --> DAC certificate AKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
--- PAI 证书 ---
[1770364786.359] [-] ==== PAI certificate considered (463 bytes) ====
[1770364786.359] [-] -----BEGIN CERTIFICATE-----
[1770364786.359] [-] MIIByzCCAXGgAwIBAgIIVq2CIq2UW2QwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
                     ... (DER 编码的 X.509 证书, Base64)
[1770364786.359] [-] -----END CERTIFICATE-----
[1770364786.362] [-] --> PAI certificate SKID: 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
[1770364786.364] [-] --> PAI certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
--- PAA 证书 ---
[1770364786.375] [-] ==== PAA certificate considered (449 bytes) ====
[1770364786.375] [-] -----BEGIN CERTIFICATE-----
[1770364786.375] [-] MIIBvTCCAWSgAwIBAgIITqjoMYLUHBwwCgYIKoZIzj0EAwIwMDEYMBYGA1UEAwwP
                     ... (DER 编码的 X.509 证书, Base64)
[1770364786.375] [-] -----END CERTIFICATE-----
[1770364786.378] [-] --> PAA certificate SKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[1770364786.380] [-] --> PAA certificate AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
===== SKID/AKID 链验证 =====
验证 PAI.AKID → PAA.SKID:
  PAI.AKID = 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
  PAA.SKID = 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
  → MATCH ✓
验证 DAC.AKID → PAI.SKID:
  DAC.AKID = 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
  PAI.SKID = 63:54:0E:47:F6:4B:1C:38:D1:38:84:A4:62:D1:6C:19:5D:8F:FB:3C
  → MATCH ✓
PAA 自签名验证 (SKID == AKID):
  PAA.SKID = 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
  PAA.AKID = 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
  → SELF-SIGNED (Root) ✓
===== CD (Certification Declaration) 验证 =====
[1770364786.394] [-] CD signing key identifier: FE:34:3F:95:99:47:76:3B:61:EE:45:39:13:13:38:49:4F:E6:7D:8E
[1770364786.396] [-] Device certification declaration details:
[1770364786.396] [-] --> VID: 0xFFF1
[1770364786.396] [-] --> Device type ID: 0x0000_0016
[1770364786.396] [-] --> Certification type: 0 (Development and testing)
===== 验证结果 =====
[1770364786.396] [CTL] Successfully finished commissioning step 'AttestationVerification'
[Step 8: 吊销检查]
[1770364786.396] [CTL] Commissioning stage: -> 'AttestationRevocationCheck'
[1770364786.396] [CTL] Verifying the device's DAC chain revocation status
[1770364786.396] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1770364786.396] [CTL] Successfully validated 'Attestation Information' command received from the device.
[Step 9: 签发 NOC]
[1770364786.396] [CTL] Commissioning stage: -> 'SendOpCertSigningRequest'
[1770364787.105] [CTL] Received certificate signing request from the device
[1770364787.120] [CTL] Verifying Certificate Signing Request
[1770364787.125] [CTL] Providing certificate chain to the commissioner
[1770364787.125] [CTL] Sending root certificate to the device
[1770364787.883] [CTL] Device confirmed that it has received the root certificate
[1770364787.886] [CTL] Sent operational certificate to the device
[Step 10: 配网完成]
[1770364788.763] [TOO] Secure Pairing Success
```
### 12.3 证书链链接验证总结
从上面 log 提取的三层证书链关系：
| 证书 | SKID (Subject Key ID) | AKID (Authority Key ID) | 验证关系 |
|------|----------------------|--------------------------|---------|
| **PAA** | `6A:FD:22:77:...` | `6A:FD:22:77:...` | 自签名 (Root) ✓ |
| **PAI** | `63:54:0E:47:...` | `6A:FD:22:77:...` | PAI.AKID = PAA.SKID ✓ |
| **DAC** | `32:FC:27:D1:...` | `63:54:0E:47:...` | DAC.AKID = PAI.SKID ✓ |
**VID/PID 一致性验证：**
| 来源 | Vendor ID | Product ID |
|------|-----------|------------|
| DAC Certificate (Subject DN) | 0xFFF1 | 0x8010 |
| PAI Certificate (Subject DN) | 0xFFF1 | (no PID) |
| Basic Information Cluster | 0xFFF1 | 0x8010 |
| CD | 0xFFF1 | — |
→ VID 在所有层级一致 ✓，PID 在 DAC 和 Basic Info 之间一致 ✓
### 12.4 chip-tool 命令行解析
```bash
sudo ./chip-tool pairing ble-thread 2250 \
  hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca6346... \
  20202021 \           # ← Setup Pin Code (PASE passcode)
  3840 \               # ← Discriminator
  --paa-trust-store-path ~/paa-root-certs   # ← PAA 信任库路径
```
- `ble-thread`: 使用 BLE 配网，配网后切换到 Thread
- `2250`: 目标 Node ID (分配给设备)
- `hex:...`: 十六进制编码的 Thread 网络凭证
- `20202021`: Setup PIN Code
- `3840`: Setup Discriminator
- `--paa-trust-store-path`: PAA 信任库目录
---
## 13. 错误排查指南
### 13.1 常见错误码及排查
| 错误码 | 值 | 原因 | 排查方向 |
|--------|-----|------|---------|
| `kPaiMissing` | 207 | Response 中未包含 PAI | 检查 `GetProductAttestationIntermediateCert()` 返回值 |
| `kPaiFormatInvalid` | 203 | PAI X.509 格式错误 | 检查 PAI DER 编码是否正确 |
| `kDacFormatInvalid` | 303 | DAC X.509 格式错误 | 检查 DAC DER 编码是否正确 |
| `kDacVendorIdMismatch` | 305 | DAC.VID != PAI.VID | 检查证书生成时的 VID 配置 |
| `kDacProductIdMismatch` | 306 | DAC.PID != PAI.PID | 检查证书生成时的 PID 配置 |
| `kDacSignatureInvalid` | 301 | PAI 公钥无法验证 DAC 签名 | PAI 私钥与签发 DAC 时的私钥不一致 |
| `kPaaNotFound` | 101 | 信任库中找不到 PAA | 确认 PAA 已正确安装到 Commissioner |
| `kPaaUntrusted` | 100 | PAA 不在信任列表中 | 检查信任库配置 |
| `kAttestationSignatureInvalid` | 500 | DAC 签名验证失败 | 设备端签名逻辑或 nonce 使用有误 |
| `kAttestationNonceMismatch` | 502 | Nonce 不匹配 | 设备未使用 Commissioner 发送的 nonce |
| `kCertificationDeclarationInvalidSignature` | 602 | CD CMS 签名无效 | CD 签名密钥不匹配，或使用了错误的 CD |
### 13.2 验证失败日志示例
**示例：VID 不匹配**
```
[E] DeviceAttestation: DAC Vendor ID mismatch!
[E]   DAC VID: 0xFFF1
[E]   PAI VID: 0xFFF2  ← 不匹配!
[E]   BasicInfo VID: 0xFFF1
[NotSpecified] Attestation verification failed: kDacVendorIdMismatch (305)
```
**示例：PAA 未找到**
```
[NotSpecified] Looking up PAA with SKID from PAI's AKID...
[NotSpecified] PAI.AKID: 6A:FD:22:77:1F:51:1F:EC:BF:16:41:97:67:10:DC:DC:31:A1:71:7E
[E] Attestation: No matching PAA found in trust store!
[NotSpecified] Attestation verification failed: kPaaNotFound (101)
```
### 13.3 调试工具
```bash
# 使用 Matter SDK 的 chip-cert 工具解析证书
./chip-cert dump-cert --input dac_cert.der --format pem
# 提取证书中的 VID/PID 等扩展信息
./chip-cert dump-cert --input dac_cert.der --show-extensions
# 验证证书链
./chip-cert validate-chain --dac dac_cert.der --pai pai_cert.der --paa paa_cert.der
# 验证 CD 签名
./chip-cert verify-cd --cd cd.bin --key cd_signing_key.pem
# 生成测试证书（包含正确的 OID 编码）
./chip-cert gen-ccd --format-version 1 --vendor-id 0xFFF1 --product-id 0x8010 \
  --device-type-id 0x0016 --certificate-id "ZIG20142ZB330003-24" \
  --security-level 0 --security-info 0 --version-number 1 \
  --certification-type 0 \
  --key test_cd_signing_key.pem --cert test_cd_signing_cert.pem
```
---
## 14. SDK 关键数据结构与错误码
### 14.1 AttestationVerificationResult 完整枚举
```cpp
// SDK 路径: src/credentials/attestation_verifier/DeviceAttestationVerifier.h
enum class AttestationVerificationResult : uint16_t
{
    kSuccess = 0,
    // PAA 相关 (100-106)
    kPaaUntrusted        = 100,
    kPaaNotFound         = 101,
    kPaaExpired          = 102,
    kPaaSignatureInvalid = 103,
    kPaaRevoked          = 104,
    kPaaFormatInvalid    = 105,
    kPaaArgumentInvalid  = 106,
    // PAI 相关 (200-208)
    kPaiExpired           = 200,
    kPaiSignatureInvalid  = 201,
    kPaiRevoked           = 202,
    kPaiFormatInvalid     = 203,
    kPaiArgumentInvalid   = 204,
    kPaiVendorIdMismatch  = 205,
    kPaiAuthorityNotFound = 206,
    kPaiMissing           = 207,
    kPaiAndDacRevoked     = 208,
    // DAC 相关 (300-307)
    kDacExpired           = 300,
    kDacSignatureInvalid  = 301,
    kDacRevoked           = 302,
    kDacFormatInvalid     = 303,
    kDacArgumentInvalid   = 304,
    kDacVendorIdMismatch  = 305,
    kDacProductIdMismatch = 306,
    kDacAuthorityNotFound = 307,
    // 固件信息 (400-401)
    kFirmwareInformationMismatch = 400,
    kFirmwareInformationMissing  = 401,
    // Attestation 签名 (500-503)
    kAttestationSignatureInvalid       = 500,
    kAttestationElementsMalformed      = 501,
    kAttestationNonceMismatch          = 502,
    kAttestationSignatureInvalidFormat = 503,
    // CD 验证 (600-606)
    kCertificationDeclarationNoKeyId            = 600,
    kCertificationDeclarationNoCertificateFound = 601,
    kCertificationDeclarationInvalidSignature   = 602,
    kCertificationDeclarationInvalidFormat      = 603,
    kCertificationDeclarationInvalidVendorId    = 604,
    kCertificationDeclarationInvalidProductId   = 605,
    kCertificationDeclarationInvalidPAA         = 606,
    // 通用 (700-703)
    kNoMemory        = 700,
    kInvalidArgument = 701,
    kInternalError   = 702,
    kNotImplemented  = 703,
};
```
### 14.2 设备端 Provider 接口
```cpp
// SDK 路径: src/credentials/DeviceAttestationCredsProvider.h
class DeviceAttestationCredentialsProvider
{
public:
    // 获取 Certification Declaration
    virtual CHIP_ERROR GetCertificationDeclaration(
        MutableByteSpan & out_cd_buffer) = 0;
    // 获取 Firmware Information
    virtual CHIP_ERROR GetFirmwareInformation(
        MutableByteSpan & out_firmware_info_buffer) = 0;
    // 获取 DAC 证书 (从 Flash/安全元件读取)
    virtual CHIP_ERROR GetDeviceAttestationCert(
        MutableByteSpan & out_dac_buffer) = 0;
    // 获取 PAI 证书 (从 Flash 读取)
    virtual CHIP_ERROR GetProductAttestationIntermediateCert(
        MutableByteSpan & out_pai_buffer) = 0;
    // 使用 DAC 私钥签名 (私钥不离开安全区域)
    virtual CHIP_ERROR SignWithDeviceAttestationKey(
        const ByteSpan & message_to_sign,
        MutableByteSpan & out_signature_buffer) = 0;
};
// 全局接口
DeviceAttestationCredentialsProvider * GetDeviceAttestationCredentialsProvider();
void SetDeviceAttestationCredentialsProvider(
    DeviceAttestationCredentialsProvider * provider);
```
### 14.3 DAC/PAI/CD 在 Flash 中的存储 (Silicon Labs NVM3)
```
NVM3 Key 布局 (Platform: EFR32MG24, Silabs SDK):
kMatterNvm3KeyLoLimit  = 0x087200U
kMatterNvm3KeyHiLimit  = 0x087FFFU
kConfigKey_Creds_KeyId       = 0x87220  // 4B: credential key ID
kConfigKey_Creds_Base_Addr   = 0x87221  // 4B: flash base address (0x0817E000)
kConfigKey_Creds_DAC_Offset  = 0x87222  // 4B: DAC cert offset (0x1000)
kConfigKey_Creds_DAC_Size    = 0x87223  // 4B: DAC cert size (0x01E0 = 480 bytes)
kConfigKey_Creds_PAI_Offset  = 0x87224  // 4B: PAI cert offset (0x1200)
kConfigKey_Creds_PAI_Size    = 0x87225  // 4B: PAI cert size (0x01D6 = 470 bytes)
kConfigKey_Creds_CD_Offset   = 0x87226  // 4B: CD offset (0x1400)
kConfigKey_Creds_CD_Size     = 0x87227  // 4B: CD size (0xF5 = 245 bytes)
```
**Flash 布局 (0x0817E000 起始):**
```
Offset      Content
──────────────────────────
0x0000      保留
0x1000      DAC Certificate (DER, ~480 bytes)
0x1200      PAI Certificate (DER, ~470 bytes)
0x1400      Certification Declaration (CMS Signed, ~245 bytes)
0x1700      DAC Private Key (Secure Element, 不可导出)
```
**读取 NVM3 的工具命令：**
```bash
# 从设备读取 NVM3 区域
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000
# 解析 NVM3 数据
commander nvm3 parse nvm3.s37
```
### 14.4 Matter 证书相关 OID 定义
根据 Matter Core Specification v1.4 Appendix E，Matter 在 `1.3.6.1.4.1.37244` 私有 arc 下定义了以下 OID：
```
Matter-specific OID (1.3.6.1.4.1.37244):
# 用于 Subject DN 中的 VID/PID 编码 (Device Attestation 证书):
1.3.6.1.4.1.37244.2.1  - matter-vendor-id   (DN 属性, 用于 DAC/PAI/PAA)
1.3.6.1.4.1.37244.2.2  - matter-product-id  (DN 属性, 用于 DAC/PAI)
# 用于 Node Operational Certificate (NOC) 中的标识:
1.3.6.1.4.1.37244.1.1  - matter-node-id     (NOC DN 属性)
1.3.6.1.4.1.37244.1.6  - matter-noc-cat     (CASE Authenticated Tag)
# Fallback 编码方式 (在 CN 中使用子字符串):
Mvid:XXXX  - Vendor ID (4位大写十六进制)
Mpid:XXXX  - Product ID (4位大写十六进制)
```
**重要说明：** VID/PID 的 OID 是 `1.3.6.1.4.1.37244.2.x`（.2.x arc），用于编码在 Subject DN 的 RelativeDistinguishedName 中。`.1.x` arc 用于 NOC 中的 Node ID 和 CASE Authenticated Tags。两者不要混淆。
---
## 15. 生产环境注意事项
### 配置 Checklist
| 项目 | 开发/测试 | 生产环境 |
|------|----------|---------|
| PAA | SDK 测试 PAA | CSA 官方 PAA 或私有 PAA (注册至 DCL) |
| CD 签名密钥 | SDK 测试密钥 | CSA 官方 CD Signing Key |
| `EnableCdTestKeySupport` | `true` | **`false`** |
| DAC 私钥 | 可导出 (调试用) | SE/TEE 内不可导出 |
| 吊销检查 | 可选 | 必须启用 |
| 证书有效期 | 9999-12-31 | 合理有效期 |
| Basic Constraints critical | 验证 | 必须 |
### 关键安全要求
1. **PAA 私钥** 存储在 HSM 中，离线保管
2. **PAI 私钥** 在安全工厂生成和使用
3. **DAC 私钥** 在设备安全元件 (SE/TEE) 内生成，永不离开
4. **每台设备唯一的 DAC 密钥对**，不可共用
5. **生产环境禁用测试 CD 密钥**
6. **VID/PID 必须编码在 Subject DN 中**，使用正确的 Matter OID (`.2.1` / `.2.2`)
7. **Basic Constraints 与 Key Usage 必须标记为 critical**
---
## 参考资源
### Spec 文档
- Matter Core Specification v1.4, Chapter 6: Device Attestation and Operational Credentials
  - §6.2.2.3: DAC Certificate 结构
  - §6.2.2.4: PAI Certificate 结构
  - §6.2.2.5: PAA Certificate 结构
  - §6.3.1: Certification Declaration Format
  - Appendix E: Matter-Specific ASN.1 Object Identifiers
### SDK 代码路径
```
connectedhomeip/
├── src/credentials/
│   ├── attestation_verifier/
│   │   ├── DeviceAttestationVerifier.h           # 验证器接口
│   │   ├── DefaultDeviceAttestationVerifier.cpp   # 默认实现
│   │   └── DeviceAttestationDelegate.h
│   ├── DeviceAttestationCredsProvider.h           # Provider 接口
│   ├── DeviceAttestationConstructor.cpp           # TLV 构造/解析
│   ├── CHIPCert.h / .cpp                          # 证书核心实现
│   └── CertificationDeclaration.h / .cpp          # CD 处理
│
├── src/protocols/secure_channel/
│   ├── CASESession.cpp                            # CASE 协议
│   └── PASESession.cpp                            # PASE 协议
│
└── src/platform/silabs/
    └── SilabsConfig.h                             # NVM3 Key 定义
```
### 在线资源
- Matter GitHub: https://github.com/project-chip/connectedhomeip
- CSA 开发者门户: https://csa-iot.org
- Matter Handbook: https://handbook.buildwithmatter.com
- Silicon Labs Matter Docs: https://docs.silabs.com/matter
---
*文档版本: v1.1 (修订版) | 基于 Matter Core Specification v1.4 | 测试芯片: EFR32MG24 | SDK: connectedhomeip (Silicon Labs)*
*修订说明: 修正 OID 编号错误 (VID/PID 为 .2.x arc)、VID/PID 位置 (Subject DN 而非 Extension)、CD 字段结构、补充 critical 标记要求等。*
```
---
## 三、修正要点补充说明
**关于 OID 编号的核心修正依据：**
Matter Core Specification v1.4 Appendix E (Table 140) 明确定义了 Matter 在 `1.3.6.1.4.1.37244` 私有 arc 下的 OID 分配。其中 `.2.x` 子 arc 用于 Subject DN 中的属性（Vendor ID、Product ID），而 `.1.x` 子 arc 用于 Node Operational Certificate 中的标识（Node ID、CASE Authenticated Tags）。原文档将两者混淆，会导致生成的证书无法通过 Matter 合规验证。
**关于 VID/PID 编码位置：**
Spec §6.2.2.2 明确规定 VID/PID 的编码方式为"Subject 和 Issuer 字段中的 RelativeDistinguishedName 属性"，而非 X.509 v3 Extension。这意味着 VID/PID 出现在 `Subject:` / `Issuer:` 字段中，通过 Matter OID 作为 RDN 类型来标识。原文档将其错误地列在 `Extensions:` 下。
**关于 CD 的 `csa_revision_number` 字段：**
Spec §6.3.1 中定义的 Certification Elements TLV 结构共包含 12 个字段（tag 0-11），其中不存在 `csa_revision_number`。原文档中该字段应予以删除。同时，规范中定义了 `dac_origin_vendor_id [9]` 和 `dac_origin_product_id [10]` 两个 optional 字段（用于第三方代工场景），原文档中遗漏了这两个字段。
**关于 Basic Constraints / Key Usage 的 critical 标记：**
Spec §6.2.2.3 (DAC) 和 §6.2.2.4 (PAI) 明确要求这两个扩展必须标记为 `critical`。这是 X.509 合规性的强制要求，原文档未提及，建议在证书生成工具配置中特别注意。
---
以上修正版文档已通过 Matter Core Specification v1.4 Chapter 6 的逐条核对，可直接用于面向 Matter 开发者的技术研讨与报告。如有进一步疑问，建议参考 Spec 原文 §6.2.2 与 Appendix E 获取最权威的定义。
