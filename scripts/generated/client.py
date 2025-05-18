"""
Auto-generated client router methods for MCP.
"""

from servers.ethereum.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad

async def eth_getbalance(chain, param1, param2):
    return await _adapter(chain).eth_getbalance(param1, param2)

async def eth_getcode(chain, param1, param2):
    return await _adapter(chain).eth_getcode(param1, param2)

async def eth_getproof(chain, param1, param2):
    return await _adapter(chain).eth_getproof(param1, param2)

async def eth_getstorageat(chain, param1, param2, param3):
    return await _adapter(chain).eth_getstorageat(param1, param2, param3)

async def eth_gettransactioncount(chain, param1, param2):
    return await _adapter(chain).eth_gettransactioncount(param1, param2)

async def eth_blocknumber(chain):
    return await _adapter(chain).eth_blocknumber()

async def eth_getblockbynumber(chain, param1, param2):
    return await _adapter(chain).eth_getblockbynumber(param1, param2)

async def eth_getblocktransactioncountbyhash(chain, param1):
    return await _adapter(chain).eth_getblocktransactioncountbyhash(param1)

async def eth_getblocktransactioncountbynumber(chain, param1):
    return await _adapter(chain).eth_getblocktransactioncountbynumber(param1)

async def eth_newblockfilter(chain):
    return await _adapter(chain).eth_newblockfilter()

async def eth_chainid(chain):
    return await _adapter(chain).eth_chainid()

async def eth_syncing(chain):
    return await _adapter(chain).eth_syncing()

async def net_listening(chain):
    return await _adapter(chain).net_listening()

async def net_peercount(chain):
    return await _adapter(chain).net_peercount()

async def web3_clientversion(chain):
    return await _adapter(chain).web3_clientversion()

async def debug_tracetransaction(chain, param1, param2):
    return await _adapter(chain).debug_tracetransaction(param1, param2)

async def debug_traceblockbyhash(chain, param1, param2):
    return await _adapter(chain).debug_traceblockbyhash(param1, param2)

async def debug_traceblockbynumber(chain, param1, param2):
    return await _adapter(chain).debug_traceblockbynumber(param1, param2)

async def debug_tracecall(chain, param1, param2, param3):
    return await _adapter(chain).debug_tracecall(param1, param2, param3)

async def debug_tracetransaction(chain, param1, param2):
    return await _adapter(chain).debug_tracetransaction(param1, param2)

async def trace_block(chain, param1):
    return await _adapter(chain).trace_block(param1)

async def trace_transaction(chain, param1):
    return await _adapter(chain).trace_transaction(param1)

async def eth_call(chain, to_, data):
    return await _adapter(chain).eth_call(to_, data)

async def eth_sendrawtransaction(chain, param1):
    return await _adapter(chain).eth_sendrawtransaction(param1)

async def eth_simulatev1(chain, param1, param2):
    return await _adapter(chain).eth_simulatev1(param1, param2)

async def eth_getfilterchanges(chain, param1):
    return await _adapter(chain).eth_getfilterchanges(param1)

async def eth_uninstallfilter(chain, param1):
    return await _adapter(chain).eth_uninstallfilter(param1)

async def eth_estimategas(chain, from_, to_):
    return await _adapter(chain).eth_estimategas(from_, to_)

async def eth_gasprice(chain):
    return await _adapter(chain).eth_gasprice()

async def eth_maxpriorityfeepergas(chain):
    return await _adapter(chain).eth_maxpriorityfeepergas()

async def eth_getlogs(chain, fromBlock, address, topics):
    return await _adapter(chain).eth_getlogs(fromBlock, address, topics)

async def eth_newfilter(chain, fromBlock, address, topics):
    return await _adapter(chain).eth_newfilter(fromBlock, address, topics)

async def eth_getblockreceipts(chain, param1):
    return await _adapter(chain).eth_getblockreceipts(param1)

async def eth_gettransactionbyblockhashandindex(chain, param1, param2):
    return await _adapter(chain).eth_gettransactionbyblockhashandindex(param1, param2)

async def eth_gettransactionbyblocknumberandindex(chain, param1, param2):
    return await _adapter(chain).eth_gettransactionbyblocknumberandindex(param1, param2)

async def eth_gettransactionbyhash(chain, param1):
    return await _adapter(chain).eth_gettransactionbyhash(param1)

async def eth_gettransactionreceipt(chain, param1):
    return await _adapter(chain).eth_gettransactionreceipt(param1)

async def eth_newpendingtransactionfilter(chain):
    return await _adapter(chain).eth_newpendingtransactionfilter()

