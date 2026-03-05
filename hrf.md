# Link
| 1 | 2 | 3 | 4 | 5 | 6 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| [memo](../../l/l/memo.md) |[silabs](./files/silabs/silabs.md)| [w](w.md) |[other](other.md) |[matter](matter.md)|

# project
| 1 | 2 | 3 | 4 | 5 | 6 |
| ---- | ---- | ---- | ---- | ---- | ---- |
|[aok](aok.md)|[ez](ez.md)|[pte9](pte9.md)|[bk](bk.md)|

# Module
## HM-MT2401B
| Pin | Name | Definition | Function |
| ---- | ---- | ---- | ---- |
|PB1|UART0_TX|UART0_TX|Serial Tx|
|PB2|UART0_RX|UART0_RX|Serial Rx|
|PA0|SPI_CS|SPI_CS|SPI Flash|
|PC0|SPI_CLK|SPI_CLK|SPI Flash|
|PC1|SPI_MISO|SPI_MISO|SPI Flash|
|PC2|SPI_MOSI|SPI_MOSI|SPI Flash|
|PA1|SWCLK|SWCLK||
|PA2|SWDIO|SWDIO||
|PA7|UART1_TX|UART1_TX||
|PA8|UART1_RX|UART1_RX||
|RST|Reset|Reset||
|VCC|VCC|VCC||
|GND|GND|GND||
# Info
```c
Shenzhen Hope Microelectronics Co., Ltd.
Add:30th floor of 8th Building, C Zone, Vanke Cloud City, Xili Sub-district, Nanshan, Shenzhen, GD, P.R. China
Email: sales@hoperf.com
Post Code: 518052
Tel: +86-755-82973805 / 4001-189-180
Fax: +86-755-82973550
```
# Working Time
```c
http://ai.hoperf.cn
HP1239
Er..1
```

# Tool
[WCH-BLEAnalyzer](https://www.wch.cn/downloads/WCH_BLEAnalyzer_zip.html)

# Compare Filter
```c
*.cpp;*.c;*.h;-.git\;-.pdm\;-.settings\;-.uceditor\;-.vscode\;-GNU ARM v12.2.1 - Default\
```
# VScode Filter
## Exclude
```c
.json,.cmake*,.ninja,.rsp,.map
```
# git
```c
$ git config --global user.name "suhuide"
$ git config --global user.email suhuide@hoperf.com
```
```c
git config --global alias.diffx 'diff -- ":!.project" ":!.cproject" ":!*.slps" ":!*.pintool" ":!*.html" ":!*.pdm*" ":!*.zap"'
git diff ':!.cproject' ':!*.slps' ':!*.pintool' ':!*.html'
```
```c
git tag
git fetch --tags
git checkout tags/v2.8.0 -f
```
```c
git reset --hard HEAD   # Remove all uncommitted changes
git switch -            # Return to the previous branch
git checkout -          # Return to the previous branch
git branch -r           # Check remote branches
git branch -a           # Check all branches (local + remote)
git remote -v           # Show all remote repositories' names and URLs
```
## git account
```c
suhuide@hoperf.com
Shd**475967
```
# VPN
[Router](http://192.168.100.1/)
```c
admin/admin
Externsoin
  ->ShadowSocks
      ->SS endpoint
          -> On/Off
              -> Apply
```

# Board
```c
WSTK Mainboard (ID: 000440045640)
```
# matter repo
```c
https://hoperf-matter/gitlab/matter
```
```c
git remote add origin https://github.com/user/repo.git
```
# samba
```c
samba: \\hoperf-matter
username: suhuide
password: HA39838M*12
```
## Commander CLI
```c
C:\SiliconLabs\SimplicityStudio\v5>commander security unlock --command-key command_key.pem --unlock-param 1111 --device EFR32MG24A410F1536IM40 -s 602712820
Unlocking with unlock payload:
C:/Users/Administrator/AppData/Local/SiliconLabs/commander/SecurityStore/device_0000000000000000d44867fffe8997ee/challenge_e4e3184d31be0e7428a6d0367269b5f7/unlock_payload_0000000000111110.bin
Secure debug successfully unlocked
DONE
```
```c
commander flash ez01_matter-signed--v0.0.13-2d274330.s37 --device efr32mg24 --no-reset
```
```c
C:\Si\ws\ez01_matter\release-fw\signfw\v0.0.13>commander security status --device efr32mg24
WARNING: DP write failed
DCI communication failed, retrying after reset and 10 ms delay...
Resetting device...
SE Firmware version   : 2.2.5
Serial number         : 0000000000000000d44867fffe8b63ab
Debug lock            : Enabled
Device erase          : Enabled
Secure debug unlock   : Enabled
Tamper status         : OK
Secure boot           : Enabled
Boot status           : 0x20 - OK
Command key installed : True
Sign key installed    : True
DONE
```
```c
//Lunch Console -> Admin
serial vcom config
serial vcom config speed 9600
serial vcom config speed 115200
serial vcom config speed 921600
```



### Debug lock
```c
commander device lock --device EFR32MG24B020F1536IM40
```

### Flash
```c
commander readmem --range 0x817e000:0x8180000 --device EFR32MG24A410F1536IM40 --outfile last_page.s37
```
```c
commander nvm3 read -o aaa_empty.s37 --device efr32mg24 --range 0x8174000:0x817e000
commander nvm3 parse aaa_empty.s37
```

# NFC
NFC AES Flash tool
```c
"\\hoperf-matter\MatterShare\AE Team\Projects\PTE9\Release\01-wireless\pte9_wireless_nfc_key_writer.zip"
```
NFC AES Flash method
```c
python3 nfc_key_writer.py --kvn 17 --key_enc "404142434445464748494A4B4C4D4E4F505152535455565758595A5B5C5D5E5F" --key_mac "404142434445464748494A4B4C4D4E4F505152535455565758595A5B5C5D5E5F" --key_dek "404142434445464748494A4B4C4D4E4F505152535455565758595A5B5C5D5E5F"
```

# MFG
```c
username: suhuide
password: +mTvwceVZk
product code: 9323718166
```
```c
matter_mfg_tool_2.5.9\mfg_tool.exe
//Load config
AOK02-MT2401B-v0.1.7-DC\mfg_config.json
```
## Prepare
```c
//Move your target .s37 file into AOK02-MT2401B-v0.1.7-DC\firmware\
Administrator@eric-pc MINGW64 /c/hrf/mfg/AOK02-MT2401B-v0.1.7-DC/firmware
$ ls -1
aok02_bootloader-v3-signed-fa98105c.s37
aok02_matter_dc-v0.1.7-signed-f5f6cb9e.s37
rail_soc_railtest_mt2401b.s37
s2c4_se_fw_upgrade_app_2v2p5.hex
```
```c
//Config mfg_config.json&debug.json accordingly
            "bootloader": "aok02_bootloader-v3-signed-fa98105c.s37",
            "application": "aok02_matter_dc-v0.1.7-signed-f5f6cb9e.s37",
```
### Tip
matter_mfg_tool_2.5.9\firmware  
mfg_tool will load "gfw_efr32_v2_mg24a.s37" first, make sure use the correct .s37 file,focus on signed/unsigned one.  
Bank Chip you can use unsigned one, after secure boot enable, you have to use signed one.  
For changing it, just rename "gfw_efr32_v2_mg24a-signed.s37" or "gfw_efr32_v2_mg24a-unsigned.s37" to "gfw_efr32_v2_mg24a.s37".  
gfw_efr32_v2_mg24a.s37 for chip that is middle secure-vault type, such as HM-MT2401A,HM-MT2401B  
gfw_efr32_v2_mg24b.s37 for chip that is high secure-vault type   
```c
Administrator@eric-pc MINGW64 /c/hrf/mfg/matter_mfg_tool_2.5.9/firmware
$ ls -1
gfw_efr32_v1.s37
gfw_efr32_v2_mg24a-signed.s37
gfw_efr32_v2_mg24a-unsigned.s37
gfw_efr32_v2_mg24a.s37
gfw_efr32_v2_mg24b.s37
```
## MFG Exe
<div align="center">
  <img src="files/mfg.png" width="1080">
</div>

# Module

<div align="center">
  <img src="files/hm-mt2401-v1.png" width="1080">
</div>