"""
Auto-generated adapter class for solana-compatible blockchain.
"""

from common.interfaces import RpcClient
from common.rpc import HttpxRpcClient
from servers.solana.common.interfaces import BlockchainAdapter


class SolanaAdapter(BlockchainAdapter):
    def __init__(self, rpc_url: str, rpc_client: RpcClient = None):
        self.rpc_url = rpc_url
        self.rpc_client = rpc_client or HttpxRpcClient()

    async def getaccountinfo(self, account, options) -> str:
        return await self.rpc_client.post("getAccountInfo", [account, options], self.rpc_url)

    async def getbalance(self, account, options) -> str:
        return await self.rpc_client.post("getBalance", [account, options], self.rpc_url)

    async def getblock(self, param1, encoding) -> str:
        return await self.rpc_client.post("getBlock", [param1, encoding], self.rpc_url)

    async def getblockcommitment(self, param1) -> str:
        return await self.rpc_client.post("getBlockCommitment", [param1], self.rpc_url)

    async def getblockheight(self) -> str:
        return await self.rpc_client.post("getBlockHeight", [], self.rpc_url)

    async def getblockproduction(self) -> str:
        return await self.rpc_client.post("getBlockProduction", [], self.rpc_url)

    async def getblocks(self, param1) -> str:
        return await self.rpc_client.post("getBlocks", [param1], self.rpc_url)

    async def getblockswithlimit(self, param1) -> str:
        return await self.rpc_client.post("getBlocksWithLimit", [param1], self.rpc_url)

    async def getblocktime(self, param1) -> str:
        return await self.rpc_client.post("getBlockTime", [param1], self.rpc_url)

    async def getclusternodes(self) -> str:
        return await self.rpc_client.post("getClusterNodes", [], self.rpc_url)

    async def getepochinfo(self) -> str:
        return await self.rpc_client.post("getEpochInfo", [], self.rpc_url)

    async def getepochschedule(self) -> str:
        return await self.rpc_client.post("getEpochSchedule", [], self.rpc_url)

    async def getfeeformessage(self, account, options) -> str:
        return await self.rpc_client.post("getFeeForMessage", [account, options], self.rpc_url)

    async def getfirstavailableblock(self) -> str:
        return await self.rpc_client.post("getFirstAvailableBlock", [], self.rpc_url)

    async def getgenesishash(self) -> str:
        return await self.rpc_client.post("getGenesisHash", [], self.rpc_url)

    async def gethealth(self) -> str:
        return await self.rpc_client.post("getHealth", [], self.rpc_url)

    async def gethighestsnapshotslot(self) -> str:
        return await self.rpc_client.post("getHighestSnapshotSlot", [], self.rpc_url)

    async def getidentity(self) -> str:
        return await self.rpc_client.post("getIdentity", [], self.rpc_url)

    async def getinflationgovernor(self) -> str:
        return await self.rpc_client.post("getInflationGovernor", [], self.rpc_url)

    async def getinflationrate(self) -> str:
        return await self.rpc_client.post("getInflationRate", [], self.rpc_url)

    async def getinflationreward(self, param1, param2) -> str:
        return await self.rpc_client.post("getInflationReward", [param1, param2], self.rpc_url)

    async def getlargestaccounts(self, filter) -> str:
        return await self.rpc_client.post("getLargestAccounts", [filter], self.rpc_url)

    async def getlatestblockhash(self) -> str:
        return await self.rpc_client.post("getLatestBlockhash", [], self.rpc_url)

    async def getleaderschedule(self) -> str:
        return await self.rpc_client.post("getLeaderSchedule", [], self.rpc_url)

    async def getmaxretransmitslot(self) -> str:
        return await self.rpc_client.post("getMaxRetransmitSlot", [], self.rpc_url)

    async def getmaxshredinsertslot(self) -> str:
        return await self.rpc_client.post("getMaxShredInsertSlot", [], self.rpc_url)

    async def getminimumbalanceforrentexemption(self, param1) -> str:
        return await self.rpc_client.post(
            "getMinimumBalanceForRentExemption", [param1], self.rpc_url
        )

    async def getmultipleaccounts(self, param1, param2) -> str:
        return await self.rpc_client.post("getMultipleAccounts", [param1, param2], self.rpc_url)

    async def getprogramaccounts(self, param1, param2) -> str:
        return await self.rpc_client.post("getProgramAccounts", [param1, param2], self.rpc_url)

    async def getrecentperformancesamples(self, param1) -> str:
        return await self.rpc_client.post("getRecentPerformanceSamples", [param1], self.rpc_url)

    async def getrecentprioritizationfees(self, param1) -> str:
        return await self.rpc_client.post("getRecentPrioritizationFees", [param1], self.rpc_url)

    async def getsignaturesforaddress(self, param1) -> str:
        return await self.rpc_client.post("getSignaturesForAddress", [param1], self.rpc_url)

    async def getsignaturestatuses(self, param1, param2) -> str:
        return await self.rpc_client.post("getSignatureStatuses", [param1, param2], self.rpc_url)

    async def getslot(self) -> str:
        return await self.rpc_client.post("getSlot", [], self.rpc_url)

    async def getslotleader(self) -> str:
        return await self.rpc_client.post("getSlotLeader", [], self.rpc_url)

    async def getslotleaders(self, start_slot, limit) -> str:
        return await self.rpc_client.post("getSlotLeaders", [start_slot, limit], self.rpc_url)

    async def getstakeminimumdelegation(self) -> str:
        return await self.rpc_client.post("getStakeMinimumDelegation", [], self.rpc_url)

    async def getsupply(self) -> str:
        return await self.rpc_client.post("getSupply", [], self.rpc_url)

    async def gettokenaccountbalance(self, param1) -> str:
        return await self.rpc_client.post("getTokenAccountBalance", [param1], self.rpc_url)

    async def gettokenaccountsbyowner(self, param1, param2, param3) -> str:
        return await self.rpc_client.post(
            "getTokenAccountsByOwner", [param1, param2, param3], self.rpc_url
        )

    async def gettokenaccountsbydelegate(self, param1, param2, param3) -> str:
        return await self.rpc_client.post(
            "getTokenAccountsByDelegate", [param1, param2, param3], self.rpc_url
        )

    async def gettokenlargestaccounts(self, param1) -> str:
        return await self.rpc_client.post("getTokenLargestAccounts", [param1], self.rpc_url)

    async def gettokensupply(self, mint, options) -> str:
        return await self.rpc_client.post("getTokenSupply", [mint, options], self.rpc_url)

    async def gettransaction(self, account, options) -> str:
        return await self.rpc_client.post("getTransaction", [account, options], self.rpc_url)

    async def gettransactioncount(self, options) -> str:
        return await self.rpc_client.post("getTransactionCount", [options], self.rpc_url)

    async def getVersion(self) -> str:
        return await self.rpc_client.post("getVersion", [], self.rpc_url)

    async def simulatetransaction(self, account, options) -> str:
        return await self.rpc_client.post("simulateTransaction", [account, options], self.rpc_url)
