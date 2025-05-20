import logging

import servers.solana.chains
import servers.solana.tools
from common.logger import setup_file_logging
from servers.solana.server import mcp

setup_file_logging(filename="mcp-solana-server.log", level=logging.INFO)

if __name__ == "__main__":
    mcp.run()
