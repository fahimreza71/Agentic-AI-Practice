from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> dict:
    """Get the current weather for a given city."""
    return {
        "city": city,
        "temperature": 20.0,
        "condition": "Sunny"
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http")