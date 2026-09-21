## 1. 需求背景

产品涉及**转 CD(Certification Declaration / 认证声明)给其客户**。  
模块完成生产(烧录固件、CD、DAC、产品信息)，交付到客户手中后，需要留有接口可以修改以下出厂定制数据：
- <font color="#dd00dd">**Vendor ID**(厂商ID)</font>
- <font color="#dd00dd">**Product ID**(产品ID)</font>
- <font color="#dd00dd">**Vendor name**(厂商名称)</font>
- <font color="#dd00dd">**Product name**(产品名称/型号名称)</font>
- **Product url**(产品URL)
- **Product label**(产品标签)
- **Part number**(型号标识)
- **CD**(认证声明)

<div align="left">
  <img src="vendor.png" width="1080">
</div>

> Matter 模块固件已固化，VID PID 目前没有对外抛出的接口。  
> PID上电时会与MCU通信获取再设置, 但这里依然要正常配置PID。  

## 2 目的

设计一套**安全、私钥不泄露**的客户化定制接口方案，**MFG_Tool 更新(JSON 配置)** 以支持 JSON 配置方式定义待修改字段，完成出厂数据无感读写。

## 3 核心安全原则

1. **签名私钥永不泄露**——私钥只存在于服务器上，客户电脑只持有服务器签发的一次性解锁材料；
2. **Challenge-Response 解锁**——每次解锁必须由服务器对芯片当前 Challenge 签名，签名与芯片 SE 序列号 + Challenge 绑定；
3. **修改前先备份**——任何写入操作前读取完整备份镜像留档(出厂数据区 + 证书区)；
4. **写后清除一次性材料**——写入后清除解锁签名材料，保证常态下不可访问敏感区域。

## 4 总体流程

量产件生产时 SE 已安装解锁公钥(一次性烧录)，交付时 Debug Lock 开启，直接读写被拒绝；须先用芯片内公钥对应的私钥(仅服务器持有)签名解锁。

```mermaid
sequenceDiagram
    participant ClientPC as 客户电脑 (上位机)
    participant Chip as EFR32 芯片
    participant Server as 服务器 (持有签名私钥)

    Note over ClientPC,Chip: 阶段一：备份 + 获取挑战值 (Challenge)
    ClientPC->>Chip: 1. 连接并读取芯片信息
    Chip-->>ClientPC: 返回 Serial No 和 Challenge
    ClientPC->>Chip: 2. (可选)备份出厂数据区 + 证书区完整镜像
    Chip-->>ClientPC: 备份镜像(本地留档 + 回传服务器存档)
    ClientPC->>ClientPC: 3. 生成待签名解锁文件

    Note over ClientPC,Server: 阶段二：请求签名
    ClientPC->>Server: 4. 上传 Serial No + Challenge + 待改字段清单
    Server->>Server: 5. 校验设备合法性，用私钥签发解锁令牌<br/>并准备定制数据包(新 VID/PID/CD 等)
    Server-->>ClientPC: 6. 返回解锁令牌 + 定制数据包

    Note over ClientPC,Chip: 阶段三：解锁
    ClientPC->>ClientPC: 7. 按工具要求放置解锁令牌
    ClientPC->>Chip: 8. 执行解锁操作
    Chip-->>ClientPC: 验证签名成功，调试接口已解锁

    Note over ClientPC,Chip: 阶段四：写入定制数据并校验
    ClientPC->>Chip: 9. 设置 VID / PID / 厂商与产品信息
    ClientPC->>Chip: 10. 更新 CD(认证声明)
    ClientPC->>Chip: 11. 读回校验

    Note over ClientPC,Server: 阶段五：结果回传
    ClientPC->>Server: 12. 上传备份与读回校验结果
    Server->>Server: 服务器比对存档，出具验证结论
```

## 5 补充要求

 - 识别模块是否已定制过
 - 已定制模块的再次定制（支持 N 次重复烧录）
 - 烧录结果判定(成功/失败需要明示提示显示)
 - 烧录日志需要保存，模块VID PID 与所使用CD应该要对应可查询
 - 烧录要在限定时间内完成，timeout不完成要锁片
 - 多模块同时烧录
