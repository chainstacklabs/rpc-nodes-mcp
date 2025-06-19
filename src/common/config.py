import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Settings:
    def __init__(self):
        # Set default RPC URLs
        self.ARBITRUM_RPC_URL = os.getenv(
            "ARBITRUM_RPC_URL",
            "https://arbitrum-mainnet.core.chainstack.com/fbc89075f67357ebc91140b9327b414e",
        )
        self.BASE_RPC_URL = os.getenv(
            "BASE_RPC_URL",
            "https://base-mainnet.core.chainstack.com/4d9c1f91e76f25d6095138096ce006b2",
        )
        self.BINANCE_SMART_CHAIN_RPC_URL = os.getenv(
            "BINANCE_SMART_CHAIN_RPC_URL",
            "https://bsc-mainnet.core.chainstack.com/9ba68ca151306ade5d3307dfd4437d4a",
        )
        self.ETHEREUM_RPC_URL = os.getenv(
            "ETHEREUM_RPC_URL",
            "https://ethereum-mainnet.core.chainstack.com/9668d156902a4a323163ec5bd652278e",
        )
        self.SONIC_RPC_URL = os.getenv(
            "SONIC_RPC_URL",
            "https://sonic-mainnet.core.chainstack.com/461f2690f6239ecb0f1640fa3224027b",
        )
        self.SOLANA_RPC_URL = os.getenv(
            "SOLANA_RPC_URL",
            "https://solana-mainnet.core.chainstack.com/c1f70bbc35644bd95ae98c944984230a",
        )

        for key, value in os.environ.items():
            if not hasattr(self, key):
                setattr(self, key, value)


settings = Settings()
