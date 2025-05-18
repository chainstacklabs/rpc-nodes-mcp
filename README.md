# MCP to access blockchain RPC nodes

Minimal, fast, and extensible [MCP server](https://modelcontextprotocol.io/introduction) for blockchain transaction analysis.
Supports EVM blockchains via a clean adapter interface.

🤖 Run the auto-generation script to generate MCP tools for other blockchains using [OpenAPI specifications](https://github.com/chainstack/dev-portal/tree/main/openapi).
```bash
uv run scripts/generate_mcp_tools.py <openapi_path> <output_dir> <blockchain_name>
```

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

A client example that interacts with the MCP server (requires `OPENAI_API_KEY` environment variable):
```bash
uv run scripts/run_mcp_client_example.py
```

Tool for auto-generating MCP interfaces and implementations (_only tools currently_) based on OpenAPI spec (see [Chainstack open-source docs](https://github.com/chainstack/dev-portal/tree/main/openapi)):
```bash
uv run scripts/generate_mcp_tools.py <openapi_path> <output_dir> <blockchain_name>
```
