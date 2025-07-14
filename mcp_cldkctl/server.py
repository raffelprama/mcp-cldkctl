#!/usr/bin/env python3
"""
MCP Server for Cloudeka CLI (cldkctl) functionality.
"""

import asyncio
import base64
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from importlib import metadata

import requests
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolResult,
    Tool,
    TextContent,
    Content,
)
from . import CLDKCTL_TOKEN as PKG_CLDKCTL_TOKEN, CLDKCTL_BASE_URL as PKG_CLDKCTL_BASE_URL

# Import the tool parameter map
try:
    from .tool_param_map import TOOL_PARAM_MAP
except ImportError:
    # Fallback if the file doesn't exist
    TOOL_PARAM_MAP = {}


class SimpleNotificationOptions:
    """Simple notification options class for MCP server capabilities."""

    def __init__(self, prompts_changed=False, resources_changed=False, tools_changed=False):
        self.prompts_changed = prompts_changed
        self.resources_changed = resources_changed
        self.tools_changed = tools_changed


# Initialize the server
server = Server("cldkctl")

# Configuration
PRODUCTION_URL = "https://ai.cloudeka.id"
STAGING_URL = "https://staging.ai.cloudeka.id"
CACHE_FILE = os.path.expanduser("~/.cldkctl/mcp_cache.json")
CACHE_DIR = os.path.expanduser("~/.cldkctl")

# Ensure cache directory exists
os.makedirs(CACHE_DIR, exist_ok=True)

# Global state for authentication and environment
auth_cache = {
    "jwt_token": None,
    "login_payload": None,
    "expires_at": None,
    "user_info": None,
    "environment": "production",
    "base_url": PRODUCTION_URL,
}

# Environment configuration
current_base_url = PRODUCTION_URL  # Default to production
environment_name = "production"


def load_cache():
    """Load cached authentication data."""
    global auth_cache, current_base_url, environment_name
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                cached_data = json.load(f)
                # Check if token is still valid
                if cached_data.get("expires_at"):
                    expires_at = datetime.fromisoformat(cached_data["expires_at"])
                    if datetime.now() < expires_at:
                        auth_cache.update(cached_data)
                        current_base_url = auth_cache["base_url"]
                        environment_name = auth_cache["environment"]
                        print(f"Loaded cached auth data, expires at {expires_at}", file=sys.stderr)
                        return True
                    else:
                        print("Cached token expired", file=sys.stderr)
                return False
    except Exception as e:
        print(f"Error loading cache: {e}", file=sys.stderr)
    return False


def save_cache():
    """Save authentication data to cache."""
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(auth_cache, f, default=str)
    except Exception as e:
        print(f"Error saving cache: {e}", file=sys.stderr)


def authenticate_with_token(token: str, force_staging: bool = False) -> bool:
    """Authenticate using a cldkctl token and get JWT."""
    global auth_cache, current_base_url, environment_name

    # Determine which URL to use
    if force_staging:
        base_url = STAGING_URL
        env_name = "staging"
    else:
        base_url = PRODUCTION_URL
        env_name = "production"

    print(f"Authenticating with {env_name} environment: {base_url}", file=sys.stderr)
    url = f"{base_url}/core/cldkctl/auth"
    payload = {"token": token}

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        print(f"Auth response status: {response.status_code}", file=sys.stderr)

        if response.status_code == 200:
            data = response.json()
            jwt_token = data.get("data", {}).get("token")
            if jwt_token:
                # Update global state
                current_base_url = base_url
                environment_name = env_name
                # Cache the authentication data
                auth_cache["jwt_token"] = jwt_token
                auth_cache["login_payload"] = base64.b64encode(json.dumps(payload).encode()).decode()
                auth_cache["expires_at"] = (datetime.now() + timedelta(hours=24)).isoformat()
                auth_cache["user_info"] = data.get("data", {})
                auth_cache["environment"] = env_name
                auth_cache["base_url"] = base_url
                save_cache()
                print(f"Authentication successful with {env_name}", file=sys.stderr)
                return True
            else:
                print("No JWT token in response", file=sys.stderr)
                return False
        elif response.status_code == 400 and "pq: relation \"cldkctl_tokens\" does not exist" in response.text:
            print("Production backend has database issue, trying staging...", file=sys.stderr)
            if not force_staging:
                return authenticate_with_token(token, force_staging=True)
            else:
                print("Staging also failed with the same issue.", file=sys.stderr)
                return False
        else:
            print(f"Authentication failed: {response.status_code} - {response.text}", file=sys.stderr)
            return False
    except requests.RequestException as e:
        print(f"Authentication request error: {e}", file=sys.stderr)
        if not force_staging:
            print("Trying staging as fallback...", file=sys.stderr)
            return authenticate_with_token(token, force_staging=True)
        return False


def get_auth_headers() -> Dict[str, str]:
    """Get headers with authentication token."""
    if not auth_cache.get("jwt_token"):
        raise Exception("Not authenticated. Please authenticate first.")

    # Check for token expiration
    expires_at_str = auth_cache.get("expires_at")
    if expires_at_str:
        if datetime.now() >= datetime.fromisoformat(expires_at_str):
            print("Token expired, attempting re-authentication", file=sys.stderr)
            if auth_cache.get("login_payload"):
                login_data = json.loads(base64.b64decode(auth_cache["login_payload"]).decode())
                if not authenticate_with_token(login_data["token"], force_staging=(environment_name == "staging")):
                    raise Exception("Re-authentication failed")
            else:
                raise Exception("Token expired and no login payload to re-authenticate.")

    return {
        "Authorization": f"Bearer {auth_cache['jwt_token']}",
        "Content-Type": "application/json",
    }


def make_authenticated_request(method: str, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
    """Make an authenticated request to the API."""
    url = f"{current_base_url}{endpoint}"
    try:
        headers = get_auth_headers()
        # For GET requests, do not send a body (data)
        if method.upper() == "GET":
            response = requests.request(method, url, headers=headers, params=params)
        else:
            response = requests.request(method, url, headers=headers, json=data, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Authenticated request failed: {e}", file=sys.stderr)
        # In case of an error, return a structured error message
        return {"error": True, "message": str(e), "status_code": getattr(e.response, "status_code", None)}


def get_tool_definitions() -> list[Tool]:
    """Generate tool definitions from TOOL_PARAM_MAP."""
    tools = []
    
    # Add basic authentication tools that are handled specially
    tools.extend([
        Tool(
            name="auth",
            description="Authenticate with a cldkctl token to get JWT access",
            inputSchema={
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "description": "Your cldkctl token (starts with 'cldkctl_')"
                    },
                    "force_staging": {
                        "type": "boolean",
                        "description": "Force using staging environment (default: false, will auto-fallback if production fails)"
                    }
                },
                "required": ["token"]
            }
        ),
    ])
    
    # Generate tools from TOOL_PARAM_MAP
    for tool_name, tool_info in TOOL_PARAM_MAP.items():
        # Remove the mcp_cldkctl_ prefix for the tool name
        clean_name = tool_name.replace("mcp_cldkctl_", "")
        
        # Build properties and required fields from the tool info
        properties = {}
        required = []
        
        # Add required parameters
        for param in tool_info.get("required_params", []):
            param_name = param["name"]
            param_type = param["type"]
            param_desc = param.get("desc", "")
            
            # Map parameter types to JSON schema types
            if param_type == "string":
                schema_type = "string"
            elif param_type == "integer":
                schema_type = "integer"
            elif param_type == "boolean":
                schema_type = "boolean"
            elif param_type == "list":
                schema_type = "array"
            elif param_type == "dict" or param_type == "object":
                schema_type = "object"
            else:
                schema_type = "string"  # Default to string
            
            properties[param_name] = {
                "type": schema_type,
                "description": param_desc
            }
            required.append(param_name)
        
        # Add optional parameters
        for param in tool_info.get("optional_params", []):
            param_name = param["name"]
            param_type = param["type"]
            param_desc = param.get("desc", "")
            
            # Map parameter types to JSON schema types
            if param_type == "string":
                schema_type = "string"
            elif param_type == "integer":
                schema_type = "integer"
            elif param_type == "boolean":
                schema_type = "boolean"
            elif param_type == "list":
                schema_type = "array"
            elif param_type == "dict" or param_type == "object":
                schema_type = "object"
            else:
                schema_type = "string"  # Default to string
            
            properties[param_name] = {
                "type": schema_type,
                "description": param_desc
            }
        
        # Create the tool
        tool = Tool(
            name=clean_name,
            description=f"Call the {clean_name} endpoint",
            inputSchema={
                "type": "object",
                "properties": properties,
                "required": required
            }
        )
        tools.append(tool)
    
    return tools


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List all available tools."""
    try:
        tools = get_tool_definitions()
        print(f"Successfully loaded {len(tools)} tools.", file=sys.stderr)
        return tools
    except Exception as e:
        print(f"!!!!!!!! ERROR GETTING TOOL DEFINITIONS !!!!!!!!", file=sys.stderr)
        print(f"Exception: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return []


def format_response(data: Any) -> str:
    """Formats API response data for display."""
    if isinstance(data, dict) and data.get("error"):
        return f"❌ API Error: {data.get('message', 'Unknown error')}"
    return f"```json\n{json.dumps(data, indent=2)}\n```"


@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> list[Content]:
    """Handle tool calls."""
    global current_base_url, environment_name
    
    # Normalize tool name by removing mcp_cldkctl_ prefix if present
    tool_name = name.replace("mcp_cldkctl_", "") if name.startswith("mcp_cldkctl_") else name
    
    try:
        # Handle authentication tools
        if tool_name == "auth":
            token = arguments["token"]
            force_staging = arguments.get("force_staging", False)
            if authenticate_with_token(token, force_staging):
                env_info = f" ({environment_name})" if environment_name != "production" else ""
                user_info = auth_cache.get('user_info', {})
                text = (
                    f"✅ Authentication successful{env_info}!\n\n"
                    f"User: {user_info.get('name', 'Unknown')}\n"
                    f"Role: {user_info.get('role', 'Unknown')}\n"
                    f"Organization: {user_info.get('organization_id', 'None')}\n"
                    f"Environment: {environment_name}\n"
                    f"Base URL: {current_base_url}"
                )
                return [TextContent(type="text", text=text)]
            else:
                return [TextContent(type="text", text="❌ Authentication failed.")]

        # Handle all other tools from TOOL_PARAM_MAP
        full_tool_name = f"mcp_cldkctl_{tool_name}"
        if full_tool_name in TOOL_PARAM_MAP:
            tool_info = TOOL_PARAM_MAP[full_tool_name]
            endpoint = tool_info["endpoint"]
            method = tool_info["method"]

            # Special case: registry list should always send page=1 and project-id if provided
            if full_tool_name == "mcp_cldkctl_cldkctl_registry_list":
                params = {"page": "1"}
                if "project-id" in arguments:
                    params["project-id"] = arguments["project-id"]
                data = make_authenticated_request(method, endpoint, params=params)
                return [TextContent(type="text", text=format_response(data))]
            
            # Handle path parameters in the endpoint
            try:
                # Replace path parameters like :param_name with actual values
                for param_name, param_value in arguments.items():
                    if f":{param_name}" in endpoint:
                        endpoint = endpoint.replace(f":{param_name}", str(param_value))
                
                # Determine what to send as body vs query params
                if method.upper() in ["POST", "PUT", "PATCH"]:
                    # For POST/PUT/PATCH, send arguments as JSON body
                    data = make_authenticated_request(method, endpoint, data=arguments)
                else:
                    # For GET/DELETE, send arguments as query parameters
                    data = make_authenticated_request(method, endpoint, params=arguments)
                
                return [TextContent(type="text", text=format_response(data))]
                
            except KeyError as e:
                return [TextContent(type="text", text=f"❌ Missing required parameter: {e}")]
            except Exception as e:
                return [TextContent(type="text", text=f"❌ Error executing {tool_name}: {str(e)}")]
        else:
            # Try without the prefix as well
            if tool_name in TOOL_PARAM_MAP:
                tool_info = TOOL_PARAM_MAP[tool_name]
                endpoint = tool_info["endpoint"]
                method = tool_info["method"]
                
                try:
                    # Replace path parameters like :param_name with actual values
                    for param_name, param_value in arguments.items():
                        if f":{param_name}" in endpoint:
                            endpoint = endpoint.replace(f":{param_name}", str(param_value))
                    
                    # Determine what to send as body vs query params
                    if method.upper() in ["POST", "PUT", "PATCH"]:
                        # For POST/PUT/PATCH, send arguments as JSON body
                        data = make_authenticated_request(method, endpoint, data=arguments)
                    else:
                        # For GET/DELETE, send arguments as query parameters
                        data = make_authenticated_request(method, endpoint, params=arguments)
                    
                    return [TextContent(type="text", text=format_response(data))]
                    
                except KeyError as e:
                    return [TextContent(type="text", text=f"❌ Missing required parameter: {e}")]
                except Exception as e:
                    return [TextContent(type="text", text=f"❌ Error executing {tool_name}: {str(e)}")]
            else:
                available_tools = [name.replace("mcp_cldkctl_", "") for name in TOOL_PARAM_MAP.keys()]
                return [TextContent(type="text", text=f"❌ Unknown tool: {tool_name}. Available tools: {', '.join(available_tools[:20])}...")]

    except Exception as e:
        print(f"Error calling tool {tool_name}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return [TextContent(type="text", text=f"❌ Error executing tool '{tool_name}': {str(e)}")]


async def main():
    """Main function."""
    print("Initializing server...", file=sys.stderr)
    try:
        __version__ = metadata.version("mcp-cldkctl")
    except metadata.PackageNotFoundError:
        __version__ = "0.0.0-dev"

    # Token loading logic moved here
    def load_token_from_mcp_json():
        import pathlib
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

    if not load_cache():
        token = os.environ.get("CLDKCTL_TOKEN")
        base_url = os.environ.get("CLDKCTL_BASE_URL")
        # Use package-level values as fallback if env not set
        if not token:
            token = PKG_CLDKCTL_TOKEN
        if not base_url:
            base_url = PKG_CLDKCTL_BASE_URL
        # If still not set, try reading mcp.json directly (legacy fallback)
        if not token:
            token, base_url = load_token_from_mcp_json()
        if token:
            print("No valid cache found, authenticating with token from environment, package, or mcp.json...", file=sys.stderr)
            force_staging = base_url == STAGING_URL if base_url else False
            authenticate_with_token(token, force_staging=force_staging)
        else:
            print("No valid cache or environment/config token found. You will be prompted for a token on first use.", file=sys.stderr)

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="cldkctl",
                server_version=__version__,
                capabilities=server.get_capabilities(
                    notification_options=SimpleNotificationOptions(
                        prompts_changed=False,
                        resources_changed=False,
                        tools_changed=False,
                    ),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shutting down.", file=sys.stderr)