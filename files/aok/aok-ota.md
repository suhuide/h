[hrf](hrf.md)  
[aok](aok.md)  


## 3. 设备入网树莓派 chip-tool，假设设备的入网节点是: 2233

## 4. 新起一个 独立的SSH窗口(不能关闭，也不要这个独立窗口执行其他命令), 使用chip-ota-provider-app工具加载打包固件
```c
./chip-ota-provider-app -f aa_pte9_wireless_matter-v06.00.00-mcu-non_0x105E_0x49B3-a2ae555c.ota      
```

## 5.入网和配置chip-ota-provider-app （下面命令中 1 是ota-provider的节点 ）
```c
./ase-chip-tool pairing onnetwork 1 20202021 
./ase-chip-tool accesscontrol write acl '[{"fabricIndex": 1, "privilege": 5, "authMode": 2, "subjects": [112233], "targets": null}, {"fabricIndex": 1, "privilege": 3, "authMode": 2, "subjects": null, "targets": null}]' 1 0 

./ase-chip-tool basicinformation read serial-number 2233 0 
```

## 6. 触发OTA升级; 启动升级后，设备白灯闪烁，升级的时间大约要6到8分钟
```c
./ase-chip-tool otasoftwareupdaterequestor announce-otaprovider 1 0 0 0 2233 0 
```

## 7. 升级成功后，设备重启，通过查看启动日志确认升级是否成功。
```c
matter固件版本号：AppVer: 06.00.00(0x00060000) BtlVer:
meter固件版本号： Meter Report Software Version=0x00060000-->(00 00 06 00).
```
```c
./ase-chip-tool pairing code 2233 3450-414-6659
```
```c
--paa-trust-store-path ~/hoperf-paa/
```