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
```c
ubuntu@ubuntu:~$ sudo ot-ctl dataset init new
Done
ubuntu@ubuntu:~$ sudo ot-ctl dataset commit active
Done
ubuntu@ubuntu:~$ sudo ot-ctl ifconfig up
Done
ubuntu@ubuntu:~$ sudo ot-ctl thread start
Done
ubuntu@ubuntu:~$ sudo ot-ctl state
detached
Done
ubuntu@ubuntu:~$ sudo ot-ctl state
leader
Done
ubuntu@ubuntu:~$ sudo ot-ctl dataset active -x
0e0800000000000100004a0300000d35060004001fffe002080ba8c26939f226680708fdd0a8de45a382e40510e9405e254d6075c62bac56ebbd930ecd030f4f70656e5468726561642d3533343601025346041013957463af0d2b6e844136e1f3fbf0300c0402a0f7f8000300000f
Done
```
```c
sudo ot-ctl dataset init new
sudo ot-ctl dataset channel 15
sudo ot-ctl dataset commit active
sudo ot-ctl ifconfig up
sudo ot-ctl thread start
sudo ot-ctl state
sudo ot-ctl channel
```