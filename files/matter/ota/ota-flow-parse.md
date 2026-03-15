# How to Parse Matter Message Types (Type XXXX:YY) from Logs

The entries like `Type 0000:10` in the logs are **OpCodes (Operation Codes)** that identify the specific protocol and message being sent or received in the Matter communication.

## 1. Message Type Reference Tables (From Your Logs)

### Protocol 0x0000: Secure Channel
Used for establishing and managing encrypted sessions (PASE and CASE).
```c
4.11. Secure Channel Protocol
    4.11.1. Secure Channel Protocol Messages
```
| Protocol Opcode | Protocol Command Name | Description | Log Example |
| :--- | :--- | :--- | :--- |
| **0x00** | `MsgCounterSyncReq` | Request to synchronize message counters | `Type 0000:00` |
| **0x01** | `MsgCounterSyncRsp` | Response to a counter sync request | `Type 0000:01` |
| **0x10** | `MRP Standalone Acknowl­edgement` | Acknowledges receipt of a previous message |  `Type 0000:10` |
| **0x20** | `PBKDFParamRequest` | Initiates PASE handshake |  `Type 0000:20` |
| **0x21** | `PBKDFParamResponse` | Provides PASE parameters |  `Type 0000:21` |
| **0x22** | `PASE_Pake1` | First round of PASE handshake |  `Type 0000:22` |
| **0x23** | `PASE_Pake2` | Second round of PASE handshake |  `Type 0000:23` |
| **0x24** | `PASE_Pake3` | Final round of PASE handshake |  `Type 0000:24` |
| **0x30** | `CASE_Sigma1` | Initiates CASE handshake |  `Type 0000:30` |
| **0x31** | `CASE_Sigma2` | Second round of CASE handshake |  `Type 0000:31` |
| **0x32** | `CASE_Sigma3` | Final round of CASE handshake |  `Type 0000:32` |
| **0x33** | `CASE_Sigma2Resume` | Optimized Sigma2 to resume session |  `Type 0000:33` |
| **0x40** | `StatusReport` | Reports protocol operation status |  `Type 0000:40` |
| **0x50** | `ICD Check-In message` | Reports protocol operation status |  `Type 0000:50` |

### Protocol 0x0001: Interaction Model (IM)
Core "business logic" protocol for reading/writing attributes and invoking commands.
```c
10.2. Messages
    10.2.1. IM Protocol Messages
```
| Protocol Opcode | Message | Action | Log Example |
| :--- | :--- | :--- | :--- |
| **0x01** | `StatusResponseMessage` | Status Response |  `Type 0001:01` |
| **0x02** | `ReadRequesStatusResponseMessage` | Request to read attributes from a device |  `Type 0001:02` |
| **0x03** | `SubscribeRequestMessage` | Subscribe Request |  `Type 0001:03` |
| **0x04** | `SubscribeResponseMessage` | Subscribe Response|  `Type 0001:04` |
| **0x05** | `ReportData` | Sends data (response to ReadRequest or subscription update) |  `Type 0001:05` |
| **0x06** | `WriteRequest` | Request to write attributes on a device |  `Type 0001:06` |
| **0x07** | `WriteResponse` | Response to WriteRequest |  `Type 0001:07` |
| **0x08** | `InvokeCommandRequest` | Request to execute a specific command (e.g., QueryImage) |  `Type 0001:08` |
| **0x09** | `InvokeCommandResponse` | Response to InvokeCommandRequest |  `Type 0001:09` |
| **0x0A** | `TimedRequestMessage` | Timed Request |  `Type 0001:0A` |

### Protocol 0x0002: Bulk Data Exchange (BDX)
Used for transferring large files, like OTA images.
```c
11.22.3. Protocol Opcodes and Status Report Values
    11.22.3.1. BDX Protocol Messages
```
| Msg Type (Hex) | Message | Description | Log Example |
| :--- | :--- | :--- | :--- |
| **0x01**| `SendInit` | | |
| **0x02**| `SendAccept` | | |
| **0x03**| `Reserved for future use` | | |
| **0x04** | `ReceiveInit` | Initiates a transfer (downloading a file) |  `Type 0002:04` |
| **0x05** | `ReceiveAccept` | Sender accepts the transfer |  `Type 0002:05` |
| **0x06**| `Reserved for future use| | |
| **0x10** | `BlockQuery` | Receiver asks for a specific data block |  `Type 0002:10` |
| **0x11** | `Block` | Sender responds with a data block |  `Type 0002:11` |
| **0x12** | `BlockEOF` | Final block, signaling end of file |  `Type 0002:12` |
| **0x14** | `BlockAckEOF` | Receiver acknowledges final block |  `Type 0002:14` |
| **0x15**| `BlockQueryWithSkip` | | |
