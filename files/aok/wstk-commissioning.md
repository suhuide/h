```c
[00:00:23.919][info  ][DL] eric, sl_bt_evt_connection_opened_id
[00:00:23.920][info  ][DL] eric, Connect Event for CHIPoBLE on handle : 1
[00:00:23.920][info  ][DL] Connection Parameters Event for handle : 1
[00:00:23.920][info  ][DL] Connection parameter ID received - i:24, l:0, t:500, sm:0
[00:00:23.921][info  ][DL] Connection phy status ID received - phy:1
[00:00:23.922][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:23.985][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:27, rxL:328
[00:00:24.314][info  ][DL] Connection Parameters Event for handle : 1
[00:00:24.315][info  ][DL] Connection parameter ID received - i:6, l:0, t:500, sm:0
[00:00:24.315][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:500
[00:00:24.601][info  ][DL] Char Write Req, char : 23
[00:00:24.601][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:24.602][info  ][BLE] local and remote recv window sizes = 5
[00:00:24.602][info  ][BLE] selected BTP version 4
[00:00:24.602][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.
[00:00:24.624][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[00:00:24.624][info  ][DL] CHIPoBLE subscribe received
[00:00:24.624][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[00:00:24.625][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[00:00:24.638][info  ][DL] Tx Confirmation received
[00:00:24.638][info  ][DL]  stop soft timer
[00:00:24.640][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:24.646][info  ][DL] Char Write Req, char : 23
[00:00:24.646][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:24.647][info  ][EM] >>> [E:53326r S:0 M:85332021] (U) Msg RX from 0:8518FFBF059558E9 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[00:00:24.651][info  ][EM] <<< [E:53326r S:0 M:81285818] (U) Msg TX from 0000000000000000 to 0:8518FFBF059558E9 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:153)
[00:00:24.654][info  ][SVR] Commissioning session establishment step started
[00:00:24.654][info  ][DL] Connection Parameters Event for handle : 1
[00:00:24.654][info  ][DL] Connection parameter ID received - i:72, l:0, t:500, sm:0
[00:00:24.794][info  ][DL] Tx Confirmation received
[00:00:24.795][info  ][DL]  stop soft timer
[00:00:24.795][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:24.797][info  ][DL] Char Write Req, char : 23
[00:00:24.797][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:247, rxL:2120
[00:00:24.798][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:24.799][info  ][EM] >>> [E:53326r S:0 M:85332022] (U) Msg RX from 0:8518FFBF059558E9 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[00:00:24.885][info  ][EM] <<< [E:53326r S:0 M:81285819] (U) Msg TX from 0000000000000000 to 0:8518FFBF059558E9 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[00:00:25.064][info  ][DL] Tx Confirmation received
[00:00:25.064][info  ][DL]  stop soft timer
[00:00:25.066][info  ][DL] Char Write Req, char : 23
[00:00:25.066][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.067][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.068][info  ][EM] >>> [E:53326r S:0 M:85332023] (U) Msg RX from 0:8518FFBF059558E9 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[00:00:25.070][info  ][EM] <<< [E:53326r S:0 M:81285820] (U) Msg TX from 0000000000000000 to 0:8518FFBF059558E9 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[00:00:25.077][info  ][SC] SecureSession[0x20006d70, LSID:26068]: State change 'kEstablishing' --> 'kActive'
[00:00:25.077][info  ][SVR] Commissioning completed session establishment step
[00:00:25.078][info  ][DIS] Updating services using commissioning mode 0
[00:00:25.078][error ][DIS] Failed to remove advertised services: 3
[00:00:25.079][error ][DIS] Failed to finalize service update: 3
[00:00:25.079][info  ][SVR] Device completed Rendezvous process
[00:00:25.079][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:25.244][info  ][DL] Tx Confirmation received
[00:00:25.246][info  ][DL]  stop soft timer
[00:00:25.246][info  ][DL] Char Write Req, char : 23
[00:00:25.247][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.247][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.250][info  ][EM] >>> [E:53327r S:26068 M:175630962] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:25.258][info  ][EM] <<< [E:53327r S:26068 M:117739446] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[00:00:25.604][info  ][DL] Tx Confirmation received
[00:00:25.604][info  ][DL]  stop soft timer
[00:00:25.606][info  ][DL] Char Write Req, char : 23
[00:00:25.606][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.607][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.610][info  ][EM] >>> [E:53328r S:26068 M:175630963] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:25.618][info  ][EM] <<< [E:53328r S:26068 M:117739447] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[00:00:25.784][info  ][DL] Tx Confirmation received
[00:00:25.786][info  ][DL]  stop soft timer
[00:00:25.786][info  ][DL] Char Write Req, char : 23
[00:00:25.787][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.787][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.790][info  ][EM] >>> [E:53329r S:26068 M:175630964] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:25.797][info  ][EM] <<< [E:53329r S:26068 M:117739448] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:82)
[00:00:25.964][info  ][DL] Tx Confirmation received
[00:00:25.965][info  ][DL]  stop soft timer
[00:00:25.966][info  ][DL] Char Write Req, char : 23
[00:00:25.966][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:25.966][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:25.969][info  ][EM] >>> [E:53330r S:26068 M:175630965] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:25.977][info  ][EM] <<< [E:53330r S:26068 M:117739449] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:26.324][info  ][DL] Tx Confirmation received
[00:00:26.326][info  ][DL]  stop soft timer
[00:00:26.326][info  ][DL] Char Write Req, char : 23
[00:00:26.327][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:26.327][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:26.330][info  ][EM] >>> [E:53331r S:26068 M:175630966] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:26.337][info  ][EM] <<< [E:53331r S:26068 M:117739450] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:26.594][info  ][DL] Tx Confirmation received
[00:00:26.595][info  ][DL]  stop soft timer
[00:00:26.596][info  ][DL] Char Write Req, char : 23
[00:00:26.596][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:26.597][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:26.600][info  ][EM] >>> [E:53332r S:26068 M:175630967] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:26.607][info  ][EM] <<< [E:53332r S:26068 M:117739451] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:26.774][info  ][DL] Tx Confirmation received
[00:00:26.775][info  ][DL]  stop soft timer
[00:00:26.775][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:26.955][info  ][DL] Char Write Req, char : 23
[00:00:26.956][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:26.958][info  ][EM] >>> [E:53333r S:26068 M:175630968] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:26.965][info  ][EM] <<< [E:53333r S:26068 M:117739452] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:27.134][info  ][DL] Tx Confirmation received
[00:00:27.135][info  ][DL]  stop soft timer
[00:00:27.136][info  ][DL] Char Write Req, char : 23
[00:00:27.136][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:27.137][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.140][info  ][EM] >>> [E:53334r S:26068 M:175630969] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:27.147][info  ][EM] <<< [E:53334r S:26068 M:117739453] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:65)
[00:00:27.314][info  ][DL] Tx Confirmation received
[00:00:27.315][info  ][DL]  stop soft timer
[00:00:27.316][info  ][DL] Char Write Req, char : 23
[00:00:27.316][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:27.317][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.319][info  ][EM] >>> [E:53335r S:26068 M:175630970] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[00:00:27.322][info  ][EM] <<< [E:53335r S:26068 M:117739454] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[00:00:27.494][info  ][DL] Tx Confirmation received
[00:00:27.495][info  ][DL]  stop soft timer
[00:00:27.496][info  ][DL] Char Write Req, char : 23
[00:00:27.497][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:27.497][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.500][info  ][EM] >>> [E:53335r S:26068 M:175630971] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:27.502][info  ][FS] GeneralCommissioning: Received ArmFailSafe (240s)
[00:00:27.505][info  ][EM] <<< [E:53335r S:26068 M:117739455] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:27.674][info  ][DL] Tx Confirmation received
[00:00:27.675][info  ][DL]  stop soft timer
[00:00:27.676][info  ][DL] Char Write Req, char : 23
[00:00:27.677][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:27.677][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:27.680][info  ][EM] >>> [E:53336r S:26068 M:175630972] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:27.683][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[00:00:27.686][info  ][EM] <<< [E:53336r S:26068 M:117739456] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:527)
[00:00:27.854][info  ][DL] Tx Confirmation received
[00:00:27.855][info  ][DL]  stop soft timer
[00:00:27.855][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.035][info  ][DL] Tx Confirmation received
[00:00:28.035][info  ][DL]  stop soft timer
[00:00:28.036][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.214][info  ][DL] Tx Confirmation received
[00:00:28.214][info  ][DL]  stop soft timer
[00:00:28.216][info  ][DL] Char Write Req, char : 23
[00:00:28.216][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.216][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:28.219][info  ][EM] >>> [E:53337r S:26068 M:175630973] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:28.222][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[00:00:28.226][info  ][EM] <<< [E:53337r S:26068 M:117739457] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:555)
[00:00:28.394][info  ][DL] Tx Confirmation received
[00:00:28.395][info  ][DL]  stop soft timer
[00:00:28.395][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.575][info  ][DL] Tx Confirmation received
[00:00:28.575][info  ][DL]  stop soft timer
[00:00:28.576][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:28.754][info  ][DL] Tx Confirmation received
[00:00:28.754][info  ][DL]  stop soft timer
[00:00:28.755][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:30.286][info  ][DL] Char Write Req, char : 23
[00:00:30.286][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:30.289][info  ][EM] >>> [E:53338r S:26068 M:175630974] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:96)
[00:00:30.291][info  ][ZCL] OpCreds: Received a CSRRequest command
[00:00:30.306][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[00:00:30.313][info  ][DL] SignWithDeviceAttestationKey, kid:0, msg_size:278, sig_size:64, err:0x00
[00:00:30.313][info  ][ZCL] OpCreds: CSRRequest successful.
[00:00:30.317][info  ][EM] <<< [E:53338r S:26068 M:117739458] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:393)
[00:00:30.464][info  ][DL] Tx Confirmation received
[00:00:30.464][info  ][DL]  stop soft timer
[00:00:30.465][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:30.644][info  ][DL] Tx Confirmation received
[00:00:30.645][info  ][DL]  stop soft timer
[00:00:30.645][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:30.915][info  ][DL] Char Write Req, char : 23
[00:00:30.916][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:30.918][info  ][EM] >>> [E:53339r S:26068 M:175630975] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:30.925][info  ][EM] <<< [E:53339r S:26068 M:117739459] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:31.094][info  ][DL] Tx Confirmation received
[00:00:31.094][info  ][DL]  stop soft timer
[00:00:31.095][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:31.100][info  ][DL] Char Write Req, char : 23
[00:00:31.100][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:31.275][info  ][DL] Char Write Req, char : 23
[00:00:31.276][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:31.279][info  ][EM] >>> [E:53340r S:26068 M:175630976] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:324)
[00:00:31.281][info  ][ZCL] OpCreds: Received an AddTrustedRootCertificate command
[00:00:31.295][info  ][ZCL] OpCreds: AddTrustedRootCertificate successful.
[00:00:31.298][info  ][EM] <<< [E:53340r S:26068 M:117739460] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:63)
[00:00:31.544][info  ][DL] Tx Confirmation received
[00:00:31.544][info  ][DL]  stop soft timer
[00:00:31.544][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:31.547][info  ][DL] Char Write Req, char : 23
[00:00:31.548][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:31.727][info  ][DL] Char Write Req, char : 23
[00:00:31.728][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:31.906][info  ][DL] Char Write Req, char : 23
[00:00:31.907][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:31.909][info  ][EM] >>> [E:53341r S:26068 M:175630977] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:629)
[00:00:31.912][info  ][ZCL] OpCreds: Received an AddNOC command
[00:00:31.916][info  ][FP] Validating NOC chain
[00:00:31.948][info  ][FP] NOC chain validation successful
[00:00:31.948][info  ][FP] Added new fabric at index: 0x1
[00:00:31.948][info  ][FP] Assigned compressed fabric ID: 0xFDA99EDEC35D5933, node ID: 0xDFBBF9951AA8C8F5
[00:00:31.949][info  ][TS] Last Known Good Time: 2023-10-10T16:28:52
[00:00:31.949][info  ][TS] New proposed Last Known Good Time: 2026-02-06T05:51:15
[00:00:31.950][info  ][TS] Updating pending Last Known Good Time to 2026-02-06T05:51:15
[00:00:31.968][info  ][ZCL] OpCreds: ACL entry created for Fabric index 0x1 CASE Admin Subject 0xFFFFFFFD00000001
[00:00:31.969][info  ][DIS] Advertise operational node FDA99EDEC35D5933-DFBBF9951AA8C8F5
[00:00:31.969][error ][SVR] Operational advertising failed: 3
[00:00:31.970][info  ][ZCL] OpCreds: successfully created fabric index 0x1 via AddNOC
[00:00:31.973][info  ][EM] <<< [E:53341r S:26068 M:117739461] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:32.174][info  ][DL] Tx Confirmation received
[00:00:32.175][info  ][DL]  stop soft timer
[00:00:32.176][info  ][DL] Char Write Req, char : 23
[00:00:32.176][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:32.176][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.179][info  ][EM] >>> [E:53342r S:26068 M:175630978] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:32.187][info  ][EM] <<< [E:53342r S:26068 M:117739462] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:90)
[00:00:32.354][info  ][DL] Tx Confirmation received
[00:00:32.355][info  ][DL]  stop soft timer
[00:00:32.356][info  ][DL] Char Write Req, char : 23
[00:00:32.357][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:32.357][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.360][info  ][EM] >>> [E:53343r S:26068 M:175630979] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:32.368][info  ][EM] <<< [E:53343r S:26068 M:117739463] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:70)
[00:00:32.534][info  ][DL] Tx Confirmation received
[00:00:32.536][info  ][DL]  stop soft timer
[00:00:32.536][info  ][DL] Char Write Req, char : 23
[00:00:32.537][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:32.537][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.540][info  ][EM] >>> [E:53344r S:26068 M:175630980] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:32.545][info  ][EM] <<< [E:53344r S:26068 M:117739464] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[00:00:32.714][info  ][DL] Tx Confirmation received
[00:00:32.714][info  ][DL]  stop soft timer
[00:00:32.715][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:32.805][info  ][DL] Char Write Req, char : 23
[00:00:32.805][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.808][info  ][EM] >>> [E:53345r S:26068 M:175630981] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:32.814][info  ][EM] <<< [E:53345r S:26068 M:117739465] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[00:00:32.984][info  ][DL] Tx Confirmation received
[00:00:32.984][info  ][DL]  stop soft timer
[00:00:32.986][info  ][DL] Char Write Req, char : 23
[00:00:32.986][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:32.987][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:32.990][info  ][EM] >>> [E:53346r S:26068 M:175630982] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:32.998][info  ][EM] <<< [E:53346r S:26068 M:117739466] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:70)
[00:00:33.164][info  ][DL] Tx Confirmation received
[00:00:33.166][info  ][DL]  stop soft timer
[00:00:33.166][info  ][DL] Char Write Req, char : 23
[00:00:33.166][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:33.166][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.169][info  ][EM] >>> [E:53347r S:26068 M:175630983] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:33.175][info  ][EM] <<< [E:53347r S:26068 M:117739467] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[00:00:33.344][info  ][DL] Tx Confirmation received
[00:00:33.344][info  ][DL]  stop soft timer
[00:00:33.346][info  ][DL] Char Write Req, char : 23
[00:00:33.346][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:33.346][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.350][info  ][EM] >>> [E:53348r S:26068 M:175630984] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:33.356][info  ][EM] <<< [E:53348r S:26068 M:117739468] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:75)
[00:00:33.524][info  ][DL] Tx Confirmation received
[00:00:33.524][info  ][DL]  stop soft timer
[00:00:33.526][info  ][DL] Char Write Req, char : 23
[00:00:33.526][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:33.527][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:33.530][info  ][EM] >>> [E:53349r S:26068 M:175630985] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:52)
[00:00:33.538][info  ][EM] <<< [E:53349r S:26068 M:117739469] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:67)
[00:00:33.705][info  ][DL] Tx Confirmation received
[00:00:33.705][info  ][DL]  stop soft timer
[00:00:33.706][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:34.875][info  ][DL] Char Write Req, char : 23
[00:00:34.875][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:34.877][info  ][EM] >>> [E:53350r S:26068 M:175630986] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[00:00:34.880][info  ][EM] <<< [E:53350r S:26068 M:117739470] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[00:00:35.144][info  ][DL] Tx Confirmation received
[00:00:35.144][info  ][DL]  stop soft timer
[00:00:35.146][info  ][DL] Char Write Req, char : 23
[00:00:35.146][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.147][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:35.150][info  ][EM] >>> [E:53350r S:26068 M:175630987] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:66)
[00:00:35.153][info  ][FS] GeneralCommissioning: Received ArmFailSafe (270s)
[00:00:35.156][info  ][EM] <<< [E:53350r S:26068 M:117739471] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:35.324][info  ][DL] Tx Confirmation received
[00:00:35.326][info  ][DL]  stop soft timer
[00:00:35.326][info  ][DL] Char Write Req, char : 23
[00:00:35.327][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.327][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:35.330][info  ][EM] >>> [E:53351r S:26068 M:175630988] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:35.337][info  ][EM] <<< [E:53351r S:26068 M:117739472] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:35.594][info  ][DL] Tx Confirmation received
[00:00:35.595][info  ][DL]  stop soft timer
[00:00:35.596][info  ][DL] Char Write Req, char : 23
[00:00:35.596][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.596][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:35.599][info  ][EM] >>> [E:53352r S:26068 M:175630989] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[00:00:35.602][info  ][EM] <<< [E:53352r S:26068 M:117739473] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[00:00:35.864][info  ][DL] Tx Confirmation received
[00:00:35.865][info  ][DL]  stop soft timer
[00:00:35.866][info  ][DL] Char Write Req, char : 23
[00:00:35.867][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:35.867][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:35.870][info  ][EM] >>> [E:53352r S:26068 M:175630990] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:102)
[00:00:35.877][info  ][EM] <<< [E:53352r S:26068 M:117739474] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:36.044][info  ][DL] Tx Confirmation received
[00:00:36.045][info  ][DL]  stop soft timer
[00:00:36.045][info  ][DL] Char Write Req, char : 23
[00:00:36.046][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.046][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.049][info  ][EM] >>> [E:53353r S:26068 M:175630991] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:36.057][info  ][EM] <<< [E:53353r S:26068 M:117739475] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:05 (IM:ReportData) (B:66)
[00:00:36.314][info  ][DL] Tx Confirmation received
[00:00:36.315][info  ][DL]  stop soft timer
[00:00:36.316][info  ][DL] Char Write Req, char : 23
[00:00:36.316][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.317][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.319][info  ][EM] >>> [E:53354r S:26068 M:175630992] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:0A (IM:TimedRequest) (B:39)
[00:00:36.322][info  ][EM] <<< [E:53354r S:26068 M:117739476] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:01 (IM:StatusResponse) (B:38)
[00:00:36.494][info  ][DL] Tx Confirmation received
[00:00:36.495][info  ][DL]  stop soft timer
[00:00:36.496][info  ][DL] Char Write Req, char : 23
[00:00:36.497][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:36.497][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:36.500][info  ][EM] >>> [E:53354r S:26068 M:175630993] (S) Msg RX from 1:FFFFFFFB00000000 [5933] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:73)
[00:00:36.527][info  ][DL] _OnPlatformEvent default:  event->Type = 32772
[00:00:36.528][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:37.093][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:37.764][info  ][DL] SRP Client was started, detected server: fd6e:d157:02b4:cdbf:9518:944f:837d:f011
[00:00:37.765][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:37.765][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[00:00:37.770][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[00:00:37.770][info  ][SVR] Scheduling OTA Requestor initialization
[00:00:37.770][info  ][SVR] Joining Multicast groups
[00:00:37.774][info  ][EM] <<< [E:53354r S:26068 M:117739477] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [5933] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[00:00:37.776][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[00:00:37.776][info  ][DIS] Advertise operational node FDA99EDEC35D5933-DFBBF9951AA8C8F5
[00:00:37.776][error ][SVR] Operational advertising failed: 3
[00:00:37.777][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:37.934][info  ][DL] Tx Confirmation received
[00:00:37.935][info  ][DL]  stop soft timer
[00:00:37.935][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:38.608][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[00:00:38.608][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[00:00:38.608][info  ][SVR] Server initialization complete
[00:00:38.609][info  ][DIS] Updating services using commissioning mode 0
[00:00:38.609][info  ][DIS] Advertise operational node FDA99EDEC35D5933-DFBBF9951AA8C8F5
[00:00:38.610][info  ][DL] advertising srp service: FDA99EDEC35D5933-DFBBF9951AA8C8F5._matter._tcp
[00:00:38.611][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[00:00:38.628][info  ][IM] No subscriptions to resume
[00:00:40.455][info  ][DL] Char Write Req, char : 23
[00:00:40.455][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:41.610][info  ][SWU] Stopping the watchdog timer
[00:00:41.611][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[00:00:41.785][info  ][EM] >>> [E:987r S:0 M:29120870] (U) Msg RX from 0:AE0F611B4A900743 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[00:00:41.786][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x20008900
[00:00:41.787][info  ][EM] <<< [E:987r S:0 M:81285821 (Ack:29120870)] (U) Msg TX from 0000000000000000 to 0:AE0F611B4A900743 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:41.788][info  ][SC] Received Sigma1 msg
[00:00:41.802][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0xDFBBF9951AA8C8F5
[00:00:41.832][info  ][EM] <<< [E:987r S:0 M:81285822 (Ack:29120870)] (U) Msg TX from 0000000000000000 to 0:AE0F611B4A900743 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:809)
[00:00:41.833][info  ][EM] ??1 [E:987r S:0 M:81285822] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3374ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:41.833][info  ][SC] Sent Sigma2 msg
[00:00:42.592][info  ][EM] >>> [E:987r S:0 M:29120871 (Ack:81285822)] (U) Msg RX from 0:AE0F611B4A900743 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:657)
[00:00:42.594][info  ][EM] <<< [E:987r S:0 M:81285823 (Ack:29120871)] (U) Msg TX from 0000000000000000 to 0:AE0F611B4A900743 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:42.595][info  ][SC] Received Sigma3 msg
[00:00:42.655][info  ][EM] <<< [E:987r S:0 M:81285824 (Ack:29120871)] (U) Msg TX from 0000000000000000 to 0:AE0F611B4A900743 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[00:00:42.656][info  ][EM] ??1 [E:987r S:0 M:81285824] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3342ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:42.662][info  ][SC] SecureSession[0x20006e48, LSID:26069]: State change 'kEstablishing' --> 'kActive'
[00:00:42.662][info  ][IN] CASE Session established to peer: <8CBDA24D2F21C48C, 1>
[00:00:42.664][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:43.064][info  ][DL] Tx Confirmation received
[00:00:43.065][info  ][DL]  stop soft timer
[00:00:43.065][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:43.101][info  ][EM] >>> [E:987r S:0 M:29120872 (Ack:81285824)] (U) Msg RX from 0:AE0F611B4A900743 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:43.142][info  ][EM] >>> [E:988r S:26069 M:62695276] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:03 (IM:SubscribeRequest) (B:59)
[00:00:43.145][info  ][DMG] Final negotiated min/max parameters: Min = 2s, Max = 600s
[00:00:43.172][info  ][EM] <<< [E:988r S:26069 M:256964189 (Ack:62695276)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:75)
[00:00:43.173][info  ][EM] ??1 [E:988r S:26069 M:256964189] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:43.748][info  ][EM] >>> [E:988r S:26069 M:62695277 (Ack:256964189)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:01 (IM:StatusResponse) (B:42)
[00:00:43.749][info  ][IM] Received status response, status is 0x00
[00:00:43.751][info  ][EM] <<< [E:988r S:26069 M:256964190 (Ack:62695277)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[00:00:43.752][info  ][EM] ??1 [E:988r S:26069 M:256964190] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3362ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:43.753][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000B2B9 and system Timestamp 0x000000000009D2A9.
[00:00:44.352][info  ][EM] >>> [E:988r S:26069 M:62695278 (Ack:256964190)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:44.387][info  ][EM] >>> [E:989r S:26069 M:62695279] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:44.389][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[00:00:44.392][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[00:00:44.405][info  ][TS] Committing Last Known Good Time to storage: 2026-02-06T05:51:15

Missed Logs: 3
[00:00:44.408][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0xFDA99EDEC35D5933, FabricId 670E44471D85389F, NodeId DFBBF9951AA8C8F5, VendorId 0x110A
[00:00:44.409][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[00:00:44.409][info  ][FS] Fail-safe cleanly disarmed
[00:00:44.414][info  ][EM] <<< [E:989r S:26069 M:256964191 (Ack:62695279)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:73)
[00:00:44.416][info  ][EM] ??1 [E:989r S:26069 M:256964191] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3405ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:44.416][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[00:00:44.416][info  ][SWU] Device commissioned, schedule a default provider query
[00:00:44.416][info  ][SVR] Commissioning completed successfully
[00:00:44.416][info  ][DIS] Updating services using commissioning mode 0
[00:00:44.417][info  ][DIS] Advertise operational node FDA99EDEC35D5933-DFBBF9951AA8C8F5
[00:00:44.594][info  ][DL] Disconnect Event for CHIPoBLE on handle : 1
[00:00:44.594][info  ][DL] BLE GATT connection closed (con 1, reason 4118)
[00:00:44.595][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[00:00:44.873][info  ][EM] >>> [E:989r S:26069 M:62695280 (Ack:256964191)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:44.894][info  ][EM] >>> [E:990r S:26069 M:62695281] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:49)
[00:00:44.902][info  ][EM] <<< [E:990r S:26069 M:256964192 (Ack:62695281)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:71)
[00:00:44.903][info  ][EM] ??1 [E:990r S:26069 M:256964192] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3394ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:45.393][info  ][EM] >>> [E:990r S:26069 M:62695282 (Ack:256964192)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:45.416][info  ][EM] >>> [E:991r S:26069 M:62695283] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:45.450][info  ][EM] <<< [E:991r S:26069 M:256964193 (Ack:62695283)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:846)
[00:00:45.452][info  ][EM] ??1 [E:991r S:26069 M:256964193] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3358ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:45.920][info  ][EM] >>> [E:991r S:26069 M:62695284 (Ack:256964193)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:45.942][info  ][EM] >>> [E:992r S:26069 M:62695285] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:45.952][info  ][EM] <<< [E:992r S:26069 M:256964194 (Ack:62695285)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:164)
[00:00:45.953][info  ][EM] ??1 [E:992r S:26069 M:256964194] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3386ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:46.439][info  ][EM] >>> [E:992r S:26069 M:62695286 (Ack:256964194)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:46.465][info  ][EM] >>> [E:993r S:26069 M:62695287] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:46.476][info  ][EM] <<< [E:993r S:26069 M:256964195 (Ack:62695287)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:174)
[00:00:46.478][info  ][EM] ??1 [E:993r S:26069 M:256964195] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3357ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:46.958][info  ][EM] >>> [E:993r S:26069 M:62695288 (Ack:256964195)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:46.980][info  ][EM] >>> [E:994r S:26069 M:62695289] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:46.990][info  ][EM] <<< [E:994r S:26069 M:256964196 (Ack:62695289)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:124)
[00:00:46.991][info  ][EM] ??1 [E:994r S:26069 M:256964196] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3351ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:47.480][info  ][EM] >>> [E:994r S:26069 M:62695290 (Ack:256964196)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:47.503][info  ][EM] >>> [E:995r S:26069 M:62695291] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:46)
[00:00:47.540][info  ][EM] <<< [E:995r S:26069 M:256964197 (Ack:62695291)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:721)
[00:00:47.541][info  ][EM] ??1 [E:995r S:26069 M:256964197] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3331ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:48.000][info  ][EM] >>> [E:995r S:26069 M:62695292 (Ack:256964197)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:48.023][info  ][EM] >>> [E:996r S:26069 M:62695293] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:48.031][info  ][EM] <<< [E:996r S:26069 M:256964198 (Ack:62695293)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:70)
[00:00:48.033][info  ][EM] ??1 [E:996r S:26069 M:256964198] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3344ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:48.519][info  ][EM] >>> [E:996r S:26069 M:62695294 (Ack:256964198)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:48.542][info  ][EM] >>> [E:997r S:26069 M:62695295] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:51)
[00:00:48.555][info  ][EM] <<< [E:997r S:26069 M:256964199 (Ack:62695295)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:70)
[00:00:48.556][info  ][EM] ??1 [E:997r S:26069 M:256964199] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3395ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:49.040][info  ][EM] >>> [E:997r S:26069 M:62695296 (Ack:256964199)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:49.060][info  ][EM] >>> [E:998r S:26069 M:62695297] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:49.070][info  ][EM] <<< [E:998r S:26069 M:256964200 (Ack:62695297)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:126)
[00:00:49.072][info  ][EM] ??1 [E:998r S:26069 M:256964200] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3368ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:49.559][info  ][EM] >>> [E:998r S:26069 M:62695298 (Ack:256964200)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:49.609][info  ][EM] >>> [E:999r S:26069 M:62695299] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[00:00:49.612][info  ][ZCL] OpCreds: Received an UpdateFabricLabel command
[00:00:49.613][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[00:00:49.617][info  ][EM] <<< [E:999r S:26069 M:256964201 (Ack:62695299)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:09 (IM:InvokeCommandResponse) (B:73)
[00:00:49.618][info  ][EM] ??1 [E:999r S:26069 M:256964201] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3377ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:50.112][info  ][EM] >>> [E:999r S:26069 M:62695300 (Ack:256964201)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:55.104][info  ][EM] >>> [E:1000r S:26069 M:62695301] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:55.122][info  ][EM] <<< [E:1000r S:26069 M:256964202 (Ack:62695301)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:477)
[00:00:55.124][info  ][EM] ??1 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3357ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:55.151][info  ][EM] >>> [E:1001r S:26069 M:62695302] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:55.157][info  ][EM] <<< [E:1001r S:26069 M:256964203 (Ack:62695302)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:41)
[00:00:55.159][info  ][EM] ??1 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3365ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:55.219][info  ][EM] >>> [E:1002r S:26069 M:62695303] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:06 (IM:WriteRequest) (B:83)
[00:00:55.226][info  ][EM] <<< [E:1002r S:26069 M:256964204 (Ack:62695303)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:07 (IM:WriteResponse) (B:62)
[00:00:55.228][info  ][EM] ??1 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3361ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:55.251][info  ][EM] >>> [E:1003r S:26069 M:62695304] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:55.271][info  ][EM] <<< [E:1003r S:26069 M:256964205 (Ack:62695304)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:477)
[00:00:55.272][info  ][EM] ??1 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3407ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:55.289][info  ][EM] >>> [E:1004r S:26069 M:62695305] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:03 (IM:SubscribeRequest) (B:57)
[00:00:55.290][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[00:00:55.308][info  ][DMG] Subscription id 0xdbfbfebb from node <8CBDA24D2F21C48C, 1> torn down
[00:00:55.311][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[00:00:55.337][info  ][EM] <<< [E:1004r S:26069 M:256964206 (Ack:62695305)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:74)
[00:00:55.339][info  ][EM] ??1 [E:1004r S:26069 M:256964206] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3345ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:56.038][info  ][EM] >>> [E:1005r S:0 M:29120873] (U) Msg RX from 0:37D30F1CB0754457 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:234)
[00:00:56.039][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x20008a90
[00:00:56.040][info  ][EM] <<< [E:1005r S:0 M:81285825 (Ack:29120873)] (U) Msg TX from 0000000000000000 to 0:37D30F1CB0754457 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:56.041][info  ][SC] Received Sigma1 msg
[00:00:56.054][info  ][EM] <<< [E:1005r S:0 M:81285826 (Ack:29120873)] (U) Msg TX from 0000000000000000 to 0:37D30F1CB0754457 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:33 (SecureChannel:CASE_Sigma2Resume) (B:99)
[00:00:56.055][info  ][EM] ??1 [E:1005r S:0 M:81285826] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3352ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:56.056][info  ][SC] Sent Sigma2Resume msg
[00:00:56.537][info  ][EM] >>> [E:1005r S:0 M:29120874 (Ack:81285826)] (U) Msg RX from 0:37D30F1CB0754457 [0000] to 0000000000000000 --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[00:00:56.538][info  ][SC] Success status report received. Session was established
[00:00:56.548][info  ][SC] SecureSession[0x20006f20, LSID:26070]: State change 'kEstablishing' --> 'kActive'
[00:00:56.549][info  ][IN] CASE Session established to peer: <8CBDA24D2F21C48C, 1>
[00:00:56.551][info  ][EM] <<< [E:1005r S:0 M:81285827 (Ack:29120874)] (U) Msg TX from 0000000000000000 to 0:37D30F1CB0754457 [0000] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[00:00:56.552][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:56.580][info  ][EM] >>> [E:1006r S:26070 M:70227163] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:03 (IM:SubscribeRequest) (B:75)
[00:00:56.581][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[00:00:56.599][info  ][DMG] Subscription id 0x2bbc5f9f from node <8CBDA24D2F21C48C, 1> torn down
[00:00:56.607][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[00:00:56.642][info  ][EM] <<< [E:1006r S:26070 M:45591343 (Ack:70227163)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:182)
[00:00:56.644][info  ][EM] ??1 [E:1006r S:26070 M:45591343] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3409ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:57.059][info  ][EM] >>> [E:1006r S:26070 M:70227164 (Ack:45591343)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:01 (IM:StatusResponse) (B:42)
[00:00:57.060][info  ][IM] Received status response, status is 0x00
[00:00:57.063][info  ][EM] <<< [E:1006r S:26070 M:45591344 (Ack:70227164)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[00:00:57.065][info  ][EM] ??1 [E:1006r S:26070 M:45591344] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3372ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:57.065][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000DEE9 and system Timestamp 0x00000000000A06A9.
[00:00:57.564][info  ][EM] >>> [E:1006r S:26070 M:70227165 (Ack:45591344)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:57.593][info  ][EM] >>> [E:1007r S:26070 M:70227166] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:57.612][info  ][EM] <<< [E:1007r S:26070 M:45591345 (Ack:70227166)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:477)
[00:00:57.614][info  ][EM] ??1 [E:1007r S:26070 M:45591345] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3337ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:57.645][info  ][EM] >>> [E:1008r S:26070 M:70227167] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:03 (IM:SubscribeRequest) (B:84)
[00:00:57.647][info  ][IM] Deleting previous active subscription from NodeId: 8CBDA24D2F21C48C, FabricIndex: 1
[00:00:57.666][info  ][DMG] Subscription id 0x63a57dc7 from node <8CBDA24D2F21C48C, 1> torn down
[00:00:57.675][info  ][DMG] Final negotiated min/max parameters: Min = 0s, Max = 600s
[00:00:57.715][info  ][EM] <<< [E:1008r S:26070 M:45591346 (Ack:70227167)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:236)
[00:00:57.717][info  ][EM] ??1 [E:1008r S:26070 M:45591346] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3330ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:57.742][info  ][EM] >>> [E:1009r S:26070 M:70227168] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:57.760][info  ][EM] <<< [E:1009r S:26070 M:45591347 (Ack:70227168)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:477)
[00:00:57.761][info  ][EM] ??1 [E:1009r S:26070 M:45591347] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3369ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.237][info  ][EM] >>> [E:1007r S:26070 M:70227169 (Ack:45591345)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:58.260][info  ][EM] >>> [E:1008r S:26070 M:70227170 (Ack:45591346)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:01 (IM:StatusResponse) (B:42)
[00:00:58.261][info  ][IM] Received status response, status is 0x00
[00:00:58.264][info  ][EM] <<< [E:1008r S:26070 M:45591348 (Ack:70227170)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:04 (IM:SubscribeResponse) (B:49)
[00:00:58.266][info  ][EM] ??1 [E:1008r S:26070 M:45591348] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3389ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.266][info  ][DMG] Registered a ReadHandler that will schedule a report between system Timestamp: 0x000000000000E39A and system Timestamp 0x00000000000A0B5A.
[00:00:58.280][info  ][EM] >>> [E:1009r S:26070 M:70227171 (Ack:45591347)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:58.315][info  ][EM] >>> [E:1010r S:26070 M:70227172] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:02 (IM:ReadRequest) (B:48)
[00:00:58.456][info  ][EM] <<< [E:1010r S:26070 M:45591349 (Ack:70227172)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:1199)
[00:00:58.458][info  ][EM] ??1 [E:1010r S:26070 M:45591349] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3397ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.458][error ][DL] Long dispatch time: 140 ms, for event type 3
[00:00:58.481][info  ][EM] <<1 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:00:58.482][info  ][EM] ??2 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3387ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.496][info  ][EM] >>> [E:1008r S:26070 M:70227173 (Ack:45591348)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:00:58.524][info  ][EM] <<1 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:00:58.525][info  ][EM] ??2 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3351ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.589][info  ][EM] <<1 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:00:58.590][info  ][EM] ??2 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3365ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.679][info  ][EM] <<1 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:00:58.680][info  ][EM] ??2 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3400ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:58.995][info  ][EM] >>> [E:1010r S:26070 M:70227174 (Ack:45591349)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0001:01 (IM:StatusResponse) (B:42)
[00:00:58.996][info  ][IM] Received status response, status is 0x00
[00:00:59.094][info  ][EM] <<< [E:1010r S:26070 M:45591350 (Ack:70227174)] (S) Msg TX from DFBBF9951AA8C8F5 to 1:8CBDA24D2F21C48C [5933] [UDP:[fddc:8360:97e9:1:8174:a1c6:1ab8:5e81]:42257] --- Type 0001:05 (IM:ReportData) (B:962)
[00:00:59.097][info  ][EM] ??1 [E:1010r S:26070 M:45591350] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3339ms from now [State:Active II:500 AI:300 AT:4000]
[00:00:59.097][error ][DL] Long dispatch time: 101 ms, for event type 3
[00:00:59.489][info  ][EM] >>> [E:1010r S:26070 M:70227175 (Ack:45591350)] (S) Msg RX from 1:8CBDA24D2F21C48C [5933] to DFBBF9951AA8C8F5 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[00:01:01.869][info  ][EM] <<2 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:01.870][info  ][EM] ??3 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3598ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:01.876][info  ][EM] <<2 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:01.877][info  ][EM] ??3 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3528ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:01.955][info  ][EM] <<2 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:01.956][info  ][EM] ??3 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3614ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:02.080][info  ][EM] <<2 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:02.081][info  ][EM] ??3 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3583ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:05.405][info  ][EM] <<3 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:05.406][info  ][EM] ??4 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4013ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:05.468][info  ][EM] <<3 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:05.469][info  ][EM] ??4 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3914ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:05.570][info  ][EM] <<3 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:05.571][info  ][EM] ??4 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4041ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:05.664][info  ][EM] <<3 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:05.665][info  ][EM] ??4 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 3886ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:09.383][info  ][EM] <<4 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:09.384][info  ][EM] ??5 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4523ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:09.419][info  ][EM] <<4 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:09.421][info  ][EM] ??5 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4676ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:09.551][info  ][EM] <<4 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:09.552][info  ][EM] ??5 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4432ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:09.612][info  ][EM] <<4 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C
[00:01:09.613][info  ][EM] ??5 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C scheduled for 4567ms from now [State:Idle II:500 AI:300 AT:4000]
[00:01:13.907][error ][EM] <<5 [E:1000r S:26069 M:256964202] (S) Msg Retransmission to 1:8CBDA24D2F21C48C failure (max retries:4)
[00:01:13.907][info  ][SC] SecureSession[0x20006e48, LSID:26069]: State change 'kActive' --> 'kDefunct'
[00:01:13.984][error ][EM] <<5 [E:1003r S:26069 M:256964205] (S) Msg Retransmission to 1:8CBDA24D2F21C48C failure (max retries:4)
[00:01:14.097][error ][EM] <<5 [E:1001r S:26069 M:256964203] (S) Msg Retransmission to 1:8CBDA24D2F21C48C failure (max retries:4)
[00:01:14.180][error ][EM] <<5 [E:1002r S:26069 M:256964204] (S) Msg Retransmission to 1:8CBDA24D2F21C48C failure (max retries:4)
[00:01:14.416][error ][SWU] No suitable OTA Provider candidate found
[00:01:14.416][info  ][SWU] No provider available

```