from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    mcp_client = MultiServerMCPClient(
        {
            "Math":{
                "command":"python",
                "args":["math-server.py"],
                "transport":"stdio"
            },
            "Weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await mcp_client.get_tools()
    model = ChatGroq(model="qwen/qwen3.6-27b")
    agent = create_agent(model, tools)

    math_response = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": "What is (3+5)*12?"}
        ]
    })

    print("Math Response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke({
        "messages": [   
            {"role": "user", "content": "What is the weather in New York City?"}
        ]
    })

    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())