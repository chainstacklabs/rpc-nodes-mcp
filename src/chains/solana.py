"""
Solana-specific implementation of the BlockchainAdapter using shared JSON-RPC logic.
"""

from config import settings
from core.adapter_registry import register_adapter
from core.interfaces import BlockchainAdapter, RpcClient
from core.rpc import HttpxRpcClient


@register_adapter("solana")
class SolanaAdapter(BlockchainAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        self.rpc_client = rpc_client or HttpxRpcClient()
        self.rpc_url = settings.SOLANA_RPC_URL

    async def fetch_transaction(self, sig: str) -> dict:
        return await self.rpc_client.post(
            "getTransaction",
            [sig, {"encoding": "base64", "maxSupportedTransactionVersion": 0}],
            endpoint=self.rpc_url,
        )
