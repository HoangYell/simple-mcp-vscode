# TL;DR — Quick MCP Setup for VS Code

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
