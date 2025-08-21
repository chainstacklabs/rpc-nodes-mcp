# AGENTS Guidelines for This Repository

This repository contains MCP (Model Context Protocol) servers for blockchain RPC node interactions. When working on the project interactively with an agent (e.g. the Codex CLI) please follow the guidelines below for efficient development and testing.

## 1. Use MCP Inspector for Development

* **Always use MCP Inspector** for testing server functionality.
* **Test with minimal RPC calls first** to verify connectivity.
* **Do _not_ make excessive RPC calls** during development to avoid rate limits.
* **Monitor response times** for performance optimization.

Run MCP Inspector:
```bash
npx @modelcontextprotocol/inspector uv run main_evm.py
npx @modelcontextprotocol/inspector uv run main_solana.py
npx @modelcontextprotocol/inspector uv run main_pumpfun.py
```

## 2. Keep Dependencies in Sync

If you update dependencies:

1. Use uv to manage packages: `uv pip install -r pyproject.toml`.
2. For development: `uv pip install -r pyproject.toml -e '.[dev]'`.
3. For testing: `uv pip install -r pyproject.toml -e '.[test]'`.
4. Verify compatibility with Python 3.13+ as specified in the project.

## 3. Environment Configuration

Create a `.env` file with RPC endpoints (optional, defaults provided):

```env
# EVM Chains
ARBITRUM_RPC_URL=
BASE_RPC_URL=
BINANCE_SMART_CHAIN_RPC_URL=
ETHEREUM_RPC_URL=
SONIC_RPC_URL=

# Solana
SOLANA_RPC_URL=

# For testing scripts only
OPENAI_API_KEY=
```

## 4. Code Quality Checks

Before completing any task, run these quality checks:

| Command               | Purpose                           |
| --------------------- | --------------------------------- |
| `ruff format`         | Format code to standards         |
| `ruff check`          | Run linting checks               |
| `ruff check --fix`    | Auto-fix linting issues          |
| `pytest`              | Run test suite                   |
| `pytest --cov`        | Run tests with coverage          |

## 5. Testing Workflow

Test changes progressively:

1. **Unit tests**: Test individual tools
   ```bash
   pytest tests/test_mcp_ethereum_tools.py
   pytest tests/test_mcp_solana_tools.py
   ```

2. **Integration testing**: Test with MCP Inspector
   ```bash
   npx @modelcontextprotocol/inspector uv run main_evm.py
   ```

3. **Client testing**: Test with example client
   ```bash
   uv run scripts/run_mcp_client_example.py
   ```

## 6. Server Development

When modifying MCP servers:

* Follow the modular structure in `src/servers/`.
* Keep chain-specific logic in `chains/` subdirectories.
* Register tools properly in `tool_registry.py`.
* Maintain interfaces in `common/interfaces.py`.
* Use proper error handling for RPC failures.

## 7. Tool Generation

For auto-generating tools from OpenAPI specs:

```bash
# Generate EVM tools
uv run scripts/generate_mcp_tools.py scripts/openapi_specs/ethereum/ethereum.json scripts/generated ethereum

# Generate Solana tools
uv run scripts/generate_mcp_tools.py scripts/openapi_specs/solana/solana.json scripts/generated solana
```

Note: Generated tools require manual review and improvements.

## 8. RPC Best Practices

* Use batch requests when possible for efficiency.
* Implement proper retry logic for failed requests.
* Handle rate limiting gracefully.
* Cache frequently requested data when appropriate.
* Use appropriate RPC methods for the chain.

## 9. MCP Server Configuration

### For Cursor
Use the installation buttons in README or configure manually in Cursor settings.

### For VS Code
Place `mcp.json` in `.vscode/` folder within your project.

### For Claude Desktop
Place `claude_desktop_config.json` in Claude Desktop data folder.

## 10. Common Development Tasks

### Add New Chain Support
1. Create chain adapter in `src/servers/[platform]/chains/`
2. Register in adapter registry
3. Add RPC URL to environment variables
4. Update configuration files
5. Add tests for new chain

### Add New Tool
1. Define tool in appropriate `tools/` directory
2. Register in `tool_registry.py`
3. Add interface if needed
4. Write unit tests
5. Test with MCP Inspector

### Debug RPC Issues
```bash
# Enable debug logging
export DEBUG=true
uv run main_evm.py
```

## 11. Project Structure

Maintain the modular structure:

```
src/
├── common/           # Shared utilities
├── servers/
│   ├── evm/         # EVM chain servers
│   │   ├── chains/  # Chain-specific adapters
│   │   ├── common/  # EVM-specific common code
│   │   └── tools/   # EVM tools
│   ├── solana/      # Solana servers
│   └── pumpfun/     # Pump.fun tools
```

## 12. Useful Commands Recap

| Command                                      | Purpose                        |
| -------------------------------------------- | ------------------------------ |
| `uv pip install -r pyproject.toml`          | Install base dependencies      |
| `npx @modelcontextprotocol/inspector uv run main_evm.py` | Test EVM server |
| `pytest`                                     | Run all tests                  |
| `ruff format && ruff check`                 | Format and lint               |
| `uv run scripts/run_mcp_client_example.py`  | Test with client              |

## 13. Safety Reminders

* **Never commit API keys** or sensitive RPC endpoints.
* **Use public RPC endpoints** for development when possible.
* **Rate limit your requests** to avoid bans.
* **Test with testnets** before mainnet operations.
* **Validate all RPC responses** for errors.

## 14. Troubleshooting

### Common Issues

**"uv not found"**
- Specify full path to uv in configuration files
- Run `where uv` (Windows) or `which uv` (Unix) to get path

**"RPC request failed"**
- Check RPC endpoint is accessible
- Verify rate limits not exceeded
- Ensure proper network connectivity

**"Tool not found"**
- Verify tool is registered in tool_registry
- Check MCP server is running correctly
- Ensure proper imports in __init__ files

---

Following these practices ensures reliable MCP server development, prevents RPC abuse, and maintains code quality. Always test thoroughly with MCP Inspector before deploying servers to production environments.