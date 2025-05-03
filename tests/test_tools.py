from unittest.mock import AsyncMock, patch

from tools.transaction import get_transaction


async def test_get_transaction_success():
    mock_tx_data = {"hash": "0x123", "from": "0xabc"}

    with patch("tools.transaction.fetch_transaction", new=AsyncMock(return_value=mock_tx_data)):
        result = await get_transaction("ethereum", "0x123")

        assert not result.isError
        assert len(result.content) == 1
        assert result.content[0].text == str(mock_tx_data)


async def test_get_transaction_error():
    with patch(
        "tools.transaction.fetch_transaction", new=AsyncMock(side_effect=ValueError("Test error"))
    ):
        result = await get_transaction("ethereum", "0x123")

        assert result.isError
        assert result.content[0].text.startswith("Error:")
