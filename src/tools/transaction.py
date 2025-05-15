"""MCP tools for transaction-related JSON-RPC calls (EVM and other chains)."""

from mcp.types import CallToolResult, TextContent

import core.client as client
from server import mcp


def _err(msg: str) -> CallToolResult:
    return CallToolResult(isError=True, content=[TextContent(type="text", text=msg)])


def _ok(data) -> CallToolResult:
    return CallToolResult(content=[TextContent(type="text", text=str(data))])


@mcp.tool(
    name="Get transaction by hash / signature",
    description="Returns the full transaction object for the provided transaction hash / signature.",
    annotations={"title": "Get transaction details", "readOnlyHint": True},
)
async def eth_get_tx_by_hash(chain: str, tx_hash: str) -> CallToolResult:
    try:
        return _ok(await client.get_transaction_by_hash(chain.lower(), tx_hash))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get transaction by block hash and transaction index",
    description="Returns the full transaction object identified by block hash and transaction index.",
    annotations={"title": "Get transaction details", "readOnlyHint": True},
)
async def eth_get_tx_by_blk_hash_idx(chain: str, block_hash: str, index: str) -> CallToolResult:
    try:
        return _ok(
            await client.get_transaction_by_block_hash_and_index(chain.lower(), block_hash, index)
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get transaction by block number and transaction index",
    description="Returns the full transaction object identified by block number and transaction index.",
    annotations={"title": "Get transaction details", "readOnlyHint": True},
)
async def eth_get_tx_by_blk_num_idx(chain: str, block_number: str, index: str) -> CallToolResult:
    try:
        return _ok(
            await client.get_transaction_by_block_number_and_index(
                chain.lower(), block_number, index
            )
        )
    except Exception as e:
        return _err(str(e))
