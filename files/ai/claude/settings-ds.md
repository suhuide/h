[hrf](../../../hrf.md)  
[ai](../ai.md)  

```c
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "xxx",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_EFFORT_LEVEL": "max",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro"
  },
  "permissions": {
    "allow": [
      "Bash(find . -type f -name *.md -o -name *.json -o -name *.yaml -o -name *.yml -o -name *.js -o -name *.ts -o -name *.py)",
      "Bash(grep -E \"\\\\.\\(py|md|json|txt\\)$\")",
      "Bash(ls -la *.json)",
      "mcp__codegraph__codegraph_search",
      "mcp__codegraph__codegraph_context",
      "mcp__codegraph__codegraph_callers",
      "mcp__codegraph__codegraph_callees",
      "mcp__codegraph__codegraph_impact",
      "mcp__codegraph__codegraph_node",
      "mcp__codegraph__codegraph_status",
      "Bash(ls \"C:\\\\hrf\\\\h\\\\files\\\\matter\")",
      "Read(//c/hrf/h/files/matter/**)",
      "Bash(ls -la \"C:\\\\hrf\\\\bk\\\\ota\\\\\")",
      "Read(//c/hrf/bk/**)",
      "Bash(cmake --build build --config base --target bk01_matter)",
      "mcp__codegraph__codegraph_explore"
    ],
    "additionalDirectories": [
      "C:\\hrf\\h\\files\\matter"
    ]
  },
  "enabledPlugins": {
    "fullstack-dev-skills@fullstack-dev-skills": true,
    "document-skills@anthropic-agent-skills": true
  },
  "extraKnownMarketplaces": {
    "fullstack-dev-skills": {
      "source": {
        "source": "github",
        "repo": "jeffallan/claude-skills"
      }
    },
    "anthropic-agent-skills": {
      "source": {
        "source": "github",
        "repo": "anthropics/skills"
      }
    }
  },
  "autoUpdatesChannel": "latest",
  "theme": "dark"
}
```