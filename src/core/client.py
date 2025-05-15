"""
Client dispatcher that routes blockchain transaction requests
through registered BlockchainAdapter instances.
"""

from core.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad


async def get_transaction_by_hash(chain, tx_hash):
    return await _adapter(chain).get_transaction_by_hash(tx_hash)


async def get_transaction_by_block_hash_and_index(chain, block_hash, index):
    return await _adapter(chain).get_transaction_by_block_hash_and_index(block_hash, index)


async def get_transaction_by_block_number_and_index(chain, block_number, index):
    return await _adapter(chain).get_transaction_by_block_number_and_index(block_number, index)
