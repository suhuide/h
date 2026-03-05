
## 2


|缩写	|全称	|角色定位|
| ---- | ---- | ---- |
|CA	|Certificate Authority	|这是一个通用术语，指代负责颁发和管理数字证书的证书颁发机构。在Matter中，它通常用来泛指后面提到的PAI或PAA这类有颁发权限的机构|
|NOC	|Node Operational Certificate	|这是节点操作证书，是设备加入特定Matter网络（称为“Fabric”）后获得的“数字身份证”。它用于设备之间的日常通信和身份验证，由网络的Root CA或Intermediate CA颁发|
|DAC	|Device Attestation Certificate	|这是设备认证证书，是设备出厂时被烧录在硬件中的“出生证明”，独一无二且不可伪造。在新设备首次入网时，它被用来向网络证明自己是来自可信厂商的、符合Matter标准的合法设备|
|PAI	|Product Attestation Intermediate	|这是产品认证中间证书，由PAA颁发给具体的设备厂商。它位于证书链的中间层，用于签署该厂商旗下具体产品的DAC证书，起到承上启下的作用|
|PAA	|Product Attestation Authority	|这是产品认证机构，是整个Matter设备认证体系的最高层级信任根（Root of Trust）。它是一个全球性的、被CSA（连接标准联盟）审核并列入公共清单的权威机构，负责签发PAI证书|