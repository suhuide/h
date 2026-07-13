# TC-S-2.3 Scenes Management 认证失败分析总结

> 平台：Silabs EFR32MG24 + Matter SDK (conan: matte8bada656e9e76)
> 项目：`C:\Si\v6\aok02_matter_ac`
> DUT：endpoint 3 = Extended Color Light（ColorControl FeatureMap = 0x19 = HueAndSaturation + ColorTemperature + XY）
> 日期：2026-07-06
>
> ⚠️ 本报告推翻了之前版本"RemoveScene 没真删 / NVM3 bug / FabricTableImpl bug"的结论。经加 log 实测，**DUT scene 逻辑完全正确，6e/6i 失败是 group message counter（test harness）问题**。

---

## 1. 问题现象

认证实验室报 TC-S-2.3 (123.2.3) 部分步骤 fail：

| endpoint | 失败步骤 |
|---|---|
| ep3 / ep4 / ep5 | step 6e, 6i |
| ep6 / ep7 | step 3, 6b, 6e, 6i, 7d, 8b, 8d, 9b, 10b |

ep3/4/5 只 fail groupcast RemoveScene 相关的 6e/6i；ep6/7 范围更广（连 unicast step 3 都 fail，疑似 ep6/7 cluster 配置/scene handler 问题，另查）。

**本文聚焦 ep3。**

---

## 2. TC-S-2.3 关键步骤（Test_TC_S_2_3.yaml）

| step | 操作 | 方向 | 期望 |
|---|---|---|---|
| 0a/0b/0c | KeySetWrite + GroupKeyMap（G1→keyset 0x01a1, TrustFirst）| unicast | — |
| 1a/1b | AddGroup G1(0x0101), G2(0x0102) | unicast | status 0 |
| 1c | 写 ACL（group authmode = manage）| unicast | — |
| 1d/1e | RemoveAllScenes G1, G2 | unicast | status 0 |
| 2 | AddScene G1 scene 1, EFS=OnOff(0x06)+LevelControl(0x08) | unicast | status 0 |
| 3 | ViewScene G1 scene 1 | unicast | status 0 |
| 5b | RecallScene G1 scene 1 | **groupcast** | — |
| 6a | AddScene G1 scene 3, EFS=OnOff+LevelControl | **groupcast** | (无响应) |
| 6b | ViewScene G1 scene 3 | unicast | status 0 |
| 6c | ViewScene G1 scene 3 | **groupcast** | — |
| 6d | RemoveScene G1 scene 3 | **groupcast** | — |
| 6e | ViewScene G1 scene 3 | unicast | **status 0x8b (NotFound)** |
| 6f | StoreScene G1 scene 3 | **groupcast** | — |
| 6g | ViewScene G1 scene 3 | unicast | status 0 |
| 6h | RemoveScene G1 scene 3 | **groupcast** | — |
| 6i | ViewScene G1 scene 3 | unicast | **status 0x8b** |
| 7~8 | CopyScene / GetSceneMembership | unicast+groupcast | — |
| 9a | RemoveAllScenes G1 | **groupcast** | — |
| 9b | GetSceneMembership G1 | unicast | SceneList=[] |
| 10a | RemoveAllScenes G2 | **groupcast** | — |
| 10b | GetSceneMembership G2 | unicast | SceneList=[] |

> **注意**：YAML 自动用例（`PICS_SDK_CI_ONLY`，step 6a 的 `command:` 块）用的是 **OnOff+LevelControl** EFS；ColorControl(0x0300) attr 0x4002 那条是 `PICS_SKIP_SAMPLE_APP` 的手动验证命令（只给 sample app），认证自动跑不用它。

---

## 3. 排查过程与各阶段结论

### 3.1 早期怀疑（都被排除）

#### a) 早期 device log 现象
- unicast AddScene/ViewScene/RemoveScene 全部正常（status 0）。
- groupcast AddScene：`HandleAddScene` 被调用，但之后没有 FabricSceneInfo version bump → 早期误以为 groupcast AddScene 整体失败。
- groupcast RemoveAllScenes（cmd 0x05）：返回 status 0x8b。

#### b) DeepSeek 的诊断（部分对、结论错）
DeepSeek 说"groupcast 时 EFS 处理中 ReturnOnFailure 导致 AddScene 整体失败"，并建议改 `FabricTableImpl.ipp` 第 431 行 `RemoveEntry`：

```cpp
// 原代码
VerifyOrReturnValue(this->Find(entry_id, entryIndex) == CHIP_NO_ERROR, CHIP_NO_ERROR);
// DeepSeek 建议改成
ReturnErrorOnFailure(this->Find(entry_id, entryIndex));
```

**这个改法是错的，不能采用**，原因：
1. `HandleRemoveScene` 在删除前**先调 `GetSceneTableEntry` 检查存在**（scenes-server.cpp:857），NOT_FOUND 就直接返回，**根本到不了 `RemoveEntry`**。
2. 所以 `RemoveEntry` 第 431 行"Find 失败返回 SUCCESS"是正确的幂等行为，且 RemoveScene 路径上不会命中。
3. 改成 `ReturnErrorOnFailure` 反而会把 unicast RemoveScene（scene 不存在时）从 Success 变成 NotFound，破坏现有正确行为。

#### c) 之前放弃的 `scenes-server.txtgroupcast` 补丁（方向错）
该补丁做两件事，都不可取：
1. **解析 fabric index（遍历所有 fabric 找 group）** —— 没必要：groupcast 的 `GetAccessingFabricIndex()` 返回有效 fabric（device log 中 groupcast RemoveAllScenes 触发了 FabricSceneInfo version bump，而 `UpdateFabricSceneInfo` 对 fabric=0 会返回 INVALID_ARGUMENT 不 bump，证明 fabric 有效）。
2. **EFS 出错就 Clear** —— 会出现"status 0 但 entry 0"（scene 存了但 EFS 空），认证 6b 要校验 EFS 内容，照样过不了。

### 3.2 用户手动 groupcast AddScene 失败的真正原因 = EFS 校验失败

用户手动测试用的命令是 TC-S-2.3 的**手动验证命令**（yaml:538）：
```
add-scene 0x0101 0x03 1000 "scene name" \
  '[{"clusterID":"0x0300","attributeValueList":[{"attributeID":"0x4002","valueUnsigned8":"0x01"}]}]' \
  0xffffffffffff0101 3
```

**`0x4002` 是 ColorControl cluster 的 ColorLoopActive 属性**（`color-control-cluster.xml:633`），int8u，**仅当支持 ColorLoop (CL) feature 时才强制**。

ep3 的 ColorControl `FeatureMap = 0x19`（= HS + CT + XY，**没有 ColorLoop bit2**），所以 0x4002 这个属性根本没生成。

AddSceneParse 的 EFS 处理（scenes-server.cpp）：
```cpp
for (auto & handler : sceneTable->mHandlerList) {
    if (handler.SupportsCluster(ep, tempEFS.mID)) {          // ColorControl handler 支持
        ReturnOnFailure(AddResponseOnError(ctx, response,
            handler.SerializeAdd(...)));                      // ← 这里失败就 return，scene 不存
        break;
    }
}
```
`SerializeAdd` → `ValidateAttributePath`（SceneHandlerImpl.cpp:134）→ `emberAfLocateAttributeMetadata(ep3, 0x0300, 0x4002)` 返回 null → `UnsupportedAttribute` → `SerializeAdd` 失败 → AddScene 整个中止 → 没 version bump。

**这是用户手动测试用错 EFS，不是 DUT bug，也不是认证失败原因**（认证自动用例用 OnOff+LevelControl，ep3 都支持）。

> 顺带：用户早期 ViewScene 查的是 scene 1（不是 groupcast 加的 scene 3），返回 139 是正常的（scene 1 早已删），不是 groupcast AddScene 失败的证据。

#### ColorControl 的 9 个 scenable 属性（color-control-server.cpp:42 DefaultColorControlSceneHandler）

| attrID | 名字 | 类型 | 需要 feature | ep3(0x19) |
|---|---|---|---|---|
| 0x0000 | CurrentHue | int8u | HueAndSaturation | ✅ |
| 0x0001 | CurrentSaturation | int8u | HueAndSaturation | ✅ |
| 0x0003 | CurrentX | int16u | XY | ✅ |
| 0x0004 | CurrentY | int16u | XY | ✅ |
| 0x0007 | ColorTemperatureMireds | int16u | ColorTemperature | ✅ |
| 0x4001 | EnhancedColorMode | enum8 | mandatory | ✅ |
| 0x4000 | EnhancedCurrentHue | int16u | EnhancedHue | ❌ |
| 0x4002 | ColorLoopActive | int8u | ColorLoop | ❌ |
| 0x4003/0x4004 | ColorLoopDirection/Time | | ColorLoop | ❌ |

要改手动命令，换成 ep3 支持的属性即可（如 `0x0000` CurrentHue，保持 `valueUnsigned8`）。

### 3.3 加诊断 log 定位

在 `scenes-server.cpp` 的 `AddSceneParse` 和 `HandleRemoveScene` 每步加 `eric,` log（只加 log，不动逻辑）：
- AddSceneParse：进入(fabric/组/scene) → group check → 每个 EFS cluster + handler + `SerializeAdd` err → EFS iter status → capacity → `SetSceneTableEntry` err → `UpdateFabricSceneInfo` err → SUCCESS
- HandleRemoveScene：进入(fabric/组/scene) → group check → `GetSceneTableEntry` err → `RemoveSceneTableEntry` err → `UpdateFabricSceneInfo` err → SUCCESS

### 3.4 第一轮 log（20260706_114822.txt）发现 groupcast 消息被丢

- groupcast AddScene scene 3（改用支持的 EFS 后）→ **SUCCESS**（scene 存进去了）。
- 但 6a 之后的 groupcast 消息（73 字节，groupcast RemoveScene/StoreScene 等）全部 `Message counter verify failed, err = c4` 被丢，**根本没到 HandleRemoveScene**。
- 接受的 groupcast counter：`M:123140924` → `M:123147924`（差 7000，明显是每进程随机/时间初始化，非持久化 +1）。

### 3.5 counter 丢包机制（根因）

代码路径：`SessionManager.cpp:1176-1204` → `PeerMessageCounter.h:111` `VerifyOrTrustFirstGroup`：

```cpp
CHIP_ERROR VerifyOrTrustFirstGroup(uint32_t counter) {
    switch (mStatus) {
    case NotSynced: SetCounter(counter); return CHIP_NO_ERROR;   // 第一条：信任
    case Synced:    return VerifyGroup(counter);                 // 之后：必须 forward 才接受
    }
}
```

Matter spec 4.7.3 TrustFirst 策略：
- 第一条 groupcast：信任，记下 max counter。
- 之后：counter > max 才接受（forward）；counter ≤ max 当 duplicate/back-track **丢弃**。

`th.md` 里每条命令都是**单独的 `docker exec -it th-sdk ./chip-tool ...` 进程**，chip-tool 每进程独立 group counter（不持久化、不共享）。所以后发的 groupcast counter 落到 device 已记录的 max 之下 → 被当重复丢弃。**这是 test harness 问题，DUT 行为完全符合 spec。**

### 3.6 第二轮 log（20260706_141409.txt，用 interactive 模式）确认 DUT 无 bug

用 `chip-tool interactive` 单进程跑，counter 单调递增，groupcast 不再被丢：

**groupcast AddScene scene 3（14:18:09）成功：**
```
eric,AddSceneParse ENTER: ep=3 grp=0x0101 scene=3 fabric=1
eric,AddSceneParse: group check OK fabric=1
eric,AddSceneParse: EFS cluster=0x300
eric,AddSceneParse: SerializeAdd err=0
eric,AddSceneParse: capacity=6 fabric=1
eric,AddSceneParse: SetSceneTableEntry err=0
eric,AddSceneParse: UpdateFabricSceneInfo err=0
eric,AddSceneParse: SUCCESS ep=3 grp=0x0101 scene=3
```

**groupcast RemoveScene scene 3（14:19:30）成功：**
```
eric,HandleRemoveScene ENTER: ep=3 grp=0x0101 scene=3 fabric=1
eric,RemoveScene: group check OK fabric=1
eric,RemoveScene: GetSceneTableEntry err=0 fabric=1 grp=0x0101 scene=3   ← 找到 scene
eric,RemoveEntry                                                          ← 进了 RemoveEntry
eric,RemoveScene: RemoveSceneTableEntry err=0                             ← 删除成功
eric,RemoveScene: UpdateFabricSceneInfo err=0
eric,RemoveScene: SUCCESS ep=3 grp=0x0101 scene=3
```

**删除后 unicast ViewScene（14:20:10）返回 NotFound：**

| 时间 | 命令 | 响应大小 | 含义 |
|---|---|---|---|
| 14:18:58 | ViewScene scene 3（删除前）| B:101 | Success（scene 在，带 EFS） |
| 14:20:10 | ViewScene scene 3（删除后）| **B:74** | **NotFound (0x8b)**（scene 已删） |

B:101 → B:74 的差 = EFS+transitionTime+sceneName 被去掉。**scene 3 已被 groupcast RemoveScene 删掉，6e 期望 0x8b，得到 0x8b → PASS。**

**接受的 groupcast counter（单调递增）：**
```
14:17:02  M:247582915   (B:73)   接受
14:18:09  M:247587915   (B:110)  接受（AddScene）
14:19:30  M:247587916   (B:73)   接受（RemoveScene，+1）
```

**14:20:09 之后的 groupcast 又被丢**：因为源端口从 56225 变成 36845 = **另一个 chip-tool 进程**，counter 落后于 247587916 → err c4。说明这次 interactive 没全程一个进程（中途切了进程）。

---

## 4. 最终结论

### DUT 没问题
- groupcast AddScene：counter 单调时正常存储（fabric=1，SerializeAdd/SetSceneTableEntry/UpdateFabricSceneInfo 全 err=0）。
- groupcast RemoveScene：counter 单调时正常删除（GetSceneTableEntry err=0 → RemoveSceneTableEntry err=0）。
- groupcast 的 `GetAccessingFabricIndex()` 返回有效 fabric（=1），无需额外解析。
- `RemoveEntry`（FabricTableImpl.ipp:431）行为正确，DeepSeek 的改法是错的。
- 删除后 ViewScene 返回 0x8b → **6e/6i 在 counter 单调时 PASS**。

### 6e/6i 失败根因 = group message counter（harness 问题）
- chip-tool 每个进程独立 group counter，不持久化、不共享。
- 多进程跑 groupcast，后发的 counter 落到 device 已记录的 max 之下 → 被 TrustFirst（spec 4.7.3）当 duplicate 丢弃（err c4），**根本没到 HandleRemoveScene**。
- DUT 行为**符合 spec**，无需修改。

### 之前所有怀疑全部排除
| 怀疑 | 结论 |
|---|---|
| groupcast AddScene 逻辑 bug | ❌ 排除（counter 单调时成功） |
| groupcast RemoveScene 逻辑 bug | ❌ 排除（counter 单调时成功） |
| RemoveScene 没真删 / NVM3 bug | ❌ 排除（RemoveSceneTableEntry err=0，删除后 ViewScene NotFound） |
| FabricTableImpl RemoveEntry bug | ❌ 排除（行为正确，DeepSeek 改法错） |
| EFS 处理 ReturnOnFailure | ❌ 仅 ColorControl 0x4002 不支持时触发，认证不用 0x4002 |
| fabric index 解析 | ❌ groupcast fabric 有效，无需解析 |
| NVM3 写入未生效 | ❌ 排除 |

---

## 5. 关键代码位置

| 文件 | 位置 | 说明 |
|---|---|---|
| `scenes-server.cpp` | `AddSceneParse` / `HandleRemoveScene` | scene 命令处理（已加 log） |
| `SceneHandlerImpl.cpp:134` | `ValidateAttributePath` | EFS 属性校验，不支持返回 UnsupportedAttribute |
| `color-control-server.cpp:42` | `DefaultColorControlSceneHandler` | ColorControl scene handler，9 个 scenable 属性 |
| `color-control-cluster.xml:633` | attr 0x4002 ColorLoopActive | int8u，需 ColorLoop feature |
| `FabricTableImpl.ipp:431` | `RemoveEntry` | DeepSeek 错误改法的目标，实际行为正确 |
| `SessionManager.cpp:1176-1204` | group 消息 counter 校验 | `VerifyOrTrustFirstGroup` |
| `PeerMessageCounter.h:111` | `VerifyOrTrustFirstGroup` | NotSynced→信任；Synced→VerifyGroup（拒 back-track） |
| `Test_TC_S_2_3.yaml` | step 6a/6d/6e/6i | 认证用例定义 |

代码路径均在 `c:\Users\huide\.silabs\slt\installs\conan\p\matte8bada656e9e76\p\third_party\matter_sdk\src\` 下。

---

## 6. 解决办法

### 6.1 DUT 侧：不用改
scene 逻辑、EFS、fabric、RemoveEntry 全部正确。**之前加的 `eric,` 调试 log 在 cert 提交前务必删掉**（恢复 `scenes-server.cpp`、`FabricTableImpl.ipp` 干净版本）。

### 6.2 本地验证：所有 groupcast 命令放同一个 chip-tool interactive 进程
```bash
# 先 setup group（unicast，可分开跑）
chip-tool groupkeymanagement key-set-write '{"groupKeySetID":417,"groupKeySecurityPolicy":0,"epochKey0":"a0a1a2a3a4a5a6a7a8a9aaabacadaeaf","epochStartTime0":1110000,"epochKey1":"b0b1b2b3b4b5b6b7b8b9babbbcbdbebf","epochStartTime1":1110001,"epochKey2":"c0c1c2c3c4c5c6c7c8c9cacbcccdcecf","epochStartTime2":1110002}' <nodeid> 0
chip-tool groupkeymanagement write group-key-map '[{"fabricIndex":1,"groupId":257,"groupKeySetID":417}]' <nodeid> 0
chip-tool groups add-group 257 "Group1" <nodeid> 3

# groupcast 测试 —— 必须一个 interactive 进程，counter 单调
chip-tool interactive start
# 进去后依次（去掉 ./chip-tool 前缀）：
# scenesmanagement add-scene 0x0101 0x03 1000 "scene name" '[{"clusterID":"0x0008","attributeValueList":[{"attributeID":"0x0000","valueUnsigned8":"0x64"}]}]' 0xffffffffffff0101 3
# scenesmanagement view-scene 0x0101 0x03 <nodeid> 3
# scenesmanagement remove-scene 0x0101 0x03 0xffffffffffff0101 3
# scenesmanagement view-scene 0x0101 0x03 <nodeid> 3
```
> groupcast 目的地用 `0xffffffffffff0101`（=group 0x0101）；unicast 用 node-id。
> EFS 用 LevelControl(0x0008) 或 OnOff(0x0006)，跟认证 YAML 一致；别用 ColorControl 0x4002。
> **重点**：6a/6c/6d/6f/6h 所有 groupcast 必须在同一个 interactive 会话里跑，中途不能退出再开新进程。
> /tmp 权限报错：docker 以 root 建了 `/tmp/chip_tool_kvs`，host 非 root 写不了。`sudo rm -f /tmp/chip_*` 清掉再以普通用户跑，或统一用 `sudo`。

### 6.3 认证实验室
- 他们报 6e/6i fail，大概率也是 chip-tool 分进程跑（SemiAutomated）导致 group counter 丢包。
- 让他们用**单进程 automated harness**（Python test runner，一个 controller 跑全程）重跑 TC-S-2.3。
- 如果他们坚持说已是单进程还失败：让他们提供 device 侧 log，确认 groupcast RemoveScene 有没有到 `HandleRemoveScene`。根据本地 log，到了就一定成功。

---

## 7. 复现 / 验证 checklist

- [ ] DUT 工厂复位，重新 commission
- [ ] 跑 step 0a/0b/0c/1a/1b/1c/1d/1e（group key + AddGroup + ACL + RemoveAllScenes）
- [ ] 跑 step 2（unicast AddScene scene 1）→ status 0
- [ ] 进 `chip-tool interactive`，**后续所有 groupcast 都在里面跑**
- [ ] step 6a groupcast AddScene scene 3（OnOff+LevelControl EFS）→ device log 应见 `eric,AddSceneParse: SUCCESS`
- [ ] step 6b unicast ViewScene scene 3 → status 0
- [ ] step 6d groupcast RemoveScene scene 3 → device log 应见 `eric,RemoveScene: SUCCESS`
- [ ] step 6e unicast ViewScene scene 3 → **status 0x8b (139)** ← 6e PASS
- [ ] step 6f/6g/6h/6i 同理，6i 也应 0x8b
- [ ] 验证通过后，删掉 `eric,` 调试 log，重新编译，准备 cert 提交

---

## 8. 附：err c4 含义

`Message counter verify failed, err = c4` —— group 消息 counter 校验失败。`VerifyOrTrustFirstGroup` 在 Synced 状态下对 back-track/duplicate counter 返回错误（DUPLICATE_MESSAGE_RECEIVED 类），device 直接丢弃该 groupcast（spec 4.7.3）。**不是 DUT bug，是 sender counter 非单调。**

---

## 9. 关键 log 证据索引

| log 文件 | 关键内容 |
|---|---|
| `20260706_114822.txt` | 第一轮：groupcast AddScene SUCCESS，但后续 groupcast 被 counter 丢（err c4） |
| `20260706_141409.txt` | 第二轮（interactive）：groupcast AddScene + RemoveScene 全 SUCCESS，删除后 ViewScene B:74 (NotFound)；counter 单调（247582915→247587915→247587916） |
| `log-device.txt` / `log-chip-tool.txt` | 最早一轮：groupcast AddScene 用 ColorControl 0x4002 失败（EFS 校验），ViewScene 查错 scene |
