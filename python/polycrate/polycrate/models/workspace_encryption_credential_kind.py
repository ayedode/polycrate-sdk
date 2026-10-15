from typing import Literal

WorkspaceEncryptionCredentialKind = Literal[
    "agent_token",
    "api-key",
    "apmstack-logs-credential",
    "apmstack-metrics-credential",
    "apmstack-traces-credential",
    "controlplane-token",
    "dns-provider",
    "domain-auth-code",
    "generic",
    "helm-repository-credential",
    "kubeconfig",
    "oci-registry-credential",
    "org_api_key",
    "provider-account",
    "s3-credential",
    "ssh-keys",
    "system_api_key",
    "unified-apm-credential",
    "unified-registry-credential",
    "webhook",
    "workspace-encryption",
]

WORKSPACE_ENCRYPTION_CREDENTIAL_KIND_VALUES: set[WorkspaceEncryptionCredentialKind] = {
    "agent_token",
    "api-key",
    "apmstack-logs-credential",
    "apmstack-metrics-credential",
    "apmstack-traces-credential",
    "controlplane-token",
    "dns-provider",
    "domain-auth-code",
    "generic",
    "helm-repository-credential",
    "kubeconfig",
    "oci-registry-credential",
    "org_api_key",
    "provider-account",
    "s3-credential",
    "ssh-keys",
    "system_api_key",
    "unified-apm-credential",
    "unified-registry-credential",
    "webhook",
    "workspace-encryption",
}


def check_workspace_encryption_credential_kind(value: str) -> WorkspaceEncryptionCredentialKind:
    if value in WORKSPACE_ENCRYPTION_CREDENTIAL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_ENCRYPTION_CREDENTIAL_KIND_VALUES!r}")
