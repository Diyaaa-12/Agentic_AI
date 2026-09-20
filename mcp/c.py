import asyncio
import os

from dotenv import load_dotenv

from langchain.mcp import MCPAdapter
from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter


load_dotenv()


async def main():

    # Connect to the MCP server through HTTP
    async with MCPAdapter(
        "http://localhost:8000/mcp"
    ) as adapter:

        # Discover MCP tools
        tools = await adapter.list_tools()

        print("Available MCP tools:")

        for tool in tools:
            print("-", tool.name)

        # OpenRouter model
        model = ChatOpenRouter(
            model="z-ai/glm-5.3-flash",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            temperature=0
        )

        # Create LangChain agent
        agent = create_agent(
            model=model,
            tools=tools
        )

        # Ask the agent
        response = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": "What are Praveen's AI marks?"
                }
            ]
        })

        print("\nAnswer:")
        print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())