# TC-WNCV Window Covering 修改总结

## 问题

TC-WNCV-3.1 / 3.2 / 3.3 / 4.5 的 step 3a 均失败：电机正在运动，但读取 `OperationalStatus` 属性值为 0（Not Moving），测试期望值为运动状态（如 5 = Lift Opening）。

```
Test Failure: The response value "0" is not a value from [5, 17, 21].
```

## 根因

`OperationalStatus` 只在 MCU 主动回报电机状态时才更新（`dev_curtain_ctrl_report_process` → `SetOperationalStatus()`），存在延迟。Matter 命令发出后 ~2 秒测试即读取 `OperationalStatus`，此时 MCU 尚未回报，属性仍为旧值 0。

调用链（修复前）：
```
Matter UpOrOpen/DownOrClose/GoToLiftValue
  → SDK 更新 TargetPositionLiftPercent100ths
    → AttributeChangedEventHandler → 发 fCurtainPercentCtrl 给 MCU
    → MCU 启动电机 → MCU 回报状态
      → dev_curtain_ctrl_report_process → SetOperationalStatus()  ← 太晚！
  
测试 step 3a (~2s 后) → 读 OperationalStatus → 0 ✗
```

## 修改内容

### 文件: `common/app/app_wdc_mgr.cpp`

#### 1. AttributeChangedEventHandler — TargetPositionLiftPercent100ths 变化时立即设 OperationalStatus

在发出 MCU 命令**之前**，根据 target vs current 判断运动方向并更新 OperationalStatus：

```cpp
case Attributes::TargetPositionLiftPercent100ths::Id:
{
    uint16_t percent = *reinterpret_cast<uint16_t *>(value);
    ...
    // 立即更新 OperationalStatus，不等 MCU 回读
    {
        app::DataModel::Nullable<Percent100ths> cur;
        PlatformMgr().LockChipStack();
        matter_attr_lock();
        Attributes::CurrentPositionLiftPercent100ths::Get(m_ep, cur);
        matter_attr_unlock();
        PlatformMgr().UnlockChipStack();
        wdc_ctrl_cmd_t dir;
        if (!cur.IsNull() && percent > cur.Value())
            dir = kWdcCtrlClose;  // target > current → 关/降
        else
            dir = kWdcCtrlOpen;   // target < current → 开/升
        SetOperationalStatus(dir);
    }
    // 然后发 MCU 命令
    app_comm_send_ctrl_cmd(fCurtainPercentCtrl, payload, 4);
    break;
}
```

#### 2. HandleStopMotion — 停止时立即设 OperationalStatus = 0

```cpp
CHIP_ERROR AppWdcDev::HandleStopMotion()
{
    // 立即更新 OperationalStatus 为 Stop，不等 MCU 回读
    SetOperationalStatus(kWdcCtrlStop);
    // 然后发 MCU 停止命令
    ...
}
```

## 修改文件清单

| 文件 | 改动 | 说明 |
|------|------|------|
| `common/app/app_wdc_mgr.cpp` | `AttributeChangedEventHandler` 加 OperationalStatus 立即更新 | 运动命令发出时同步设状态 |
| `common/app/app_wdc_mgr.cpp` | `HandleStopMotion` 加 `SetOperationalStatus(kWdcCtrlStop)` | 停止命令发出时同步设状态 |

## 关键设计决策

| 项目 | 决策 |
|------|------|
| 更新时机 | Matter 命令到达时立即更新，不等 MCU 回报 |
| 方向判断 | 比较 target vs current position（target > current → Close，否则 Open） |
| OperationalStatus 值 | Open=5 (kGlobal=1, kLift=1), Close=10 (kGlobal=2, kLift=2), Stop=0 |
| 覆盖范围 | TC-WNCV-3.1/3.2/3.3/4.5 所有涉及 OperationalStatus 读取的 step |
