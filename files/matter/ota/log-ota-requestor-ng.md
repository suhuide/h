```c
[18:26:40.791]  [00:00:26.710][silabs ]NWK: Thread Established
[18:26:40.791]  [00:00:26.710][silabs ]COM: notify network [Joined]
[18:26:40.792]  [00:00:26.710][info  ][SVR] Scheduling OTA Requestor initialization
[18:26:40.792]  [00:00:26.711][info  ][SVR] Joining Multicast groups
[18:26:40.794]  [00:00:26.713][info  ][EM] <<< [E:41039r S:1630 M:118042724] (S) Msg TX from 0000000000000000 to 1:FFFFFFFB00000000 [F0EB] [BLE] --- Type 0001:09 (IM:InvokeCommandResponse) (B:65)
[18:26:40.795]  [00:00:26.714][info  ][DL] _OnPlatformEvent default:  event->Type = 32785
[18:26:40.797]  [00:00:26.714][info  ][DIS] Advertise operational node 0FCE5DA14975F0EB-00000000000008CA
[18:26:40.798]  [00:00:26.715][error ][SVR] Operational advertising failed: 3
[18:26:40.798]  [00:00:26.715][silabs ]NWK: platform event type 32785
[18:26:40.798]  [00:00:26.715][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[18:26:40.800]  [00:00:26.716][silabs ]NWK: platform event type 32779
[18:26:40.947]  [00:00:26.868][info  ][DL] Tx Confirmation received
[18:26:40.947]  [00:00:26.868][info  ][DL]  stop soft timer
[18:26:40.947]  [00:00:26.869][info  ][DL] _OnPlatformEvent kCHIPoBLEIndicateConfirm
[18:26:41.223]  [00:00:27.145][info  ][DL] _OnPlatformEvent default:  event->Type = 32786
[18:26:41.223]  [00:00:27.146][silabs ]NWK: platform event type 32786
[18:26:41.225]  [00:00:27.146][info  ][SVR] DNS-SD initialized, scheduling OTA Requestor initialization
[18:26:41.225]  [00:00:27.146][info  ][SVR] Server initialization complete
[18:26:41.226]  [00:00:27.146][info  ][DIS] Updating services using commissioning mode 0
[18:26:41.226]  [00:00:27.146][info  ][DIS] Advertise operational node 0FCE5DA14975F0EB-00000000000008CA
[18:26:41.228]  [00:00:27.147][info  ][DL] advertising srp service: 0FCE5DA14975F0EB-00000000000008CA._matter._tcp
[18:26:41.229]  [00:00:27.147][info  ][DL] _OnPlatformEvent default:  event->Type = 32790
[18:26:41.229]  [00:00:27.148][silabs ]NWK: platform event type 32790
[18:26:41.239]  [00:00:27.158][info  ][IM] No subscriptions to resume
[18:26:43.228]  [00:00:29.150][info  ][EM] >>> [E:41040r S:0 M:61323360] (U) Msg RX from 0:95101FF690DB3684 [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[18:26:43.230]  [00:00:29.151][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[18:26:43.231]  [00:00:29.151][info  ][EM] <<< [E:41040r S:0 M:156745217 (Ack:61323360)] (U) Msg TX from 0000000000000000 to 0:95101FF690DB3684 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:48131] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:26:43.236]  [00:00:29.152][info  ][SC] Received Sigma1 msg
[18:26:43.243]  [00:00:29.161][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[18:26:43.264]  [00:00:29.185][info  ][EM] <<< [E:41040r S:0 M:156745218 (Ack:61323360)] (U) Msg TX from 0000000000000000 to 0:95101FF690DB3684 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:48131] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[18:26:43.265]  [00:00:29.186][info  ][EM] ??1 [E:41040r S:0 M:156745218] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3340ms from now [State:Active II:500 AI:300 AT:4000]
[18:26:43.270]  [00:00:29.186][info  ][SC] Sent Sigma2 msg
[18:26:43.386]  [00:00:29.305][info  ][DL] Char Write Req, char : 23
[18:26:43.386]  [00:00:29.305][info  ][DL] _OnPlatformEvent kCHIPoBLEWriteReceived
[18:26:44.002]  [00:00:29.924][info  ][EM] >>> [E:41040r S:0 M:61323361 (Ack:156745218)] (U) Msg RX from 0:95101FF690DB3684 [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[18:26:44.004]  [00:00:29.925][info  ][EM] <<< [E:41040r S:0 M:156745219 (Ack:61323361)] (U) Msg TX from 0000000000000000 to 0:95101FF690DB3684 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:48131] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:26:44.010]  [00:00:29.925][info  ][SC] Received Sigma3 msg
[18:26:44.053]  [00:00:29.974][info  ][EM] <<< [E:41040r S:0 M:156745220 (Ack:61323361)] (U) Msg TX from 0000000000000000 to 0:95101FF690DB3684 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:48131] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[18:26:44.054]  [00:00:29.975][info  ][EM] ??1 [E:41040r S:0 M:156745220] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3374ms from now [State:Active II:500 AI:300 AT:4000]
[18:26:44.057]  [00:00:29.979][info  ][SC] SecureSession[0x20006d50, LSID:1629]: State change 'kEstablishing' --> 'kActive'
[18:26:44.058]  [00:00:29.979][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[18:26:44.058]  [00:00:29.980][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[18:26:44.063]  [00:00:29.980][silabs ]NWK: platform event type 32792
[18:26:44.226]  [00:00:30.147][info  ][SWU] Stopping the watchdog timer
[18:26:44.226]  [00:00:30.148][info  ][SWU] Starting the periodic query timer, timeout: 86400 seconds
[18:26:44.509]  [00:00:30.430][info  ][EM] >>> [E:41041r S:1629 M:138337965] (S) Msg RX from 1:000000000001B669 [F0EB] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[18:26:44.511]  [00:00:30.432][info  ][FS] GeneralCommissioning: Received CommissioningComplete
[18:26:44.511]  [00:00:30.433][info  ][FP] Metadata for Fabric 0x1 persisted to storage.
[18:26:44.523]  [00:00:30.444][info  ][TS] Committing Last Known Good Time to storage: 2023-10-10T16:28:52
[18:26:44.523]  [00:00:30.446][info  ][ZCL] OpCreds: Fabric index 0x1 was committed to storage. Compressed Fabric Id 0x0FCE5DA14975F0EB, FabricId 0000000000000001, NodeId 00000000000008CA, VendorId 0xFFF1
[18:26:44.526]  [00:00:30.447][info  ][FS] GeneralCommissioning: Successfully committed pending fabric data
[18:26:44.526]  [00:00:30.447][info  ][FS] Fail-safe cleanly disarmed
[18:26:44.528]  [00:00:30.449][info  ][EM] <<< [E:41041r S:1629 M:93077980 (Ack:138337965)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:48131] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[18:26:44.530]  [00:00:30.450][info  ][EM] ??1 [E:41041r S:1629 M:93077980] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3398ms from now [State:Active II:500 AI:300 AT:4000]
[18:26:44.531]  [00:00:30.450][info  ][DL] _OnPlatformEvent default:  event->Type = 32783
[18:26:44.533]  [00:00:30.451][info  ][SWU] Device commissioned, schedule a default provider query
[18:26:44.534]  [00:00:30.451][info  ][SVR] Commissioning completed successfully
[18:26:44.534]  [00:00:30.451][info  ][DIS] Updating services using commissioning mode 0
[18:26:44.535]  [00:00:30.451][info  ][DIS] Advertise operational node 0FCE5DA14975F0EB-00000000000008CA
[18:26:44.535]  [00:00:30.452][info  ][SC] SecureSession[0x20006e28, LSID:1630]: State change 'kActive' --> 'kPendingEviction'
[18:26:44.537]  [00:00:30.452][info  ][BLE] Releasing end point's BLE connection back to application.
[18:26:44.538]  [00:00:30.452][info  ][DL] Closing BLE GATT connection (con 1)
[18:26:44.538]  [00:00:30.452][silabs ]NWK: kCommissioningComplete,32783
[18:26:44.540]  [00:00:30.453][silabs ]COM: notify network [Joined]
[18:26:44.541]  [00:00:30.458][info  ][EM] >>> [E:41040r S:0 M:61323362 (Ack:156745220)] (U) Msg RX from 0:95101FF690DB3684 [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:26:44.651]  [00:00:30.573][info  ][DL] Disconnect Event for CHIPoBLE on handle : 1
[18:26:44.651]  [00:00:30.573][info  ][DL] BLE GATT connection closed (con 1, reason 4118)
[18:26:44.654]  [00:00:30.573][info  ][DL] _OnPlatformEvent kCHIPoBLEConnectionError
[18:26:45.532]  [00:00:31.454][info  ][EM] >>> [E:41041r S:1629 M:138337966 (Ack:93077980)] (S) Msg RX from 1:000000000001B669 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:27:14.532]  [00:01:00.451][error ][SWU] No suitable OTA Provider candidate found
[18:27:14.532]  [00:01:00.451][info  ][SWU] No provider available
[18:28:06.642]  [00:01:52.566][info  ][EM] >>> [E:44720r S:0 M:103119992] (U) Msg RX from 0:AAE0E5A4B5F8F66B [0000] to 0000000000000000 --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:196)
[18:28:06.643]  [00:01:52.566][info  ][IN] CASE Server received Sigma1 message . Starting handshake. EC 0x200087a8
[18:28:06.645]  [00:01:52.567][info  ][EM] <<< [E:44720r S:0 M:156745221 (Ack:103119992)] (U) Msg TX from 0000000000000000 to 0:AAE0E5A4B5F8F66B [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:47684] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:28:06.649]  [00:01:52.568][info  ][SC] Received Sigma1 msg
[18:28:06.654]  [00:01:52.577][info  ][SC] CASE matched destination ID: fabricIndex 1, NodeID 0x00000000000008CA
[18:28:06.678]  [00:01:52.601][info  ][EM] <<< [E:44720r S:0 M:156745222 (Ack:103119992)] (U) Msg TX from 0000000000000000 to 0:AAE0E5A4B5F8F66B [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:47684] --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[18:28:06.679]  [00:01:52.602][info  ][EM] ??1 [E:44720r S:0 M:156745222] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3333ms from now [State:Active II:500 AI:300 AT:4000]
[18:28:06.684]  [00:01:52.603][info  ][SC] Sent Sigma2 msg
[18:28:07.624]  [00:01:53.549][info  ][EM] >>> [E:44720r S:0 M:103119993 (Ack:156745222)] (U) Msg RX from 0:AAE0E5A4B5F8F66B [0000] to 0000000000000000 --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:598)
[18:28:07.626]  [00:01:53.549][info  ][EM] <<< [E:44720r S:0 M:156745223 (Ack:103119993)] (U) Msg TX from 0000000000000000 to 0:AAE0E5A4B5F8F66B [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:47684] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:28:07.631]  [00:01:53.550][info  ][SC] Received Sigma3 msg
[18:28:07.692]  [00:01:53.616][info  ][EM] <<< [E:44720r S:0 M:156745224 (Ack:103119993)] (U) Msg TX from 0000000000000000 to 0:AAE0E5A4B5F8F66B [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:47684] --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[18:28:07.693]  [00:01:53.617][info  ][EM] ??1 [E:44720r S:0 M:156745224] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3341ms from now [State:Active II:500 AI:300 AT:4000]
[18:28:07.696]  [00:01:53.621][info  ][SC] SecureSession[0x20006f00, LSID:1631]: State change 'kEstablishing' --> 'kActive'
[18:28:07.697]  [00:01:53.621][info  ][IN] CASE Session established to peer: <000000000001B669, 1>
[18:28:07.697]  [00:01:53.622][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[18:28:07.700]  [00:01:53.622][silabs ]NWK: platform event type 32792
[18:28:08.250]  [00:01:54.174][info  ][EM] >>> [E:44721r S:1631 M:62718677] (S) Msg RX from 1:000000000001B669 [F0EB] to 00000000000008CA --- Type 0001:08 (IM:InvokeCommandRequest) (B:71)
[18:28:08.253]  [00:01:54.176][info  ][SWU] OTA Requestor received AnnounceOTAProvider
[18:28:08.253]  [00:01:54.178][info  ][EM] <<< [E:44721r S:1631 M:95435557 (Ack:62718677)] (S) Msg TX from 00000000000008CA to 1:000000000001B669 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:47684] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[18:28:08.255]  [00:01:54.179][info  ][EM] ??1 [E:44721r S:1631 M:95435557] (S) Msg Retransmission to 1:000000000001B669 scheduled for 3374ms from now [State:Active II:500 AI:300 AT:4000]
[18:28:08.258]  [00:01:54.180][info  ][SWU] Stopping the Periodic Query timer
[18:28:08.258]  [00:01:54.180][info  ][SWU] Starting the watchdog timer, timeout: 21600 seconds
[18:28:08.259]  [00:01:54.180][info  ][DIS] Resolving 0FCE5DA14975F0EB:0000000000000001 ...
[18:28:08.259]  [00:01:54.181][info  ][DIS] Lookup started for 0FCE5DA14975F0EB-0000000000000001
[18:28:08.267]  [00:01:54.192][info  ][EM] >>> [E:44720r S:0 M:103119994 (Ack:156745224)] (U) Msg RX from 0:AAE0E5A4B5F8F66B [0000] to 0000000000000000 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:28:08.323]  [00:01:54.248][info  ][EM] >>> [E:44721r S:1631 M:62718678 (Ack:95435557)] (S) Msg RX from 1:000000000001B669 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:28:08.459]  [00:01:54.380][info  ][DIS] Checking node lookup status for 0FCE5DA14975F0EB-0000000000000001 after 200 ms
[18:28:09.587]  [00:01:55.512][info  ][DIS] Node ID resolved for 0FCE5DA14975F0EB-0000000000000001
[18:28:09.587]  [00:01:55.512][info  ][DIS] UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540: new best score: 3 (for 0FCE5DA14975F0EB-0000000000000001)
[18:28:09.590]  [00:01:55.513][info  ][DIS] Checking node lookup status for 0FCE5DA14975F0EB-0000000000000001 after 1333 ms
[18:28:09.591]  [00:01:55.514][info  ][SC] Initiating session on local FabricIndex 1 from 0x00000000000008CA -> 0x0000000000000001
[18:28:09.606]  [00:01:55.530][info  ][EM] <<< [E:4204i S:0 M:156745225] (U) Msg TX from B3B857A8AB43390B to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:30 (SecureChannel:CASE_Sigma1) (B:195)
[18:28:09.607]  [00:01:55.531][info  ][EM] ??1 [E:4204i S:0 M:156745225] (U) Msg Retransmission to 0:0000000000000000 scheduled for 3583ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:28:09.612]  [00:01:55.531][info  ][SC] Sent Sigma1 msg to <0000000000000001, 1> [II:3000ms AI:2500ms AT:0ms]
[18:28:10.302]  [00:01:56.226][info  ][EM] >>> [E:4204i S:0 M:155012594 (Ack:156745225)] (U) Msg RX from 0:0000000000000000 [0000] to B3B857A8AB43390B --- Type 0000:31 (SecureChannel:CASE_Sigma2) (B:751)
[18:28:10.304]  [00:01:56.227][info  ][EM] <<< [E:4204i S:0 M:156745226 (Ack:155012594)] (U) Msg TX from B3B857A8AB43390B to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:28:10.309]  [00:01:56.228][info  ][SC] Received Sigma2 msg
[18:28:10.367]  [00:01:56.291][info  ][EM] <<< [E:4204i S:0 M:156745227 (Ack:155012594)] (U) Msg TX from B3B857A8AB43390B to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:32 (SecureChannel:CASE_Sigma3) (B:596)
[18:28:10.368]  [00:01:56.291][info  ][EM] ??1 [E:4204i S:0 M:156745227] (U) Msg Retransmission to 0:0000000000000000 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:10.374]  [00:01:56.292][info  ][SC] Sent Sigma3 msg
[18:28:13.725]  [00:01:59.650][info  ][EM] >>> [E:4204i S:0 M:155012595 (Ack:156745227)] (U) Msg RX from 0:0000000000000000 [0000] to B3B857A8AB43390B --- Type 0000:40 (SecureChannel:StatusReport) (B:34)
[18:28:13.728]  [00:01:59.650][info  ][SC] Success status report received. Session was established
[18:28:13.734]  [00:01:59.657][info  ][SC] SecureSession[0x20006fd8, LSID:1633]: State change 'kEstablishing' --> 'kActive'
[18:28:13.734]  [00:01:59.660][info  ][EM] <<< [E:4205i S:1633 M:80981786] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0001:08 (IM:InvokeCommandRequest) (B:85)
[18:28:13.736]  [00:01:59.661][info  ][EM] ??1 [E:4205i S:1633 M:80981786] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:13.740]  [00:01:59.661][info  ][EM] <<< [E:4204i S:0 M:156745228 (Ack:155012595)] (U) Msg TX from B3B857A8AB43390B to 0:0000000000000000 [0000] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:26)
[18:28:13.741]  [00:01:59.662][info  ][DL] _OnPlatformEvent default:  event->Type = 32792
[18:28:13.745]  [00:01:59.662][silabs ]NWK: platform event type 32792
[18:28:14.388]  [00:02:00.312][info  ][EM] >>> [E:4205i S:1633 M:57786204 (Ack:80981786)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0001:09 (IM:InvokeCommandResponse) (B:196)
[18:28:14.390]  [00:02:00.314][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[18:28:14.391]  [00:02:00.314][info  ][SWU] Update available from version 1 to 2
[18:28:14.391]  [00:02:00.316][info  ][EM] <<< [E:4205i S:1633 M:80981787 (Ack:57786204)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:28:14.434]  [00:02:00.317][info  ][DIS] Found an existing secure session to [1:0000000000000001]!
[18:28:14.434]  [00:02:00.318][info  ][SWU] HandlePrepareDownload: started
[18:28:14.436]  [00:02:00.361][info  ][EM] <<< [E:4206i S:1633 M:80981788] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:04 (BDX:ReceiveInit) (B:88)
[18:28:14.438]  [00:02:00.362][info  ][EM] ??1 [E:4206i S:1633 M:80981788] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:14.989]  [00:02:00.914][info  ][EM] >>> [E:4206i S:1633 M:57786205 (Ack:80981788)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:05 (BDX:ReceiveAccept) (B:38)
[18:28:14.990]  [00:02:00.916][info  ][EM] <<< [E:4206i S:1633 M:80981789 (Ack:57786205)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:14.993]  [00:02:00.916][info  ][EM] ??1 [E:4206i S:1633 M:80981789] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:16.433]  [00:02:02.358][info  ][EM] >>> [E:4206i S:1633 M:57786206 (Ack:80981789)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:16.514]  [00:02:02.359][info  ][SWU] Image Header software version: 2 payload size: 553476
[18:28:16.561]  [00:02:02.485][info  ][EM] <<< [E:4206i S:1633 M:80981790 (Ack:57786206)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:16.562]  [00:02:02.486][info  ][EM] ??1 [E:4206i S:1633 M:80981790] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:16.567]  [00:02:02.486][error ][DL] Long dispatch time: 127 ms, for event type 2
[18:28:17.332]  [00:02:03.256][info  ][EM] >>> [E:4206i S:1633 M:57786207 (Ack:80981790)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:17.393]  [00:02:03.317][info  ][EM] <<< [E:4206i S:1633 M:80981791 (Ack:57786207)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:17.395]  [00:02:03.318][info  ][EM] ??1 [E:4206i S:1633 M:80981791] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:18.109]  [00:02:04.033][info  ][EM] >>> [E:4206i S:1633 M:57786208 (Ack:80981791)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:18.169]  [00:02:04.093][info  ][EM] <<< [E:4206i S:1633 M:80981792 (Ack:57786208)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:18.171]  [00:02:04.094][info  ][EM] ??1 [E:4206i S:1633 M:80981792] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:19.004]  [00:02:04.929][info  ][EM] >>> [E:4206i S:1633 M:57786209 (Ack:80981792)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:19.065]  [00:02:04.990][info  ][EM] <<< [E:4206i S:1633 M:80981793 (Ack:57786209)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:19.067]  [00:02:04.991][info  ][EM] ??1 [E:4206i S:1633 M:80981793] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:20.417]  [00:02:06.341][info  ][EM] >>> [E:4206i S:1633 M:57786210 (Ack:80981793)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:20.551]  [00:02:06.475][info  ][EM] <<< [E:4206i S:1633 M:80981794 (Ack:57786210)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:20.552]  [00:02:06.476][info  ][EM] ??1 [E:4206i S:1633 M:80981794] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:20.558]  [00:02:06.476][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:28:21.430]  [00:02:07.355][info  ][EM] >>> [E:4206i S:1633 M:57786211 (Ack:80981794)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:21.490]  [00:02:07.416][info  ][EM] <<< [E:4206i S:1633 M:80981795 (Ack:57786211)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:21.492]  [00:02:07.416][info  ][EM] ??1 [E:4206i S:1633 M:80981795] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:22.454]  [00:02:08.378][info  ][EM] >>> [E:4206i S:1633 M:57786212 (Ack:80981795)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:22.515]  [00:02:08.439][info  ][EM] <<< [E:4206i S:1633 M:80981796 (Ack:57786212)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:22.516]  [00:02:08.440][info  ][EM] ??1 [E:4206i S:1633 M:80981796] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:23.246]  [00:02:09.169][info  ][EM] >>> [E:4206i S:1633 M:57786213 (Ack:80981796)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:23.306]  [00:02:09.230][info  ][EM] <<< [E:4206i S:1633 M:80981797 (Ack:57786213)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:23.307]  [00:02:09.231][info  ][EM] ??1 [E:4206i S:1633 M:80981797] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5489ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:24.023]  [00:02:09.947][info  ][EM] >>> [E:4206i S:1633 M:57786214 (Ack:80981797)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:24.156]  [00:02:10.081][info  ][EM] <<< [E:4206i S:1633 M:80981798 (Ack:57786214)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:24.158]  [00:02:10.082][info  ][EM] ??1 [E:4206i S:1633 M:80981798] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5422ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:24.163]  [00:02:10.082][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:28:25.078]  [00:02:11.002][info  ][EM] >>> [E:4206i S:1633 M:57786215 (Ack:80981798)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:25.138]  [00:02:11.063][info  ][EM] <<< [E:4206i S:1633 M:80981799 (Ack:57786215)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:25.141]  [00:02:11.064][info  ][EM] ??1 [E:4206i S:1633 M:80981799] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:25.971]  [00:02:11.895][info  ][EM] >>> [E:4206i S:1633 M:57786216 (Ack:80981799)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:26.031]  [00:02:11.956][info  ][EM] <<< [E:4206i S:1633 M:80981800 (Ack:57786216)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:26.033]  [00:02:11.956][info  ][EM] ??1 [E:4206i S:1633 M:80981800] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:27.609]  [00:02:13.534][info  ][EM] >>> [E:4206i S:1633 M:57786217 (Ack:80981800)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:27.669]  [00:02:13.594][info  ][EM] <<< [E:4206i S:1633 M:80981801 (Ack:57786217)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:27.671]  [00:02:13.595][info  ][EM] ??1 [E:4206i S:1633 M:80981801] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:28.389]  [00:02:14.313][info  ][EM] >>> [E:4206i S:1633 M:57786218 (Ack:80981801)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:28.523]  [00:02:14.447][info  ][EM] <<< [E:4206i S:1633 M:80981802 (Ack:57786218)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:28.524]  [00:02:14.448][info  ][EM] ??1 [E:4206i S:1633 M:80981802] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:28.528]  [00:02:14.449][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:28:29.373]  [00:02:15.297][info  ][EM] >>> [E:4206i S:1633 M:57786219 (Ack:80981802)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:29.434]  [00:02:15.358][info  ][EM] <<< [E:4206i S:1633 M:80981803 (Ack:57786219)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:29.435]  [00:02:15.359][info  ][EM] ??1 [E:4206i S:1633 M:80981803] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:30.156]  [00:02:16.080][info  ][EM] >>> [E:4206i S:1633 M:57786220 (Ack:80981803)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:30.216]  [00:02:16.140][info  ][EM] <<< [E:4206i S:1633 M:80981804 (Ack:57786220)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:30.217]  [00:02:16.141][info  ][EM] ??1 [E:4206i S:1633 M:80981804] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:31.057]  [00:02:16.981][info  ][EM] >>> [E:4206i S:1633 M:57786221 (Ack:80981804)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:31.117]  [00:02:17.041][info  ][EM] <<< [E:4206i S:1633 M:80981805 (Ack:57786221)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:31.119]  [00:02:17.042][info  ][EM] ??1 [E:4206i S:1633 M:80981805] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:31.937]  [00:02:17.861][info  ][EM] >>> [E:4206i S:1633 M:57786222 (Ack:80981805)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:32.070]  [00:02:17.995][info  ][EM] <<< [E:4206i S:1633 M:80981806 (Ack:57786222)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:32.072]  [00:02:17.996][info  ][EM] ??1 [E:4206i S:1633 M:80981806] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:32.077]  [00:02:17.996][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:28:32.712]  [00:02:18.637][info  ][EM] >>> [E:4206i S:1633 M:57786223 (Ack:80981806)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:32.773]  [00:02:18.698][info  ][EM] <<< [E:4206i S:1633 M:80981807 (Ack:57786223)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:32.774]  [00:02:18.699][info  ][EM] ??1 [E:4206i S:1633 M:80981807] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5652ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:36.772]  [00:02:22.697][info  ][EM] >>> [E:4206i S:1633 M:57786224 (Ack:80981807)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:36.833]  [00:02:22.757][info  ][EM] <<< [E:4206i S:1633 M:80981808 (Ack:57786224)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:36.835]  [00:02:22.758][info  ][EM] ??1 [E:4206i S:1633 M:80981808] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5568ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:37.773]  [00:02:23.698][info  ][EM] >>> [E:4206i S:1633 M:57786225 (Ack:80981808)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:37.834]  [00:02:23.758][info  ][EM] <<< [E:4206i S:1633 M:80981809 (Ack:57786225)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:37.836]  [00:02:23.759][info  ][EM] ??1 [E:4206i S:1633 M:80981809] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:42.098]  [00:02:28.022][info  ][EM] >>> [E:4206i S:1633 M:57786226 (Ack:80981809)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:42.232]  [00:02:28.156][info  ][EM] <<< [E:4206i S:1633 M:80981810 (Ack:57786226)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:42.234]  [00:02:28.157][info  ][EM] ??1 [E:4206i S:1633 M:80981810] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:42.238]  [00:02:28.158][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:28:46.514]  [00:02:32.438][info  ][EM] >>> [E:4206i S:1633 M:57786227 (Ack:80981810)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:46.574]  [00:02:32.499][info  ][EM] <<< [E:4206i S:1633 M:80981811 (Ack:57786227)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:46.576]  [00:02:32.500][info  ][EM] ??1 [E:4206i S:1633 M:80981811] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:47.295]  [00:02:33.219][info  ][EM] >>> [E:4206i S:1633 M:57786228 (Ack:80981811)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:47.356]  [00:02:33.280][info  ][EM] <<< [E:4206i S:1633 M:80981812 (Ack:57786228)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:47.357]  [00:02:33.281][info  ][EM] ??1 [E:4206i S:1633 M:80981812] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:51.493]  [00:02:37.418][info  ][EM] >>> [E:4206i S:1633 M:57786229 (Ack:80981812)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:51.554]  [00:02:37.479][info  ][EM] <<< [E:4206i S:1633 M:80981813 (Ack:57786229)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:51.556]  [00:02:37.480][info  ][EM] ??1 [E:4206i S:1633 M:80981813] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:55.434]  [00:02:41.358][info  ][EM] >>> [E:4206i S:1633 M:57786230 (Ack:80981813)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:55.567]  [00:02:41.492][info  ][EM] <<< [E:4206i S:1633 M:80981814 (Ack:57786230)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:55.568]  [00:02:41.493][info  ][EM] ??1 [E:4206i S:1633 M:80981814] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5473ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:55.574]  [00:02:41.493][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:28:56.435]  [00:02:42.359][info  ][EM] >>> [E:4206i S:1633 M:57786231 (Ack:80981814)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:56.495]  [00:02:42.419][info  ][EM] <<< [E:4206i S:1633 M:80981815 (Ack:57786231)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:56.496]  [00:02:42.420][info  ][EM] ??1 [E:4206i S:1633 M:80981815] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5422ms from now [State:Active II:500 AI:2000 AT:4000]
[18:28:57.484]  [00:02:43.408][info  ][EM] >>> [E:4206i S:1633 M:57786232 (Ack:80981815)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:28:57.544]  [00:02:43.468][info  ][EM] <<< [E:4206i S:1633 M:80981816 (Ack:57786232)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:28:57.545]  [00:02:43.469][info  ][EM] ??1 [E:4206i S:1633 M:80981816] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:03.173]  [00:02:49.097][info  ][EM] <<1 [E:4206i S:1633 M:80981816] (S) Msg Retransmission to 1:0000000000000001
[18:29:03.173]  [00:02:49.098][info  ][EM] ??2 [E:4206i S:1633 M:80981816] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:29:03.208]  [00:02:49.132][info  ][EM] >>> [E:4206i S:1633 M:57786234 (Ack:80981816)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:29:04.501]  [00:02:50.425][info  ][EM] >>> [E:4206i S:1633 M:57786233 (Ack:80981816)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:04.561]  [00:02:50.486][info  ][EM] <<< [E:4206i S:1633 M:80981817 (Ack:57786233)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:04.563]  [00:02:50.487][info  ][EM] ??1 [E:4206i S:1633 M:80981817] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5562ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:05.276]  [00:02:51.201][info  ][EM] >>> [E:4206i S:1633 M:57786235 (Ack:80981817)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:05.410]  [00:02:51.334][info  ][EM] <<< [E:4206i S:1633 M:80981818 (Ack:57786235)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:05.411]  [00:02:51.335][info  ][EM] ??1 [E:4206i S:1633 M:80981818] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5312ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:05.416]  [00:02:51.335][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:29:06.787]  [00:02:52.711][info  ][EM] >>> [E:4206i S:1633 M:57786236 (Ack:80981818)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:06.848]  [00:02:52.772][info  ][EM] <<< [E:4206i S:1633 M:80981819 (Ack:57786236)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:06.849]  [00:02:52.773][info  ][EM] ??1 [E:4206i S:1633 M:80981819] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5443ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:07.775]  [00:02:53.700][info  ][EM] >>> [E:4206i S:1633 M:57786237 (Ack:80981819)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:07.835]  [00:02:53.760][info  ][EM] <<< [E:4206i S:1633 M:80981820 (Ack:57786237)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:07.837]  [00:02:53.761][info  ][EM] ??1 [E:4206i S:1633 M:80981820] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:08.834]  [00:02:54.758][info  ][EM] >>> [E:4206i S:1633 M:57786238 (Ack:80981820)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:08.894]  [00:02:54.819][info  ][EM] <<< [E:4206i S:1633 M:80981821 (Ack:57786238)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:08.896]  [00:02:54.820][info  ][EM] ??1 [E:4206i S:1633 M:80981821] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:09.844]  [00:02:55.768][info  ][EM] >>> [E:4206i S:1633 M:57786239 (Ack:80981821)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:09.978]  [00:02:55.903][info  ][EM] <<< [E:4206i S:1633 M:80981822 (Ack:57786239)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:09.979]  [00:02:55.903][info  ][EM] ??1 [E:4206i S:1633 M:80981822] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:09.986]  [00:02:55.904][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:29:13.934]  [00:02:59.858][info  ][EM] >>> [E:4206i S:1633 M:57786240 (Ack:80981822)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:13.994]  [00:02:59.918][info  ][EM] <<< [E:4206i S:1633 M:80981823 (Ack:57786240)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:13.995]  [00:02:59.919][info  ][EM] ??1 [E:4206i S:1633 M:80981823] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:15.048]  [00:03:00.972][info  ][EM] >>> [E:4206i S:1633 M:57786241 (Ack:80981823)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:15.109]  [00:03:01.033][info  ][EM] <<< [E:4206i S:1633 M:80981824 (Ack:57786241)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:15.110]  [00:03:01.034][info  ][EM] ??1 [E:4206i S:1633 M:80981824] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5723ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:15.867]  [00:03:01.791][info  ][EM] >>> [E:4206i S:1633 M:57786242 (Ack:80981824)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:15.927]  [00:03:01.852][info  ][EM] <<< [E:4206i S:1633 M:80981825 (Ack:57786242)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:15.928]  [00:03:01.853][info  ][EM] ??1 [E:4206i S:1633 M:80981825] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:17.219]  [00:03:03.143][info  ][EM] >>> [E:4206i S:1633 M:57786243 (Ack:80981825)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:17.354]  [00:03:03.278][info  ][EM] <<< [E:4206i S:1633 M:80981826 (Ack:57786243)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:17.355]  [00:03:03.279][info  ][EM] ??1 [E:4206i S:1633 M:80981826] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5553ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:17.361]  [00:03:03.279][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:29:18.528]  [00:03:04.453][info  ][EM] >>> [E:4206i S:1633 M:57786244 (Ack:80981826)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:18.588]  [00:03:04.513][info  ][EM] <<< [E:4206i S:1633 M:80981827 (Ack:57786244)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:18.590]  [00:03:04.513][info  ][EM] ??1 [E:4206i S:1633 M:80981827] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:19.323]  [00:03:05.247][info  ][EM] >>> [E:4206i S:1633 M:57786245 (Ack:80981827)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:19.383]  [00:03:05.307][info  ][EM] <<< [E:4206i S:1633 M:80981828 (Ack:57786245)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:19.385]  [00:03:05.308][info  ][EM] ??1 [E:4206i S:1633 M:80981828] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:23.672]  [00:03:09.596][info  ][EM] >>> [E:4206i S:1633 M:57786246 (Ack:80981828)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:23.732]  [00:03:09.657][info  ][EM] <<< [E:4206i S:1633 M:80981829 (Ack:57786246)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:23.734]  [00:03:09.658][info  ][EM] ??1 [E:4206i S:1633 M:80981829] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:25.011]  [00:03:10.936][info  ][EM] >>> [E:4206i S:1633 M:57786247 (Ack:80981829)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:25.146]  [00:03:11.070][info  ][EM] <<< [E:4206i S:1633 M:80981830 (Ack:57786247)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:25.148]  [00:03:11.071][info  ][EM] ??1 [E:4206i S:1633 M:80981830] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5740ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:25.152]  [00:03:11.072][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:29:26.017]  [00:03:11.941][info  ][EM] >>> [E:4206i S:1633 M:57786248 (Ack:80981830)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:26.077]  [00:03:12.001][info  ][EM] <<< [E:4206i S:1633 M:80981831 (Ack:57786248)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:26.079]  [00:03:12.002][info  ][EM] ??1 [E:4206i S:1633 M:80981831] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:30.046]  [00:03:15.971][info  ][EM] >>> [E:4206i S:1633 M:57786249 (Ack:80981831)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:30.107]  [00:03:16.032][info  ][EM] <<< [E:4206i S:1633 M:80981832 (Ack:57786249)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:30.109]  [00:03:16.032][info  ][EM] ??1 [E:4206i S:1633 M:80981832] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:35.785]  [00:03:21.710][info  ][EM] <<1 [E:4206i S:1633 M:80981832] (S) Msg Retransmission to 1:0000000000000001
[18:29:35.785]  [00:03:21.710][info  ][EM] ??2 [E:4206i S:1633 M:80981832] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:29:35.966]  [00:03:21.891][info  ][EM] >>> [E:4206i S:1633 M:57786251 (Ack:80981832)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:29:36.730]  [00:03:22.655][info  ][EM] >>> [E:4206i S:1633 M:57786250 (Ack:80981832)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:36.790]  [00:03:22.715][info  ][EM] <<< [E:4206i S:1633 M:80981833 (Ack:57786250)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:36.792]  [00:03:22.716][info  ][EM] ??1 [E:4206i S:1633 M:80981833] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:37.759]  [00:03:23.684][info  ][EM] >>> [E:4206i S:1633 M:57786252 (Ack:80981833)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:37.893]  [00:03:23.818][info  ][EM] <<< [E:4206i S:1633 M:80981834 (Ack:57786252)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:37.894]  [00:03:23.819][info  ][EM] ??1 [E:4206i S:1633 M:80981834] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:37.900]  [00:03:23.819][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:29:38.890]  [00:03:24.815][info  ][EM] >>> [E:4206i S:1633 M:57786253 (Ack:80981834)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:38.951]  [00:03:24.875][info  ][EM] <<< [E:4206i S:1633 M:80981835 (Ack:57786253)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:38.952]  [00:03:24.876][info  ][EM] ??1 [E:4206i S:1633 M:80981835] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:44.653]  [00:03:30.578][info  ][EM] <<1 [E:4206i S:1633 M:80981835] (S) Msg Retransmission to 1:0000000000000001
[18:29:44.653]  [00:03:30.579][info  ][EM] ??2 [E:4206i S:1633 M:80981835] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:29:44.993]  [00:03:30.917][info  ][EM] >>> [E:4206i S:1633 M:57786255 (Ack:80981835)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:29:50.024]  [00:03:35.949][info  ][EM] >>> [E:4206i S:1633 M:57786254 (Ack:80981835)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:50.084]  [00:03:36.009][info  ][EM] <<< [E:4206i S:1633 M:80981836 (Ack:57786254)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:50.086]  [00:03:36.010][info  ][EM] ??1 [E:4206i S:1633 M:80981836] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5349ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:51.152]  [00:03:37.078][info  ][EM] >>> [E:4206i S:1633 M:57786256 (Ack:80981836)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:51.213]  [00:03:37.138][info  ][EM] <<< [E:4206i S:1633 M:80981837 (Ack:57786256)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:51.214]  [00:03:37.138][info  ][EM] ??1 [E:4206i S:1633 M:80981837] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:52.356]  [00:03:38.282][info  ][EM] >>> [E:4206i S:1633 M:57786257 (Ack:80981837)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:52.490]  [00:03:38.416][info  ][EM] <<< [E:4206i S:1633 M:80981838 (Ack:57786257)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:52.492]  [00:03:38.416][info  ][EM] ??1 [E:4206i S:1633 M:80981838] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:52.499]  [00:03:38.417][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:29:56.175]  [00:03:42.100][info  ][EM] >>> [E:4206i S:1633 M:57786258 (Ack:80981838)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:56.235]  [00:03:42.161][info  ][EM] <<< [E:4206i S:1633 M:80981839 (Ack:57786258)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:56.236]  [00:03:42.162][info  ][EM] ??1 [E:4206i S:1633 M:80981839] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5265ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:56.964]  [00:03:42.889][info  ][EM] >>> [E:4206i S:1633 M:57786259 (Ack:80981839)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:57.024]  [00:03:42.950][info  ][EM] <<< [E:4206i S:1633 M:80981840 (Ack:57786259)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:57.025]  [00:03:42.951][info  ][EM] ??1 [E:4206i S:1633 M:80981840] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[18:29:57.772]  [00:03:43.698][info  ][EM] >>> [E:4206i S:1633 M:57786260 (Ack:80981840)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:29:57.833]  [00:03:43.758][info  ][EM] <<< [E:4206i S:1633 M:80981841 (Ack:57786260)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:29:57.834]  [00:03:43.759][info  ][EM] ??1 [E:4206i S:1633 M:80981841] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5633ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:01.873]  [00:03:47.798][info  ][EM] >>> [E:4206i S:1633 M:57786261 (Ack:80981841)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:02.007]  [00:03:47.932][info  ][EM] <<< [E:4206i S:1633 M:80981842 (Ack:57786261)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:02.009]  [00:03:47.933][info  ][EM] ??1 [E:4206i S:1633 M:80981842] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5478ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:02.014]  [00:03:47.933][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:30:03.279]  [00:03:49.204][info  ][EM] >>> [E:4206i S:1633 M:57786262 (Ack:80981842)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:03.338]  [00:03:49.264][info  ][EM] <<< [E:4206i S:1633 M:80981843 (Ack:57786262)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:03.340]  [00:03:49.265][info  ][EM] ??1 [E:4206i S:1633 M:80981843] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:09.005]  [00:03:54.932][info  ][EM] <<1 [E:4206i S:1633 M:80981843] (S) Msg Retransmission to 1:0000000000000001
[18:30:09.005]  [00:03:54.933][info  ][EM] ??2 [E:4206i S:1633 M:80981843] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:30:09.256]  [00:03:55.182][info  ][EM] >>> [E:4206i S:1633 M:57786264 (Ack:80981843)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:30:15.253]  [00:04:01.180][info  ][EM] >>> [E:4206i S:1633 M:57786263 (Ack:80981843)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:15.314]  [00:04:01.240][info  ][EM] <<< [E:4206i S:1633 M:80981844 (Ack:57786263)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:15.315]  [00:04:01.241][info  ][EM] ??1 [E:4206i S:1633 M:80981844] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:16.163]  [00:04:02.089][info  ][EM] >>> [E:4206i S:1633 M:57786265 (Ack:80981844)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:16.224]  [00:04:02.150][info  ][EM] <<< [E:4206i S:1633 M:80981845 (Ack:57786265)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:16.225]  [00:04:02.151][info  ][EM] ??1 [E:4206i S:1633 M:80981845] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5246ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:17.496]  [00:04:03.422][info  ][EM] >>> [E:4206i S:1633 M:57786266 (Ack:80981845)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:17.630]  [00:04:03.556][info  ][EM] <<< [E:4206i S:1633 M:80981846 (Ack:57786266)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:17.631]  [00:04:03.557][info  ][EM] ??1 [E:4206i S:1633 M:80981846] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:17.638]  [00:04:03.557][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:30:21.630]  [00:04:07.556][info  ][EM] >>> [E:4206i S:1633 M:57786267 (Ack:80981846)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:21.690]  [00:04:07.617][info  ][EM] <<< [E:4206i S:1633 M:80981847 (Ack:57786267)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:21.691]  [00:04:07.618][info  ][EM] ??1 [E:4206i S:1633 M:80981847] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5304ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:25.591]  [00:04:11.517][info  ][EM] >>> [E:4206i S:1633 M:57786268 (Ack:80981847)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:25.651]  [00:04:11.578][info  ][EM] <<< [E:4206i S:1633 M:80981848 (Ack:57786268)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:25.653]  [00:04:11.579][info  ][EM] ??1 [E:4206i S:1633 M:80981848] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5654ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:27.326]  [00:04:13.252][info  ][EM] >>> [E:4206i S:1633 M:57786269 (Ack:80981848)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:27.387]  [00:04:13.313][info  ][EM] <<< [E:4206i S:1633 M:80981849 (Ack:57786269)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:27.388]  [00:04:13.314][info  ][EM] ??1 [E:4206i S:1633 M:80981849] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5465ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:28.443]  [00:04:14.370][info  ][EM] >>> [E:4206i S:1633 M:57786270 (Ack:80981849)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:28.577]  [00:04:14.503][info  ][EM] <<< [E:4206i S:1633 M:80981850 (Ack:57786270)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:28.579]  [00:04:14.504][info  ][EM] ??1 [E:4206i S:1633 M:80981850] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5228ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:28.584]  [00:04:14.505][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:30:29.224]  [00:04:15.151][info  ][EM] >>> [E:4206i S:1633 M:57786271 (Ack:80981850)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:29.285]  [00:04:15.211][info  ][EM] <<< [E:4206i S:1633 M:80981851 (Ack:57786271)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:29.286]  [00:04:15.212][info  ][EM] ??1 [E:4206i S:1633 M:80981851] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:30.014]  [00:04:15.941][info  ][EM] >>> [E:4206i S:1633 M:57786272 (Ack:80981851)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:30.074]  [00:04:16.001][info  ][EM] <<< [E:4206i S:1633 M:80981852 (Ack:57786272)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:30.076]  [00:04:16.001][info  ][EM] ??1 [E:4206i S:1633 M:80981852] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:34.215]  [00:04:20.141][info  ][EM] >>> [E:4206i S:1633 M:57786273 (Ack:80981852)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:34.276]  [00:04:20.202][info  ][EM] <<< [E:4206i S:1633 M:80981853 (Ack:57786273)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:34.277]  [00:04:20.203][info  ][EM] ??1 [E:4206i S:1633 M:80981853] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:35.092]  [00:04:21.019][info  ][EM] >>> [E:4206i S:1633 M:57786274 (Ack:80981853)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:35.228]  [00:04:21.155][info  ][EM] <<< [E:4206i S:1633 M:80981854 (Ack:57786274)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:35.230]  [00:04:21.156][info  ][EM] ??1 [E:4206i S:1633 M:80981854] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:35.236]  [00:04:21.157][error ][DL] Long dispatch time: 136 ms, for event type 2
[18:30:38.972]  [00:04:24.899][info  ][EM] >>> [E:4206i S:1633 M:57786275 (Ack:80981854)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:39.032]  [00:04:24.959][info  ][EM] <<< [E:4206i S:1633 M:80981855 (Ack:57786275)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:39.034]  [00:04:24.960][info  ][EM] ??1 [E:4206i S:1633 M:80981855] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:39.767]  [00:04:25.695][info  ][EM] >>> [E:4206i S:1633 M:57786276 (Ack:80981855)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:39.829]  [00:04:25.755][info  ][EM] <<< [E:4206i S:1633 M:80981856 (Ack:57786276)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:39.830]  [00:04:25.756][info  ][EM] ??1 [E:4206i S:1633 M:80981856] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:40.958]  [00:04:26.885][info  ][EM] >>> [E:4206i S:1633 M:57786277 (Ack:80981856)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:41.019]  [00:04:26.946][info  ][EM] <<< [E:4206i S:1633 M:80981857 (Ack:57786277)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:41.020]  [00:04:26.946][info  ][EM] ??1 [E:4206i S:1633 M:80981857] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5684ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:41.735]  [00:04:27.663][info  ][EM] >>> [E:4206i S:1633 M:57786278 (Ack:80981857)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:41.870]  [00:04:27.796][info  ][EM] <<< [E:4206i S:1633 M:80981858 (Ack:57786278)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:41.871]  [00:04:27.797][info  ][EM] ??1 [E:4206i S:1633 M:80981858] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5220ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:41.876]  [00:04:27.797][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:30:42.633]  [00:04:28.560][info  ][EM] >>> [E:4206i S:1633 M:57786279 (Ack:80981858)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:42.695]  [00:04:28.621][info  ][EM] <<< [E:4206i S:1633 M:80981859 (Ack:57786279)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:42.696]  [00:04:28.622][info  ][EM] ??1 [E:4206i S:1633 M:80981859] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5360ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:48.055]  [00:04:33.982][info  ][EM] <<1 [E:4206i S:1633 M:80981859] (S) Msg Retransmission to 1:0000000000000001
[18:30:48.055]  [00:04:33.982][info  ][EM] ??2 [E:4206i S:1633 M:80981859] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:30:48.414]  [00:04:34.341][info  ][EM] >>> [E:4206i S:1633 M:57786281 (Ack:80981859)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:30:50.357]  [00:04:36.285][info  ][EM] >>> [E:4206i S:1633 M:57786280 (Ack:80981859)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:50.418]  [00:04:36.345][info  ][EM] <<< [E:4206i S:1633 M:80981860 (Ack:57786280)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:50.419]  [00:04:36.346][info  ][EM] ??1 [E:4206i S:1633 M:80981860] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:51.814]  [00:04:37.742][info  ][EM] >>> [E:4206i S:1633 M:57786282 (Ack:80981860)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:51.874]  [00:04:37.802][info  ][EM] <<< [E:4206i S:1633 M:80981861 (Ack:57786282)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:51.877]  [00:04:37.802][info  ][EM] ??1 [E:4206i S:1633 M:80981861] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:52.916]  [00:04:38.843][info  ][EM] >>> [E:4206i S:1633 M:57786283 (Ack:80981861)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:53.050]  [00:04:38.977][info  ][EM] <<< [E:4206i S:1633 M:80981862 (Ack:57786283)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:53.051]  [00:04:38.978][info  ][EM] ??1 [E:4206i S:1633 M:80981862] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:53.056]  [00:04:38.978][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:30:56.817]  [00:04:42.745][info  ][EM] >>> [E:4206i S:1633 M:57786284 (Ack:80981862)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:56.878]  [00:04:42.805][info  ][EM] <<< [E:4206i S:1633 M:80981863 (Ack:57786284)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:56.879]  [00:04:42.806][info  ][EM] ??1 [E:4206i S:1633 M:80981863] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:58.018]  [00:04:43.946][info  ][EM] >>> [E:4206i S:1633 M:57786285 (Ack:80981863)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:58.079]  [00:04:44.005][info  ][EM] <<< [E:4206i S:1633 M:80981864 (Ack:57786285)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:58.080]  [00:04:44.006][info  ][EM] ??1 [E:4206i S:1633 M:80981864] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5280ms from now [State:Active II:500 AI:2000 AT:4000]
[18:30:59.759]  [00:04:45.687][info  ][EM] >>> [E:4206i S:1633 M:57786286 (Ack:80981864)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:30:59.820]  [00:04:45.748][info  ][EM] <<< [E:4206i S:1633 M:80981865 (Ack:57786286)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:30:59.821]  [00:04:45.749][info  ][EM] ??1 [E:4206i S:1633 M:80981865] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5671ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:00.859]  [00:04:46.787][info  ][EM] >>> [E:4206i S:1633 M:57786287 (Ack:80981865)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:00.993]  [00:04:46.920][info  ][EM] <<< [E:4206i S:1633 M:80981866 (Ack:57786287)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:00.995]  [00:04:46.921][info  ][EM] ??1 [E:4206i S:1633 M:80981866] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:01.000]  [00:04:46.921][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:31:01.849]  [00:04:47.777][info  ][EM] >>> [E:4206i S:1633 M:57786288 (Ack:80981866)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:01.910]  [00:04:47.837][info  ][EM] <<< [E:4206i S:1633 M:80981867 (Ack:57786288)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:01.911]  [00:04:47.838][info  ][EM] ??1 [E:4206i S:1633 M:80981867] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5280ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:02.629]  [00:04:48.556][info  ][EM] >>> [E:4206i S:1633 M:57786289 (Ack:80981867)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:02.690]  [00:04:48.617][info  ][EM] <<< [E:4206i S:1633 M:80981868 (Ack:57786289)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:02.691]  [00:04:48.618][info  ][EM] ??1 [E:4206i S:1633 M:80981868] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:03.524]  [00:04:49.452][info  ][EM] >>> [E:4206i S:1633 M:57786290 (Ack:80981868)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:03.586]  [00:04:49.512][info  ][EM] <<< [E:4206i S:1633 M:80981869 (Ack:57786290)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:03.587]  [00:04:49.513][info  ][EM] ??1 [E:4206i S:1633 M:80981869] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5562ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:05.148]  [00:04:51.075][info  ][EM] >>> [E:4206i S:1633 M:57786291 (Ack:80981869)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:05.282]  [00:04:51.209][info  ][EM] <<< [E:4206i S:1633 M:80981870 (Ack:57786291)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:05.283]  [00:04:51.209][info  ][EM] ??1 [E:4206i S:1633 M:80981870] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5605ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:05.288]  [00:04:51.210][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:31:05.934]  [00:04:51.861][info  ][EM] >>> [E:4206i S:1633 M:57786292 (Ack:80981870)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:05.995]  [00:04:51.921][info  ][EM] <<< [E:4206i S:1633 M:80981871 (Ack:57786292)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:05.996]  [00:04:51.922][info  ][EM] ??1 [E:4206i S:1633 M:80981871] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:07.256]  [00:04:53.184][info  ][EM] >>> [E:4206i S:1633 M:57786293 (Ack:80981871)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:07.317]  [00:04:53.244][info  ][EM] <<< [E:4206i S:1633 M:80981872 (Ack:57786293)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:07.318]  [00:04:53.245][info  ][EM] ??1 [E:4206i S:1633 M:80981872] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:11.665]  [00:04:57.592][info  ][EM] >>> [E:4206i S:1633 M:57786294 (Ack:80981872)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:11.726]  [00:04:57.653][info  ][EM] <<< [E:4206i S:1633 M:80981873 (Ack:57786294)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:11.727]  [00:04:57.654][info  ][EM] ??1 [E:4206i S:1633 M:80981873] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:12.766]  [00:04:58.694][info  ][EM] >>> [E:4206i S:1633 M:57786295 (Ack:80981873)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:12.900]  [00:04:58.828][info  ][EM] <<< [E:4206i S:1633 M:80981874 (Ack:57786295)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:12.901]  [00:04:58.829][info  ][EM] ??1 [E:4206i S:1633 M:80981874] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5727ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:12.905]  [00:04:58.829][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:31:13.864]  [00:04:59.791][info  ][EM] >>> [E:4206i S:1633 M:57786296 (Ack:80981874)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:13.924]  [00:04:59.852][info  ][EM] <<< [E:4206i S:1633 M:80981875 (Ack:57786296)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:13.925]  [00:04:59.853][info  ][EM] ??1 [E:4206i S:1633 M:80981875] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:14.968]  [00:05:00.896][info  ][EM] >>> [E:4206i S:1633 M:57786297 (Ack:80981875)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:15.029]  [00:05:00.957][info  ][EM] <<< [E:4206i S:1633 M:80981876 (Ack:57786297)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:15.030]  [00:05:00.958][info  ][EM] ??1 [E:4206i S:1633 M:80981876] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:15.873]  [00:05:01.800][info  ][EM] >>> [E:4206i S:1633 M:57786298 (Ack:80981876)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:15.933]  [00:05:01.861][info  ][EM] <<< [E:4206i S:1633 M:80981877 (Ack:57786298)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:15.935]  [00:05:01.862][info  ][EM] ??1 [E:4206i S:1633 M:80981877] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5633ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:17.168]  [00:05:03.096][info  ][EM] >>> [E:4206i S:1633 M:57786299 (Ack:80981877)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:17.304]  [00:05:03.232][info  ][EM] <<< [E:4206i S:1633 M:80981878 (Ack:57786299)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:17.305]  [00:05:03.233][info  ][EM] ??1 [E:4206i S:1633 M:80981878] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:17.310]  [00:05:03.233][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:31:18.577]  [00:05:04.504][info  ][EM] >>> [E:4206i S:1633 M:57786300 (Ack:80981878)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:18.637]  [00:05:04.565][info  ][EM] <<< [E:4206i S:1633 M:80981879 (Ack:57786300)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:18.639]  [00:05:04.566][info  ][EM] ??1 [E:4206i S:1633 M:80981879] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:19.682]  [00:05:05.610][info  ][EM] >>> [E:4206i S:1633 M:57786301 (Ack:80981879)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:19.742]  [00:05:05.669][info  ][EM] <<< [E:4206i S:1633 M:80981880 (Ack:57786301)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:19.744]  [00:05:05.670][info  ][EM] ??1 [E:4206i S:1633 M:80981880] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:20.612]  [00:05:06.540][info  ][EM] >>> [E:4206i S:1633 M:57786302 (Ack:80981880)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:20.672]  [00:05:06.600][info  ][EM] <<< [E:4206i S:1633 M:80981881 (Ack:57786302)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:20.673]  [00:05:06.600][info  ][EM] ??1 [E:4206i S:1633 M:80981881] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:26.064]  [00:05:11.992][info  ][EM] <<1 [E:4206i S:1633 M:80981881] (S) Msg Retransmission to 1:0000000000000001
[18:31:26.064]  [00:05:11.993][info  ][EM] ??2 [E:4206i S:1633 M:80981881] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:31:26.364]  [00:05:12.291][info  ][EM] >>> [E:4206i S:1633 M:57786304 (Ack:80981881)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:31:28.226]  [00:05:14.155][info  ][EM] >>> [E:4206i S:1633 M:57786303 (Ack:80981881)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:28.365]  [00:05:14.292][info  ][EM] <<< [E:4206i S:1633 M:80981882 (Ack:57786303)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:28.366]  [00:05:14.293][info  ][EM] ??1 [E:4206i S:1633 M:80981882] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:28.371]  [00:05:14.293][error ][DL] Long dispatch time: 138 ms, for event type 2
[18:31:29.128]  [00:05:15.055][info  ][EM] >>> [E:4206i S:1633 M:57786305 (Ack:80981882)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:29.188]  [00:05:15.116][info  ][EM] <<< [E:4206i S:1633 M:80981883 (Ack:57786305)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:29.189]  [00:05:15.117][info  ][EM] ??1 [E:4206i S:1633 M:80981883] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:29.925]  [00:05:15.853][info  ][EM] >>> [E:4206i S:1633 M:57786306 (Ack:80981883)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:29.985]  [00:05:15.914][info  ][EM] <<< [E:4206i S:1633 M:80981884 (Ack:57786306)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:29.987]  [00:05:15.915][info  ][EM] ??1 [E:4206i S:1633 M:80981884] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:31.459]  [00:05:17.387][info  ][EM] >>> [E:4206i S:1633 M:57786307 (Ack:80981884)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:31.520]  [00:05:17.448][info  ][EM] <<< [E:4206i S:1633 M:80981885 (Ack:57786307)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:31.521]  [00:05:17.449][info  ][EM] ??1 [E:4206i S:1633 M:80981885] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5598ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:32.448]  [00:05:18.376][info  ][EM] >>> [E:4206i S:1633 M:57786308 (Ack:80981885)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:32.582]  [00:05:18.510][info  ][EM] <<< [E:4206i S:1633 M:80981886 (Ack:57786308)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:32.584]  [00:05:18.511][info  ][EM] ??1 [E:4206i S:1633 M:80981886] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:32.589]  [00:05:18.511][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:31:33.555]  [00:05:19.483][info  ][EM] >>> [E:4206i S:1633 M:57786309 (Ack:80981886)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:33.615]  [00:05:19.543][info  ][EM] <<< [E:4206i S:1633 M:80981887 (Ack:57786309)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:33.617]  [00:05:19.544][info  ][EM] ??1 [E:4206i S:1633 M:80981887] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:34.682]  [00:05:20.610][info  ][EM] >>> [E:4206i S:1633 M:57786310 (Ack:80981887)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:34.741]  [00:05:20.670][info  ][EM] <<< [E:4206i S:1633 M:80981888 (Ack:57786310)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:34.744]  [00:05:20.670][info  ][EM] ??1 [E:4206i S:1633 M:80981888] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5430ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:40.171]  [00:05:26.100][info  ][EM] <<1 [E:4206i S:1633 M:80981888] (S) Msg Retransmission to 1:0000000000000001
[18:31:40.171]  [00:05:26.101][info  ][EM] ??2 [E:4206i S:1633 M:80981888] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:31:40.482]  [00:05:26.410][info  ][EM] >>> [E:4206i S:1633 M:57786312 (Ack:80981888)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:31:41.797]  [00:05:27.725][info  ][EM] >>> [E:4206i S:1633 M:57786311 (Ack:80981888)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:41.857]  [00:05:27.786][info  ][EM] <<< [E:4206i S:1633 M:80981889 (Ack:57786311)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:41.859]  [00:05:27.787][info  ][EM] ??1 [E:4206i S:1633 M:80981889] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5430ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:43.133]  [00:05:29.061][info  ][EM] >>> [E:4206i S:1633 M:57786313 (Ack:80981889)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:43.266]  [00:05:29.195][info  ][EM] <<< [E:4206i S:1633 M:80981890 (Ack:57786313)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:43.268]  [00:05:29.196][info  ][EM] ??1 [E:4206i S:1633 M:80981890] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5549ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:43.273]  [00:05:29.196][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:31:47.044]  [00:05:32.972][info  ][EM] >>> [E:4206i S:1633 M:57786314 (Ack:80981890)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:47.104]  [00:05:33.033][info  ][EM] <<< [E:4206i S:1633 M:80981891 (Ack:57786314)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:47.105]  [00:05:33.034][info  ][EM] ??1 [E:4206i S:1633 M:80981891] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5678ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:50.912]  [00:05:36.841][info  ][EM] >>> [E:4206i S:1633 M:57786315 (Ack:80981891)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:50.972]  [00:05:36.902][info  ][EM] <<< [E:4206i S:1633 M:80981892 (Ack:57786315)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:50.975]  [00:05:36.903][info  ][EM] ??1 [E:4206i S:1633 M:80981892] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:52.223]  [00:05:38.151][info  ][EM] >>> [E:4206i S:1633 M:57786316 (Ack:80981892)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:52.283]  [00:05:38.211][info  ][EM] <<< [E:4206i S:1633 M:80981893 (Ack:57786316)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:52.284]  [00:05:38.211][info  ][EM] ??1 [E:4206i S:1633 M:80981893] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:53.440]  [00:05:39.369][info  ][EM] >>> [E:4206i S:1633 M:57786317 (Ack:80981893)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:53.574]  [00:05:39.502][info  ][EM] <<< [E:4206i S:1633 M:80981894 (Ack:57786317)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:53.575]  [00:05:39.503][info  ][EM] ??1 [E:4206i S:1633 M:80981894] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[18:31:53.583]  [00:05:39.503][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:31:57.486]  [00:05:43.415][info  ][EM] >>> [E:4206i S:1633 M:57786318 (Ack:80981894)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:31:57.546]  [00:05:43.475][info  ][EM] <<< [E:4206i S:1633 M:80981895 (Ack:57786318)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:31:57.547]  [00:05:43.476][info  ][EM] ??1 [E:4206i S:1633 M:80981895] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:01.688]  [00:05:47.617][info  ][EM] >>> [E:4206i S:1633 M:57786319 (Ack:80981895)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:01.748]  [00:05:47.677][info  ][EM] <<< [E:4206i S:1633 M:80981896 (Ack:57786319)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:01.749]  [00:05:47.678][info  ][EM] ??1 [E:4206i S:1633 M:80981896] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:02.805]  [00:05:48.734][info  ][EM] >>> [E:4206i S:1633 M:57786320 (Ack:80981896)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:02.866]  [00:05:48.794][info  ][EM] <<< [E:4206i S:1633 M:80981897 (Ack:57786320)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:02.867]  [00:05:48.795][info  ][EM] ??1 [E:4206i S:1633 M:80981897] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5495ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:04.028]  [00:05:49.958][info  ][EM] >>> [E:4206i S:1633 M:57786321 (Ack:80981897)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:04.162]  [00:05:50.091][info  ][EM] <<< [E:4206i S:1633 M:80981898 (Ack:57786321)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:04.163]  [00:05:50.091][info  ][EM] ??1 [E:4206i S:1633 M:80981898] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5203ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:04.168]  [00:05:50.092][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:32:04.939]  [00:05:50.868][info  ][EM] >>> [E:4206i S:1633 M:57786322 (Ack:80981898)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:04.999]  [00:05:50.928][info  ][EM] <<< [E:4206i S:1633 M:80981899 (Ack:57786322)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:05.001]  [00:05:50.929][info  ][EM] ??1 [E:4206i S:1633 M:80981899] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:08.987]  [00:05:54.916][info  ][EM] >>> [E:4206i S:1633 M:57786323 (Ack:80981899)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:09.047]  [00:05:54.977][info  ][EM] <<< [E:4206i S:1633 M:80981900 (Ack:57786323)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:09.050]  [00:05:54.977][info  ][EM] ??1 [E:4206i S:1633 M:80981900] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5291ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:09.880]  [00:05:55.809][info  ][EM] >>> [E:4206i S:1633 M:57786324 (Ack:80981900)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:09.941]  [00:05:55.870][info  ][EM] <<< [E:4206i S:1633 M:80981901 (Ack:57786324)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:09.942]  [00:05:55.871][info  ][EM] ??1 [E:4206i S:1633 M:80981901] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:15.365]  [00:06:01.282][info  ][EM] <<1 [E:4206i S:1633 M:80981901] (S) Msg Retransmission to 1:0000000000000001
[18:32:15.365]  [00:06:01.282][info  ][EM] ??2 [E:4206i S:1633 M:80981901] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:32:15.515]  [00:06:01.430][info  ][EM] >>> [E:4206i S:1633 M:57786326 (Ack:80981901)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:32:17.115]  [00:06:03.031][info  ][EM] >>> [E:4206i S:1633 M:57786325 (Ack:80981901)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:17.249]  [00:06:03.165][info  ][EM] <<< [E:4206i S:1633 M:80981902 (Ack:57786325)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:17.249]  [00:06:03.166][info  ][EM] ??1 [E:4206i S:1633 M:80981902] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:17.249]  [00:06:03.166][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:32:18.132]  [00:06:04.053][info  ][EM] >>> [E:4206i S:1633 M:57786327 (Ack:80981902)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:18.198]  [00:06:04.114][info  ][EM] <<< [E:4206i S:1633 M:80981903 (Ack:57786327)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:18.198]  [00:06:04.114][info  ][EM] ??1 [E:4206i S:1633 M:80981903] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:22.081]  [00:06:08.006][info  ][EM] >>> [E:4206i S:1633 M:57786328 (Ack:80981903)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:22.149]  [00:06:08.067][info  ][EM] <<< [E:4206i S:1633 M:80981904 (Ack:57786328)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:22.149]  [00:06:08.068][info  ][EM] ??1 [E:4206i S:1633 M:80981904] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:22.885]  [00:06:08.814][info  ][EM] >>> [E:4206i S:1633 M:57786329 (Ack:80981904)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:22.948]  [00:06:08.875][info  ][EM] <<< [E:4206i S:1633 M:80981905 (Ack:57786329)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:22.948]  [00:06:08.875][info  ][EM] ??1 [E:4206i S:1633 M:80981905] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:23.782]  [00:06:09.710][info  ][EM] >>> [E:4206i S:1633 M:57786330 (Ack:80981905)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:23.915]  [00:06:09.844][info  ][EM] <<< [E:4206i S:1633 M:80981906 (Ack:57786330)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:23.915]  [00:06:09.845][info  ][EM] ??1 [E:4206i S:1633 M:80981906] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:23.931]  [00:06:09.845][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:32:29.121]  [00:06:15.050][info  ][EM] <<1 [E:4206i S:1633 M:80981906] (S) Msg Retransmission to 1:0000000000000001
[18:32:29.121]  [00:06:15.050][info  ][EM] ??2 [E:4206i S:1633 M:80981906] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5536ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:32:29.348]  [00:06:15.269][info  ][EM] >>> [E:4206i S:1633 M:57786332 (Ack:80981906)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:32:44.675]  [00:06:30.605][info  ][EM] >>> [E:4206i S:1633 M:57786331 (Ack:80981906)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:44.735]  [00:06:30.666][info  ][EM] <<< [E:4206i S:1633 M:80981907 (Ack:57786331)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:44.737]  [00:06:30.666][info  ][EM] ??1 [E:4206i S:1633 M:80981907] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5433ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:49.347]  [00:06:35.277][info  ][EM] >>> [E:4206i S:1633 M:57786333 (Ack:80981907)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:32:49.407]  [00:06:35.337][info  ][EM] <<< [E:4206i S:1633 M:80981908 (Ack:57786333)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:32:49.408]  [00:06:35.338][info  ][EM] ??1 [E:4206i S:1633 M:80981908] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5357ms from now [State:Active II:500 AI:2000 AT:4000]
[18:32:54.763]  [00:06:40.695][info  ][EM] <<1 [E:4206i S:1633 M:80981908] (S) Msg Retransmission to 1:0000000000000001
[18:32:54.763]  [00:06:40.696][info  ][EM] ??2 [E:4206i S:1633 M:80981908] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:32:55.240]  [00:06:41.170][info  ][EM] >>> [E:4206i S:1633 M:57786335 (Ack:80981908)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:33:02.033]  [00:06:47.963][info  ][EM] >>> [E:4206i S:1633 M:57786334 (Ack:80981908)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:02.093]  [00:06:48.024][info  ][EM] <<< [E:4206i S:1633 M:80981909 (Ack:57786334)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:02.094]  [00:06:48.024][info  ][EM] ??1 [E:4206i S:1633 M:80981909] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:07.768]  [00:06:53.700][info  ][EM] <<1 [E:4206i S:1633 M:80981909] (S) Msg Retransmission to 1:0000000000000001
[18:33:07.768]  [00:06:53.701][info  ][EM] ??2 [E:4206i S:1633 M:80981909] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:33:07.970]  [00:06:53.902][info  ][EM] >>> [E:4206i S:1633 M:57786337 (Ack:80981909)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:33:09.066]  [00:06:54.998][info  ][EM] >>> [E:4206i S:1633 M:57786336 (Ack:80981909)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:09.200]  [00:06:55.131][info  ][EM] <<< [E:4206i S:1633 M:80981910 (Ack:57786336)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:09.202]  [00:06:55.132][info  ][EM] ??1 [E:4206i S:1633 M:80981910] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5574ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:09.208]  [00:06:55.132][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:33:10.185]  [00:06:56.117][info  ][EM] >>> [E:4206i S:1633 M:57786338 (Ack:80981910)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:10.246]  [00:06:56.176][info  ][EM] <<< [E:4206i S:1633 M:80981911 (Ack:57786338)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:10.247]  [00:06:56.177][info  ][EM] ??1 [E:4206i S:1633 M:80981911] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5564ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:11.592]  [00:06:57.523][info  ][EM] >>> [E:4206i S:1633 M:57786339 (Ack:80981911)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:11.652]  [00:06:57.583][info  ][EM] <<< [E:4206i S:1633 M:80981912 (Ack:57786339)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:11.653]  [00:06:57.584][info  ][EM] ??1 [E:4206i S:1633 M:80981912] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5615ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:17.266]  [00:07:03.198][info  ][EM] <<1 [E:4206i S:1633 M:80981912] (S) Msg Retransmission to 1:0000000000000001
[18:33:17.266]  [00:07:03.199][info  ][EM] ??2 [E:4206i S:1633 M:80981912] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:33:17.719]  [00:07:03.651][info  ][EM] >>> [E:4206i S:1633 M:57786341 (Ack:80981912)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:33:18.841]  [00:07:04.771][info  ][EM] >>> [E:4206i S:1633 M:57786340 (Ack:80981912)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:18.901]  [00:07:04.832][info  ][EM] <<< [E:4206i S:1633 M:80981913 (Ack:57786340)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:18.902]  [00:07:04.833][info  ][EM] ??1 [E:4206i S:1633 M:80981913] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:19.763]  [00:07:05.695][info  ][EM] >>> [E:4206i S:1633 M:57786342 (Ack:80981913)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:19.899]  [00:07:05.831][info  ][EM] <<< [E:4206i S:1633 M:80981914 (Ack:57786342)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:19.901]  [00:07:05.832][info  ][EM] ??1 [E:4206i S:1633 M:80981914] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5437ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:19.905]  [00:07:05.832][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:33:24.325]  [00:07:10.255][info  ][EM] >>> [E:4206i S:1633 M:57786343 (Ack:80981914)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:24.384]  [00:07:10.316][info  ][EM] <<< [E:4206i S:1633 M:80981915 (Ack:57786343)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:24.386]  [00:07:10.317][info  ][EM] ??1 [E:4206i S:1633 M:80981915] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5340ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:25.446]  [00:07:11.378][info  ][EM] >>> [E:4206i S:1633 M:57786344 (Ack:80981915)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:25.507]  [00:07:11.439][info  ][EM] <<< [E:4206i S:1633 M:80981916 (Ack:57786344)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:25.509]  [00:07:11.439][info  ][EM] ??1 [E:4206i S:1633 M:80981916] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5319ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:26.560]  [00:07:12.492][info  ][EM] >>> [E:4206i S:1633 M:57786345 (Ack:80981916)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:26.621]  [00:07:12.552][info  ][EM] <<< [E:4206i S:1633 M:80981917 (Ack:57786345)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:26.622]  [00:07:12.552][info  ][EM] ??1 [E:4206i S:1633 M:80981917] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5357ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:27.374]  [00:07:13.306][info  ][EM] >>> [E:4206i S:1633 M:57786346 (Ack:80981917)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:27.509]  [00:07:13.440][info  ][EM] <<< [E:4206i S:1633 M:80981918 (Ack:57786346)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:27.510]  [00:07:13.441][info  ][EM] ??1 [E:4206i S:1633 M:80981918] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5379ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:27.514]  [00:07:13.441][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:33:32.888]  [00:07:18.820][info  ][EM] <<1 [E:4206i S:1633 M:80981918] (S) Msg Retransmission to 1:0000000000000001
[18:33:32.888]  [00:07:18.821][info  ][EM] ??2 [E:4206i S:1633 M:80981918] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:33:33.332]  [00:07:19.263][info  ][EM] >>> [E:4206i S:1633 M:57786348 (Ack:80981918)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:33:39.205]  [00:07:25.137][info  ][EM] >>> [E:4206i S:1633 M:57786347 (Ack:80981918)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:39.266]  [00:07:25.198][info  ][EM] <<< [E:4206i S:1633 M:80981919 (Ack:57786347)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:39.268]  [00:07:25.199][info  ][EM] ??1 [E:4206i S:1633 M:80981919] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:44.974]  [00:07:30.907][info  ][EM] <<1 [E:4206i S:1633 M:80981919] (S) Msg Retransmission to 1:0000000000000001
[18:33:44.974]  [00:07:30.907][info  ][EM] ??2 [E:4206i S:1633 M:80981919] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:33:45.211]  [00:07:31.143][info  ][EM] >>> [E:4206i S:1633 M:57786350 (Ack:80981919)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:33:46.538]  [00:07:32.470][info  ][EM] >>> [E:4206i S:1633 M:57786349 (Ack:80981919)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:46.599]  [00:07:32.531][info  ][EM] <<< [E:4206i S:1633 M:80981920 (Ack:57786349)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:46.600]  [00:07:32.532][info  ][EM] ??1 [E:4206i S:1633 M:80981920] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:51.026]  [00:07:36.958][info  ][EM] >>> [E:4206i S:1633 M:57786351 (Ack:80981920)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:51.086]  [00:07:37.019][info  ][EM] <<< [E:4206i S:1633 M:80981921 (Ack:57786351)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:51.088]  [00:07:37.019][info  ][EM] ??1 [E:4206i S:1633 M:80981921] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:52.176]  [00:07:38.109][info  ][EM] >>> [E:4206i S:1633 M:57786352 (Ack:80981921)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:52.310]  [00:07:38.243][info  ][EM] <<< [E:4206i S:1633 M:80981922 (Ack:57786352)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:52.312]  [00:07:38.244][info  ][EM] ??1 [E:4206i S:1633 M:80981922] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:52.317]  [00:07:38.244][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:33:52.981]  [00:07:38.914][info  ][EM] >>> [E:4206i S:1633 M:57786353 (Ack:80981922)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:53.042]  [00:07:38.974][info  ][EM] <<< [E:4206i S:1633 M:80981923 (Ack:57786353)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:53.043]  [00:07:38.975][info  ][EM] ??1 [E:4206i S:1633 M:80981923] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:57.399]  [00:07:43.331][info  ][EM] >>> [E:4206i S:1633 M:57786354 (Ack:80981923)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:57.460]  [00:07:43.391][info  ][EM] <<< [E:4206i S:1633 M:80981924 (Ack:57786354)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:57.461]  [00:07:43.392][info  ][EM] ??1 [E:4206i S:1633 M:80981924] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[18:33:58.708]  [00:07:44.641][info  ][EM] >>> [E:4206i S:1633 M:57786355 (Ack:80981924)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:33:58.769]  [00:07:44.701][info  ][EM] <<< [E:4206i S:1633 M:80981925 (Ack:57786355)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:33:58.770]  [00:07:44.702][info  ][EM] ??1 [E:4206i S:1633 M:80981925] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:00.145]  [00:07:46.078][info  ][EM] >>> [E:4206i S:1633 M:57786356 (Ack:80981925)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:00.279]  [00:07:46.211][info  ][EM] <<< [E:4206i S:1633 M:80981926 (Ack:57786356)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:00.280]  [00:07:46.212][info  ][EM] ??1 [E:4206i S:1633 M:80981926] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:00.286]  [00:07:46.212][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:34:06.004]  [00:07:51.937][info  ][EM] <<1 [E:4206i S:1633 M:80981926] (S) Msg Retransmission to 1:0000000000000001
[18:34:06.004]  [00:07:51.938][info  ][EM] ??2 [E:4206i S:1633 M:80981926] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:34:06.101]  [00:07:52.034][info  ][EM] >>> [E:4206i S:1633 M:57786358 (Ack:80981926)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:34:12.096]  [00:07:58.029][info  ][EM] >>> [E:4206i S:1633 M:57786357 (Ack:80981926)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:12.156]  [00:07:58.088][info  ][EM] <<< [E:4206i S:1633 M:80981927 (Ack:57786357)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:12.158]  [00:07:58.089][info  ][EM] ??1 [E:4206i S:1633 M:80981927] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5538ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:17.694]  [00:08:03.627][info  ][EM] <<1 [E:4206i S:1633 M:80981927] (S) Msg Retransmission to 1:0000000000000001
[18:34:17.694]  [00:08:03.627][info  ][EM] ??2 [E:4206i S:1633 M:80981927] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:34:17.786]  [00:08:03.718][info  ][EM] >>> [E:4206i S:1633 M:57786360 (Ack:80981927)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:34:18.587]  [00:08:04.520][info  ][EM] >>> [E:4206i S:1633 M:57786359 (Ack:80981927)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:18.648]  [00:08:04.581][info  ][EM] <<< [E:4206i S:1633 M:80981928 (Ack:57786359)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:18.649]  [00:08:04.582][info  ][EM] ??1 [E:4206i S:1633 M:80981928] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5534ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:24.183]  [00:08:10.116][info  ][EM] <<1 [E:4206i S:1633 M:80981928] (S) Msg Retransmission to 1:0000000000000001
[18:34:24.183]  [00:08:10.116][info  ][EM] ??2 [E:4206i S:1633 M:80981928] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:34:24.450]  [00:08:10.383][info  ][EM] >>> [E:4206i S:1633 M:57786362 (Ack:80981928)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:34:25.739]  [00:08:11.672][info  ][EM] >>> [E:4206i S:1633 M:57786361 (Ack:80981928)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:25.800]  [00:08:11.732][info  ][EM] <<< [E:4206i S:1633 M:80981929 (Ack:57786361)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:25.801]  [00:08:11.733][info  ][EM] ??1 [E:4206i S:1633 M:80981929] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:26.970]  [00:08:12.903][info  ][EM] >>> [E:4206i S:1633 M:57786363 (Ack:80981929)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:27.103]  [00:08:13.037][info  ][EM] <<< [E:4206i S:1633 M:80981930 (Ack:57786363)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:27.105]  [00:08:13.038][info  ][EM] ??1 [E:4206i S:1633 M:80981930] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:27.110]  [00:08:13.038][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:34:27.864]  [00:08:13.796][info  ][EM] >>> [E:4206i S:1633 M:57786364 (Ack:80981930)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:27.925]  [00:08:13.857][info  ][EM] <<< [E:4206i S:1633 M:80981931 (Ack:57786364)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:27.926]  [00:08:13.858][info  ][EM] ??1 [E:4206i S:1633 M:80981931] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:33.505]  [00:08:19.439][info  ][EM] <<1 [E:4206i S:1633 M:80981931] (S) Msg Retransmission to 1:0000000000000001
[18:34:33.505]  [00:08:19.439][info  ][EM] ??2 [E:4206i S:1633 M:80981931] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5465ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:34:33.848]  [00:08:19.782][info  ][EM] >>> [E:4206i S:1633 M:57786366 (Ack:80981931)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:34:34.967]  [00:08:20.900][info  ][EM] >>> [E:4206i S:1633 M:57786365 (Ack:80981931)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:35.027]  [00:08:20.960][info  ][EM] <<< [E:4206i S:1633 M:80981932 (Ack:57786365)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:35.029]  [00:08:20.961][info  ][EM] ??1 [E:4206i S:1633 M:80981932] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:36.186]  [00:08:22.119][info  ][EM] >>> [E:4206i S:1633 M:57786367 (Ack:80981932)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:36.247]  [00:08:22.179][info  ][EM] <<< [E:4206i S:1633 M:80981933 (Ack:57786367)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:36.248]  [00:08:22.180][info  ][EM] ??1 [E:4206i S:1633 M:80981933] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5256ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:37.105]  [00:08:23.038][info  ][EM] >>> [E:4206i S:1633 M:57786368 (Ack:80981933)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:37.239]  [00:08:23.171][info  ][EM] <<< [E:4206i S:1633 M:80981934 (Ack:57786368)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:37.239]  [00:08:23.172][info  ][EM] ??1 [E:4206i S:1633 M:80981934] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5441ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:37.246]  [00:08:23.173][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:34:38.004]  [00:08:23.938][info  ][EM] >>> [E:4206i S:1633 M:57786369 (Ack:80981934)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:38.065]  [00:08:23.998][info  ][EM] <<< [E:4206i S:1633 M:80981935 (Ack:57786369)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:38.066]  [00:08:23.999][info  ][EM] ??1 [E:4206i S:1633 M:80981935] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:39.104]  [00:08:25.038][info  ][EM] >>> [E:4206i S:1633 M:57786370 (Ack:80981935)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:39.164]  [00:08:25.097][info  ][EM] <<< [E:4206i S:1633 M:80981936 (Ack:57786370)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:39.166]  [00:08:25.098][info  ][EM] ??1 [E:4206i S:1633 M:80981936] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:40.009]  [00:08:25.943][info  ][EM] >>> [E:4206i S:1633 M:57786371 (Ack:80981936)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:40.070]  [00:08:26.002][info  ][EM] <<< [E:4206i S:1633 M:80981937 (Ack:57786371)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:40.071]  [00:08:26.003][info  ][EM] ??1 [E:4206i S:1633 M:80981937] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:40.791]  [00:08:26.725][info  ][EM] >>> [E:4206i S:1633 M:57786372 (Ack:80981937)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:40.925]  [00:08:26.859][info  ][EM] <<< [E:4206i S:1633 M:80981938 (Ack:57786372)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:40.927]  [00:08:26.860][info  ][EM] ??1 [E:4206i S:1633 M:80981938] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:40.934]  [00:08:26.860][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:34:41.827]  [00:08:27.760][info  ][EM] >>> [E:4206i S:1633 M:57786373 (Ack:80981938)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:41.888]  [00:08:27.821][info  ][EM] <<< [E:4206i S:1633 M:80981939 (Ack:57786373)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:41.889]  [00:08:27.822][info  ][EM] ??1 [E:4206i S:1633 M:80981939] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5549ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:45.832]  [00:08:31.765][info  ][EM] >>> [E:4206i S:1633 M:57786374 (Ack:80981939)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:45.892]  [00:08:31.826][info  ][EM] <<< [E:4206i S:1633 M:80981940 (Ack:57786374)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:45.894]  [00:08:31.826][info  ][EM] ??1 [E:4206i S:1633 M:80981940] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:47.061]  [00:08:32.994][info  ][EM] >>> [E:4206i S:1633 M:57786375 (Ack:80981940)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:47.121]  [00:08:33.054][info  ][EM] <<< [E:4206i S:1633 M:80981941 (Ack:57786375)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:47.122]  [00:08:33.055][info  ][EM] ??1 [E:4206i S:1633 M:80981941] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:52.746]  [00:08:38.679][info  ][EM] <<1 [E:4206i S:1633 M:80981941] (S) Msg Retransmission to 1:0000000000000001
[18:34:52.746]  [00:08:38.679][info  ][EM] ??2 [E:4206i S:1633 M:80981941] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:34:54.744]  [00:08:40.677][info  ][EM] >>> [E:4206i S:1633 M:57786376 (Ack:80981941)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:54.878]  [00:08:40.811][info  ][EM] <<< [E:4206i S:1633 M:80981942 (Ack:57786376)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:54.879]  [00:08:40.812][info  ][EM] ??1 [E:4206i S:1633 M:80981942] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5641ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:54.884]  [00:08:40.813][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:34:55.540]  [00:08:41.474][info  ][EM] >>> [E:4206i S:1633 M:57786378 (Ack:80981942)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:55.601]  [00:08:41.535][info  ][EM] <<< [E:4206i S:1633 M:80981943 (Ack:57786378)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:55.602]  [00:08:41.535][info  ][EM] ??1 [E:4206i S:1633 M:80981943] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:56.746]  [00:08:42.679][info  ][EM] >>> [E:4206i S:1633 M:57786379 (Ack:80981943)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:56.806]  [00:08:42.740][info  ][EM] <<< [E:4206i S:1633 M:80981944 (Ack:57786379)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:56.808]  [00:08:42.741][info  ][EM] ??1 [E:4206i S:1633 M:80981944] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[18:34:57.646]  [00:08:43.579][info  ][EM] >>> [E:4206i S:1633 M:57786380 (Ack:80981944)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:34:57.706]  [00:08:43.639][info  ][EM] <<< [E:4206i S:1633 M:80981945 (Ack:57786380)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:34:57.707]  [00:08:43.640][info  ][EM] ??1 [E:4206i S:1633 M:80981945] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5699ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:01.082]  [00:08:47.016][info  ][EM] >>> [E:4206i S:1633 M:57786381 (Ack:80981945)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:01.216]  [00:08:47.150][info  ][EM] <<< [E:4206i S:1633 M:80981946 (Ack:57786381)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:01.217]  [00:08:47.151][info  ][EM] ??1 [E:4206i S:1633 M:80981946] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5562ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:01.223]  [00:08:47.151][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:35:04.780]  [00:08:50.713][info  ][EM] >>> [E:4206i S:1633 M:57786382 (Ack:80981946)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:04.841]  [00:08:50.774][info  ][EM] <<< [E:4206i S:1633 M:80981947 (Ack:57786382)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:04.842]  [00:08:50.775][info  ][EM] ??1 [E:4206i S:1633 M:80981947] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5549ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:06.009]  [00:08:51.942][info  ][EM] >>> [E:4206i S:1633 M:57786383 (Ack:80981947)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:06.069]  [00:08:52.002][info  ][EM] <<< [E:4206i S:1633 M:80981948 (Ack:57786383)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:06.070]  [00:08:52.003][info  ][EM] ??1 [E:4206i S:1633 M:80981948] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5351ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:07.125]  [00:08:53.059][info  ][EM] >>> [E:4206i S:1633 M:57786384 (Ack:80981948)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:07.186]  [00:08:53.119][info  ][EM] <<< [E:4206i S:1633 M:80981949 (Ack:57786384)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:07.187]  [00:08:53.120][info  ][EM] ??1 [E:4206i S:1633 M:80981949] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:08.251]  [00:08:54.185][info  ][EM] >>> [E:4206i S:1633 M:57786385 (Ack:80981949)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:08.385]  [00:08:54.319][info  ][EM] <<< [E:4206i S:1633 M:80981950 (Ack:57786385)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:08.387]  [00:08:54.320][info  ][EM] ??1 [E:4206i S:1633 M:80981950] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:08.392]  [00:08:54.320][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:35:09.066]  [00:08:55.000][info  ][EM] >>> [E:4206i S:1633 M:57786386 (Ack:80981950)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:09.126]  [00:08:55.060][info  ][EM] <<< [E:4206i S:1633 M:80981951 (Ack:57786386)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:09.127]  [00:08:55.060][info  ][EM] ??1 [E:4206i S:1633 M:80981951] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5299ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:09.990]  [00:08:55.923][info  ][EM] >>> [E:4206i S:1633 M:57786387 (Ack:80981951)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:10.050]  [00:08:55.984][info  ][EM] <<< [E:4206i S:1633 M:80981952 (Ack:57786387)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:10.051]  [00:08:55.984][info  ][EM] ??1 [E:4206i S:1633 M:80981952] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:14.107]  [00:09:00.041][info  ][EM] >>> [E:4206i S:1633 M:57786388 (Ack:80981952)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:14.168]  [00:09:00.101][info  ][EM] <<< [E:4206i S:1633 M:80981953 (Ack:57786388)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:14.169]  [00:09:00.102][info  ][EM] ??1 [E:4206i S:1633 M:80981953] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:14.918]  [00:09:00.851][info  ][EM] >>> [E:4206i S:1633 M:57786389 (Ack:80981953)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:15.051]  [00:09:00.985][info  ][EM] <<< [E:4206i S:1633 M:80981954 (Ack:57786389)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:15.052]  [00:09:00.986][info  ][EM] ??1 [E:4206i S:1633 M:80981954] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:15.058]  [00:09:00.986][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:35:19.401]  [00:09:05.334][info  ][EM] >>> [E:4206i S:1633 M:57786390 (Ack:80981954)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:19.461]  [00:09:05.395][info  ][EM] <<< [E:4206i S:1633 M:80981955 (Ack:57786390)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:19.463]  [00:09:05.396][info  ][EM] ??1 [E:4206i S:1633 M:80981955] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:20.395]  [00:09:06.330][info  ][EM] >>> [E:4206i S:1633 M:57786391 (Ack:80981955)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:20.456]  [00:09:06.390][info  ][EM] <<< [E:4206i S:1633 M:80981956 (Ack:57786391)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:20.458]  [00:09:06.390][info  ][EM] ??1 [E:4206i S:1633 M:80981956] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:21.594]  [00:09:07.528][info  ][EM] >>> [E:4206i S:1633 M:57786392 (Ack:80981956)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:21.655]  [00:09:07.588][info  ][EM] <<< [E:4206i S:1633 M:80981957 (Ack:57786392)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:21.656]  [00:09:07.589][info  ][EM] ??1 [E:4206i S:1633 M:80981957] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5639ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:23.084]  [00:09:09.018][info  ][EM] >>> [E:4206i S:1633 M:57786393 (Ack:80981957)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:23.218]  [00:09:09.152][info  ][EM] <<< [E:4206i S:1633 M:80981958 (Ack:57786393)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:23.220]  [00:09:09.153][info  ][EM] ??1 [E:4206i S:1633 M:80981958] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:23.226]  [00:09:09.153][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:35:27.203]  [00:09:13.137][info  ][EM] >>> [E:4206i S:1633 M:57786394 (Ack:80981958)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:27.263]  [00:09:13.198][info  ][EM] <<< [E:4206i S:1633 M:80981959 (Ack:57786394)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:27.265]  [00:09:13.198][info  ][EM] ??1 [E:4206i S:1633 M:80981959] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:28.310]  [00:09:14.243][info  ][EM] >>> [E:4206i S:1633 M:57786395 (Ack:80981959)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:28.370]  [00:09:14.303][info  ][EM] <<< [E:4206i S:1633 M:80981960 (Ack:57786395)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:28.371]  [00:09:14.304][info  ][EM] ??1 [E:4206i S:1633 M:80981960] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5695ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:29.537]  [00:09:15.470][info  ][EM] >>> [E:4206i S:1633 M:57786396 (Ack:80981960)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:29.597]  [00:09:15.531][info  ][EM] <<< [E:4206i S:1633 M:80981961 (Ack:57786396)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:29.598]  [00:09:15.532][info  ][EM] ??1 [E:4206i S:1633 M:80981961] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:30.865]  [00:09:16.799][info  ][EM] >>> [E:4206i S:1633 M:57786397 (Ack:80981961)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:31.000]  [00:09:16.933][info  ][EM] <<< [E:4206i S:1633 M:80981962 (Ack:57786397)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:31.001]  [00:09:16.934][info  ][EM] ??1 [E:4206i S:1633 M:80981962] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:31.006]  [00:09:16.934][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:35:31.858]  [00:09:17.792][info  ][EM] >>> [E:4206i S:1633 M:57786398 (Ack:80981962)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:31.919]  [00:09:17.853][info  ][EM] <<< [E:4206i S:1633 M:80981963 (Ack:57786398)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:31.920]  [00:09:17.853][info  ][EM] ??1 [E:4206i S:1633 M:80981963] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:37.518]  [00:09:23.453][info  ][EM] <<1 [E:4206i S:1633 M:80981963] (S) Msg Retransmission to 1:0000000000000001
[18:35:37.518]  [00:09:23.454][info  ][EM] ??2 [E:4206i S:1633 M:80981963] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:35:37.750]  [00:09:23.683][info  ][EM] >>> [E:4206i S:1633 M:57786400 (Ack:80981963)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:35:38.989]  [00:09:24.922][info  ][EM] >>> [E:4206i S:1633 M:57786399 (Ack:80981963)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:39.049]  [00:09:24.983][info  ][EM] <<< [E:4206i S:1633 M:80981964 (Ack:57786399)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:39.051]  [00:09:24.984][info  ][EM] ??1 [E:4206i S:1633 M:80981964] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:39.775]  [00:09:25.708][info  ][EM] >>> [E:4206i S:1633 M:57786401 (Ack:80981964)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:39.835]  [00:09:25.769][info  ][EM] <<< [E:4206i S:1633 M:80981965 (Ack:57786401)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:39.836]  [00:09:25.770][info  ][EM] ??1 [E:4206i S:1633 M:80981965] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:40.670]  [00:09:26.604][info  ][EM] >>> [E:4206i S:1633 M:57786402 (Ack:80981965)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:40.804]  [00:09:26.738][info  ][EM] <<< [E:4206i S:1633 M:80981966 (Ack:57786402)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:40.805]  [00:09:26.739][info  ][EM] ??1 [E:4206i S:1633 M:80981966] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:40.810]  [00:09:26.739][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:35:45.006]  [00:09:30.941][info  ][EM] >>> [E:4206i S:1633 M:57786403 (Ack:80981966)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:45.067]  [00:09:31.001][info  ][EM] <<< [E:4206i S:1633 M:80981967 (Ack:57786403)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:45.068]  [00:09:31.001][info  ][EM] ??1 [E:4206i S:1633 M:80981967] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:46.102]  [00:09:32.037][info  ][EM] >>> [E:4206i S:1633 M:57786404 (Ack:80981967)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:46.163]  [00:09:32.096][info  ][EM] <<< [E:4206i S:1633 M:80981968 (Ack:57786404)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:46.164]  [00:09:32.097][info  ][EM] ??1 [E:4206i S:1633 M:80981968] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5284ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:46.900]  [00:09:32.833][info  ][EM] >>> [E:4206i S:1633 M:57786405 (Ack:80981968)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:46.960]  [00:09:32.893][info  ][EM] <<< [E:4206i S:1633 M:80981969 (Ack:57786405)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:46.961]  [00:09:32.894][info  ][EM] ??1 [E:4206i S:1633 M:80981969] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:51.679]  [00:09:37.613][info  ][EM] >>> [E:4206i S:1633 M:57786406 (Ack:80981969)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:51.813]  [00:09:37.747][info  ][EM] <<< [E:4206i S:1633 M:80981970 (Ack:57786406)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:51.814]  [00:09:37.748][info  ][EM] ??1 [E:4206i S:1633 M:80981970] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5271ms from now [State:Active II:500 AI:2000 AT:4000]
[18:35:51.820]  [00:09:37.749][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:35:57.085]  [00:09:43.019][info  ][EM] <<1 [E:4206i S:1633 M:80981970] (S) Msg Retransmission to 1:0000000000000001
[18:35:57.085]  [00:09:43.019][info  ][EM] ??2 [E:4206i S:1633 M:80981970] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5418ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:35:57.616]  [00:09:43.550][info  ][EM] >>> [E:4206i S:1633 M:57786408 (Ack:80981970)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:35:58.906]  [00:09:44.839][info  ][EM] >>> [E:4206i S:1633 M:57786407 (Ack:80981970)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:35:58.966]  [00:09:44.900][info  ][EM] <<< [E:4206i S:1633 M:80981971 (Ack:57786407)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:35:58.967]  [00:09:44.901][info  ][EM] ??1 [E:4206i S:1633 M:80981971] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5409ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:00.329]  [00:09:46.262][info  ][EM] >>> [E:4206i S:1633 M:57786409 (Ack:80981971)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:00.388]  [00:09:46.323][info  ][EM] <<< [E:4206i S:1633 M:80981972 (Ack:57786409)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:00.389]  [00:09:46.324][info  ][EM] ??1 [E:4206i S:1633 M:80981972] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:04.992]  [00:09:50.926][info  ][EM] >>> [E:4206i S:1633 M:57786410 (Ack:80981972)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:05.051]  [00:09:50.986][info  ][EM] <<< [E:4206i S:1633 M:80981973 (Ack:57786410)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:05.054]  [00:09:50.987][info  ][EM] ??1 [E:4206i S:1633 M:80981973] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5663ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:10.715]  [00:09:56.650][info  ][EM] <<1 [E:4206i S:1633 M:80981973] (S) Msg Retransmission to 1:0000000000000001
[18:36:10.715]  [00:09:56.650][info  ][EM] ??2 [E:4206i S:1633 M:80981973] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:36:11.129]  [00:09:57.064][info  ][EM] >>> [E:4206i S:1633 M:57786412 (Ack:80981973)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:36:17.544]  [00:10:03.479][info  ][EM] >>> [E:4206i S:1633 M:57786411 (Ack:80981973)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:17.678]  [00:10:03.613][info  ][EM] <<< [E:4206i S:1633 M:80981974 (Ack:57786411)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:17.679]  [00:10:03.614][info  ][EM] ??1 [E:4206i S:1633 M:80981974] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:17.685]  [00:10:03.614][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:36:18.535]  [00:10:04.470][info  ][EM] >>> [E:4206i S:1633 M:57786413 (Ack:80981974)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:18.596]  [00:10:04.531][info  ][EM] <<< [E:4206i S:1633 M:80981975 (Ack:57786413)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:18.597]  [00:10:04.532][info  ][EM] ??1 [E:4206i S:1633 M:80981975] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:19.655]  [00:10:05.589][info  ][EM] >>> [E:4206i S:1633 M:57786414 (Ack:80981975)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:19.715]  [00:10:05.650][info  ][EM] <<< [E:4206i S:1633 M:80981976 (Ack:57786414)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:19.716]  [00:10:05.651][info  ][EM] ??1 [E:4206i S:1633 M:80981976] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:20.893]  [00:10:06.828][info  ][EM] >>> [E:4206i S:1633 M:57786415 (Ack:80981976)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:20.953]  [00:10:06.888][info  ][EM] <<< [E:4206i S:1633 M:80981977 (Ack:57786415)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:20.955]  [00:10:06.889][info  ][EM] ??1 [E:4206i S:1633 M:80981977] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5598ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:21.785]  [00:10:07.719][info  ][EM] >>> [E:4206i S:1633 M:57786416 (Ack:80981977)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:21.918]  [00:10:07.853][info  ][EM] <<< [E:4206i S:1633 M:80981978 (Ack:57786416)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:21.920]  [00:10:07.854][info  ][EM] ??1 [E:4206i S:1633 M:80981978] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:21.925]  [00:10:07.854][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:36:23.220]  [00:10:09.155][info  ][EM] >>> [E:4206i S:1633 M:57786417 (Ack:80981978)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:23.280]  [00:10:09.215][info  ][EM] <<< [E:4206i S:1633 M:80981979 (Ack:57786417)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:23.281]  [00:10:09.216][info  ][EM] ??1 [E:4206i S:1633 M:80981979] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:28.742]  [00:10:14.677][info  ][EM] <<1 [E:4206i S:1633 M:80981979] (S) Msg Retransmission to 1:0000000000000001
[18:36:28.742]  [00:10:14.678][info  ][EM] ??2 [E:4206i S:1633 M:80981979] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:36:28.960]  [00:10:14.895][info  ][EM] >>> [E:4206i S:1633 M:57786419 (Ack:80981979)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:36:30.363]  [00:10:16.297][info  ][EM] >>> [E:4206i S:1633 M:57786418 (Ack:80981979)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:30.423]  [00:10:16.358][info  ][EM] <<< [E:4206i S:1633 M:80981980 (Ack:57786418)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:30.424]  [00:10:16.359][info  ][EM] ??1 [E:4206i S:1633 M:80981980] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5428ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:31.368]  [00:10:17.303][info  ][EM] >>> [E:4206i S:1633 M:57786420 (Ack:80981980)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:31.428]  [00:10:17.364][info  ][EM] <<< [E:4206i S:1633 M:80981981 (Ack:57786420)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:31.430]  [00:10:17.365][info  ][EM] ??1 [E:4206i S:1633 M:80981981] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:32.491]  [00:10:18.426][info  ][EM] >>> [E:4206i S:1633 M:57786421 (Ack:80981981)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:32.625]  [00:10:18.560][info  ][EM] <<< [E:4206i S:1633 M:80981982 (Ack:57786421)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:32.627]  [00:10:18.561][info  ][EM] ??1 [E:4206i S:1633 M:80981982] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:32.633]  [00:10:18.561][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:36:36.300]  [00:10:22.235][info  ][EM] >>> [E:4206i S:1633 M:57786422 (Ack:80981982)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:36.361]  [00:10:22.295][info  ][EM] <<< [E:4206i S:1633 M:80981983 (Ack:57786422)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:36.362]  [00:10:22.296][info  ][EM] ??1 [E:4206i S:1633 M:80981983] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5538ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:37.310]  [00:10:23.245][info  ][EM] >>> [E:4206i S:1633 M:57786423 (Ack:80981983)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:37.371]  [00:10:23.305][info  ][EM] <<< [E:4206i S:1633 M:80981984 (Ack:57786423)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:37.372]  [00:10:23.306][info  ][EM] ??1 [E:4206i S:1633 M:80981984] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:38.601]  [00:10:24.536][info  ][EM] >>> [E:4206i S:1633 M:57786424 (Ack:80981984)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:38.661]  [00:10:24.596][info  ][EM] <<< [E:4206i S:1633 M:80981985 (Ack:57786424)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:38.662]  [00:10:24.597][info  ][EM] ??1 [E:4206i S:1633 M:80981985] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:42.928]  [00:10:28.864][info  ][EM] >>> [E:4206i S:1633 M:57786425 (Ack:80981985)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:43.062]  [00:10:28.998][info  ][EM] <<< [E:4206i S:1633 M:80981986 (Ack:57786425)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:43.064]  [00:10:28.999][info  ][EM] ??1 [E:4206i S:1633 M:80981986] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:43.068]  [00:10:28.999][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:36:46.756]  [00:10:32.691][info  ][EM] >>> [E:4206i S:1633 M:57786426 (Ack:80981986)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:46.816]  [00:10:32.751][info  ][EM] <<< [E:4206i S:1633 M:80981987 (Ack:57786426)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:46.818]  [00:10:32.752][info  ][EM] ??1 [E:4206i S:1633 M:80981987] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:47.535]  [00:10:33.470][info  ][EM] >>> [E:4206i S:1633 M:57786427 (Ack:80981987)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:47.595]  [00:10:33.531][info  ][EM] <<< [E:4206i S:1633 M:80981988 (Ack:57786427)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:47.597]  [00:10:33.532][info  ][EM] ??1 [E:4206i S:1633 M:80981988] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:51.148]  [00:10:37.083][info  ][EM] >>> [E:4206i S:1633 M:57786428 (Ack:80981988)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:51.208]  [00:10:37.144][info  ][EM] <<< [E:4206i S:1633 M:80981989 (Ack:57786428)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:51.210]  [00:10:37.145][info  ][EM] ??1 [E:4206i S:1633 M:80981989] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:52.242]  [00:10:38.178][info  ][EM] >>> [E:4206i S:1633 M:57786429 (Ack:80981989)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:52.376]  [00:10:38.312][info  ][EM] <<< [E:4206i S:1633 M:80981990 (Ack:57786429)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:52.377]  [00:10:38.312][info  ][EM] ??1 [E:4206i S:1633 M:80981990] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:52.381]  [00:10:38.313][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:36:53.358]  [00:10:39.293][info  ][EM] >>> [E:4206i S:1633 M:57786430 (Ack:80981990)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:53.418]  [00:10:39.354][info  ][EM] <<< [E:4206i S:1633 M:80981991 (Ack:57786430)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:53.420]  [00:10:39.355][info  ][EM] ??1 [E:4206i S:1633 M:80981991] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:54.141]  [00:10:40.077][info  ][EM] >>> [E:4206i S:1633 M:57786431 (Ack:80981991)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:54.201]  [00:10:40.137][info  ][EM] <<< [E:4206i S:1633 M:80981992 (Ack:57786431)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:54.202]  [00:10:40.137][info  ][EM] ??1 [E:4206i S:1633 M:80981992] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5650ms from now [State:Active II:500 AI:2000 AT:4000]
[18:36:55.243]  [00:10:41.179][info  ][EM] >>> [E:4206i S:1633 M:57786432 (Ack:80981992)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:36:55.303]  [00:10:41.240][info  ][EM] <<< [E:4206i S:1633 M:80981993 (Ack:57786432)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:36:55.306]  [00:10:41.241][info  ][EM] ??1 [E:4206i S:1633 M:80981993] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5592ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:00.896]  [00:10:46.833][info  ][EM] <<1 [E:4206i S:1633 M:80981993] (S) Msg Retransmission to 1:0000000000000001
[18:37:00.896]  [00:10:46.833][info  ][EM] ??2 [E:4206i S:1633 M:80981993] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:37:01.210]  [00:10:47.145][info  ][EM] >>> [E:4206i S:1633 M:57786434 (Ack:80981993)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:37:02.205]  [00:10:48.142][info  ][EM] >>> [E:4206i S:1633 M:57786433 (Ack:80981993)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:02.339]  [00:10:48.276][info  ][EM] <<< [E:4206i S:1633 M:80981994 (Ack:57786433)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:02.340]  [00:10:48.276][info  ][EM] ??1 [E:4206i S:1633 M:80981994] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:02.346]  [00:10:48.277][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:37:06.354]  [00:10:52.291][info  ][EM] >>> [E:4206i S:1633 M:57786435 (Ack:80981994)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:06.414]  [00:10:52.351][info  ][EM] <<< [E:4206i S:1633 M:80981995 (Ack:57786435)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:06.416]  [00:10:52.352][info  ][EM] ??1 [E:4206i S:1633 M:80981995] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:07.455]  [00:10:53.392][info  ][EM] >>> [E:4206i S:1633 M:57786436 (Ack:80981995)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:07.515]  [00:10:53.453][info  ][EM] <<< [E:4206i S:1633 M:80981996 (Ack:57786436)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:07.517]  [00:10:53.453][info  ][EM] ??1 [E:4206i S:1633 M:80981996] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5577ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:08.583]  [00:10:54.519][info  ][EM] >>> [E:4206i S:1633 M:57786437 (Ack:80981996)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:08.643]  [00:10:54.580][info  ][EM] <<< [E:4206i S:1633 M:80981997 (Ack:57786437)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:08.645]  [00:10:54.581][info  ][EM] ??1 [E:4206i S:1633 M:80981997] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:09.377]  [00:10:55.313][info  ][EM] >>> [E:4206i S:1633 M:57786438 (Ack:80981997)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:09.510]  [00:10:55.447][info  ][EM] <<< [E:4206i S:1633 M:80981998 (Ack:57786438)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:09.511]  [00:10:55.448][info  ][EM] ??1 [E:4206i S:1633 M:80981998] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:09.516]  [00:10:55.448][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:37:10.502]  [00:10:56.438][info  ][EM] >>> [E:4206i S:1633 M:57786439 (Ack:80981998)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:10.561]  [00:10:56.498][info  ][EM] <<< [E:4206i S:1633 M:80981999 (Ack:57786439)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:10.563]  [00:10:56.499][info  ][EM] ??1 [E:4206i S:1633 M:80981999] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:11.295]  [00:10:57.232][info  ][EM] >>> [E:4206i S:1633 M:57786440 (Ack:80981999)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:11.356]  [00:10:57.292][info  ][EM] <<< [E:4206i S:1633 M:80982000 (Ack:57786440)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:11.357]  [00:10:57.293][info  ][EM] ??1 [E:4206i S:1633 M:80982000] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5600ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:15.327]  [00:11:01.263][info  ][EM] >>> [E:4206i S:1633 M:57786441 (Ack:80982000)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:15.386]  [00:11:01.324][info  ][EM] <<< [E:4206i S:1633 M:80982001 (Ack:57786441)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:15.388]  [00:11:01.324][info  ][EM] ??1 [E:4206i S:1633 M:80982001] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5418ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:16.414]  [00:11:02.351][info  ][EM] >>> [E:4206i S:1633 M:57786442 (Ack:80982001)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:16.548]  [00:11:02.485][info  ][EM] <<< [E:4206i S:1633 M:80982002 (Ack:57786442)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:16.549]  [00:11:02.486][info  ][EM] ??1 [E:4206i S:1633 M:80982002] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5254ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:16.556]  [00:11:02.486][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:37:20.950]  [00:11:06.886][info  ][EM] >>> [E:4206i S:1633 M:57786443 (Ack:80982002)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:21.010]  [00:11:06.947][info  ][EM] <<< [E:4206i S:1633 M:80982003 (Ack:57786443)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:21.011]  [00:11:06.948][info  ][EM] ??1 [E:4206i S:1633 M:80982003] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5549ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:21.721]  [00:11:07.658][info  ][EM] >>> [E:4206i S:1633 M:57786444 (Ack:80982003)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:21.781]  [00:11:07.718][info  ][EM] <<< [E:4206i S:1633 M:80982004 (Ack:57786444)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:21.782]  [00:11:07.718][info  ][EM] ??1 [E:4206i S:1633 M:80982004] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:22.504]  [00:11:08.441][info  ][EM] >>> [E:4206i S:1633 M:57786445 (Ack:80982004)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:22.564]  [00:11:08.501][info  ][EM] <<< [E:4206i S:1633 M:80982005 (Ack:57786445)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:22.565]  [00:11:08.501][info  ][EM] ??1 [E:4206i S:1633 M:80982005] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5738ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:23.507]  [00:11:09.444][info  ][EM] >>> [E:4206i S:1633 M:57786446 (Ack:80982005)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:23.641]  [00:11:09.578][info  ][EM] <<< [E:4206i S:1633 M:80982006 (Ack:57786446)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:23.642]  [00:11:09.579][info  ][EM] ??1 [E:4206i S:1633 M:80982006] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:23.647]  [00:11:09.579][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:37:25.250]  [00:11:11.187][info  ][EM] >>> [E:4206i S:1633 M:57786447 (Ack:80982006)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:25.311]  [00:11:11.248][info  ][EM] <<< [E:4206i S:1633 M:80982007 (Ack:57786447)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:25.312]  [00:11:11.249][info  ][EM] ??1 [E:4206i S:1633 M:80982007] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5345ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:26.150]  [00:11:12.087][info  ][EM] >>> [E:4206i S:1633 M:57786448 (Ack:80982007)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:26.211]  [00:11:12.148][info  ][EM] <<< [E:4206i S:1633 M:80982008 (Ack:57786448)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:26.212]  [00:11:12.148][info  ][EM] ??1 [E:4206i S:1633 M:80982008] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:27.044]  [00:11:12.981][info  ][EM] >>> [E:4206i S:1633 M:57786449 (Ack:80982008)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:27.104]  [00:11:13.041][info  ][EM] <<< [E:4206i S:1633 M:80982009 (Ack:57786449)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:27.106]  [00:11:13.042][info  ][EM] ??1 [E:4206i S:1633 M:80982009] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:27.830]  [00:11:13.767][info  ][EM] >>> [E:4206i S:1633 M:57786450 (Ack:80982009)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:27.964]  [00:11:13.901][info  ][EM] <<< [E:4206i S:1633 M:80982010 (Ack:57786450)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:27.965]  [00:11:13.902][info  ][EM] ??1 [E:4206i S:1633 M:80982010] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:27.969]  [00:11:13.902][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:37:28.830]  [00:11:14.766][info  ][EM] >>> [E:4206i S:1633 M:57786451 (Ack:80982010)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:28.890]  [00:11:14.827][info  ][EM] <<< [E:4206i S:1633 M:80982011 (Ack:57786451)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:28.891]  [00:11:14.828][info  ][EM] ??1 [E:4206i S:1633 M:80982011] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:34.382]  [00:11:20.319][info  ][EM] <<1 [E:4206i S:1633 M:80982011] (S) Msg Retransmission to 1:0000000000000001
[18:37:34.382]  [00:11:20.319][info  ][EM] ??2 [E:4206i S:1633 M:80982011] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5282ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:37:34.608]  [00:11:20.545][info  ][EM] >>> [E:4206i S:1633 M:57786453 (Ack:80982011)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:37:40.466]  [00:11:26.404][info  ][EM] >>> [E:4206i S:1633 M:57786452 (Ack:80982011)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:40.527]  [00:11:26.464][info  ][EM] <<< [E:4206i S:1633 M:80982012 (Ack:57786452)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:40.529]  [00:11:26.465][info  ][EM] ??1 [E:4206i S:1633 M:80982012] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5645ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:44.607]  [00:11:30.544][info  ][EM] >>> [E:4206i S:1633 M:57786454 (Ack:80982012)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:44.668]  [00:11:30.605][info  ][EM] <<< [E:4206i S:1633 M:80982013 (Ack:57786454)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:44.669]  [00:11:30.606][info  ][EM] ??1 [E:4206i S:1633 M:80982013] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:45.375]  [00:11:31.313][info  ][EM] >>> [E:4206i S:1633 M:57786455 (Ack:80982013)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:45.510]  [00:11:31.447][info  ][EM] <<< [E:4206i S:1633 M:80982014 (Ack:57786455)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:45.511]  [00:11:31.448][info  ][EM] ??1 [E:4206i S:1633 M:80982014] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5725ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:45.516]  [00:11:31.449][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:37:46.261]  [00:11:32.199][info  ][EM] >>> [E:4206i S:1633 M:57786456 (Ack:80982014)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:46.321]  [00:11:32.259][info  ][EM] <<< [E:4206i S:1633 M:80982015 (Ack:57786456)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:46.324]  [00:11:32.260][info  ][EM] ??1 [E:4206i S:1633 M:80982015] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:47.472]  [00:11:33.410][info  ][EM] >>> [E:4206i S:1633 M:57786457 (Ack:80982015)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:47.533]  [00:11:33.470][info  ][EM] <<< [E:4206i S:1633 M:80982016 (Ack:57786457)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:47.534]  [00:11:33.471][info  ][EM] ??1 [E:4206i S:1633 M:80982016] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5562ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:53.094]  [00:11:39.033][info  ][EM] <<1 [E:4206i S:1633 M:80982016] (S) Msg Retransmission to 1:0000000000000001
[18:37:53.094]  [00:11:39.034][info  ][EM] ??2 [E:4206i S:1633 M:80982016] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5540ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:37:53.533]  [00:11:39.471][info  ][EM] >>> [E:4206i S:1633 M:57786459 (Ack:80982016)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:37:54.648]  [00:11:40.586][info  ][EM] >>> [E:4206i S:1633 M:57786458 (Ack:80982016)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:54.709]  [00:11:40.647][info  ][EM] <<< [E:4206i S:1633 M:80982017 (Ack:57786458)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:54.710]  [00:11:40.648][info  ][EM] ??1 [E:4206i S:1633 M:80982017] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:55.536]  [00:11:41.475][info  ][EM] >>> [E:4206i S:1633 M:57786460 (Ack:80982017)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:55.671]  [00:11:41.609][info  ][EM] <<< [E:4206i S:1633 M:80982018 (Ack:57786460)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:55.672]  [00:11:41.610][info  ][EM] ??1 [E:4206i S:1633 M:80982018] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:55.679]  [00:11:41.610][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:37:56.425]  [00:11:42.364][info  ][EM] >>> [E:4206i S:1633 M:57786461 (Ack:80982018)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:56.486]  [00:11:42.424][info  ][EM] <<< [E:4206i S:1633 M:80982019 (Ack:57786461)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:56.487]  [00:11:42.425][info  ][EM] ??1 [E:4206i S:1633 M:80982019] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[18:37:57.422]  [00:11:43.361][info  ][EM] >>> [E:4206i S:1633 M:57786462 (Ack:80982019)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:37:57.483]  [00:11:43.421][info  ][EM] <<< [E:4206i S:1633 M:80982020 (Ack:57786462)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:37:57.485]  [00:11:43.422][info  ][EM] ??1 [E:4206i S:1633 M:80982020] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5332ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:00.781]  [00:11:46.719][info  ][EM] >>> [E:4206i S:1633 M:57786463 (Ack:80982020)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:00.841]  [00:11:46.780][info  ][EM] <<< [E:4206i S:1633 M:80982021 (Ack:57786463)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:00.842]  [00:11:46.780][info  ][EM] ??1 [E:4206i S:1633 M:80982021] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:01.674]  [00:11:47.613][info  ][EM] >>> [E:4206i S:1633 M:57786464 (Ack:80982021)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:01.808]  [00:11:47.747][info  ][EM] <<< [E:4206i S:1633 M:80982022 (Ack:57786464)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:01.810]  [00:11:47.748][info  ][EM] ??1 [E:4206i S:1633 M:80982022] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5658ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:01.814]  [00:11:47.748][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:38:02.803]  [00:11:48.742][info  ][EM] >>> [E:4206i S:1633 M:57786465 (Ack:80982022)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:02.863]  [00:11:48.801][info  ][EM] <<< [E:4206i S:1633 M:80982023 (Ack:57786465)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:02.864]  [00:11:48.802][info  ][EM] ??1 [E:4206i S:1633 M:80982023] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:06.621]  [00:11:52.559][info  ][EM] >>> [E:4206i S:1633 M:57786466 (Ack:80982023)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:06.681]  [00:11:52.620][info  ][EM] <<< [E:4206i S:1633 M:80982024 (Ack:57786466)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:06.682]  [00:11:52.620][info  ][EM] ??1 [E:4206i S:1633 M:80982024] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:07.439]  [00:11:53.377][info  ][EM] >>> [E:4206i S:1633 M:57786467 (Ack:80982024)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:07.499]  [00:11:53.438][info  ][EM] <<< [E:4206i S:1633 M:80982025 (Ack:57786467)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:07.500]  [00:11:53.439][info  ][EM] ??1 [E:4206i S:1633 M:80982025] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5407ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:12.906]  [00:11:58.846][info  ][EM] <<1 [E:4206i S:1633 M:80982025] (S) Msg Retransmission to 1:0000000000000001
[18:38:12.906]  [00:11:58.846][info  ][EM] ??2 [E:4206i S:1633 M:80982025] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5615ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:38:13.098]  [00:11:59.039][info  ][EM] >>> [E:4206i S:1633 M:57786469 (Ack:80982025)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:38:19.566]  [00:12:05.505][info  ][EM] >>> [E:4206i S:1633 M:57786468 (Ack:80982025)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:19.699]  [00:12:05.639][info  ][EM] <<< [E:4206i S:1633 M:80982026 (Ack:57786468)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:19.701]  [00:12:05.640][info  ][EM] ??1 [E:4206i S:1633 M:80982026] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5383ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:19.707]  [00:12:05.640][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:38:20.360]  [00:12:06.300][info  ][EM] >>> [E:4206i S:1633 M:57786470 (Ack:80982026)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:20.421]  [00:12:06.360][info  ][EM] <<< [E:4206i S:1633 M:80982027 (Ack:57786470)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:20.422]  [00:12:06.361][info  ][EM] ??1 [E:4206i S:1633 M:80982027] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5237ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:21.396]  [00:12:07.334][info  ][EM] >>> [E:4206i S:1633 M:57786471 (Ack:80982027)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:21.455]  [00:12:07.395][info  ][EM] <<< [E:4206i S:1633 M:80982028 (Ack:57786471)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:21.457]  [00:12:07.396][info  ][EM] ??1 [E:4206i S:1633 M:80982028] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:22.191]  [00:12:08.131][info  ][EM] >>> [E:4206i S:1633 M:57786472 (Ack:80982028)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:22.252]  [00:12:08.192][info  ][EM] <<< [E:4206i S:1633 M:80982029 (Ack:57786472)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:22.253]  [00:12:08.192][info  ][EM] ??1 [E:4206i S:1633 M:80982029] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5626ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:22.982]  [00:12:08.921][info  ][EM] >>> [E:4206i S:1633 M:57786473 (Ack:80982029)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:23.116]  [00:12:09.056][info  ][EM] <<< [E:4206i S:1633 M:80982030 (Ack:57786473)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:23.117]  [00:12:09.056][info  ][EM] ??1 [E:4206i S:1633 M:80982030] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:23.122]  [00:12:09.057][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:38:23.777]  [00:12:09.717][info  ][EM] >>> [E:4206i S:1633 M:57786474 (Ack:80982030)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:23.837]  [00:12:09.778][info  ][EM] <<< [E:4206i S:1633 M:80982031 (Ack:57786474)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:23.839]  [00:12:09.778][info  ][EM] ??1 [E:4206i S:1633 M:80982031] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5452ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:24.777]  [00:12:10.717][info  ][EM] >>> [E:4206i S:1633 M:57786475 (Ack:80982031)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:24.838]  [00:12:10.778][info  ][EM] <<< [E:4206i S:1633 M:80982032 (Ack:57786475)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:24.839]  [00:12:10.779][info  ][EM] ??1 [E:4206i S:1633 M:80982032] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5334ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:28.744]  [00:12:14.684][info  ][EM] >>> [E:4206i S:1633 M:57786476 (Ack:80982032)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:28.805]  [00:12:14.745][info  ][EM] <<< [E:4206i S:1633 M:80982033 (Ack:57786476)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:28.806]  [00:12:14.746][info  ][EM] ??1 [E:4206i S:1633 M:80982033] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:32.573]  [00:12:18.513][info  ][EM] >>> [E:4206i S:1633 M:57786477 (Ack:80982033)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:32.707]  [00:12:18.647][info  ][EM] <<< [E:4206i S:1633 M:80982034 (Ack:57786477)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:32.708]  [00:12:18.648][info  ][EM] ??1 [E:4206i S:1633 M:80982034] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5325ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:32.713]  [00:12:18.648][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:38:33.579]  [00:12:19.520][info  ][EM] >>> [E:4206i S:1633 M:57786478 (Ack:80982034)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:33.640]  [00:12:19.580][info  ][EM] <<< [E:4206i S:1633 M:80982035 (Ack:57786478)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:33.641]  [00:12:19.581][info  ][EM] ??1 [E:4206i S:1633 M:80982035] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:34.477]  [00:12:20.417][info  ][EM] >>> [E:4206i S:1633 M:57786479 (Ack:80982035)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:34.537]  [00:12:20.478][info  ][EM] <<< [E:4206i S:1633 M:80982036 (Ack:57786479)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:34.539]  [00:12:20.478][info  ][EM] ??1 [E:4206i S:1633 M:80982036] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5555ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:39.168]  [00:12:25.109][info  ][EM] >>> [E:4206i S:1633 M:57786480 (Ack:80982036)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:39.229]  [00:12:25.169][info  ][EM] <<< [E:4206i S:1633 M:80982037 (Ack:57786480)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:39.230]  [00:12:25.169][info  ][EM] ??1 [E:4206i S:1633 M:80982037] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5231ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:39.958]  [00:12:25.899][info  ][EM] >>> [E:4206i S:1633 M:57786481 (Ack:80982037)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:40.092]  [00:12:26.033][info  ][EM] <<< [E:4206i S:1633 M:80982038 (Ack:57786481)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:40.093]  [00:12:26.034][info  ][EM] ??1 [E:4206i S:1633 M:80982038] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:40.098]  [00:12:26.034][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:38:40.737]  [00:12:26.678][info  ][EM] >>> [E:4206i S:1633 M:57786482 (Ack:80982038)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:40.797]  [00:12:26.739][info  ][EM] <<< [E:4206i S:1633 M:80982039 (Ack:57786482)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:40.799]  [00:12:26.739][info  ][EM] ??1 [E:4206i S:1633 M:80982039] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5430ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:46.227]  [00:12:32.169][info  ][EM] <<1 [E:4206i S:1633 M:80982039] (S) Msg Retransmission to 1:0000000000000001
[18:38:46.227]  [00:12:32.169][info  ][EM] ??2 [E:4206i S:1633 M:80982039] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:38:46.401]  [00:12:32.343][info  ][EM] >>> [E:4206i S:1633 M:57786484 (Ack:80982039)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:38:47.780]  [00:12:33.722][info  ][EM] >>> [E:4206i S:1633 M:57786483 (Ack:80982039)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:47.841]  [00:12:33.782][info  ][EM] <<< [E:4206i S:1633 M:80982040 (Ack:57786483)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:47.842]  [00:12:33.783][info  ][EM] ??1 [E:4206i S:1633 M:80982040] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:52.309]  [00:12:38.251][info  ][EM] >>> [E:4206i S:1633 M:57786485 (Ack:80982040)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:52.370]  [00:12:38.312][info  ][EM] <<< [E:4206i S:1633 M:80982041 (Ack:57786485)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:52.371]  [00:12:38.312][info  ][EM] ??1 [E:4206i S:1633 M:80982041] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:57.875]  [00:12:43.818][info  ][EM] <<1 [E:4206i S:1633 M:80982041] (S) Msg Retransmission to 1:0000000000000001
[18:38:57.875]  [00:12:43.819][info  ][EM] ??2 [E:4206i S:1633 M:80982041] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:38:57.970]  [00:12:43.913][info  ][EM] >>> [E:4206i S:1633 M:57786487 (Ack:80982041)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:38:59.258]  [00:12:45.200][info  ][EM] >>> [E:4206i S:1633 M:57786486 (Ack:80982041)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:38:59.392]  [00:12:45.333][info  ][EM] <<< [E:4206i S:1633 M:80982042 (Ack:57786486)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:38:59.393]  [00:12:45.334][info  ][EM] ??1 [E:4206i S:1633 M:80982042] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5387ms from now [State:Active II:500 AI:2000 AT:4000]
[18:38:59.397]  [00:12:45.334][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:39:00.143]  [00:12:46.084][info  ][EM] >>> [E:4206i S:1633 M:57786488 (Ack:80982042)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:00.203]  [00:12:46.145][info  ][EM] <<< [E:4206i S:1633 M:80982043 (Ack:57786488)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:00.204]  [00:12:46.146][info  ][EM] ??1 [E:4206i S:1633 M:80982043] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5716ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:01.348]  [00:12:47.291][info  ][EM] >>> [E:4206i S:1633 M:57786489 (Ack:80982043)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:01.408]  [00:12:47.351][info  ][EM] <<< [E:4206i S:1633 M:80982044 (Ack:57786489)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:01.410]  [00:12:47.352][info  ][EM] ??1 [E:4206i S:1633 M:80982044] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:02.445]  [00:12:48.388][info  ][EM] >>> [E:4206i S:1633 M:57786490 (Ack:80982044)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:02.505]  [00:12:48.449][info  ][EM] <<< [E:4206i S:1633 M:80982045 (Ack:57786490)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:02.507]  [00:12:48.449][info  ][EM] ??1 [E:4206i S:1633 M:80982045] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:03.254]  [00:12:49.197][info  ][EM] >>> [E:4206i S:1633 M:57786491 (Ack:80982045)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:03.388]  [00:12:49.331][info  ][EM] <<< [E:4206i S:1633 M:80982046 (Ack:57786491)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:03.390]  [00:12:49.332][info  ][EM] ??1 [E:4206i S:1633 M:80982046] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5566ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:03.395]  [00:12:49.333][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:39:04.247]  [00:12:50.189][info  ][EM] >>> [E:4206i S:1633 M:57786492 (Ack:80982046)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:04.307]  [00:12:50.250][info  ][EM] <<< [E:4206i S:1633 M:80982047 (Ack:57786492)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:04.308]  [00:12:50.250][info  ][EM] ??1 [E:4206i S:1633 M:80982047] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5336ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:05.057]  [00:12:51.000][info  ][EM] >>> [E:4206i S:1633 M:57786493 (Ack:80982047)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:05.118]  [00:12:51.061][info  ][EM] <<< [E:4206i S:1633 M:80982048 (Ack:57786493)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:05.119]  [00:12:51.061][info  ][EM] ??1 [E:4206i S:1633 M:80982048] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5729ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:10.846]  [00:12:56.790][info  ][EM] <<1 [E:4206i S:1633 M:80982048] (S) Msg Retransmission to 1:0000000000000001
[18:39:10.846]  [00:12:56.791][info  ][EM] ??2 [E:4206i S:1633 M:80982048] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5362ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:39:11.153]  [00:12:57.096][info  ][EM] >>> [E:4206i S:1633 M:57786495 (Ack:80982048)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:39:11.667]  [00:12:57.609][info  ][EM] >>> [E:4206i S:1633 M:57786494 (Ack:80982048)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:11.726]  [00:12:57.669][info  ][EM] <<< [E:4206i S:1633 M:80982049 (Ack:57786494)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:11.728]  [00:12:57.669][info  ][EM] ??1 [E:4206i S:1633 M:80982049] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:15.466]  [00:13:01.410][info  ][EM] >>> [E:4206i S:1633 M:57786496 (Ack:80982049)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:15.601]  [00:13:01.543][info  ][EM] <<< [E:4206i S:1633 M:80982050 (Ack:57786496)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:15.602]  [00:13:01.544][info  ][EM] ??1 [E:4206i S:1633 M:80982050] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:15.606]  [00:13:01.544][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:39:19.404]  [00:13:05.346][info  ][EM] >>> [E:4206i S:1633 M:57786497 (Ack:80982050)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:19.464]  [00:13:05.407][info  ][EM] <<< [E:4206i S:1633 M:80982051 (Ack:57786497)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:19.466]  [00:13:05.408][info  ][EM] ??1 [E:4206i S:1633 M:80982051] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5209ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:20.199]  [00:13:06.142][info  ][EM] >>> [E:4206i S:1633 M:57786498 (Ack:80982051)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:20.259]  [00:13:06.203][info  ][EM] <<< [E:4206i S:1633 M:80982052 (Ack:57786498)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:20.261]  [00:13:06.203][info  ][EM] ??1 [E:4206i S:1633 M:80982052] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5744ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:23.722]  [00:13:09.666][info  ][EM] >>> [E:4206i S:1633 M:57786499 (Ack:80982052)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:23.783]  [00:13:09.726][info  ][EM] <<< [E:4206i S:1633 M:80982053 (Ack:57786499)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:23.784]  [00:13:09.726][info  ][EM] ??1 [E:4206i S:1633 M:80982053] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5622ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:27.750]  [00:13:13.693][info  ][EM] >>> [E:4206i S:1633 M:57786500 (Ack:80982053)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:27.884]  [00:13:13.827][info  ][EM] <<< [E:4206i S:1633 M:80982054 (Ack:57786500)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:27.885]  [00:13:13.828][info  ][EM] ??1 [E:4206i S:1633 M:80982054] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5327ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:27.890]  [00:13:13.828][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:39:28.537]  [00:13:14.481][info  ][EM] >>> [E:4206i S:1633 M:57786501 (Ack:80982054)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:28.599]  [00:13:14.541][info  ][EM] <<< [E:4206i S:1633 M:80982055 (Ack:57786501)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:28.600]  [00:13:14.542][info  ][EM] ??1 [E:4206i S:1633 M:80982055] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:32.019]  [00:13:17.961][info  ][EM] >>> [E:4206i S:1633 M:57786502 (Ack:80982055)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:32.079]  [00:13:18.022][info  ][EM] <<< [E:4206i S:1633 M:80982056 (Ack:57786502)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:32.081]  [00:13:18.023][info  ][EM] ??1 [E:4206i S:1633 M:80982056] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:33.118]  [00:13:19.061][info  ][EM] >>> [E:4206i S:1633 M:57786503 (Ack:80982056)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:33.178]  [00:13:19.121][info  ][EM] <<< [E:4206i S:1633 M:80982057 (Ack:57786503)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:33.180]  [00:13:19.122][info  ][EM] ??1 [E:4206i S:1633 M:80982057] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5609ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:34.013]  [00:13:19.956][info  ][EM] >>> [E:4206i S:1633 M:57786504 (Ack:80982057)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:34.147]  [00:13:20.089][info  ][EM] <<< [E:4206i S:1633 M:80982058 (Ack:57786504)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:34.148]  [00:13:20.090][info  ][EM] ??1 [E:4206i S:1633 M:80982058] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:34.153]  [00:13:20.090][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:39:34.910]  [00:13:20.852][info  ][EM] >>> [E:4206i S:1633 M:57786505 (Ack:80982058)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:34.970]  [00:13:20.913][info  ][EM] <<< [E:4206i S:1633 M:80982059 (Ack:57786505)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:34.971]  [00:13:20.914][info  ][EM] ??1 [E:4206i S:1633 M:80982059] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5712ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:40.683]  [00:13:26.626][info  ][EM] <<1 [E:4206i S:1633 M:80982059] (S) Msg Retransmission to 1:0000000000000001
[18:39:40.683]  [00:13:26.626][info  ][EM] ??2 [E:4206i S:1633 M:80982059] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:39:41.057]  [00:13:27.000][info  ][EM] >>> [E:4206i S:1633 M:57786507 (Ack:80982059)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:39:41.962]  [00:13:27.905][info  ][EM] >>> [E:4206i S:1633 M:57786506 (Ack:80982059)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:42.022]  [00:13:27.965][info  ][EM] <<< [E:4206i S:1633 M:80982060 (Ack:57786506)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:42.024]  [00:13:27.965][info  ][EM] ??1 [E:4206i S:1633 M:80982060] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:42.956]  [00:13:28.899][info  ][EM] >>> [E:4206i S:1633 M:57786508 (Ack:80982060)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:43.016]  [00:13:28.959][info  ][EM] <<< [E:4206i S:1633 M:80982061 (Ack:57786508)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:43.018]  [00:13:28.960][info  ][EM] ??1 [E:4206i S:1633 M:80982061] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5418ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:43.741]  [00:13:29.684][info  ][EM] >>> [E:4206i S:1633 M:57786509 (Ack:80982061)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:43.875]  [00:13:29.818][info  ][EM] <<< [E:4206i S:1633 M:80982062 (Ack:57786509)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:43.876]  [00:13:29.819][info  ][EM] ??1 [E:4206i S:1633 M:80982062] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:43.882]  [00:13:29.819][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:39:44.546]  [00:13:30.489][info  ][EM] >>> [E:4206i S:1633 M:57786510 (Ack:80982062)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:44.606]  [00:13:30.549][info  ][EM] <<< [E:4206i S:1633 M:80982063 (Ack:57786510)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:44.608]  [00:13:30.550][info  ][EM] ??1 [E:4206i S:1633 M:80982063] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:45.535]  [00:13:31.477][info  ][EM] >>> [E:4206i S:1633 M:57786511 (Ack:80982063)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:45.595]  [00:13:31.538][info  ][EM] <<< [E:4206i S:1633 M:80982064 (Ack:57786511)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:45.596]  [00:13:31.539][info  ][EM] ??1 [E:4206i S:1633 M:80982064] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:46.546]  [00:13:32.488][info  ][EM] >>> [E:4206i S:1633 M:57786512 (Ack:80982064)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:46.606]  [00:13:32.548][info  ][EM] <<< [E:4206i S:1633 M:80982065 (Ack:57786512)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:46.607]  [00:13:32.549][info  ][EM] ??1 [E:4206i S:1633 M:80982065] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:47.870]  [00:13:33.813][info  ][EM] >>> [E:4206i S:1633 M:57786513 (Ack:80982065)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:48.004]  [00:13:33.947][info  ][EM] <<< [E:4206i S:1633 M:80982066 (Ack:57786513)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:48.006]  [00:13:33.948][info  ][EM] ??1 [E:4206i S:1633 M:80982066] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5226ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:48.010]  [00:13:33.948][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:39:51.585]  [00:13:37.529][info  ][EM] >>> [E:4206i S:1633 M:57786514 (Ack:80982066)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:51.646]  [00:13:37.589][info  ][EM] <<< [E:4206i S:1633 M:80982067 (Ack:57786514)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:51.647]  [00:13:37.589][info  ][EM] ??1 [E:4206i S:1633 M:80982067] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5435ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:52.572]  [00:13:38.516][info  ][EM] >>> [E:4206i S:1633 M:57786515 (Ack:80982067)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:52.633]  [00:13:38.577][info  ][EM] <<< [E:4206i S:1633 M:80982068 (Ack:57786515)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:52.634]  [00:13:38.577][info  ][EM] ??1 [E:4206i S:1633 M:80982068] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5628ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:53.351]  [00:13:39.294][info  ][EM] >>> [E:4206i S:1633 M:57786516 (Ack:80982068)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:53.412]  [00:13:39.355][info  ][EM] <<< [E:4206i S:1633 M:80982069 (Ack:57786516)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:53.413]  [00:13:39.356][info  ][EM] ??1 [E:4206i S:1633 M:80982069] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:54.270]  [00:13:40.213][info  ][EM] >>> [E:4206i S:1633 M:57786517 (Ack:80982069)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:54.402]  [00:13:40.345][info  ][EM] <<< [E:4206i S:1633 M:80982070 (Ack:57786517)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:54.403]  [00:13:40.346][info  ][EM] ??1 [E:4206i S:1633 M:80982070] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5667ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:54.409]  [00:13:40.346][error ][DL] Long dispatch time: 132 ms, for event type 2
[18:39:55.058]  [00:13:41.000][info  ][EM] >>> [E:4206i S:1633 M:57786518 (Ack:80982070)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:55.118]  [00:13:41.061][info  ][EM] <<< [E:4206i S:1633 M:80982071 (Ack:57786518)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:55.119]  [00:13:41.062][info  ][EM] ??1 [E:4206i S:1633 M:80982071] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:55.937]  [00:13:41.880][info  ][EM] >>> [E:4206i S:1633 M:57786519 (Ack:80982071)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:55.998]  [00:13:41.941][info  ][EM] <<< [E:4206i S:1633 M:80982072 (Ack:57786519)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:55.999]  [00:13:41.941][info  ][EM] ??1 [E:4206i S:1633 M:80982072] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5411ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:56.734]  [00:13:42.677][info  ][EM] >>> [E:4206i S:1633 M:57786520 (Ack:80982072)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:56.794]  [00:13:42.737][info  ][EM] <<< [E:4206i S:1633 M:80982073 (Ack:57786520)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:56.795]  [00:13:42.738][info  ][EM] ??1 [E:4206i S:1633 M:80982073] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:57.622]  [00:13:43.565][info  ][EM] >>> [E:4206i S:1633 M:57786521 (Ack:80982073)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:57.756]  [00:13:43.699][info  ][EM] <<< [E:4206i S:1633 M:80982074 (Ack:57786521)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:57.757]  [00:13:43.700][info  ][EM] ??1 [E:4206i S:1633 M:80982074] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:57.762]  [00:13:43.700][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:39:58.520]  [00:13:44.463][info  ][EM] >>> [E:4206i S:1633 M:57786522 (Ack:80982074)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:58.581]  [00:13:44.524][info  ][EM] <<< [E:4206i S:1633 M:80982075 (Ack:57786522)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:58.582]  [00:13:44.525][info  ][EM] ??1 [E:4206i S:1633 M:80982075] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5594ms from now [State:Active II:500 AI:2000 AT:4000]
[18:39:59.885]  [00:13:45.828][info  ][EM] >>> [E:4206i S:1633 M:57786523 (Ack:80982075)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:39:59.945]  [00:13:45.888][info  ][EM] <<< [E:4206i S:1633 M:80982076 (Ack:57786523)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:39:59.946]  [00:13:45.889][info  ][EM] ??1 [E:4206i S:1633 M:80982076] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:00.666]  [00:13:46.609][info  ][EM] >>> [E:4206i S:1633 M:57786524 (Ack:80982076)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:00.726]  [00:13:46.669][info  ][EM] <<< [E:4206i S:1633 M:80982077 (Ack:57786524)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:00.728]  [00:13:46.670][info  ][EM] ??1 [E:4206i S:1633 M:80982077] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5289ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:01.570]  [00:13:47.513][info  ][EM] >>> [E:4206i S:1633 M:57786525 (Ack:80982077)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:01.704]  [00:13:47.647][info  ][EM] <<< [E:4206i S:1633 M:80982078 (Ack:57786525)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:01.706]  [00:13:47.648][info  ][EM] ??1 [E:4206i S:1633 M:80982078] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5637ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:01.712]  [00:13:47.648][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:40:02.356]  [00:13:48.299][info  ][EM] >>> [E:4206i S:1633 M:57786526 (Ack:80982078)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:02.416]  [00:13:48.359][info  ][EM] <<< [E:4206i S:1633 M:80982079 (Ack:57786526)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:02.417]  [00:13:48.360][info  ][EM] ??1 [E:4206i S:1633 M:80982079] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:03.337]  [00:13:49.281][info  ][EM] >>> [E:4206i S:1633 M:57786527 (Ack:80982079)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:03.398]  [00:13:49.340][info  ][EM] <<< [E:4206i S:1633 M:80982080 (Ack:57786527)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:03.399]  [00:13:49.341][info  ][EM] ??1 [E:4206i S:1633 M:80982080] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:04.712]  [00:13:50.655][info  ][EM] >>> [E:4206i S:1633 M:57786528 (Ack:80982080)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:04.772]  [00:13:50.715][info  ][EM] <<< [E:4206i S:1633 M:80982081 (Ack:57786528)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:04.773]  [00:13:50.715][info  ][EM] ??1 [E:4206i S:1633 M:80982081] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5721ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:09.294]  [00:13:55.237][info  ][EM] >>> [E:4206i S:1633 M:57786529 (Ack:80982081)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:09.428]  [00:13:55.371][info  ][EM] <<< [E:4206i S:1633 M:80982082 (Ack:57786529)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:09.429]  [00:13:55.372][info  ][EM] ??1 [E:4206i S:1633 M:80982082] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5235ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:09.434]  [00:13:55.372][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:40:10.224]  [00:13:56.167][info  ][EM] >>> [E:4206i S:1633 M:57786530 (Ack:80982082)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:10.284]  [00:13:56.228][info  ][EM] <<< [E:4206i S:1633 M:80982083 (Ack:57786530)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:10.286]  [00:13:56.228][info  ][EM] ??1 [E:4206i S:1633 M:80982083] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:11.014]  [00:13:56.957][info  ][EM] >>> [E:4206i S:1633 M:57786531 (Ack:80982083)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:11.075]  [00:13:57.017][info  ][EM] <<< [E:4206i S:1633 M:80982084 (Ack:57786531)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:11.076]  [00:13:57.018][info  ][EM] ??1 [E:4206i S:1633 M:80982084] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:12.013]  [00:13:57.957][info  ][EM] >>> [E:4206i S:1633 M:57786532 (Ack:80982084)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:12.073]  [00:13:58.017][info  ][EM] <<< [E:4206i S:1633 M:80982085 (Ack:57786532)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:12.075]  [00:13:58.017][info  ][EM] ??1 [E:4206i S:1633 M:80982085] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5211ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:12.793]  [00:13:58.736][info  ][EM] >>> [E:4206i S:1633 M:57786533 (Ack:80982085)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:12.927]  [00:13:58.870][info  ][EM] <<< [E:4206i S:1633 M:80982086 (Ack:57786533)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:12.928]  [00:13:58.871][info  ][EM] ??1 [E:4206i S:1633 M:80982086] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:12.934]  [00:13:58.872][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:40:13.696]  [00:13:59.639][info  ][EM] >>> [E:4206i S:1633 M:57786534 (Ack:80982086)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:13.756]  [00:13:59.700][info  ][EM] <<< [E:4206i S:1633 M:80982087 (Ack:57786534)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:13.757]  [00:13:59.700][info  ][EM] ??1 [E:4206i S:1633 M:80982087] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:14.521]  [00:14:00.464][info  ][EM] >>> [E:4206i S:1633 M:57786535 (Ack:80982087)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:14.581]  [00:14:00.525][info  ][EM] <<< [E:4206i S:1633 M:80982088 (Ack:57786535)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:14.583]  [00:14:00.525][info  ][EM] ??1 [E:4206i S:1633 M:80982088] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5559ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:18.236]  [00:14:04.178][info  ][EM] >>> [E:4206i S:1633 M:57786536 (Ack:80982088)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:18.296]  [00:14:04.239][info  ][EM] <<< [E:4206i S:1633 M:80982089 (Ack:57786536)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:18.297]  [00:14:04.240][info  ][EM] ??1 [E:4206i S:1633 M:80982089] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:19.225]  [00:14:05.168][info  ][EM] >>> [E:4206i S:1633 M:57786537 (Ack:80982089)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:19.360]  [00:14:05.302][info  ][EM] <<< [E:4206i S:1633 M:80982090 (Ack:57786537)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:19.361]  [00:14:05.303][info  ][EM] ??1 [E:4206i S:1633 M:80982090] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:19.367]  [00:14:05.303][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:40:20.236]  [00:14:06.179][info  ][EM] >>> [E:4206i S:1633 M:57786538 (Ack:80982090)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:20.296]  [00:14:06.240][info  ][EM] <<< [E:4206i S:1633 M:80982091 (Ack:57786538)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:20.298]  [00:14:06.240][info  ][EM] ??1 [E:4206i S:1633 M:80982091] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5308ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:21.347]  [00:14:07.291][info  ][EM] >>> [E:4206i S:1633 M:57786539 (Ack:80982091)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:21.407]  [00:14:07.350][info  ][EM] <<< [E:4206i S:1633 M:80982092 (Ack:57786539)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:21.409]  [00:14:07.351][info  ][EM] ??1 [E:4206i S:1633 M:80982092] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5362ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:26.770]  [00:14:12.713][info  ][EM] <<1 [E:4206i S:1633 M:80982092] (S) Msg Retransmission to 1:0000000000000001
[18:40:26.770]  [00:14:12.713][info  ][EM] ??2 [E:4206i S:1633 M:80982092] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5398ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:40:27.161]  [00:14:13.104][info  ][EM] >>> [E:4206i S:1633 M:57786541 (Ack:80982092)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:40:28.678]  [00:14:14.621][info  ][EM] >>> [E:4206i S:1633 M:57786540 (Ack:80982092)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:28.738]  [00:14:14.681][info  ][EM] <<< [E:4206i S:1633 M:80982093 (Ack:57786540)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:28.739]  [00:14:14.682][info  ][EM] ??1 [E:4206i S:1633 M:80982093] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5239ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:29.464]  [00:14:15.406][info  ][EM] >>> [E:4206i S:1633 M:57786542 (Ack:80982093)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:29.596]  [00:14:15.540][info  ][EM] <<< [E:4206i S:1633 M:80982094 (Ack:57786542)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:29.599]  [00:14:15.541][info  ][EM] ??1 [E:4206i S:1633 M:80982094] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5454ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:29.602]  [00:14:15.541][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:40:30.469]  [00:14:16.412][info  ][EM] >>> [E:4206i S:1633 M:57786543 (Ack:80982094)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:30.530]  [00:14:16.472][info  ][EM] <<< [E:4206i S:1633 M:80982095 (Ack:57786543)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:30.531]  [00:14:16.473][info  ][EM] ??1 [E:4206i S:1633 M:80982095] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:31.245]  [00:14:17.188][info  ][EM] >>> [E:4206i S:1633 M:57786544 (Ack:80982095)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:31.305]  [00:14:17.248][info  ][EM] <<< [E:4206i S:1633 M:80982096 (Ack:57786544)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:31.307]  [00:14:17.249][info  ][EM] ??1 [E:4206i S:1633 M:80982096] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5224ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:32.033]  [00:14:17.975][info  ][EM] >>> [E:4206i S:1633 M:57786545 (Ack:80982096)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:32.093]  [00:14:18.036][info  ][EM] <<< [E:4206i S:1633 M:80982097 (Ack:57786545)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:32.094]  [00:14:18.037][info  ][EM] ??1 [E:4206i S:1633 M:80982097] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:32.924]  [00:14:18.867][info  ][EM] >>> [E:4206i S:1633 M:57786546 (Ack:80982097)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:33.058]  [00:14:19.000][info  ][EM] <<< [E:4206i S:1633 M:80982098 (Ack:57786546)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:33.060]  [00:14:19.001][info  ][EM] ??1 [E:4206i S:1633 M:80982098] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:33.065]  [00:14:19.001][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:40:33.696]  [00:14:19.638][info  ][EM] >>> [E:4206i S:1633 M:57786547 (Ack:80982098)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:33.756]  [00:14:19.699][info  ][EM] <<< [E:4206i S:1633 M:80982099 (Ack:57786547)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:33.758]  [00:14:19.700][info  ][EM] ??1 [E:4206i S:1633 M:80982099] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5293ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:34.483]  [00:14:20.425][info  ][EM] >>> [E:4206i S:1633 M:57786548 (Ack:80982099)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:34.543]  [00:14:20.486][info  ][EM] <<< [E:4206i S:1633 M:80982100 (Ack:57786548)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:34.545]  [00:14:20.487][info  ][EM] ??1 [E:4206i S:1633 M:80982100] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:35.377]  [00:14:21.320][info  ][EM] >>> [E:4206i S:1633 M:57786549 (Ack:80982100)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:35.438]  [00:14:21.380][info  ][EM] <<< [E:4206i S:1633 M:80982101 (Ack:57786549)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:35.439]  [00:14:21.381][info  ][EM] ??1 [E:4206i S:1633 M:80982101] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5216ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:36.582]  [00:14:22.524][info  ][EM] >>> [E:4206i S:1633 M:57786550 (Ack:80982101)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:36.718]  [00:14:22.661][info  ][EM] <<< [E:4206i S:1633 M:80982102 (Ack:57786550)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:36.719]  [00:14:22.661][info  ][EM] ??1 [E:4206i S:1633 M:80982102] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5510ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:36.724]  [00:14:22.662][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:40:37.684]  [00:14:23.626][info  ][EM] >>> [E:4206i S:1633 M:57786551 (Ack:80982102)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:37.745]  [00:14:23.687][info  ][EM] <<< [E:4206i S:1633 M:80982103 (Ack:57786551)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:37.746]  [00:14:23.688][info  ][EM] ??1 [E:4206i S:1633 M:80982103] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:38.893]  [00:14:24.836][info  ][EM] >>> [E:4206i S:1633 M:57786552 (Ack:80982103)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:38.954]  [00:14:24.897][info  ][EM] <<< [E:4206i S:1633 M:80982104 (Ack:57786552)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:38.955]  [00:14:24.898][info  ][EM] ??1 [E:4206i S:1633 M:80982104] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:39.887]  [00:14:25.830][info  ][EM] >>> [E:4206i S:1633 M:57786553 (Ack:80982104)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:39.947]  [00:14:25.890][info  ][EM] <<< [E:4206i S:1633 M:80982105 (Ack:57786553)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:39.949]  [00:14:25.891][info  ][EM] ??1 [E:4206i S:1633 M:80982105] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5458ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:41.083]  [00:14:27.026][info  ][EM] >>> [E:4206i S:1633 M:57786554 (Ack:80982105)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:41.217]  [00:14:27.160][info  ][EM] <<< [E:4206i S:1633 M:80982106 (Ack:57786554)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:41.218]  [00:14:27.161][info  ][EM] ??1 [E:4206i S:1633 M:80982106] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5611ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:41.225]  [00:14:27.161][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:40:41.865]  [00:14:27.808][info  ][EM] >>> [E:4206i S:1633 M:57786555 (Ack:80982106)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:41.925]  [00:14:27.869][info  ][EM] <<< [E:4206i S:1633 M:80982107 (Ack:57786555)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:41.927]  [00:14:27.870][info  ][EM] ??1 [E:4206i S:1633 M:80982107] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:42.750]  [00:14:28.693][info  ][EM] >>> [E:4206i S:1633 M:57786556 (Ack:80982107)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:42.811]  [00:14:28.753][info  ][EM] <<< [E:4206i S:1633 M:80982108 (Ack:57786556)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:42.812]  [00:14:28.753][info  ][EM] ??1 [E:4206i S:1633 M:80982108] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5362ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:43.527]  [00:14:29.470][info  ][EM] >>> [E:4206i S:1633 M:57786557 (Ack:80982108)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:43.588]  [00:14:29.531][info  ][EM] <<< [E:4206i S:1633 M:80982109 (Ack:57786557)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:43.590]  [00:14:29.532][info  ][EM] ??1 [E:4206i S:1633 M:80982109] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:44.426]  [00:14:30.369][info  ][EM] >>> [E:4206i S:1633 M:57786558 (Ack:80982109)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:44.559]  [00:14:30.502][info  ][EM] <<< [E:4206i S:1633 M:80982110 (Ack:57786558)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:44.560]  [00:14:30.503][info  ][EM] ??1 [E:4206i S:1633 M:80982110] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5454ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:44.566]  [00:14:30.503][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:40:45.619]  [00:14:31.561][info  ][EM] >>> [E:4206i S:1633 M:57786559 (Ack:80982110)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:45.678]  [00:14:31.622][info  ][EM] <<< [E:4206i S:1633 M:80982111 (Ack:57786559)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:45.680]  [00:14:31.622][info  ][EM] ??1 [E:4206i S:1633 M:80982111] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:46.397]  [00:14:32.339][info  ][EM] >>> [E:4206i S:1633 M:57786560 (Ack:80982111)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:46.458]  [00:14:32.400][info  ][EM] <<< [E:4206i S:1633 M:80982112 (Ack:57786560)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:46.459]  [00:14:32.401][info  ][EM] ??1 [E:4206i S:1633 M:80982112] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:47.490]  [00:14:33.432][info  ][EM] >>> [E:4206i S:1633 M:57786561 (Ack:80982112)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:47.550]  [00:14:33.492][info  ][EM] <<< [E:4206i S:1633 M:80982113 (Ack:57786561)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:47.551]  [00:14:33.493][info  ][EM] ??1 [E:4206i S:1633 M:80982113] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5439ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:48.489]  [00:14:34.431][info  ][EM] >>> [E:4206i S:1633 M:57786562 (Ack:80982113)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:48.625]  [00:14:34.567][info  ][EM] <<< [E:4206i S:1633 M:80982114 (Ack:57786562)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:48.626]  [00:14:34.568][info  ][EM] ??1 [E:4206i S:1633 M:80982114] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5306ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:48.631]  [00:14:34.569][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:40:49.364]  [00:14:35.307][info  ][EM] >>> [E:4206i S:1633 M:57786563 (Ack:80982114)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:49.426]  [00:14:35.368][info  ][EM] <<< [E:4206i S:1633 M:80982115 (Ack:57786563)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:49.427]  [00:14:35.369][info  ][EM] ??1 [E:4206i S:1633 M:80982115] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5317ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:50.559]  [00:14:36.501][info  ][EM] >>> [E:4206i S:1633 M:57786564 (Ack:80982115)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:50.620]  [00:14:36.562][info  ][EM] <<< [E:4206i S:1633 M:80982116 (Ack:57786564)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:50.621]  [00:14:36.563][info  ][EM] ??1 [E:4206i S:1633 M:80982116] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5233ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:54.882]  [00:14:40.824][info  ][EM] >>> [E:4206i S:1633 M:57786565 (Ack:80982116)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:54.942]  [00:14:40.884][info  ][EM] <<< [E:4206i S:1633 M:80982117 (Ack:57786565)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:54.944]  [00:14:40.885][info  ][EM] ??1 [E:4206i S:1633 M:80982117] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5706ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:55.710]  [00:14:41.653][info  ][EM] >>> [E:4206i S:1633 M:57786566 (Ack:80982117)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:40:55.842]  [00:14:41.785][info  ][EM] <<< [E:4206i S:1633 M:80982118 (Ack:57786566)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:40:55.843]  [00:14:41.786][info  ][EM] ??1 [E:4206i S:1633 M:80982118] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[18:40:55.849]  [00:14:41.786][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:41:00.800]  [00:14:46.744][info  ][EM] >>> [E:4206i S:1633 M:57786567 (Ack:80982118)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:00.860]  [00:14:46.803][info  ][EM] <<< [E:4206i S:1633 M:80982119 (Ack:57786567)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:00.862]  [00:14:46.804][info  ][EM] ??1 [E:4206i S:1633 M:80982119] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:02.013]  [00:14:47.955][info  ][EM] >>> [E:4206i S:1633 M:57786568 (Ack:80982119)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:02.073]  [00:14:48.015][info  ][EM] <<< [E:4206i S:1633 M:80982120 (Ack:57786568)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:02.074]  [00:14:48.016][info  ][EM] ??1 [E:4206i S:1633 M:80982120] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5426ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:03.222]  [00:14:49.165][info  ][EM] >>> [E:4206i S:1633 M:57786569 (Ack:80982120)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:03.282]  [00:14:49.225][info  ][EM] <<< [E:4206i S:1633 M:80982121 (Ack:57786569)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:03.284]  [00:14:49.225][info  ][EM] ??1 [E:4206i S:1633 M:80982121] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5701ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:04.315]  [00:14:50.258][info  ][EM] >>> [E:4206i S:1633 M:57786570 (Ack:80982121)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:04.450]  [00:14:50.392][info  ][EM] <<< [E:4206i S:1633 M:80982122 (Ack:57786570)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:04.451]  [00:14:50.393][info  ][EM] ??1 [E:4206i S:1633 M:80982122] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:04.455]  [00:14:50.393][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:41:05.202]  [00:14:51.144][info  ][EM] >>> [E:4206i S:1633 M:57786571 (Ack:80982122)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:05.262]  [00:14:51.205][info  ][EM] <<< [E:4206i S:1633 M:80982123 (Ack:57786571)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:05.263]  [00:14:51.206][info  ][EM] ??1 [E:4206i S:1633 M:80982123] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5222ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:06.103]  [00:14:52.045][info  ][EM] >>> [E:4206i S:1633 M:57786572 (Ack:80982123)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:06.163]  [00:14:52.106][info  ][EM] <<< [E:4206i S:1633 M:80982124 (Ack:57786572)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:06.166]  [00:14:52.107][info  ][EM] ??1 [E:4206i S:1633 M:80982124] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5719ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:07.097]  [00:14:53.040][info  ][EM] >>> [E:4206i S:1633 M:57786573 (Ack:80982124)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:07.158]  [00:14:53.100][info  ][EM] <<< [E:4206i S:1633 M:80982125 (Ack:57786573)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:07.159]  [00:14:53.101][info  ][EM] ??1 [E:4206i S:1633 M:80982125] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:12.528]  [00:14:58.471][info  ][EM] <<1 [E:4206i S:1633 M:80982125] (S) Msg Retransmission to 1:0000000000000001
[18:41:12.528]  [00:14:58.471][info  ][EM] ??2 [E:4206i S:1633 M:80982125] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5570ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:41:13.039]  [00:14:58.982][info  ][EM] >>> [E:4206i S:1633 M:57786575 (Ack:80982125)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:41:14.031]  [00:14:59.973][info  ][EM] >>> [E:4206i S:1633 M:57786574 (Ack:80982125)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:14.164]  [00:15:00.107][info  ][EM] <<< [E:4206i S:1633 M:80982126 (Ack:57786574)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:14.166]  [00:15:00.108][info  ][EM] ??1 [E:4206i S:1633 M:80982126] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:14.171]  [00:15:00.108][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:15.133]  [00:15:01.076][info  ][EM] >>> [E:4206i S:1633 M:57786576 (Ack:80982126)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:15.193]  [00:15:01.136][info  ][EM] <<< [E:4206i S:1633 M:80982127 (Ack:57786576)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:15.194]  [00:15:01.136][info  ][EM] ??1 [E:4206i S:1633 M:80982127] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:16.146]  [00:15:02.088][info  ][EM] >>> [E:4206i S:1633 M:57786577 (Ack:80982127)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:16.207]  [00:15:02.149][info  ][EM] <<< [E:4206i S:1633 M:80982128 (Ack:57786577)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:16.208]  [00:15:02.150][info  ][EM] ??1 [E:4206i S:1633 M:80982128] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:17.129]  [00:15:03.071][info  ][EM] >>> [E:4206i S:1633 M:57786578 (Ack:80982128)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:17.189]  [00:15:03.131][info  ][EM] <<< [E:4206i S:1633 M:80982129 (Ack:57786578)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:17.190]  [00:15:03.132][info  ][EM] ??1 [E:4206i S:1633 M:80982129] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5529ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:17.923]  [00:15:03.866][info  ][EM] >>> [E:4206i S:1633 M:57786579 (Ack:80982129)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:18.057]  [00:15:04.000][info  ][EM] <<< [E:4206i S:1633 M:80982130 (Ack:57786579)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:18.058]  [00:15:04.000][info  ][EM] ??1 [E:4206i S:1633 M:80982130] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:18.063]  [00:15:04.000][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:41:18.705]  [00:15:04.647][info  ][EM] >>> [E:4206i S:1633 M:57786580 (Ack:80982130)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:18.766]  [00:15:04.708][info  ][EM] <<< [E:4206i S:1633 M:80982131 (Ack:57786580)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:18.767]  [00:15:04.708][info  ][EM] ??1 [E:4206i S:1633 M:80982131] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5400ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:19.484]  [00:15:05.427][info  ][EM] >>> [E:4206i S:1633 M:57786581 (Ack:80982131)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:19.545]  [00:15:05.487][info  ][EM] <<< [E:4206i S:1633 M:80982132 (Ack:57786581)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:19.546]  [00:15:05.488][info  ][EM] ??1 [E:4206i S:1633 M:80982132] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5572ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:20.264]  [00:15:06.207][info  ][EM] >>> [E:4206i S:1633 M:57786582 (Ack:80982132)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:20.324]  [00:15:06.267][info  ][EM] <<< [E:4206i S:1633 M:80982133 (Ack:57786582)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:20.326]  [00:15:06.267][info  ][EM] ??1 [E:4206i S:1633 M:80982133] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5633ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:21.255]  [00:15:07.197][info  ][EM] >>> [E:4206i S:1633 M:57786583 (Ack:80982133)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:21.390]  [00:15:07.333][info  ][EM] <<< [E:4206i S:1633 M:80982134 (Ack:57786583)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:21.391]  [00:15:07.333][info  ][EM] ??1 [E:4206i S:1633 M:80982134] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5413ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:21.398]  [00:15:07.333][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:22.042]  [00:15:07.985][info  ][EM] >>> [E:4206i S:1633 M:57786584 (Ack:80982134)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:22.102]  [00:15:08.045][info  ][EM] <<< [E:4206i S:1633 M:80982135 (Ack:57786584)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:22.103]  [00:15:08.045][info  ][EM] ??1 [E:4206i S:1633 M:80982135] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5587ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:25.797]  [00:15:11.741][info  ][EM] >>> [E:4206i S:1633 M:57786585 (Ack:80982135)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:25.858]  [00:15:11.801][info  ][EM] <<< [E:4206i S:1633 M:80982136 (Ack:57786585)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:25.860]  [00:15:11.801][info  ][EM] ??1 [E:4206i S:1633 M:80982136] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5461ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:26.707]  [00:15:12.650][info  ][EM] >>> [E:4206i S:1633 M:57786586 (Ack:80982136)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:26.767]  [00:15:12.710][info  ][EM] <<< [E:4206i S:1633 M:80982137 (Ack:57786586)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:26.768]  [00:15:12.710][info  ][EM] ??1 [E:4206i S:1633 M:80982137] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5274ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:27.703]  [00:15:13.645][info  ][EM] >>> [E:4206i S:1633 M:57786587 (Ack:80982137)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:27.836]  [00:15:13.779][info  ][EM] <<< [E:4206i S:1633 M:80982138 (Ack:57786587)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:27.838]  [00:15:13.780][info  ][EM] ??1 [E:4206i S:1633 M:80982138] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:27.843]  [00:15:13.781][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:28.698]  [00:15:14.641][info  ][EM] >>> [E:4206i S:1633 M:57786588 (Ack:80982138)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:28.758]  [00:15:14.702][info  ][EM] <<< [E:4206i S:1633 M:80982139 (Ack:57786588)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:28.760]  [00:15:14.702][info  ][EM] ??1 [E:4206i S:1633 M:80982139] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5465ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:29.906]  [00:15:15.849][info  ][EM] >>> [E:4206i S:1633 M:57786589 (Ack:80982139)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:29.967]  [00:15:15.910][info  ][EM] <<< [E:4206i S:1633 M:80982140 (Ack:57786589)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:29.968]  [00:15:15.910][info  ][EM] ??1 [E:4206i S:1633 M:80982140] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:30.703]  [00:15:16.646][info  ][EM] >>> [E:4206i S:1633 M:57786590 (Ack:80982140)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:30.763]  [00:15:16.706][info  ][EM] <<< [E:4206i S:1633 M:80982141 (Ack:57786590)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:30.764]  [00:15:16.707][info  ][EM] ??1 [E:4206i S:1633 M:80982141] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:31.493]  [00:15:17.436][info  ][EM] >>> [E:4206i S:1633 M:57786591 (Ack:80982141)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:31.625]  [00:15:17.568][info  ][EM] <<< [E:4206i S:1633 M:80982142 (Ack:57786591)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:31.627]  [00:15:17.569][info  ][EM] ??1 [E:4206i S:1633 M:80982142] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5456ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:31.633]  [00:15:17.569][error ][DL] Long dispatch time: 132 ms, for event type 2
[18:41:32.901]  [00:15:18.844][info  ][EM] >>> [E:4206i S:1633 M:57786592 (Ack:80982142)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:32.961]  [00:15:18.904][info  ][EM] <<< [E:4206i S:1633 M:80982143 (Ack:57786592)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:32.963]  [00:15:18.905][info  ][EM] ??1 [E:4206i S:1633 M:80982143] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5286ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:33.797]  [00:15:19.739][info  ][EM] >>> [E:4206i S:1633 M:57786593 (Ack:80982143)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:33.857]  [00:15:19.799][info  ][EM] <<< [E:4206i S:1633 M:80982144 (Ack:57786593)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:33.858]  [00:15:19.800][info  ][EM] ??1 [E:4206i S:1633 M:80982144] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5299ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:34.607]  [00:15:20.549][info  ][EM] >>> [E:4206i S:1633 M:57786594 (Ack:80982144)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:34.668]  [00:15:20.610][info  ][EM] <<< [E:4206i S:1633 M:80982145 (Ack:57786594)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:34.669]  [00:15:20.611][info  ][EM] ??1 [E:4206i S:1633 M:80982145] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5746ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:35.691]  [00:15:21.634][info  ][EM] >>> [E:4206i S:1633 M:57786595 (Ack:80982145)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:35.825]  [00:15:21.768][info  ][EM] <<< [E:4206i S:1633 M:80982146 (Ack:57786595)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:35.827]  [00:15:21.769][info  ][EM] ??1 [E:4206i S:1633 M:80982146] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5493ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:35.832]  [00:15:21.769][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:41:39.903]  [00:15:25.845][info  ][EM] >>> [E:4206i S:1633 M:57786596 (Ack:80982146)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:39.963]  [00:15:25.906][info  ][EM] <<< [E:4206i S:1633 M:80982147 (Ack:57786596)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:39.964]  [00:15:25.907][info  ][EM] ??1 [E:4206i S:1633 M:80982147] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5480ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:40.681]  [00:15:26.624][info  ][EM] >>> [E:4206i S:1633 M:57786597 (Ack:80982147)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:40.742]  [00:15:26.684][info  ][EM] <<< [E:4206i S:1633 M:80982148 (Ack:57786597)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:40.743]  [00:15:26.685][info  ][EM] ??1 [E:4206i S:1633 M:80982148] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5723ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:41.759]  [00:15:27.702][info  ][EM] >>> [E:4206i S:1633 M:57786598 (Ack:80982148)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:41.819]  [00:15:27.762][info  ][EM] <<< [E:4206i S:1633 M:80982149 (Ack:57786598)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:41.821]  [00:15:27.763][info  ][EM] ??1 [E:4206i S:1633 M:80982149] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5243ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:42.660]  [00:15:28.603][info  ][EM] >>> [E:4206i S:1633 M:57786599 (Ack:80982149)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:42.794]  [00:15:28.737][info  ][EM] <<< [E:4206i S:1633 M:80982150 (Ack:57786599)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:42.795]  [00:15:28.738][info  ][EM] ??1 [E:4206i S:1633 M:80982150] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5364ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:42.799]  [00:15:28.738][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:44.218]  [00:15:30.161][info  ][EM] >>> [E:4206i S:1633 M:57786600 (Ack:80982150)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:44.278]  [00:15:30.221][info  ][EM] <<< [E:4206i S:1633 M:80982151 (Ack:57786600)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:44.280]  [00:15:30.222][info  ][EM] ??1 [E:4206i S:1633 M:80982151] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5501ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:45.137]  [00:15:31.081][info  ][EM] >>> [E:4206i S:1633 M:57786601 (Ack:80982151)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:45.197]  [00:15:31.140][info  ][EM] <<< [E:4206i S:1633 M:80982152 (Ack:57786601)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:45.200]  [00:15:31.141][info  ][EM] ??1 [E:4206i S:1633 M:80982152] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:46.238]  [00:15:32.180][info  ][EM] >>> [E:4206i S:1633 M:57786602 (Ack:80982152)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:46.298]  [00:15:32.241][info  ][EM] <<< [E:4206i S:1633 M:80982153 (Ack:57786602)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:46.300]  [00:15:32.242][info  ][EM] ??1 [E:4206i S:1633 M:80982153] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:47.027]  [00:15:32.970][info  ][EM] >>> [E:4206i S:1633 M:57786603 (Ack:80982153)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:47.161]  [00:15:33.104][info  ][EM] <<< [E:4206i S:1633 M:80982154 (Ack:57786603)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:47.163]  [00:15:33.105][info  ][EM] ??1 [E:4206i S:1633 M:80982154] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:47.167]  [00:15:33.105][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:47.810]  [00:15:33.753][info  ][EM] >>> [E:4206i S:1633 M:57786604 (Ack:80982154)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:47.870]  [00:15:33.814][info  ][EM] <<< [E:4206i S:1633 M:80982155 (Ack:57786604)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:47.872]  [00:15:33.814][info  ][EM] ??1 [E:4206i S:1633 M:80982155] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5372ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:48.595]  [00:15:34.538][info  ][EM] >>> [E:4206i S:1633 M:57786605 (Ack:80982155)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:48.655]  [00:15:34.598][info  ][EM] <<< [E:4206i S:1633 M:80982156 (Ack:57786605)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:48.657]  [00:15:34.599][info  ][EM] ??1 [E:4206i S:1633 M:80982156] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5304ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:52.928]  [00:15:38.871][info  ][EM] >>> [E:4206i S:1633 M:57786606 (Ack:80982156)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:52.988]  [00:15:38.930][info  ][EM] <<< [E:4206i S:1633 M:80982157 (Ack:57786606)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:52.990]  [00:15:38.931][info  ][EM] ??1 [E:4206i S:1633 M:80982157] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:54.251]  [00:15:40.195][info  ][EM] >>> [E:4206i S:1633 M:57786607 (Ack:80982157)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:54.388]  [00:15:40.331][info  ][EM] <<< [E:4206i S:1633 M:80982158 (Ack:57786607)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:54.389]  [00:15:40.332][info  ][EM] ??1 [E:4206i S:1633 M:80982158] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5392ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:54.397]  [00:15:40.332][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:41:55.140]  [00:15:41.083][info  ][EM] >>> [E:4206i S:1633 M:57786608 (Ack:80982158)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:55.200]  [00:15:41.143][info  ][EM] <<< [E:4206i S:1633 M:80982159 (Ack:57786608)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:55.201]  [00:15:41.143][info  ][EM] ??1 [E:4206i S:1633 M:80982159] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5630ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:56.080]  [00:15:42.023][info  ][EM] >>> [E:4206i S:1633 M:57786609 (Ack:80982159)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:56.140]  [00:15:42.083][info  ][EM] <<< [E:4206i S:1633 M:80982160 (Ack:57786609)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:56.143]  [00:15:42.084][info  ][EM] ??1 [E:4206i S:1633 M:80982160] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:56.858]  [00:15:42.802][info  ][EM] >>> [E:4206i S:1633 M:57786610 (Ack:80982160)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:56.919]  [00:15:42.862][info  ][EM] <<< [E:4206i S:1633 M:80982161 (Ack:57786610)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:56.921]  [00:15:42.863][info  ][EM] ??1 [E:4206i S:1633 M:80982161] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:57.754]  [00:15:43.697][info  ][EM] >>> [E:4206i S:1633 M:57786611 (Ack:80982161)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:57.888]  [00:15:43.832][info  ][EM] <<< [E:4206i S:1633 M:80982162 (Ack:57786611)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:57.890]  [00:15:43.832][info  ][EM] ??1 [E:4206i S:1633 M:80982162] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:57.896]  [00:15:43.833][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:41:58.703]  [00:15:44.646][info  ][EM] >>> [E:4206i S:1633 M:57786612 (Ack:80982162)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:58.763]  [00:15:44.707][info  ][EM] <<< [E:4206i S:1633 M:80982163 (Ack:57786612)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:58.766]  [00:15:44.708][info  ][EM] ??1 [E:4206i S:1633 M:80982163] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5585ms from now [State:Active II:500 AI:2000 AT:4000]
[18:41:59.932]  [00:15:45.875][info  ][EM] >>> [E:4206i S:1633 M:57786613 (Ack:80982163)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:41:59.993]  [00:15:45.936][info  ][EM] <<< [E:4206i S:1633 M:80982164 (Ack:57786613)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:41:59.995]  [00:15:45.936][info  ][EM] ??1 [E:4206i S:1633 M:80982164] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5450ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:00.839]  [00:15:46.782][info  ][EM] >>> [E:4206i S:1633 M:57786614 (Ack:80982164)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:00.899]  [00:15:46.842][info  ][EM] <<< [E:4206i S:1633 M:80982165 (Ack:57786614)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:00.902]  [00:15:46.843][info  ][EM] ??1 [E:4206i S:1633 M:80982165] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5590ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:01.735]  [00:15:47.677][info  ][EM] >>> [E:4206i S:1633 M:57786615 (Ack:80982165)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:01.869]  [00:15:47.811][info  ][EM] <<< [E:4206i S:1633 M:80982166 (Ack:57786615)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:01.870]  [00:15:47.812][info  ][EM] ??1 [E:4206i S:1633 M:80982166] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:01.876]  [00:15:47.813][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:42:02.531]  [00:15:48.475][info  ][EM] >>> [E:4206i S:1633 M:57786616 (Ack:80982166)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:02.592]  [00:15:48.535][info  ][EM] <<< [E:4206i S:1633 M:80982167 (Ack:57786616)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:02.594]  [00:15:48.536][info  ][EM] ??1 [E:4206i S:1633 M:80982167] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:03.311]  [00:15:49.253][info  ][EM] >>> [E:4206i S:1633 M:57786617 (Ack:80982167)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:03.372]  [00:15:49.314][info  ][EM] <<< [E:4206i S:1633 M:80982168 (Ack:57786617)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:03.373]  [00:15:49.315][info  ][EM] ??1 [E:4206i S:1633 M:80982168] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5385ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:04.207]  [00:15:50.149][info  ][EM] >>> [E:4206i S:1633 M:57786618 (Ack:80982168)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:04.267]  [00:15:50.209][info  ][EM] <<< [E:4206i S:1633 M:80982169 (Ack:57786618)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:04.269]  [00:15:50.210][info  ][EM] ??1 [E:4206i S:1633 M:80982169] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5302ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:05.336]  [00:15:51.278][info  ][EM] >>> [E:4206i S:1633 M:57786619 (Ack:80982169)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:05.469]  [00:15:51.412][info  ][EM] <<< [E:4206i S:1633 M:80982170 (Ack:57786619)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:05.471]  [00:15:51.413][info  ][EM] ??1 [E:4206i S:1633 M:80982170] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5448ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:05.476]  [00:15:51.413][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:42:06.242]  [00:15:52.185][info  ][EM] >>> [E:4206i S:1633 M:57786620 (Ack:80982170)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:06.303]  [00:15:52.246][info  ][EM] <<< [E:4206i S:1633 M:80982171 (Ack:57786620)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:06.305]  [00:15:52.247][info  ][EM] ??1 [E:4206i S:1633 M:80982171] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5714ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:10.784]  [00:15:56.726][info  ][EM] >>> [E:4206i S:1633 M:57786621 (Ack:80982171)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:10.844]  [00:15:56.787][info  ][EM] <<< [E:4206i S:1633 M:80982172 (Ack:57786621)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:10.845]  [00:15:56.788][info  ][EM] ??1 [E:4206i S:1633 M:80982172] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:11.568]  [00:15:57.511][info  ][EM] >>> [E:4206i S:1633 M:57786622 (Ack:80982172)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:11.629]  [00:15:57.572][info  ][EM] <<< [E:4206i S:1633 M:80982173 (Ack:57786622)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:11.630]  [00:15:57.573][info  ][EM] ??1 [E:4206i S:1633 M:80982173] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5420ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:15.779]  [00:16:01.722][info  ][EM] >>> [E:4206i S:1633 M:57786623 (Ack:80982173)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:15.913]  [00:16:01.856][info  ][EM] <<< [E:4206i S:1633 M:80982174 (Ack:57786623)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:15.915]  [00:16:01.857][info  ][EM] ??1 [E:4206i S:1633 M:80982174] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5742ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:15.920]  [00:16:01.857][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:42:16.663]  [00:16:02.606][info  ][EM] >>> [E:4206i S:1633 M:57786624 (Ack:80982174)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:16.724]  [00:16:02.666][info  ][EM] <<< [E:4206i S:1633 M:80982175 (Ack:57786624)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:16.725]  [00:16:02.667][info  ][EM] ??1 [E:4206i S:1633 M:80982175] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5433ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:17.543]  [00:16:03.487][info  ][EM] >>> [E:4206i S:1633 M:57786625 (Ack:80982175)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:17.605]  [00:16:03.546][info  ][EM] <<< [E:4206i S:1633 M:80982176 (Ack:57786625)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:17.605]  [00:16:03.547][info  ][EM] ??1 [E:4206i S:1633 M:80982176] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5424ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:23.028]  [00:16:08.971][info  ][EM] <<1 [E:4206i S:1633 M:80982176] (S) Msg Retransmission to 1:0000000000000001
[18:42:23.028]  [00:16:08.972][info  ][EM] ??2 [E:4206i S:1633 M:80982176] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5607ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:42:23.487]  [00:16:09.431][info  ][EM] >>> [E:4206i S:1633 M:57786627 (Ack:80982176)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:42:25.161]  [00:16:11.104][info  ][EM] >>> [E:4206i S:1633 M:57786626 (Ack:80982176)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:25.221]  [00:16:11.165][info  ][EM] <<< [E:4206i S:1633 M:80982177 (Ack:57786626)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:25.222]  [00:16:11.166][info  ][EM] ??1 [E:4206i S:1633 M:80982177] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5390ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:26.056]  [00:16:11.999][info  ][EM] >>> [E:4206i S:1633 M:57786628 (Ack:80982177)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:26.189]  [00:16:12.132][info  ][EM] <<< [E:4206i S:1633 M:80982178 (Ack:57786628)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:26.191]  [00:16:12.133][info  ][EM] ??1 [E:4206i S:1633 M:80982178] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5463ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:26.195]  [00:16:12.133][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:42:26.839]  [00:16:12.783][info  ][EM] >>> [E:4206i S:1633 M:57786629 (Ack:80982178)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:26.899]  [00:16:12.842][info  ][EM] <<< [E:4206i S:1633 M:80982179 (Ack:57786629)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:26.901]  [00:16:12.843][info  ][EM] ??1 [E:4206i S:1633 M:80982179] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5469ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:27.887]  [00:16:13.831][info  ][EM] >>> [E:4206i S:1633 M:57786630 (Ack:80982179)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:27.947]  [00:16:13.890][info  ][EM] <<< [E:4206i S:1633 M:80982180 (Ack:57786630)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:27.948]  [00:16:13.891][info  ][EM] ??1 [E:4206i S:1633 M:80982180] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5433ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:29.272]  [00:16:15.215][info  ][EM] >>> [E:4206i S:1633 M:57786631 (Ack:80982180)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:29.332]  [00:16:15.276][info  ][EM] <<< [E:4206i S:1633 M:80982181 (Ack:57786631)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:29.333]  [00:16:15.277][info  ][EM] ??1 [E:4206i S:1633 M:80982181] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5688ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:33.084]  [00:16:19.028][info  ][EM] >>> [E:4206i S:1633 M:57786632 (Ack:80982181)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:33.219]  [00:16:19.162][info  ][EM] <<< [E:4206i S:1633 M:80982182 (Ack:57786632)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:33.220]  [00:16:19.163][info  ][EM] ??1 [E:4206i S:1633 M:80982182] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5476ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:33.224]  [00:16:19.164][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:42:34.185]  [00:16:20.129][info  ][EM] >>> [E:4206i S:1633 M:57786633 (Ack:80982182)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:34.246]  [00:16:20.190][info  ][EM] <<< [E:4206i S:1633 M:80982183 (Ack:57786633)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:34.247]  [00:16:20.191][info  ][EM] ??1 [E:4206i S:1633 M:80982183] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5551ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:35.178]  [00:16:21.123][info  ][EM] >>> [E:4206i S:1633 M:57786634 (Ack:80982183)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:35.239]  [00:16:21.182][info  ][EM] <<< [E:4206i S:1633 M:80982184 (Ack:57786634)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:35.240]  [00:16:21.183][info  ][EM] ??1 [E:4206i S:1633 M:80982184] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:36.363]  [00:16:22.306][info  ][EM] >>> [E:4206i S:1633 M:57786635 (Ack:80982184)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:36.422]  [00:16:22.367][info  ][EM] <<< [E:4206i S:1633 M:80982185 (Ack:57786635)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:36.424]  [00:16:22.368][info  ][EM] ??1 [E:4206i S:1633 M:80982185] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5542ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:37.272]  [00:16:23.216][info  ][EM] >>> [E:4206i S:1633 M:57786636 (Ack:80982185)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:37.406]  [00:16:23.350][info  ][EM] <<< [E:4206i S:1633 M:80982186 (Ack:57786636)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:37.408]  [00:16:23.351][info  ][EM] ??1 [E:4206i S:1633 M:80982186] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5581ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:37.413]  [00:16:23.351][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:42:38.410]  [00:16:24.354][info  ][EM] >>> [E:4206i S:1633 M:57786637 (Ack:80982186)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:38.470]  [00:16:24.415][info  ][EM] <<< [E:4206i S:1633 M:80982187 (Ack:57786637)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:38.471]  [00:16:24.416][info  ][EM] ??1 [E:4206i S:1633 M:80982187] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5508ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:39.409]  [00:16:25.354][info  ][EM] >>> [E:4206i S:1633 M:57786638 (Ack:80982187)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:39.470]  [00:16:25.415][info  ][EM] <<< [E:4206i S:1633 M:80982188 (Ack:57786638)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:39.472]  [00:16:25.416][info  ][EM] ??1 [E:4206i S:1633 M:80982188] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:40.417]  [00:16:26.362][info  ][EM] >>> [E:4206i S:1633 M:57786639 (Ack:80982188)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:40.477]  [00:16:26.422][info  ][EM] <<< [E:4206i S:1633 M:80982189 (Ack:57786639)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:40.479]  [00:16:26.422][info  ][EM] ??1 [E:4206i S:1633 M:80982189] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:41.308]  [00:16:27.252][info  ][EM] >>> [E:4206i S:1633 M:57786640 (Ack:80982189)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:41.443]  [00:16:27.386][info  ][EM] <<< [E:4206i S:1633 M:80982190 (Ack:57786640)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:41.444]  [00:16:27.387][info  ][EM] ??1 [E:4206i S:1633 M:80982190] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5213ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:41.448]  [00:16:27.387][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:42:42.210]  [00:16:28.154][info  ][EM] >>> [E:4206i S:1633 M:57786641 (Ack:80982190)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:42.270]  [00:16:28.214][info  ][EM] <<< [E:4206i S:1633 M:80982191 (Ack:57786641)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:42.271]  [00:16:28.215][info  ][EM] ??1 [E:4206i S:1633 M:80982191] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:42.995]  [00:16:28.940][info  ][EM] >>> [E:4206i S:1633 M:57786642 (Ack:80982191)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:43.055]  [00:16:29.000][info  ][EM] <<< [E:4206i S:1633 M:80982192 (Ack:57786642)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:43.057]  [00:16:29.000][info  ][EM] ??1 [E:4206i S:1633 M:80982192] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:43.788]  [00:16:29.732][info  ][EM] >>> [E:4206i S:1633 M:57786643 (Ack:80982192)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:43.848]  [00:16:29.792][info  ][EM] <<< [E:4206i S:1633 M:80982193 (Ack:57786643)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:43.849]  [00:16:29.793][info  ][EM] ??1 [E:4206i S:1633 M:80982193] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:47.932]  [00:16:33.876][info  ][EM] >>> [E:4206i S:1633 M:57786644 (Ack:80982193)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:48.066]  [00:16:34.010][info  ][EM] <<< [E:4206i S:1633 M:80982194 (Ack:57786644)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:48.068]  [00:16:34.011][info  ][EM] ??1 [E:4206i S:1633 M:80982194] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5499ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:48.073]  [00:16:34.012][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:42:48.933]  [00:16:34.878][info  ][EM] >>> [E:4206i S:1633 M:57786645 (Ack:80982194)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:48.994]  [00:16:34.939][info  ][EM] <<< [E:4206i S:1633 M:80982195 (Ack:57786645)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:48.995]  [00:16:34.939][info  ][EM] ??1 [E:4206i S:1633 M:80982195] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5660ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:50.264]  [00:16:36.208][info  ][EM] >>> [E:4206i S:1633 M:57786646 (Ack:80982195)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:50.324]  [00:16:36.269][info  ][EM] <<< [E:4206i S:1633 M:80982196 (Ack:57786646)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:50.326]  [00:16:36.270][info  ][EM] ??1 [E:4206i S:1633 M:80982196] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:51.389]  [00:16:37.334][info  ][EM] >>> [E:4206i S:1633 M:57786647 (Ack:80982196)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:51.450]  [00:16:37.394][info  ][EM] <<< [E:4206i S:1633 M:80982197 (Ack:57786647)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:51.451]  [00:16:37.395][info  ][EM] ??1 [E:4206i S:1633 M:80982197] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:52.517]  [00:16:38.461][info  ][EM] >>> [E:4206i S:1633 M:57786648 (Ack:80982197)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:52.653]  [00:16:38.597][info  ][EM] <<< [E:4206i S:1633 M:80982198 (Ack:57786648)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:52.654]  [00:16:38.597][info  ][EM] ??1 [E:4206i S:1633 M:80982198] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5504ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:52.658]  [00:16:38.598][error ][DL] Long dispatch time: 137 ms, for event type 2
[18:42:53.307]  [00:16:39.251][info  ][EM] >>> [E:4206i S:1633 M:57786649 (Ack:80982198)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:53.366]  [00:16:39.311][info  ][EM] <<< [E:4206i S:1633 M:80982199 (Ack:57786649)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:53.368]  [00:16:39.312][info  ][EM] ??1 [E:4206i S:1633 M:80982199] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5201ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:54.437]  [00:16:40.382][info  ][EM] >>> [E:4206i S:1633 M:57786650 (Ack:80982199)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:54.498]  [00:16:40.443][info  ][EM] <<< [E:4206i S:1633 M:80982200 (Ack:57786650)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:54.500]  [00:16:40.444][info  ][EM] ??1 [E:4206i S:1633 M:80982200] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:55.550]  [00:16:41.494][info  ][EM] >>> [E:4206i S:1633 M:57786651 (Ack:80982200)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:55.609]  [00:16:41.554][info  ][EM] <<< [E:4206i S:1633 M:80982201 (Ack:57786651)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:55.611]  [00:16:41.555][info  ][EM] ??1 [E:4206i S:1633 M:80982201] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5467ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:56.558]  [00:16:42.502][info  ][EM] >>> [E:4206i S:1633 M:57786652 (Ack:80982201)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:42:56.692]  [00:16:42.636][info  ][EM] <<< [E:4206i S:1633 M:80982202 (Ack:57786652)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:42:56.693]  [00:16:42.637][info  ][EM] ??1 [E:4206i S:1633 M:80982202] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5514ms from now [State:Active II:500 AI:2000 AT:4000]
[18:42:56.698]  [00:16:42.637][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:43:02.205]  [00:16:48.151][info  ][EM] <<1 [E:4206i S:1633 M:80982202] (S) Msg Retransmission to 1:0000000000000001
[18:43:02.205]  [00:16:48.152][info  ][EM] ??2 [E:4206i S:1633 M:80982202] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5596ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:43:02.401]  [00:16:48.345][info  ][EM] >>> [E:4206i S:1633 M:57786654 (Ack:80982202)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:43:02.822]  [00:16:48.767][info  ][EM] >>> [E:4206i S:1633 M:57786653 (Ack:80982202)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:02.882]  [00:16:48.828][info  ][EM] <<< [E:4206i S:1633 M:80982203 (Ack:57786653)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:02.884]  [00:16:48.829][info  ][EM] ??1 [E:4206i S:1633 M:80982203] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5218ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:03.609]  [00:16:49.554][info  ][EM] >>> [E:4206i S:1633 M:57786655 (Ack:80982203)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:03.670]  [00:16:49.615][info  ][EM] <<< [E:4206i S:1633 M:80982204 (Ack:57786655)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:03.671]  [00:16:49.616][info  ][EM] ??1 [E:4206i S:1633 M:80982204] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5532ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:04.529]  [00:16:50.474][info  ][EM] >>> [E:4206i S:1633 M:57786656 (Ack:80982204)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:04.589]  [00:16:50.535][info  ][EM] <<< [E:4206i S:1633 M:80982205 (Ack:57786656)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:04.591]  [00:16:50.535][info  ][EM] ??1 [E:4206i S:1633 M:80982205] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:05.443]  [00:16:51.388][info  ][EM] >>> [E:4206i S:1633 M:57786657 (Ack:80982205)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:05.577]  [00:16:51.522][info  ][EM] <<< [E:4206i S:1633 M:80982206 (Ack:57786657)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:05.578]  [00:16:51.523][info  ][EM] ??1 [E:4206i S:1633 M:80982206] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:05.583]  [00:16:51.524][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:43:06.605]  [00:16:52.550][info  ][EM] >>> [E:4206i S:1633 M:57786658 (Ack:80982206)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:06.666]  [00:16:52.611][info  ][EM] <<< [E:4206i S:1633 M:80982207 (Ack:57786658)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:06.667]  [00:16:52.612][info  ][EM] ??1 [E:4206i S:1633 M:80982207] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:07.698]  [00:16:53.644][info  ][EM] >>> [E:4206i S:1633 M:57786659 (Ack:80982207)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:07.759]  [00:16:53.705][info  ][EM] <<< [E:4206i S:1633 M:80982208 (Ack:57786659)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:07.761]  [00:16:53.706][info  ][EM] ??1 [E:4206i S:1633 M:80982208] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5482ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:08.613]  [00:16:54.558][info  ][EM] >>> [E:4206i S:1633 M:57786660 (Ack:80982208)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:08.673]  [00:16:54.619][info  ][EM] <<< [E:4206i S:1633 M:80982209 (Ack:57786660)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:08.675]  [00:16:54.620][info  ][EM] ??1 [E:4206i S:1633 M:80982209] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5394ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:09.493]  [00:16:55.439][info  ][EM] >>> [E:4206i S:1633 M:57786661 (Ack:80982209)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:09.628]  [00:16:55.573][info  ][EM] <<< [E:4206i S:1633 M:80982210 (Ack:57786661)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:09.629]  [00:16:55.574][info  ][EM] ??1 [E:4206i S:1633 M:80982210] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5731ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:09.633]  [00:16:55.574][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:43:13.433]  [00:16:59.378][info  ][EM] >>> [E:4206i S:1633 M:57786662 (Ack:80982210)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:13.493]  [00:16:59.439][info  ][EM] <<< [E:4206i S:1633 M:80982211 (Ack:57786662)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:13.494]  [00:16:59.440][info  ][EM] ??1 [E:4206i S:1633 M:80982211] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5310ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:14.950]  [00:17:00.895][info  ][EM] >>> [E:4206i S:1633 M:57786663 (Ack:80982211)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:15.011]  [00:17:00.956][info  ][EM] <<< [E:4206i S:1633 M:80982212 (Ack:57786663)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:15.012]  [00:17:00.957][info  ][EM] ??1 [E:4206i S:1633 M:80982212] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5207ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:15.826]  [00:17:01.771][info  ][EM] >>> [E:4206i S:1633 M:57786664 (Ack:80982212)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:15.886]  [00:17:01.832][info  ][EM] <<< [E:4206i S:1633 M:80982213 (Ack:57786664)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:15.888]  [00:17:01.833][info  ][EM] ??1 [E:4206i S:1633 M:80982213] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5267ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:16.760]  [00:17:02.707][info  ][EM] >>> [E:4206i S:1633 M:57786665 (Ack:80982213)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:16.895]  [00:17:02.840][info  ][EM] <<< [E:4206i S:1633 M:80982214 (Ack:57786665)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:16.896]  [00:17:02.841][info  ][EM] ??1 [E:4206i S:1633 M:80982214] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:16.902]  [00:17:02.841][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:43:17.711]  [00:17:03.656][info  ][EM] >>> [E:4206i S:1633 M:57786666 (Ack:80982214)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:17.771]  [00:17:03.716][info  ][EM] <<< [E:4206i S:1633 M:80982215 (Ack:57786666)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:17.772]  [00:17:03.717][info  ][EM] ??1 [E:4206i S:1633 M:80982215] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5259ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:18.528]  [00:17:04.474][info  ][EM] >>> [E:4206i S:1633 M:57786667 (Ack:80982215)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:18.588]  [00:17:04.535][info  ][EM] <<< [E:4206i S:1633 M:80982216 (Ack:57786667)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:18.590]  [00:17:04.535][info  ][EM] ??1 [E:4206i S:1633 M:80982216] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:19.670]  [00:17:05.615][info  ][EM] >>> [E:4206i S:1633 M:57786668 (Ack:80982216)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:19.730]  [00:17:05.675][info  ][EM] <<< [E:4206i S:1633 M:80982217 (Ack:57786668)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:19.731]  [00:17:05.676][info  ][EM] ??1 [E:4206i S:1633 M:80982217] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5635ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:21.215]  [00:17:07.161][info  ][EM] >>> [E:4206i S:1633 M:57786669 (Ack:80982217)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:21.349]  [00:17:07.294][info  ][EM] <<< [E:4206i S:1633 M:80982218 (Ack:57786669)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:21.351]  [00:17:07.295][info  ][EM] ??1 [E:4206i S:1633 M:80982218] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:21.356]  [00:17:07.295][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:43:22.382]  [00:17:08.328][info  ][EM] >>> [E:4206i S:1633 M:57786670 (Ack:80982218)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:22.443]  [00:17:08.388][info  ][EM] <<< [E:4206i S:1633 M:80982219 (Ack:57786670)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:22.444]  [00:17:08.389][info  ][EM] ??1 [E:4206i S:1633 M:80982219] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5424ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:23.260]  [00:17:09.206][info  ][EM] >>> [E:4206i S:1633 M:57786671 (Ack:80982219)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:23.321]  [00:17:09.266][info  ][EM] <<< [E:4206i S:1633 M:80982220 (Ack:57786671)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:23.322]  [00:17:09.267][info  ][EM] ??1 [E:4206i S:1633 M:80982220] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5521ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:24.363]  [00:17:10.309][info  ][EM] >>> [E:4206i S:1633 M:57786672 (Ack:80982220)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:24.424]  [00:17:10.370][info  ][EM] <<< [E:4206i S:1633 M:80982221 (Ack:57786672)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:24.425]  [00:17:10.370][info  ][EM] ??1 [E:4206i S:1633 M:80982221] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5396ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:28.585]  [00:17:14.530][info  ][EM] >>> [E:4206i S:1633 M:57786673 (Ack:80982221)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:28.718]  [00:17:14.664][info  ][EM] <<< [E:4206i S:1633 M:80982222 (Ack:57786673)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:28.720]  [00:17:14.665][info  ][EM] ??1 [E:4206i S:1633 M:80982222] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5347ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:28.726]  [00:17:14.665][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:43:29.714]  [00:17:15.660][info  ][EM] >>> [E:4206i S:1633 M:57786674 (Ack:80982222)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:29.774]  [00:17:15.720][info  ][EM] <<< [E:4206i S:1633 M:80982223 (Ack:57786674)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:29.777]  [00:17:15.721][info  ][EM] ??1 [E:4206i S:1633 M:80982223] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5241ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:31.019]  [00:17:16.965][info  ][EM] >>> [E:4206i S:1633 M:57786675 (Ack:80982223)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:31.080]  [00:17:17.026][info  ][EM] <<< [E:4206i S:1633 M:80982224 (Ack:57786675)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:31.082]  [00:17:17.026][info  ][EM] ??1 [E:4206i S:1633 M:80982224] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5353ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:31.820]  [00:17:17.765][info  ][EM] >>> [E:4206i S:1633 M:57786676 (Ack:80982224)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:31.880]  [00:17:17.826][info  ][EM] <<< [E:4206i S:1633 M:80982225 (Ack:57786676)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:31.881]  [00:17:17.827][info  ][EM] ??1 [E:4206i S:1633 M:80982225] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5710ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:32.821]  [00:17:18.766][info  ][EM] >>> [E:4206i S:1633 M:57786677 (Ack:80982225)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:32.955]  [00:17:18.900][info  ][EM] <<< [E:4206i S:1633 M:80982226 (Ack:57786677)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:32.956]  [00:17:18.901][info  ][EM] ??1 [E:4206i S:1633 M:80982226] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5428ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:32.961]  [00:17:18.901][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:43:33.841]  [00:17:19.787][info  ][EM] >>> [E:4206i S:1633 M:57786678 (Ack:80982226)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:33.902]  [00:17:19.846][info  ][EM] <<< [E:4206i S:1633 M:80982227 (Ack:57786678)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:33.903]  [00:17:19.847][info  ][EM] ??1 [E:4206i S:1633 M:80982227] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5250ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:35.183]  [00:17:21.127][info  ][EM] >>> [E:4206i S:1633 M:57786679 (Ack:80982227)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:35.243]  [00:17:21.188][info  ][EM] <<< [E:4206i S:1633 M:80982228 (Ack:57786679)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:35.244]  [00:17:21.189][info  ][EM] ??1 [E:4206i S:1633 M:80982228] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5516ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:40.759]  [00:17:26.705][info  ][EM] <<1 [E:4206i S:1633 M:80982228] (S) Msg Retransmission to 1:0000000000000001
[18:43:40.759]  [00:17:26.706][info  ][EM] ??2 [E:4206i S:1633 M:80982228] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5276ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:43:40.895]  [00:17:26.839][info  ][EM] >>> [E:4206i S:1633 M:57786681 (Ack:80982228)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:43:47.644]  [00:17:33.588][info  ][EM] >>> [E:4206i S:1633 M:57786680 (Ack:80982228)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:47.704]  [00:17:33.649][info  ][EM] <<< [E:4206i S:1633 M:80982229 (Ack:57786680)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:47.705]  [00:17:33.650][info  ][EM] ??1 [E:4206i S:1633 M:80982229] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5278ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:48.558]  [00:17:34.504][info  ][EM] >>> [E:4206i S:1633 M:57786682 (Ack:80982229)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:48.692]  [00:17:34.637][info  ][EM] <<< [E:4206i S:1633 M:80982230 (Ack:57786682)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:48.694]  [00:17:34.638][info  ][EM] ??1 [E:4206i S:1633 M:80982230] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5686ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:48.700]  [00:17:34.639][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:43:49.556]  [00:17:35.501][info  ][EM] >>> [E:4206i S:1633 M:57786683 (Ack:80982230)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:49.616]  [00:17:35.562][info  ][EM] <<< [E:4206i S:1633 M:80982231 (Ack:57786683)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:49.618]  [00:17:35.562][info  ][EM] ??1 [E:4206i S:1633 M:80982231] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5620ms from now [State:Active II:500 AI:2000 AT:4000]
[18:43:55.237]  [00:17:41.182][info  ][EM] <<1 [E:4206i S:1633 M:80982231] (S) Msg Retransmission to 1:0000000000000001
[18:43:55.237]  [00:17:41.182][info  ][EM] ??2 [E:4206i S:1633 M:80982231] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5491ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:43:55.667]  [00:17:41.612][info  ][EM] >>> [E:4206i S:1633 M:57786685 (Ack:80982231)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:43:56.442]  [00:17:42.386][info  ][EM] >>> [E:4206i S:1633 M:57786684 (Ack:80982231)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:43:56.501]  [00:17:42.447][info  ][EM] <<< [E:4206i S:1633 M:80982232 (Ack:57786684)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:43:56.503]  [00:17:42.448][info  ][EM] ??1 [E:4206i S:1633 M:80982232] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5708ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:02.210]  [00:17:48.156][info  ][EM] <<1 [E:4206i S:1633 M:80982232] (S) Msg Retransmission to 1:0000000000000001
[18:44:02.210]  [00:17:48.156][info  ][EM] ??2 [E:4206i S:1633 M:80982232] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5332ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:44:02.485]  [00:17:48.430][info  ][EM] >>> [E:4206i S:1633 M:57786687 (Ack:80982232)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:44:03.767]  [00:17:49.711][info  ][EM] >>> [E:4206i S:1633 M:57786686 (Ack:80982232)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:03.827]  [00:17:49.772][info  ][EM] <<< [E:4206i S:1633 M:80982233 (Ack:57786686)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:03.828]  [00:17:49.773][info  ][EM] ??1 [E:4206i S:1633 M:80982233] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5323ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:05.282]  [00:17:51.228][info  ][EM] >>> [E:4206i S:1633 M:57786688 (Ack:80982233)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:05.418]  [00:17:51.362][info  ][EM] <<< [E:4206i S:1633 M:80982234 (Ack:57786688)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:05.419]  [00:17:51.363][info  ][EM] ??1 [E:4206i S:1633 M:80982234] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5703ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:05.424]  [00:17:51.363][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:44:06.396]  [00:17:52.341][info  ][EM] >>> [E:4206i S:1633 M:57786689 (Ack:80982234)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:06.457]  [00:17:52.402][info  ][EM] <<< [E:4206i S:1633 M:80982235 (Ack:57786689)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:06.458]  [00:17:52.403][info  ][EM] ??1 [E:4206i S:1633 M:80982235] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5519ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:07.522]  [00:17:53.467][info  ][EM] >>> [E:4206i S:1633 M:57786690 (Ack:80982235)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:07.582]  [00:17:53.528][info  ][EM] <<< [E:4206i S:1633 M:80982236 (Ack:57786690)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:07.584]  [00:17:53.528][info  ][EM] ??1 [E:4206i S:1633 M:80982236] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:08.318]  [00:17:54.263][info  ][EM] >>> [E:4206i S:1633 M:57786691 (Ack:80982236)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:08.378]  [00:17:54.323][info  ][EM] <<< [E:4206i S:1633 M:80982237 (Ack:57786691)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:08.380]  [00:17:54.324][info  ][EM] ??1 [E:4206i S:1633 M:80982237] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5351ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:09.224]  [00:17:55.169][info  ][EM] >>> [E:4206i S:1633 M:57786692 (Ack:80982237)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:09.358]  [00:17:55.303][info  ][EM] <<< [E:4206i S:1633 M:80982238 (Ack:57786692)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:09.359]  [00:17:55.304][info  ][EM] ??1 [E:4206i S:1633 M:80982238] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5405ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:09.365]  [00:17:55.304][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:44:10.431]  [00:17:56.376][info  ][EM] >>> [E:4206i S:1633 M:57786693 (Ack:80982238)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:10.492]  [00:17:56.436][info  ][EM] <<< [E:4206i S:1633 M:80982239 (Ack:57786693)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:10.493]  [00:17:56.437][info  ][EM] ??1 [E:4206i S:1633 M:80982239] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5495ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:11.206]  [00:17:57.150][info  ][EM] >>> [E:4206i S:1633 M:57786694 (Ack:80982239)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:11.266]  [00:17:57.210][info  ][EM] <<< [E:4206i S:1633 M:80982240 (Ack:57786694)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:11.267]  [00:17:57.211][info  ][EM] ??1 [E:4206i S:1633 M:80982240] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5648ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:13.082]  [00:17:59.027][info  ][EM] >>> [E:4206i S:1633 M:57786695 (Ack:80982240)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:13.142]  [00:17:59.087][info  ][EM] <<< [E:4206i S:1633 M:80982241 (Ack:57786695)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:13.144]  [00:17:59.088][info  ][EM] ??1 [E:4206i S:1633 M:80982241] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5617ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:14.209]  [00:18:00.154][info  ][EM] >>> [E:4206i S:1633 M:57786696 (Ack:80982241)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:14.343]  [00:18:00.288][info  ][EM] <<< [E:4206i S:1633 M:80982242 (Ack:57786696)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:14.344]  [00:18:00.289][info  ][EM] ??1 [E:4206i S:1633 M:80982242] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5497ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:14.349]  [00:18:00.289][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:44:15.328]  [00:18:01.274][info  ][EM] >>> [E:4206i S:1633 M:57786697 (Ack:80982242)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:15.389]  [00:18:01.333][info  ][EM] <<< [E:4206i S:1633 M:80982243 (Ack:57786697)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:15.390]  [00:18:01.334][info  ][EM] ??1 [E:4206i S:1633 M:80982243] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:16.768]  [00:18:02.713][info  ][EM] >>> [E:4206i S:1633 M:57786698 (Ack:80982243)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:16.829]  [00:18:02.774][info  ][EM] <<< [E:4206i S:1633 M:80982244 (Ack:57786698)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:16.830]  [00:18:02.774][info  ][EM] ??1 [E:4206i S:1633 M:80982244] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5506ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:17.634]  [00:18:03.580][info  ][EM] >>> [E:4206i S:1633 M:57786699 (Ack:80982244)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:17.695]  [00:18:03.639][info  ][EM] <<< [E:4206i S:1633 M:80982245 (Ack:57786699)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:17.696]  [00:18:03.640][info  ][EM] ??1 [E:4206i S:1633 M:80982245] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5501ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:18.558]  [00:18:04.502][info  ][EM] >>> [E:4206i S:1633 M:57786700 (Ack:80982245)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:18.692]  [00:18:04.636][info  ][EM] <<< [E:4206i S:1633 M:80982246 (Ack:57786700)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:18.693]  [00:18:04.637][info  ][EM] ??1 [E:4206i S:1633 M:80982246] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5329ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:18.698]  [00:18:04.638][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:44:20.101]  [00:18:06.045][info  ][EM] >>> [E:4206i S:1633 M:57786701 (Ack:80982246)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:20.161]  [00:18:06.106][info  ][EM] <<< [E:4206i S:1633 M:80982247 (Ack:57786701)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:20.163]  [00:18:06.107][info  ][EM] ??1 [E:4206i S:1633 M:80982247] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5613ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:21.212]  [00:18:07.157][info  ][EM] >>> [E:4206i S:1633 M:57786702 (Ack:80982247)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:21.272]  [00:18:07.216][info  ][EM] <<< [E:4206i S:1633 M:80982248 (Ack:57786702)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:21.274]  [00:18:07.217][info  ][EM] ??1 [E:4206i S:1633 M:80982248] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:22.107]  [00:18:08.051][info  ][EM] >>> [E:4206i S:1633 M:57786703 (Ack:80982248)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:22.167]  [00:18:08.112][info  ][EM] <<< [E:4206i S:1633 M:80982249 (Ack:57786703)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:22.169]  [00:18:08.113][info  ][EM] ??1 [E:4206i S:1633 M:80982249] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5557ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:26.343]  [00:18:12.288][info  ][EM] >>> [E:4206i S:1633 M:57786704 (Ack:80982249)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:26.477]  [00:18:12.421][info  ][EM] <<< [E:4206i S:1633 M:80982250 (Ack:57786704)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:26.479]  [00:18:12.422][info  ][EM] ??1 [E:4206i S:1633 M:80982250] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5665ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:26.483]  [00:18:12.422][error ][DL] Long dispatch time: 133 ms, for event type 2
[18:44:27.546]  [00:18:13.491][info  ][EM] >>> [E:4206i S:1633 M:57786705 (Ack:80982250)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:27.606]  [00:18:13.550][info  ][EM] <<< [E:4206i S:1633 M:80982251 (Ack:57786705)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:27.608]  [00:18:13.551][info  ][EM] ??1 [E:4206i S:1633 M:80982251] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5381ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:28.573]  [00:18:14.518][info  ][EM] >>> [E:4206i S:1633 M:57786706 (Ack:80982251)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:28.634]  [00:18:14.579][info  ][EM] <<< [E:4206i S:1633 M:80982252 (Ack:57786706)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:28.635]  [00:18:14.580][info  ][EM] ??1 [E:4206i S:1633 M:80982252] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5564ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:29.746]  [00:18:15.691][info  ][EM] >>> [E:4206i S:1633 M:57786707 (Ack:80982252)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:29.807]  [00:18:15.751][info  ][EM] <<< [E:4206i S:1633 M:80982253 (Ack:57786707)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:29.808]  [00:18:15.752][info  ][EM] ??1 [E:4206i S:1633 M:80982253] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5624ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:31.048]  [00:18:16.993][info  ][EM] >>> [E:4206i S:1633 M:57786708 (Ack:80982253)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:31.181]  [00:18:17.126][info  ][EM] <<< [E:4206i S:1633 M:80982254 (Ack:57786708)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:31.182]  [00:18:17.127][info  ][EM] ??1 [E:4206i S:1633 M:80982254] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5377ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:31.188]  [00:18:17.127][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:44:31.855]  [00:18:17.800][info  ][EM] >>> [E:4206i S:1633 M:57786709 (Ack:80982254)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:31.916]  [00:18:17.861][info  ][EM] <<< [E:4206i S:1633 M:80982255 (Ack:57786709)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:31.917]  [00:18:17.862][info  ][EM] ??1 [E:4206i S:1633 M:80982255] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5205ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:32.641]  [00:18:18.586][info  ][EM] >>> [E:4206i S:1633 M:57786710 (Ack:80982255)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:32.702]  [00:18:18.646][info  ][EM] <<< [E:4206i S:1633 M:80982256 (Ack:57786710)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:32.703]  [00:18:18.647][info  ][EM] ??1 [E:4206i S:1633 M:80982256] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5547ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:34.068]  [00:18:20.013][info  ][EM] >>> [E:4206i S:1633 M:57786711 (Ack:80982256)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:34.129]  [00:18:20.074][info  ][EM] <<< [E:4206i S:1633 M:80982257 (Ack:57786711)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:34.131]  [00:18:20.075][info  ][EM] ??1 [E:4206i S:1633 M:80982257] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5486ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:35.079]  [00:18:21.025][info  ][EM] >>> [E:4206i S:1633 M:57786712 (Ack:80982257)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:35.213]  [00:18:21.159][info  ][EM] <<< [E:4206i S:1633 M:80982258 (Ack:57786712)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:35.215]  [00:18:21.159][info  ][EM] ??1 [E:4206i S:1633 M:80982258] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5527ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:35.219]  [00:18:21.160][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:44:36.079]  [00:18:22.024][info  ][EM] >>> [E:4206i S:1633 M:57786713 (Ack:80982258)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:36.139]  [00:18:22.084][info  ][EM] <<< [E:4206i S:1633 M:80982259 (Ack:57786713)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:36.140]  [00:18:22.084][info  ][EM] ??1 [E:4206i S:1633 M:80982259] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5523ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:36.964]  [00:18:22.909][info  ][EM] >>> [E:4206i S:1633 M:57786714 (Ack:80982259)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:37.024]  [00:18:22.969][info  ][EM] <<< [E:4206i S:1633 M:80982260 (Ack:57786714)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:37.026]  [00:18:22.970][info  ][EM] ??1 [E:4206i S:1633 M:80982260] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5446ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:38.183]  [00:18:24.127][info  ][EM] >>> [E:4206i S:1633 M:57786715 (Ack:80982260)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:38.243]  [00:18:24.188][info  ][EM] <<< [E:4206i S:1633 M:80982261 (Ack:57786715)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:38.244]  [00:18:24.189][info  ][EM] ??1 [E:4206i S:1633 M:80982261] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:39.075]  [00:18:25.020][info  ][EM] >>> [E:4206i S:1633 M:57786716 (Ack:80982261)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:39.209]  [00:18:25.154][info  ][EM] <<< [E:4206i S:1633 M:80982262 (Ack:57786716)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:39.211]  [00:18:25.155][info  ][EM] ??1 [E:4206i S:1633 M:80982262] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5263ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:39.218]  [00:18:25.156][error ][DL] Long dispatch time: 135 ms, for event type 2
[18:44:39.857]  [00:18:25.802][info  ][EM] >>> [E:4206i S:1633 M:57786717 (Ack:80982262)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:39.917]  [00:18:25.863][info  ][EM] <<< [E:4206i S:1633 M:80982263 (Ack:57786717)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:39.919]  [00:18:25.864][info  ][EM] ??1 [E:4206i S:1633 M:80982263] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5357ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:40.970]  [00:18:26.915][info  ][EM] >>> [E:4206i S:1633 M:57786718 (Ack:80982263)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:41.030]  [00:18:26.975][info  ][EM] <<< [E:4206i S:1633 M:80982264 (Ack:57786718)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:41.032]  [00:18:26.976][info  ][EM] ??1 [E:4206i S:1633 M:80982264] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5693ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:42.269]  [00:18:28.214][info  ][EM] >>> [E:4206i S:1633 M:57786719 (Ack:80982264)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:42.330]  [00:18:28.275][info  ][EM] <<< [E:4206i S:1633 M:80982265 (Ack:57786719)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:42.331]  [00:18:28.276][info  ][EM] ??1 [E:4206i S:1633 M:80982265] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5723ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:46.127]  [00:18:32.073][info  ][EM] >>> [E:4206i S:1633 M:57786720 (Ack:80982265)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:46.262]  [00:18:32.208][info  ][EM] <<< [E:4206i S:1633 M:80982266 (Ack:57786720)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:46.263]  [00:18:32.208][info  ][EM] ??1 [E:4206i S:1633 M:80982266] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5370ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:46.268]  [00:18:32.208][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:44:47.253]  [00:18:33.199][info  ][EM] >>> [E:4206i S:1633 M:57786721 (Ack:80982266)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:47.313]  [00:18:33.258][info  ][EM] <<< [E:4206i S:1633 M:80982267 (Ack:57786721)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:47.315]  [00:18:33.259][info  ][EM] ??1 [E:4206i S:1633 M:80982267] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5293ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:48.254]  [00:18:34.200][info  ][EM] >>> [E:4206i S:1633 M:57786722 (Ack:80982267)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:44:48.314]  [00:18:34.260][info  ][EM] <<< [E:4206i S:1633 M:80982268 (Ack:57786722)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:44:48.316]  [00:18:34.260][info  ][EM] ??1 [E:4206i S:1633 M:80982268] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5697ms from now [State:Active II:500 AI:2000 AT:4000]
[18:44:54.010]  [00:18:39.957][info  ][EM] <<1 [E:4206i S:1633 M:80982268] (S) Msg Retransmission to 1:0000000000000001
[18:44:54.010]  [00:18:39.958][info  ][EM] ??2 [E:4206i S:1633 M:80982268] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5676ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:44:54.312]  [00:18:40.258][info  ][EM] >>> [E:4206i S:1633 M:57786724 (Ack:80982268)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[18:45:08.318]  [00:18:54.264][info  ][EM] >>> [E:4206i S:1633 M:57786723 (Ack:80982268)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:45:08.378]  [00:18:54.325][info  ][EM] <<< [E:4206i S:1633 M:80982269 (Ack:57786723)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:45:08.379]  [00:18:54.326][info  ][EM] ??1 [E:4206i S:1633 M:80982269] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5403ms from now [State:Active II:500 AI:2000 AT:4000]
[18:45:09.223]  [00:18:55.169][info  ][EM] >>> [E:4206i S:1633 M:57786725 (Ack:80982269)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:45:09.356]  [00:18:55.303][info  ][EM] <<< [E:4206i S:1633 M:80982270 (Ack:57786725)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:45:09.358]  [00:18:55.304][info  ][EM] ??1 [E:4206i S:1633 M:80982270] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5342ms from now [State:Active II:500 AI:2000 AT:4000]
[18:45:09.363]  [00:18:55.304][error ][DL] Long dispatch time: 134 ms, for event type 2
[18:45:10.200]  [00:18:56.147][info  ][EM] >>> [E:4206i S:1633 M:57786726 (Ack:80982270)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:45:10.260]  [00:18:56.207][info  ][EM] <<< [E:4206i S:1633 M:80982271 (Ack:57786726)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:45:10.262]  [00:18:56.208][info  ][EM] ??1 [E:4206i S:1633 M:80982271] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5602ms from now [State:Active II:500 AI:2000 AT:4000]
[18:45:11.611]  [00:18:57.557][info  ][EM] >>> [E:4206i S:1633 M:57786727 (Ack:80982271)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0002:11 (BDX:Block) (B:1062)
[18:45:11.671]  [00:18:57.618][info  ][EM] <<< [E:4206i S:1633 M:80982272 (Ack:57786727)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [F0EB] [UDP:[fd53:6f42:3a33:4efe:8aa2:9eff:fe1d:c2c2]:5540] --- Type 0002:10 (BDX:BlockQuery) (B:38)
[18:45:11.673]  [00:18:57.619][info  ][EM] ??1 [E:4206i S:1633 M:80982272] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5495ms from now [State:Active II:500 AI:2000 AT:4000]
[18:45:17.167]  [00:19:03.114][info  ][EM] <<1 [E:4206i S:1633 M:80982272] (S) Msg Retransmission to 1:0000000000000001
[18:45:17.167]  [00:19:03.114][info  ][EM] ??2 [E:4206i S:1633 M:80982272] (S) Msg Retransmission to 1:0000000000000001 scheduled for 5338ms from now [State:Idle II:500 AI:2000 AT:4000]
[18:45:17.352]  [00:19:03.298][info  ][EM] >>> [E:4206i S:1633 M:57786729 (Ack:80982272)] (S) Msg RX from 1:0000000000000001 [F0EB] to 00000000000008CA --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
```
