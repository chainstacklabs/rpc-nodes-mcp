import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Settings:
    def __init__(self):
        for key, value in os.environ.items():
            setattr(self, key, value)


settings = Settings()
