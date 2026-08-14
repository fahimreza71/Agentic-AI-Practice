# Agentic AI Practice

A personal learning repository for building agentic AI systems with [LangGraph](https://langchain-ai.github.io/langgraph/), [LangChain](https://www.langchain.com/), and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Each project explores a different pattern — from a basic chatbot to multi-agent supervisor workflows and custom MCP tool servers.

## Repository layout

| Path | Description |
|---|---|
| [`AgenticAi-LangGraph-MCP/`](AgenticAi-LangGraph-MCP) | Main project: LangGraph agents, MCP tool servers (`math-server.py`, `weather-server.py`), and an MCP client that wires them into a LangChain agent. |
| [`AgenticAi-LangGraph-MCP/Agents/`](AgenticAi-LangGraph-MCP/Agents) | A supervisor-based multi-agent workflow (researcher → analyst → writer) with structured-output routing and a loop guard. |
| [`AgenticAi-LangGraph-MCP/ChatBot/`](AgenticAi-LangGraph-MCP/ChatBot) | A basic LangGraph chatbot notebook. |
| [`AgenticAi-LangGraph-MCP/LangSmith-Tracing/`](AgenticAi-LangGraph-MCP/LangSmith-Tracing) | A tool-calling agent set up for local tracing with LangGraph Studio / LangSmith. |
| [`LangGraph/`](LangGraph) | Earlier LangGraph exercises, including a multi-tool chatbot notebook. |
| [`dummyProject/`](dummyProject) | Scratch project used for trying out `uv` project setup. |

## Getting started

Each project manages its own dependencies with [`uv`](https://docs.astral.sh/uv/). From inside a project directory (e.g. `AgenticAi-LangGraph-MCP/`):

```bash
uv sync
```

Or with `pip`:

```bash
pip install -r requirements.txt
```

### Environment variables

Each project expects a local `.env` file (not committed) with the API keys it needs, typically:

```
GROQ_API_KEY=...
LANGCHAIN_API_KEY=...
TAVILY_API_KEY=...
```

### Running

Notebooks (`.ipynb`) run directly in Jupyter or VS Code. Standalone scripts run with:

```bash
python <script>.py
```

For the MCP client/server setup in `AgenticAi-LangGraph-MCP/`, start `weather-server.py` in one terminal before running `client.py` (it connects to the weather server over HTTP; the math server is spawned automatically over stdio).

## Notes

- This is a practice/learning repository — code favors clarity over production hardening.
- Dependency versions are pinned where a known incompatibility exists (see `AgenticAi-LangGraph-MCP/pyproject.toml`); check there before upgrading `mcp` or related packages.
