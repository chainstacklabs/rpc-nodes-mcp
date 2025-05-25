import ast

import servers.evm.chains
from servers.evm.tools import json_rpc_methods as tools
from servers.evm.tools import utilities as utilities


async def test_web3_client_version():
    result = await tools.web3_clientVersion(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert len(text) > 0


async def test_web3_sha3():
    data = "0x68656c6c6f20776f726c64"  # "hello world" in hex
    result = await tools.web3_sha3(chain="Ethereum", data=data)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    assert len(text) == 66  # 0x + 64 hex chars


async def test_net_version():
    result = await tools.net_version(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.isdigit()


async def test_net_listening():
    result = await tools.net_listening(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert text in ["True", "False"]


async def test_net_peer_count():
    result = await tools.net_peerCount(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    peer_count = utilities.convert_hex_to_int(text)
    assert peer_count.content[0].text.isdigit()


async def test_eth_syncing():
    result = await tools.eth_syncing(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    # Can be "false" if not syncing, or JSON object if syncing
    assert text == "False" or text.startswith("{")


async def test_eth_chain_id():
    result = await tools.eth_chainId(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    chain_id = utilities.convert_hex_to_int(text)
    assert chain_id.content[0].text.isdigit()
    assert int(chain_id.content[0].text) > 0


async def test_eth_block_number():
    result = await tools.eth_blockNumber(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    block_num = utilities.convert_hex_to_int(text)
    assert block_num.content[0].text.isdigit()
    assert int(block_num.content[0].text) > 0


async def test_eth_gas_price():
    result = await tools.eth_gasPrice(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    gas_price = utilities.convert_hex_to_int(text)
    assert gas_price.content[0].text.isdigit()
    assert int(gas_price.content[0].text) > 0


async def test_eth_max_priority_fee_per_gas():
    result = await tools.eth_maxPriorityFeePerGas(chain="Ethereum")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    priority_fee = utilities.convert_hex_to_int(text)
    assert priority_fee.content[0].text.isdigit()
    assert int(priority_fee.content[0].text) >= 0


async def test_eth_fee_history():
    result = await tools.eth_feeHistory(
        chain="Ethereum",
        block_count="0x5",  # Changed to hex
        newest_block="latest",
        reward_percentiles=[10, 50, 90],  # Changed to integers
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)
    assert "baseFeePerGas" in parsed_result
    assert "gasUsedRatio" in parsed_result
    assert isinstance(parsed_result["baseFeePerGas"], list)
    assert isinstance(parsed_result["gasUsedRatio"], list)


async def test_eth_get_balance():
    result = await tools.eth_getBalance(
        chain="Ethereum", address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", block="latest"
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    balance = utilities.convert_hex_to_int(text)
    assert balance.content[0].text.isdigit()


async def test_eth_get_storage_at():
    result = await tools.eth_getStorageAt(
        chain="Ethereum",
        address="0xA0b86a33E6441c8C92E4c6700f7e9C6b3b1e4D8A",
        position="0x0",
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")


async def test_eth_get_transaction_count():
    result = await tools.eth_getTransactionCount(
        chain="Ethereum", address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", block="latest"
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    nonce = utilities.convert_hex_to_int(text)
    assert nonce.content[0].text.isdigit()


async def test_eth_get_code():
    result = await tools.eth_getCode(
        chain="Ethereum", address="0xA0b86a33E6441c8C92E4c6700f7e9C6b3b1e4D8A", block="latest"
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")


async def test_eth_call():
    result = await tools.eth_call(
        chain="Ethereum",
        to_address="0x6b175474e89094c44da98b954eedeac495271d0f",
        data="0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")


async def test_eth_estimate_gas():
    result = await tools.eth_estimateGas(
        chain="Ethereum",
        to_address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        value="0x9184e72a000",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    gas_estimate = utilities.convert_hex_to_int(text)
    assert gas_estimate.content[0].text.isdigit()
    assert int(gas_estimate.content[0].text) > 0


async def test_eth_call_with_overrides():
    result = await tools.eth_call(
        chain="Ethereum",
        to_address="0x6b175474e89094c44da98b954eedeac495271d0f",
        data="0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        block="latest",
        override_address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        override_balance="0xffffffffffffffff",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")


async def test_eth_estimate_gas_with_overrides():
    result = await tools.eth_estimateGas(
        chain="Ethereum",
        to_address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        value="0x9184e72a000",
        override_address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        override_balance="0xffffffffffffffff",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    gas_estimate = utilities.convert_hex_to_int(text)
    assert gas_estimate.content[0].text.isdigit()


async def test_convert_wei_to_eth():
    wei_amount = "0x1bc16d674ec80000"  # 2 ETH in wei
    result = utilities.convert_wei_to_eth(wei_amount)
    assert result.content[0].text == "2.0"


async def test_format_gas_price_in_gwei():
    gas_price = "0x3b9aca00"  # 1 Gwei in wei
    result = utilities.format_gas_price_in_gwei(gas_price)
    assert result.content[0].text == "1.0"


async def test_eth_get_block_by_number():
    result = await tools.eth_getBlockByNumber(
        chain="ethereum", block_number="latest", full_tx=False
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)
    assert "number" in parsed_result
    assert "hash" in parsed_result
    assert "transactions" in parsed_result


async def test_eth_get_block_by_number_full_tx():
    result = await tools.eth_getBlockByNumber(chain="Ethereum", block_number="latest", full_tx=True)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)
    assert "transactions" in parsed_result
    assert isinstance(parsed_result["transactions"], list)


async def test_eth_get_block_by_hash():
    result = await tools.eth_getBlockByHash(
        chain="Ethereum",
        block_hash="0x4725335feac695de65deb8662235f52692522d4f623a81468cc6479b43dc9782",
        full_tx=False,
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict) or parsed_result is None


async def test_eth_get_block_transaction_count_by_number():
    result = await tools.eth_getBlockTransactionCountByNumber(
        chain="Ethereum", block_number="latest"
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x")
    tx_count = utilities.convert_hex_to_int(text)
    assert tx_count.content[0].text.isdigit()


async def test_eth_get_block_transaction_count_by_hash():
    result = await tools.eth_getBlockTransactionCountByHash(
        chain="Ethereum",
        block_hash="0x4725335feac695de65deb8662235f52692522d4f623a81468cc6479b43dc9782",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert isinstance(text, str)
    assert text.startswith("0x") or text == "null"


async def test_eth_get_transaction_by_hash():
    result = await tools.eth_getTransactionByHash(
        chain="Ethereum",
        tx_hash="0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict) or parsed_result is None


async def test_eth_get_transaction_receipt():
    result = await tools.eth_getTransactionReceipt(
        chain="Ethereum",
        tx_hash="0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict) or parsed_result is None
    if parsed_result:
        assert "blockHash" in parsed_result
        assert "gasUsed" in parsed_result
        assert "status" in parsed_result


async def test_eth_get_logs():
    result = await tools.eth_getLogs(
        chain="Ethereum",
        from_block="0x1420453",
        to_block="0x1420500",
        address="0xA0b86a33E6441c8C92E4c6700f7e9C6b3b1e4D8A",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_eth_get_logs_with_topics():
    result = await tools.eth_getLogs(
        chain="Ethereum",
        from_block="0x1420453",
        to_block="0x1420500",
        topics=["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"],
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_convert_timestamp_to_datetime():
    timestamp = "1716300000"
    result = utilities.convert_timestamp_to_datetime(timestamp)
    assert isinstance(result.content[0].text, str)
    assert "T" in result.content[0].text
    assert "Z" in result.content[0].text


async def test_convert_int_to_hex():
    value = 255
    result = utilities.convert_int_to_hex(value)
    assert result.content[0].text == "0xff"


async def test_debug_trace_transaction():
    result = await tools.debug_traceTransaction(
        chain="Ethereum",
        tx_hash="0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_debug_trace_transaction_with_call_tracer():
    result = await tools.debug_traceTransaction(
        chain="Ethereum",
        tx_hash="0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5",
        tracer="callTracer",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_debug_trace_call():
    result = await tools.debug_traceCall(
        chain="Ethereum",
        to_address="0x6b175474e89094c44da98b954eedeac495271d0f",
        data="0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_debug_trace_call_with_tracer():
    result = await tools.debug_traceCall(
        chain="Ethereum",
        to_address="0x6b175474e89094c44da98b954eedeac495271d0f",
        data="0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        block="latest",
        tracer="callTracer",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_debug_trace_block_by_number():
    result = await tools.debug_traceBlockByNumber(
        chain="Ethereum", block_number="0xE486B7", tracer="callTracer"
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_debug_trace_block_by_hash():
    result = await tools.debug_traceBlockByHash(
        chain="Ethereum",
        block_hash="0x4725335feac695de65deb8662235f52692522d4f623a81468cc6479b43dc9782",
        tracer="callTracer",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_trace_call():
    result = await tools.trace_call(
        chain="Ethereum",
        to_address="0x6b175474e89094c44da98b954eedeac495271d0f",
        data="0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        trace_types=["trace"],
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_trace_call_many():
    calls = [
        {
            "call": {
                "to": "0x6b175474e89094c44da98b954eedeac495271d0f",
                "data": "0x70a08231000000000000000000000000de0b295669a9fd93d5f28d9ec85e40f4cb697bae",
            },
            "trace_types": ["trace"],
        }
    ]
    result = await tools.trace_callMany(chain="Ethereum", calls=calls, block="latest")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_trace_raw_transaction():
    result = await tools.trace_rawTransaction(
        chain="Ethereum",
        raw_tx="0xf86c808504a817c800825208945dd25e4e73b24e1d6a0be0b906c3b44ccdd7ce9e880de0b6b3a764000080820151a0de0b295669a9fd93d5f28d9ec85e40f4cb697bae5dd25e4e73b24e1d6a0be0b90a05dd25e4e73b24e1d6a0be0b906c3b44ccdd7ce9e88de0b6b3a764000080820151",
        trace_types=["trace"],
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_trace_replay_transaction():
    result = await tools.trace_replayTransaction(
        chain="Ethereum",
        tx_hash="0x85d995eba9763907fdf35cd2034144dd9d53ce32cbec21349d4b12823c6860c5",
        trace_types=["trace"],
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)


async def test_trace_replay_block_transactions():
    result = await tools.trace_replayBlockTransactions(
        chain="Ethereum", block_number="0xccb93d", trace_types=["trace"]
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_trace_block():
    result = await tools.trace_block(chain="Ethereum", block_number="0xccb93d")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_get_supported_blockchains():
    result = utilities.get_supported_blockchains()
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    supported_chains = ast.literal_eval(text)
    assert isinstance(supported_chains, list)
    assert "ethereum" in supported_chains


async def test_convert_hex_to_int_small():
    hex_str = "0x10"
    result = utilities.convert_hex_to_int(hex_str)
    assert result.content[0].text == "16"


async def test_convert_hex_to_int_large():
    hex_str = "0x1bc16d674ec80000"
    result = utilities.convert_hex_to_int(hex_str)
    assert result.content[0].text == "2000000000000000000"


async def test_convert_int_to_hex_small():
    value = 16
    result = utilities.convert_int_to_hex(value)
    assert result.content[0].text == "0x10"


async def test_convert_int_to_hex_large():
    value = 1000000000
    result = utilities.convert_int_to_hex(value)
    assert result.content[0].text == "0x3b9aca00"


async def test_convert_wei_to_eth_zero():
    wei_amount = "0x0"
    result = utilities.convert_wei_to_eth(wei_amount)
    assert result.content[0].text == "0.0"


async def test_convert_wei_to_eth_one():
    wei_amount = "0xde0b6b3a7640000"  # 1 ETH
    result = utilities.convert_wei_to_eth(wei_amount)
    assert result.content[0].text == "1.0"


async def test_convert_wei_to_eth_fraction():
    wei_amount = "0x6f05b59d3b20000"  # 0.5 ETH
    result = utilities.convert_wei_to_eth(wei_amount)
    assert result.content[0].text == "0.5"


async def test_format_gas_price_in_gwei_low():
    gas_price = "0x1"  # 1 wei
    result = utilities.format_gas_price_in_gwei(gas_price)
    assert result.content[0].text == "1e-09"


async def test_format_gas_price_in_gwei_standard():
    gas_price = "0x77359400"  # 2 Gwei
    result = utilities.format_gas_price_in_gwei(gas_price)
    assert result.content[0].text == "2.0"


async def test_format_gas_price_in_gwei_high():
    gas_price = "0x2540be400"  # 10 Gwei
    result = utilities.format_gas_price_in_gwei(gas_price)
    assert result.content[0].text == "10.0"


async def test_convert_timestamp_to_datetime_unix():
    timestamp = "1640995200"  # 2022-01-01 00:00:00 UTC
    result = utilities.convert_timestamp_to_datetime(timestamp)
    assert "2022-01-01T00:00:00Z" in result.content[0].text


async def test_convert_timestamp_to_datetime_hex():
    timestamp = "0x660b6c80"
    result = utilities.convert_timestamp_to_datetime(timestamp)
    assert isinstance(result.content[0].text, str)
    assert "T" in result.content[0].text
    assert "Z" in result.content[0].text


async def test_web3_sha3_empty():
    data = "0x"
    result = await tools.web3_sha3(chain="Ethereum", data=data)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert text.startswith("0x")
    assert len(text) == 66


async def test_eth_call_balance_of():
    result = await tools.eth_call(
        chain="Ethereum",
        to_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",  # USDT
        data="0x70a08231000000000000000000000000f977814e90da44bfa03b6295a0616a897441acec",  # Balance of large holder
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert text.startswith("0x")


async def test_eth_estimate_gas_transfer():
    result = await tools.eth_estimateGas(
        chain="Ethereum",
        from_address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        to_address="0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13",
        value="0xde0b6b3a7640000",  # 1 ETH
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    assert text.startswith("0x")
    gas_estimate = utilities.convert_hex_to_int(text)
    assert int(gas_estimate.content[0].text) == 21000  # Standard ETH transfer gas


async def test_eth_get_logs_erc20_transfer():
    result = await tools.eth_getLogs(
        chain="Ethereum",
        from_block="latest",
        to_block="latest",
        topics=[
            "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
        ],  # Transfer event
        address="0xA0b86a33E6441c8C92E4c6700f7e9C6b3b1e4D8A",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)


async def test_eth_get_proof():
    result = await tools.eth_getProof(
        chain="Ethereum",
        address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
        storage_keys=["0x0000000000000000000000000000000000000000000000000000000000000000"],
        block="latest",
    )
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, dict)
    assert "accountProof" in parsed_result
    assert "balance" in parsed_result
    assert "codeHash" in parsed_result
    assert "nonce" in parsed_result
    assert "storageHash" in parsed_result
    assert "storageProof" in parsed_result


async def test_eth_simulate_v1():
    params = {
        "blockStateCalls": [
            {
                "calls": [
                    {
                        "from": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
                        "to": "0xae2Fc483527B8EF99EB5D9B44875F005ba1FaE13",
                        "value": "0x1",
                        "gas": "0x5208",  # Added gas limit
                        "gasPrice": "0x3b9aca00",  # Added gas price (1 gwei)
                    }
                ]
            }
        ]
    }
    result = await tools.eth_simulateV1(chain="Ethereum", block_state_calls=params, block="latest")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, (dict, list))


async def test_eth_get_block_receipts():
    result = await tools.eth_getBlockReceipts(chain="Ethereum", block="latest")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed_result = ast.literal_eval(text)
    assert isinstance(parsed_result, list)
    for receipt in parsed_result:
        assert isinstance(receipt, dict)
        assert "blockHash" in receipt
        assert "gasUsed" in receipt
        assert "status" in receipt
        assert "transactionHash" in receipt
