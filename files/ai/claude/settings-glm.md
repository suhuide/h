[hrf](../../../hrf.md)  
[ai](../ai.md)  

```c
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "xxx",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5-air",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.1",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.1"
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