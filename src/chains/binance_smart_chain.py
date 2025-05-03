"""
BSC-specific implementation of the BlockchainAdapter using EVM base logic.
"""

from chains.evm import EvmAdapter
from config import settings
from core.adapter_registry import register_adapter
from core.interfaces import RpcClient


@register_adapter("binance smart chain")
class BinanceSmartChainAdapter(EvmAdapter):
    def __init__(self, rpc_client: RpcClient = None):
        super().__init__(rpc_url=settings.BINANCE_SMART_CHAIN_RPC_URL, rpc_client=rpc_client)
