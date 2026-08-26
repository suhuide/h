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
commander nvm3 parse nvm3.s37 --key 0x0f00f
```
### Ctune
```c
commander ctune get --device efr32mg24
commander ctune set --value 0x47 --device efr32mg24
```

# SecureBoot功能说明

# 1. 生成key

```shell
# 生成 Sign Key
commander util genkey --type ecc-p256 --privkey sign_key.pem --pubkey sign_pubkey.pem --tokenfile sign_pubkey.txt
# 生成 GBL AES key
commander util genkey --type aes-ccm --outfile aes_key.txt
# 生成 Command Key
commander util genkey --type ecc-p256 --privkey command_key.pem --pubkey command_pubkey.pem
```

## 2. 将pubkey/aeskey临时写入芯片 （LockBit）

```shell
commander flash --tokengroup znet --tokenfile sign_pubkey.txt --device efr32mg24
commander flash --tokengroup znet --tokenfile aes_key.txt --device efr32mg24
```

## 3. 将pubkey/aeskey永久写入到OTP中 (每个芯片只可写入1次)

```shell
# 写入
commander security writekey --sign sign_pubkey.pem --device EFR32MG24A410F1536IM40
commander security writekey --decrypt aes_key.txt --device EFR32MG24A410F1536IM40
commander security writekey --command command_key.pem --device EFR32MG24A410F1536IM40
# 写入SE配置
TODO.
# 使能SE
TODO.
```

## 4. 查询key写入情况

```shell
# LockBit
commander tokendump --tokengroup znet --device EFR32MG24A410F1536IM40
# OTP
commander security readkey --sign --device EFR32MG24A410F1536IM40
```
### Compare
```c
& "C:\Program Files\Git\usr\bin\openssl.exe" ec -pubin -in .\sign_pubkey.pem -text -noout
```

```c
commander device reset
commander device reset --serialno <>
commander device recover
commander device recover --device EFR32MG24A410F1536IM40 --serialno 440045640
commander security erasedevice
commander security erasedevice --device EFR32MG24A410F1536IM40 --serialno 440045640
```

```c
commander convert gfw_efr32_v2_mg24a-unsigned.s37 --secureboot --keyfile sign_key.pem --verify sign_pubkey.pem --outfile gfw_efr32_v2_mg24a-hrf.s37
```

## Debug Lock
```c
commander security lockconfig --secure-debug-unlock enable --device EFR32MG24A410F1536IM40 -s 440045640
commander security lock --device EFR32MG24A410F1536IM40 -s 440045640
```
## Status
```c
commander security status --trustzone --device EFR32MG24A410F1536IM40  -s 440045640
SE Firmware version   : 2.2.5
Serial number         : 000000000000000038398ffffe536e4b
Debug lock            : Enabled
Device erase          : Enabled
Secure debug unlock   : Enabled

Debug lock state: Locked

TrustZone Config:
Non-secure, invasive debug lock     (DBGLOCK)  : Unlocked
Non-secure, non-invasive debug lock (NIDLOCK)  : Unlocked
Secure, invasive debug lock         (SPIDLOCK) : Unlocked
Secure, non-invasive debug lock     (SPNIDLOCK): Unlocked

TrustZone State:
Non-secure, invasive debug lock state     (DBGLOCK)  : Unlocked
Non-secure, non-invasive debug lock state (NIDLOCK)  : Unlocked
Secure, invasive debug lock state         (SPIDLOCK) : Unlocked
Secure, non-invasive debug lock state     (SPNIDLOCK): Unlocked

Tamper status         : Not OK
Secure boot           : Enabled
Boot status           : 0x20 - OK
Command key installed : True
Sign key installed    : True
DONE
```
### Sign
```c
commander security readkey --sign --device EFR32MG24A410F1536IM40
888BC18F78E7B9AC87A0B9289E696A0651E1A4B49A31E6FF4F4DB596CA4D9BA2727E902C565C7267CADD9001CA9B0808D24CF35AA5454D352EAA3E6FDC2CCBF2
DONE
```
```c
  888BC18F78E7B9AC87A0B9289E69
6A0651E1A4B49A31E6FF4F4DB596CA
4D9BA2727E902C565C7267CADD9001
CA9B0808D24CF35AA5454D352EAA3E
6FDC2CCBF2
```
```c
& "C:\Program Files\Git\usr\bin\openssl.exe" ec -pubin -in .\sign_pubkey.pem -text -noout
read EC key
Public-Key: (256 bit)
pub:
    04:88:8b:c1:8f:78:e7:b9:ac:87:a0:b9:28:9e:69:
    6a:06:51:e1:a4:b4:9a:31:e6:ff:4f:4d:b5:96:ca:
    4d:9b:a2:72:7e:90:2c:56:5c:72:67:ca:dd:90:01:
    ca:9b:08:08:d2:4c:f3:5a:a5:45:4d:35:2e:aa:3e:
    6f:dc:2c:cb:f2
ASN1 OID: prime256v1
NIST CURVE: P-256
```
### Command
```c
commander security readkey --command --device EFR32MG24A410F1536IM40
58D46B1C2EC807DA78234853AE9295DA4526E82A39DDC5C40493B4429CBAD18EE6CED6482661E03E64823C17847F1F4396BF9D73C50C64852189B81D9F1D605E
DONE
```
```c
  58D46B1C2EC807DA78234853AE92
95DA4526E82A39DDC5C40493B4429C
BAD18EE6CED6482661E03E64823C17
847F1F4396BF9D73C50C64852189B8
1D9F1D605E
```
```c
& "C:\Program Files\Git\usr\bin\openssl.exe" ec -pubin -in .\command_pubkey.pem -text -noout
read EC key
Public-Key: (256 bit)
pub:
    04:58:d4:6b:1c:2e:c8:07:da:78:23:48:53:ae:92:
    95:da:45:26:e8:2a:39:dd:c5:c4:04:93:b4:42:9c:
    ba:d1:8e:e6:ce:d6:48:26:61:e0:3e:64:82:3c:17:
    84:7f:1f:43:96:bf:9d:73:c5:0c:64:85:21:89:b8:
    1d:9f:1d:60:5e
ASN1 OID: prime256v1
NIST CURVE: P-256
```

## Unlock
```c
commander security gencommand --action debug-unlock --device EFR32MG24A410F1536IM40 -s 440045640
Unsigned command file written to Security Store:
C:/Users/huide/AppData/Local/SiliconLabs/commander/SecurityStore/device_000000000000000038398ffffe536e4b/challenge_af7815d1cf0a9ccd557dbc061c81b139/unlock_command_to_be_signed14_08_2026.bin
DONE
```
```c
PS C:\Users\huide\AppData\Local\SiliconLabs\commander\SecurityStore\device_000000000000000038398ffffe536e4b> commander security unlock --cert access_certificate.bin --cert-privkey cert_key.pem --unlock-param 1111 --device EFR32MG24A410F1536IM40 -s 440045640
Unlocking with unlock payload:
C:/Users/huide/AppData/Local/SiliconLabs/commander/SecurityStore/device_000000000000000038398ffffe536e4b/challenge_af7815d1cf0a9ccd557dbc061c81b139/unlock_payload_0000000000111110.bin
Secure debug successfully unlocked
DONE
```