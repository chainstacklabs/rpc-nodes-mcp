"""MCP tools for transaction-related JSON-RPC calls."""

from mcp.types import CallToolResult

import servers.evm.common.client as client
from common.utils import _err, _ok
from servers.evm.tool_registry import mcp


@mcp.tool(
    name="web3_clientVersion",
    description=(
        "Call the web3_clientVersion JSON-RPC method to retrieve the current client version of the Ethereum node.\n\n"
        "Description: Returns the current client version of the Ethereum node.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: A string representing the Ethereum client version.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "web3_clientVersion",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "web3_clientVersion", "readOnlyHint": True},
)
async def web3_clientVersion(chain: str) -> CallToolResult:
    try:
        return _ok(await client.web3_clientVersion(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="web3_sha3",
    description=(
        "Call the web3_sha3 JSON-RPC method to compute the Keccak-256 (not the standardized SHA3-256) hash of the provided data.\n\n"
        "Description: Returns Keccak-256 (not the standardized SHA3-256) of the given data.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "- data (str): The data to convert into a SHA3 hash (must be a hex string with 0x prefix).\n\n"
        "Returns: A hex string containing the SHA3 result.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "web3_sha3",\n'
        '  "params": ["0x68656c6c6f20776f726c64"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "web3_sha3", "readOnlyHint": True},
)
async def web3_sha3(chain: str, data: str) -> CallToolResult:
    try:
        return _ok(await client.web3_sha3(chain.lower(), data))
    except Exception as e:
        return _err(str(e))


# @mcp.tool(
#     name="net_version",
#     description=(
#         "Call the net_version JSON-RPC method to retrieve the current network ID.\n\n"
#         "Description: Returns the current network ID used by the client.\n\n"
#         "Parameters:\n"
#         "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
#         "Returns: A string representing the network ID.\n\n"
#         "Example:\n"
#         'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
#         "{\n"
#         '  "jsonrpc": "2.0",\n'
#         '  "method": "net_version",\n'
#         '  "params": [],\n'
#         '  "id": 1\n'
#         "}'"
#     ),
#     annotations={"title": "net_version", "readOnlyHint": True},
# )
# async def net_version(chain: str) -> CallToolResult:
#     try:
#         return _ok(await client.net_version(chain.lower()))
#     except Exception as e:
#         return _err(str(e))


# @mcp.tool(
#     name="net_listening",
#     description=(
#         "Call the net_listening JSON-RPC method to determine if the client is actively listening for network connections.\n\n"
#         "Description: Returns true if the client is actively listening for network connections, otherwise false.\n\n"
#         "Parameters:\n"
#         "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
#         "Returns: A boolean value indicating if the client is listening.\n\n"
#         "Example:\n"
#         'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
#         "{\n"
#         '  "jsonrpc": "2.0",\n'
#         '  "method": "net_listening",\n'
#         '  "params": [],\n'
#         '  "id": 1\n'
#         "}'"
#     ),
#     annotations={"title": "net_listening", "readOnlyHint": True},
# )
# async def net_listening(chain: str) -> CallToolResult:
#     try:
#         return _ok(await client.net_listening(chain.lower()))
#     except Exception as e:
#         return _err(str(e))


# @mcp.tool(
#     name="net_peerCount",
#     description=(
#         "Call the net_peerCount JSON-RPC method to retrieve the number of peers currently connected to the client.\n\n"
#         "Description: Returns the number of peers currently connected to the client as a hexadecimal string.\n\n"
#         "Parameters:\n"
#         "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
#         "Returns: A hex string representing the number of connected peers.\n\n"
#         "Example:\n"
#         'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
#         "{\n"
#         '  "jsonrpc": "2.0",\n'
#         '  "method": "net_peerCount",\n'
#         '  "params": [],\n'
#         '  "id": 1\n'
#         "}'"
#     ),
#     annotations={"title": "net_peerCount", "readOnlyHint": True},
# )
# async def net_peerCount(chain: str) -> CallToolResult:
#     try:
#         return _ok(await client.net_peerCount(chain.lower()))
#     except Exception as e:
#         return _err(str(e))


@mcp.tool(
    name="eth_syncing",
    description=(
        "Call the eth_syncing JSON-RPC method to check if the node is syncing.\n\n"
        "Description: Returns an object with data about the sync status or false if the node is not syncing.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: An object with sync status or false.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_syncing",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_syncing", "readOnlyHint": True},
)
async def eth_syncing(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_syncing(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_chainId",
    description=(
        "Call the eth_chainId JSON-RPC method to retrieve the chain ID.\n\n"
        "Description: Returns the chain ID used by the current network.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: A hex string representing the chain ID.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_chainId",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_chainId", "readOnlyHint": True},
)
async def eth_chainId(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_chainId(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_blockNumber",
    description=(
        "Call the eth_blockNumber JSON-RPC method to retrieve the current block number.\n\n"
        "Description: Returns the number of the most recent block.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: A hex string representing the latest block number.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_blockNumber",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_blockNumber", "readOnlyHint": True},
)
async def eth_blockNumber(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_blockNumber(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_gasPrice",
    description=(
        "Call the eth_gasPrice JSON-RPC method to retrieve the current gas price in wei.\n\n"
        "Description: Returns the current price per gas in wei.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: A hex string of the current gas price in wei.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_gasPrice",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_gasPrice", "readOnlyHint": True},
)
async def eth_gasPrice(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_gasPrice(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_feeHistory",
    description=(
        "Call the eth_feeHistory JSON-RPC method to retrieve a list of historical gas fee data.\n\n"
        "Description: Returns fee history for the last blocks to estimate EIP-1559 fee parameters.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_count (str): Number of blocks in the requested range.\n"
        "- newest_block (str): Highest block number in the range.\n"
        "- reward_percentiles (list[str], optional): A list of percentile values for priority fee rewards.\n\n"
        "Returns: An object with baseFeePerGas, gasUsedRatio, and optional rewards.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_feeHistory",\n'
        '  "params": ["0x5", "latest", [10, 30, 50, 70, 90]],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_feeHistory", "readOnlyHint": True},
)
async def eth_feeHistory(
    chain: str,
    block_count: str,
    newest_block: str,
    reward_percentiles: list[str] = [],
) -> CallToolResult:
    try:
        return _ok(
            await client.eth_feeHistory(
                chain.lower(), block_count, newest_block, reward_percentiles
            )
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_maxPriorityFeePerGas",
    description=(
        "Call the eth_maxPriorityFeePerGas JSON-RPC method to get the suggested max priority fee per gas.\n\n"
        "Description: Returns a suggested max priority fee per gas in wei.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "Returns: A hex string representing the priority fee per gas.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_maxPriorityFeePerGas",\n'
        '  "params": [],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_maxPriorityFeePerGas", "readOnlyHint": True},
)
async def eth_maxPriorityFeePerGas(chain: str) -> CallToolResult:
    try:
        return _ok(await client.eth_maxPriorityFeePerGas(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBalance",
    description=(
        "Call the eth_getBalance JSON-RPC method to get the balance of an address.\n\n"
        "Description: Returns the balance of the account of given address in wei.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- address (str): Address to check the balance of (0x-prefixed).\n"
        "- block (str): Block number or keyword like 'latest', 'earliest', or 'pending'.\n\n"
        "Returns: A hex string with the balance in wei.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBalance",\n'
        '  "params": ["0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBalance", "readOnlyHint": True},
)
async def eth_getBalance(chain: str, address: str, block: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getBalance(chain.lower(), address, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getStorageAt",
    description=(
        "Call the eth_getStorageAt JSON-RPC method to retrieve the value at a storage position.\n\n"
        "Description: Returns the value from a storage position at a given address.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- address (str): The address of the storage contract.\n"
        "- position (str): The hex-encoded position in storage.\n"
        "- block (str): Block number or keyword like 'latest', 'earliest', or 'pending'.\n\n"
        "Returns: The value at that storage position as a hex string.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getStorageAt",\n'
        '  "params": ["0x1234567890abcdef1234567890abcdef12345678", "0x0", "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getStorageAt", "readOnlyHint": True},
)
async def eth_getStorageAt(chain: str, address: str, position: str, block: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getStorageAt(chain.lower(), address, position, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getTransactionCount",
    description=(
        "Call the eth_getTransactionCount JSON-RPC method to get the number of transactions sent from an address.\n\n"
        "Description: Returns the number of transactions sent from an address (nonce).\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- address (str): The address to get the nonce for.\n"
        "- block (str): Block number or keyword like 'latest', 'earliest', or 'pending'.\n\n"
        "Returns: A hex string with the nonce.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getTransactionCount",\n'
        '  "params": ["0x1234567890abcdef1234567890abcdef12345678", "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getTransactionCount", "readOnlyHint": True},
)
async def eth_getTransactionCount(chain: str, address: str, block: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getTransactionCount(chain.lower(), address, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getCode",
    description=(
        "Call the eth_getCode JSON-RPC method to retrieve the contract code at a given address.\n\n"
        "Description: Returns code at a given address. Useful for identifying smart contracts.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- address (str): The address to get the code from.\n"
        "- block (str): Block number or keyword like 'latest', 'earliest', or 'pending'.\n\n"
        "Returns: A hex string containing the contract code.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getCode",\n'
        '  "params": ["0x1234567890abcdef1234567890abcdef12345678", "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getCode", "readOnlyHint": True},
)
async def eth_getCode(chain: str, address: str, block: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getCode(chain.lower(), address, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_call",
    description=(
        "Call the eth_call JSON-RPC method to simulate a contract call without submitting a transaction.\n\n"
        "Description: Executes a new message call immediately without creating a transaction on the blockchain.\n"
        "You can also override contract storage and account values using optional state override parameters.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- from_address (str, optional): Sender address.\n"
        "- to_address (str): Target contract address.\n"
        "- gas (str, optional): Gas limit (hex).\n"
        "- gas_price (str, optional): Gas price (hex).\n"
        "- value (str, optional): Value to send (hex).\n"
        "- data (str, optional): Encoded function call data.\n"
        "- block (str): Block number or keyword (e.g., 'latest').\n"
        "- override_address (str, optional): Address to apply state overrides to.\n"
        "- override_balance (str, optional): Fake balance (hex).\n"
        "- override_nonce (str, optional): Fake nonce (hex).\n"
        "- override_code (str, optional): Fake EVM bytecode (hex).\n"
        "- override_state (dict, optional): Full key-value storage overrides.\n"
        "- override_state_diff (dict, optional): Partial key-value storage diff overrides.\n\n"
        "Returns: Hex-encoded result of the contract method execution.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_call",\n'
        '  "params": [\n'
        '    {"to": "0x6b175474e89094c44da98b954eedeac495271d0f", "data": "0x70a08231..."},\n'
        '    "latest",\n'
        '    {"0x111...111": {"balance": "0xFFFF..."}}\n'
        "  ],\n"
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_call", "readOnlyHint": True},
)
async def eth_call(
    chain: str,
    from_address: str = None,
    to_address: str = "",
    gas: str = None,
    gas_price: str = None,
    value: str = None,
    data: str = None,
    block: str = "latest",
    override_address: str = None,
    override_balance: str = None,
    override_nonce: str = None,
    override_code: str = None,
    override_state: dict = None,
    override_state_diff: dict = None,
) -> CallToolResult:
    try:
        call_object = {
            "to": to_address,
        }
        if from_address:
            call_object["from"] = from_address
        if gas:
            call_object["gas"] = gas
        if gas_price:
            call_object["gasPrice"] = gas_price
        if value:
            call_object["value"] = value
        if data:
            call_object["data"] = data

        overrides = None
        if override_address:
            overrides = {override_address: {}}
            if override_balance:
                overrides[override_address]["balance"] = override_balance
            if override_nonce:
                overrides[override_address]["nonce"] = override_nonce
            if override_code:
                overrides[override_address]["code"] = override_code
            if override_state:
                overrides[override_address]["state"] = override_state
            if override_state_diff:
                overrides[override_address]["stateDiff"] = override_state_diff

        return _ok(await client.eth_call(chain.lower(), call_object, block, overrides))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_estimateGas",
    description=(
        "Call the eth_estimateGas JSON-RPC method to estimate the gas required to execute a transaction.\n\n"
        "Description: Simulates a transaction to estimate the gas usage without broadcasting it. Supports optional state override.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- from_address (str, optional): Sender address.\n"
        "- to_address (str): Recipient contract or account address.\n"
        "- gas (str, optional): Gas limit (hex).\n"
        "- gas_price (str, optional): Gas price (hex).\n"
        "- value (str, optional): Value to send (hex).\n"
        "- data (str, optional): Encoded method data.\n"
        "- block (str, optional): Block number or keyword (e.g., 'latest').\n"
        "- override_address (str, optional): Address to override state for.\n"
        "- override_balance (str, optional): Fake balance for that address.\n"
        "- override_nonce (str, optional): Fake nonce.\n"
        "- override_code (str, optional): Fake bytecode.\n"
        "- override_state (dict, optional): Complete storage override.\n"
        "- override_state_diff (dict, optional): Partial storage override.\n\n"
        "Returns: Estimated gas usage as a hex string.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_estimateGas",\n'
        '  "params": [{"from": "0x...", "to": "0x...", "value": "0x..."}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_estimateGas", "readOnlyHint": True},
)
async def eth_estimateGas(
    chain: str,
    from_address: str = None,
    to_address: str = "",
    gas: str = None,
    gas_price: str = None,
    value: str = None,
    data: str = None,
    block: str = "latest",
    override_address: str = None,
    override_balance: str = None,
    override_nonce: str = None,
    override_code: str = None,
    override_state: dict = None,
    override_state_diff: dict = None,
) -> CallToolResult:
    try:
        tx = {"to": to_address}
        if from_address:
            tx["from"] = from_address
        if gas:
            tx["gas"] = gas
        if gas_price:
            tx["gasPrice"] = gas_price
        if value:
            tx["value"] = value
        if data:
            tx["data"] = data

        overrides = None
        if override_address:
            overrides = {override_address: {}}
            if override_balance:
                overrides[override_address]["balance"] = override_balance
            if override_nonce:
                overrides[override_address]["nonce"] = override_nonce
            if override_code:
                overrides[override_address]["code"] = override_code
            if override_state:
                overrides[override_address]["state"] = override_state
            if override_state_diff:
                overrides[override_address]["stateDiff"] = override_state_diff

        return _ok(await client.eth_estimateGas(chain.lower(), tx, block, overrides))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBlockByHash",
    description=(
        "Call the eth_getBlockByHash JSON-RPC method to get information about a block using its hash.\n\n"
        "Description: Returns information about a block by block hash.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_hash (str): The hash of the block.\n"
        "- full_tx (bool): Whether to return full transaction objects or only hashes.\n\n"
        "Returns: A block object or null if not found.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBlockByHash",\n'
        '  "params": ["0x...", true],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBlockByHash", "readOnlyHint": True},
)
async def eth_getBlockByHash(chain: str, block_hash: str, full_tx: bool) -> CallToolResult:
    try:
        return _ok(await client.eth_getBlockByHash(chain.lower(), block_hash, full_tx))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBlockByNumber",
    description=(
        "Call the eth_getBlockByNumber JSON-RPC method to get information about a block using its number.\n\n"
        "Description: Returns information about a block by block number.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_number (str): The block number or keyword like 'latest'.\n"
        "- full_tx (bool): Whether to return full transaction objects or only hashes.\n\n"
        "Returns: A block object or null if not found.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBlockByNumber",\n'
        '  "params": ["latest", true],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBlockByNumber", "readOnlyHint": True},
)
async def eth_getBlockByNumber(chain: str, block_number: str, full_tx: bool) -> CallToolResult:
    try:
        return _ok(await client.eth_getBlockByNumber(chain.lower(), block_number, full_tx))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBlockTransactionCountByHash",
    description=(
        "Call the eth_getBlockTransactionCountByHash JSON-RPC method to get the number of transactions in a block by its hash.\n\n"
        "Description: Returns the number of transactions in a block matching the given block hash.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_hash (str): The hash of the block.\n\n"
        "Returns: A hex string with the transaction count.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBlockTransactionCountByHash",\n'
        '  "params": ["0x..."],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBlockTransactionCountByHash", "readOnlyHint": True},
)
async def eth_getBlockTransactionCountByHash(chain: str, block_hash: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getBlockTransactionCountByHash(chain.lower(), block_hash))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBlockTransactionCountByNumber",
    description=(
        "Call the eth_getBlockTransactionCountByNumber JSON-RPC method to get the number of transactions in a block by its number.\n\n"
        "Description: Returns the number of transactions in a block matching the given block number.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_number (str): The block number or keyword like 'latest'.\n\n"
        "Returns: A hex string with the transaction count.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBlockTransactionCountByNumber",\n'
        '  "params": ["latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBlockTransactionCountByNumber", "readOnlyHint": True},
)
async def eth_getBlockTransactionCountByNumber(chain: str, block_number: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getBlockTransactionCountByNumber(chain.lower(), block_number))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getTransactionByHash",
    description=(
        "Call the eth_getTransactionByHash JSON-RPC method to get a transaction by its hash.\n\n"
        "Description: Returns the information about a transaction requested by transaction hash.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- tx_hash (str): The hash of the transaction.\n\n"
        "Returns: A transaction object or null if not found.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getTransactionByHash",\n'
        '  "params": ["0x..."],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getTransactionByHash", "readOnlyHint": True},
)
async def eth_getTransactionByHash(chain: str, tx_hash: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getTransactionByHash(chain.lower(), tx_hash))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getTransactionReceipt",
    description=(
        "Call the eth_getTransactionReceipt JSON-RPC method to retrieve the receipt of a transaction.\n\n"
        "Description: Returns the transaction receipt by hash. The receipt includes execution results, logs, gas usage, and other metadata.\n"
        "Returns null if the transaction is not yet mined or not found.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- tx_hash (str): The hash of the transaction to query.\n\n"
        "Returns: A transaction receipt object or null.\n\n"
        "Returned object includes:\n"
        "- blockHash: Hash of the block where the transaction was included.\n"
        "- blockNumber: Block number (hex).\n"
        "- contractAddress: Created contract address (if contract creation), otherwise null.\n"
        "- cumulativeGasUsed: Total gas used in the block up to and including this tx (hex).\n"
        "- effectiveGasPrice: Gas price paid (base + tip) per unit (hex).\n"
        "- from: Sender address.\n"
        "- to: Recipient address (null if contract creation).\n"
        "- gasUsed: Gas used by this specific transaction (hex).\n"
        "- logs: List of event logs generated by this transaction.\n"
        "- logsBloom: Bloom filter for quick log retrieval.\n"
        "- status: 0x1 (success) or 0x0 (failure).\n"
        "- transactionHash: Hash of the transaction.\n"
        "- transactionIndex: Index position within the block (hex).\n"
        "- type: Transaction type identifier (e.g., '0x2').\n"
        "- Each log includes: address, topics[], data, logIndex, blockNumber, blockHash, txHash, txIndex, removed.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getTransactionReceipt",\n'
        '  "params": ["0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getTransactionReceipt", "readOnlyHint": True},
)
async def eth_getTransactionReceipt(chain: str, tx_hash: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getTransactionReceipt(chain.lower(), tx_hash))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getLogs",
    description=(
        "Call the eth_getLogs JSON-RPC method to fetch logs emitted by smart contracts based on filter parameters.\n\n"
        "Description: Returns an array of log objects that match the filter options. You can filter by address, topics, block range, and block hashes.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- from_block (str, optional): Start block number or tag (e.g., 'latest', 'earliest').\n"
        "- to_block (str, optional): End block number or tag.\n"
        "- address (str, optional): Address of the contract to filter logs for.\n"
        "- topics (list[str], optional): List of topic filters (e.g., event signature hashes).\n"
        "- block_hash (str, optional): Specific block hash to filter logs (cannot be used with fromBlock/toBlock).\n\n"
        "Returns: An array of log objects.\n\n"
        "Each log object includes:\n"
        "- address: Address that emitted the log.\n"
        "- topics: List of indexed event parameters (first topic is the event signature).\n"
        "- data: Unindexed event data.\n"
        "- blockNumber: Block number where the log was generated.\n"
        "- transactionHash: Transaction hash that produced the log.\n"
        "- transactionIndex: Index of the transaction in the block.\n"
        "- blockHash: Hash of the block.\n"
        "- logIndex: Index of the log in the block.\n"
        "- removed: True if log was removed due to chain reorg, else False.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getLogs",\n'
        '  "params": [{"fromBlock": "0x1", "toBlock": "latest", "address": "0x..."}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getLogs", "readOnlyHint": True},
)
async def eth_getLogs(
    chain: str,
    from_block: str = None,
    to_block: str = None,
    address: str = None,
    topics: list[str] = None,
    block_hash: str = None,
) -> CallToolResult:
    try:
        filter_params = {}
        if from_block:
            filter_params["fromBlock"] = from_block
        if to_block:
            filter_params["toBlock"] = to_block
        if address:
            filter_params["address"] = address
        if topics:
            filter_params["topics"] = topics
        if block_hash:
            filter_params["blockHash"] = block_hash

        return _ok(await client.eth_getLogs(chain.lower(), filter_params))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="debug_traceTransaction",
    description=(
        "Call the debug_traceTransaction JSON-RPC method to trace the execution of a transaction.\n\n"
        "Description: Re-executes a transaction exactly as the Ethereum node would, returning detailed execution trace data.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- tx_hash (str): Transaction hash to trace.\n"
        "- tracer (str, optional): Tracer type (e.g., 'callTracer', 'prestateTracer').\n"
        "- only_top_call (bool, optional): If true, trace only the top-level call (used in tracerConfig).\n"
        "- diff_mode (bool, optional): If true, returns pre and post state diff (used in tracerConfig).\n"
        "- timeout (str, optional): Timeout string for the trace call (e.g., '10s').\n\n"
        "Returns: A trace object with execution metadata.\n\n"
        "Returned trace fields include:\n"
        "- type: Call type (e.g., CALL).\n"
        "- from: Sender address.\n"
        "- to: Recipient or contract address.\n"
        "- value: Transferred value (hex).\n"
        "- gas / gasUsed: Provided and consumed gas (hex).\n"
        "- input / output: Data sent and returned.\n"
        "- error / revertReason: Error info, if applicable.\n"
        "- calls: Nested traced calls.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "debug_traceTransaction",\n'
        '  "params": ["0x...", {"tracer": "callTracer", "tracerConfig": {"onlyTopCall": true}}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "debug_traceTransaction", "readOnlyHint": True},
)
async def debug_traceTransaction(
    chain: str,
    tx_hash: str,
    tracer: str = None,
    only_top_call: bool = None,
    diff_mode: bool = None,
    timeout: str = None,
) -> CallToolResult:
    try:
        options = {}

        if tracer:
            options["tracer"] = tracer

        config = {}
        if only_top_call is not None:
            config["onlyTopCall"] = only_top_call
        if diff_mode is not None:
            config["diffMode"] = diff_mode
        if config:
            options["tracerConfig"] = config

        if timeout:
            options["timeout"] = timeout

        return _ok(await client.debug_traceTransaction(chain.lower(), tx_hash, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="debug_traceCall",
    description=(
        "Call the debug_traceCall JSON-RPC method to trace the execution of a call without broadcasting it.\n\n"
        "Description: Simulates a contract call at a given block and returns an execution trace. Useful for inspecting internal call behavior.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- from_address (str, optional): Sender address.\n"
        "- to_address (str): Target contract address.\n"
        "- gas (str, optional): Gas limit (hex).\n"
        "- gas_price (str, optional): Gas price (hex).\n"
        "- value (str, optional): ETH value sent (hex).\n"
        "- data (str, optional): Encoded method input.\n"
        "- block (str): Block tag or number (e.g., 'latest').\n"
        "- tracer (str, optional): Tracer type (e.g., 'callTracer').\n"
        "- only_top_call (bool, optional): Trace only top-level call if true.\n"
        "- diff_mode (bool, optional): Show state diff if true.\n"
        "- timeout (str, optional): Timeout string (e.g., '5s').\n\n"
        "Returns: A transaction trace object with the following fields:\n"
        "- failed: Boolean indicating whether the execution failed.\n"
        "- gas: Total gas consumed during execution (hex).\n"
        "- returnValue: Return value of the call (hex).\n"
        "- structLogs: List of execution steps with:\n"
        "  - pc: Current program counter (bytecode index).\n"
        "  - op: Opcode name being executed.\n"
        "  - gas: Remaining gas at that step.\n"
        "  - gasCost: Gas cost of the operation.\n"
        "  - depth: Call stack depth.\n"
        "  - error: Error message, if any.\n"
        "  - stack: Current EVM stack values.\n"
        "  - memory: Current EVM memory.\n"
        "  - storage: Current storage mapping.\n"
        "  - refund: Refund counter value.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "debug_traceCall",\n'
        '  "params": [{"to": "0x...", "data": "0x..."}, "latest", {"tracer": "callTracer"}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "debug_traceCall", "readOnlyHint": True},
)
async def debug_traceCall(
    chain: str,
    from_address: str = None,
    to_address: str = "",
    gas: str = None,
    gas_price: str = None,
    value: str = None,
    data: str = None,
    block: str = "latest",
    tracer: str = None,
    only_top_call: bool = None,
    diff_mode: bool = None,
    timeout: str = None,
) -> CallToolResult:
    try:
        call_object = {"to": to_address}
        if from_address:
            call_object["from"] = from_address
        if gas:
            call_object["gas"] = gas
        if gas_price:
            call_object["gasPrice"] = gas_price
        if value:
            call_object["value"] = value
        if data:
            call_object["data"] = data

        options = {}
        if tracer:
            options["tracer"] = tracer

        config = {}
        if only_top_call is not None:
            config["onlyTopCall"] = only_top_call
        if diff_mode is not None:
            config["diffMode"] = diff_mode
        if config:
            options["tracerConfig"] = config

        if timeout:
            options["timeout"] = timeout

        return _ok(await client.debug_traceCall(chain.lower(), call_object, block, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="debug_traceBlock",
    description=(
        "Call the debug_traceBlock JSON-RPC method to trace all transactions in a block.\n\n"
        "Description: Executes all transactions in the provided block and returns detailed traces for each.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- rlp_encoded_block (str): The RLP-encoded full block containing transactions.\n"
        "- tracer (str, optional): Tracer type (e.g., 'callTracer', 'prestateTracer').\n"
        "- only_top_call (bool, optional): If true, traces only top-level calls.\n"
        "- diff_mode (bool, optional): If true, includes pre/post state differences.\n"
        "- timeout (str, optional): Tracer timeout value (e.g., '5s').\n\n"
        "Returns: An array of transaction trace objects with the following fields:\n"
        "- type: Call type (CALL, STATICCALL, etc).\n"
        "- from: Sender address.\n"
        "- to: Target contract or address.\n"
        "- value: Transferred ETH (hex).\n"
        "- gas: Provided gas (hex).\n"
        "- gasUsed: Gas consumed (hex).\n"
        "- input: Input data of the call.\n"
        "- output: Returned output data.\n"
        "- calls: Nested sub-calls, if any.\n\n"
        "Each sub-call also includes the same structure recursively.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "debug_traceBlock",\n'
        '  "params": ["RLP_ENCODED_BLOCK", {"tracer": "callTracer"}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "debug_traceBlock", "readOnlyHint": True},
)
async def debug_traceBlock(
    chain: str,
    rlp_encoded_block: str,
    tracer: str = None,
    only_top_call: bool = None,
    diff_mode: bool = None,
    timeout: str = None,
) -> CallToolResult:
    try:
        options = {}
        if tracer:
            options["tracer"] = tracer

        config = {}
        if only_top_call is not None:
            config["onlyTopCall"] = only_top_call
        if diff_mode is not None:
            config["diffMode"] = diff_mode
        if config:
            options["tracerConfig"] = config

        if timeout:
            options["timeout"] = timeout

        return _ok(await client.debug_traceBlock(chain.lower(), rlp_encoded_block, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="debug_traceBlockByHash",
    description=(
        "Call the debug_traceBlockByHash JSON-RPC method to trace all transactions in a block using its hash.\n\n"
        "Description: Re-executes and traces every transaction in the block identified by the given hash.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_hash (str): Hash of the block to trace.\n"
        "- tracer (str, optional): Type of tracer (e.g., 'callTracer', 'prestateTracer').\n"
        "- only_top_call (bool, optional): If true, traces only top-level calls.\n"
        "- diff_mode (bool, optional): If true, returns pre/post state differences.\n"
        "- timeout (str, optional): Timeout duration string (e.g., '5s').\n\n"
        "Returns: A list of trace objects for each transaction in the block, each with:\n"
        "- type: Call type (e.g., CALL, STATICCALL).\n"
        "- from: Sender address.\n"
        "- to: Target contract or address.\n"
        "- value: ETH value transferred (hex).\n"
        "- gas: Gas provided (hex).\n"
        "- gasUsed: Gas consumed (hex).\n"
        "- input: Call input data.\n"
        "- output: Returned output data.\n"
        "- calls: List of nested sub-calls, each with the same structure.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "debug_traceBlockByHash",\n'
        '  "params": ["0x97b49e4...", {"tracer": "callTracer"}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "debug_traceBlockByHash", "readOnlyHint": True},
)
async def debug_traceBlockByHash(
    chain: str,
    block_hash: str,
    tracer: str = None,
    only_top_call: bool = None,
    diff_mode: bool = None,
    timeout: str = None,
) -> CallToolResult:
    try:
        options = {}
        if tracer:
            options["tracer"] = tracer

        config = {}
        if only_top_call is not None:
            config["onlyTopCall"] = only_top_call
        if diff_mode is not None:
            config["diffMode"] = diff_mode
        if config:
            options["tracerConfig"] = config

        if timeout:
            options["timeout"] = timeout

        return _ok(await client.debug_traceBlockByHash(chain.lower(), block_hash, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="debug_traceBlockByNumber",
    description=(
        "Call the debug_traceBlockByNumber JSON-RPC method to trace all transactions in a block by number.\n\n"
        "Description: Re-executes and traces every transaction in the specified block.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_number (str): Block number or tag (e.g., 'latest', 'pending', 'finalized').\n"
        "- tracer (str, optional): Tracer type (e.g., 'callTracer', 'prestateTracer').\n"
        "- only_top_call (bool, optional): If true, traces only top-level calls.\n"
        "- diff_mode (bool, optional): If true, includes pre/post state differences.\n"
        "- timeout (str, optional): Optional timeout (e.g., '5s').\n\n"
        "Returns: A list of transaction trace objects, each with:\n"
        "- type: Type of call (CALL, STATICCALL, etc).\n"
        "- from / to: Sender and receiver addresses.\n"
        "- value: Transferred amount in hex.\n"
        "- gas / gasUsed: Gas limit and consumed gas.\n"
        "- input / output: Call input and output data.\n"
        "- calls: List of internal sub-calls, each with the same structure.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "debug_traceBlockByNumber",\n'
        '  "params": ["latest", {"tracer": "callTracer"}],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "debug_traceBlockByNumber", "readOnlyHint": True},
)
async def debug_traceBlockByNumber(
    chain: str,
    block_number: str,
    tracer: str = None,
    only_top_call: bool = None,
    diff_mode: bool = None,
    timeout: str = None,
) -> CallToolResult:
    try:
        options = {}
        if tracer:
            options["tracer"] = tracer

        config = {}
        if only_top_call is not None:
            config["onlyTopCall"] = only_top_call
        if diff_mode is not None:
            config["diffMode"] = diff_mode
        if config:
            options["tracerConfig"] = config

        if timeout:
            options["timeout"] = timeout

        return _ok(await client.debug_traceBlockByNumber(chain.lower(), block_number, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_call",
    description=(
        "Call the trace_call JSON-RPC method to execute a call and return a full trace.\n\n"
        "Description: Executes a transaction call as if it were mined in the specified block and returns a detailed execution trace.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- from_address (str, optional): Sender address.\n"
        "- to_address (str): Target contract address.\n"
        "- gas (str, optional): Gas limit (hex).\n"
        "- gas_price (str, optional): Gas price (hex).\n"
        "- value (str, optional): ETH value to send (hex).\n"
        "- data (str, optional): Call data (hex).\n"
        "- trace_types (list[str]): List of trace types (e.g., ['trace'], ['vmTrace', 'stateDiff']).\n"
        "- block (str): Block tag or number (e.g., 'latest').\n\n"
        "Returns: A trace result object with the following fields:\n"
        "- output: Return value of the call.\n"
        "- stateDiff: Changes to Ethereum state caused by the call.\n"
        "- trace: List of actions performed during the call, including:\n"
        "  - action: {from, to, value, gas, input, callType}.\n"
        "  - result: {gasUsed, output}.\n"
        "  - subtraces: Number of sub-calls.\n"
        "  - traceAddress: Call path.\n"
        "  - type: Call type (e.g., call, create).\n"
        "- vmTrace: Full virtual machine trace (if requested).\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_call",\n'
        '  "params": [{"to": "0x6b17...", "data": "0x70a0..."}, ["trace"], "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_call", "readOnlyHint": True},
)
async def trace_call(
    chain: str,
    from_address: str = None,
    to_address: str = "",
    gas: str = None,
    gas_price: str = None,
    value: str = None,
    data: str = None,
    trace_types: list[str] = ["trace"],
    block: str = "latest",
) -> CallToolResult:
    try:
        call_object = {"to": to_address}
        if from_address:
            call_object["from"] = from_address
        if gas:
            call_object["gas"] = gas
        if gas_price:
            call_object["gasPrice"] = gas_price
        if value:
            call_object["value"] = value
        if data:
            call_object["data"] = data

        return _ok(await client.trace_call(chain.lower(), call_object, trace_types, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_callMany",
    description=(
        "Call the trace_callMany JSON-RPC method to simulate multiple contract calls and return trace results for each.\n\n"
        "Description: Executes multiple calls in the context of the same block and returns detailed traces for each.\n\n"
        "Parameters:\n"
        "- chain (str): Must be Ethereum.\n"
        "- calls (list): List of objects, each with 'call' and 'trace_types' fields.\n"
        "  * call (dict): Contains from, to, value, gas, data, etc.\n"
        "  * trace_types (list[str]): e.g., ['trace'], ['vmTrace'].\n"
        "- block (str): Block tag or number (e.g., 'latest').\n\n"
        "Expected input format for `calls`:\n"
        "[\n"
        "  {\n"
        '    "call": {\n'
        '      "from": "0x...",\n'
        '      "to": "0x...",\n'
        '      "value": "0x...",\n'
        '      "data": "0x..."\n'
        "    },\n"
        '    "trace_types": ["trace"]\n'
        "  }\n"
        "]\n\n"
        "Returns: A list of trace results per call.\n"
        "Each trace includes output, stateDiff, trace actions, and vmTrace (if requested).\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_callMany",\n'
        '  "params": [[\n'
        '    {"call": {"to": "0x...", "data": "0x..."}, "trace_types": ["trace"]}\n'
        '  ], "latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_callMany", "readOnlyHint": True},
)
async def trace_callMany(
    chain: str,
    calls: list[dict],
    block: str,
) -> CallToolResult:
    try:
        formatted_calls = [[c["call"], c["trace_types"]] for c in calls]
        return _ok(await client.trace_callMany(chain.lower(), formatted_calls, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_rawTransaction",
    description=(
        "Call the trace_rawTransaction JSON-RPC method to simulate and trace a raw transaction.\n\n"
        "Description: Executes a raw, signed Ethereum transaction without broadcasting it and returns trace data based on selected trace types.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- raw_tx (str): The raw transaction data as a 0x-prefixed hex string.\n"
        "- trace_types (list[str]): List of trace types to return, such as ['trace'], ['vmTrace'], or ['stateDiff'].\n\n"
        "Returns: A list containing one trace result object with the following fields:\n"
        "- output: Return data of the call (hex).\n"
        "- stateDiff: State changes caused by execution.\n"
        "- trace: Low-level actions with:\n"
        "  - action: Includes from, to, value, gas, input, callType.\n"
        "  - result: Contains gasUsed and output.\n"
        "  - subtraces: Number of internal calls.\n"
        "  - traceAddress: Nested call path.\n"
        "  - type: Call type (e.g., call, create).\n"
        "- vmTrace: Full VM instruction trace, including gas cost and state transitions.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_rawTransaction",\n'
        '  "params": ["0xf86c...", ["trace"]],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_rawTransaction", "readOnlyHint": True},
)
async def trace_rawTransaction(
    chain: str, raw_tx: str, trace_types: list[str] = ["trace"]
) -> CallToolResult:
    try:
        return _ok(await client.trace_rawTransaction(chain.lower(), raw_tx, trace_types))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_replayTransaction",
    description=(
        "Call the trace_replayTransaction JSON-RPC method to replay a transaction and return trace data.\n\n"
        "Description: Re-executes a mined transaction using the current state and returns detailed traces including EVM execution steps, state changes, and basic action info.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- tx_hash (str): Transaction hash to replay.\n"
        "- trace_types (list[str]): Types of traces to include (e.g., ['trace'], ['vmTrace', 'stateDiff']).\n\n"
        "Returns: A trace result object with the following fields:\n"
        "- output: Return value from the transaction execution.\n"
        "- stateDiff: Mapping of all state changes caused by execution.\n"
        "- trace: List of low-level call actions:\n"
        "  - action: Contains from, to, value, gas, input, callType.\n"
        "  - result: Contains gasUsed and output.\n"
        "  - traceAddress: Path to subcalls.\n"
        "  - type: Call type (e.g., call, create).\n"
        "- vmTrace: Instruction-level trace of the EVM (if requested).\n"
        "- transactionHash: The hash of the replayed transaction.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_replayTransaction",\n'
        '  "params": ["0x3277c7...", ["trace"]],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_replayTransaction", "readOnlyHint": True},
)
async def trace_replayTransaction(
    chain: str,
    tx_hash: str,
    trace_types: list[str],
) -> CallToolResult:
    try:
        return _ok(await client.trace_replayTransaction(chain.lower(), tx_hash, trace_types))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_replayBlockTransactions",
    description=(
        "Call the trace_replayBlockTransactions JSON-RPC method to replay all transactions in a block and return traces.\n\n"
        "Description: Re-executes all transactions in the specified block and returns trace data for each transaction. "
        "Supported trace types include 'trace', 'vmTrace', and 'stateDiff'.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_number (str): Block number or tag (e.g., 'latest', 'pending', 'finalized').\n"
        "- trace_types (list[str]): List of trace types to return, such as ['trace'], ['vmTrace'], or ['stateDiff'].\n\n"
        "Returns: A list of trace result objects, one per transaction, each with:\n"
        "- output: Hex-encoded return value of the transaction.\n"
        "- stateDiff: Ethereum state changes caused by the transaction.\n"
        "- trace: Sequence of low-level actions:\n"
        "  - action: Includes from, to, gas, input, value, callType.\n"
        "  - result: Contains gasUsed and output.\n"
        "  - traceAddress: Execution path for nested calls.\n"
        "  - type: Method type ('call', 'create', etc).\n"
        "- vmTrace: Full EVM instruction trace with gas and stack/memory transitions (if requested).\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_replayBlockTransactions",\n'
        '  "params": ["0xccb93d", ["trace"]],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_replayBlockTransactions", "readOnlyHint": True},
)
async def trace_replayBlockTransactions(
    chain: str,
    block_number: str,
    trace_types: list[str],
) -> CallToolResult:
    try:
        return _ok(
            await client.trace_replayBlockTransactions(chain.lower(), block_number, trace_types)
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="trace_block",
    description=(
        "Call the trace_block JSON-RPC method to trace all transactions in a block by number.\n\n"
        "Description: Replays and returns trace information for each transaction in the given block. "
        "This method works with Parity/OpenEthereum-compatible nodes.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains..\n"
        "- block_number (str): Block number in hex format or tag (e.g., 'latest').\n\n"
        "Returns: A list of trace objects for each transaction, including:\n"
        "- action: Object with from, to, value, gas, input, callType.\n"
        "- blockHash: Hash of the block containing the transaction.\n"
        "- blockNumber: Number of the block.\n"
        "- error: Execution error message, if any.\n"
        "- result: Execution result with:\n"
        "  - gasUsed: Gas consumed by the transaction.\n"
        "  - output: Returned value (hex).\n"
        "- subtraces: Number of internal calls.\n"
        "- traceAddress: Path to nested calls.\n"
        "- transactionHash: Hash of the traced transaction.\n"
        "- transactionPosition: Index of the transaction in the block.\n"
        "- type: Type of call (e.g., 'call', 'create').\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "trace_block",\n'
        '  "params": ["0xccb93d"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "trace_block", "readOnlyHint": True},
)
async def trace_block(chain: str, block_number: str) -> CallToolResult:
    try:
        return _ok(await client.trace_block(chain.lower(), block_number))
    except Exception as e:
        return _err(str(e))


# @mcp.tool(
#     name="eth_getProof",
#     description=(
#         "Call the eth_getProof JSON-RPC method to get Merkle proof for account and storage values.\n\n"
#         "Description: Returns the account and storage values of the specified account including the Merkle-proof.\n\n"
#         "Parameters:\n"
#         "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
#         "- address (str): The address of the account or contract.\n"
#         "- storage_keys (list[str]): Array of storage-keys to be proofed and included.\n"
#         "- block (str): Block number or keyword like 'latest', 'earliest', or 'pending'.\n\n"
#         "Returns: Account proof object with balance, codeHash, nonce, storageHash, accountProof, and storageProof.\n\n"
#         "Example:\n"
#         'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
#         "{\n"
#         '  "jsonrpc": "2.0",\n'
#         '  "method": "eth_getProof",\n'
#         '  "params": ["0x...", ["0x0000000000000000000000000000000000000000000000000000000000000000"], "latest"],\n'
#         '  "id": 1\n'
#         "}'"
#     ),
#     annotations={"title": "eth_getProof", "readOnlyHint": True},
# )
# async def eth_getProof(
#     chain: str, address: str, storage_keys: list[str], block: str = "latest"
# ) -> CallToolResult:
#     try:
#         return _ok(await client.eth_getProof(chain.lower(), address, storage_keys, block))
#     except Exception as e:
#         return _err(str(e))


@mcp.tool(
    name="eth_simulateV1",
    description=(
        "Call the eth_simulateV1 JSON-RPC method to simulate transaction execution with state overrides.\n\n"
        "Description: Simulates a list of transactions on top of a block and returns trace data.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "- block_state_calls (dict): Object containing blockOverrides, stateOverrides, and calls arrays.\n"
        "- block (str): Block number or keyword like 'latest'.\n"
        "- validation (bool, optional): Enable validation. Default is True.\n"
        "- trace_transfers (bool, optional): Include trace transfers. Default is False.\n\n"
        "Returns: Simulation result with call results and traces.\n\n"
        "Example:\n"
        'curl -X POST https://ethereum-mainnet.core.chainstack.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_simulateV1",\n'
        '  "params": [\n'
        "    {\n"
        '      "blockStateCalls": [{\n'
        '        "calls": [{"from": "0x...", "to": "0x...", "value": "0x1"}]\n'
        "      }],\n"
        '      "validation": true\n'
        "    },\n"
        '    "latest"\n'
        "  ],\n"
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_simulateV1", "readOnlyHint": True},
)
async def eth_simulateV1(
    chain: str,
    block_state_calls: dict,
    block: str = "latest",
    validation: bool = True,
    trace_transfers: bool = False,
) -> CallToolResult:
    try:
        params = {
            "blockStateCalls": block_state_calls.get("blockStateCalls", []),
            "validation": validation,
            "traceTransfers": trace_transfers,
        }
        if "stateOverrides" in block_state_calls:
            params["stateOverrides"] = block_state_calls["stateOverrides"]
        if "blockOverrides" in block_state_calls:
            params["blockOverrides"] = block_state_calls["blockOverrides"]

        return _ok(await client.eth_simulateV1(chain.lower(), params, block))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="eth_getBlockReceipts",
    description=(
        "Call the eth_getBlockReceipts JSON-RPC method to get all transaction receipts for a block.\n\n"
        "Description: Returns all transaction receipts for a given block.\n\n"
        "Parameters:\n"
        "- chain (str): Blockchain name. Run get_supported_blockchains tool to get the list of supported blockchains.\n"
        "- block (str): Block number (hex) or keyword like 'latest', 'earliest', or 'pending'.\n\n"
        "Returns: Array of transaction receipt objects for all transactions in the block.\n\n"
        "Example:\n"
        'curl -X POST https://nd-422-757-666.p2pify.com/key -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "method": "eth_getBlockReceipts",\n'
        '  "params": ["latest"],\n'
        '  "id": 1\n'
        "}'"
    ),
    annotations={"title": "eth_getBlockReceipts", "readOnlyHint": True},
)
async def eth_getBlockReceipts(chain: str, block: str) -> CallToolResult:
    try:
        return _ok(await client.eth_getBlockReceipts(chain.lower(), block))
    except Exception as e:
        return _err(str(e))
