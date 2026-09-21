# Matter 指令速查

> 用途：看 log 时对照确认每条指令（协议消息 / cluster 命令）的 ID、方向、用途。
> 依据：`spec`（Matter Specification **R1.5**, Doc 23-27349）为权威；[commissioning-attestation.md](attestation/commissioning-attestation.md)（chip-tool 完整配网+认证 log）为实际样本；格式参考 [ota-flow-parse.md](ota/ota-flow-parse.md)。
> 所有 ID 与章节号均已逐一对照 spec 核实，其中 OTA cluster ID 以本机真实 OTA log 交叉验证。

---

## 1. 协议层消息类型（`Type XXXX:YY`）

log 行格式：`[EM] <<< [E:38762i S:0 M:23679077] (U) Msg TX ... --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)`

方向判读：`<<<` = 本端 TX，`>>>` = 本端 RX；`(S)` = 走加密会话（PASE/CASE 已建立），`(U)` = 未加密（握手阶段）。
`(E:38762i)` = Exchange ID（一次请求-响应事务），`S:` = Session ID，`M:` = Message Counter。

### 1.1 Protocol 0x0000 — Secure Channel（spec §4.11.1, Table 18）

| Opcode | 消息 | 用途 | log 样例 |
| :--- | :--- | :--- | :--- |
| **0x00** | `MsgCounterSyncReq` | 消息计数器同步请求 | `Type 0000:00` |
| **0x01** | `MsgCounterSyncRsp` | 计数器同步响应 | `Type 0000:01` |
| **0x10** | `MRP Standalone Ack` | 无数据可捎带时的独立可靠传输确认 | `Type 0000:10 (SecureChannel:StandaloneAck)` |
| **0x20** | `PBKDFParamRequest` | 发起 PASE（携带 Passcode-Id、nonce） | `Type 0000:20` |
| **0x21** | `PBKDFParamResponse` | 返回 PBKDF 参数（迭代次数、salt） | `Type 0000:21` |
| **0x22** | `PASE_Pake1` | SPAKE2+ 第 1 轮 | `Type 0000:22` |
| **0x23** | `PASE_Pake2` | SPAKE2+ 第 2 轮 | `Type 0000:23` |
| **0x24** | `PASE_Pake3` | SPAKE2+ 第 3 轮（完成） | `Type 0000:24` |
| **0x30** | `CASE_Sigma1` | 发起 CASE（携带 NOC 链目标 Fabric） | `Type 0000:30` |
| **0x31** | `CASE_Sigma2` | CASE 第 2 轮（返回设备 NOC+签名） | `Type 0000:31` |
| **0x32** | `CASE_Sigma3` | CASE 第 3 轮（发起方 NOC+签名） | `Type 0000:32` |
| **0x33** | `CASE_Sigma2Resume` | 会话恢复的优化 Sigma2 | `Type 0000:33` |
| **0x40** | `StatusReport` | 子协议结束状态（PASE/CASE 成功=1/2） | `Type 0000:40` |
| **0x50** | `ICD Check-In` | ICD 设备主动上线报文 | `Type 0000:50` |

配网 log 中的顺序：PASE = `20→21→22→23→24→40`（BLE 上）；CASE = `30→10→31→32→10→40`（Thread UDP 上）。

### 1.2 Protocol 0x0001 — Interaction Model（spec §10.2.1）

| Opcode | 消息 | 用途 | log 样例 |
| :--- | :--- | :--- | :--- |
| **0x01** | `StatusResponseMessage` | 通用状态应答（如 Subscribe 确认） | `Type 0001:01` |
| **0x02** | `ReadRequestMessage` | 读属性/事件请求 | `Type 0001:02 (IM:ReadRequest)` |
| **0x03** | `SubscribeRequestMessage` | 订阅请求 | `Type 0001:03` |
| **0x04** | `SubscribeResponseMessage` | 订阅应答 | `Type 0001:04` |
| **0x05** | `ReportDataMessage` | 属性/事件上报（Read 应答或订阅推送） | `Type 0001:05 (IM:ReportData)` |
| **0x06** | `WriteRequestMessage` | 写属性请求 | `Type 0001:06` |
| **0x07** | `WriteResponseMessage` | 写属性应答 | `Type 0001:07` |
| **0x08** | `InvokeRequestMessage` | **调用 cluster 命令**（见第 3 节） | `Type 0001:08 (IM:InvokeCommandRequest)` |
| **0x09** | `InvokeResponseMessage` | 命令执行结果 | `Type 0001:09 (IM:InvokeCommandResponse)` |
| **0x0A** | `TimedRequestMessage` | Timed 事务握手（防中间人重放） | `Type 0001:0A` |

### 1.3 Protocol 0x0002 — BDX 文件传输（spec §11.22.3.1, Table 108）

OTA 镜像等大文件传输。注意：**0x13 = BlockAck，0x14 = BlockAckEOF**（ota-flow-parse.md 中 0x14 标成 BlockAckEOF 是笔误）。

| Opcode | 消息 | 用途 |
| :--- | :--- | :--- |
| **0x01** | `SendInit` | 发送方发起传输 |
| **0x02** | `SendAccept` | 接受 SendInit |
| **0x04** | `ReceiveInit` | 接收方发起传输（OTA 下载用这个） |
| **0x05** | `ReceiveAccept` | 发送方接受接收请求 |
| **0x10** | `BlockQuery` | 请求下一个数据块 |
| **0x11** | `Block` | 数据块 |
| **0x12** | `BlockEOF` | 最后一个数据块 |
| **0x13** | `BlockAck` | 块确认 |
| **0x14** | `BlockAckEOF` | 最终块确认（传输结束） |
| **0x15** | `BlockQueryWithSkip` | 带偏移跳过的块请求（断点续传） |

---

## 2. Commissioning 全流程 ↔ 指令对照

来自 commissioning-attestation.md 的真实序列（`pairing ble-thread`，含设备认证）。
流程定位关键字：`Commissioning stage next step: 'A' -> 'B'`、`Starting commissioning stage 'B'`。

| # | 阶段（log 关键字） | 传输 | 发出的指令 | 收到的应答 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | SecurePairing | BLE 未加密 | `0000:20/22/24` PASE | `0000:21/23/40`；log: `PASE establishment successful` |
| 2 | ReadCommissioningInfo | BLE PASE 会话 | `0001:02` ReadRequest（EP0：0x28 / 0x30 / 0x31 / 0x3E 属性） | `0001:05` ReportData（含 UNSUPPORTED_ATTRIBUTE 忽略即可） |
| 3 | ArmFailSafe | BLE | **0x30/0x00 ArmFailSafe**（60s） | 0x30/0x01 ArmFailSafeResponse |
| 4 | ConfigRegulatory | BLE | **0x30/0x02 SetRegulatoryConfig** | 0x30/0x03 |
| 5 | ConfigureTCAcknowledgments | — | （设备不支持时自动跳过） | — |
| 6 | SendPAICertificateRequest | BLE | **0x3E/0x02 CertificateChainRequest**（CertificateType=1 PAI） | 0x3E/0x03 CertificateChainResponse（PAI 证书 DER） |
| 7 | SendDACCertificateRequest | BLE | **0x3E/0x02**（CertificateType=2 DAC） | 0x3E/0x03（DAC 证书 DER） |
| 8 | SendAttestationRequest | BLE | **0x3E/0x00 AttestationRequest**（nonce） | 0x3E/0x01 AttestationResponse（AttestationElements+签名）；随后本地 AttestationVerification（PAA 验签）/ AttestationRevocationCheck |
| 9 | SendOpCertSigningRequest | BLE | **0x3E/0x04 CSRRequest**（CSR nonce） | 0x3E/0x05 CSRResponse（NOCSR 元素）；本地 ValidateCSR / GenerateNOCChain |
| 10 | SendTrustedRootCert | BLE | **0x3E/0x0B AddTrustedRootCertificate** | **无应答命令**（成功标志是下一条 AddNOC 正常执行） |
| 11 | SendNOC | BLE | **0x3E/0x06 AddNOC**（NOC+ICAC，配网会话切换到新 fabric） | 0x3E/0x08 NOCResponse（StatusCode=0 SUCCESS） |
| 12 | ThreadNetworkSetup | BLE | **0x31/0x03 AddOrUpdateThreadNetwork**（Dataset） | 0x31/0x05 NetworkConfigResponse |
| 13 | FailsafeBeforeThreadEnable | BLE | **0x30/0x00 ArmFailSafe**（重挂，900s） | 0x30/0x01 |
| 14 | ThreadNetworkEnable | BLE | **0x31/0x06 ConnectNetwork**（NetworkID） | 0x31/0x07 ConnectNetworkResponse（networkingStatus=0） |
| 15 | FindOperationalForStayActive | Thread 未加密 | `0000:30/31/32` CASE + `0000:10` Ack | `0000:40` StatusReport；此后走 CASE 加密会话 |
| 16 | ICDSendStayActive | — | （非 ICD 设备自动跳过） | — |
| 17 | SendComplete | Thread CASE | **0x30/0x04 CommissioningComplete** | 0x30/0x05 CommissioningCompleteResponse；log: `Device commissioning completed with success` |

命令应答定位行：`Received Command Response Data, Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0001`（此后一行是 `[CTL]` 的语义化结果）。

---

## 3. Cluster 命令速查

通用格式：IM 层面所有命令都包在 `0001:08 InvokeCommandRequest`（请求）/ `0001:09 InvokeCommandResponse`（应答）里，内层 `CommandPathIB = {EndpointId, ClusterId, CommandId}` 定位具体命令。
方向标记：`⇒` client→server（控制端发给设备），`⇐` server→client（设备应答）。

### 3.1 配网核心 4 个 cluster

**General Commissioning 0x0030**（spec §11.10，EP0）

| Cmd | 名称 | 方向 | 用途 |
| :--- | :--- | :--- | :--- |
| 0x00 | ArmFailSafe | ⇒ | 武装 fail-safe 定时器（超时自动回滚所有配网改动）；重挂用于延长 |
| 0x01 | ArmFailSafeResponse | ⇐ | errorCode（0=OK）+ DebugText |
| 0x02 | SetRegulatoryConfig | ⇒ | 设置地区/法规配置 |
| 0x03 | SetRegulatoryConfigResponse | ⇐ | errorCode |
| 0x04 | CommissioningComplete | ⇒ | 配网收尾（必须在 CASE 会话上发；解除 fail-safe） |
| 0x05 | CommissioningCompleteResponse | ⇐ | errorCode |
| 0x06 | SetTCAcknowledgements | ⇒ | 条款确认（R1.5 新增，多数设备不支持则跳过） |
| 0x07 | SetTCAcknowledgementsResponse | ⇐ | 应答 |

**Network Commissioning 0x0031**（spec §11.9，EP0；Feature 位：WI=WiFi / TH=Thread）

| Cmd | 名称 | 方向 | 用途 |
| :--- | :--- | :--- | :--- |
| 0x00 | ScanNetworks | ⇒ | 扫描周边网络（需 fail-safe，否则 FAILSAFE_REQUIRED） |
| 0x01 | ScanNetworksResponse | ⇐ | 扫描结果（ThreadDiscovery/WiFiScan 结果表） |
| 0x02 | AddOrUpdateWiFiNetwork | ⇒ | 写入 WiFi 凭据（SSID+PSK） |
| 0x03 | AddOrUpdateThreadNetwork | ⇒ | 写入 Thread Operational Dataset |
| 0x04 | RemoveNetwork | ⇒ | 删除网络配置 |
| 0x05 | NetworkConfigResponse | ⇐ | 0x02/0x03/0x04/0x08 的统一应答（networkingStatus + DebugText） |
| 0x06 | ConnectNetwork | ⇒ | 连接已写入的网络（此步设备切换到操作网络） |
| 0x07 | ConnectNetworkResponse | ⇐ | networkingStatus（0=Success）+ ConnectedNetworkID |
| 0x08 | ReorderNetwork | ⇒ | 调整网络优先级 |

**Operational Credentials 0x003E**（spec §11.18，EP0 —— 设备认证/证书核心 cluster）

| Cmd | 名称 | 方向 | 用途 |
| :--- | :--- | :--- | :--- |
| 0x00 | AttestationRequest | ⇒ | 请求认证声明（带 AttestationNonce）；设备返回 DAC 签名的 AttestationElements |
| 0x01 | AttestationResponse | ⇐ | AttestationElements（含 certification declaration）+ DAC 签名 → commissioner 用 PAA 验签 |
| 0x02 | CertificateChainRequest | ⇒ | 请求证书链（CertificateType：1=PAI，2=DAC） |
| 0x03 | CertificateChainResponse | ⇐ | 证书 DER |
| 0x04 | CSRRequest | ⇒ | 请求生成密钥对+CSR（带 CSRNonce）；私钥不出设备 |
| 0x05 | CSRResponse | ⇐ | NOCSR 元素（公钥+签名）；commissioner 据此签发 NOC |
| 0x06 | AddNOC | ⇒ | 灌入新 fabric 的 NOC（可选 ICAC）；成功后设备具备操作身份 |
| 0x07 | UpdateNOC | ⇒ | 替换当前 fabric 的 NOC（如换 ICAC/Root） |
| 0x08 | NOCResponse | ⇐ | 0x06/0x07/0x09/0x0A 的统一应答（StatusCode/FabricIndex） |
| 0x09 | UpdateFabricLabel | ⇒ | 改 fabric 标签名 |
| 0x0A | RemoveFabric | ⇒ | 删除 fabric（自助退网） |
| 0x0B | AddTrustedRootCertificate | ⇒ | 灌入 RCAC（信任根）；**无应答** |
| 0x0C/0x0D/0x0E | SetVIDVerificationStatement / SignVIDVerificationRequest / Response | — | R1.5 VID 验证声明（少见） |

**Basic Information 0x0028**（spec §11.1，EP0；无命令，只读属性）

属性读取阶段（ReadCommissioningInfo）最常见：`Cluster = 0x28, Attribute = 0x0000_0002` → VendorID，`0x0000_0004` → ProductID。详见第 4 节。

### 3.2 OTA 软件升级

**OTA Provider 0x0029**（spec §11.20.6）—— 存镜像的一端（本机 OTA log 已交叉验证）

| Cmd | 名称 | 方向 | 用途 |
| :--- | :--- | :--- | :--- |
| 0x00 | QueryImage | ⇒ | 请求方问"有没有新固件"（带 VID/PID/SoftwareVersion/ProtocolsSupported） |
| 0x01 | QueryImageResponse | ⇐ | Status：0=UpdateAvailable（带 URI）、1=Busy、2=NotAvailable（可带 UpdateToken/用户同意标志） |
| 0x02 | ApplyUpdateRequest | ⇐ | 请求方下载完成后问"现在能重启吗" |
| 0x03 | ApplyUpdateResponse | ⇐ | Action：0=Proceed（到时间可重启）/1=AwaitNextAction/2=Discontinue |
| 0x04 | NotifyUpdateApplied | ⇐ | 请求方告知新版本已生效（更新流程闭环） |

**OTA Requestor 0x002A**（spec §11.20.7）—— 跑在设备上的请求方

| Cmd | 名称 | 方向 | 用途 |
| :--- | :--- | :--- | :--- |
| 0x00 | AnnounceOTAProvider | ⇒ | 管理端广播 Provider 地址，触发请求方发起查询 |

镜像本体走 **BDX 0x0002**（见 1.3）。完整时序：QueryImage → BDX ReceiveInit/ReceiveAccept → BlockQuery/Block…→ BlockEOF/BlockAckEOF → ApplyUpdateRequest → ApplyUpdateResponse → NotifyUpdateApplied。

### 3.3 管理与诊断

| Cluster | 名称（spec 章节） | 命令 |
| :--- | :--- | :--- |
| 0x001F | Access Control（§9.10） | 0x00 ReviewFabricRestrictions ⇒，0x01 …Response ⇐（ARL 限制复审） |
| 0x0032 | Diagnostic Logs（§11.11） | 0x00 RetrieveLogsRequest ⇒，0x01 RetrieveLogsResponse ⇐（BDX/ResponsePayload 拉日志） |
| 0x0033 | General Diagnostics（§11.12） | 0x00 TestEventTrigger ⇒（调试钩子）、0x01 TimeSnapshot ⇒ / 0x02 …Response ⇐、0x03 PayloadTestRequest（DMTEST） |
| 0x0034 | Software Diagnostics（§11.13） | 0x00 ResetWatermarks ⇒（清内存高水位） |
| 0x0035 | Thread Network Diagnostics（§11.14） | 0x00 ResetCounts ⇒ |
| 0x0036 | Wi-Fi Network Diagnostics（§11.15） | 0x00 ResetCounts ⇒ |
| 0x0037 | Ethernet Network Diagnostics（§11.16） | 0x00 ResetCounts ⇒ |
| 0x003C | Administrator Commissioning（§11.19） | 0x00 OpenCommissioningWindow ⇒（ECM，带随机 Passcode）、0x01 OpenBasicCommissioningWindow ⇒、0x02 RevokeCommissioning ⇒（同时只允许一个窗口） |
| 0x003F | Group Key Management（§11.2） | 0x00 KeySetWrite ⇒、0x01 KeySetRead ⇒（0x02 Resp）、0x03 KeySetRemove ⇒、0x04 KeySetReadAllIndices ⇒（0x05 Resp） |
| 0x0046 | ICD Management（§9.16） | 0x00 RegisterClient ⇒（0x01 Resp）、0x02 UnregisterClient ⇒、0x03 StayActiveRequest ⇒（0x04 Resp）；配网中 `ICDSendStayActive` 阶段对非 ICD 设备自动跳过 |
| 0x0038 | Time Synchronization（§11.17） | 0x00 SetUTCTime ⇒、0x01 SetTrustedTimeSource ⇒、0x02 SetTimeZone ⇒（0x03 Resp）、0x04 SetDSTOffset ⇒ |
| 0x001D | Descriptor（§9.5） | 无命令；读 Attributes（DeviceTypeList/ServerList/ClientList/PartsList）可看端点构成 |
| 0x000E | Actions（§9.14） | 0x00 InstantAction 等场景触发（桥接设备常见） |
| 0x000B | Bridged Device Basic Information（§9.13） | 0x00 KeepActive ⇒（桥接设备保活） |

### 3.4 设备控制类（ZCL Device Library 规范，不在本 Core spec 内，ID 为标准 ZCL 值）

| Cluster | 名称 | 常用命令 |
| :--- | :--- | :--- |
| 0x0003 | Identify | 0x00 Identify ⇒、0x01 IdentifyQuery（遗留）、0x40 TriggerEffect ⇒（闪灯等效果） |
| 0x0004 | Groups | 0x00 AddGroup、0x01 ViewGroup、0x02 GetGroupMembership、0x03 RemoveGroup、0x04 RemoveAllGroups、0x05 AddIfIdentifying |
| 0x0006 | OnOff | 0x00 Off、0x01 On、0x02 Toggle、0x40 OffWithEffect、0x41 OnWithRecallGlobalScene、0x42 OnWithTimedOff |
| 0x0008 | Level Control | 0x00 MoveToLevel、0x01 Move、0x02 Step、0x03 Stop；0x04-0x07 为对应 *WithOnOff 变体 |

---

## 4. 常用属性 ID 速查

log 定位：ReportData 里的 `AttributePathIB = {Endpoint, Cluster, Attribute = 0x0000_XXXX}`。

**全局属性**（所有 cluster 都有，spec §8.2.8 / 通配展开规则）：

| ID | 名称 | 用途 |
| :--- | :--- | :--- |
| 0xFFF8 | GeneratedCommandList | 本 cluster 会产生的命令 ID 列表 |
| 0xFFF9 | AcceptedCommandList | 本 cluster 接受的命令 ID 列表（查"支持哪些命令"最快） |
| 0xFFFA | EventList | 事件列表 |
| 0xFFFB | AttributeList | 属性列表 |
| 0xFFFC | FeatureMap | Feature 位图（如 NetComm 的 WI/TH 位） |
| 0xFFFD | ClusterRevision | cluster 版本号 |

**Basic Information 0x0028**（§11.1.5）：0x00 DataModelRevision、0x01 VendorName、0x02 VendorID、0x03 ProductName、0x04 ProductID、0x05 NodeLabel、0x06 Location、0x07/0x08 HardwareVersion(String)、0x09/0x0A SoftwareVersion(String)、0x0B ManufacturingDate、0x0C PartNumber、0x0F SerialNumber、0x12 Reachable、0x13 UniqueID、0x14 CapabilityMinima

**General Commissioning 0x0030**（§11.10.6）：0x00 Breadcrumb、0x01 BasicCommissioningInfo（{FailSafeExpiryLength, MaxCumulativeFailsafeSeconds}，log 中 {60,900}）、0x02 RegulatoryConfig、0x03 LocationCapability、0x04 SupportsConcurrentConnection、0x05-0x0A TC 条款相关

**Network Commissioning 0x0031**（§11.9.6）：0x00 MaxNetworks、0x01 Networks（已存网络表）、0x02 ScanMaxTimeSeconds、0x03 ConnectMaxTimeSeconds、0x04 InterfaceEnabled、0x05 LastNetworkingStatus、0x06 LastNetworkID、0x07 LastConnectErrorValue（连接失败时先看 0x05/0x06/0x07）

**Operational Credentials 0x003E**（§11.18.5）：0x00 NOCs、0x01 Fabrics（fabric 表：NodeId/VendorId/FabricId/Label）、0x02 SupportedFabrics、0x03 CommissionedFabrics、0x04 TrustedRootCertificates、0x05 CurrentFabricIndex

**Access Control 0x001F**（§9.10.6）：0x00 ACL、0x01 Extension、0x02 SubjectsPerAccessControlEntry、0x03 TargetsPerAccessControlEntry、0x04 AccessControlEntriesPerFabric

---

## 5. Log 定位技巧与状态码

### 5.1 grep 速查

| 想确认什么 | grep |
| :--- | :--- |
| 某条协议消息收发 | `grep "Type 0001:08"`（替换成目标 Opcode） |
| 某命令的请求/应答 ID | `grep "Received Command Response Data"` |
| 命令路径（Invoke 内层） | `grep -A4 "CommandPathIB"`（看 ClusterId/CommandId） |
| 读到的属性 | `grep -B8 "Data = " | grep Attribute`（或直接看 `AttributePathIB`） |
| 配网走到哪一步 | `grep "Commissioning stage next step"` |
| 配网失败点 | `grep -E "failed|error|FAIL|Abort"`（看 `Successfully finished commissioning step` 断在哪） |
| 某属性为何报错 | `grep "StatusIB" -A2`（看 status 码） |

### 5.2 全局状态码（spec §8.10.1 Status Code Table）

StatusIB 打印格式：`status = 0x86 (UNSUPPORTED_ATTRIBUTE)`。

| 值 | 名称 | 含义 |
| :--- | :--- | :--- |
| 0x00 | SUCCESS | 成功 |
| 0x01 | FAILURE | 通用失败 |
| 0x80 | UNSUPPORTED_ACCESS | 无权限/访问被拒 |
| 0x81 | UNSUPPORTED_ENDPOINT | 端点不存在 |
| 0x82 | INVALID_ACTION | 动作格式错误 |
| 0x83 | UNSUPPORTED_COMMAND | 命令 ID 不支持（查 AcceptedCommandList） |
| 0x84 | INVALID_COMMAND | 命令字段畸形 |
| 0x86 | UNSUPPORTED_ATTRIBUTE | 属性不存在（配网探测性读取时常见，可忽略） |
| 0x87 | CONSTRAINT_ERROR | 值超范围/非法（写入被拒但保留旧值） |
| 0x88 | UNSUPPORTED_WRITE | 写只读属性 |
| 0x89 | RESOURCE_EXHAUSTED | 资源不足 |
| 0x8A | NOT_FOUND | 找不到数据字段/条目 |
| 0x92 | DATA_VERSION_MISMATCH | 数据版本不匹配（条件写） |
| 0x94 | TIMEOUT | Timed 事务超时 |
| 0x9C | BUSY | 设备忙 |
| 0xC3 | UNSUPPORTED_CLUSTER | cluster 不支持（配网探测常见；本例 log 中 0x46 即如此） |
| 0xC6 | NEEDS_TIMED_INTERACTION | 需要 Timed Write/Invoke |
| 0xC8 | PATHS_EXHAUSTED | 路径数超限 |
| 0xC9 | TIMED_REQUEST_MISMATCH | TimedRequest 标志与事务不符 |
| 0xCA | FAILSAFE_REQUIRED | 需要先 ArmFailSafe（如 ScanNetworks 未挂 fail-safe 就发） |
| 0xCB | INVALID_IN_STATE | 当前设备状态不接受该请求 |

### 5.3 常见易混点

- **两轮 ArmFailSafe**（阶段 3 和 13）是正常的：第一轮保护配网前半程，`FailsafeBeforeThreadEnable` 阶段重挂并延长到 MaxCumulativeFailsafeSeconds（本例 900s）。
- **CertificateChainRequest 发两次**（阶段 6/7）：CertificateType=1 取 PAI、=2 取 DAC，都是同一个命令 ID 0x02。
- **AddTrustedRootCertificate 没有应答**：log 里只有 `0001:08` 没有 `0001:09`，不是丢包；下一阶段的 AddNOC 成功即说明 RCAC 已收下。
- **AddNOC 之后传输切换**：AddNOC 使配网会话关联到新 fabric，后续 CommissioningComplete 必须走 CASE（Thread/Ethernet），不再走 BLE PASE。
- **`Type 0000:10` StandaloneAck 大量出现**是 MRP 可靠传输的正常行为，尤其在 BLE/UDP 上，不是重传风暴。
- **`(U)` 报文上出现 IM 命令**（`0001:08` in unencrypted）才是异常；正常业务命令都在 `(S)` 加密会话上。
