# Ubuntu 上 chip-tool 与 OTBR 完整编译配置指南
## 环境准备与依赖安装
在开始编译前，需要先安装必要的系统依赖和开发工具。
### 1. 更新系统并安装基础依赖
打开终端，执行以下命令来更新包列表并安装编译所需的工具和库：
```c
sudo apt update
sudo apt upgrade -y
# 安装编译工具、库和 Python 环境
sudo apt install -y git gcc g++ ninja-build pkg-config \
    libssl-dev libdbus-1-dev libglib2.0-dev libavahi-client-dev \
    python3 python3-venv python3-dev python3-pip \
    unzip libgirepository1.0-dev libcairo2-dev libreadline-dev \
    libncurses-dev
```
### 2. 安装额外依赖（针对不同需求）
需要安装以下包：
```c
# 如果你的 RCP 设备需要特定的 USB 串口权限（如 nRF52840）
sudo apt install -y udev
# 如果计划使用 ot-br-posix 的 Web GUI（可选）
sudo apt install -y python3-setuptools python3-wheel
```
<details>
<summary><strong>依赖包说明（可选阅读）</strong></summary>
-   **build-essential** / **gcc** / **g++**: C/C++ 编译器。
-   **ninja-build**: 快速构建工具。
-   **pkg-config**: 用于获取库的编译标志。
-   **libssl-dev**: OpenSSL 库（Matter/Thread 安全加密）。
-   **libdbus-1-dev**: D-Bus 通信（OTBR 系统服务集成）。
-   **libavahi-client-dev**: mDNS/Bonjour 支持（设备发现）。
-   **Python 环境**: 用于运行脚本和工具链。
-   **libreadline-dev** / **libncurses-dev**: 命令行界面支持。
</details>

## 编译 chip-tool (Matter 控制器)
`chip-tool` 是 Matter 协议的核心调试和开发工具。
### 1. 获取 Matter SDK 源代码
从官方 GitHub 仓库克隆代码并进入目录：
```c
git clone https://github.com/project-chip/connectedhomeip.git
cd connectedhomeip
```
### 2. 初始化子模块与环境
拉取所有必要的子模块并设置 Python 虚拟环境。此步骤至关重要：
```c
# 拉取并初始化子模块
./scripts/checkout_submodules.py --shallow --recursive
# 激活 Python 虚拟环境并设置编译所需的环境变量
source ./scripts/bootstrap.sh
```
> **注意**：执行 `source ./scripts/bootstrap.sh` 后，**当前终端会话**就拥有了编译所需的所有环境变量。若打开新终端，需要**重新执行**此命令。

### 3. 编译 chip-tool
使用官方提供的 GN 构建脚本进行编译：
```c
# 编译 chip-tool，输出到 out/standalone 目录
./scripts/examples/gn_build_example.sh examples/chip-tool out/standalone
```
编译成功后，可执行文件将位于：
```c
connectedhomeip/out/standalone/chip-tool
```
可以直接运行 `./out/standalone/chip-tool` 来查看帮助和测试。

## 编译并配置 OTBR (Thread 边界路由器)
OTBR 是连接 Thread 网络与 IP 网络的桥梁。
### 1. 获取 OTBR 源代码
克隆 `ot-br-posix` 仓库并进入目录：
```c
# 返回到用户主目录（或你存放项目的目录）
cd ~
git clone https://github.com/openthread/ot-br-posix.git
cd ot-br-posix
```
### 2. 引导脚本（Bootstrap）
运行引导脚本，它会自动安装依赖并设置 Python 环境：
```c
./script/bootstrap
```
### 3. 编译并安装 OTBR
这是最关键的一步。需要通过环境变量指定**基础设施网络接口**（例如Wi-Fi 接口 `wlan0` 或以太网接口 `eth0**）。

```c
# 使用以太网接口 (例如 eth0)
sudo INFRA_IF_NAME=eth0 ./script/setup
# 或者使用 Wi-Fi 接口 (例如 wlan0)
# sudo INFRA_IF_NAME=wlan0 ./script/setup
```

此命令会：
1.  编译 OTBR 及其所有依赖（包括 OpenThread）。
2.  将编译好的文件安装到系统目录（如 `/usr/sbin`, `/etc`）。
3.  设置 `otbr-agent` 服务为开机自启。
编译和安装过程可能需要较长时间，请耐心等待。
### 4. 验证 OTBR 服务状态
安装后，检查 `otbr-agent` 服务是否正在运行：
```c
sudo systemctl status otbr-agent
```
如果服务状态显示 `active (running)`，则说明 OTBR 服务已成功启动。如果显示 `failed` 或 `inactive`，请检查日志：
```c
sudo journalctl -u otbr-agent -n 50
```
## OTBR 详细配置与调试
服务安装后，进行必要的配置才能使其稳定工作。
### 1. 配置 RCP (Radio Co-Processor) 设备
OTBR 通过 RCP 设备进行 Thread 无线通信。需要确认 RCP 设备的串口路径。
1.  **查找 RCP 设备路径**：
    插入RCP USB 设备（如 nRF52840 Dongle），然后执行：
    ```c
    ls /dev/tty* | grep -E "ACM|USB"
    ```
    常见的路径可能是 `/dev/ttyACM0` 或 `/dev/ttyUSB0`。请记住你的设备路径。
2.  **编辑 OTBR 配置文件**：
    ```c
    sudo nano /etc/default/otbr-agent
    ```
    找到以 `OTBR_AGENT_OPTS` 开头的行，确保 `spinel+hdlc+uart://` 后面的路径与你的 RCP 设备一致。例如：
    ```text
    OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyACM0 trel://eth0"
    ```
    **关键参数解释**：
    -   `-I wpan0`: OTBR 创建的 Thread 网络接口名。
    -   `-B eth0`: 你的**基础设施网络接口**（与编译时 `INFRA_IF_NAME` 一致）。
    -   `spinel+hdlc+uart:///dev/ttyACM0`: RCP 设备的通信协议和路径。
    -   `trel://eth0`: 使用基础设施网络进行 Thread 传输。
3.  **重启服务使配置生效**：
    ```c
    sudo systemctl restart otbr-agent
    ```
### 2. 验证 Thread 网络状态
使用 OTBR 的命令行工具 `ot-ctl` 来检查 Thread 网络状态：
```c
sudo ot-ctl state
# 预期输出: "disabled" (表示线程已停止) 或 "detached" (表示未加入网络)
sudo ot-ctl ifconfig up
# 预期输出: "Done"
sudo ot-ctl thread start
# 预期输出: "Done"
sudo ot-ctl state
# 预期输出: "leader" 或 "router" (表示已成功启动并成为线程网络中的设备)
```
