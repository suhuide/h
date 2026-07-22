# Protocol
| header   | header |header  | header | Version | Mode | Config(Endpoint) | Cid |Cid| Aid |Aid | Value |Value| Check |
|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|
| D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 |
| 55 | AA | AA | 55 | 00 | 02 | 00 | 00 | 00 | 00 | 00  | 00  | 00  | 13  |
| 55 | AA | AA | 55 | 00 | 01 | 03 | 00 | 11 | 00 | 00  | 00  | 00  | 13  |
| 55 | AA | AA | 55 | 00 | 03 | 01 | 01 | 02 | 00 | 08  | 00  | 32  | 3B  |
| 55 | AA | AA | 55 | 00 | 03 | 01 | 00 | 2F | 00 | 09  | 00  | 00  | 24  |

# RGBCW 配置
|通道	|引脚	|定时器	|组件|
|---|---|---|---|
|Red	|PD02	|TIMER0 CC0	|simple_rgb_pwm_led instance rgb|
|Green	|PA04	|TIMER0 CC1	|↑|
|Blue	|PB00	|TIMER0 CC2	|↑|
|Cold	|PA08	|TIMER1 CC0	|无组件，hal_light.c 直驱|
|Warm	|PD03	|TIMER1 CC1	|↑|

```c
    // --- Hardware diagnostic: toggle PA08 & PD03 to verify LED connections ---
    // If CW LEDs blink 3 times during boot, hardware wiring is OK.
    // Remove this block after confirmation.
    {
        volatile uint32_t d;
        for (int i = 0; i < 3; i++) {
            GPIO_PinOutSet(HAL_LIGHT_CW_COLD_PORT, HAL_LIGHT_CW_COLD_PIN);
            GPIO_PinOutSet(HAL_LIGHT_CW_WARM_PORT, HAL_LIGHT_CW_WARM_PIN);
            for (d = 0; d < 8000000; d++) { __asm volatile("nop"); }
            GPIO_PinOutClear(HAL_LIGHT_CW_COLD_PORT, HAL_LIGHT_CW_COLD_PIN);
            GPIO_PinOutClear(HAL_LIGHT_CW_WARM_PORT, HAL_LIGHT_CW_WARM_PIN);
            for (d = 0; d < 8000000; d++) { __asm volatile("nop"); }
        }
    }
```    
```c
   // Init CW manually on TIMER1
    cw_pwm_init();

    // --- PWM diagnostic: blink CW LEDs 3 times via PWM ---
    // If CW LEDs blink 3 times with visible fade, full PWM path is OK.
    // Remove this block after confirmation.
    {
        volatile uint32_t d;
        hal_light_start_cw();
        for (int i = 0; i < 3; i++) {
            hal_light_set_cw(HAL_LIGHT_CW_RESOLUTION / 2, HAL_LIGHT_CW_RESOLUTION / 2);
            for (d = 0; d < 8000000; d++) { __asm volatile("nop"); }
            hal_light_set_cw(0, 0);
            for (d = 0; d < 8000000; d++) { __asm volatile("nop"); }
        }
        hal_light_stop_cw();
    }
```    

# Checksum

<div align="center">
  <img src="files/zh/xor.png" width="1080">
</div>

```c
uint8_t SPProtocol::check_sum_buffer(const uint8_t * buf, uint16_t size)
{
    uint8_t temp = 0;
    for (uint16_t i = 0; i < size; ++i) {
        #if 1
        temp ^= buf[i];
        #else
        temp += buf[i];
        #endif
    }

    return temp;
}
```
```c
    //...
    } else if (cur_idx == (rx_payload_size + SP_HEAD_SIZE)) { // checksum
        rx_buffer[cur_idx++] = data;

        #if 1
        {
            uint8_t buf1[] = {0x55, 0xAA, 0xAA, 0x55, 0x00, 0x01, 0x03, 0x00, 0x11, 0x00, 0x00, 0x00, 0x00};
            uint8_t sum = 0;
            for (size_t i = 0; i < sizeof(buf1); i++) sum ^= buf1[i];
            SP_LOG("eric,xor sum1 =0x%02X", sum);
            sum = check_sum_buffer(buf1, sizeof(buf1));
            SP_LOG("eric,xor sum1 =0x%02X", sum);
        }
        {
            uint8_t buf2[] = {0x55, 0xAA, 0xAA, 0x55, 0x00, 0x03, 0x01, 0x01, 0x02, 0x00, 0x08, 0x00, 0x32};
            uint8_t sum = 0;
            for (size_t i = 0; i < sizeof(buf2); i++) sum ^= buf2[i];
            SP_LOG("eric,xor sum2 =0x%02X", sum);
            sum = check_sum_buffer(buf2, sizeof(buf2));
            SP_LOG("eric,xor sum2 =0x%02X", sum);
        }
        {
            uint8_t buf3[] = {0x55, 0xAA, 0xAA, 0x55, 0x00, 0x03, 0x01, 0x00, 0x2F, 0x00, 0x09, 0x00, 0x00};
            uint8_t sum = 0;
            for (size_t i = 0; i < sizeof(buf3); i++) sum ^= buf3[i];
            SP_LOG("eric,xor sum3 =0x%02X", sum);
            sum = check_sum_buffer(buf3, sizeof(buf3));
            SP_LOG("eric,xor sum3 =0x%02X", sum);
        }
        #endif

        // checksum
        uint8_t checksum_value = check_sum_buffer(rx_buffer, cur_idx - 1);
        // Debug
        #if 1
        if (checksum_value != rx_buffer[cur_idx - 1]) {
            // checksum error
            SP_LOG("Error: checksum 0x%x != 0x%x\n", checksum_value, rx_buffer[cur_idx - 1]);
            cur_idx = 0;
            return FRAME_STATUS_ERR;
        }
        #endif
        sp_frame_t frame;
        memset(frame.payload, 0, sizeof(frame.payload));
        frame.sn           = get_uint16_from_network(&rx_buffer[5]);
        frame.type         = static_cast<msg_type_t>(rx_buffer[7]);
        frame.payload_size = rx_payload_size;
        if (frame.payload_size) {
            memcpy(frame.payload, &rx_buffer[SP_HEAD_SIZE], frame.payload_size);
        }

        LOG_API_HEX("MATTER RX", rx_buffer, cur_idx);
        recv_frame_cb(&frame);

        cur_idx = 0;
        return FRAME_STATUS_READY;
    } else {
        rx_buffer[cur_idx++] = data;
    }
    //...
```
```c
[10:42:41.690]  [00:00:12.115][silabs ]eric,xor sum1 =0x13
[10:42:41.690]  [00:00:12.116][silabs ]eric,xor sum1 =0x13
[10:42:41.690]  [00:00:12.116][silabs ]eric,xor sum2 =0x3B
[10:42:41.692]  [00:00:12.116][silabs ]eric,xor sum2 =0x3B
[10:42:41.692]  [00:00:12.116][silabs ]eric,xor sum3 =0x24
```