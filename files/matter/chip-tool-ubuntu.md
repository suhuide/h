# Ubuntu 上 chip-tool / chip-cert / OTBR 完整编译配置指南

> 实测环境：eric-pc · Ubuntu 26.04 LTS (resolute) · kernel 7.0.0-31-generic · Intel i5-14500 (14C/17G) · VirtualBox 虚拟机
> 实测日期：2026-09-17 ~ 09-22（snap 方案失败后全部改为源码编译，本文为实际踩坑与解决方案记录）
>
> 硬件接线：
> - **RCP（Thread 无线协处理器）= `/dev/ttyUSB0`**（Silicon Labs CP210x UART Bridge，115200）
> - **BLE 蓝牙控制器 = `/dev/ttyACM0`**（J-Link OB 板载 VCOM，用 `hciattach` 挂成 `hci0`）
> - 基础网络口（infra interface）= `enp0s3`（192.168.100.x）
---

## 1 速查（结果一览 / 路径 / 命令）

### 1.1 结果一览

| 工具 | 源码位置 | 产物 | 版本 |
|---|---|---|---|
| chip-tool | `/data/connectedhomeip` (master 6c8f029dd2) | `/data/connectedhomeip/out/chip-tool/chip-tool` → 软链 `/usr/local/bin/chip-tool` | master 1.4 分支 |
| chip-cert | 同上 | `/data/connectedhomeip/out/linux-x64-chip-cert/chip-cert` → `/usr/local/bin/chip-cert` | chip 0.0.0 |
| chip-ota-provider-app | 同上 | `/data/connectedhomeip/out/ota-provider-app/chip-ota-provider-app` → 软链 `~/chip-ota-provider-app` | 0.3.0 级（配网后可当 OTA 服务端） |
| otbr-agent / ot-ctl | `/data/ot-br-posix` (7bda286) | `/usr/sbin/otbr-agent`、`/usr/sbin/ot-ctl`（systemd 服务） | 0.3.0-7bda286 |

已验证功能：chip-tool 手动码解析（34970112332 → disc 15 / PIN 20202021）；chip-cert 证书链生成+校验（ECDSA P-256）；OTBR 组网、Border Routing、邻居节点收发；**OTA 全流程**（配网 provider → announce → BDX 传输 → ApplyUpdate，实测通过）。

### 1.2 相关路径速查

```text
/data/connectedhomeip/                     Matter SDK（已离线修复 bootstrap）
/data/connectedhomeip/.environment/        pigweed CIPD 工具链（gn/ninja/clang/zap）
/data/connectedhomeip/scripts/activate.sh  每次编译前先 source
/data/connectedhomeip/out/chip-tool/       chip-tool 产物
/data/connectedhomeip/out/linux-x64-chip-cert/  chip-cert 产物
/data/connectedhomeip/out/ota-provider-app/  chip-ota-provider-app 产物
/data/ot-br-posix/                         OTBR 源码（build/otbr 为构建目录）
/data/lldshim/                             llvm linker shim（ld/ar/ranlib/nm）
/usr/local/bin/{ld,ar,ranlib,nm}           shim 永久软链（删掉即还原 GNU binutils）
/usr/local/bin/{chip-tool,chip-cert}       工具软链
/etc/default/otbr-agent                    OTBR 启动参数（RCP/infra 接口）
/etc/systemd/system/otbr-agent.service     原生 OTBR 服务（Restart=always）
/etc/systemd/system/hciattach-jlink.service  BLE 热插拔 attach 服务
/etc/udev/rules.d/90-jlink-ble.rules        BLE udev 规则（别名 jlink-ble + 触发服务）
/var/lib/thread/                           Thread 网络凭据（持久化，重启自动回连）
/data/chiptool/                            迁移部署包
```

### 1.3 日常使用命令

```c
# Thread 网络（首次组网）
sudo ot-ctl dataset init new
sudo ot-ctl dataset commit active
sudo ot-ctl ifconfig up
sudo ot-ctl thread start
sudo ot-ctl state                # → leader / router
sudo ot-ctl dataset active -x    # 导出数据集(hex)，BLE 配网用

# Matter 配网（chip-tool 走 BLE + Thread，数据集用上一条的输出）
chip-tool pairing ble-thread <dataset-hex> 20202021 3840
```

### 1.4 版本（Matter 核心规范）

本构建（master 6c8f029dd2, 2026-08-07）实现的 Matter 核心规范版本：**1.6.1**

| 项 | 值 | 来源 |
|---|---|---|
| Matter 核心规范 | **1.6.1**（`kSpecificationVersion = 0x01060100`） | `src/app/SpecificationDefinedRevisions.h` |
| Interaction Model revision | 12 | 同上 |
| Data Model revision | 21 | 同上 |
| SDK 发布线 | v1.4.2.0-3584-g6c8f029dd2（发布 tag ≠ 规范版本） | `git describe --tags` |
```c
[DMG] 	InteractionModelRevision = 12
```
```c
# 查任意 SDK 的规范级别：按 MAJOR.MINOR.REV.BUILD 打包
grep kSpecificationVersion /data/connectedhomeip/src/app/SpecificationDefinedRevisions.h
# 0x01000000=1.0  0x01040000=1.4  0x01050000=1.5  0x01060100=1.6.1

# 查已配网设备的认证规范级别（注意：是设备的，不是 commissioner 的）
chip-tool basicinformation read specification-version <nodeid> 0
```

注意事项：
- **二进制本身无内嵌版本信息**（无 version 子命令、无版本字符串），部署包用 `sdk-version.txt` 记录打包时的版本。
- 仓库根目录 `SPECIFICATION_VERSION` 文件（写着 1.2.0）只是认证工具链标记，**不代表** SDK 实现的规范版本。
- 规范级别以**编译时**为准：`git pull` 重编后可能变化，拷贝出去的二进制停留在打包时的 1.6.1。

---

## 2 编译前的关键坑

### 坑 1：CIPD 服务器被墙 → bootstrap 卡死
`scripts/bootstrap.sh` / `activate.sh` 需要访问 `chrome-infra-packages.appspot.com`，本网络 DNS 污染 + 连接超时，会重试 20+ 分钟后失败，且 Python venv 装不上一半（报 `No module named 'coloredlogs'`）。

**解决：离线修复（工具链其实早已在 `.environment/` 里，4.9G）**

```c
cd /data/connectedhomeip
# 1) 用 --trust-cipd-hash 跳过 CIPD 联网（本机缓存的 packages.sha256 与 ensure 文件匹配才生效）
export PW_ROOT=/data/connectedhomeip/third_party/pigweed/repo
export PW_PROJECT_ROOT=/data/connectedhomeip
export PATH=/data/connectedhomeip/.environment/cipd:/data/connectedhomeip/.environment/cipd/packages/pigweed:$PATH
/usr/bin/python3.11 third_party/pigweed/repo/pw_env_setup/py/pw_env_setup/env_setup.py \
  --shell-file /data/connectedhomeip/.environment/activate.sh \
  --install-dir /data/connectedhomeip/.environment \
  --config-file scripts/setup/environment.json \
  --virtualenv-gn-out-dir /data/connectedhomeip/.environment/gn_out \
  --additional-cipd-file /data/connectedhomeip/.environment/pigweed.json \
  --use-existing-cipd --trust-cipd-hash
```
注意：
- 若日志显示 `equal: False`（hash 不匹配，因调用路径不同 digest 会变），把 `hash.log` 里的 `calculated digest` 写进 `.environment/cipd/packages.sha256` 再跑一次即可。
- 跑完后 `.environment/activate.sh` 会重新生成，以后 `source scripts/activate.sh` 秒过。
- **离线修复后 zap 不在 PATH 里**，编译时必须加：
  ```c
  export ZAP_INSTALL_PATH=/data/connectedhomeip/.environment/cipd/packages/zap
  ```

### 坑 2：GNU binutils 2.46 在 i5-14500 上段错误（最大坑）
系统 `ld`/`ar`（binutils 2.46-3ubuntu2）在链接/打包时长命令行下 100% 段错误（`ld terminated with signal 11`，kernel log 落在 `libbfd-2.46-system.so` 同一偏移）。`dpkg -V` 校验文件无损 —— 这是 Raptor Lake（13/14 代）缩基金问题的典型症状：编译器/链接器随机崩、轻负载正常。
- llvm 工具链不受影响（pigweed cipd 里自带 `ld.lld`/`llvm-ar`）。
- **解决：llvm shim（已做成永久方案）**

```c
mkdir -p /data/lldshim
ln -sf /data/connectedhomeip/.environment/cipd/packages/pigweed/bin/ld.lld   /data/lldshim/ld
ln -sf /data/connectedhomeip/.environment/cipd/packages/pigweed/bin/llvm-ar /data/lldshim/ar
ln -sf /data/connectedhomeip/.environment/cipd/packages/pigweed/bin/llvm-ranlib /data/lldshim/ranlib
ln -sf /data/connectedhomeip/.environment/cipd/packages/pigweed/bin/llvm-nm /data/lldshim/nm
# 永久生效：/usr/local/bin 优先级高于 /usr/bin（含 sudo secure_path），不用每次 export
sudo ln -sf /data/lldshim/ld      /usr/local/bin/ld
sudo ln -sf /data/lldshim/ar      /usr/local/bin/ar
sudo ln -sf /data/lldshim/ranlib  /usr/local/bin/ranlib
sudo ln -sf /data/lldshim/nm      /usr/local/bin/nm
```
> 以后升级 BIOS（含 Intel 微码 0x12B+）修复 CPU 后，删掉这 4 个软链即可还原 GNU binutils。

其他编译纪律：
- **并行度压到 `-j4`**（`ninja -j4`），14 核全开加重崩溃概率。
- 任何编译前 `export PATH=/data/lldshim:$PATH`（有了 /usr/local/bin 软链后可省）。
- cmake 工程注意：cmake 会把 `CMAKE_AR/CMAKE_RANLIB` 的**绝对路径**写进 `CMakeCache.txt` 和 `CMakeFiles/*/CMakeCCompiler.cmake`。如果曾经用 `/tmp/...` 路径 configure 过（重启后 /tmp 被清空），会报 `/tmp/lldshim/ar: not found`，用下面命令整体替换：
  ```c
  cd <build目录>
  grep -rl '/tmp/lldshim' . | while read f; do sed -i 's|/tmp/lldshim|/data/lldshim|g' "$f"; done
  cmake . && ninja -j4
  ```

### 坑 3：缺包（上游 bootstrap 会装、手工装容易漏）
```c
sudo apt install -y ipset libprotobuf-dev protobuf-compiler   # OTBR firewall / DBUS proto 必需
sudo apt install -y libevent-dev                              # 可选：chip-tool 的 ot-commissioner 需要
```

---

## 3 编译 chip-tool + chip-cert（实测命令）

```c
cd /data/connectedhomeip
export PATH=/data/lldshim:$PATH
export ZAP_INSTALL_PATH=/data/connectedhomeip/.environment/cipd/packages/zap
unset JAVA_HOME
source scripts/activate.sh        # 已离线修复过，秒过
```

chip-tool（**不带 ot-commissioner**，避开 libevent 依赖；不影响 BLE/Thread 常规配网）：
```c
gn gen --check --fail-on-unused-args --root=examples/chip-tool out/chip-tool \
    --args=chip_support_thread_meshcop=false
ninja -C out/chip-tool -j4
# 产物: /data/connectedhomeip/out/chip-tool/chip-tool
```
> 如果装了 `libevent-dev` 想要全功能（含 OTBR 代理 commissioner），用官方方式即可：
> `./scripts/build/build_examples.py --target linux-x64-chip-tool build`

chip-cert：
```c
gn gen --check --fail-on-unused-args --root=/data/connectedhomeip out/linux-x64-chip-cert
ninja -C out/linux-x64-chip-cert -j4 src/tools/chip-cert
# 产物: /data/connectedhomeip/out/linux-x64-chip-cert/chip-cert
# 注意：不要加 -mbedtls/-psa 修饰，chip-cert 只支持 openssl/boringssl
```

全局命令行软链（任何目录可直接敲 `chip-tool`）：
```c
sudo ln -sf /data/connectedhomeip/out/chip-tool/chip-tool /usr/local/bin/chip-tool
sudo ln -sf /data/connectedhomeip/out/linux-x64-chip-cert/chip-cert /usr/local/bin/chip-cert
sudo setcap 'cap_net_raw+eip cap_net_admin+eip' /data/connectedhomeip/out/chip-tool/chip-tool  # 免 sudo 用 BLE
sudo usermod -aG dialout eric   # 串口权限，重新登录生效
```

功能自检（不需要任何硬件）：
```c
chip-tool payload parse-setup-payload 34970112332
# 期望: Short discriminator: 15 (0xf), Passcode: 20202021
chip-cert gen-cert -t r -i 0x0001 -o /tmp/root.pem -O /tmp/root.key.pem -F x509-pem --lifetime 3650
chip-cert gen-cert -t n --subject-chip-id 0x1234 --subject-fab-id 0x0001 \
    --ca-cert /tmp/root.pem --ca-key /tmp/root.key.pem \
    --out /tmp/node.pem --out-key /tmp/node.key.pem -F x509-pem --lifetime 3650
chip-cert validate-cert -t /tmp/root.pem /tmp/node.pem     # rc=0 即通过
```

---

## 4 编译 + 安装 OTBR（实测命令）

```c
cd /data
git clone https://github.com/openthread/ot-br-posix
cd ot-br-posix
git submodule update --init --recursive --depth 1   # 必须递归！openthread 里还嵌套 mbedtls

# 预配置构建（agent-only：无 web GUI / REST；RCP 指向 ttyUSB0）
export PATH=/data/lldshim:$PATH
mkdir -p build/otbr && cd build/otbr
cmake -GNinja -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DBUILD_TESTING=OFF \                              # 免装 GTest
  -DCMAKE_AR=/data/lldshim/ar -DCMAKE_RANLIB=/data/lldshim/ranlib -DCMAKE_NM=/data/lldshim/nm \
  -DOTBR_INFRA_IF_NAME=enp0s3 \
  -DOTBR_RADIO_URL='spinel+hdlc+uart:///dev/ttyUSB0' \
  -DOTBR_WEB=OFF ..
ninja -j4
cd /data/ot-br-posix

# 正式安装（内部会再 cmake 一次并 sudo ninja install 到 /usr，同时装 firewall/nat64/ipforward）
WEB_GUI=0 REST_API=0 INFRA_IF_NAME=enp0s3 ./script/setup
```
> `examples/platforms/ubuntu/default` 默认 `WEB_GUI=1 REST_API=1`，不要 web 就用环境变量压掉。
> `script/setup` 依赖 `ipset`（otbr-firewall 脚本用），缺了会在 "Failed to start firewall service!" 处中断。

安装后的配置文件 `/etc/default/otbr-agent`（自动生成，确认内容）：
```text
OTBR_AGENT_OPTS="-I wpan0 -B enp0s3 spinel+hdlc+uart:///dev/ttyUSB0 trel://enp0s3"
OTBR_NO_AUTO_ATTACH=0
```

---

## 5 开机自启（重点：官方 SysV 服务有两个缺陷，必须替换）

官方 `script/setup` 只装了 SysV init 脚本（`/etc/init.d/otbr-agent`），缺陷：
1. RCP 超时（`radio tx timeout`）时 agent 会自杀，但 SysV 方式 systemd **探测不到进程死亡**（status 一直显示 active，实际已死，ot-ctl 报 `Connection refused`）；
2. 不会自动重启。

### 5.1 otbr-agent 原生 systemd 服务（替换 SysV，已实测）
`/etc/systemd/system/otbr-agent.service`（同名覆盖 SysV 生成的 unit）：
```ini
[Unit]
Description=OpenThread Border Router Agent (native, supervised)
Documentation=man:otbr-agent(1)
After=network.target
Wants=dev-ttyUSB0.device
After=dev-ttyUSB0.device
Wants=otbr-firewall.service
After=otbr-firewall.service

[Service]
Type=simple
EnvironmentFile=-/etc/default/otbr-agent
ExecStartPre=-/bin/rm -f /run/openthread-wpan0.sock /run/openthread-wpan0.lock
ExecStart=/usr/sbin/otbr-agent $OTBR_AGENT_OPTS
Restart=always
RestartSec=3
RuntimeMaxSec=infinity

[Install]
WantedBy=multi-user.target
```
安装：
```c
sudo systemctl stop otbr-agent
sudo cp /tmp/otbr-agent.service /etc/systemd/system/    # unit 文件放哪都行，cp 到位即可
sudo systemctl daemon-reload
sudo systemctl enable --now otbr-agent
```
`Restart=always`：RCP 再超时，3 秒后自动重连（会重新 spinel 握手 + 恢复组网，网络凭据存在 `/var/lib/thread`，重启不掉网）。

### 5.2 BLE 热插拔（插上即用、拔插自恢复，2026-09-23 定稿）
设计目标：**J-Link 一插上就自动 attach 成 hci0；有问题拔插一次就恢复**。机制 = udev 规则 + 服务，源文件在部署包 `ble-hotplug/` 里。

`/etc/udev/rules.d/90-jlink-ble.rules`：
```text
# 稳定别名 /dev/jlink-ble（无论内核编号成 ttyACM0/1/2 都指向它）+ 屏蔽 ModemManager 探测占用
SUBSYSTEM=="tty", ATTRS{idVendor}=="1366", ATTRS{idProduct}=="1024", \
    SYMLINK+="jlink-ble", ENV{ID_MM_DEVICE_IGNORE}="1"
# 插上 → 自动拉起 attach 服务 + 重启 bluetooth（开机冷插拔会重放 add 事件，开机自启同样覆盖）
ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="1366", ATTRS{idProduct}=="1024", \
    TAG+="systemd", ENV{SYSTEMD_WANTS}="hciattach-jlink.service", \
    RUN+="/bin/systemctl --no-block try-restart bluetooth.service"
# 拔掉 → 停服务（remove 事件用 udev db 里持久化的 ENV 匹配）
ACTION=="remove", SUBSYSTEM=="tty", ENV{ID_VENDOR_ID}=="1366", ENV{ID_MODEL_ID}=="1024", \
    RUN+="/bin/systemctl --no-block stop hciattach-jlink.service"
```

`/etc/systemd/system/hciattach-jlink.service`：
```ini
[Unit]
Description=Attach J-Link OB BLE controller as hci0 (via /dev/jlink-ble)
Before=bluetooth.service
StopWhenUnneeded=yes
StartLimitIntervalSec=60
StartLimitBurst=6

[Service]
Type=forking
ExecCondition=/bin/test -e /dev/jlink-ble
ExecStartPre=-/usr/bin/fuser -k /dev/jlink-ble
ExecStartPre=-/bin/sleep 0.5
ExecStartPre=-/usr/bin/hciattach /dev/jlink-ble release
ExecStart=/usr/bin/hciattach -s 115200 /dev/jlink-ble any 115200
Restart=on-failure
RestartSec=3
```

安装（同时退役旧的 hciattach-ttyACM0 服务）：
```c
sudo systemctl disable --now hciattach-ttyACM0.service 2>/dev/null
sudo rm -f /etc/systemd/system/hciattach-ttyACM0.service
sudo cp /data/chiptool/ble-hotplug/90-jlink-ble.rules /etc/udev/rules.d/
sudo cp /data/chiptool/ble-hotplug/hciattach-jlink.service /etc/systemd/system/
sudo udevadm control --reload
sudo systemctl daemon-reload
# 设备已插着时,模拟一次 add 事件触发 attach:
sudo udevadm trigger --subsystem-match=tty --attr-match=idVendor=1366 --attr-match=idProduct=1024 --action=add
hciconfig -a      # 应看到 hci0 UP RUNNING
```

设计要点（为什么"插上就用、拔插必恢复"）：
- **稳定别名**：服务全部指向 `/dev/jlink-ble`，内核把它编号成 ttyACM0/1/2 都无所谓；
- **ModemManager 屏蔽**：`ID_MM_DEVICE_IGNORE` 干掉最大的占用干扰源（MM 会探测占用所有 CDC-ACM 口 15~30 秒，这是 attach 时好时坏的最常见根因）；
- **插上**：udev add → 拉起服务 → `fuser -k` 杀残余占用者 → `release` 清行规程残留 → attach → `try-restart bluetooth`；
- **拔掉**：udev remove 规则停服务 + `StopWhenUnneeded`（设备引用消失即停）（不会在设备缺失时反复失败重启）；USB 重新枚举本身就是对 BLE 芯片的硬件复位，所以"有问题拔插一次"几乎总能恢复；
- **开机**：udev 冷插拔会重放 add 事件，插着电开机一样自动 attach；
- **防打环**：`ExecCondition` 设备不存在时跳过（不算失败）；`StartLimitIntervalSec/Burst` 防止坏设备时无限刷重启。
- 注意：该服务**不进 `systemctl enable`**（触发源是 udev），`is-enabled` 显示 disabled 是正常的。
### 5.3 Reset Bluetooth
```c
sudo systemctl restart bluetooth
sudo hciconfig hci0 reset

sudo hciconfig hci0 down
sudo hciconfig hci0 up
```
### 5.4 开机自启核对清单
```c
for s in otbr-agent otbr-firewall otbr-nat44 hciattach-jlink bluetooth; do \
  printf '%-22s %s\n' "$s" "$(systemctl is-enabled $s 2>/dev/null) / $(systemctl is-active $s)"; done
```
开机顺序：内核枚举 USB 串口 → udev 触发 `hciattach-jlink`（hci0）→ `bluetooth` → `otbr-agent`（wpan0，自动回连原网络）→ firewall/nat44。
（`hciattach-jlink` 由 udev 触发，`is-enabled` 显示 disabled 属正常，看 `is-active` 即可。）

---

## 6 BLE 配网通道要点（chip-tool 配网通道）

本机最终方案：**Telink 串口模块（/dev/ttyACM0）+ hciattach + systemd 开机自启**（服务见 5.2），已实测配网成功。

### 6.1 控制器必须是"真 HCI 控制器"固件
本次最大教训：**应用固件 ≠ HCI 控制器固件**。Telink 模块跑 Matter 应用固件时，HCI 基础命令（读 BD addr/版本）能应答，但 **LE 扫描事件一个都不上报**（表现：`bluetoothctl scan on` 正常启动、`Discovering: yes`，扫几分钟 0 个设备；扫描期间 `hciconfig` RX bytes 零增长）。判定方法：

```c
timeout 6 bluetoothctl scan on >/dev/null; RX1=$(hciconfig hci0 | grep -oP 'RX bytes:\K[0-9]+')
sleep 10; RX2=$(hciconfig hci0 | grep -oP 'RX bytes:\K[0-9]+')
timeout 6 bluetoothctl scan off >/dev/null
echo "10s 扫描 RX 增量: $((RX2-RX1))"    # 0 = 射频接收路径死；>几百 = 正常
btmgmt info                              # manufacturer 767 = Telink
```
修复：给模块刷 Telink SDK 的 **`ble_hci`（HCI controller）固件**，或换标准 USB 蓝牙 dongle（内核 btusb 驱动原生支持，免 hciattach，`USE_UART_BLE=0`）。

### 6.2 BLE-only 芯片的"假报错"不用管
Telink 这类 BLE-only 控制器会报 `Can't read local name on hci0: Input/output error` —— 这是 BR/EDR 命令不存在所致，**不影响 BLE 扫描/连接**（`btmgmt info` 的 `supported settings` 含 `le` 即可）。

### 6.3 hciattach 服务化注意点（hciattach-jlink.service，udev 热插拔触发）
- 先 `release` 再 attach（`ExecStartPre=-` 容错），防止重复 attach 卡死；
- 波特率 115200 与固件一致；`Type=forking`（hciattach 完成后自行 fork 后台）；
- 换新 BLE 适配器时只改 udev 规则里的 `idVendor/idProduct`，服务无需动。

### 6.4 权限
```c
sudo setcap 'cap_net_raw+eip cap_net_admin+eip' /usr/local/bin/chip-tool  # 免 sudo 扫描/连接
sudo usermod -aG dialout eric     # 串口类 BLE（重新登录生效）
systemctl is-enabled bluetooth    # bluetoothd 必须自启
bluetoothctl show                 # Powered: yes
```

### 6.5 配网失败先分清"哪一侧"问题
- **外设侧**：Matter 设备只有**未配网/进入配网模式时才广播 BLE**（服务 UUID `0xFFF6`）。已配过网的设备不再广播 → chip-tool 扫描必超时。用手机 nRF Connect 确认外设在广播（设备名如 `MATTER-xxxx`，服务 0xFFF6）。
- **PC 侧**：用 6.1 的 RX 增量法测扫描通路。`BLE initiating scan` 后 20s `Timeout` 有两种情况：**扫到了但没匹配**（外设没广播/广播数据不匹配）或**一个设备都扫不到**（PC 适配器问题，本机当时就是这种）。

---

## 7 故障排查实录（遇到同类问题对号入座）

| 症状 | 原因 | 处理 |
|---|---|---|
| bootstrap 卡 "Setting up CIPD package manager" 20 分钟 | CIPD 服务器被墙 | 用坑 1 的离线修复命令 |
| `ld terminated with signal 11` / `ar` 段错误 / `ninja: build stopped` 随机失败 | binutils 2.46 + i5-14500（Raptor Lake）缩基金 | llvm shim（坑 2）+ `-j4`；彻底解决靠升 BIOS 微码 |
| `No module named 'coloredlogs'` | bootstrap 中断，venv 没装完 | 坑 1 跑完即好 |
| chip-tool 编译报 `zap-cli not found` | 离线修复后 zap 不在 PATH | `export ZAP_INSTALL_PATH=/data/connectedhomeip/.environment/cipd/packages/zap` |
| chip-tool 编译缺 `event2/event.h` | ot-commissioner 需要 libevent | 装 libevent-dev，或 `chip_support_thread_meshcop=false` |
| OTBR cmake 缺 GTest / Protobuf | 可选依赖 | `-DBUILD_TESTING=OFF`；`apt install libprotobuf-dev protobuf-compiler` |
| `Failed to start firewall service!` | 缺 `ipset` | `apt install ipset` |
| `/tmp/lldshim/ar: not found` | /tmp 重启被清，cmake 缓存里是绝对路径 | sed 替换为 /data/lldshim（坑 2） |
| `sudo ot-ctl state` → `Connection refused` | agent 进程死了，socket 残留 | 换 5.1 原生 unit 后自动恢复 |
| journal 出现 `radio tx timeout` + cp210x `failed set request 0x0 status: -32`（EPIPE） | RCP 串口异常导致 CP210x USB 管道 stall，且之后每次 `open uart failed: Input/output error` | 强制 USB 重新枚举（见下）；频繁出现则给 RCP 加流控：把 `/etc/default/otbr-agent` 里 URL 改成 `spinel+hdlc+uart:///dev/ttyUSB0?uart-flow-control=1` 后 `systemctl restart otbr-agent` |

USB 设备假死免插拔复位（利用新的 Restart=always 自动重连）：
```c
DEV=$(for d in /sys/bus/usb/devices/*/idVendor; do [ "$(cat $d 2>/dev/null)" = "10c4" ] && dirname $d; done | head -1)
sudo sh -c "echo 0 > $DEV/authorized; sleep 1; echo 1 > $DEV/authorized"
sleep 4 && sudo ot-ctl state
```

---

## 8 迁移到另一台 Ubuntu PC（离线部署包 /data/chiptool）

已打包好 `/data/chiptool/`（12 个文件），整目录拷到新 PC（x86_64 Ubuntu）后一条命令部署：

```c
sudo ./install.sh
# 硬件不同时的参数：
INFRA_IF=eth0 RCP_DEV=/dev/ttyACM1 sudo -E ./install.sh
USE_UART_BLE=0 sudo -E ./install.sh   # 新 PC 用标准 USB 蓝牙 dongle 时
```

### 8.1 包内容
| 文件 | 安装到 | 作用 |
|---|---|---|
| chip-tool / chip-cert | /usr/local/bin | 工具（install.sh 自动 setcap） |
| otbr-agent / ot-ctl | /usr/sbin | OTBR 主程序 / CLI |
| otbr-firewall / otbr-nat44 | /etc/init.d | 防火墙 / NAT44（infra 接口名自动替换） |
| otbr-agent.service | /etc/systemd/system | 开机自启 + 崩溃 3s 自动重启 |
| hciattach-jlink.service + 90-jlink-ble.rules | /etc/systemd/system + /etc/udev/rules.d | BLE 热插拔（插上自动 attach，拔掉自动停） |
| default-otbr-agent | /etc/default/otbr-agent | RCP/infra 参数模板 |
| install.sh / README.md | — | 一键安装脚本 / 说明 |

### 8.2 install.sh 自动做的事
1. 装运行时依赖：`ipset iptables libdbus-1-3 libreadline8 libncurses6 bluez`（**无需编译器**）
2. 安装 4 个二进制 + setcap + dialout 组
3. 按新 PC 参数生成 `/etc/default/otbr-agent`（OTBR_AGENT_OPTS）
4. 写 sysctl（ipv6 forward、accept_ra）+ rt_tables(88 openthread)，替换 otbr-nat44 里的接口名
5. 安装两个 systemd unit（otbr-agent unit 内 ttyUSB0/enp0s3 自动按参数替换）+ BLE 热插拔 udev 规则与服务，并 enable --now
6. 打印核对清单

### 8.3 必改三处（新 PC 硬件不同时）
1. `INFRA_IF` 基础网口名（默认 enp0s3）
2. `RCP_DEV` RCP 串口（默认 /dev/ttyUSB0）
3. `BLE_DEV` BLE 串口（默认 /dev/ttyACM0）；用 USB dongle 则 `USE_UART_BLE=0`

### 8.4 部署后验证
```c
hciconfig -a                     # hci0 UP RUNNING
sudo ot-ctl state                # disabled/leader（RCP 应答）
chip-tool payload parse-setup-payload 34970112332
systemctl is-enabled otbr-agent                    # enabled = 开机自启 ready
systemctl is-active hciattach-jlink                # active（udev 触发，is-enabled 显示 disabled 属正常）
```

> 注意：chip-tool 是 debug 版（187MB），同架构直拷即可用；正式环境可在新 PC 按第三节重编 release。Thread 网络凭据不随包迁移：新 PC 首次要重新 `ot-ctl dataset init new` 组网，或把旧机 `/var/lib/thread/` 一并拷过去即可自动回连原网络。

---

## 9 OTA 升级服务端（chip-ota-provider-app，实测全流程通过）

### 9.1 编译

```c
cd /data/connectedhomeip
export PATH=/data/lldshim:$PATH
export ZAP_INSTALL_PATH=/data/connectedhomeip/.environment/cipd/packages/zap
unset JAVA_HOME
source scripts/activate.sh

# 与 chip-tool 同样关掉 ot-commissioner（避开 libevent）；chip_detail_logging 保持开
gn gen --check --fail-on-unused-args --root=examples/ota-provider-app/linux out/ota-provider-app \
    --args='chip_support_thread_meshcop=false chip_detail_logging=true'
ninja -C out/ota-provider-app -j4
# 产物: /data/connectedhomeip/out/ota-provider-app/chip-ota-provider-app
```
### 9.2 启动与配网

```c
sudo killall ota-provider-app 2>/dev/null   # 先杀旧实例!否则 5540 端口冲突直接 abort
sudo ./chip-ota-provider-app --KVS /tmp/chip_kvs_provider \
    -f xxx.ota

# provider 也是 Matter 节点,要配进同一 fabric(和目标设备同一个 chip-tool 配):
./chip-tool pairing onnetwork <providerNodeId> 20202021
```

### 9.3 触发 OTA 升级

```c
./chip-tool otasoftwareupdater announce-ota-provider <providerNodeId> 0 0 <设备nodeid> 0
```
设备端流程：QueryImage → provider 按 `.ota` 文件头的 VendorID/ProductID/版本匹配 → AcceptStart → BDX 传输（`[ATM] Block Counter / Data Length` 每 1KB 一块）→ BlockEOF/BlockAckEOF → 设备端收 `ApplyUpdateRequest`（新版本号）→ 设备自行动应用重启。

> `Last Known Good Time: 2023-10-14` 是开发证书 NotBefore 的下限+持久化值，非系统时间错误，不用理会；证书校验用的是真实系统时钟（保持 NTP 即可）。

---
