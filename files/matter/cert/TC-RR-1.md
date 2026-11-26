# TC-RR-1.1

## 问题

TC-RR-1.1 验证的是 **"Minimal Resource Requirements for Matter Node"**——设备配置的资源下限是否满足规范要求。

### 失败现象

```c
// 测试在 step 15 (Add Group to endpoints) 时报 ResourceExhausted
Test test_TC_RR_1_1 failed for the following reason:
Details=<Status.Success: 0> != 137, Extras=None

// Matter Interaction Model 状态码定义
// src/protocols/interaction_model/StatusCodeList.h
CHIP_IM_STATUS_CODE(ResourceExhausted, RESOURCE_EXHAUSTED, 0x89)  // 0x89 = 137
```

DUT 在处理 Write GroupKeyMap / Add Group 时返回 `RESOURCE_EXHAUSTED (0x89)`，表明 **KVS 存储空间或 Group 端点配额耗尽**。

### KVS 消耗分析（6 个 Fabric：5 test + 1 THTF）

```
GroupKeyMap (step 14):    5 × 20 = 100
Groups + Endpoints (step 15): 100 × 2 = 200 (加到第99个group = 198)
Keysets (step 13):        5 × 3 = 15
FabricGroups metadata:    6
GroupFabricList:          1
──────────────────────────────
Group 小计:              ~320
Fabric certs/keys (6 fabrics): ~42
ACL (6 fabrics × 4):          24
UserLabel + 其他属性:          ~30
──────────────────────────────
总计:                    ~416+
```

KVS 写入值约为 **416 条**，远超原有 NVM3 40KB 空间能承载的上限。

### 端点与 Groups 关系

| Endpoint | Type | Groups 需求 |
|----------|------|-------------|
| 1 | MA-extendedcolorlight | ✓ 必须 |
| 2 | MA-dimmablelight | ✓ 必须 |
| 3 | MA-dimmablelight | ✓ 必须 |
| 4 | MA-onoffpluginunit | ✓ 必须 |
| 5 | MA-onoffpluginunit | ✓ 必须 |

规范要求每个 Fabric 下，每个支持 Groups 的 endpoint 需要支持**至少 4 个 Group**（即 `endpoint_count × 4 = 5 × 4 = 20` 个 Group 每 Fabric）。

原有 `CHIP_CONFIG_MAX_GROUP_ENDPOINTS_PER_FABRIC = 3`，只允许 3 个 endpoint 存储 Group 数据，无法覆盖 5 个 endpoint。

## 修改内容

### 1. 增大 Groups 端点上限 — CHIPProjectConfig.h

**文件**: `include/CHIPProjectConfig.h`

```diff
- #define CHIP_CONFIG_MAX_GROUP_ENDPOINTS_PER_FABRIC 3
+ #define CHIP_CONFIG_MAX_GROUP_ENDPOINTS_PER_FABRIC 5
```

**原因**: 5 个 endpoint 需要 Groups 支持，`3 < 5` 不满足规范。改为 5 刚好覆盖。

### 2. 移除 Window Covering 端点的 Groups 集群 — window-app.zap

**文件**: `config/common/window-app.zap`

Window Covering 端点（EP1/2）的 Groups 集群设为 `enabled: 0`（禁用）。

**原因**: Matter 规范中 Window Covering 设备类型的 Groups 集群为 Optional。移除后 Groups 端点从 7 降到 5，与配置值匹配。

### 3. 增大 NVM3 存储空间 — nvm3_default_config.h + slcp

**文件**: `config/nvm3_default_config.h` + `aok02_matter_ac.slcp`

```diff
- #define NVM3_DEFAULT_NVM_SIZE  40960
+ #define NVM3_DEFAULT_NVM_SIZE  57344
```

**原因**: 6 个 Fabric 下 KVS 数据量约 416+ 条，40KB 空间不足导致 `RESOURCE_EXHAUSTED`。增大到 56KB 提供足够余量。

## 修改文件清单

| 文件 | 改动 | 说明 |
|------|------|------|
| `include/CHIPProjectConfig.h` | `3 → 5` | 每 Fabric 最大 Group 端点数 |
| `config/common/window-app.zap` | Groups 禁用 | EP1/2 移除 Groups 集群 |
| `config/nvm3_default_config.h` | `40960 → 57344` | NVM3 存储空间大小 |
| `aok02_matter_ac.slcp` | `40960 → 57344` | SLC 项目配置同步 |

## 关键设计决策

| 项目 | 决策 |
|------|------|
| Group 端点 | 5 个：EP1~5（全部为 Lights/Plugins 类型） |
| EP1/2 Window Covering Groups | 移除，规范中为 Optional |
| NVM3 空间 | 56KB，容纳 6 Fabric × 416+ KVS key |
| 根因 | `CHIP_CONFIG_MAX_GROUP_ENDPOINTS_PER_FABRIC` 过小 → Groups 配额不够，要加大 → KVS 满 → ResourceExhausted |
