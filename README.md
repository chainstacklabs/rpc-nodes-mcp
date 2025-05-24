# MCP to access blockchain RPC nodes

Minimal, fast, and extensible [MCP servers](https://modelcontextprotocol.io/introduction) for interactions with JSON-RPC blockchain nodes. Support EVM and Solana blockchains.

🍒 Extra feature: tools for pump.fun bonding curve calculations and analysis.

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

### 3. Set environment variables
```
ARBITRUM_RPC_URL=
BASE_RPC_URL=
BINANCE_SMART_CHAIN_RPC_URL=
ETHEREUM_RPC_URL=
SONIC_RPC_URL=

SOLANA_RPC_URL=

OPENAI_API_KEY=
```

**Note:** `OPENAI_API_KEY` is only required for tests with `scripts/run_mcp_client_example.py`.

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
**Note:** auto-generated tools reuire further improvements, see [here](https://github.com/chainstacklabs/rpc-nodes-mcp/blob/main/scripts/README.md).

## Configuration

### VS Code

The `mcp.json` file contains MCP server configurations. For VS Code users, place this file in the `.vscode` folder within your project directory. GitHub Copilot in Agent Mode will automatically discover and launch the configured servers.

### Claude Desktop

The `claude_desktop_config.json` file contains MCP server configurations. For Claude Desktop users, place this file in the Claude Desktop data folder. Claude Desktop will automatically discover and launch the configured servers.

**uv location errors**: specify the full path to `uv` in the `mcp.json` file. To get the full path, run `where uv` command.

**environment variables**: double check you created `.env` file in the MCP servers folder and required endpoints.

### References

- [Cursor](https://docs.cursor.com/context/model-context-protocol#model-context-protocol)
- [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [Claude Desktop](https://modelcontextprotocol.io/quickstart/user#windows)
