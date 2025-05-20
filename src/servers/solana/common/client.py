"""
Client dispatcher that routes blockchain transaction requests
through registered BlockchainAdapter instances.
"""

from servers.solana.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad


async def getaccountinfo(chain, account, options):
    return await _adapter(chain).getaccountinfo(account, options)


async def getbalance(chain, param1):
    return await _adapter(chain).getbalance(param1)


async def getblock(chain, param1, encoding):
    return await _adapter(chain).getblock(param1, encoding)


async def getblockcommitment(chain, param1):
    return await _adapter(chain).getblockcommitment(param1)


async def getblockheight(chain):
    return await _adapter(chain).getblockheight()


async def getblockproduction(chain):
    return await _adapter(chain).getblockproduction()


async def getblocks(chain, param1):
    return await _adapter(chain).getblocks(param1)


async def getblockswithlimit(chain, param1):
    return await _adapter(chain).getblockswithlimit(param1)


async def getblocktime(chain, param1):
    return await _adapter(chain).getblocktime(param1)


async def getclusternodes(chain):
    return await _adapter(chain).getclusternodes()


async def getepochinfo(chain):
    return await _adapter(chain).getepochinfo()


async def getepochschedule(chain):
    return await _adapter(chain).getepochschedule()


async def getfeeformessage(chain, account, options):
    return await _adapter(chain).getfeeformessage(account, options)


async def getfirstavailableblock(chain):
    return await _adapter(chain).getfirstavailableblock()


async def getgenesishash(chain):
    return await _adapter(chain).getgenesishash()


async def gethighestsnapshotslot(chain):
    return await _adapter(chain).gethighestsnapshotslot()


async def getidentity(chain):
    return await _adapter(chain).getidentity()


async def getinflationgovernor(chain):
    return await _adapter(chain).getinflationgovernor()


async def getinflationrate(chain):
    return await _adapter(chain).getinflationrate()


async def getinflationreward(chain, param1, param2):
    return await _adapter(chain).getinflationreward(param1, param2)


async def getlargestaccounts(chain, filter):
    return await _adapter(chain).getlargestaccounts(filter)


async def getlatestblockhash(chain):
    return await _adapter(chain).getlatestblockhash()


async def getleaderschedule(chain):
    return await _adapter(chain).getleaderschedule()


async def getmaxretransmitslot(chain):
    return await _adapter(chain).getmaxretransmitslot()


async def getmaxshredinsertslot(chain):
    return await _adapter(chain).getmaxshredinsertslot()


async def getminimumbalanceforrentexemption(chain, param1):
    return await _adapter(chain).getminimumbalanceforrentexemption(param1)


async def getmultipleaccounts(chain, param1, param2):
    return await _adapter(chain).getmultipleaccounts(param1, param2)


async def getprogramaccounts(chain, param1, param2):
    return await _adapter(chain).getprogramaccounts(param1, param2)


async def getrecentblockhash(chain):
    return await _adapter(chain).getrecentblockhash()


async def getrecentperformancesamples(chain, param1):
    return await _adapter(chain).getrecentperformancesamples(param1)


async def getrecentprioritizationfees(chain, param1):
    return await _adapter(chain).getrecentprioritizationfees(param1)


async def getsignaturesforaddress(chain, param1):
    return await _adapter(chain).getsignaturesforaddress(param1)


async def getsignaturestatuses(chain, param1, param2):
    return await _adapter(chain).getsignaturestatuses(param1, param2)


async def getslot(chain):
    return await _adapter(chain).getslot()


async def getslotleader(chain):
    return await _adapter(chain).getslotleader()


async def getstakeactivation(chain, param1, param2):
    return await _adapter(chain).getstakeactivation(param1, param2)


async def getstakeminimumdelegation(chain):
    return await _adapter(chain).getstakeminimumdelegation()


async def getsupply(chain):
    return await _adapter(chain).getsupply()


async def gettokenaccountbalance(chain, param1):
    return await _adapter(chain).gettokenaccountbalance(param1)


async def gettokenaccountsbyowner(chain, param1, param2, param3):
    return await _adapter(chain).gettokenaccountsbyowner(param1, param2, param3)


async def gettokenlargestaccounts(chain, param1):
    return await _adapter(chain).gettokenlargestaccounts(param1)


async def gettransaction(chain, account, options):
    return await _adapter(chain).gettransaction(account, options)


async def isblockhashvalid(chain, account, options):
    return await _adapter(chain).isblockhashvalid(account, options)


async def simulatetransaction(chain, account, options):
    return await _adapter(chain).simulatetransaction(account, options)
