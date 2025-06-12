"""
Client dispatcher that routes blockchain transaction requests
through registered BlockchainAdapter instances.
"""

from src.servers.solana.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad


async def getaccountinfo(chain, account, options):
    return await _adapter(chain).getaccountinfo(account, options)


async def getbalance(chain, account, options):
    return await _adapter(chain).getbalance(account, options)


async def getblock(chain, slot_number, options):
    return await _adapter(chain).getblock(slot_number, options)


async def getblockcommitment(chain, slot_number):
    return await _adapter(chain).getblockcommitment(slot_number)


async def getblockheight(chain, options):
    return await _adapter(chain).getblockheight(options)


async def getblockproduction(chain, options):
    return await _adapter(chain).getblockproduction(options)


async def getblocks(chain, start_slot, end_slot, options):
    return await _adapter(chain).getblocks(start_slot, end_slot, options)


async def getblockswithlimit(chain, start_slot, end_slot, options):
    return await _adapter(chain).getblockswithlimit(start_slot, end_slot, options)


async def getblocktime(chain, slot_number):
    return await _adapter(chain).getblocktime(slot_number)


async def getclusternodes(chain):
    return await _adapter(chain).getclusternodes()


async def getepochinfo(chain, options):
    return await _adapter(chain).getepochinfo(options)


async def getepochschedule(chain):
    return await _adapter(chain).getepochschedule()


async def getfeeformessage(chain, account, options):
    return await _adapter(chain).getfeeformessage(account, options)


async def getfirstavailableblock(chain):
    return await _adapter(chain).getfirstavailableblock()


async def getgenesishash(chain):
    return await _adapter(chain).getgenesishash()


async def gethealth(chain):
    return await _adapter(chain).gethealth()


async def gethighestsnapshotslot(chain):
    return await _adapter(chain).gethighestsnapshotslot()


async def getidentity(chain):
    return await _adapter(chain).getidentity()


async def getinflationgovernor(chain, options):
    return await _adapter(chain).getinflationgovernor(options)


async def getinflationrate(chain):
    return await _adapter(chain).getinflationrate()


async def getinflationreward(chain, addresses, options):
    return await _adapter(chain).getinflationreward(addresses, options)


async def getlargestaccounts(chain, filter):
    return await _adapter(chain).getlargestaccounts(filter)


async def getlatestblockhash(chain, options):
    return await _adapter(chain).getlatestblockhash(options)


async def getleaderschedule(chain, slot_number, options):
    return await _adapter(chain).getleaderschedule(slot_number, options)


async def getmaxretransmitslot(chain):
    return await _adapter(chain).getmaxretransmitslot()


async def getmaxshredinsertslot(chain):
    return await _adapter(chain).getmaxshredinsertslot()


async def getminimumbalanceforrentexemption(chain, account_data_length, options):
    return await _adapter(chain).getminimumbalanceforrentexemption(account_data_length, options)


async def getmultipleaccounts(chain, pubkeys, options):
    return await _adapter(chain).getmultipleaccounts(pubkeys, options)


async def getprogramaccounts(chain, pubkey, options):
    return await _adapter(chain).getprogramaccounts(pubkey, options)


async def getrecentperformancesamples(chain, samples_number):
    return await _adapter(chain).getrecentperformancesamples(samples_number)


async def getrecentprioritizationfees(chain, addresses):
    return await _adapter(chain).getrecentprioritizationfees(addresses)


async def getsignaturesforaddress(chain, account, options):
    return await _adapter(chain).getsignaturesforaddress(account, options)


async def getsignaturestatuses(chain, signatures, options):
    return await _adapter(chain).getsignaturestatuses(signatures, options)


async def getslot(chain, options):
    return await _adapter(chain).getslot(options)


async def getslotleader(chain, options):
    return await _adapter(chain).getslotleader(options)


async def getslotleaders(chain, start_slot, limit):
    return await _adapter(chain).getslotleaders(start_slot, limit)


async def getstakeminimumdelegation(chain, options):
    return await _adapter(chain).getstakeminimumdelegation(options)


async def getsupply(chain, options):
    return await _adapter(chain).getsupply(options)


async def gettokenaccountbalance(chain, account, options):
    return await _adapter(chain).gettokenaccountbalance(account, options)


async def gettokenaccountsbyowner(chain, param1, param2, param3):
    return await _adapter(chain).gettokenaccountsbyowner(param1, param2, param3)


async def gettokenaccountsbydelegate(chain, param1, param2, param3):
    return await _adapter(chain).gettokenaccountsbydelegate(param1, param2, param3)


async def gettokenlargestaccounts(chain, mint, options):
    return await _adapter(chain).gettokenlargestaccounts(mint, options)


async def gettokensupply(chain, mint, options):
    return await _adapter(chain).gettokensupply(mint, options)


async def gettransaction(chain, account, options):
    return await _adapter(chain).gettransaction(account, options)


async def gettransactioncount(chain, options):
    return await _adapter(chain).gettransactioncount(options)


async def getversion(chain):
    return await _adapter(chain).getversion()


async def simulatetransaction(chain, account, options):
    return await _adapter(chain).simulatetransaction(account, options)
