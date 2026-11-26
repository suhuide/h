# Matter 自定义 Cluster XML 新增与修改指南

本文说明如何在 SDK 目录中新增、修改 Matter Cluster 的 XML 定义，供使用 ZAP 数据模型的开发者参考。内容仅涉及 XML 文件、加载清单和定义校验，不涉及具体项目、业务代码或固件构建。

示例采用 Silicon Labs / Matter SDK 常见的 ZAP XML 格式。不同 SDK 版本的目录、标签支持情况可能不同，应以所用 SDK 中的现有 XML 和 ZAP 校验结果为准。

## 1 XML 文件放在哪里

**自定义 Cluster XML 应放在 SDK 目录中。** 常见目录如下：

```text
<Matter SDK>/src/app/zap-templates/zcl/data-model/chip/
```

如果使用 Silicon Labs Matter Extension，常见目录为：

```text
<Simplicity SDK>/extension/matter_extension/
  third_party/matter_sdk/src/app/zap-templates/zcl/data-model/chip/
```

可在上述目录新增独立文件，例如 `vendor-diagnostic-cluster.xml`。也可以在 SDK 内建立专用厂商目录，但需要将其加入实际使用的 `zcl.json` 的 `xmlRoot` 搜索路径。

建议将自定义定义放在独立 XML 中，便于维护、分发和 SDK 升级迁移。修改已有 Cluster 时，先备份对应文件。

## 2 新增一个自定义 Cluster

### 2.1 分配 Cluster ID

Matter 厂商自定义 Cluster 使用完整的 32 位 ID：

```text
Cluster ID = (Vendor ID << 16) | 厂商 Cluster 编号
```

- 高 16 位：Vendor ID。
- 低 16 位：厂商 Cluster 编号，范围为 `0xFC00～0xFFFE`。
- `0xFFF1～0xFFF4` 是测试 Vendor ID；量产应使用自己的正式 Vendor ID。

例如，测试 Vendor ID `0xFFF1` 与编号 `0xFC10` 组合得到 `0xFFF1FC10`。使用前应检查 SDK 已加载的 XML，避免 ID 冲突。

不要套用 Zigbee 的“16 位 Cluster ID 加 manufacturerCode”写法。Matter 的厂商标识已经包含在完整 ID 中。参见 [Silicon Labs 自定义 XML 规则](https://docs.silabs.com/zap-tool/latest/zap-users-guide/custom-xml)。

### 2.2 创建 XML 文件

在 SDK 中新建 `vendor-diagnostic-cluster.xml`，内容示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configurator>
  <domain name="CHIP"/>

  <cluster>
    <name>Vendor Diagnostic</name>
    <domain>General</domain>
    <description>Vendor-specific diagnostic data.</description>
    <code>0xFFF1FC10</code>
    <define>VENDOR_DIAGNOSTIC_CLUSTER</define>

    <client tick="false" init="false">true</client>
    <server tick="false" init="false">true</server>

    <attribute side="server"
               code="0x0000"
               name="SampleValue"
               define="SAMPLE_VALUE"
               type="int16u"
               writable="false"
               default="0">
      <mandatoryConform/>
    </attribute>

    <command source="client" code="0x00" name="ResetCounter">
      <description>Reset the diagnostic counter.</description>
      <mandatoryConform/>
    </command>
  </cluster>
</configurator>
```

该示例定义一个只读属性 `SampleValue` 和一个客户端发出的无参数命令 `ResetCounter`。示例应先通过所用 SDK 的 ZAP 校验，再纳入正式模型。

### 2.3 主要字段说明

| 字段 | 含义 |
| --- | --- |
| `configurator` | XML 根节点 |
| `name` | Cluster 名称，也会影响生成的类型和标识符名称 |
| `domain` | ZAP 中的分类，例如 `General` |
| `description` | 定义说明 |
| `code` | 完整的 32 位 Cluster ID |
| `define` | Cluster 的符号名称，建议大写并以下划线分隔 |
| `client`、`server` | 声明支持的角色；不表示已在某个 Endpoint 上启用 |
| `attribute` | 属性定义 |
| `command` | 命令定义 |
| `event` | 事件定义 |
| `mandatoryConform` | 声明必选性；复杂条件应参考当前 SDK 的同类定义 |

名称、ID 和符号应在相应作用域内唯一。重命名可能影响生成代码的名称，因此对已发布定义也应谨慎处理。

## 3 让 ZAP 加载新增 XML

仅把文件放入 SDK 目录，不一定会被 ZAP 自动加载。可选择下面一种方式，同一文件不要重复加载。

### 3.1 通过 zcl.json 加载

先确认 ZAP 当前使用的 `zcl.json`。常见位置包括：

```text
<Matter SDK>/src/app/zap-templates/zcl/zcl.json
```

Silicon Labs 扩展还可能使用：

```text
<Simplicity SDK>/extension/matter_extension/src/app/zap-templates/zcl/zcl.json
```

同一 SDK 中可能存在多份清单，必须修改实际生效的那一份。可以通过 ZAP 加载配置或 `.zap` 中 `type` 为 `zcl-properties` 的 package 路径确认。

检查两个配置项：

- `xmlRoot`：XML 文件的搜索目录。相对路径以该 `zcl.json` 所在目录为基准。
- `xmlFile`：需要加载的 XML 文件名清单。

在现有 `xmlFile` 数组中追加：

```json
"vendor-diagnostic-cluster.xml"
```

上面只是数组中的一个元素，不是完整 JSON。追加时保留原有内容，注意逗号，并保证文件名与实际文件完全一致。

如果 XML 已放在 `xmlRoot` 覆盖的目录，不需要增加搜索路径；如果采用 SDK 内独立厂商目录，则需要同时增加对应 `xmlRoot`。

保存后重新加载或重启 ZAP，确认新 Cluster 出现在预期分类中。保留 SDK 原有清单顺序要求，不要为了新增一个文件重排整个清单。

### 3.2 通过 ZAP Extensions 加载

也可以在 ZAP 中打开 **Extensions**，添加 SDK 目录中的 XML 文件，然后保存配置。此方式同样要求其他开发者的 SDK 中存在该文件，且引用路径能够正确解析。参见 [Silicon Labs 自定义 Cluster 说明](https://docs.silabs.com/matter/2.5.2/matter-references/custom-matter-device)。

如果已经通过 `xmlFile` 加载该文件，就不要再通过 Extensions 重复添加。

## 4 修改自定义 Cluster 的内容

以下片段用于补充前面的示例。属性、命令和事件放在对应 `<cluster>` 内；枚举、结构体等类型定义放在 `<configurator>` 下，与 `<cluster>` 同级。

### 4.1 新增或修改属性

例如新增一个可写的采样周期属性：

```xml
<attribute side="server"
           code="0x0001"
           name="SamplePeriod"
           define="SAMPLE_PERIOD"
           type="int16u"
           min="1"
           max="3600"
           writable="true"
           default="60">
  <mandatoryConform/>
</attribute>
```

| 配置项 | 修改原则 |
| --- | --- |
| `code` | 在该 Cluster 内分配未使用的属性 ID，避开全局属性保留 ID |
| `type` | 明确整数宽度、符号、字符串或复合类型 |
| `min`、`max` | 与类型范围及业务定义一致 |
| `default` | 与类型匹配，并位于允许范围内 |
| `writable` | 声明是否允许写入，不代表业务逻辑已经实现 |
| `name`、`define` | 使用稳定且清晰的名称 |

常见类型包括 `boolean`、`int8u`、`int16u`、`int32u`、`int64s`、`char_string`、`enum8`、`bitmap16`、`array`。准确类型名及可用标签以当前 SDK 为准。

XML 的 `default` 不等于运行时业务缓存自动初始化；XML 也不负责实现存储、写入或订阅上报行为。

### 4.2 新增带参数的命令

例如新增配置采样周期的命令：

```xml
<command source="client" code="0x01" name="SetSamplePeriod">
  <description>Set the sampling period in seconds.</description>
  <arg name="PeriodSeconds" type="int16u"/>
  <mandatoryConform/>
</command>
```

`source="client"` 表示命令由客户端发送、服务端接收；`source="server"` 表示由服务端发送，例如自定义响应。

命令参数的编号和顺序属于协议的一部分。上面的写法沿用常见 SDK 中省略参数编号的格式，不应在已发布命令中随意插入或重排参数；需要显式编号时，按当前 SDK 支持的 XML 格式定义。

### 4.3 定义请求与响应

```xml
<command source="client" code="0x02"
         name="GetSnapshot" response="GetSnapshotResponse">
  <description>Request the current snapshot.</description>
  <mandatoryConform/>
</command>

<command source="server" code="0x03"
         name="GetSnapshotResponse" disableDefaultResponse="true">
  <description>Return the current snapshot.</description>
  <arg name="Value" type="int16u"/>
  <mandatoryConform/>
</command>
```

`response` 必须与响应命令的 `name` 完全一致。定义响应只描述协议关系，不会自动实现返回动作。

### 4.4 定义枚举和结构体

在 `<configurator>` 下添加类型，并通过完整 Cluster ID 建立关联：

```xml
<enum name="DiagnosticModeEnum" type="enum8">
  <cluster code="0xFFF1FC10"/>
  <item name="Normal" value="0x00"/>
  <item name="Extended" value="0x01"/>
</enum>

<struct name="DiagnosticSampleStruct">
  <cluster code="0xFFF1FC10"/>
  <item fieldId="0" name="Value" type="int16u"/>
  <item fieldId="1" name="Mode" type="DiagnosticModeEnum"/>
</struct>
```

然后在 `<cluster>` 内引用该类型，例如：

```xml
<attribute side="server" code="0x0002"
           name="Samples" define="SAMPLES"
           type="array" entryType="DiagnosticSampleStruct"
           writable="false">
  <mandatoryConform/>
</attribute>
```

`fieldId` 是结构体字段的协议编号，应保持唯一、稳定；枚举值也不应在发布后重新分配含义。引用其他 XML 的类型时，确保其文件已加载，并且类型与当前 Cluster 的关联正确。

### 4.5 新增事件

```xml
<event side="server" code="0x00"
       name="SampleChanged" priority="info">
  <description>The diagnostic value changed.</description>
  <field id="0" name="Value" type="int16u"/>
  <mandatoryConform/>
</event>
```

事件使用自己的 ID 空间，可以与属性或命令使用相同数字。事件字段使用 `id`，不要与结构体的 `fieldId` 混淆。定义事件不等于属性变化时会自动产生事件。

## 5 给标准 Cluster 增加厂商扩展

新增独立厂商 Cluster 与扩展标准 Cluster 是两种不同操作。

**扩展标准 Cluster 时，保留标准 Cluster ID，并给新增的厂商属性或命令分配包含 Vendor ID 的完整扩展 ID。** 建议在 SDK 中新建独立扩展 XML，用 `<clusterExtension>`，不要直接改写标准属性或命令的原有定义。

以下示例给 On/Off Cluster `0x0006` 增加一个厂商属性：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configurator>
  <clusterExtension code="0x0006">
    <attribute side="server"
               code="0xFFF10001"
               name="VendorTransitionTime"
               define="VENDOR_TRANSITION_TIME"
               type="int16u"
               writable="true"
               default="0">
      <mandatoryConform/>
    </attribute>
  </clusterExtension>
</configurator>
```

示例属性 ID 的高 16 位是测试 Vendor ID `0xFFF1`，低 16 位是属性编号 `0x0001`。标准 Cluster 内的厂商属性低 16 位范围为 `0x0000～0x4FFF`，厂商命令低 16 位范围为 `0x0000～0x00FF`。这与独立厂商 Cluster 的低 16 位编号范围不同。参见 [Matter 厂商属性和命令扩展规则](https://docs.silabs.com/zap-tool/latest/zap-users-guide/custom-xml)。

扩展文件也需要按第 3 节加入加载配置。

## 6 修改后的检查

1. **XML 语法**：检查标签闭合、引号、编码和转义。文本中的 `&` 应写为 `&amp;`。
2. **ID 唯一性**：检查 Cluster ID，以及 Cluster 内各类元素各自的 ID；检查结构体和事件的字段编号。
3. **类型引用**：检查自定义类型拼写、Cluster 关联和跨文件依赖。
4. **加载路径**：确认改的是当前使用的 SDK 文件和 zcl.json，没有同一模型的重复加载。
5. **ZAP 校验**：重新加载数据模型，检查 Cluster、属性、命令、事件是否显示正确，并处理类型、conformance 和引用错误。
6. **已有配置同步**：XML 修改后，已保存的 ZAP 配置未必自动选择新增元素或覆盖原默认值，需要重新核对。

可以用 PowerShell 检查 XML 是否能被正常解析：

```powershell
$xmlPath = 'C:/SDK/path/vendor-diagnostic-cluster.xml'
[xml]$definition = Get-Content -LiteralPath $xmlPath -Raw -Encoding UTF8
```

该命令只检查 XML 语法，不验证 Matter 语义或 ZAP schema；不能代替 ZAP 校验。

## 7 对外分发与版本维护

提供给其他开发者时，至少附上 XML 文件、适用 SDK/ZAP 版本、SDK 内放置位置，以及 `zcl.json` 的加载变更或 Extensions 加载说明。若引用共享类型，同时说明依赖文件。

对已发布的模型，保留既有 ID、字段编号和数据含义；新增能力优先分配新 ID。变更类型、删除字段或复用旧 ID 都可能破坏控制器兼容性，应按协议版本策略处理，并核对 ClusterRevision。

SDK 更新或重新安装可能覆盖定制文件，建议将 XML 和清单变更保存为补丁或纳入独立版本库。不要把自动生成的头文件当作 XML 定义的替代品。
