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
sudo ot-ctl dataset init new
Done
sudo ot-ctl dataset commit active
Done
sudo ot-ctl ifconfig up
Done
sudo ot-ctl thread start
Done
sudo ot-ctl state
detached
Done
sudo ot-ctl state
leader
Done
sudo ot-ctl dataset active -x
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
```c
sudo systemctl daemon-reload
sudo systemctl restart otbr-agent
sudo systemctl status otbr-agent
● otbr-agent.service - OpenThread Border Router Agent
     Loaded: loaded (/lib/systemd/system/otbr-agent.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2026-06-24 03:29:00 UTC; 83ms ago
    Process: 234959 ExecStartPre=/usr/sbin/service mdns start (code=exited, status=0/SUCCESS)
   Main PID: 235059 (otbr-agent)
      Tasks: 1 (limit: 9240)
     Memory: 848.0K
        CPU: 66ms
     CGroup: /system.slice/otbr-agent.service
             └─235059 /usr/sbin/otbr-agent -I wpan0 -B eth0 "spinel+hdlc+uart:///dev/ttyUSB0?uart-flow-control=1" trel://eth0

Jun 24 03:29:00 ubuntu otbr-agent[235059]: [INFO]-DPROXY--: Started
Jun 24 03:29:00 ubuntu otbr-agent[235059]: [INFO]-APP-----: Co-processor version: SL-OPENTHREAD/3.0.0.0_GitHub-61e43cffb; EFR32; Jun  3 2026 14:43:06
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] Notifier------: StateChanged (0x521fc310) [MLAddr KeySeqCntr NetData Channel PanId NetName ExtPanId NetworkKey PSKc ...
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] Notifier------: StateChanged (0x521fc310) ... SecPolicy BbrState ActDset Nat64]
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] Bbr-----------: Start listening on port 61631
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] Bbr-----------: Backbone TMF subscribes ff32:40:fdf8:718c:cf83:a998:0:3: OK
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] BbrManager----: Start Backbone TMF agent: OK
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] AnnounceSender: ChannelMask:{ 11-26 }, period:21500
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] AnnounceSender: StartingChannel:11
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.041 [I] AnnounceSender: StartingChannel:11
Jun 24 03:29:00 ubuntu otbr-agent[235059]: 00:00:00.052 [I] Platform------: Execute command `ipset flush otbr-ingress-allow-dst-swap` = 0
sudo ot-ctl state
leader
Done
sudo ot-ctl dataset active -x
0e080000000000010000000300000b4a0300000f35060004001fffe002082d786bf354e59df80708fdf8718ccf83a9980510c1d7bed0358c657c7e4e42bd42a2d091030f4f70656e5468726561642d3962333901029b39041080f2e38b9b69d2c9e3bd1fbc8053313c0c0402a0f7f8

Done
```

```c
sudo systemctl stop otbr-agent
sudo otbr-agent -I wpan0 -B eth0 spinel+hdlc+uart:///dev/ttyUSB0?uart-flow-control=1 -v -d7
sudo ot-ctl state
```