"""
Shared JSON-RPC helper to reduce duplication across blockchain adapters.
"""

import json
import logging
import time

import httpx

from src.common.interfaces import RpcClient
from src.common.logger import get_logger

logger = get_logger(__name__)


class HttpxRpcClient(RpcClient):
    async def post(self, method: str, params: list, endpoint: str) -> dict:
        logger.info(f"Making RPC call: method={method}, endpoint={endpoint}")

        if logger.isEnabledFor(logging.DEBUG):
            safe_params = self._prepare_params_for_logging(params)
            logger.debug(f"Request params: {safe_params}")

        try:
            async with httpx.AsyncClient(timeout=120) as client:
                logger.debug(f"Sending HTTP request to {endpoint}")
                start_time = time.time()
                resp = await client.post(
                    endpoint, json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
                )
                elapsed_time = time.time() - start_time
                logger.debug(
                    f"RPC response received in {elapsed_time:.2f}s with status {resp.status_code}"
                )

                response_data = resp.json()
                if "error" in response_data:
                    error_data = response_data["error"]
                    error_message = error_data.get("message", "Unknown RPC error")
                    error_code = error_data.get("code", -1)
                    logger.error(f"RPC Error ({error_code}): {error_message} for method={method}")
                    raise ValueError(f"RPC Error ({error_code}): {error_message}")

                logger.info(f"RPC call successful: method={method}, time={elapsed_time:.2f}s")
                # Log result size but not content for privacy and brevity
                result = response_data.get("result")
                if isinstance(result, (list, dict)):
                    logger.debug(f"Result size: {len(result)} items")
                return result

        except httpx.RequestError as e:
            logger.error(f"HTTP request failed for {method}: {str(e)}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON response for method={method}")
            raise ValueError(f"Invalid JSON response from RPC endpoint: {endpoint}")
        except Exception:
            logger.exception(f"Unexpected error in RPC call {method}")
            raise

    def _prepare_params_for_logging(self, params):
        """Prepare parameters for safe logging by truncating large values."""
        if not params:
            return []

        MAX_LENGTH = 100  # Maximum length for string representation

        safe_params = []
        for param in params:
            if isinstance(param, str) and len(param) > MAX_LENGTH:
                safe_params.append(f"{param[:MAX_LENGTH]}... (truncated, total len: {len(param)})")
            elif isinstance(param, (dict, list)) and len(str(param)) > MAX_LENGTH:
                type_name = type(param).__name__
                if isinstance(param, dict):
                    size = len(param)
                    safe_params.append(f"<{type_name} with {size} items> (truncated)")
                else:
                    safe_params.append(f"<{type_name} of length {len(param)}> (truncated)")
            else:
                safe_params.append(param)

        return safe_params
