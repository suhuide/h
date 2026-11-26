```c
[00:00:00.091][info  ][DL] Starting scheduler
[00:00:00.091][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] SL-Window starting
[00:00:00.092][info  ][DL] ==================================================
[00:00:00.092][info  ][DL] Init CHIP Stack

Missed Logs: 11
[00:00:00.095][info  ][DL] Setting device name to : "SL-Window"
[00:00:00.095][info  ][DL] Provision mode disabled
[00:00:00.095][info  ][DL] Initializing OpenThread stack
[00:00:00.097][info  ][DL] OpenThread started: OK
[00:00:00.166][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[00:00:00.166][info  ][DL] RAIL version:, v3.0.0-b0
[00:00:00.167][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[00:00:00.169][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:00.171][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:00.173][info  ][SVR] Current Software Version String: 1
[00:00:00.418][info  ][SVR] SetupQRCode: [MT:SAGA442C00KA0648G00]
[00:00:00.419][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[00:00:00.419][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3ASAGA442C00KA0648G00
[00:00:00.422][silabs ]App Task started
matterCli> [00:00:14.074][info  ][DL] sl_bt_evt_connection_opened_id
[00:00:14.074][info  ][DL] Connect Event for CHIPoBLE on handle : 1
[00:00:14.075][info  ][DL] Connection Parameters Event for handle : 1
[00:00:14.075][info  ][DL] Connection parameter ID received - i:39, l:0, t:42, sm:0
[00:00:14.075][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:100
[00:00:14.076][info  ][DL] Connection phy status ID received - phy:1
[00:00:14.077][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:14.583][info  ][DL] Connection Parameters Event for handle : 1
[00:00:14.583][info  ][DL] Connection parameter ID received - i:78, l:0, t:100, sm:0
[00:00:17.663][info  ][DL] Char Write Req, char : 23
[00:00:17.664][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:17.664][info  ][BLE] local and remote recv window sizes = 5
[00:00:17.664][info  ][BLE] selected BTP version 4
[00:00:17.665][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[00:00:17.858][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[00:00:17.858][info  ][DL] CHIPoBLE subscribe received
[00:00:17.859][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[00:00:17.860][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[00:00:18.150][info  ][DL] Tx Confirmation received
[00:00:18.151][info  ][DL]  stop soft timer
[00:00:18.152][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:18.249][info  ][DL] Char Write Req, char : 23
[00:00:18.250][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:18.250][info  ][EM] >>> [E:51540r S:0 M:237354424] (U) Msg RX from 0:62C1268F274E3116 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[00:00:18.253][info  ][EM] <<< [E:51540r S:0 M:204966106] (U) Msg TX from 0000000000000000 to 0:62C1268F274E3116 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[00:00:18.255][info  ][SVR] Commissioning session establishment step started
[00:00:18.540][info  ][DL] Tx Confirmation received
[00:00:18.541][info  ][DL]  stop soft timer
[00:00:18.541][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:18.543][info  ][DL] Char Write Req, char : 23
[00:00:18.543][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:18.544][info  ][EM] >>> [E:51540r S:0 M:237354425] (U) Msg RX from 0:62C1268F274E3116 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[00:00:18.631][info  ][EM] <<< [E:51540r S:0 M:204966107] (U) Msg TX from 0000000000000000 to 0:62C1268F274E3116 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[00:00:18.833][info  ][DL] Tx Confirmation received
[00:00:18.833][info  ][DL]  stop soft timer
[00:00:18.835][info  ][DL] Char Write Req, char : 23
[00:00:18.835][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:18.835][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:18.836][info  ][EM] >>> [E:51540r S:0 M:237354426] (U) Msg RX from 0:62C1268F274E3116 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[00:00:18.838][info  ][EM] <<< [E:51540r S:0 M:204966108] (U) Msg TX from 0000000000000000 to 0:62C1268F274E3116 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[00:00:18.846][info  ][SC] SecureSession[0x20006d70, LSID:54307]: State change 'kEstablishing' --> 'kActive'
[00:00:18.846][info  ][SVR] Commissioning completed session establishment step
[00:00:18.847][info  ][DIS] Updating services using commissioning mode 0
[00:00:18.847][error ][DIS] Failed to remove advertised services: 3
[00:00:18.847][error ][DIS] Failed to finalize service update: 3
[00:00:18.848][info  ][SVR] Device completed Rendezvous process
[00:00:18.848][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:19.320][info  ][DL] Tx Confirmation received
[00:00:19.321][info  ][DL]  stop soft timer
[00:00:19.322][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:19.614][info  ][DL] Char Write Req, char : 23
[00:00:19.614][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:19.617][info  ][EM] >>> [E:51541r S:54307 M:264736067] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:134)
[00:00:19.649][info  ][EM] <<< [E:51541r S:54307 M:78474672] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:257)
[00:00:20.002][info  ][DL] Tx Confirmation received
[00:00:20.003][info  ][DL]  stop soft timer
[00:00:20.003][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:20.392][info  ][DL] Tx Confirmation received
[00:00:20.393][info  ][DL]  stop soft timer
[00:00:20.394][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:20.587][info  ][DL] Char Write Req, char : 23
[00:00:20.588][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:20.591][info  ][EM] >>> [E:51542r S:54307 M:264736068] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:103)
[00:00:20.607][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0007err = 586
[00:00:20.611][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0006err = 586
[00:00:20.618][info  ][EM] <<< [E:51542r S:54307 M:78474673] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:191)
[00:00:21.075][info  ][DL] Tx Confirmation received
[00:00:21.076][info  ][DL]  stop soft timer
[00:00:21.077][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:21.271][info  ][DL] Char Write Req, char : 23
[00:00:21.272][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:21.274][info  ][EM] >>> [E:51543r S:54307 M:264736069] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:21.277][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[00:00:21.281][info  ][EM] <<< [E:51543r S:54307 M:78474674] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:21.562][info  ][DL] Tx Confirmation received
[00:00:21.563][info  ][DL]  stop soft timer
[00:00:21.565][info  ][DL] Char Write Req, char : 23
[00:00:21.566][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:21.566][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:21.569][info  ][EM] >>> [E:51544r S:54307 M:264736070] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[00:00:21.576][info  ][EM] <<< [E:51544r S:54307 M:78474675] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:21.757][info  ][DL] Tx Confirmation received
[00:00:21.758][info  ][DL]  stop soft timer
[00:00:21.760][info  ][DL] Char Write Req, char : 23
[00:00:21.760][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:21.760][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:21.763][info  ][EM] >>> [E:51545r S:54307 M:264736071] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:21.766][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[00:00:21.770][info  ][EM] <<< [E:51545r S:54307 M:78474676] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[00:00:22.050][info  ][DL] Tx Confirmation received
[00:00:22.050][info  ][DL]  stop soft timer
[00:00:22.051][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:22.831][info  ][DL] Tx Confirmation received
[00:00:22.831][info  ][DL]  stop soft timer
[00:00:22.832][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:23.416][info  ][DL] Tx Confirmation received
[00:00:23.416][info  ][DL]  stop soft timer
[00:00:23.416][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:23.514][info  ][DL] Char Write Req, char : 23
[00:00:23.515][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:23.517][info  ][EM] >>> [E:51546r S:54307 M:264736072] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:23.520][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[00:00:23.524][info  ][EM] <<< [E:51546r S:54307 M:78474677] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[00:00:23.903][info  ][DL] Tx Confirmation received
[00:00:23.903][info  ][DL]  stop soft timer
[00:00:23.904][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:24.292][info  ][DL] Tx Confirmation received
[00:00:24.293][info  ][DL]  stop soft timer
[00:00:24.293][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:24.487][info  ][DL] Tx Confirmation received
[00:00:24.489][info  ][DL]  stop soft timer
[00:00:24.489][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:24.586][info  ][DL] Char Write Req, char : 23
[00:00:24.587][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:24.590][info  ][EM] >>> [E:51547r S:54307 M:264736073] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:24.592][info  ][ZCL] OpCreds: Received an AttestationRequest command
[00:00:24.599][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:599, sig_size:64, err:0x00
[00:00:24.600][info  ][ZCL] OpCreds: AttestationRequest successful.
[00:00:24.603][info  ][EM] <<< [E:51547r S:54307 M:78474678] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:714)
[00:00:24.877][info  ][DL] Tx Confirmation received
[00:00:24.878][info  ][DL]  stop soft timer
[00:00:24.878][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.170][info  ][DL] Tx Confirmation received
[00:00:25.170][info  ][DL]  stop soft timer
[00:00:25.171][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.462][info  ][DL] Tx Confirmation received
[00:00:25.463][info  ][DL]  stop soft timer
[00:00:25.464][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.465][info  ][DL] Char Write Req, char : 23
[00:00:25.466][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.469][info  ][EM] >>> [E:51548r S:54307 M:264736074] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:25.472][info  ][ZCL] OpCreds: Received a CSRRequest command
[00:00:25.487][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[00:00:25.494][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:277, sig_size:64, err:0x00
[00:00:25.494][info  ][ZCL] OpCreds: CSRRequest successful.
[00:00:25.498][info  ][EM] <<< [E:51548r S:54307 M:78474679] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:392)
[00:00:25.950][info  ][DL] Tx Confirmation received
[00:00:25.951][info  ][DL]  stop soft timer
[00:00:25.951][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:26.243][info  ][DL] Tx Confirmation received
[00:00:26.243][info  ][DL]  stop soft timer
[00:00:26.245][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:26.438][info  ][DL] Char Write Req, char : 23
[00:00:26.438][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:26.732][info  ][DL] Char Write Req, char : 23
[00:00:26.732][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:26.735][info  ][EM] >>> [E:51549r S:54307 M:264736075] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:293)
[00:00:26.738][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[00:00:26.751][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[00:00:26.755][info  ][EM] <<< [E:51549r S:54307 M:78474680] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[00:00:27.022][info  ][DL] Tx Confirmation received
[00:00:27.023][info  ][DL]  stop soft timer
[00:00:27.024][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:27.220][info  ][DL] Char Write Req, char : 23
[00:00:27.221][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.513][info  ][DL] Char Write Req, char : 23
[00:00:27.513][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.708][info  ][DL] Char Write Req, char : 23
[00:00:27.708][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.710][info  ][EM] >>> [E:51550r S:54307 M:264736076] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:567)
[00:00:27.713][info  ][ZCL] OpCreds: Received an AddNOC command
[00:00:27.716][info  ][FP] Validating NOC chain
[00:00:27.750][info  ][FP] NOC chain validation successful
[00:00:27.750][info  ][FP] Added new fabric at index: 0x1
[00:00:27.750][info  ][FP] Assigned compressed fabric ID: 0x4B6873C4587CC6ED, node ID: 0x00000000000008CA
[00:00:27.750][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[00:00:27.750][info  ][TS] New proposed Last Known Good Time: 2021-01-01T00:00:00
[00:00:27.751][info  ][TS] Retaining current Last Known Good Time
[00:00:27.770][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0x000000000001B669
[00:00:27.771][info  ][DIS] Advertise operational node 4B6873C4587CC6ED-00000000000008CA
[00:00:27.771][error ][SVR] Operational advertising failed: 3
[00:00:27.772][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[00:00:27.775][info  ][EM] <<< [E:51550r S:54307 M:78474681] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [C6ED] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:27.900][info  ][DL] Tx Confirmation received
[00:00:27.901][info  ][DL]  stop soft timer
[00:00:27.902][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.292][info  ][DL] Char Write Req, char : 23
[00:00:28.293][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:28.295][info  ][EM] >>> [E:51551r S:54307 M:264736077] (S) Msg RX from 1:FFFFFFFB00000000 [C6ED] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:171)
[00:00:28.303][info  ][EM] <<< [E:51551r S:54307 M:78474682] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [C6ED] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:28.583][info  ][DL] Tx Confirmation received
[00:00:28.583][info  ][DL]  stop soft timer
[00:00:28.584][info  ][DL] Char Write Req, char : 23
[00:00:28.585][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.585][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:28.588][info  ][EM] >>> [E:51552r S:54307 M:264736078] (S) Msg RX from 1:FFFFFFFB00000000 [C6ED] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:28.591][info  ][FS] GeneralCommissioning: Received ArmFailSafe (164s)
[00:00:28.594][info  ][EM] <<< [E:51552r S:54307 M:78474683] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [C6ED] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:28.777][info  ][DL] Tx Confirmation received
[00:00:28.778][info  ][DL]  stop soft timer
[00:00:28.780][info  ][DL] Char Write Req, char : 23
[00:00:28.781][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.781][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:28.784][info  ][EM] >>> [E:51553r S:54307 M:264736079] (S) Msg RX from 1:FFFFFFFB00000000 [C6ED] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[00:00:28.814][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[00:00:28.817][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:30.124][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[00:00:30.125][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:30.125][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[00:00:30.129][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[00:00:30.129][info  ][SVR] Scheduling OTA Requestor initialization
[00:00:30.129][info  ][SVR] Joining Multicast groups
[00:00:30.134][info  ][EM] <<< [E:51553r S:54307 M:78474684] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [C6ED] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[00:00:30.135][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[00:00:30.135][info  ][DIS] Advertise operational node 4B6873C4587CC6ED-00000000000008CA
[00:00:30.136][error ][SVR] Operational advertising failed: 3
[00:00:30.136][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:30.435][info  ][DL] Tx Confirmation received
[00:00:30.436][info  ][DL]  stop soft timer
[00:00:30.436][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:30.483][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[00:00:30.484][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[00:00:30.484][info  ][SVR] Server initialization complete
[00:00:30.484][info  ][DIS] Updating services using commissioning mode 0
[00:00:30.485][info  ][DIS] Advertise operational node 4B6873C4587CC6ED-00000000000008CA
[00:00:30.486][info  ][DL] advertising srp service: 4B6873C4587CC6ED-00000000000008CA._matter._tcp
[00:00:30.486][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[00:00:30.503][info  ][IM] No subscriptions to resume
[00:00:32.269][info  ][EM] >>> [E:51554r S:0 M:237354427] (U) Msg RX from 0:02C9A27FCA63A7BE [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[00:00:32.269][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x20008900
[00:00:32.271][info  ][EM] <<< [E:51554r S:0 M:204966109 (Ack:237354427)] (U) Msg TX from 0000000000000000 to 0:02C9A27FCA63A7BE [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:53110] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:32.272][info  ][SC] Received Sigma1 msg
[00:00:32.287][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[00:00:32.316][info  ][EM] <<< [E:51554r S:0 M:204966110 (Ack:237354427)] (U) Msg TX from 0000000000000000 to 0:02C9A27FCA63A7BE [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:53110] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[00:00:32.318][info  ][EM] ??1 [E:51554r S:0 M:204966110] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3349ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:32.319][info  ][SC] Sent Sigma2 msg
[00:00:32.874][info  ][DL] Char Write Req, char : 23
[00:00:32.874][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.083][info  ][EM] >>> [E:51554r S:0 M:237354428 (Ack:204966110)] (U) Msg RX from 0:02C9A27FCA63A7BE [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[00:00:33.084][info  ][EM] <<< [E:51554r S:0 M:204966111 (Ack:237354428)] (U) Msg TX from 0000000000000000 to 0:02C9A27FCA63A7BE [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:53110] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:33.085][info  ][SC] Received Sigma3 msg
[00:00:33.144][info  ][EM] <<< [E:51554r S:0 M:204966112 (Ack:237354428)] (U) Msg TX from 0000000000000000 to 0:02C9A27FCA63A7BE [0000] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:53110] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[00:00:33.145][info  ][EM] ??1 [E:51554r S:0 M:204966112] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3377ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:33.151][info  ][SC] SecureSession[0x20006e48, LSID:54308]: State change 'kEstablishing' --> 'kActive'
[00:00:33.151][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[00:00:33.153][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:33.486][info  ][SWU] Stopping the watchdog timer
[00:00:33.487][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[00:00:33.592][info  ][EM] >>> [E:51555r S:54308 M:45911556] (S) Msg RX from 1:000000000001B669 [C6ED] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[00:00:33.594][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[00:00:33.597][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[00:00:33.610][info  ][TS] Committing Last Known Good Time to storage: 2023-10-10T16:28:52
[00:00:33.623][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x4B6873C4587CC6ED, FabricId 0000000000000001, NodeId 00000000000008CA, VendorId 0xFFF1

Missed Logs: 3
[00:00:33.624][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[00:00:33.624][info  ][FS] Fail-safe cleanly disarmed
[00:00:33.627][info  ][EM] <<< [E:51555r S:54308 M:5928595 (Ack:45911556)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [C6ED] [UDP:[fd98:42ee:f6b4:1:cc62:db03:753:ecd0]:53110] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[00:00:33.628][info  ][EM] ??1 [E:51555r S:54308 M:5928595] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:33.630][info  ][EM] >>> [E:51554r S:0 M:237354429 (Ack:204966112)] (U) Msg RX from 0:02C9A27FCA63A7BE [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:33.630][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[00:00:33.631][info  ][SWU] Device commissioned, schedule a default provider query
[00:00:33.631][info  ][SVR] Commissioning completed successfully
[00:00:33.631][info  ][DIS] Updating services using commissioning mode 0
[00:00:33.632][info  ][DIS] Advertise operational node 4B6873C4587CC6ED-00000000000008CA
[00:00:33.750][info  ][DL] Disconnect Event for CHIPoBLE on handle : 1
[00:00:33.750][info  ][DL] BLE GATT connection closed (con 1, reason 4118)
[00:00:33.750][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[00:00:34.250][info  ][EM] >>> [E:51555r S:54308 M:45911557 (Ack:5928595)] (S) Msg RX from 1:000000000001B669 [C6ED] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:01:03.631][error ][SWU] No suitable OTA Provider candidate found
[00:01:03.631][info  ][SWU] No provider available
```