from unittest.mock import AsyncMock

from chains.solana import SolanaAdapter
from core.interfaces import RpcClient


class MockRpcClient(RpcClient):
    def __init__(self, mock_response=None):
        self.mock_response = mock_response or {"signature": "sig123", "slot": 12345}
        self.post_mock = AsyncMock(return_value=self.mock_response)

    async def post(self, method: str, params: list, endpoint: str) -> dict:
        return await self.post_mock(method=method, params=params, endpoint=endpoint)


async def test_solana_fetch_transaction():
    mock_client = MockRpcClient()
    adapter = SolanaAdapter(rpc_client=mock_client)
    result = await adapter.fetch_transaction("sig123")

    assert result == mock_client.mock_response
    mock_client.post_mock.assert_called_once()

    call_args = mock_client.post_mock.call_args.kwargs
    assert call_args["method"] == "getTransaction"
    assert call_args["params"] == [
        "sig123",
        {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0},
    ]
    assert call_args["endpoint"] == adapter.rpc_url
