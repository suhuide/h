# AweSun 虚拟显示驱动导致多屏失效 — 排查与修复总结

**日期**：2026-08-21
**机器**：本机（Windows 11 Pro，Intel UHD Graphics 770）
**症状触发**：使用 AweSun（向日葵/Sunlogin）远程访问另一台电脑后

---

## 1. 故障现象

- 本机原为双屏：**Dell P2225H**（主屏，DisplayPort）+ **Lenovo S27i-30**（副屏）
- 用完 AweSun 远程后，只剩单屏可用
- **两块屏单独插都能用，但同时插只识别一块** —— 副屏在 Windows 里"未检测到"
- 重启不恢复，跨重启持续
- 远端机当时未确认状态

## 2. 根因

AweSun 装了一个 **Indirect Display Driver（IDD）虚拟显示驱动** `OrayIddDriver Device`，作为虚拟显卡挂在显示适配器列表里，和 Intel UHD Graphics 770 平起平坐。这个虚拟显卡**开机自启、常驻启用**，占了一个显示位，导致 Intel GPU 不再去枚举 DisplayPort 上的 Dell P2225H。

不是临时会话状态问题，是**驱动级配置改动**，所以重启无效。

## 3. 关键证据

### 显示适配器（PnP）
| 设备 | InstanceId | 状态 |
|---|---|---|
| OrayIddDriver Device（虚拟显卡） | `ROOT\DISPLAY\0000` | OK ← 占用显示位 |
| Intel(R) UHD Graphics 770 | `PCI\VEN_8086&DEV_4680...` | OK |

### 显示器（PnP）
| FriendlyName | InstanceId | 修复前状态 |
|---|---|---|
| Dell P2225H(DisplayPort) | `DISPLAY\DELA25F\...UID8258` | **Unknown** ← 真副屏没驱动起来 |
| Generic Monitor (S27i-30) | `DISPLAY\LEN63DF\...UID49` | OK |
| Generic Monitor（虚拟屏） | `DISPLAY\MS_0001\...UID2142332` | Unknown（Oray 虚拟屏） |

Dell P2225H 的 `ConfigFlags=0`、无 ProblemCode —— 说明 Windows 记得这台显示器存在过，只是当前没在驱动它，不是设备本身坏了或被禁用。

### 虚拟驱动信息
- 发布名：`oem73.inf`
- 原名：`orayidddriver.inf`
- 厂商：Shanghai Best Oray Information Technology Co., Ltd.
- 驱动日期：2025-06-11，版本 17.50.19.949
- 服务：WUDFRd（用户态驱动框架）
- 同机还存在另两个 Oray 驱动：`orayusbvhci.inf`（USB 虚拟化）、`orayvgc.inf`（虚拟显卡配套）

### AweSun 安装信息
- 程序目录：`C:\Program Files\Oray\AweSun`
- 数据目录：`C:\ProgramData\Oray\AweSun`、`C:\ProgramData\Oray\Webview2`
- 服务：`AweSunService`、`SunloginService`（均为 Manual 启动、当时已停止）
- 没有标准的 Uninstall 注册表项（不在"添加删除程序"列表里）

## 4. 修复方案

只禁用虚拟显卡，不卸载 AweSun（用户选择保留 AweSun 以备后用）。

### 执行脚本
路径：`C:\Users\huide\AppData\Local\Temp\fix-awesun-display.ps1`
日志：`C:\Users\huide\AppData\Local\Temp\fix-awesun-display.log`
提权方式：`Start-Process -Verb RunAs`（弹 UAC，用户点"是"）

### 关键步骤
```powershell
# 1) 停服务（本就停着）
Stop-Service -Name AweSunService, SunloginService -Force

# 2) 禁用虚拟显卡（核心动作）
Disable-PnpDevice -InstanceId "ROOT\DISPLAY\0000" -Confirm:$false

# 3) 触发硬件重扫，让 Intel GPU 重新枚举 DisplayPort
Start-Process pnputil.exe -ArgumentList "/scan-devices" -Wait

# 4) 给副屏兜底（实际不需要，重扫后 Dell 直接 OK）
Enable-PnpDevice -InstanceId "DISPLAY\DELA25F\4&1FBA9F9&0&UID8258" -Confirm:$false

# 5) 强制扩展模式
Start-Process displayswitch.exe -ArgumentList "/extend" -Wait
```

### 修复后状态
| 设备 | 修复前 | 修复后 |
|---|---|---|
| OrayIddDriver Device | OK（占位） | Error（已禁用，符合预期） |
| Intel UHD Graphics 770 | OK | OK |
| **Dell P2225H（主屏）** | **Unknown** | **OK** |
| Lenovo S27i-30（副屏） | OK | OK |
| Generic Monitor（虚拟屏） | Unknown | Unknown（随虚拟显卡一起失效，正常） |

## 5. 后续注意事项

- **Dell 主屏身份需手动恢复**：Settings → System → Display → 点 Dell → "Make this my main display"。Windows 当前可能误把 Lenovo 当主屏
- **屏幕排列**：在 Display 设置里把两个矩形拖到与物理摆位一致，否则鼠标穿屏方向会反
- **刷新率可能降到 60Hz**：单 Lenovo 时是 99Hz，双屏后 Intel GPU 当前是 1920×1080@60Hz。要恢复高刷：Settings → System → Display → Advanced display → 选 Lenovo → 调高 Refresh rate
- **AweSun 仍可用**：只禁用了虚拟显示驱动，远程控制功能不受影响。只是 AweSun 的"虚拟显示器"特性（远程时伪造一块屏）失效
- **要恢复虚拟屏**：设备管理器 → 显示适配器 → OrayIddDriver Device → 启用；或 `Enable-PnpDevice -InstanceId "ROOT\DISPLAY\0000" -Confirm:$false`（需管理员）

## 6. 备选方案（未采用）

**彻底卸载 AweSun**：清除 AweSun + Sunlogin 所有组件 + 三个 oray 驱动（`orayidddriver.inf`、`orayusbvhci.inf`、`orayvgc.inf`）。适合以后不再用 AweSun 的情况。当时用户选了保守路线。

## 7. 教训

- 远程桌面软件（AweSun/Sunlogin、TeamViewer、AnyDesk、向日葵等）安装的**虚拟显示驱动**会改动本机显示拓扑，不只是临时影响会话期间
- 双屏单独能用但不能同时用 + PnP 显示器状态 Unknown + 重启无效 —— 这个组合几乎是虚拟显示驱动冲突的指纹特征
- 修这类问题先看 `Get-PnpDevice -Class Display` 和 `-Class Monitor`，定位虚拟显卡和挂掉的副屏，不要急着重装显卡驱动
