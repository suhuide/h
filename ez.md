<!-- vscode-markdown-toc -->
* 1. [Code](#Code)
* 2. [Sign](#Sign)
* 3. [Flash](#Flash)
* 4. [Debug](#Debug)
* 5. [Track](#Track)
	* 5.1. [ Init](#Init)
	* 5.2. [ Switch](#Switch)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

[hrf](hrf.md)  
[blink-test-code](./files/ez/blink-test-code.md)  

## 0. Serial Port
```c
//VCom,PA7-TX,PA8-RX
Baudrate:961200
```

##  1. <a name='Code'></a>Code
```c
git clone git@hoperf-matter:matter/customerproject/ez01_matter.git
```

##  2. <a name='Sign'></a>Sign
```c
cd C:\Si\ws\ez01_matter
python gen_ota.py
```
```c
PS C:\Si\ws\ez01_matter> cd "GNU ARM v12.2.1 - Default"
PS C:\Si\ws\ez01_matter\GNU ARM v12.2.1 - Default> ls
-a----          2026/1/4     16:11        2765722 ez01_matter-46b1d014.s37
-a----          2026/1/4     16:19        2765924 ez01_matter-signed-4c94a90f.s37
-a----          2026/1/4     16:19         568008 ez01_matter-signed.gbl
-a----          2026/1/4     16:19         568090 ez01_matter_0x1470_0xFF01-v0.0.12-signed-7457cdcb.ota
-a----          2026/1/4     16:08          16392 makefile
-a----          2026/1/4     16:08           2108 objects.mk
-a----          2026/1/4     16:08          10642 sources.mk
```
##  3. <a name='Flash'></a>Flash
```c
cd C:\Si\ws\ez01_matter\se_key\
```
Run unlock_se.bat first then do the programming.  
Flash the signed .s37
```c
ez01_matter-signed-4c94a90f.s37
```

##  4. <a name='Debug'></a>Debug
```c
LOG_MSG_INFO(TAG_LIT, "operation completed, output CW: %u WW: %u", c_temp, w_temp);
```
##  5. <a name='Track'></a>Track
###  5.1. <a name='Init'></a> Init
```c
CHIP_ERROR AppTask::Init()-AppTask.cpp
    app_light_mgr_init()-app_light_mgr.cpp
```
###  5.2. <a name='Switch'></a> Switch
```c
//C:\Si\ws\ez01_matter\src\app\AppTask.cpp
void AppTask::PdEventHandler(AppEvent * aEvent)
{
     static uint32_t low_count = 0;
     static uint32_t event_count = 0;
     static uint32_t high_count = 0;
     static uint8_t release_flag = 0;
     static uint8_t timeout_flag = 0;
     uint8_t cur_onoff = 0;
     event_count++;
     if(event_count >= 320 && release_flag == 1 && 0 == timeout_flag) {
         event_count = 0;
         timeout_flag = 1;
         _light_onoff_event_handler();//大于4s状态翻转
     }
}
```

## GPIO(PWM)
```c
#include "sl_gpio.h"
sl_gpio_t gpio;
gpio.port = SL_GPIO_PORT_A;
gpio.pin  = 5;
sl_gpio_set_pin_mode(&gpio, SL_GPIO_MODE_PUSH_PULL, 0);
gpio.port = SL_GPIO_PORT_A;
gpio.pin  = 6;
sl_gpio_set_pin_mode(&gpio, SL_GPIO_MODE_PUSH_PULL, 0);
```
## Part No.
```c
EFR32MG24A420F1536IM40
```

## QR
[1号:MT:K2CA0WSC00UOGZ72M10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0WSC00UOGZ72M10)  
[2号:MT:K2CA0YDG150LSN6MC10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0YDG150LSN6MC10)  
[3号:MT:K2CA0AFT02KQ194RJ10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0AFT02KQ194RJ10)  
[4号:MT:K2CA04QO161KD754L10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA04QO161KD754L10)  
[4号:MT:6FCJ142C00KA0648G00](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A6FCJ142C00KA0648G00)  
[5号:MT:K2CA0C0X17IIIZ3MY10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0C0X17IIIZ3MY10)  

## Customer Report Issue
1、PWM信号频率改为16KHZ  
2、最低占空比1%分辨率降低一半  
3、断电时来电记忆亮灯爆闪  
4、最小亮度时APP开灯和关断没有缓冲  

## Fade in&out
```c
static app_event_t slsd_timer_event;           // 缓起缓灭定时器
_slsd_timer_event_handler
ev_set_delay_ms(ev, SLSD_STEP_TIME_MS); // next
```
```c
void fade_cold_on(void) {
      cold_onoff = 1;
      ev_set_delay_ms(&test_run_event, 50);
}

void fade_cold_off(void) {
      cold_onoff = 0;
      ev_set_delay_ms(&test_run_event, 50);
}
```
## Remote
### Funcution Location
```c
C:\Si\ws\ez01_matter\src\app\app_rc_mgr.cpp
app_rc_mgr_init()
_process_rc_key_onoff()
_rc_data_notify_app_handler()
C:\Si\ws\ez01_matter\src\app\rc_protocol.cpp
rc_protocol_init()
_rc_protocol_data_decode()
```
### Relationship
```c
AppTask::Init()
    app_rc_mgr_init()
        rc_protocol_init(_rc_data_notify_callback)
            _rc_data_notify_app_handler()
                _process_rc_key_onoff()
                    cluster_api_onoff_server_set_onoff_value()

```
```c
rc_protocol_init()
    hal_rc_init(_rc_protocol_data_decode)
        _rc_protocol_data_decode()
    gpio_communicate_protocol_mainloop()
        _rc_notify_cb(remote_control_id, code)
            _rc_data_notify_callback()
                _rc_data_notify_app_handler()
```



## Bug
[Remote-turn-off](files/ez/Remote-turn-off.md)  
[blink](files/ez/blink.md)  
[blink2](files/ez/blink2.md)  

Blink at 
```c
[00:00:00.453][silabs ][LIT] INFO: target_brightness: 33, step_brightness:1
[00:00:00.453][silabs ][LIT] INFO: ColorTemp: 48500 Level: 33-28, output CW: 19 WW: 8
[00:00:00.458][silabs ][LIT] INFO: operation completed, output CW: 19 WW: 8
```
```c
typedef struct {
    uint32_t brightness;
    uint32_t pwm;

} slsd_model_entry_t;
```
```c
_slsd_timer_event_handler
    curve_brightness = calculate_curve_pwm(cur_brightness, slsd_entry_5s, sizeof(slsd_entry_5s) / sizeof(slsd_model_entry_t));

开始
  ↓
进入原子操作区（关中断）
  ↓
更新亮度/色温状态
  ↓
计算PWM输出值
  ↓
退出原子操作区（开中断）
  ↓
是否需要快速切换？ → 是 → 跳回next_sw（重新计算）
  ↓ 否
设置PWM输出
  ↓
检查是否完成渐变
  ↓
  是 → 执行完成回调/关闭灯光
  ↓
  否 → 设置下一次定时器触发
```    
```c
calulate_exp_table()
calulate_exp_table_warm()
calulate_exp_table_cold()
```
### 2KHz FW
```c
ez01_matter/release-fw/signfw/v0.0.12/ez01_matter-signed--V0.0.12-2-4e9ec2c3.s37
```
This FW, brightness < 20%, it also blink. Compare with the 16KHz FW(<50%), it shoud be better.  

## Reference
### Jiabo Info
需求可以总结为:
 - 双色温灯(CW+WW)，现在PWM查表递增，CW和WW都是指数分布,但从0到最小亮度(wW=8,CW=19)在视觉上不是同步渐变，而是存在WW先亮、CW随后才亮的先后感-体验不好
 - 希望代码"优化"，让视觉上Ww和CW渐变感觉更平滑，更"同步"
一、为什么会有渐变不同步的现象
1. 查表步数、起点不同
    - WW和CW分别用自己的查表，不等长/跨度不同(wW8步到8，CW20步到19)，且每步PWM增量不一致  
    - 程序for循环同步递增时，WW一下就到最小亮度，CW还在低级游荡-人眼感受到Ww先亮，Cw后亮  
2. "先后渐变"根本原因:
    - 没有做到在同一总渐变步长上，"两路曲线数值输出都同步走完整条渐变表"
    - 每次输出都是(cw_table[i],ww_table[i])，但i的终点不同，导致有一路提前到最大，后一路还在爬坡  
二、核心优化原理
办法A:拉步数&对输出(强烈推荐)
- 让Ww和CW的查表表长相同(长度取两者最大，例如20)
    - 短表用线性插值、末值补齐等方式补全
- 循环次数和i统一，每步都能输出CW/WW一个成对的PWM
- 效果:从0到亮，两个灯珠从头到尾共进退一视觉渐亮同步

## Commander CLI
```c
C:\SiliconLabs\SimplicityStudio\v5>commander security unlock --command-key command_key.pem --unlock-param 1111 --device EFR32MG24A410F1536IM40 -s 602712820
Unlocking with unlock payload:
C:/Users/Administrator/AppData/Local/SiliconLabs/commander/SecurityStore/device_0000000000000000d44867fffe8997ee/challenge_e4e3184d31be0e7428a6d0367269b5f7/unlock_payload_0000000000111110.bin
Secure debug successfully unlocked
DONE
```
```c
commander flash ez01_matter-signed--v0.0.13-2d274330.s37 --device efr32mg24 --no-reset
```
```c
C:\Si\ws\ez01_matter\release-fw\signfw\v0.0.13>commander security status --device efr32mg24
WARNING: DP write failed
DCI communication failed, retrying after reset and 10 ms delay...
Resetting device...
SE Firmware version   : 2.2.5
Serial number         : 0000000000000000d44867fffe8b63ab
Debug lock            : Enabled
Device erase          : Enabled
Secure debug unlock   : Enabled
Tamper status         : OK
Secure boot           : Enabled
Boot status           : 0x20 - OK
Command key installed : True
Sign key installed    : True
DONE
```
## Timer Priority
```c
C:\Si\SDKs\simplicity_sdk_v2025.6.2\extension\matter_extension\third_party\matter_sdk\examples\platform\silabs\BaseApplication.cpp
constexpr osThreadAttr_t appTaskAttr = { .name       = APP_TASK_NAME,
                                         .attr_bits  = osThreadDetached,
                                         .cb_mem     = &appTaskControlBlock,
                                         .cb_size    = osThreadCbSize,
                                         .stack_mem  = appStack,
                                         .stack_size = APP_TASK_STACK_SIZE,
                                         .priority   = osPriorityNormal };

```