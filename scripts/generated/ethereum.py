
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

    async def eth_getbalance(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getBalance", [param1, param2], self.rpc_url)

    async def eth_getcode(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getCode", [param1, param2], self.rpc_url)

    async def eth_getproof(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getProof", [param1, param2], self.rpc_url)

    async def eth_getstorageat(self, param1, param2, param3) -> str:
        return await self.rpc_client.post("eth_getStorageAt", [param1, param2, param3], self.rpc_url)

    async def eth_gettransactioncount(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getTransactionCount", [param1, param2], self.rpc_url)

    async def eth_blocknumber(self) -> str:
        return await self.rpc_client.post("eth_blockNumber", [], self.rpc_url)

    async def eth_getblockbynumber(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getBlockByNumber", [param1, param2], self.rpc_url)

    async def eth_getblocktransactioncountbyhash(self, param1) -> str:
        return await self.rpc_client.post("eth_getBlockTransactionCountByHash", [param1], self.rpc_url)

    async def eth_getblocktransactioncountbynumber(self, param1) -> str:
        return await self.rpc_client.post("eth_getBlockTransactionCountByNumber", [param1], self.rpc_url)

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

    async def debug_tracetransaction(self, param1, param2) -> str:
        return await self.rpc_client.post("debug_traceTransaction", [param1, param2], self.rpc_url)

    async def debug_traceblockbyhash(self, param1, param2) -> str:
        return await self.rpc_client.post("debug_traceBlockByHash", [param1, param2], self.rpc_url)

    async def debug_traceblockbynumber(self, param1, param2) -> str:
        return await self.rpc_client.post("debug_traceBlockByNumber", [param1, param2], self.rpc_url)

    async def debug_tracecall(self, param1, param2, param3) -> str:
        return await self.rpc_client.post("debug_traceCall", [param1, param2, param3], self.rpc_url)

    async def debug_tracetransaction(self, param1, param2) -> str:
        return await self.rpc_client.post("debug_traceTransaction", [param1, param2], self.rpc_url)

    async def trace_block(self, param1) -> str:
        return await self.rpc_client.post("trace_block", [param1], self.rpc_url)

    async def trace_transaction(self, param1) -> str:
        return await self.rpc_client.post("trace_transaction", [param1], self.rpc_url)

    async def eth_call(self, to_, data) -> str:
        return await self.rpc_client.post("eth_call", [to_, data], self.rpc_url)

    async def eth_sendrawtransaction(self, param1) -> str:
        return await self.rpc_client.post("eth_sendRawTransaction", [param1], self.rpc_url)

    async def eth_simulatev1(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_simulateV1", [param1, param2], self.rpc_url)

    async def eth_getfilterchanges(self, param1) -> str:
        return await self.rpc_client.post("eth_getFilterChanges", [param1], self.rpc_url)

    async def eth_uninstallfilter(self, param1) -> str:
        return await self.rpc_client.post("eth_uninstallFilter", [param1], self.rpc_url)

    async def eth_estimategas(self, from_, to_) -> str:
        return await self.rpc_client.post("eth_estimateGas", [from_, to_], self.rpc_url)

    async def eth_gasprice(self) -> str:
        return await self.rpc_client.post("eth_gasPrice", [], self.rpc_url)

    async def eth_maxpriorityfeepergas(self) -> str:
        return await self.rpc_client.post("eth_maxPriorityFeePerGas", [], self.rpc_url)

    async def eth_getlogs(self, fromBlock, address, topics) -> str:
        return await self.rpc_client.post("eth_getLogs", [fromBlock, address, topics], self.rpc_url)

    async def eth_newfilter(self, fromBlock, address, topics) -> str:
        return await self.rpc_client.post("eth_newFilter", [fromBlock, address, topics], self.rpc_url)

    async def eth_getblockreceipts(self, param1) -> str:
        return await self.rpc_client.post("eth_getBlockReceipts", [param1], self.rpc_url)

    async def eth_gettransactionbyblockhashandindex(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getTransactionByBlockHashAndIndex", [param1, param2], self.rpc_url)

    async def eth_gettransactionbyblocknumberandindex(self, param1, param2) -> str:
        return await self.rpc_client.post("eth_getTransactionByBlockNumberAndIndex", [param1, param2], self.rpc_url)

    async def eth_gettransactionbyhash(self, param1) -> str:
        return await self.rpc_client.post("eth_getTransactionByHash", [param1], self.rpc_url)

    async def eth_gettransactionreceipt(self, param1) -> str:
        return await self.rpc_client.post("eth_getTransactionReceipt", [param1], self.rpc_url)

    async def eth_newpendingtransactionfilter(self) -> str:
        return await self.rpc_client.post("eth_newPendingTransactionFilter", [], self.rpc_url)

