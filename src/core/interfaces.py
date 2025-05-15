"""
Abstract base class defining the interface all blockchain adapters must implement.
"""

from abc import ABC, abstractmethod


class RpcClient(ABC):
    @abstractmethod
    async def post(self, method: str, params: list, endpoint: str) -> dict:
        pass


class BlockchainAdapter(ABC):
    """Unified interface every chain‑specific adapter must provide."""

    @abstractmethod
    async def get_transaction_by_hash(self, tx_hash: str) -> dict: ...

    @abstractmethod
    async def get_transaction_by_block_hash_and_index(
        self, block_hash: str, index: str
    ) -> dict: ...

    @abstractmethod
    async def get_transaction_by_block_number_and_index(
        self, block_number: str, index: str
    ) -> dict: ...
