from typing import Literal

ApiV1CredentialsListKindItem = Literal[
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

API_V1_CREDENTIALS_LIST_KIND_ITEM_VALUES: set[ApiV1CredentialsListKindItem] = {
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


def check_api_v1_credentials_list_kind_item(value: str) -> ApiV1CredentialsListKindItem:
    if value in API_V1_CREDENTIALS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_KIND_ITEM_VALUES!r}")
