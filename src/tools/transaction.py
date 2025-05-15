"""
MCP tool for retrieving transaction data from blockchains.
"""

from mcp.types import CallToolResult, TextContent

from core.client import fetch_transaction
from server import mcp


def error_result(message: str) -> CallToolResult:
    return CallToolResult(isError=True, content=[TextContent(type="text", text=message)])


@mcp.tool(
    name="get_transaction",
    description="Returns the full transaction object",
    annotations={
        "title": "",
        "readOnlyHint": True,
        "destructiveHint": False,
    },
)
async def get_transaction(blockchain_name: str, tx_id: str) -> CallToolResult:
    try:
        tx_data = await fetch_transaction(blockchain_name.lower(), tx_id)
        return CallToolResult(content=[TextContent(type="text", text=str(tx_data))])
    except Exception as e:
        return error_result(f"Error: {str(e)}")
