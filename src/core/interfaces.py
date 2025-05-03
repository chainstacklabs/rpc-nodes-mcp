"""
Abstract base class defining the interface all blockchain adapters must implement.
"""

from abc import ABC, abstractmethod


class RpcClient(ABC):
    @abstractmethod
    async def post(self, method: str, params: list, endpoint: str) -> dict:
        pass


class BlockchainAdapter(ABC):
    @abstractmethod
    async def fetch_transaction(self, tx_id: str) -> dict:
        pass
