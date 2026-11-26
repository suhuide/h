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
308BC18F78E7B9AC87A0B9289E696A0651E1A4B49A31E6FF4F4DB596CA4D9BA2727E902C565C7267CADD9001CA9B0808D217F35AA5454D352EAA3E6FDC2CCB8C
DONE
```
```c
  308BC18F78E7B9AC87A0B9289E69
6A0651E1A4B49A31E6FF4F4DB596CA
4D9BA2727E902C565C7267CADD9001
CA9B0808D217F35AA5454D352EAA3E
6FDC2CCB8C
```
```c
& "C:\Program Files\Git\usr\bin\openssl.exe" ec -pubin -in .\sign_pubkey.pem -text -noout
read EC key
Public-Key: (256 bit)
pub:
    04:30:8b:c1:8f:78:e7:b9:ac:87:a0:b9:28:9e:69:
    6a:06:51:e1:a4:b4:9a:31:e6:ff:4f:4d:b5:96:ca:
    4d:9b:a2:72:7e:90:2c:56:5c:72:67:ca:dd:90:01:
    ca:9b:08:08:d2:17:f3:5a:a5:45:4d:35:2e:aa:3e:
    6f:dc:2c:cb:8c
ASN1 OID: prime256v1
NIST CURVE: P-256
```
### Command
```c
commander security readkey --command --device EFR32MG24A410F1536IM40
70D46B1C2EC807DA78234853AE9295DA4526E82A39DDC5C40493B4429CBAD18EE6CED6482661E03E64823C17847F1F4396BF9D73C50C64852189B81D9F1D4E5E
DONE
```
```c
  70D46B1C2EC807DA78234853AE92
95DA4526E82A39DDC5C40493B4429C
BAD18EE6CED6482661E03E64823C17
847F1F4396BF9D73C50C64852189B8
1D9F1D4E5E
```
```c
& "C:\Program Files\Git\usr\bin\openssl.exe" ec -pubin -in .\command_pubkey.pem -text -noout
read EC key
Public-Key: (256 bit)
pub:
    04:70:d4:6b:1c:2e:c8:07:da:78:23:48:53:ae:92:
    95:da:45:26:e8:2a:39:dd:c5:c4:04:93:b4:42:9c:
    ba:d1:8e:e6:ce:d6:48:26:61:e0:3e:64:82:3c:17:
    84:7f:1f:43:96:bf:9d:73:c5:0c:64:85:21:89:b8:
    1d:9f:1d:4e:5e
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