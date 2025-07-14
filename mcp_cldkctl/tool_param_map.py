TOOL_PARAM_MAP = {
    # --- Authentication ---
    "mcp_cldkctl_cldkctl_auth": {
        "endpoint": "/core/cldkctl/auth",
        "method": "POST",
        "required_params": [
            {"name": "token", "type": "string", "desc": "Your cldkctl token (starts with 'cldkctl_')"},
        ],
        "optional_params": [
            {"name": "force_staging", "type": "boolean", "desc": "Force using staging environment (default: false)"},
        ],
    },
    # --- Auth & Profile ---
    "mcp_cldkctl_cldkctl_login": {
        "endpoint": "/core/user/login",
        "method": "POST",
        "required_params": [
            {"name": "username", "type": "string", "desc": "User's login name"},
            {"name": "password", "type": "string", "desc": "User's password"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_profile_detail": {
        "endpoint": "/core/user/profile",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_update_profile": {
        "endpoint": "/core/user/organization/profile/member/:user_id",
        "method": "PUT",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "ID of the user to update"},
            {"name": "name", "type": "string", "desc": "Full name"},
            {"name": "email", "type": "string", "desc": "Email address"},
            {"name": "phone_number", "type": "string", "desc": "Phone number"},
            {"name": "address", "type": "string", "desc": "Address"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_change_password": {
        "endpoint": "/core/user/change-password",
        "method": "POST",
        "required_params": [
            {"name": "old_password", "type": "string", "desc": "Current password"},
            {"name": "new_password", "type": "string", "desc": "New password"},
        ],
        "optional_params": [],
    },
    # --- Project Management ---
    "mcp_cldkctl_cldkctl_project_list": {
        "endpoint": "/core/user/organization/projects/byOrg",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_project_detail": {
        "endpoint": "/core/user/project/detail/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_update_project": {
        "endpoint": "/core/user/projects/:project_id",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
            {"name": "description", "type": "string", "desc": "New project description"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_check_before_delete_project": {
        "endpoint": "/core/user/checking/projects/:project_id",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_project": {
        "endpoint": "/core/user/projects/:project_id",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    # --- Balance & Billing ---
    "mcp_cldkctl_cldkctl_balance_detail": {
        "endpoint": "/core/balance/accumulated/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_payment_history": {
        "endpoint": "/core/payment/history",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_daily_cost": {
        "endpoint": "/core/billing/v2/daily-cost/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_monthly_cost": {
        "endpoint": "/core/billing/monthly-cost/total-billed/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_history": {
        "endpoint": "/core/billing/monthly-cost/history",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
            {"name": "start", "type": "string", "desc": "Start date (YYYY-MM-DD)"},
            {"name": "end", "type": "string", "desc": "End date (YYYY-MM-DD)"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_invoice_sme": {
        "endpoint": "/core/balance/history/invoice",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_invoice_sme_detail": {
        "endpoint": "/core/balance/history/invoice/detail/:invoice_id",
        "method": "GET",
        "required_params": [
            {"name": "invoice_id", "type": "string", "desc": "ID of the invoice"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_invoice_enterprise": {
        "endpoint": "/core/billing/invoice/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "ID of the project"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_billing_invoice_enterprise_detail": {
        "endpoint": "/core/billing/v2/invoice/detail/:invoice_id",
        "method": "GET",
        "required_params": [
            {"name": "invoice_id", "type": "string", "desc": "ID of the invoice"},
        ],
        "optional_params": [],
    },
    # --- Organization & Members ---
    "mcp_cldkctl_cldkctl_org_detail": {
        "endpoint": "/core/user/organization",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_members": {
        "endpoint": "/core/user/organization/member",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_add": {
        "endpoint": "/core/user/organization/member",
        "method": "POST",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "ID of the user to add"},
            {"name": "role_id", "type": "string", "desc": "Role ID to assign"},
            {"name": "project_id", "type": "string", "desc": "Project ID to assign"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_edit": {
        "endpoint": "/core/user/organization/member/:user_id",
        "method": "PUT",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "ID of the user to edit"},
            {"name": "role_id", "type": "string", "desc": "Role ID to assign"},
            {"name": "project_id", "type": "string", "desc": "Project ID to assign"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_delete": {
        "endpoint": "/core/user/organization/member/:user_id",
        "method": "DELETE",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "ID of the user to delete"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_list": {
        "endpoint": "/core/user/organization/role",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_add": {
        "endpoint": "/core/user/organization/role",
        "method": "POST",
        "required_params": [
            {"name": "name", "type": "string", "desc": "Role name"},
            {"name": "privileges", "type": "list", "desc": "List of privileges"},
        ],
        "optional_params": [],
    },
    # --- Kubernetes ---
    "mcp_cldkctl_cldkctl_k8s_pods": {
        "endpoint": "/core/pods",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_deployments": {
        "endpoint": "/core/deployment",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_services": {
        "endpoint": "/core/kubernetes/services",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_configmaps": {
        "endpoint": "/core/kubernetes/configmap",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_secrets": {
        "endpoint": "/core/kubernetes/secret",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    # --- VM Management ---
    "mcp_cldkctl_cldkctl_vm_list": {
        "endpoint": "/core/virtual-machine/list/all",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "limit", "type": "string", "desc": "Limit (use -1 for all)"}
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_vm_detail": {
        "endpoint": "/core/virtual-machine/detail-vm",
        "method": "POST",
        "required_params": [
            {"name": "vm_id", "type": "string", "desc": "ID of the VM"},
        ],
        "optional_params": [],
    },
    # --- Registry ---
    "mcp_cldkctl_cldkctl_registry_list": {
        "endpoint": "/core/dekaregistry/v2/registry",
        "method": "GET",
        "required_params": [],
        "optional_params": [
            {"name": "project-id", "type": "string", "desc": "Project ID (hyphenated, as required by backend)"},
            {"name": "page", "type": "string", "desc": "Page number (default 1)"}
        ],
    },
    "mcp_cldkctl_cldkctl_registry_repositories": {
        "endpoint": "/core/dekaregistry/v2/repository",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    # --- Notebook ---
    "mcp_cldkctl_cldkctl_notebook_list": {
        "endpoint": "/core/deka-notebook",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_notebook_create": {
        "endpoint": "/core/deka-notebook",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Notebook name"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "image", "type": "string", "desc": "Image ID"},
            {"name": "cpu", "type": "string", "desc": "CPU amount"},
            {"name": "memory", "type": "string", "desc": "Memory size"},
            {"name": "storage", "type": "string", "desc": "Storage size"},
        ],
        "optional_params": [
            {"name": "gpu", "type": "string", "desc": "GPU amount (optional)"},
        ],
    },
    # --- More Kubernetes ---
    "mcp_cldkctl_cldkctl_k8s_pod_create": {
        "endpoint": "/core/pods",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "spec", "type": "dict", "desc": "Pod spec (YAML/JSON)"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_pod_edit": {
        "endpoint": "/core/pods/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Pod name"},
            {"name": "spec", "type": "dict", "desc": "Pod spec (YAML/JSON)"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_k8s_pod_delete": {
        "endpoint": "/core/pods/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Pod name"},
        ],
        "optional_params": [],
    },
    # --- More VM Management ---
    "mcp_cldkctl_cldkctl_vm_create": {
        "endpoint": "/core/virtual-machine",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "VM name"},
            {"name": "flavor", "type": "string", "desc": "Flavor ID"},
            {"name": "image", "type": "string", "desc": "Image ID"},
            {"name": "network", "type": "string", "desc": "Network ID"},
            {"name": "storage", "type": "string", "desc": "Storage size"},
        ],
        "optional_params": [
            {"name": "gpu", "type": "string", "desc": "GPU type (optional)"},
        ],
    },
    "mcp_cldkctl_cldkctl_vm_delete": {
        "endpoint": "/core/virtual-machine/delete",
        "method": "POST",
        "required_params": [
            {"name": "vm_id", "type": "string", "desc": "ID of the VM to delete"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_vm_reboot": {
        "endpoint": "/core/virtual-machine/reboot",
        "method": "POST",
        "required_params": [
            {"name": "vm_id", "type": "string", "desc": "ID of the VM to reboot"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_vm_turn_on": {
        "endpoint": "/core/virtual-machine/turn-on/vm",
        "method": "POST",
        "required_params": [
            {"name": "vm_id", "type": "string", "desc": "ID of the VM to turn on"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_vm_turn_off": {
        "endpoint": "/core/virtual-machine/turn-off/vm",
        "method": "POST",
        "required_params": [
            {"name": "vm_id", "type": "string", "desc": "ID of the VM to turn off"},
        ],
        "optional_params": [],
    },
    # --- More Registry ---
    "mcp_cldkctl_cldkctl_registry_detail": {
        "endpoint": "/core/dekaregistry/v2/registry/:registry_id",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_overview": {
        "endpoint": "/core/dekaregistry/v2/registry/:registry_id/overview",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_member_list": {
        "endpoint": "/core/dekaregistry/v2/member/:registry_id",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_member_add": {
        "endpoint": "/core/dekaregistry/v2/member/:registry_id",
        "method": "POST",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "user_id", "type": "string", "desc": "User ID to add"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_member_delete": {
        "endpoint": "/core/dekaregistry/v2/member/:registry_id/detail/:member_id",
        "method": "DELETE",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "member_id", "type": "string", "desc": "Member ID to delete"},
        ],
        "optional_params": [],
    },
    # --- More Notebook ---
    "mcp_cldkctl_cldkctl_notebook_delete": {
        "endpoint": "/core/deka-notebook/delete",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Notebook name"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_notebook_update": {
        "endpoint": "/core/deka-notebook/yaml",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Notebook name"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "yaml", "type": "string", "desc": "Notebook YAML"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_notebook_start": {
        "endpoint": "/core/deka-notebook/start",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Notebook name"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_notebook_stop": {
        "endpoint": "/core/deka-notebook/stop",
        "method": "POST",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Notebook name"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
        ],
        "optional_params": [],
    },
    # --- More Billing/Quota ---
    "mcp_cldkctl_cldkctl_project_r_quota_post": {
        "endpoint": "/mid/billing/projectdekagpu/quota/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_project_r_quota_pre": {
        "endpoint": "/mid/billing/projectflavorgpu/project/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    # --- More Token Management ---
    "mcp_cldkctl_cldkctl_token_update": {
        "endpoint": "/core/cldkctl/token/:token_id",
        "method": "PUT",
        "required_params": [
            {"name": "token_id", "type": "string", "desc": "Token ID to update"},
            {"name": "name", "type": "string", "desc": "New token name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_token_regenerate": {
        "endpoint": "/core/cldkctl/token/regenerate/:token_id",
        "method": "POST",
        "required_params": [
            {"name": "token_id", "type": "string", "desc": "Token ID to regenerate"},
            {"name": "expiration_days", "type": "integer", "desc": "Expiration in days"},
        ],
        "optional_params": [],
    },
    # --- Miscellaneous ---
    "mcp_cldkctl_cldkctl_kube_dashboard": {
        "endpoint": "/core/user/projects/:project_id/vcluster/dashboard",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_kubeconfig": {
        "endpoint": "/core/user/projects/:project_id/vcluster/kubeconfig",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_namespace": {
        "endpoint": "/core/user/projects/:project_id/vcluster/namespaces",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    # --- Missing tools from endpoint map ---
    "mcp_cldkctl_cldkctl_org_edit": {
        "endpoint": "/core/user/organization/edit/:organization_id",
        "method": "PUT",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "org_data", "type": "object", "desc": "Organization data to update"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_activate": {
        "endpoint": "/core/user/manageuser/active/:user_id",
        "method": "PUT",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "User ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_deactivate": {
        "endpoint": "/core/user/manageuser/deactive/:user_id",
        "method": "PUT",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "User ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_member_resend_invitation": {
        "endpoint": "/core/superadmin/manageuser/resend-verified/:user_id",
        "method": "POST",
        "required_params": [
            {"name": "user_id", "type": "string", "desc": "User ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_voucher_claim": {
        "endpoint": "/core/user/voucher-credit/claim",
        "method": "POST",
        "required_params": [
            {"name": "claim_data", "type": "object", "desc": "Claim data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_voucher_claimed_list": {
        "endpoint": "/core/user/voucher-credit/claimed",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_voucher_trial_claimed_list": {
        "endpoint": "/core/user/voucher/claimed",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_audit_log": {
        "endpoint": "/core/api/v1.1/user/activity/sp/get-auditlog",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_detail": {
        "endpoint": "/core/user/organization/role/:role_id",
        "method": "GET",
        "required_params": [
            {"name": "role_id", "type": "string", "desc": "Role ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_edit": {
        "endpoint": "/core/user/organization/role/:role_id",
        "method": "PUT",
        "required_params": [
            {"name": "role_id", "type": "string", "desc": "Role ID"},
            {"name": "role_data", "type": "object", "desc": "Role data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_delete": {
        "endpoint": "/core/user/organization/role/:role_id",
        "method": "DELETE",
        "required_params": [
            {"name": "role_id", "type": "string", "desc": "Role ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_org_role_add": {
        "endpoint": "/core/user/organization/role",
        "method": "POST",
        "required_params": [
            {"name": "role_data", "type": "object", "desc": "Role data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_kube_dashboard": {
        "endpoint": "/core/user/projects/:project_id/vcluster/dashboard",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_kubeconfig": {
        "endpoint": "/core/user/projects/:project_id/vcluster/kubeconfig",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    # --- More missing tools from endpoint map ---
    "mcp_cldkctl_cldkctl_get_pod": {
        "endpoint": "/core/pods",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_pod": {
        "endpoint": "/core/pods",
        "method": "POST",
        "required_params": [
            {"name": "pod_data", "type": "object", "desc": "Pod data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_pod": {
        "endpoint": "/core/pods/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Pod name"},
            {"name": "pod_data", "type": "object", "desc": "Pod data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_pod": {
        "endpoint": "/core/pods/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Pod name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_console_pod": {
        "endpoint": "/core/pods/console/:token",
        "method": "GET",
        "required_params": [
            {"name": "token", "type": "string", "desc": "Console token"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_console_token_pod": {
        "endpoint": "/core/pods/console",
        "method": "POST",
        "required_params": [
            {"name": "console_data", "type": "object", "desc": "Console data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_deployment": {
        "endpoint": "/core/deployment",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_deployment": {
        "endpoint": "/core/deployment",
        "method": "POST",
        "required_params": [
            {"name": "deployment_data", "type": "object", "desc": "Deployment data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_deployment": {
        "endpoint": "/core/deployment/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Deployment name"},
            {"name": "deployment_data", "type": "object", "desc": "Deployment data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_deployment": {
        "endpoint": "/core/deployment/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Deployment name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_daemonset": {
        "endpoint": "/core/daemonset",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_daemonset": {
        "endpoint": "/core/daemonset",
        "method": "POST",
        "required_params": [
            {"name": "daemonset_data", "type": "object", "desc": "DaemonSet data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_daemonset": {
        "endpoint": "/core/daemonset/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "DaemonSet name"},
            {"name": "daemonset_data", "type": "object", "desc": "DaemonSet data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_daemonset": {
        "endpoint": "/core/daemonset/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "DaemonSet name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_statefulset": {
        "endpoint": "/core/statefulsets",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_statefulset": {
        "endpoint": "/core/statefulsets",
        "method": "POST",
        "required_params": [
            {"name": "statefulset_data", "type": "object", "desc": "StatefulSet data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_statefulset": {
        "endpoint": "/core/statefulsets/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "StatefulSet name"},
            {"name": "statefulset_data", "type": "object", "desc": "StatefulSet data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_statefulset": {
        "endpoint": "/core/statefulsets/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "StatefulSet name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_service": {
        "endpoint": "/core/kubernetes/services",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_service": {
        "endpoint": "/core/kubernetes/services",
        "method": "POST",
        "required_params": [
            {"name": "service_data", "type": "object", "desc": "Service data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_service": {
        "endpoint": "/core/kubernetes/services/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Service name"},
            {"name": "service_data", "type": "object", "desc": "Service data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_service": {
        "endpoint": "/core/kubernetes/services/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Service name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_persistent_volume": {
        "endpoint": "/core/kubernetes/pv",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_persistent_volume": {
        "endpoint": "/core/kubernetes/pv",
        "method": "POST",
        "required_params": [
            {"name": "pv_data", "type": "object", "desc": "Persistent Volume data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_persistent_volume": {
        "endpoint": "/core/kubernetes/pv/:project_id/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Persistent Volume name"},
            {"name": "pv_data", "type": "object", "desc": "Persistent Volume data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_persistent_volume": {
        "endpoint": "/core/kubernetes/pv/:project_id/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "Persistent Volume name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_pvc": {
        "endpoint": "/core/kubernetes/pvc",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_pvc": {
        "endpoint": "/core/kubernetes/pvc",
        "method": "POST",
        "required_params": [
            {"name": "pvc_data", "type": "object", "desc": "Persistent Volume Claim data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_pvc": {
        "endpoint": "/core/kubernetes/pvc/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "PVC name"},
            {"name": "pvc_data", "type": "object", "desc": "Persistent Volume Claim data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_pvc": {
        "endpoint": "/core/kubernetes/pvc/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "PVC name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_data_volume": {
        "endpoint": "/core/datavolume",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_data_volume": {
        "endpoint": "/core/datavolume",
        "method": "POST",
        "required_params": [
            {"name": "datavolume_data", "type": "object", "desc": "Data Volume data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_data_volume": {
        "endpoint": "/core/datavolume/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Data Volume name"},
            {"name": "datavolume_data", "type": "object", "desc": "Data Volume data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_data_volume": {
        "endpoint": "/core/datavolume/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Data Volume name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_resource_v1": {
        "endpoint": "/core/kubernetes/:resource",
        "method": "GET",
        "required_params": [
            {"name": "resource", "type": "string", "desc": "Kubernetes resource type"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_resource_v1": {
        "endpoint": "/core/kubernetes/:resource",
        "method": "POST",
        "required_params": [
            {"name": "resource", "type": "string", "desc": "Kubernetes resource type"},
            {"name": "resource_data", "type": "object", "desc": "Resource data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_resource_v1": {
        "endpoint": "/core/kubernetes/:resource/:project_id/:namespace/:name",
        "method": "PATCH",
        "required_params": [
            {"name": "resource", "type": "string", "desc": "Kubernetes resource type"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Resource name"},
            {"name": "resource_data", "type": "object", "desc": "Resource data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_resource_v1": {
        "endpoint": "/core/kubernetes/:resource/:project_id/:namespace/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "resource", "type": "string", "desc": "Kubernetes resource type"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "Resource name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_custom_resources": {
        "endpoint": "/core/kubernetes/apiresources/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_crd": {
        "endpoint": "/core/kubernetes/resource/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_crd": {
        "endpoint": "/core/kubernetes/resource",
        "method": "POST",
        "required_params": [
            {"name": "crd_data", "type": "object", "desc": "CRD data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_crd": {
        "endpoint": "/core/kubernetes/resource/:project_id/:name",
        "method": "PATCH",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "CRD name"},
            {"name": "crd_data", "type": "object", "desc": "CRD data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_crd": {
        "endpoint": "/core/kubernetes/resource/:project_id/:name",
        "method": "DELETE",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "name", "type": "string", "desc": "CRD name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_image_os": {
        "endpoint": "/core/cluster-image-os",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_vm_flavor_type": {
        "endpoint": "/core/virtual-machine/flavor_type",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_vm_gpu": {
        "endpoint": "/core/virtual-machine/gpu/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_vm_storage_class": {
        "endpoint": "/core/virtual-machine/storage-class/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_vm_flavor": {
        "endpoint": "/core/virtual-machine/flavor/:flavorType_id",
        "method": "GET",
        "required_params": [
            {"name": "flavorType_id", "type": "string", "desc": "Flavor Type ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_vm": {
        "endpoint": "/core/virtual-machine",
        "method": "POST",
        "required_params": [
            {"name": "vm_data", "type": "object", "desc": "VM data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_create_vm_yaml": {
        "endpoint": "/core/virtual-machine/yaml",
        "method": "POST",
        "required_params": [
            {"name": "vm_yaml_data", "type": "object", "desc": "VM YAML data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_get_vm": {
        "endpoint": "/core/virtual-machine/list/all",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_edit_vm_yaml": {
        "endpoint": "/core/virtual-machine/yaml/:project_id/:namespace/:name",
        "method": "PUT",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "namespace", "type": "string", "desc": "Namespace"},
            {"name": "name", "type": "string", "desc": "VM name"},
            {"name": "vm_yaml_data", "type": "object", "desc": "VM YAML data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_delete_vm": {
        "endpoint": "/core/virtual-machine/delete",
        "method": "POST",
        "required_params": [
            {"name": "vm_delete_data", "type": "object", "desc": "VM delete data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_reboot_vm": {
        "endpoint": "/core/virtual-machine/reboot",
        "method": "POST",
        "required_params": [
            {"name": "vm_reboot_data", "type": "object", "desc": "VM reboot data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_turn_off_vm": {
        "endpoint": "/core/virtual-machine/turn-off/vm",
        "method": "POST",
        "required_params": [
            {"name": "vm_turn_off_data", "type": "object", "desc": "VM turn off data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_turn_on_vm": {
        "endpoint": "/core/virtual-machine/turn-on/vm",
        "method": "POST",
        "required_params": [
            {"name": "vm_turn_on_data", "type": "object", "desc": "VM turn on data"},
        ],
        "optional_params": [],
    },
    # --- Final batch of missing tools from endpoint map ---
    "mcp_cldkctl_cldkctl_registry_quota": {
        "endpoint": "/core/dekaregistry/v2/project/quota/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_cert": {
        "endpoint": "/core/dekaregistry/v1/registry/downloadcrt",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_create": {
        "endpoint": "/core/dekaregistry/v2/registry",
        "method": "POST",
        "required_params": [
            {"name": "registry_data", "type": "object", "desc": "Registry data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_update": {
        "endpoint": "/core/dekaregistry/v2/registry/:registry_id",
        "method": "PUT",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "registry_data", "type": "object", "desc": "Registry data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_logs": {
        "endpoint": "/core/dekaregistry/v2/registry/:registry_id/logs",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_labels": {
        "endpoint": "/core/dekaregistry/v1/registry/lislabels/:organization_id/:user_id/:project_id/:registry_id",
        "method": "GET",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "user_id", "type": "string", "desc": "User ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_labels_update": {
        "endpoint": "/core/dekaregistry/v1/registry/updatelabels/:organization_id/:user_id/:project_id/:registry_id",
        "method": "PUT",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "user_id", "type": "string", "desc": "User ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "labels_data", "type": "object", "desc": "Labels data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_labels_create": {
        "endpoint": "/core/dekaregistry/v1/registry/createlabels/:organization_id/:user_id/:project_id/:registry_id",
        "method": "POST",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "user_id", "type": "string", "desc": "User ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "labels_data", "type": "object", "desc": "Labels data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_labels_delete": {
        "endpoint": "/core/dekaregistry/v1/registry/deletelabels/:organization_id/:user_id/:project_id/:labels_id/:registry_id",
        "method": "DELETE",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "user_id", "type": "string", "desc": "User ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
            {"name": "labels_id", "type": "string", "desc": "Labels ID"},
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_list": {
        "endpoint": "/core/dekaregistry/v2/tag/:registry_id",
        "method": "GET",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_create": {
        "endpoint": "/core/dekaregistry/v2/tag/:registry_id",
        "method": "POST",
        "required_params": [
            {"name": "registry_id", "type": "string", "desc": "Registry ID"},
            {"name": "tag_data", "type": "object", "desc": "Tag data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_update": {
        "endpoint": "/core/dekaregistry/v2/tag/detail/:tag_id",
        "method": "PUT",
        "required_params": [
            {"name": "tag_id", "type": "string", "desc": "Tag ID"},
            {"name": "tag_data", "type": "object", "desc": "Tag data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_delete": {
        "endpoint": "/core/dekaregistry/v2/tag/detail/:tag_id",
        "method": "DELETE",
        "required_params": [
            {"name": "tag_id", "type": "string", "desc": "Tag ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_disable": {
        "endpoint": "/core/dekaregistry/v2/tag/detail/:tag_id/disable",
        "method": "POST",
        "required_params": [
            {"name": "tag_id", "type": "string", "desc": "Tag ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_tag_enable": {
        "endpoint": "/core/dekaregistry/v2/tag/detail/:tag_id/enable",
        "method": "POST",
        "required_params": [
            {"name": "tag_id", "type": "string", "desc": "Tag ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_available_member": {
        "endpoint": "/core/dekaregistry/v2/project/member/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_show_password": {
        "endpoint": "/core/dekaregistry/v2/user/password/show",
        "method": "POST",
        "required_params": [
            {"name": "password_data", "type": "object", "desc": "Password data"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_repository_list": {
        "endpoint": "/core/dekaregistry/v2/repository",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_detail": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id",
        "method": "GET",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_add_label": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/assign-label/:label_id",
        "method": "PATCH",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
            {"name": "label_id", "type": "string", "desc": "Label ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_remove_label": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/unassign-label/:label_id",
        "method": "PATCH",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
            {"name": "label_id", "type": "string", "desc": "Label ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_scan": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/scan",
        "method": "POST",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_stop_scan": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/stop-scan",
        "method": "POST",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_tags": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/tag",
        "method": "GET",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_delete_tag": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/tag/:tag",
        "method": "DELETE",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
            {"name": "tag", "type": "string", "desc": "Tag name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_registry_artifact_add_tag": {
        "endpoint": "/core/dekaregistry/v2/artifact/:artifact_id/tag/:tag",
        "method": "POST",
        "required_params": [
            {"name": "artifact_id", "type": "string", "desc": "Artifact ID"},
            {"name": "tag", "type": "string", "desc": "Tag name"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_notebook_images": {
        "endpoint": "/core/deka-notebook/images",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_superadmin_project_list": {
        "endpoint": "/core/superadmin/list/manageorgproject",
        "method": "GET",
        "required_params": [],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_superadmin_org_detail": {
        "endpoint": "/core/superadmin/manageorg/:organization_id",
        "method": "GET",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_superadmin_balance_detail": {
        "endpoint": "/core/superadmin/balance/accumulated/:organization_id/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_superadmin_billing_invoice_sme": {
        "endpoint": "/core/superadmin/balance/history/invoice/:organization_id",
        "method": "GET",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
        ],
        "optional_params": [],
    },
    "mcp_cldkctl_cldkctl_superadmin_billing_invoice_enterprise": {
        "endpoint": "/core/superadmin/invoice/:organization_id/:project_id",
        "method": "GET",
        "required_params": [
            {"name": "organization_id", "type": "string", "desc": "Organization ID"},
            {"name": "project_id", "type": "string", "desc": "Project ID"},
        ],
        "optional_params": [],
    },
} 