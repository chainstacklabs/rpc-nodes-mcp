import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Settings:
    def __init__(self):
        # Set default RPC URLs
        self.ARBITRUM_RPC_URL = os.getenv("ARBITRUM_RPC_URL", "https://arb1.arbitrum.io/rpc")
        self.BASE_RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
        self.BINANCE_SMART_CHAIN_RPC_URL = os.getenv(
            "BINANCE_SMART_CHAIN_RPC_URL", "https://bsc-dataseed.binance.org"
        )
        self.ETHEREUM_RPC_URL = os.getenv("ETHEREUM_RPC_URL", "https://eth.llamarpc.com")
        self.SONIC_RPC_URL = os.getenv("SONIC_RPC_URL", "https://rpc.soniclabs.com")
        self.SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

        for key, value in os.environ.items():
            if not hasattr(self, key):
                setattr(self, key, value)


settings = Settings()
