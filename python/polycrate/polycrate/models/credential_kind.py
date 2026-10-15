from typing import Literal

CredentialKind = Literal[
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

CREDENTIAL_KIND_VALUES: set[CredentialKind] = {
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


def check_credential_kind(value: str) -> CredentialKind:
    if value in CREDENTIAL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_KIND_VALUES!r}")
