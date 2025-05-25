"""
Reusable base class for all EVM-compatible blockchain adapters.
"""

from common.interfaces import RpcClient
from common.rpc import HttpxRpcClient
from servers.evm.common.interfaces import BlockchainAdapter


class EvmAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def web3_clientVersion(self) -> str:
        return await self.rpc_client.post("web3_clientVersion", [], self.rpc_url)

    async def web3_sha3(self, data: str) -> str:
        return await self.rpc_client.post("web3_sha3", [data], self.rpc_url)

    async def net_version(self) -> str:
        return await self.rpc_client.post("net_version", [], self.rpc_url)

    async def net_listening(self) -> str:
        return await self.rpc_client.post("net_listening", [], self.rpc_url)

    async def net_peerCount(self) -> str:
        return await self.rpc_client.post("net_peerCount", [], self.rpc_url)

    async def eth_syncing(self) -> str:
        return await self.rpc_client.post("eth_syncing", [], self.rpc_url)

    async def eth_chainId(self) -> str:
        return await self.rpc_client.post("eth_chainId", [], self.rpc_url)

    async def eth_blockNumber(self) -> str:
        return await self.rpc_client.post("eth_blockNumber", [], self.rpc_url)

    async def eth_gasPrice(self) -> str:
        return await self.rpc_client.post("eth_gasPrice", [], self.rpc_url)

    async def eth_feeHistory(
        self, block_count: str, newest_block: str, reward_percentiles: list[str]
    ) -> str:
        return await self.rpc_client.post(
            "eth_feeHistory", [block_count, newest_block, reward_percentiles], self.rpc_url
        )

    async def eth_maxPriorityFeePerGas(self) -> str:
        return await self.rpc_client.post("eth_maxPriorityFeePerGas", [], self.rpc_url)

    async def eth_getBalance(self, address: str, block: str) -> str:
        return await self.rpc_client.post("eth_getBalance", [address, block], self.rpc_url)

    async def eth_getStorageAt(self, address: str, position: str, block: str) -> str:
        return await self.rpc_client.post(
            "eth_getStorageAt", [address, position, block], self.rpc_url
        )

    async def eth_getTransactionCount(self, address: str, block: str) -> str:
        return await self.rpc_client.post("eth_getTransactionCount", [address, block], self.rpc_url)

    async def eth_getCode(self, address: str, block: str) -> str:
        return await self.rpc_client.post("eth_getCode", [address, block], self.rpc_url)

    async def eth_call(self, call_object: dict, block: str, overrides: dict = None) -> str:
        params = [call_object, block]
        if overrides:
            params.append(overrides)
        return await self.rpc_client.post("eth_call", params, self.rpc_url)

    async def eth_estimateGas(self, tx: dict, block: str, overrides: dict = None) -> str:
        params = [tx, block]
        if overrides:
            params.append(overrides)
        return await self.rpc_client.post("eth_estimateGas", params, self.rpc_url)

    async def eth_getBlockByHash(self, block_hash: str, full_tx: bool) -> str:
        return await self.rpc_client.post("eth_getBlockByHash", [block_hash, full_tx], self.rpc_url)

    async def eth_getBlockByNumber(self, block_number: str, full_tx: bool) -> str:
        return await self.rpc_client.post(
            "eth_getBlockByNumber", [block_number, full_tx], self.rpc_url
        )

    async def eth_getBlockTransactionCountByHash(self, block_hash: str) -> str:
        return await self.rpc_client.post(
            "eth_getBlockTransactionCountByHash", [block_hash], self.rpc_url
        )

    async def eth_getBlockTransactionCountByNumber(self, block_number: str) -> str:
        return await self.rpc_client.post(
            "eth_getBlockTransactionCountByNumber", [block_number], self.rpc_url
        )

    async def eth_getTransactionByHash(self, tx_hash: str) -> str:
        return await self.rpc_client.post("eth_getTransactionByHash", [tx_hash], self.rpc_url)

    async def eth_getTransactionReceipt(self, tx_hash: str) -> str:
        return await self.rpc_client.post("eth_getTransactionReceipt", [tx_hash], self.rpc_url)

    async def eth_getLogs(self, filter_params: dict) -> str:
        return await self.rpc_client.post("eth_getLogs", [filter_params], self.rpc_url)

    async def debug_traceTransaction(self, tx_hash: str, options: dict) -> str:
        return await self.rpc_client.post(
            "debug_traceTransaction", [tx_hash, options], self.rpc_url
        )

    async def debug_traceCall(self, call_object: dict, block: str, options: dict) -> str:
        return await self.rpc_client.post(
            "debug_traceCall", [call_object, block, options], self.rpc_url
        )

    async def debug_traceBlock(self, rlp_encoded_block: str, options: dict) -> str:
        return await self.rpc_client.post(
            "debug_traceBlock", [rlp_encoded_block, options], self.rpc_url
        )

    async def debug_traceBlockByHash(self, block_hash: str, options: dict) -> str:
        return await self.rpc_client.post(
            "debug_traceBlockByHash", [block_hash, options], self.rpc_url
        )

    async def debug_traceBlockByNumber(self, block_number: str, options: dict) -> str:
        return await self.rpc_client.post(
            "debug_traceBlockByNumber", [block_number, options], self.rpc_url
        )

    async def trace_call(self, call_object: dict, trace_types: list[str], block: str) -> str:
        return await self.rpc_client.post(
            "trace_call", [call_object, trace_types, block], self.rpc_url
        )

    async def trace_callMany(self, calls: list[tuple[dict, list[str]]], block: str) -> str:
        return await self.rpc_client.post("trace_callMany", [calls, block], self.rpc_url)

    async def trace_rawTransaction(self, raw_tx: str, trace_types: list[str]) -> str:
        return await self.rpc_client.post(
            "trace_rawTransaction", [raw_tx, trace_types], self.rpc_url
        )

    async def trace_replayTransaction(self, tx_hash: str, trace_types: list[str]) -> str:
        return await self.rpc_client.post(
            "trace_replayTransaction", [tx_hash, trace_types], self.rpc_url
        )

    async def trace_replayBlockTransactions(self, block_number: str, trace_types: list[str]) -> str:
        return await self.rpc_client.post(
            "trace_replayBlockTransactions", [block_number, trace_types], self.rpc_url
        )

    async def trace_block(self, block_number: str) -> str:
        return await self.rpc_client.post("trace_block", [block_number], self.rpc_url)

    async def eth_getProof(self, address: str, storage_keys: list[str], block: str) -> str:
        return await self.rpc_client.post(
            "eth_getProof", [address, storage_keys, block], self.rpc_url
        )

    async def eth_simulateV1(self, params: dict, block: str) -> str:
        return await self.rpc_client.post("eth_simulateV1", [params, block], self.rpc_url)

    async def eth_getBlockReceipts(self, block: str) -> str:
        return await self.rpc_client.post("eth_getBlockReceipts", [block], self.rpc_url)
