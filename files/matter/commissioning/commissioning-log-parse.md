
# Abbar

|前缀	|全称	|所属模块	|主要作用|
| --- | --- | --- | --- |
|[BLE]	|	Bluetooth Low Energy	|BLE 层	|BLE 连接管理、GATT 服务、特征值读写|
|[DL]	|	Device Layer	|设备层	|平台抽象层，处理硬件事件、定时器、BLE 驱动|
|[EM]	|	Exchange Manager	|交换管理层	|管理消息交换、重传机制、消息计数器|
|[SVR]	|	Server	|服务器层	|设备服务器功能、 commissioning 窗口、QR 码|
|[SC]	|	Secure Channel	|安全通道层	|PASE/CASE 安全会话建立和管理|
|[IN]	|	Interaction Model	|交互模型层	|处理 IM 协议、消息路由|
|[DMG]	|	Data Model Glue	|数据模型层	|处理 attribute/command 读写、编解码|
|[FP]	|	Fabric Provider	Fabric |管理层	|Fabric 表管理、NOC 链验证|
|[TS]	|	Time Service	|时间服务	|时间同步、Last Known Good Time 管理|
|[ZCL]	|	Zigbee Cluster Library	|集群层	|实现具体集群功能(OpCreds、GeneralCommissioning等)|
|[CTL]	|	Controller	|控制器层	|Commissioner 端逻辑、配网状态机|
|[TOO]	|	Tool	|工具层	|chip-tool 命令行工具的输出|
|[DIS]	|	Discovery	|发现层	|mDNS/DNS-SD 服务发现、通告|
|[FS]	|	FailSafe	|FailSafe 管理	|fail-safe 定时器管理、状态维护|
|[SWU]	|	Software Update	|软件更新	|OTA 查询、软件更新管理|
|[PAF]	|	Platform Adaptation	|平台适配层	|平台特定的网络适配|
|[IM]	|	Interaction Model	|交互模型	|与 [IN]	类似，部分版本混用|