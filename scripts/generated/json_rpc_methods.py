"""
Auto-generated MCP tools for JSON-RPC methods.
"""

from mcp.types import CallToolResult
from common.utils import _err, _ok
import servers.ethereum.common.client as client
from servers.ethereum.server import mcp

@mcp.tool(
    name="eth_getbalance",
    description="Auto-generated tool for eth_getBalance",
    annotations={"title": "eth_getBalance", "readOnlyHint": True},
)
async def eth_getbalance(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getbalance(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getcode",
    description="Auto-generated tool for eth_getCode",
    annotations={"title": "eth_getCode", "readOnlyHint": True},
)
async def eth_getcode(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getcode(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getproof",
    description="Auto-generated tool for eth_getProof",
    annotations={"title": "eth_getProof", "readOnlyHint": True},
)
async def eth_getproof(chain: str, param0: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getproof(chain.lower(), param0, param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getstorageat",
    description="Auto-generated tool for eth_getStorageAt",
    annotations={"title": "eth_getStorageAt", "readOnlyHint": True},
)
async def eth_getstorageat(chain: str, param0: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getstorageat(chain.lower(), param0, param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactioncount",
    description="Auto-generated tool for eth_getTransactionCount",
    annotations={"title": "eth_getTransactionCount", "readOnlyHint": True},
)
async def eth_gettransactioncount(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactioncount(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_blocknumber",
    description="Auto-generated tool for eth_blockNumber",
    annotations={"title": "eth_blockNumber", "readOnlyHint": True},
)
async def eth_blocknumber(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_blocknumber(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblockbynumber",
    description="Auto-generated tool for eth_getBlockByNumber",
    annotations={"title": "eth_getBlockByNumber", "readOnlyHint": True},
)
async def eth_getblockbynumber(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblockbynumber(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblocktransactioncountbyhash",
    description="Auto-generated tool for eth_getBlockTransactionCountByHash",
    annotations={"title": "eth_getBlockTransactionCountByHash", "readOnlyHint": True},
)
async def eth_getblocktransactioncountbyhash(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblocktransactioncountbyhash(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblocktransactioncountbynumber",
    description="Auto-generated tool for eth_getBlockTransactionCountByNumber",
    annotations={"title": "eth_getBlockTransactionCountByNumber", "readOnlyHint": True},
)
async def eth_getblocktransactioncountbynumber(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblocktransactioncountbynumber(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newblockfilter",
    description="Auto-generated tool for eth_newBlockFilter",
    annotations={"title": "eth_newBlockFilter", "readOnlyHint": True},
)
async def eth_newblockfilter(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newblockfilter(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_chainid",
    description="Auto-generated tool for eth_chainId",
    annotations={"title": "eth_chainId", "readOnlyHint": True},
)
async def eth_chainid(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_chainid(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_syncing",
    description="Auto-generated tool for eth_syncing",
    annotations={"title": "eth_syncing", "readOnlyHint": True},
)
async def eth_syncing(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_syncing(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="net_listening",
    description="Auto-generated tool for net_listening",
    annotations={"title": "net_listening", "readOnlyHint": True},
)
async def net_listening(chain: str) -> CallToolResult:
    try:
        return _ok(await client.net_listening(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="net_peercount",
    description="Auto-generated tool for net_peerCount",
    annotations={"title": "net_peerCount", "readOnlyHint": True},
)
async def net_peercount(chain: str) -> CallToolResult:
    try:
        return _ok(await client.net_peercount(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="web3_clientversion",
    description="Auto-generated tool for web3_clientVersion",
    annotations={"title": "web3_clientVersion", "readOnlyHint": True},
)
async def web3_clientversion(chain: str) -> CallToolResult:
    try:
        return _ok(await client.web3_clientversion(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracetransaction",
    description="Auto-generated tool for debug_traceTransaction",
    annotations={"title": "debug_traceTransaction", "readOnlyHint": True},
)
async def debug_tracetransaction(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracetransaction(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_traceblockbyhash",
    description="Auto-generated tool for debug_traceBlockByHash",
    annotations={"title": "debug_traceBlockByHash", "readOnlyHint": True},
)
async def debug_traceblockbyhash(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.debug_traceblockbyhash(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_traceblockbynumber",
    description="Auto-generated tool for debug_traceBlockByNumber",
    annotations={"title": "debug_traceBlockByNumber", "readOnlyHint": True},
)
async def debug_traceblockbynumber(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.debug_traceblockbynumber(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracecall",
    description="Auto-generated tool for debug_traceCall",
    annotations={"title": "debug_traceCall", "readOnlyHint": True},
)
async def debug_tracecall(chain: str, param0: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracecall(chain.lower(), param0, param1, param2))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="debug_tracetransaction",
    description="Auto-generated tool for debug_traceTransaction",
    annotations={"title": "debug_traceTransaction", "readOnlyHint": True},
)
async def debug_tracetransaction(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.debug_tracetransaction(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="trace_block",
    description="Auto-generated tool for trace_block",
    annotations={"title": "trace_block", "readOnlyHint": True},
)
async def trace_block(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.trace_block(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="trace_transaction",
    description="Auto-generated tool for trace_transaction",
    annotations={"title": "trace_transaction", "readOnlyHint": True},
)
async def trace_transaction(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.trace_transaction(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_call",
    description="Auto-generated tool for eth_call",
    annotations={"title": "eth_call", "readOnlyHint": True},
)
async def eth_call(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_call(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_sendrawtransaction",
    description="Auto-generated tool for eth_sendRawTransaction",
    annotations={"title": "eth_sendRawTransaction", "readOnlyHint": True},
)
async def eth_sendrawtransaction(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_sendrawtransaction(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_simulatev1",
    description="Auto-generated tool for eth_simulateV1",
    annotations={"title": "eth_simulateV1", "readOnlyHint": True},
)
async def eth_simulatev1(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_simulatev1(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getfilterchanges",
    description="Auto-generated tool for eth_getFilterChanges",
    annotations={"title": "eth_getFilterChanges", "readOnlyHint": True},
)
async def eth_getfilterchanges(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getfilterchanges(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_uninstallfilter",
    description="Auto-generated tool for eth_uninstallFilter",
    annotations={"title": "eth_uninstallFilter", "readOnlyHint": True},
)
async def eth_uninstallfilter(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_uninstallfilter(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_estimategas",
    description="Auto-generated tool for eth_estimateGas",
    annotations={"title": "eth_estimateGas", "readOnlyHint": True},
)
async def eth_estimategas(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_estimategas(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gasprice",
    description="Auto-generated tool for eth_gasPrice",
    annotations={"title": "eth_gasPrice", "readOnlyHint": True},
)
async def eth_gasprice(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gasprice(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_maxpriorityfeepergas",
    description="Auto-generated tool for eth_maxPriorityFeePerGas",
    annotations={"title": "eth_maxPriorityFeePerGas", "readOnlyHint": True},
)
async def eth_maxpriorityfeepergas(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_maxpriorityfeepergas(chain.lower()))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getlogs",
    description="Auto-generated tool for eth_getLogs",
    annotations={"title": "eth_getLogs", "readOnlyHint": True},
)
async def eth_getlogs(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getlogs(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newfilter",
    description="Auto-generated tool for eth_newFilter",
    annotations={"title": "eth_newFilter", "readOnlyHint": True},
)
async def eth_newfilter(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newfilter(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_getblockreceipts",
    description="Auto-generated tool for eth_getBlockReceipts",
    annotations={"title": "eth_getBlockReceipts", "readOnlyHint": True},
)
async def eth_getblockreceipts(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getblockreceipts(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyblockhashandindex",
    description="Auto-generated tool for eth_getTransactionByBlockHashAndIndex",
    annotations={"title": "eth_getTransactionByBlockHashAndIndex", "readOnlyHint": True},
)
async def eth_gettransactionbyblockhashandindex(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyblockhashandindex(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyblocknumberandindex",
    description="Auto-generated tool for eth_getTransactionByBlockNumberAndIndex",
    annotations={"title": "eth_getTransactionByBlockNumberAndIndex", "readOnlyHint": True},
)
async def eth_gettransactionbyblocknumberandindex(chain: str, param0: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyblocknumberandindex(chain.lower(), param0, param1))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionbyhash",
    description="Auto-generated tool for eth_getTransactionByHash",
    annotations={"title": "eth_getTransactionByHash", "readOnlyHint": True},
)
async def eth_gettransactionbyhash(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionbyhash(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_gettransactionreceipt",
    description="Auto-generated tool for eth_getTransactionReceipt",
    annotations={"title": "eth_getTransactionReceipt", "readOnlyHint": True},
)
async def eth_gettransactionreceipt(chain: str, param0: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gettransactionreceipt(chain.lower(), param0))
    except Exception as e:
        return _err(str(e))

@mcp.tool(
    name="eth_newpendingtransactionfilter",
    description="Auto-generated tool for eth_newPendingTransactionFilter",
    annotations={"title": "eth_newPendingTransactionFilter", "readOnlyHint": True},
)
async def eth_newpendingtransactionfilter(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_newpendingtransactionfilter(chain.lower()))
    except Exception as e:
        return _err(str(e))

