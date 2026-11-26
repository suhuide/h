# 烧录工具操作手册 (User Guide)

---

## 一、工具概述

烧录工具核心位于 `mfg\matter_mfg_tool_2.5.9\`，是一个 Matter 设备量产烧录软件，用于给 EFR32MG24 等芯片烧录固件、证书和安全密钥。

### 工具目录结构

```
matter_mfg_tool_2.5.9\
├── mfg_tool.exe          ← 主程序，双击启动
├── config.json           ← 指向当前项目的 mfg_config.json (可通过GUI界面导入)
├── firmware\             ← 工具内部固件（基础镜像，区分签名/未签名）
│   ├── gfw_efr32_v2_mg24a.s37    ← 当前使用的基础固件（MG24A芯片）
│   ├── gfw_efr32_v2_mg24b.s37    ← MG24B芯片用
│   └── se_key\            ← SE安全密钥（工具自带的参考密钥）
├── third_party\           ← 第三方烧录工具
│   ├── SimplicityCommanderCLI\  ← SiLabs Commander (EFR32烧录)
│   ├── ASR_downloader_V1.1.2\   ← ASR芯片烧录
│   └── BK_tool\                 ← BK芯片烧录
└── log\                   ← 生产记录
    ├── manufacture_record.txt   ← 烧录记录
    ├── manualcode.txt           ← 最近一次的手动配对码
    ├── qrcode.txt               ← 最近一次的二维码数据
    └── recod_data.xlsx          ← 生产记录Excel
```

### 项目目录结构（以 AOK02 v0.3.0 为例）

每个项目/版本需要开一个独立的目录，例如 `mfg\AOK02-MT2401B-v0.3.0-DC-hrf\`：

```
AOK02-MT2401B-v0.3.0-DC-hrf\
├── mfg_config.json        ← ★ 主配置文件（生产用）
├── debug.json             ← ★ 调试配置文件（开发用）
├── pic.jpg                ← 产品图片
├── cert\                  ← ★ Matter认证证书
│   ├── 0x122f-0x000f-0x{VID}-0x{PID1}.der   ← DAC证书1
│   ├── 0x122f-0x000f-0x{VID}-0x{PID2}.der   ← DAC证书2
│   └── cd-0x{VID}-0x{PID}.der               ← CD证书
├── firmware\              ← ★ 固件文件
│   ├── {name}_bootloader-xxx.s37     ← 引导程序
│   ├── {name}_matter_dc-vX.X.X-signed-xxx.s37  ← 应用程序
│   ├── rail_soc_railtest_xxx.s37     ← RF测试固件
│   └── s2c4_se_fw_upgrade_app_xxx.hex ← SE升级固件
└── se\                    ← ★ 安全引擎密钥
    ├── aes_key.txt               ← AES-128 解密密钥
    ├── sign_pubkey.pem / .txt    ← ECDSA签名公钥
    ├── command_pubkey.pem        ← Commander命令公钥
    ├── user_configuration.json   ← SE配置（芯片型号+安全选项）
    ├── unlock_se.bat             ← SE解锁脚本
    └── write_pubkey_in_lockbit.bat ← 公钥写入脚本
```

---

## 二、运行原理

### 烧录流程

产线操作：**J-Link 有线连接**芯片，操作员扫描模块二维码识别设备(空片可以让其生成二维码)，工具按顺序自动执行以下步骤：

| 顺序 | 步骤 | 对应配置项 | 说明 |
|---|---|---|---|
| 1 | 烧写 SecureEngine | `flash_se` | SE 固件，对应 `firmware/se/*.hex` |
| 2 | 擦除芯片 | `erase_chip` | 量产新芯片开启，回烧旧芯片也建议开启 |
| 3 | 烧写 DAC/PA 证书 | `flash_dac_certs` | 对应 `cert/` 目录下的 `.der` 文件 |
| 4 | 烧写 CD 证书 | `flash_cd_certs` | Certification Declaration |
| 5 | 烧写配网参数 | `flash_verifier` | 写入 discriminator、passcode、BLE UUID 等 |
| 6 | 烧写 Bootloader | `flash_btl` | 对应 `firmware/*bootloader*.s37` |
| 7 | 烧写应用程序 | `flash_app` | 对应 `firmware/*matter_dc*.s37` |

以上 7 步走完后，工具还会执行：
- `secure_boot`：使能 Secure Boot + 写入 Sign PubKey + SE 配置
- `gbl_decrypt_key`：写入 GBL 解密密钥（AES Key）
- 生成二维码 + 手动配对码 → 打印标签

### 工具内部 GFW 固件 vs 项目固件（重要！）

| 位置 | 用途 |
|---|---|
| `matter_mfg_tool_2.5.9\firmware\gfw_efr32_v2_mg24a.s37` | **GFW 基础固件**（含引导+应用），工具启动时先下载到芯片作为运行基础，然后再在上面写入项目的 bootloader 和 app。新空芯片用未签名版，已开 Secure Boot 的芯片用签名版 |
| `{项目}\firmware\{name}_bootloader-xxx.s37` | **项目引导程序**，由 mfg_config.json/debug.json 指定 |
| `{项目}\firmware\{name}_matter_dc-xxx.s37` | **项目应用程序**，由 mfg_config.json/debug.json 指定 |

---

## 三、新项目烧录需要改什么

### 场景：从 AOK02 换成 BK01（不同的客户不同的产品）

以实际案例说明：产线原来烧 AOK02-MT2401B-v0.3.0-DC-hrf，现在要切换到 BK01-MT2401B-v0.0.4-hrf。如果还是用HRF DAC,则两者 VID/PID 相同（0x1470/0xFF01），但固件、SE 密钥、产品品牌不同。

以下逐一列出所有需要改动的文件和内容：

---

#### 步骤 1：创建新的项目目录

在 `mfg\` 下新建目录：`BK01-MT2401B-v0.0.4-hrf`

内部创建三个子目录：`cert\`、`firmware\`、`se\`

---

#### 步骤 2：准备证书文件 → 放入 `cert\`

| 文件 | BK01 | AOK02 | 是否要改 |
|---|---|---|---|
| `0x122f-0x000f-0x1470-0x8005.der` | 243 bytes | 243 bytes | 本配置未使用 |
| `0x122f-0x000f-0x1470-0xff01.der` | 241 bytes | 241 bytes | 本配置未使用 |
| `cd-0x1470-0xff01.der` | 244 bytes | 244 bytes | **用的是HRF DAC,在json文件配置** |

> 证书是 Matter CSA 联盟按 VID/PID 签发的。当前用的是HRF DAC，BK01 和 AOK02 共用 VID=0x1470 / PID=0xFF01，所以 cert\ 目录可以直接从 AOK02 复制过来。
>
> **如果新项目的 VID/PID 不同，则证书文件必须对应更换。**

---

#### 步骤 3：准备固件文件 → 放入 `firmware\`

| 文件 | BK01 | AOK02 | 是否要改 |
|---|---|---|---|
| Bootloader | `bk01_bootloader-v2-signed-30cbab01.s37` | `aok02_bootloader-v3-signed-fa98105c.s37` | **需替换** |
| 应用程序 | `bk01_matter-v0.0.4-signed-31c15004.s37` | `aok02_matter_dc-v0.3.0-signed-e956f33a.s37` | **需替换** |
| SE 固件 | `s2c4_se_fw_upgrade_app_2v2p5.hex` | `s2c4_se_fw_upgrade_app_2v2p5.hex` | 根据实际情况来，一般不变 |
| Railtest | `rail_soc_railtest_mt2401b.s37` | `rail_soc_railtest_mt2401b.s37` | 根据实际情况来，一般不变 |

> 固件文件由固件工程师提供。必须使用 **签名版** (signed)，因为量产芯片开启了 Secure Boot。SE 固件和 Railtest 是 SiLabs 通用文件，通常不变。

---

#### 步骤 4：准备 SE 密钥 → 放入 `se\`

**这是最容易遗漏的部分。** BK01 和 AOK02 使用完全不同的密钥：

| 文件 | BK01 | AOK02 | 是否要改 |
|---|---|---|---|
| `aes_key.txt` | `TOKEN_MFG_SECURE_BOOTLOADER_KEY: 0A2BD0FC...` | `...E41F7908...` | **需替换** |
| `sign_pubkey.pem` | 不同的 ECDSA P-256 公钥 | — | **需替换** |
| `sign_pubkey.txt` | X=`9B2B9511...`, Y=`46EB27B3...` | X=`308BC18F...`, Y=`727E902C...` | **需替换** |
| `command_pubkey.pem` | 不同的命令公钥 | — | **需替换** |
| `user_configuration.json` | OPN=`EFR32MG24A410F1536IM40` | 相同 | 不变（同款芯片） |
| `unlock_se.bat` | 相同命令 | 相同 | 不变 |
| `write_pubkey_in_lockbit.bat` | 相同命令 | 相同 | 不变 |

> 关键：**aes_key.txt + sign_pubkey.pem + sign_pubkey.txt + command_pubkey.pem 这四个文件必须配套更换**。它们由 Secure Boot 密钥生成流程产出（见 `matter_mfg_tool_2.5.9\firmware\se_key\readme.md`）。烧录时工具会把 sign_pubkey 和 aes_key 写入芯片的 OTP（一次性写入，不可逆），密钥不匹配会导致芯片变砖。

---

#### 步骤 5：编辑 `mfg_config.json` ★ 核心

以 AOK02 的 `mfg_config.json` 为模板，修改以下字段：

**产品标识（必须改）：**

| 字段 | AOK02 值 | BK01 值 |
|---|---|---|
| `hardware` | `"AOK02-DC"` | `"cc"`（或自定义代号） |
| `vendor_name` | `"A-OK"` | `"BK"` |
| `product_name` | `"Window Covering"` | 按实际填 |
| `product_label` | `"Window Covering"` | 按实际填 |
| `part_number` | `"Window Covering"` | 按实际填 |
| `product_url` | `"https://www.aoksz.com/"` | `"https://www.bk.com/"` |

**固件文件名（必须改）：**

| 字段 | AOK02 值 | BK01 值 |
|---|---|---|
| `firmware.bootloader` | `aok02_bootloader-v3-signed-fa98105c.s37` | `bk01_bootloader-v2-signed-30cbab01.s37` |
| `firmware.application` | `aok02_matter_dc-v0.3.0-signed-e956f33a.s37` | `bk01_matter-v0.0.4-signed-31c15004.s37` |

**VID/PID（用HRF DAC故不变，BK01 和 AOK02 共用）：**

```json
"vendor_id": 5232,
"product_id": 65281,
"cd_cert": "cd-0x1470-0xff01.der",
```

> 如果新项目的 VID 或 PID 不同，`vendor_id`、`product_id`、`cd_cert` 全部要对应修改。

---

#### 步骤 6：编辑 `debug.json`

同样以 AOK02 的 `debug.json` 为模板，同步修改上面步骤 5 中列出的所有字段（hardware、vendor_name、固件文件名等）。

`debug.json` 与 `mfg_config.json` 的差异点保持不变：
- `hardware` 名称加调试标识（如 `"bk01_matter-v0.0.1-signed-69e44212"`）
- `erase_chip: true`（调试时先擦除）
- `flash_se: false`（调试时不重新烧 SE）
- `ui_lock: false`（调试时不锁界面）

---

#### 步骤 7：修改工具配置指向新项目(可在后期使用时通过GUI界面导入)

编辑 `mfg\matter_mfg_tool_2.5.9\config.json`：

```json
{
    "config_name": "D:/hrf/mfg/BK01-MT2401B-v0.0.4-hrf/mfg_config.json"
}
```

---

#### 步骤 8：更新工具内部 GFW 固件 ★ 容易遗漏

工具 `firmware\` 目录下的 `gfw_efr32_v2_mg24a.s37` 也区分签名版本。从 AOK 切到 BK 时，需要切换到 BK 签名的 GFW 固件：

```bash
# 进入工具 firmware 目录
cd D:\hrf\mfg\matter_mfg_tool_2.5.9\firmware

# 切换到 BK 签名版
signed-bk.bat

# 或者如果是新空芯片（未开 Secure Boot）
unsigned.bat
```
```c
huide@eric-pc MINGW64 /d/hrf/mfg/matter_mfg_tool_2.5.9/firmware
$ ls -1
gfw_efr32_v1.s37
gfw_efr32_v2_mg24a-signed-aok.s37
gfw_efr32_v2_mg24a-signed-bk.s37
gfw_efr32_v2_mg24a-unsigned.s37
gfw_efr32_v2_mg24a.s37
gfw_efr32_v2_mg24b.s37
signed-aok.bat
signed-bk.bat
unsigned.bat
```
##### signed-aok.bat
```c
del gfw_efr32_v2_mg24a.s37
copy gfw_efr32_v2_mg24a-signed-aok.s37 gfw_efr32_v2_mg24a.s37
```
##### signed-bk.bat
```c
del gfw_efr32_v2_mg24a.s37
copy gfw_efr32_v2_mg24a-signed-bk.s37 gfw_efr32_v2_mg24a.s37
```
##### unsigned.bat
```c
del gfw_efr32_v2_mg24a.s37
copy gfw_efr32_v2_mg24a-unsigned.s37 gfw_efr32_v2_mg24a.s37
```
| 场景 | 执行 |
|---|---|
| 全新空芯片（首次烧录） | `unsigned.bat` |
| 已开 Secure Boot 的 AOK 芯片 | `signed-aok.bat` |
| 已开 Secure Boot 的 BK 芯片 | `signed-bk.bat` |

**GFW 固件选择要点：**

> - `gfw_efr32_v2_mg24a.s37` 是工具启动时首先加载的固件，必须确保使用正确的版本。
> - **空芯片（未开 Secure Boot）**：使用未签名版。手动操作就是把 `gfw_efr32_v2_mg24a-unsigned.s37` 重命名为 `gfw_efr32_v2_mg24a.s37`（或直接运行 `unsigned.bat`）。
> - **已开 Secure Boot 的芯片**：必须使用签名版，否则芯片会拒绝启动。根据产品选择 `signed-aok.bat` 或 `signed-bk.bat`。
> - `gfw_efr32_v2_mg24a.s37` 适用于 **Mid Secure-Vault** 类型芯片，如 HM-MT2401A、HM-MT2401B。
> - `gfw_efr32_v2_mg24b.s37` 适用于 **High Secure-Vault** 类型芯片。

---

### 新项目 check list 汇总

- [ ] 创建项目目录 + cert/firmware/se 子目录
- [ ] cert\：复制/准备 3 个证书文件（VID/PID 相同则复用）
- [ ] firmware\：放入 4 个固件文件（bootloader + app **需替换**，SE FW + railtest FW 通常复用）
- [ ] se\：放入 7 个文件（aes_key/sign_pubkey/command_pubkey **需替换**，其余复用）
- [ ] 修改 mfg_config.json（hardware、vendor_name、固件文件名）
- [ ] 修改 debug.json（同步 mfg_config.json 的改动）
- [ ] 修改工具 config.json，指向新项目目录(可通过GUI界面导入)
- [ ] 更新工具 firmware\gfw_efr32_v2_mg24a.s37（运行对应 .bat）
- [ ] 启动 mfg_tool.exe 验证

---

## 四、同一项目新固件版本需要改什么

### 场景：AOK02 从 v0.1.7 升级到 v0.3.0，只更新应用程序固件

#### 只需改 3 处：

**1. 放入新的固件文件**

将新的应用程序 .s37 文件复制到 `{项目}\firmware\` 目录。

```
firmware\
├── aok02_bootloader-v3-signed-fa98105c.s37   ← 不变
├── aok02_matter_dc-v0.3.0-signed-e956f33a.s37 ← ★ 新文件
├── rail_soc_railtest_mt2401b.s37             ← 不变
└── s2c4_se_fw_upgrade_app_2v2p5.hex         ← 不变
```

旧的应用固件文件可以删除或保留备用。

**2. 修改 `mfg_config.json` 中的固件路径**

```json
"firmware": {
    "application": "aok02_matter_dc-v0.3.0-signed-e956f33a.s37"  ← 改成新文件名
}
```

**3. 同步修改 `debug.json` 中的固件路径**（如果使用）

```json
"firmware": {
    "application": "aok02_matter_dc-v0.3.0-signed-e956f33a.s37"  ← 改成新文件名
}
```

#### 不需要改的：

| 项目 | 说明 |
|---|---|
| `cert\` | 证书不变（VID/PID 没变） |
| `se\` | 密钥不变 |
| `vendor_id / product_id` | 产品标识不变 |
| `printer` 配置 | 标签不变 |
| `qrconfig` | 二维码布局不变 |
| 工具 `config.json` | 指向同一个 mfg_config.json，不变 |
| 工具 `firmware\gfw_efr32_v2_mg24a.s37` | 基础固件不变（除非引导程序也有更新） |

#### 如果引导程序也更新了：

额外替换 `firmware\{name}_bootloader-xxx.s37`，并在 `mfg_config.json` 和 `debug.json` 中更新 `bootloader` 文件名。

#### 如果 SE 固件更新了（极少见）：

替换 `firmware\s2c4_se_fw_upgrade_app_xxx.hex`，并在两个 json 中更新 `se` 文件名。

---

## 五、日常生产操作

### 启动烧录工具

1. 确保烧录器（J-Link）已连接芯片
2. 双击 `mfg\matter_mfg_tool_2.5.9\mfg_tool.exe`
3. 扫描模块上的二维码，工具自动识别设备
4. 点击"烧录"，等待进度条完成
5. 查看结果（OK/ERR），如需打印标签，点击打印

### 切换生产项目

两步操作：
1. 编辑 `mfg\matter_mfg_tool_2.5.9\config.json`，将 `config_name` 改为目标项目的 `mfg_config.json` 路径，可通过GUI界面导入
2. 进入 `mfg\matter_mfg_tool_2.5.9\firmware\`，运行对应的 `.bat` 切换 GFW 签名版本（`signed-aok.bat` / `signed-bk.bat` / `unsigned.bat`）

重启工具即可。

### 查看生产记录

- 文本记录：`matter_mfg_tool_2.5.9\log\manufacture_record.txt`
- Excel 记录：`matter_mfg_tool_2.5.9\log\recod_data.xlsx`

每条记录格式：`日期 时间  MT:{二维码数据}  {手动配对码}  OK/ERR`

### 切换签名/未签名 GFW 固件

- 全新空芯片（未开 Secure Boot） → 运行 `unsigned.bat`
- 已开 Secure Boot 的 AOK 芯片 → 运行 `signed-aok.bat`
- 已开 Secure Boot 的 BK 芯片 → 运行 `signed-bk.bat`

---

## 六、常见问题

| 问题 | 原因 | 解决 |
|---|---|---|
| 烧录失败 ERR | 芯片已有 Secure Boot，但用了未签名 GFW 固件 | 运行对应签名 .bat（signed-aok / signed-bk） |
| 烧录失败 ERR | 芯片与 GFW 固件不匹配 (MG24A vs MG24B) | 检查 `gfw_efr32_v2_mg24a.s37` 是否对应芯片型号 |
| GFW 固件与项目不符 | config.json 指向 A 项目但 GFW 固件是 B 的签名 | 改到与项目匹配的配置 |
| J-Link 连接失败 | 芯片未上电或接线松动 | 检查 J-Link 排线、芯片供电 |

