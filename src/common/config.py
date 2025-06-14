import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Settings:
    def __init__(self):
        # Set default RPC URLs
        self.ARBITRUM_RPC_URL = os.getenv(
            "ARBITRUM_RPC_URL", "https://nd-000-364-211.p2pify.com/5b8d22690a57f293b3a1ed8758014e35"
        )
        self.BASE_RPC_URL = os.getenv(
            "BASE_RPC_URL",
            "https://base-mainnet.core.chainstack.com/2fc1de7f08c0465f6a28e3c355e0cb14",
        )
        self.BINANCE_SMART_CHAIN_RPC_URL = os.getenv(
            "BINANCE_SMART_CHAIN_RPC_URL",
            "https://bsc-mainnet.core.chainstack.com/35848e183f3e3303c8cfeacbea831cab",
        )
        self.ETHEREUM_RPC_URL = os.getenv(
            "ETHEREUM_RPC_URL", "https://nd-422-757-666.p2pify.com/0a9d79d93fb2f4a4b1e04695da2b77a7"
        )
        self.SONIC_RPC_URL = os.getenv("SONIC_RPC_URL", "https://rpc.soniclabs.com")
        self.SOLANA_RPC_URL = os.getenv(
            "SOLANA_RPC_URL", "https://nd-326-444-187.p2pify.com/9de47db917d4f69168e3fed02217d15b"
        )

        for key, value in os.environ.items():
            if not hasattr(self, key):
                setattr(self, key, value)


settings = Settings()
