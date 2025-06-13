# src/servers/solana/tool_registry.py
from mcp.server.fastmcp import FastMCP

# Global MCP instance
mcp = FastMCP("SolanaJsonRpcNodeMCP")


def get_mcp_server():
    return mcp
