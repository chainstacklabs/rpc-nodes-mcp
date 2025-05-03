from unittest.mock import AsyncMock, MagicMock

import pytest

from core.adapter_registry import registry
from core.client import fetch_transaction


async def test_fetch_transaction_delegates_to_adapter():
    mock_adapter = MagicMock()
    mock_adapter.fetch_transaction = AsyncMock(return_value={"tx": "data"})

    original_adapter = registry.get("ethereum")
    registry["ethereum"] = mock_adapter

    try:
        result = await fetch_transaction("ethereum", "0x123")
        assert result == {"tx": "data"}
        mock_adapter.fetch_transaction.assert_called_once_with("0x123")
    finally:
        if original_adapter:
            registry["ethereum"] = original_adapter
        else:
            del registry["ethereum"]


async def test_fetch_transaction_unsupported_blockchain():
    with pytest.raises(ValueError, match="Unsupported blockchain: nonexistent"):
        await fetch_transaction("nonexistent", "0x123")
