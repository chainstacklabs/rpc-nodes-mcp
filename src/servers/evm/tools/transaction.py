"""MCP tools for transaction-related JSON-RPC calls (EVM and other chains)."""

from mcp.types import CallToolResult

import servers.evm.common.client as client
from common.utils import _err, _ok
from servers.evm.server import mcp


@mcp.tool(
    name="get_transaction_by_id",
    description="Returns the full transaction object for the provided transaction hash / signature.",
    annotations={"title": "Get transaction details", "readOnlyHint": True},
)
async def eth_get_tx_by_hash(chain: str, tx_hash: str) -> CallToolResult:
    try:
        return _ok(await client.get_transaction_by_hash(chain.lower(), tx_hash))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_transaction_by_block_hash_index",
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
    name="get_transaction_by_block_number_index",
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
    name="get_latest_block_number",
    description="Returns the most recent block number.",
    annotations={"title": "Get block number", "readOnlyHint": True},
)
async def get_block_number(chain: str) -> CallToolResult:
    try:
        return _ok(await client.get_block_number(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_block_by_hash",
    description="Returns a block object by block hash.",
    annotations={"title": "Get block by hash", "readOnlyHint": True},
)
async def get_block_by_hash(chain: str, block_hash: str, full_tx: bool = False) -> CallToolResult:
    try:
        return _ok(await client.get_block_by_hash(chain.lower(), block_hash, full_tx))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_block_by_number",
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
    name="get_balance",
    description="Returns the account balance at a given block tag.",
    annotations={"title": "Get balance", "readOnlyHint": True},
)
async def get_balance(chain: str, address: str, block: str = "latest") -> CallToolResult:
    try:
        return _ok(await client.get_balance(chain.lower(), address, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="call_contract",
    description="Performs a stateless contract call.",
    annotations={"title": "Call contract (eth_call, simulateTransaction)", "readOnlyHint": True},
)
async def eth_call(chain: str, payload: dict, block: str = "latest") -> CallToolResult:
    try:
        return _ok(await client.eth_call(chain.lower(), payload, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="get_gas_fees",
    description="Returns the current gas price.",
    annotations={"title": "Get gas price", "readOnlyHint": True},
)
async def get_gas_price(chain: str) -> CallToolResult:
    try:
        return _ok(await client.gas_price(chain.lower()))
    except Exception as e:
        return _err(str(e))
