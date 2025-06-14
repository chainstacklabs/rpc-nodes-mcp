# MCP to access blockchain RPC nodes

### EVM chains
[![Install EVM MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rpc-nodes-evm&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1ldm0ifQ%3D%3D)

### Solana 
[![Install Solana MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rpc-nodes-solana&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1zb2xhbmEifQ%3D%3D)

Minimal, fast, and extensible [MCP servers](https://modelcontextprotocol.io/introduction) for interactions with JSON-RPC blockchain nodes. Support EVM and Solana blockchains.

<div align="center">
    <img src="https://github.com/user-attachments/assets/f9266d2b-2fc1-48e7-8dad-ef08ad93c07e" alt="Animation">
</div>

🍒 Extra feature: tools for pump.fun bonding curve calculations and analysis.

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
**Note:** auto-generated tools require further improvements, see [here](https://github.com/chainstacklabs/rpc-nodes-mcp/blob/main/scripts/README.md).

## Configuration

### Cursor

**EVM chains**

[![Install EVM MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rpc-nodes-evm&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1ldm0ifQ%3D%3D)

**Solana** 

[![Install Solana MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rpc-nodes-solana&config=eyJjb21tYW5kIjoidXZ4IC0tZnJvbSBnaXQraHR0cHM6Ly9naXRodWIuY29tL2NoYWluc3RhY2tsYWJzL3JwYy1ub2Rlcy1tY3AuZ2l0IG1jcC1zb2xhbmEifQ%3D%3D)


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

# 🧰 For developers

### Architecture

The project uses a **modular adapter pattern** with automatic registration:

```
src/
├── common/           # Shared utilities (RPC client, logging, config)
├── servers/
│   ├── evm/         # EVM-compatible blockchain support
│   │   ├── chains/  # Individual chain implementations
│   │   ├── common/  # Shared EVM logic
│   │   ├── tools/   # MCP tool definitions
│   │   └── evm.py   # Base EVM adapter
│   └── solana/      # Solana-specific implementation
│       ├── chains/
│       ├── common/
│       ├── tools/
│       └── solana.py
```

### Key components

1. **Adapter registry**: automatically registers blockchain adapters
2. **Abstract interfaces**: define contracts for blockchain operations
3. **RPC client**: handles HTTP requests to blockchain nodes with error handling and logging
4. **MCP tools**: expose JSON-RPC methods as AI-accessible tools
5. **Auto-generation (experimental)**: scripts to generate new tools from OpenAPI specifications

### How it works

1. **Registration**: chain adapters register themselves automatically when imported
2. **Routing**: client dispatcher routes requests to appropriate adapters based on chain name
3. **RPC Communication**: HttpxRpcClient handles JSON-RPC requests with proper error handling
4. **Tool Exposure**: MCP tools wrap adapter methods for AI consumption

## Modifying existing blockchains/tools

### Adding new core tools

1. Update the interface (`src/servers/evm/common/interfaces.py`):

```python
@abstractmethod
async def new_method(self, param1: str, param2: str) -> str: ...
```

2. Implement in base adapter (`src/servers/evm/evm.py`):

```python
async def new_method(self, param1: str, param2: str) -> str:
    return await self.rpc_client.post("new_method", [param1, param2], self.rpc_url)
```

3. Add client router (`src/servers/evm/common/client.py`):

```python
async def new_method(chain, param1, param2):
    return await _adapter(chain).new_method(param1, param2)
```

4. Create MCP tool (`src/servers/evm/tools/json_rpc_methods.py`):

```python
@mcp.tool(
    name="new_method",
    description="Description of what this method does...",
    annotations={"title": "New Method", "readOnlyHint": True},
)
async def new_method(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.new_method(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

```

### Adding utility tools

Create new utility functions in `src/servers/*/tools/utilities.py`:

```python
@mcp.tool(
    name="convert_something",
    description="Converts something to something else",
    annotations={"title": "Convert Something", "readOnlyHint": True},
)
def convert_something(value: str) -> CallToolResult:
    try:
        result = your_conversion_logic(value)
        return _ok(result)
    except Exception as e:
        return _err(str(e))

```

## Adding new blockchains

### For EVM-compatible chains

1. Create chain file (`src/servers/evm/chains/newchain.py`):

```python
from common.config import settings
from common.interfaces import RpcClient
from servers.evm.common.adapter_registry import register_adapter
from servers.evm.evm import EvmAdapter

@register_adapter("newchain")
class NewChainAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.NEWCHAIN_RPC_URL, rpc_client=rpc_client)
```

2. Add environment variable to `.env`:

```bash
NEWCHAIN_RPC_URL=https://your-rpc-endpoint.com
```

3. Import in main (`src/main_evm.py`):
The auto-discovery mechanism will automatically import your new chain.

### For non-EVM chains

1. Create adapter interface (`src/servers/newchain/common/interfaces.py`)
2. Implement base adapter (`src/servers/newchain/newchain.py`)
3. Create chain registration (`src/servers/newchain/chains/newchain.py`)
4. Add client dispatcher (`src/servers/newchain/common/client.py`)
5. Create MCP tools (`src/servers/newchain/tools/`)
6. Create main entry point (`src/main_newchain.py`)
