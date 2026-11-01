# MCP CLDKCTL - Model Context Protocol Server for Cloudeka CLI

## 🏠 Home Page

### Description
MCP CLDKCTL is a Model Context Protocol (MCP) server that provides seamless integration between AI assistants (Claude Desktop, Cursor) and Cloudeka's cloud infrastructure management platform. It transforms the cldkctl CLI functionality into AI-accessible tools, enabling natural language interaction with Kubernetes clusters, virtual machines, container registries, billing systems, and more.

### Key Benefits
- **🤖 AI-Native Interface**: Control your entire cloud infrastructure through natural language conversations
- **🔐 Smart Authentication**: Automatic token management with environment fallback (production → staging)
- **⚡ Persistent Caching**: JWT tokens cached locally for optimal performance
- **🔄 Auto-Reauthentication**: Seamless token renewal without manual intervention
- **🌍 Multi-Environment Support**: Easy switching between production and staging environments
- **📊 Complete API Coverage**: Access to all cldkctl endpoints as MCP tools

### Quick Preview Tools
- **Kubernetes Management**: Pods, deployments, services, configmaps, secrets
- **Virtual Machine Operations**: Create, manage, start/stop VMs
- **Container Registry**: Manage Docker registries and artifacts
- **Billing & Cost Management**: Monitor usage, view invoices, track expenses
- **Project & Organization**: User management, role assignments, project configuration
- **Notebook Management**: Create and manage Deka notebooks
- **Audit & Security**: View audit logs, manage tokens

---

## 1. Prerequisites and Setup

### Required Components
- **Python 3.8+** with pip or uv package manager
- **cldkctl Token**: Valid authentication token from Cloudeka platform
- **MCP-Compatible Client**: Claude Desktop, Cursor, or other MCP hosts
- **Network Access**: Connection to Cloudeka API endpoints

### Installation Options

#### Option A: From PyPI (Recommended)
```bash
# Using uvx (recommended)
uvx mcp-cldkctl-t

# Using pip
pip install mcp-cldkctl-t
```

#### Option B: From Source
```bash
git clone https://github.com/cloudeka/mcp-cldkctl.git
cd mcp-cldkctl
pip install -e .
# or
uv sync
```

### Environment Configuration

#### Environment Variables
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `CLDKCTL_TOKEN` | Yes | - | Your cldkctl token (starts with `cldkctl_`) |
| `CLDKCTL_BASE_URL` | No | `https://ai.cloudeka.id` | Base URL (auto-fallback to staging) |
| `CLDKCTL_DEFAULT_PROJECT_ID` | No | - | Default project ID for convenience |

#### Setup Examples

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

---

## 2. Integration with AI (Claude Desktop, Cursor)

### Claude Desktop Configuration

Add to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "cldkctl": {
      "command": "uvx",
      "args": ["mcp-cldkctl-t@0.1.12"],
      "env": {
        "CLDKCTL_TOKEN": "cldkctl_your_token_here",
        "CLDKCTL_BASE_URL": "https://staging.ai.cloudeka.id"
      }
    }
  }
}
```

### Cursor Configuration

Add to your Cursor settings (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "cldkctl": {
      "command": "uvx",
      "args": ["mcp-cldkctl-t@0.1.12"],
      "env": {
        "CLDKCTL_TOKEN": "your_cldkctl_token_here",
        "CLDKCTL_BASE_URL": "https://staging.ai.cloudeka.id"
      }
    }
  }
}
```

### Configuration Features
- **Automatic Token Loading**: Reads from environment variables or `mcp.json`
- **Environment Fallback**: Automatically switches to staging if production fails
- **Persistent Caching**: Stores authentication tokens locally
- **Cross-Platform Support**: Works on Windows, macOS, and Linux

---

## 3. Core Functions (Tools)

### Authentication & Environment Management

#### `auth`
Authenticate with your cldkctl token to get JWT access.
```python
auth(token="cldkctl_your_token_here", force_staging=False)
```

#### `switch_environment`
Switch between production and staging environments.
```python
switch_environment(environment="staging")  # or "production"
```

#### `status`
Check current authentication and environment status.
```python
status()
```

### Project & Organization Management

#### `project_list`
List all projects in your organization.
```python
project_list()
```

#### `project_detail`
Get detailed information about a specific project.
```python
project_detail(project_id="your_project_id")
```

#### `org_detail`
Get organization details and information.
```python
org_detail()
```

#### `org_members`
List all members in your organization.
```python
org_members()
```

### Kubernetes Management

#### `k8s_pods`
List Kubernetes pods in a namespace.
```python
k8s_pods(project_id="your_project_id", namespace="default")
```

#### `k8s_deployments`
List Kubernetes deployments.
```python
k8s_deployments(project_id="your_project_id", namespace="default")
```

#### `k8s_services`
List Kubernetes services.
```python
k8s_services(project_id="your_project_id", namespace="default")
```

#### `k8s_configmaps`
List Kubernetes configmaps.
```python
k8s_configmaps(project_id="your_project_id", namespace="default")
```

#### `k8s_secrets`
List Kubernetes secrets.
```python
k8s_secrets(project_id="your_project_id", namespace="default")
```

### Virtual Machine Management

#### `vm_list`
List all virtual machines.
```python
vm_list()
```

#### `vm_detail`
Get detailed information about a specific VM.
```python
vm_detail(vm_id="your_vm_id")
```

#### `vm_create`
Create a new virtual machine.
```python
vm_create(
    project_id="your_project_id",
    name="my-vm",
    flavor="flavor_id",
    image="image_id",
    network="network_id",
    storage="100GB"
)
```

#### `vm_turn_on` / `vm_turn_off`
Control VM power states.
```python
vm_turn_on(vm_id="your_vm_id")
vm_turn_off(vm_id="your_vm_id")
```

### Container Registry Management

#### `registry_list`
List container registries in a project.
```python
registry_list(project_id="your_project_id")
```

#### `registry_repositories`
List repositories in a registry.
```python
registry_repositories(registry_id="your_registry_id")
```

#### `registry_detail`
Get detailed registry information.
```python
registry_detail(registry_id="your_registry_id")
```

### Billing & Cost Management

#### `balance_detail`
Get project balance details.
```python
balance_detail(project_id="your_project_id")
```

#### `billing_daily_cost`
Get daily billing costs for a project.
```python
billing_daily_cost(project_id="your_project_id")
```

#### `billing_monthly_cost`
Get monthly billing costs for a project.
```python
billing_monthly_cost(project_id="your_project_id")
```

#### `billing_history`
Get billing history for a date range.
```python
billing_history(
    project_id="your_project_id",
    start="2024-01-01",
    end="2024-01-31"
)
```

#### `billing_invoice_sme`
List SME invoices.
```python
billing_invoice_sme()
```

### Notebook Management

#### `notebook_list`
List Deka notebooks in a project.
```python
notebook_list(project_id="your_project_id")
```

#### `notebook_create`
Create a new Deka notebook.
```python
notebook_create(
    project_id="your_project_id",
    name="my-notebook",
    namespace="default",
    image="image_id",
    cpu="2",
    memory="4GB",
    storage="50GB"
)
```

### Voucher & Token Management

#### `voucher_list`
List available vouchers.
```python
voucher_list()
```

#### `voucher_apply`
Apply a voucher code.
```python
voucher_apply(voucher_code="VOUCHER123")
```

#### `token_list`
List your cldkctl tokens.
```python
token_list()
```

#### `token_create`
Create a new cldkctl token.
```python
token_create(name="my-token", expiration_days=30)
```

### Audit & Security

#### `audit_logs`
Get audit logs.
```python
audit_logs()
```

### Advanced Kubernetes Operations

#### `k8s_pod_create`
Create a new Kubernetes pod.
```python
k8s_pod_create(
    project_id="your_project_id",
    namespace="default",
    spec={"apiVersion": "v1", "kind": "Pod", ...}
)
```

#### `k8s_pod_edit`
Edit an existing Kubernetes pod.
```python
k8s_pod_edit(
    project_id="your_project_id",
    namespace="default",
    name="pod-name",
    spec={"apiVersion": "v1", "kind": "Pod", ...}
)
```

#### `k8s_pod_delete`
Delete a Kubernetes pod.
```python
k8s_pod_delete(
    project_id="your_project_id",
    namespace="default",
    name="pod-name"
)
```

---

## 4. Local Testing and Development

### Running the Server Locally

#### Direct Execution
```bash
# Using uvx (recommended)
uvx mcp-cldkctl-t

# Direct Python execution
python -m mcp_cldkctl.server

# Using the installed script
mcp-cldkctl-t
```

### Development Setup

#### Install Development Dependencies
```bash
pip install -e ".[dev]"
# or
uv sync --dev
```

#### Available Test Files
- `test_auth.py` - Basic authentication tests
- `test_production_auth.py` - Production environment auth tests
- `test_staging_auth.py` - Staging environment auth tests
- `test_api_endpoint.py` - API endpoint tests
- `test_package.py` - Package functionality tests

#### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest test_auth.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=mcp_cldkctl
```

### Debugging Tools

#### Debug Authentication
```bash
python debug_auth.py
```

#### Debug Environment Switching
```bash
python debug_production_vs_staging.py
```

#### Debug API Endpoints
```bash
python debug_tools.py
```

### Building and Publishing

#### Build Package
```bash
python build_and_publish.py
```

#### Manual Build
```bash
# Build wheel
python -m build

# Build source distribution
python setup.py sdist bdist_wheel
```

---

## 5. Architecture Overview

### System Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   MCP Client    │    │   MCP Server     │    │  Cloudeka API   │
│  (Claude/Cursor)│◄──►│  (mcp-cldkctl)   │◄──►│  (ai.cloudeka.id)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Local Cache    │
                       │  (~/.cldkctl/)   │
                       └──────────────────┘
```

### Data Flow

1. **MCP Client Request**: AI assistant sends tool call request
2. **MCP Server Processing**: Server validates and processes the request
3. **Authentication Check**: Verify JWT token or re-authenticate if needed
4. **API Call**: Make authenticated request to Cloudeka API
5. **Response Processing**: Format and return response to client
6. **Caching**: Store authentication tokens locally

### Authentication Flow

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   cldkctl   │───►│   JWT Token  │───►│   API Call  │───►│   Response  │
│   Token     │    │   (24h exp)  │    │             │    │             │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                          │
                          ▼
                   ┌──────────────┐
                   │ Local Cache  │
                   │ (~/.cldkctl) │
                   └──────────────┘
```

### Environment Fallback Mechanism

```
┌─────────────────┐
│ Try Production  │
│ (ai.cloudeka.id)│
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Database Error? │
│ (cldkctl_tokens)│
└─────────┬───────┘
          │ Yes
          ▼
┌─────────────────┐
│ Try Staging     │
│ (staging.ai...) │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Cache Working   │
│ Environment     │
└─────────────────┘
```

### File Structure

```
mcp-cldkctl/
├── mcp_cldkctl/
│   ├── __init__.py          # Package initialization, token loading
│   ├── __main__.py          # CLI entry point
│   ├── server.py            # Main MCP server implementation
│   └── tool_param_map.py    # Tool definitions and API mappings
├── pyproject.toml           # Package configuration
├── README.md               # Package documentation
└── build_and_publish.py    # Build and deployment script
```

### Key Features

#### Smart Token Management
- **Automatic Loading**: Reads from environment variables, `mcp.json`, or cache
- **Persistent Storage**: Caches JWT tokens locally with expiration tracking
- **Auto-Reauthentication**: Seamlessly renews expired tokens
- **Environment Persistence**: Remembers working environment (production/staging)

#### Tool Generation
- **Dynamic Tool Creation**: Generates MCP tools from `TOOL_PARAM_MAP`
- **Parameter Validation**: Validates required and optional parameters
- **Type Mapping**: Converts API types to JSON schema types
- **Error Handling**: Comprehensive error handling and reporting

#### API Integration
- **RESTful Interface**: Full REST API coverage for all cldkctl endpoints
- **Method Support**: GET, POST, PUT, PATCH, DELETE operations
- **Path Parameters**: Dynamic URL parameter substitution
- **Query/Body Handling**: Automatic parameter routing based on HTTP method

### Security Considerations

- **Token Encryption**: JWT tokens stored with base64 encoding
- **Local Storage**: Authentication data stored in user's home directory
- **Environment Isolation**: Separate configurations for production/staging
- **Automatic Cleanup**: Expired tokens automatically removed from cache

### Performance Optimizations

- **Connection Pooling**: Reuses HTTP connections for better performance
- **Caching Strategy**: 24-hour JWT token caching reduces authentication overhead
- **Lazy Loading**: Tools loaded only when needed
- **Error Recovery**: Automatic retry mechanisms for transient failures

## 5. API Testing Summary

| Group            | Tool Name / Action         | Endpoint (from note.txt)                                         | Result / Notes                                 | Status   |
|------------------|---------------------------|------------------------------------------------------------------|------------------------------------------------|----------|
| **User & Profile** | Auth (token)              | /core/cldkctl/auth                                               | Success, valid JWT                             | ✅        |
|                  | Login                     | /core/user/login                                                 | 400 Bad Request (no backend handler)           | ❌        |
|                  | ProfileDetail             | /core/user/profile                                               | Success                                        | ✅        |
|                  | UpdateProfile             | /core/user/organization/profile/member/:user_id                  | 400 Bad Request (invalid user)                 | ❌        |
|                  | ChangePassword            | /core/user/change-password                                       | 400 Bad Request (invalid password)             | ❌        |
| **Project**      | ProjectList               | /core/user/organization/projects/byOrg                           | Success (1 project found)                      | ✅        |
|                  | ProjectDetail             | /core/user/project/detail/:project_id                            | Success                                        | ✅        |
|                  | UpdateProject             | /core/user/projects/:project_id                                  | 400 Bad Request                                | ❌        |
|                  | CheckBeforeDeleteProject  | /core/user/checking/projects/:project_id                         | Success                                        | ✅        |
|                  | DeleteProject             | /core/user/projects/:project_id                                  | Not tested (no delete performed)               | -        |
|                  | ProjectRQuotaPost         | /mid/billing/projectdekagpu/quota/:project_id                    | Not tested                                     | -        |
|                  | ProjectRQuotaPre          | /mid/billing/projectflavorgpu/project/:project_id                | Not tested                                     | -        |
| **Balance & Billing** | BalanceDetail         | /core/balance/accumulated/:project_id                            | Success (all balances 0)                       | ✅        |
|                  | PaymentHistory            | /core/payment/history                                            | Not tested                                     | -        |
|                  | BillingDailyCost          | /core/billing/v2/daily-cost/:project_id                          | Not tested                                     | -        |
|                  | BillingMonthlyCostTotalBilled | /core/billing/monthly-cost/total-billed/:project_id           | Not tested                                     | -        |
|                  | BillingHistoryDetail      | /core/billing/v2/history                                         | Success (empty)                                | ✅        |
|                  | BillingInvoiceEnterprise  | /core/billing/invoice/:project_id                                | Success (empty)                                | ✅        |
| **VM**           | GetVm                     | /core/virtual-machine/list/all                                   | 400 Bad Request (Python client/tool), CLI works| ❌/✅     |
|                  | VmDetail                  | /core/virtual-machine/detail-vm                                  | Not tested (no VM ID)                          | -        |
|                  | CreateVm                  | /core/virtual-machine                                            | Not tested                                     | -        |
|                  | DeleteVm                  | /core/virtual-machine/delete                                     | Not tested                                     | -        |
| **Organization** | OrgDetail                 | /core/user/organization                                          | Success                                        | ✅        |
|                  | OrgMemberList             | /core/user/organization/member                                   | Success (1 member: you)                        | ✅        |
|                  | OrgRoleList               | /core/user/organization/role                                     | Success (Owner, Member)                        | ✅        |
|                  | OrgMemberAdd/Edit/Delete  | /core/user/organization/member                                   | 400 Bad Request or restricted                  | ❌        |
|                  | OrgMemberActivate         | /core/user/manageuser/active/:user_id                            | Success                                        | ✅        |
|                  | OrgMemberDeactivate       | /core/user/manageuser/deactive/:user_id                          | No result (restricted)                         | ❌        |
|                  | OrgMemberResendInvitation | /core/superadmin/manageuser/resend-verified/:user_id             | 400 Bad Request                                | ❌        |
| **Kubernetes**   | KubeDashboard             | /core/user/projects/:project_id/vcluster/dashboard               | API Error                                      | ❌        |
|                  | Kubeconfig                | /core/user/projects/:project_id/vcluster/kubeconfig              | 400 Bad Request                                | ❌        |
|                  | GetPod                    | /core/pods                                                       | Success (1 pod: coredns)                       | ✅        |
|                  | GetDeployment             | /core/deployment                                                 | Success (1 deployment: coredns)                | ✅        |
|                  | GetService                | /core/kubernetes/services                                        | Success (3 services)                           | ✅        |
|                  | GetNamespace              | /core/user/projects/:project_id/vcluster/namespaces              | Success (3 namespaces)                         | ✅        |
|                  | GetConfigMap              | /core/kubernetes/configmaps                                      | Success (multiple configmaps)                  | ✅        |
|                  | GetSecret                 | /core/kubernetes/secrets                                         | Success (1 secret)                             | ✅        |
| **Registry**     | RegistryList              | /core/dekaregistry/v2/registry                                   | 400 Bad Request (no registry)                  | ❌        |
|                  | RegistryDetail/Overview   | /core/dekaregistry/v2/registry/:registry_id                      | 400 Bad Request (invalid registry ID)          | ❌        |
|                  | RegistryMemberList/Add    | /core/dekaregistry/v2/member/:registry_id                        | 400 Bad Request (invalid registry ID)          | ❌        |
| **Notebook**     | NotebookList              | /core/deka-notebook                                              | Success (empty)                                | ✅        |
|                  | NotebookCreate            | /core/deka-notebook                                              | 400 Bad Request (invalid image/spec)           | ❌        |
| **Voucher**      | VoucherClaimedList        | /core/user/voucher-credit/claimed                                | Success (empty)                                | ✅        |
|                  | VoucherTrialClaimedList   | /core/user/voucher/claimed                                       | Success (empty)                                | ✅        |
|                  | VoucherClaim              | /core/user/voucher-credit/claim                                  | Requires claim data                            | ❌        |
| **Audit**        | AuditLog                  | /core/api/v1.1/user/activity/sp/get-auditlog                     | 404 Not Found                                  | ❌        |
| **Superadmin**   | SuperadminBalanceDetail   | /core/superadmin/balance/accumulated/:organization_id/:project_id| Success (all balances 0)                       | ✅        |
|                  | SuperadminBillingInvoiceEnterprise | /core/superadmin/invoice/:organization_id/:project_id     | Success (empty)                                | ✅        |
|                  | SuperadminProjectDetail   | /core/user/project/detail/:project_id                            | Success                                        | ✅        |
