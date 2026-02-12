## Matter Stack
### Log
[rgb-serial-data-off2on](rgb-serial-data-off2on.md)  
```c
[12:28:40.460][detail][IN] UDP Message Received packet nb : 236 SrcAddr : fdf7:dc9d:f190:0:82d:b81c:c988:57af[58993] DestAddr : fdf7:dc9d:f190:0:c7b7:fda5:a41f:86a8[5540] Payload Length 70
[12:28:40.462][info  ][EM] >>> [E:44405r S:36965 M:92784410] (S) Msg RX from 1:00000000A5E93870 [AAAB] to 00000000864E3838 --- Type 0001:08 (IM:InvokeCommandRequest) (B:70)
[12:28:40.463][detail][EM] Handling via exchange: 44405r, Delegate: 0x2000413c
[12:28:40.464][detail][DMG] Received command for Endpoint=3 Cluster=0x0000_0008 Command=0x0000_0004
[12:28:40.464][info  ][ZCL] RX level-control: MOVE_TO_LEVEL_WITH_ON_OFF fe null 0 0
[12:28:40.464][silabs ]LAM: eric,endpoint_id 3, OnLevel 254

bool emberAfLevelControlClusterMoveToLevelWithOnOffCallback(CommandHandler * commandObj, const ConcreteCommandPath & commandPath,
                                                            const Commands::MoveToLevelWithOnOff::DecodableType & commandData)
{
    MATTER_TRACE_SCOPE("MoveToLevelWithOnOff", "LevelControl");
    auto & level           = commandData.level;
    auto & transitionTime  = commandData.transitionTime;
    auto & optionsMask     = commandData.optionsMask;
    auto & optionsOverride = commandData.optionsOverride;

    if (transitionTime.IsNull())
    {
        ChipLogProgress(Zcl, "%s MOVE_TO_LEVEL_WITH_ON_OFF %x null %x %x", "RX level-control:", level, optionsMask.Raw(),
                        optionsOverride.Raw());
    }
    else
    {
        ChipLogProgress(Zcl, "%s MOVE_TO_LEVEL_WITH_ON_OFF %x %2x %x %x", "RX level-control:", level, transitionTime.Value(),
                        optionsMask.Raw(), optionsOverride.Raw());
    }

    level_control_on_level_changed(commandPath.mEndpointId, level);

    Status status =
        moveToLevelHandler(commandPath.mEndpointId, Commands::MoveToLevelWithOnOff::Id, level, transitionTime,
                           Optional<BitMask<OptionsBitmap>>(optionsMask), Optional<BitMask<OptionsBitmap>>(optionsOverride),
                           INVALID_STORED_LEVEL); // Don't revert to the stored level

    commandObj->AddStatus(commandPath, status);

    return true;
}

```

## Serial Debug
### CMD Rx and process
```c
frame_status_t SPProtocol::decode(uint8_t data)
    recv_frame_cb(&frame);
        static SPProtocol spp_instance(_spp_recv_frame_callback);
        _spp_recv_frame_callback
            spp_app_event_handler
                process_dev_report

```
### On/Off Operation
```c
MatterPostAttributeChangeCallback
    app_colorlight_mgr_attr_change_event_handler
        OnOffAttributeChangedEventHandler
            app_comm_send_ctrl_cmd
        LevelControlAttributeChangedEventHandler
            app_comm_send_ctrl_cmd
        ColorControlAttributeChangedEventHandler
            app_comm_send_ctrl_cmd

```

## LED on/off Control
```c
[14:52:03.534][silabs ] MATTER TX: : 55 aa 02 02 ac 
04 00 05 
07 01 
00 01 
10 
d1 
[14:52:03.534][silabs ]COM: CMD: 0x04, SN: 684, LEN: 14

[14:52:03.565][silabs ] MATTER RX: : 55 aa 02 08 19 
05 00 05 
07 01 
00 01 
10 
45 
[14:52:03.565][silabs ]COM: device report ID: 0x07 TYPE: 1 LEN: 1 [passive]
[14:52:03.734][silabs ]COM: mcu2host: 02 06 6f ff ff 03 54 00 13 88 ff ff ff ff ff ff ff ff ff ff ff ff 

[14:52:10.136][silabs ] MATTER RX: : 55 aa 02 08 1a 
05 00 05 
07 01 
00 01 
11 
47 
```
## RGB Control
```c
[14:52:10.136][silabs ]COM: device report ID: 0x07 TYPE: 1 LEN: 1 [passive]
[14:52:10.206][silabs ] MATTER TX: : 55 aa 02 02 ae 
04 00 08 //RGB
0d 02 
00 04 //data len
01 0a fe 00 //RGB data
d9 
[14:52:10.206][silabs ]COM: CMD: 0x04, SN: 686, LEN: 17

[14:52:10.378][silabs ] MATTER RX: : 55 aa 02 08 1b 
05 00 08 
0d 02 
00 04 
01 0a fe 00 
4d 
[14:52:10.379][silabs ]COM: device report ID: 0x0d TYPE: 2 LEN: 4 [passive]
[14:52:10.563][silabs ]COM: mcu2host: 03 13 74 ff ff 0a fe 00 13 88 ff ff ff ff ff ff ff ff ff ff ff ff 

//Battery
[14:52:11.258][silabs ] MATTER RX: : 55 aa 02 08 1c 
06 00 08 
04 02 
00 04 
00 00 00 63 
a0 
[14:52:11.258][silabs ]COM: device report ID: 0x04 TYPE: 2 LEN: 4 [active]
[14:52:11.426][silabs ]COM: mcu2host: 00 00 00 00 63 
```