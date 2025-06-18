"""
Auto-generated MCP tools for JSON-RPC methods.
"""

import json

from mcp.types import CallToolResult

import servers.solana.common.client as client
from common.utils import _err, _ok
from servers.solana.tool_registry import mcp


@mcp.tool(
    name="getaccountinfo",
    description=(
        "Call the getAccountInfo JSON-RPC method.\n"
        "Returns detailed account information for a given public key.\n\n"
        "Parameters:\n"
        "- chain (str): Must be Solana.\n"
        "- account (str): The base-58 encoded public key of the account to query.\n"
        "- encoding (str, optional): Encoding format for account data. One of: 'base58', 'base64', 'base64+zstd', 'jsonParsed'.\n"
        "    - base58: Slow and limited to Account data less than 129 bytes.\n"
        "    - base64: Returns base64-encoded data for Account data of any size.\n"
        "    - base64+zstd: Compresses the Account data using Zstandard, then base64-encodes the result.\n"
        "    - jsonParsed: Attempts to use program-specific state parsers to return more human-readable and explicit account state data.\n"
        "      If jsonParsed is requested but a parser cannot be found, the field falls back to base64 encoding. This can be detected when the data field is a string. Default is base64.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- data_slice (dict, optional): A dictionary with optional 'offset' and 'length' integers to specify a slice of the account data.\n"
        "- min_context_slot (str, optional): Minimum slot that the request can be evaluated at.\n\n"
        "Returns: Account information object including lamports, owner, data, executable, rentEpoch, and space.\n\n"
        "Example:\n"
        'curl -X POST https://api.devnet.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getAccountInfo",\n'
        '  "params": [\n'
        '    "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg",\n'
        '    { "encoding": "base58" }\n'
        "  ]\n"
        "}'"
    ),
    annotations={"title": "getAccountInfo", "readOnlyHint": True},
)
async def getaccountinfo(
    chain: str,
    account: str,
    encoding: str = "base64",
    commitment: str = "finalized",
    data_slice: dict = None,
    min_context_slot: str = None,
) -> CallToolResult:
    try:
        options = {
            "encoding": encoding,
            "commitment": commitment,
        }
        if data_slice:
            options["dataSlice"] = data_slice
        if min_context_slot:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getaccountinfo(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getbalance",
    description=(
        "Call the getBalance JSON-RPC method to retrieve the lamport balance of a given Solana account.\n\n"
        "Parameters:\n"
        "- chain (str): Must be Solana.\n"
        "- account (str): The base-58 encoded public key of the account. [Example: 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM]\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): The minimum slot that the request can be evaluated at.\n\n"
        "Returns: Balance of the account in lamports as a numeric value.\n\n"
        "Example:\n"
        'curl -X POST https://api.devnet.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBalance",\n'
        '  "params": [\n'
        '    "83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri"\n'
        "  ]\n"
        "}'"
    ),
    annotations={"title": "getBalance", "readOnlyHint": True},
)
async def getbalance(
    chain: str,
    account: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {"commitment": commitment}
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getbalance(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblock",
    description=(
        "Call the getBlock JSON-RPC method to retrieve information about a block by slot number.\n\n"
        "Parameters:\n"
        "- chain (str): Must be Solana.\n"
        "- slot (int): Slot number of the block to retrieve. [Example: 378967388]\n"
        "- encoding (str, optional): Encoding for returned transactions. Options:\n"
        "  - 'json'\n"
        "  - 'jsonParsed'\n"
        "  - 'base58'\n"
        "  - 'base64' (default)\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- transaction_details (str, optional): Level of transaction detail: 'full', 'accounts', 'signatures', or 'none'. Default is 'full'.\n"
        "- max_supported_transaction_version (int, optional): Maximum transaction version to return. Default is 0.\n"
        "- rewards (bool, optional): Whether to include rewards array. Default is True.\n\n"
        "Returns: Block details including transactions, blockhash, parent slot, block height, and optionally rewards.\n\n"
        "Example:\n"
        'curl -X POST https://api.devnet.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBlock",\n'
        '  "params": [\n'
        "    378967388,\n"
        "    {\n"
        '      "encoding": "json",\n'
        '      "maxSupportedTransactionVersion": 0,\n'
        '      "transactionDetails": "full",\n'
        '      "rewards": false\n'
        "    }\n"
        "  ]\n"
        "}'"
    ),
    annotations={"title": "getBlock", "readOnlyHint": True},
)
async def getblock(
    chain: str,
    slot: int,
    encoding: str = "base64",
    commitment: str = "finalized",
    transaction_details: str = "signatures",
    max_supported_transaction_version: int = 0,
    rewards: bool = False,
) -> CallToolResult:
    try:
        options = {
            "encoding": encoding,
            "commitment": commitment,
            "transactionDetails": transaction_details,
            "maxSupportedTransactionVersion": max_supported_transaction_version,
            "rewards": rewards,
        }
        return _ok(await client.getblock(chain.lower(), slot, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockcommitment",
    description=(
        "Call the getBlockCommitment JSON-RPC method to retrieve the commitment for a particular block.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- slot (int): Slot number of the block to retrieve commitment for.\n\n"
        "Returns: Commitment information for the specified block, including the commitment array and total stake.\n\n"
        "Example:\n"
        'curl -X POST https://api.devnet.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBlockCommitment",\n'
        '  "params": [\n'
        "    12345678\n"
        "  ]\n"
        "}'"
    ),
    annotations={"title": "getBlockCommitment", "readOnlyHint": True},
)
async def getblockcommitment(
    chain: str,
    slot: int,
) -> CallToolResult:
    try:
        return _ok(await client.getblockcommitment(chain.lower(), slot))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockheight",
    description=(
        "Call the getBlockHeight JSON-RPC method to retrieve the current block height of the node.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum slot at which the request can be evaluated.\n\n"
        "Returns: The current block height.\n"
    ),
    annotations={"title": "getBlockHeight", "readOnlyHint": True},
)
async def getblockheight(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getblockheight(chain.lower(), options))
    except Exception as e:
        return _err(str(e))


# @mcp.tool(
#     name="getblockproduction",
#     description=(
#         "Call the getBlockProduction JSON-RPC method to get recent block production stats.\n\n"
#         "Parameters:\n"
#         "- chain (str): Must be 'solana'.\n"
#         "- commitment (str, optional)\n"
#         "- identity (str, optional)\n"
#         "- first_slot (int, optional)\n"
#         "- last_slot (int, optional)\n"
#         "Returns: Validator block production info.\n"
#     ),
#     annotations={"title": "getBlockProduction", "readOnlyHint": True},
# )
# async def getblockproduction(
#     chain: str,
#     commitment: str = "finalized",
#     identity: str = None,
#     first_slot: int = None,
#     last_slot: int = None,
# ) -> CallToolResult:
#     try:
#         options = {}
#         if commitment:
#             options["commitment"] = commitment
#         if identity:
#             options["identity"] = identity
#         if first_slot is not None:
#             options["range"] = {"firstSlot": first_slot}
#             if last_slot is not None:
#                 options["range"]["lastSlot"] = last_slot
#         return _ok(await client.getblockproduction(chain.lower(), options))
#     except Exception as e:
#         return _err(str(e))


@mcp.tool(
    name="getblocks",
    description=(
        "Call the getBlocks JSON-RPC method to retrieve a list of confirmed blocks between two slots.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- start_slot (int): Start slot (inclusive).\n"
        "- end_slot (int, optional): End slot (inclusive).\n"
        "- commitment (str, optional): Desired commitment level (confirmed or finalized). Default is finalized.\n"
        "Returns: An array of confirmed block slots between the specified range.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBlocks",\n'
        '  "params": [100000000, 100000005, {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getBlocks", "readOnlyHint": True},
)
async def getblocks(
    chain: str,
    start_slot: int,
    end_slot: int = None,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getblocks(chain.lower(), start_slot, end_slot, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockswithlimit",
    description=(
        "Call the getBlocksWithLimit JSON-RPC method to retrieve a list of confirmed blocks starting at the given slot.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- start_slot (int): Start slot (inclusive).\n"
        "- limit (int, optional): Limit on the number of blocks to return (max 500,000).\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: An array of confirmed block slots starting at the specified slot.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBlocksWithLimit",\n'
        '  "params": [100000000, 3, {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getBlocksWithLimit", "readOnlyHint": True},
)
async def getblockswithlimit(
    chain: str,
    start_slot: int,
    limit: int = None,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(
            await client.getblockswithlimit(chain.lower(), start_slot, limit, options or None)
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblocktime",
    description=(
        "Call the getBlockTime JSON-RPC method to retrieve the estimated production time of a block.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- slot (int): Slot number of the block.\n\n"
        "Returns: Estimated Unix timestamp of when the block was produced.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getBlockTime",\n'
        '  "params": [100000000]\n'
        "}'"
    ),
    annotations={"title": "getBlockTime", "readOnlyHint": True},
)
async def getblocktime(
    chain: str,
    slot: int,
) -> CallToolResult:
    try:
        return _ok(await client.getblocktime(chain.lower(), slot))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getclusternodes",
    description=(
        "Call the getClusterNodes JSON-RPC method to retrieve information about all nodes in the cluster.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: A list of nodes, including their public key, gossip, TPU, RPC addresses, and software version.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getClusterNodes"}\''
    ),
    annotations={"title": "getClusterNodes", "readOnlyHint": True},
)
async def getclusternodes(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getclusternodes(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getepochinfo",
    description=(
        "Call the getEpochInfo JSON-RPC method to retrieve information about the current epoch.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum slot for evaluation.\n\n"
        "Returns: Info about the current epoch, including epoch number, slot index, and remaining slots.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getEpochInfo"}\''
    ),
    annotations={"title": "getEpochInfo", "readOnlyHint": True},
)
async def getepochinfo(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getepochinfo(chain.lower(), options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getepochschedule",
    description=(
        "Call the getEpochSchedule JSON-RPC method to retrieve epoch scheduling parameters.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: Epoch schedule details including slots per epoch, warmup phase, and first normal epoch.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getEpochSchedule"}\''
    ),
    annotations={"title": "getEpochSchedule", "readOnlyHint": True},
)
async def getepochschedule(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getepochschedule(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getfeeformessage",
    description=(
        "Call the getFeeForMessage JSON-RPC method to estimate the fee for a base64-encoded transaction message.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- message (str): Base64-encoded compiled transaction message.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum slot at which the request can be evaluated.\n\n"
        "Returns: Estimated transaction fee in lamports or null if invalid.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getFeeForMessage",\n'
        '  "params": ["AQABAgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQAA"]\n'
        "}'"
    ),
    annotations={"title": "getFeeForMessage", "readOnlyHint": True},
)
async def getfeeformessage(
    chain: str,
    message: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getfeeformessage(chain.lower(), message, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getfirstavailableblock",
    description=(
        "Call the getFirstAvailableBlock JSON-RPC method to retrieve the lowest slot still available on the node.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: The slot number of the first available block.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getFirstAvailableBlock"}\''
    ),
    annotations={"title": "getFirstAvailableBlock", "readOnlyHint": True},
)
async def getfirstavailableblock(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getfirstavailableblock(chain.lower()))
    except Exception as e:
        return _err(str(e))


# @mcp.tool(
#     name="getgenesishash",
#     description=(
#         "Call the getGenesisHash JSON-RPC method to retrieve the genesis hash of the current network.\n\n"
#         "Parameters:\n"
#         "- chain (str): Must be 'solana'.\n\n"
#         "Returns: The genesis hash as a base-58 encoded string.\n\n"
#         "Example:\n"
#         'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getGenesisHash"}\''
#     ),
#     annotations={"title": "getGenesisHash", "readOnlyHint": True},
# )
# async def getgenesishash(chain: str) -> CallToolResult:
#     try:
#         return _ok(await client.getgenesishash(chain.lower()))
#     except Exception as e:
#         return _err(str(e))


@mcp.tool(
    name="gethealth",
    description=(
        "Call the getHealth JSON-RPC method to check if the node is healthy.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: 'ok' if healthy, or an error string if not.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{"jsonrpc":"2.0","id":1,"method":"getHealth"}\''
    ),
    annotations={"title": "getHealth", "readOnlyHint": True},
)
async def gethealth(chain: str) -> CallToolResult:
    try:
        return _ok(await client.gethealth(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gethighestsnapshotslot",
    description=(
        "Call the getHighestSnapshotSlot JSON-RPC method to retrieve the highest full and incremental snapshot slot available.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: A JSON object with 'full' and 'incremental' slot numbers.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getHighestSnapshotSlot"\n'
        "}'"
    ),
    annotations={"title": "getHighestSnapshotSlot", "readOnlyHint": True},
)
async def gethighestsnapshotslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.gethighestsnapshotslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


# @mcp.tool(
#     name="getidentity",
#     description=(
#         "Call the getIdentity JSON-RPC method to retrieve the identity public key for the current node.\n\n"
#         "Parameters:\n"
#         "- chain (str): Must be 'solana'.\n\n"
#         "Returns: A JSON object containing the node's identity public key.\n\n"
#         "Example:\n"
#         'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
#         '  "jsonrpc": "2.0",\n'
#         '  "id": 1,\n'
#         '  "method": "getIdentity"\n'
#         "}'"
#     ),
#     annotations={"title": "getIdentity", "readOnlyHint": True},
# )
# async def getidentity(chain: str) -> CallToolResult:
#     try:
#         return _ok(await client.getidentity(chain.lower()))
#     except Exception as e:
#         return _err(str(e))


# @mcp.tool(
#     name="getinflationgovernor",
#     description=(
#         "Call the getInflationGovernor JSON-RPC method to retrieve the current inflation governor parameters.\n\n"
#         "Parameters:\n"
#         "- chain (str): Must be 'solana'.\n"
#         "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
#         "Returns: An object containing inflation parameters including foundation and validator rewards.\n\n"
#         "Example:\n"
#         'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
#         '  "jsonrpc": "2.0",\n'
#         '  "id": 1,\n'
#         '  "method": "getInflationGovernor"\n'
#         "}'"
#     ),
#     annotations={"title": "getInflationGovernor", "readOnlyHint": True},
# )
# async def getinflationgovernor(
#     chain: str,
#     commitment: str = "finalized",
# ) -> CallToolResult:
#     try:
#         options = {}
#         if commitment:
#             options["commitment"] = commitment
#         return _ok(await client.getinflationgovernor(chain.lower(), options))
#     except Exception as e:
#         return _err(str(e))


@mcp.tool(
    name="getinflationrate",
    description=(
        "Call the getInflationRate JSON-RPC method to retrieve the current inflation rate.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: A JSON object with current inflation rate details including total yearly percentage and validator rewards.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getInflationRate"\n'
        "}'"
    ),
    annotations={"title": "getInflationRate", "readOnlyHint": True},
)
async def getinflationrate(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getinflationrate(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getinflationreward",
    description=(
        "Call the getInflationReward JSON-RPC method to fetch the inflation reward for a list of addresses.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- addresses (List[str]): List of base-58 encoded account addresses.\n"
        "- epoch (int, optional): Epoch number to query.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: A list of inflation rewards corresponding to the given addresses.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "getInflationReward",\n'
        '  "params": [["vote111111111111111111111111111111111111111"], {"epoch": 345, "commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getInflationReward", "readOnlyHint": True},
)
async def getinflationreward(
    chain: str,
    addresses: list,
    epoch: int = None,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if epoch is not None:
            options["epoch"] = epoch
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getinflationreward(chain.lower(), addresses, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getlargestaccounts",
    description=(
        "Call the getLargestAccounts JSON-RPC method to retrieve the addresses of the largest accounts by lamport balance.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- filter (str, optional): Filter by account type, one of: 'circulating', 'nonCirculating'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: List of the 20 largest accounts and their balances.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getLargestAccounts",\n'
        '  "params": [{"filter": "circulating", "commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getLargestAccounts", "readOnlyHint": True},
)
async def getlargestaccounts(
    chain: str,
    filter: str = None,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if filter:
            options["filter"] = filter
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getlargestaccounts(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getlatestblockhash",
    description=(
        "Call the getLatestBlockhash JSON-RPC method to get the most recent blockhash and last valid block height.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot for the blockhash.\n\n"
        "Returns: A blockhash object with value and lastValidBlockHeight.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getLatestBlockhash",\n'
        '  "params": [{"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getLatestBlockhash", "readOnlyHint": True},
)
async def getlatestblockhash(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getlatestblockhash(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getleaderschedule",
    description=(
        "Call the getLeaderSchedule JSON-RPC method to get the current or specified slot leader schedule.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- slot (int, optional): Epoch start slot.\n"
        "- identity (str, optional): Validator identity to filter.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: Mapping of leader identity to assigned slot indexes.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getLeaderSchedule",\n'
        '  "params": [null, {"identity": "ValidatorPubkey"}]\n'
        "}'"
    ),
    annotations={"title": "getLeaderSchedule", "readOnlyHint": True},
)
async def getleaderschedule(
    chain: str,
    slot: int = None,
    identity: str = None,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if identity:
            options["identity"] = identity
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getleaderschedule(chain.lower(), slot, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmaxretransmitslot",
    description=(
        "Call the getMaxRetransmitSlot JSON-RPC method to get the current max retransmit slot the node has seen.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: Slot number of the max retransmit slot.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getMaxRetransmitSlot"\n'
        "}'"
    ),
    annotations={"title": "getMaxRetransmitSlot", "readOnlyHint": True},
)
async def getmaxretransmitslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getmaxretransmitslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmaxshredinsertslot",
    description=(
        "Call the getMaxShredInsertSlot JSON-RPC method to get the highest slot for shred insertion.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: Slot number of the max shred insert slot.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getMaxShredInsertSlot"\n'
        "}'"
    ),
    annotations={"title": "getMaxShredInsertSlot", "readOnlyHint": True},
)
async def getmaxshredinsertslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getmaxshredinsertslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getminimumbalanceforrentexemption",
    description=(
        "Call the getMinimumBalanceForRentExemption JSON-RPC method to calculate the minimum balance needed for rent exemption.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- data_length (int): Length of the account data in bytes.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: Minimum lamports required for rent exemption.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getMinimumBalanceForRentExemption",\n'
        '  "params": [128, {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getMinimumBalanceForRentExemption", "readOnlyHint": True},
)
async def getminimumbalanceforrentexemption(
    chain: str,
    data_length: int,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(
            await client.getminimumbalanceforrentexemption(
                chain.lower(), data_length, options or None
            )
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmultipleaccounts",
    description=(
        "Call the getMultipleAccounts JSON-RPC method to retrieve account info for a list of public keys.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- pubkeys (List[str]): List of base-58 encoded public keys.\n"
        "- encoding (str, optional): Data encoding. Options:\n"
        "  - 'base58'\n"
        "  - 'base64' (default)\n"
        "  - 'base64+zstd'\n"
        "  - 'jsonParsed'\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n"
        "- data_slice (dict, optional): Object with 'offset' and 'length' keys to specify data range.\n\n"
        "Returns: Account information array for the specified pubkeys.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getMultipleAccounts",\n'
        '  "params": [["Vote111111111111111111111111111111111111111"], {"encoding": "base64"}]\n'
        "}'"
    ),
    annotations={"title": "getMultipleAccounts", "readOnlyHint": True},
)
async def getmultipleaccounts(
    chain: str,
    pubkeys: list,
    commitment: str = "finalized",
    encoding: str = "base64",
    min_context_slot: int = None,
    data_slice: dict = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if encoding:
            options["encoding"] = encoding
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        if data_slice:
            options["dataSlice"] = data_slice
        return _ok(await client.getmultipleaccounts(chain.lower(), pubkeys, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getprogramaccounts",
    description=(
        "Call the getProgramAccounts JSON-RPC method to get all accounts owned by a program.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- program_id (str): Base-58 encoded public key of the program. For graduating bonding curves, use `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P`.\n"
        "- encoding (str, optional): Data encoding. Default is 'base64'.\n"
        "- commitment (str, optional): Commitment level. Default is 'confirmed'.\n"
        "- filters (list, optional): List of filter objects. Each filter can be:\n"
        "  - memcmp filter: {'memcmp': {'offset': int, 'bytes': 'base58_string'}}\n"
        "  - dataSize filter: {'dataSize': int}\n"
        "  Example: [{'memcmp': {'offset': 0, 'bytes': '4y6pru6YvC7'}}]\n"
        "  Use output from get_graduating_bonding_curves() directly.\n"
        "- data_slice (dict, optional): Object with 'offset' and 'length'.\n"
        "- with_context (bool, optional): Whether to include response context.\n\n"
        "Usage:\n"
        "1. filters_list = get_graduating_bonding_curves()  # Returns filter list\n"
        "2. getprogramaccounts('solana', program_id, filters=filters_list)\n\n"
        "Returns: Array of account info owned by the given program."
    ),
    annotations={"title": "getProgramAccounts", "readOnlyHint": True},
)
async def getprogramaccounts(
    chain: str,
    program_id: str,
    commitment: str = "confirmed",
    encoding: str = "base64",
    filters: list = None,
    data_slice: dict = None,
    with_context: bool = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if encoding:
            options["encoding"] = encoding
        if filters:
            options["filters"] = filters
        if data_slice:
            options["dataSlice"] = data_slice
        if with_context is not None:
            options["withContext"] = with_context

        return _ok(await client.getprogramaccounts(chain, program_id, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getrecentperformancesamples",
    description=(
        "Call the getRecentPerformanceSamples JSON-RPC method to fetch recent performance metrics.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- limit (int, optional): Number of samples to return (max 720).\n\n"
        "Returns: A list of performance sample objects (numSlots, numTransactions, etc).\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getRecentPerformanceSamples",\n'
        '  "params": [10]\n'
        "}'"
    ),
    annotations={"title": "getRecentPerformanceSamples", "readOnlyHint": True},
)
async def getrecentperformancesamples(
    chain: str,
    limit: int = None,
) -> CallToolResult:
    try:
        return _ok(await client.getrecentperformancesamples(chain.lower(), limit))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getrecentprioritizationfees",
    description=(
        "Call the getRecentPrioritizationFees JSON-RPC method to get recent prioritization fees for given accounts.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- accounts (List[str]): List of base-58 encoded account addresses.\n\n"
        "Returns: Prioritization fee info for the provided addresses.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getRecentPrioritizationFees",\n'
        '  "params": [["Vote111111111111111111111111111111111111111"]]\n'
        "}'"
    ),
    annotations={"title": "getRecentPrioritizationFees", "readOnlyHint": True},
)
async def getrecentprioritizationfees(
    chain: str,
    accounts: list,
) -> CallToolResult:
    try:
        return _ok(await client.getrecentprioritizationfees(chain.lower(), accounts))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsignaturesforaddress",
    description=(
        "Call the getSignaturesForAddress JSON-RPC method to retrieve confirmed signatures for transactions involving an address.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- address (str): Base-58 encoded address.\n"
        "- limit (int, optional): Maximum number of results to return (max 1,000).\n"
        "- before (str, optional): Start searching backward before this signature.\n"
        "- until (str, optional): Search until this signature is reached.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: A list of transaction signature info objects.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSignaturesForAddress",\n'
        '  "params": ["Vote111111111111111111111111111111111111111", {"limit": 10}]\n'
        "}'"
    ),
    annotations={"title": "getSignaturesForAddress", "readOnlyHint": True},
)
async def getsignaturesforaddress(
    chain: str,
    address: str,
    limit: int = None,
    before: str = None,
    until: str = None,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if limit is not None:
            options["limit"] = limit
        if before:
            options["before"] = before
        if until:
            options["until"] = until
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getsignaturesforaddress(chain.lower(), address, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsignaturestatuses",
    description=(
        "Call the getSignatureStatuses JSON-RPC method to retrieve the status of one or more transaction signatures.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- signatures (List[str]): List of transaction signature strings.\n"
        "- search_transaction_history (bool, optional): If true, search the entire ledger.\n\n"
        "Returns: Status information for the provided signatures.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSignatureStatuses",\n'
        '  "params": [["5Zs...Qp"], {"searchTransactionHistory": true}]\n'
        "}'"
    ),
    annotations={"title": "getSignatureStatuses", "readOnlyHint": True},
)
async def getsignaturestatuses(
    chain: str,
    signatures: list,
    search_transaction_history: bool = False,
) -> CallToolResult:
    try:
        options = {}
        if search_transaction_history is not None:
            options["searchTransactionHistory"] = search_transaction_history
        return _ok(await client.getsignaturestatuses(chain.lower(), signatures, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getslot",
    description=(
        "Call the getSlot JSON-RPC method to return the current slot the node is processing.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: Current slot number.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSlot"\n'
        "}'"
    ),
    annotations={"title": "getSlot", "readOnlyHint": True},
)
async def getslot(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getslot(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getslotleader",
    description=(
        "Call the getSlotLeader JSON-RPC method to get the identity of the current slot leader.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: The base-58 encoded public key of the current slot leader.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSlotLeader"\n'
        "}'"
    ),
    annotations={"title": "getSlotLeader", "readOnlyHint": True},
)
async def getslotleader(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.getslotleader(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getslotleaders",
    description=(
        "Call the getSlotLeaders JSON-RPC method to get the slot leaders for a range of slots.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- start_slot (int): Starting slot number.\n"
        "- limit (int): Number of slot leaders to return.\n\n"
        "Returns: List of validator identity public keys for each slot.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSlotLeaders",\n'
        '  "params": [100000000, 10]\n'
        "}'"
    ),
    annotations={"title": "getSlotLeaders", "readOnlyHint": True},
)
async def getslotleaders(
    chain: str,
    start_slot: int,
    limit: int,
) -> CallToolResult:
    try:
        return _ok(await client.getslotleaders(chain.lower(), start_slot, limit))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getstakeminimumdelegation",
    description=(
        "Call the getStakeMinimumDelegation JSON-RPC method to retrieve the minimum stake amount needed for delegation.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: Minimum number of lamports required for stake delegation.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getStakeMinimumDelegation"\n'
        "}'"
    ),
    annotations={"title": "getStakeMinimumDelegation", "readOnlyHint": True},
)
async def getstakeminimumdelegation(chain: str, commitment: str) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getstakeminimumdelegation(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsupply",
    description=(
        "Call the getSupply JSON-RPC method to return information about the current supply of SOL.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: A JSON object with total, circulating, and non-circulating supply values.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getSupply",\n'
        '  "params": [{"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getSupply", "readOnlyHint": True},
)
async def getsupply(
    chain: str,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.getsupply(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenaccountbalance",
    description=(
        "Call the getTokenAccountBalance JSON-RPC method to return the token balance of a specific SPL Token account.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- account (str): Base-58 encoded token account address.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: Token balance object with amount and decimals.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTokenAccountBalance",\n'
        '  "params": ["AccountAddress", {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getTokenAccountBalance", "readOnlyHint": True},
)
async def gettokenaccountbalance(
    chain: str,
    account: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.gettokenaccountbalance(chain.lower(), account, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenaccountsbydelegate",
    description=(
        "Call the getTokenAccountsByDelegate JSON-RPC method to get SPL Token accounts delegated to a specific address.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- delegate (str): Base-58 encoded public key of the delegate.\n"
        "- mint (str, optional): Filter by mint address. If it's used, then program_id argument must be skipped.\n"
        "- program_id (str, optional): Override default Token program.  If it's used, then mint argument must be skipped.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- encoding (str, optional): Data encoding format. Options:\n"
        "  - 'base58'\n"
        "  - 'base64' (default)\n"
        "  - 'base64+zstd'\n"
        "  - 'jsonParsed'\n"
        "- data_slice (dict, optional): Optional offset/length object for slicing data.\n\n"
        "Returns: List of token accounts matching the delegate and filters.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTokenAccountsByDelegate",\n'
        '  "params": ["DelegateAddress", {"mint": "MintAddress", "encoding": "jsonParsed"}]\n'
        "}'"
    ),
    annotations={"title": "getTokenAccountsByDelegate", "readOnlyHint": True},
)
async def gettokenaccountsbydelegate(
    chain: str,
    delegate: str,
    mint: str = None,
    program_id: str = None,
    commitment: str = "finalized",
    encoding: str = "base64",
    data_slice: dict = None,
) -> CallToolResult:
    try:
        options1 = {}
        if mint:
            options1["mint"] = mint
        elif program_id:
            options1["programId"] = program_id

        options2 = {}
        if commitment:
            options2["commitment"] = commitment
        if encoding:
            options2["encoding"] = encoding
        if data_slice:
            options2["dataSlice"] = data_slice
        return _ok(
            await client.gettokenaccountsbydelegate(
                chain.lower(), delegate, options1, options2 or None
            )
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenaccountsbyowner",
    description=(
        "Call the getTokenAccountsByOwner JSON-RPC method to get all SPL Token accounts owned by a wallet.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- owner (str): Base-58 encoded public key of the owner.\n"
        "- mint (str, optional): Filter by mint address. If it's used, then program_id argument must be skipped.\n"
        "- program_id (str, optional): Override default Token program.  If it's used, then mint argument must be skipped.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- encoding (str, optional): Data encoding format. Options:\n"
        "  - 'base58'\n"
        "  - 'base64' (default)\n"
        "  - 'base64+zstd'\n"
        "  - 'jsonParsed'\n"
        "- data_slice (dict, optional): Optional offset/length object for slicing data.\n\n"
        "Returns: Token accounts associated with the owner and filters.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTokenAccountsByOwner",\n'
        '  "params": ["OwnerAddress", {"mint": "MintAddress", "encoding": "jsonParsed"}]\n'
        "}'"
    ),
    annotations={"title": "getTokenAccountsByOwner", "readOnlyHint": True},
)
async def gettokenaccountsbyowner(
    chain: str,
    owner: str,
    mint: str = None,
    program_id: str = None,
    commitment: str = "finalized",
    encoding: str = "base64",
    data_slice: dict = None,
) -> CallToolResult:
    try:
        options1 = {}
        if mint:
            options1["mint"] = mint
        elif program_id:
            options1["programId"] = program_id

        options2 = {}
        if commitment:
            options2["commitment"] = commitment
        if encoding:
            options2["encoding"] = encoding
        if data_slice:
            options2["dataSlice"] = data_slice
        return _ok(
            await client.gettokenaccountsbyowner(chain.lower(), owner, options1, options2 or None)
        )
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenlargestaccounts",
    description=(
        "Call the getTokenLargestAccounts JSON-RPC method to retrieve the top SPL Token accounts by balance for a given mint.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- mint (str): Base-58 encoded mint address.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "Returns: A list of the 20 largest token accounts and their balances.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTokenLargestAccounts",\n'
        '  "params": ["MintAddress", {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getTokenLargestAccounts", "readOnlyHint": True},
)
async def gettokenlargestaccounts(
    chain: str,
    mint: str,
    commitment: str = "finalized",
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        return _ok(await client.gettokenlargestaccounts(chain.lower(), mint, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokensupply",
    description=(
        "Call the getTokenSupply JSON-RPC method to retrieve the total supply of a specified SPL Token.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- mint (str): Base-58 encoded mint address.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: Supply information including total amount and decimals.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTokenSupply",\n'
        '  "params": ["MintAddress", {"commitment": "finalized"}]\n'
        "}'"
    ),
    annotations={"title": "getTokenSupply", "readOnlyHint": True},
)
async def gettokensupply(
    chain: str,
    mint: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.gettokensupply(chain.lower(), mint, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettransaction",
    description=(
        "Call the getTransaction JSON-RPC method to retrieve transaction details by signature.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- signature (str): Base-58 encoded transaction signature.\n"
        "- encoding (str, optional): Encoding format: 'json', 'jsonParsed', 'base58', 'base64'. Default is base64.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- max_supported_transaction_version (int, optional): Max tx version to return. Currently, the only valid value for this parameter is 0. Setting it to 0 allows you to fetch all transactions, including both Versioned and legacy transactions.\n\n"
        "Returns: Transaction object, optionally parsed.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTransaction",\n'
        '  "params": ["TransactionSignature", {"encoding": "jsonParsed"}]\n'
        "}'"
    ),
    annotations={"title": "getTransaction", "readOnlyHint": True},
)
async def gettransaction(
    chain: str,
    signature: str,
    encoding: str = "base64",
    commitment: str = "confirmed",
    max_supported_transaction_version: int = 0,
) -> CallToolResult:
    try:
        options = {}
        if encoding:
            options["encoding"] = encoding
        if commitment:
            options["commitment"] = commitment
        if max_supported_transaction_version is not None:
            options["maxSupportedTransactionVersion"] = max_supported_transaction_version
        return _ok(await client.gettransaction(chain.lower(), signature, options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettransactioncount",
    description=(
        "Call the getTransactionCount JSON-RPC method to retrieve the current transaction count.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- min_context_slot (int, optional): Minimum context slot.\n\n"
        "Returns: Total number of transactions processed by the node.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getTransactionCount"\n'
        "}'"
    ),
    annotations={"title": "getTransactionCount", "readOnlyHint": True},
)
async def gettransactioncount(
    chain: str,
    commitment: str = "finalized",
    min_context_slot: int = None,
) -> CallToolResult:
    try:
        options = {}
        if commitment:
            options["commitment"] = commitment
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        return _ok(await client.gettransactioncount(chain.lower(), options or None))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getversion",
    description=(
        "Call the getVersion JSON-RPC method to retrieve the current version of the Solana node.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n\n"
        "Returns: Node version object including 'solana-core' and 'feature-set'.\n\n"
        "Example:\n"
        'curl -X POST https://api.mainnet-beta.solana.com -H "Content-Type: application/json" -d \'{\n'
        '  "jsonrpc": "2.0", "id": 1, "method": "getVersion"\n'
        "}'"
    ),
    annotations={"title": "getVersion", "readOnlyHint": True},
)
async def getversion(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getversion(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="simulatetransaction",
    description=(
        "Call the simulateTransaction JSON-RPC method to simulate sending a transaction without broadcasting it.\n\n"
        "Parameters:\n"
        "- chain (str): Must be 'solana'.\n"
        "- transaction (str): Base64 or base58 encoded transaction string. Must contain a valid blockhash.\n"
        "- encoding (str, optional): Encoding used for transaction data. Options:\n"
        "  - 'base64' (default)\n"
        "  - 'base58' (deprecated)\n"
        "- commitment (str, optional): Desired commitment level (processed, confirmed or finalized). Default is finalized.\n"
        "- sig_verify (bool, optional): Whether to verify signatures. Conflicts with replace_recent_blockhash.\n"
        "- replace_recent_blockhash (bool, optional): Whether to replace recent blockhash with latest. Conflicts with sig_verify.\n"
        "- min_context_slot (int, optional): Minimum slot at which the request can be evaluated.\n"
        "- inner_instructions (bool, optional): Whether to include inner instructions in the result.\n"
        "- accounts (dict, optional): Include account addresses and optional encoding. Format: {'addresses': [str], 'encoding': str}.\n\n"
        "Returns: A simulation result object including logs, error (if any), account data, compute units used, and return data.\n\n"
        "Example:\n"
        'curl https://api.devnet.solana.com -s -X POST -H "Content-Type: application/json" -d \'\n'
        "{\n"
        '  "jsonrpc": "2.0",\n'
        '  "id": 1,\n'
        '  "method": "simulateTransaction",\n'
        '  "params": [\n'
        '    "BASE64_ENCODED_TX",\n'
        "    {\n"
        '      "encoding": "base64",\n'
        '      "sigVerify": false,\n'
        '      "replaceRecentBlockhash": true\n'
        "    }\n"
        "  ]\n"
        "}'"
    ),
    annotations={"title": "simulateTransaction", "readOnlyHint": True},
)
async def simulatetransaction(
    chain: str,
    transaction: str,
    encoding: str = "base64",
    commitment: str = "finalized",
    sig_verify: bool = None,
    replace_recent_blockhash: bool = None,
    min_context_slot: int = None,
    inner_instructions: bool = None,
    accounts: dict = None,
) -> CallToolResult:
    try:
        options = {"encoding": encoding}
        if commitment:
            options["commitment"] = commitment
        if sig_verify is not None:
            options["sigVerify"] = sig_verify
        if replace_recent_blockhash is not None:
            options["replaceRecentBlockhash"] = replace_recent_blockhash
        if min_context_slot is not None:
            options["minContextSlot"] = min_context_slot
        if inner_instructions is not None:
            options["innerInstructions"] = inner_instructions
        if accounts:
            options["accounts"] = accounts

        return _ok(await client.simulatetransaction(chain.lower(), transaction, options))
    except Exception as e:
        return _err(str(e))
