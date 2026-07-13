# TC-OO-2-4 StartUpOnOff 修改总结

## 问题

TC-OO-2-4 测试设备重启后 StartUpOnOff 行为是否正确。EP6/EP7（Plugin）失败：

| Step | 场景 | 期望 | 实际 | 结果 |
|------|------|------|------|------|
| 4d | StartUpOnOff=1 (On) → 重启 | OnOff=TRUE | OnOff=FALSE | FAIL |
| 5g | StartUpOnOff=2 (Toggle) → 第二次重启 | OnOff=TRUE | OnOff=FALSE | FAIL |
| 6d | StartUpOnOff=NULL → 重启 | OnOff=TRUE | OnOff=FALSE | FAIL |

## 根因

OnOff 属性变更时发硬件命令（`fLightSwitch` / `fHeaterSwitch`）没有设置 `g_loopback` 防回环标志，导致硬件回读的 OnOff 状态覆盖了 Matter 属性中刚设置的正确值。

### 启动时序问题

```
1. Init() -> GetStartUpOnOff() -> 返回正确值 (例如 OnOff=TRUE)
2. -> setOnOffValue(TRUE) -> Matter 属性 OnOff=TRUE
3. -> app_comm_send_ctrl_cmd(fHeaterSwitch, ON) -> 发送硬件命令
4. -> 硬件收到命令，但可能尚未执行完毕
5. -> 硬件上报当前状态（可能仍为 OFF）
6. -> dev_plugin_onff_report_process -> 无 loopback 检查 -> SetOnOff(FALSE)
7. -> Matter 属性 OnOff=FALSE -> 覆盖！
8. DUT 重启后回到 OFF 状态
```

### 防回环对比

| 回读处理函数 | 防回环 (`g_loopback`) | 状态 |
|-------------|----------------------|------|
| `dev_ligth_color_report_process` | 有 | OK |
| `dev_ligth_level_report_process` | 有 | OK |
| `dev_ligth_onff_report_process` | **无** | **缺** |
| `dev_plugin_onff_report_process` | **无** | **缺** |

## 修改内容

### 1. 回读处理加 loopback 检查 -- app_spm_mgr.cpp

`dev_ligth_onff_report_process` 和 `dev_plugin_onff_report_process` 开头加：
```cpp
if (g_loopback) {
    LOG_MSG_INFO(..., "ant loopback, skip\n");
    return;
}
```

### 2. 发硬件命令前设 loopback -- app_colorlight_mgr.cpp

`Init()` 和 `OnOffAttributeChangedEventHandler` 中：
```cpp
app_spm_mgr_light_ant_loopbak();  // 新增
app_comm_send_ctrl_cmd(fLightSwitch, payload, 1);
```

### 3. 发硬件命令前设 loopback -- app_plugin_mgr.cpp

`Init()` 和 `OnOffAttributeChangedEventHandler` 中：
```cpp
app_spm_mgr_light_ant_loopbak();  // 新增
app_comm_send_ctrl_cmd(fHeaterSwitch, payload, 1);
```

## 修改文件清单

| 文件 | 改动 | 说明 |
|------|------|------|
| `common/app/app_spm_mgr.cpp` | +6 行 | `dev_ligth_onff_report_process` / `dev_plugin_onff_report_process` 加 loopback 检查 |
| `common/app/app_colorlight_mgr.cpp` | +2 行 | `Init()` / `OnOffAttributeChangedEventHandler` 设回环标志 |
| `common/app/app_plugin_mgr.cpp` | +2 行 | `Init()` / `OnOffAttributeChangedEventHandler` 设回环标志 |

## 关键设计决策

| 项目 | 决策 |
|------|------|
| 防回环 | 统一使用 `g_loopback` + `ant_loopbak()` 机制，与 color/level 报告一致 |
| 覆盖范围 | Light + Plugin 的 OnOff 路径 |
| 影响面 | 不影响 Init() 和 OnOff 属性变更的正常流程 |
