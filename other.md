# [E](./files/other/e.md)
# Tip
```c
给我一个完整的、可直接复制粘贴的 Markdown 源码,
严格按照这次的标准来：使用标题、列表、段落等 Markdown 语法，
所有代码块均采用四个空格缩进的方式，避免使用 ``` 符号，
确保文档在任何平台上都能正确显示且不会中断。
```
# VPN
网址一: https://fbweb02.flyingbird.la
网址二: https://fbweb03.flyingbird.id
网址三: https://www.fbweb.cc

# Raspi
<div align="left">
  <img src="files/other/raspberrypi-pinmap.png" width="1080">
</div>

```c
ln -s ~/connectedhomeip/out/standalone/chip-tool ~/chip-tool
ln -s ~/connectedhomeip/out/ota-provider/chip-ota-provider-app ~/chip-ota-provider-app
ln -s ~/ot-br-posix/build/otbr/third_party/openthread/repo/src/posix/ot-ctl ~/ot-ctl
```
```c
cat /etc/default/otbr-agent
# Default settings for otbr-agent. This file is sourced by systemd

# Options to pass to otbr-agent
# OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyUSB0?uart-baudrate=460800&uart-flow-control trel://eth0"
OTBR_AGENT_OPTS="-I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyUSB0?uart-baudrate=460800 trel://eth0"
OTBR_NO_AUTO_ATTACH=0

sudo gedit /etc/default/otbr-agent
```
```c
sudo systemctl daemon-reload
sudo systemctl restart otbr-agent.service
```
```c
ubuntu:$y$j9T$hjmlkoibe.0MGn/58.0dJ1$myNLRHr/VQ6gF8BNnDY31m./sDxiHA55Mu.gGA2bt52:20476:0:99999:7:::
```
## Linux CMD
```c
//Check disk
sudo fdisk -l
// Original disk
Device     Boot   Start       End   Sectors  Size Id Type
/dev/sdb1  *       2048   1050623   1048576  512M  c W95 FAT32 (LBA)
/dev/sdb2       1050624 124735454 123684831   59G 83 Linux
//Target disk
Device     Boot   Start       End   Sectors  Size Id Type
/dev/sdb1  *       2048   1050623   1048576  512M  c W95 FAT32 (LBA)
/dev/sdb2       1050624 124735454 123684831   59G 83 Linux

//Check directory size
du -sh
//Check disk status
df -h /dev/sd*
//Check memory status  
free -h
//Check thread
ps aux
//Kill
kill -9 xxxx
```
### DD
```c
sudo dd if=/dev/sdb of=./sdb.img bs=2M conv=noerror,sync status=progress
sudo dd if=./sdb.img of=/dev/sdb bs=2M status=progress
```
# Tips
```c
//文件数
find . -name "*.c"|wc -l
//行数
find . -name "*.c" -or  -name "*.h" | xargs cat|wc -l
//行数(除空白行)
find . -name "*.c" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
find . -name "*.cpp" -or  -name "*.h" | xargs cat|grep -v ^$|wc -l
```
```c
//wildcard
.+?
```
```c
//每行前8个字符
.{8}
//包含0x00000044的所有行
.*0x00000044.*
```
```c
//删除空白行
^\s*(?=\r?$)\n
//只保留commit开头的行
^((?!commit ).)*$
^((?!(TASK|task|BUG|bug|JENKINS_JOB)).)*$
^(?!(.*(TASK|task|BUG|bug|JENKINS_JOB))).*$

//BDADDR, AC:86:D1:54:07:2D
\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b
\b(?!00:00:00:00:00:00\b)([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b
\b(?!00:00:00:00:00:00\b)([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b(?![:0-9A-Fa-f])
```
```c
//Scan and remove char before "收←◆" in each line
^.*收←◆

```
```c
(.*10 04.*)|(.*10 01.*)|(.*11 04.*)
```
```c
//[MT:MNKA1UNB00278B2QQ10] -> []
\[[^\]]*\]
[]
```
```c
(MATTER )[^)]*(X: :)
MATTER TX: :
MATTER RX: :
(MATTER )[^)]*(X: :)[^)]*(02 00 01 )
```
```c
//(https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3AMNKA1UNB00278B2QQ10) ->(https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A)
(data=MT%3A)[^)]*
data=MT%3A
```

# Beyond Compare
Remove CacheID under HKEY_CURRENT_USER\Software\Scooter Software\Beyond Compare 4 can make you happy.
```c
cmd
regedit

HKEY_CURRENT_USER\Software\Scooter Software\Beyond Compare 4
                                                    CacheID
```
# TaskBar
```c
C:\Users\huide\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar
```
# MarkItDown
```c
python -m pip install markitdown[all]
python -m pip install --upgrade pip
```
# Gith
```c
ghp_222ROGSaDsqttL5MamO6FvMxe3v1Va2hksdG
```
# IP
```c
C:\Users\Administrator\Desktop>curl ipinfo.io
{
  "ip": "103.172.81.131",
  "city": "Tung Chung",
  "region": "Islands",
  "country": "HK",
  "loc": "22.2878,113.9424",
  "org": "AS146961 NEXET LIMITED",
  "postal": "999077",
  "timezone": "Asia/Hong_Kong",
  "readme": "https://ipinfo.io/missingauth"
}
```
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
