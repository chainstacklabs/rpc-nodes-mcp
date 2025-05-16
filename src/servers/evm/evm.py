"""
Reusable base class for all EVM-compatible blockchain adapters.
"""

from common.interfaces import RpcClient
from common.rpc import HttpxRpcClient
from servers.evm.common.interfaces import BlockchainAdapter


class EvmAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def get_transaction_by_hash(self, tx_hash):
        return await self.rpc_client.post("eth_getTransactionByHash", [tx_hash], self.rpc_url)

    async def get_transaction_by_block_hash_and_index(self, block_hash, index):
        return await self.rpc_client.post(
            "eth_getTransactionByBlockHashAndIndex", [block_hash, hex(int(index))], self.rpc_url
        )

    async def get_transaction_by_block_number_and_index(self, block_number, index):
        return await self.rpc_client.post(
            "eth_getTransactionByBlockNumberAndIndex",
            [hex(int(block_number)), hex(int(index))],
            self.rpc_url,
        )

    # TODO: implement them
    async def get_block_number(self) -> str:
        raise NotImplementedError("TODO: implement it")

    async def get_block_by_hash(self, block_hash: str, full_tx: bool = False) -> dict:
        raise NotImplementedError("TODO: implement it")

    async def get_block_by_number(self, block_number: str, full_tx: bool = False) -> dict:
        raise NotImplementedError("TODO: implement it")

    async def get_balance(self, address: str, block: str = "latest") -> str:
        return int(await self.rpc_client.post("eth_getBalance", [address, block], self.rpc_url), 16)

    async def call(self, payload: dict, block: str = "latest") -> str:
        raise NotImplementedError("TODO: implement it")

    async def gas_price(self) -> str:
        raise NotImplementedError("TODO: implement it")
