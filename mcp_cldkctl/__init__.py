"""MCP server for Cloudeka cldkctl CLI integration (Testing Version)"""

__version__ = "0.1.36"

import os
import json
import pathlib

# Try to load token and base_url from mcp.json at import time
CLDKCTL_TOKEN = None
CLDKCTL_BASE_URL = None

def _load_token_from_mcp_json():
    config_path = os.path.expanduser("~/.cursor/mcp.json")
    if not os.path.exists(config_path):
        config_path = str(pathlib.Path.home() / ".cursor" / "mcp.json")
    try:
        with open(config_path, "r") as f:
            data = json.load(f)
            token = data.get("mcpServers", {}).get("cldkctl", {}).get("env", {}).get("CLDKCTL_TOKEN")
            base_url = data.get("mcpServers", {}).get("cldkctl", {}).get("env", {}).get("CLDKCTL_BASE_URL")
            return token, base_url
    except Exception:
        return None, None

CLDKCTL_TOKEN, CLDKCTL_BASE_URL = _load_token_from_mcp_json()

# mcp_cldkctl package 