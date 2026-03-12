```mermaid
sequenceDiagram
    participant Commissioner
    participant Commissionee

    Note over Commissioner, Commissionee: Phase 0: Preparation (Spec. Step 1)

    Commissioner->>Commissioner: 1. Initialize, load/create Fabric
    Note left of Commissioner: [CTL] Generating RCAC/ICAC/NOC<br/>[FP] Added new fabric at index: 0x1, Assigned compressed fabric and node ID

    Commissionee->>Commissionee: 1. Device starts, initialize Matter stack
    Note right of Commissionee: [DL] Init CHIP Stack, Setting device name to : "SL-Window"

    Commissionee->>Commissionee: Open commissioning window (BLE advertising)
    Note right of Commissionee: [DL] Starting advertising... [SVR] SetupQRCode: [MT:...]

    Note over Commissioner, Commissionee: Phase 1: Device discovery and establish commissioning channel (Spec. Step 2)

    Commissioner->>Commissioner: BLE scan, search for target device

    Note left of Commissioner: [BLE] Device discriminator match. Attempting to connect.
    Commissioner->>+Commissionee: BLE discovery (Discriminator match. Attempting to connect)

    
    Note right of Commissionee: [DL] sl_bt_evt_connection_opened_id
    Commissionee-->>Commissioner: BLE connection established
    Note left of Commissioner: [BLE] New device connected: CC:C0:BF:C1:8D:CE

    Commissioner->>Commissioner: BLE Connection complete, ready to discover services

    Commissioner->>Commissionee: 2. Discover and subscribe to Matter service and characteristics
    Note left of Commissioner: [DL] CHIP service found, Valid C1/C2 characteristic found

    Note right of Commissionee: [DL] CHIPoBLE subscribe received, _OnPlatformEvent kCHIPoBLESubscribe(BLEManagerImpl.cpp)
    Commissionee-->>Commissioner: 2. Subscription success confirmation

    Note over Commissioner, Commissionee: **BLE Commissioning channel established**


    Note over Commissioner, Commissionee: Phase 2: Security setup using PASE (Spec. Step 6)


    Note left of Commissioner: [EM] Msg TX ... Type 0000:20 (SecureChannel:PBKDFParamRequest)
    Commissioner->>Commissionee: 6a. PBKDFParamRequest (request security parameters)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:20 (PBKDFParamRequest)<br/>[EM] <<< Msg TX ... Type 0000:21 (PBKDFParamResponse)<br/>[SVR] Commissioning session establishment step started
    Commissionee-->>Commissioner: 6a. PBKDFParamResponse (reply with parameters)


    Note left of Commissioner: [EM] Msg TX ... Type 0000:22 (SecureChannel:PASE_Pake1)<br/>[SC] Sent spake2p msg1
    Commissioner->>Commissionee: 6b. PASE_Pake1 (Spake2+ message 1)


    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:22 (PASE_Pake1)<br/>[EM] <<< Msg TX ... Type 0000:23 (PASE_Pake2)
    Commissionee-->>Commissioner: 6b. PASE_Pake2 (Spake2+ message 2)


    Note left of Commissioner: [EM] Msg TX ... Type 0000:24 (SecureChannel:PASE_Pake3)<br/>[SC] Sent spake2p msg3
    Commissioner->>Commissionee: 6c. PASE_Pake3 (Spake2+ message 3)

    Commissionee->>Commissionee: Verify PASE_Pake3, compute shared key
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:24 (PASE_Pake3)<br/>[EM] <<< Msg TX ... Type 0000:40 (StatusReport)

    Commissionee-->>Commissioner: 6c. StatusReport (report success status)
    Note right of Commissionee: [SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'<br/>[SVR] Commissioning completed session establishment step

    Commissioner->>Commissioner: PASE established successfully
    Note left of Commissioner: [TOO] Pairing Success<br/>[TOO] PASE establishment successful

    Note over Commissioner, Commissionee: **PASE secure channel established, All messages encrypted with PASE-derived encryption keys**


    Note over Commissioner, Commissionee: Phase 3: Configure information (Spec. Step 7,8)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'SecurePairing' -> 'ReadCommissioningInfo'<br/>[DMG] SendReadRequest ... Sending Read Request
    Commissioner->>Commissionee: ReadRequest (request basic information)
    
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:02 (IM:ReadRequest)<br/>[EM] <<< Msg TX ... Type 0001:05 (IM:ReportData)
    Commissionee-->>Commissioner: ReportData (return basic information)

    Commissioner->>Commissioner: Parse device basic information
    Note left of Commissioner: [DMG] (Parsing VendorID/ProductID etc.)<br/>[SVR] OnReadCommissioningInfo - vendorId=0xFFF1 productId=0x8010<br/>[CTL] Commissioning stage next step: 'ReadCommissioningInfo' -> 'ArmFailSafe'<br/>[CTL] Arming failsafe (60 seconds)
    Commissioner->>Commissionee: 7. InvokeCommandRequest (ArmFailSafe, open 60s fail-safe)


    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received ArmFailSafe (60s)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'ArmFailSafe' -> 'ConfigRegulatory'<br/>[CTL] Setting Regulatory Config
    Commissioner->>Commissionee: 8. InvokeCommandRequest (SetRegulatoryConfig, set regulatory configuration)


    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Note over Commissioner, Commissionee: Phase 4: Commissionee Attestation (Spec. Step 10)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'ConfigRegulatory' -> 'SendPAICertificateRequest'<br/>[CTL] Sending request for PAI certificate
    Commissioner->>Commissionee: 10a. InvokeCommandRequest (CertificateChainRequest, request PAI certificate)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Certificate Chain request received for PAI<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (return PAI certificate)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'<br/>[CTL] Sending request for DAC certificate
    Commissioner->>Commissionee: 10b. InvokeCommandRequest (CertificateChainRequest, request DAC certificate)


    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Certificate Chain request received for DAC<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (return DAC certificate)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'<br/>[CTL] Sending Attestation Request to the device.
    Commissioner->>Commissionee: 10c. InvokeCommandRequest (AttestationRequest, request attestation information)

    Commissionee->>Commissionee: Generate attestation information, sign with DAC private key

    Note right of Commissionee: [ZCL] OpCreds: Received an AttestationRequest command<br/>[DL] SignWithDeviceAttestationKey...<br/>[ZCL] OpCreds: AttestationRequest successful.<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (return Attestation information and signature)

    Commissioner->>Commissioner: Verify Attestation information, certificate chain and signature
    Note left of Commissioner: [CTL] Verifying Device Attestation information...<br/>[-] (Printing DAC/PAI/PAA certificate details)<br/>[CTL] Successfully validated 'Attestation Information' command


    Note over Commissioner, Commissionee: Phase 5: Operational CSR exchange/Generate Operational Certificate (Spec. Step 11,13)


    Note left of Commissioner: [CTL] Commissioning stage next step: 'AttestationRevocationCheck' -> 'SendOpCertSigningRequest'<br/>[CTL] Sending CSR request to device
    Commissioner->>Commissionee: 11. InvokeCommandRequest (CSRRequest, request Certificate Signing Request)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received a CSRRequest command<br/>[ZCL] OpCreds: AllocatePendingOperationalKey succeeded<br/>[DL] SignWithDeviceAttestationKey...<br/>[ZCL] OpCreds: CSRRequest successful.
    Commissionee->>Commissionee: Generate NOCSR and sign with DAC private key

    Note right of Commissionee: [EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (return NOCSR and signature)

    Note left of Commissioner: [CTL] Verifying Certificate Signing Request<br/>[CTL] Generating NOC<br/>[CTL] Successfully finished commissioning step 'GenerateNOCChain'
    Commissioner->>Commissioner: Verify CSR, issue NOC using CA certificate

    Note left of Commissioner: [CTL] Commissioning stage next step: 'GenerateNOCChain' -> 'SendTrustedRootCert'<br/>[CTL] Sending root certificate to the device
    Commissioner->>Commissionee: 13a. InvokeCommandRequest (AddTrustedRootCertificate, add operational network root certificate)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received an AddTrustedRootCertificate command<br/>[ZCL] OpCreds: AddTrustedRootCertificate successful.<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendTrustedRootCert' -> 'SendNOC'<br/>[CTL] Sent operational certificate to the device
    Commissioner->>Commissionee: 13b. InvokeCommandRequest (AddNOC, add NOC and ICAC)

    Commissionee->>Commissionee: Verify NOC chain, store operational identity, create Fabric
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[ZCL] OpCreds: Received an AddNOC command[FP] Validating NOC chain<br/>[FP] NOC chain validation successful [FP] Added new fabric at index: 0x1<br/>[FP] Assigned compressed fabric ID: 0x4B6873C4587CC6ED, node ID: 0x00000000000008CA<br/>[ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissionee-->>Commissioner: InvokeCommandResponse (success, return NOC index)

    Note over Commissioner, Commissionee: **Operational Identity installed (Configure information: Operational Certificate)**
    Note over Commissioner, Commissionee: Phase 6: Configure/Join operational network (Spec. Step 15,16,17.Step 14 can be optional)    
    Note right of Commissionee: 15. [ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0x000000000001B669




    Note left of Commissioner: [CTL] Commissioning stage next step: 'SendNOC' -> 'ThreadNetworkSetup'<br/>[CTL] Configure information: operational network
    Commissioner->>Commissionee: 16. InvokeCommandRequest (AddOrUpdateThreadNetwork, add Thread network credentials)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)


    Note left of Commissioner: [CTL] Commissioning stage next step: 'ThreadNetworkSetup' -> 'FailsafeBeforeThreadEnable'<br/>[CTL] Arming failsafe (164 seconds)
    Commissioner->>Commissionee: ArmFailSafe (enable longer duration fail-safe)

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received ArmFailSafe (164s)<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'<br/>[CTL] Trigger joining of operational network at Commissionee
    Commissioner->>Commissionee: 17. InvokeCommandRequest (ConnectNetwork, connect to Thread network)

    Commissionee->>Commissionee: Start Thread network connection
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[DL] SRP Client was started...[DIS] Advertise operational node ...<br/>[SVR] Server initialization complete<br/>[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)

    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Note over Commissioner, Commissionee: **Device joined operational network**


    Note over Commissioner, Commissionee: Commissioning channel terminated (BLE commissioning channel closed [BLE connection closed])
    Note right of Commissionee: [DL] Disconnect Event for CHIPoBLE on handle : 1<br/>(Connection will close later)


    Note over Commissioner, Commissionee: Phase 7: Operational discovery / Security setup using CASE (Spec. Step 19,20)

    Commissioner->>Commissioner: Clear old PASE session
    Note left of Commissioner: [CTL] Commissioning stage next step: 'ThreadNetworkEnable' -> 'kEvictPreviousCaseSessions'<br/>[IN] Expiring all sessions for node

    Commissioner->>Commissioner: 19. Discover device's operational address (Operational discovery)
    Note left of Commissioner: [CTL] Commissioning stage next step: 'kEvictPreviousCaseSessions' -> 'kFindOperationalForStayActive'<br/>[DIS] Lookup started for 4B6873C4587CC6ED-00000000000008CA<br/>[DIS] Updating device address to UDP:[fd98:42ee:f6b4:1:5c1:cfe:88ed:a143]:5540

    Note left of Commissioner: [IN] Initiating session on local FabricIndex 1<br/>[EM] Msg TX ... Type 0000:30 (SecureChannel:CASE_Sigma1)<br/>[SC] Sent Sigma1 msg to <00000000000008CA, 1>
    Commissioner->>Commissionee: 20a. Initiate CASE handshake (Sigma1) via new Thread/IP channel

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:30 (CASE_Sigma1)<br/>[IN] CASE Server received Sigma1 message. Starting handshake.<br/>[SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA<br/>[EM] <<< Msg TX ... Type 0000:31 (CASE_Sigma2)
    Commissionee-->>Commissioner: 20b. CASE_Sigma2

    Note left of Commissioner: [EM] Msg TX ... Type 0000:32 (SecureChannel:CASE_Sigma3)<br/>[SC] Sent Sigma3 msg
    Commissioner->>Commissionee: 20c. CASE_Sigma3

    Note right of Commissionee: [EM] >>> Msg RX ... Type 0000:32 (CASE_Sigma3)<br/>[SC] Received Sigma3 msg
    Commissionee->>Commissionee: Verify Sigma3, compute shared key

    Note right of Commissionee: [EM] <<< Msg TX ... Type 0000:40 (StatusReport)<br/>[SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'<br/>[IN] CASE Session established to peer: <000000000001B669, 1>
    Commissionee-->>Commissioner: 20d. StatusReport (report success status)

    Commissioner->>Commissioner: CASE established successfully
    Note left of Commissioner: [SC] Success status report received. Session was established<br/>[SC] SecureSession[...]: State change 'kEstablishing' --> 'kActive'

    Note over Commissioner, Commissionee: **CASE secure channel established, All messages encrypted with CASE-derived encryption keys**

    Note over Commissioner, Commissionee: Phase 8: Commissioning complete (Spec. Step 21)

    Note left of Commissioner: [CTL] Commissioning stage next step: 'kFindOperationalForCommissioningComplete' -> 'SendComplete'<br/>[EM] Msg TX ... Type 0001:08 (IM:InvokeCommandRequest)
    Commissioner->>Commissionee: 21. InvokeCommandRequest (CommissioningComplete, notify device commissioning completed)
    Commissionee->>Commissionee: Commit Fabric data, clean up fail-safe
    Note right of Commissionee: [EM] >>> Msg RX ... Type 0001:08 (IM:InvokeCommandRequest)<br/>[FS] GeneralCommissioning: Received CommissioningComplete<br/>[FP] Metadata for Fabric 0x1 persisted to storage.[TS] Committing Last Known Good Time...<br/>[FS] GeneralCommissioning: Successfully committed pending fabric data<br/>[FS] Fail-safe cleanly disarmed.[EM] <<< Msg TX ... Type 0001:09 (IM:InvokeCommandResponse)
    Commissionee-->>Commissioner: InvokeCommandResponse (success)

    Commissioner->>Commissioner: Commissioning complete
    Note left of Commissioner: [CTL] Received CommissioningComplete response, errorCode=0<br/>[CTL] Successfully finished commissioning step 'SendComplete'<br/>[CTL] Commissioning complete for node ID 0x00000000000008CA: success<br/>[TOO] Device commissioning completed with success

    Commissionee->>Commissionee: Enter operational state
    Note right of Commissionee: [SVR] Commissioning completed successfully

    Note over Commissioner, Commissionee: **Device commissioning successful, entering operational state (Commissioning successfully complete)**
```