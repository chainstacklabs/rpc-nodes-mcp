"""
Shared JSON-RPC helper to reduce duplication across blockchain adapters.
"""

import httpx

from common.interfaces import RpcClient


class HttpxRpcClient(RpcClient):
    async def post(self, method: str, params: list, endpoint: str) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                endpoint, json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
            )

            response_data = resp.json()

            if "error" in response_data:
                error_data = response_data["error"]
                error_message = error_data.get("message", "Unknown RPC error")
                error_code = error_data.get("code", -1)
                raise ValueError(f"RPC Error ({error_code}): {error_message}")

            return response_data.get("result")
