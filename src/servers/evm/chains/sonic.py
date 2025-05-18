"""
Sonic-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from common.config import settings
from common.interfaces import RpcClient
from servers.evm.common.adapter_registry import register_adapter
from servers.evm.evm import EvmAdapter


@register_adapter("sonic")
class SonicAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.SONIC_RPC_URL, rpc_client=rpc_client)
