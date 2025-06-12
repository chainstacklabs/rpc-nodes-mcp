"""
Solana-specific implementation of the BlockchainAdapter.
"""

from src.common.config import settings
from src.common.interfaces import RpcClient
from src.servers.solana.common.adapter_registry import register_adapter
from src.servers.solana.solana import SolanaAdapter


@register_adapter("solana")
class SolanaChainAdapter(SolanaAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.SOLANA_RPC_URL, rpc_client=rpc_client)
