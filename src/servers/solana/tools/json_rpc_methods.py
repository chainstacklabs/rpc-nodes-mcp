"""
Auto-generated MCP tools for JSON-RPC methods.
"""

from mcp.types import CallToolResult

import servers.solana.common.client as client
from common.utils import _err, _ok
from servers.solana.server import mcp


@mcp.tool(
    name="getaccountinfo",
    description="Call the getAccountInfo JSON-RPC method: getAccountInfo\nReturns: Account information\n\nParameters:\n- account: The public key of the account [Example: 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM]\n- options (Options object): Options including: encoding, commitment [Object Example: {encoding=jsonParsed, commitment=finalized}]",
    annotations={"title": "getAccountInfo", "readOnlyHint": True},
)
async def getaccountinfo(chain: str, account: str, options: str) -> CallToolResult:
    try:
        return _ok(await client.getaccountinfo(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getbalance",
    description="Get account balance on Solana. Call the getBalance JSON-RPC method: getBalance\nReturns: Account balance\n\nParameters:\n- param1: The public key of the account [Example: 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM]",
    annotations={"title": "getBalance", "readOnlyHint": True},
)
async def getbalance(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getbalance(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblock",
    description="Call the getBlock JSON-RPC method: getBlock\nReturns: Block details\n\nParameters:\n- param1: The slot of the block [Example: 239462061]\n- encoding",
    annotations={"title": "getBlock", "readOnlyHint": True},
)
async def getblock(chain: str, param1: str, encoding: str) -> CallToolResult:
    try:
        return _ok(await client.getblock(chain.lower(), param1, encoding))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockcommitment",
    description="Call the getBlockCommitment JSON-RPC method: getBlockCommitment\nReturns: Block commitment details\n\nParameters:\n- param1: The slot of the block [Example: 166974442]",
    annotations={"title": "getBlockCommitment", "readOnlyHint": True},
)
async def getblockcommitment(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getblockcommitment(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockheight",
    description="Call the getBlockHeight JSON-RPC method: getBlockHeight\nReturns: Block height",
    annotations={"title": "getBlockHeight", "readOnlyHint": True},
)
async def getblockheight(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getblockheight(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockproduction",
    description="Call the getBlockProduction JSON-RPC method: getBlockProduction\nReturns: Block production details",
    annotations={"title": "getBlockProduction", "readOnlyHint": True},
)
async def getblockproduction(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getblockproduction(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblocks",
    description="Call the getBlocks JSON-RPC method: getBlocks\nReturns: Blocks details\n\nParameters:\n- param1: The start slot of the blocks [Example: 166974442]",
    annotations={"title": "getBlocks", "readOnlyHint": True},
)
async def getblocks(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getblocks(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblockswithlimit",
    description="Call the getBlocksWithLimit JSON-RPC method: getBlocksWithLimit\nReturns: Blocks details\n\nParameters:\n- param1: The start slot of the blocks and the maximum number of blocks [Example: 166974442]",
    annotations={"title": "getBlocksWithLimit", "readOnlyHint": True},
)
async def getblockswithlimit(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getblockswithlimit(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getblocktime",
    description="Call the getBlockTime JSON-RPC method: getBlockTime\nReturns: Block time details\n\nParameters:\n- param1: The slot of the block [Example: 166974442]",
    annotations={"title": "getBlockTime", "readOnlyHint": True},
)
async def getblocktime(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getblocktime(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getclusternodes",
    description="Call the getClusterNodes JSON-RPC method: getClusterNodes\nReturns: Cluster nodes details",
    annotations={"title": "getClusterNodes", "readOnlyHint": True},
)
async def getclusternodes(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getclusternodes(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getepochinfo",
    description="Call the getEpochInfo JSON-RPC method: getEpochInfo\nReturns: Epoch info details",
    annotations={"title": "getEpochInfo", "readOnlyHint": True},
)
async def getepochinfo(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getepochinfo(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getepochschedule",
    description="Call the getEpochSchedule JSON-RPC method: getEpochSchedule\nReturns: Epoch schedule details",
    annotations={"title": "getEpochSchedule", "readOnlyHint": True},
)
async def getepochschedule(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getepochschedule(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getfeeformessage",
    description="Call the getFeeForMessage JSON-RPC method: getFeeForMessage\nReturns: Fee details\n\nParameters:\n- account: The serialized message [Example: AQABA36MCIdgv94d3c8ywX8gm4JC7lKq8TH6zYjQ6ixtCwbyhwEgP0xzGjSa7QhxjYGUHwUPDgYsz9S8Mb/9c7ejFiwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOnEi/spkCilDriqSI6o2AneB2xk65o4Xm9EM+yGyiPAQICAAEMAgAAAADKmjsAAAAA]\n- options (Options object): Options including: commitment [Object Example: {commitment=finalized}]",
    annotations={"title": "getFeeForMessage", "readOnlyHint": True},
)
async def getfeeformessage(chain: str, account: str, options: str) -> CallToolResult:
    try:
        return _ok(await client.getfeeformessage(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getfirstavailableblock",
    description="Call the getFirstAvailableBlock JSON-RPC method: getFirstAvailableBlock\nReturns: First available block details",
    annotations={"title": "getFirstAvailableBlock", "readOnlyHint": True},
)
async def getfirstavailableblock(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getfirstavailableblock(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getgenesishash",
    description="Call the getGenesisHash JSON-RPC method: getGenesisHash\nReturns: Genesis hash details",
    annotations={"title": "getGenesisHash", "readOnlyHint": True},
)
async def getgenesishash(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getgenesishash(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gethighestsnapshotslot",
    description="Call the getHighestSnapshotSlot JSON-RPC method: getHighestSnapshotSlot\nReturns: Highest snapshot slot details",
    annotations={"title": "getHighestSnapshotSlot", "readOnlyHint": True},
)
async def gethighestsnapshotslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.gethighestsnapshotslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getidentity",
    description="Call the getIdentity JSON-RPC method: getIdentity\nReturns: Identity details",
    annotations={"title": "getIdentity", "readOnlyHint": True},
)
async def getidentity(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getidentity(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getinflationgovernor",
    description="Call the getInflationGovernor JSON-RPC method: getInflationGovernor\nReturns: Inflation governor details",
    annotations={"title": "getInflationGovernor", "readOnlyHint": True},
)
async def getinflationgovernor(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getinflationgovernor(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getinflationrate",
    description="Call the getInflationRate JSON-RPC method: getInflationRate\nReturns: Inflation rate details",
    annotations={"title": "getInflationRate", "readOnlyHint": True},
)
async def getinflationrate(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getinflationrate(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getinflationreward",
    description="Call the getInflationReward JSON-RPC method: getInflationReward\nReturns: Inflation reward details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2",
    annotations={"title": "getInflationReward", "readOnlyHint": True},
)
async def getinflationreward(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.getinflationreward(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getlargestaccounts",
    description="Call the getLargestAccounts JSON-RPC method: getLargestAccounts\nReturns: Largest accounts details\n\nParameters:\n- filter [Example: circulating]",
    annotations={"title": "getLargestAccounts", "readOnlyHint": True},
)
async def getlargestaccounts(chain: str, filter: str) -> CallToolResult:
    try:
        return _ok(await client.getlargestaccounts(chain.lower(), filter))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getlatestblockhash",
    description="Call the getLatestBlockhash JSON-RPC method: getLatestBlockhash\nReturns: Latest blockhash details",
    annotations={"title": "getLatestBlockhash", "readOnlyHint": True},
)
async def getlatestblockhash(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getlatestblockhash(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getleaderschedule",
    description="Call the getLeaderSchedule JSON-RPC method: getLeaderSchedule\nReturns: Leader schedule details",
    annotations={"title": "getLeaderSchedule", "readOnlyHint": True},
)
async def getleaderschedule(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getleaderschedule(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmaxretransmitslot",
    description="Call the getMaxRetransmitSlot JSON-RPC method: getMaxRetransmitSlot\nReturns: Max retransmit slot details",
    annotations={"title": "getMaxRetransmitSlot", "readOnlyHint": True},
)
async def getmaxretransmitslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getmaxretransmitslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmaxshredinsertslot",
    description="Call the getMaxShredInsertSlot JSON-RPC method: getMaxShredInsertSlot\nReturns: Max shred insert slot details",
    annotations={"title": "getMaxShredInsertSlot", "readOnlyHint": True},
)
async def getmaxshredinsertslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getmaxshredinsertslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getminimumbalanceforrentexemption",
    description="Call the getMinimumBalanceForRentExemption JSON-RPC method: getMinimumBalanceForRentExemption\nReturns: Minimum balance for rent exemption details\n\nParameters:\n- param1",
    annotations={"title": "getMinimumBalanceForRentExemption", "readOnlyHint": True},
)
async def getminimumbalanceforrentexemption(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getminimumbalanceforrentexemption(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getmultipleaccounts",
    description="Call the getMultipleAccounts JSON-RPC method: getMultipleAccounts\nReturns: Multiple accounts details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2",
    annotations={"title": "getMultipleAccounts", "readOnlyHint": True},
)
async def getmultipleaccounts(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.getmultipleaccounts(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getprogramaccounts",
    description="Call the getProgramAccounts JSON-RPC method: getProgramAccounts\nReturns: Program accounts details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2",
    annotations={"title": "getProgramAccounts", "readOnlyHint": True},
)
async def getprogramaccounts(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.getprogramaccounts(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getrecentblockhash",
    description="Call the getRecentBlockhash JSON-RPC method: getRecentBlockhash\nReturns: Recent blockhash details",
    annotations={"title": "getRecentBlockhash", "readOnlyHint": True},
)
async def getrecentblockhash(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getrecentblockhash(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getrecentperformancesamples",
    description="Call the getRecentPerformanceSamples JSON-RPC method: getRecentPerformanceSamples\nReturns: Recent performance samples details\n\nParameters:\n- param1: Parameter 1",
    annotations={"title": "getRecentPerformanceSamples", "readOnlyHint": True},
)
async def getrecentperformancesamples(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getrecentperformancesamples(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getrecentprioritizationfees",
    description="Call the getRecentPrioritizationFees JSON-RPC method: getRecentPrioritizationFees\nReturns: Recent prioritization fees details\n\nParameters:\n- param1: Parameter 1",
    annotations={"title": "getRecentPrioritizationFees", "readOnlyHint": True},
)
async def getrecentprioritizationfees(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getrecentprioritizationfees(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsignaturesforaddress",
    description="Call the getSignaturesForAddress JSON-RPC method: getSignaturesForAddress\nReturns: Signatures for address details\n\nParameters:\n- param1: Parameter 1",
    annotations={"title": "getSignaturesForAddress", "readOnlyHint": True},
)
async def getsignaturesforaddress(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.getsignaturesforaddress(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsignaturestatuses",
    description="Call the getSignatureStatuses JSON-RPC method: getSignatureStatuses\nReturns: Signature statuses details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2",
    annotations={"title": "getSignatureStatuses", "readOnlyHint": True},
)
async def getsignaturestatuses(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.getsignaturestatuses(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getslot",
    description="Call the getSlot JSON-RPC method: getSlot\nReturns: Slot details",
    annotations={"title": "getSlot", "readOnlyHint": True},
)
async def getslot(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getslot(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getslotleader",
    description="Call the getSlotLeader JSON-RPC method: getSlotLeader\nReturns: Slot leader details",
    annotations={"title": "getSlotLeader", "readOnlyHint": True},
)
async def getslotleader(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getslotleader(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getstakeactivation",
    description="Call the getStakeActivation JSON-RPC method: getStakeActivation\nReturns: Stake activation details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2",
    annotations={"title": "getStakeActivation", "readOnlyHint": True},
)
async def getstakeactivation(chain: str, param1: str, param2: str) -> CallToolResult:
    try:
        return _ok(await client.getstakeactivation(chain.lower(), param1, param2))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getstakeminimumdelegation",
    description="Call the getStakeMinimumDelegation JSON-RPC method: getStakeMinimumDelegation\nReturns: Minimum delegation details",
    annotations={"title": "getStakeMinimumDelegation", "readOnlyHint": True},
)
async def getstakeminimumdelegation(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getstakeminimumdelegation(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="getsupply",
    description="Call the getSupply JSON-RPC method: getSupply\nReturns: Supply details",
    annotations={"title": "getSupply", "readOnlyHint": True},
)
async def getsupply(chain: str) -> CallToolResult:
    try:
        return _ok(await client.getsupply(chain.lower()))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenaccountbalance",
    description="Call the getTokenAccountBalance JSON-RPC method: getTokenAccountBalance\nReturns: Token account balance details\n\nParameters:\n- param1: Parameter 1",
    annotations={"title": "getTokenAccountBalance", "readOnlyHint": True},
)
async def gettokenaccountbalance(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.gettokenaccountbalance(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenaccountsbyowner",
    description="Call the getTokenAccountsByOwner JSON-RPC method: getTokenAccountsByOwner\nReturns: Token accounts by owner details\n\nParameters:\n- param1: Parameter 1\n- param2: Parameter 2\n- param3: Parameter 3",
    annotations={"title": "getTokenAccountsByOwner", "readOnlyHint": True},
)
async def gettokenaccountsbyowner(
    chain: str, param1: str, param2: str, param3: str
) -> CallToolResult:
    try:
        return _ok(await client.gettokenaccountsbyowner(chain.lower(), param1, param2, param3))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettokenlargestaccounts",
    description="Call the getTokenLargestAccounts JSON-RPC method: getTokenLargestAccounts\nReturns: Largest token accounts details\n\nParameters:\n- param1: Parameter 1",
    annotations={"title": "getTokenLargestAccounts", "readOnlyHint": True},
)
async def gettokenlargestaccounts(chain: str, param1: str) -> CallToolResult:
    try:
        return _ok(await client.gettokenlargestaccounts(chain.lower(), param1))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="gettransaction",
    description="Call the getTransaction JSON-RPC method: getTransaction\nReturns: Transaction details\n\nParameters:\n- account: Transaction signature [Example: 4VAGET7z5g7ogVGmbmZ6KBtF6DS8ftLWzD65BXZWQJjwASUqLod7LhGB6mqThcqo97QcC7r7uNmBY8GwsnLAA52n]\n- options (Options object): Options including: encoding, maxSupportedTransactionVersion [Object Example: {encoding=jsonParsed, maxSupportedTransactionVersion=0}]",
    annotations={"title": "getTransaction", "readOnlyHint": True},
)
async def gettransaction(chain: str, account: str, options: str) -> CallToolResult:
    try:
        return _ok(await client.gettransaction(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="isblockhashvalid",
    description="Call the isBlockhashValid JSON-RPC method: isBlockhashValid\nReturns: Blockhash validity status\n\nParameters:\n- account: The blockhash to validate, as a base-58 encoded string [Example: AspJzsEukGPuLYsebpUSSeS79GtYVVh6Bn4478qWXqBK]\n- options (Options object): Options including: commitment [Object Example: {commitment=processed}]",
    annotations={"title": "isBlockhashValid", "readOnlyHint": True},
)
async def isblockhashvalid(chain: str, account: str, options: str) -> CallToolResult:
    try:
        return _ok(await client.isblockhashvalid(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))


@mcp.tool(
    name="simulatetransaction",
    description="Call the simulateTransaction JSON-RPC method: simulateTransaction\nReturns: Simulated transaction details\n\nParameters:\n- account: Transaction, as an encoded string\n- options (Options object): Options including: encoding [Object Example: {encoding=base64}]",
    annotations={"title": "simulateTransaction", "readOnlyHint": True},
)
async def simulatetransaction(chain: str, account: str, options: str) -> CallToolResult:
    try:
        return _ok(await client.simulatetransaction(chain.lower(), account, options))
    except Exception as e:
        return _err(str(e))
