# MCP cldkctl Server

A Model Context Protocol (MCP) server that provides full access to Cloudeka's cldkctl CLI functionality through Claude Desktop, Cursor, and other MCP-compatible clients.

## Features

- **Smart Authentication**: Automatic environment fallback (production -> staging)
- **Auto-Reauthentication**: Handles token expiry automatically
- **Complete API Coverage**: All cldkctl endpoints available as MCP tools
- **Persistent Caching**: JWT tokens cached locally for performance
- **Environment Management**: Easy switching between production and staging
- **Full Tool Suite**: Kubernetes, billing, VMs, registry, notebooks, and more

## Installation

### From PyPI

```bash
pip install mcp-cldkctl
# or
uvx mcp-cldkctl
```

### From Source

```bash
git clone https://github.com/cloudeka/mcp-cldkctl.git
cd mcp-cldkctl
pip install -e .
# or
uv sync
```

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `CLDKCTL_TOKEN` | Yes | - | Your cldkctl token (starts with `cldkctl_`) |
| `CLDKCTL_BASE_URL` | No | `https://ai.cloudeka.id` | Base URL (auto-fallback to staging if production fails) |
| `CLDKCTL_DEFAULT_PROJECT_ID` | No | - | Default project ID for convenience |

### Example Setup

**Linux/macOS:**
```bash
export CLDKCTL_TOKEN="cldkctl_your_token_here"
export CLDKCTL_BASE_URL="https://ai.cloudeka.id"
export CLDKCTL_DEFAULT_PROJECT_ID="your_project_id"
```

**Windows:**
```cmd
set CLDKCTL_TOKEN=cldkctl_your_token_here
set CLDKCTL_BASE_URL=https://ai.cloudeka.id
set CLDKCTL_DEFAULT_PROJECT_ID=your_project_id
```

## Usage

### Running the Server

```bash
# Using uvx (recommended)
uvx mcp-cldkctl

# Direct execution
python -m mcp_cldkctl.server

# Using the installed script
mcp-cldkctl
```

### Claude Desktop Configuration

Add this to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "cldkctl": {
      "command": "uvx",
      "args": ["mcp-cldkctl"],
      "env": {
        "CLDKCTL_TOKEN": "your_cldkctl_token_here",
        "CLDKCTL_BASE_URL": "https://ai.cloudeka.id"
      }
    }
  }
}
```

### Cursor Configuration

Add this to your Cursor settings:

```json
{
  "mcpServers": {
    "cldkctl": {
      "command": "uvx",
      "args": ["mcp-cldkctl"],
      "env": {
        "CLDKCTL_TOKEN": "your_cldkctl_token_here"
      }
    }
  }
}
```

## Development

For development, install the package with development dependencies:

```bash
pip install -e ".[dev]"
```

## Available Tools

### Authentication & Environment
- **`auth`** - Authenticate with your cldkctl token
- **`switch_environment`** - Switch between production/staging
- **`status`** - Check current environment and auth status

### Balance & Billing
- **`balance_detail`** - Get project balance details
- **`billing_daily_cost`** - Get daily billing costs
- **`billing_monthly_cost`** - Get monthly billing costs
- **`billing_history`** - Get billing history

### Kubernetes Management
- **`k8s_pods`** - List Kubernetes pods
- **`k8s_deployments`** - List Kubernetes deployments
- **`k8s_services`** - List Kubernetes services
- **`k8s_configmaps`** - List Kubernetes configmaps
- **`k8s_secrets`** - List Kubernetes secrets

### Project & Organization
- **`project_list`** - List all projects
- **`project_detail`** - Get project details
- **`org_detail`** - Get organization details
- **`org_members`** - List organization members
- **`profile_detail`** - Get user profile

### Virtual Machines
- **`vm_list`** - List virtual machines
- **`vm_detail`** - Get VM details

### Container Registry
- **`registry_list`** - List container registries
- **`registry_repositories`** - List registry repositories

### Notebooks
- **`notebook_list`** - List Deka notebooks
- **`notebook_create`** - Create a new notebook

### Vouchers & Tokens
- **`voucher_list`** - List available vouchers
- **`voucher_apply`** - Apply a voucher code
- **`token_list`** - List cldkctl tokens
- **`token_create`** - Create a new token
- **`token_delete`** - Delete a token

### Logs
- **`audit_logs`** - Get audit logs

## Environment Fallback

The MCP server automatically handles environment issues:

1. **Tries production first** (`https://ai.cloudeka.id`)
2. **Detects database errors** (missing `cldkctl_tokens` table)
3. **Auto-fallbacks to staging** (`https://staging.ai.cloudeka.id`)
4. **Caches the working environment** for future requests

### Manual Environment Switching

```python
# Switch to staging
switch_environment(environment="staging")

# Switch to production
switch_environment(environment="production")

# Check current status
status()
```

## Authentication Flow

1. **Initial Auth**: Exchange cldkctl token for JWT
2. **Token Caching**: JWT stored locally with 24-hour expiry
3. **Auto-Reauth**: Automatically re-authenticate when token expires
4. **Environment Persistence**: Remember which environment works

## Example Usage

### Basic Authentication
```python
# Authenticate (auto-fallback if production fails)
auth(token="cldkctl_your_token_here")

# Check status
status()
```

### Project Management
```python
# List all projects
project_list()

# Get specific project details
project_detail(project_id="your_project_id")
```

### Kubernetes Operations
```python
# List pods in default namespace
k8s_pods(project_id="your_project_id")

# List deployments in specific namespace
k8s_deployments(project_id="your_project_id", namespace="kube-system")
```

### Billing Queries
```python
# Get daily costs
billing_daily_cost(project_id="your_project_id")

# Get billing history
billing_history(
    project_id="your_project_id",
    start_date="2024-01-01",
    end_date="2024-01-31"
)
```

## Troubleshooting

### Common Issues

**Authentication Failed**
- Check your `CLDKCTL_TOKEN` is valid
- Ensure token starts with `cldkctl_`
- Try using staging environment manually

**Production Database Error**
- This is normal - the server auto-fallbacks to staging
- Check status to see which environment is active

**Token Expired**
- The server auto-reauthenticates
- Check status to verify authentication

**Environment Issues**
```python
# Force staging environment
auth(token="your_token", force_staging=True)

# Check current environment
status()
```

## Version History

Current version: 1.0.0 (Production)

## License

MIT License

---

## Security

**Never commit your real tokens, secrets, or credentials to the repository.**
All authentication is handled via environment variables or user input. Example tokens in this documentation are placeholders only.

--- 