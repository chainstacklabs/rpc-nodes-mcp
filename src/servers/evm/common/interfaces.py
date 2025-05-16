"""
Abstract base class defining the interface all blockchain adapters must implement.
"""

from abc import ABC, abstractmethod


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

    @abstractmethod
    async def get_block_number(self) -> str:
        """eth_blockNumber  – Solana: getSlot"""

    @abstractmethod
    async def get_block_by_hash(self, block_hash: str, full_tx: bool = False) -> dict:
        """eth_getBlockByHash – Solana: getBlock"""

    @abstractmethod
    async def get_block_by_number(self, block_number: str, full_tx: bool = False) -> dict:
        """eth_getBlockByNumber – Solana: getBlock"""

    @abstractmethod
    async def get_balance(self, address: str, block: str = "latest") -> str:
        """eth_getBalance – Solana: getBalance"""

    @abstractmethod
    async def call(self, payload: dict, block: str = "latest") -> str:
        """eth_call – Solana: simulateTransaction"""

    @abstractmethod
    async def gas_price(self) -> str:
        """eth_gasPrice – Solana: getFeeForMessage (lamports/compute-unit)"""
