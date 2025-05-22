# MCP to access blockchain RPC nodes

Minimal, fast, and extensible [MCP server](https://modelcontextprotocol.io/introduction) for interactions with JSON-RPC blockchain nodes. Supports EVM blockchains.

🤖 Run the auto-generation script to generate MCP tools for other blockchains using [OpenAPI specifications](https://github.com/chainstack/dev-portal/tree/main/openapi).
```bash
uv run scripts/generate_mcp_tools.py <openapi_path> <output_dir> <blockchain_name>

# Example
uv run scripts/generate_mcp_tools.py scripts/openapi_specs/ethereum.json scripts/generated evm
```

## 🚀 Quick start

### 1. Clone the repository
```bash
git clone https://github.com/chainstacklabs/rpc-nodes-mcp.git
cd rpc-nodes-mcp
```

### 2. Install dependencies with `uv`
| Mode       | Command                                           |
|------------|---------------------------------------------------|
| Base       | `uv pip install -r pyproject.toml`                |
| Dev        | `uv pip install -r pyproject.toml -e '.[dev]'`    |
| Test       | `uv pip install -r pyproject.toml -e '.[test]'`   |

### ▶️ Run MCP server
```bash
npx @modelcontextprotocol/inspector uv run src/main_evm.py
```
For more details, visit [Model Context Inspector](https://modelcontextprotocol.io/docs/tools/inspector).

## Scripts

A client example that interacts with the MCP server (requires `OPENAI_API_KEY` environment variable):
```bash
uv run scripts/run_mcp_client_example.py
```

Tool for auto-generating MCP interfaces and implementations (_only tools currently_) based on OpenAPI spec (see [Chainstack open-source docs](https://github.com/chainstack/dev-portal/tree/main/openapi)):
```bash
uv run scripts/generate_mcp_tools.py scripts/openapi_specs/ethereum.json scripts/generated evm
```

## Configuration (VS Code example)

The `mcp.json` file contains MCP server configurations. For VS Code users, place this file in the `.vscode` folder within your project directory. GitHub Copilot in Agent Mode will automatically discover and launch the configured servers.

### Setup

When running for the first time, you'll be prompted to provide:
- **API key**: Your authentication credentials to one of LLM providers
- **Project folder path**: The directory where MCP servers are located (e.g., `C:\Users\Projects\rpc-nodes-mcp`)

Ensure you specify the path to where you copied this project.

### Troubleshooting

**uv location errors**: If you encounter errors related to `uv` location, specify the full path to `uv` in the `mcp.json` file.

**Project path issues**: The project path should point to the root project folder, not the `/src` subdirectory.

### References

- [Cursor](https://docs.cursor.com/context/model-context-protocol#model-context-protocol)
- [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [Claude Desktop](https://modelcontextprotocol.io/quickstart/user#windows)

### Generate LLM API key

- [Mistral](https://console.mistral.ai/api-keys)
- [Claude](https://docs.anthropic.com/en/api/overview)
- [OpenAI](https://platform.openai.com/api-keys)
