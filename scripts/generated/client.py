"""
Auto-generated client router methods for MCP.
"""

from servers.ethereum.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad

async def eth_getbalance(chain, param0, param1):
    return await _adapter(chain).eth_getbalance(param0, param1)

async def eth_getcode(chain, param0, param1):
    return await _adapter(chain).eth_getcode(param0, param1)

async def eth_getproof(chain, param0, param1, param2):
    return await _adapter(chain).eth_getproof(param0, param1, param2)

async def eth_getstorageat(chain, param0, param1, param2):
    return await _adapter(chain).eth_getstorageat(param0, param1, param2)

async def eth_gettransactioncount(chain, param0, param1):
    return await _adapter(chain).eth_gettransactioncount(param0, param1)

async def eth_blocknumber(chain):
    return await _adapter(chain).eth_blocknumber()

async def eth_getblockbynumber(chain, param0, param1):
    return await _adapter(chain).eth_getblockbynumber(param0, param1)

async def eth_getblocktransactioncountbyhash(chain, param0):
    return await _adapter(chain).eth_getblocktransactioncountbyhash(param0)

async def eth_getblocktransactioncountbynumber(chain, param0):
    return await _adapter(chain).eth_getblocktransactioncountbynumber(param0)

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

async def debug_tracetransaction(chain, param0, param1):
    return await _adapter(chain).debug_tracetransaction(param0, param1)

async def debug_traceblockbyhash(chain, param0, param1):
    return await _adapter(chain).debug_traceblockbyhash(param0, param1)

async def debug_traceblockbynumber(chain, param0, param1):
    return await _adapter(chain).debug_traceblockbynumber(param0, param1)

async def debug_tracecall(chain, param0, param1, param2):
    return await _adapter(chain).debug_tracecall(param0, param1, param2)

async def debug_tracetransaction(chain, param0, param1):
    return await _adapter(chain).debug_tracetransaction(param0, param1)

async def trace_block(chain, param0):
    return await _adapter(chain).trace_block(param0)

async def trace_transaction(chain, param0):
    return await _adapter(chain).trace_transaction(param0)

async def eth_call(chain, param0, param1):
    return await _adapter(chain).eth_call(param0, param1)

async def eth_sendrawtransaction(chain, param0):
    return await _adapter(chain).eth_sendrawtransaction(param0)

async def eth_simulatev1(chain, param0, param1):
    return await _adapter(chain).eth_simulatev1(param0, param1)

async def eth_getfilterchanges(chain, param0):
    return await _adapter(chain).eth_getfilterchanges(param0)

async def eth_uninstallfilter(chain, param0):
    return await _adapter(chain).eth_uninstallfilter(param0)

async def eth_estimategas(chain, param0, param1):
    return await _adapter(chain).eth_estimategas(param0, param1)

async def eth_gasprice(chain):
    return await _adapter(chain).eth_gasprice()

async def eth_maxpriorityfeepergas(chain):
    return await _adapter(chain).eth_maxpriorityfeepergas()

async def eth_getlogs(chain, param0):
    return await _adapter(chain).eth_getlogs(param0)

async def eth_newfilter(chain, param0):
    return await _adapter(chain).eth_newfilter(param0)

async def eth_getblockreceipts(chain, param0):
    return await _adapter(chain).eth_getblockreceipts(param0)

async def eth_gettransactionbyblockhashandindex(chain, param0, param1):
    return await _adapter(chain).eth_gettransactionbyblockhashandindex(param0, param1)

async def eth_gettransactionbyblocknumberandindex(chain, param0, param1):
    return await _adapter(chain).eth_gettransactionbyblocknumberandindex(param0, param1)

async def eth_gettransactionbyhash(chain, param0):
    return await _adapter(chain).eth_gettransactionbyhash(param0)

async def eth_gettransactionreceipt(chain, param0):
    return await _adapter(chain).eth_gettransactionreceipt(param0)

async def eth_newpendingtransactionfilter(chain):
    return await _adapter(chain).eth_newpendingtransactionfilter()

