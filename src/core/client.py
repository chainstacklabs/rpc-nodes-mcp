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


async def get_block_number(blockchain: str) -> str:
    return await _adapter(blockchain).get_block_number()


async def get_block_by_hash(blockchain: str, block_hash: str, full_tx: bool = False) -> dict:
    return await _adapter(blockchain).get_block_by_hash(block_hash, full_tx)


async def get_block_by_number(blockchain: str, block_number: str, full_tx: bool = False) -> dict:
    return await _adapter(blockchain).get_block_by_number(block_number, full_tx)


async def get_balance(blockchain: str, address: str, block: str = "latest") -> str:
    return await _adapter(blockchain).get_balance(address, block)


async def eth_call(blockchain: str, payload: dict, block: str = "latest") -> str:
    return await _adapter(blockchain).call(payload, block)


async def gas_price(blockchain: str) -> str:
    return await _adapter(blockchain).gas_price()
