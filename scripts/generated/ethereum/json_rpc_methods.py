"""
Auto-generated MCP tools for JSON-RPC methods.
"""

from mcp.types import CallToolResult
from common.utils import _err, _ok
import servers.ethereum.common.client as client
from servers.ethereum.server import mcp

@mcp.tool(
    name="eth_getbalance",
    description="Call the eth_getBalance JSON-RPC method: eth_getBalance\nReturns: The account balance.\n\nParameters:\n- param1 (Address): The address identifier.\n- param2 (Block identifier): The block identifier.",
    annotations={"title": "eth_getBalance", "readOnlyHint": True},
)
async def eth_getbalance(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getbalance(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getcode",
    description="Call the eth_getCode JSON-RPC method: eth_getCode\nReturns: The smart contract code.\n\nParameters:\n- param1 (Smart contract address): The address identifier.\n- param2 (Block identifier): The block identifier.",
    annotations={"title": "eth_getCode", "readOnlyHint": True},
)
async def eth_getcode(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getcode(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getproof",
    description="Call the eth_getProof JSON-RPC method: eth_getProof\nReturns: The proof information\n\nParameters:\n- param1\n- param2",
    annotations={"title": "eth_getProof", "readOnlyHint": True},
)
async def eth_getproof(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getproof(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getstorageat",
    description="Call the eth_getStorageAt JSON-RPC method: eth_getStorageAt\nReturns: The value stored at the specified position.\n\nParameters:\n- param1 (Smart contract address): The address of the contract to query.\n- param2 (Slot index): The index of the storage position to query.\n- param3 (Block ID): The block number or tag to use as a reference.",
    annotations={"title": "eth_getStorageAt", "readOnlyHint": True},
)
async def eth_getstorageat(chain: str, param1: str, param2: str, param3: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getstorageat(chain.lower(), param1, param2, param3))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactioncount",
    description="Call the eth_getTransactionCount JSON-RPC method: eth_getTransactionCount\nReturns: The address nonce\n\nParameters:\n- param1 (Address): The address to check\n- param2 (Block identifier): The block identifier",
    annotations={"title": "eth_getTransactionCount", "readOnlyHint": True},
)
async def eth_gettransactioncount(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactioncount(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_blocknumber",
    description="Call the eth_blockNumber JSON-RPC method: eth_blockNumber\nReturns: The latest block number.",
    annotations={"title": "eth_blockNumber", "readOnlyHint": True},
)
async def eth_blocknumber(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_blocknumber(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblockbynumber",
    description="Call the eth_getBlockByNumber JSON-RPC method: eth_getBlockByNumber\nReturns: The block information\n\nParameters:\n- param1 (Block identifier): The block number or tag.\n- param2 (Transaction selector): True for the full transactions, false for only the transaction hashes.",
    annotations={"title": "eth_getBlockByNumber", "readOnlyHint": True},
)
async def eth_getblockbynumber(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblockbynumber(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblocktransactioncountbyhash",
    description="Call the eth_getBlockTransactionCountByHash JSON-RPC method: eth_getBlockTransactionCountByHash\nReturns: The block information\n\nParameters:\n- param1 (Block hash): The block hash identifier.",
    annotations={"title": "eth_getBlockTransactionCountByHash", "readOnlyHint": True},
)
async def eth_getblocktransactioncountbyhash(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblocktransactioncountbyhash(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblocktransactioncountbynumber",
    description="Call the eth_getBlockTransactionCountByNumber JSON-RPC method: eth_getBlockTransactionCountByNumber\nReturns: The block transaction count information\n\nParameters:\n- param1 (Block identifier): The block number or tag.",
    annotations={"title": "eth_getBlockTransactionCountByNumber", "readOnlyHint": True},
)
async def eth_getblocktransactioncountbynumber(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblocktransactioncountbynumber(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newblockfilter",
    description="Call the eth_newBlockFilter JSON-RPC method: eth_newBlockFilter\nReturns: The new filter ID.",
    annotations={"title": "eth_newBlockFilter", "readOnlyHint": True},
)
async def eth_newblockfilter(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newblockfilter(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_chainid",
    description="Call the eth_chainId JSON-RPC method: eth_chainId\nReturns: The network Chain ID",
    annotations={"title": "eth_chainId", "readOnlyHint": True},
)
async def eth_chainid(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_chainid(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_syncing",
    description="Call the eth_syncing JSON-RPC method: eth_syncing\nReturns: Syncing information",
    annotations={"title": "eth_syncing", "readOnlyHint": True},
)
async def eth_syncing(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_syncing(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="net_listening",
    description="Call the net_listening JSON-RPC method: net_listening\nReturns: The boolean value that indicates whether or not a node is currently actively seeking peer connections.",
    annotations={"title": "net_listening", "readOnlyHint": True},
)
async def net_listening(chain: str) -> CallToolResult:
    try:
        return _ok(await client.net_listening(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="net_peercount",
    description="Call the net_peerCount JSON-RPC method: net_peerCount\nReturns: The number of peers connected to the client.",
    annotations={"title": "net_peerCount", "readOnlyHint": True},
)
async def net_peercount(chain: str) -> CallToolResult:
    try:
        return _ok(await client.net_peercount(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="web3_clientversion",
    description="Call the web3_clientVersion JSON-RPC method: web3_clientVersion\nReturns: The client running on this node.",
    annotations={"title": "web3_clientVersion", "readOnlyHint": True},
)
async def web3_clientversion(chain: str) -> CallToolResult:
    try:
        return _ok(await client.web3_clientversion(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracetransaction",
    description="Call the debug_traceTransaction JSON-RPC method: Custom JS tracer\nReturns: The transaction's trace\n\nParameters:\n- param1 (Transaction hash): The hash of the transaction to trace.\n- param2 (The JS custom tracer object)",
    annotations={"title": "debug_traceTransaction", "readOnlyHint": True},
)
async def debug_tracetransaction(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracetransaction(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_traceblockbyhash",
    description="Call the debug_traceBlockByHash JSON-RPC method: debug_traceBlockByHash\nReturns: The block traces.\n\nParameters:\n- param1 (Block Hash): The block hash.\n- tracer (Tracer type): The type of tracer.",
    annotations={"title": "debug_traceBlockByHash", "readOnlyHint": True},
)
async def debug_traceblockbyhash(chain: str, param1: str, tracer: str) -> CallToolResult:
    try:
        return _ok(await client.debug_traceblockbyhash(chain.lower(), param1, tracer))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_traceblockbynumber",
    description="Call the debug_traceBlockByNumber JSON-RPC method: debug_traceBlockByNumber\nReturns: The block traces.\n\nParameters:\n- param1 (Block identifier): The block hash.\n- tracer (Tracer type): The type of tracer.",
    annotations={"title": "debug_traceBlockByNumber", "readOnlyHint": True},
)
async def debug_traceblockbynumber(chain: str, param1: str, tracer: str) -> CallToolResult:
    try:
        return _ok(await client.debug_traceblockbynumber(chain.lower(), param1, tracer))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracecall",
    description="Call the debug_traceCall JSON-RPC method: debug_traceCall\nReturns: The result of the debug trace call\n\nParameters:\n- from_\n- param2 [Example: latest]\n- tracer",
    annotations={"title": "debug_traceCall", "readOnlyHint": True},
)
async def debug_tracecall(chain: str, from_: str, param2: str, tracer: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracecall(chain.lower(), from_, param2, tracer))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracetransaction",
    description="Call the debug_traceTransaction JSON-RPC method: debug_traceTransaction\nReturns: The transaction's trace.\n\nParameters:\n- param1 (Transaction hash): The hash of the transaction to trace.\n- param2 (Tracing options)",
    annotations={"title": "debug_traceTransaction", "readOnlyHint": True},
)
async def debug_tracetransaction(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracetransaction(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="trace_block",
    description="Call the trace_block JSON-RPC method: trace_block\nReturns: The block's trace.\n\nParameters:\n- param1 (Block identifier): The block number or tag.",
    annotations={"title": "trace_block", "readOnlyHint": True},
)
async def trace_block(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.trace_block(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="trace_transaction",
    description="Call the trace_transaction JSON-RPC method: trace_transaction\nReturns: The transaction's trace.\n\nParameters:\n- param1 (Transaction hash): The hash of the transaction to trace.",
    annotations={"title": "trace_transaction", "readOnlyHint": True},
)
async def trace_transaction(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.trace_transaction(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_call",
    description="Call the eth_call JSON-RPC method: eth_call\nReturns: The result of the call.\n\nParameters:\n- to_: The address of the contract to call.\n- data: The data to send with the call.",
    annotations={"title": "eth_call", "readOnlyHint": True},
)
async def eth_call(chain: str, to_: str, data: str) -> CallToolResult:
    try:
        return _ok(await client.eth_call(chain.lower(), to_, data))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_sendrawtransaction",
    description="Call the eth_sendRawTransaction JSON-RPC method: eth_sendRawTransaction\nReturns: The transaction hash.\n\nParameters:\n- param1: The signed transaction.",
    annotations={"title": "eth_sendRawTransaction", "readOnlyHint": True},
)
async def eth_sendrawtransaction(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_sendrawtransaction(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_simulatev1",
    description="Call the eth_simulateV1 JSON-RPC method: eth_simulateV1\nReturns: Successful response\n\nParameters:\n- blockStateCalls\n- param2",
    annotations={"title": "eth_simulateV1", "readOnlyHint": True},
)
async def eth_simulatev1(chain: str, blockStateCalls: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_simulatev1(chain.lower(), blockStateCalls, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getfilterchanges",
    description="Call the eth_getFilterChanges JSON-RPC method: eth_getFilterChanges\nReturns: The filter changes.\n\nParameters:\n- param1 (The filter ID)",
    annotations={"title": "eth_getFilterChanges", "readOnlyHint": True},
)
async def eth_getfilterchanges(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getfilterchanges(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_uninstallfilter",
    description="Call the eth_uninstallFilter JSON-RPC method: eth_uninstallFilter\nReturns: Boolean value indicating if the filter was removed or not.\n\nParameters:\n- param1 (Filter ID)",
    annotations={"title": "eth_uninstallFilter", "readOnlyHint": True},
)
async def eth_uninstallfilter(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_uninstallfilter(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_estimategas",
    description="Call the eth_estimateGas JSON-RPC method: eth_estimateGas\nReturns: The estimated gas amount\n\nParameters:\n- from_\n- to_",
    annotations={"title": "eth_estimateGas", "readOnlyHint": True},
)
async def eth_estimategas(chain: str, from_: str, to_: str) -> CallToolResult:
    try:
        return _ok(await client.eth_estimategas(chain.lower(), from_, to_))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gasprice",
    description="Call the eth_gasPrice JSON-RPC method: eth_gasPrice\nReturns: The value of the current gas base fee in Wei.",
    annotations={"title": "eth_gasPrice", "readOnlyHint": True},
)
async def eth_gasprice(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gasprice(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_maxpriorityfeepergas",
    description="Call the eth_maxPriorityFeePerGas JSON-RPC method: eth_maxPriorityFeePerGas\nReturns: The estimated max priority fee per gas",
    annotations={"title": "eth_maxPriorityFeePerGas", "readOnlyHint": True},
)
async def eth_maxpriorityfeepergas(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_maxpriorityfeepergas(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getlogs",
    description="Call the eth_getLogs JSON-RPC method: eth_getLogs\nReturns: An array of log objects matching the specified filter.\n\nParameters:\n- fromBlock (from block): The block number or tag to start searching for logs from. [Example: latest]\n- address (smart contract address): The contract address to retrieve the logs for.\n- topics (topics): An array of 32-byte topics to filter for. Each topic is treated as an OR condition.",
    annotations={"title": "eth_getLogs", "readOnlyHint": True},
)
async def eth_getlogs(chain: str, fromBlock: str, address: str, topics: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getlogs(chain.lower(), fromBlock, address, topics))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newfilter",
    description="Call the eth_newFilter JSON-RPC method: eth_newFilter\nReturns: The filter ID.\n\nParameters:\n- fromBlock (from block): The block number or tag to start searching for logs from. [Example: latest]\n- address (smart contract address): The contract address to retrieve the logs for.\n- topics (topics): An array of 32-byte topics to filter for. Each topic is treated as an OR condition.",
    annotations={"title": "eth_newFilter", "readOnlyHint": True},
)
async def eth_newfilter(chain: str, fromBlock: str, address: str, topics: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newfilter(chain.lower(), fromBlock, address, topics))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblockreceipts",
    description="Call the eth_getBlockReceipts JSON-RPC method: eth_getBlockReceipts\nReturns: The block receipts information\n\nParameters:\n- param1 (Block identifier)",
    annotations={"title": "eth_getBlockReceipts", "readOnlyHint": True},
)
async def eth_getblockreceipts(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblockreceipts(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyblockhashandindex",
    description="Call the eth_getTransactionByBlockHashAndIndex JSON-RPC method: eth_getTransactionByBlockHashAndIndex\nReturns: The transaction information\n\nParameters:\n- param1 (Block hash)\n- param2 (Transaction index)",
    annotations={"title": "eth_getTransactionByBlockHashAndIndex", "readOnlyHint": True},
)
async def eth_gettransactionbyblockhashandindex(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyblockhashandindex(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyblocknumberandindex",
    description="Call the eth_getTransactionByBlockNumberAndIndex JSON-RPC method: eth_getTransactionByBlockNumberAndIndex\nReturns: The transaction information\n\nParameters:\n- param1 (Block number)\n- param2 (Transaction index)",
    annotations={"title": "eth_getTransactionByBlockNumberAndIndex", "readOnlyHint": True},
)
async def eth_gettransactionbyblocknumberandindex(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyblocknumberandindex(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyhash",
    description="Call the eth_getTransactionByHash JSON-RPC method: eth_getTransactionByHash\nReturns: The transaction information\n\nParameters:\n- param1 (Transaction hash)",
    annotations={"title": "eth_getTransactionByHash", "readOnlyHint": True},
)
async def eth_gettransactionbyhash(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyhash(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionreceipt",
    description="Call the eth_getTransactionReceipt JSON-RPC method: eth_getTransactionReceipt\nReturns: The transaction receipt\n\nParameters:\n- param1 (Transaction hash)",
    annotations={"title": "eth_getTransactionReceipt", "readOnlyHint": True},
)
async def eth_gettransactionreceipt(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionreceipt(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newpendingtransactionfilter",
    description="Call the eth_newPendingTransactionFilter JSON-RPC method: eth_newPendingTransactionFilter\nReturns: The new filter ID.",
    annotations={"title": "eth_newPendingTransactionFilter", "readOnlyHint": True},
)
async def eth_newpendingtransactionfilter(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newpendingtransactionfilter(chain.lower()))
    except Exception as e:
        return _err(str(e))

