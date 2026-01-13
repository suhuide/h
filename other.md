# PWM
## Resolution(分辨率)  
占空比可以设置的最小步进数量  
Resolution = 2ⁿ (n为PWM计数器位数)  
2400 → 表示占空比可以设置为0到2399之间的2400个不同值  
每个亮度等级占空比增量：1/2400 ≈ 0.0417%  

## Frequency(频率)  
PWM信号每秒完成的周期数  
16000Hz → 每秒16000个完整周期  
周期时间：T = 1/16000 = 62.5µs  

## Curve
```c
typedef struct {
    uint32_t brightness;
    uint32_t pwm;

} slsd_model_entry_t;
```
### brightness

- 表面含义：输入亮度等级  
- 实际作用：控制系统的输入值，通常来自用户界面(如滑动条、旋钮、App设置)  
- 范围：在你的表中是从0-2400(对应SLSD_MIN_PWM_ADJ到SLSD_MAX_PWM_ADJ)  
- 重要理解：这不是实际光输出，而是用户期望的亮度级别。比如：  
     - brightness = 2400 表示用户想要最亮  
     - brightness = 1200 表示用户想要50%亮度(但实际光输出可能不是50%！)  
     - brightness = 100 表示用户想要很暗  

### pwm
- 表面含义：PWM输出值  
- 实际作用：实际发送给LED驱动器的PWM占空比值  
- 范围：同样从0-2400(对应0%-100%占空比)  
- 重要理解：这是实际控制LED亮度的硬件参数，但与人眼感知的亮度不是线性关系！  

```c
用户界面     →   查表函数             →     PWM输出        →   LED实际亮度
brightness  →   calculate_curve_pwm  →     pwm            →   人眼感知亮度
(0-2400)        (非线性转换)               (0-2400占空比)      (非线性感知)
```