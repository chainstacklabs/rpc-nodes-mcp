"""
Decorator-based registry for automatically registering blockchain adapters.
"""

from core.interfaces import BlockchainAdapter

registry: dict[str, BlockchainAdapter] = {}


def register_adapter(chain: str):
    def wrapper(adapter_cls):
        registry[chain] = adapter_cls()
        return adapter_cls

    return wrapper
