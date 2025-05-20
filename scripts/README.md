## ⚠️ Important Notice for Developers

The auto-generation of class tools significantly accelerates development time but produces output that **requires review and enhancement**.

## Current Limitations

Auto-generated tools typically have these issues:
- Incomplete or unclear annotations
- Missing or generic examples
- Suboptimal parameter descriptions
- Lack of context-specific usage guidance

## Required Enhancements After Auto-Generation

### 1. Improve Annotations

Enhance the automatically generated annotations to provide better context for the model:

```python
# Auto-generated (needs improvement)
@mcp.tool(
    name="getaccountinfo",
    description="Call the getAccountInfo JSON-RPC method: getAccountInfo\nReturns: Account information\n\nParameters:\n- account: The public key of the account [Example: 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM]\n- options (Options object): Options including: encoding, commitment [Object Example: {encoding=jsonParsed, commitment=finalized}]",
    annotations={"title": "getAccountInfo", "readOnlyHint": True},
)

# After enhancement
@mcp.tool(
    name="getaccountinfo",
    description="""Retrieves detailed account information from the Solana blockchain.

Parameters:
- account (string): The public key of the account to query. Example: 9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM
- options (object): Configuration options for the request.
  - encoding (string): Data encoding format. One of: base58, base64, jsonParsed. Default: jsonParsed
  - commitment (string): Confirmation level to use. One of: processed, confirmed, finalized. Default: finalized

Example Input:
{
  "account": "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
  "options": {"encoding": "jsonParsed", "commitment": "finalized"}
}

Example Output:
{
  "lamports": 1000000000,
  "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
  "executable": false,
  "rentEpoch": 361,
  "data": {
    "parsed": {
      "info": {
        "mint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "owner": "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg",
        "tokenAmount": {
          "amount": "100000000",
          "decimals": 6,
          "uiAmount": 100
        }
      },
      "type": "account"
    },
    "program": "spl-token",
    "space": 165
  }
}
""",
    annotations={
        "title": "Get Account Information",
        "readOnlyHint": True,
        "resultDescription": "Returns detailed account data including balance, ownership, and program-specific data"
    },
)
```

## Resources

- [Model Context Protocol: Tools](https://modelcontextprotocol.io/docs/concepts/tools#best-practices)