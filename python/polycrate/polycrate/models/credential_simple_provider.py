from typing import Literal

CredentialSimpleProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

CREDENTIAL_SIMPLE_PROVIDER_VALUES: set[CredentialSimpleProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_credential_simple_provider(value: str) -> CredentialSimpleProvider:
    if value in CREDENTIAL_SIMPLE_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_SIMPLE_PROVIDER_VALUES!r}")
