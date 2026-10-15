from typing import Literal

IdentityProviderProvider = Literal[
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

IDENTITY_PROVIDER_PROVIDER_VALUES: set[IdentityProviderProvider] = {
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


def check_identity_provider_provider(value: str) -> IdentityProviderProvider:
    if value in IDENTITY_PROVIDER_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDENTITY_PROVIDER_PROVIDER_VALUES!r}")
