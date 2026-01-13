## Log
```c
[15:08:12.440]收←◆[00:01:42.787][silabs ][LIT] INFO: operation completed, output CW: 0 WW: 175

[15:08:15.132]收←◆[00:01:45.477][silabs ][RCT] INFO: CODE=07
[00:01:45.477][silabs ][RCT] INFO: CT 155, STEP 55
[00:01:45.478][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=155 current_level=51
[00:01:45.478][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:45.478][silabs ][LIT] INFO: CT 10000->15500(28) BR 502->502(1)

[15:08:15.288]收←◆[00:01:45.633][silabs ][RCT] INFO: CODE=07
[00:01:45.633][silabs ][RCT] INFO: CT 210, STEP 55
[00:01:45.634][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=210 current_level=51
[00:01:45.634][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:45.634][silabs ][LIT] INFO: CT 10812->21000(51) BR 502->502(1)

[15:08:15.453]收←◆[00:01:45.799][silabs ][RCT] INFO: CODE=07
[00:01:45.799][silabs ][RCT] INFO: CT 265, STEP 55
[00:01:45.800][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=265 current_level=51
[00:01:45.800][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:45.800][silabs ][LIT] INFO: CT 12342->26500(71) BR 502->502(1)

[15:08:15.611]收←◆[00:01:45.956][silabs ][RCT] INFO: CODE=07
[00:01:45.956][silabs ][RCT] INFO: CT 320, STEP 55
[00:01:45.957][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=320 current_level=51
[00:01:45.957][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:45.957][silabs ][LIT] INFO: CT 14401->32000(88) BR 502->502(1)

[15:08:15.776]收←◆[00:01:46.122][silabs ][RCT] INFO: CODE=07
[00:01:46.122][silabs ][RCT] INFO: CT 375, STEP 55
[00:01:46.123][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=375 current_level=51
[00:01:46.123][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:46.123][silabs ][LIT] INFO: CT 17129->37500(102) BR 502->502(1)

[15:08:15.933]收←◆[00:01:46.278][silabs ][RCT] INFO: CODE=07
[00:01:46.278][silabs ][RCT] INFO: CT 430, STEP 55
[00:01:46.279][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=430 current_level=51
[00:01:46.279][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:46.279][silabs ][LIT] INFO: CT 20087->43000(115) BR 502->502(1)

[15:08:16.089]收←◆[00:01:46.434][silabs ][RCT] INFO: CODE=07
[00:01:46.434][silabs ][RCT] INFO: CT 485, STEP 55
[00:01:46.435][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=485 current_level=51
[00:01:46.435][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
[00:01:46.435][silabs ][LIT] INFO: CT 23307->48500(126) BR 502->502(1)
```
## 1
```c
gpio_communicate_protocol_mainloop()
        LOG_MSG_INFO(TAG_RCT, "CODE=%02x", code)
        _rc_notify_cb(remote_control_id, code)
```
```c
[15:08:15.132]收←◆[00:01:45.477][silabs ][RCT] INFO: CODE=07
```
## 2
```c
_process_rc_key_move_ct()
    if (key == RC_KEY_CT_DEC) {
        _INC_VALUE(cur_ct, step_ct, max_ct);
    } else {
        _DEC_VALUE(cur_ct, step_ct, min_ct);
    }
    LOG_MSG_INFO(TAG_RCT, "CT %u, STEP %u", cur_ct, step_ct);
```
```c
[00:01:45.477][silabs ][RCT] INFO: CT 155, STEP 55
```
## 3
```c
cluster_api_color_control_color_temperature_mireds_set()
    MatterPostAttributeChangeCallback()
        case ColorControl::Id:
            LOG_MSG_INFO(TAG_CLS, "Callback: ColorControl ColorTemperature=%u current_level=%u", cur_ct, current_level)
            app_light_mgr_move_cw_with_time(((uint32_t) cur_ct) * LIGHT_COLOR_TEMP_SCALE, current_level,
                                                SLSD_MOVING_TRANSITION_TIME_MS)
```
```c
[00:01:45.478][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=155 current_level=51
```
## 4
```c
app_light_mgr_move_cw_with_time()
    LOG_MSG_INFO(TAG_LIT, "jiabo target_brightness:%d brightness %u", target_brightness, brightness);
```
```c
[00:01:45.478][silabs ][LIT] INFO: jiabo target_brightness:502 brightness 51
```
## 5
```c
app_light_mgr_move_cw_with_time()
    LOG_MSG_INFO(TAG_LIT, "CT %d->%d(%d) BR %d->%d(%d)", cur_colortemp, target_colortemp, step_colortemp, cur_brightness,
                 target_brightness, step_brightness)
```
```c
[00:01:45.478][silabs ][LIT] INFO: CT 10000->15500(28) BR 502->502(1)
```

## Power on/off
```c
_slsd_timer_event_handler()
    LOG_MSG_INFO(TAG_LIT, "target_brightness: %u, step_brightness:%u", target_brightness, step_brightness);
    LOG_MSG_INFO(TAG_LIT, "ColorTemp: %u Level: %u-%u, output CW: %u WW: %u", cur_colortemp, cur_brightness, curve_brightness,
                    c_temp, w_temp);
    _light_ll_set_level()
```