"""MCP tools for post-processing JSON-RPC responses."""

from mcp.types import CallToolResult

from common.utils import _err, _ok
from servers.evm.server import mcp


@mcp.tool(
    name="convert_hex_wei_to_decimal_eth",
    description="Returns Eth in decimal format based on passed Wei amount in hexadecimal format.",
    annotations={
        "title": "Convert Wei amount (in hexadecimal format) into Eth amount (in decimal format)",
        "readOnlyHint": True,
    },
)
def convert_wei_to_eth(wei: str) -> CallToolResult:
    try:
        return _ok(int(wei, 16) / 10**18)
    except Exception as e:
        return _err(str(e))
