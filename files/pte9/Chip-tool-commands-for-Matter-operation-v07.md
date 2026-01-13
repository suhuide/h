# **Chip-tool commands for Matter operation**

note:

## Version v0.7

## 1. Shows commands for a specific cluster/attributes

### Command:
```c
./chip-tool-sprint9-1 <cluster>
```
### Example:
```c
./chip-tool-sprint9-1 onoff
```
## Shows readable for a cluster

### Command:
```c
./chip-tool-sprint9-1 <cluster> read
```
### Example:
```c
./chip-tool-sprint9-1 onoff read
```
## 3. Starts interactive mode (avoids session timeouts)

### Command:
```c
./chip-tool-sprint9-1 interactive start
```
## 4. Clear the previous distribution network information

### Example:
```c
sudo rm -r /tmp/chip(\_\*)
```
## 5. Cheack thread dataset(The OTBR tool needs to be installed)

### Command:
```c
sudo ot-ctl dataset active -x
```
## 6. Commissioning

## Parses a QR code payload to extract commissioning info

### Command:
```c
./chip-tool-sprint9-1 onoff read on-off <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 payload parse-setup-payload MT:Y.K9042C00KA0648G00
```
## Commissions a Thread device via BLE

### Command:
```c
./chip-tool-sprint9-1 pairing ble-thread <node_id> hex:<dataset> <pin> <discriminator>
```
### Example:
```c
./chip-tool-sprint9-1 pairing ble-thread 2252 hex:0e08... 20202021 3840
```
## Commissions a Wi-Fi device via BLE

### Command:
```c
./chip-tool-sprint9-1 pairing ble-wifi <node_id> <ssid> <password> <pin> <discriminator>
```
### Example:
```c
./chip-tool-sprint9-1 pairing ble-wifi 2252 hoperf pass1234 20202021 3840
```
## Commissions a device already on the IP network using its PIN

### Command:
```c
./chip-tool-sprint9-1 pairing onnetwork <node_id> <pin>
```
### Example:
```c
./chip-tool-sprint9-1 pairing onnetwork 2252 20202021
```
## Commissioning for Thread devices

### Command:
```c
./chip-tool-sprint9-1 pairing nfc-thread <node_id> <Dataset> <setup-pin-code> <discriminator>
```
### Example:
```c
./chip-tool-sprint9-1 pairing nfc-thread 2252 0e08... 20202021 3840
```
## Commissions a device using its QR code or manual pairing code

### Command:
```c
./chip-tool-sprint9-1 pairing code <node_id> <qrcode_content>
```
### Example:
```c
./chip-tool-sprint9-1 pairing code 2252 MT:4S5U4PSB00SC5K73310
```
## The method of connecting multiple fabrics to the network using the chip-tool command

### Command:
```c
./chip-tool-sprint9-1 pairing code <node_id> <Pairing code> commissioner-name
```
### Example:
```c
./chip-tool-sprint pairing code 2252 3347-125-4824 --commissioner-name "alpha" //The default setting is this <br>
./chip-tool-sprint9-1 pairing code 2233 2631-665-6369 --commissioner-name "beta" <br>
./chip-tool-sprint9-1 pairing code 2233 3393-744-8360 --commissioner-name "gamma" <br>
./chip-tool-sprint9-1 pairing code 2233 3393-744-8360 --commissioner-name "4"
```
## Removes a commissioned device from the controller's fabric

### Command:
```c
./chip-tool-sprint9-1 pairing unpair <node_id>
```
### Example:
```c
./chip-tool-sprint9-1 pairing unpair 2252
```
## 7. Reads the vendor name from the device

### Command:
```c
./chip-tool-sprint9-1 basicinformation read vendor-name <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 basicinformation read vendor-name 2252 0
```
## 8. The accuracy of reading energy/power data

### Command:
```c
./chip-tool-sprint9-1 electrical energy measurement read accuracy <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 electricalenergymeasurement read accuracy 2252 1
```
## Read the voltage data

### Command:
```c
./chip-tool-sprint9-1 electricalpowermeasurement read rmsvoltage <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 electricalpowermeasurement read rmsvoltage 2252 1
```
## Read the current data

### Command:
```c
./chip-tool-sprint9-1 electricalpowermeasurement read rmscurrent <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 electricalpowermeasurement read rmscurrent 2252 1
```
## reading power data

### Command:
```c
./chip-tool-sprint9-1 electrical power measurement read accuracy <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 electricalpowermeasurement read accuracy 2252 1
```
## 9. Subscribes to real-time events from a device

### Command:
```c
./chip-tool-sprint9-1 subscribe-event <event> <min> <max> <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 switch subscribe-event initial-press 5 10 2252 1
```
## 10. This is used to configure the specific channel parameters of an electricity meter device that supports the Matter protocol.

### Command:
```c
./chip-tool-sprint9-1 meterconfiguration set-channel <channel_id>
```
### Example:
```c
./chip-tool-sprint9-1 interactive start<br>
meterconfiguration read number-of-channels 2252 10 <br>
meterconfiguration set-channel 0 '{"CTRating":50000,"CTDirection":1,"CTType":0,"phaseID":1}' 2252 10 <br>
meterconfiguration read channels 2252 10
```
## 11. Subscribe measurement-period-ranges event:

### Command:
```c
./chip-tool-sprint9-1 electricalpowermeasurement <commands> <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 electricalpowermeasurement subscribe-event measurement-period-ranges 5 30 2252 1 <br>
./chip-tool-sprint9-1 electricalpowermeasurement read ranges 2252 1 <br>
./chip-tool-sprint9-1 electricalpowermeasurement read-event measurement-period-ranges 2252 1
```
## 12. Write/Read userlabell

### Command:
```c
./chip-tool-sprint9-1 userlabel write label-list <node_id> <channel_id>
```
### Example:
```c
./chip-tool-sprint9-1 userlabel write label-list '[{"label":"01","value":"1111"},{"label":"02","value":"2222"},{"label":"03","value":"3333"},{"label":"04","value":"4444"}]' 2252 1
```
### Command:
```c
./chip-tool-sprint9-1 userlabel read label-list <node_id> <channel_id>
```
### Example:
```c
./chip-tool-sprint9-1 userlabel read label-list 2252 1
```
## 13. Configure permissions and synchronize the current time comman

### Example:
```c
sudo chown 777 chip-tool<br>
sudo date -s "2025-01-08 10:00:00"
```
## 14. Set/Read UTC time

### Command:
```c
./chip-tool-sprint9-1 timesynchronization set-utctime <date> 2 <node_id> 0
```
### Example:
```c
./chip-tool-sprint9-1 timesynchronization set-utctime 1757039010000000 2 2252 0
```
## Read UTC time

### Command:
```c
./chip-tool-sprint9-1 timesynchronization read utctime <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 timesynchronization read utctime 2252 0
```
## 15. Read the private cluster command

### Command:
```c
./chip-tool-sprint9-1 read <cluster>
```
### Example:
```c
**read of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read number-of-channels 2252 10
**read channels-config of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read channels 2252 10
**read ct presence status of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read ctpresence 2252 10
**read number-of-circuit of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read number-of-circuit 2252 10
**read phase-loss status of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read phase-loss 2252 10
**read circuits config of the private cluster**
./chip-tool-sprint9-1 meterconfiguration read circuits 2252 10
```
## 16. Verify the reporting of Alarm messages

### Command:
```c
./chip-tool-sprint9-1 meterconfiguration subscribe-event <event> <min> <max> <node_id> <endpoint_id>
```
### Example:
```c
**Verify the reporting of Phase loss Alarm messages**
./chip-tool-sprint9-1 interactive start <br>
meterconfiguration subscribe-event phase-loss-changed 0 10 2252 10
**Verify the reporting of the CtpresenceAlarm message**
./chip-tool-sprint9-1 interactive start <br>
meterconfiguration subscribe-event ctpresence-changed 0 10 2252 10
```
## 17. Read log information

### Command:
```c
./chip-tool-sprint9-1 diagnosticlogs retrieve-logs-request <event> <min> <max> <node_id> <endpoint_id>
```
### Example:
```c
**Use the following command to read the normal logs through ResponsePayload<br>**
./chip-tool-sprint9-1 interactive start <br>
diagnosticlogs retrieve-logs-request 0 0 2252 0 <br>
diagnosticlogs retrieve-logs-request 0 1 2252 0 --TransferFileDesignator user-diag.log
**Use the following command to read the crash log through ResponsePayload**
./chip-tool-sprint9-1 interactive start <br>
diagnosticlogs retrieve-logs-request 2 0 2252 0 <br>
diagnosticlogs retrieve-logs-request 2 1 2252 0 --TransferFileDesignator crash-diag.log
```
## 18. Versioning rules implement

### Command:
```
./chip-tool-sprint9-1 basicinformation read <attribute> <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 basicinformation read software-version-string 2252 0
./chip-tool-sprint9-1 basicinformation read software-version 2252 0
./chip-tool-sprint9-1 basicinformation read hardware-version-string 2252 0
./chip-tool-sprint9-1 basicinformation read hardware-version 2252 0
./chip-tool-sprint9-1 basicinformation read manufacturing-date 2252 0
./chip-tool-sprint9-1 basicinformation read serial-number 2252 0
./chip-tool basicinformation read-by-id 0xffffffff 2252 0
```
## 19. Select a test channel on the device

### Command:
```c
./chip-tool-sprint9-1 meterconfiguration select-test-channel <node_id> <endpoint_id>
```
### Example:
```c
./chip-tool-sprint9-1 meterconfiguration select-test-channel 1 2252 10
```
## 36. CT short circuit status report command

### Command:
```c
./chip-tool-sprint9-1 interactive start
meterconfiguration subscribe-event ctis-shorted
```
### Example:
```c
./chip-tool-sprint9-1 interactive start
meterconfiguration subscribe-event ctis-shorted 0 10 2252 10
```