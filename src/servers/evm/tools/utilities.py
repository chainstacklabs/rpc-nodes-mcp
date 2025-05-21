"""MCP tools for post-processing JSON-RPC responses."""

from mcp.types import CallToolResult

from common.utils import _err, _ok
from servers.evm.common.adapter_registry import registry
from servers.evm.server import mcp


@mcp.tool(
    name="convert_hex_wei_to_decimal_eth",
    description="Converts Wei amount (in hexadecimal format) into Ether (ETH) in decimal format.",
    annotations={
        "title": "Converts Wei amount (hexadecimal) into Ether amount (decimal)",
        "readOnlyHint": True,
    },
)
def convert_wei_to_eth(wei: str) -> CallToolResult:
    try:
        return _ok(int(wei, 16) / 10**18)
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_supported_blockchains",
    description="Returns the list of blockchain names supported by the MCP server.",
    annotations={
        "title": "",
        "readOnlyHint": True,
    },
)
def get_supported_blockchains() -> CallToolResult:
    try:
        return _ok(list(registry.keys()))
    except Exception as e:
        return _err(str(e))
