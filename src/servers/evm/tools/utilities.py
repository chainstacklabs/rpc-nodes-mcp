"""MCP tools for post-processing JSON-RPC responses."""

import datetime

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


@mcp.tool(
    name="convert_hex_to_int",
    description="""
    Converts a hexadecimal string (e.g., block number, gas used) into an integer.

    Example:
    convert_hex_to_int("0x10") -> 16
    """,
    annotations={"title": "Hexadecimal to Integer", "readOnlyHint": True},
)
def convert_hex_to_int(hex_str: str) -> CallToolResult:
    try:
        return _ok(int(hex_str, 16))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="convert_int_to_hex",
    description="""
    Converts an integer to a hexadecimal string prefixed with 0x.

    Example:
    convert_int_to_hex(255) -> "0xff"
    """,
    annotations={"title": "Integer to Hexadecimal", "readOnlyHint": True},
)
def convert_int_to_hex(value: int) -> CallToolResult:
    try:
        return _ok(hex(value))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="convert_timestamp_to_datetime",
    description="""
    Converts a Unix timestamp (decimal or hex string) into an ISO 8601 datetime.

    Example:
    convert_timestamp_to_datetime("1716300000") -> "2024-05-21T12:00:00Z"
    convert_timestamp_to_datetime("0x660b6c80") -> "2024-03-31T00:00:00Z"
    """,
    annotations={"title": "Timestamp to ISO DateTime", "readOnlyHint": True},
)
def convert_timestamp_to_datetime(timestamp: str) -> CallToolResult:
    try:
        ts = int(timestamp, 16) if timestamp.startswith("0x") else int(timestamp)
        return _ok(datetime.datetime.utcfromtimestamp(ts).isoformat() + "Z")
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="format_gas_price_in_gwei",
    description="""
    Converts gas price in Wei (hex or int string) to Gwei (decimal).

    Example:
    format_gas_price_in_gwei("0x3b9aca00") -> 1.0
    format_gas_price_in_gwei("1000000000") -> 1.0
    """,
    annotations={"title": "Gas Price (Wei) to Gwei", "readOnlyHint": True},
)
def format_gas_price_in_gwei(gas_price: str) -> CallToolResult:
    try:
        wei = int(gas_price, 16) if gas_price.startswith("0x") else int(gas_price)
        return _ok(wei / 1e9)
    except Exception as e:
        return _err(str(e))
