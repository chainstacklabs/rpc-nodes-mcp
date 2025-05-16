"""
Base-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from config import settings

from core.adapter_registry import register_adapter
from core.interfaces import RpcClient
from servers.evm.evm import EvmAdapter


@register_adapter("base")
class BaseChainAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.BASE_RPC_URL, rpc_client=rpc_client)
