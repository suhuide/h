```c
[19:04:23.238]  [00:01:04.569][silabs ]NWK: Thread Established
[19:04:23.238]  [00:01:04.569][silabs ]COM: notify network [Joined]
[19:04:23.239]  [00:01:04.569][info  ][SVR] Scheduling OTA Requestor initialization
[19:04:23.239]  [00:01:04.569][info  ][SVR] Joining Multicast groups
[19:04:23.240]  [00:01:04.572][info  ][EM] <<< [E:31168r S:14006 M:129160807] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [E9EB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[19:04:23.242]  [00:01:04.573][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[19:04:23.243]  [00:01:04.573][info  ][DIS] Advertise operational node 5985E29CD6F3E9EB-00000000000008CA
[19:04:23.244]  [00:01:04.573][error ][SVR] Operational advertising failed: 3
[19:04:23.244]  [00:01:04.573][silabs ]NWK: platform event type 32785
[19:04:23.244]  [00:01:04.574][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[19:04:23.246]  [00:01:04.574][silabs ]NWK: platform event type 32779
[19:04:23.366]  [00:01:04.701][info  ][DL] Tx Confirmation received
[19:04:23.366]  [00:01:04.701][info  ][DL]  stop soft timer
[19:04:23.366]  [00:01:04.701][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[19:04:24.309]  [00:01:05.643][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[19:04:24.309]  [00:01:05.643][silabs ]NWK: platform event type 32786
[19:04:24.311]  [00:01:05.643][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[19:04:24.311]  [00:01:05.643][info  ][SVR] Server initialization complete
[19:04:24.312]  [00:01:05.643][info  ][DIS] Updating services using commissioning mode 0
[19:04:24.312]  [00:01:05.644][info  ][DIS] Advertise operational node 5985E29CD6F3E9EB-00000000000008CA
[19:04:24.314]  [00:01:05.644][info  ][DL] advertising srp service: 5985E29CD6F3E9EB-00000000000008CA._matter._tcp
[19:04:24.315]  [00:01:05.645][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[19:04:24.315]  [00:01:05.645][silabs ]NWK: platform event type 32790
[19:04:24.323]  [00:01:05.655][info  ][IM] No subscriptions to resume
[19:04:25.807]  [00:01:07.137][info  ][DL] Char Write Req, char : 23
[19:04:25.807]  [00:01:07.138][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[19:04:26.470]  [00:01:07.802][info  ][EM] >>> [E:31169r S:0 M:141066275] (U) Msg RX from 0:83872933EDEFFC75 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[19:04:26.471]  [00:01:07.803][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[19:04:26.472]  [00:01:07.804][info  ][EM] <<< [E:31169r S:0 M:223126973 (Ack:141066275)] (U) Msg TX from 0000000000000000 to 0:83872933EDEFFC75 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:57389] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:04:26.477]  [00:01:07.804][info  ][SC] Received Sigma1 msg
[19:04:26.482]  [00:01:07.813][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[19:04:26.504]  [00:01:07.837][info  ][EM] <<< [E:31169r S:0 M:223126974 (Ack:141066275)] (U) Msg TX from 0000000000000000 to 0:83872933EDEFFC75 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:57389] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[19:04:26.505]  [00:01:07.838][info  ][EM] ??1 [E:31169r S:0 M:223126974] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3389ms from now [State:Active II:500 AI:300 AT:4000]
[19:04:26.511]  [00:01:07.838][info  ][SC] Sent Sigma2 msg
[19:04:27.315]  [00:01:08.648][info  ][SWU] Stopping the watchdog timer
[19:04:27.315]  [00:01:08.648][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[19:04:27.336]  [00:01:08.669][info  ][EM] >>> [E:31169r S:0 M:141066276 (Ack:223126974)] (U) Msg RX from 0:83872933EDEFFC75 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[19:04:27.337]  [00:01:08.670][info  ][EM] <<< [E:31169r S:0 M:223126975 (Ack:141066276)] (U) Msg TX from 0000000000000000 to 0:83872933EDEFFC75 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:57389] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:04:27.342]  [00:01:08.670][info  ][SC] Received Sigma3 msg
[19:04:27.386]  [00:01:08.719][info  ][EM] <<< [E:31169r S:0 M:223126976 (Ack:141066276)] (U) Msg TX from 0000000000000000 to 0:83872933EDEFFC75 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:57389] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[19:04:27.388]  [00:01:08.720][info  ][EM] ??1 [E:31169r S:0 M:223126976] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3346ms from now [State:Active II:500 AI:300 AT:4000]
[19:04:27.390]  [00:01:08.723][info  ][SC] SecureSession[0x20006d50, LSID:14005]: State change 'kEstablishing' --> 'kActive'
[19:04:27.391]  [00:01:08.723][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[19:04:27.391]  [00:01:08.724][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[19:04:27.396]  [00:01:08.724][silabs ]NWK: platform event type 32792
[19:04:27.836]  [00:01:09.169][info  ][EM] >>> [E:31170r S:14005 M:38561636] (S) Msg RX from 1:000000000001B669 [E9EB] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[19:04:27.838]  [00:01:09.171][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[19:04:27.838]  [00:01:09.173][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[19:04:27.852]  [00:01:09.183][info  ][TS] Committing Last Known Good Time to storage: 2023-10-10T16:28:52
[19:04:27.858]  [00:01:09.191][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x5985E29CD6F3E9EB, FabricId 0000000000000001, NodeId 00000000000008CA, VendorId 0xFFF1
[19:04:27.859]  [00:01:09.192][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[19:04:27.860]  [00:01:09.192][info  ][FS] Fail-safe cleanly disarmed
[19:04:27.860]  [00:01:09.194][info  ][EM] <<< [E:31170r S:14005 M:202071665 (Ack:38561636)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:57389] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[19:04:27.864]  [00:01:09.195][info  ][EM] ??1 [E:31170r S:14005 M:202071665] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3404ms from now [State:Active II:500 AI:300 AT:4000] 
[19:04:27.866]  [00:01:09.196][info  ][EM] >>> [E:31169r S:0 M:141066277 (Ack:223126976)] (U) Msg RX from 0:83872933EDEFFC75 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26) 
[19:04:27.868]  [00:01:09.196][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[19:04:27.869]  [00:01:09.196][info  ][SWU] Device commissioned, schedule a default provider query
[19:04:27.869]  [00:01:09.197][info  ][SVR] Commissioning completed successfully
[19:04:27.870]  [00:01:09.197][info  ][DIS] Updating services using commissioning mode 0
[19:04:27.872]  [00:01:09.197][info  ][DIS] Advertise operational node 5985E29CD6F3E9EB-00000000000008CA
[19:04:27.872]  [00:01:09.197][info  ][SC] SecureSession[0x20006e28, LSID:14006]: State change 'kActive' --> 'kPendingEviction'
[19:04:27.873]  [00:01:09.198][info  ][BLE] Releasing end point's BLE connection back to application.
[19:04:27.874]  [00:01:09.198][info  ][DL] Closing BLE GATT connection (con 2)
[19:04:27.874]  [00:01:09.198][silabs ]NWK: kCommissioningComplete,32783
[19:04:28.047]  [00:01:09.380][info  ][DL] Disconnect Event for CHIPoBLE on handle : 2
[19:04:28.047]  [00:01:09.380][info  ][DL] BLE GATT connection closed (con 2, reason 4118)
[19:04:28.050]  [00:01:09.380][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[19:04:28.483]  [00:01:09.816][info  ][EM] >>> [E:31170r S:14005 M:38561637 (Ack:202071665)] (S) Msg RX from 1:000000000001B669 [E9EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[19:04:57.865]  [00:01:39.197][error ][SWU] No suitable OTA Provider candidate found
[19:04:57.865]  [00:01:39.197][info  ][SWU] No provider available
[19:05:25.570]  [00:02:06.908][info  ][EM] >>> [E:14649r S:0 M:180107312] (U) Msg RX from 0:BF093BA1E3DF51A3 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[19:05:25.572]  [00:02:06.909][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[19:05:25.573]  [00:02:06.910][info  ][EM] <<< [E:14649r S:0 M:223126977 (Ack:180107312)] (U) Msg TX from 0000000000000000 to 0:BF093BA1E3DF51A3 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:44293] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:05:25.578]  [00:02:06.910][info  ][SC] Received Sigma1 msg
[19:05:25.583]  [00:02:06.918][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[19:05:25.606]  [00:02:06.944][info  ][EM] <<< [E:14649r S:0 M:223126978 (Ack:180107312)] (U) Msg TX from 0000000000000000 to 0:BF093BA1E3DF51A3 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:44293] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[19:05:25.607]  [00:02:06.945][info  ][EM] ??1 [E:14649r S:0 M:223126978] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3336ms from now [State:Active II:500 AI:300 AT:4000]
[19:05:25.613]  [00:02:06.945][info  ][SC] Sent Sigma2 msg
[19:05:26.215]  [00:02:07.553][info  ][EM] >>> [E:14649r S:0 M:180107313 (Ack:223126978)] (U) Msg RX from 0:BF093BA1E3DF51A3 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[19:05:26.216]  [00:02:07.554][info  ][EM] <<< [E:14649r S:0 M:223126979 (Ack:180107313)] (U) Msg TX from 0000000000000000 to 0:BF093BA1E3DF51A3 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:44293] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:05:26.223]  [00:02:07.554][info  ][SC] Received Sigma3 msg
[19:05:26.266]  [00:02:07.604][info  ][EM] <<< [E:14649r S:0 M:223126980 (Ack:180107313)] (U) Msg TX from 0000000000000000 to 0:BF093BA1E3DF51A3 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:44293] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[19:05:26.267]  [00:02:07.604][info  ][EM] ??1 [E:14649r S:0 M:223126980] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3364ms from now [State:Active II:500 AI:300 AT:4000]
[19:05:26.270]  [00:02:07.608][info  ][SC] SecureSession[0x20006f00, LSID:14007]: State change 'kEstablishing' --> 'kActive'
[19:05:26.271]  [00:02:07.608][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[19:05:26.271]  [00:02:07.609][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[19:05:26.274]  [00:02:07.609][silabs ]NWK: platform event type 32792
[19:05:26.727]  [00:02:08.065][info  ][EM] >>> [E:14650r S:14007 M:221680434] (S) Msg RX from 1:000000000001B669 [E9EB] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:71)
[19:05:26.730]  [00:02:08.067][info  ][SWU] OTA Requestor received AnnounceOTAProvider
[19:05:26.730]  [00:02:08.069][info  ][EM] <<< [E:14650r S:14007 M:161305172 (Ack:221680434)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:44293] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[19:05:26.732]  [00:02:08.070][info  ][EM] ??1 [E:14650r S:14007 M:161305172] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3403ms from now [State:Active II:500 AI:300 AT:4000]
[19:05:26.735]  [00:02:08.071][info  ][SWU] Stopping the Periodic Query timer
[19:05:26.735]  [00:02:08.071][info  ][SWU] Starting the watchdog timer, timeout: 21600 seconds
[19:05:26.737]  [00:02:08.071][info  ][DIS] Resolving 5985E29CD6F3E9EB:0000000000000001 ...
[19:05:26.737]  [00:02:08.072][info  ][DIS] Lookup started for 5985E29CD6F3E9EB-0000000000000001
[19:05:26.761]  [00:02:08.099][info  ][EM] >>> [E:14649r S:0 M:180107314 (Ack:223126980)] (U) Msg RX from 0:BF093BA1E3DF51A3 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:05:26.935]  [00:02:08.271][info  ][DIS] Checking node lookup status for 5985E29CD6F3E9EB-0000000000000001 after 200 ms
[19:05:27.246]  [00:02:08.584][info  ][EM] >>> [E:14650r S:14007 M:221680435 (Ack:161305172)] (S) Msg RX from 1:000000000001B669 [E9EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[19:05:27.321]  [00:02:08.660][info  ][DIS] Node ID resolved for 5985E29CD6F3E9EB-0000000000000001
[19:05:27.321]  [00:02:08.660][info  ][DIS] UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540: new best score: 3 (for 5985E29CD6F3E9EB-0000000000000001)
[19:05:27.322]  [00:02:08.661][info  ][DIS] Checking node lookup status for 5985E29CD6F3E9EB-0000000000000001 after 590 ms
[19:05:27.325]  [00:02:08.662][info  ][SC] Initiating session on local FabricIndex 1 from 0x00000000000008CA -> 0x0000000000000001
[19:05:27.339]  [00:02:08.677][info  ][EM] <<< [E:29146i S:0 M:223126981] (U) Msg TX from 0D8EFFEFEAB198BD to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:195)
[19:05:27.342]  [00:02:08.678][info  ][EM] ??1 [E:29146i S:0 M:223126981] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3558ms from now [State:Idle II:500 AI:2000 AT:4000]
[19:05:27.348]  [00:02:08.678][info  ][SC] Sent Sigma1 msg to <0000000000000001, 1> [II:3000ms AI:2500ms AT:0ms]
[19:05:28.030]  [00:02:09.367][info  ][EM] >>> [E:29146i S:0 M:262024123 (Ack:223126981)] (U) Msg RX from 0:0000000000000000 [0000] to 0D8EFFEFEAB198BD --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[19:05:28.031]  [00:02:09.368][info  ][EM] <<< [E:29146i S:0 M:223126982 (Ack:262024123)] (U) Msg TX from 0D8EFFEFEAB198BD to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:05:28.038]  [00:02:09.369][info  ][SC] Received Sigma2 msg
[19:05:28.093]  [00:02:09.431][info  ][EM] <<< [E:29146i S:0 M:223126983 (Ack:262024123)] (U) Msg TX from 0D8EFFEFEAB198BD to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:596)
[19:05:28.096]  [00:02:09.433][info  ][EM] ??1 [E:29146i S:0 M:223126983] (U) Msg Retransmission to 0:0000000000000000 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:28.100]  [00:02:09.433][info  ][SC] Sent Sigma3 msg
[19:05:28.533]  [00:02:09.871][info  ][EM] >>> [E:29146i S:0 M:262024124 (Ack:223126983)] (U) Msg RX from 0:0000000000000000 [0000] to 0D8EFFEFEAB198BD --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[19:05:28.534]  [00:02:09.872][info  ][SC] Success status report received. Session was established
[19:05:28.566]  [00:02:09.903][info  ][SC] SecureSession[0x20006fd8, LSID:14009]: State change 'kEstablishing' --> 'kActive'
[19:05:28.566]  [00:02:09.906][info  ][EM] <<< [E:29147i S:14009 M:240766365] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[19:05:28.569]  [00:02:09.907][info  ][EM] ??1 [E:29147i S:14009 M:240766365] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:28.573]  [00:02:09.908][info  ][EM] <<< [E:29146i S:0 M:223126984 (Ack:262024124)] (U) Msg TX from 0D8EFFEFEAB198BD to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:05:28.574]  [00:02:09.908][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[19:05:28.578]  [00:02:09.908][silabs ]NWK: platform event type 32792
[19:05:29.074]  [00:02:10.412][info  ][EM] >>> [E:29147i S:14009 M:31549737 (Ack:240766365)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:196)
[19:05:29.076]  [00:02:10.413][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[19:05:29.077]  [00:02:10.414][info  ][SWU] Update available from version 1 to 2
[19:05:29.077]  [00:02:10.416][info  ][EM] <<< [E:29147i S:14009 M:240766366 (Ack:31549737)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[19:05:29.120]  [00:02:10.416][info  ][DIS] Found an existing secure session to [1:0000000000000001]!
[19:05:29.120]  [00:02:10.416][info  ][SWU] HandlePrepareDownload: started
[19:05:29.123]  [00:02:10.460][info  ][EM] <<< [E:29148i S:14009 M:240766367] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:04 (BDX:ReceiveInit) (B:88)
[19:05:29.124]  [00:02:10.461][info  ][EM] ??1 [E:29148i S:14009 M:240766367] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:29.578]  [00:02:10.916][info  ][EM] >>> [E:29148i S:14009 M:31549738 (Ack:240766367)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:05 (BDX:ReceiveAccept) (B:38)
[19:05:29.580]  [00:02:10.918][info  ][EM] <<< [E:29148i S:14009 M:240766368 (Ack:31549738)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:29.582]  [00:02:10.919][info  ][EM] ??1 [E:29148i S:14009 M:240766368] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:30.775]  [00:02:12.112][info  ][EM] >>> [E:29148i S:14009 M:31549739 (Ack:240766368)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:30.854]  [00:02:12.113][info  ][SWU] Image Header software version: 2 payload size: 553476
[19:05:30.901]  [00:02:12.239][info  ][EM] <<< [E:29148i S:14009 M:240766369 (Ack:31549739)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:30.902]  [00:02:12.240][info  ][EM] ??1 [E:29148i S:14009 M:240766369] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:30.908]  [00:02:12.240][error ][DL] Long dispatch time: 127 ms, for event type 2
[19:05:31.531]  [00:02:12.869][info  ][EM] >>> [E:29148i S:14009 M:31549740 (Ack:240766369)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:31.591]  [00:02:12.929][info  ][EM] <<< [E:29148i S:14009 M:240766370 (Ack:31549740)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:31.592]  [00:02:12.930][info  ][EM] ??1 [E:29148i S:14009 M:240766370] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:32.513]  [00:02:13.850][info  ][EM] >>> [E:29148i S:14009 M:31549741 (Ack:240766370)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:32.573]  [00:02:13.911][info  ][EM] <<< [E:29148i S:14009 M:240766371 (Ack:31549741)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:32.574]  [00:02:13.912][info  ][EM] ??1 [E:29148i S:14009 M:240766371] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:33.279]  [00:02:14.616][info  ][EM] >>> [E:29148i S:14009 M:31549742 (Ack:240766371)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:33.339]  [00:02:14.676][info  ][EM] <<< [E:29148i S:14009 M:240766372 (Ack:31549742)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:33.340]  [00:02:14.677][info  ][EM] ??1 [E:29148i S:14009 M:240766372] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:34.073]  [00:02:15.412][info  ][EM] >>> [E:29148i S:14009 M:31549743 (Ack:240766372)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:34.207]  [00:02:15.545][info  ][EM] <<< [E:29148i S:14009 M:240766373 (Ack:31549743)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:34.208]  [00:02:15.546][info  ][EM] ??1 [E:29148i S:14009 M:240766373] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:34.214]  [00:02:15.546][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:05:34.949]  [00:02:16.287][info  ][EM] >>> [E:29148i S:14009 M:31549744 (Ack:240766373)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:35.010]  [00:02:16.347][info  ][EM] <<< [E:29148i S:14009 M:240766374 (Ack:31549744)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:35.011]  [00:02:16.348][info  ][EM] ??1 [E:29148i S:14009 M:240766374] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:35.834]  [00:02:17.171][info  ][EM] >>> [E:29148i S:14009 M:31549745 (Ack:240766374)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:35.894]  [00:02:17.232][info  ][EM] <<< [E:29148i S:14009 M:240766375 (Ack:31549745)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:35.895]  [00:02:17.232][info  ][EM] ??1 [E:29148i S:14009 M:240766375] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:36.718]  [00:02:18.055][info  ][EM] >>> [E:29148i S:14009 M:31549746 (Ack:240766375)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:36.778]  [00:02:18.116][info  ][EM] <<< [E:29148i S:14009 M:240766376 (Ack:31549746)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:36.780]  [00:02:18.117][info  ][EM] ??1 [E:29148i S:14009 M:240766376] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:37.702]  [00:02:19.040][info  ][EM] >>> [E:29148i S:14009 M:31549747 (Ack:240766376)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:37.836]  [00:02:19.173][info  ][EM] <<< [E:29148i S:14009 M:240766377 (Ack:31549747)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:37.838]  [00:02:19.174][info  ][EM] ??1 [E:29148i S:14009 M:240766377] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:37.842]  [00:02:19.175][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:05:38.726]  [00:02:20.063][info  ][EM] >>> [E:29148i S:14009 M:31549748 (Ack:240766377)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:38.786]  [00:02:20.124][info  ][EM] <<< [E:29148i S:14009 M:240766378 (Ack:31549748)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:38.787]  [00:02:20.125][info  ][EM] ??1 [E:29148i S:14009 M:240766378] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:39.602]  [00:02:20.939][info  ][EM] >>> [E:29148i S:14009 M:31549749 (Ack:240766378)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:39.662]  [00:02:21.000][info  ][EM] <<< [E:29148i S:14009 M:240766379 (Ack:31549749)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:39.664]  [00:02:21.000][info  ][EM] ??1 [E:29148i S:14009 M:240766379] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:40.588]  [00:02:21.925][info  ][EM] >>> [E:29148i S:14009 M:31549750 (Ack:240766379)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:40.650]  [00:02:21.986][info  ][EM] <<< [E:29148i S:14009 M:240766380 (Ack:31549750)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:40.650]  [00:02:21.987][info  ][EM] ??1 [E:29148i S:14009 M:240766380] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:41.737]  [00:02:23.074][info  ][EM] >>> [E:29148i S:14009 M:31549751 (Ack:240766380)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:41.871]  [00:02:23.208][info  ][EM] <<< [E:29148i S:14009 M:240766381 (Ack:31549751)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:41.872]  [00:02:23.208][info  ][EM] ??1 [E:29148i S:14009 M:240766381] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:41.877]  [00:02:23.209][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:05:42.927]  [00:02:24.264][info  ][EM] >>> [E:29148i S:14009 M:31549752 (Ack:240766381)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:42.987]  [00:02:24.325][info  ][EM] <<< [E:29148i S:14009 M:240766382 (Ack:31549752)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:42.989]  [00:02:24.326][info  ][EM] ??1 [E:29148i S:14009 M:240766382] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:43.798]  [00:02:25.135][info  ][EM] >>> [E:29148i S:14009 M:31549753 (Ack:240766382)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:43.858]  [00:02:25.195][info  ][EM] <<< [E:29148i S:14009 M:240766383 (Ack:31549753)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:43.859]  [00:02:25.196][info  ][EM] ??1 [E:29148i S:14009 M:240766383] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:44.598]  [00:02:25.936][info  ][EM] >>> [E:29148i S:14009 M:31549754 (Ack:240766383)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:44.659]  [00:02:25.997][info  ][EM] <<< [E:29148i S:14009 M:240766384 (Ack:31549754)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:44.660]  [00:02:25.997][info  ][EM] ??1 [E:29148i S:14009 M:240766384] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5269ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:45.363]  [00:02:26.700][info  ][EM] >>> [E:29148i S:14009 M:31549755 (Ack:240766384)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:45.496]  [00:02:26.833][info  ][EM] <<< [E:29148i S:14009 M:240766385 (Ack:31549755)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:45.498]  [00:02:26.834][info  ][EM] ??1 [E:29148i S:14009 M:240766385] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:45.502]  [00:02:26.834][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:05:46.359]  [00:02:27.696][info  ][EM] >>> [E:29148i S:14009 M:31549756 (Ack:240766385)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:46.420]  [00:02:27.756][info  ][EM] <<< [E:29148i S:14009 M:240766386 (Ack:31549756)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:46.421]  [00:02:27.756][info  ][EM] ??1 [E:29148i S:14009 M:240766386] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:47.121]  [00:02:28.458][info  ][EM] >>> [E:29148i S:14009 M:31549757 (Ack:240766386)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:47.182]  [00:02:28.519][info  ][EM] <<< [E:29148i S:14009 M:240766387 (Ack:31549757)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:47.183]  [00:02:28.520][info  ][EM] ??1 [E:29148i S:14009 M:240766387] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:48.103]  [00:02:29.441][info  ][EM] >>> [E:29148i S:14009 M:31549758 (Ack:240766387)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:48.164]  [00:02:29.501][info  ][EM] <<< [E:29148i S:14009 M:240766388 (Ack:31549758)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:48.165]  [00:02:29.502][info  ][EM] ??1 [E:29148i S:14009 M:240766388] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:49.120]  [00:02:30.457][info  ][EM] >>> [E:29148i S:14009 M:31549759 (Ack:240766388)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:49.254]  [00:02:30.590][info  ][EM] <<< [E:29148i S:14009 M:240766389 (Ack:31549759)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:49.255]  [00:02:30.591][info  ][EM] ??1 [E:29148i S:14009 M:240766389] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:49.262]  [00:02:30.592][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:05:50.401]  [00:02:31.739][info  ][EM] >>> [E:29148i S:14009 M:31549760 (Ack:240766389)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:50.462]  [00:02:31.799][info  ][EM] <<< [E:29148i S:14009 M:240766390 (Ack:31549760)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:50.463]  [00:02:31.799][info  ][EM] ??1 [E:29148i S:14009 M:240766390] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:51.361]  [00:02:32.698][info  ][EM] >>> [E:29148i S:14009 M:31549761 (Ack:240766390)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:51.421]  [00:02:32.758][info  ][EM] <<< [E:29148i S:14009 M:240766391 (Ack:31549761)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:51.422]  [00:02:32.759][info  ][EM] ??1 [E:29148i S:14009 M:240766391] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5658ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:52.120]  [00:02:33.458][info  ][EM] >>> [E:29148i S:14009 M:31549762 (Ack:240766391)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:52.181]  [00:02:33.518][info  ][EM] <<< [E:29148i S:14009 M:240766392 (Ack:31549762)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:52.182]  [00:02:33.518][info  ][EM] ??1 [E:29148i S:14009 M:240766392] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5220ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:53.001]  [00:02:34.337][info  ][EM] >>> [E:29148i S:14009 M:31549763 (Ack:240766392)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:53.135]  [00:02:34.471][info  ][EM] <<< [E:29148i S:14009 M:240766393 (Ack:31549763)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:53.137]  [00:02:34.472][info  ][EM] ??1 [E:29148i S:14009 M:240766393] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:53.142]  [00:02:34.473][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:05:54.304]  [00:02:35.641][info  ][EM] >>> [E:29148i S:14009 M:31549764 (Ack:240766393)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:54.365]  [00:02:35.702][info  ][EM] <<< [E:29148i S:14009 M:240766394 (Ack:31549764)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:54.366]  [00:02:35.703][info  ][EM] ??1 [E:29148i S:14009 M:240766394] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5749ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:55.043]  [00:02:36.379][info  ][EM] >>> [E:29148i S:14009 M:31549765 (Ack:240766394)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:55.104]  [00:02:36.440][info  ][EM] <<< [E:29148i S:14009 M:240766395 (Ack:31549765)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:55.105]  [00:02:36.441][info  ][EM] ??1 [E:29148i S:14009 M:240766395] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:55.899]  [00:02:37.236][info  ][EM] >>> [E:29148i S:14009 M:31549766 (Ack:240766395)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:55.959]  [00:02:37.296][info  ][EM] <<< [E:29148i S:14009 M:240766396 (Ack:31549766)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:55.961]  [00:02:37.297][info  ][EM] ??1 [E:29148i S:14009 M:240766396] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5701ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:57.396]  [00:02:38.733][info  ][EM] >>> [E:29148i S:14009 M:31549767 (Ack:240766396)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:57.530]  [00:02:38.867][info  ][EM] <<< [E:29148i S:14009 M:240766397 (Ack:31549767)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:57.531]  [00:02:38.868][info  ][EM] ??1 [E:29148i S:14009 M:240766397] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:57.536]  [00:02:38.868][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:05:58.150]  [00:02:39.486][info  ][EM] >>> [E:29148i S:14009 M:31549768 (Ack:240766397)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:58.211]  [00:02:39.546][info  ][EM] <<< [E:29148i S:14009 M:240766398 (Ack:31549768)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:58.212]  [00:02:39.547][info  ][EM] ??1 [E:29148i S:14009 M:240766398] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:58.934]  [00:02:40.270][info  ][EM] >>> [E:29148i S:14009 M:31549769 (Ack:240766398)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:58.994]  [00:02:40.331][info  ][EM] <<< [E:29148i S:14009 M:240766399 (Ack:31549769)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:58.995]  [00:02:40.332][info  ][EM] ??1 [E:29148i S:14009 M:240766399] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[19:05:59.910]  [00:02:41.248][info  ][EM] >>> [E:29148i S:14009 M:31549770 (Ack:240766399)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:05:59.971]  [00:02:41.307][info  ][EM] <<< [E:29148i S:14009 M:240766400 (Ack:31549770)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:05:59.973]  [00:02:41.308][info  ][EM] ??1 [E:29148i S:14009 M:240766400] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:00.703]  [00:02:42.040][info  ][EM] >>> [E:29148i S:14009 M:31549771 (Ack:240766400)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:00.838]  [00:02:42.173][info  ][EM] <<< [E:29148i S:14009 M:240766401 (Ack:31549771)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:00.839]  [00:02:42.174][info  ][EM] ??1 [E:29148i S:14009 M:240766401] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:00.844]  [00:02:42.175][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:01.559]  [00:02:42.896][info  ][EM] >>> [E:29148i S:14009 M:31549772 (Ack:240766401)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:01.620]  [00:02:42.957][info  ][EM] <<< [E:29148i S:14009 M:240766402 (Ack:31549772)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:01.621]  [00:02:42.958][info  ][EM] ??1 [E:29148i S:14009 M:240766402] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:02.432]  [00:02:43.768][info  ][EM] >>> [E:29148i S:14009 M:31549773 (Ack:240766402)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:02.492]  [00:02:43.829][info  ][EM] <<< [E:29148i S:14009 M:240766403 (Ack:31549773)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:02.494]  [00:02:43.830][info  ][EM] ??1 [E:29148i S:14009 M:240766403] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:03.403]  [00:02:44.740][info  ][EM] >>> [E:29148i S:14009 M:31549774 (Ack:240766403)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:03.464]  [00:02:44.800][info  ][EM] <<< [E:29148i S:14009 M:240766404 (Ack:31549774)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:03.465]  [00:02:44.800][info  ][EM] ??1 [E:29148i S:14009 M:240766404] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:04.287]  [00:02:45.624][info  ][EM] >>> [E:29148i S:14009 M:31549775 (Ack:240766404)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:04.421]  [00:02:45.757][info  ][EM] <<< [E:29148i S:14009 M:240766405 (Ack:31549775)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:04.422]  [00:02:45.758][info  ][EM] ??1 [E:29148i S:14009 M:240766405] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:04.427]  [00:02:45.759][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:05.158]  [00:02:46.495][info  ][EM] >>> [E:29148i S:14009 M:31549776 (Ack:240766405)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:05.219]  [00:02:46.555][info  ][EM] <<< [E:29148i S:14009 M:240766406 (Ack:31549776)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:05.220]  [00:02:46.556][info  ][EM] ??1 [E:29148i S:14009 M:240766406] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:06.431]  [00:02:47.768][info  ][EM] >>> [E:29148i S:14009 M:31549777 (Ack:240766406)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:06.492]  [00:02:47.829][info  ][EM] <<< [E:29148i S:14009 M:240766407 (Ack:31549777)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:06.493]  [00:02:47.830][info  ][EM] ??1 [E:29148i S:14009 M:240766407] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:07.296]  [00:02:48.633][info  ][EM] >>> [E:29148i S:14009 M:31549778 (Ack:240766407)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:07.358]  [00:02:48.694][info  ][EM] <<< [E:29148i S:14009 M:240766408 (Ack:31549778)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:07.359]  [00:02:48.695][info  ][EM] ??1 [E:29148i S:14009 M:240766408] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:08.169]  [00:02:49.505][info  ][EM] >>> [E:29148i S:14009 M:31549779 (Ack:240766408)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:08.304]  [00:02:49.639][info  ][EM] <<< [E:29148i S:14009 M:240766409 (Ack:31549779)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:08.305]  [00:02:49.640][info  ][EM] ??1 [E:29148i S:14009 M:240766409] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5633ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:08.310]  [00:02:49.640][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:08.973]  [00:02:50.309][info  ][EM] >>> [E:29148i S:14009 M:31549780 (Ack:240766409)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:09.034]  [00:02:50.370][info  ][EM] <<< [E:29148i S:14009 M:240766410 (Ack:31549780)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:09.035]  [00:02:50.371][info  ][EM] ??1 [E:29148i S:14009 M:240766410] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:09.767]  [00:02:51.102][info  ][EM] >>> [E:29148i S:14009 M:31549781 (Ack:240766410)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:09.828]  [00:02:51.164][info  ][EM] <<< [E:29148i S:14009 M:240766411 (Ack:31549781)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:09.829]  [00:02:51.164][info  ][EM] ??1 [E:29148i S:14009 M:240766411] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:10.918]  [00:02:52.255][info  ][EM] >>> [E:29148i S:14009 M:31549782 (Ack:240766411)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:10.979]  [00:02:52.316][info  ][EM] <<< [E:29148i S:14009 M:240766412 (Ack:31549782)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:10.981]  [00:02:52.316][info  ][EM] ??1 [E:29148i S:14009 M:240766412] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:11.776]  [00:02:53.112][info  ][EM] >>> [E:29148i S:14009 M:31549783 (Ack:240766412)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:11.910]  [00:02:53.246][info  ][EM] <<< [E:29148i S:14009 M:240766413 (Ack:31549783)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:11.911]  [00:02:53.247][info  ][EM] ??1 [E:29148i S:14009 M:240766413] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:11.916]  [00:02:53.247][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:12.867]  [00:02:54.204][info  ][EM] >>> [E:29148i S:14009 M:31549784 (Ack:240766413)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:12.929]  [00:02:54.264][info  ][EM] <<< [E:29148i S:14009 M:240766414 (Ack:31549784)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:12.930]  [00:02:54.265][info  ][EM] ??1 [E:29148i S:14009 M:240766414] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:13.645]  [00:02:54.981][info  ][EM] >>> [E:29148i S:14009 M:31549785 (Ack:240766414)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:13.706]  [00:02:55.041][info  ][EM] <<< [E:29148i S:14009 M:240766415 (Ack:31549785)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:13.707]  [00:02:55.042][info  ][EM] ??1 [E:29148i S:14009 M:240766415] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:14.445]  [00:02:55.781][info  ][EM] >>> [E:29148i S:14009 M:31549786 (Ack:240766415)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:14.506]  [00:02:55.841][info  ][EM] <<< [E:29148i S:14009 M:240766416 (Ack:31549786)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:14.507]  [00:02:55.842][info  ][EM] ??1 [E:29148i S:14009 M:240766416] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:15.539]  [00:02:56.875][info  ][EM] >>> [E:29148i S:14009 M:31549787 (Ack:240766416)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:15.674]  [00:02:57.009][info  ][EM] <<< [E:29148i S:14009 M:240766417 (Ack:31549787)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:15.675]  [00:02:57.010][info  ][EM] ??1 [E:29148i S:14009 M:240766417] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:15.680]  [00:02:57.010][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:16.426]  [00:02:57.762][info  ][EM] >>> [E:29148i S:14009 M:31549788 (Ack:240766417)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:16.486]  [00:02:57.823][info  ][EM] <<< [E:29148i S:14009 M:240766418 (Ack:31549788)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:16.489]  [00:02:57.824][info  ][EM] ??1 [E:29148i S:14009 M:240766418] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:17.286]  [00:02:58.622][info  ][EM] >>> [E:29148i S:14009 M:31549789 (Ack:240766418)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:17.346]  [00:02:58.682][info  ][EM] <<< [E:29148i S:14009 M:240766419 (Ack:31549789)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:17.348]  [00:02:58.683][info  ][EM] ??1 [E:29148i S:14009 M:240766419] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:18.149]  [00:02:59.486][info  ][EM] >>> [E:29148i S:14009 M:31549790 (Ack:240766419)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:18.210]  [00:02:59.545][info  ][EM] <<< [E:29148i S:14009 M:240766420 (Ack:31549790)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:18.212]  [00:02:59.546][info  ][EM] ??1 [E:29148i S:14009 M:240766420] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:18.918]  [00:03:00.254][info  ][EM] >>> [E:29148i S:14009 M:31549791 (Ack:240766420)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:19.053]  [00:03:00.388][info  ][EM] <<< [E:29148i S:14009 M:240766421 (Ack:31549791)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:19.054]  [00:03:00.389][info  ][EM] ??1 [E:29148i S:14009 M:240766421] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:19.060]  [00:03:00.389][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:06:19.800]  [00:03:01.136][info  ][EM] >>> [E:29148i S:14009 M:31549792 (Ack:240766421)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:19.861]  [00:03:01.197][info  ][EM] <<< [E:29148i S:14009 M:240766422 (Ack:31549792)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:19.863]  [00:03:01.198][info  ][EM] ??1 [E:29148i S:14009 M:240766422] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:20.783]  [00:03:02.120][info  ][EM] >>> [E:29148i S:14009 M:31549793 (Ack:240766422)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:20.844]  [00:03:02.180][info  ][EM] <<< [E:29148i S:14009 M:240766423 (Ack:31549793)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:20.845]  [00:03:02.180][info  ][EM] ??1 [E:29148i S:14009 M:240766423] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:21.565]  [00:03:02.901][info  ][EM] >>> [E:29148i S:14009 M:31549794 (Ack:240766423)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:21.626]  [00:03:02.961][info  ][EM] <<< [E:29148i S:14009 M:240766424 (Ack:31549794)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:21.627]  [00:03:02.962][info  ][EM] ??1 [E:29148i S:14009 M:240766424] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5544ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:22.451]  [00:03:03.786][info  ][EM] >>> [E:29148i S:14009 M:31549795 (Ack:240766424)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:22.584]  [00:03:03.919][info  ][EM] <<< [E:29148i S:14009 M:240766425 (Ack:31549795)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:22.585]  [00:03:03.920][info  ][EM] ??1 [E:29148i S:14009 M:240766425] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5680ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:22.590]  [00:03:03.920][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:06:23.435]  [00:03:04.771][info  ][EM] >>> [E:29148i S:14009 M:31549796 (Ack:240766425)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:23.495]  [00:03:04.831][info  ][EM] <<< [E:29148i S:14009 M:240766426 (Ack:31549796)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:23.497]  [00:03:04.832][info  ][EM] ??1 [E:29148i S:14009 M:240766426] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5304ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:24.333]  [00:03:05.668][info  ][EM] >>> [E:29148i S:14009 M:31549797 (Ack:240766426)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:24.394]  [00:03:05.729][info  ][EM] <<< [E:29148i S:14009 M:240766427 (Ack:31549797)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:24.395]  [00:03:05.730][info  ][EM] ??1 [E:29148i S:14009 M:240766427] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:25.200]  [00:03:06.536][info  ][EM] >>> [E:29148i S:14009 M:31549798 (Ack:240766427)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:25.261]  [00:03:06.596][info  ][EM] <<< [E:29148i S:14009 M:240766428 (Ack:31549798)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:25.262]  [00:03:06.597][info  ][EM] ??1 [E:29148i S:14009 M:240766428] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:25.999]  [00:03:07.334][info  ][EM] >>> [E:29148i S:14009 M:31549799 (Ack:240766428)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:26.132]  [00:03:07.468][info  ][EM] <<< [E:29148i S:14009 M:240766429 (Ack:31549799)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:26.135]  [00:03:07.469][info  ][EM] ??1 [E:29148i S:14009 M:240766429] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:26.139]  [00:03:07.469][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:06:26.767]  [00:03:08.102][info  ][EM] >>> [E:29148i S:14009 M:31549800 (Ack:240766429)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:26.828]  [00:03:08.163][info  ][EM] <<< [E:29148i S:14009 M:240766430 (Ack:31549800)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:26.829]  [00:03:08.164][info  ][EM] ??1 [E:29148i S:14009 M:240766430] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:27.641]  [00:03:08.977][info  ][EM] >>> [E:29148i S:14009 M:31549801 (Ack:240766430)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:27.702]  [00:03:09.038][info  ][EM] <<< [E:29148i S:14009 M:240766431 (Ack:31549801)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:27.703]  [00:03:09.038][info  ][EM] ??1 [E:29148i S:14009 M:240766431] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5736ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:28.384]  [00:03:09.719][info  ][EM] >>> [E:29148i S:14009 M:31549802 (Ack:240766431)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:28.444]  [00:03:09.780][info  ][EM] <<< [E:29148i S:14009 M:240766432 (Ack:31549802)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:28.447]  [00:03:09.781][info  ][EM] ??1 [E:29148i S:14009 M:240766432] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:29.263]  [00:03:10.599][info  ][EM] >>> [E:29148i S:14009 M:31549803 (Ack:240766432)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:29.400]  [00:03:10.735][info  ][EM] <<< [E:29148i S:14009 M:240766433 (Ack:31549803)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:29.401]  [00:03:10.736][info  ][EM] ??1 [E:29148i S:14009 M:240766433] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:29.406]  [00:03:10.736][error ][DL] Long dispatch time: 136 ms, for event type 2
[19:06:30.131]  [00:03:11.466][info  ][EM] >>> [E:29148i S:14009 M:31549804 (Ack:240766433)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:30.192]  [00:03:11.527][info  ][EM] <<< [E:29148i S:14009 M:240766434 (Ack:31549804)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:30.193]  [00:03:11.528][info  ][EM] ??1 [E:29148i S:14009 M:240766434] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:31.108]  [00:03:12.444][info  ][EM] >>> [E:29148i S:14009 M:31549805 (Ack:240766434)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:31.168]  [00:03:12.504][info  ][EM] <<< [E:29148i S:14009 M:240766435 (Ack:31549805)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:31.170]  [00:03:12.504][info  ][EM] ??1 [E:29148i S:14009 M:240766435] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:32.117]  [00:03:13.452][info  ][EM] >>> [E:29148i S:14009 M:31549806 (Ack:240766435)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:32.178]  [00:03:13.512][info  ][EM] <<< [E:29148i S:14009 M:240766436 (Ack:31549806)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:32.179]  [00:03:13.513][info  ][EM] ??1 [E:29148i S:14009 M:240766436] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:33.099]  [00:03:14.434][info  ][EM] >>> [E:29148i S:14009 M:31549807 (Ack:240766436)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:33.233]  [00:03:14.568][info  ][EM] <<< [E:29148i S:14009 M:240766437 (Ack:31549807)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:33.234]  [00:03:14.569][info  ][EM] ??1 [E:29148i S:14009 M:240766437] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:33.240]  [00:03:14.569][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:33.971]  [00:03:15.306][info  ][EM] >>> [E:29148i S:14009 M:31549808 (Ack:240766437)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:34.032]  [00:03:15.367][info  ][EM] <<< [E:29148i S:14009 M:240766438 (Ack:31549808)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:34.033]  [00:03:15.368][info  ][EM] ??1 [E:29148i S:14009 M:240766438] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:34.792]  [00:03:16.127][info  ][EM] >>> [E:29148i S:14009 M:31549809 (Ack:240766438)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:34.852]  [00:03:16.188][info  ][EM] <<< [E:29148i S:14009 M:240766439 (Ack:31549809)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:34.854]  [00:03:16.188][info  ][EM] ??1 [E:29148i S:14009 M:240766439] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:35.557]  [00:03:16.892][info  ][EM] >>> [E:29148i S:14009 M:31549810 (Ack:240766439)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:35.618]  [00:03:16.953][info  ][EM] <<< [E:29148i S:14009 M:240766440 (Ack:31549810)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:35.619]  [00:03:16.954][info  ][EM] ??1 [E:29148i S:14009 M:240766440] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:36.327]  [00:03:17.663][info  ][EM] >>> [E:29148i S:14009 M:31549811 (Ack:240766440)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:36.461]  [00:03:17.796][info  ][EM] <<< [E:29148i S:14009 M:240766441 (Ack:31549811)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:36.462]  [00:03:17.797][info  ][EM] ??1 [E:29148i S:14009 M:240766441] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5633ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:36.469]  [00:03:17.797][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:06:37.212]  [00:03:18.547][info  ][EM] >>> [E:29148i S:14009 M:31549812 (Ack:240766441)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:37.273]  [00:03:18.608][info  ][EM] <<< [E:29148i S:14009 M:240766442 (Ack:31549812)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:37.274]  [00:03:18.609][info  ][EM] ??1 [E:29148i S:14009 M:240766442] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5641ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:37.990]  [00:03:19.326][info  ][EM] >>> [E:29148i S:14009 M:31549813 (Ack:240766442)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:38.051]  [00:03:19.386][info  ][EM] <<< [E:29148i S:14009 M:240766443 (Ack:31549813)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:38.053]  [00:03:19.387][info  ][EM] ??1 [E:29148i S:14009 M:240766443] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:38.968]  [00:03:20.303][info  ][EM] >>> [E:29148i S:14009 M:31549814 (Ack:240766443)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:39.029]  [00:03:20.364][info  ][EM] <<< [E:29148i S:14009 M:240766444 (Ack:31549814)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:39.030]  [00:03:20.365][info  ][EM] ??1 [E:29148i S:14009 M:240766444] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:39.735]  [00:03:21.070][info  ][EM] >>> [E:29148i S:14009 M:31549815 (Ack:240766444)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:39.868]  [00:03:21.204][info  ][EM] <<< [E:29148i S:14009 M:240766445 (Ack:31549815)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:39.870]  [00:03:21.204][info  ][EM] ??1 [E:29148i S:14009 M:240766445] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5297ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:39.875]  [00:03:21.205][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:06:40.508]  [00:03:21.842][info  ][EM] >>> [E:29148i S:14009 M:31549816 (Ack:240766445)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:40.568]  [00:03:21.903][info  ][EM] <<< [E:29148i S:14009 M:240766446 (Ack:31549816)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:40.569]  [00:03:21.904][info  ][EM] ??1 [E:29148i S:14009 M:240766446] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:41.262]  [00:03:22.598][info  ][EM] >>> [E:29148i S:14009 M:31549817 (Ack:240766446)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:41.323]  [00:03:22.658][info  ][EM] <<< [E:29148i S:14009 M:240766447 (Ack:31549817)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:41.325]  [00:03:22.659][info  ][EM] ??1 [E:29148i S:14009 M:240766447] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5478ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:42.051]  [00:03:23.386][info  ][EM] >>> [E:29148i S:14009 M:31549818 (Ack:240766447)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:42.111]  [00:03:23.447][info  ][EM] <<< [E:29148i S:14009 M:240766448 (Ack:31549818)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:42.114]  [00:03:23.448][info  ][EM] ??1 [E:29148i S:14009 M:240766448] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:42.931]  [00:03:24.266][info  ][EM] >>> [E:29148i S:14009 M:31549819 (Ack:240766448)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:43.065]  [00:03:24.400][info  ][EM] <<< [E:29148i S:14009 M:240766449 (Ack:31549819)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:43.067]  [00:03:24.401][info  ][EM] ??1 [E:29148i S:14009 M:240766449] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:43.074]  [00:03:24.401][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:06:43.851]  [00:03:25.186][info  ][EM] >>> [E:29148i S:14009 M:31549820 (Ack:240766449)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:43.912]  [00:03:25.247][info  ][EM] <<< [E:29148i S:14009 M:240766450 (Ack:31549820)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:43.913]  [00:03:25.248][info  ][EM] ??1 [E:29148i S:14009 M:240766450] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:44.712]  [00:03:26.047][info  ][EM] >>> [E:29148i S:14009 M:31549821 (Ack:240766450)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:44.773]  [00:03:26.108][info  ][EM] <<< [E:29148i S:14009 M:240766451 (Ack:31549821)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:44.775]  [00:03:26.109][info  ][EM] ??1 [E:29148i S:14009 M:240766451] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5299ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:45.596]  [00:03:26.930][info  ][EM] >>> [E:29148i S:14009 M:31549822 (Ack:240766451)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:45.657]  [00:03:26.991][info  ][EM] <<< [E:29148i S:14009 M:240766452 (Ack:31549822)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:45.658]  [00:03:26.992][info  ][EM] ??1 [E:29148i S:14009 M:240766452] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:46.660]  [00:03:27.995][info  ][EM] >>> [E:29148i S:14009 M:31549823 (Ack:240766452)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:46.793]  [00:03:28.128][info  ][EM] <<< [E:29148i S:14009 M:240766453 (Ack:31549823)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:46.795]  [00:03:28.129][info  ][EM] ??1 [E:29148i S:14009 M:240766453] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:46.800]  [00:03:28.129][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:06:47.538]  [00:03:28.874][info  ][EM] >>> [E:29148i S:14009 M:31549824 (Ack:240766453)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:47.599]  [00:03:28.934][info  ][EM] <<< [E:29148i S:14009 M:240766454 (Ack:31549824)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:47.600]  [00:03:28.935][info  ][EM] ??1 [E:29148i S:14009 M:240766454] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5501ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:48.413]  [00:03:29.748][info  ][EM] >>> [E:29148i S:14009 M:31549825 (Ack:240766454)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:48.473]  [00:03:29.808][info  ][EM] <<< [E:29148i S:14009 M:240766455 (Ack:31549825)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:48.475]  [00:03:29.809][info  ][EM] ??1 [E:29148i S:14009 M:240766455] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5658ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:49.198]  [00:03:30.533][info  ][EM] >>> [E:29148i S:14009 M:31549826 (Ack:240766455)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:49.258]  [00:03:30.593][info  ][EM] <<< [E:29148i S:14009 M:240766456 (Ack:31549826)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:49.260]  [00:03:30.594][info  ][EM] ??1 [E:29148i S:14009 M:240766456] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:49.953]  [00:03:31.288][info  ][EM] >>> [E:29148i S:14009 M:31549827 (Ack:240766456)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:50.089]  [00:03:31.424][info  ][EM] <<< [E:29148i S:14009 M:240766457 (Ack:31549827)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:50.091]  [00:03:31.424][info  ][EM] ??1 [E:29148i S:14009 M:240766457] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:50.096]  [00:03:31.425][error ][DL] Long dispatch time: 136 ms, for event type 2
[19:06:50.929]  [00:03:32.260][info  ][EM] >>> [E:29148i S:14009 M:31549828 (Ack:240766457)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:50.993]  [00:03:32.321][info  ][EM] <<< [E:29148i S:14009 M:240766458 (Ack:31549828)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:50.993]  [00:03:32.322][info  ][EM] ??1 [E:29148i S:14009 M:240766458] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:51.910]  [00:03:33.244][info  ][EM] >>> [E:29148i S:14009 M:31549829 (Ack:240766458)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:51.972]  [00:03:33.304][info  ][EM] <<< [E:29148i S:14009 M:240766459 (Ack:31549829)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:51.972]  [00:03:33.305][info  ][EM] ??1 [E:29148i S:14009 M:240766459] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:52.680]  [00:03:34.015][info  ][EM] >>> [E:29148i S:14009 M:31549830 (Ack:240766459)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:52.748]  [00:03:34.076][info  ][EM] <<< [E:29148i S:14009 M:240766460 (Ack:31549830)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:52.748]  [00:03:34.077][info  ][EM] ??1 [E:29148i S:14009 M:240766460] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:53.443]  [00:03:34.773][info  ][EM] >>> [E:29148i S:14009 M:31549831 (Ack:240766460)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:53.577]  [00:03:34.911][info  ][EM] <<< [E:29148i S:14009 M:240766461 (Ack:31549831)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:53.577]  [00:03:34.911][info  ][EM] ??1 [E:29148i S:14009 M:240766461] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:53.588]  [00:03:34.912][error ][DL] Long dispatch time: 139 ms, for event type 2
[19:06:54.358]  [00:03:35.680][info  ][EM] >>> [E:29148i S:14009 M:31549832 (Ack:240766461)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:54.407]  [00:03:35.741][info  ][EM] <<< [E:29148i S:14009 M:240766462 (Ack:31549832)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:54.407]  [00:03:35.742][info  ][EM] ??1 [E:29148i S:14009 M:240766462] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:55.199]  [00:03:36.532][info  ][EM] >>> [E:29148i S:14009 M:31549833 (Ack:240766462)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:55.260]  [00:03:36.591][info  ][EM] <<< [E:29148i S:14009 M:240766463 (Ack:31549833)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:55.260]  [00:03:36.592][info  ][EM] ??1 [E:29148i S:14009 M:240766463] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:56.054]  [00:03:37.375][info  ][EM] >>> [E:29148i S:14009 M:31549834 (Ack:240766463)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:56.102]  [00:03:37.435][info  ][EM] <<< [E:29148i S:14009 M:240766464 (Ack:31549834)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:56.102]  [00:03:37.436][info  ][EM] ??1 [E:29148i S:14009 M:240766464] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:56.816]  [00:03:38.144][info  ][EM] >>> [E:29148i S:14009 M:31549835 (Ack:240766464)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:56.946]  [00:03:38.278][info  ][EM] <<< [E:29148i S:14009 M:240766465 (Ack:31549835)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:56.946]  [00:03:38.279][info  ][EM] ??1 [E:29148i S:14009 M:240766465] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:56.958]  [00:03:38.280][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:06:57.596]  [00:03:38.928][info  ][EM] >>> [E:29148i S:14009 M:31549836 (Ack:240766465)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:57.655]  [00:03:38.989][info  ][EM] <<< [E:29148i S:14009 M:240766466 (Ack:31549836)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:57.655]  [00:03:38.990][info  ][EM] ??1 [E:29148i S:14009 M:240766466] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5213ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:58.331]  [00:03:39.666][info  ][EM] >>> [E:29148i S:14009 M:31549837 (Ack:240766466)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:58.394]  [00:03:39.727][info  ][EM] <<< [E:29148i S:14009 M:240766467 (Ack:31549837)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:58.394]  [00:03:39.728][info  ][EM] ??1 [E:29148i S:14009 M:240766467] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:59.090]  [00:03:40.424][info  ][EM] >>> [E:29148i S:14009 M:31549838 (Ack:240766467)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:06:59.160]  [00:03:40.485][info  ][EM] <<< [E:29148i S:14009 M:240766468 (Ack:31549838)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:06:59.160]  [00:03:40.485][info  ][EM] ??1 [E:29148i S:14009 M:240766468] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[19:06:59.982]  [00:03:41.311][info  ][EM] >>> [E:29148i S:14009 M:31549839 (Ack:240766468)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:00.115]  [00:03:41.445][info  ][EM] <<< [E:29148i S:14009 M:240766469 (Ack:31549839)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:00.115]  [00:03:41.446][info  ][EM] ??1 [E:29148i S:14009 M:240766469] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:00.126]  [00:03:41.446][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:01.227]  [00:03:42.552][info  ][EM] >>> [E:29148i S:14009 M:31549840 (Ack:240766469)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:01.292]  [00:03:42.613][info  ][EM] <<< [E:29148i S:14009 M:240766470 (Ack:31549840)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:01.292]  [00:03:42.613][info  ][EM] ??1 [E:29148i S:14009 M:240766470] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:02.107]  [00:03:43.434][info  ][EM] >>> [E:29148i S:14009 M:31549841 (Ack:240766470)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:02.161]  [00:03:43.495][info  ][EM] <<< [E:29148i S:14009 M:240766471 (Ack:31549841)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:02.161]  [00:03:43.496][info  ][EM] ??1 [E:29148i S:14009 M:240766471] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:03.073]  [00:03:44.396][info  ][EM] >>> [E:29148i S:14009 M:31549842 (Ack:240766471)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:03.122]  [00:03:44.457][info  ][EM] <<< [E:29148i S:14009 M:240766472 (Ack:31549842)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:03.133]  [00:03:44.458][info  ][EM] ??1 [E:29148i S:14009 M:240766472] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:04.707]  [00:03:46.034][info  ][EM] >>> [E:29148i S:14009 M:31549843 (Ack:240766472)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:04.835]  [00:03:46.167][info  ][EM] <<< [E:29148i S:14009 M:240766473 (Ack:31549843)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:04.835]  [00:03:46.168][info  ][EM] ??1 [E:29148i S:14009 M:240766473] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:04.850]  [00:03:46.168][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:07:05.473]  [00:03:46.794][info  ][EM] >>> [E:29148i S:14009 M:31549844 (Ack:240766473)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:05.520]  [00:03:46.855][info  ][EM] <<< [E:29148i S:14009 M:240766474 (Ack:31549844)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:05.533]  [00:03:46.855][info  ][EM] ??1 [E:29148i S:14009 M:240766474] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:06.512]  [00:03:47.840][info  ][EM] >>> [E:29148i S:14009 M:31549845 (Ack:240766474)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:06.570]  [00:03:47.901][info  ][EM] <<< [E:29148i S:14009 M:240766475 (Ack:31549845)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:06.570]  [00:03:47.902][info  ][EM] ??1 [E:29148i S:14009 M:240766475] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:07.257]  [00:03:48.584][info  ][EM] >>> [E:29148i S:14009 M:31549846 (Ack:240766475)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:07.310]  [00:03:48.645][info  ][EM] <<< [E:29148i S:14009 M:240766476 (Ack:31549846)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:07.322]  [00:03:48.645][info  ][EM] ??1 [E:29148i S:14009 M:240766476] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:08.045]  [00:03:49.379][info  ][EM] >>> [E:29148i S:14009 M:31549847 (Ack:240766476)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:08.180]  [00:03:49.513][info  ][EM] <<< [E:29148i S:14009 M:240766477 (Ack:31549847)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:08.180]  [00:03:49.514][info  ][EM] ??1 [E:29148i S:14009 M:240766477] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:08.192]  [00:03:49.514][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:09.500]  [00:03:50.834][info  ][EM] >>> [E:29148i S:14009 M:31549848 (Ack:240766477)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:09.561]  [00:03:50.895][info  ][EM] <<< [E:29148i S:14009 M:240766478 (Ack:31549848)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:09.575]  [00:03:50.896][info  ][EM] ??1 [E:29148i S:14009 M:240766478] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5729ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:10.563]  [00:03:51.895][info  ][EM] >>> [E:29148i S:14009 M:31549849 (Ack:240766478)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:10.626]  [00:03:51.955][info  ][EM] <<< [E:29148i S:14009 M:240766479 (Ack:31549849)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:10.626]  [00:03:51.956][info  ][EM] ??1 [E:29148i S:14009 M:240766479] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:11.645]  [00:03:52.974][info  ][EM] >>> [E:29148i S:14009 M:31549850 (Ack:240766479)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:11.707]  [00:03:53.035][info  ][EM] <<< [E:29148i S:14009 M:240766480 (Ack:31549850)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:11.707]  [00:03:53.036][info  ][EM] ??1 [E:29148i S:14009 M:240766480] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5656ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:12.410]  [00:03:53.739][info  ][EM] >>> [E:29148i S:14009 M:31549851 (Ack:240766480)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:12.537]  [00:03:53.873][info  ][EM] <<< [E:29148i S:14009 M:240766481 (Ack:31549851)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:12.549]  [00:03:53.874][info  ][EM] ??1 [E:29148i S:14009 M:240766481] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:12.549]  [00:03:53.874][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:13.190]  [00:03:54.514][info  ][EM] >>> [E:29148i S:14009 M:31549852 (Ack:240766481)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:13.243]  [00:03:54.575][info  ][EM] <<< [E:29148i S:14009 M:240766482 (Ack:31549852)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:13.243]  [00:03:54.576][info  ][EM] ??1 [E:29148i S:14009 M:240766482] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:14.149]  [00:03:55.475][info  ][EM] >>> [E:29148i S:14009 M:31549853 (Ack:240766482)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:14.210]  [00:03:55.535][info  ][EM] <<< [E:29148i S:14009 M:240766483 (Ack:31549853)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:14.210]  [00:03:55.536][info  ][EM] ??1 [E:29148i S:14009 M:240766483] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:15.044]  [00:03:56.375][info  ][EM] >>> [E:29148i S:14009 M:31549854 (Ack:240766483)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:15.112]  [00:03:56.436][info  ][EM] <<< [E:29148i S:14009 M:240766484 (Ack:31549854)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:15.112]  [00:03:56.437][info  ][EM] ??1 [E:29148i S:14009 M:240766484] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5375ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:15.826]  [00:03:57.160][info  ][EM] >>> [E:29148i S:14009 M:31549855 (Ack:240766484)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:15.965]  [00:03:57.293][info  ][EM] <<< [E:29148i S:14009 M:240766485 (Ack:31549855)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:15.965]  [00:03:57.294][info  ][EM] ??1 [E:29148i S:14009 M:240766485] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:15.976]  [00:03:57.294][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:16.900]  [00:03:58.234][info  ][EM] >>> [E:29148i S:14009 M:31549856 (Ack:240766485)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:16.968]  [00:03:58.294][info  ][EM] <<< [E:29148i S:14009 M:240766486 (Ack:31549856)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:16.968]  [00:03:58.295][info  ][EM] ??1 [E:29148i S:14009 M:240766486] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:17.776]  [00:03:59.099][info  ][EM] >>> [E:29148i S:14009 M:31549857 (Ack:240766486)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:17.826]  [00:03:59.160][info  ][EM] <<< [E:29148i S:14009 M:240766487 (Ack:31549857)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:17.826]  [00:03:59.161][info  ][EM] ??1 [E:29148i S:14009 M:240766487] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:18.550]  [00:03:59.879][info  ][EM] >>> [E:29148i S:14009 M:31549858 (Ack:240766487)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:18.616]  [00:03:59.940][info  ][EM] <<< [E:29148i S:14009 M:240766488 (Ack:31549858)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:18.616]  [00:03:59.940][info  ][EM] ??1 [E:29148i S:14009 M:240766488] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:19.282]  [00:04:00.617][info  ][EM] >>> [E:29148i S:14009 M:31549859 (Ack:240766488)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:19.419]  [00:04:00.750][info  ][EM] <<< [E:29148i S:14009 M:240766489 (Ack:31549859)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:19.419]  [00:04:00.751][info  ][EM] ??1 [E:29148i S:14009 M:240766489] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:19.431]  [00:04:00.751][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:07:20.079]  [00:04:01.409][info  ][EM] >>> [E:29148i S:14009 M:31549860 (Ack:240766489)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:20.143]  [00:04:01.469][info  ][EM] <<< [E:29148i S:14009 M:240766490 (Ack:31549860)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:20.143]  [00:04:01.470][info  ][EM] ??1 [E:29148i S:14009 M:240766490] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:20.870]  [00:04:02.199][info  ][EM] >>> [E:29148i S:14009 M:31549861 (Ack:240766490)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:20.927]  [00:04:02.259][info  ][EM] <<< [E:29148i S:14009 M:240766491 (Ack:31549861)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:20.927]  [00:04:02.260][info  ][EM] ??1 [E:29148i S:14009 M:240766491] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:21.612]  [00:04:02.943][info  ][EM] >>> [E:29148i S:14009 M:31549862 (Ack:240766491)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:21.673]  [00:04:03.003][info  ][EM] <<< [E:29148i S:14009 M:240766492 (Ack:31549862)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:21.673]  [00:04:03.004][info  ][EM] ??1 [E:29148i S:14009 M:240766492] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:22.491]  [00:04:03.823][info  ][EM] >>> [E:29148i S:14009 M:31549863 (Ack:240766492)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:22.625]  [00:04:03.957][info  ][EM] <<< [E:29148i S:14009 M:240766493 (Ack:31549863)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:22.625]  [00:04:03.958][info  ][EM] ??1 [E:29148i S:14009 M:240766493] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:22.636]  [00:04:03.958][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:23.261]  [00:04:04.591][info  ][EM] >>> [E:29148i S:14009 M:31549864 (Ack:240766493)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:23.320]  [00:04:04.652][info  ][EM] <<< [E:29148i S:14009 M:240766494 (Ack:31549864)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:23.320]  [00:04:04.653][info  ][EM] ??1 [E:29148i S:14009 M:240766494] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:24.171]  [00:04:05.495][info  ][EM] >>> [E:29148i S:14009 M:31549865 (Ack:240766494)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:24.229]  [00:04:05.555][info  ][EM] <<< [E:29148i S:14009 M:240766495 (Ack:31549865)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:24.229]  [00:04:05.556][info  ][EM] ??1 [E:29148i S:14009 M:240766495] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:25.040]  [00:04:06.368][info  ][EM] >>> [E:29148i S:14009 M:31549866 (Ack:240766495)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:25.100]  [00:04:06.428][info  ][EM] <<< [E:29148i S:14009 M:240766496 (Ack:31549866)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:25.100]  [00:04:06.429][info  ][EM] ??1 [E:29148i S:14009 M:240766496] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5286ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:25.785]  [00:04:07.108][info  ][EM] >>> [E:29148i S:14009 M:31549867 (Ack:240766496)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:25.908]  [00:04:07.240][info  ][EM] <<< [E:29148i S:14009 M:240766497 (Ack:31549867)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:25.908]  [00:04:07.241][info  ][EM] ??1 [E:29148i S:14009 M:240766497] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:25.919]  [00:04:07.241][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:07:26.636]  [00:04:07.958][info  ][EM] >>> [E:29148i S:14009 M:31549868 (Ack:240766497)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:26.685]  [00:04:08.018][info  ][EM] <<< [E:29148i S:14009 M:240766498 (Ack:31549868)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:26.696]  [00:04:08.019][info  ][EM] ??1 [E:29148i S:14009 M:240766498] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5643ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:27.509]  [00:04:08.844][info  ][EM] >>> [E:29148i S:14009 M:31549869 (Ack:240766498)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:27.574]  [00:04:08.905][info  ][EM] <<< [E:29148i S:14009 M:240766499 (Ack:31549869)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:27.574]  [00:04:08.905][info  ][EM] ??1 [E:29148i S:14009 M:240766499] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5435ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:28.286]  [00:04:09.612][info  ][EM] >>> [E:29148i S:14009 M:31549870 (Ack:240766499)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:28.348]  [00:04:09.672][info  ][EM] <<< [E:29148i S:14009 M:240766500 (Ack:31549870)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:28.348]  [00:04:09.673][info  ][EM] ??1 [E:29148i S:14009 M:240766500] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:29.378]  [00:04:10.709][info  ][EM] >>> [E:29148i S:14009 M:31549871 (Ack:240766500)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:29.514]  [00:04:10.843][info  ][EM] <<< [E:29148i S:14009 M:240766501 (Ack:31549871)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:29.514]  [00:04:10.844][info  ][EM] ??1 [E:29148i S:14009 M:240766501] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:29.526]  [00:04:10.845][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:30.260]  [00:04:11.585][info  ][EM] >>> [E:29148i S:14009 M:31549872 (Ack:240766501)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:30.319]  [00:04:11.646][info  ][EM] <<< [E:29148i S:14009 M:240766502 (Ack:31549872)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:30.319]  [00:04:11.646][info  ][EM] ??1 [E:29148i S:14009 M:240766502] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:31.037]  [00:04:12.368][info  ][EM] >>> [E:29148i S:14009 M:31549873 (Ack:240766502)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:31.093]  [00:04:12.428][info  ][EM] <<< [E:29148i S:14009 M:240766503 (Ack:31549873)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:31.104]  [00:04:12.428][info  ][EM] ??1 [E:29148i S:14009 M:240766503] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:31.922]  [00:04:13.253][info  ][EM] >>> [E:29148i S:14009 M:31549874 (Ack:240766503)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:31.979]  [00:04:13.314][info  ][EM] <<< [E:29148i S:14009 M:240766504 (Ack:31549874)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:31.991]  [00:04:13.315][info  ][EM] ??1 [E:29148i S:14009 M:240766504] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5682ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:32.930]  [00:04:14.261][info  ][EM] >>> [E:29148i S:14009 M:31549875 (Ack:240766504)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:33.061]  [00:04:14.395][info  ][EM] <<< [E:29148i S:14009 M:240766505 (Ack:31549875)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:33.072]  [00:04:14.396][info  ][EM] ??1 [E:29148i S:14009 M:240766505] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:33.072]  [00:04:14.396][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:33.986]  [00:04:15.306][info  ][EM] >>> [E:29148i S:14009 M:31549876 (Ack:240766505)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:34.045]  [00:04:15.366][info  ][EM] <<< [E:29148i S:14009 M:240766506 (Ack:31549876)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:34.045]  [00:04:15.367][info  ][EM] ??1 [E:29148i S:14009 M:240766506] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:34.796]  [00:04:16.126][info  ][EM] >>> [E:29148i S:14009 M:31549877 (Ack:240766506)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:34.857]  [00:04:16.187][info  ][EM] <<< [E:29148i S:14009 M:240766507 (Ack:31549877)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:34.857]  [00:04:16.187][info  ][EM] ??1 [E:29148i S:14009 M:240766507] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:35.550]  [00:04:16.884][info  ][EM] >>> [E:29148i S:14009 M:31549878 (Ack:240766507)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:35.612]  [00:04:16.945][info  ][EM] <<< [E:29148i S:14009 M:240766508 (Ack:31549878)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:35.612]  [00:04:16.946][info  ][EM] ??1 [E:29148i S:14009 M:240766508] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:36.351]  [00:04:17.675][info  ][EM] >>> [E:29148i S:14009 M:31549879 (Ack:240766508)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:36.486]  [00:04:17.809][info  ][EM] <<< [E:29148i S:14009 M:240766509 (Ack:31549879)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:36.486]  [00:04:17.810][info  ][EM] ??1 [E:29148i S:14009 M:240766509] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:36.486]  [00:04:17.810][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:37.259]  [00:04:18.581][info  ][EM] >>> [E:29148i S:14009 M:31549880 (Ack:240766509)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:37.307]  [00:04:18.641][info  ][EM] <<< [E:29148i S:14009 M:240766510 (Ack:31549880)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:37.321]  [00:04:18.641][info  ][EM] ??1 [E:29148i S:14009 M:240766510] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:38.155]  [00:04:19.490][info  ][EM] >>> [E:29148i S:14009 M:31549881 (Ack:240766510)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:38.226]  [00:04:19.550][info  ][EM] <<< [E:29148i S:14009 M:240766511 (Ack:31549881)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:38.226]  [00:04:19.551][info  ][EM] ??1 [E:29148i S:14009 M:240766511] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:38.929]  [00:04:20.258][info  ][EM] >>> [E:29148i S:14009 M:31549882 (Ack:240766511)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:38.986]  [00:04:20.319][info  ][EM] <<< [E:29148i S:14009 M:240766512 (Ack:31549882)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:38.986]  [00:04:20.319][info  ][EM] ??1 [E:29148i S:14009 M:240766512] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:40.253]  [00:04:21.576][info  ][EM] >>> [E:29148i S:14009 M:31549883 (Ack:240766512)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:40.384]  [00:04:21.709][info  ][EM] <<< [E:29148i S:14009 M:240766513 (Ack:31549883)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:40.384]  [00:04:21.709][info  ][EM] ??1 [E:29148i S:14009 M:240766513] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5478ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:40.384]  [00:04:21.710][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:41.136]  [00:04:22.470][info  ][EM] >>> [E:29148i S:14009 M:31549884 (Ack:240766513)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:41.205]  [00:04:22.531][info  ][EM] <<< [E:29148i S:14009 M:240766514 (Ack:31549884)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:41.205]  [00:04:22.532][info  ][EM] ??1 [E:29148i S:14009 M:240766514] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:41.930]  [00:04:23.261][info  ][EM] >>> [E:29148i S:14009 M:31549885 (Ack:240766514)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:41.989]  [00:04:23.322][info  ][EM] <<< [E:29148i S:14009 M:240766515 (Ack:31549885)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:41.989]  [00:04:23.323][info  ][EM] ??1 [E:29148i S:14009 M:240766515] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5471ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:42.700]  [00:04:24.023][info  ][EM] >>> [E:29148i S:14009 M:31549886 (Ack:240766515)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:42.751]  [00:04:24.083][info  ][EM] <<< [E:29148i S:14009 M:240766516 (Ack:31549886)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:42.751]  [00:04:24.084][info  ][EM] ??1 [E:29148i S:14009 M:240766516] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5508ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:43.699]  [00:04:25.028][info  ][EM] >>> [E:29148i S:14009 M:31549887 (Ack:240766516)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:43.834]  [00:04:25.161][info  ][EM] <<< [E:29148i S:14009 M:240766517 (Ack:31549887)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:43.834]  [00:04:25.162][info  ][EM] ??1 [E:29148i S:14009 M:240766517] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5220ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:43.834]  [00:04:25.163][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:44.777]  [00:04:26.101][info  ][EM] >>> [E:29148i S:14009 M:31549888 (Ack:240766517)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:44.828]  [00:04:26.162][info  ][EM] <<< [E:29148i S:14009 M:240766518 (Ack:31549888)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:44.845]  [00:04:26.163][info  ][EM] ??1 [E:29148i S:14009 M:240766518] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:45.550]  [00:04:26.883][info  ][EM] >>> [E:29148i S:14009 M:31549889 (Ack:240766518)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:45.615]  [00:04:26.944][info  ][EM] <<< [E:29148i S:14009 M:240766519 (Ack:31549889)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:45.615]  [00:04:26.944][info  ][EM] ??1 [E:29148i S:14009 M:240766519] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5203ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:46.347]  [00:04:27.667][info  ][EM] >>> [E:29148i S:14009 M:31549890 (Ack:240766519)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:46.403]  [00:04:27.728][info  ][EM] <<< [E:29148i S:14009 M:240766520 (Ack:31549890)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:46.403]  [00:04:27.729][info  ][EM] ??1 [E:29148i S:14009 M:240766520] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:47.106]  [00:04:28.434][info  ][EM] >>> [E:29148i S:14009 M:31549891 (Ack:240766520)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:47.237]  [00:04:28.568][info  ][EM] <<< [E:29148i S:14009 M:240766521 (Ack:31549891)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:47.237]  [00:04:28.569][info  ][EM] ??1 [E:29148i S:14009 M:240766521] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:47.249]  [00:04:28.569][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:47.916]  [00:04:29.246][info  ][EM] >>> [E:29148i S:14009 M:31549892 (Ack:240766521)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:47.978]  [00:04:29.306][info  ][EM] <<< [E:29148i S:14009 M:240766522 (Ack:31549892)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:47.978]  [00:04:29.307][info  ][EM] ??1 [E:29148i S:14009 M:240766522] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:48.720]  [00:04:30.043][info  ][EM] >>> [E:29148i S:14009 M:31549893 (Ack:240766522)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:48.770]  [00:04:30.104][info  ][EM] <<< [E:29148i S:14009 M:240766523 (Ack:31549893)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:48.783]  [00:04:30.105][info  ][EM] ??1 [E:29148i S:14009 M:240766523] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:49.623]  [00:04:30.950][info  ][EM] >>> [E:29148i S:14009 M:31549894 (Ack:240766523)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:49.685]  [00:04:31.010][info  ][EM] <<< [E:29148i S:14009 M:240766524 (Ack:31549894)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:49.685]  [00:04:31.011][info  ][EM] ??1 [E:29148i S:14009 M:240766524] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:50.369]  [00:04:31.696][info  ][EM] >>> [E:29148i S:14009 M:31549895 (Ack:240766524)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:50.494]  [00:04:31.830][info  ][EM] <<< [E:29148i S:14009 M:240766525 (Ack:31549895)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:50.507]  [00:04:31.830][info  ][EM] ??1 [E:29148i S:14009 M:240766525] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5304ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:50.507]  [00:04:31.831][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:51.269]  [00:04:32.587][info  ][EM] >>> [E:29148i S:14009 M:31549896 (Ack:240766525)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:51.315]  [00:04:32.648][info  ][EM] <<< [E:29148i S:14009 M:240766526 (Ack:31549896)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:51.315]  [00:04:32.649][info  ][EM] ??1 [E:29148i S:14009 M:240766526] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:52.359]  [00:04:33.694][info  ][EM] >>> [E:29148i S:14009 M:31549897 (Ack:240766526)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:52.420]  [00:04:33.754][info  ][EM] <<< [E:29148i S:14009 M:240766527 (Ack:31549897)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:52.432]  [00:04:33.755][info  ][EM] ??1 [E:29148i S:14009 M:240766527] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5390ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:53.157]  [00:04:34.489][info  ][EM] >>> [E:29148i S:14009 M:31549898 (Ack:240766527)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:53.217]  [00:04:34.549][info  ][EM] <<< [E:29148i S:14009 M:240766528 (Ack:31549898)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:53.217]  [00:04:34.549][info  ][EM] ??1 [E:29148i S:14009 M:240766528] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:54.565]  [00:04:35.890][info  ][EM] >>> [E:29148i S:14009 M:31549899 (Ack:240766528)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:54.696]  [00:04:36.024][info  ][EM] <<< [E:29148i S:14009 M:240766529 (Ack:31549899)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:54.696]  [00:04:36.024][info  ][EM] ??1 [E:29148i S:14009 M:240766529] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:54.696]  [00:04:36.025][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:07:55.660]  [00:04:36.983][info  ][EM] >>> [E:29148i S:14009 M:31549900 (Ack:240766529)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:55.710]  [00:04:37.043][info  ][EM] <<< [E:29148i S:14009 M:240766530 (Ack:31549900)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:55.710]  [00:04:37.044][info  ][EM] ??1 [E:29148i S:14009 M:240766530] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5291ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:56.413]  [00:04:37.747][info  ][EM] >>> [E:29148i S:14009 M:31549901 (Ack:240766530)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:56.481]  [00:04:37.807][info  ][EM] <<< [E:29148i S:14009 M:240766531 (Ack:31549901)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:56.481]  [00:04:37.808][info  ][EM] ??1 [E:29148i S:14009 M:240766531] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:57.188]  [00:04:38.518][info  ][EM] >>> [E:29148i S:14009 M:31549902 (Ack:240766531)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:57.249]  [00:04:38.579][info  ][EM] <<< [E:29148i S:14009 M:240766532 (Ack:31549902)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:57.249]  [00:04:38.580][info  ][EM] ??1 [E:29148i S:14009 M:240766532] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:57.974]  [00:04:39.305][info  ][EM] >>> [E:29148i S:14009 M:31549903 (Ack:240766532)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:58.110]  [00:04:39.439][info  ][EM] <<< [E:29148i S:14009 M:240766533 (Ack:31549903)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:58.110]  [00:04:39.440][info  ][EM] ??1 [E:29148i S:14009 M:240766533] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:58.110]  [00:04:39.440][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:07:58.958]  [00:04:40.291][info  ][EM] >>> [E:29148i S:14009 M:31549904 (Ack:240766533)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:59.020]  [00:04:40.350][info  ][EM] <<< [E:29148i S:14009 M:240766534 (Ack:31549904)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:59.020]  [00:04:40.351][info  ][EM] ??1 [E:29148i S:14009 M:240766534] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[19:07:59.757]  [00:04:41.090][info  ][EM] >>> [E:29148i S:14009 M:31549905 (Ack:240766534)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:07:59.819]  [00:04:41.151][info  ][EM] <<< [E:29148i S:14009 M:240766535 (Ack:31549905)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:07:59.819]  [00:04:41.152][info  ][EM] ??1 [E:29148i S:14009 M:240766535] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:01.138]  [00:04:42.473][info  ][EM] >>> [E:29148i S:14009 M:31549906 (Ack:240766535)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:01.200]  [00:04:42.534][info  ][EM] <<< [E:29148i S:14009 M:240766536 (Ack:31549906)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:01.200]  [00:04:42.535][info  ][EM] ??1 [E:29148i S:14009 M:240766536] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:02.271]  [00:04:43.606][info  ][EM] >>> [E:29148i S:14009 M:31549907 (Ack:240766536)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:02.415]  [00:04:43.740][info  ][EM] <<< [E:29148i S:14009 M:240766537 (Ack:31549907)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:02.415]  [00:04:43.741][info  ][EM] ??1 [E:29148i S:14009 M:240766537] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:02.415]  [00:04:43.741][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:03.079]  [00:04:44.409][info  ][EM] >>> [E:29148i S:14009 M:31549908 (Ack:240766537)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:03.134]  [00:04:44.469][info  ][EM] <<< [E:29148i S:14009 M:240766538 (Ack:31549908)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:03.147]  [00:04:44.470][info  ][EM] ??1 [E:29148i S:14009 M:240766538] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:03.979]  [00:04:45.308][info  ][EM] >>> [E:29148i S:14009 M:31549909 (Ack:240766538)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:04.044]  [00:04:45.369][info  ][EM] <<< [E:29148i S:14009 M:240766539 (Ack:31549909)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:04.044]  [00:04:45.370][info  ][EM] ??1 [E:29148i S:14009 M:240766539] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:05.083]  [00:04:46.413][info  ][EM] >>> [E:29148i S:14009 M:31549910 (Ack:240766539)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:05.144]  [00:04:46.473][info  ][EM] <<< [E:29148i S:14009 M:240766540 (Ack:31549910)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:05.144]  [00:04:46.474][info  ][EM] ??1 [E:29148i S:14009 M:240766540] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5729ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:05.844]  [00:04:47.168][info  ][EM] >>> [E:29148i S:14009 M:31549911 (Ack:240766540)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:05.975]  [00:04:47.302][info  ][EM] <<< [E:29148i S:14009 M:240766541 (Ack:31549911)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:05.975]  [00:04:47.303][info  ][EM] ??1 [E:29148i S:14009 M:240766541] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5443ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:05.975]  [00:04:47.303][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:06.644]  [00:04:47.969][info  ][EM] >>> [E:29148i S:14009 M:31549912 (Ack:240766541)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:06.704]  [00:04:48.030][info  ][EM] <<< [E:29148i S:14009 M:240766542 (Ack:31549912)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:06.704]  [00:04:48.031][info  ][EM] ??1 [E:29148i S:14009 M:240766542] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:07.391]  [00:04:48.721][info  ][EM] >>> [E:29148i S:14009 M:31549913 (Ack:240766542)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:07.449]  [00:04:48.782][info  ][EM] <<< [E:29148i S:14009 M:240766543 (Ack:31549913)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:07.449]  [00:04:48.783][info  ][EM] ??1 [E:29148i S:14009 M:240766543] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:08.291]  [00:04:49.625][info  ][EM] >>> [E:29148i S:14009 M:31549914 (Ack:240766543)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:08.351]  [00:04:49.686][info  ][EM] <<< [E:29148i S:14009 M:240766544 (Ack:31549914)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:08.364]  [00:04:49.687][info  ][EM] ??1 [E:29148i S:14009 M:240766544] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:09.072]  [00:04:50.400][info  ][EM] >>> [E:29148i S:14009 M:31549915 (Ack:240766544)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:09.198]  [00:04:50.534][info  ][EM] <<< [E:29148i S:14009 M:240766545 (Ack:31549915)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:09.209]  [00:04:50.535][info  ][EM] ??1 [E:29148i S:14009 M:240766545] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:09.209]  [00:04:50.535][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:10.761]  [00:04:52.088][info  ][EM] >>> [E:29148i S:14009 M:31549916 (Ack:240766545)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:10.820]  [00:04:52.149][info  ][EM] <<< [E:29148i S:14009 M:240766546 (Ack:31549916)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:10.820]  [00:04:52.149][info  ][EM] ??1 [E:29148i S:14009 M:240766546] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:11.857]  [00:04:53.190][info  ][EM] >>> [E:29148i S:14009 M:31549917 (Ack:240766546)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:11.922]  [00:04:53.250][info  ][EM] <<< [E:29148i S:14009 M:240766547 (Ack:31549917)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:11.922]  [00:04:53.250][info  ][EM] ??1 [E:29148i S:14009 M:240766547] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5587ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:12.649]  [00:04:53.979][info  ][EM] >>> [E:29148i S:14009 M:31549918 (Ack:240766547)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:12.712]  [00:04:54.040][info  ][EM] <<< [E:29148i S:14009 M:240766548 (Ack:31549918)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:12.712]  [00:04:54.040][info  ][EM] ??1 [E:29148i S:14009 M:240766548] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:13.955]  [00:04:55.288][info  ][EM] >>> [E:29148i S:14009 M:31549919 (Ack:240766548)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:14.087]  [00:04:55.421][info  ][EM] <<< [E:29148i S:14009 M:240766549 (Ack:31549919)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:14.087]  [00:04:55.422][info  ][EM] ??1 [E:29148i S:14009 M:240766549] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:14.099]  [00:04:55.422][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:08:14.862]  [00:04:56.197][info  ][EM] >>> [E:29148i S:14009 M:31549920 (Ack:240766549)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:14.921]  [00:04:56.257][info  ][EM] <<< [E:29148i S:14009 M:240766550 (Ack:31549920)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:14.934]  [00:04:56.258][info  ][EM] ??1 [E:29148i S:14009 M:240766550] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:15.789]  [00:04:57.125][info  ][EM] >>> [E:29148i S:14009 M:31549921 (Ack:240766550)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:15.854]  [00:04:57.185][info  ][EM] <<< [E:29148i S:14009 M:240766551 (Ack:31549921)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:15.854]  [00:04:57.186][info  ][EM] ??1 [E:29148i S:14009 M:240766551] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5484ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:16.904]  [00:04:58.241][info  ][EM] >>> [E:29148i S:14009 M:31549922 (Ack:240766551)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:16.966]  [00:04:58.301][info  ][EM] <<< [E:29148i S:14009 M:240766552 (Ack:31549922)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:16.977]  [00:04:58.302][info  ][EM] ??1 [E:29148i S:14009 M:240766552] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5213ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:17.694]  [00:04:59.028][info  ][EM] >>> [E:29148i S:14009 M:31549923 (Ack:240766552)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:17.836]  [00:04:59.162][info  ][EM] <<< [E:29148i S:14009 M:240766553 (Ack:31549923)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:17.836]  [00:04:59.163][info  ][EM] ??1 [E:29148i S:14009 M:240766553] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:17.836]  [00:04:59.163][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:18.822]  [00:05:00.147][info  ][EM] >>> [E:29148i S:14009 M:31549924 (Ack:240766553)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:18.873]  [00:05:00.208][info  ][EM] <<< [E:29148i S:14009 M:240766554 (Ack:31549924)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:18.873]  [00:05:00.208][info  ][EM] ??1 [E:29148i S:14009 M:240766554] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:19.778]  [00:05:01.112][info  ][EM] >>> [E:29148i S:14009 M:31549925 (Ack:240766554)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:19.836]  [00:05:01.172][info  ][EM] <<< [E:29148i S:14009 M:240766555 (Ack:31549925)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:19.847]  [00:05:01.172][info  ][EM] ??1 [E:29148i S:14009 M:240766555] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5297ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:20.902]  [00:05:02.238][info  ][EM] >>> [E:29148i S:14009 M:31549926 (Ack:240766555)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:20.977]  [00:05:02.298][info  ][EM] <<< [E:29148i S:14009 M:240766556 (Ack:31549926)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:20.977]  [00:05:02.299][info  ][EM] ??1 [E:29148i S:14009 M:240766556] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:21.746]  [00:05:03.083][info  ][EM] >>> [E:29148i S:14009 M:31549927 (Ack:240766556)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:21.886]  [00:05:03.216][info  ][EM] <<< [E:29148i S:14009 M:240766557 (Ack:31549927)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:21.886]  [00:05:03.217][info  ][EM] ??1 [E:29148i S:14009 M:240766557] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:21.898]  [00:05:03.217][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:22.837]  [00:05:04.166][info  ][EM] >>> [E:29148i S:14009 M:31549928 (Ack:240766557)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:22.902]  [00:05:04.227][info  ][EM] <<< [E:29148i S:14009 M:240766558 (Ack:31549928)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:22.902]  [00:05:04.228][info  ][EM] ??1 [E:29148i S:14009 M:240766558] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:23.822]  [00:05:05.151][info  ][EM] >>> [E:29148i S:14009 M:31549929 (Ack:240766558)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:23.878]  [00:05:05.211][info  ][EM] <<< [E:29148i S:14009 M:240766559 (Ack:31549929)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:23.878]  [00:05:05.212][info  ][EM] ??1 [E:29148i S:14009 M:240766559] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:24.944]  [00:05:06.270][info  ][EM] >>> [E:29148i S:14009 M:31549930 (Ack:240766559)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:24.995]  [00:05:06.330][info  ][EM] <<< [E:29148i S:14009 M:240766560 (Ack:31549930)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:24.995]  [00:05:06.331][info  ][EM] ??1 [E:29148i S:14009 M:240766560] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:25.978]  [00:05:07.307][info  ][EM] >>> [E:29148i S:14009 M:31549931 (Ack:240766560)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:26.113]  [00:05:07.441][info  ][EM] <<< [E:29148i S:14009 M:240766561 (Ack:31549931)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:26.113]  [00:05:07.441][info  ][EM] ??1 [E:29148i S:14009 M:240766561] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:26.113]  [00:05:07.442][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:27.369]  [00:05:08.703][info  ][EM] >>> [E:29148i S:14009 M:31549932 (Ack:240766561)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:27.433]  [00:05:08.763][info  ][EM] <<< [E:29148i S:14009 M:240766562 (Ack:31549932)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:27.433]  [00:05:08.763][info  ][EM] ??1 [E:29148i S:14009 M:240766562] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:28.379]  [00:05:09.712][info  ][EM] >>> [E:29148i S:14009 M:31549933 (Ack:240766562)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:28.448]  [00:05:09.773][info  ][EM] <<< [E:29148i S:14009 M:240766563 (Ack:31549933)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:28.448]  [00:05:09.774][info  ][EM] ??1 [E:29148i S:14009 M:240766563] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:29.385]  [00:05:10.720][info  ][EM] >>> [E:29148i S:14009 M:31549934 (Ack:240766563)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:29.447]  [00:05:10.781][info  ][EM] <<< [E:29148i S:14009 M:240766564 (Ack:31549934)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:29.447]  [00:05:10.782][info  ][EM] ??1 [E:29148i S:14009 M:240766564] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:30.399]  [00:05:11.733][info  ][EM] >>> [E:29148i S:14009 M:31549935 (Ack:240766564)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:30.533]  [00:05:11.867][info  ][EM] <<< [E:29148i S:14009 M:240766565 (Ack:31549935)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:30.533]  [00:05:11.867][info  ][EM] ??1 [E:29148i S:14009 M:240766565] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:30.547]  [00:05:11.868][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:31.218]  [00:05:12.548][info  ][EM] >>> [E:29148i S:14009 M:31549936 (Ack:240766565)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:31.272]  [00:05:12.609][info  ][EM] <<< [E:29148i S:14009 M:240766566 (Ack:31549936)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:31.284]  [00:05:12.610][info  ][EM] ??1 [E:29148i S:14009 M:240766566] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5544ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:31.997]  [00:05:13.333][info  ][EM] >>> [E:29148i S:14009 M:31549937 (Ack:240766566)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:32.059]  [00:05:13.393][info  ][EM] <<< [E:29148i S:14009 M:240766567 (Ack:31549937)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:32.059]  [00:05:13.394][info  ][EM] ??1 [E:29148i S:14009 M:240766567] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:33.359]  [00:05:14.688][info  ][EM] >>> [E:29148i S:14009 M:31549938 (Ack:240766567)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:33.412]  [00:05:14.749][info  ][EM] <<< [E:29148i S:14009 M:240766568 (Ack:31549938)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:33.423]  [00:05:14.750][info  ][EM] ??1 [E:29148i S:14009 M:240766568] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:34.373]  [00:05:15.700][info  ][EM] >>> [E:29148i S:14009 M:31549939 (Ack:240766568)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:34.508]  [00:05:15.833][info  ][EM] <<< [E:29148i S:14009 M:240766569 (Ack:31549939)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:34.508]  [00:05:15.834][info  ][EM] ??1 [E:29148i S:14009 M:240766569] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:34.508]  [00:05:15.835][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:35.158]  [00:05:16.482][info  ][EM] >>> [E:29148i S:14009 M:31549940 (Ack:240766569)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:35.215]  [00:05:16.542][info  ][EM] <<< [E:29148i S:14009 M:240766570 (Ack:31549940)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:35.215]  [00:05:16.543][info  ][EM] ??1 [E:29148i S:14009 M:240766570] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5209ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:36.146]  [00:05:17.478][info  ][EM] >>> [E:29148i S:14009 M:31549941 (Ack:240766570)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:36.213]  [00:05:17.538][info  ][EM] <<< [E:29148i S:14009 M:240766571 (Ack:31549941)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:36.213]  [00:05:17.539][info  ][EM] ??1 [E:29148i S:14009 M:240766571] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:37.172]  [00:05:18.506][info  ][EM] >>> [E:29148i S:14009 M:31549942 (Ack:240766571)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:37.235]  [00:05:18.567][info  ][EM] <<< [E:29148i S:14009 M:240766572 (Ack:31549942)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:37.235]  [00:05:18.567][info  ][EM] ??1 [E:29148i S:14009 M:240766572] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:37.979]  [00:05:19.307][info  ][EM] >>> [E:29148i S:14009 M:31549943 (Ack:240766572)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:38.107]  [00:05:19.441][info  ][EM] <<< [E:29148i S:14009 M:240766573 (Ack:31549943)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:38.107]  [00:05:19.442][info  ][EM] ??1 [E:29148i S:14009 M:240766573] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:38.120]  [00:05:19.442][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:38.772]  [00:05:20.098][info  ][EM] >>> [E:29148i S:14009 M:31549944 (Ack:240766573)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:38.828]  [00:05:20.159][info  ][EM] <<< [E:29148i S:14009 M:240766574 (Ack:31549944)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:38.828]  [00:05:20.159][info  ][EM] ??1 [E:29148i S:14009 M:240766574] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:39.530]  [00:05:20.864][info  ][EM] >>> [E:29148i S:14009 M:31549945 (Ack:240766574)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:39.589]  [00:05:20.924][info  ][EM] <<< [E:29148i S:14009 M:240766575 (Ack:31549945)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:39.589]  [00:05:20.925][info  ][EM] ??1 [E:29148i S:14009 M:240766575] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:40.477]  [00:05:21.809][info  ][EM] >>> [E:29148i S:14009 M:31549946 (Ack:240766575)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:40.538]  [00:05:21.870][info  ][EM] <<< [E:29148i S:14009 M:240766576 (Ack:31549946)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:40.538]  [00:05:21.870][info  ][EM] ??1 [E:29148i S:14009 M:240766576] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5691ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:41.281]  [00:05:22.616][info  ][EM] >>> [E:29148i S:14009 M:31549947 (Ack:240766576)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:41.413]  [00:05:22.750][info  ][EM] <<< [E:29148i S:14009 M:240766577 (Ack:31549947)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:41.424]  [00:05:22.750][info  ][EM] ??1 [E:29148i S:14009 M:240766577] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:41.424]  [00:05:22.750][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:08:42.183]  [00:05:23.520][info  ][EM] >>> [E:29148i S:14009 M:31549948 (Ack:240766577)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:42.252]  [00:05:23.580][info  ][EM] <<< [E:29148i S:14009 M:240766578 (Ack:31549948)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:42.252]  [00:05:23.581][info  ][EM] ??1 [E:29148i S:14009 M:240766578] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:43.189]  [00:05:24.526][info  ][EM] >>> [E:29148i S:14009 M:31549949 (Ack:240766578)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:43.251]  [00:05:24.586][info  ][EM] <<< [E:29148i S:14009 M:240766579 (Ack:31549949)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:43.251]  [00:05:24.587][info  ][EM] ??1 [E:29148i S:14009 M:240766579] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:44.221]  [00:05:25.550][info  ][EM] >>> [E:29148i S:14009 M:31549950 (Ack:240766579)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:44.287]  [00:05:25.611][info  ][EM] <<< [E:29148i S:14009 M:240766580 (Ack:31549950)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:44.287]  [00:05:25.611][info  ][EM] ??1 [E:29148i S:14009 M:240766580] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:45.314]  [00:05:26.646][info  ][EM] >>> [E:29148i S:14009 M:31549951 (Ack:240766580)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:45.446]  [00:05:26.780][info  ][EM] <<< [E:29148i S:14009 M:240766581 (Ack:31549951)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:45.446]  [00:05:26.780][info  ][EM] ??1 [E:29148i S:14009 M:240766581] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:45.457]  [00:05:26.781][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:46.475]  [00:05:27.809][info  ][EM] >>> [E:29148i S:14009 M:31549952 (Ack:240766581)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:46.534]  [00:05:27.869][info  ][EM] <<< [E:29148i S:14009 M:240766582 (Ack:31549952)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:46.534]  [00:05:27.870][info  ][EM] ??1 [E:29148i S:14009 M:240766582] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:47.374]  [00:05:28.704][info  ][EM] >>> [E:29148i S:14009 M:31549953 (Ack:240766582)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:47.433]  [00:05:28.764][info  ][EM] <<< [E:29148i S:14009 M:240766583 (Ack:31549953)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:47.433]  [00:05:28.765][info  ][EM] ??1 [E:29148i S:14009 M:240766583] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:48.340]  [00:05:29.674][info  ][EM] >>> [E:29148i S:14009 M:31549954 (Ack:240766583)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:48.408]  [00:05:29.735][info  ][EM] <<< [E:29148i S:14009 M:240766584 (Ack:31549954)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:48.408]  [00:05:29.735][info  ][EM] ??1 [E:29148i S:14009 M:240766584] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:49.131]  [00:05:30.467][info  ][EM] >>> [E:29148i S:14009 M:31549955 (Ack:240766584)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:49.275]  [00:05:30.601][info  ][EM] <<< [E:29148i S:14009 M:240766585 (Ack:31549955)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:49.275]  [00:05:30.602][info  ][EM] ??1 [E:29148i S:14009 M:240766585] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:49.275]  [00:05:30.602][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:08:49.934]  [00:05:31.271][info  ][EM] >>> [E:29148i S:14009 M:31549956 (Ack:240766585)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:49.995]  [00:05:31.332][info  ][EM] <<< [E:29148i S:14009 M:240766586 (Ack:31549956)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:50.007]  [00:05:31.332][info  ][EM] ??1 [E:29148i S:14009 M:240766586] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5549ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:50.708]  [00:05:32.044][info  ][EM] >>> [E:29148i S:14009 M:31549957 (Ack:240766586)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:50.769]  [00:05:32.105][info  ][EM] <<< [E:29148i S:14009 M:240766587 (Ack:31549957)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:50.781]  [00:05:32.106][info  ][EM] ??1 [E:29148i S:14009 M:240766587] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:51.585]  [00:05:32.920][info  ][EM] >>> [E:29148i S:14009 M:31549958 (Ack:240766587)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:51.651]  [00:05:32.981][info  ][EM] <<< [E:29148i S:14009 M:240766588 (Ack:31549958)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:51.651]  [00:05:32.982][info  ][EM] ??1 [E:29148i S:14009 M:240766588] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:52.625]  [00:05:33.948][info  ][EM] >>> [E:29148i S:14009 M:31549959 (Ack:240766588)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:52.747]  [00:05:34.082][info  ][EM] <<< [E:29148i S:14009 M:240766589 (Ack:31549959)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:52.747]  [00:05:34.083][info  ][EM] ??1 [E:29148i S:14009 M:240766589] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:52.760]  [00:05:34.083][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:53.376]  [00:05:34.713][info  ][EM] >>> [E:29148i S:14009 M:31549960 (Ack:240766589)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:53.447]  [00:05:34.773][info  ][EM] <<< [E:29148i S:14009 M:240766590 (Ack:31549960)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:53.447]  [00:05:34.774][info  ][EM] ??1 [E:29148i S:14009 M:240766590] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5525ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:54.475]  [00:05:35.810][info  ][EM] >>> [E:29148i S:14009 M:31549961 (Ack:240766590)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:54.536]  [00:05:35.871][info  ][EM] <<< [E:29148i S:14009 M:240766591 (Ack:31549961)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:54.536]  [00:05:35.872][info  ][EM] ??1 [E:29148i S:14009 M:240766591] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:55.483]  [00:05:36.815][info  ][EM] >>> [E:29148i S:14009 M:31549962 (Ack:240766591)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:55.548]  [00:05:36.875][info  ][EM] <<< [E:29148i S:14009 M:240766592 (Ack:31549962)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:55.548]  [00:05:36.876][info  ][EM] ??1 [E:29148i S:14009 M:240766592] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:56.586]  [00:05:37.916][info  ][EM] >>> [E:29148i S:14009 M:31549963 (Ack:240766592)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:56.719]  [00:05:38.050][info  ][EM] <<< [E:29148i S:14009 M:240766593 (Ack:31549963)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:56.719]  [00:05:38.051][info  ][EM] ??1 [E:29148i S:14009 M:240766593] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:56.732]  [00:05:38.051][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:08:57.549]  [00:05:38.885][info  ][EM] >>> [E:29148i S:14009 M:31549964 (Ack:240766593)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:57.611]  [00:05:38.946][info  ][EM] <<< [E:29148i S:14009 M:240766594 (Ack:31549964)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:57.611]  [00:05:38.947][info  ][EM] ??1 [E:29148i S:14009 M:240766594] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:58.350]  [00:05:39.677][info  ][EM] >>> [E:29148i S:14009 M:31549965 (Ack:240766594)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:58.401]  [00:05:39.738][info  ][EM] <<< [E:29148i S:14009 M:240766595 (Ack:31549965)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:58.401]  [00:05:39.738][info  ][EM] ??1 [E:29148i S:14009 M:240766595] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[19:08:59.112]  [00:05:40.436][info  ][EM] >>> [E:29148i S:14009 M:31549966 (Ack:240766595)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:08:59.171]  [00:05:40.496][info  ][EM] <<< [E:29148i S:14009 M:240766596 (Ack:31549966)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:08:59.171]  [00:05:40.497][info  ][EM] ??1 [E:29148i S:14009 M:240766596] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5284ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:00.037]  [00:05:41.369][info  ][EM] >>> [E:29148i S:14009 M:31549967 (Ack:240766596)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:00.171]  [00:05:41.502][info  ][EM] <<< [E:29148i S:14009 M:240766597 (Ack:31549967)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:00.171]  [00:05:41.503][info  ][EM] ??1 [E:29148i S:14009 M:240766597] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:00.187]  [00:05:41.504][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:01.752]  [00:05:43.089][info  ][EM] >>> [E:29148i S:14009 M:31549968 (Ack:240766597)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:01.815]  [00:05:43.150][info  ][EM] <<< [E:29148i S:14009 M:240766598 (Ack:31549968)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:01.815]  [00:05:43.151][info  ][EM] ??1 [E:29148i S:14009 M:240766598] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:02.776]  [00:05:44.106][info  ][EM] >>> [E:29148i S:14009 M:31549969 (Ack:240766598)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:02.838]  [00:05:44.166][info  ][EM] <<< [E:29148i S:14009 M:240766599 (Ack:31549969)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:02.838]  [00:05:44.167][info  ][EM] ??1 [E:29148i S:14009 M:240766599] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5473ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:03.776]  [00:05:45.105][info  ][EM] >>> [E:29148i S:14009 M:31549970 (Ack:240766599)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:03.837]  [00:05:45.165][info  ][EM] <<< [E:29148i S:14009 M:240766600 (Ack:31549970)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:03.837]  [00:05:45.166][info  ][EM] ??1 [E:29148i S:14009 M:240766600] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5540ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:04.746]  [00:05:46.074][info  ][EM] >>> [E:29148i S:14009 M:31549971 (Ack:240766600)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:04.876]  [00:05:46.208][info  ][EM] <<< [E:29148i S:14009 M:240766601 (Ack:31549971)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:04.876]  [00:05:46.208][info  ][EM] ??1 [E:29148i S:14009 M:240766601] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:04.876]  [00:05:46.208][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:05.647]  [00:05:46.975][info  ][EM] >>> [E:29148i S:14009 M:31549972 (Ack:240766601)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:05.711]  [00:05:47.036][info  ][EM] <<< [E:29148i S:14009 M:240766602 (Ack:31549972)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:05.711]  [00:05:47.037][info  ][EM] ??1 [E:29148i S:14009 M:240766602] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:06.411]  [00:05:47.746][info  ][EM] >>> [E:29148i S:14009 M:31549973 (Ack:240766602)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:06.480]  [00:05:47.806][info  ][EM] <<< [E:29148i S:14009 M:240766603 (Ack:31549973)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:06.480]  [00:05:47.806][info  ][EM] ??1 [E:29148i S:14009 M:240766603] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:07.431]  [00:05:48.764][info  ][EM] >>> [E:29148i S:14009 M:31549974 (Ack:240766603)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:07.492]  [00:05:48.825][info  ][EM] <<< [E:29148i S:14009 M:240766604 (Ack:31549974)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:07.492]  [00:05:48.826][info  ][EM] ??1 [E:29148i S:14009 M:240766604] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5435ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:08.420]  [00:05:49.751][info  ][EM] >>> [E:29148i S:14009 M:31549975 (Ack:240766604)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:08.548]  [00:05:49.885][info  ][EM] <<< [E:29148i S:14009 M:240766605 (Ack:31549975)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:08.548]  [00:05:49.885][info  ][EM] ??1 [E:29148i S:14009 M:240766605] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:08.559]  [00:05:49.886][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:09.338]  [00:05:50.674][info  ][EM] >>> [E:29148i S:14009 M:31549976 (Ack:240766605)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:09.398]  [00:05:50.734][info  ][EM] <<< [E:29148i S:14009 M:240766606 (Ack:31549976)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:09.398]  [00:05:50.735][info  ][EM] ??1 [E:29148i S:14009 M:240766606] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:10.171]  [00:05:51.499][info  ][EM] >>> [E:29148i S:14009 M:31549977 (Ack:240766606)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:10.232]  [00:05:51.559][info  ][EM] <<< [E:29148i S:14009 M:240766607 (Ack:31549977)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:10.232]  [00:05:51.560][info  ][EM] ??1 [E:29148i S:14009 M:240766607] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5484ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:10.974]  [00:05:52.303][info  ][EM] >>> [E:29148i S:14009 M:31549978 (Ack:240766607)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:11.036]  [00:05:52.364][info  ][EM] <<< [E:29148i S:14009 M:240766608 (Ack:31549978)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:11.036]  [00:05:52.365][info  ][EM] ??1 [E:29148i S:14009 M:240766608] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:12.110]  [00:05:53.442][info  ][EM] >>> [E:29148i S:14009 M:31549979 (Ack:240766608)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:12.239]  [00:05:53.576][info  ][EM] <<< [E:29148i S:14009 M:240766609 (Ack:31549979)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:12.239]  [00:05:53.577][info  ][EM] ??1 [E:29148i S:14009 M:240766609] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:12.251]  [00:05:53.577][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:12.882]  [00:05:54.217][info  ][EM] >>> [E:29148i S:14009 M:31549980 (Ack:240766609)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:12.942]  [00:05:54.278][info  ][EM] <<< [E:29148i S:14009 M:240766610 (Ack:31549980)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:12.942]  [00:05:54.278][info  ][EM] ??1 [E:29148i S:14009 M:240766610] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:14.297]  [00:05:55.626][info  ][EM] >>> [E:29148i S:14009 M:31549981 (Ack:240766610)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:14.357]  [00:05:55.687][info  ][EM] <<< [E:29148i S:14009 M:240766611 (Ack:31549981)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:14.357]  [00:05:55.688][info  ][EM] ??1 [E:29148i S:14009 M:240766611] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5643ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:15.380]  [00:05:56.714][info  ][EM] >>> [E:29148i S:14009 M:31549982 (Ack:240766611)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:15.441]  [00:05:56.775][info  ][EM] <<< [E:29148i S:14009 M:240766612 (Ack:31549982)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:15.441]  [00:05:56.776][info  ][EM] ??1 [E:29148i S:14009 M:240766612] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:16.176]  [00:05:57.503][info  ][EM] >>> [E:29148i S:14009 M:31549983 (Ack:240766612)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:16.299]  [00:05:57.637][info  ][EM] <<< [E:29148i S:14009 M:240766613 (Ack:31549983)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:16.311]  [00:05:57.638][info  ][EM] ??1 [E:29148i S:14009 M:240766613] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:16.311]  [00:05:57.639][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:17.067]  [00:05:58.404][info  ][EM] >>> [E:29148i S:14009 M:31549984 (Ack:240766613)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:17.131]  [00:05:58.463][info  ][EM] <<< [E:29148i S:14009 M:240766614 (Ack:31549984)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:17.131]  [00:05:58.464][info  ][EM] ??1 [E:29148i S:14009 M:240766614] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:18.055]  [00:05:59.392][info  ][EM] >>> [E:29148i S:14009 M:31549985 (Ack:240766614)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:18.121]  [00:05:59.452][info  ][EM] <<< [E:29148i S:14009 M:240766615 (Ack:31549985)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:18.121]  [00:05:59.453][info  ][EM] ??1 [E:29148i S:14009 M:240766615] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5538ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:18.963]  [00:06:00.299][info  ][EM] >>> [E:29148i S:14009 M:31549986 (Ack:240766615)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:19.024]  [00:06:00.360][info  ][EM] <<< [E:29148i S:14009 M:240766616 (Ack:31549986)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:19.024]  [00:06:00.361][info  ][EM] ??1 [E:29148i S:14009 M:240766616] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:20.058]  [00:06:01.394][info  ][EM] >>> [E:29148i S:14009 M:31549987 (Ack:240766616)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:20.198]  [00:06:01.528][info  ][EM] <<< [E:29148i S:14009 M:240766617 (Ack:31549987)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:20.198]  [00:06:01.528][info  ][EM] ??1 [E:29148i S:14009 M:240766617] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:20.198]  [00:06:01.529][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:20.965]  [00:06:02.300][info  ][EM] >>> [E:29148i S:14009 M:31549988 (Ack:240766617)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:21.026]  [00:06:02.361][info  ][EM] <<< [E:29148i S:14009 M:240766618 (Ack:31549988)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:21.026]  [00:06:02.362][info  ][EM] ??1 [E:29148i S:14009 M:240766618] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:21.897]  [00:06:03.230][info  ][EM] >>> [E:29148i S:14009 M:31549989 (Ack:240766618)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:21.963]  [00:06:03.290][info  ][EM] <<< [E:29148i S:14009 M:240766619 (Ack:31549989)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:21.963]  [00:06:03.291][info  ][EM] ??1 [E:29148i S:14009 M:240766619] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:22.660]  [00:06:03.991][info  ][EM] >>> [E:29148i S:14009 M:31549990 (Ack:240766619)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:22.714]  [00:06:04.051][info  ][EM] <<< [E:29148i S:14009 M:240766620 (Ack:31549990)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:22.714]  [00:06:04.052][info  ][EM] ??1 [E:29148i S:14009 M:240766620] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5355ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:23.649]  [00:06:04.980][info  ][EM] >>> [E:29148i S:14009 M:31549991 (Ack:240766620)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:23.776]  [00:06:05.114][info  ][EM] <<< [E:29148i S:14009 M:240766621 (Ack:31549991)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:23.787]  [00:06:05.114][info  ][EM] ??1 [E:29148i S:14009 M:240766621] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:23.787]  [00:06:05.115][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:24.570]  [00:06:05.899][info  ][EM] >>> [E:29148i S:14009 M:31549992 (Ack:240766621)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:24.627]  [00:06:05.959][info  ][EM] <<< [E:29148i S:14009 M:240766622 (Ack:31549992)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:24.627]  [00:06:05.960][info  ][EM] ??1 [E:29148i S:14009 M:240766622] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:25.399]  [00:06:06.731][info  ][EM] >>> [E:29148i S:14009 M:31549993 (Ack:240766622)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:25.455]  [00:06:06.791][info  ][EM] <<< [E:29148i S:14009 M:240766623 (Ack:31549993)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:25.455]  [00:06:06.791][info  ][EM] ??1 [E:29148i S:14009 M:240766623] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:26.310]  [00:06:07.639][info  ][EM] >>> [E:29148i S:14009 M:31549994 (Ack:240766623)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:26.369]  [00:06:07.700][info  ][EM] <<< [E:29148i S:14009 M:240766624 (Ack:31549994)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:26.369]  [00:06:07.701][info  ][EM] ??1 [E:29148i S:14009 M:240766624] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5736ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:27.321]  [00:06:08.654][info  ][EM] >>> [E:29148i S:14009 M:31549995 (Ack:240766624)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:27.461]  [00:06:08.788][info  ][EM] <<< [E:29148i S:14009 M:240766625 (Ack:31549995)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:27.461]  [00:06:08.789][info  ][EM] ??1 [E:29148i S:14009 M:240766625] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:27.461]  [00:06:08.790][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:28.082]  [00:06:09.418][info  ][EM] >>> [E:29148i S:14009 M:31549996 (Ack:240766625)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:28.149]  [00:06:09.479][info  ][EM] <<< [E:29148i S:14009 M:240766626 (Ack:31549996)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:28.149]  [00:06:09.479][info  ][EM] ??1 [E:29148i S:14009 M:240766626] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:29.314]  [00:06:10.640][info  ][EM] >>> [E:29148i S:14009 M:31549997 (Ack:240766626)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:29.365]  [00:06:10.701][info  ][EM] <<< [E:29148i S:14009 M:240766627 (Ack:31549997)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:29.365]  [00:06:10.702][info  ][EM] ??1 [E:29148i S:14009 M:240766627] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:30.125]  [00:06:11.460][info  ][EM] >>> [E:29148i S:14009 M:31549998 (Ack:240766627)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:30.182]  [00:06:11.521][info  ][EM] <<< [E:29148i S:14009 M:240766628 (Ack:31549998)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:30.193]  [00:06:11.522][info  ][EM] ??1 [E:29148i S:14009 M:240766628] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:30.936]  [00:06:12.267][info  ][EM] >>> [E:29148i S:14009 M:31549999 (Ack:240766628)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:31.077]  [00:06:12.401][info  ][EM] <<< [E:29148i S:14009 M:240766629 (Ack:31549999)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:31.077]  [00:06:12.402][info  ][EM] ??1 [E:29148i S:14009 M:240766629] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:31.077]  [00:06:12.402][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:32.029]  [00:06:13.369][info  ][EM] >>> [E:29148i S:14009 M:31550000 (Ack:240766629)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:32.100]  [00:06:13.429][info  ][EM] <<< [E:29148i S:14009 M:240766630 (Ack:31550000)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:32.100]  [00:06:13.429][info  ][EM] ??1 [E:29148i S:14009 M:240766630] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:32.785]  [00:06:14.124][info  ][EM] >>> [E:29148i S:14009 M:31550001 (Ack:240766630)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:32.848]  [00:06:14.184][info  ][EM] <<< [E:29148i S:14009 M:240766631 (Ack:31550001)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:32.848]  [00:06:14.185][info  ][EM] ??1 [E:29148i S:14009 M:240766631] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:33.578]  [00:06:14.913][info  ][EM] >>> [E:29148i S:14009 M:31550002 (Ack:240766631)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:33.639]  [00:06:14.973][info  ][EM] <<< [E:29148i S:14009 M:240766632 (Ack:31550002)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:33.639]  [00:06:14.974][info  ][EM] ??1 [E:29148i S:14009 M:240766632] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5314ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:34.340]  [00:06:15.669][info  ][EM] >>> [E:29148i S:14009 M:31550003 (Ack:240766632)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:34.470]  [00:06:15.803][info  ][EM] <<< [E:29148i S:14009 M:240766633 (Ack:31550003)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:34.470]  [00:06:15.804][info  ][EM] ??1 [E:29148i S:14009 M:240766633] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5583ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:34.470]  [00:06:15.805][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:35.111]  [00:06:16.447][info  ][EM] >>> [E:29148i S:14009 M:31550004 (Ack:240766633)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:35.172]  [00:06:16.507][info  ][EM] <<< [E:29148i S:14009 M:240766634 (Ack:31550004)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:35.172]  [00:06:16.507][info  ][EM] ??1 [E:29148i S:14009 M:240766634] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:35.912]  [00:06:17.245][info  ][EM] >>> [E:29148i S:14009 M:31550005 (Ack:240766634)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:35.980]  [00:06:17.304][info  ][EM] <<< [E:29148i S:14009 M:240766635 (Ack:31550005)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:35.980]  [00:06:17.305][info  ][EM] ??1 [E:29148i S:14009 M:240766635] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5430ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:36.736]  [00:06:18.065][info  ][EM] >>> [E:29148i S:14009 M:31550006 (Ack:240766635)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:36.791]  [00:06:18.125][info  ][EM] <<< [E:29148i S:14009 M:240766636 (Ack:31550006)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:36.791]  [00:06:18.126][info  ][EM] ??1 [E:29148i S:14009 M:240766636] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:37.754]  [00:06:19.089][info  ][EM] >>> [E:29148i S:14009 M:31550007 (Ack:240766636)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:37.888]  [00:06:19.223][info  ][EM] <<< [E:29148i S:14009 M:240766637 (Ack:31550007)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:37.888]  [00:06:19.224][info  ][EM] ??1 [E:29148i S:14009 M:240766637] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:37.899]  [00:06:19.224][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:38.580]  [00:06:19.910][info  ][EM] >>> [E:29148i S:14009 M:31550008 (Ack:240766637)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:38.630]  [00:06:19.969][info  ][EM] <<< [E:29148i S:14009 M:240766638 (Ack:31550008)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:38.644]  [00:06:19.970][info  ][EM] ??1 [E:29148i S:14009 M:240766638] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:39.359]  [00:06:20.687][info  ][EM] >>> [E:29148i S:14009 M:31550009 (Ack:240766638)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:39.410]  [00:06:20.748][info  ][EM] <<< [E:29148i S:14009 M:240766639 (Ack:31550009)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:39.410]  [00:06:20.749][info  ][EM] ??1 [E:29148i S:14009 M:240766639] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:40.241]  [00:06:21.581][info  ][EM] >>> [E:29148i S:14009 M:31550010 (Ack:240766639)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:40.304]  [00:06:21.641][info  ][EM] <<< [E:29148i S:14009 M:240766640 (Ack:31550010)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:40.304]  [00:06:21.641][info  ][EM] ??1 [E:29148i S:14009 M:240766640] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:41.029]  [00:06:22.361][info  ][EM] >>> [E:29148i S:14009 M:31550011 (Ack:240766640)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:41.161]  [00:06:22.495][info  ][EM] <<< [E:29148i S:14009 M:240766641 (Ack:31550011)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:41.161]  [00:06:22.496][info  ][EM] ??1 [E:29148i S:14009 M:240766641] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5295ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:41.161]  [00:06:22.496][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:09:42.305]  [00:06:23.636][info  ][EM] >>> [E:29148i S:14009 M:31550012 (Ack:240766641)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:42.362]  [00:06:23.697][info  ][EM] <<< [E:29148i S:14009 M:240766642 (Ack:31550012)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:42.362]  [00:06:23.697][info  ][EM] ??1 [E:29148i S:14009 M:240766642] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:43.202]  [00:06:24.537][info  ][EM] >>> [E:29148i S:14009 M:31550013 (Ack:240766642)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:43.264]  [00:06:24.597][info  ][EM] <<< [E:29148i S:14009 M:240766643 (Ack:31550013)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:43.264]  [00:06:24.598][info  ][EM] ??1 [E:29148i S:14009 M:240766643] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5415ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:44.328]  [00:06:25.666][info  ][EM] >>> [E:29148i S:14009 M:31550014 (Ack:240766643)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:44.399]  [00:06:25.726][info  ][EM] <<< [E:29148i S:14009 M:240766644 (Ack:31550014)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:44.399]  [00:06:25.727][info  ][EM] ??1 [E:29148i S:14009 M:240766644] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:45.117]  [00:06:26.451][info  ][EM] >>> [E:29148i S:14009 M:31550015 (Ack:240766644)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:45.245]  [00:06:26.584][info  ][EM] <<< [E:29148i S:14009 M:240766645 (Ack:31550015)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:45.257]  [00:06:26.584][info  ][EM] ??1 [E:29148i S:14009 M:240766645] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5220ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:45.257]  [00:06:26.585][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:46.275]  [00:06:27.615][info  ][EM] >>> [E:29148i S:14009 M:31550016 (Ack:240766645)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:46.338]  [00:06:27.675][info  ][EM] <<< [E:29148i S:14009 M:240766646 (Ack:31550016)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:46.338]  [00:06:27.676][info  ][EM] ??1 [E:29148i S:14009 M:240766646] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:47.046]  [00:06:28.386][info  ][EM] >>> [E:29148i S:14009 M:31550017 (Ack:240766646)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:47.106]  [00:06:28.446][info  ][EM] <<< [E:29148i S:14009 M:240766647 (Ack:31550017)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:47.120]  [00:06:28.447][info  ][EM] ??1 [E:29148i S:14009 M:240766647] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:48.345]  [00:06:29.676][info  ][EM] >>> [E:29148i S:14009 M:31550018 (Ack:240766647)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:48.399]  [00:06:29.736][info  ][EM] <<< [E:29148i S:14009 M:240766648 (Ack:31550018)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:48.399]  [00:06:29.737][info  ][EM] ??1 [E:29148i S:14009 M:240766648] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:49.249]  [00:06:30.578][info  ][EM] >>> [E:29148i S:14009 M:31550019 (Ack:240766648)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:49.382]  [00:06:30.711][info  ][EM] <<< [E:29148i S:14009 M:240766649 (Ack:31550019)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:49.382]  [00:06:30.712][info  ][EM] ??1 [E:29148i S:14009 M:240766649] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:49.382]  [00:06:30.713][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:49.997]  [00:06:31.337][info  ][EM] >>> [E:29148i S:14009 M:31550020 (Ack:240766649)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:50.058]  [00:06:31.398][info  ][EM] <<< [E:29148i S:14009 M:240766650 (Ack:31550020)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:50.070]  [00:06:31.398][info  ][EM] ??1 [E:29148i S:14009 M:240766650] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:50.919]  [00:06:32.253][info  ][EM] >>> [E:29148i S:14009 M:31550021 (Ack:240766650)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:50.989]  [00:06:32.314][info  ][EM] <<< [E:29148i S:14009 M:240766651 (Ack:31550021)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:50.989]  [00:06:32.315][info  ][EM] ??1 [E:29148i S:14009 M:240766651] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:51.805]  [00:06:33.142][info  ][EM] >>> [E:29148i S:14009 M:31550022 (Ack:240766651)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:51.864]  [00:06:33.202][info  ][EM] <<< [E:29148i S:14009 M:240766652 (Ack:31550022)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:51.864]  [00:06:33.203][info  ][EM] ??1 [E:29148i S:14009 M:240766652] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:52.705]  [00:06:34.036][info  ][EM] >>> [E:29148i S:14009 M:31550023 (Ack:240766652)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:52.839]  [00:06:34.169][info  ][EM] <<< [E:29148i S:14009 M:240766653 (Ack:31550023)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:52.839]  [00:06:34.170][info  ][EM] ??1 [E:29148i S:14009 M:240766653] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5598ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:52.839]  [00:06:34.170][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:09:53.519]  [00:06:34.858][info  ][EM] >>> [E:29148i S:14009 M:31550024 (Ack:240766653)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:53.582]  [00:06:34.918][info  ][EM] <<< [E:29148i S:14009 M:240766654 (Ack:31550024)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:53.582]  [00:06:34.919][info  ][EM] ??1 [E:29148i S:14009 M:240766654] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:54.509]  [00:06:35.840][info  ][EM] >>> [E:29148i S:14009 M:31550025 (Ack:240766654)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:54.569]  [00:06:35.901][info  ][EM] <<< [E:29148i S:14009 M:240766655 (Ack:31550025)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:54.569]  [00:06:35.902][info  ][EM] ??1 [E:29148i S:14009 M:240766655] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:55.673]  [00:06:37.008][info  ][EM] >>> [E:29148i S:14009 M:31550026 (Ack:240766655)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:55.734]  [00:06:37.069][info  ][EM] <<< [E:29148i S:14009 M:240766656 (Ack:31550026)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:55.734]  [00:06:37.070][info  ][EM] ??1 [E:29148i S:14009 M:240766656] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:56.497]  [00:06:37.832][info  ][EM] >>> [E:29148i S:14009 M:31550027 (Ack:240766656)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:56.627]  [00:06:37.965][info  ][EM] <<< [E:29148i S:14009 M:240766657 (Ack:31550027)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:56.627]  [00:06:37.965][info  ][EM] ??1 [E:29148i S:14009 M:240766657] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:56.638]  [00:06:37.966][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:09:58.183]  [00:06:39.522][info  ][EM] >>> [E:29148i S:14009 M:31550028 (Ack:240766657)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:58.252]  [00:06:39.583][info  ][EM] <<< [E:29148i S:14009 M:240766658 (Ack:31550028)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:58.252]  [00:06:39.583][info  ][EM] ??1 [E:29148i S:14009 M:240766658] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:58.988]  [00:06:40.328][info  ][EM] >>> [E:29148i S:14009 M:31550029 (Ack:240766658)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:59.049]  [00:06:40.387][info  ][EM] <<< [E:29148i S:14009 M:240766659 (Ack:31550029)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:59.049]  [00:06:40.388][info  ][EM] ??1 [E:29148i S:14009 M:240766659] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[19:09:59.908]  [00:06:41.241][info  ][EM] >>> [E:29148i S:14009 M:31550030 (Ack:240766659)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:09:59.961]  [00:06:41.301][info  ][EM] <<< [E:29148i S:14009 M:240766660 (Ack:31550030)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:09:59.974]  [00:06:41.302][info  ][EM] ??1 [E:29148i S:14009 M:240766660] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:00.838]  [00:06:42.168][info  ][EM] >>> [E:29148i S:14009 M:31550031 (Ack:240766660)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:00.971]  [00:06:42.302][info  ][EM] <<< [E:29148i S:14009 M:240766661 (Ack:31550031)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:00.971]  [00:06:42.303][info  ][EM] ??1 [E:29148i S:14009 M:240766661] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:00.971]  [00:06:42.303][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:10:01.618]  [00:06:42.948][info  ][EM] >>> [E:29148i S:14009 M:31550032 (Ack:240766661)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:01.668]  [00:06:43.008][info  ][EM] <<< [E:29148i S:14009 M:240766662 (Ack:31550032)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:01.680]  [00:06:43.008][info  ][EM] ??1 [E:29148i S:14009 M:240766662] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:02.366]  [00:06:43.696][info  ][EM] >>> [E:29148i S:14009 M:31550033 (Ack:240766662)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:02.426]  [00:06:43.756][info  ][EM] <<< [E:29148i S:14009 M:240766663 (Ack:31550033)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:02.426]  [00:06:43.757][info  ][EM] ??1 [E:29148i S:14009 M:240766663] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:03.225]  [00:06:44.565][info  ][EM] >>> [E:29148i S:14009 M:31550034 (Ack:240766663)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:03.287]  [00:06:44.625][info  ][EM] <<< [E:29148i S:14009 M:240766664 (Ack:31550034)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:03.287]  [00:06:44.626][info  ][EM] ??1 [E:29148i S:14009 M:240766664] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5252ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:04.015]  [00:06:45.347][info  ][EM] >>> [E:29148i S:14009 M:31550035 (Ack:240766664)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:04.148]  [00:06:45.481][info  ][EM] <<< [E:29148i S:14009 M:240766665 (Ack:31550035)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:04.148]  [00:06:45.482][info  ][EM] ??1 [E:29148i S:14009 M:240766665] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5583ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:04.148]  [00:06:45.482][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:10:04.992]  [00:06:46.333][info  ][EM] >>> [E:29148i S:14009 M:31550036 (Ack:240766665)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:05.055]  [00:06:46.393][info  ][EM] <<< [E:29148i S:14009 M:240766666 (Ack:31550036)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:05.055]  [00:06:46.393][info  ][EM] ??1 [E:29148i S:14009 M:240766666] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:05.903]  [00:06:47.241][info  ][EM] >>> [E:29148i S:14009 M:31550037 (Ack:240766666)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:05.965]  [00:06:47.301][info  ][EM] <<< [E:29148i S:14009 M:240766667 (Ack:31550037)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:05.965]  [00:06:47.301][info  ][EM] ??1 [E:29148i S:14009 M:240766667] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:06.783]  [00:06:48.116][info  ][EM] >>> [E:29148i S:14009 M:31550038 (Ack:240766667)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:06.845]  [00:06:48.176][info  ][EM] <<< [E:29148i S:14009 M:240766668 (Ack:31550038)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:06.845]  [00:06:48.177][info  ][EM] ??1 [E:29148i S:14009 M:240766668] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5443ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:07.659]  [00:06:48.991][info  ][EM] >>> [E:29148i S:14009 M:31550039 (Ack:240766668)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:07.797]  [00:06:49.125][info  ][EM] <<< [E:29148i S:14009 M:240766669 (Ack:31550039)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:07.797]  [00:06:49.125][info  ][EM] ??1 [E:29148i S:14009 M:240766669] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:07.797]  [00:06:49.125][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:08.443]  [00:06:49.773][info  ][EM] >>> [E:29148i S:14009 M:31550040 (Ack:240766669)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:08.496]  [00:06:49.833][info  ][EM] <<< [E:29148i S:14009 M:240766670 (Ack:31550040)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:08.496]  [00:06:49.834][info  ][EM] ??1 [E:29148i S:14009 M:240766670] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:09.333]  [00:06:50.673][info  ][EM] >>> [E:29148i S:14009 M:31550041 (Ack:240766670)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:09.400]  [00:06:50.734][info  ][EM] <<< [E:29148i S:14009 M:240766671 (Ack:31550041)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:09.400]  [00:06:50.735][info  ][EM] ??1 [E:29148i S:14009 M:240766671] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:10.358]  [00:06:51.690][info  ][EM] >>> [E:29148i S:14009 M:31550042 (Ack:240766671)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:10.423]  [00:06:51.750][info  ][EM] <<< [E:29148i S:14009 M:240766672 (Ack:31550042)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:10.423]  [00:06:51.751][info  ][EM] ??1 [E:29148i S:14009 M:240766672] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:11.405]  [00:06:52.742][info  ][EM] >>> [E:29148i S:14009 M:31550043 (Ack:240766672)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:11.535]  [00:06:52.875][info  ][EM] <<< [E:29148i S:14009 M:240766673 (Ack:31550043)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:11.547]  [00:06:52.876][info  ][EM] ??1 [E:29148i S:14009 M:240766673] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5248ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:11.547]  [00:06:52.876][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:12.187]  [00:06:53.519][info  ][EM] >>> [E:29148i S:14009 M:31550044 (Ack:240766673)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:12.243]  [00:06:53.580][info  ][EM] <<< [E:29148i S:14009 M:240766674 (Ack:31550044)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:12.243]  [00:06:53.581][info  ][EM] ??1 [E:29148i S:14009 M:240766674] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:13.218]  [00:06:54.550][info  ][EM] >>> [E:29148i S:14009 M:31550045 (Ack:240766674)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:13.277]  [00:06:54.611][info  ][EM] <<< [E:29148i S:14009 M:240766675 (Ack:31550045)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:13.277]  [00:06:54.611][info  ][EM] ??1 [E:29148i S:14009 M:240766675] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:14.003]  [00:06:55.334][info  ][EM] >>> [E:29148i S:14009 M:31550046 (Ack:240766675)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:14.061]  [00:06:55.395][info  ][EM] <<< [E:29148i S:14009 M:240766676 (Ack:31550046)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:14.061]  [00:06:55.396][info  ][EM] ??1 [E:29148i S:14009 M:240766676] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:14.794]  [00:06:56.120][info  ][EM] >>> [E:29148i S:14009 M:31550047 (Ack:240766676)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:14.921]  [00:06:56.253][info  ][EM] <<< [E:29148i S:14009 M:240766677 (Ack:31550047)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:14.921]  [00:06:56.254][info  ][EM] ??1 [E:29148i S:14009 M:240766677] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:14.921]  [00:06:56.254][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:15.955]  [00:06:57.285][info  ][EM] >>> [E:29148i S:14009 M:31550048 (Ack:240766677)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:16.005]  [00:06:57.345][info  ][EM] <<< [E:29148i S:14009 M:240766678 (Ack:31550048)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:16.018]  [00:06:57.346][info  ][EM] ??1 [E:29148i S:14009 M:240766678] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:16.732]  [00:06:58.068][info  ][EM] >>> [E:29148i S:14009 M:31550049 (Ack:240766678)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:16.796]  [00:06:58.128][info  ][EM] <<< [E:29148i S:14009 M:240766679 (Ack:31550049)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:16.796]  [00:06:58.129][info  ][EM] ??1 [E:29148i S:14009 M:240766679] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:17.517]  [00:06:58.854][info  ][EM] >>> [E:29148i S:14009 M:31550050 (Ack:240766679)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:17.577]  [00:06:58.915][info  ][EM] <<< [E:29148i S:14009 M:240766680 (Ack:31550050)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:17.577]  [00:06:58.915][info  ][EM] ??1 [E:29148i S:14009 M:240766680] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:18.339]  [00:06:59.672][info  ][EM] >>> [E:29148i S:14009 M:31550051 (Ack:240766680)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:18.469]  [00:06:59.808][info  ][EM] <<< [E:29148i S:14009 M:240766681 (Ack:31550051)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:18.469]  [00:06:59.809][info  ][EM] ??1 [E:29148i S:14009 M:240766681] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:18.482]  [00:06:59.810][error ][DL] Long dispatch time: 137 ms, for event type 2
[19:10:19.142]  [00:07:00.479][info  ][EM] >>> [E:29148i S:14009 M:31550052 (Ack:240766681)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:19.200]  [00:07:00.540][info  ][EM] <<< [E:29148i S:14009 M:240766682 (Ack:31550052)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:19.200]  [00:07:00.541][info  ][EM] ??1 [E:29148i S:14009 M:240766682] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:20.153]  [00:07:01.491][info  ][EM] >>> [E:29148i S:14009 M:31550053 (Ack:240766682)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:20.211]  [00:07:01.551][info  ][EM] <<< [E:29148i S:14009 M:240766683 (Ack:31550053)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:20.222]  [00:07:01.552][info  ][EM] ??1 [E:29148i S:14009 M:240766683] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:20.907]  [00:07:02.242][info  ][EM] >>> [E:29148i S:14009 M:31550054 (Ack:240766683)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:20.976]  [00:07:02.301][info  ][EM] <<< [E:29148i S:14009 M:240766684 (Ack:31550054)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:20.976]  [00:07:02.302][info  ][EM] ??1 [E:29148i S:14009 M:240766684] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:21.915]  [00:07:03.244][info  ][EM] >>> [E:29148i S:14009 M:31550055 (Ack:240766684)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:22.047]  [00:07:03.377][info  ][EM] <<< [E:29148i S:14009 M:240766685 (Ack:31550055)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:22.047]  [00:07:03.378][info  ][EM] ??1 [E:29148i S:14009 M:240766685] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:22.047]  [00:07:03.378][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:23.028]  [00:07:04.366][info  ][EM] >>> [E:29148i S:14009 M:31550056 (Ack:240766685)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:23.089]  [00:07:04.426][info  ][EM] <<< [E:29148i S:14009 M:240766686 (Ack:31550056)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:23.089]  [00:07:04.427][info  ][EM] ??1 [E:29148i S:14009 M:240766686] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:24.083]  [00:07:05.414][info  ][EM] >>> [E:29148i S:14009 M:31550057 (Ack:240766686)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:24.143]  [00:07:05.473][info  ][EM] <<< [E:29148i S:14009 M:240766687 (Ack:31550057)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:24.143]  [00:07:05.474][info  ][EM] ??1 [E:29148i S:14009 M:240766687] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:25.395]  [00:07:06.727][info  ][EM] >>> [E:29148i S:14009 M:31550058 (Ack:240766687)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:25.458]  [00:07:06.788][info  ][EM] <<< [E:29148i S:14009 M:240766688 (Ack:31550058)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:25.458]  [00:07:06.789][info  ][EM] ??1 [E:29148i S:14009 M:240766688] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5654ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:26.207]  [00:07:07.544][info  ][EM] >>> [E:29148i S:14009 M:31550059 (Ack:240766688)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:26.347]  [00:07:07.678][info  ][EM] <<< [E:29148i S:14009 M:240766689 (Ack:31550059)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:26.347]  [00:07:07.679][info  ][EM] ??1 [E:29148i S:14009 M:240766689] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:26.347]  [00:07:07.679][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:10:27.148]  [00:07:08.481][info  ][EM] >>> [E:29148i S:14009 M:31550060 (Ack:240766689)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:27.201]  [00:07:08.541][info  ][EM] <<< [E:29148i S:14009 M:240766690 (Ack:31550060)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:27.213]  [00:07:08.542][info  ][EM] ??1 [E:29148i S:14009 M:240766690] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:27.911]  [00:07:09.252][info  ][EM] >>> [E:29148i S:14009 M:31550061 (Ack:240766690)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:27.976]  [00:07:09.312][info  ][EM] <<< [E:29148i S:14009 M:240766691 (Ack:31550061)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:27.976]  [00:07:09.313][info  ][EM] ??1 [E:29148i S:14009 M:240766691] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:28.814]  [00:07:10.146][info  ][EM] >>> [E:29148i S:14009 M:31550062 (Ack:240766691)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:28.875]  [00:07:10.207][info  ][EM] <<< [E:29148i S:14009 M:240766692 (Ack:31550062)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:28.875]  [00:07:10.208][info  ][EM] ??1 [E:29148i S:14009 M:240766692] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5435ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:29.811]  [00:07:11.150][info  ][EM] >>> [E:29148i S:14009 M:31550063 (Ack:240766692)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:29.955]  [00:07:11.286][info  ][EM] <<< [E:29148i S:14009 M:240766693 (Ack:31550063)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:29.955]  [00:07:11.287][info  ][EM] ??1 [E:29148i S:14009 M:240766693] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5585ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:29.955]  [00:07:11.288][error ][DL] Long dispatch time: 137 ms, for event type 2
[19:10:30.617]  [00:07:11.952][info  ][EM] >>> [E:29148i S:14009 M:31550064 (Ack:240766693)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:30.678]  [00:07:12.012][info  ][EM] <<< [E:29148i S:14009 M:240766694 (Ack:31550064)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:30.678]  [00:07:12.013][info  ][EM] ??1 [E:29148i S:14009 M:240766694] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:31.475]  [00:07:12.814][info  ][EM] >>> [E:29148i S:14009 M:31550065 (Ack:240766694)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:31.534]  [00:07:12.874][info  ][EM] <<< [E:29148i S:14009 M:240766695 (Ack:31550065)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:31.545]  [00:07:12.875][info  ][EM] ??1 [E:29148i S:14009 M:240766695] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5375ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:32.257]  [00:07:13.593][info  ][EM] >>> [E:29148i S:14009 M:31550066 (Ack:240766695)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:32.329]  [00:07:13.654][info  ][EM] <<< [E:29148i S:14009 M:240766696 (Ack:31550066)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:32.329]  [00:07:13.655][info  ][EM] ??1 [E:29148i S:14009 M:240766696] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:33.047]  [00:07:14.387][info  ][EM] >>> [E:29148i S:14009 M:31550067 (Ack:240766696)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:33.190]  [00:07:14.518][info  ][EM] <<< [E:29148i S:14009 M:240766697 (Ack:31550067)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:33.190]  [00:07:14.519][info  ][EM] ??1 [E:29148i S:14009 M:240766697] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:33.190]  [00:07:14.520][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:34.327]  [00:07:15.660][info  ][EM] >>> [E:29148i S:14009 M:31550068 (Ack:240766697)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:34.387]  [00:07:15.720][info  ][EM] <<< [E:29148i S:14009 M:240766698 (Ack:31550068)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:34.387]  [00:07:15.721][info  ][EM] ??1 [E:29148i S:14009 M:240766698] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5478ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:35.116]  [00:07:16.453][info  ][EM] >>> [E:29148i S:14009 M:31550069 (Ack:240766698)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:35.182]  [00:07:16.513][info  ][EM] <<< [E:29148i S:14009 M:240766699 (Ack:31550069)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:35.182]  [00:07:16.514][info  ][EM] ??1 [E:29148i S:14009 M:240766699] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:36.133]  [00:07:17.474][info  ][EM] >>> [E:29148i S:14009 M:31550070 (Ack:240766699)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:36.195]  [00:07:17.534][info  ][EM] <<< [E:29148i S:14009 M:240766700 (Ack:31550070)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:36.195]  [00:07:17.535][info  ][EM] ??1 [E:29148i S:14009 M:240766700] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:36.904]  [00:07:18.240][info  ][EM] >>> [E:29148i S:14009 M:31550071 (Ack:240766700)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:37.039]  [00:07:18.374][info  ][EM] <<< [E:29148i S:14009 M:240766701 (Ack:31550071)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:37.039]  [00:07:18.375][info  ][EM] ??1 [E:29148i S:14009 M:240766701] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:37.053]  [00:07:18.375][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:10:37.803]  [00:07:19.143][info  ][EM] >>> [E:29148i S:14009 M:31550072 (Ack:240766701)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:37.873]  [00:07:19.204][info  ][EM] <<< [E:29148i S:14009 M:240766702 (Ack:31550072)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:37.873]  [00:07:19.205][info  ][EM] ??1 [E:29148i S:14009 M:240766702] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:38.668]  [00:07:19.998][info  ][EM] >>> [E:29148i S:14009 M:31550073 (Ack:240766702)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:38.727]  [00:07:20.058][info  ][EM] <<< [E:29148i S:14009 M:240766703 (Ack:31550073)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:38.727]  [00:07:20.059][info  ][EM] ??1 [E:29148i S:14009 M:240766703] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:39.530]  [00:07:20.863][info  ][EM] >>> [E:29148i S:14009 M:31550074 (Ack:240766703)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:39.581]  [00:07:20.923][info  ][EM] <<< [E:29148i S:14009 M:240766704 (Ack:31550074)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:39.598]  [00:07:20.924][info  ][EM] ??1 [E:29148i S:14009 M:240766704] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:40.431]  [00:07:21.757][info  ][EM] >>> [E:29148i S:14009 M:31550075 (Ack:240766704)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:40.552]  [00:07:21.891][info  ][EM] <<< [E:29148i S:14009 M:240766705 (Ack:31550075)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:40.552]  [00:07:21.892][info  ][EM] ??1 [E:29148i S:14009 M:240766705] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:40.563]  [00:07:21.892][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:10:41.311]  [00:07:22.641][info  ][EM] >>> [E:29148i S:14009 M:31550076 (Ack:240766705)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:41.370]  [00:07:22.702][info  ][EM] <<< [E:29148i S:14009 M:240766706 (Ack:31550076)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:41.370]  [00:07:22.703][info  ][EM] ??1 [E:29148i S:14009 M:240766706] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:42.186]  [00:07:23.519][info  ][EM] >>> [E:29148i S:14009 M:31550077 (Ack:240766706)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:42.247]  [00:07:23.580][info  ][EM] <<< [E:29148i S:14009 M:240766707 (Ack:31550077)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:42.247]  [00:07:23.581][info  ][EM] ??1 [E:29148i S:14009 M:240766707] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:43.290]  [00:07:24.622][info  ][EM] >>> [E:29148i S:14009 M:31550078 (Ack:240766707)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:43.341]  [00:07:24.682][info  ][EM] <<< [E:29148i S:14009 M:240766708 (Ack:31550078)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:43.353]  [00:07:24.683][info  ][EM] ??1 [E:29148i S:14009 M:240766708] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5562ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:44.128]  [00:07:25.467][info  ][EM] >>> [E:29148i S:14009 M:31550079 (Ack:240766708)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:44.260]  [00:07:25.601][info  ][EM] <<< [E:29148i S:14009 M:240766709 (Ack:31550079)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:44.271]  [00:07:25.602][info  ][EM] ??1 [E:29148i S:14009 M:240766709] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:44.271]  [00:07:25.602][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:10:45.389]  [00:07:26.723][info  ][EM] >>> [E:29148i S:14009 M:31550080 (Ack:240766709)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:45.454]  [00:07:26.784][info  ][EM] <<< [E:29148i S:14009 M:240766710 (Ack:31550080)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:45.454]  [00:07:26.785][info  ][EM] ??1 [E:29148i S:14009 M:240766710] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5484ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:46.146]  [00:07:27.480][info  ][EM] >>> [E:29148i S:14009 M:31550081 (Ack:240766710)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:46.202]  [00:07:27.540][info  ][EM] <<< [E:29148i S:14009 M:240766711 (Ack:31550081)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:46.202]  [00:07:27.541][info  ][EM] ??1 [E:29148i S:14009 M:240766711] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:47.041]  [00:07:28.376][info  ][EM] >>> [E:29148i S:14009 M:31550082 (Ack:240766711)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:47.101]  [00:07:28.436][info  ][EM] <<< [E:29148i S:14009 M:240766712 (Ack:31550082)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:47.101]  [00:07:28.437][info  ][EM] ??1 [E:29148i S:14009 M:240766712] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5716ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:47.836]  [00:07:29.168][info  ][EM] >>> [E:29148i S:14009 M:31550083 (Ack:240766712)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:47.967]  [00:07:29.304][info  ][EM] <<< [E:29148i S:14009 M:240766713 (Ack:31550083)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:47.967]  [00:07:29.305][info  ][EM] ??1 [E:29148i S:14009 M:240766713] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5699ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:47.978]  [00:07:29.305][error ][DL] Long dispatch time: 137 ms, for event type 2
[19:10:48.841]  [00:07:30.177][info  ][EM] >>> [E:29148i S:14009 M:31550084 (Ack:240766713)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:48.896]  [00:07:30.238][info  ][EM] <<< [E:29148i S:14009 M:240766714 (Ack:31550084)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:48.914]  [00:07:30.238][info  ][EM] ??1 [E:29148i S:14009 M:240766714] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:49.729]  [00:07:31.068][info  ][EM] >>> [E:29148i S:14009 M:31550085 (Ack:240766714)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:49.790]  [00:07:31.127][info  ][EM] <<< [E:29148i S:14009 M:240766715 (Ack:31550085)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:49.790]  [00:07:31.128][info  ][EM] ??1 [E:29148i S:14009 M:240766715] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:50.827]  [00:07:32.160][info  ][EM] >>> [E:29148i S:14009 M:31550086 (Ack:240766715)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:50.880]  [00:07:32.220][info  ][EM] <<< [E:29148i S:14009 M:240766716 (Ack:31550086)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:50.880]  [00:07:32.221][info  ][EM] ??1 [E:29148i S:14009 M:240766716] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:51.701]  [00:07:33.042][info  ][EM] >>> [E:29148i S:14009 M:31550087 (Ack:240766716)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:51.835]  [00:07:33.176][info  ][EM] <<< [E:29148i S:14009 M:240766717 (Ack:31550087)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:51.846]  [00:07:33.177][info  ][EM] ??1 [E:29148i S:14009 M:240766717] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:51.846]  [00:07:33.177][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:10:52.983]  [00:07:34.315][info  ][EM] >>> [E:29148i S:14009 M:31550088 (Ack:240766717)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:53.040]  [00:07:34.375][info  ][EM] <<< [E:29148i S:14009 M:240766718 (Ack:31550088)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:53.040]  [00:07:34.376][info  ][EM] ??1 [E:29148i S:14009 M:240766718] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:53.905]  [00:07:35.235][info  ][EM] >>> [E:29148i S:14009 M:31550089 (Ack:240766718)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:53.954]  [00:07:35.295][info  ][EM] <<< [E:29148i S:14009 M:240766719 (Ack:31550089)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:53.966]  [00:07:35.295][info  ][EM] ??1 [E:29148i S:14009 M:240766719] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:54.700]  [00:07:36.039][info  ][EM] >>> [E:29148i S:14009 M:31550090 (Ack:240766719)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:54.757]  [00:07:36.098][info  ][EM] <<< [E:29148i S:14009 M:240766720 (Ack:31550090)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:54.768]  [00:07:36.099][info  ][EM] ??1 [E:29148i S:14009 M:240766720] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5252ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:55.603]  [00:07:36.937][info  ][EM] >>> [E:29148i S:14009 M:31550091 (Ack:240766720)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:55.728]  [00:07:37.069][info  ][EM] <<< [E:29148i S:14009 M:240766721 (Ack:31550091)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:55.742]  [00:07:37.070][info  ][EM] ??1 [E:29148i S:14009 M:240766721] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:55.742]  [00:07:37.070][error ][DL] Long dispatch time: 132 ms, for event type 2
[19:10:56.505]  [00:07:37.835][info  ][EM] >>> [E:29148i S:14009 M:31550092 (Ack:240766721)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:56.560]  [00:07:37.896][info  ][EM] <<< [E:29148i S:14009 M:240766722 (Ack:31550092)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:56.560]  [00:07:37.897][info  ][EM] ??1 [E:29148i S:14009 M:240766722] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:57.269]  [00:07:38.610][info  ][EM] >>> [E:29148i S:14009 M:31550093 (Ack:240766722)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:57.337]  [00:07:38.670][info  ][EM] <<< [E:29148i S:14009 M:240766723 (Ack:31550093)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:57.337]  [00:07:38.671][info  ][EM] ??1 [E:29148i S:14009 M:240766723] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:58.174]  [00:07:39.509][info  ][EM] >>> [E:29148i S:14009 M:31550094 (Ack:240766723)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:58.235]  [00:07:39.570][info  ][EM] <<< [E:29148i S:14009 M:240766724 (Ack:31550094)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:58.235]  [00:07:39.570][info  ][EM] ??1 [E:29148i S:14009 M:240766724] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:58.911]  [00:07:40.246][info  ][EM] >>> [E:29148i S:14009 M:31550095 (Ack:240766724)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:59.045]  [00:07:40.379][info  ][EM] <<< [E:29148i S:14009 M:240766725 (Ack:31550095)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:59.045]  [00:07:40.380][info  ][EM] ??1 [E:29148i S:14009 M:240766725] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[19:10:59.045]  [00:07:40.380][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:10:59.694]  [00:07:41.035][info  ][EM] >>> [E:29148i S:14009 M:31550096 (Ack:240766725)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:10:59.761]  [00:07:41.095][info  ][EM] <<< [E:29148i S:14009 M:240766726 (Ack:31550096)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:10:59.761]  [00:07:41.096][info  ][EM] ??1 [E:29148i S:14009 M:240766726] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:00.654]  [00:07:41.994][info  ][EM] >>> [E:29148i S:14009 M:31550097 (Ack:240766726)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:00.724]  [00:07:42.054][info  ][EM] <<< [E:29148i S:14009 M:240766727 (Ack:31550097)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:00.724]  [00:07:42.055][info  ][EM] ??1 [E:29148i S:14009 M:240766727] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:01.447]  [00:07:42.789][info  ][EM] >>> [E:29148i S:14009 M:31550098 (Ack:240766727)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:01.512]  [00:07:42.849][info  ][EM] <<< [E:29148i S:14009 M:240766728 (Ack:31550098)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:01.512]  [00:07:42.849][info  ][EM] ??1 [E:29148i S:14009 M:240766728] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:02.257]  [00:07:43.594][info  ][EM] >>> [E:29148i S:14009 M:31550099 (Ack:240766728)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:02.393]  [00:07:43.728][info  ][EM] <<< [E:29148i S:14009 M:240766729 (Ack:31550099)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:02.393]  [00:07:43.729][info  ][EM] ??1 [E:29148i S:14009 M:240766729] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:02.404]  [00:07:43.729][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:04.412]  [00:07:45.748][info  ][EM] >>> [E:29148i S:14009 M:31550100 (Ack:240766729)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:04.467]  [00:07:45.808][info  ][EM] <<< [E:29148i S:14009 M:240766730 (Ack:31550100)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:04.478]  [00:07:45.809][info  ][EM] ??1 [E:29148i S:14009 M:240766730] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:05.205]  [00:07:46.539][info  ][EM] >>> [E:29148i S:14009 M:31550101 (Ack:240766730)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:05.258]  [00:07:46.599][info  ][EM] <<< [E:29148i S:14009 M:240766731 (Ack:31550101)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:05.270]  [00:07:46.600][info  ][EM] ??1 [E:29148i S:14009 M:240766731] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:06.115]  [00:07:47.447][info  ][EM] >>> [E:29148i S:14009 M:31550102 (Ack:240766731)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:06.174]  [00:07:47.507][info  ][EM] <<< [E:29148i S:14009 M:240766732 (Ack:31550102)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:06.174]  [00:07:47.508][info  ][EM] ??1 [E:29148i S:14009 M:240766732] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:07.002]  [00:07:48.333][info  ][EM] >>> [E:29148i S:14009 M:31550103 (Ack:240766732)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:07.126]  [00:07:48.466][info  ][EM] <<< [E:29148i S:14009 M:240766733 (Ack:31550103)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:07.138]  [00:07:48.467][info  ][EM] ??1 [E:29148i S:14009 M:240766733] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5525ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:07.138]  [00:07:48.467][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:07.904]  [00:07:49.242][info  ][EM] >>> [E:29148i S:14009 M:31550104 (Ack:240766733)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:07.963]  [00:07:49.302][info  ][EM] <<< [E:29148i S:14009 M:240766734 (Ack:31550104)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:07.963]  [00:07:49.302][info  ][EM] ??1 [E:29148i S:14009 M:240766734] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:08.803]  [00:07:50.144][info  ][EM] >>> [E:29148i S:14009 M:31550105 (Ack:240766734)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:08.872]  [00:07:50.205][info  ][EM] <<< [E:29148i S:14009 M:240766735 (Ack:31550105)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:08.872]  [00:07:50.205][info  ][EM] ??1 [E:29148i S:14009 M:240766735] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5559ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:09.709]  [00:07:51.041][info  ][EM] >>> [E:29148i S:14009 M:31550106 (Ack:240766735)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:09.772]  [00:07:51.102][info  ][EM] <<< [E:29148i S:14009 M:240766736 (Ack:31550106)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:09.772]  [00:07:51.103][info  ][EM] ??1 [E:29148i S:14009 M:240766736] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5443ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:10.725]  [00:07:52.058][info  ][EM] >>> [E:29148i S:14009 M:31550107 (Ack:240766736)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:10.857]  [00:07:52.194][info  ][EM] <<< [E:29148i S:14009 M:240766737 (Ack:31550107)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:10.857]  [00:07:52.195][info  ][EM] ??1 [E:29148i S:14009 M:240766737] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:10.868]  [00:07:52.195][error ][DL] Long dispatch time: 136 ms, for event type 2
[19:11:11.767]  [00:07:53.103][info  ][EM] >>> [E:29148i S:14009 M:31550108 (Ack:240766737)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:11.832]  [00:07:53.164][info  ][EM] <<< [E:29148i S:14009 M:240766738 (Ack:31550108)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:11.832]  [00:07:53.164][info  ][EM] ??1 [E:29148i S:14009 M:240766738] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5587ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:12.571]  [00:07:53.908][info  ][EM] >>> [E:29148i S:14009 M:31550109 (Ack:240766738)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:12.633]  [00:07:53.967][info  ][EM] <<< [E:29148i S:14009 M:240766739 (Ack:31550109)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:12.633]  [00:07:53.968][info  ][EM] ??1 [E:29148i S:14009 M:240766739] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:13.625]  [00:07:54.957][info  ][EM] >>> [E:29148i S:14009 M:31550110 (Ack:240766739)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:13.676]  [00:07:55.016][info  ][EM] <<< [E:29148i S:14009 M:240766740 (Ack:31550110)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:13.689]  [00:07:55.017][info  ][EM] ??1 [E:29148i S:14009 M:240766740] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5736ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:14.435]  [00:07:55.772][info  ][EM] >>> [E:29148i S:14009 M:31550111 (Ack:240766740)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:14.574]  [00:07:55.906][info  ][EM] <<< [E:29148i S:14009 M:240766741 (Ack:31550111)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:14.574]  [00:07:55.907][info  ][EM] ??1 [E:29148i S:14009 M:240766741] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5299ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:14.574]  [00:07:55.907][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:11:15.460]  [00:07:56.800][info  ][EM] >>> [E:29148i S:14009 M:31550112 (Ack:240766741)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:15.529]  [00:07:56.861][info  ][EM] <<< [E:29148i S:14009 M:240766742 (Ack:31550112)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:15.529]  [00:07:56.861][info  ][EM] ??1 [E:29148i S:14009 M:240766742] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5723ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:16.239]  [00:07:57.576][info  ][EM] >>> [E:29148i S:14009 M:31550113 (Ack:240766742)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:16.301]  [00:07:57.636][info  ][EM] <<< [E:29148i S:14009 M:240766743 (Ack:31550113)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:16.301]  [00:07:57.637][info  ][EM] ??1 [E:29148i S:14009 M:240766743] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:17.145]  [00:07:58.486][info  ][EM] >>> [E:29148i S:14009 M:31550114 (Ack:240766743)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:17.209]  [00:07:58.545][info  ][EM] <<< [E:29148i S:14009 M:240766744 (Ack:31550114)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:17.209]  [00:07:58.546][info  ][EM] ??1 [E:29148i S:14009 M:240766744] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:17.945]  [00:07:59.282][info  ][EM] >>> [E:29148i S:14009 M:31550115 (Ack:240766744)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:18.079]  [00:07:59.415][info  ][EM] <<< [E:29148i S:14009 M:240766745 (Ack:31550115)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:18.079]  [00:07:59.416][info  ][EM] ??1 [E:29148i S:14009 M:240766745] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:18.091]  [00:07:59.416][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:18.848]  [00:08:00.184][info  ][EM] >>> [E:29148i S:14009 M:31550116 (Ack:240766745)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:18.910]  [00:08:00.245][info  ][EM] <<< [E:29148i S:14009 M:240766746 (Ack:31550116)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:18.910]  [00:08:00.246][info  ][EM] ??1 [E:29148i S:14009 M:240766746] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5723ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:19.867]  [00:08:01.206][info  ][EM] >>> [E:29148i S:14009 M:31550117 (Ack:240766746)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:19.929]  [00:08:01.265][info  ][EM] <<< [E:29148i S:14009 M:240766747 (Ack:31550117)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:19.929]  [00:08:01.266][info  ][EM] ??1 [E:29148i S:14009 M:240766747] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5291ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:20.869]  [00:08:02.198][info  ][EM] >>> [E:29148i S:14009 M:31550118 (Ack:240766747)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:20.919]  [00:08:02.258][info  ][EM] <<< [E:29148i S:14009 M:240766748 (Ack:31550118)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:20.919]  [00:08:02.258][info  ][EM] ??1 [E:29148i S:14009 M:240766748] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:21.738]  [00:08:03.070][info  ][EM] >>> [E:29148i S:14009 M:31550119 (Ack:240766748)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:21.864]  [00:08:03.204][info  ][EM] <<< [E:29148i S:14009 M:240766749 (Ack:31550119)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:21.864]  [00:08:03.204][info  ][EM] ??1 [E:29148i S:14009 M:240766749] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:21.879]  [00:08:03.205][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:11:22.750]  [00:08:04.091][info  ][EM] >>> [E:29148i S:14009 M:31550120 (Ack:240766749)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:22.812]  [00:08:04.151][info  ][EM] <<< [E:29148i S:14009 M:240766750 (Ack:31550120)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:22.812]  [00:08:04.152][info  ][EM] ??1 [E:29148i S:14009 M:240766750] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:23.537]  [00:08:04.871][info  ][EM] >>> [E:29148i S:14009 M:31550121 (Ack:240766750)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:23.599]  [00:08:04.931][info  ][EM] <<< [E:29148i S:14009 M:240766751 (Ack:31550121)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:23.599]  [00:08:04.932][info  ][EM] ??1 [E:29148i S:14009 M:240766751] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:24.307]  [00:08:05.643][info  ][EM] >>> [E:29148i S:14009 M:31550122 (Ack:240766751)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:24.368]  [00:08:05.704][info  ][EM] <<< [E:29148i S:14009 M:240766752 (Ack:31550122)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:24.368]  [00:08:05.705][info  ][EM] ??1 [E:29148i S:14009 M:240766752] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5738ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:25.199]  [00:08:06.527][info  ][EM] >>> [E:29148i S:14009 M:31550123 (Ack:240766752)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:25.323]  [00:08:06.661][info  ][EM] <<< [E:29148i S:14009 M:240766753 (Ack:31550123)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:25.323]  [00:08:06.662][info  ][EM] ??1 [E:29148i S:14009 M:240766753] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:25.337]  [00:08:06.663][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:26.426]  [00:08:07.763][info  ][EM] >>> [E:29148i S:14009 M:31550124 (Ack:240766753)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:26.489]  [00:08:07.823][info  ][EM] <<< [E:29148i S:14009 M:240766754 (Ack:31550124)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:26.489]  [00:08:07.824][info  ][EM] ??1 [E:29148i S:14009 M:240766754] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5699ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:27.359]  [00:08:08.694][info  ][EM] >>> [E:29148i S:14009 M:31550125 (Ack:240766754)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:27.418]  [00:08:08.754][info  ][EM] <<< [E:29148i S:14009 M:240766755 (Ack:31550125)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:27.418]  [00:08:08.754][info  ][EM] ??1 [E:29148i S:14009 M:240766755] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:28.242]  [00:08:09.582][info  ][EM] >>> [E:29148i S:14009 M:31550126 (Ack:240766755)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:28.311]  [00:08:09.641][info  ][EM] <<< [E:29148i S:14009 M:240766756 (Ack:31550126)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:28.311]  [00:08:09.642][info  ][EM] ??1 [E:29148i S:14009 M:240766756] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:29.027]  [00:08:10.357][info  ][EM] >>> [E:29148i S:14009 M:31550127 (Ack:240766756)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:29.159]  [00:08:10.491][info  ][EM] <<< [E:29148i S:14009 M:240766757 (Ack:31550127)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:29.159]  [00:08:10.492][info  ][EM] ??1 [E:29148i S:14009 M:240766757] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:29.159]  [00:08:10.492][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:30.022]  [00:08:11.356][info  ][EM] >>> [E:29148i S:14009 M:31550128 (Ack:240766757)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:30.077]  [00:08:11.416][info  ][EM] <<< [E:29148i S:14009 M:240766758 (Ack:31550128)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:30.088]  [00:08:11.416][info  ][EM] ??1 [E:29148i S:14009 M:240766758] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:31.007]  [00:08:12.345][info  ][EM] >>> [E:29148i S:14009 M:31550129 (Ack:240766758)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:31.071]  [00:08:12.406][info  ][EM] <<< [E:29148i S:14009 M:240766759 (Ack:31550129)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:31.071]  [00:08:12.406][info  ][EM] ??1 [E:29148i S:14009 M:240766759] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5564ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:31.920]  [00:08:13.252][info  ][EM] >>> [E:29148i S:14009 M:31550130 (Ack:240766759)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:31.973]  [00:08:13.313][info  ][EM] <<< [E:29148i S:14009 M:240766760 (Ack:31550130)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:31.988]  [00:08:13.314][info  ][EM] ??1 [E:29148i S:14009 M:240766760] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:32.888]  [00:08:14.221][info  ][EM] >>> [E:29148i S:14009 M:31550131 (Ack:240766760)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:33.025]  [00:08:14.355][info  ][EM] <<< [E:29148i S:14009 M:240766761 (Ack:31550131)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:33.025]  [00:08:14.356][info  ][EM] ??1 [E:29148i S:14009 M:240766761] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:33.025]  [00:08:14.356][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:33.658]  [00:08:14.998][info  ][EM] >>> [E:29148i S:14009 M:31550132 (Ack:240766761)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:33.717]  [00:08:15.058][info  ][EM] <<< [E:29148i S:14009 M:240766762 (Ack:31550132)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:33.728]  [00:08:15.058][info  ][EM] ??1 [E:29148i S:14009 M:240766762] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5465ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:34.574]  [00:08:15.914][info  ][EM] >>> [E:29148i S:14009 M:31550133 (Ack:240766762)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:34.643]  [00:08:15.974][info  ][EM] <<< [E:29148i S:14009 M:240766763 (Ack:31550133)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:34.643]  [00:08:15.975][info  ][EM] ??1 [E:29148i S:14009 M:240766763] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:35.378]  [00:08:16.712][info  ][EM] >>> [E:29148i S:14009 M:31550134 (Ack:240766763)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:35.442]  [00:08:16.773][info  ][EM] <<< [E:29148i S:14009 M:240766764 (Ack:31550134)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:35.442]  [00:08:16.774][info  ][EM] ??1 [E:29148i S:14009 M:240766764] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:36.167]  [00:08:17.504][info  ][EM] >>> [E:29148i S:14009 M:31550135 (Ack:240766764)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:36.304]  [00:08:17.638][info  ][EM] <<< [E:29148i S:14009 M:240766765 (Ack:31550135)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:36.304]  [00:08:17.639][info  ][EM] ??1 [E:29148i S:14009 M:240766765] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:36.304]  [00:08:17.639][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:11:37.290]  [00:08:18.620][info  ][EM] >>> [E:29148i S:14009 M:31550136 (Ack:240766765)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:37.339]  [00:08:18.680][info  ][EM] <<< [E:29148i S:14009 M:240766766 (Ack:31550136)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:37.351]  [00:08:18.680][info  ][EM] ??1 [E:29148i S:14009 M:240766766] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:38.061]  [00:08:19.396][info  ][EM] >>> [E:29148i S:14009 M:31550137 (Ack:240766766)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:38.124]  [00:08:19.457][info  ][EM] <<< [E:29148i S:14009 M:240766767 (Ack:31550137)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:38.124]  [00:08:19.458][info  ][EM] ??1 [E:29148i S:14009 M:240766767] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:38.913]  [00:08:20.252][info  ][EM] >>> [E:29148i S:14009 M:31550138 (Ack:240766767)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:38.978]  [00:08:20.313][info  ][EM] <<< [E:29148i S:14009 M:240766768 (Ack:31550138)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:38.978]  [00:08:20.314][info  ][EM] ??1 [E:29148i S:14009 M:240766768] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:39.739]  [00:08:21.077][info  ][EM] >>> [E:29148i S:14009 M:31550139 (Ack:240766768)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:39.878]  [00:08:21.210][info  ][EM] <<< [E:29148i S:14009 M:240766769 (Ack:31550139)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:39.878]  [00:08:21.211][info  ][EM] ??1 [E:29148i S:14009 M:240766769] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5252ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:39.878]  [00:08:21.211][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:11:41.001]  [00:08:22.334][info  ][EM] >>> [E:29148i S:14009 M:31550140 (Ack:240766769)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:41.063]  [00:08:22.395][info  ][EM] <<< [E:29148i S:14009 M:240766770 (Ack:31550140)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:41.063]  [00:08:22.396][info  ][EM] ??1 [E:29148i S:14009 M:240766770] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:41.800]  [00:08:23.138][info  ][EM] >>> [E:29148i S:14009 M:31550141 (Ack:240766770)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:41.861]  [00:08:23.199][info  ][EM] <<< [E:29148i S:14009 M:240766771 (Ack:31550141)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:41.861]  [00:08:23.200][info  ][EM] ??1 [E:29148i S:14009 M:240766771] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5398ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:42.713]  [00:08:24.048][info  ][EM] >>> [E:29148i S:14009 M:31550142 (Ack:240766771)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:42.775]  [00:08:24.108][info  ][EM] <<< [E:29148i S:14009 M:240766772 (Ack:31550142)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:42.775]  [00:08:24.109][info  ][EM] ??1 [E:29148i S:14009 M:240766772] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:43.619]  [00:08:24.958][info  ][EM] >>> [E:29148i S:14009 M:31550143 (Ack:240766772)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:43.755]  [00:08:25.090][info  ][EM] <<< [E:29148i S:14009 M:240766773 (Ack:31550143)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:43.755]  [00:08:25.091][info  ][EM] ??1 [E:29148i S:14009 M:240766773] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:43.769]  [00:08:25.092][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:44.817]  [00:08:26.155][info  ][EM] >>> [E:29148i S:14009 M:31550144 (Ack:240766773)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:44.875]  [00:08:26.215][info  ][EM] <<< [E:29148i S:14009 M:240766774 (Ack:31550144)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:44.886]  [00:08:26.216][info  ][EM] ??1 [E:29148i S:14009 M:240766774] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:45.851]  [00:08:27.183][info  ][EM] >>> [E:29148i S:14009 M:31550145 (Ack:240766774)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:45.905]  [00:08:27.244][info  ][EM] <<< [E:29148i S:14009 M:240766775 (Ack:31550145)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:45.905]  [00:08:27.245][info  ][EM] ??1 [E:29148i S:14009 M:240766775] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:46.715]  [00:08:28.054][info  ][EM] >>> [E:29148i S:14009 M:31550146 (Ack:240766775)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:46.787]  [00:08:28.114][info  ][EM] <<< [E:29148i S:14009 M:240766776 (Ack:31550146)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:46.787]  [00:08:28.115][info  ][EM] ??1 [E:29148i S:14009 M:240766776] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:47.517]  [00:08:28.850][info  ][EM] >>> [E:29148i S:14009 M:31550147 (Ack:240766776)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:47.646]  [00:08:28.986][info  ][EM] <<< [E:29148i S:14009 M:240766777 (Ack:31550147)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:47.657]  [00:08:28.987][info  ][EM] ??1 [E:29148i S:14009 M:240766777] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5252ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:47.657]  [00:08:28.987][error ][DL] Long dispatch time: 136 ms, for event type 2
[19:11:48.879]  [00:08:30.212][info  ][EM] >>> [E:29148i S:14009 M:31550148 (Ack:240766777)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:48.936]  [00:08:30.273][info  ][EM] <<< [E:29148i S:14009 M:240766778 (Ack:31550148)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:48.936]  [00:08:30.274][info  ][EM] ??1 [E:29148i S:14009 M:240766778] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:49.783]  [00:08:31.113][info  ][EM] >>> [E:29148i S:14009 M:31550149 (Ack:240766778)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:49.843]  [00:08:31.173][info  ][EM] <<< [E:29148i S:14009 M:240766779 (Ack:31550149)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:49.843]  [00:08:31.174][info  ][EM] ??1 [E:29148i S:14009 M:240766779] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:50.903]  [00:08:32.235][info  ][EM] >>> [E:29148i S:14009 M:31550150 (Ack:240766779)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:50.956]  [00:08:32.294][info  ][EM] <<< [E:29148i S:14009 M:240766780 (Ack:31550150)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:50.956]  [00:08:32.295][info  ][EM] ??1 [E:29148i S:14009 M:240766780] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:51.652]  [00:08:32.989][info  ][EM] >>> [E:29148i S:14009 M:31550151 (Ack:240766780)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:51.785]  [00:08:33.123][info  ][EM] <<< [E:29148i S:14009 M:240766781 (Ack:31550151)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:51.785]  [00:08:33.124][info  ][EM] ??1 [E:29148i S:14009 M:240766781] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:51.797]  [00:08:33.124][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:11:52.428]  [00:08:33.767][info  ][EM] >>> [E:29148i S:14009 M:31550152 (Ack:240766781)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:52.492]  [00:08:33.828][info  ][EM] <<< [E:29148i S:14009 M:240766782 (Ack:31550152)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:52.492]  [00:08:33.828][info  ][EM] ??1 [E:29148i S:14009 M:240766782] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5295ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:53.220]  [00:08:34.550][info  ][EM] >>> [E:29148i S:14009 M:31550153 (Ack:240766782)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:53.282]  [00:08:34.611][info  ][EM] <<< [E:29148i S:14009 M:240766783 (Ack:31550153)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:53.282]  [00:08:34.612][info  ][EM] ??1 [E:29148i S:14009 M:240766783] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:54.238]  [00:08:35.576][info  ][EM] >>> [E:29148i S:14009 M:31550154 (Ack:240766783)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:54.298]  [00:08:35.636][info  ][EM] <<< [E:29148i S:14009 M:240766784 (Ack:31550154)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:54.298]  [00:08:35.637][info  ][EM] ??1 [E:29148i S:14009 M:240766784] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:55.341]  [00:08:36.672][info  ][EM] >>> [E:29148i S:14009 M:31550155 (Ack:240766784)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:55.472]  [00:08:36.806][info  ][EM] <<< [E:29148i S:14009 M:240766785 (Ack:31550155)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:55.472]  [00:08:36.806][info  ][EM] ??1 [E:29148i S:14009 M:240766785] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:55.472]  [00:08:36.807][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:11:56.122]  [00:08:37.455][info  ][EM] >>> [E:29148i S:14009 M:31550156 (Ack:240766785)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:56.187]  [00:08:37.515][info  ][EM] <<< [E:29148i S:14009 M:240766786 (Ack:31550156)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:56.187]  [00:08:37.516][info  ][EM] ??1 [E:29148i S:14009 M:240766786] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5286ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:56.906]  [00:08:38.237][info  ][EM] >>> [E:29148i S:14009 M:31550157 (Ack:240766786)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:56.959]  [00:08:38.297][info  ][EM] <<< [E:29148i S:14009 M:240766787 (Ack:31550157)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:56.959]  [00:08:38.298][info  ][EM] ??1 [E:29148i S:14009 M:240766787] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:57.796]  [00:08:39.136][info  ][EM] >>> [E:29148i S:14009 M:31550158 (Ack:240766787)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:57.862]  [00:08:39.197][info  ][EM] <<< [E:29148i S:14009 M:240766788 (Ack:31550158)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:57.862]  [00:08:39.198][info  ][EM] ??1 [E:29148i S:14009 M:240766788] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5471ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:58.602]  [00:08:39.933][info  ][EM] >>> [E:29148i S:14009 M:31550159 (Ack:240766788)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:58.730]  [00:08:40.067][info  ][EM] <<< [E:29148i S:14009 M:240766789 (Ack:31550159)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:58.730]  [00:08:40.068][info  ][EM] ??1 [E:29148i S:14009 M:240766789] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[19:11:58.742]  [00:08:40.068][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:11:59.358]  [00:08:40.695][info  ][EM] >>> [E:29148i S:14009 M:31550160 (Ack:240766789)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:11:59.415]  [00:08:40.755][info  ][EM] <<< [E:29148i S:14009 M:240766790 (Ack:31550160)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:11:59.415]  [00:08:40.755][info  ][EM] ??1 [E:29148i S:14009 M:240766790] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:00.431]  [00:08:41.770][info  ][EM] >>> [E:29148i S:14009 M:31550161 (Ack:240766790)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:00.492]  [00:08:41.831][info  ][EM] <<< [E:29148i S:14009 M:240766791 (Ack:31550161)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:00.492]  [00:08:41.832][info  ][EM] ??1 [E:29148i S:14009 M:240766791] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:01.441]  [00:08:42.781][info  ][EM] >>> [E:29148i S:14009 M:31550162 (Ack:240766791)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:01.506]  [00:08:42.841][info  ][EM] <<< [E:29148i S:14009 M:240766792 (Ack:31550162)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:01.506]  [00:08:42.842][info  ][EM] ??1 [E:29148i S:14009 M:240766792] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:02.198]  [00:08:43.537][info  ][EM] >>> [E:29148i S:14009 M:31550163 (Ack:240766792)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:02.338]  [00:08:43.670][info  ][EM] <<< [E:29148i S:14009 M:240766793 (Ack:31550163)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:02.338]  [00:08:43.671][info  ][EM] ??1 [E:29148i S:14009 M:240766793] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5418ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:02.338]  [00:08:43.671][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:12:02.984]  [00:08:44.314][info  ][EM] >>> [E:29148i S:14009 M:31550164 (Ack:240766793)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:03.043]  [00:08:44.375][info  ][EM] <<< [E:29148i S:14009 M:240766794 (Ack:31550164)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:03.043]  [00:08:44.375][info  ][EM] ??1 [E:29148i S:14009 M:240766794] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:04.184]  [00:08:45.524][info  ][EM] >>> [E:29148i S:14009 M:31550165 (Ack:240766794)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:04.246]  [00:08:45.584][info  ][EM] <<< [E:29148i S:14009 M:240766795 (Ack:31550165)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:04.246]  [00:08:45.585][info  ][EM] ??1 [E:29148i S:14009 M:240766795] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:04.963]  [00:08:46.295][info  ][EM] >>> [E:29148i S:14009 M:31550166 (Ack:240766795)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:05.023]  [00:08:46.356][info  ][EM] <<< [E:29148i S:14009 M:240766796 (Ack:31550166)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:05.023]  [00:08:46.357][info  ][EM] ??1 [E:29148i S:14009 M:240766796] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:05.867]  [00:08:47.207][info  ][EM] >>> [E:29148i S:14009 M:31550167 (Ack:240766796)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:06.006]  [00:08:47.340][info  ][EM] <<< [E:29148i S:14009 M:240766797 (Ack:31550167)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:06.006]  [00:08:47.341][info  ][EM] ??1 [E:29148i S:14009 M:240766797] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5407ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:06.006]  [00:08:47.341][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:12:07.112]  [00:08:48.445][info  ][EM] >>> [E:29148i S:14009 M:31550168 (Ack:240766797)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:07.165]  [00:08:48.504][info  ][EM] <<< [E:29148i S:14009 M:240766798 (Ack:31550168)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:07.165]  [00:08:48.505][info  ][EM] ??1 [E:29148i S:14009 M:240766798] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:07.868]  [00:08:49.207][info  ][EM] >>> [E:29148i S:14009 M:31550169 (Ack:240766798)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:07.930]  [00:08:49.266][info  ][EM] <<< [E:29148i S:14009 M:240766799 (Ack:31550169)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:07.930]  [00:08:49.267][info  ][EM] ??1 [E:29148i S:14009 M:240766799] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5209ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:08.651]  [00:08:49.988][info  ][EM] >>> [E:29148i S:14009 M:31550170 (Ack:240766799)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:08.711]  [00:08:50.048][info  ][EM] <<< [E:29148i S:14009 M:240766800 (Ack:31550170)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:08.711]  [00:08:50.049][info  ][EM] ??1 [E:29148i S:14009 M:240766800] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5512ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:09.682]  [00:08:51.013][info  ][EM] >>> [E:29148i S:14009 M:31550171 (Ack:240766800)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:09.811]  [00:08:51.147][info  ][EM] <<< [E:29148i S:14009 M:240766801 (Ack:31550171)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:09.811]  [00:08:51.148][info  ][EM] ??1 [E:29148i S:14009 M:240766801] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:09.825]  [00:08:51.148][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:10.595]  [00:08:51.936][info  ][EM] >>> [E:29148i S:14009 M:31550172 (Ack:240766801)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:10.661]  [00:08:51.997][info  ][EM] <<< [E:29148i S:14009 M:240766802 (Ack:31550172)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:10.661]  [00:08:51.998][info  ][EM] ??1 [E:29148i S:14009 M:240766802] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:11.515]  [00:08:52.843][info  ][EM] >>> [E:29148i S:14009 M:31550173 (Ack:240766802)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:11.567]  [00:08:52.904][info  ][EM] <<< [E:29148i S:14009 M:240766803 (Ack:31550173)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:11.567]  [00:08:52.904][info  ][EM] ??1 [E:29148i S:14009 M:240766803] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:12.396]  [00:08:53.731][info  ][EM] >>> [E:29148i S:14009 M:31550174 (Ack:240766803)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:12.450]  [00:08:53.791][info  ][EM] <<< [E:29148i S:14009 M:240766804 (Ack:31550174)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:12.461]  [00:08:53.792][info  ][EM] ??1 [E:29148i S:14009 M:240766804] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:13.157]  [00:08:54.495][info  ][EM] >>> [E:29148i S:14009 M:31550175 (Ack:240766804)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:13.298]  [00:08:54.628][info  ][EM] <<< [E:29148i S:14009 M:240766805 (Ack:31550175)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:13.298]  [00:08:54.628][info  ][EM] ??1 [E:29148i S:14009 M:240766805] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:13.298]  [00:08:54.629][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:14.535]  [00:08:55.873][info  ][EM] >>> [E:29148i S:14009 M:31550176 (Ack:240766805)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:14.592]  [00:08:55.932][info  ][EM] <<< [E:29148i S:14009 M:240766806 (Ack:31550176)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:14.603]  [00:08:55.933][info  ][EM] ??1 [E:29148i S:14009 M:240766806] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:15.406]  [00:08:56.742][info  ][EM] >>> [E:29148i S:14009 M:31550177 (Ack:240766806)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:15.461]  [00:08:56.802][info  ][EM] <<< [E:29148i S:14009 M:240766807 (Ack:31550177)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:15.472]  [00:08:56.803][info  ][EM] ??1 [E:29148i S:14009 M:240766807] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:16.206]  [00:08:57.543][info  ][EM] >>> [E:29148i S:14009 M:31550178 (Ack:240766807)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:16.264]  [00:08:57.604][info  ][EM] <<< [E:29148i S:14009 M:240766808 (Ack:31550178)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:16.276]  [00:08:57.605][info  ][EM] ??1 [E:29148i S:14009 M:240766808] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5525ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:16.937]  [00:08:58.276][info  ][EM] >>> [E:29148i S:14009 M:31550179 (Ack:240766808)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:17.068]  [00:08:58.409][info  ][EM] <<< [E:29148i S:14009 M:240766809 (Ack:31550179)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:17.080]  [00:08:58.410][info  ][EM] ??1 [E:29148i S:14009 M:240766809] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:17.080]  [00:08:58.411][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:17.742]  [00:08:59.078][info  ][EM] >>> [E:29148i S:14009 M:31550180 (Ack:240766809)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:17.804]  [00:08:59.138][info  ][EM] <<< [E:29148i S:14009 M:240766810 (Ack:31550180)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:17.804]  [00:08:59.138][info  ][EM] ??1 [E:29148i S:14009 M:240766810] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:18.733]  [00:09:00.071][info  ][EM] >>> [E:29148i S:14009 M:31550181 (Ack:240766810)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:18.795]  [00:09:00.131][info  ][EM] <<< [E:29148i S:14009 M:240766811 (Ack:31550181)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:18.795]  [00:09:00.132][info  ][EM] ??1 [E:29148i S:14009 M:240766811] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5362ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:19.494]  [00:09:00.833][info  ][EM] >>> [E:29148i S:14009 M:31550182 (Ack:240766811)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:19.561]  [00:09:00.892][info  ][EM] <<< [E:29148i S:14009 M:240766812 (Ack:31550182)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:19.561]  [00:09:00.893][info  ][EM] ??1 [E:29148i S:14009 M:240766812] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:20.302]  [00:09:01.632][info  ][EM] >>> [E:29148i S:14009 M:31550183 (Ack:240766812)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:20.431]  [00:09:01.766][info  ][EM] <<< [E:29148i S:14009 M:240766813 (Ack:31550183)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:20.431]  [00:09:01.766][info  ][EM] ??1 [E:29148i S:14009 M:240766813] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:20.431]  [00:09:01.767][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:21.796]  [00:09:03.132][info  ][EM] >>> [E:29148i S:14009 M:31550184 (Ack:240766813)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:21.858]  [00:09:03.193][info  ][EM] <<< [E:29148i S:14009 M:240766814 (Ack:31550184)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:21.858]  [00:09:03.194][info  ][EM] ??1 [E:29148i S:14009 M:240766814] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:22.633]  [00:09:03.971][info  ][EM] >>> [E:29148i S:14009 M:31550185 (Ack:240766814)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:22.696]  [00:09:04.032][info  ][EM] <<< [E:29148i S:14009 M:240766815 (Ack:31550185)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:22.696]  [00:09:04.033][info  ][EM] ??1 [E:29148i S:14009 M:240766815] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:23.389]  [00:09:04.729][info  ][EM] >>> [E:29148i S:14009 M:31550186 (Ack:240766815)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:23.447]  [00:09:04.790][info  ][EM] <<< [E:29148i S:14009 M:240766816 (Ack:31550186)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:23.461]  [00:09:04.790][info  ][EM] ??1 [E:29148i S:14009 M:240766816] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:24.272]  [00:09:05.614][info  ][EM] >>> [E:29148i S:14009 M:31550187 (Ack:240766816)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:24.416]  [00:09:05.748][info  ][EM] <<< [E:29148i S:14009 M:240766817 (Ack:31550187)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:24.416]  [00:09:05.748][info  ][EM] ??1 [E:29148i S:14009 M:240766817] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:24.416]  [00:09:05.749][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:25.031]  [00:09:06.372][info  ][EM] >>> [E:29148i S:14009 M:31550188 (Ack:240766817)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:25.097]  [00:09:06.432][info  ][EM] <<< [E:29148i S:14009 M:240766818 (Ack:31550188)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:25.097]  [00:09:06.433][info  ][EM] ??1 [E:29148i S:14009 M:240766818] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5749ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:25.942]  [00:09:07.279][info  ][EM] >>> [E:29148i S:14009 M:31550189 (Ack:240766818)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:26.001]  [00:09:07.339][info  ][EM] <<< [E:29148i S:14009 M:240766819 (Ack:31550189)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:26.001]  [00:09:07.339][info  ][EM] ??1 [E:29148i S:14009 M:240766819] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:26.736]  [00:09:08.068][info  ][EM] >>> [E:29148i S:14009 M:31550190 (Ack:240766819)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:26.787]  [00:09:08.128][info  ][EM] <<< [E:29148i S:14009 M:240766820 (Ack:31550190)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:26.801]  [00:09:08.129][info  ][EM] ??1 [E:29148i S:14009 M:240766820] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5297ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:27.490]  [00:09:08.832][info  ][EM] >>> [E:29148i S:14009 M:31550191 (Ack:240766820)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:27.623]  [00:09:08.964][info  ][EM] <<< [E:29148i S:14009 M:240766821 (Ack:31550191)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:27.640]  [00:09:08.965][info  ][EM] ??1 [E:29148i S:14009 M:240766821] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5579ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:27.640]  [00:09:08.966][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:28.504]  [00:09:09.835][info  ][EM] >>> [E:29148i S:14009 M:31550192 (Ack:240766821)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:28.561]  [00:09:09.896][info  ][EM] <<< [E:29148i S:14009 M:240766822 (Ack:31550192)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:28.561]  [00:09:09.897][info  ][EM] ??1 [E:29148i S:14009 M:240766822] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:29.281]  [00:09:10.621][info  ][EM] >>> [E:29148i S:14009 M:31550193 (Ack:240766822)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:29.343]  [00:09:10.680][info  ][EM] <<< [E:29148i S:14009 M:240766823 (Ack:31550193)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:29.343]  [00:09:10.681][info  ][EM] ??1 [E:29148i S:14009 M:240766823] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5422ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:30.183]  [00:09:11.525][info  ][EM] >>> [E:29148i S:14009 M:31550194 (Ack:240766823)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:30.254]  [00:09:11.585][info  ][EM] <<< [E:29148i S:14009 M:240766824 (Ack:31550194)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:30.254]  [00:09:11.586][info  ][EM] ??1 [E:29148i S:14009 M:240766824] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:30.950]  [00:09:12.292][info  ][EM] >>> [E:29148i S:14009 M:31550195 (Ack:240766824)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:31.094]  [00:09:12.426][info  ][EM] <<< [E:29148i S:14009 M:240766825 (Ack:31550195)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:31.094]  [00:09:12.427][info  ][EM] ??1 [E:29148i S:14009 M:240766825] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:31.094]  [00:09:12.427][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:31.755]  [00:09:13.093][info  ][EM] >>> [E:29148i S:14009 M:31550196 (Ack:240766825)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:31.817]  [00:09:13.154][info  ][EM] <<< [E:29148i S:14009 M:240766826 (Ack:31550196)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:31.817]  [00:09:13.155][info  ][EM] ??1 [E:29148i S:14009 M:240766826] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5587ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:32.560]  [00:09:13.898][info  ][EM] >>> [E:29148i S:14009 M:31550197 (Ack:240766826)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:32.620]  [00:09:13.958][info  ][EM] <<< [E:29148i S:14009 M:240766827 (Ack:31550197)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:32.620]  [00:09:13.958][info  ][EM] ??1 [E:29148i S:14009 M:240766827] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5577ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:33.438]  [00:09:14.771][info  ][EM] >>> [E:29148i S:14009 M:31550198 (Ack:240766827)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:33.498]  [00:09:14.831][info  ][EM] <<< [E:29148i S:14009 M:240766828 (Ack:31550198)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:33.498]  [00:09:14.832][info  ][EM] ??1 [E:29148i S:14009 M:240766828] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:34.235]  [00:09:15.569][info  ][EM] >>> [E:29148i S:14009 M:31550199 (Ack:240766828)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:34.370]  [00:09:15.703][info  ][EM] <<< [E:29148i S:14009 M:240766829 (Ack:31550199)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:34.370]  [00:09:15.704][info  ][EM] ??1 [E:29148i S:14009 M:240766829] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:34.370]  [00:09:15.704][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:35.423]  [00:09:16.755][info  ][EM] >>> [E:29148i S:14009 M:31550200 (Ack:240766829)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:35.474]  [00:09:16.816][info  ][EM] <<< [E:29148i S:14009 M:240766830 (Ack:31550200)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:35.485]  [00:09:16.817][info  ][EM] ??1 [E:29148i S:14009 M:240766830] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:36.176]  [00:09:17.511][info  ][EM] >>> [E:29148i S:14009 M:31550201 (Ack:240766830)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:36.236]  [00:09:17.572][info  ][EM] <<< [E:29148i S:14009 M:240766831 (Ack:31550201)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:36.236]  [00:09:17.572][info  ][EM] ??1 [E:29148i S:14009 M:240766831] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:36.957]  [00:09:18.295][info  ][EM] >>> [E:29148i S:14009 M:31550202 (Ack:240766831)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:37.017]  [00:09:18.356][info  ][EM] <<< [E:29148i S:14009 M:240766832 (Ack:31550202)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:37.017]  [00:09:18.356][info  ][EM] ??1 [E:29148i S:14009 M:240766832] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:37.712]  [00:09:19.051][info  ][EM] >>> [E:29148i S:14009 M:31550203 (Ack:240766832)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:37.855]  [00:09:19.185][info  ][EM] <<< [E:29148i S:14009 M:240766833 (Ack:31550203)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:37.855]  [00:09:19.185][info  ][EM] ??1 [E:29148i S:14009 M:240766833] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:37.855]  [00:09:19.186][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:38.719]  [00:09:20.057][info  ][EM] >>> [E:29148i S:14009 M:31550204 (Ack:240766833)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:38.778]  [00:09:20.118][info  ][EM] <<< [E:29148i S:14009 M:240766834 (Ack:31550204)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:38.778]  [00:09:20.119][info  ][EM] ??1 [E:29148i S:14009 M:240766834] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5729ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:39.544]  [00:09:20.876][info  ][EM] >>> [E:29148i S:14009 M:31550205 (Ack:240766834)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:39.597]  [00:09:20.936][info  ][EM] <<< [E:29148i S:14009 M:240766835 (Ack:31550205)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:39.597]  [00:09:20.937][info  ][EM] ??1 [E:29148i S:14009 M:240766835] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:40.375]  [00:09:21.708][info  ][EM] >>> [E:29148i S:14009 M:31550206 (Ack:240766835)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:40.434]  [00:09:21.769][info  ][EM] <<< [E:29148i S:14009 M:240766836 (Ack:31550206)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:40.434]  [00:09:21.770][info  ][EM] ??1 [E:29148i S:14009 M:240766836] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:41.276]  [00:09:22.618][info  ][EM] >>> [E:29148i S:14009 M:31550207 (Ack:240766836)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:41.420]  [00:09:22.751][info  ][EM] <<< [E:29148i S:14009 M:240766837 (Ack:31550207)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:41.420]  [00:09:22.752][info  ][EM] ??1 [E:29148i S:14009 M:240766837] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:41.420]  [00:09:22.752][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:12:42.035]  [00:09:23.376][info  ][EM] >>> [E:29148i S:14009 M:31550208 (Ack:240766837)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:42.101]  [00:09:23.437][info  ][EM] <<< [E:29148i S:14009 M:240766838 (Ack:31550208)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:42.101]  [00:09:23.437][info  ][EM] ??1 [E:29148i S:14009 M:240766838] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:43.392]  [00:09:24.730][info  ][EM] >>> [E:29148i S:14009 M:31550209 (Ack:240766838)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:43.452]  [00:09:24.790][info  ][EM] <<< [E:29148i S:14009 M:240766839 (Ack:31550209)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:43.452]  [00:09:24.791][info  ][EM] ??1 [E:29148i S:14009 M:240766839] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:44.370]  [00:09:25.708][info  ][EM] >>> [E:29148i S:14009 M:31550210 (Ack:240766839)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:44.429]  [00:09:25.768][info  ][EM] <<< [E:29148i S:14009 M:240766840 (Ack:31550210)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:44.429]  [00:09:25.769][info  ][EM] ??1 [E:29148i S:14009 M:240766840] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:45.358]  [00:09:26.692][info  ][EM] >>> [E:29148i S:14009 M:31550211 (Ack:240766840)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:45.493]  [00:09:26.826][info  ][EM] <<< [E:29148i S:14009 M:240766841 (Ack:31550211)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:45.493]  [00:09:26.827][info  ][EM] ??1 [E:29148i S:14009 M:240766841] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5332ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:45.493]  [00:09:26.828][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:46.159]  [00:09:27.500][info  ][EM] >>> [E:29148i S:14009 M:31550212 (Ack:240766841)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:46.225]  [00:09:27.560][info  ][EM] <<< [E:29148i S:14009 M:240766842 (Ack:31550212)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:46.225]  [00:09:27.560][info  ][EM] ??1 [E:29148i S:14009 M:240766842] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:46.947]  [00:09:28.286][info  ][EM] >>> [E:29148i S:14009 M:31550213 (Ack:240766842)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:47.006]  [00:09:28.345][info  ][EM] <<< [E:29148i S:14009 M:240766843 (Ack:31550213)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:47.006]  [00:09:28.346][info  ][EM] ??1 [E:29148i S:14009 M:240766843] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5465ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:47.965]  [00:09:29.298][info  ][EM] >>> [E:29148i S:14009 M:31550214 (Ack:240766843)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:48.016]  [00:09:29.359][info  ][EM] <<< [E:29148i S:14009 M:240766844 (Ack:31550214)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:48.027]  [00:09:29.360][info  ][EM] ??1 [E:29148i S:14009 M:240766844] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:48.760]  [00:09:30.089][info  ][EM] >>> [E:29148i S:14009 M:31550215 (Ack:240766844)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:48.885]  [00:09:30.223][info  ][EM] <<< [E:29148i S:14009 M:240766845 (Ack:31550215)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:48.885]  [00:09:30.224][info  ][EM] ??1 [E:29148i S:14009 M:240766845] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:48.898]  [00:09:30.224][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:12:49.565]  [00:09:30.896][info  ][EM] >>> [E:29148i S:14009 M:31550216 (Ack:240766845)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:49.624]  [00:09:30.956][info  ][EM] <<< [E:29148i S:14009 M:240766846 (Ack:31550216)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:49.624]  [00:09:30.957][info  ][EM] ??1 [E:29148i S:14009 M:240766846] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:50.832]  [00:09:32.170][info  ][EM] >>> [E:29148i S:14009 M:31550217 (Ack:240766846)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:50.889]  [00:09:32.231][info  ][EM] <<< [E:29148i S:14009 M:240766847 (Ack:31550217)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:50.889]  [00:09:32.232][info  ][EM] ??1 [E:29148i S:14009 M:240766847] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5540ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:51.724]  [00:09:33.057][info  ][EM] >>> [E:29148i S:14009 M:31550218 (Ack:240766847)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:51.780]  [00:09:33.118][info  ][EM] <<< [E:29148i S:14009 M:240766848 (Ack:31550218)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:51.780]  [00:09:33.119][info  ][EM] ??1 [E:29148i S:14009 M:240766848] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:52.486]  [00:09:33.821][info  ][EM] >>> [E:29148i S:14009 M:31550219 (Ack:240766848)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:52.615]  [00:09:33.955][info  ][EM] <<< [E:29148i S:14009 M:240766849 (Ack:31550219)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:52.615]  [00:09:33.956][info  ][EM] ??1 [E:29148i S:14009 M:240766849] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:52.627]  [00:09:33.956][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:53.254]  [00:09:34.596][info  ][EM] >>> [E:29148i S:14009 M:31550220 (Ack:240766849)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:53.314]  [00:09:34.656][info  ][EM] <<< [E:29148i S:14009 M:240766850 (Ack:31550220)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:53.314]  [00:09:34.657][info  ][EM] ??1 [E:29148i S:14009 M:240766850] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:54.249]  [00:09:35.585][info  ][EM] >>> [E:29148i S:14009 M:31550221 (Ack:240766850)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:54.305]  [00:09:35.645][info  ][EM] <<< [E:29148i S:14009 M:240766851 (Ack:31550221)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:54.305]  [00:09:35.646][info  ][EM] ??1 [E:29148i S:14009 M:240766851] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:55.246]  [00:09:36.581][info  ][EM] >>> [E:29148i S:14009 M:31550222 (Ack:240766851)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:55.309]  [00:09:36.641][info  ][EM] <<< [E:29148i S:14009 M:240766852 (Ack:31550222)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:55.309]  [00:09:36.642][info  ][EM] ??1 [E:29148i S:14009 M:240766852] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:56.025]  [00:09:37.359][info  ][EM] >>> [E:29148i S:14009 M:31550223 (Ack:240766852)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:56.151]  [00:09:37.493][info  ][EM] <<< [E:29148i S:14009 M:240766853 (Ack:31550223)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:56.151]  [00:09:37.494][info  ][EM] ??1 [E:29148i S:14009 M:240766853] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:56.164]  [00:09:37.494][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:12:56.779]  [00:09:38.112][info  ][EM] >>> [E:29148i S:14009 M:31550224 (Ack:240766853)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:56.836]  [00:09:38.172][info  ][EM] <<< [E:29148i S:14009 M:240766854 (Ack:31550224)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:56.836]  [00:09:38.173][info  ][EM] ??1 [E:29148i S:14009 M:240766854] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5669ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:57.704]  [00:09:39.043][info  ][EM] >>> [E:29148i S:14009 M:31550225 (Ack:240766854)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:57.769]  [00:09:39.104][info  ][EM] <<< [E:29148i S:14009 M:240766855 (Ack:31550225)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:57.769]  [00:09:39.104][info  ][EM] ??1 [E:29148i S:14009 M:240766855] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:58.501]  [00:09:39.836][info  ][EM] >>> [E:29148i S:14009 M:31550226 (Ack:240766855)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:58.554]  [00:09:39.897][info  ][EM] <<< [E:29148i S:14009 M:240766856 (Ack:31550226)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:58.565]  [00:09:39.897][info  ][EM] ??1 [E:29148i S:14009 M:240766856] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:59.593]  [00:09:40.926][info  ][EM] >>> [E:29148i S:14009 M:31550227 (Ack:240766856)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:12:59.719]  [00:09:41.060][info  ][EM] <<< [E:29148i S:14009 M:240766857 (Ack:31550227)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:12:59.719]  [00:09:41.061][info  ][EM] ??1 [E:29148i S:14009 M:240766857] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5555ms from now [State:Active II:500 AI:2000 AT:4000]
[19:12:59.730]  [00:09:41.061][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:13:00.364]  [00:09:41.695][info  ][EM] >>> [E:29148i S:14009 M:31550228 (Ack:240766857)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:00.414]  [00:09:41.755][info  ][EM] <<< [E:29148i S:14009 M:240766858 (Ack:31550228)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:00.414]  [00:09:41.756][info  ][EM] ??1 [E:29148i S:14009 M:240766858] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5471ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:01.242]  [00:09:42.583][info  ][EM] >>> [E:29148i S:14009 M:31550229 (Ack:240766858)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:01.300]  [00:09:42.642][info  ][EM] <<< [E:29148i S:14009 M:240766859 (Ack:31550229)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:01.314]  [00:09:42.643][info  ][EM] ??1 [E:29148i S:14009 M:240766859] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:02.148]  [00:09:43.486][info  ][EM] >>> [E:29148i S:14009 M:31550230 (Ack:240766859)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:02.214]  [00:09:43.546][info  ][EM] <<< [E:29148i S:14009 M:240766860 (Ack:31550230)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:02.214]  [00:09:43.547][info  ][EM] ??1 [E:29148i S:14009 M:240766860] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:03.006]  [00:09:44.342][info  ][EM] >>> [E:29148i S:14009 M:31550231 (Ack:240766860)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:03.143]  [00:09:44.476][info  ][EM] <<< [E:29148i S:14009 M:240766861 (Ack:31550231)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:03.143]  [00:09:44.476][info  ][EM] ??1 [E:29148i S:14009 M:240766861] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5691ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:03.143]  [00:09:44.477][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:04.341]  [00:09:45.675][info  ][EM] >>> [E:29148i S:14009 M:31550232 (Ack:240766861)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:04.395]  [00:09:45.736][info  ][EM] <<< [E:29148i S:14009 M:240766862 (Ack:31550232)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:04.395]  [00:09:45.736][info  ][EM] ??1 [E:29148i S:14009 M:240766862] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:05.132]  [00:09:46.470][info  ][EM] >>> [E:29148i S:14009 M:31550233 (Ack:240766862)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:05.194]  [00:09:46.530][info  ][EM] <<< [E:29148i S:14009 M:240766863 (Ack:31550233)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:05.194]  [00:09:46.531][info  ][EM] ??1 [E:29148i S:14009 M:240766863] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5280ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:05.893]  [00:09:47.226][info  ][EM] >>> [E:29148i S:14009 M:31550234 (Ack:240766863)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:05.949]  [00:09:47.287][info  ][EM] <<< [E:29148i S:14009 M:240766864 (Ack:31550234)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:05.949]  [00:09:47.288][info  ][EM] ??1 [E:29148i S:14009 M:240766864] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:07.089]  [00:09:48.428][info  ][EM] >>> [E:29148i S:14009 M:31550235 (Ack:240766864)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:07.226]  [00:09:48.562][info  ][EM] <<< [E:29148i S:14009 M:240766865 (Ack:31550235)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:07.226]  [00:09:48.562][info  ][EM] ??1 [E:29148i S:14009 M:240766865] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5749ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:07.226]  [00:09:48.563][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:08.494]  [00:09:49.835][info  ][EM] >>> [E:29148i S:14009 M:31550236 (Ack:240766865)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:08.563]  [00:09:49.895][info  ][EM] <<< [E:29148i S:14009 M:240766866 (Ack:31550236)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:08.563]  [00:09:49.896][info  ][EM] ??1 [E:29148i S:14009 M:240766866] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5304ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:09.728]  [00:09:51.067][info  ][EM] >>> [E:29148i S:14009 M:31550237 (Ack:240766866)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:09.790]  [00:09:51.127][info  ][EM] <<< [E:29148i S:14009 M:240766867 (Ack:31550237)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:09.790]  [00:09:51.128][info  ][EM] ??1 [E:29148i S:14009 M:240766867] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:10.497]  [00:09:51.837][info  ][EM] >>> [E:29148i S:14009 M:31550238 (Ack:240766867)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:10.562]  [00:09:51.897][info  ][EM] <<< [E:29148i S:14009 M:240766868 (Ack:31550238)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:10.562]  [00:09:51.898][info  ][EM] ??1 [E:29148i S:14009 M:240766868] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:11.298]  [00:09:52.632][info  ][EM] >>> [E:29148i S:14009 M:31550239 (Ack:240766868)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:11.430]  [00:09:52.766][info  ][EM] <<< [E:29148i S:14009 M:240766869 (Ack:31550239)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:11.430]  [00:09:52.767][info  ][EM] ??1 [E:29148i S:14009 M:240766869] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:11.430]  [00:09:52.767][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:12.418]  [00:09:53.750][info  ][EM] >>> [E:29148i S:14009 M:31550240 (Ack:240766869)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:12.467]  [00:09:53.810][info  ][EM] <<< [E:29148i S:14009 M:240766870 (Ack:31550240)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:12.478]  [00:09:53.811][info  ][EM] ??1 [E:29148i S:14009 M:240766870] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:13.402]  [00:09:54.746][info  ][EM] >>> [E:29148i S:14009 M:31550241 (Ack:240766870)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:13.473]  [00:09:54.805][info  ][EM] <<< [E:29148i S:14009 M:240766871 (Ack:31550241)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:13.473]  [00:09:54.806][info  ][EM] ??1 [E:29148i S:14009 M:240766871] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:14.695]  [00:09:56.035][info  ][EM] >>> [E:29148i S:14009 M:31550242 (Ack:240766871)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:14.760]  [00:09:56.095][info  ][EM] <<< [E:29148i S:14009 M:240766872 (Ack:31550242)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:14.760]  [00:09:56.096][info  ][EM] ??1 [E:29148i S:14009 M:240766872] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:15.491]  [00:09:56.833][info  ][EM] >>> [E:29148i S:14009 M:31550243 (Ack:240766872)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:15.625]  [00:09:56.967][info  ][EM] <<< [E:29148i S:14009 M:240766873 (Ack:31550243)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:15.636]  [00:09:56.968][info  ][EM] ??1 [E:29148i S:14009 M:240766873] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:15.636]  [00:09:56.968][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:13:16.401]  [00:09:57.742][info  ][EM] >>> [E:29148i S:14009 M:31550244 (Ack:240766873)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:16.460]  [00:09:57.802][info  ][EM] <<< [E:29148i S:14009 M:240766874 (Ack:31550244)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:16.475]  [00:09:57.803][info  ][EM] ??1 [E:29148i S:14009 M:240766874] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:17.191]  [00:09:58.528][info  ][EM] >>> [E:29148i S:14009 M:31550245 (Ack:240766874)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:17.253]  [00:09:58.588][info  ][EM] <<< [E:29148i S:14009 M:240766875 (Ack:31550245)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:17.253]  [00:09:58.589][info  ][EM] ??1 [E:29148i S:14009 M:240766875] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:18.157]  [00:09:59.498][info  ][EM] >>> [E:29148i S:14009 M:31550246 (Ack:240766875)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:18.223]  [00:09:59.557][info  ][EM] <<< [E:29148i S:14009 M:240766876 (Ack:31550246)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:18.223]  [00:09:59.558][info  ][EM] ??1 [E:29148i S:14009 M:240766876] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:19.298]  [00:10:00.636][info  ][EM] >>> [E:29148i S:14009 M:31550247 (Ack:240766876)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:19.433]  [00:10:00.767][info  ][EM] <<< [E:29148i S:14009 M:240766877 (Ack:31550247)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:19.433]  [00:10:00.768][info  ][EM] ??1 [E:29148i S:14009 M:240766877] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:19.433]  [00:10:00.769][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:13:20.317]  [00:10:01.651][info  ][EM] >>> [E:29148i S:14009 M:31550248 (Ack:240766877)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:20.378]  [00:10:01.711][info  ][EM] <<< [E:29148i S:14009 M:240766878 (Ack:31550248)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:20.378]  [00:10:01.711][info  ][EM] ??1 [E:29148i S:14009 M:240766878] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5540ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:21.437]  [00:10:02.772][info  ][EM] >>> [E:29148i S:14009 M:31550249 (Ack:240766878)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:21.490]  [00:10:02.833][info  ][EM] <<< [E:29148i S:14009 M:240766879 (Ack:31550249)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:21.503]  [00:10:02.833][info  ][EM] ??1 [E:29148i S:14009 M:240766879] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:22.351]  [00:10:03.692][info  ][EM] >>> [E:29148i S:14009 M:31550250 (Ack:240766879)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:22.412]  [00:10:03.752][info  ][EM] <<< [E:29148i S:14009 M:240766880 (Ack:31550250)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:22.412]  [00:10:03.753][info  ][EM] ??1 [E:29148i S:14009 M:240766880] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:23.333]  [00:10:04.668][info  ][EM] >>> [E:29148i S:14009 M:31550251 (Ack:240766880)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:23.467]  [00:10:04.802][info  ][EM] <<< [E:29148i S:14009 M:240766881 (Ack:31550251)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:23.467]  [00:10:04.803][info  ][EM] ??1 [E:29148i S:14009 M:240766881] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:23.467]  [00:10:04.803][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:24.506]  [00:10:05.846][info  ][EM] >>> [E:29148i S:14009 M:31550252 (Ack:240766881)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:24.568]  [00:10:05.906][info  ][EM] <<< [E:29148i S:14009 M:240766882 (Ack:31550252)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:24.568]  [00:10:05.907][info  ][EM] ??1 [E:29148i S:14009 M:240766882] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:25.723]  [00:10:07.058][info  ][EM] >>> [E:29148i S:14009 M:31550253 (Ack:240766882)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:25.783]  [00:10:07.119][info  ][EM] <<< [E:29148i S:14009 M:240766883 (Ack:31550253)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:25.783]  [00:10:07.120][info  ][EM] ??1 [E:29148i S:14009 M:240766883] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5691ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:26.487]  [00:10:07.819][info  ][EM] >>> [E:29148i S:14009 M:31550254 (Ack:240766883)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:26.539]  [00:10:07.878][info  ][EM] <<< [E:29148i S:14009 M:240766884 (Ack:31550254)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:26.539]  [00:10:07.879][info  ][EM] ??1 [E:29148i S:14009 M:240766884] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5418ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:27.466]  [00:10:08.802][info  ][EM] >>> [E:29148i S:14009 M:31550255 (Ack:240766884)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:27.596]  [00:10:08.936][info  ][EM] <<< [E:29148i S:14009 M:240766885 (Ack:31550255)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:27.596]  [00:10:08.937][info  ][EM] ??1 [E:29148i S:14009 M:240766885] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5643ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:27.607]  [00:10:08.938][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:28.853]  [00:10:10.196][info  ][EM] >>> [E:29148i S:14009 M:31550256 (Ack:240766885)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:28.915]  [00:10:10.255][info  ][EM] <<< [E:29148i S:14009 M:240766886 (Ack:31550256)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:28.915]  [00:10:10.256][info  ][EM] ??1 [E:29148i S:14009 M:240766886] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5495ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:29.964]  [00:10:11.301][info  ][EM] >>> [E:29148i S:14009 M:31550257 (Ack:240766886)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:30.035]  [00:10:11.362][info  ][EM] <<< [E:29148i S:14009 M:240766887 (Ack:31550257)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:30.035]  [00:10:11.363][info  ][EM] ??1 [E:29148i S:14009 M:240766887] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:31.687]  [00:10:13.020][info  ][EM] >>> [E:29148i S:14009 M:31550258 (Ack:240766887)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:31.740]  [00:10:13.081][info  ][EM] <<< [E:29148i S:14009 M:240766888 (Ack:31550258)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:31.740]  [00:10:13.082][info  ][EM] ??1 [E:29148i S:14009 M:240766888] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:32.484]  [00:10:13.824][info  ][EM] >>> [E:29148i S:14009 M:31550259 (Ack:240766888)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:32.615]  [00:10:13.958][info  ][EM] <<< [E:29148i S:14009 M:240766889 (Ack:31550259)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:32.628]  [00:10:13.958][info  ][EM] ??1 [E:29148i S:14009 M:240766889] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5544ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:32.628]  [00:10:13.959][error ][DL] Long dispatch time: 134 ms, for event type 2
[19:13:33.411]  [00:10:14.750][info  ][EM] >>> [E:29148i S:14009 M:31550260 (Ack:240766889)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:33.469]  [00:10:14.811][info  ][EM] <<< [E:29148i S:14009 M:240766890 (Ack:31550260)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:33.469]  [00:10:14.811][info  ][EM] ??1 [E:29148i S:14009 M:240766890] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:34.198]  [00:10:15.539][info  ][EM] >>> [E:29148i S:14009 M:31550261 (Ack:240766890)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:34.259]  [00:10:15.598][info  ][EM] <<< [E:29148i S:14009 M:240766891 (Ack:31550261)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:34.259]  [00:10:15.599][info  ][EM] ??1 [E:29148i S:14009 M:240766891] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:35.111]  [00:10:16.454][info  ][EM] >>> [E:29148i S:14009 M:31550262 (Ack:240766891)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:35.182]  [00:10:16.514][info  ][EM] <<< [E:29148i S:14009 M:240766892 (Ack:31550262)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:35.182]  [00:10:16.515][info  ][EM] ??1 [E:29148i S:14009 M:240766892] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:35.894]  [00:10:17.235][info  ][EM] >>> [E:29148i S:14009 M:31550263 (Ack:240766892)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:36.029]  [00:10:17.369][info  ][EM] <<< [E:29148i S:14009 M:240766893 (Ack:31550263)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:36.029]  [00:10:17.370][info  ][EM] ??1 [E:29148i S:14009 M:240766893] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:36.044]  [00:10:17.370][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:36.817]  [00:10:18.150][info  ][EM] >>> [E:29148i S:14009 M:31550264 (Ack:240766893)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:36.868]  [00:10:18.210][info  ][EM] <<< [E:29148i S:14009 M:240766894 (Ack:31550264)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:36.881]  [00:10:18.211][info  ][EM] ??1 [E:29148i S:14009 M:240766894] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5473ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:37.595]  [00:10:18.937][info  ][EM] >>> [E:29148i S:14009 M:31550265 (Ack:240766894)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:37.667]  [00:10:18.998][info  ][EM] <<< [E:29148i S:14009 M:240766895 (Ack:31550265)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:37.667]  [00:10:18.999][info  ][EM] ??1 [E:29148i S:14009 M:240766895] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:38.485]  [00:10:19.827][info  ][EM] >>> [E:29148i S:14009 M:31550266 (Ack:240766895)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:38.550]  [00:10:19.887][info  ][EM] <<< [E:29148i S:14009 M:240766896 (Ack:31550266)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:38.550]  [00:10:19.888][info  ][EM] ??1 [E:29148i S:14009 M:240766896] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:39.586]  [00:10:20.926][info  ][EM] >>> [E:29148i S:14009 M:31550267 (Ack:240766896)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:39.724]  [00:10:21.058][info  ][EM] <<< [E:29148i S:14009 M:240766897 (Ack:31550267)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:39.724]  [00:10:21.059][info  ][EM] ??1 [E:29148i S:14009 M:240766897] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:39.724]  [00:10:21.059][error ][DL] Long dispatch time: 133 ms, for event type 2
[19:13:40.407]  [00:10:21.745][info  ][EM] >>> [E:29148i S:14009 M:31550268 (Ack:240766897)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:40.467]  [00:10:21.805][info  ][EM] <<< [E:29148i S:14009 M:240766898 (Ack:31550268)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:40.467]  [00:10:21.805][info  ][EM] ??1 [E:29148i S:14009 M:240766898] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:41.324]  [00:10:22.664][info  ][EM] >>> [E:29148i S:14009 M:31550269 (Ack:240766898)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:41.382]  [00:10:22.724][info  ][EM] <<< [E:29148i S:14009 M:240766899 (Ack:31550269)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:41.393]  [00:10:22.725][info  ][EM] ??1 [E:29148i S:14009 M:240766899] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:42.128]  [00:10:23.468][info  ][EM] >>> [E:29148i S:14009 M:31550270 (Ack:240766899)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:42.189]  [00:10:23.529][info  ][EM] <<< [E:29148i S:14009 M:240766900 (Ack:31550270)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:42.189]  [00:10:23.530][info  ][EM] ??1 [E:29148i S:14009 M:240766900] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:43.024]  [00:10:24.363][info  ][EM] >>> [E:29148i S:14009 M:31550271 (Ack:240766900)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:43.161]  [00:10:24.498][info  ][EM] <<< [E:29148i S:14009 M:240766901 (Ack:31550271)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:43.161]  [00:10:24.498][info  ][EM] ??1 [E:29148i S:14009 M:240766901] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:43.161]  [00:10:24.499][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:43.946]  [00:10:25.280][info  ][EM] >>> [E:29148i S:14009 M:31550272 (Ack:240766901)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:43.999]  [00:10:25.339][info  ][EM] <<< [E:29148i S:14009 M:240766902 (Ack:31550272)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:43.999]  [00:10:25.340][info  ][EM] ??1 [E:29148i S:14009 M:240766902] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:44.860]  [00:10:26.200][info  ][EM] >>> [E:29148i S:14009 M:31550273 (Ack:240766902)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:44.923]  [00:10:26.260][info  ][EM] <<< [E:29148i S:14009 M:240766903 (Ack:31550273)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:44.923]  [00:10:26.260][info  ][EM] ??1 [E:29148i S:14009 M:240766903] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:45.620]  [00:10:26.962][info  ][EM] >>> [E:29148i S:14009 M:31550274 (Ack:240766903)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:45.690]  [00:10:27.023][info  ][EM] <<< [E:29148i S:14009 M:240766904 (Ack:31550274)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:45.690]  [00:10:27.024][info  ][EM] ??1 [E:29148i S:14009 M:240766904] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5738ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:46.416]  [00:10:27.756][info  ][EM] >>> [E:29148i S:14009 M:31550275 (Ack:240766904)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:46.556]  [00:10:27.890][info  ][EM] <<< [E:29148i S:14009 M:240766905 (Ack:31550275)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:46.556]  [00:10:27.891][info  ][EM] ??1 [E:29148i S:14009 M:240766905] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:46.556]  [00:10:27.891][error ][DL] Long dispatch time: 135 ms, for event type 2
[19:13:47.193]  [00:10:28.532][info  ][EM] >>> [E:29148i S:14009 M:31550276 (Ack:240766905)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:47.253]  [00:10:28.592][info  ][EM] <<< [E:29148i S:14009 M:240766906 (Ack:31550276)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:47.253]  [00:10:28.592][info  ][EM] ??1 [E:29148i S:14009 M:240766906] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5428ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:48.090]  [00:10:29.425][info  ][EM] >>> [E:29148i S:14009 M:31550277 (Ack:240766906)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:48.148]  [00:10:29.485][info  ][EM] <<< [E:29148i S:14009 M:240766907 (Ack:31550277)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:48.148]  [00:10:29.486][info  ][EM] ??1 [E:29148i S:14009 M:240766907] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:48.890]  [00:10:30.228][info  ][EM] >>> [E:29148i S:14009 M:31550278 (Ack:240766907)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[19:13:48.952]  [00:10:30.288][info  ][EM] <<< [E:29148i S:14009 M:240766908 (Ack:31550278)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[19:13:48.952]  [00:10:30.289][info  ][EM] ??1 [E:29148i S:14009 M:240766908] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:49.562]  [00:10:30.901][info  ][EM] >>> [E:29148i S:14009 M:31550279 (Ack:240766908)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0002:12 (BDX:BlockEOF) (B:635)
[19:13:49.562]  [00:10:30.903][info  ][EM] <<< [E:29148i S:14009 M:240766909 (Ack:31550279)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:14 (BDX:BlockAckEOF) (B:38)
[19:13:49.562]  [00:10:30.904][info  ][EM] ??1 [E:29148i S:14009 M:240766909] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5673ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:49.575]  [00:10:30.907][info  ][DIS] Found an existing secure session to [1:0000000000000001]!
[19:13:49.575]  [00:10:30.910][info  ][EM] <<< [E:29149i S:14009 M:240766910] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:97)
[19:13:49.575]  [00:10:30.911][info  ][EM] ??1 [E:29149i S:14009 M:240766910] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[19:13:49.689]  [00:10:31.021][error ][DL] Long dispatch time: 110 ms, for event type 2
[19:13:49.689]  [00:10:31.025][info  ][SWU] OTA image downloaded successfully
[19:13:50.034]  [00:10:31.371][info  ][EM] >>> [E:29148i S:14009 M:31550280 (Ack:240766909)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[19:13:50.096]  [00:10:31.427][info  ][EM] >>> [E:29149i S:14009 M:31550281 (Ack:240766910)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[19:13:50.096]  [00:10:31.428][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0003
[19:13:50.096]  [00:10:31.430][info  ][EM] <<< [E:29149i S:14009 M:240766911 (Ack:31550281)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[19:13:50.096]  [00:10:31.431][info  ][SWU] HandleApply: verifying image
[19:14:02.982]  [00:10:44.318][info  ][SWU] Image verified, Set image to bootload
[19:14:02.982]  [00:10:44.319][info \00> 
[19:15:07.729]  [00:00:00.068][info  ][DL] Starting scheduler
[19:15:07.729]  [00:00:00.068][info  ][DL] ==================================================
[19:15:07.729]  [00:00:00.068][info  ][DL]  starting
[19:15:07.729]  [00:00:00.068][info  ][DL] ==================================================
[19:15:07.729]  [00:00:00.069][info  ][DL] Init CHIP Stack
[19:15:07.729]  [00:00:00.070][info  ][DL] Provision mode disabled
[19:15:07.729]  [00:00:00.070][info  ][DL] Initializing OpenThread stack
[19:15:07.740]  [00:00:00.072][info  ][DL] OpenThread ifconfig up and thread start
[19:15:07.740]  [00:00:00.072][info  ][DL] OpenThread started: OK
[19:15:07.740]  [00:00:00.107][info  ][DL] Bluetooth stack booted: v11.0.0-b0
[19:15:07.740]  [00:00:00.107][info  ][DL] RAIL version:, v3.0.0-b0
[19:15:07.740]  [00:00:00.110][info  ][SVR] Current Software Version String: 0.0.2
[19:15:07.740]  [00:00:00.110][info  ][SVR] Current Software Version: 2
[19:15:07.740]  [00:00:00.112][info  ][DL] Device Configuration:
[19:15:07.740]  [00:00:00.114][info  ][DL]   Serial Number: 0C1777D69F5694F8
[19:15:07.740]  [00:00:00.115][info  ][DL]   Vendor Id: 5274 (0x149A)
[19:15:07.751]  [00:00:00.115][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[19:15:07.751]  [00:00:00.118][info  ][DL]   Product Id: 12821 (0x3215)
[19:15:07.751]  [00:00:00.118][info  ][DL]   Product Name: Curtain Controller
[19:15:07.751]  [00:00:00.118][info  ][DL]   Hardware Version: 1
[19:15:07.751]  [00:00:00.118][info  ][DL]   Setup Pin Code (0 for UNKNOWN/ERROR): 0
[19:15:07.751]  [00:00:00.119][info  ][DL]   Setup Discriminator (0xFFFF for UNKNOWN/ERROR): 1884 (0x75C)
[19:15:07.751]  [00:00:00.119][info  ][DL]   Manufacturing Date: (not set)
[19:15:07.751]  [00:00:00.119][info  ][DL]   Device Type: 65535 (0xFFFF)
[19:15:07.751]  [00:00:00.120][info  ][SVR] SetupQRCode: [MT:GYFB5KY61495TG11V10]
[19:15:07.751]  [00:00:00.120][info  ][SVR] Copy/paste the below URL in a browser to see the QR Code:
[19:15:07.751]  [00:00:00.120][info  ][SVR] https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AGYFB5KY61495TG11V10
[19:15:07.751]  [00:00:00.121][silabs ]Ver: 2 Btl: 0x03000003 Time:Mar 11 2026 17:09:25
[19:15:07.762]  [00:00:00.121][silabs ]Reset Reason: 0x00000000
[19:15:07.762]  [00:00:00.121][silabs ]SetupQRCode: [MT:GYFB5KY61495TG11V10]
[19:15:07.762]  [00:00:00.122][silabs ]COM: Init done
[19:15:07.762]  [00:00:00.123][silabs ]NWK: device has provisioned
[19:15:07.762]  [00:00:00.123][silabs ]COM: notify network [Leave]
[19:15:07.762]  [00:00:00.123][silabs ]CLS: register device: dev 0x2002a706 endpoint 1 type 0 idx 1
[19:15:07.762]  [00:00:00.125][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[19:15:07.762]  [00:00:00.125][silabs ]CLS: skip cls: 0x0000_0102 attr: 0x0000_0007
[19:15:07.762]  [00:00:00.125][silabs ]App Task started
[19:15:07.762]  matterCli> [00:00:00.353][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[19:15:07.989]  [00:00:00.353][info  ][ZCL] ThreadDiagnosticsDelegate: OnConnectionStatusChanged
[19:15:07.989]  [00:00:00.354][silabs ]NWK: platform event type 32779
[19:15:07.989]  [00:00:00.355][info  ][DL] _OnPlatformEvent default:  event->Type = 32769
[19:15:07.989]  [00:00:00.355][silabs ]NWK: kThreadConnectivityChange,32769
[19:15:07.989]  [00:00:00.355][silabs ]NWK: Thread Established
[19:15:07.989]  [00:00:00.355][silabs ]COM: notify network [Joined]
[19:15:07.989]  [00:00:00.356][info  ][SVR] Scheduling OTA Requestor initialization
[19:15:07.989]  [00:00:00.356][info  ][SVR] Joining Multicast groups
[19:15:08.146]  [00:00:00.513][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[19:15:08.146]  [00:00:00.514][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[19:15:08.146]  [00:00:00.514][silabs ]NWK: platform event type 32779
[19:15:08.146]  [00:00:00.515][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[19:15:08.163]  [00:00:00.515][silabs ]NWK: platform event type 32779
[19:15:08.232]  [00:00:00.594][error ][IN] Data received on an unknown session (LSID=14009). Dropping it!
[19:15:08.256]  [00:00:00.629][error ][IN] Data received on an unknown session (LSID=14009). Dropping it!
[19:15:08.347]  [00:00:00.718][error ][IN] Data received on an unknown session (LSID=14009). Dropping it!
[19:15:08.736]  [00:00:01.098][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[19:15:08.736]  [00:00:01.098][silabs ]NWK: platform event type 32786
[19:15:08.736]  [00:00:01.098][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[19:15:08.736]  [00:00:01.098][info  ][SVR] Server initialization complete
[19:15:08.736]  [00:00:01.099][info  ][DIS] Updating services using commissioning mode 0
[19:15:08.736]  [00:00:01.099][info  ][DIS] Advertise operational node 5985E29CD6F3E9EB-00000000000008CA
[19:15:08.736]  [00:00:01.100][info  ][DL] advertising srp service: 5985E29CD6F3E9EB-00000000000008CA._matter._tcp
[19:15:08.736]  [00:00:01.100][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[19:15:08.736]  [00:00:01.100][silabs ]NWK: platform event type 32790
[19:15:08.747]  [00:00:01.111][info  ][IM] No subscriptions to resume
[19:15:11.737]  [00:00:04.101][info  ][DIS] Resolving 5985E29CD6F3E9EB:0000000000000001 ...
[19:15:11.737]  [00:00:04.102][info  ][DIS] Lookup started for 5985E29CD6F3E9EB-0000000000000001
[19:15:11.920]  [00:00:04.294][info  ][DIS] Node ID resolved for 5985E29CD6F3E9EB-0000000000000001
[19:15:11.920]  [00:00:04.295][info  ][DIS] UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540: new best score: 3 (for 5985E29CD6F3E9EB-0000000000000001)
[19:15:11.933]  [00:00:04.295][info  ][DIS] Checking node lookup status for 5985E29CD6F3E9EB-0000000000000001 after 194 ms
[19:15:11.933]  [00:00:04.295][info  ][DIS] Keeping DNSSD lookup active
[19:15:11.933]  [00:00:04.301][info  ][DIS] Checking node lookup status for 5985E29CD6F3E9EB-0000000000000001 after 200 ms
[19:15:11.933]  [00:00:04.302][info  ][SC] Initiating session on local FabricIndex 1 from 0x00000000000008CA -> 0x0000000000000001
[19:15:11.947]  [00:00:04.321][info  ][EM] <<< [E:13355i S:0 M:160167513] (U) Msg TX from 0CEFBA9386199E27 to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:233)
[19:15:11.958]  [00:00:04.322][info  ][EM] ??1 [E:13355i S:0 M:160167513] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3642ms from now [State:Idle II:500 AI:2000 AT:4000]
[19:15:11.958]  [00:00:04.322][info  ][SC] Sent Sigma1 msg to <0000000000000001, 1> [II:3000ms AI:2500ms AT:0ms]
[19:15:12.447]  [00:00:04.813][info  ][EM] >>> [E:13355i S:0 M:262024125 (Ack:160167513)] (U) Msg RX from 0:0000000000000000 [0000] to 0CEFBA9386199E27 --- Type 0000:33 (SecureChannel:CASE_Sigma2Resume) (B:100)
[19:15:12.447]  [00:00:04.814][info  ][EM] <<< [E:13355i S:0 M:160167514 (Ack:262024125)] (U) Msg TX from 0CEFBA9386199E27 to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:15:12.447]  [00:00:04.821][info  ][EM] <<< [E:13355i S:0 M:160167515 (Ack:262024125)] (U) Msg TX from 0CEFBA9386199E27 to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[19:15:12.458]  [00:00:04.822][info  ][EM] ??1 [E:13355i S:0 M:160167515] (U) Msg Retransmission to 0:0000000000000000 scheduled for 5390ms from now [State:Active II:500 AI:2000 AT:4000]
[19:15:12.458]  [00:00:04.826][info  ][SC] SecureSession[0x20006e28, LSID:58350]: State change 'kEstablishing' --> 'kActive'
[19:15:12.458]  [00:00:04.826][info  ][SWU] Stopping the watchdog timer
[19:15:12.458]  [00:00:04.827][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[19:15:12.458]  [00:00:04.832][info  ][EM] <<< [E:13356i S:58350 M:58482518] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:97)
[19:15:12.472]  [00:00:04.832][info  ][EM] ??1 [E:13356i S:58350 M:58482518] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[19:15:12.472]  [00:00:04.833][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[19:15:12.472]  [00:00:04.833][silabs ]NWK: platform event type 32792
[19:15:12.952]  [00:00:05.316][info  ][EM] >>> [E:13355i S:0 M:262024126 (Ack:160167515)] (U) Msg RX from 0:0000000000000000 [0000] to 0CEFBA9386199E27 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[19:15:12.963]  [00:00:05.336][info  ][EM] >>> [E:13356i S:58350 M:250540467 (Ack:58482518)] (S) Msg RX from 1:0000000000000001 [E9EB] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[19:15:12.977]  [00:00:05.337][info  ][DMG] Received Command Response Status for Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0004 Status=0x0
[19:15:12.977]  [00:00:05.339][info  ][EM] <<< [E:13356i S:58350 M:58482519 (Ack:250540467)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E9EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[21:03:55.317]  [01:48:47.861][info  ][DL] SRP Client was stopped, because current server is no longer detected.
[21:03:55.317]  [01:48:47.861][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[21:03:55.317]  [01:48:47.862][silabs ]NWK: platform event type 32779
[21:03:57.574]  [01:48:50.127][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[21:03:57.574]  [01:48:50.128][silabs ]NWK: platform event type 32779
[21:04:06.998]  [01:48:59.552][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[21:04:06.998]  [01:48:59.552][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[21:04:07.009]  [01:48:59.552][silabs ]NWK: platform event type 32779
[23:59:39.072]  [04:44:31.922][info  ][DL] SRP Client was stopped, because current server is no longer detected.
[23:59:39.072]  [04:44:31.923][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:39.072]  [04:44:31.923][silabs ]NWK: platform event type 32779
[23:59:39.072]  [04:44:31.924][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:39.072]  [04:44:31.924][silabs ]NWK: platform event type 32779
[23:59:39.343]  [04:44:32.198][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:39.343]  [04:44:32.198][silabs ]NWK: platform event type 32779
[23:59:39.354]  [04:44:32.199][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:39.354]  [04:44:32.200][silabs ]NWK: platform event type 32779
[23:59:40.613]  [04:44:33.470][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:40.613]  [04:44:33.470][silabs ]NWK: platform event type 32779
[23:59:49.892]  [04:44:42.745][info  ][DL] SRP Client was started, detected server: fdf9:32b5:0229:8114:6099:a3c9:ee56:68a9
[23:59:49.892]  [04:44:42.746][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[23:59:49.892]  [04:44:42.746][silabs ]NWK: platform event type 32779
```