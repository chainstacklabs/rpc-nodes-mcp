import base64
import struct

import base58
from mcp.types import CallToolResult
from solders.pubkey import Pubkey

from common.utils import _err, _ok
from servers.solana.server import mcp

LAMPORTS_PER_SOL = 1_000_000_000
TOKEN_DECIMALS = 6
EXPECTED_DISCRIMINATOR = struct.pack("<Q", 6966180631402821399)

PUMP_PROGRAM_ID = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
ATA_PROGRAM_ID = "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"


def _parse_bonding_curve_data(data: str, encoding: str) -> dict:
    raw = base64.b64decode(data) if encoding == "base64" else bytes.fromhex(data)
    if raw[:8] != EXPECTED_DISCRIMINATOR:
        raise ValueError("Invalid discriminator for bonding curve")
    fields = struct.unpack_from("<QQQQQ?", raw, 8)
    return {
        "virtual_token_reserves": fields[0],
        "virtual_sol_reserves": fields[1],
        "real_token_reserves": fields[2],
        "real_sol_reserves": fields[3],
        "token_total_supply": fields[4],
        "complete": fields[5],
    }


@mcp.tool(
    name="calculate_bonding_curve_address",
    description="""
    Derive the bonding curve PDA for a given token mint using Pump.fun rules.
    This is for Pump.fun tokens on bonding curve operations.
    
    Parameters:
    - mint (str): The base-58 mint address.

    Returns: Dictionary with 'bonding_curve_address' and 'bump'.
    """,
    annotations={"title": "Calculate bonding curve address", "readOnlyHint": True},
)
def calculate_bonding_curve_address(mint: str) -> CallToolResult:
    try:
        program_id = Pubkey.from_string(PUMP_PROGRAM_ID)
        mint_key = Pubkey.from_string(mint)
        curve, bump = Pubkey.find_program_address([b"bonding-curve", bytes(mint_key)], program_id)
        return _ok({"bonding_curve_address": str(curve), "bump": bump})
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="calculate_associated_bonding_curve_address",
    description="""
    Calculate the associated bonding curve token account address for a mint.
    This is for Pump.fun tokens on bonding curve operations.

    Parameters:
    - mint (str): The base-58 mint address.

    Returns: Base-58 ATA address for bonding curve.
    """,
    annotations={"title": "Associated bonding curve ATA", "readOnlyHint": True},
)
def calculate_associated_bonding_curve_address(mint: str) -> CallToolResult:
    try:
        token_program = Pubkey.from_string(TOKEN_PROGRAM_ID)
        ata_program = Pubkey.from_string(ATA_PROGRAM_ID)
        pump_program = Pubkey.from_string(PUMP_PROGRAM_ID)

        mint_key = Pubkey.from_string(mint)
        curve, _ = Pubkey.find_program_address([b"bonding-curve", bytes(mint_key)], pump_program)
        assoc, _ = Pubkey.find_program_address(
            [bytes(curve), bytes(token_program), bytes(mint_key)], ata_program
        )
        return _ok(str(assoc))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_bonding_curve_data",
    description="""
    Parse bonding curve state from raw account data.
    This is for Pump.fun tokens on bonding curve operations.

    Parameters:
    - data (str): Base64 or hex string.
    - encoding (str): One of 'base64' (default) or 'hex'.

    Returns: Dictionary with parsed curve fields.
    """,
    annotations={"title": "Parse bonding curve state", "readOnlyHint": True},
)
def get_bonding_curve_data(data: str, encoding: str = "base64") -> CallToolResult:
    try:
        return _ok(_parse_bonding_curve_data(data, encoding))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="calculate_bonding_curve_price",
    description="""
    Calculate the token price in SOL using bonding curve state data.
    This is for Pump.fun tokens on bonding curve operations.
    Requires base64/hex input from getAccountInfo.
    """,
    annotations={"title": "Token price from curve", "readOnlyHint": True},
)
def calculate_bonding_curve_price(data: str, encoding: str = "base64") -> CallToolResult:
    try:
        state = _parse_bonding_curve_data(data, encoding)
        price = (state["virtual_sol_reserves"] / LAMPORTS_PER_SOL) / (
            state["virtual_token_reserves"] / 10**TOKEN_DECIMALS
        )
        return _ok(price)
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="calculate_bonding_curve_progress",
    description="""
    Calculate bonding curve completion percent (0-100).
    This is for Pump.fun tokens on bonding curve operations.
    Requires base64/hex input from getAccountInfo.
    """,
    annotations={"title": "Bonding curve progress %", "readOnlyHint": True},
)
def calculate_bonding_curve_progress(data: str, encoding: str = "base64") -> CallToolResult:
    try:
        state = _parse_bonding_curve_data(data, encoding)
        if state["token_total_supply"] == 0:
            return _ok(0.0)
        progress = 100 - (100 * state["real_token_reserves"] / state["token_total_supply"])
        return _ok(progress)
    except Exception as e:
        return _err(str(e))
