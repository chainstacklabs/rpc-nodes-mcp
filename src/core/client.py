"""
Client dispatcher that routes blockchain transaction requests
through registered BlockchainAdapter instances.
"""

from core.adapter_registry import registry


async def fetch_transaction(blockchain: str, tx_id: str) -> dict:
    adapter = registry.get(blockchain)
    if not adapter:
        raise ValueError(f"Unsupported blockchain: {blockchain}")
    return await adapter.fetch_transaction(tx_id)
