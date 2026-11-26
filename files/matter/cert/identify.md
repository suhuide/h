# TC-I-2 Identify Cluster 修改总结

## 问题

MCU 端的 Identify 集群回调走了 SDK `BaseApplication` 的 `OnIdentifyStart`/`OnIdentifyStop`/`OnTriggerIdentifyEffect`，而没有走应用层 `app_identify_mgr` 的实现。原因：

1. SDK 的 `emberAfIdentifyClusterInitCallback` (BaseApplication.cpp) 通过 `IdentifyPool.CreateObject` 注册了 `BaseApplication::OnIdentify*` 静态回调
2. 应用层 `app_identify_mgr_create_with_endpoint` 通过 `std::make_unique<Identify>` 创建了另一套 `Identify` 对象
3. 两套对象都注册到同一个全局链表 `firstLegacyIdentify`，SDK 注册在先，应用层在后
4. `GetLegacyIdentifyInstance` 遍历链表返回第一个匹配的，具体走哪套取决于注册顺序
5. 应用层的 `app_identify_mgr_set_time` 也是死代码——完全没人调用

## 修改内容

### 1. SDK 修改（1 行） — BaseApplication.cpp

**文件**: `third_party/matter_sdk/examples/platform/silabs/BaseApplication.cpp:827`

```cpp
// 加 __attribute__((weak))，允许应用层覆盖
__attribute__((weak)) void emberAfIdentifyClusterInitCallback(chip::EndpointId endpoint)
{
    IdentifyPool.CreateObject(endpoint, BaseApplication::OnIdentifyStart, BaseApplication::OnIdentifyStop,
                              Clusters::Identify::IdentifyTypeEnum::kVisibleIndicator, BaseApplication::OnTriggerIdentifyEffect);
}
```

### 2. 应用层修改 — app_identify_mgr.cpp

**文件**: `common/app/app_identify_mgr.cpp`

#### 2.1 覆盖 SDK 回调（阻止 IdentifyPool 重复注册）
```cpp
void emberAfIdentifyClusterInitCallback(chip::EndpointId endpoint)
{
    (void) endpoint;  // No-op: Identify 对象由 app_identify_mgr_create_with_endpoint 统一管理
}
```

#### 2.2 OnIdentifyStart — 开始闪灯
```cpp
static void OnIdentifyStart(Identify * identify)
{
    uint16_t ep = identify->mCluster.Cluster().GetPaths()[0].mEndpointId;
    uint16_t identifyTime = identify->mCluster.Cluster().GetIdentifyTime();
    if (_is_light_endpoint(ep)) {
        _onoff_blink(identifyTime, ep);
    }
}
```

#### 2.3 OnIdentifyStop — 停止闪灯
```cpp
static void OnIdentifyStop(Identify * identify)
{
    idf_test_count = 0;
}
```

#### 2.4 OnTriggerIdentifyEffect — 触发热门效果（按端点过滤）
```cpp
static void OnTriggerIdentifyEffect(Identify * identify)
{
    uint16_t ep = identify->mCluster.Cluster().GetPaths()[0].mEndpointId;
    if (!_is_light_endpoint(ep)) return;
    switch (identify->mCurrentEffectIdentifier) {
        case kBlink/kOkay/kBreathe/kChannelChange: _onoff_blink(5, ep); break;
        case kFinishEffect:  _onoff_blink(3, ep); break;
        case kStopEffect:    _onoff_blink(1, ep); break;
    }
}
```

#### 2.5 send_cmd_to_onoff_light — 按端点精准控制对应的灯
```cpp
static uint8_t idf_active_ep = 0;

static void send_cmd_to_onoff_light(bool onoff)
{
    BaseDev * dev = BaseDev::find_dev_by_endpoint(idf_active_ep);
    if (dev != nullptr && dev->m_dev_type == kBaseDevLight) {
        uint8_t dev_index = dev->m_dev_index;
        // 只往该端点对应的灯发送命令
        app_comm_send_ctrl_cmd(fLightSwitch, payload, 1);
    }
}
```

#### 2.6 _onoff_blink — 记录当前端点
```cpp
static void _onoff_blink(int count, uint8_t endpoint)
{
    idf_active_ep  = endpoint;
    idf_test_count = count * 2;
    ev_set_active(&onoff_event);
}
```

#### 2.7 删除死代码
删除 `app_identify_mgr_set_time`（无声明无调用）。

### 3. 端点-灯映射识别

```cpp
static bool _is_light_endpoint(uint8_t endpoint)
{
    return (endpoint >= 3 && endpoint <= 5);
}
```
- EP3 = RGB Light (Extended Color Light 0x010D)
- EP4 = White Light #1 (Dimmable Light 0x0101)
- EP5 = White Light #2 (Dimmable Light 0x0101)
- EP1/2 = Window Covering — Identify 仅打 log，不控制灯
- EP6/7 = Plugin — Identify 仅打 log，不控制灯

灯端点创建 `IdentifyTypeEnum::kVisibleIndicator`，非灯端点创建 `IdentifyTypeEnum::kNone`。

## 调用链

```
chip-tool identify identify <time> <node-id> <endpoint>
  → IdentifyCluster::InvokeCommand
    → SetIdentifyTime
      → IdentifyLegacyDelegate::OnIdentifyStart
        → GetLegacyIdentifyInstance(endpoint)  // 找到唯一一份 Identify 对象
          → app_identify_mgr::OnIdentifyStart
            → _onoff_blink(identifyTime, ep)
              → idf_active_ep = ep
              → 定时器 500ms 间隔
                → send_cmd_to_onoff_light  // 只控该 ep 的灯
```

## 关键设计决策

| 项目 | 决策 |
|------|------|
| Identify 对象管理 | app_identify_mgr 统一管理，IdentifyPool 不再创建 |
| 灯控粒度 | 按 endpoint 精准控制，Identify EP3 只闪 EP3 的灯 |
| 非灯端点 | Identify 命令正常响应但不触发灯操作 |
| SDK 侵入 | 最小化 —— 仅 1 行 `__attribute__((weak))` |
