## Commander CLI
```c
C:\SiliconLabs\SimplicityStudio\v5>commander security unlock --command-key command_key.pem --unlock-param 1111 --device EFR32MG24A410F1536IM40 -s 602712820
Unlocking with unlock payload:
C:/Users/Administrator/AppData/Local/SiliconLabs/commander/SecurityStore/device_0000000000000000d44867fffe8997ee/challenge_e4e3184d31be0e7428a6d0367269b5f7/unlock_payload_0000000000111110.bin
Secure debug successfully unlocked
DONE
```

### Security
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

### Debug lock
```c
commander device lock --device EFR32MG24B020F1536IM40
```

### Flash
```c
//AOK
commander readmem --range 0x817e000:0x8180000 --device EFR32MG24A410F1536IM40 --outfile last_page.s37
commander readmem --range 0x8000000:0x80FC000 --device EFR32MG24A410F1536IM40 --outfile hex.s37
```
```c
//EZ
commander readmem --range 0x817e000:0x8180000 --device EFR32MG24A420F1536IM40 --outfile last_page.s37
commander readmem --range 0x8000000:0x80FC000 --device EFR32MG24A420F1536IM40 --outfile hex.s37
```
```c
commander readmem --range 0x8000000:0x80FC000 --device EFR32MG24B210F1536IM48 --outfile hex.s37 -s 440054379
```
```c
commander flash ez01_matter-signed--v0.0.13-2d274330.s37 --device efr32mg24 --no-reset
```

### NVM3
```c
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000
commander nvm3 parse nvm3.s37
commander nvm3 read -o nvm3.s37 --device efr32mg24 --range 0x8174000:0x817e000
commander nvm3 parse nvm3.s37
```
### Ctune
```c
commander ctune get --device efr32mg24
commander ctune set --value 0x47 --device efr32mg24
```
