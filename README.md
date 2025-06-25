# Create a Custom MCP Server and Use It with GitHub Copilot in VS Code

> **Description:**
> Basic example for using Model Context Protocol (MCP) with VS Code. This repo shows how to create your own MCP server and interact with it by chatting custom prompts to GitHub Copilot in VS Code.

1. **Clone & enter the repo**

```sh
git clone git@github.com:HoangYell/simple-mcp-vscode.git
cd simple-mcp-vscode
```

2. **(If needed) Install venv module**

```sh
sudo apt install python3-venv
```

3. **Create & activate a virtual environment**

```sh
python3 -m venv .venv
source .venv/bin/activate
```

4. **Install dependencies**

```sh
pip install -r requirements.txt
```

5. **Configure VS Code**

Add to your [settings.json](vscode://settings/chat.mcp.discovery.enabled):

```jsonc
{
  "chat.mcp.discovery.enabled": true,
  "mcp": {
    "servers": {
      "SimpleMCP": {
        "type": "python",
        "command": "/path/to/project/.venv/bin/python", // e.g. /home/hoangyell/simple-mcp-vscode/.venv/bin/python
        "args": ["/path/to/project/server.py"], // e.g. /home/hoangyell/simple-mcp-vscode/server.py
        "cwd": "/path/to/project" // e.g. /home/hoangyell/simple-mcp-vscode
      }
    }
  }
}
```

- Click <Start> above SimpleMCP in VS Code's settings, or run:

```sh
python server.py
```

7. **Try it!**

- In the chat, type: `who the fuck is hoangyell?`
- Or: `who the fuck is yellshark?`

---

You should now see the MCP tools working in VS Code chat.

https://www.youtube.com/watch?v=U1YMyUdjqCw

![funny_mcp](https://raw.githubusercontent.com/HoangGeek/store/refs/heads/main/github_copilot/mcp/custom_mcp.png)

+-----------------------------+ +-----------------------------+ +-----------------------------+
| VS Code | | MCP Server | | VS Code |
| +-----------------------+ | | +-----------------------+ | | +-----------------------+ |
| | MCP Client Extension |<-------->| | Parses Input |<-------->| | MCP Client Extension | |
| | (Chat Window / | | | +----------+------------+ | | | (Displays output | |
| | Interactive Panel) | | | | | | | to user) | |
| | - User types input | | | v | | +-----------------------+ |
| | - Displays output | | | +-----------------------+ | +-----------------------------+
| +----------+------------+ | | | Detects Tool/Keyword | |
+-----------------------------+ | +----------+------------+ |
| | |
| v |
| +-----------------------+ |
| | Finds Registered Tool | |
| | (e.g. @mcp.tool) | |
| +----------+------------+ |
| | |
| v |
| +-----------------------+ |
| | Calls Tool Function | |
| | (e.g. who*the_fuck* | |
| | is_yellshark) | |
| +----------+------------+ |
| | |
| v |
| +-----------------------+ |
| | Returns Tool Output | |
| +-----------------------+ |
+-----------------------------+
