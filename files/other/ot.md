```c
//Channel Config
sudo ot-ctl channel //Read current channel
sudo ot-ctl dataset channel 15 //set new channel
sudo ot-ctl dataset commit active //make it active
sudo ot-ctl channel //Read current channel again
```
```c
sudo ot-ctl factoryreset 
sudo ot-ctl dataset init new
sudo ot-ctl dataset networkkey 00112233445566778899aabbccddeeff
sudo ot-ctl dataset extpanid 1111111122222222
sudo ot-ctl dataset panid 0x1234
sudo ot-ctl dataset channel 15
sudo ot-ctl dataset commit active
sudo ot-ctl prefix add fd11:22::/64 pasor
sudo ot-ctl ifconfig up
sudo ot-ctl thread start
```