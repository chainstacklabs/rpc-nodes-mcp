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

    async def get_transaction_by_hash(self, sig: str) -> dict:
        return await self.rpc_client.post(
            "getTransaction",
            [sig, {"encoding": "base64", "maxSupportedTransactionVersion": 0}],
            endpoint=self.rpc_url,
        )

    async def get_transaction_by_block_hash_and_index(self, block_hash: str, index: str) -> dict:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def get_transaction_by_block_number_and_index(
        self, block_number: str, index: str
    ) -> dict:
        raise NotImplementedError("Unavailable for Solana RPC")

    # TODO: implement/review them
    async def get_block_number(self) -> str:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def get_block_by_hash(self, block_hash: str, full_tx: bool = False) -> dict:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def get_block_by_number(self, block_number: str, full_tx: bool = False) -> dict:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def get_balance(self, address: str, block: str = "latest") -> str:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def call(self, payload: dict, block: str = "latest") -> str:
        raise NotImplementedError("Unavailable for Solana RPC")

    async def gas_price(self) -> str:
        raise NotImplementedError("Unavailable for Solana RPC")
