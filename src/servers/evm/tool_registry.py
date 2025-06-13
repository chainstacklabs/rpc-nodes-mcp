# src/servers/evm/tool_registry.py
from mcp.server.fastmcp import FastMCP

# Global MCP instance
mcp = FastMCP("EvmJsonRpcNodeMCP")


def get_mcp_server():
    return mcp
