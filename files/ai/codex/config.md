```c
DEEPSEEK_API_KEY = "xxx"
model_provider = "DeepSeek"
model = "deepseek-v4-pro"

[model_providers.DeepSeek]
name = "DeepSeek"
base_url = "https://api.deepseek.com/v1"   # 使用标准 OpenAI base URL
env_key = "DEEPSEEK_API_KEY"
wire_api = "responses"                     # Codex 新版要求

# 可选：启用思考模式（对应 deepseek-v4-pro 的 thinking 功能）
[model_providers.DeepSeek.options]
thinking_enabled = true
reasoning_effort = "high"

[projects.'c:\users\huide\Destop']
trust_level = "trusted"

[tui.model_availability_nux]
"gpt-5.5" = 1

[windows]
sandbox = "elevated"
```