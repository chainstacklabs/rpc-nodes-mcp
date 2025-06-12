"""
Solana-specific implementation of the BlockchainAdapter.
"""

from common.config import settings
from common.interfaces import RpcClient
from servers.solana.common.adapter_registry import register_adapter
from servers.solana.solana import SolanaAdapter


@register_adapter("solana")
class SolanaChainAdapter(SolanaAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.SOLANA_RPC_URL, rpc_client=rpc_client)
