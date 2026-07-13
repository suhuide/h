
# Enable log
```c
cd certification-tool
docker compose logs
```
# Stop thread
```c
docker ps

CONTAINER ID   IMAGE                                                                     COMMAND                  CREATED         STATUS          PORTS                                                                                                                                       NAMES
8388ed9fc3a5   nrfconnect/otbr:9185bda                                                   "/app/etc/docker/doc"   3 minutes ago   Up 3 minutes                                                                                                                                                compassionate_feynman
99ff20f80b90   connectedhomeip/chip-cert-bins:ca9d1118e097fe947b2aec1ba84f265d6cf2447e   "tail -f /dev/null"      3 minutes ago   Up 3 minutes                                                                                                                                                th-sdk
eccd7cb63c4d   ghcr.io/project-chip/csa-certification-tool-frontend:1acbec0              "docker-entrypoint.s"   4 weeks ago     Up 38 minutes   4200/tcp                                                                                                                                    certification-tool-frontend-1
839a93fe029c   ghcr.io/project-chip/csa-certification-tool-backend:e20beac               "bash -c './prestart"   4 weeks ago     Up 38 minutes   0.0.0.0:8888->8888/tcp, [::]:8888->8888/tcp, 0.0.0.0:5000->5000/udp, [::]:5000->5000/udp, 0.0.0.0:50000->50000/tcp, [::]:50000->50000/tcp   certification-tool-backend-1
36d3c10046ff   postgres:12                                                               "docker-entrypoint.s"   4 weeks ago     Up 38 minutes   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp                                                                                                 certification-tool-db-1
e47e367bee1f   traefik:v2.2                                                              "/entrypoint.sh --pr"   4 weeks ago     Up 38 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:8090->8080/tcp, [::]:8090->8080/tcp                                                            certification-tool-proxy-1
```
```c
docker ps
CONTAINER ID   IMAGE                                                          COMMAND                  CREATED       STATUS      PORTS                                                                                                                                       NAMES
eccd7cb63c4d   ghcr.io/project-chip/csa-certification-tool-frontend:1acbec0   "docker-entrypoint.s…"   5 weeks ago   Up 2 days   4200/tcp                                                                                                                                    certification-tool-frontend-1
839a93fe029c   ghcr.io/project-chip/csa-certification-tool-backend:e20beac    "bash -c './prestart…"   5 weeks ago   Up 2 days   0.0.0.0:8888->8888/tcp, [::]:8888->8888/tcp, 0.0.0.0:5000->5000/udp, [::]:5000->5000/udp, 0.0.0.0:50000->50000/tcp, [::]:50000->50000/tcp   certification-tool-backend-1
36d3c10046ff   postgres:12                                                    "docker-entrypoint.s…"   5 weeks ago   Up 2 days   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp                                                                                                 certification-tool-db-1
e47e367bee1f   traefik:v2.2                                                   "/entrypoint.sh --pr…"   5 weeks ago   Up 2 days   0.0.0.0:80->80/tcp, [::]:80->80/tcp, 0.0.0.0:8090->8080/tcp, [::]:8090->8080/tcp                                                            certification-tool-proxy-1

```
```c
sudo docker stop compassionate_feynman
sudo docker stop th-sdk
```
# OTBR config
```c
/home/ubuntu/certification-tool/backend/test_collections/matter/scripts/OTBR/otbr_start.sh

sudo docker run --privileged -d --network host --name otbr-chip -e NAT64=1 -e DNS64=0 -e WEB_GUI=0 -v $AVAHI_PATH:/etc/avahi -v /dev/ttyUSB0:/dev/radio $BR_IMAGE --radio-url spinel+hdlc+uart:///dev/radio?uart-baudrate=460800 -B $BR_INTERFACE || exit 1
```
# OTBR test
```c
cd /home/ubuntu/certification-tool/backend/test_collections/matter/scripts/OTBR/
./otbr_start.sh
./otbr_stop.sh
```
# SemiAutomated
## Node Id
```c
INFO       | 2026-07-01 09:36:31.798870 | Run Test Runner is Ready
INFO       | 2026-07-01 09:36:31.801997 | TH Version: v2.14+fall2025
INFO       | 2026-07-01 09:36:31.805679 | TH SHA: e20beac
INFO       | 2026-07-01 09:36:31.808492 | TH SDK SHA: ca9d111
INFO       | 2026-07-01 09:36:31.840823 | Project config:
{'test_parameters': {'int-arg': 'use_pase_only:0', 'endpoint': '0'}, 'network': {'wifi': {'ssid': 'testharness', 'password': 'wifi-password'}, 'thread': {'rcp_serial_path': '/dev/ttyACM0', 'rcp_baudrate': 115200, 'on_mesh_prefix': 'fdf9:90b5:843a:b42f::/64', 'network_interface': 'eth0', 'dataset': {'channel': '24', 'panid': '0xea90', 'extpanid': '7af209f53e7a696b', 'networkkey': '385da7215bb901ac6da3788cedfb245a', 'networkname': 'OpenThread-ea90'}, 'otbr_docker_image': None}}, 'dut_config': {'discriminator': '200', 'setup_code': '74652754', 'pairing_mode': 'ble-thread', 'chip_timeout': None, 'chip_use_paa_certs': True, 'trace_log': True, 'enhanced_setup_flow': None}}
INFO       | 2026-07-01 09:36:31.847131 | Project PICS:
//...
INFO       | 2026-07-01 09:36:31.855501 | Test Run Executing
//...
INFO       | 2026-07-01 09:36:34.292610 | Setting up test runner
INFO       | 2026-07-01 09:36:34.314107 | Starting chip server
INFO       | 2026-07-01 09:36:34.317496 | New Node Id generated: 0x8a7d35a148366270
```
## Test Command
```c
docker exec -it th-sdk ./chip-tool descriptor read parts-list 0x8a7d35a148366270 0
```
```c
docker exec -it th-sdk ./chip-tool basicinformation read-event start-up 0x8a7d35a148366270 0
docker exec -it th-sdk ./chip-tool basicinformation read software-version 0x8a7d35a148366270 0
docker exec -it th-sdk ./chip-tool basicinformation read-event shut-down 0x8a7d35a148366270 0
```
```c
docker exec -it th-sdk ./chip-tool onoff on 0xd52dafde42e7bc8a 6
docker exec -it th-sdk ./chip-tool onoff write start-up-on-off 0 0xd52dafde42e7bc8a 6
docker exec -it th-sdk ./chip-tool onoff read on-off 0xd52dafde42e7bc8a 6
```

```c
./chip-tool scenesmanagement add-scene 
  <GroupID>           # 第1参数: GroupID (0x0101)
  <SceneID>           # 第2参数: SceneID (0x03)
  <TransitionTime>    # 第3参数: TransitionTime (1000)
  <SceneName>         # 第4参数: 场景名称 ("scene name")
  <ExtensionFields>   # 第5参数: 扩展字段 (JSON格式)
  <Destination>       # 第6参数: 目标地址 (单播节点ID 或 组播Group)
  <Endpoint>          # 第7参数: 端点号 (1)
```  
```c
docker exec -it th-sdk /bin/bash
```
```c
./chip-tool scenesmanagement add-scene 0x0101 0x01 1000 'scene name' '[{"clusterID": "0x0008", "attributeValueList":[{"attributeID": "0x0000", "valueUnsigned8": "0x64"}]}]' 0xe5325bdce8944315 3

./chip-tool scenesmanagement add-scene 0x0101 0x01 1000 "scene name" '[{"clusterID": "0x0008", "attributeValueList":[{"attributeID": "0x0000", "valueUnsigned8": "0x64"}]}]' 0xe5325bdce8944315 3
./chip-tool scenesmanagement view-scene 0x0101 0x01 0xe5325bdce8944315 3 
./chip-tool levelcontrol move-to-level-with-on-off 200 0 0 0 0xe5325bdce8944315 3
./chip-tool levelcontrol read current-level 0xe5325bdce8944315 3

./chip-tool scenesmanagement add-scene 0x0101 0x03 1000 'scene name' '[{"clusterID": "0x0300", "attributeValueList":[{"attributeID": "0x0000", "valueUnsigned8": "0x64"}]}]' 0xffffffffffff0101 3

./chip-tool scenesmanagement add-scene 0x0101 0x03 1000 "scene name" '[{"clusterID": "0x0300", "attributeValueList":[{"attributeID": "0x0000", "valueUnsigned8": "0x64"}]}]' 0xffffffffffff0101 3

./chip-tool scenesmanagement add-scene 0x0101 0x03 1000 "scene name" '[{"clusterID": "0x0300", "attributeValueList":[{"attributeID": "0x4002", "valueUnsigned8": "0x01"}]}]' 0xffffffffffff0101 3
./chip-tool scenesmanagement view-scene 0x0101 0x03 0xe5325bdce8944315 3

./chip-tool scenesmanagement remove-scene 0x0101 0x01 0xe5325bdce8944315 3
```

A. setup group（每条单独跑就行，unicast 不涉及 group counter）

# 0a: 写 group key set (keyset 0x01a1=417, TrustFirst)
```c
sudo ./chip-tool groupkeymanagement key-set-write \
  '{"groupKeySetID":417,"groupKeySecurityPolicy":0,
    "epochKey0":"a0a1a2a3a4a5a6a7a8a9aaabacadaeaf","epochStartTime0":1110000,
    "epochKey1":"b0b1b2b3b4b5b6b7b8b9babbbcbdbebf","epochStartTime1":1110001,
    "epochKey2":"c0c1c2c3c4c5c6c7c8c9cacbcccdcecf","epochStartTime2":1110002}' \
  2250 0
```
# 0c: 把 group 0x0101=257 绑到 keyset 417
```c
sudo ./chip-tool groupkeymanagement write group-key-map \
  '[{"fabricIndex":1,"groupId":257,"groupKeySetID":417}]' 2250 0
```
# 1a: AddGroup —— 把 group 257 映射到 endpoint 3（这样 HasEndpoint(1,257,3)=true）
```c
sudo ./chip-tool groups add-group 257 "Group1" 2250 3
```
跑完 A，先验证 unicast AddScene 能过（应返回 status 0）：

```c
sudo ./chip-tool scenesmanagement add-scene 0x0101 0x01 1000 "scene name" \
  '[{"clusterID":"0x0008","attributeValueList":[{"attributeID":"0x0000","valueUnsigned8":"0x64"}]}]' \
  2250 3
```
如果还回 133，说明 AddGroup 没把 257 映射到 ep3（可能 ep3 的 Groups cluster 不在 3），告诉我返回值。

B. groupcast 测试 —— 必须一个进程（interactive 模式，counter 单调）
```c
sudo ./chip-tool interactive start
```
进去后在同一个 interactive 会话里依次跑（去掉 ./chip-tool 前缀，直接输子命令）：
```c
scenesmanagement add-scene 0x0101 0x03 1000 'scene name' '[{"clusterID":"0x0008","attributeValueList":[{"attributeID":"0x0000","valueUnsigned8":"0x64"}]}]' 0xffffffffffff0101 3

scenesmanagement view-scene 0x0101 0x03 2250 3

scenesmanagement remove-scene 0x0101 0x03 0xffffffffffff0101 3

scenesmanagement view-scene 0x0101 0x03 2250 3
```
groupcast 目的地用 0xffffffffffff0101（= group 0x0101）；unicast 用 2250。
EFS 我用 LevelControl(0x0008)，跟认证 YAML 一致，ep3 肯定支持。想测 ColorControl 就把 clusterID 换 0x0300、attributeID 换 0x0000（CurrentHue，别用 0x4002）。