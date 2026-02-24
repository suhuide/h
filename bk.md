
[hrf](hrf.md)  
[reset](./files/bk/reset.md)  

## Info
```c
@日志Richy 我们产品软件的外包商李总。
@蔡工 我们公司内部软件工程师蔡工
@从此醉 我们公司内部硬件工程师李工
@石韧 华普微Matter孙总
```
```c
广东省东莞市樟木头镇文裕路8号，东莞保康电子科技有限公司，吴长春，13620049295
```
### PartNo.
```c
HM-MT2401B-HPBK01
EFR32MG24A410F1536IM40
```
### Ones
[保康Matter窗帘电机](https://ones.cn/wiki/#/team/VocipTXV/space/7jKfDSiJ/page/UAgVbQvf)  

<div align="left">
  <img src="files/bk/bk.png" width="2160">
</div>

## MCU DFU
```mermaid
sequenceDiagram
    participant Matter模块
    participant MCU
    
    Matter模块->>MCU: 发送版本请求
    MCU-->>Matter模块: 返回当前版本
    
    alt Matter模块端版本检查
        Matter模块->>MCU: 发送升级通知
        MCU-->>Matter模块: 升级响应
        
        alt MCU拒绝升级
            MCU-->>Matter模块: 拒绝升级
            Note over MCU: 原因：<br>1. 存储空间不足<br>2. 电池电量低<br>3. 正在执行关键任务
            Note over Matter模块, MCU: 流程直接结束<br>下次上电重新检测
        else MCU接受升级
            loop 固件片段传输
                MCU-->>Matter模块: 请求固件片段N
                Matter模块->>MCU: 发送固件片段N
                
                alt 传输中断
                    MCU-->>Matter模块: 传输错误报告
                    Note over MCU: 原因：<br>1. 通讯中断<br>2. 校验失败<br>3. 接收超时
                    Note over Matter模块, MCU: 流程终止<br>下次上电重新开始
                end
            end
            
            alt 升级执行结果
                MCU-->>Matter模块: 升级成功
                Matter模块->>MCU: 发送确认ACK
            else 升级执行失败
                MCU-->>Matter模块: 升级失败报告
                Note over MCU: 原因：<br>1. 固件验证失败<br>2. 写入闪存错误<br>3. 重启失败
                Note over Matter模块, MCU: 流程结束<br>保持原版本运行
            end
        end
    else 无需升级
        Note over Matter模块: 当前版本已是最新
        Note over Matter模块, MCU: 流程结束
    end
```    