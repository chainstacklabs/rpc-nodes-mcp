import logging

import src.servers.evm.chains
import src.servers.evm.tools
from src.common.logger import setup_file_logging
from src.servers.evm.server import mcp


def main():
    setup_file_logging(filename="mcp-evm-server.log", level=logging.INFO)
    mcp.run()


if __name__ == "__main__":
    main()
