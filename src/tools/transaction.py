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


@mcp.tool(
    name="Get latest block number",
    description="Returns the most recent block number.",
    annotations={"title": "Get block number", "readOnlyHint": True},
)
async def get_block_number(chain: str) -> CallToolResult:
    try:
        return _ok(await client.get_block_number(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get block by hash",
    description="Returns a block object by block hash.",
    annotations={"title": "Get block by hash", "readOnlyHint": True},
)
async def get_block_by_hash(chain: str, block_hash: str, full_tx: bool = False) -> CallToolResult:
    try:
        return _ok(await client.get_block_by_hash(chain.lower(), block_hash, full_tx))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get block by number",
    description="Returns a block object by block number.",
    annotations={"title": "Get block by number", "readOnlyHint": True},
)
async def get_block_by_number(
    chain: str, block_number: str, full_tx: bool = False
) -> CallToolResult:
    try:
        return _ok(await client.get_block_by_number(chain.lower(), block_number, full_tx))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get balance",
    description="Returns the account balance at a given block tag.",
    annotations={"title": "Get balance", "readOnlyHint": True},
)
async def get_balance(chain: str, address: str, block: str = "latest") -> CallToolResult:
    try:
        return _ok(await client.get_balance(chain.lower(), address, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Call contract",
    description="Performs a stateless contract call.",
    annotations={"title": "Call contract (eth_call, simulateTransaction)", "readOnlyHint": True},
)
async def eth_call(chain: str, payload: dict, block: str = "latest") -> CallToolResult:
    try:
        return _ok(await client.eth_call(chain.lower(), payload, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="Get gas price",
    description="Returns the current gas price.",
    annotations={"title": "Get gas price", "readOnlyHint": True},
)
async def get_gas_price(chain: str) -> CallToolResult:
    try:
        return _ok(await client.gas_price(chain.lower()))
    except Exception as e:
        return _err(str(e))
