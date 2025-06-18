from mcp.server.fastmcp import FastMCP

# Global MCP instance
mcp = FastMCP("PumpFunMCP")


def get_mcp_server():
    return mcp
