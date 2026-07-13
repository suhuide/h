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
[reset](./files/ez/reset.md)  
[blink-test-code](./files/ez/blink-test-code.md)  
[Module-QRcode-20260526](./files/ez/Module-20260526.md)  

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
```c
//Use TIMER0 for PWM
static sl_led_pwm_t cold_light = {
    .port     = gpioPortA,
    .pin      = 6,
    .level    = SL_SIMPLE_RGB_PWM_LED_LIGHT_RESOLUTION - 1,
    .polarity = 1,
    .channel  = 1,
#if defined(SL_SIMPLE_RGB_PWM_LED_LIGHT_GREEN_LOC)
    .location = SL_SIMPLE_RGB_PWM_LED_LIGHT_GREEN_LOC,
#endif
    .timer      = TIMER0,
    .frequency  = SL_SIMPLE_RGB_PWM_LED_LIGHT_FREQUENCY * 2,
    .resolution = SL_SIMPLE_RGB_PWM_LED_LIGHT_RESOLUTION,
};

static sl_led_pwm_t warm_light = {
    .port     = gpioPortA,
    .pin      = 5,
    .level    = 0,
    .polarity = 0,
    .channel  = 0,
#if defined(SL_SIMPLE_RGB_PWM_LED_LIGHT_BLUE_LOC)
    .location = SL_SIMPLE_RGB_PWM_LED_LIGHT_BLUE_LOC,
#endif
    .timer      = TIMER0,
    .frequency  = SL_SIMPLE_RGB_PWM_LED_LIGHT_FREQUENCY * 2,
    .resolution = SL_SIMPLE_RGB_PWM_LED_LIGHT_RESOLUTION,
};
```
## Part No.
```c
HPTSB01
```
```c
EFR32MG24A420F1536IM40
```
## HW
Hi7011 VDD 5.8V(-0.3~7.0V)
Hi7011 Pin2 PWM in
Hi7011 Pin5&6 LED Control -

R10 -> Hi7011 pin2  
R16 -> Hi7011 pin2  

## QR
[Default:MT:6FCJ142C00KA0648G00](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A6FCJ142C00KA0648G00)  
[1号:MT:K2CA0WSC00UOGZ72M10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0WSC00UOGZ72M10)  
[2号:MT:K2CA0YDG150LSN6MC10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0YDG150LSN6MC10)  
[3号:MT:K2CA0AFT02KQ194RJ10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA0AFT02KQ194RJ10)  
[4号:MT:K2CA04QO161KD754L10](https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AK2CA04QO161KD754L10)  
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

## Curve
```c
static uint32_t calculate_curve_pwm(uint32_t brightness, const slsd_model_entry_t * model, uint8_t model_entry_count)
{
    uint32_t res = 0;

    if (brightness >= model[0].brightness) {
        // Return with max pwm if brightness is greater than the max brightness in the model.
        res = model[0].pwm;
    } else if (brightness <= model[model_entry_count - 1].brightness) {
        // Return with min pwm if brightness is smaller than the min brightness in the model.
        res = model[model_entry_count - 1].pwm;
    } else {
        uint8_t i;
        // Otherwise find the 2 points in the model where the brightness level fits in between,
        // and do linear interpolation to get the estimated pwm value.
        for (i = 0; i < (model_entry_count - 1); i++) {
            if ((brightness < model[i].brightness) && (brightness >= model[i + 1].brightness)) {
                res = (brightness - model[i + 1].brightness) * (model[i].pwm - model[i + 1].pwm) /
                    (model[i].brightness - model[i + 1].brightness);
                res += model[i + 1].pwm;
                break;
            }
        }
    }

    return res;
}
//model[i+1].brightness（区间下限亮度）
//model[i].brightness（区间上限亮度）
//model[i+1].pwm（区间下限PWM）
//model[i].pwm（区间上限PWM）
```
```c
    curve_brightness = calculate_curve_pwm(cur_brightness, slsd_entry_5s, sizeof(slsd_entry_5s) / sizeof(slsd_model_entry_t));
    c_temp = static_cast<uint16_t>((curve_brightness * (cur_colortemp - min_colortemp)) / (max_colortemp - min_colortemp));
    w_temp = static_cast<uint16_t>((curve_brightness * (max_colortemp - min_colortemp - (cur_colortemp - min_colortemp))) /
                                   (max_colortemp - min_colortemp));
//总亮度 = 冷光亮度 + 暖光亮度 = c_temp + w_temp = curve_brightness
//色温比例计算
cold_ratio = (cur_colortemp - min_colortemp) / (max_colortemp - min_colortemp)
warm_ratio = 1 - cold_ratio
```   
```c
//直接对应两个PWM通道
_light_ll_set_level(c_temp, w_temp);
```                                

## PWM
### Adjust
```c
app_light_mgr_move_cw_with_time()
```
### Not in Matter Net
It does not blink.

<div align="center">
  <img src="files/ez/pwm-no-net.png" width="1080">
</div>

Control by app or press RC, it do blink.

<div align="center">
  <img src="files/ez/pwm-app-operate.png" width="1080">
</div>

### CW
```c
//gpio_communicate_protocol_mainloop()
[11:05:59.411]  [00:07:38.811][silabs ][RCT] INFO: GC_RCV_DATA: RemoteControlID=00000 CODE=07
//_process_rc_key_move_ct()
[11:05:59.412]  [00:07:38.811][silabs ][RCT] INFO: CT 430, STEP 55
//MatterPostAttributeChangeCallback()
[11:05:59.413]  [00:07:38.812][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=430 current_level=77
//app_light_mgr_move_cw_with_time()
[11:05:59.414]  [00:07:38.812][silabs ][LIT] INFO: CT 23126->43000(100) BR 746->746(2)
//_slsd_timer_event_handler()
[11:06:00.519]  [00:07:39.919][silabs ][LIT] INFO: operation completed, output CW: 163 WW: 109

[11:06:24.149]  [00:08:03.547][silabs ][RCT] INFO: GC_RCV_DATA: RemoteControlID=00000 CODE=07
[11:06:24.150]  [00:08:03.547][silabs ][RCT] INFO: CT 485, STEP 55
[11:06:24.150]  [00:08:03.548][silabs ][CLS] INFO: Callback: ColorControl ColorTemperature=485 current_level=77
[11:06:24.151]  [00:08:03.548][silabs ][LIT] INFO: CT 43000->48500(28) BR 746->746(2)
[11:06:25.252]  [00:08:04.652][silabs ][LIT] INFO: operation completed, output CW: 191 WW: 81
```
```mermaid
graph TD
    A[gpio_communicate_protocol_mainloop] --> |then| B[_process_rc_key_move_ct]
	B --> |then| C[MatterPostAttributeChangeCallback]
    C --> |then| D[app_light_mgr_move_cw_with_time]
	D --> |then| E[_slsd_timer_event_handler]
	style A fill:#f9f,stroke:#333,stroke-width:2px
	style B fill:#09f,stroke:#333,stroke-width:2px
	style C fill:#4f0,stroke:#333,stroke-width:2px
	style D fill:#87f,stroke:#333,stroke-width:2px
	style E fill:#9f0,stroke:#333,stroke-width:2px
```

## New Request @20260625
### 需求
PWM频率从16kHz降到5kHz，APP=1%时实际占空比从~0.6%提升到1.5%。  
背景：新硬件方案没有通讯干扰，低频PWM可行；暗端0.6%占空比灯光抖动，提高到1.5%后加电容滤波，最暗亮度依然够低。

### 最终改动（3处）

| 文件 | 改动 | 说明 |
|------|------|------|
| `src/hal/hal_light.h:13` | `SL_SIMPLE_RGB_PWM_LED_LIGHT_FREQUENCY` 16000→5000 | PWM频率5.4kHz |
| `src/app/app_light_mgr.cpp:19` | `SLSD_MIN_PWM_ADJ` = 36（原为公式算出的24） | 映射起点 |
| `src/app/app_light_mgr.cpp:60` | 曲线表插入 `{45, SLSD_MIN_PWM_ADJ}` | 最低亮度锚点 |

`SLSD_MIN_PWM` 保持为 1 不动——关灯 fade-out 路径依赖 `{1,1}` 作为渐变终点。

### PWM硬件配置
- TIMER0, Up/Down 模式（中心对齐PWM）
- 冷光 PA6 (CC1), polarity=1（反相）
- 暖光 PA5 (CC0), polarity=0
- 时钟源: EM01GRPACLK → HFRCODPLL → **78MHz**

### 频率与分辨率的关系
`_pwm_led_init()` (`hal_light.c:207-225`)：

```
top = 78MHz / (FREQ×2) - 1           // 频率→TOP，×2是Up/Down补偿
top = (top / (R-1)) × (R-1)          // 对齐到分辨率的整数倍
若 TOP < R-1 → TOP = R-1             // 分辨率优先
```

| 参数 | 旧 (16kHz) | 新 (5kHz) |
|------|-----------|----------|
| led->frequency | 32000 | 10000 |
| 计算 top | 2436 | 7799 |
| 对齐后 TOP | 2399 (1×2399) | 7197 (3×2399) |
| 实际频率 | 16.25kHz | **5.42kHz** |
| level_increments | 1 | 3 |

### TOP / Resolution / 占空比 三层结构
```
78MHz 时钟
  │
  ▼  TOP = 7197                 ← 硬件寄存器上限（频率决定）
  │
  ▼  level_increments = 7197/2399 = 3    ← 每软件步 = 3个硬件计数
  │
  ▼  Resolution = 2400          ← 软件刻度 0~2399
  │
  ▼  PWM比较值 = software_level × 3      ← hal_light_set_cw():258-261
  │
  ▼  占空比 ≈ software_level / 2400
```

- TOP 由频率决定（5kHz → 7197），是寄存器实际能到的最大值
- Resolution = 2400 是在 TOP 范围内的软件刻度，够用即可
- 代码位置：`hal_light.c:258` `level_increments = TIMER_TopGet() / (RESOLUTION-1)`
- 分辨率不改为 7000+ 的原因：2400 档已超肉眼极限，改大需全部宏和曲线表等比例重算，零实际收益

### 亮度映射链路
```
Matter Level(1~254) → target_brightness → 曲线查表(slsd_entry_5s) → c_temp+w_temp → hal_light_set_cw() → TIMER_CompareBufSet()
```

关键宏（`app_light_mgr.cpp`）：
```c
SLSD_MIN_PWM_ADJ = 36   // 映射起点，原公式 MIN_PWM_PERCENT*R/100=24，改为硬编码36
SLSD_MAX_PWM_ADJ = 2399 // 映射终点（不改）
SLSD_MIN_PWM      = 1   // 最低 clamp 值（不改，关灯路径需要）
```

映射公式：
```c
target_brightness = brightness × (2399-36) / 253 + 36
// Matter level 1→45, 127→1222, 254→2399
// clamp: if < SLSD_MIN_PWM(1) → = 1
```

### 曲线表 slsd_entry_5s[]（13段）
| # | brightness | pwm | 占空比 | 等效γ | Matter Level | 亮度% | 说明 |
|---|-----------|-----|--------|-------|-------------|-------|------|
| 0 | 2399 | 2399 | 100% | — | 253 | 99.6% | 最亮 |
| 1 | 2250 | 1900 | 79.2% | 3.64 | 237 | 93.3% | |
| 2 | 2000 | 1350 | 56.3% | 3.15 | 210 | 82.7% | |
| 3 | 1750 | 1000 | 41.7% | 2.78 | 183 | 72.0% | |
| 4 | 1500 | 750 | 31.3% | 2.47 | 156 | 61.4% | |
| 5 | 1250 | 550 | 22.9% | 2.26 | 130 | 51.2% | |
| 6 | 1000 | 400 | 16.7% | 2.05 | 103 | 40.6% | |
| 7 | 750 | 275 | 11.5% | 1.86 | 76 | 29.9% | |
| 8 | 500 | 175 | 7.3% | 1.67 | 50 | 19.7% | |
| 9 | 250 | 100 | 4.2% | 1.40 | 23 | 9.1% | |
| 10 | 100 | 60 | 2.5% | 1.16 | 7 | 2.8% | |
| 11 | **45** | **36** | **1.5%** | — | 1 | 0.4% | **新增**：level=1锚点 |
| 12 | 1 | 1 | 0.04% | — | 0 | 0% | fade-out终点（保留） |

Matter Level 与 brightness 的转换：`Level = (brightness - 36) × 253 / 2363`
亮度% = Level / 254 × 100

- 整体以 γ≈2.4 为主，亮端高γ压缩，暗端低γ抬尾防抖动
- `{45,36}` 中的 45 是 level=1 时的 target_brightness 值（1×2363/253+36=45）
- `{1,1}` 保留不动——关灯 fade-out 需要经此段平滑降到接近零，再由 `_light_ll_set_onoff(0)` 彻底关闭
- 色温拆分：`cold = curve × ratio`, `warm = curve × (1-ratio)`, 两路之和 = curve

### 曲线表 slsd_entry_5s[]（24段）
顶部 5 阶等距扩展为 16 阶（步长≈60），下部 8 阶保持不变。

| # | brightness | pwm | 占空比 | 等效γ | Matter Level | 亮度% | 说明 |
|---|-----------|-----|--------|-------|-------------|-------|------|
| 0 | 2399 | 2399 | 100% | — | 253 | 99.6% | 最亮 |
| 1 | 2340 | 2201 | 91.7% | 3.95 | 247 | 97.2% | 扩展 |
| 2 | 2280 | 2000 | 83.3% | 3.80 | 240 | 94.5% | 扩展 |
| 3 | 2220 | 1834 | 76.4% | 3.49 | 234 | 92.1% | 扩展 |
| 4 | 2160 | 1702 | 70.9% | 3.17 | 227 | 89.4% | 扩展 |
| 5 | 2100 | 1570 | 65.4% | 2.95 | 221 | 87.0% | 扩展 |
| 6 | 2040 | 1438 | 59.9% | 2.82 | 215 | 84.6% | 扩展 |
| 7 | 1980 | 1322 | 55.1% | 2.68 | 208 | 81.9% | 扩展 |
| 8 | 1920 | 1238 | 51.6% | 2.49 | 201 | 79.1% | 扩展 |
| 9 | 1860 | 1154 | 48.1% | 2.34 | 195 | 76.8% | 扩展 |
| 10 | 1800 | 1070 | 44.6% | 2.21 | 189 | 74.4% | 扩展 |
| 11 | 1740 | 990 | 41.2% | 2.08 | 182 | 71.7% | 扩展 |
| 12 | 1680 | 930 | 38.8% | 1.93 | 176 | 69.3% | 扩展 |
| 13 | 1620 | 870 | 36.2% | 1.81 | 170 | 66.9% | 扩展 |
| 14 | 1560 | 810 | 33.8% | 1.71 | 163 | 64.2% | 扩展 |
| 15 | 1500 | 750 | 31.3% | 1.62 | 157 | 61.8% | 扩展 |
| 16 | 1250 | 550 | 22.9% | 2.26 | 130 | 51.2% | |
| 17 | 1000 | 400 | 16.7% | 2.05 | 103 | 40.6% | |
| 18 | 750 | 275 | 11.5% | 1.86 | 76 | 29.9% | |
| 19 | 500 | 175 | 7.3% | 1.67 | 50 | 19.7% | |
| 20 | 250 | 100 | 4.2% | 1.40 | 23 | 9.1% | |
| 21 | 100 | 60 | 2.5% | 1.16 | 7 | 2.8% | |
| 22 | **45** | **36** | **1.5%** | — | 1 | 0.4% | level=1锚点 |
| 23 | 1 | 1 | 0.04% | — | 0 | 0% | fade-out终点 |

### 曲线表 slsd_entry_5s[]（用户定义，24段）
由用户提供的 254 级 PWM 数据抽取 24 个关键点生成。

| # | brightness | pwm | 占空比 | Matter Level | 亮度% | 说明 |
|---|-----------|-----|--------|-------------|-------|------|
| 0 | 2399 | 2399 | 100% | 253 | 99.6% | 最亮 |
| 1 | 2290 | 1969 | 82.0% | 241 | 94.9% | |
| 2 | 2181 | 1640 | 68.3% | 230 | 90.6% | |
| 3 | 2072 | 1343 | 56.0% | 218 | 85.8% | |
| 4 | 1963 | 1100 | 45.8% | 206 | 81.1% | |
| 5 | 1854 | 916 | 38.2% | 195 | 76.8% | |
| 6 | 1744 | 750 | 31.3% | 183 | 72.0% | |
| 7 | 1635 | 615 | 25.6% | 171 | 67.3% | |
| 8 | 1526 | 512 | 21.3% | 160 | 63.0% | |
| 9 | 1417 | 420 | 17.5% | 148 | 58.3% | |
| 10 | 1308 | 344 | 14.3% | 136 | 53.5% | |
| 11 | 1198 | 282 | 11.8% | 124 | 48.8% | |
| 12 | 1089 | 234 | 9.8% | 113 | 44.5% | |
| 13 | 980 | 192 | 8.0% | 101 | 39.8% | |
| 14 | 871 | 157 | 6.5% | 89 | 35.0% | |
| 15 | 762 | 131 | 5.5% | 78 | 30.7% | |
| 16 | 652 | 107 | 4.5% | 66 | 26.0% | |
| 17 | 543 | 87 | 3.6% | 54 | 21.3% | |
| 18 | 434 | 73 | 3.0% | 43 | 16.9% | |
| 19 | 325 | 59 | 2.5% | 31 | 12.2% | |
| 20 | 216 | 48 | 2.0% | 19 | 7.5% | |
| 21 | 106 | 39 | 1.6% | 7 | 2.8% | |
| 22 | **45** | **36** | **1.5%** | 1 | 0.4% | level=1锚点 |
| 23 | 1 | 1 | 0.04% | 0 | 0% | fade-out终点 |

### level=1 最终结果
```
target_brightness = 1 × 2363/253 + 36 = 45
curve_pwm(45): 45 落在 {100,60} 和 {45,36} 之间 → = 36
占空比 = 36/2400 = 1.50% ✓
```

### 夜灯（LIGHT_LEVEL_MIN_VALUE=1）PWM值
- 改前：target=33 → curve=20 → 占空比 0.83%（抖动）
- 改后：target=45 → curve=36 → 占空比 **1.50%**
