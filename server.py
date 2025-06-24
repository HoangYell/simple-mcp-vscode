from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("SimpleMCP")

@mcp.tool()
def who_the_fuck_is_hoangyell() -> str:
    """Fetches info about hoangyell from hoangyell.com and returns a short summary."""
    # Fetch webpage content
    try:
        resp = httpx.get("https://hoangyell.com", timeout=10)
        if resp.status_code == 200:
            # Just return the first 300 chars as a summary (for demo)
            text = resp.text
            summary = text[:300].replace("\n", " ").replace("\r", " ")
            return f"hoangyell.com summary: {summary}..."
        else:
            return f"I think MCP just DDoSed hoangyell.com: {resp.status_code}"
    except Exception as e:
        return f"I think MCP just DDoSed hoangyell.com: {e}"

@mcp.tool()
def who_the_fuck_is_yellshark() -> str:
    """Creates a file with a message from yellshark and returns the file path."""
    file_path = os.path.abspath("yellshark.txt")
    with open(file_path, "w") as f:
        f.write("You're mad — from YellShark, with love. 🦈❤️😈\n")
    return f"The response is in this file: {file_path}"

if __name__ == "__main__":
    mcp.run()
