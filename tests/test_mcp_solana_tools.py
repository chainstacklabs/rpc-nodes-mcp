import ast

import servers.solana.chains
from servers.solana.tools import json_rpc_methods as tools


async def test_getaccountinfo_live():
    account = "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"
    result = await tools.getaccountinfo("solana", account)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getbalance_live():
    account = "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"
    result = await tools.getbalance("solana", account)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblock_live():
    slot = 341767387
    result = await tools.getblock("solana", slot)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblockcommitment_live():
    slot = 341767387
    result = await tools.getblockcommitment("solana", slot)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblockheight_live():
    result = await tools.getblockheight("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getblockproduction_live():
    result = await tools.getblockproduction("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblocks_live():
    start_slot = 341767387
    end_slot = 341767390
    result = await tools.getblocks("solana", start_slot, end_slot)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblockswithlimit_live():
    start_slot = 341767387
    limit = 2
    result = await tools.getblockswithlimit("solana", start_slot, limit)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getblocktime_live():
    slot = 341767387
    result = await tools.getblocktime("solana", slot)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getclusternodes_live():
    result = await tools.getclusternodes("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getepochinfo_live():
    result = await tools.getepochinfo("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getepochschedule_live():
    result = await tools.getepochschedule("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getfeeformessage_live():
    message = "AQABA36MCIdgv94d3c8ywX8gm4JC7lKq8TH6zYjQ6ixtCwbyhwEgP0xzGjSa7QhxjYGUHwUPDgYsz9S8Mb/9c7ejFiwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOnEi/spkCilDriqSI6o2AneB2xk65o4Xm9EM+yGyiPAQICAAEMAgAAAADKmjsAAAAA"
    result = await tools.getfeeformessage("solana", message)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getfirstavailableblock_live():
    result = await tools.getfirstavailableblock("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getgenesishash_live():
    result = await tools.getgenesishash("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1


async def test_gethealth_live():
    result = await tools.gethealth("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    assert result.content[0].text == "ok"


async def test_gethighestsnapshotslot_live():
    result = await tools.gethighestsnapshotslot("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getidentity_live():
    result = await tools.getidentity("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getinflationgovernor_live():
    result = await tools.getinflationgovernor("solana", "confirmed")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getinflationrate_live():
    result = await tools.getinflationrate("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getinflationreward_live():
    addresses = ["6D2jqw9hyVCpppZexquxa74Fn33rJzzBx38T58VucHx9"]
    result = await tools.getinflationreward("solana", addresses)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getlargestaccounts_live():
    result = await tools.getlargestaccounts("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getlatestblockhash_live():
    result = await tools.getlatestblockhash("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getleaderschedule_live():
    result = await tools.getleaderschedule("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getmaxretransmitslot_live():
    result = await tools.getmaxretransmitslot("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getmaxshredinsertslot_live():
    result = await tools.getmaxshredinsertslot("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getminimumbalanceforrentexemption_live():
    data_length = 128
    result = await tools.getminimumbalanceforrentexemption("solana", data_length)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getmultipleaccounts_live():
    pubkeys = [
        "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
        "7mhcgF1DVsj5iv4CxZDgp51H6MBBwqamsH1KnqXhSRc5",
    ]
    result = await tools.getmultipleaccounts("solana", pubkeys)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getprogramaccounts_live():
    program_id = "FsJ3A3u2vn5cTVofAjvy6y5kwABJAqYWpe4975bi2epH"
    result = await tools.getprogramaccounts("solana", program_id)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getrecentperformancesamples_live():
    result = await tools.getrecentperformancesamples("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getrecentprioritizationfees_live():
    accounts = ["CxELquR1gPP8wHe33gZ4QxqGB3sZ9RSwsJ2KshVewkFY"]
    result = await tools.getrecentprioritizationfees("solana", accounts)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getsignaturesforaddress_live():
    address = "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"
    result = await tools.getsignaturesforaddress("solana", address)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getsignaturestatuses_live():
    signatures = [
        "5VERv8NMvzbJMEkV8xnrLkEaWRtSz9CosKDYjCJjBRnbJLgp8uirBgmQpjKhoR4tjF3ZpRzrFmBV6UjKdiSZkQUW"
    ]
    result = await tools.getsignaturestatuses("solana", signatures)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getslot_live():
    result = await tools.getslot("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getslotleader_live():
    result = await tools.getslotleader("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1


async def test_getslotleaders_live():
    start_slot = 341767387
    limit = 10
    result = await tools.getslotleaders("solana", start_slot, limit)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getstakeminimumdelegation_live():
    commitment = "finalized"
    result = await tools.getstakeminimumdelegation("solana", commitment)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_getsupply_live():
    result = await tools.getsupply("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettokenaccountbalance_live():
    account = "3emsAVdmGKERbHjmGfQ6oZ1e35dkf5iYcS6U4CPKFVaa"
    result = await tools.gettokenaccountbalance("solana", account)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettokenaccountsbydelegate_live():
    delegate = "oQPnhXAbLbMuKHESaGrbXT17CyvWCpLyERSJA9HCYd7"
    mint = "GAehkgN1ZDNvavX81FmzCcwRnzekKMkSyUNq8WkMsjX1"
    result = await tools.gettokenaccountsbydelegate("solana", delegate, mint)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettokenaccountsbyowner_live():
    owner = "CEXq1uy9y15PL2Wb4vDQwQfcJakBGjaAjeuR2nKLj8dk"
    mint = "8wXtPeU6557ETkp9WHFY1n1EcU6NxDvbAggHGsMYiHsB"
    result = await tools.gettokenaccountsbyowner("solana", owner, mint)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettokenlargestaccounts_live():
    mint = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"
    result = await tools.gettokenlargestaccounts("solana", mint)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettokensupply_live():
    mint = "3wyAj7Rt1TWVPZVteFJPLa26JmLvdb1CAKEFZm3NY75E"
    result = await tools.gettokensupply("solana", mint)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettransaction_live():
    signature = (
        "49nKCKHSgAFEUDwwpY3p8p5HEhpN3hrZZ2qfbGSFUcB64Y65oscGp58sdgazLSvShahUFaezvoUkXtn7gdhgmRg9"
    )
    result = await tools.gettransaction("solana", signature)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_gettransactioncount_live():
    result = await tools.gettransactioncount("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert isinstance(parsed, int)


async def test_getversion_live():
    result = await tools.getversion("solana")
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))


async def test_simulatetransaction_live():
    transaction = "AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAEDArczbMia1tLmq7zz4DinMNN0pJ1JtLdqIJPUw3YrGCzYAMHBsgN27lcgB6H2WQvFgyZuJYHa46puOQo9yQ8CVQbd9uHXZaGT2cvhRs7reawctIXtX1s3kTqM9YV+/wCp20C7Wj2aiuk5TReAXo+VTVg8QTHjs0UjNMMKCvpzZ+ABAgEBARU="
    result = await tools.simulatetransaction("solana", transaction)
    assert not result.isError, f"Error: {result.content}"
    assert isinstance(result.content, list)
    assert len(result.content) == 1
    text = result.content[0].text
    parsed = ast.literal_eval(text)
    assert "value" in parsed or "result" in parsed or isinstance(parsed, (dict, list))
