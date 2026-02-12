```c
[12:28:40.460][detail][IN] UDP Message Received packet nb : 236 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 70
[12:28:40.462][info  ][EM] >>> [E:44405r S:36965 M:92784410] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[12:28:40.463][detail][EM] Handling via exchange: 44405r, Delegate: 0x2000413c
[12:28:40.464][detail][DMG] Received command for Endpoint=3 Cluster=0x0000_0008 Command=0x0000_0004
[12:28:40.464][info  ][ZCL] RX level-control: MOVE_TO_LEVEL_WITH_ON_OFF fe null 0 0
[12:28:40.464][silabs ]LAM: eric,endpoint_id 3, OnLevel 254
[12:28:40.466][detail][DMG] Endpoint 3, Cluster 0x0000_0008 update version to a9a21e0e
[12:28:40.466][info  ][DMG] Handler: 0x20001258 with min: 0x0000000002AD54C6 and max: 0x0000000002B67C86
[12:28:40.466][detail][DMG] Cannot merge the new path into any existing path, create one.

Missed Logs: 2
[12:28:40.467][info  ][ZCL] Setting on/off to ON due to level change
[12:28:40.467][info  ][ZCL] Toggle ep3 on/off from state 0 to 1
[12:28:40.467][info  ][ZCL] On Command - OffWaitTime :  0
[12:28:40.467][info  ][ZCL] On/Toggle Command - Stop Timer
[12:28:40.469][detail][DMG] Endpoint 3, Cluster 0x0000_0006 update version to 5c90bf67
[12:28:40.469][detail][DMG] Cannot merge the new path into any existing path, create one.
[12:28:40.470][detail][DMG] Command handler moving to [NewRespons]
[12:28:40.470][detail][DMG] Command handler moving to [ Preparing]
[12:28:40.470][detail][DMG] Command handler moving to [AddingComm]
[12:28:40.470][detail][DMG] Command handler moving to [AddedComma]
[12:28:40.471][detail][DMG] Command handler moving to [AwaitingDe]
[12:28:40.473][info  ][EM] <<< [E:44405r S:36965 M:232270006 (Ack:92784410)] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[12:28:40.474][info  ][EM] ??1 [E:44405r S:36965 M:232270006] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3402ms from now [State:Active II:500 AI:300 AT:4000]
[12:28:40.475][detail][DMG] Command response sender moving to [AllInvokeR]
[12:28:40.475][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000043 DirtyGeneration = 0x0000000000000045
[12:28:40.480][detail][DMG] <RE:Run> Cluster 6, Attribute 0 is dirty
[12:28:40.481][detail][DMG] Reading attribute: Cluster=0x0000_0006 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[12:28:40.481][detail][DMG] <RE:Run> Cluster 8, Attribute 11 is dirty
[12:28:40.482][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0011 (expanded=1)
[12:28:40.487][detail][DMG] Fetched 0 events
[12:28:40.487][detail][DMG] <RE> Sending report (payload has 65 bytes)...
[12:28:40.489][info  ][EM] <<< [E:23736i S:36965 M:232270007] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:95)

Missed Logs: 5
[12:28:40.490][info  ][EM] ??1 [E:23736i S:36965 M:232270007] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3401ms from now [State:Active II:500 AI:300 AT:4000]
[12:28:40.490][detail][DMG] IM RH moving to [AwaitingReportResponse]
[12:28:40.490][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[12:28:40.491][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[12:28:40.491][detail][ZCL] Event: move from 1
[12:28:40.491][detail][ZCL]  to 254 
[12:28:40.491][detail][ZCL] (diff +1)
[12:28:40.492][detail][DMG] Endpoint 3, Cluster 0x0000_0008 update version to a9a21e0f
[12:28:40.493][detail][DMG] Cannot merge the new path into any existing path, create one.
[12:28:40.493][info  ][ZCL] Setting on/off to ON due to level change
[12:28:40.524][silabs ] MATTER RX: : 55 aa 02 02 ed 05 00 05 07 01 00 01 11 14 
[12:28:40.524][silabs ]COM: device report ID: 0x07 TYPE: 1 LEN: 1 [passive]
[12:28:40.525][silabs ]LAM: report passive onoff, skip

[12:28:40.595][silabs ] MATTER TX: : 55 aa 02 00 16 04 00 08 0d 02 00 04 01 fe fe fe 31 
[12:28:40.595][silabs ]COM: CMD: 0x04, SN: 22, LEN: 17

[12:28:40.638][detail][IN] UDP Message Received packet nb : 237 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 34
[12:28:40.640][info  ][EM] >>> [E:44405r S:36965 M:92784411 (Ack:232270006)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[12:28:40.640][detail][EM] Found matching exchange: 44405r, Delegate: 0
[12:28:40.640][detail][EM] Rxd Ack; Removing MessageCounter:232270006 from Retrans Table on exchange 44405r
[12:28:40.654][detail][IN] UDP Message Received packet nb : 238 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 42
[12:28:40.656][info  ][EM] >>> [E:23736i S:36965 M:92784412 (Ack:232270007)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0001:01 (IM:StatusResponse) (B:42)
[12:28:40.656][detail][EM] Found matching exchange: 23736i, Delegate: 0x20005e60
[12:28:40.657][detail][EM] Rxd Ack; Removing MessageCounter:232270007 from Retrans Table on exchange 23736i
[12:28:40.657][info  ][IM] Received status response, status is 0x00
[12:28:40.657][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[12:28:40.657][detail][DMG] IM RH moving to [CanStartReporting]
[12:28:40.657][info  ][DMG] Handler: 0x20001258 with min: 0x0000000002AD6EAA and max: 0x0000000002B6966A
[12:28:40.660][info  ][EM] <<< [E:23736i S:36965 M:232270008 (Ack:92784412)] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[12:28:40.660][detail][EM] Flushed pending ack for MessageCounter:92784412 on exchange 23736i
[12:28:40.661][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000045 DirtyGeneration = 0x0000000000000046
[12:28:40.666][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[12:28:40.666][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[12:28:40.670][detail][DMG] Fetched 0 events
[12:28:40.671][detail][DMG] <RE> Sending report (payload has 40 bytes)...
[12:28:40.673][info  ][EM] <<< [E:23737i S:36965 M:232270009] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:05 (IM:ReportData) (B:70)
[12:28:40.674][info  ][EM] ??1 [E:23737i S:36965 M:232270009] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3337ms from now [State:Active II:500 AI:300 AT:4000]
[12:28:40.674][detail][DMG] IM RH moving to [AwaitingReportResponse]
[12:28:40.674][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[12:28:40.674][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[12:28:40.682][detail][IN] UDP Message Received packet nb : 239 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 59
[12:28:40.684][info  ][EM] >>> [E:44406r S:36965 M:92784413] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0001:08 (IM:InvokeCommandRequest) (B:59)
[12:28:40.685][detail][EM] Handling via exchange: 44406r, Delegate: 0x2000413c
[12:28:40.686][detail][DMG] Received command for Endpoint=3 Cluster=0x0000_0006 Command=0x0000_0001
[12:28:40.686][info  ][ZCL] Endpoint 3 On/off already set to new value
[12:28:40.686][detail][DMG] Command handler moving to [NewRespons]
[12:28:40.687][detail][DMG] Command handler moving to [ Preparing]
[12:28:40.687][detail][DMG] Command handler moving to [AddingComm]
[12:28:40.687][detail][DMG] Command handler moving to [AddedComma]
[12:28:40.687][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[12:28:40.687][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[12:28:40.688][detail][DMG] Command handler moving to [AwaitingDe]
[12:28:40.691][info  ][EM] <<< [E:44406r S:36965 M:232270010 (Ack:92784413)] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0001:09 (IM:InvokeCommandResponse) (B:67)
[12:28:40.691][info  ][EM] ??1 [E:44406r S:36965 M:232270010] (S) Msg Retransmission to 1:00000000A5E93870 scheduled for 3331ms from now [State:Active II:500 AI:300 AT:4000]
[12:28:40.692][detail][DMG] Command response sender moving to [AllInvokeR]
[12:28:40.801][silabs ] MATTER RX: : 55 aa 02 02 ee 05 00 08 0d 02 00 04 01 fe fe fe 0c 
[12:28:40.802][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [passive]
[12:28:40.802][silabs ]LAM: report passive rgb, skip

[12:28:40.834][detail][IN] UDP Message Received packet nb : 240 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 42
[12:28:40.836][info  ][EM] >>> [E:23737i S:36965 M:92784414 (Ack:232270009)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0001:01 (IM:StatusResponse) (B:42)
[12:28:40.836][detail][EM] Found matching exchange: 23737i, Delegate: 0x20005e60
[12:28:40.836][detail][EM] Rxd Ack; Removing MessageCounter:232270009 from Retrans Table on exchange 23737i
[12:28:40.837][info  ][IM] Received status response, status is 0x00
[12:28:40.837][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[12:28:40.837][detail][DMG] IM RH moving to [CanStartReporting]
[12:28:40.839][info  ][EM] <<< [E:23737i S:36965 M:232270011 (Ack:92784414)] (S) Msg TX from 00000000864E3838 to 1:00000000A5E93870 [AAAB] [UDP:[fdf7:dc9d:f190:0:82d:b81c:c988:57af]:58993] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[12:28:40.839][detail][EM] Flushed pending ack for MessageCounter:92784414 on exchange 23737i
[12:28:40.849][detail][IN] UDP Message Received packet nb : 241 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 34
[12:28:40.850][info  ][EM] >>> [E:44406r S:36965 M:92784415 (Ack:232270010)] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[12:28:40.850][detail][EM] Found matching exchange: 44406r, Delegate: 0
[12:28:40.851][detail][EM] Rxd Ack; Removing MessageCounter:232270010 from Retrans Table on exchange 44406r
[12:28:40.987][silabs ]BLE: mcu2host type=0xA9 len=22
[12:28:40.987][silabs ]COM: mcu2host: 01 13 74 ff ff fe fe fe 13 88 ff ff ff ff ff ff ff ff ff ff ff ff 
[12:28:40.987][silabs ]BLE: RC Connection: 3 auth_state: 0 53:4F:42:7D:EF:99
[12:28:41.584][silabs ]BLE: mcu2host type=0x5C len=4
[12:28:41.585][silabs ]COM: mcu2host: 02 63 06 61 
[12:28:41.585][silabs ]BLE: RC Connection: 3 auth_state: 0 53:4F:42:7D:EF:99
[12:28:41.815][silabs ] MATTER RX: : 55 aa 02 02 ef 06 00 08 04 02 00 04 00 00 00 62 6c 
[12:28:41.815][silabs ]COM: device report ID: 0x04 TYPE: 2 LEN: 4 [active]
[12:28:41.815][silabs ]PWR: report battery percent 98

[12:28:41.815][info  ][ZCL] WRITE ERR: ep 0 clus 0x0000_002F attr 0x0000_000C not supported
[12:28:41.982][silabs ]BLE: mcu2host type=0xA2 len=5
[12:28:41.983][silabs ]COM: mcu2host: 00 00 00 00 62 
[12:28:41.983][silabs ]BLE: RC Connection: 3 auth_state: 0 53:4F:42:7D:EF:99
```