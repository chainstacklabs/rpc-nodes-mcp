from unittest.mock import AsyncMock

from chains.ethereum import EthereumAdapter
from core.interfaces import RpcClient


class MockRpcClient(RpcClient):
    def __init__(self, mock_response=None):
        self.mock_response = mock_response or {
            "hash": "0x123",
            "from": "0xabc",
            "to": "0xdef",
        }
        self.post_mock = AsyncMock(return_value=self.mock_response)

    async def post(self, method: str, params: list, endpoint: str) -> dict:
        return await self.post_mock(method=method, params=params, endpoint=endpoint)


async def test_ethereum_fetch_transaction():
    mock_client = MockRpcClient()
    adapter = EthereumAdapter(rpc_client=mock_client)
    result = await adapter.fetch_transaction("0x123abc")

    assert result == mock_client.mock_response
    mock_client.post_mock.assert_called_once()

    call_args = mock_client.post_mock.call_args.kwargs
    assert call_args["method"] == "eth_getTransactionByHash"
    assert call_args["params"] == ["0x123abc"]
    assert call_args["endpoint"] == adapter.rpc_url
