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

    async def getblock(self, slot_number, options) -> str:
        return await self.rpc_client.post("getBlock", [slot_number, options], self.rpc_url)

    async def getblockcommitment(self, slot_number) -> str:
        return await self.rpc_client.post("getBlockCommitment", [slot_number], self.rpc_url)

    async def getblockheight(self, options) -> str:
        return await self.rpc_client.post("getBlockHeight", [options], self.rpc_url)

    async def getblockproduction(self, options) -> str:
        return await self.rpc_client.post("getBlockProduction", [options], self.rpc_url)

    async def getblocks(self, start_slot, end_slot, options) -> str:
        return await self.rpc_client.post(
            "getBlocks", [start_slot, end_slot, options], self.rpc_url
        )

    async def getblockswithlimit(self, start_slot, end_slot, options) -> str:
        return await self.rpc_client.post(
            "getBlocksWithLimit", [start_slot, end_slot, options], self.rpc_url
        )

    async def getblocktime(self, slot_number) -> str:
        return await self.rpc_client.post("getBlockTime", [slot_number], self.rpc_url)

    async def getclusternodes(self) -> str:
        return await self.rpc_client.post("getClusterNodes", [], self.rpc_url)

    async def getepochinfo(self, options) -> str:
        return await self.rpc_client.post("getEpochInfo", [options], self.rpc_url)

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

    async def getinflationgovernor(self, options) -> str:
        return await self.rpc_client.post("getInflationGovernor", [options], self.rpc_url)

    async def getinflationrate(self) -> str:
        return await self.rpc_client.post("getInflationRate", [], self.rpc_url)

    async def getinflationreward(self, addresses, options) -> str:
        return await self.rpc_client.post("getInflationReward", [addresses, options], self.rpc_url)

    async def getlargestaccounts(self, filter) -> str:
        return await self.rpc_client.post("getLargestAccounts", [filter], self.rpc_url)

    async def getlatestblockhash(self, options) -> str:
        return await self.rpc_client.post("getLatestBlockhash", [options], self.rpc_url)

    async def getleaderschedule(self, slot_number, options) -> str:
        return await self.rpc_client.post("getLeaderSchedule", [slot_number, options], self.rpc_url)

    async def getmaxretransmitslot(self) -> str:
        return await self.rpc_client.post("getMaxRetransmitSlot", [], self.rpc_url)

    async def getmaxshredinsertslot(self) -> str:
        return await self.rpc_client.post("getMaxShredInsertSlot", [], self.rpc_url)

    async def getminimumbalanceforrentexemption(self, account_data_length, options) -> str:
        return await self.rpc_client.post(
            "getMinimumBalanceForRentExemption", [account_data_length, options], self.rpc_url
        )

    async def getmultipleaccounts(self, pubkeys, options) -> str:
        return await self.rpc_client.post("getMultipleAccounts", [pubkeys, options], self.rpc_url)

    async def getprogramaccounts(self, pubkey, options) -> str:
        return await self.rpc_client.post("getProgramAccounts", [pubkey, options], self.rpc_url)

    async def getrecentperformancesamples(self, samples_number) -> str:
        return await self.rpc_client.post(
            "getRecentPerformanceSamples", [samples_number], self.rpc_url
        )

    async def getrecentprioritizationfees(self, addresses) -> str:
        return await self.rpc_client.post("getRecentPrioritizationFees", [addresses], self.rpc_url)

    async def getsignaturesforaddress(self, account, options) -> str:
        return await self.rpc_client.post(
            "getSignaturesForAddress", [account, options], self.rpc_url
        )

    async def getsignaturestatuses(self, signatures, options) -> str:
        return await self.rpc_client.post(
            "getSignatureStatuses", [signatures, options], self.rpc_url
        )

    async def getslot(self, options) -> str:
        return await self.rpc_client.post("getSlot", [options], self.rpc_url)

    async def getslotleader(self, options) -> str:
        return await self.rpc_client.post("getSlotLeader", [options], self.rpc_url)

    async def getslotleaders(self, start_slot, limit) -> str:
        return await self.rpc_client.post("getSlotLeaders", [start_slot, limit], self.rpc_url)

    async def getstakeminimumdelegation(self, options) -> str:
        return await self.rpc_client.post("getStakeMinimumDelegation", [options], self.rpc_url)

    async def getsupply(self, options) -> str:
        return await self.rpc_client.post("getSupply", [options], self.rpc_url)

    async def gettokenaccountbalance(self, account, options) -> str:
        return await self.rpc_client.post(
            "getTokenAccountBalance", [account, options], self.rpc_url
        )

    async def gettokenaccountsbyowner(self, param1, param2, param3) -> str:
        return await self.rpc_client.post(
            "getTokenAccountsByOwner", [param1, param2, param3], self.rpc_url
        )

    async def gettokenaccountsbydelegate(self, param1, param2, param3) -> str:
        return await self.rpc_client.post(
            "getTokenAccountsByDelegate", [param1, param2, param3], self.rpc_url
        )

    async def gettokenlargestaccounts(self, mint, options) -> str:
        return await self.rpc_client.post("getTokenLargestAccounts", [mint, options], self.rpc_url)

    async def gettokensupply(self, mint, options) -> str:
        return await self.rpc_client.post("getTokenSupply", [mint, options], self.rpc_url)

    async def gettransaction(self, account, options) -> str:
        return await self.rpc_client.post("getTransaction", [account, options], self.rpc_url)

    async def gettransactioncount(self, options) -> str:
        return await self.rpc_client.post("getTransactionCount", [options], self.rpc_url)

    async def getversion(self) -> str:
        return await self.rpc_client.post("getVersion", [], self.rpc_url)

    async def simulatetransaction(self, account, options) -> str:
        return await self.rpc_client.post("simulateTransaction", [account, options], self.rpc_url)
