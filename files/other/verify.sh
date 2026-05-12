#!/bin/bash
NODE_ID=2250
ENDPOINT=0
CHIP_TOOL="sudo ./chip-tool"

echo "=== ICD Management Cluster 参数验证 ==="

# 统一读取函数
check_icd_attr() {
    local attr_chip=$1          # chip-tool 中的属性名（例如 idle-mode-duration）
    local attr_desc=$2          # 描述名称（用于显示）
    local expected=$3
    echo -n "[ICD Mgmt] $attr_desc 期望: $expected -> "
    output=$($CHIP_TOOL icdmanagement read $attr_chip $NODE_ID $ENDPOINT 2>&1)
    actual=$(echo "$output" | grep -oE '(Data = [0-9]+|'$attr_chip': [0-9]+)' | head -1 | grep -oE '[0-9]+')
    if [ -z "$actual" ]; then
        echo "✗ 读取失败（可能属性名不对）"
        echo "$output" | head -3 | sed 's/^/    /'
    elif [ "$actual" -eq "$expected" ]; then
        echo "✓ 匹配 (实际值: $actual)"
    else
        echo "✗ 不匹配 (实际值: $actual)"
    fi
}

# 读取所有 ICD Management 属性
check_icd_attr "idle-mode-duration"       "IdleModeDuration (SIT回退用)"        3600
check_icd_attr "active-mode-duration"     "ActiveModeDuration (SIT用)"          0
check_icd_attr "active-mode-threshold"    "ActiveModeThreshold"                 25000
check_icd_attr "feature-map"              "FeatureMap (bit0=1 for LIT)"         2
check_icd_attr "cluster-revision"         "ClusterRevision"                     3

echo ""
echo "=== Basic Information Cluster 参考信息 ==="
# Basic Information 的 SpecificationVersion (Matter 版本编码)
spec_output=$($CHIP_TOOL basicinformation read specification-version $NODE_ID $ENDPOINT 2>&1)
spec_ver=$(echo "$spec_output" | grep -oE 'Data = [0-9]+' | grep -oE '[0-9]+')
if [ -n "$spec_ver" ]; then
    major=$(( (spec_ver >> 24) & 0xFF ))
    minor=$(( (spec_ver >> 16) & 0xFF ))
    patch=$(( (spec_ver >> 8) & 0xFF ))
    echo "SpecificationVersion: $spec_ver (Matter $major.$minor.$patch)"
else
    echo "SpecificationVersion: 读取失败"
fi
