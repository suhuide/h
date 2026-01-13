# **chip-tool 命令**

## 1. 查看 thread date set hex:

sudo ot-ctl dataset active -x

## 2. 解析二维码信息命令

./chip-tool payload parse-setup-payload MT:4S5U4X2K01HF.12JO00

sudo ./chip-tool pairing open-commissioning-window 2252 1 400 2000 3001 //打开配网窗口


## 3. 清除配网信息命令

sudo rm -rf /tmp/chip\_\*
sudo rm -rf /tmp/chip_tool_kvs

## 4. chip-tool 配网命令

./chip-tool pairing code 2253 25582323305 --commissioner-name beta

Ethernet 配网命令：
sudo ./chip-tool pairing onnetwork 1 20202021
./chip-tool basicinformation read-by-id 0xffffffff 2252 0 | grep TOO //验证配网成功命令

Thread 配网命令示例：
sudo ./chip-tool pairing ble-thread 2252 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 30515365 3001 --paa-trust-store-path ~/paa-test/

sudo pcsc_scan

NFC 配网命令
sudo ./chip-tool pairing nfc-thread 2252 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 20202021 3840

~/paa-root-certs
~/paa-test/

## 5. 离网命令

sudo ./chip-tool pairing unpair 2252

## 6. 在 commander tool 校准命令

commander ctune set --value 0x47 --device efr32mg24

## 7. docker 命令

cd certification-tool/backend/docker //进入 docker 目录
./scripts/build.sh //编译
./scripts/stop.sh //停止
./scripts/start.sh //开始
sudo docker compose logs -f //所有容器的日志输出
sudo docker compose down //停止并删除所有容器
ssh-keygen //主要用于生成和管理用于 SSH 加密和认证的密钥

## 8. 配置权限和同步当前时间命令

chown 777 chip-tool
sudo date -s "2026-01-04"

sudo ./chip-tool timesynchronization read utctime 2252 0

./chip-tool timesynchronization set-utctime 1757050000000000 2 0 2252 0

## 9. git 命令

git branch -v //
git branch -a //显示本地所有分支
git clone //克隆远程版本库
git init //初始化本地版本库
git status //查看状态
git add xyz //添加 xyz 文件到 index
git log 显示提交日志
git show dfb02 //显示摸铺个提交的详细内容
git tag //显示已存在的 tag
git fetch origin //拉取远程版本库
git fetch //
git submodule init //初始化子模块
git submodule update //更新子模块
git checkout v2.14-beta3+fall2025-develop //切换分支

## 10. 解压命令··

tar xvf simplicity_sdk_v2024.12.2.tar
./chip-tool diagnosticlogs retrieve-logs-request

## 11. Channel 电能计量读取命令

./chip-tool electricalenergymeasurement read accuracy <nodie> 1

Electrical Power Measurement 电能计量读取命令

sudo ./chip-tool electricalpowermeasurement read rmscurrent 2255 1

./chip-tool electricalpowermeasurement read rmsvoltage <nodie> <endpointid>

sudo ./chip-tool electricalpowermeasurement read rmsvoltage 2252 3 | grep TOO

./chip-tool meterconfiguration set-channel 0 '{"CTRating":50000,"CTDirection":1,"CTType":0,"phaseID":1}' 102 19

## 12. 编译命令

[--verify <public key file>] --outfile <signed GBL file>
例如：  
 commander gbl sign example.gbl.extsign --signature example.gbl.extsign.sig --verify ecdsakey.pub--outfile example-signed.gbl

1.  commander convert pte9_wireless_bootloader-v3-unsigned-671d57b5.s37 --secureboot --signature pte9_wireless_bootloader-v3-unsigned-671d57b5.sig --verify PTE9_Wireless_Public_key.pem --outfile pte9_wireless_bootloader-v3-signed-671d57b5.s37 //签名合并

2.  commander convert pte9_wireless_matter-v02.00.00-non-d3e187ad.s37 --secureboot --signature pte9_wireless_matter-v02.00.00-non-d3e187ad.s37.sig --verify PTE9_Wireless_Public_key.pem --outfile pte9_wireless_matter-v02.00.00-signed-d3e187ad.s37

## 13. 日志命令

### 请求诊断日志

diagnosticlogs retrieve-logs-request 0 0 2252 0

### 请求并写入用户诊断日志

diagnosticlogs retrieve-logs-request 0 1 2252 0 --Transfer File Designator user-diag.log //

### 请求并写入崩溃诊断日志

diagnosticlogs retrieve-logs-request 2 1 2252 0 --Transfer File Designator crash-diag.log //

## 14.杂项命令

sudo pcsc_scan //NFC 读取

serial vcom config speed 921600 //串口波特率配置

serial vcom config handshake rtscts //串口流速配置

commander ctune set --value 102 --device efr32mg24 //频偏值校准

docker exec -it th-sdk /脚本测试前缀

sudo scp -r /home/ubuntu/paa-test ubuntu@192.168.100.3:/home/ubuntu/ //传输文件命令

sudo ./chip-tool-sprint9 identify identify 5 2252 10 //identify 验证

sudo chmod 777 //给文件赋予权限

./chip-all-clusters-app --trace_decode 1 //日志解码

ls /dev/ttyACM\* //查看 RCP 串口

generalcommissioning arm-fail-safe 900 1 2 0 --commissioner-name beta

sudo ./chip-tool meterconfiguration read ctshorted 2252 10

./chip-tool log read 20 //查看日志

tar -czvf paa-test.tar.gz paa-test/

tar -cavf paa-test.tar.gz './paa-test/'

tar -xzvf paa-test.tar.gz

sudo ./chip-tool-6 timesynchronization set-utctime 810813600000000 2 2252 0 //设置时间

onoff subscribe on-off 10 100 1 1 --keepSubscriptions true //

sudo ./chip-tool networkcommissioning read networks 2252 0

sudo ./chip-tool-sprint9-1 meterconfiguration read ctshorted 2252 10

sudo ./chip-tool-sprint9-1 descriptor read parts-list 2252 0

sudo ./chip-tool-sprint9-1 descriptor read server-list 2252 0 //查看 parts-list

sudo ./chip-tool userlabel read label-list 2252 11 //

sudo ./chip-tool-sprint9-1 meterconfiguration set-channel 8 '{"CTRating":75000,"CTDirection":0,"CTType":0,"phaseID":1}' 2252 10 // 设置 CT 阈值

sudo ./chip-tool-sprint9-1 meterconfiguration read channels 2252 10

sudo pkill -9 -f chip-all //杀死应用

ps aux | grep chip-all-clusters-app //检查应用是否仍在进程中运行

lsb_release -a //查看 ubuntu 版本信息

ps -ef | grep "ota" //查看进程

killall -9 chip-ota-provider-app //杀死 ota 进程

## . 15 电表配置命令

sudo ./chip-tool-6 meterconfiguration add-circuit '{"index":0, "loadType":1, "channels":3, "equipmentType":4, "output":2}' 2252 10 //添加电表配置
sudo ./chip-tool-6 meterconfiguration read number-of-channels 2252 10 //
sudo ./chip-tool-6 meterconfiguration set-channel 0 '{"CTRating":50000,"CTDirection":1,"CTType":0,"phaseID":1}' 2252 10

## 16. 写入自定义 name

sudo ./chip-tool-6 userlabel write label-list '[{"label":"01","value":"1111"},{"label":"02","value":"2222"},{"label":"03","value":"3333"},{"label":"04","value":"4444"}]' 2252 1
sudo ./chip-tool-6 userlabel read label-list 2252 1

## 17. OTA command

sudo ./chip-ota-provider-app --KVS /tmp/chip_kvs-rr -f /tmp/ez01_matter_0x1470_0xFF01-v0.0.11-signed-a1d9c26d.ota --discriminator 81 --passcode 25771968

sudo ./chip-ota-provider-app --KVS /tmp/chip_kvs_provider -f /tmp/ez01_matter_0x1470_0xFF01-v0.0.11-signed-a1d9c26d.ota

./chip-tool otasoftwareupdaterequestor announce-otaprovider 222 0 0 0 2252 0

ps -ef | grep "ota" //查看进程

killall -9 chip-ota-provider-app

./chip-all-clusters-app --trace_decode 1 //日志解码

./chip-tool otasoftwareupdaterequestor announce-otaprovider 1 0 0 0 2252 0 //发布 OTA 信息

## 18. 挂载命令

ls /dev/sd* //查看所有 sd 卡
df // 查看磁盘使用情况
mkdir tenp //创建挂载目录
sudo mount /dev/sda1 tenp //挂载 sd 卡
sudo umount tenp //卸载 sd 卡
cd tenp //进入挂载目录
ls //查看挂载目录下文件
cd home //进入 home 目录
cd ubuntutest //进入 ubuntutest 目录
cd certification/ //进入 certification 目录
cd backend //
cd matter //
find ./ -type f -name "*.py" //查找 py 文件
tar -jcvf matter-scirpt.tar.bz2 matter-script //压缩 matter-script 目录
twb

## 19. 查看 bash_history 命令

vim <脚本名> //查看脚本内容
grep "chip-tool" ~/.bash_history

## 20. 树莓派内 cp 命令

cp ~/Test_TC_DD_3_23.yaml ./backend/test_collections/matter/sdk_tests/sdk_checkout/yaml_tests/yaml/sdk/.
sudo cp ~/Test_TC_DD_3_23.yaml ./backend/test_collections/matter/sdk_tests/sdk_checkout/yaml_tests/yaml/sdk/.

## 21. 订阅电表短路事件命令

./9se-chip-tool interactive start
meterconfiguration subscribe-event ctis-shorted 0 10 2252 10 // 订阅电表短路事件

## 22. 在树莓派上订阅 CT Short 告警，执行如下命令:

./9se-chip-tool interactive start
meterconfiguration subscribe-event ctis-shorted 0 10 2252 10

## 23. test mode

./9se-chip-tool meterconfiguration select-test-channel 1 2252 10

## 24 .OT 指令

sudo ot-ctl factoryreset

sudo ot-ctl dataset init new

sudo ot-ctl dataset commit active

sudo ot-ctl prefix add fd11:22::/64 pasor

sudo ot-ctl ifconfig up

sudo ot-ctl thread start

sudo ot-ctl dataset active -x

## 25. TH 更新命令

1. 确保获取最新远程信息
   git fetch --all

2. 查看所有可用分支
   git branch -a

3. 切换到目标分支
   git checkout v2.15-beta1+winter2025

4. 拉取该分支的最新更新
   git pull origin v2.15-beta1+winter2025

5. 更新
   ./scripts/ubuntu/auto-update.sh v2.15-beta1+winter2025
