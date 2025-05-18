# MCP to access blockchain RPC nodes

Minimal, fast, and extensible [MCP server](https://modelcontextprotocol.io/introduction) for blockchain transaction analysis.
Supports Ethereum, Solana, and EVM-compatible chains via a clean adapter interface.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/chainstacklabs/rpc-nodes-mcp.git
cd repo
```

### 2. Install Dependencies with `uv`
| Mode       | Command                                           |
|------------|---------------------------------------------------|
| Base       | `uv pip install -r pyproject.toml`                |
| Dev        | `uv pip install -r pyproject.toml -e '.[dev]'`    |
| Test       | `uv pip install -r pyproject.toml -e '.[test]'`   |

## ▶️ Run the Server
```bash
npx @modelcontextprotocol/inspector uv run src/main_evm.py
```
For more details, visit [Model Context Inspector](https://modelcontextprotocol.io/docs/tools/inspector).

## Scripts

A client example which interacts with the MCP server (it requires `OPENAI_API_KEY` env var):
```bash
uv run scripts/run_mcp_client_example.py
```

Auto generation tools and required interfaces based on OpenAPI spec:
```bash
uv run scripts/generate_mcp_tools.py <openapi_path> <output_dir> <blockchain_name>
```
