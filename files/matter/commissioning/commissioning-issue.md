
# 1 PASE pass but fail to establish CASE

**Normal CASE establishment flow:**
1. Commissioner clears old PASE session
2. Commissioner discovers device's operational address (DNS-SD)
3. Commissioner sends CASE_Sigma1 → Commissionee
4. Commissionee replies CASE_Sigma2 → Commissioner
5. Commissioner sends CASE_Sigma3 → Commissionee
6. Commissionee verifies Sigma3 and sends StatusReport (success) → Commissioner
7. CASE secure channel established

**Debugging flow by step:**

- **Step 1-2: Commissioner fails to discover device's operational address**
  - *Symptoms:* No "Lookup started" or "Updating device address" logs on Commissioner side
  - *Possible causes:* Device not publishing operational DNS-SD records (missing SRV/TXT), IPv6 network issue, Thread Border Router not forwarding mDNS, or Commissioner not listening on correct network interface

- **Step 3: Commissioner sends CASE_Sigma1, but Commissionee does not receive it**
  - *Possible causes:*
    - IPv6 connectivity broken between Commissioner and Commissionee
    - UDP port 5540 blocked by firewall
    - Thread Border Router forwarding failure (if device on Thread network)
    - Device not listening on operational port (interface down, not joined to Thread/Wi-Fi)
    - Commissioner using wrong IP address (stale or incorrect operational discovery result)

- **Step 4: Commissionee receives Sigma1 but does not send Sigma2**
  - *Possible causes:*
    - Device cannot find matching fabric/destination (fabricIndex mismatch, NodeID mismatch)
    - Operational certificate missing or corrupted (`StorageAdapter::GetKeyValue ... Key Not Found`)
    - Operational key pair missing or invalid
    - Device in ICD (Intermittently Connected Device) sleep state when Sigma1 arrives
    - SDK bug in CASE Server handshake processing

- **Step 5: Commissionee sends Sigma2, but Commissioner does not receive it**
  - *Possible causes:*
    - Network asymmetry (ICMPv6 ping works but UDP packets dropped in one direction)
    - Multiple Border Routers causing path confusion (reply routed to wrong Border Router)
    - Commissioner no longer listening on the port/address (session timeout or cleaned up)
    - Firewall dropping return packets

- **Step 6: Commissioner receives Sigma2, sends Sigma3, but Commissionee does not receive Sigma3**
  - *Possible causes:*
    - Same network issues as Step 3 (packet loss, routing, firewall)
    - Device moved to sleep after sending Sigma2 before receiving Sigma3 (ICD devices)

- **Step 7: Commissionee receives Sigma3 but fails to establish session (no StatusReport or StatusReport with error)**
  - *Possible causes:*
    - Sigma3 verification failed (crypto mismatch, incorrect keys derived from Sigma1/Sigma2 exchange)
    - Device state corrupted during handshake
    - Device failed to compute shared key or create secure session object

**Quick diagnostics based on logs:**

| Last log seen on Commissioner | Last log seen on Commissionee | Likely issue area |
|------------------------------|-------------------------------|-------------------|
| "Lookup started for ..." no update address | None | Operational discovery failed (DNS-SD) |
| "Sent Sigma1 msg" | No "RX ... CASE_Sigma1" | Network (Sigma1 lost) |
| "Sent Sigma1 msg" | "RX ... CASE_Sigma1" but no "TX ... CASE_Sigma2" | Device side (cert/key missing or fabric mismatch) |
| "Sent Sigma1 msg" | "TX ... CASE_Sigma2" | Network (Sigma2 lost) |
| "Sent Sigma3 msg" | "RX ... CASE_Sigma2" but no "RX ... CASE_Sigma3" | Network (Sigma3 lost) |
| "Sent Sigma3 msg" | "RX ... CASE_Sigma3" but no "State change to Active" | Sigma3 verification failure |

**Retry or reboot OTBR then retry**

# 2 Failed to read BasicCommissioningInfo
```c
[1770349734.962] [2665:2668] [DL] BLE connection closed: conn=0xffffa4027880
[1770349734.963] [2665:2683] [IN] Clearing BLE pending packets.
[1770349760.543] [2665:2683] [DMG] Time out! failed to receive report data from Exchange: 28547i
[1770349760.543] [2665:2683] [CTL] Failed to read BasicCommissioningInfo: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.543] [2665:2683] [CTL] Failed to read RegulatoryConfig: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.543] [2665:2683] [CTL] Failed to read LocationCapability: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read Breadcrumb: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Ignoring failure to read SupportsConcurrentConnection: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read VendorID: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Failed to read ProductID: src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error
[1770349760.544] [2665:2683] [CTL] Error on commissioning step 'ReadCommissioningInfo': 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error'
[1770349760.544] [2665:2683] [CTL] Going from commissioning step 'ReadCommissioningInfo' with lastErr = 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error' -> 'Cleanup'
[1770349760.544] [2665:2683] [CTL] Performing next commissioning step 'Cleanup' with completion status = 'src/app/ClusterStateCache.cpp:294: CHIP Error 0x000000CA: Interaction Model Error'
[1770349760.544] [2665:2683] [CTL] Disarming failsafe on device 0xffff9c00f750
```

**Should be cause by ZAP config,double check it**

# 3 Failed Device Attestation
```c
[1772527499.736] [4036:4052] [CTL] Commissioning stage next step: 'ConfigureTCAcknowledgments' -> 'SendPAICertificateRequest'
[1772527499.736] [4036:4052] [CTL] Performing next commissioning step 'SendPAICertificateRequest'
[1772527499.736] [4036:4052] [CTL] Sending request for PAI certificate
[1772527499.736] [4036:4052] [CTL] Sending Certificate Chain request to 0xffff940217c0 device
[1772527499.737] [4036:4052] [DMG] ICR moving to [AddingComm]
[1772527499.737] [4036:4052] [DMG] ICR moving to [AddedComma]
[1772527499.737] [4036:4052] [EM] <<< [E:46813i S:6294 M:108272815] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1772527499.738] [4036:4052] [DMG] ICR moving to [AwaitingRe]
[1772527499.738] [4036:4052] [DMG] ICR moving to [AwaitingDe]
[1772527499.922] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16389
[1772527500.024] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527500.024] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527500.414] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527500.414] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527500.606] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527500.607] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527500.607] [4036:4052] [EM] >>> [E:46813i S:6294 M:34933759] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:534)
[1772527500.607] [4036:4052] [EM] Found matching exchange: 46813i, Delegate: 0xffff9400db18
[1772527500.607] [4036:4052] [DMG] ICR moving to [ResponseRe]
[1772527500.607] [4036:4052] [DMG] InvokeResponseMessage =
[1772527500.607] [4036:4052] [DMG] {
[1772527500.607] [4036:4052] [DMG]      suppressResponse = false,
[1772527500.607] [4036:4052] [DMG]      InvokeResponseIBs =
[1772527500.607] [4036:4052] [DMG]      [
[1772527500.608] [4036:4052] [DMG]              InvokeResponseIB =
[1772527500.608] [4036:4052] [DMG]              {
[1772527500.608] [4036:4052] [DMG]                      CommandDataIB =
[1772527500.608] [4036:4052] [DMG]                      {
[1772527500.608] [4036:4052] [DMG]                              CommandPathIB =
[1772527500.608] [4036:4052] [DMG]                              {
[1772527500.608] [4036:4052] [DMG]                                      EndpointId = 0x0,
[1772527500.608] [4036:4052] [DMG]                                      ClusterId = 0x3e,
[1772527500.608] [4036:4052] [DMG]                                      CommandId = 0x3,
[1772527500.608] [4036:4052] [DMG]                              },
[1772527500.608] [4036:4052] [DMG]
[1772527500.608] [4036:4052] [DMG]                              CommandFields =
[1772527500.608] [4036:4052] [DMG]                              {
[1772527500.608] [4036:4052] [DMG]                                      0x0 = [
[1772527500.609] [4036:4052] [DMG]                                             0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x
[1772527500.609] [4036:4052] [DMG]                                      ] (470 bytes)
[1772527500.609] [4036:4052] [DMG]                              },
[1772527500.609] [4036:4052] [DMG]                      },
[1772527500.609] [4036:4052] [DMG]
[1772527500.609] [4036:4052] [DMG]              },
[1772527500.609] [4036:4052] [DMG]
[1772527500.609] [4036:4052] [DMG]      ],
[1772527500.610] [4036:4052] [DMG]
[1772527500.610] [4036:4052] [DMG]      InteractionModelRevision = 11
[1772527500.610] [4036:4052] [DMG] },
[1772527500.610] [4036:4052] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1772527500.610] [4036:4052] [CTL] Received certificate chain from the device
[1772527500.610] [4036:4052] [CTL] Successfully finished commissioning step 'SendPAICertificateRequest'
[1772527500.610] [4036:4052] [CTL] Commissioning stage next step: 'SendPAICertificateRequest' -> 'SendDACCertificateRequest'
[1772527500.610] [4036:4052] [CTL] Performing next commissioning step 'SendDACCertificateRequest'
[1772527500.610] [4036:4052] [CTL] Sending request for DAC certificate
[1772527500.610] [4036:4052] [CTL] Sending Certificate Chain request to 0xffff940217c0 device
[1772527500.610] [4036:4052] [DMG] ICR moving to [AddingComm]
[1772527500.611] [4036:4052] [DMG] ICR moving to [AddedComma]
[1772527500.611] [4036:4052] [EM] <<< [E:46814i S:6294 M:108272816] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[1772527500.612] [4036:4052] [DMG] ICR moving to [AwaitingRe]
[1772527500.613] [4036:4052] [DMG] ICR moving to [AwaitingDe]
[1772527500.898] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16389
[1772527500.999] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527500.999] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527501.486] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527501.487] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527501.680] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527501.680] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527501.681] [4036:4052] [EM] >>> [E:46814i S:6294 M:34933760] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:545)
[1772527501.681] [4036:4052] [EM] Found matching exchange: 46814i, Delegate: 0xffff9400e0b8
[1772527501.682] [4036:4052] [DMG] ICR moving to [ResponseRe]
[1772527501.682] [4036:4052] [DMG] InvokeResponseMessage =
[1772527501.682] [4036:4052] [DMG] {
[1772527501.682] [4036:4052] [DMG]      suppressResponse = false,
[1772527501.682] [4036:4052] [DMG]      InvokeResponseIBs =
[1772527501.682] [4036:4052] [DMG]      [
[1772527501.682] [4036:4052] [DMG]              InvokeResponseIB =
[1772527501.683] [4036:4052] [DMG]              {
[1772527501.683] [4036:4052] [DMG]                      CommandDataIB =
[1772527501.683] [4036:4052] [DMG]                      {
[1772527501.684] [4036:4052] [DMG]                              CommandPathIB =
[1772527501.684] [4036:4052] [DMG]                              {
[1772527501.684] [4036:4052] [DMG]                                      EndpointId = 0x0,
[1772527501.684] [4036:4052] [DMG]                                      ClusterId = 0x3e,
[1772527501.684] [4036:4052] [DMG]                                      CommandId = 0x3,
[1772527501.684] [4036:4052] [DMG]                              },
[1772527501.685] [4036:4052] [DMG]
[1772527501.685] [4036:4052] [DMG]                              CommandFields =
[1772527501.685] [4036:4052] [DMG]                              {
[1772527501.685] [4036:4052] [DMG]                                      0x0 = [
[1772527501.685] [4036:4052] [DMG]                                             0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x
[1772527501.685] [4036:4052] [DMG]                                      ] (481 bytes)
[1772527501.685] [4036:4052] [DMG]                              },
[1772527501.685] [4036:4052] [DMG]                      },
[1772527501.685] [4036:4052] [DMG]
[1772527501.685] [4036:4052] [DMG]              },
[1772527501.685] [4036:4052] [DMG]
[1772527501.685] [4036:4052] [DMG]      ],
[1772527501.686] [4036:4052] [DMG]
[1772527501.686] [4036:4052] [DMG]      InteractionModelRevision = 11
[1772527501.686] [4036:4052] [DMG] },
[1772527501.686] [4036:4052] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0003
[1772527501.686] [4036:4052] [CTL] Received certificate chain from the device
[1772527501.686] [4036:4052] [CTL] Successfully finished commissioning step 'SendDACCertificateRequest'
[1772527501.686] [4036:4052] [CTL] Commissioning stage next step: 'SendDACCertificateRequest' -> 'SendAttestationRequest'
[1772527501.686] [4036:4052] [CTL] Performing next commissioning step 'SendAttestationRequest'
[1772527501.686] [4036:4052] [CTL] Sending Attestation Request to the device.
[1772527501.686] [4036:4052] [CTL] Sending Attestation request to 0xffff940217c0 device
[1772527501.686] [4036:4052] [DMG] ICR moving to [AddingComm]
[1772527501.687] [4036:4052] [DMG] ICR moving to [AddedComma]
[1772527501.687] [4036:4052] [EM] <<< [E:46815i S:6294 M:108272817] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[1772527501.688] [4036:4052] [DMG] ICR moving to [AwaitingRe]
[1772527501.688] [4036:4052] [CTL] Sent Attestation request, waiting for the Attestation Information
[1772527501.688] [4036:4052] [DMG] ICR moving to [AwaitingDe]
[1772527501.873] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16389
[1772527501.974] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527501.975] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527502.362] [4036:4041] [DL] Indication received, conn = 0xffff9c02a2a0
[1772527502.363] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16391
[1772527502.363] [4036:4052] [EM] >>> [E:46815i S:6294 M:34933761] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:09 (IM:InvokeCommandResponse) (B:418)
[1772527502.363] [4036:4052] [EM] Found matching exchange: 46815i, Delegate: 0xffff9400db18
[1772527502.364] [4036:4052] [DMG] ICR moving to [ResponseRe]
[1772527502.364] [4036:4052] [DMG] InvokeResponseMessage =
[1772527502.364] [4036:4052] [DMG] {
[1772527502.364] [4036:4052] [DMG]      suppressResponse = false,
[1772527502.364] [4036:4052] [DMG]      InvokeResponseIBs =
[1772527502.364] [4036:4052] [DMG]      [
[1772527502.364] [4036:4052] [DMG]              InvokeResponseIB =
[1772527502.364] [4036:4052] [DMG]              {
[1772527502.364] [4036:4052] [DMG]                      CommandDataIB =
[1772527502.365] [4036:4052] [DMG]                      {
[1772527502.365] [4036:4052] [DMG]                              CommandPathIB =
[1772527502.365] [4036:4052] [DMG]                              {
[1772527502.365] [4036:4052] [DMG]                                      EndpointId = 0x0,
[1772527502.365] [4036:4052] [DMG]                                      ClusterId = 0x3e,
[1772527502.365] [4036:4052] [DMG]                                      CommandId = 0x1,
[1772527502.365] [4036:4052] [DMG]                              },
[1772527502.365] [4036:4052] [DMG]
[1772527502.366] [4036:4052] [DMG]                              CommandFields =
[1772527502.366] [4036:4052] [DMG]                              {
[1772527502.366] [4036:4052] [DMG]                                      0x0 = [
[1772527502.367] [4036:4052] [DMG]                                             0x15, 0x30, 0x01, 0xf4, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x30, 0x02, 0x20, 0xa7, 0xcb, 0x22, 0x8c, 0x65, 0x8f, 0xec, 0x97, 0x79, 0x1a, 0x27, 0xe8, 0xe6, 0xa9, 0x9c, 0xa6, 0xc5, 0xf6, 0x45, 0xc7, 0x25, 0x35, 0x28, 0xa8, 0x78, 0x78, 0x5e, 0xeb, 0xb9, 0xc1, 0x1b, 0x55, 0x
[1772527502.367] [4036:4052] [DMG]                                      ] (287 bytes)
[1772527502.367] [4036:4052] [DMG]                                      0x1 = [
[1772527502.367] [4036:4052] [DMG]                                             0x1d, 0x62, 0x6a, 0x57, 0xca, 0x37, 0x00, 0x32, 0x81, 0x39, 0xc9, 0x99, 0xe1, 0xe1, 0xc3, 0x0b, 0xb6, 0xdd, 0x79, 0x41, 0x87, 0x8d, 0xf5, 0x99, 0x20, 0x6f, 0xf2, 0x64, 0x74, 0x3f, 0x1b, 0x01, 0xdc, 0xc2, 0x55, 0xf9, 0x1e, 0xbb, 0x90, 0xd8, 0xdf, 0xa5, 0xde, 0x15, 0xd1, 0xd5, 0xf5, 0x3d, 0x32, 0x23, 0x69, 0x55, 0x99, 0xce, 0x96, 0x02, 0xdf, 0x72, 0x3c, 0xd5, 0xb2, 0x5f, 0xfc, 0x47,
[1772527502.368] [4036:4052] [DMG]                                      ] (64 bytes)
[1772527502.368] [4036:4052] [DMG]                              },
[1772527502.368] [4036:4052] [DMG]                      },
[1772527502.368] [4036:4052] [DMG]
[1772527502.368] [4036:4052] [DMG]              },
[1772527502.368] [4036:4052] [DMG]
[1772527502.368] [4036:4052] [DMG]      ],
[1772527502.369] [4036:4052] [DMG]
[1772527502.369] [4036:4052] [DMG]      InteractionModelRevision = 11
[1772527502.369] [4036:4052] [DMG] },
[1772527502.369] [4036:4052] [DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_003E Command=0x0000_0001
[1772527502.369] [4036:4052] [CTL] Received Attestation Information from the device
[1772527502.369] [4036:4052] [CTL] Successfully finished commissioning step 'SendAttestationRequest'
[1772527502.369] [4036:4052] [CTL] AutoCommissioner setting attestationElements buffer size 287/287
[1772527502.369] [4036:4052] [CTL] Commissioning stage next step: 'SendAttestationRequest' -> 'AttestationVerification'
[1772527502.369] [4036:4052] [CTL] Performing next commissioning step 'AttestationVerification'
[1772527502.369] [4036:4052] [CTL] Verifying Device Attestation information received from the device
[1772527502.370] [4036:4052] [CTL] Error on commissioning step 'AttestationVerification': 'src/controller/CHIPDeviceController.cpp:1291: CHIP Error 0x00000020: Failed Device Attestation'
[1772527502.370] [4036:4052] [CTL] Failed verifying attestation information. Now checking DAC chain revoked status.
[1772527502.370] [4036:4052] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1772527502.370] [4036:4052] [CTL] Performing next commissioning step 'AttestationRevocationCheck' with completion status = 'src/controller/CHIPDeviceController.cpp:1291: CHIP Error 0x00000020: Failed Device Attestation'
[1772527502.370] [4036:4052] [CTL] Verifying the device's DAC chain revocation status
[1772527502.370] [4036:4052] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1772527502.370] [4036:4052] [CTL] Failed in verifying 'Attestation Information' command received from the device: err 203 (PAI format is invalid)
[1772527502.370] [4036:4052] [CTL] Error on commissioning step 'AttestationRevocationCheck': 'src/controller/CHIPDeviceController.cpp:1338: CHIP Error 0x00000020: Failed Device Attestation'
[1772527502.370] [4036:4052] [CTL] Going from commissioning step 'AttestationRevocationCheck' with lastErr = 'src/controller/CHIPDeviceController.cpp:1338: CHIP Error 0x00000020: Failed Device Attestation' -> 'Cleanup'
[1772527502.370] [4036:4052] [CTL] Performing next commissioning step 'Cleanup' with completion status = 'src/controller/CHIPDeviceController.cpp:1338: CHIP Error 0x00000020: Failed Device Attestation'
[1772527502.371] [4036:4052] [CTL] Disarming failsafe on device 0xffff940217c0
[1772527502.371] [4036:4052] [DMG] ICR moving to [AddingComm]
[1772527502.371] [4036:4052] [DMG] ICR moving to [AddedComma]
[1772527502.371] [4036:4052] [EM] <<< [E:46816i S:6294 M:108272818] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[1772527502.372] [4036:4052] [DMG] ICR moving to [AwaitingRe]
[1772527502.372] [4036:4052] [DMG] ICR moving to [AwaitingDe]
[1772527502.555] [4036:4052] [DL] HandlePlatformSpecificBLEEvent 16389
[1772527502.561] [4036:4041] [DL] BLE connection closed: conn=0xffff9c02a2a0
[1772527502.561] [4036:4052] [IN] Clearing BLE pending packets.
```
**Cause by corrupt NVM3 data**

# 4 Failed Device Attestation
```c
[1778485826.760] [6606:6628] [-] -----END CERTIFICATE-----
[1778485826.761] [6606:6628] [-] --> PAA certificate SKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1778485826.762] [6606:6628] [-] --> PAA certificate AKID: E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
[1778485826.769] [6606:6628] [-] CD signing key identifier: 62:FA:82:33:59:AC:FA:A9:96:3E:1C:FA:14:0A:DD:F5:04:F3:71:60
[1778485826.769] [6606:6628] [-] Allowing CD signed by test key
[1778485826.770] [6606:6628] [CTL] Error on commissioning step 'AttestationVerification': 'src/controller/CHIPDeviceController.cpp:1338: CHIP Error 0x00000020: Failed Device Attestation'
[1778485826.770] [6606:6628] [CTL] Failed verifying attestation information. Now checking DAC chain revoked status.
[1778485826.770] [6606:6628] [CTL] Commissioning stage next step: 'AttestationVerification' -> 'AttestationRevocationCheck'
[1778485826.770] [6606:6628] [CTL] Performing next commissioning step 'AttestationRevocationCheck' with completion status = 'src/controller/CHIPDeviceController.cpp:1338: CHIP Error 0x00000020: Failed Device Attestation'
[1778485826.770] [6606:6628] [TOO] Starting commissioning stage 'AttestationRevocationCheck'
[1778485826.770] [6606:6628] [CTL] Verifying the device's DAC chain revocation status
[1778485826.770] [6606:6628] [-] WARNING: No revocation delegate available. Revocation checks will be skipped!
[1778485826.770] [6606:6628] [CTL] Failed in verifying 'Attestation Information' command received from the device: err 604 (Certification declaration vendor ID failed to cross-reference with DAC and/or PAI and/or Basic Information cluster)
[1778485826.770] [6606:6628] [CTL] Error on commissioning step 'AttestationRevocationCheck': 'src/controller/CHIPDeviceController.cpp:1385: CHIP Error 0x00000020: Failed Device Attestation'
[1778485826.770] [6606:6628] [CTL] Going from commissioning step 'AttestationRevocationCheck' with lastErr = 'src/controller/CHIPDeviceController.cpp:1385: CHIP Error 0x00000020: Failed Device Attestation' -> 'Cleanup'
//...
[1778485827.442] [6606:6606] [TOO] Run command failure: src/controller/CHIPDeviceController.cpp:1385: CHIP Error 0x00000020: Failed Device Attestation
```
**Check DAC,VID PID, or bypass the verify**  
```c
//Bypass attestation verifier
sudo ./chip-tool pairing ble-thread 2250 hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f 85956333 1884 --bypass-attestation-verifier 1
```

# 5 Reset(Code is unsafe)
```c
//Cause reset, ;
[00:03:50.712][error ][DL] Chip stack locking error at 'C:/Users/Administrator/.silabs/slt/installs/conan/p/matte66ea43dc8d7de/p/third_party/matter_sdk/src/app/util/attribute-storage.cpp:659'. Code is unsafe/racy
```
**PlatformMgr().LockChipStack&PlatformMgr().UnlockChipStack()**