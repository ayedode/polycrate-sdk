from typing import Literal

PatchedIdentityProviderRequestProvider = Literal[
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

PATCHED_IDENTITY_PROVIDER_REQUEST_PROVIDER_VALUES: set[PatchedIdentityProviderRequestProvider] = {
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


def check_patched_identity_provider_request_provider(value: str) -> PatchedIdentityProviderRequestProvider:
    if value in PATCHED_IDENTITY_PROVIDER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_IDENTITY_PROVIDER_REQUEST_PROVIDER_VALUES!r}"
    )
