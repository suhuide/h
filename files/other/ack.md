# ACK SDK for Matter 接入总结
Alexa Connect Kit
## 一、协议限制

| 项目 | 现状 |
|------|------|
| 官方支持协议 | **仅 Matter over Wi-Fi** |
| Thread 支持 | **尚未推出**，ACK SDK for Matter 不支持 Thread |
| 文档中"Thread"表述 | 指的是 Alexa 生态原生支持 Matter over Thread 设备，**非 ACK SDK 的开发能力** |

> 关键结论：**不要基于"ACK SDK 支持 Thread"的假设来规划 EFR32MG24 项目。**

## 二、认证芯片平台

ACK SDK for Matter 有严格的认证芯片列表，目前官方支持的平台包括：

- 乐鑫 **ESP32-C3**
- 乐鑫 **ESP32-C6**（2026年3月新增）
- Beken **BK7235**
- Bouffalo Lab **BL616**

**EFR32MG24 不在认证列表中**，它被定位为 Matter over Thread 的原生解决方案。

## 三、SDK 申请方式

### 申请入口

**没有公开的在线申请页面或自助注册入口**，唯一途径是邮件联系 Amazon ACK 团队。

**申请邮箱：** `ack-apply@amazon.com`

### 邮件必填信息

- 姓名和联系方式
- 公司名称
- 项目描述

### 邮件建议提供信息

- 产品计划上市时间（年份和季度）
- 目标出货量（四舍五入到千台）
- Amazon Vendor ID（需先注册 Amazon Developer Account）
- 计划使用的 ACK 方案（明确写 **ACK for Matter**）
- 已从 CSA 获得的 Matter VID/PID（如有）

### 后续流程

1. Amazon 分配一名 **ACK 支持工程师**
2. 开通 ACK SDK for Matter 访问权限
3. 分配测试用 Matter VID 和 PID
4. 提供 AWS S3 桶下载通道

> SDK 不通过公开网站下载，由 Amazon 审核项目后通过专属渠道分发。

## 四、EFR32MG24 项目的实际选择

| 方案 | 可行性 | 说明 |
|------|--------|------|
| 更换硬件平台 | ✅ 推荐 | 转向 ESP32-C3/C6 等官方认证 Wi-Fi SoC，走标准 ACK SDK 流程 |
| 坚持 MG24，放弃 ACK SDK | ✅ 推荐 | 走**原生 Matter over Thread** 路线，可接入 Alexa，但需自行处理 OTA、云连接 |
| MG24 主控 + Wi-Fi NCP | ❌ 不推荐 | ACK SDK 是**单芯片解决方案**，强行拆分等于重写定制版 SDK，工作量与风险远超"移植" |

## 五、核心结论

```c
1. ACK SDK for Matter 当前 = Wi-Fi 专用
2. EFR32MG24 不在认证芯片列表
3. SDK 申请唯一途径：ack-apply@amazon.com
4. MG24 项目最合理路径：原生 Matter over Thread（放弃 ACK SDK）
5. "MG24 + Wi-Fi NCP" 架构与 ACK SDK 单芯片设计根本冲突
```