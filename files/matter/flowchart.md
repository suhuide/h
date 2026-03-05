```mermaid
sequenceDiagram
    participant Commissioner
    participant Commissionee

    Note over Commissioner, Commissionee: Phase 0: Preparation(Spec. Steps 1)

    Commissioner->>Commissioner: 1.初始化，加载/创建 Fabric
    Note left of Commissioner: [CTL] Generating RCAC/ICAC/NOC<br/>[FP] Added new fabric at index: 0x1, Assigned compressed fabric and node ID

    Commissionee->>Commissionee: 1.设备启动，初始化Matter堆栈
    Note right of Commissionee: [DL] Init CHIP Stack, Setting device name to : "SL-Window"

    Commissionee->>Commissionee: 打开 commissioning 窗口 (BLE广播)
    Note right of Commissionee: [DL] Starting advertising... [SVR] SetupQRCode: [MT:...]

    Note over Commissioner, Commissionee: Phase 1: Device discovery and establish commissioning channel(Spec. Steps 2)

    Commissioner->>Commissioner: BLE scan, search for target devcie

    Commissioner->>+Commissionee: BLE discovery(Discriminator match. Attempting to connect)
    Note left of Commissioner: [BLE] Device discriminator match. Attempting to connect.

    Commissionee-->>Commissioner: BLE connection establish
    Note right of Commissionee: [DL] sl_bt_evt_connection_opened_id
    Note left of Commissioner: [BLE] New device connected: CC:C0:BF:C1:8D:CE

    Commissioner->>Commissioner: 连接完成，准备发现服务

    Commissioner->>Commissionee: 2.发现并订阅Matter服务与特征值
    Note left of Commissioner: [DL] CHIP service found, Valid C1/C2 characteristic found

    Commissionee-->>Commissioner: 2.订阅成功确认
    Note right of Commissionee: [DL] CHIPoBLE subscribe received, _OnPlatformEvent kCHIPoBLESubscribe(BLEManagerImpl.cpp)

    Note over Commissioner, Commissionee: **BLE Commissioning channel established**


    Note over Commissioner, Commissionee: Phase 2: Security setup using PASE(Spec. Steps 3,4,5,6,7,8)

    Commissioner->>Commissionee: 3. PBKDFParamRequest (请求安全参数)
    Note left of Commissioner: [EM] Msg TX ... Type 0000:20 (SecureChannel:PBKDFParamRequest)

    Commissionee-->>Commissioner: 4. PBKDFParamResponse (回复参数)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:20 (PBKDFParamRequest)<br/>[EM] <<< Msg TX ... Type 0000:21 (PBKDFParamResponse)<br/>[SVR] Commissioning session establishment step started

    Commissioner->>Commissionee: 5. PASE_Pake1 (Spake2+ 消息1)
    Note left of Commissioner: [EM] Msg TX ... Type 0000:22 (SecureChannel:PASE_Pake1)<br/>[SC] Sent spake2p msg1

    Commissionee-->>Commissioner: 6. PASE_Pake2 (Spake2+ 消息2)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:22 (PASE_Pake1)<br/>[EM] <<< Msg TX ... Type 0000:23 (PASE_Pake2)

    Commissioner->>Commissionee: 7. PASE_Pake3 (Spake2+ 消息3)
    Note left of Commissioner: [EM] Msg TX ... Type 0000:24 (SecureChannel:PASE_Pake3)<br/>[SC] Sent spake2p msg3

    Commissionee->>Commissionee: 验证PASE_Pake3，计算共享密钥
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:24 (PASE_Pake3)

    Commissionee-->>Commissioner: 8. StatusReport (报告成功状态)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0000:40 (StatusReport)<br/>[SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'<br/>[SVR] Commissioning completed session establishment step

    Commissioner->>Commissioner: PASE 建立成功
    Note left of Commissioner: [TOO] Pairing Success<br/>[TOO] PASE establishment successful

    Note over Commissioner, Commissionee: **PASE secure channel have established，All messages encrypted with PASE-derived encryption keys**


    Note over Commissioner, Commissionee: Phase 3: Configure information(Spec. Steps 9,10)

    Commissioner->>Commissionee: 9. ReadRequest (请求基本信息)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'<br/>[DMG] SendReadRequest ... Sending Read Request

    Commissionee-->>Commissioner: ReportData (返回基本信息)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:02 (IM:ReadRequest)<br/>[EM] <<< Msg TX ... Type 0001:05 (IM:ReportData)

    Commissioner->>Commissioner: 解析设备基本信息
    Note left of Commissioner: [DMG] (解析VendorID/ProductID等)<br/>[SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010

    Commissioner->>Commissionee: 10. InvokeCommandRequest (ArmFailSafe, 开启60s fail-safe) 7?
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'<br/>[CTL] Arming failsafe (60 seconds)

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received ArmFailSafe (60s)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: InvokeCommandRequest (SetRegulatoryConfig, 设置区域配置) 8?
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'<br/>[CTL] Setting Regulatory Config

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)


    Note over Commissioner, Commissionee: Phase 4: Commissionee Attestation(Spec. Step 10)

    Commissioner->>Commissionee: 11a. InvokeCommandRequest (CertificateChainRequest, 请求PAI证书)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'SendPAICertificateRequest'<br/>[CTL] Sending request for PAI certificate

    Commissionee-->>Commissioner: InvokeCommandResponse (返回PAI证书)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Certificate Chain request received for PAI<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: 11b. InvokeCommandRequest (CertificateChainRequest, 请求DAC证书)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'<br/>[CTL] Sending request for DAC certificate

    Commissionee-->>Commissioner: InvokeCommandResponse (返回DAC证书)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Certificate Chain request received for DAC<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: 11c. InvokeCommandRequest (AttestationRequest, 请求认证信息)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'<br/>[CTL] Sending Attestation Request to the device.

    Commissionee->>Commissionee: 生成认证信息，并用DAC私钥签名
    Note right of Commissionee: [ZCL] OpCreds: Received an AttestationRequest command<br/>[DL] SignWithDeviceAttestationKey...<br/>[ZCL] OpCreds: AttestationRequest successful.

    Commissionee-->>Commissioner: InvokeCommandResponse (返回Attestation信息及签名)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissioner: 验证Attestation信息、证书链和签名
    Note left of Commissioner: [CTL] Verifying Device Attestation information...<br/>[-] (打印DAC/PAI/PAA证书详情)<br/>[CTL] Successfully validated 'Attestation Information' command


    Note over Commissioner, Commissionee: Phase 5: Operational CSR exchange/Generate Operational Certificate(Spec. Steps 12,13) 11?

    Commissioner->>Commissionee: 12. InvokeCommandRequest (CSRRequest, 请求证书签名请求) 11?
    Note left of Commissioner: [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'<br/>[CTL] Sending CSR request to device

    Commissionee->>Commissionee: 生成NOCSR并用DAC私钥签名
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received a CSRRequest command<br/>[ZCL] OpCreds: AllocatePendingOperationalKey succeeded<br/>[DL] SignWithDeviceAttestationKey...<br/>[ZCL] OpCreds: CSRRequest successful.

    Commissionee-->>Commissioner: InvokeCommandResponse (返回NOCSR及签名)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissioner: 验证CSR，使用CA证书颁发NOC
    Note left of Commissioner: [CTL] Verifying Certificate Signing Request<br/>[CTL] Generating NOC<br/>[CTL] Successfully finished commissioning step 'GenerateNOCChain'

    Commissioner->>Commissionee: 13a. InvokeCommandRequest (AddTrustedRootCertificate, 添加运营网络根证书)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'GenerateNOCChain' -> 'SendTrustedRootCert'<br/>[CTL] Sending root certificate to the device

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received an AddTrustedRootCertificate command<br/>[ZCL] OpCreds: AddTrustedRootCertificate successful.<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: 13b. InvokeCommandRequest (AddNOC, 添加NOC和ICAC)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'<br/>[CTL] Sent operational certificate to the device

    Commissionee->>Commissionee: 验证NOC链，存储运营身份，创建Fabric
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received an AddNOC command<br/>[FP] Validating NOC chain<br/>[FP] NOC chain validation successful<br/>[FP] Added new fabric at index: 0x1<br/>[FP] Assigned compressed fabric ID: 0x4B6873C4587CC6ED, node ID: 0x00000000000008CA<br/>[ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC

    Commissionee-->>Commissioner: InvokeCommandResponse (成功, 返回NOC索引)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Note over Commissioner, Commissionee: **运营身份(Operational Identity)已安装<br/>(Configure information: Operational Certificate)**


    Note over Commissioner, Commissionee: Phase 6: Configure/Join operational network(Spec. Steps 14,15,16,17)

    Commissioner->>Commissionee: 14-15. InvokeCommandRequest (AddOrUpdateThreadNetwork, 添加Thread网络凭据)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'<br/>[CTL] Configure information: operational network

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: 16. InvokeCommandRequest (ArmFailSafe, 启用更长时效的fail-safe)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'<br/>[CTL] Arming failsafe (164 seconds)

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received ArmFailSafe (164s)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissionee: 17. InvokeCommandRequest (ConnectNetwork, 连接到Thread网络)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'<br/>[CTL] Trigger joining of operational network at Commissionee

    Commissionee->>Commissionee: 启动Thread网络连接
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[DL] SRP Client was started...<br/>[DIS] Advertise operational node ...<br/>[SVR] Server initialization complete

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Note over Commissioner, Commissionee: **设备加入运营网络 (Device joined operational network)**


    Note over Commissioner, Commissionee: Phase 7: Commissioning channel terminated(Spec. Step 18)

    Note over Commissioner, Commissionee: 18. BLE配网通道关闭 (BLE connection closed)
    Note right of Commissionee: [DL] Disconnect Event for CHIPoBLE on handle : 1<br/>(连接将在稍后关闭)


    Note over Commissioner, Commissionee: Phase 8: Operational discovery / Security setup using CASE(Spec. Steps 19,20)

    Commissioner->>Commissioner: 清除旧的PASE会话
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'<br/>[IN] Expiring all sessions for node

    Commissioner->>Commissioner: 19. 发现设备的运营地址 (Operational discovery)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'<br/>[DIS] Lookup started for 4B6873C4587CC6ED-00000000000008CA<br/>[DIS] Updating device address to UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540

    Commissioner->>Commissionee: 20a. 发起CASE握手 (Sigma1) 通过新Thread/IP信道
    Note left of Commissioner: [IN] Initiating session on local FabricIndex 1<br/>[EM] Msg TX ... Type 0000:30 (SecureChannel:CASE_Sigma1)<br/>[SC] Sent Sigma1 msg to <00000000000008CA, 1>

    Commissionee-->>Commissioner: 20b. CASE_Sigma2
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:30 (CASE_Sigma1)<br/>[IN] CASE Server received Sigma1 message. Starting handshake.<br/>[SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA<br/>[EM] <<< Msg TX ... Type 0000:31 (CASE_Sigma2)

    Commissioner->>Commissionee: 20c. CASE_Sigma3
    Note left of Commissioner: [EM] Msg TX ... Type 0000:32 (SecureChannel:CASE_Sigma3)<br/>[SC] Sent Sigma3 msg

    Commissionee->>Commissionee: 验证Sigma3，计算共享密钥
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:32 (CASE_Sigma3)<br/>[SC] Received Sigma3 msg

    Commissionee-->>Commissioner: 20d. StatusReport (报告成功状态)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0000:40 (StatusReport)<br/>[SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'<br/>[IN] CASE Session established to peer: <000000000001B669, 1>

    Commissioner->>Commissioner: CASE 建立成功
    Note left of Commissioner: [SC] Success status report received. Session was established<br/>[SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'

    Note over Commissioner, Commissionee: **CASE安全通道已建立，所有消息使用CASE派生密钥加密<br/>(All messages encrypted with CASE-derived encryption keys)**


    Note over Commissioner, Commissionee: Phase 9: Commissioning complete(Spec. Step 21)

    Commissioner->>Commissionee: 21. InvokeCommandRequest (CommissioningComplete, 通知设备配网完成)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'<br/>[EM] Msg TX ... Type 0001:08 (IM:InvokeCommandRequest)

    Commissionee->>Commissionee: 提交Fabric数据，清理fail-safe
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received CommissioningComplete<br/>[FP] Metadata for Fabric 0x1 persisted to storage.<br/>[TS] Committing Last Known Good Time...<br/>[FS] GeneralCommissioning: Successfully committed pending fabric data<br/>[FS] Fail-safe cleanly disarmed

    Commissionee-->>Commissioner: InvokeCommandResponse (成功)
    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissioner->>Commissioner: 配网完成
    Note left of Commissioner: [CTL] Received CommissioningComplete response, errorCode=0<br/>[CTL] Successfully finished commissioning step 'SendComplete'<br/>[CTL] Commissioning complete for node ID 0x00000000000008CA: success<br/>[TOO] Device commissioning completed with success

    Commissionee->>Commissionee: 关闭BLE连接，进入运营状态
    Note right of Commissionee: [DL] Disconnect Event for CHIPoBLE on handle : 1<br/>[SVR] Commissioning completed successfully

    Note over Commissioner, Commissionee: **设备配网成功，进入运营状态 (Commissioning successfully complete)**
```