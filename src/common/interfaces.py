from abc import ABC, abstractmethod


class RpcClient(ABC):
    @abstractmethod
    async def post(self, method: str, params: list, endpoint: str) -> dict:
        pass
