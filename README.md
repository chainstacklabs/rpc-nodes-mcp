# MCP to access blockchain RPC nodes

Minimal, fast, and extensible [MCP servers](https://modelcontextprotocol.io/introduction) for interactions with JSON-RPC blockchain nodes. Support EVM and Solana blockchains.

<div align="center">
    <img src="https://github.com/user-attachments/assets/f9266d2b-2fc1-48e7-8dad-ef08ad93c07e" alt="Animation">
</div>

🍒 Extra feature: a separate MCP server with tools for pump.fun bonding curve calculations and analysis.

## 🚀 Quick start

### 1. Clone the repository
```bash
git clone https://github.com/chainstacklabs/rpc-nodes-mcp.git
cd rpc-nodes-mcp
```

### 2. Install dependencies with [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
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
npx @modelcontextprotocol/inspector uv run main_evm.py
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
**Note:** auto-generated tools require further improvements, see [here](https://github.com/chainstacklabs/rpc-nodes-mcp/blob/main/scripts/README.md).

## Configuration

### Cursor

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**EVM chains**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Install EVM MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=chainstack-evm-nodes&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1ldm0ifQ%3D%3D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Solana**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Install Solana MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=chainstack-solana-nodes&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1zb2xhbmEifQ%3D%3D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Pump Fun**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=chainstack-pumpfun-tools&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1wdW1wZnVuIn0%3D)


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
