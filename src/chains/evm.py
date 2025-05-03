"""
Reusable base class for all EVM-compatible blockchain adapters.
"""

from core.interfaces import BlockchainAdapter, RpcClient
from core.rpc import HttpxRpcClient


class EvmAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def fetch_transaction(self, tx_id: str) -> dict:
        if not tx_id.startswith("0x"):
            tx_id = "0x" + tx_id

        result = await self.rpc_client.post(
            method="eth_getTransactionByHash", params=[tx_id], endpoint=self.rpc_url
        )
        return result
