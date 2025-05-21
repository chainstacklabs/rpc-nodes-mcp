import base64

import base58
from mcp.types import CallToolResult

from common.utils import _err, _ok
from servers.solana.server import mcp

LAMPORTS_PER_SOL = 10**9


@mcp.tool(
    name="convert_lamports_to_sol",
    description="""
    Converts lamport amount (int or string) into SOL (decimal).
    Example:
    convert_lamports_to_sol("1000000000") -> 1.0
    """,
    annotations={"title": "Lamports to SOL", "readOnlyHint": True},
)
def convert_lamports_to_sol(lamports: str) -> CallToolResult:
    try:
        return _ok(int(lamports) / LAMPORTS_PER_SOL)
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="convert_sol_to_lamports",
    description="""
    Converts SOL amount (decimal string or float) into lamports (integer).
    Example:
    convert_sol_to_lamports("1.5") -> 1500000000
    """,
    annotations={"title": "SOL to Lamports", "readOnlyHint": True},
)
def convert_sol_to_lamports(sol: str) -> CallToolResult:
    try:
        return _ok(int(float(sol) * LAMPORTS_PER_SOL))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="base58_to_base64",
    description="""
    Converts a base58 string into a base64-encoded string.
    Example:
    base58_to_base64("3CMCRgEm8HVz3DrWaCCid3vAANE42jcEv9") -> "MTIzNDU2Nzg5MA=="
    """,
    annotations={"title": "Base58 to Base64", "readOnlyHint": True},
)
def base58_to_base64(value: str) -> CallToolResult:
    try:
        return _ok(base64.b64encode(base58.b58decode(value)).decode())
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="base64_to_base58",
    description="""
    Converts a base64 string into a base58-encoded string.
    Example:
    base64_to_base58("MTIzNDU2Nzg5MA==") -> "3CMCRgEm8HVz3DrWaCCid3vAANE42jcEv9"
    """,
    annotations={"title": "Base64 to Base58", "readOnlyHint": True},
)
def base64_to_base58(value: str) -> CallToolResult:
    try:
        return _ok(base58.b58encode(base64.b64decode(value)).decode())
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="convert_microlamports_to_lamports",
    description="""
    Converts microlamport amount (int or string) into lamports (decimal).
    Example:
    convert_microlamports_to_lamports("1000000") -> 1.0
    """,
    annotations={"title": "Microlamports to Lamports", "readOnlyHint": True},
)
def convert_microlamports_to_lamports(microlamports: str) -> CallToolResult:
    try:
        return _ok(int(microlamports) / 1000000)
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="convert_lamports_to_microlamports",
    description="""
    Converts lamport amount (int or string) into microlamports (integer).
    Example:
    convert_lamports_to_microlamports("2.5") -> 2500000
    """,
    annotations={"title": "Lamports to Microlamports", "readOnlyHint": True},
)
def convert_lamports_to_microlamports(lamports: str) -> CallToolResult:
    try:
        return _ok(int(float(lamports) * 1000000))
    except Exception as e:
        return _err(str(e))
