## Version
### Chip-tool log
```c
[1787711396.532193][3742025:3742025] CHIP:EM: Handling via exchange: 36286r, Delegate: 0xaaaab799c880
[1787711396.532279][3742025:3742025] CHIP:DMG: InvokeRequestMessage =
[1787711396.532306][3742025:3742025] CHIP:DMG: {
[1787711396.532325][3742025:3742025] CHIP:DMG:  suppressResponse = false,
[1787711396.532347][3742025:3742025] CHIP:DMG:  timedRequest = false,
[1787711396.532367][3742025:3742025] CHIP:DMG:  InvokeRequests =
[1787711396.532395][3742025:3742025] CHIP:DMG:  [
[1787711396.532415][3742025:3742025] CHIP:DMG:          CommandDataIB =
[1787711396.532439][3742025:3742025] CHIP:DMG:          {
[1787711396.532463][3742025:3742025] CHIP:DMG:                  CommandPathIB =
[1787711396.532487][3742025:3742025] CHIP:DMG:                  {
[1787711396.532510][3742025:3742025] CHIP:DMG:                          EndpointId = 0x0,
[1787711396.532533][3742025:3742025] CHIP:DMG:                          ClusterId = 0x29,
[1787711396.532556][3742025:3742025] CHIP:DMG:                          CommandId = 0x0,
[1787711396.532578][3742025:3742025] CHIP:DMG:                  },
[1787711396.532602][3742025:3742025] CHIP:DMG:
[1787711396.532622][3742025:3742025] CHIP:DMG:                  CommandFields =
[1787711396.532644][3742025:3742025] CHIP:DMG:                  {
[1787711396.532667][3742025:3742025] CHIP:DMG:                          0x0 = 5232 (unsigned),
[1787711396.532691][3742025:3742025] CHIP:DMG:                          0x1 = 65281 (unsigned),
[1787711396.532715][3742025:3742025] CHIP:DMG:                          0x2 = 10001 (unsigned),
[1787711396.532737][3742025:3742025] CHIP:DMG:                          0x3 = [
[1787711396.532761][3742025:3742025] CHIP:DMG:                                          0 (unsigned),
[1787711396.532788][3742025:3742025] CHIP:DMG:                          ],
[1787711396.532812][3742025:3742025] CHIP:DMG:                          0x4 = 1 (unsigned),
[1787711396.532837][3742025:3742025] CHIP:DMG:                          0x5 = "XX" (2 chars),
[1787711396.532862][3742025:3742025] CHIP:DMG:                          0x6 = false,
[1787711396.532885][3742025:3742025] CHIP:DMG:                  },
[1787711396.532905][3742025:3742025] CHIP:DMG:          },
[1787711396.532931][3742025:3742025] CHIP:DMG:
[1787711396.532949][3742025:3742025] CHIP:DMG:  ],
[1787711396.532975][3742025:3742025] CHIP:DMG:
[1787711396.532993][3742025:3742025] CHIP:DMG:  InteractionModelRevision = 12
[1787711396.533011][3742025:3742025] CHIP:DMG: },
[1787711396.533141][3742025:3742025] CHIP:DMG: AccessControl: checking f=1 a=c s=0x00000000000008CA t= c=0x0000_0029 e=0 p=o r=i
[1787711396.533177][3742025:3742025] CHIP:DMG: AccessControl: allowed
[1787711396.533200][3742025:3742025] CHIP:DMG: Received command for Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0000
[1787711396.533249][3742025:3742025] CHIP:ZCL: OTA Provider received QueryImage
[1787711396.533273][3742025:3742025] CHIP:ZCL:   VendorID: 0x1470
[1787711396.533288][3742025:3742025] CHIP:ZCL:   ProductID: 65281
[1787711396.533302][3742025:3742025] CHIP:ZCL:   SoftwareVersion: 10001
[1787711396.533348][3742025:3742025] CHIP:ZCL:   ProtocolsSupported: [
[1787711396.533370][3742025:3742025] CHIP:ZCL:     0
[1787711396.533385][3742025:3742025] CHIP:ZCL:   ]
[1787711396.533399][3742025:3742025] CHIP:ZCL:   HardwareVersion: 1
[1787711396.533413][3742025:3742025] CHIP:ZCL:   Location: XX
[1787711396.533428][3742025:3742025] CHIP:ZCL:   RequestorCanConsent: 0
[1787711396.533956][3742025:3742025] CHIP:SWU: Generated updateToken: 13BC5CA48B68F0DA8EF6679956BD54
[1787711396.533992][3742025:3742025] CHIP:SWU: Generated URI: bdx://0000000000000001/aok02_matter_ac_0x149A_0x3005-v1.0.0-signed-2e795aba.ota
[1787711396.534013][3742025:3742025] CHIP:BDX: Start polling for messages
```

[CHIP:ZCL:   SoftwareVersion: 10001] is current/old version
### Matter device log
#### 1
```c
[00:04:25.578][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[10:29:55.440]  [00:04:25.578][detail][SWU] QueryImageResponse:
[10:29:55.440]  [00:04:25.579][detail][SWU]   status: 0
[10:29:55.440]  [00:04:25.579][detail][SWU]   imageURI: bdx://0000000000000001/aok02_matter_ac_0x149A_0x3005-v1.0.0-signed-2e795aba.ota
[10:29:55.442]  [00:04:25.579][detail][SWU]   softwareVersion: 1004
[10:29:55.443]  [00:04:25.579][detail][SWU]   softwareVersionString: 1.0.0
[10:29:55.443]  [00:04:25.579][detail][SWU]   updateToken: 32
[10:29:55.443]  [00:04:25.579][detail][SWU]   userConsentNeeded: 0
[10:29:55.444]  [00:04:25.580][detail][DMG] Endpoint 0, Cluster 0x0000_002A update version to 96e0023e
[10:29:55.447]  [00:04:25.582][detail][DMG] ICR moving to [AwaitingDe]
[10:29:55.447]  [00:04:25.583][info  ][EM] <<< [E:36286i S:53886 M:42843872 (Ack:133085000)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [666E] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[10:29:55.449]  [00:04:25.584][detail][EM] Flushed pending ack for MessageCounter:133085000 on exchange 36286i
```
#### 2
```c
[11:30:24.449]  [00:02:50.281][detail][EM] Rxd Ack; Removing MessageCounter:215126173 from Retrans Table on exchange 26060i
[11:30:24.451]  
[11:30:24.451]  Missed Logs: 4
[11:30:24.451]  [00:02:50.282][detail][DMG] ICR moving to [ResponseRe]
[11:30:24.452]  [00:02:50.282][info  ][DMG] Received Command Response Data, Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0001
[11:30:24.454]  [00:02:50.283][detail][SWU] QueryImageResponse:
[11:30:24.454]  [00:02:50.283][detail][SWU]   status: 0
[11:30:24.454]  [00:02:50.283][detail][SWU]   imageURI: bdx://0000000000000001/aok02_matter_ac_0x149A_0x3005-v1.0.0-signed-2e795aba.ota
[11:30:24.455]  [00:02:50.283][detail][SWU]   softwareVersion: 1004
[11:30:24.456]  [00:02:50.283][detail][SWU]   softwareVersionString: 1.0.0
[11:30:24.456]  [00:02:50.284][detail][SWU]   updateToken: 32
[11:30:24.456]  [00:02:50.284][detail][SWU]   userConsentNeeded: 0
[11:30:24.457]  [00:02:50.284][detail][SWU] Available update version 1004 is <= current version 10000, update ignored
[11:30:24.459]  [00:02:50.286][detail][DMG] ICR moving to [AwaitingDe]
[11:30:24.459]  [00:02:50.288][info  ][EM] <<< [E:26060i S:10084 M:215126174 (Ack:146213790)] (S) Msg TX from 00000000000008CA to 1:0000000000000001 [E017] [UDP:[fd00:dcff:665f:1:29c8:86f3:61b8:969e]:5540] --- Type 0000:10 (SecureChannel:StandaloneAck) (B:34)
[11:30:24.461]  [00:02:50.289][detail][EM] Flushed pending ack for MessageCounter:146213790 on exchange 26060i
```
1# and 2#, FW is the same, 1# Some log is missing. 2# show that version is smaller then current version, cause by packet mistake.

## OTA End
```c
[1787715970.905977][260941:260941] CHIP:DMG: Received command for Endpoint=0 Cluster=0x0000_0029 Command=0x0000_0002
[1787715970.906015][260941:260941] CHIP:ZCL: OTA Provider received ApplyUpdateRequest
[1787715970.906033][260941:260941] CHIP:ZCL:   Update Token: 32
[1787715970.906048][260941:260941] CHIP:ZCL:   New Version: 10004
[1787715970.906072][260941:260941] CHIP:SWU: HandleApplyUpdateRequest: token: A9A64899B281ACC26D2A792ED21279, version: 10004
[1787715970.906125][260941:260941] CHIP:DMG: Command handler moving to [NewRespons]
[1787715970.906147][260941:260941] CHIP:DMG: Command handler moving to [ Preparing]
[1787715970.906171][260941:260941] CHIP:DMG: Command handler moving to [AddingComm]
[1787715970.906195][260941:260941] CHIP:DMG: Command handler moving to [AddedComma]
[1787715970.906237][260941:260941] CHIP:DMG: Decreasing reference count for CommandHandlerImpl, remaining 1
[1787715970.906258][260941:260941] CHIP:DMG: Decreasing reference count for CommandHandlerImpl, remaining 0
[1787715970.906281][260941:260941] CHIP:DMG: Command handler moving to [AwaitingDe]
[1787715970.906425][260941:260941] CHIP:EM: <<< [E:48828r S:10609 M:29845720 (Ack:91777380)] (S) Msg TX from 0000000000000001 to 1:00000000000008CA [629A] [UDP:[fd00:dcff:665f:1:39d0:cbd6:3a0b:f6c0]:5540] --- Type 0001:09 (IM:InvokeCommandResponse) (B:70)
[1787715970.906631][260941:260941] CHIP:EM: ??1 [E:48828r S:10609 M:29845720] (S) Msg Retransmission to 1:00000000000008CA in 2504ms [State:Active II:2000 AI:2000 AT:4000]
[1787715970.906701][260941:260941] CHIP:DMG: Command response sender moving to [AllInvokeR]
[1787715970.926915][260941:260941] CHIP:BDX: OutputEvent type: AckEOFReceived
[1787715970.926972][260941:260941] CHIP:BDX: Transfer completed, got AckEOF
[1787715970.926998][260941:260941] CHIP:BDX: Stop polling for messages
[1787715970.927160][260941:260941] CHIP:EM: <<< [E:48827r S:10609 M:298457
```
## Key Error
```c
[11:46:09.883]  [00:05:41.491][info  ][SWU] HandleApply: verifying image
[11:46:09.883]  [00:05:41.497][error ][SWU] bootloader_verifyImage() error: 4104
[11:46:09.883]  [00:05:41.497][error ][BDX] No download in progress
```
```c
#define BOOTLOADER_ERROR_PARSER_KEYERROR \
  (BOOTLOADER_ERROR_PARSER_BASE | 0x04L)
```