"""
Ethereum-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from chains.evm import EvmAdapter
from config import settings
from core.adapter_registry import register_adapter
from core.interfaces import RpcClient


@register_adapter("ethereum")
class EthereumAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.ETHEREUM_RPC_URL, rpc_client=rpc_client)
