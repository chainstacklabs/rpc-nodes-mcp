"""
Arbitrum-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from common.config import settings
from core.adapter_registry import register_adapter
from core.interfaces import RpcClient
from servers.evm.evm import EvmAdapter


@register_adapter("arbitrum")
class ArbitrumAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.ARBITRUM_RPC_URL, rpc_client=rpc_client)
