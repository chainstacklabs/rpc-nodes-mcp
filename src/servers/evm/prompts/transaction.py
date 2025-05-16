"""
MCP prompt that provides a natural language entry point for transaction analysis.
"""

from mcp.server.fastmcp.prompts import base

from server import mcp


@mcp.prompt(name="review_transaction")
def review_transaction(tx_signature: str) -> list[base.Message]:
    return [
        base.UserMessage(
            "I want you to analyze this transaction from a Web3 developer perspective:"
        ),
        base.UserMessage(tx_signature),
    ]
