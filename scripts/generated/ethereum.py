
"""
Auto-generated adapter class for ethereum-compatible blockchain.
"""

from common.interfaces import RpcClient
from common.rpc import HttpxRpcClient
from servers.ethereum.common.interfaces import BlockchainAdapter


class EthereumAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def eth_getbalance(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getBalance", [param0, param1], self.rpc_url)

    async def eth_getcode(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getCode", [param0, param1], self.rpc_url)

    async def eth_getproof(self, param0, param1, param2) -> str:
        return await self.rpc_client.post("eth_getProof", [param0, param1, param2], self.rpc_url)

    async def eth_getstorageat(self, param0, param1, param2) -> str:
        return await self.rpc_client.post("eth_getStorageAt", [param0, param1, param2], self.rpc_url)

    async def eth_gettransactioncount(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getTransactionCount", [param0, param1], self.rpc_url)

    async def eth_blocknumber(self) -> str:
        return await self.rpc_client.post("eth_blockNumber", [], self.rpc_url)

    async def eth_getblockbynumber(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getBlockByNumber", [param0, param1], self.rpc_url)

    async def eth_getblocktransactioncountbyhash(self, param0) -> str:
        return await self.rpc_client.post("eth_getBlockTransactionCountByHash", [param0], self.rpc_url)

    async def eth_getblocktransactioncountbynumber(self, param0) -> str:
        return await self.rpc_client.post("eth_getBlockTransactionCountByNumber", [param0], self.rpc_url)

    async def eth_newblockfilter(self) -> str:
        return await self.rpc_client.post("eth_newBlockFilter", [], self.rpc_url)

    async def eth_chainid(self) -> str:
        return await self.rpc_client.post("eth_chainId", [], self.rpc_url)

    async def eth_syncing(self) -> str:
        return await self.rpc_client.post("eth_syncing", [], self.rpc_url)

    async def net_listening(self) -> str:
        return await self.rpc_client.post("net_listening", [], self.rpc_url)

    async def net_peercount(self) -> str:
        return await self.rpc_client.post("net_peerCount", [], self.rpc_url)

    async def web3_clientversion(self) -> str:
        return await self.rpc_client.post("web3_clientVersion", [], self.rpc_url)

    async def debug_tracetransaction(self, param0, param1) -> str:
        return await self.rpc_client.post("debug_traceTransaction", [param0, param1], self.rpc_url)

    async def debug_traceblockbyhash(self, param0, param1) -> str:
        return await self.rpc_client.post("debug_traceBlockByHash", [param0, param1], self.rpc_url)

    async def debug_traceblockbynumber(self, param0, param1) -> str:
        return await self.rpc_client.post("debug_traceBlockByNumber", [param0, param1], self.rpc_url)

    async def debug_tracecall(self, param0, param1, param2) -> str:
        return await self.rpc_client.post("debug_traceCall", [param0, param1, param2], self.rpc_url)

    async def debug_tracetransaction(self, param0, param1) -> str:
        return await self.rpc_client.post("debug_traceTransaction", [param0, param1], self.rpc_url)

    async def trace_block(self, param0) -> str:
        return await self.rpc_client.post("trace_block", [param0], self.rpc_url)

    async def trace_transaction(self, param0) -> str:
        return await self.rpc_client.post("trace_transaction", [param0], self.rpc_url)

    async def eth_call(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_call", [param0, param1], self.rpc_url)

    async def eth_sendrawtransaction(self, param0) -> str:
        return await self.rpc_client.post("eth_sendRawTransaction", [param0], self.rpc_url)

    async def eth_simulatev1(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_simulateV1", [param0, param1], self.rpc_url)

    async def eth_getfilterchanges(self, param0) -> str:
        return await self.rpc_client.post("eth_getFilterChanges", [param0], self.rpc_url)

    async def eth_uninstallfilter(self, param0) -> str:
        return await self.rpc_client.post("eth_uninstallFilter", [param0], self.rpc_url)

    async def eth_estimategas(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_estimateGas", [param0, param1], self.rpc_url)

    async def eth_gasprice(self) -> str:
        return await self.rpc_client.post("eth_gasPrice", [], self.rpc_url)

    async def eth_maxpriorityfeepergas(self) -> str:
        return await self.rpc_client.post("eth_maxPriorityFeePerGas", [], self.rpc_url)

    async def eth_getlogs(self, param0) -> str:
        return await self.rpc_client.post("eth_getLogs", [param0], self.rpc_url)

    async def eth_newfilter(self, param0) -> str:
        return await self.rpc_client.post("eth_newFilter", [param0], self.rpc_url)

    async def eth_getblockreceipts(self, param0) -> str:
        return await self.rpc_client.post("eth_getBlockReceipts", [param0], self.rpc_url)

    async def eth_gettransactionbyblockhashandindex(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getTransactionByBlockHashAndIndex", [param0, param1], self.rpc_url)

    async def eth_gettransactionbyblocknumberandindex(self, param0, param1) -> str:
        return await self.rpc_client.post("eth_getTransactionByBlockNumberAndIndex", [param0, param1], self.rpc_url)

    async def eth_gettransactionbyhash(self, param0) -> str:
        return await self.rpc_client.post("eth_getTransactionByHash", [param0], self.rpc_url)

    async def eth_gettransactionreceipt(self, param0) -> str:
        return await self.rpc_client.post("eth_getTransactionReceipt", [param0], self.rpc_url)

    async def eth_newpendingtransactionfilter(self) -> str:
        return await self.rpc_client.post("eth_newPendingTransactionFilter", [], self.rpc_url)

