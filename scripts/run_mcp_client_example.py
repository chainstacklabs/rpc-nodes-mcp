import asyncio

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# API key will be read from env var OPENAI_API_KEY
model = ChatOpenAI(model="gpt-4o")
server_params = StdioServerParameters(
    command="python",
    args=["src/main_evm.py"],
)


def print_messages_pretty(messages):
    """Print messages with nice formatting using Rich"""
    for msg in messages:
        msg_type = str(msg.type).upper()
        content = msg.content

        title = Text(msg_type, style="bold blue")
        console.print(
            Panel(content, title=title, border_style="green", expand=False, padding=(1, 2))
        )


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            console.print("[bold yellow]Sending query to agent...[/]")

            agent = create_react_agent(model, tools)

            # In this example, you will see how LLM calls two tools (get balance and convert Wei to Eth)
            agent_response = await agent.ainvoke(
                {
                    "messages": "Get mainnet Ethereum account balance 0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326 in Eth"
                }
            )

            print_messages_pretty(agent_response["messages"])


if __name__ == "__main__":
    asyncio.run(main())
