"""
Client dispatcher that routes blockchain transaction requests
through registered BlockchainAdapter instances.
"""

from servers.evm.common.adapter_registry import registry


def _adapter(chain: str):
    ad = registry.get(chain)
    if not ad:
        raise ValueError(f"Unsupported blockchain: {chain}")
    return ad


async def web3_clientVersion(chain):
    return await _adapter(chain).web3_clientVersion()


async def web3_sha3(chain, data):
    return await _adapter(chain).web3_sha3(data)


async def net_version(chain):
    return await _adapter(chain).net_version()


async def net_listening(chain):
    return await _adapter(chain).net_listening()


async def net_peerCount(chain):
    return await _adapter(chain).net_peerCount()


async def eth_syncing(chain):
    return await _adapter(chain).eth_syncing()


async def eth_chainId(chain):
    return await _adapter(chain).eth_chainId()


async def eth_blockNumber(chain):
    return await _adapter(chain).eth_blockNumber()


async def eth_gasPrice(chain):
    return await _adapter(chain).eth_gasPrice()


async def eth_feeHistory(chain, block_count, newest_block, reward_percentiles):
    return await _adapter(chain).eth_feeHistory(block_count, newest_block, reward_percentiles)


async def eth_maxPriorityFeePerGas(chain):
    return await _adapter(chain).eth_maxPriorityFeePerGas()


async def eth_getBalance(chain, address, block):
    return await _adapter(chain).eth_getBalance(address, block)


async def eth_getStorageAt(chain, address, position, block):
    return await _adapter(chain).eth_getStorageAt(address, position, block)


async def eth_getTransactionCount(chain, address, block):
    return await _adapter(chain).eth_getTransactionCount(address, block)


async def eth_getCode(chain, address, block):
    return await _adapter(chain).eth_getCode(address, block)


async def eth_call(chain, call_object, block, overrides=None):
    return await _adapter(chain).eth_call(call_object, block, overrides)


async def eth_estimateGas(chain, tx, block, overrides=None):
    return await _adapter(chain).eth_estimateGas(tx, block, overrides)


async def eth_getBlockByHash(chain, block_hash, full_tx):
    return await _adapter(chain).eth_getBlockByHash(block_hash, full_tx)


async def eth_getBlockByNumber(chain, block_number, full_tx):
    return await _adapter(chain).eth_getBlockByNumber(block_number, full_tx)


async def eth_getBlockTransactionCountByHash(chain, block_hash):
    return await _adapter(chain).eth_getBlockTransactionCountByHash(block_hash)


async def eth_getBlockTransactionCountByNumber(chain, block_number):
    return await _adapter(chain).eth_getBlockTransactionCountByNumber(block_number)


async def eth_getTransactionByHash(chain, tx_hash):
    return await _adapter(chain).eth_getTransactionByHash(tx_hash)


async def eth_getTransactionReceipt(chain, tx_hash):
    return await _adapter(chain).eth_getTransactionReceipt(tx_hash)


async def eth_getLogs(chain, filter_params):
    return await _adapter(chain).eth_getLogs(filter_params)


async def debug_traceTransaction(chain, tx_hash, options):
    return await _adapter(chain).debug_traceTransaction(tx_hash, options)


async def debug_traceCall(chain, call_object, block, options):
    return await _adapter(chain).debug_traceCall(call_object, block, options)


async def debug_traceBlock(chain, rlp_encoded_block, options):
    return await _adapter(chain).debug_traceBlock(rlp_encoded_block, options)


async def debug_traceBlockByHash(chain, block_hash, options):
    return await _adapter(chain).debug_traceBlockByHash(block_hash, options)


async def debug_traceBlockByNumber(chain, block_number, options):
    return await _adapter(chain).debug_traceBlockByNumber(block_number, options)


async def trace_call(chain, call_object, trace_types, block):
    return await _adapter(chain).trace_call(call_object, trace_types, block)


async def trace_callMany(chain, calls, block):
    return await _adapter(chain).trace_callMany(calls, block)


async def trace_rawTransaction(chain, raw_tx, trace_types):
    return await _adapter(chain).trace_rawTransaction(raw_tx, trace_types)


async def trace_replayTransaction(chain, tx_hash, trace_types):
    return await _adapter(chain).trace_replayTransaction(tx_hash, trace_types)


async def trace_replayBlockTransactions(chain, block_number, trace_types):
    return await _adapter(chain).trace_replayBlockTransactions(block_number, trace_types)


async def trace_block(chain, block_number):
    return await _adapter(chain).trace_block(block_number)


async def eth_getProof(chain, address, storage_keys, block):
    return await _adapter(chain).eth_getProof(address, storage_keys, block)


async def eth_simulateV1(chain, params, block):
    return await _adapter(chain).eth_simulateV1(params, block)


async def eth_getBlockReceipts(chain, block):
    return await _adapter(chain).eth_getBlockReceipts(block)
