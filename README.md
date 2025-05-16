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
npx @modelcontextprotocol/inspector uv run src/main.py
```
For more details, visit [Model Context Inspector](https://modelcontextprotocol.io/docs/tools/inspector). There is also a client example which interacts with the MCP server (it requires `OPENAI_API_KEY` env var).
```bash
uv run src/client_example.py
```

## 🧪 Run Tests
```bash
uv run pytest
```

## 🧩 Add a Blockchain Adapter
1. Create a file in `src/chains/`, e.g. `fantom.py`
2. Subclass `EvmAdapter` or implement `BlockchainAdapter`
3. Register the adapter:
   ```python
   @register_adapter("fantom")
   class FantomAdapter(EvmAdapter):
       def __init__(self, rpc_client: RpcClient = None):
           super().__init__(rpc_url=settings.FANTOM_RPC_URL, rpc_client=rpc_client)
   ```

## 🔧 Add a Tool
1. Add a new function in `src/tools/`, use `@mcp.tool(...)`
2. Optionally use `fetch_transaction(...)` from `core.client`
3. Return a `CallToolResult`

Example:
```python
@mcp.tool(name="example_tool")
async def example_tool(...) -> CallToolResult:
    ...
```

## 🧠 Project Structure
```
src/
├── chains/        # Blockchain adapters (EVM & Solana)
├── core/          # Interfaces, RPC client, registry
├── tools/         # MCP-exposed tools
├── prompts/       # Prompt templates
├── tests/         # Unit tests (pytest)
├── config.py      # Environment variable loader
├── main.py        # Entrypoint
├── server.py      # MCP server instance
```
