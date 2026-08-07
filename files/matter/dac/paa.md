
#### 验证 4：VID/PID 一致性校验

确保证书链中的身份信息一致：

| 检查项 | 说明 |
|--------|------|
| DAC.vid == PAI.vid | DAC 与 PAI 的 Vendor ID 必须匹配（如 PAI 包含 VID） |
| DAC.vid == CD.vid | DAC 与 Certification Declaration 的 VID 匹配 |
| DAC.pid == CD.pid | DAC 与 Certification Declaration 的 PID 匹配 |

---

## 三、Certification Declaration（CD）的补充作用

CD 与证书链配合使用，提供设备认证的额外证据：

| 属性 | 说明 |
|------|------|
| **签发者** | CSA（Connectivity Standards Alliance） |
| **内容** | VID、PID、设备类型、安全等级、**认证类型**（development/provisional/official） |
| **存储位置** | 设备固件中 |
| **验证方式** | 使用 CSA 的公钥验证 CD 签名 |

CD 的签名验证确保该 (VID, PID) 对已通过 CSA 的 Matter 认证测试。

---

## 四、证书字段关联关系总结

| 证书 | Issuer | Subject | 关键扩展字段 |
|------|--------|---------|--------------|
| **PAA** | 自身 | CN=..., VID=...（可选） | SKID（用于 PAI 的 AKID 匹配） |
| **PAI** | PAA Subject | CN=..., VID=...（可选） | AKID（指向 PAA 的 SKID） |
| **DAC** | PAI Subject | CN=..., VID=..., PID=... | AKID（指向 PAI 的 SKID） |

**证书链验证的核心依赖**：
1. **AKID → SKID 链**：DAC.AKID → PAI.SKID，PAI.AKID → PAA.SKID
2. **数字签名链**：每级证书的签名由上级私钥签署
3. **身份信息一致性**：VID/PID 在整个链中保持一致

---

## 五、生产部署注意事项

1. **DAC 唯一性**：每台设备必须有唯一的 DAC 和公私钥对，不能多设备共享
2. **私钥保护**：DAC 私钥应在安全环境中生成（如设备内部生成 CSR 或 HSM 生成后安全注入），生产后销毁外部副本
3. **PAA 离线保存**：PAA 私钥应保持离线/气隙状态，仅用于签发 PAI 证书
4. **DCL 注册**：生产用 PAA 证书必须在 DCL 中注册，Commissioner 才能信任