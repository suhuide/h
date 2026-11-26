[hrf](../../../hrf.md)  
[ai](../ai.md)  

```c
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "xxx",
    "ANTHROPIC_BASE_URL": "https://dashscope.aliyuncs.com/apps/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro"
  },
  "permissions": {
    "allow": [
      "Bash(find . -type f -name *.md -o -name *.json -o -name *.yaml -o -name *.yml -o -name *.js -o -name *.ts -o -name *.py)",
      "Bash(grep -E \"\\\\.\\(py|md|json|txt\\)$\")",
      "Bash(ls -la *.json)"
    ]
  },
  "enabledPlugins": {
    "fullstack-dev-skills@fullstack-dev-skills": true
  },
  "autoUpdatesChannel": "latest",
  "theme": "dark",
  "extraKnownMarketplaces": {
    "fullstack-dev-skills": {
      "source": {
        "source": "github",
        "repo": "jeffallan/claude-skills"
      }
    }
  }
}
```