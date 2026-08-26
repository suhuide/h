```c
[00:00:00.077][info  ][DL] Starting scheduler
[00:00:00.077][info  ][DL] ==================================================
[00:00:00.077][info  ][DL]  starting
[00:00:00.077][info  ][DL] ==================================================
[00:00:00.077][info  ][DL] Init CHIP Stack
[00:00:00.079][info  ][DL] Provision mode disabled
[00:00:00.079][info  ][DL] Initializing OpenThread stack
[00:00:00.080][info  ][DL] OpenThread started: OK
[00:00:00.080][info  ][DL] Setting OpenThread device type to ROUTER
[00:00:00.137][info  ][DL] Bluetooth stack booted: v11.0.2-b0
[00:00:00.137][info  ][DL] RAIL version:, v3.0.3-b0
[00:00:00.138][silabs ]BLE: product type [Pergolux]
[00:00:00.156][silabs ]BLE: MTU size 249
[00:00:00.156][detail][DL] CHIP event task running
[00:00:00.157][info  ][SVR] Current Software Version String: 1.0.1
[00:00:00.157][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[00:00:00.157][detail][DL] OpenThread State Changed (Flags: 0x00038210)
[00:00:00.158][detail][DL]    Network Name: OpenThread
[00:00:00.158][detail][DL]    PAN Id: 0xFFFF
[00:00:00.158][detail][DL]    Extended PAN Id: 0xDEAD00BEEF00CAFE
[00:00:00.158][detail][DL]    Channel: 11

Missed Logs: 1
[00:00:00.158][detail][DL]    Mesh Prefix: fdde:ad00:beef:0:0:0:0:0/64

Missed Logs: 3
[00:00:00.159][info  ][SVR] Current Software Version: 10001
[00:00:00.159][info  ][DL] Device Configuration:
[00:00:00.159][info  ][DL]   Serial Number: 29FBB744AC11619C
[00:00:00.160][info  ][DL]   Vendor Id: 5232 (0x1470)
[00:00:00.160][info  ][DL]   Product Id: 65281 (0xFF01)
[00:00:00.160][info  ][DL]   Product Name: Window Covering
[00:00:00.161][info  ][DL]   Hardware Version: 1
[00:00:00.161][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[00:00:00.161][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 2273 (0x8E1)
[00:00:00.162][info  ][DL]   Device Type: 65535 (0xFFFF)
matterCli> [00:00:00.167][silabs ]CTM: Ver: 10001 Build:  # Time:Aug 13 2026 11:48:18
[00:00:00.172][silabs ]CTM: Btl Ver: core: v3.0 user: v3
[00:00:00.177][silabs ] Reset Reason: 0x00000000
[00:00:00.182][silabs ] Tx power 10dBm
[00:00:00.187][silabs ]SetupQRCode: [MT:K2CA023L01GG.V5I600]
[00:00:00.188][info  ][DL] Configuring BLE Channel
[00:00:00.188][detail][DL] BLE Static Device Address D1:13:93:C1:7F:B1
[00:00:00.189][silabs ]BLE: _create_second_adv, adv Handle = 0, interval 320/400 (units of 0.625ms)
[00:00:00.189][silabs ]BLE: advertiser start without white list
[00:00:00.191][silabs ]COM: Init done
[00:00:00.192][silabs ]NWK: open basic commissioning window time 300 sec
[00:00:00.193][detail][IN] SecureSession[0x20007be8]: Allocated Type:1 LSID:54081
[00:00:00.194][detail][SC] Assigned local session key ID 54081
[00:00:00.194][detail][SC] Waiting for PBKDF param request
[00:00:00.194][info  ][DIS] Updating services using commissioning mode 1
[00:00:00.194][error ][DIS] Failed to remove advertised services: 3
[00:00:00.194][detail][DL] Using Thread extended MAC for hostname.
[00:00:00.195][detail][DIS] DNS-SD Pairing Instruction not set
[00:00:00.195][info  ][DIS] Advertise commission parameter vendorID=5232 productID=65281 discriminator=2273/08 cm=1 cp=0 jf=0
[00:00:00.195][error ][DIS] Failed to advertise commissionable node: 3
[00:00:00.195][error ][DIS] Failed to finalize service update: 3
[00:00:00.196][detail][DL] Start BLE advertisement
[00:00:00.196][info  ][DL] BLE Static Device Address FC:B1:19:A3:B2:3F

Missed Logs: 1
[00:00:00.197][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)
[00:00:00.198][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:00.198][silabs ]NWK: platform event type 800d
[00:00:00.199][silabs ]COM: notify network [Leave]
[00:00:00.200][detail][DMG] Endpoint 1, Cluster 0x0000_0102 update version to 75db0ee8
[00:00:00.200][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[00:00:00.202][detail][DMG] Endpoint 1, Cluster 0x0000_0102 update version to 75db0ee9
[00:00:00.202][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[00:00:00.202][silabs ]App Task started
[00:00:00.203][silabs ] MATTER TX: : 55 aa 02 00 00 02 00 01 00 04 

[16:16:27.222]�ա���[00:00:00.303][silabs ] MATTER TX: : 55 aa 02 00 01 04 00 08 12 02 00 04 00 00 00 00 26 
[00:00:00.303][silabs ]COM: CMD: 0x04, SN: 1, LEN: 17


[16:16:27.373]�ա���[00:00:00.455][silabs ] MATTER RX: : 55 aa 02 00 09 05 00 08 12 02 00 04 00 00 00 01 30 
[00:00:00.455][silabs ]COM: device report ID: 0x12 TYPE: 2 LEN: 4 [passive]
[00:00:00.455][silabs ]COM: [00-00-00-01]:curtain_num=1 switch_num=0 light_num=0
[00:00:00.455][silabs ]COM: light1[--:--] light2[--:--] light3[--:--]
[00:00:00.456][silabs ]EP: wc_num=1 plug_num=0 rgb_num=0 led_num=0
[00:00:00.456][silabs ]EP: EP_config(len=35).
[00:00:00.456][silabs ] CFG: ef ab 08 00 00 00 01 01 00 01 01 02 00 02 00 03 00 03 00 04 00 04 00 05 00 05 00 06 00 06 00 07 00 
[00:00:00.457][silabs ]EP: EP_token(len=35).
[00:00:00.457][silabs ] CFG: ef ab 08 00 00 00 01 01 00 01 01 02 00 02 00 03 00 03 00 04 00 04 00 05 00 05 00 06 00 06 00 07 00 
[00:00:00.458][silabs ]EP: EPConfig == NVM3 Token.


[16:16:29.118]�ա���[00:00:02.200][silabs ] MATTER TX: : 9a 52 05 00 00 00 00 00 cd 
[00:00:02.205][silabs ]COM: got device info 0 0

[16:16:29.270]�ա���[00:00:02.352][silabs ]BLE: mcu2host type=0x52 len=10
[00:00:02.352][silabs ]COM: mcu2host: 02 00 01 00 00 00 80 00 00 00 

[16:16:34.031]�ա���[00:00:07.113][info  ][DL] Connect Event for CHIPoBLE on handle : 2
[00:00:07.114][info  ][DL] Connection Parameters Event for handle : 2
[00:00:07.114][info  ][DL] Connection parameter ID received - i:24, l:0, t:72, sm:0
[00:00:07.114][info  ][DL] Renegotiate BLE connection parameters to minInterval:16, maxInterval:80, timeout:100
[00:00:07.114][info  ][DL] Connection phy status ID received - phy:1

[16:16:34.158]�ա���[00:00:07.241][info  ][DL] Connection data length ID received - txL:251, txT:2120, rxL:251, rxL:2120

[16:16:34.338]�ա���[00:00:07.420][info  ][DL] Connection Parameters Event for handle : 2
[00:00:07.420][info  ][DL] Connection parameter ID received - i:72, l:0, t:100, sm:0

[16:16:35.448]�ա���[00:00:08.531][info  ][DL] Connection phy status ID received - phy:2

[16:16:36.801]�ա���[00:00:09.880][info  ][DL] Handling CCCD Write
[00:00:09.881][error ][-] mConnectionState.allocated:456 false: 3
[00:00:09.881][error ][-] Error CHIP:0x00000003 at C:/Users/huide/.silabs/slt/installs/conan/p/matte8bada656e9e76/p/third_party/matter_sdk/src/platform/silabs/efr32/BLEChannelImpl.cpp:329

[16:16:37.159]�ա���[00:00:10.241][info  ][DL] Char Write Req, char : 49
[00:00:10.241][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 9)
[00:00:10.242][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:10.242][info  ][BLE] local and remote recv window sizes = 5
[00:00:10.243][info  ][BLE] selected BTP version 4
[00:00:10.243][info  ][BLE] using BTP fragment sizes rx 244 / tx 244.

[16:16:37.519]�ա���[00:00:10.601][info  ][DL] HandleTXcharCCCDWrite - Config Flags value : 2
[00:00:10.601][info  ][DL] CHIPoBLE subscribe received
[00:00:10.601][info  ][DL] _OnPlatformEvent kCHIPoBLESubscribe
[00:00:10.602][detail][IN] BLE EndPoint 0x20015a68 Connection Complete
[00:00:10.602][info  ][DL] _OnPlatformEvent default:  event->Type = 32774
[00:00:10.602][silabs ]NWK: platform event type 8006
[00:00:10.602][silabs ]COM: notify network [Leave]
[00:00:10.603][silabs ] MATTER TX: : 55 aa 02 00 02 02 00 01 00 06 
[00:00:10.603][silabs ]COM: CMD: 0x02, SN: 2, LEN: 10


[16:16:37.698]�ա���[00:00:10.781][info  ][DL] Tx Confirmation received
[00:00:10.781][info  ][DL]  stop soft timer
[00:00:10.781][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:10.782][info  ][DL] Char Write Req, char : 49
[00:00:10.783][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 103)
[00:00:10.783][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:10.783][info  ][EM] >>> [E:16876r S:0 M:72900103] (U) Msg RX from 0:8BABE1FE5FDD9619 [0000] to 0000000000000000 --- Type 0000:20 (SecureChannel:PBKDFParamRequest) (B:98)
[00:00:10.784][detail][EM] Handling via exchange: 16876r, Delegate: 0x2000a370
[00:00:10.784][detail][SC] Received PBKDF param request
[00:00:10.784][detail][SC] Peer assigned session ID 24517
[00:00:10.785][detail][SC] Found MRP parameters in the message
[00:00:10.787][info  ][EM] <<< [E:16876r S:0 M:31346289] (U) Msg TX from 0000000000000000 to 0:8BABE1FE5FDD9619 [0000] [BLE] --- Type 0000:21 (SecureChannel:PBKDFParamResponse) (B:154)
[00:00:10.787][detail][SC] Sent PBKDF param response
[00:00:10.787][info  ][SVR] Commissioning session establishment step started

[16:16:37.968]�ա���[00:00:11.050][info  ][DL] Tx Confirmation received
[00:00:11.050][info  ][DL]  stop soft timer
[00:00:11.052][info  ][DL] Char Write Req, char : 49
[00:00:11.052][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 97)
[00:00:11.052][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:11.052][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:11.053][info  ][EM] >>> [E:16876r S:0 M:72900104] (U) Msg RX from 0:8BABE1FE5FDD9619 [0000] to 0000000000000000 --- Type 0000:22 (SecureChannel:PASE_Pake1) (B:92)
[00:00:11.053][detail][EM] Found matching exchange: 16876r, Delegate: 0x2000a370
[00:00:11.053][detail][SC] Received spake2p msg1

[16:16:38.030]�ա���[00:00:11.112][info  ][EM] <<< [E:16876r S:0 M:31346290] (U) Msg TX from 0000000000000000 to 0:8BABE1FE5FDD9619 [0000] [BLE] --- Type 0000:23 (SecureChannel:PASE_Pake2) (B:127)
[00:00:11.113][detail][SC] Sent spake2p msg2

[16:16:38.149]�ա���[00:00:11.231][info  ][DL] Tx Confirmation received
[00:00:11.231][info  ][DL]  stop soft timer
[00:00:11.232][info  ][DL] Char Write Req, char : 49
[00:00:11.232][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 64)
[00:00:11.232][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:11.233][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:11.233][info  ][EM] >>> [E:16876r S:0 M:72900105] (U) Msg RX from 0:8BABE1FE5FDD9619 [0000] to 0000000000000000 --- Type 0000:24 (SecureChannel:PASE_Pake3) (B:59)
[00:00:11.233][detail][EM] Found matching exchange: 16876r, Delegate: 0x2000a370
[00:00:11.234][detail][SC] Received spake2p msg3
[00:00:11.234][detail][SC] Sending status report. Protocol code 0, exchange 16876
[00:00:11.235][info  ][EM] <<< [E:16876r S:0 M:31346291] (U) Msg TX from 0000000000000000 to 0:8BABE1FE5FDD9619 [0000] [BLE] --- Type 0000:40 (SecureChannel:StatusReport) (B:30)
[00:00:11.239][info  ][SC] SecureSession[0x20007be8, LSID:54081]: State change 'kEstablishing' --> 'kActive'

Missed Logs: 1
[00:00:11.239][detail][IN] SecureSession[0x20007be8]: Activated - Type:1 LSID:54081
[00:00:11.240][detail][IN] New secure session activated for device <FFFFFFFB00000000, 0>, LSID:54081 PSID:24517!
[00:00:11.240][info  ][SVR] Commissioning completed session establishment step
[00:00:11.240][info  ][DIS] Updating services using commissioning mode 0
[00:00:11.240][error ][DIS] Failed to remove advertised services: 3
[00:00:11.241][error ][DIS] Failed to finalize service update: 3
[00:00:11.241][info  ][SVR] Device completed Rendezvous process
[00:00:11.241][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[00:00:11.241][silabs ]NWK: platform event type 8018
[00:00:11.242][info  ][DL] _OnPlatformEvent default:  event->Type = 32781

[16:16:38.328]�ա���[00:00:11.411][info  ][DL] Tx Confirmation received
[00:00:11.411][info  ][DL]  stop soft timer
[00:00:11.411][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:11.413][info  ][DL] Char Write Req, char : 49
[00:00:11.413][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 141)
[00:00:11.413][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:11.415][info  ][EM] >>> [E:16877r S:54081 M:90312241] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:136)
[00:00:11.416][detail][EM] Handling via exchange: 16877r, Delegate: 0x20004cf4
[00:00:11.416][detail][IM] Received Read request
[00:00:11.419][detail][DMG] IM RH moving to [CanStartReporting]
[00:00:11.419][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[00:00:11.420][detail][DMG] <RE:Run> Cluster 28, Attribute 4 is dirty
[00:00:11.421][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[00:00:11.422][detail][DMG] <RE:Run> Cluster 28, Attribute 2 is dirty
[00:00:11.423][detail][DMG] Reading attribute: Cluster=0x0000_0028 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[00:00:11.424][detail][DMG] <RE:Run> Cluster 30, Attribute c is dirty
[00:00:11.425][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0030, attributeId: 0x0000_000Cerr = 586
[00:00:11.426][detail][DMG] <RE:Run> Cluster 30, Attribute 3 is dirty
[00:00:11.427][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=0)
[00:00:11.428][detail][DMG] <RE:Run> Cluster 30, Attribute 2 is dirty
[00:00:11.428][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=0)
[00:00:11.429][detail][DMG] <RE:Run> Cluster 30, Attribute 1 is dirty
[00:00:11.430][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=0)
[00:00:11.431][detail][DMG] <RE:Run> Cluster 30, Attribute 0 is dirty
[00:00:11.432][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[00:00:11.433][detail][DMG] <RE:Run> Cluster 30, Attribute 4 is dirty
[00:00:11.433][detail][DMG] Reading attribute: Cluster=0x0000_0030 Endpoint=0x0 AttributeId=0x0000_0004 (expanded=0)
[00:00:11.434][detail][DMG] <RE> Sending report (payload has 223 bytes)...
[00:00:11.436][info  ][EM] <<< [E:16877r S:54081 M:95271716] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:253)
[00:00:11.437][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[00:00:11.437][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[00:00:11.437][detail][DMG] IM RH moving to [AwaitingDestruction]
[00:00:11.437][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet

[16:16:38.509]�ա���[00:00:11.590][info  ][DL] Tx Confirmation received
[00:00:11.591][info  ][DL]  stop soft timer
[00:00:11.591][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:38.688]�ա���[00:00:11.771][info  ][DL] Tx Confirmation received
[00:00:11.771][info  ][DL]  stop soft timer
[00:00:11.771][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:11.772][info  ][DL] Char Write Req, char : 49
[00:00:11.772][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 139)
[00:00:11.773][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:11.775][info  ][EM] >>> [E:16878r S:54081 M:90312242] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:134)
[00:00:11.775][detail][EM] Handling via exchange: 16878r, Delegate: 0x20004cf4
[00:00:11.775][detail][IM] Received Read request
[00:00:11.779][detail][DMG] IM RH moving to [CanStartReporting]
[00:00:11.779][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[00:00:11.780][detail][DMG] <RE:Run> Cluster 1349fc00, Attribute 1 is dirty
[00:00:11.781][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.781][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x1349_FC00, attributeId: 0x0000_0001err = 5c3
[00:00:11.782][detail][DMG] <RE:Run> Cluster 46, Attribute 2 is dirty
[00:00:11.783][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.783][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0002err = 5c3
[00:00:11.784][detail][DMG] <RE:Run> Cluster 46, Attribute 1 is dirty
[00:00:11.785][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.785][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0001err = 5c3
[00:00:11.786][detail][DMG] <RE:Run> Cluster 46, Attribute 0 is dirty
[00:00:11.787][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.787][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0000err = 5c3
[00:00:11.788][detail][DMG] <RE:Run> Cluster 46, Attribute 7 is dirty
[00:00:11.789][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.790][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0007err = 5c3
[00:00:11.791][detail][DMG] <RE:Run> Cluster 46, Attribute 6 is dirty
[00:00:11.791][error ][DMG] Read request on unknown cluster - no data version available
[00:00:11.791][error ][DMG] Fail to retrieve data, roll back and encode status on clusterId: 0x0000_0046, attributeId: 0x0000_0006err = 5c3

Missed Logs: 2
[00:00:11.792][detail][DMG] <RE:Run> Cluster 31, Attribute 2 is dirty
[00:00:11.792][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0002 (expanded=1)
[00:00:11.793][detail][DMG] <RE:Run> Cluster 31, Attribute 3 is dirty
[00:00:11.794][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0003 (expanded=1)
[00:00:11.795][detail][DMG] <RE:Run> Cluster 31, Attribute fffc is dirty
[00:00:11.796][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_FFFC (expanded=1)
[00:00:11.797][detail][DMG] <RE> Sending report (payload has 230 bytes)...
[00:00:11.799][info  ][EM] <<< [E:16878r S:54081 M:95271717] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:260)
[00:00:11.799][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[00:00:11.800][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages

[16:16:38.868]�ա���[00:00:11.951][info  ][DL] Tx Confirmation received
[00:00:11.951][info  ][DL]  stop soft timer
[00:00:11.952][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:39.048]�ա���[00:00:12.130][info  ][DL] Tx Confirmation received
[00:00:12.130][info  ][DL]  stop soft timer
[00:00:12.131][info  ][DL] Char Write Req, char : 49
[00:00:12.132][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 64)
[00:00:12.132][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:12.132][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:12.134][info  ][EM] >>> [E:16879r S:54081 M:90312243] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:02 (IM:ReadRequest) (B:59)
[00:00:12.135][detail][EM] Handling via exchange: 16879r, Delegate: 0x20004cf4
[00:00:12.135][detail][IM] Received Read request
[00:00:12.136][detail][DMG] IM RH moving to [CanStartReporting]
[00:00:12.136][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000000 DirtyGeneration = 0x0000000000000000
[00:00:12.137][detail][DMG] <RE:Run> Cluster 31, Attribute 1 is dirty
[00:00:12.138][detail][DMG] Reading attribute: Cluster=0x0000_0031 Endpoint=0x0 AttributeId=0x0000_0001 (expanded=1)
[00:00:12.139][detail][DMG] <RE:Run> Cluster 33, Attribute 0 is dirty
[00:00:12.140][detail][DMG] Reading attribute: Cluster=0x0000_0033 Endpoint=0x0 AttributeId=0x0000_0000 (expanded=0)
[00:00:12.140][detail][DMG] <RE> Sending report (payload has 103 bytes)...
[00:00:12.142][info  ][EM] <<< [E:16879r S:54081 M:95271718] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:05 (IM:ReportData) (B:133)
[00:00:12.143][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[00:00:12.144][detail][DMG] <RE> ReportsInFlight = 0 with readHandler 0, RE has no more messages
[00:00:12.144][detail][DMG] IM RH moving to [AwaitingDestruction]
[00:00:12.144][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet

[16:16:39.228]�ա���[00:00:12.311][info  ][DL] Tx Confirmation received
[00:00:12.311][info  ][DL]  stop soft timer
[00:00:12.312][info  ][DL] Char Write Req, char : 49
[00:00:12.312][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[00:00:12.312][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:12.313][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:12.315][info  ][EM] >>> [E:16880r S:54081 M:90312244] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:12.315][detail][EM] Handling via exchange: 16880r, Delegate: 0x20004cf4
[00:00:12.316][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[00:00:12.317][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[00:00:12.317][detail][DMG] Command handler moving to [NewRespons]
[00:00:12.317][detail][DMG] Command handler moving to [ Preparing]
[00:00:12.317][detail][DMG] Command handler moving to [AddingComm]
[00:00:12.317][detail][DMG] Command handler moving to [AddedComma]
[00:00:12.318][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:12.318][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:12.318][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:12.320][info  ][EM] <<< [E:16880r S:54081 M:95271719] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:12.321][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:39.409]�ա���[00:00:12.491][info  ][DL] Tx Confirmation received
[00:00:12.491][info  ][DL]  stop soft timer
[00:00:12.492][info  ][DL] Char Write Req, char : 49
[00:00:12.493][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 75)
[00:00:12.493][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:12.493][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:12.495][info  ][EM] >>> [E:16881r S:54081 M:90312245] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[00:00:12.495][detail][EM] Handling via exchange: 16881r, Delegate: 0x20004cf4
[00:00:12.497][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0002
[00:00:12.497][detail][DMG] Command handler moving to [NewRespons]
[00:00:12.497][detail][DMG] Command handler moving to [ Preparing]
[00:00:12.497][detail][DMG] Command handler moving to [AddingComm]
[00:00:12.498][detail][DMG] Command handler moving to [AddedComma]
[00:00:12.498][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:12.498][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:12.499][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:12.500][info  ][EM] <<< [E:16881r S:54081 M:95271720] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:12.500][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:39.588]�ա���[00:00:12.670][info  ][DL] Tx Confirmation received
[00:00:12.670][info  ][DL]  stop soft timer
[00:00:12.672][info  ][DL] Char Write Req, char : 49
[00:00:12.672][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[00:00:12.672][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:12.672][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:12.675][info  ][EM] >>> [E:16882r S:54081 M:90312246] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:12.675][detail][EM] Handling via exchange: 16882r, Delegate: 0x20004cf4
[00:00:12.676][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[00:00:12.676][info  ][ZCL] OpCreds: Certificate Chain request received for PAI
[00:00:12.677][info  ][DL] GetProductAttestationIntermediateCert, addr:0x817e000+512, size:470
[00:00:12.677][detail][DMG] Command handler moving to [NewRespons]
[00:00:12.677][detail][DMG] Command handler moving to [ Preparing]
[00:00:12.677][detail][DMG] Command handler moving to [AddingComm]
[00:00:12.678][detail][DMG] Command handler moving to [AddedComma]
[00:00:12.678][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:12.678][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:12.678][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:12.680][info  ][EM] <<< [E:16882r S:54081 M:95271721] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:534)
[00:00:12.681][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:39.862]�ա���[00:00:12.941][info  ][DL] Tx Confirmation received
[00:00:12.941][info  ][DL]  stop soft timer
[00:00:12.941][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:40.038]�ա���[00:00:13.121][info  ][DL] Tx Confirmation received
[00:00:13.121][info  ][DL]  stop soft timer
[00:00:13.122][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:40.219]�ա���[00:00:13.300][info  ][DL] Tx Confirmation received
[00:00:13.301][info  ][DL]  stop soft timer
[00:00:13.302][info  ][DL] Char Write Req, char : 49
[00:00:13.302][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 67)
[00:00:13.302][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:13.303][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:13.305][info  ][EM] >>> [E:16883r S:54081 M:90312247] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:62)
[00:00:13.305][detail][EM] Handling via exchange: 16883r, Delegate: 0x20004cf4
[00:00:13.306][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0002
[00:00:13.306][info  ][ZCL] OpCreds: Certificate Chain request received for DAC
[00:00:13.307][info  ][DL] GetDeviceAttestationCert, addr:0x817e000+000, size:481
[00:00:13.307][detail][DMG] Command handler moving to [NewRespons]
[00:00:13.307][detail][DMG] Command handler moving to [ Preparing]
[00:00:13.307][detail][DMG] Command handler moving to [AddingComm]
[00:00:13.308][detail][DMG] Command handler moving to [AddedComma]
[00:00:13.308][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:13.308][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:13.308][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:13.310][info  ][EM] <<< [E:16883r S:54081 M:95271722] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:545)
[00:00:13.311][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:40.398]�ա���[00:00:13.481][info  ][DL] Tx Confirmation received
[00:00:13.481][info  ][DL]  stop soft timer
[00:00:13.482][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:40.578]�ա���[00:00:13.661][info  ][DL] Tx Confirmation received
[00:00:13.662][info  ][DL]  stop soft timer
[00:00:13.662][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:40.758]�ա���[00:00:13.840][info  ][DL] Tx Confirmation received
[00:00:13.841][info  ][DL]  stop soft timer
[00:00:13.841][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:13.842][info  ][DL] Char Write Req, char : 49
[00:00:13.842][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[00:00:13.842][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:13.845][info  ][EM] >>> [E:16884r S:54081 M:90312248] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:13.845][detail][EM] Handling via exchange: 16884r, Delegate: 0x20004cf4
[00:00:13.846][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0000
[00:00:13.846][info  ][ZCL] OpCreds: Received an AttestationRequest command
[00:00:13.847][info  ][DL] GetCertificationDeclaration, addr:0x817e000+1024, size:244
[00:00:13.853][info  ][DL] SignWithDeviceAttestationKey, kid:2, msg_size:303, sig_size:64, err:0x00
[00:00:13.854][info  ][ZCL] OpCreds: AttestationRequest successful.
[00:00:13.854][detail][DMG] Command handler moving to [NewRespons]
[00:00:13.854][detail][DMG] Command handler moving to [ Preparing]
[00:00:13.854][detail][DMG] Command handler moving to [AddingComm]
[00:00:13.854][detail][DMG] Command handler moving to [AddedComma]
[00:00:13.855][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:13.855][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:13.855][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:13.857][info  ][EM] <<< [E:16884r S:54081 M:95271723] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:418)
[00:00:13.858][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:40.938]�ա���[00:00:14.021][info  ][DL] Tx Confirmation received
[00:00:14.021][info  ][DL]  stop soft timer
[00:00:14.021][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:41.118]�ա���[00:00:14.201][info  ][DL] Tx Confirmation received
[00:00:14.201][info  ][DL]  stop soft timer
[00:00:14.202][info  ][DL] Char Write Req, char : 49
[00:00:14.203][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[00:00:14.203][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:14.203][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:14.205][info  ][EM] >>> [E:16885r S:54081 M:90312249] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:14.205][detail][EM] Handling via exchange: 16885r, Delegate: 0x20004cf4
[00:00:14.207][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[00:00:14.207][info  ][FS] GeneralCommissioning: Received ArmFailSafe (60s)
[00:00:14.207][detail][DMG] Command handler moving to [NewRespons]
[00:00:14.207][detail][DMG] Command handler moving to [ Preparing]
[00:00:14.207][detail][DMG] Command handler moving to [AddingComm]
[00:00:14.208][detail][DMG] Command handler moving to [AddedComma]
[00:00:14.208][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:14.208][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:14.208][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:14.209][info  ][EM] <<< [E:16885r S:54081 M:95271724] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)
[00:00:14.210][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:41.300]�ա���[00:00:14.381][info  ][DL] Tx Confirmation received
[00:00:14.381][info  ][DL]  stop soft timer
[00:00:14.381][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:43.010]�ա���[00:00:16.091][info  ][DL] Char Write Req, char : 49
[00:00:16.091][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 99)
[00:00:16.092][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:16.094][info  ][EM] >>> [E:16886r S:54081 M:90312250] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:94)
[00:00:16.094][detail][EM] Handling via exchange: 16886r, Delegate: 0x20004cf4
[00:00:16.095][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_003E Command=0x0000_0004
[00:00:16.095][info  ][ZCL] OpCreds: Received a CSRRequest command
[00:00:16.109][info  ][ZCL] OpCreds: AllocatePendingOperationalKey succeeded
[00:00:16.115][info  ][DL] SignWithDeviceAttestationKey, kid:2, msg_size:278, sig_size:64, err:0x00
[00:00:16.116][info  ][ZCL] OpCreds: CSRRequest successful.
[00:00:16.116][detail][DMG] Command handler moving to [NewRespons]
[00:00:16.116][detail][DMG] Command handler moving to [ Preparing]
[00:00:16.116][detail][DMG] Command handler moving to [AddingComm]
[00:00:16.116][detail][DMG] Command handler moving to [AddedComma]
[00:00:16.117][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[00:00:16.117][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[00:00:16.117][detail][DMG] Command handler moving to [AwaitingDe]
[00:00:16.119][info  ][EM] <<< [E:16886r S:54081 M:95271725] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:393)
[00:00:16.120][detail][DMG] Command response sender moving to [AllInvokeR]

[16:16:43.189]�ա���[00:00:16.271][info  ][DL] Tx Confirmation received
[00:00:16.271][info  ][DL]  stop soft timer
[00:00:16.271][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm

[16:16:43.368]�ա���[00:00:16.451][info  ][DL] Tx Confirmation received
[00:00:16.451][info  ][DL]  stop soft timer
[00:00:16.453][info  ][DL] Char Write Req, char : 49
[00:00:16.453][detail][DL] Write request/command received for CHIPoBLE RX characteristic (con 2, len 70)
[00:00:16.453][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[00:00:16.453][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[00:00:16.455][info  ][EM] >>> [E:16887r S:54081 M:90312251] (S) Msg RX from 0:FFFFFFFB00000000 [0000] to 0000000000000000 --- Type 0001:08 (IM:InvokeCommandRequest) (B:65)
[00:00:16.456][detail][EM] Handling via exchange: 16887r, Delegate: 0x20004cf4
[00:00:16.457][detail][DMG] Received command for Endpoint=0 Cluster=0x0000_0030 Command=0x0000_0000
[00:00:16.457][info  ][FS] GeneralCommissioning: Received ArmFailSafe (0s)
[00:00:16.457][info  ][FS] Fail-safe timer expired
[00:00:16.457][detail][DMG] Command handler moving to [NewRespons]
[00:00:16.458][detail][DMG] Command handler moving to [ Preparing]

Missed Logs: 1
[00:00:16.458][detail][DMG] Command handler moving to [AddingComm]

Missed Logs: 4
[00:00:16.458][detail][DMG] Command handler moving to [AddedComma]
[00:00:16.458][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1

Missed Logs: 4
[00:00:16.458][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0

Missed Logs: 5
[00:00:16.458][detail][DMG] Command handler moving to [AwaitingDe]

Missed Logs: 1
[00:00:16.460][info  ][EM] <<< [E:16887r S:54081 M:95271726] (S) Msg TX from 0000000000000000 to 0:FFFFFFFB00000000 [0000] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:66)

Missed Logs: 5
[00:00:16.461][detail][DMG] Command response sender moving to [AllInvokeR]
[00:00:16.461][info  ][DL] _OnPlatformEvent default:  event->Type = 32784

Missed Logs: 1
[00:00:16.461][error ][SVR] Failsafe timer expired
[00:00:16.461][detail][IN] SecureSession[0x20007be8]: MarkForEviction Type:1 LSID:54081

Missed Logs: 1
[00:00:16.462][error ][SVR] Commissioning failed (attempt 1): 32
[00:00:16.464][detail][IN] SecureSession[0x20007be8]: Allocated Type:1 LSID:54082
[00:00:16.464][detail][SC] Assigned local session key ID 54082
[00:00:16.465][detail][DIS] DNS-SD Pairing Instruction not set
[00:00:16.466][error ][ZCL] OpCreds: Got FailSafeTimerExpired
[00:00:16.467][info  ][TS] Pending Last Known Good Time: 2023-10-10T16:28:52
[00:00:16.470][info  ][DL] BLE Static Device Address FC:B1:19:A3:B2:3F
[00:00:16.472][info  ][DL] _OnPlatformEvent default:  event->Type = 32781
[00:00:16.472][silabs ]NWK: platform event type 800d
[00:00:16.472][silabs ] MATTER TX: : 55 aa 02 00 03 02 00 01 00 07 

[16:16:43.554]�ա���[00:00:16.631][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[00:00:16.632][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[00:00:16.632][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[00:00:16.632][detail][BLE] No endpoint for connection error
[00:00:16.633][info  ][DL] Starting advertising with interval_min=32, intverval_max=96 (units of 625us)

[16:16:49.377]�ա���[00:00:22.460][info  ][DL] BLEManagerImpl::HandleSoftTimerEvent CHIPOBLE_PROTOCOL_ABORT
[00:00:22.461][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[00:00:22.461][detail][BLE] No endpoint for connection error
```
