from typing import Literal

ExternalCredentialKind = Literal[
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

EXTERNAL_CREDENTIAL_KIND_VALUES: set[ExternalCredentialKind] = {
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


def check_external_credential_kind(value: str) -> ExternalCredentialKind:
    if value in EXTERNAL_CREDENTIAL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXTERNAL_CREDENTIAL_KIND_VALUES!r}")
