```c
[11:29:37.556]  [00:01:34.035][info  ][DL] _OnPlatformEvent default:  event->Type = 32779
[11:29:37.556]  [00:01:34.035][detail][DL] OpenThread State Changed (Flags: 0x00000064)
[11:29:37.561]  [00:01:34.036][detail][DL]    Device Role: ROUTER
[11:29:37.561]  [00:01:34.036][silabs ]NWK: platform event type 800b
[11:32:46.964]  [00:04:43.444][silabs ]BLE: mcu2host type=0xA9 len=22
[11:32:46.964]  [00:04:43.445][silabs ]COM: mcu2host: 01 07 db ff ff 00 00 66 13 88 ff ff ff ff ff 13 88 ff ff ff ff ff 
[11:32:47.155]  [00:04:43.635][silabs ] MATTER RX: : 55 aa 02 00 dc 06 00 08 0d 02 00 04 01 00 00 66 65 
[11:32:47.155]  [00:04:43.635][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [active]
[11:32:47.157]  [00:04:43.635][silabs ]LAM: report rgb R 0 G 0 B 102 dev_index 1
[11:32:47.157]  [00:04:43.635][silabs ]LAM: EP[3] set HSV rgb 0:0:102 -> hsv 169:254:101 (240 100 40)
[11:32:47.159]  
[11:32:47.159]  [00:04:43.635][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56ef
[11:32:47.160]  [00:04:43.636][info  ][DMG] Handler: 0x20001230 with min: 0x0000000000012B9E and max: 0x00000000000A535E
[11:32:47.160]  [00:04:43.636][info  ][DMG] Handler: 0x20001258 with min: 0x0000000000012BD2 and max: 0x00000000000A5392
[11:32:47.160]  [00:04:43.637][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:32:47.162]  [00:04:43.637][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000037 DirtyGeneration = 0x0000000000000038
[11:32:47.163]  [00:04:43.643][detail][DMG] <RE:Run> Cluster 300, Attribute 0 is dirty
[11:32:47.166]  [00:04:43.643][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[11:32:47.172]  [00:04:43.651][detail][DMG] Fetched 0 events
[11:32:47.172]  [00:04:43.651][detail][DMG] <RE> Sending report (payload has 41 bytes)...
[11:32:47.173]  [00:04:43.653][info  ][EM] <<< [E:18267i S:4935 M:64957199] (S) Msg TX from 00000000C9D93985 to 1:0000000067E0F50A [669F] [UDP:[fdbe:1f23:7e2c:4809:9:c1ed:9845:8bed]:57337] --- Type 0001:05 (IM:ReportData) (B:71)
[11:32:47.174]  [00:04:43.654][info  ][EM] ??1 [E:18267i S:4935 M:64957199] (S) Msg Retransmission to 1:0000000067E0F50A scheduled for 3139ms from now [State:Idle II:500 AI:300 AT:4000]
[11:32:47.177]  [00:04:43.654][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:32:47.177]  [00:04:43.654][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:32:47.178]  [00:04:43.655][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000037 DirtyGeneration = 0x0000000000000038
[11:32:47.180]  [00:04:43.660][detail][DMG] <RE:Run> Cluster 300, Attribute 0 is dirty
[11:32:47.182]  [00:04:43.660][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[11:32:47.189]  [00:04:43.667][detail][DMG] Fetched 0 events
[11:32:47.189]  [00:04:43.667][detail][DMG] <RE> Sending report (payload has 41 bytes)...
[11:32:47.189]  [00:04:43.669][info  ][EM] <<< [E:18268i S:4938 M:41656583] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:71)
[11:32:47.192]  [00:04:43.670][info  ][EM] ??1 [E:18268i S:4938 M:41656583] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 3174ms from now [State:Idle II:500 AI:300 AT:4000]
[11:32:47.193]  [00:04:43.670][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:32:47.194]  [00:04:43.671][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[11:32:47.196]  [00:04:43.671][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:32:47.196]  [00:04:43.671][silabs ]LAM: EP[3] set XY rgb 0:0:102 -> xy 9831:3932
[11:32:47.197]  
[11:32:47.197]  [00:04:43.671][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f0
[11:32:47.199]  [00:04:43.672][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:32:47.199]  [00:04:43.672][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f1
[11:32:47.200]  [00:04:43.674][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:32:47.228]  [00:04:43.707][detail][IN] UDP Message Received packet nb : 109 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:32:47.229]  [00:04:43.709][info  ][EM] >>> [E:18268i S:4938 M:239959567 (Ack:41656583)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:32:47.230]  [00:04:43.709][detail][EM] Found matching exchange: 18268i, Delegate: 0x20006a18
[11:32:47.232]  [00:04:43.709][detail][EM] Rxd Ack; Removing MessageCounter:41656583 from Retrans Table on exchange 18268i
[11:32:47.233]  [00:04:43.710][info  ][IM] Received status response, status is 0x00
[11:32:47.233]  [00:04:43.710][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[11:32:47.234]  [00:04:43.710][detail][DMG] IM RH moving to [CanStartReporting]
[11:32:47.234]  [00:04:43.710][info  ][DMG] Handler: 0x20001258 with min: 0x0000000000045416 and max: 0x00000000000D7BD6
[11:32:47.236]  [00:04:43.712][info  ][EM] <<< [E:18268i S:4938 M:41656584 (Ack:239959567)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:32:47.238]  [00:04:43.712][detail][EM] Flushed pending ack for MessageCounter:239959567 on exchange 18268i
[11:32:47.240]  [00:04:43.713][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000038 DirtyGeneration = 0x000000000000003A
[11:32:47.241]  [00:04:43.718][detail][DMG] <RE:Run> Cluster 300, Attribute 3 is dirty
[11:32:47.242]  [00:04:43.719][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0003 (expanded=1)
[11:32:47.244]  [00:04:43.719][detail][DMG] <RE:Run> Cluster 300, Attribute 4 is dirty
[11:32:47.244]  [00:04:43.720][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0004 (expanded=1)
[11:32:47.248]  [00:04:43.728][detail][DMG] Fetched 0 events
[11:32:47.248]  [00:04:43.728][detail][DMG] <RE> Sending report (payload has 70 bytes)...
[11:32:47.250]  [00:04:43.730][info  ][EM] <<< [E:18269i S:4938 M:41656585] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:100)
[11:32:47.253]  [00:04:43.731][info  ][EM] ??1 [E:18269i S:4938 M:41656585] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2855ms from now [State:Active II:500 AI:300 AT:4000]
[11:32:47.254]  [00:04:43.731][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:32:47.257]  [00:04:43.731][detail][DMG] <RE> ReportsInFlight = 2 with readHandler 1, RE has no more messages
[11:32:47.286]  [00:04:43.766][detail][IN] UDP Message Received packet nb : 110 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:32:47.288]  [00:04:43.768][info  ][EM] >>> [E:18269i S:4938 M:239959568 (Ack:41656585)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:32:47.289]  [00:04:43.769][detail][EM] Found matching exchange: 18269i, Delegate: 0x20006a18
[11:32:47.291]  [00:04:43.769][detail][EM] Rxd Ack; Removing MessageCounter:41656585 from Retrans Table on exchange 18269i
[11:32:47.292]  [00:04:43.769][info  ][IM] Received status response, status is 0x00
[11:32:47.292]  [00:04:43.769][detail][DMG] <RE> OnReportConfirm: NumReports = 1
[11:32:47.294]  [00:04:43.770][detail][DMG] IM RH moving to [CanStartReporting]
[11:32:47.294]  [00:04:43.771][info  ][EM] <<< [E:18269i S:4938 M:41656586 (Ack:239959568)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:32:47.297]  [00:04:43.772][detail][EM] Flushed pending ack for MessageCounter:239959568 on exchange 18269i
[11:32:47.340]  [00:04:43.819][detail][IN] UDP Message Received packet nb : 111 SrcAddr : fdbe:1f23:7e2c:4809:9:c1ed:9845:8bed[57337] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:32:47.341]  [00:04:43.821][info  ][EM] >>> [E:18267i S:4935 M:46074457 (Ack:64957199)] (S) Msg RX from 1:0000000067E0F50A [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:32:47.342]  [00:04:43.822][detail][EM] Found matching exchange: 18267i, Delegate: 0x20006988
[11:32:47.344]  [00:04:43.822][detail][EM] Rxd Ack; Removing MessageCounter:64957199 from Retrans Table on exchange 18267i
[11:32:47.347]  [00:04:43.822][info  ][IM] Received status response, status is 0x7d
[11:32:47.353]  [00:04:43.833][info  ][DMG] Subscription id 0x2e453dfa from node <0000000067E0F50A, 1> torn down
[11:32:47.353]  [00:04:43.833][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:32:47.354]  [00:04:43.833][detail][DMG] IM RH moving to [AwaitingDestruction]
[11:32:47.354]  [00:04:43.835][info  ][EM] <<< [E:18267i S:4935 M:64957200 (Ack:46074457)] (S) Msg TX from 00000000C9D93985 to 1:0000000067E0F50A [669F] [UDP:[fdbe:1f23:7e2c:4809:9:c1ed:9845:8bed]:57337] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:32:47.357]  [00:04:43.835][detail][EM] Flushed pending ack for MessageCounter:46074457 on exchange 18267i
[11:33:03.715]  [00:05:00.193][silabs ]BLE: close rc join
[11:33:03.715]  [00:05:00.193][silabs ]BLE: Not kBLEProduct_P
```
silabs Matter SDK, log, 11:29 到 11:32这段时间，做了什么？

## RGB Log 分析
在 11:29:37 到 11:32:47（约 3 分钟）这段时间内，设备主要完成了 Thread 网络角色确认、本地灯控状态变更（RGB 颜色变化），以及 向两个 Matter 订阅者（Subscriber）主动上报状态的过程。

以下是详细的时间线拆解：

## 1. 11:29:37 —— Thread 网络角色确认
设备确认 OpenThread 状态变更，设备角色变为 ROUTER（路由节点）。

这意味着设备已稳定接入 Thread 网格网络，并具备了路由转发能力。

## 2. 11:32:46.964 ~ 11:32:47.157 —— 本地事件触发（颜色改变）
系统通过 BLE 或内部通讯（MCU2HOST）收到一包数据（Type=0xA9），解析后触发 Matter 接收逻辑。

关键动作：应用层（LAM，即 Light Application Module）接收到一条设置指令，将 RGB 颜色设置为 R=0, G=0, B=102（蓝色）。

系统将该颜色值转换为 HSV（169:254:101，即色相 240°、饱和度 100%、明度 40%），并应用在 端点 3（Endpoint 3） 上。

## 3. 11:32:47.159 ~ 11:32:47.196 —— Matter 数据模型标记脏数据并构建报告
由于颜色状态变更，Matter 数据管理（DMG）层检测到端点 3 上的 集群 0x0300（照明与颜色控制 Cluster） 属性发生变化。

系统将该属性（Attribute 0）标记为“脏”（Dirty），并准备生成订阅报告（Report Data）。

同时，系统为该颜色计算了 XY 色度坐标（9831:3932），并更新了集群的版本号（dcef56ef -> dcef56f1）。

## 4. 11:32:47.173 ~ 11:32:47.254 —— 向订阅者发送状态报告（Report Data）
设备当前维护着 两个活跃的 Matter 订阅会话，因此触发了两次独立的上报流程：

第一次上报（目标节点 A：0000000067E0F50A）：

发送包含颜色属性的 Report Data 消息（Msg TX）。

结果：该节点返回状态码 0x7d（即 125）。在 Matter 协议中，这通常对应 RESOURCE_EXHAUSTED（资源耗尽）或订阅协商失败。设备随即强制拆除了该订阅（日志明确显示 Subscription ... torn down）。

第二次上报（目标节点 B：00000000A3166874）：

先发送包含属性 0 的初始报告，收到对方成功确认（状态码 0x00）。

紧接着，系统发现属性 3（CurrentHue）和属性 4（CurrentSaturation）也变脏，于是立即发送了第二份报告（包含属性 3 和 4）。

对方再次回复成功确认（状态码 0x00），该订阅保持有效。

## 5. 总结与结论
在这段时间内，设备的核心行为是：
响应本地颜色变化指令（变为蓝色），将状态同步给 Matter 控制器。其中一个订阅者（67E0F50A）因返回错误码导致连接被断开，另一个订阅者（A3166874）则成功接收并确认了全部属性更新。


```c
[11:52:47.188]  [00:24:43.668][info  ][DMG] Handler: 0x20001258 with min: 0x00000000000D7BD4 and max: 0x000000000016A394
[11:52:47.188]  [00:24:43.668][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x000000000000003A DirtyGeneration = 0x000000000000003A
[11:52:47.200]  [00:24:43.679][detail][DMG] Fetched 0 events
[11:52:47.200]  [00:24:43.679][detail][DMG] <RE> Sending report (payload has 11 bytes)...
[11:52:47.200]  [00:24:43.682][info  ][EM] <<< [E:18271i S:4938 M:41656589] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:41)
[11:52:47.203]  [00:24:43.682][info  ][EM] ??1 [E:18271i S:4938 M:41656589] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 3091ms from now [State:Idle II:500 AI:300 AT:4000]
[11:52:47.205]  [00:24:43.683][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:52:47.206]  [00:24:43.683][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:52:47.210]  [00:24:43.683][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:52:47.227]  [00:24:43.708][detail][IN] UDP Message Received packet nb : 113 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:52:47.229]  [00:24:43.709][info  ][EM] >>> [E:18271i S:4938 M:239959570 (Ack:41656589)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:52:47.230]  [00:24:43.710][detail][EM] Found matching exchange: 18271i, Delegate: 0x20006a18
[11:52:47.231]  [00:24:43.710][detail][EM] Rxd Ack; Removing MessageCounter:41656589 from Retrans Table on exchange 18271i
[11:52:47.233]  [00:24:43.710][info  ][IM] Received status response, status is 0x00
[11:52:47.233]  [00:24:43.710][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:52:47.234]  [00:24:43.711][detail][DMG] IM RH moving to [CanStartReporting]
[11:52:47.234]  [00:24:43.712][info  ][EM] <<< [E:18271i S:4938 M:41656590 (Ack:239959570)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:52:47.237]  [00:24:43.713][detail][EM] Flushed pending ack for MessageCounter:239959570 on exchange 18271i
[11:52:55.897]  [00:24:52.377][detail][IN] UDP Message Received packet nb : 114 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 75
[11:52:55.898]  [00:24:52.379][info  ][EM] >>> [E:37861r S:4938 M:239959571] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:08 (IM:InvokeCommandRequest) (B:75)
[11:52:55.900]  [00:24:52.379][detail][EM] Handling via exchange: 37861r, Delegate: 0x20004cf4
[11:52:55.901]  [00:24:52.381][detail][DMG] Received command for Endpoint=3 Cluster=0x0000_0300 Command=0x0000_0006
[11:52:55.902]  [00:24:52.381][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f2
[11:52:55.902]  [00:24:52.382][info  ][DMG] Handler: 0x20001258 with min: 0x000000000016A3A3 and max: 0x00000000001FCB63
[11:52:55.904]  [00:24:52.382][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:52:55.905]  [00:24:52.383][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f3
[11:52:55.907]  [00:24:52.384][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:52:55.907]  [00:24:52.385][detail][DMG] Endpoint 3, Cluster 0x0000_0062 update version to 3ca13894
[11:52:55.908]  [00:24:52.386][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:52:55.909]  [00:24:52.388][detail][DMG] Endpoint 3, Cluster 0x0000_0062 update version to 3ca13895
[11:52:55.909]  [00:24:52.388][detail][DMG] Command handler moving to [NewRespons]
[11:52:55.911]  [00:24:52.388][detail][DMG] Command handler moving to [ Preparing]
[11:52:55.912]  [00:24:52.389][detail][DMG] Command handler moving to [AddingComm]
[11:52:55.912]  [00:24:52.389][detail][DMG] Command handler moving to [AddedComma]
[11:52:55.913]  [00:24:52.389][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 1
[11:52:55.913]  [00:24:52.389][detail][DMG] Decreasing reference count for CommandHandlerImpl, remaining 0
[11:52:55.915]  [00:24:52.390][detail][DMG] Command handler moving to [AwaitingDe]
[11:52:55.916]  [00:24:52.392][info  ][EM] <<< [E:37861r S:4938 M:41656591 (Ack:239959571)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:09 (IM:InvokeCommandResponse) (B:68)
[11:52:55.917]  [00:24:52.393][info  ][EM] ??1 [E:37861r S:4938 M:41656591] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2860ms from now [State:Active II:500 AI:300 AT:4000]
[11:52:55.920]  [00:24:52.393][detail][DMG] Command response sender moving to [AllInvokeR]
[11:52:55.920]  [00:24:52.393][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x000000000000003A DirtyGeneration = 0x000000000000003E
[11:52:55.923]  [00:24:52.399][detail][DMG] <RE:Run> Cluster 62, Attribute 2 is dirty
[11:52:55.923]  [00:24:52.399][detail][DMG] Reading attribute: Cluster=0x0000_0062 Endpoint=0x3 AttributeId=0x0000_0002 (expanded=1)
[11:52:55.924]  [00:24:52.402][detail][DMG] <RE:Run> Cluster 300, Attribute 8 is dirty
[11:52:55.926]  [00:24:52.402][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0008 (expanded=1)
[11:52:55.927]  [00:24:52.403][detail][DMG] <RE:Run> Cluster 300, Attribute 4001 is dirty
[11:52:55.927]  [00:24:52.403][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_4001 (expanded=1)
[11:52:55.929]  [00:24:52.411][detail][DMG] Fetched 0 events
[11:52:55.929]  [00:24:52.411][detail][DMG] <RE> Sending report (payload has 125 bytes)...
[11:52:55.932]  [00:24:52.414][info  ][EM] <<< [E:18272i S:4938 M:41656592] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:155)
[11:52:55.935]  [00:24:52.414][info  ][EM] ??1 [E:18272i S:4938 M:41656592] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2830ms from now [State:Active II:500 AI:300 AT:4000]
[11:52:55.936]  [00:24:52.415][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:52:55.937]  [00:24:52.415][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:52:55.937]  
[11:52:55.937]  Missed Logs: 1
[11:52:55.937]  [00:24:52.415][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:52:55.939]  [00:24:52.415][info  ][ZCL] Hue 86 endpoint 3
[11:52:55.939]  [00:24:52.416][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f4
[11:52:55.940]  [00:24:52.416][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:52:55.942]  [00:24:52.416][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f5
[11:52:55.944]  [00:24:52.416][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:52:55.944]  [00:24:52.417][silabs ]LAM: EP[3] Attr ColorMode changed
[11:52:55.945]  [00:24:52.417][silabs ] MATTER TX: : 55 aa 02 00 09 04 00 08 0d 02 00 04 01 00 65 00 8f 
[11:52:55.945]  [00:24:52.418][silabs ]COM: CMD: 0x04, SN: 9, LEN: 17
[11:52:55.949]  
[11:52:55.949]  [00:24:52.418][silabs ]LAM: EP[3] Attr ColorMode changed
[11:52:55.972]  [00:24:52.453][detail][IN] UDP Message Received packet nb : 115 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 34
[11:52:55.973]  [00:24:52.455][info  ][EM] >>> [E:37861r S:4938 M:239959572 (Ack:41656591)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:52:55.976]  [00:24:52.455][detail][EM] Found matching exchange: 37861r, Delegate: 0
[11:52:55.976]  [00:24:52.455][detail][EM] Rxd Ack; Removing MessageCounter:41656591 from Retrans Table on exchange 37861r
[11:52:55.989]  [00:24:52.469][detail][IN] UDP Message Received packet nb : 116 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:52:55.990]  [00:24:52.471][info  ][EM] >>> [E:18272i S:4938 M:239959573 (Ack:41656592)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:52:55.992]  [00:24:52.472][detail][EM] Found matching exchange: 18272i, Delegate: 0x20006a18
[11:52:55.993]  [00:24:52.472][detail][EM] Rxd Ack; Removing MessageCounter:41656592 from Retrans Table on exchange 18272i
[11:52:55.994]  [00:24:52.472][info  ][IM] Received status response, status is 0x00
[11:52:55.994]  [00:24:52.472][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:52:55.996]  [00:24:52.473][detail][DMG] IM RH moving to [CanStartReporting]
[11:52:55.996]  [00:24:52.473][info  ][DMG] Handler: 0x20001258 with min: 0x000000000016C5BF and max: 0x00000000001FED7F
[11:52:55.997]  [00:24:52.475][info  ][EM] <<< [E:18272i S:4938 M:41656593 (Ack:239959573)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:52:56.000]  [00:24:52.475][detail][EM] Flushed pending ack for MessageCounter:239959573 on exchange 18272i
[11:52:56.001]  [00:24:52.475][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x000000000000003E DirtyGeneration = 0x0000000000000040
[11:52:56.004]  [00:24:52.481][detail][DMG] <RE:Run> Cluster 300, Attribute 0 is dirty
[11:52:56.005]  [00:24:52.482][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[11:52:56.006]  [00:24:52.482][detail][DMG] <RE:Run> Cluster 300, Attribute 1 is dirty
[11:52:56.006]  [00:24:52.483][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[11:52:56.009]  [00:24:52.490][detail][DMG] Fetched 0 events
[11:52:56.009]  [00:24:52.491][detail][DMG] <RE> Sending report (payload has 68 bytes)...
[11:52:56.012]  [00:24:52.493][info  ][EM] <<< [E:18273i S:4938 M:41656594] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:98)
[11:52:56.014]  [00:24:52.494][info  ][EM] ??1 [E:18273i S:4938 M:41656594] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2887ms from now [State:Active II:500 AI:300 AT:4000]
[11:52:56.016]  [00:24:52.494][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:52:56.017]  [00:24:52.494][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:52:56.017]  [00:24:52.494][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:52:56.038]  [00:24:52.519][silabs ] MATTER TX: : 55 aa 02 00 0a 04 00 08 0d 02 00 04 01 00 65 00 90 
[11:52:56.038]  [00:24:52.519][silabs ]COM: CMD: 0x04, SN: 10, LEN: 17
[11:52:56.042]  
[11:52:56.060]  [00:24:52.541][detail][IN] UDP Message Received packet nb : 117 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:52:56.062]  [00:24:52.543][info  ][EM] >>> [E:18273i S:4938 M:239959574 (Ack:41656594)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:52:56.064]  [00:24:52.543][detail][EM] Found matching exchange: 18273i, Delegate: 0x20006a18
[11:52:56.065]  [00:24:52.543][detail][EM] Rxd Ack; Removing MessageCounter:41656594 from Retrans Table on exchange 18273i
[11:52:56.066]  [00:24:52.544][info  ][IM] Received status response, status is 0x00
[11:52:56.066]  [00:24:52.544][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:52:56.068]  [00:24:52.544][detail][DMG] IM RH moving to [CanStartReporting]
[11:52:56.068]  [00:24:52.546][info  ][EM] <<< [E:18273i S:4938 M:41656595 (Ack:239959574)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:52:56.071]  [00:24:52.546][detail][EM] Flushed pending ack for MessageCounter:239959574 on exchange 18273i
[11:52:56.139]  [00:24:52.620][silabs ] MATTER TX: : 55 aa 02 00 0b 04 00 08 0d 02 00 04 01 00 65 00 91 
[11:52:56.139]  [00:24:52.620][silabs ]COM: CMD: 0x04, SN: 11, LEN: 17
[11:52:56.142]  
[11:52:56.612]  [00:24:53.093][silabs ] MATTER RX: : 55 aa 02 00 dd 05 00 08 0d 02 00 04 01 00 65 00 64 
[11:52:56.612]  [00:24:53.093][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [passive]
[11:52:56.618]  [00:24:53.093][silabs ]LAM: report passive rgb, skip
[11:52:56.618]  
[11:52:56.833]  [00:24:53.314][silabs ]BLE: mcu2host type=0xA9 len=22
[11:52:56.833]  [00:24:53.314][silabs ]COM: mcu2host: 01 07 c7 ff ff 00 65 00 13 88 ff ff ff ff ff 13 88 ff ff ff ff ff 
[11:53:10.986]  [00:25:07.466][silabs ]BLE: mcu2host type=0xA9 len=22
[11:53:10.986]  [00:25:07.467][silabs ]COM: mcu2host: 01 07 c7 ff ff 65 65 65 13 88 ff ff ff ff ff 13 88 ff ff ff ff ff 
[11:53:11.176]  [00:25:07.657][silabs ] MATTER RX: : 55 aa 02 00 de 06 00 08 0d 02 00 04 01 65 65 65 30 
[11:53:11.176]  [00:25:07.658][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [active]
[11:53:11.177]  [00:25:07.658][silabs ]LAM: report rgb R 101 G 101 B 101 dev_index 1
[11:53:11.177]  [00:25:07.658][silabs ]LAM: EP[3] set HSV rgb 101:101:101 -> hsv 0:0:100 (0 0 39)
[11:53:11.180]  
[11:53:11.180]  [00:25:07.658][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f6
[11:53:11.181]  [00:25:07.659][info  ][DMG] Handler: 0x20001258 with min: 0x000000000016C60E and max: 0x00000000001FEDCE
[11:53:11.182]  [00:25:07.659][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:11.182]  [00:25:07.660][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f7
[11:53:11.184]  [00:25:07.660][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:11.185]  [00:25:07.661][detail][DMG] Endpoint 3, Cluster 0x0000_0008 update version to 5cbc7766
[11:53:11.185]  [00:25:07.662][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:11.186]  [00:25:07.662][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000040 DirtyGeneration = 0x0000000000000043
[11:53:11.188]  [00:25:07.667][detail][DMG] <RE:Run> Cluster 8, Attribute 0 is dirty
[11:53:11.189]  [00:25:07.667][detail][DMG] Reading attribute: Cluster=0x0000_0008 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[11:53:11.191]  [00:25:07.668][detail][DMG] <RE:Run> Cluster 300, Attribute 0 is dirty
[11:53:11.191]  [00:25:07.668][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0000 (expanded=1)
[11:53:11.192]  [00:25:07.669][detail][DMG] <RE:Run> Cluster 300, Attribute 1 is dirty
[11:53:11.194]  [00:25:07.669][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[11:53:11.197]  [00:25:07.677][detail][DMG] Fetched 0 events
[11:53:11.197]  [00:25:07.677][detail][DMG] <RE> Sending report (payload has 94 bytes)...
[11:53:11.199]  [00:25:07.679][info  ][EM] <<< [E:18274i S:4938 M:41656596] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:124)
[11:53:11.200]  [00:25:07.680][info  ][EM] ??1 [E:18274i S:4938 M:41656596] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 3076ms from now [State:Idle II:500 AI:300 AT:4000]
[11:53:11.203]  [00:25:07.681][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:53:11.203]  [00:25:07.681][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:53:11.204]  [00:25:07.681][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:53:11.204]  [00:25:07.681][silabs ]LAM: EP[3] set XY rgb 101:101:101 -> xy 20493:21561
[11:53:11.206]  
[11:53:11.206]  [00:25:07.682][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f8
[11:53:11.208]  [00:25:07.683][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:11.208]  [00:25:07.683][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56f9
[11:53:11.209]  [00:25:07.684][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:11.239]  [00:25:07.719][detail][IN] UDP Message Received packet nb : 118 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:53:11.240]  [00:25:07.721][info  ][EM] >>> [E:18274i S:4938 M:239959575 (Ack:41656596)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:53:11.242]  [00:25:07.722][detail][EM] Found matching exchange: 18274i, Delegate: 0x20006a18
[11:53:11.243]  [00:25:07.722][detail][EM] Rxd Ack; Removing MessageCounter:41656596 from Retrans Table on exchange 18274i
[11:53:11.245]  [00:25:07.722][info  ][IM] Received status response, status is 0x00
[11:53:11.245]  [00:25:07.722][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:53:11.246]  [00:25:07.722][detail][DMG] IM RH moving to [CanStartReporting]
[11:53:11.246]  [00:25:07.723][info  ][DMG] Handler: 0x20001258 with min: 0x0000000000170161 and max: 0x0000000000202921
[11:53:11.247]  [00:25:07.724][info  ][EM] <<< [E:18274i S:4938 M:41656597 (Ack:239959575)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:53:11.250]  [00:25:07.725][detail][EM] Flushed pending ack for MessageCounter:239959575 on exchange 18274i
[11:53:11.251]  [00:25:07.725][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000043 DirtyGeneration = 0x0000000000000045
[11:53:11.253]  [00:25:07.731][detail][DMG] <RE:Run> Cluster 300, Attribute 3 is dirty
[11:53:11.254]  [00:25:07.731][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0003 (expanded=1)
[11:53:11.255]  [00:25:07.732][detail][DMG] <RE:Run> Cluster 300, Attribute 4 is dirty
[11:53:11.255]  [00:25:07.733][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0004 (expanded=1)
[11:53:11.261]  [00:25:07.741][detail][DMG] Fetched 0 events
[11:53:11.261]  [00:25:07.741][detail][DMG] <RE> Sending report (payload has 70 bytes)...
[11:53:11.261]  [00:25:07.744][info  ][EM] <<< [E:18275i S:4938 M:41656598] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:100)
[11:53:11.263]  [00:25:07.744][info  ][EM] ??1 [E:18275i S:4938 M:41656598] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2890ms from now [State:Active II:500 AI:300 AT:4000]
[11:53:11.265]  [00:25:07.745][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:53:11.266]  [00:25:07.745][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:53:11.271]  [00:25:07.745][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:53:11.302]  [00:25:07.783][detail][IN] UDP Message Received packet nb : 119 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:53:11.304]  [00:25:07.785][info  ][EM] >>> [E:18275i S:4938 M:239959576 (Ack:41656598)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:53:11.306]  [00:25:07.786][detail][EM] Found matching exchange: 18275i, Delegate: 0x20006a18
[11:53:11.307]  [00:25:07.786][detail][EM] Rxd Ack; Removing MessageCounter:41656598 from Retrans Table on exchange 18275i
[11:53:11.308]  [00:25:07.786][info  ][IM] Received status response, status is 0x00
[11:53:11.308]  [00:25:07.786][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:53:11.309]  [00:25:07.786][detail][DMG] IM RH moving to [CanStartReporting]
[11:53:11.309]  [00:25:07.788][info  ][EM] <<< [E:18275i S:4938 M:41656599 (Ack:239959576)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:53:11.312]  [00:25:07.789][detail][EM] Flushed pending ack for MessageCounter:239959576 on exchange 18275i
[11:53:16.789]  [00:25:13.269][silabs ]BLE: mcu2host type=0xA9 len=22
[11:53:16.789]  [00:25:13.269][silabs ]COM: mcu2host: 01 07 c7 ff ff 65 00 00 13 88 ff ff ff ff ff 13 88 ff ff ff ff ff 
[11:53:16.980]  [00:25:13.459][silabs ] MATTER RX: : 55 aa 02 00 df 06 00 08 0d 02 00 04 01 65 00 00 67 
[11:53:16.980]  [00:25:13.459][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [active]
[11:53:16.981]  [00:25:13.460][silabs ]LAM: report rgb R 101 G 0 B 0 dev_index 1
[11:53:16.981]  [00:25:13.460][silabs ]LAM: EP[3] set HSV rgb 101:0:0 -> hsv 0:254:100 (0 100 39)
[11:53:16.982]  
[11:53:16.982]  [00:25:13.460][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56fa
[11:53:16.983]  [00:25:13.461][info  ][DMG] Handler: 0x20001258 with min: 0x00000000001701A1 and max: 0x0000000000202961
[11:53:16.983]  [00:25:13.461][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:16.985]  [00:25:13.461][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000045 DirtyGeneration = 0x0000000000000046
[11:53:16.986]  [00:25:13.467][detail][DMG] <RE:Run> Cluster 300, Attribute 1 is dirty
[11:53:16.987]  [00:25:13.467][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0001 (expanded=1)
[11:53:16.996]  [00:25:13.476][detail][DMG] Fetched 0 events
[11:53:16.996]  [00:25:13.476][detail][DMG] <RE> Sending report (payload has 41 bytes)...
[11:53:16.996]  [00:25:13.479][info  ][EM] <<< [E:18276i S:4938 M:41656600] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:71)
[11:53:16.999]  [00:25:13.479][info  ][EM] ??1 [E:18276i S:4938 M:41656600] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 3152ms from now [State:Idle II:500 AI:300 AT:4000]
[11:53:17.001]  [00:25:13.480][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:53:17.002]  [00:25:13.480][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:53:17.004]  [00:25:13.480][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:53:17.004]  [00:25:13.480][silabs ]LAM: EP[3] set XY rgb 101:0:0 -> xy 41947:21624
[11:53:17.005]  
[11:53:17.005]  [00:25:13.481][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56fb
[11:53:17.007]  [00:25:13.482][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:17.007]  [00:25:13.483][detail][DMG] Endpoint 3, Cluster 0x0000_0300 update version to dcef56fc
[11:53:17.008]  [00:25:13.483][detail][DMG] Cannot merge the new path into any existing path, create one.
[11:53:17.027]  [00:25:13.508][detail][IN] UDP Message Received packet nb : 120 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:53:17.029]  [00:25:13.510][info  ][EM] >>> [E:18276i S:4938 M:239959577 (Ack:41656600)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:53:17.030]  [00:25:13.510][detail][EM] Found matching exchange: 18276i, Delegate: 0x20006a18
[11:53:17.031]  [00:25:13.511][detail][EM] Rxd Ack; Removing MessageCounter:41656600 from Retrans Table on exchange 18276i
[11:53:17.033]  [00:25:13.511][info  ][IM] Received status response, status is 0x00
[11:53:17.033]  [00:25:13.511][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:53:17.034]  [00:25:13.511][detail][DMG] IM RH moving to [CanStartReporting]
[11:53:17.034]  [00:25:13.511][info  ][DMG] Handler: 0x20001258 with min: 0x0000000000171808 and max: 0x0000000000203FC8
[11:53:17.035]  [00:25:13.513][info  ][EM] <<< [E:18276i S:4938 M:41656601 (Ack:239959577)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:53:17.038]  [00:25:13.514][detail][EM] Flushed pending ack for MessageCounter:239959577 on exchange 18276i
[11:53:17.040]  [00:25:13.514][detail][DMG] Building Reports for ReadHandler with LastReportGeneration = 0x0000000000000046 DirtyGeneration = 0x0000000000000048
[11:53:17.041]  [00:25:13.520][detail][DMG] <RE:Run> Cluster 300, Attribute 3 is dirty
[11:53:17.042]  [00:25:13.520][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0003 (expanded=1)
[11:53:17.044]  [00:25:13.521][detail][DMG] <RE:Run> Cluster 300, Attribute 4 is dirty
[11:53:17.044]  [00:25:13.521][detail][DMG] Reading attribute: Cluster=0x0000_0300 Endpoint=0x3 AttributeId=0x0000_0004 (expanded=1)
[11:53:17.048]  [00:25:13.529][detail][DMG] Fetched 0 events
[11:53:17.048]  [00:25:13.529][detail][DMG] <RE> Sending report (payload has 70 bytes)...
[11:53:17.050]  [00:25:13.531][info  ][EM] <<< [E:18277i S:4938 M:41656602] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0001:05 (IM:ReportData) (B:100)
[11:53:17.053]  [00:25:13.532][info  ][EM] ??1 [E:18277i S:4938 M:41656602] (S) Msg Retransmission to 1:00000000A3166874 scheduled for 2858ms from now [State:Active II:500 AI:300 AT:4000]
[11:53:17.054]  [00:25:13.533][detail][DMG] IM RH moving to [AwaitingReportResponse]
[11:53:17.056]  [00:25:13.533][detail][DMG] <RE> ReportsInFlight = 1 with readHandler 0, RE has no more messages
[11:53:17.056]  [00:25:13.533][detail][DMG] All ReadHandler-s are clean, clear GlobalDirtySet
[11:53:17.091]  [00:25:13.572][detail][IN] UDP Message Received packet nb : 121 SrcAddr : fd77:954d:dddd:0:aafc:163c:9ffe:6845[61286] DestAddr : fd77:954d:dddd:0:7581:fba4:2c4a:aeb6[5540] Payload Length 42
[11:53:17.093]  [00:25:13.575][info  ][EM] >>> [E:18277i S:4938 M:239959578 (Ack:41656602)] (S) Msg RX from 1:00000000A3166874 [669F] to 00000000C9D93985 --- Type 0001:01 (IM:StatusResponse) (B:42)
[11:53:17.095]  [00:25:13.575][detail][EM] Found matching exchange: 18277i, Delegate: 0x20006a18
[11:53:17.096]  [00:25:13.575][detail][EM] Rxd Ack; Removing MessageCounter:41656602 from Retrans Table on exchange 18277i
[11:53:17.098]  [00:25:13.575][info  ][IM] Received status response, status is 0x00
[11:53:17.098]  [00:25:13.576][detail][DMG] <RE> OnReportConfirm: NumReports = 0
[11:53:17.099]  [00:25:13.576][detail][DMG] IM RH moving to [CanStartReporting]
[11:53:17.099]  [00:25:13.577][info  ][EM] <<< [E:18277i S:4938 M:41656603 (Ack:239959578)] (S) Msg TX from 00000000C9D93985 to 1:00000000A3166874 [669F] [UDP:[fd77:954d:dddd:0:aafc:163c:9ffe:6845]:61286] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:53:17.102]  [00:25:13.578][detail][EM] Flushed pending ack for MessageCounter:239959578 on exchange 18277i
```
再看这个log,11:52从Home app点了改颜色，11:53后再从remote改了两次颜色都成功更新。 结合前面的log,分析，Home app是哪个订阅者？为什么这样？怎么解决？需要任何时候app上颜色能更新同步

## 1. 哪个订阅者是 Apple Home？
第一份日志（11:32） 中，设备向两个节点发送了报告：

0000000067E0F50A → 返回错误 0x7d（UNSUPPORTED_ACCESS），订阅被强制拆除。

00000000A3166874 → 返回成功 0x00，订阅存活。

第二份日志（11:52:55） 中，只有 00000000A3166874 存在，并且它向设备发送了 InvokeCommandRequest（色相/饱和度移动命令）。

结论：Apple Home 应用就是节点 00000000A3166874（因为只有它发起了下行控制指令）。第一份日志中 67E0F50A 是另一个控制器（可能是 Google Home 或旧订阅），其订阅已经失效并被清理。

## 2. 为什么 11:32 时 App 颜色没有更新？
对比两次上报的属性内容，就能发现关键差异：

11:32 上报（失败）：
日志仅标记了 Cluster 300, Attribute 0 is dirty（即 CurrentHue）。
设备只上报了 色相值，没有上报 ColorMode（属性 8）。

11:52 上报（成功）：
Apple Home 发送 MoveToHueAndSaturation 指令后，设备在回复中明确标记了：
Cluster 300, Attribute 8 is dirty（即 ColorMode）。
随后上报了完整的颜色属性（色相、饱和度、颜色模式等）。

Apple Home 的渲染逻辑：
Matter 的 Color Control 集群支持 HS（色相/饱和度）和 XY（色度）两种模式。Apple Home 在接收到上报时，必须依赖 ColorMode 属性（属性 8）来决定如何解析颜色数据。如果上报包中缺少这个属性，Home 应用会认为数据不完整，从而丢弃该更新，UI 保持原样。

## 3. 为什么 11:53 遥控器（Remote）修改后，设备硬件变了但 App 仍未更新？
您提到“11:53 后再从 remote 改了两次颜色都成功更新”——这很可能指的是设备物理灯光颜色变化成功，而 App 界面依然没有同步更新。

查看 11:53 的日志（灰色 101,101,101 和红色 101,0,0），设备上报时只标记了：

Cluster 8, Attribute 0（亮度电平）

Cluster 300, Attribute 0（CurrentHue）

Cluster 300, Attribute 1（CurrentSaturation）

依然没有标记和上报 ColorMode（属性 8）。因此，即便设备硬件改变了，Apple Home 因收不到颜色模式属性，再次忽略了这次上报，App 界面不会更新。

## 4. 如何解决？（确保任何时候 App 都能同步）
根本办法是：只要颜色发生改变（无论来源于 Matter 命令、本地物理按键、MCU 串口指令），固件都必须将 ColorMode 属性标记为“脏”并随报告一起发送。

具体操作步骤：

在应用层（LAM）颜色变更函数中，除了更新 RGB/HSV 和 XY 值外，显式更新并标记 ColorMode 属性：

若使用 HS 模式，设置 ColorMode = 0x02。

若使用 XY 模式，设置 ColorMode = 0x03。

调用 Matter 数据模型的 MarkDirty 接口，将该属性标记为待上报。

```c
cpp
// 伪代码示例（基于 Silabs SDK）
Matter::AttributeAccessInterface::Instance()->MarkDirty(EndpointId, ClusterId, AttributeId);
// 例如：标记端点 3，集群 0x0300，属性 0x0008 (ColorMode)
```

确保在生成报告时，ColorMode 被包含在内：
您需要检查 ZAP 配置中的 “Reporting” 策略，确保属性 8 的 MinInterval 和 MaxInterval 配置正确，且未被禁用。通常建议将其纳入默认报告列表中。

同步更新 ColorCapabilities（属性 0x4001）：
Apple Home 有时也会参考此字段。请确认该属性在 ZAP 中已正确勾选支持 HS 和 XY 能力（通常设为 0x07 以支持所有模式）。

处理订阅拆除问题：
第一份日志中的 67E0F50A 被拆除，可能是由于版本不匹配或会话超时。确保设备的时间同步（如 UTC）和 Fabric 索引管理正确，避免 Apple Home 频繁重建订阅导致状态不同步。

## 5. 验证方法
修改固件后，您可以通过抓取日志确认：

每当颜色改变时（无论是本地触发还是远程触发），日志中必须出现 Cluster 300, Attribute 8 is dirty。

同时上报的报告中，Payload 长度会增加（包含属性 8 的数据），并且 Apple Home 界面会随之立即刷新。

总结：问题的核心不是网络连接或协议握手失败，而是 上报数据内容不完整。Apple Home 对 ColorMode 有硬性要求，补齐此属性的上报即可解决所有场景下的同步问题。


11:53 遥控器（Remote）修改后 App 更新了，而 11:32 遥控器修改后 App 没更新。结合两次日志的差异，真相是：

11:53 之所以能更新，是因为 11:52 时您通过 Home App 主动点了一次颜色，设备在响应这次操作时，带上了 ColorMode（颜色模式）属性，让 Apple Home 本地“缓存”了这个模式。
随后 11:53 遥控器再改颜色时，即便设备上报依然缺少 ColorMode，Apple Home 凭借缓存的模式（HS模式）成功解析了传过来的 Hue/Saturation，所以界面刷新了。

而 11:32 失败，是因为在那之前，Home App 从未向设备发过任何指令，设备启动后主动上报的第一包颜色数据（蓝色）中 没有包含 ColorMode。Apple Home 本地没有任何缓存，收到孤立的 Hue/Saturation 数据后，不知道应该用 HS 还是 XY 模式去渲染，直接丢弃了这包数据，所以 App 界面没变。

核心结论：为什么“在那之前”会失败？
设备刚上电或刚建立订阅时，Apple Home 对颜色模式（ColorMode）的上下文是空的。如果设备首次或早期上报不主动带 ColorMode，Home 就会忽略此次颜色更新。

终极解决方案（确保任何时候 App 都能同步）
要解决“遥控器在任何时刻（尤其是 App 从未操作过之前）修改，App 都能更新”，绝对不能在逻辑上依赖 App 端的缓存。必须让设备固件在每次颜色变更时，强制、主动地上报 ColorMode 属性。

请按以下步骤修改固件（Silabs Matter SDK）：

在本地颜色更新函数中强制标记 ColorMode
找到应用层（LAM）处理 RGB/HSV 变化的代码位置（日志中对应 LAM: EP[3] set HSV 的地方）。
在更新 CurrentHue（属性0）和 CurrentSaturation（属性1）的同时，显式设置 ColorMode（属性 0x0008）为 0x02（代表 HS 模式），并调用 SDK 接口将其标记为“脏”（Dirty）。

cpp
// 伪代码逻辑（基于 Silabs 示例）
// 1. 设置颜色模式为 HS (0x02)
emberAfWriteAttribute(endpoint, ZCL_COLOR_CONTROL_CLUSTER_ID, 
                      ZCL_CURRENT_COLOR_MODE_ATTRIBUTE_ID, 
                      (uint8_t*)&mode, ZCL_UINT8_ATTRIBUTE_TYPE);

// 2. 强制标记该属性为脏，确保它被包含在下一次上报中
Matter::AttributeAccessInterface::Instance()->MarkDirty(endpoint, 
                      ZCL_COLOR_CONTROL_CLUSTER_ID, 
                      ZCL_CURRENT_COLOR_MODE_ATTRIBUTE_ID);
处理“颜色模式未变但颜色值变了”的场景
您的遥控器只调亮度或色相，模式（HS）本身没变。但为了纠正 App 缓存丢失问题，依然要执行 MarkDirty。即使属性值相同，标记脏并重发一次，可以强行刷新 App 端的缓存记录。

针对刚上电/重订阅的初始状态推送
在设备 Thread 网络就绪、Matter 订阅建立完成（如日志中 [CanStartReporting] 状态出现）后，主动触发一次全量报告，其中必须包含 ColorMode、ColorCapabilities（属性 0x4001）和当前的 Hue/Saturation。确保 App 在第一次收到数据时就有完整的颜色上下文。

验证标准
修改后，无论设备是冷启动后首次变色，还是遥控器连续快速变色，您抓取日志时都会看到：
<RE:Run> Cluster 300, Attribute 8 is dirty（即 ColorMode 被标记）。
此时上报的 Payload 会包含 Attribute 8，Apple Home 的 UI 就会立刻跟随变化，不再依赖之前的“预操作”。