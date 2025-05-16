from mcp.types import CallToolResult, TextContent


def _err(msg: str) -> CallToolResult:
    return CallToolResult(isError=True, content=[TextContent(type="text", text=msg)])


def _ok(data) -> CallToolResult:
    return CallToolResult(content=[TextContent(type="text", text=str(data))])
