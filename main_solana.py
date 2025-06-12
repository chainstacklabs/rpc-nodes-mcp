import logging
import os
import sys

# Add src to Python path so internal imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import src.servers.solana.chains
import src.servers.solana.tools
from src.common.logger import setup_file_logging
from src.servers.solana.server import mcp


def main():
    setup_file_logging(filename="mcp-solana-server.log", level=logging.INFO)
    mcp.run()


if __name__ == "__main__":
    main()
