https://csa-iot.org/csa-iot_products/page/3/?p_keywords&p_type%5B0%5D=14&p_device_type%5B0%5D=654&p_program_type%5B0%5D=1049&p_certificate&p_family&p_spec_ver%5B0%5D=1.5&p_spec_ver%5B1%5D=1.5.1&p_firmware_ver&p_product_id&p_vendor#post-feed-block-4b75856a1cb81c23f4249ff4dfa85044
https://csa-iot.org/csa_product/govee-permanent-outdoor-lights-prism/

## IDM Client
在 Matter 1.5 规范中，关于“OTA Requestor 必须具备 IDM Client 能力”的规定，并不是由单一的一句话直接写明，而是通过 设备角色定义 与 交互模型（Interaction Model, IDM）规则 的结合来强制约束的。
可以在以下 3 个核心 Spec 文件 中找到明确的依据和逻辑链条：
### 1. 《Matter Application Cluster Specification》（应用集群规范）
具体章节：11.19 OTA Requestor Cluster （在 Matter 1.4 / 1.5 版本中，通常为第 11.19 节）
规范内容：
在该章节的 "Client" 或 "Commands Generated" 部分，规范明确指出：OTA Requestor 必须能够主动向 OTA Provider 发送特定的 Commands，例如 QueryImage（查询镜像）和 ApplyUpdateRequest（应用更新请求）。
逻辑推导：在 Matter 规范中，主动发送 Command (Invoke) 是 IDM Client 的专属行为。如果设备不支持 IDM Client，它就无法生成和发送这些 OTA 必需的命令。
### 2. 《Matter Core Specification》（核心规范）
具体章节：Chapter 8: Interaction Model (交互模型，不同小版本可能在 Chapter 8 或 9)
规范内容：
该章节明确定义了 Matter 的 C/S（客户端/服务端）架构规则：
Client (客户端)：负责主动发起 Read（读取）、Write（写入）、Invoke（调用命令）和 Subscribe（订阅）请求。
Server (服务端)：负责被动响应这些请求，并托管属性和事件。
逻辑推导：既然 OTA Requestor 需要主动向 Provider 发起交互（无论是发 Command，还是在某些流程中 Read Provider 的状态/Subscribe 事件），它在 IDM 层面就必须被定义为 Client，并实现 MCORE.IDM.C 及其子项（如 InvokeRequest, ReadRequest, SubscribeRequest）。
### 3. 《Matter PICS Definition》（PICS 定义文档）
具体位置：PICS 定义表中的 MCORE.OTA.Requestor 条目及其依赖关系说明。
规范内容：
在 CSA 的 PICS 定义规则中，声明一个设备为特定的 Device Type（如 OTA Requestor），意味着它必须满足该 Device Type 在 Application Cluster Spec 中定义的所有行为。由于 OTA Requestor 的行为强依赖 IDM Client 的交互能力，测试计划生成工具（如 picstool）在解析 PICS 时，会自动将 MCORE.OTA.Requestor = true 与 MCORE.IDM.C = true 及其相关的 Read/Subscribe/Invoke 能力绑定。
💡 为什么偏偏是 TC-IDM-6.3 (Read Event) 和 TC-IDM-6.4 (Subscribe Event)？
虽然 OTA 的核心交互是 Invoke (发送 Command)，但 CSA 的认证测试逻辑是：
XML 中声明了 MCORE.IDM.C = true（因为 OTA Requestor 需要它）。
XML 中同时也声明了 MCORE.IDM.C.ReadEvent = true 和 MCORE.IDM.C.SubscribeEvent = true。
测试工具看到这些标志位为 true，就会严格按照 PICS 声明，生成对应的通用 IDM Client 测试用例（即 TC-IDM-6.3 和 6.4），以验证设备是否真的具备了它所声明的 Read/Subscribe 能力。
### 4. 最终解决建议（基于Base.xml）
查看 Base.xml，应该会发现以下关键项被设置为了 true：
```xml
<itemNumber>MCORE.IDM.C</itemNumber> ... <support>true</support>
<itemNumber>MCORE.IDM.C.ReadRequest</itemNumber> ... <support>true</support>
<itemNumber>MCORE.IDM.C.SubscribeRequest</itemNumber> ... <support>true</support>
<itemNumber>MCORE.IDM.C.ReadEvent</itemNumber> ... <support>true</support>
<itemNumber>MCORE.IDM.C.SubscribeEvent</itemNumber> ... <support>true</support>
<itemNumber>MCORE.OTA.Requestor</itemNumber> ... <support>true</support>
```
如果确认设备不需要 Matter OTA 功能：
请直接在 Base.xml 中将 MCORE.OTA.Requestor 以及上述所有 MCORE.IDM.C.* 的 <support> 改为 false，然后重新生成测试计划，这两个用例就会消失。
如果确认设备需要 Matter OTA 功能：
不能去除这两个测试用例。必须保留这些 true 声明，并确保 Matter SDK 固件中启用了 IDM Client 功能（通常 SDK 默认全局启用），以顺利通过这两项基础交互能力测试，这是 OTA 认证的前置条件。