# BLE Side Channel

Silicon Labs SiSDK 2025.12.0&ME v2.8.0推出了BLE Side Channel，  
该 BLE (Side Channel)为 Matter over Thread 设备提供了一条额外的 BLE 通信路径，  
通过自定义 GATT 服务和特征进行数据交换。以下是如何使用它以及需要注意的常见陷阱。  

---

## 一、如何使用

### 1. 初始化 Side Channel
在系统启动或 BLE 堆栈就绪后，需要初始化 Side Channel 并创建 GATT 服务。  
实际集成时，通常由 BLEManagerImpl 在内部自动完成（需定义宏 SL_USE_INTERNAL_BLE_SIDE_CHANNEL）。  
BLEManagerImpl 集成模式下，初始化流程已在 BLEManagerImpl::_Init() 中完成：
```c
    #if SL_USE_INTERNAL_BLE_SIDE_CHANNEL
        ReturnErrorOnFailure(sBleSideChannel.Init());
        BLEMgrImpl().InjectSideChannel(&sBleSideChannel);
        BLEMgrImpl().SideChannelConfigureAdvertisingDefaultData();
    #endif
```
InjectSideChannel 用于将 Side Channel 实例注入到 BLEManagerImpl 中，以便事件分发。

### 2. 配置广播数据
构造 `AdvConfigStruct`，填入广播数据和扫描响应数据，然后调用 `ConfigureAdvertising()`。
```c
    BLEChannelImpl::AdvConfigStruct advConfig;
    // 填充广播数据(例如设备名称、Service UUID)
    advConfig.advData = ByteSpan(yourAdvData, yourAdvDataLen);
    advConfig.responseData = ByteSpan(yourScanRspData, yourScanRspDataLen);
    advConfig.intervalMin = 160;   // 100ms (单位 0.625ms)
    advConfig.intervalMax = 160;
    advConfig.duration = 0;         // 持续广播直到停止
    advConfig.maxEvents = 0;        // 无限制
    advConfig.advConnectableMode = sl_bt_legacy_advertiser_connectable; // 可连接广播

    err = sBleSideChannel.ConfigureAdvertising(advConfig);
```
如果需要更精细的控制，也可以单独调用 `SetAdvertisingParams()` 和 `SetAdvHandle()`。

### 3. 启动 / 停止广播
```c
    err = sBleSideChannel.StartAdvertising();
    // ...
    err = sBleSideChannel.StopAdvertising();
```
### 4. 集成 BLE 事件处理
在 BLE 事件回调函数 sl_bt_on_event 中，先将事件传递给 BLEManagerImpl::ParseEvent()，未处理的事件再转给 Side Channel 的 ParseEvent()。
```c
    void sl_bt_on_event(sl_bt_msg_t *evt) {
        // 先让 BLEManagerImpl 处理 CHIPoBLE 相关事件
        chip::DeviceLayer::Internal::BLEManagerImpl::EventFilter eventFilter;
        eventFilter = chip::DeviceLayer::Internal::BLEMgrImpl().ParseEvent(evt);

        #if SL_BLE_SIDE_CHANNEL_ENABLED
        if (chip::DeviceLayer::Internal::BLEMgrImpl().GetSideChannel() != nullptr &&
            eventFilter != chip::DeviceLayer::Internal::BLEManagerImpl::EventFilter::MatterReservedEvent)
        {
            // The side channel may process events directly.
            chip::DeviceLayer::Internal::BLEMgrImpl().GetSideChannel()->ParseEvent(evt);
        }
        #endif
    }
```
Side Channel 内部会处理连接、断开、读写、MTU 交换、CCCD 写入等事件。

### 5. 读写数据
#### 接收数据
- **接收数据**：当对端写入 RX 特征时，`HandleWriteRequest()` 会将数据复制到一个 `MutableByteSpan` 中，然后打印。需要修改该函数，将数据转发给应用层(例如通过回调或队列)。
- **发送数据**：如果对端订阅了 TX 特征的指示，可以调用 `sl_bt_gatt_server_send_indication()` 主动发送数据。
当前代码没有封装发送函数，需要自行实现：
```c
    CHIP_ERROR BLEChannelImpl::SendIndication(const uint8_t* data, size_t len) {
        if (!mConnectionState.allocated || !mConnectionState.subscribed) {
            return CHIP_ERROR_INCORRECT_STATE;
        }
        // 可在此添加 MTU 检查和分片逻辑
        sl_status_t ret = sl_bt_gatt_server_send_indication(
            mConnectionState.connectionHandle,
            mSideTxCharHandle,
            len,
            data
        );
        return MapBLEError(ret);
    }
```
注意发送前需检查 MTU，必要时对数据进行分片。

### 6. 管理连接
- 连接成功时自动记录在 `mConnectionState` （单连接限制）中。
- 断开连接时自动清除记录。
- 如果需要主动断开连接，调用 `CHIP_ERROR BLEChannelImpl::CloseConnection()`。
- 可以通过 `CHIP_ERROR BLEChannelImpl::SetConnectionParams()` 调整连接参数。

---

## 二、常见陷阱与注意事项

#### 1. 单连接限制
`BLEChannelImpl` 内部只维护一个连接状态(`mConnectionState`)。如果多个设备同时连接，只有第一个会被处理，后续连接会被忽略或覆盖。适用于点对点场景。

#### 2. MTU 处理
MTU 交换后，`mConnectionState.mtu` 被更新，但代码未自动处理大于 MTU 的数据分片。发送数据时需自行检查长度，必要时分片发送。

#### 3. CCCD 订阅处理
- TX 特征支持指示(Indicate)，但订阅状态仅在 `HandleCCCDWriteRequest()` 中记录，未触发上层回调。需要在此处添加应用逻辑，例如通知数据发送任务可以开始发送。
- 发送指示前务必检查 `mConnectionState.subscribed`，否则对端可能不会确认，导致堆栈错误。

#### 4. 读写请求的默认实现
- **读请求**：`HandleReadRequest()` 目前返回固定字符串 `"You are reading the Si-Channel TX characteristic"`，这不是一个通用的实现。需要根据实际特征返回有意义的数据。
- **写请求**：`HandleWriteRequest()` 将数据拷贝到栈上的临时缓冲区并打印，数据随即丢失。如需持久化或转发，应在此处添加回调或队列。

#### 5. 缓冲区大小与生命周期
- 写请求的数据指针 `evt->data.evt_gatt_server_user_write_request.value.data` 指向事件内部缓冲区，在事件处理完成后会被释放。如需长期保存，必须拷贝。
- 示例中使用 `MutableByteSpan` 和栈数组(255 字节)，注意最大特征长度为 255，缓冲区足够，但若需处理更大数据需调整。

#### 6. 广播数据冲突
`ConfigureAdvertising()` 和 `GeneratAdvertisingData()` 都可能设置广播数据。后者调用 `sl_bt_legacy_advertiser_generate_data` 会生成默认数据，可能覆盖前者设置。建议统一使用 `ConfigureAdvertising()` 手动设置数据，避免混合使用。

#### 7. 条件编译差异
无
#### 8. 地址管理
`ConfigureAdvertising()` 中为广播集生成了一个随机的静态地址，并将两个 MSB 置为 `11`(符合 BLE 静态地址要求)。但若设备需要特定地址或公共地址，需修改此处逻辑。同时，每次停止广播后调用 `sl_bt_advertiser_clear_random_address` 会清除地址，下次启动会重新随机生成，可能影响对端白名单。

#### 9. 错误映射
`MapBLEError()` 将部分 BLE 错误码映射为 Chip 错误，但未覆盖所有可能值。对于未处理的错误码，返回 `CHIP_ERROR(ChipError::Range::kPlatform, bleErr + CHIP_DEVICE_CONFIG_SILABS_BLE_ERROR_MIN)`，调用者需要根据平台错误码进一步解析。

#### 10. 资源释放
`StopAdvertising()` 中调用了 `sl_bt_advertiser_delete_set` 删除广播集。如果后续需要再次广播，必须重新创建广播集(`ConfigureAdvertising()` 中会检查并创建)。注意避免重复创建导致资源泄漏。

#### 11. 多线程/任务安全性
该代码通常在 BLE 事件线程中执行，若应用层在不同任务中调用其方法(如 `StartAdvertising`、`SendIndication`)，需要确保线程安全(例如通过互斥锁保护共享状态)。

#### 12. 测试与调试
- 使用 LightBlue 或 nRF Connect 等工具连接设备，查看Side Channel服务和特征。
- 订阅 TX 特征指示，写入 RX 特征，观察日志输出。
- 确认 MTU 交换后的值，确保数据包大小合适。

---

## 三、扩展建议
- 为Side Channel添加应用层回调接口，例如 `SetOnMessageReceivedCallback()`，以便在收到写请求时通知应用。
- 实现数据发送队列，支持分片和重传(如果使用指示)。
- 考虑多连接场景(如需要)，修改 `mConnectionState` 为数组或动态分配。
- 完善错误处理和日志，便于定位问题。

通过遵循上述步骤并留意陷阱，可以顺利集成并使用 Silicon Labs 的 BLE Side Channel功能。如有更具体的需求，可参考 SiSDK 的 BLE 相关文档和 Matter 集成示例。

---

# BLEManagerImpl 代码深度分析 (Silicon Labs EFR32, Matter)

你提供的第二段代码是 Silicon Labs EFR32 平台上 Matter 设备的 BLEManager 实现核心部分。它负责管理标准的 CHIPoBLE(Matter over BLE)服务，并与之前分析的 `BLEChannelImpl` Side Channel进行集成。以下是对该代码的详细分析，包括架构、关键机制、与Side Channel的协作以及潜在的陷阱。

---

## 一、整体架构与职责

`BLEManagerImpl` 是 Matter 设备层 BLE 管理的单例实现，继承自 `BleLayer` 并实现 `BlePlatformDelegate` 和 `BleApplicationDelegate`。其主要职责包括：

1. **初始化 BLE 栈和 GATT 数据库**：通过 `_Init()` 初始化 BleLayer、创建软件定时器、设置随机静态地址。
2. **管理 CHIPoBLE 服务**：控制广播的启停、广播模式(快速/慢速/扩展)、处理连接。
3. **处理 BLE 事件**：在 `sl_bt_on_event` 中接收蓝牙事件，通过 `ParseEvent` 分发到对应处理函数。
4. **与上层交互**：将收到的数据通过 `CHIPoBLEWriteReceived` 事件传递给 Matter 协议栈。
5. **集成Side Channel**：如果启用了Side Channel(`SL_USE_INTERNAL_BLE_SIDE_CHANNEL`)，则创建 `BLEChannelImpl` 实例，并注入到 BLEManager 中，实现事件分流。

---

## 二、关键数据结构

### 1. BLEConState
```c
    typedef struct
    {
        bool allocated;          // 连接槽是否被占用
        uint8_t connectionHandle; // BLE 连接句柄
        uint8_t bondingHandle;    // 绑定句柄
        uint16_t mtu;             // 当前连接 MTU
        uint8_t subscribed;       // TX 特征是否被订阅
    } BLEConState;
```
维护每个 CHIPoBLE 连接的状态，数组大小 `kMaxConnections`(通常为 2 或 3)。

### 2. mIndConfId
```c
    uint8_t mIndConfId[kMaxConnections];
```
用于记录每个连接对应的软件定时器句柄，用于指示(Indication)确认超时监控。

### 3. Flags 位掩码
```c
    enum Flags {
        kAdvertisingEnabled,          // 广播使能(上层设置)
        kFastAdvertisingEnabled,      // 快速广播模式(true=快速，false=慢速)
        kAdvertising,                 // 当前正在广播
        kRestartAdvertising,          // 需要重启广播(配置变更)
        kDeviceNameSet,               // 设备名称已设置
        kSiLabsBLEStackInitialize,    // BLE 栈已初始化
        kExtAdvertisingEnabled,       // 扩展广播模式(用于更长广播周期)
    };
```
控制广播状态机和行为。

---

## 三、核心功能解析

### 1. 初始化流程 `_Init()`
- 调用 `BleLayer::Init` 初始化 CHIP BLE 层。
- 清零连接数组和指示确认数组。
- 创建软件定时器 `sbleAdvTimeoutTimer` 用于广播模式切换。
- 生成随机静态地址(满足 BLE 静态地址要求：两高位为 `11`)。
- **Side Channel初始化**：若定义 `SL_USE_INTERNAL_BLE_SIDE_CHANNEL`，则调用 `sBleSideChannel.Init()`，并将Side Channel注入 `BLEMgrImpl`，然后调用 `SideChannelConfigureAdvertisingDefaultData()` 配置Side Channel默认广播数据。
- 触发状态机 `DriveBLEState` 运行。

**注意**：随机地址在每次系统启动时生成，但符合“地址更改仅在启动时”的 BLE 规范。重启应用(非重启芯片)不会改变地址。

### 2. 广播管理
广播状态由 `DriveBLEState` 驱动，基于以下条件：
- 服务模式为 Enabled
- 广播使能 `kAdvertisingEnabled` 为 true
- 当前连接数未达上限

**启动广播 `StartAdvertising()`**：
- 停止当前广播(如果存在)。
- 调用 `ConfigureAdvertisingData()` 组装广播包和扫描响应包。
- 根据 `kFastAdvertisingEnabled` 设置广播间隔。
- 调用 `sl_bt_legacy_advertiser_start` 启动可连接/可扫描广播。
- 若为快速广播，启动定时器 `sbleAdvTimeoutTimer` 用于切换到慢速/扩展广播。

**广播数据配置 `ConfigureAdvertisingData()`**：
- 获取设备识别信息 `mDeviceIdInfo`。
- 如果未设置设备名，则根据 discriminator 生成默认名(如 `Matter-1234`)。
- 组装广播数据：Flags、Service Data(包含短 UUID 和设备识别信息)。
- 组装扫描响应：Service UUID、设备名称。
- 创建广播集 `mAdvertisingSetHandle` 并设置随机地址。
- 调用 `sl_bt_legacy_advertiser_set_data` 设置广播和扫描响应数据。

**广播模式切换**：
- 快速广播超时后调用 `BleAdvTimeoutHandler`，根据配置切换到慢速或扩展广播，并可能再次启动定时器。

**注意**：扩展广播(`kExtAdvertisingEnabled`)逻辑较复杂，需确保宏 `CHIP_DEVICE_CONFIG_EXT_ADVERTISING` 正确配置。

### 3. 连接管理
- **连接打开**：`HandleConnectEvent` 检查是否是 CHIPoBLE 广播集发起的连接，若是则调用 `AddConnection` 记录连接状态，并触发状态机。
- **连接关闭**：`HandleConnectionCloseEvent` 移除连接状态，根据断开原因构造 `kCHIPoBLEConnectionError` 事件，并设置 `kRestartAdvertising` 以恢复广播。
- **连接参数协商**：`HandleConnectParams` 检查中央设备协商的参数(间隔、延迟、超时)，若不符合预期则重新设置更合适的参数(如最小/最大间隔、超时时间)。这有助于提高连接稳定性。

### 4. GATT 事件处理
`ParseEvent` 是事件入口，在芯片锁保护下处理各类事件。处理结果标记为 `MatterReservedEvent`(CHIPoBLE 已处理)或 `UnprocessedEvent`(未处理)。之后，未处理的事件会传递给Side Channel(如果存在)。

**关键事件处理**：

- **`sl_bt_evt_gatt_server_attribute_value_id`**：写请求。
    - 检查连接是否属于 CHIPoBLE。
    - 若为 RX 特征(`gattdb_CHIPoBLEChar_Rx`)，则调用 `HandleRXCharWrite`：将数据拷贝到 PacketBuffer，并通过 `kCHIPoBLEWriteReceived` 事件传递给上层。
    - 若为其他 CHIPoBLE 特征但连接不属于 CHIPoBLE，则返回错误，防止非法写入。

- **`sl_bt_evt_gatt_server_characteristic_status_id`**：
    - 若状态为 `sl_bt_gatt_server_confirmation`，表示指示确认，调用 `HandleTxConfirmationEvent` 停止定时器并向上层发送确认事件。
    - 若状态为 `sl_bt_gatt_server_client_config`，表示 CCCD 写入，调用 `HandleTXCharCCCDWrite` 处理订阅/取消订阅。

- **`sl_bt_evt_gatt_server_user_read_request_id`**：
    - 若定义了 `CHIP_ENABLE_ADDITIONAL_DATA_ADVERTISING`，处理 C3 特征读取请求，返回附加数据 TLV。

- **`sl_bt_evt_system_soft_timer_id`**：软件定时器超时，用于指示确认超时检查。若超时，发送 `kCHIPoBLEConnectionError` 事件，协议终止。

### 5. 指示发送与确认超时
`SendIndication` 通过 `sl_bt_gatt_server_send_indication` 发送数据，并启动一个 6 秒的软定时器(使用 `sl_bt_system_set_lazy_soft_timer`)。定时器句柄通过 `GetTimerHandle` 分配，并与连接句柄绑定。如果收到确认，定时器被取消；否则超时后触发错误事件。

**注意**：软定时器数量有限(`BLE_CONFIG_MAX_SOFTWARE_TIMERS` 为 4)，每个连接最多占用一个，`kMaxConnections` 应小于等于该值。

### 6. 与Side Channel集成
- **注入**：InjectSideChannel 允许注入一个Side Channel实例。
- **配置默认广播**：`SideChannelConfigureAdvertisingDefaultData` 为Side Channel配置一套示例广播数据(包含自定义 UUID 和名称 “Si-Channel”)。
- **事件分流**：在 `sl_bt_on_event` 中，先调用 `BLEMgrImpl().ParseEvent(evt)` 让 CHIPoBLE 处理事件；若返回 `EventFilter::MatterReservedEvent`，则Side Channel不再处理；否则(`UnprocessedEvent` 或 `SharableEvent`)将事件传递给Side Channel的 `ParseEvent`。

**潜在问题**：
- Side Channel广播配置为默认数据，可能与 CHIPoBLE 广播冲突(尽管使用不同广播集，但若同时广播可能占用相同信道，需确保广播集句柄不同)。

---

## 四、潜在陷阱与注意事项

#### 1. 连接数限制
`kMaxConnections` 硬编码(代码中未给出定义，但根据数组大小推测为 2 或 3)。若设备需同时连接多个 central，需调整该值并确保内存足够。

#### 2. 线程安全
`ParseEvent` 在 `sl_bt_on_event` 中调用，该函数运行在蓝牙任务上下文。`PlatformMgr().LockChipStack()` 保护了 CHIP 内部状态，但 `BLEManagerImpl` 的其他公共方法(如 `_SetAdvertisingEnabled`)可能被应用线程直接调用，这些方法未加锁，可能导致竞态条件。建议调用方在调用前自行锁栈，或内部实现锁机制。

#### 3. 事件过滤逻辑
事件先由 CHIPoBLE 处理，标记为 `MatterReservedEvent` 后Side Channel不再处理。这意味着：
- 如果 CHIPoBLE 错误地将本应属于Side Channel的事件标记为自己处理，Side Channel将收不到该事件。
- 某些事件(如连接打开)可能被两个通道同时需要？当前设计是互斥的。若Side Channel需要知道连接事件，应在 CHIPoBLE 未处理时自己处理。

#### 4. 广播集句柄冲突
`mAdvertisingSetHandle` 用于 CHIPoBLE 广播，Side Channel有自己的广播句柄(保存在 `BLEChannelImpl` 中)。两者可以共存，但需注意：
- 同时广播可能增加功耗和信道竞争。
- 如果Side Channel使用与 CHIPoBLE 相同的广播类型和信道，可能相互干扰。建议错开广播时段或使用不同 PHY。

#### 5. 内存管理
`HandleRXCharWrite` 中将数据拷贝到 `PacketBufferHandle`，然后通过事件传递所有权。需确保 `PacketBuffer` 正确释放(上层会处理)。若上层处理延迟，可能导致缓冲区耗尽。

#### 6. 条件编译宏的依赖
代码中大量使用宏控制功能，如：
- `SL_USE_INTERNAL_BLE_SIDE_CHANNEL`：启用Side Channel，否则相关代码被排除。
- `CHIP_ENABLE_ADDITIONAL_DATA_ADVERTISING`：启用 C3 特征和附加数据。
- `SL_BLE_SIDE_CHANNEL_ENABLED`：控制Side Channel相关接口的编译。

配置错误可能导致功能缺失或编译失败。

#### 7. 定时器句柄管理
`GetTimerHandle` 分配软定时器句柄时，循环查找空闲槽。但若 `mIndConfId` 数组被填满且没有空闲(例如连接数超过数组大小)，会返回 `kMaxConnections`，上层未检查返回值直接使用，可能导致数组越界。调用处 `GetTimerHandle(conId, true)` 后应检查返回值是否 `< kMaxConnections`。

#### 8. 连接参数协商逻辑
`HandleConnectParams` 中比较当前协商参数与期望值，若间隔超出范围或超时小于期望值，则重新设置。但设置新参数时使用了 `sl_bt_connection_set_parameters`，该调用可能失败(如连接已断开)，未检查返回值。此外，重新设置参数可能引发 L2CAP 信令交互，影响用户体验。

#### 9. 扩展广播切换逻辑
`BleAdvTimeoutHandler` 中设置 `kExtAdvertisingEnabled` 并调用 `SetAdvertisingMode(kSlowAdvertising)`，但 `SetAdvertisingMode` 只设置标志并触发状态机，未立即修改广播数据。广播数据中的 VID/PID 清零在 `ConfigureAdvertisingData` 中根据 `kExtAdvertisingEnabled` 决定。若定时器触发后立即调用 `ConfigureAdvertisingData` 可能来不及，需确保状态机在下次广播启动前重新配置数据。

#### 10. 错误码映射
`MapBLEError` 将部分常见错误映射为 CHIP 错误，但未覆盖所有可能。对于未知错误，返回的平台错误码范围 `CHIP_DEVICE_CONFIG_SILABS_BLE_ERROR_MIN` 需要调用者进一步解析。

#### 11. 多Side Channel支持不完整
无

#### 12. 日志级别
部分日志使用 `ChipLogProgress`，在生产环境中可能过于冗长。可根据需要调整日志级别。

---

## 五、与 BLEChannelImpl 的协作总结

- **初始化**：BLEManagerImpl 创建并初始化Side Channel，配置其默认广播数据。
- **事件分发**：在 `sl_bt_on_event` 中，先由 BLEManagerImpl 处理 CHIPoBLE 相关事件，剩余事件交给Side Channel处理。
- **功能互补**：
    - CHIPoBLE 用于 Matter 协议通信(通过 RX/TX 特征)。
    - Side Channel提供额外的自定义 GATT 服务，可用于诊断、配置或私有数据传输。
- **资源隔离**：各自使用独立的广播集、连接状态管理(Side Channel内部维护自己的连接状态)，但共享 BLE 栈资源。

---

## 六、改进建议

1. **增强线程安全**：在公共方法(如 `_SetAdvertisingEnabled`)中添加 `PlatformMgr().LockChipStack()` / `UnlockChipStack()`。
2. **检查定时器句柄有效性**：在 `SendIndication` 中验证 `timerHandle` 是否有效。
3. **支持多Side Channel**：如果确实需要两个Side Channel，修改事件循环遍历所有注入的通道。
4. **优化广播切换**：确保广播数据在模式切换前重新配置，避免使用过期数据。
5. **错误处理增强**：在连接参数协商、定时器启动等处检查返回值并记录错误。
6. **文档化宏定义**：清晰说明每个宏的作用和依赖，方便配置。

---

## 七、总结

`BLEManagerImpl` 是 Matter on EFR32 平台 BLE 通信的核心，它封装了 CHIPoBLE 服务的完整生命周期，并通过事件分流机制与 `BLEChannelImpl` Side Channel协同工作。理解其内部状态机、事件处理和资源管理，对于调试 BLE 相关问题、扩展Side Channel功能至关重要。使用过程中需特别注意连接数限制、线程安全、定时器管理以及宏的正确配置。