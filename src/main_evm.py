import logging

import servers.evm.chains
import servers.evm.tools
from common.logger import setup_file_logging
from servers.evm.server import mcp


def main():
    setup_file_logging(filename="mcp-evm-server.log", level=logging.INFO)
    mcp.run()


if __name__ == "__main__":
    main()
