
# 1 OTA Upgrade Operation
## 1.1 OTA Requestor Join network
Kill OTA thread.
```c
ps -ef | grep "ota"
killall -9 sudo chip-ota-provider-app
```
Commission, keep Terminal A open
```c
sudo rm -rf /tmp/chip_*
sudo ./chip-tool pairing ble-thread 2250 hex:0e080000000000010000000300001835060004001fffe002084c579a3a07ca63460708fdf932b502298114051045595f06b2527f449aea00b5e951f986030f4f70656e5468726561642d636464320102cdd20410b0e3317425a943ad8267f8b9abbde4d20c0402a0f7f8 85956333 1884 --paa-trust-store-path ~/paa-root-certs
```
## 1.2 OTA Provider Load File
Open a new Terminal B. Use chip-ota-provider-app to load the target xxx.ota file.
```c
sudo ./chip-ota-provider-app --KVS /tmp/chip_kvs_provider -f xxx.ota
```
## 1.3 OTA Provider Join Network
```c
sudo ./chip-tool pairing onnetwork 1 20202021 
sudo ./chip-tool accesscontrol write acl '[{"fabricIndex": 1, "privilege": 5, "authMode": 2, "subjects": [112233], "targets": null}, {"fabricIndex": 1, "privilege": 3, "authMode": 2, "subjects": null, "targets": null}]' 1 0 
```
## 1.4 OTA Requestor Trigger
```c
sudo ./chip-tool otasoftwareupdaterequestor announce-otaprovider 1 0 0 0 2250 0 
```
## 1.5 OTA Requestor Version Check
```c
sudo ./chip-tool basicinformation read software-version-string 2250 0
```

# 2 Flowchart on Spec
<div align="center">
  <img src="ota-workflow.png" width="1080">
</div>  

# 3 [ota-flow](ota-flow.md)
## [log-chip-tool](log-chip-tool.md)
## [log-ota-provider](log-ota-provider.md)
## [log-ota-requestor](log-ota-requestor.md)

# 4 [ota-issue](ota-issue.md)