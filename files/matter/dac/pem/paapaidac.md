
## DAC
```c
openssl x509 -in dac.pem -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            0e:cb:29:b3:32:16:a9:9d:31:83:fc:5d:fe:c9:24:f9
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: CN=HOPERF Matter PAI 01, 1.3.6.1.4.1.37244.2.1=1470
        Validity
            Not Before: Oct 21 05:10:28 2024 GMT
            Not After : Sep 27 06:10:28 2124 GMT
        Subject: CN=HOPERF Matter DAC, 1.3.6.1.4.1.37244.2.1=1470, 1.3.6.1.4.1.37244.2.2=8006
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:e9:56:79:4b:3d:63:e4:e6:32:b1:60:ac:b2:3d:
                    e6:50:47:76:1f:e6:dc:20:e2:16:11:d1:7e:9e:7b:
                    3d:73:5c:a9:f7:3a:60:84:ca:2d:61:07:29:4b:bb:
                    0a:f9:bd:eb:92:98:b4:7f:7c:11:73:00:39:b2:76:
                    36:c9:a2:a0:8e
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Authority Key Identifier:
                EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
            X509v3 Subject Key Identifier:
                9C:44:E4:A9:69:D2:AA:CE:76:05:51:CB:E8:4C:DB:E9:68:39:3C:BC
            X509v3 Key Usage: critical
                Digital Signature
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value:
        30:45:02:21:00:f7:7e:ac:88:9a:d6:ce:bd:65:f1:84:8b:f4:
        35:79:85:09:c3:d3:b8:17:a3:3a:bd:fe:70:ad:35:82:ba:56:
        d4:02:20:02:f5:86:53:79:95:b3:a3:7b:e6:a2:1f:33:75:b0:
        a4:21:a8:84:9a:d3:e3:81:0f:72:6c:ed:0e:a6:d6:f1:2e
```

## PAI
```c
openssl x509 -in pai.pem -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            eb:49:bf:aa:73:8f:a5:5d:a8:eb:1b:36:94:58:3f:ec
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: CN=HOPERF Matter PAA 01, 1.3.6.1.4.1.37244.2.1=1470
        Validity
            Not Before: Sep  5 00:19:40 2023 GMT
            Not After : Oct 22 01:19:40 2220 GMT
        Subject: CN=HOPERF Matter PAI 01, 1.3.6.1.4.1.37244.2.1=1470
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:02:37:c9:8e:c5:fb:fc:70:3b:9c:17:63:4a:94:
                    4a:e1:0e:06:22:2e:ab:58:8e:60:e4:c8:8c:71:07:
                    be:e9:eb:b6:43:36:e5:ea:19:f3:4f:69:16:42:63:
                    ca:e2:09:7e:65:a5:16:f8:a0:5f:b3:6d:0c:45:1f:
                    3c:a6:50:88:24
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Authority Key Identifier:
                E9:16:0D:C4:17:F7:41:9C:95:32:0B:BF:36:56:71:93:3F:F3:12:22
            X509v3 Subject Key Identifier:
                EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value:
        30:46:02:21:00:99:85:dc:c5:9a:00:1d:fe:58:56:af:f3:d0:
        f7:6b:42:a8:0d:9f:bb:73:84:86:98:9b:63:0d:dc:b3:08:f6:
        82:02:21:00:f0:37:e7:cc:53:1a:57:3f:10:68:3c:88:ff:28:
        1d:08:61:0f:30:16:e9:bc:7c:71:f4:a3:44:88:9b:3b:81:c1
```

## PAA
```c
openssl x509 -in dac.pem -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            0e:cb:29:b3:32:16:a9:9d:31:83:fc:5d:fe:c9:24:f9
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: CN=HOPERF Matter PAI 01, 1.3.6.1.4.1.37244.2.1=1470
        Validity
            Not Before: Oct 21 05:10:28 2024 GMT
            Not After : Sep 27 06:10:28 2124 GMT
        Subject: CN=HOPERF Matter DAC, 1.3.6.1.4.1.37244.2.1=1470, 1.3.6.1.4.1.37244.2.2=8006
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:e9:56:79:4b:3d:63:e4:e6:32:b1:60:ac:b2:3d:
                    e6:50:47:76:1f:e6:dc:20:e2:16:11:d1:7e:9e:7b:
                    3d:73:5c:a9:f7:3a:60:84:ca:2d:61:07:29:4b:bb:
                    0a:f9:bd:eb:92:98:b4:7f:7c:11:73:00:39:b2:76:
                    36:c9:a2:a0:8e
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Authority Key Identifier:
                EB:B4:9A:F1:2D:D5:23:57:BD:3E:5A:D2:3D:6F:47:06:D0:BF:9F:9A
            X509v3 Subject Key Identifier:
                9C:44:E4:A9:69:D2:AA:CE:76:05:51:CB:E8:4C:DB:E9:68:39:3C:BC
            X509v3 Key Usage: critical
                Digital Signature
    Signature Algorithm: ecdsa-with-SHA256
    Signature Value:
        30:45:02:21:00:f7:7e:ac:88:9a:d6:ce:bd:65:f1:84:8b:f4:
        35:79:85:09:c3:d3:b8:17:a3:3a:bd:fe:70:ad:35:82:ba:56:
        d4:02:20:02:f5:86:53:79:95:b3:a3:7b:e6:a2:1f:33:75:b0:
        a4:21:a8:84:9a:d3:e3:81:0f:72:6c:ed:0e:a6:d6:f1:2e
```