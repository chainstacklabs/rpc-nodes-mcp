"""
Reusable base class for all EVM-compatible blockchain adapters.
"""

from core.interfaces import BlockchainAdapter, RpcClient
from core.rpc import HttpxRpcClient


class EvmAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def get_transaction_by_hash(self, tx_hash):
        return await self.rpc_client.post("eth_getTransactionByHash", [tx_hash], self.rpc_url)

    async def get_transaction_by_block_hash_and_index(self, block_hash, index):
        return await self.rpc_client.post(
            "eth_getTransactionByBlockHashAndIndex", [block_hash, hex(int(index))], self.rpc_url
        )

    async def get_transaction_by_block_number_and_index(self, block_number, index):
        return await self.rpc_client.post(
            "eth_getTransactionByBlockNumberAndIndex",
            [hex(int(block_number)), hex(int(index))],
            self.rpc_url,
        )
