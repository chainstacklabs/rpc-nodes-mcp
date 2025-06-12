"""
Arbitrum-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from src.common.config import settings
from src.common.interfaces import RpcClient
from src.servers.evm.common.adapter_registry import register_adapter
from src.servers.evm.evm import EvmAdapter


@register_adapter("arbitrum")
class ArbitrumAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.ARBITRUM_RPC_URL, rpc_client=rpc_client)
