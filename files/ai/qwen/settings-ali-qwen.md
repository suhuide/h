[hrf](../../../hrf.md)  
[ai](../ai.md)  

```c
{
  "env": {
    "BAILIAN_API_KEY": "sk-8d3bf4cd827a468784f98f2f0696a671"
  },
  "modelProviders": {
    "openai": [
      {
        "id": "qwen3.6-plus",
        "name": "[Bailian] qwen3.6-plus",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "qwen3-coder-plus",
        "name": "[Bailian] qwen3-coder-plus",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY"
      },
      {
        "id": "qwen3-coder-next",
        "name": "[Bailian] qwen3-coder-next",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY"
      },
      {
        "id": "glm-5.1",
        "name": "[Bailian] glm-5.1",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "MiniMax-M2.5",
        "name": "[Bailian] MiniMax-M2.5",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      },
      {
        "id": "kimi-k2.5",
        "name": "[Bailian] kimi-k2.5",
        "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "envKey": "BAILIAN_API_KEY",
        "generationConfig": {
          "extra_body": {
            "enable_thinking": true
          }
        }
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "qwen3.6-plus"
  },
  "$version": 4,
  "permissions": {
    "allow": [
      "Read(C:\\hrf\\other\\Matter_V_1_5_PICS_XML_For_RPI/**)",
      "Bash(git *)"
    ]
  }
}
```