from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import END,START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langchain_core.tools import tool

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_PROJECT"] = "Practice-LangSmith-Tracing"

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="qwen/qwen3.6-27b"
)

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def tool_graph():

    @tool
    def add_numbers(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b

    tools = [add_numbers]
    tool_node = ToolNode(tools)
    llm_with_tools = llm.bind_tools(tools)

    def tool_calling_llm(state: State) :
        return {"messages":[llm_with_tools.invoke(state["messages"])]}

    # Node Definition
    def tool_calling_llm(state: State):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # Graph Construction
    builder = StateGraph(State)
    builder.add_node("tool_calling_llm", tool_calling_llm)
    builder.add_node("tools", ToolNode(tools=tools))

    # Edge Definition
    builder.add_edge(START, "tool_calling_llm")
    builder.add_conditional_edges("tool_calling_llm", tools_condition)
    builder.add_edge("tools", "tool_calling_llm")

    graph = builder.compile()
    return graph

tool_agent = tool_graph()
