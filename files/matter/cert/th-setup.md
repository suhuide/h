# Matter Test-Harness (TH) 手把手指南（安装 + 自启 + OTBR 配网 + 踩坑实录）
> 适用版本：**Matter 1.6 / TH v2.15+spring2026**（SDK commit: `b91b83f`）
> 环境：Raspberry Pi 4（Ubuntu Server 24.04, IP `192.168.100.22`，用户 `ubuntu`）+ Windows 开发机
> 本文档合并了：安装指南、`q.md` 踩坑总结（阶段一~四）、2026-11-24 实战排障结论（开机自启竞态、OTBR 镜像、SiLabs RCP、代理隧道中断）
> 2026-11-24 整理

---

## 一、三种安装方式怎么选？
| 方式 | 适用场景 | Thread 支持 | 官方支持程度 |
|------|---------|------------|-------------|
| **A：树莓派** | 正式认证测试 | ✅ 完整支持 | ⭐⭐⭐ 官方主推路径 |
| **B：Ubuntu 虚拟机 (VM) + RCP + OTBR** | 开发学习 / 自用 Thread 测试 | ⚠️ **实际可跑通**（需正确配置网络，见方式 B 详解） | ⭐⭐ 官方声明仅 onnetwork，Thread 属于"不官方支持"但技术上可行 |
| **C：Ubuntu 裸机（实体机）+ RCP + OTBR** | 开发 + 自用 Thread 测试 | ⚠️ 技术上可跑通 | ⭐⭐ 社区路径 |

### 关于"VM 能不能跑 Thread"的澄清
官方手册原话是 **"thread networking is not officially supported in VM installations at the moment"**，措辞是 **"not officially supported"（不官方支持）**，不是 **"impossible"（做不到）**：
- ❌ VM **默认 NAT 网络**下：IPv6 包出不去、mDNS 发现不了 DUT → Thread 确实不通
- ✅ VM 配置了**桥接网络 + USB 透传 RCP + IPv6 开启**后：链路和树莓派原理完全一致 → **实际可以跑通 Thread 配网**

**结论**：只要网络配置对，VM + RCP + OTBR 测 Thread 完全可行；但这不在官方测试范围，**正式送 CSA 认证请用树莓派**，自用/开发/预验证没问题。

---
## 二、提前准备清单
### 必备
- ✅ 一台电脑（烧录镜像 / 访问 Web UI / 跑 VM）
- ✅ **Ubuntu Server 24.04.x LTS (64-bit)** 系统镜像（官方只认这个版本）
- ✅ 良好的网络环境（安装时从 GitHub Container Registry 拉 docker 镜像）

### 方式 A（树莓派）额外需要
- ✅ **Raspberry Pi 4 或 5，内存 ≥ 8 GB**（硬性要求）
- ✅ **SD 卡 ≥ 64 GB**（⚠️ 实测杂牌 SD 卡写入仅 ~0.5MB/s，拉镜像会到 1~2 小时；有条件用 SSD/高速卡）
- ✅ Raspberry Pi Imager 或 Balena Etcher

### 方式 B / C（Thread 测试）额外需要
- ✅ **RCP dongle** 二选一：
  - Nordic **nRF52840 dongle**（刷 RCP 固件，见手册 7.1 节）→ 串口设备 **`/dev/ttyACM0`**
  - SiLabs RCP dongle（EFR32，经 CP2102N 桥接）→ 串口设备 **`/dev/ttyUSB0`**
- ✅ 方式 B 还需：Multipass 或其他虚拟机软件 + **桥接网络**配置能力
- ✅ x86_64 平台需本地构建 SDK 镜像（约 3 小时，见文末进阶）

### 可选
- ✅ GitHub Personal Access Token（权限报错时用）
- ✅ CSA 会员账号（访问 PICS 文件、Test Plans）

### 代理隧道（国内网络必配）
TH 宿主机拉 docker 镜像（Docker Hub / ghcr）需要代理。**代理在 Windows 上（clash，127.0.0.1:7890），通过 SSH 反向隧道送到树莓派**：
```powershell
# Windows PowerShell（保持窗口开着，隧道就活着）
ssh -R 0.0.0.0:7890:127.0.0.1:7890 ubuntu@192.168.100.22 -N
```
```bash
# Pi 上验证（应返回非 405/非 000 的 HTTP 响应）
curl -x http://127.0.0.1:7890 -I https://github.com
ss -tlnp | grep 7890        # 应见 0.0.0.0:7890
```
Pi 端 `/etc/ssh/sshd_config` 需有 `GatewayPorts clientspecified`（否则隧道只绑 127.0.0.1，dockerd 连 `192.168.100.22:7890` 会 refused）。

> ⚠️ **隧道是"活物"**：Windows 关机/ssh 窗口关闭/网络抖动都会断。断掉后 docker pull 会**挂死不报错**（症状见踩坑 #13）。**每次上电后要先建隧道、验证通，再做任何 docker pull。**

---
## 三、方式 A：树莓派安装（官方推荐，最省心）
### 第 1 步：烧录系统镜像
1. SD 卡插入电脑，打开 Raspberry Pi Imager 或 Balena Etcher，选 **`Ubuntu Server 24.04.x LTS (64-bit)`**。
2. 自定义设置**必须**配置：
   - `username`：**`ubuntu`** ⚠️ 必须叫 ubuntu，改名会导致 TH 跑不起来
   - `password`：`raspberrypi`
   - `hostname`：`ubuntu`
3. 开启 SSH 服务，刻录完成后插入树莓派。
### 第 2 步：首次开机
接好网线/显示器/键盘，输入 `ubuntu` / `raspberrypi` 登录。
### 第 3 步：安装 TH
```bash
git clone -b v2.15+spring2026 https://github.com/project-chip/certification-tool.git --recurse-submodules
cd certification-tool
./scripts/pi-setup/auto-install.sh
```
结束时**选 1 重启树莓派**，等 10 分钟。
### 第 4 步：获取 IP 并打开 Web UI
```bash
ifconfig    # 记下 IP
```
浏览器访问 `http://<树莓派IP>`，看到 Matter Test Harness 即成功 🎉
> 💡 **每次开机后约 8~10 分钟内网页打不开是正常的**：backend prestart（迁移+解析 XML）约 3 分钟 + frontend 是 Angular 开发服务器（ng serve JIT 编译）约 3~4 分钟。别急着判定故障，等够时间再看。

### 第 5 步（如测 Thread 设备）：RCP + OTBR
1. 刷好 RCP 固件（Nordic 见手册 7.1 / SiLabs 见手册 7.3），插到树莓派 USB。
2. 确认串口设备出现：`ls /dev/ttyUSB* /dev/ttyACM*`
3. **提前拉好 OTBR 镜像**（约 1.2GB，SD 卡上要 1~2 小时，别等跑测试时再拉）：
   ```bash
   docker pull nrfconnect/otbr:9185bda
   ```
4. OTBR 是**按需容器**：跑 Thread 用例时 TH 自动拉起；手动测试/自定义参数用脚本（见第十节）。

---
## 四、方式 B：Ubuntu 虚拟机（VM）+ Thread 配网 ⭐ 重点
> ✅ 适合：已经习惯用 VM 的用户。基础安装官方支持；Thread 配网属于"实际可行、非官方支持"。
### 第 1 步：创建 Ubuntu 虚拟机
```bash
brew install multipass
multipass launch 24.04.x -n matter-vm -c 2 -m 8G -d 50G
multipass shell matter-vm
```
> 💡 如果你的虚拟化方案支持**桥接网络**（bridge mode），第 1 步就配置好，后面 Thread 会顺利很多。Multipass 默认 NAT 网络，需要额外配置桥接。
### 第 2 步：安装 TH（官方支持部分）
```bash
git clone -b v2.15+spring2026 https://github.com/project-chip/certification-tool.git --recurse-submodules
cd certification-tool
./scripts/ubuntu/auto-install.sh
sudo reboot
```
### 第 3 步：获取 IP 并访问 Web UI
```bash
multipass list   # 或 VM 内 ip a
```
浏览器访问 `http://<VM的IP>`。
### 第 4 步：为 Thread 配网做准备（非官方支持，需要手工配置）
#### 4.1 虚拟机网络必须桥接
VM 的网卡必须桥接到**与 DUT 相同的局域网**，否则：
- VM 里 chip-tool 发的 IPv6 包到不了 DUT
- DUT 广播的 mDNS/SD 服务发现包进不了 VM
检查方法：
```bash
ip a    # 确认 VM 有一个和宿主机同网段的 IP
ping <DUT的IP>   # 如果 DUT 已在网内，能 ping 通是基本前提
```
#### 4.2 USB 透传 RCP dongle
RCP 是 `/dev/ttyACM0` 串口设备，需要透传进 VM：
- **VMware / VirtualBox**：USB 设置里添加 nRF52840 dongle（Vendor ID 1915）
- **Multipass**：对 USB 透传支持较弱，建议换 VMware/VirtualBox/KVM 或用 SiLabs Ethernet RCP
VM 内确认：
```bash
ls /dev/ttyACM*
dmesg | tail    # 看是否枚举成功
```
#### 4.3 IPv6 相关
```bash
# 确认 IPv6 没被禁用
sysctl net.ipv6.conf.all.disable_ipv6    # 应为 0
```
### 第 5 步：刷 RCP 固件（可在宿主机或 VM 内刷）
```bash
python3 -m pip install -U nrfutil
nrfutil install nrf5sdk-tools
# dongle 进 DFU 模式（按 Reset 键，红灯闪烁）后刷入
nrfutil dfu usb-serial -pkg nrf52840dongle_rcp_c084c62.zip -p /dev/ttyACM0
```
### 第 6 步：Project Config 里配置 Thread
在 Web UI 创建 Project，编辑 Project Config：
```json
"dut_config": {
  "discriminator": "3840",
  "setup_code": "20202021",
  "pairing_mode": "ble-thread",
  "chip_timeout": null,
  "chip_use_paa_certs": false,
  "trace_log": true
},
"network": {
  "thread": {
    "rcp_serial_path": "/dev/ttyACM0",
    "rcp_baudrate": 115200,
    "on_mesh_prefix": "fd11:22::/64",
    "network_interface": "eth0",
    "dataset": {
      "channel": "15",
      "panid": "0x1234",
      "extpanid": "1111111122222222",
      "networkkey": "00112233445566778899aabbccddeeff",
      "networkname": "DEMO"
    },
    "otbr_docker_image": null
  }
}
```
> ⚠️ `network_interface` 要填 VM 里**桥接到 LAN 的那块网卡名**（`ip a` 查看，可能是 `enp0s3`、`ens33` 等，不一定是 `eth0`）。
> 如果已有现成 Thread 网络和 Border Router，可改用 `operational_dataset_hex`，TH 就不会自己起 OTBR。
### 第 7 步：验证
1. DUT 进入 discoverable 模式（如 nRF52840 DK 按 Button 4）
2. 跑一个基础用例（如 `TC-DRLK-1.1`）
3. TH 日志确认 commissioning 成功
### 方式 B 常见坑
| 问题 | 处理 |
|------|------|
| DUT 发现不了 / commissioning 卡住 | 90% 是网络不是真桥接；确认 VM 和 DUT 同网段、IPv6 通 |
| `/dev/ttyACM0` 不存在 | USB 没透传成功，重配 VM USB 设置；`dmesg` 排查 |
| OTBR 容器报 `409 Conflict` | `docker ps` 清理残留 otbr 容器 |
| `RTNETLINK answers: File exists` | 宿主机/VM 有 IP 段和 OTBR 默认网段（如 `192.168.255.1`）冲突，改 IP |
| 手动想生成 dataset | 跑 `./certification-tool/backend/test_collections/matter/scripts/OTBR/otbr_start.sh` |

---
## 五、方式 C：Ubuntu 裸机（实体机）+ RCP + OTBR
> ✅ 比 VM 少了网络透传这一层，Thread 更稳，配置方法与方式 B 的第 5-6 步完全相同，只是**不需要 USB 透传**（dongle 直接插在实体机上）、`network_interface` 填实体机网卡名即可。
```bash
git clone -b v2.15+spring2026 https://github.com/project-chip/certification-tool.git --recurse-submodules
cd certification-tool
./scripts/ubuntu/auto-install.sh
sudo reboot
```
其余步骤（刷 RCP → Project Config 配 `ble-thread` → 跑测试）与方式 B 第 5-7 步相同。

---
## 六、更新已有 TH
> ⚠️ 前提：系统必须是 Ubuntu Server 24.04.x LTS (64-bit)
```bash
cd ~/certification-tool
./scripts/ubuntu/auto-update.sh v2.15+spring2026
./scripts/start.sh
```
等 10 分钟后浏览器访问。

---
## 七、通用故障排查（三种方式都适用）
### 1️⃣ 启动慢 / `ModuleNotFoundError: No module named 'chipyaml'`
```bash
docker logs certification-tool-backend-1
./scripts/stop.sh
rm ~/certification-tool/backend/test_collections/matter/sdk_tests/sdk_checkout/.version
./scripts/start.sh
```
### 2️⃣ Docker 容器没自动起来
```bash
./certification-tool/scripts/start.sh   # 等 5-10 分钟
```
### 3️⃣ 只读文件系统 / "Is docker daemon running?"
```bash
sudo fsck        # 全部按 y
sudo reboot
# 不行则：
sudo fsck -y -f /dev/mmcblk0p2
```
### 4️⃣ 彻底清理重装（⚠️ 会删光所有数据、镜像、容器）
```bash
./certification-tool/scripts/clean-up.sh
# 树莓派： ./scripts/pi-setup/auto-install.sh
# Ubuntu： ./scripts/ubuntu/auto-install.sh
```
### 5️⃣ "remote: Repository not found"
```bash
mv certification-tool certification-tool-backup
git clone https://<你的token>@github.com/project-chip/certification-tool.git
```
（Token：GitHub → Settings → Developer settings → Personal access tokens (classic)）

---
## 八、进阶：x86_64 平台本地构建 SDK 镜像
> 官方镜像主要面向 arm64（树莓派）。x86_64 的 VM/裸机通常需要本地构建（约 3 小时）：
1. 查 SDK commit：看 `certification-tool/backend/test_collections/matter/config.py` 里的 `SDK_DOCKER_TAG`（最新 `b91b83f`）
2. 下载对应 Dockerfile：
   `github.com/project-chip/connectedhomeip/blob/<COMMIT_SHA>/integrations/docker/images/chip-cert-bins/Dockerfile`
3. 删旧镜像：`docker images` → `docker image rm <IMAGE_ID>`
4. 构建：
   ```bash
   docker buildx build --load --build-arg COMMITHASH=<COMMIT_SHA> --tag connectedhomeip/chip-cert-bins:<COMMIT_SHA> .
   ```
5. 更新示例 app：
   ```bash
   ./backend/test_collections/matter/scripts/update-sample-apps.sh
   ```

---
## 九、开机自启（"上电即用"）配置 ⭐ 2026-11-24 修正版
目标：**上电 → 服务全自动起来 → 浏览器直接访问**。

### 9.1 systemd 单元（⚠️ 不要加 `compose down`！）
```bash
sudo tee /etc/systemd/system/certification-tool.service > /dev/null <<'EOF'
[Unit]
Description=Matter Test Harness (docker compose)
After=docker.service docker.socket network-online.target
Wants=network-online.target docker.socket
Requires=docker.socket

[Service]
Type=oneshot
RemainAfterExit=yes
User=ubuntu
WorkingDirectory=/home/ubuntu/certification-tool
ExecStartPre=/usr/bin/sleep 10
ExecStart=/usr/bin/docker compose up -d --remove-orphans
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=300

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable certification-tool.service
```

**为什么不能加 `ExecStartPre=-docker compose down`（老文档/q.md 坑10 的做法）：**
容器都配了 `restart: unless-stopped` 后，**开机时 docker daemon 会先自动拉起容器**，10 秒后 systemd 再跑 `compose down` 就和它打架：
1. `down` 把启动慢的容器（proxy、db）**删掉**，又因 backend/frontend 还占着网络删不干净而以 exit 1 失败
2. 接着 `up -d` 撞上前端容器名冲突 → 整体失败
3. 结果：**proxy 和 db 再也起不来** → 浏览器 80 端口不通、backend 无限重连数据库
（2026-11-24 实测踩中，见踩坑 #12。`up -d --remove-orphans` 本身幂等且会清孤儿容器，`down` 完全多余。）

### 9.2 容器 restart 策略（四个都要有）
`docker-compose.yml` 中 **db / backend / frontend / proxy** 全部加：
```yaml
    restart: unless-stopped
```
（2026-11-24 实测 frontend 漏了这条，已补。有了它，开机不需要 compose 也能全起来，systemd 单元只是兜底。）

### 9.3 依赖服务自启（应全为 enabled）
```bash
systemctl is-enabled docker                  # enabled
systemctl is-enabled avahi-daemon            # enabled（mDNS 必需，没装先 apt install avahi-daemon）
systemctl is-enabled certification-tool.service   # enabled
```
> ⚠️ **7890 代理隧道不在自启清单里**——它来自 Windows 侧的 `ssh -R`，Windows 开机后要手动开（或做成 Windows 计划任务/autossh）。只要不在 raspi 上做 docker pull，隧道断了不影响 TH 跑测试，只影响拉镜像。

### 9.4 开机时序与验收清单
```
上电 → docker daemon 自启四容器（restart 策略）
     → +10s systemd 跑 up -d（幂等，秒过）
     → backend prestart ~3min → frontend ng serve 编译 ~3-4min
     → 上电后约 8~10 分钟浏览器可访问
```
重启后验收（1 分钟内可完成的检查）：
```bash
systemctl is-active certification-tool.service   # active
docker ps -a --format '{{.Names}}: {{.Status}}'  # proxy/db/backend/frontend 四个全 Up
curl -I http://localhost/docs                    # backend 就绪后 200
```
浏览器：`http://<Pi_IP>/`（frontend，可能要等编译）+ `http://<Pi_IP>/docs`（backend API）。

---
## 十、OTBR 与 Thread 设备手动配网（2026-11-24 实战版）
### 10.1 OTBR 的定位
- **不是常驻服务**：官方 TH 在跑 Thread 用例时按需自动拉起 `otbr-chip` 容器；平时 `docker ps` 看不到它**是正常的**。
- 手动配网/自定义参数时用脚本启动：`~/certification-tool/backend/test_collections/matter/scripts/OTBR/otbr_start.sh`
- 镜像 `nrfconnect/otbr:9185bda`（~1.2GB）**必须提前在本地**（SD 卡上下载+解压要 1~2 小时）。

### 10.2 RCP 串口设备对照（⚠️ 脚本默认值要改）
| RCP | 串口设备 | 脚本适配 |
|-----|---------|---------|
| Nordic nRF52840 dongle | `/dev/ttyACM0` | 默认即可 |
| SiLabs EFR32（CP2102N 桥接，`lsusb` 显示 Silicon Labs CP210x） | **`/dev/ttyUSB0`** | **必须改脚本：设备路径 + 波特率** |

SiLabs RCP 的改法（2026-11-24/25 在 TH 上实测验证：**SiLabs RCP 是 460800 波特率，不是默认的 115200**——115200 下 otbr-agent 报 `Failed to communicate with RCP - no response`，改 460800 后立即可用）：
```bash
sed -i 's|/dev/ttyACM0|/dev/ttyUSB0|g; s|uart-baudrate=115200|uart-baudrate=460800|' \
  ~/certification-tool/backend/test_collections/matter/scripts/OTBR/otbr_start.sh
```
> 判据：`sudo docker logs otbr-chip | grep -i 'RCP'` 出现 `no response from RCP during initialization` = 波特率或固件不对；ot-ctl 能回 `state` = 链路通。

### 10.3 手动配网实战六步（2026-11-25 全链路跑通版本）
> ⚠️ chip-tool 在 cert-bins 镜像里的实际路径是 **`/root/apps/chip-tool`**（不在 PATH）；必须挂载 DBus（否则启动即报 `CHIP Error 0x000000AD: Open file failed`）；测试 DAC 需要 PAA 证书库。
```bash
# ① 起 OTBR（内部用 sudo 起 --network host 的 otbr-chip 容器）
sudo ~/certification-tool/backend/test_collections/matter/scripts/OTBR/otbr_start.sh

# ② 确认 RCP 链路通（应回 disabled/retained；NoResponse = 波特率/固件不对）
sudo docker exec otbr-chip ot-ctl state

# ③ 建 Thread 网络 + 取 dataset
sudo docker exec otbr-chip ot-ctl dataset init new
sudo docker exec otbr-chip ot-ctl dataset commit active
sudo docker exec otbr-chip ot-ctl ifconfig up
sudo docker exec otbr-chip ot-ctl thread start
sudo docker exec otbr-chip ot-ctl state          # 应为 leader
sudo docker exec otbr-chip ot-ctl dataset active -x   # 输出 hex，下面要用

# ④ 准备开发 PAA 证书库（一次性；232 个官方开发 PAA）
https_proxy=http://127.0.0.1:7890 git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/project-chip/connectedhomeip /tmp/chip-cred
cd /tmp/chip-cred && git sparse-checkout set credentials/development/paa-root-certs

# ⑤ BLE+Thread 配网（DUT 先进入 BLE 配网广播！）
sudo docker run --rm --privileged --network host \
  -v /var/run/dbus:/var/run/dbus \
  -v /tmp/chip-cred/credentials/development/paa-root-certs:/paa:ro \
  connectedhomeip/chip-cert-bins:b91b83ffa967e2fffca471fb28c745ae6fd3ec9d \
  /root/apps/chip-tool pairing ble-thread 1 hex:<dataset_hex> <setup_code> <discriminator> \
  --paa-trust-store-path /paa
# 成功标志：Received CommissioningComplete response, errorCode=0 / completed with success

# ⑥ 验证 DUT 已挂网（OTBR 侧看 child table 出现 DUT 即成）
sudo docker exec otbr-chip ot-ctl child table
sudo docker exec otbr-chip ot-ctl neighbor list
```
实测（2026-11-25）：`discriminator=1064`、`setup_code=41784691`，一次通过。
> ⚠️ **chip-tool 的 fabric 存在容器临时目录里，`docker run --rm` 每次都是全新 fabric**——配网后想做 CASE 应用层验证（如 `basicinformation read vendor-id 1 0`），必须把 kvs 挂出来持久化（`-v /tmp/chiptool:/tmp`），且**配网和应用层验证要在同一份存储里做**；否则需让 DUT 重新进配网模式再来一遍。
> raspi 的 BLE（`hciconfig` 应见 `hci0 UP RUNNING`）与 Avahi 需正常。

### 10.4 BLE 配网失败模式与对策（2026-11-25 实测汇总）
| 报错 | 含义 | 对策 |
|------|------|------|
| `No matching device found` / 扫不到 | DUT 退出了配网模式（一次失败的配网尝试就会退出） | DUT 重新进配网模式（断电重上电） |
| 连上后 20s `CHIP Error 0x00000032: Timeout` | 瞬态，BLE 通道首包无响应 | **直接重试**（实测第二次就通到 Attestation） |
| `GDBus le-connection-abort-by-local` | BlueZ 残留连接缓存 | `bluetoothctl remove <DUT_BLE_MAC>` 后重试 |
| `err 101 (PAA not found in DCL...)` | DUT 是测试 DAC，PAA 不在 DCL | 挂载开发 PAA 库 + `--paa-trust-store-path`（见 10.3 ④⑤） |
| 启动即 `CHIP Error 0x000000AD: Open file failed` | 容器里没有 DBus socket | docker run 加 `-v /var/run/dbus:/var/run/dbus` |

### 10.4 ⚠️ MT 二维码转录坑
包装/软件里的 `MT:` 码是 base38 **分块**编码（5 字符→3 字节），**手抄或 OCR 极易错一个字符**——整串解码会得到完全不同的 discriminator/pin（实测 `MT:K2CA0WSC00J19D1LX00` 解出 disc=143/pin=10485760，与设备真实值 1064/41784691 对不上）。
**配网凭据以设备日志、供应商 App 显示的 discriminator/setup_code 为准，不要依赖手抄的 MT 码解码。**

---
## 十一、国内网络拉镜像实战（2026-11-24 补充）
### 路径 A：代理隧道（默认方案）
见第二节。**每次上电后先验隧道再 pull**：
```bash
curl -x http://192.168.100.22:7890 -sI --max-time 8 https://registry-1.docker.io/v2/ | head -1
# 返回 HTTP/1.1 401 即通（401=要鉴权=链路通）
```
### 路径 B：国内镜像站直连（隧道不稳时的备选）
Docker Hub 直连必超时，但国内镜像站可直连（无需代理）。**daemon.json 配 registry-mirrors 或直接换完整镜像名**：
```bash
# 直接从镜像站拉（拉完改名，脚本认原名）
docker pull docker.m.daocloud.io/nrfconnect/otbr:9185bda
docker tag  docker.m.daocloud.io/nrfconnect/otbr:9185bda nrfconnect/otbr:9185bda
```
> ⚠️ 实测 daocloud 会抖（单层重试 65 次仍失败），配自动重试循环自愈：
> ```bash
> nohup bash -c 'for i in $(seq 1 25); do docker pull docker.m.daocloud.io/nrfconnect/otbr:9185bda && break; sleep 10; done' > ~/pull.log 2>&1 &
> ```
> blob 按 digest 缓存，重试不重下已完成的层；SD 卡解压慢（~7min/层）是正常速度。
> ⚠️ ghcr.io（backend/frontend 镜像）国内可直连，不需要代理。

---
## 十二、踩坑实录（q.md 全量 + 2026-11-24 新坑）
> 排障口诀：**先二分（本地通不通）→ 看 `ps -a` 和 journalctl 具体报错行 → 报错变化 = 进展**。

### 阶段一：安装（auto-install.sh）
| # | 现象 | 根因 | 解法 |
|---|------|------|------|
| 1 | `curl (35) Connection reset`，且 sudo/非 sudo 报错各不同 | docker.com CDN 间歇重置 + sudo 写 keyrings 权限墙 | 手动下载 GPG key 到 /tmp 再 sudo 移入；sed 注释掉脚本报错行；手动补 apt 源（详见 q.md 坑1） |
| 2 | `git@github.com: Permission denied (publickey)` | submodule remote 是 SSH 协议 | `git config --global url."https://github.com/".insteadOf git@github.com:` |
| 3 | CMD 能 ssh，MobaXterm/Tabby 不能 | GUI 工具不自动加载 `~/.ssh` 私钥 | 手动指定与 CMD 相同的私钥文件 |

### 阶段二：首启与 Web UI
| # | 现象 | 根因 | 解法 |
|---|------|------|------|
| 4 | 重启后网页打不开、容器列表为空 | 安装中断导致容器没创建 | 本地 `curl -I http://localhost` 二分；`docker compose up -d` 手动拉起 |
| 5 | `registry-1.docker.io` 拉镜像超时 | 国内直连 Docker Hub 受限 | 镜像加速器或 dockerd 代理（见第二/十一节） |
| 6 | `required variable DOMAIN is missing` | `.env` 缺失/被手写覆盖 | `rm .env` 后用官方脚本重新生成，绝不手写 |

### 阶段三：代理链路
| # | 现象 | 根因 | 解法 |
|---|------|------|------|
| 7 | git clone GnuTLS 错 / 拉镜像慢 | 容器代理、daemon 代理、隧道绑定是**三层**不同主体 | 逐层配置逐层验证（见第二节表格） |
| 8 | commissioning 报 `CHIP Error 0x000000AC` | 宿主机没装 Avahi，mDNS 不可用（容器挂了 DBus socket ≠ mDNS 可用） | `apt install avahi-daemon avahi-utils && enable --now` |

### 阶段四：开机自启
| # | 现象 | 根因 | 解法 |
|---|------|------|------|
| 9 | "敲了命令才好"的错觉 | `logs` 不启动服务；看现象别推断因果 | 状态看 `compose ps -a`，日志看具体报错行 |
| 10 | 自启后容器 `Created` 残留 / 撞名 | 上次半途失败留残骸 | 老方案是加 `compose down`——**已被 #12 推翻**，改用 #12 方案 |
| 11 | `active (exited)` 误判为故障 | oneshot 正常状态 | `status=0/SUCCESS` + RemainAfterExit 就是正常 |
| **12** | **自启后 proxy/db 消失，backend 连不上 db，网页不通**（2026-11-24） | **daemon 先自动拉容器，systemd 的 `compose down` 把 proxy/db 删掉后撞名冲突** | **删掉 `ExecStartPre down`，改 `up -d --remove-orphans`（第九节修正版）** |
| **13** | **docker pull 挂死无报错：无 443 连接、负载归零、日志无错误；重启后直接 `proxyconnect refused`**（2026-11-24） | **Windows 侧 7890 隧道中断，daemon 对死连接干等** | 重建隧道并 `curl -x` 验证后再 pull；根治靠 daemon.json mirrors 或 autossh 常驻隧道 |
| **14** | OTBR 镜像不存在，Thread 用例跑不了；脚本挂 `/dev/ttyACM0` 但 RCP 是 SiLabs（`/dev/ttyUSB0`） | 定制安装不含预置镜像；脚本按 Nordic 写死 | 提前 `docker pull`（第十一节）；`sed` 改脚本 ttyUSB0（第十节） |
| **15** | frontend 重启后不起 | compose 里 frontend 无 restart 策略 | 四个服务统一 `restart: unless-stopped` |
| **16** | 手抄 MT 码解码出的 disc/pin 与设备真实值不符 | base38 转录误差 | 用设备日志/App 显示的凭据（第十节 10.4） |

### 重点坑排查复盘（命令级，按实际排查顺序）

> 通用方法论（每个案例都在用）：
> 1. **先二分**：Web 不通时先在 Pi 本地 `curl -I http://localhost`——本地不通=服务没起，本地通外部不通=网络/防火墙
> 2. **看状态与日志的具体行**：`docker compose ps -a`（含退出容器）、`journalctl -u <svc> -b --no-pager`，不凭"敲了什么之后好了"推断因果
> 3. **报错变化 = 进展**：`deadline exceeded` → `connection refused` 说明代理已生效、只剩绑定问题
> 4. **判"挂死"用三零判据**：无 443 连接 + 负载≈0 + 日志无新行，三者齐 = 真挂死；只是慢的话三者至少有一个在动

#### 复盘 1：上电后浏览器不通，db 卡 Created、proxy 容器凭空消失（坑 12）
**现象**：上电约 12 分钟后 `http://<Pi_IP>/` 不通；backend 日志刷屏 `could not translate host name "db" to address`（已重试 300 次）。

**排查链**：
```bash
docker ps -a --format '{{.Names}}: {{.Status}}'
# → db: Created（创建了但从没启动过！）；proxy: 整个不存在；backend/frontend: Up
docker start certification-tool-db-1        # 手动拉 db，成功，backend 立刻恢复
# ↑ 说明镜像、数据卷、配置全正常，问题只剩"为什么开机没把它拉起来"
journalctl -u certification-tool.service -b --no-pager | tail -30
# → 还原了完整时间线：
#   ① 02:14:25  compose down 停掉 proxy、db 并删除（能删到说明它们当时是停着的）
#   ② 02:14:44  删 chip-default 网络失败 "Resource is still in use"（backend/frontend 占着）→ down 以 exit 1 结束
#   ③ 02:14:46  up -d 撞上 "container name frontend-1 already in use" → 单元整体 failed
#   结论：开机时 docker daemon 先按 restart 策略自动拉起了容器，
#        10 秒后 systemd 的 ExecStartPre compose down 与它打架：把启动慢的 proxy/db 删了，
#        又因网络删不干净而失败，随后的 up 再撞名 → proxy/db 永久缺失
```
**根因**：`ExecStartPre=-docker compose down`（老文档为治"残留容器"加的）在"四容器都配了 `restart: unless-stopped`"的新前提下变成了**自毁机制**。
**解法**：删掉 `ExecStartPre down`；`ExecStart` 改 `up -d --remove-orphans`（幂等、自带孤儿清理）；frontend 补 `restart: unless-stopped`。改动前备份：`cp xxx.service xxx.service.bak`，改完 `systemctl daemon-reload`。
**验证**：一次计划外重启（05:41）天然成为验收——开机后 `docker ps` 四容器全 Up、`systemctl is-active` = active，浏览器 8~10 分钟后可访问。
**反直觉点**：`Created` 状态 ≠ 启动失败，= "创建了但从未 start"；看到它就往"谁创建了它但没启动它/谁把它删了"方向查。

#### 复盘 2：docker pull 先挂死不报错、重启后秒报 proxyconnect refused（坑 13）
**现象**：pull 先后两次在"下载完/解压中途"卡死 25 分钟以上，无任何报错；重启后 `docker pull` 秒败：`proxyconnect tcp: dial tcp 192.168.100.22:7890: connect: connection refused`。

**排查链**：
```bash
# ① 先区分"慢"还是"挂死"（三零判据）：
ss -tn | grep ':443'            # 0 条连接
cat /proc/loadavg               # 0.3 左右（归零）
tail -f /tmp/otbr_pull.log      # 十几分钟无新行
# 三者齐 → 真挂死；kill 掉 pull 进程重拉（blob 按 digest 缓存，不重下已完成的层）
# ② 重启后 pull5 直接给答案：
#    "proxyconnect tcp: dial tcp 192.168.100.22:7890: connection refused"
#    → daemon 配置了代理且代理不在了
grep -r 7890 /etc/docker/ /etc/systemd/system/docker.service.d/ 2>/dev/null
# → /etc/systemd/system/docker.service.d/http-proxy.conf: HTTP(S)_PROXY=http://192.168.100.22:7890
pgrep -af 'clash|mihomo|v2ray|sing-box'   # 空！Pi 上根本没有代理进程
# ③ 关键认知：7890 是 Windows 侧 `ssh -R 0.0.0.0:7890` 反向隧道；
#    隧道随 Windows/ssh 会话消失，Pi 重启后更不会自己回来。
#    "下载到一半挂死" = 隧道中途断，daemon 对死连接干等（三零）；"重启后 refused" = 隧道根本不在。
# ④ 恢复隧道后先验证再 pull（401=链路通）：
curl -x http://127.0.0.1:7890 -sI --max-time 8 https://registry-1.docker.io/v2/ | head -1   # HTTP/1.1 401
```
**根因**：daemon 代理指向 raspi 自身 7890，而该端口靠 Windows `ssh -R` 隧道供给——隧道是"活物"。
**解法**：每次上电后先建隧道并 curl 验证，再做 pull；根治两条路：daemon.json 配 `registry-mirrors`（镜像站直连，不依赖隧道），或 Windows 侧 autossh/计划任务保活隧道。
**附带教训**：
- `systemctl restart docker` 可解 daemon 层挂死，代价是四容器弹一下自动恢复（blob 缓存在磁盘，不重下）
- `pkill -f` 的模式字符串会匹配到**自己所在的 ssh 命令行**把自己杀掉（exit 255）——模式写短点或用 pgrep 出 PID 再 kill

#### 复盘 3：镜像拉取整体极慢（1.2GB 要 1~2 小时）
**现象**：7 层镜像，~7 分钟/层，下载 ~100~200KB/s，重启/失败后进度"回退"。
**排查**：`grep -c 'Pull complete' 日志` 看层数进度；`grep eth0 /proc/net/dev` 两次采样差值看实时速率；对照 `loadavg` 区分"在下载（CPU 闲但流量>0）"与"在解压（CPU 忙）"。
**结论与对策**：
- 瓶颈=SD 卡解压写盘 + 出口带宽，换路径（代理 vs daocloud 镜像站）实测都在 ~100KB/s 量级 → 不折腾路径
- docker pull **无断点续传**：未完成的 blob 丢了就整层重下；但**已完成的 blob 按 digest 全局缓存**，跨重启、跨镜像站（同 digest）都复用 → 配 `for i in $(seq 1 25); do docker pull … && break; sleep 10; done` 自愈循环兜底，失败自动续
- 根本解：**提前把镜像拉好**（搭好环境就 pull 完 nrfconnect/otbr），别在测试当天拉

#### 复盘 4：OTBR 镜像缺失 + 脚本挂错串口（坑 14）
**现象**：`docker images` 里没有 otbr；Thread 用例会失败。
**排查链**：
```bash
docker images | grep otbr                          # 空 → 镜像没预装
grep -riE 'otbr' ~/certification-tool/docs/        # 官方文档确认：OTBR 是按需容器，
                                                   # 跑 Thread 用例时 TH 自动拉起 → 平时看不到它是正常的
grep -E 'docker run' .../scripts/OTBR/otbr_start.sh  # 发现硬编码 -v /dev/ttyACM0:/dev/radio
udevadm info /dev/ttyUSB0 | grep -E 'VENDOR|MODEL'   # → Silicon Labs CP2102N → 这是 SiLabs RCP！
ls /dev/ttyACM*                                     # 不存在 → 本机根本没有 Nordic 棒
```
**解法**：`sed -i 's|/dev/ttyACM0|/dev/ttyUSB0|g' otbr_start.sh`；提前 `docker pull nrfconnect/otbr:9185bda`。
**方法**：设备到底是谁，用 `udevadm info` 看 USB VID/PID 说话，不靠猜。

#### 复盘 5：MT 二维码解码结果与设备真实凭据对不上（坑 16）
**现象**：手抄的 `MT:K2CA0WSC00J19D1LX00` 解码得 disc=143 / pin=10485760，但设备真实值是 disc=1064 / pin=41784691。
**排查链**：
```bash
# ① 第一次按"整串一个大数"解码 → 结果不合理（version/flow/discovery 越界）→ 编码方式错了
# ② 查 SDK 源码（本地 matter_sdk/src/setup_payload/python/Base38.py）：
#    base38 是分块编码：5 字符→3 字节、4→2、2→1；字符表是 0-9A-Z-.（38 个，没有下划线）
# ③ 按分块重解 → 字段格式全合理（version=0、flow=0、8 位 pin）但数值与设备不符
#    → 编码理解已对，输入（手抄的码）有错
```
**结论**：**不要依赖手抄/OCR 的 MT 码**；discriminator/setup_code 以设备日志或供应商 App 显示为准。此坑也说明：解码结果"字段格式合理"≠"数值正确"，转录错一个字符整个 payload 全变。

#### 复盘 6：开机后浏览器 502/000——不是故障，是启动时序（坑 4 的姊妹）
**现象**：上电后 `http://<Pi_IP>/` 返回 502，`/docs` 也 000。
**排查**：
```bash
docker ps                     # 四容器全 Up → 容器没问题
docker logs certification-tool-frontend-1 | tail   # 还在 "Compiling @angular/..." → ng serve JIT 编译中
# traefik 日志: 502 → http://172.19.0.5:4200   → 转发正常，是 frontend 没绑完 4200
docker exec certification-tool-frontend-1 cat /proc/net/tcp | grep -i 1068   # 4200 未绑定
# 等 2~4 分钟后 4200 绑定（00000000:1068），浏览器 200
```
**结论**：backend prestart（~3 分钟）+ frontend Angular 开发服务器编译（~3-4 分钟），**上电 8~10 分钟内网页不可用是设计如此**，先等够时间再排查；期间 `/docs` 200 即 backend 已就绪。

### 通用管理速查
| 操作 | 命令 |
|---|---|
| 查看服务状态（避免分页） | `systemctl status certification-tool.service --no-pager` |
| 手动启动/停止 | `sudo systemctl start/stop certification-tool.service` |
| 重启单个服务 | `docker compose restart backend` |
| 修改 .env 后生效 | `docker compose up -d backend`（restart 不会重读 .env） |
| 查开机日志 | `journalctl -u certification-tool.service -b --no-pager` |
| 判断 pull 是否真挂死 | `ss -tn \| grep 443`（无连接）+ `cat /proc/loadavg`（≈0）+ 日志无新行，三齐 = 挂死，杀掉重来 |

---
## 十三、迁移
直接 dd if=/dev/sdX of=image.img 会把整张卡的物理容量（包括尾部未使用的空隙）都复制进去，产物与原卡等大，而且：
换一张更小的卡 → 写不进去
换一张“看起来同容量”的卡 → 实际容量往往差几百 MB（不同厂商标称 64GB 实际可能是 62.9 vs 63.3GB），直接失败
映像文件巨大（64GB 卡 = 64GB 文件，哪怕实际只用了 20GB）
### 方案
dd 截断到最后使用的扇区 + PiShrink 收缩
#### 1. 找到最后写入的扇区
把 TF 卡插到 Linux 机器（或用 Pi 自身 + 读卡器），假设卡是 /dev/sdb：
    
```c
# 找最后一个分区的结束扇区
sudo fdisk -l /dev/sdb
```
      
记录输出里最后一个分区的 End 扇区号，比如 End = 24575999。用 Pi 本身也行（用读卡器挂另一张卡更方便；如果 dd 自己正在运行的系统盘会有不一致风险，尽量在关机后用另一台 Linux 操作）。

#### 2. 只复制到该扇区（截断 dd）
```c
# count = End扇区 + 1
sudo dd if=/dev/sdb of=th-backup.img bs=4M count=24576000 bs 单位换算见下 status=progress conv=fsync
```  
更稳妥的算法（按扇区 × 512）：
```c
sudo dd if=/dev/sdb of=th-backup.img \
  bs=512 count=$((24575999 + 1)) status=progress conv=fsync
```      
这样产出的映像只包含实际数据区（可能 25GB 而不是 64GB），且分区表完整、能直接写回任何不小于此映像的卡。

## 十四、重要提醒
| # | 提醒 |
|---|------|
| 1 | 系统只认 **Ubuntu Server 24.04.x LTS (64-bit)** |
| 2 | 树莓派用户名**必须是 `ubuntu`** |
| 3 | `git clone` 一定带 `--recurse-submodules` |
| 4 | 第一次启动慢（要下载镜像）是正常的；**每次开机后 8~10 分钟网页才可用也是正常的**（ng serve 编译） |
| 5 | **VM 跑 Thread 的关键三件事**：桥接网络、USB 透传 RCP、IPv6 开启 |
| 6 | VM/裸机跑 Thread 属于"非官方支持但可行"，**正式送 CSA 认证请用树莓派** |
| 7 | PICS 文件、Test Plans 等官方文档需要 CSA 会员账号 |
| 8 | **上电三查**：四容器 Up？隧道 7890 通？`docker images` 里 otbr 镜像在？——齐了才开测 |

---
## 附：版本速查表（最新在最下）
| Matter 版本 | TH 版本 | 安装用的 tag/branch | SDK commit |
|------------|---------|--------------------|-----------|
| 1.3 | v2.10.4+spring2024 | `v2.10.4+spring2024` | 50bcad1 |
| 1.4 | v2.11+fall2024 | `v2.11+fall2024` | f2e5de7 |
| 1.4.1 | v2.12+spring2025 | `v2.12+spring2025` | 91eab26 |
| 1.4.2 | v2.13+summer2025 | `v2.13+summer2025` | 1b2b3fd |
| 1.5 | v2.14+fall2025 | `v2.14+fall2025` | ca9d111 |
| 1.5.1 | v2.14.1+winter2026 | `v2.14.1+winter2026`（branch） | e9ecfc2 |
| **1.6（最新）** | **v2.15+spring2026** | **`v2.15+spring2026`（branch）** | **b91b83f** |
