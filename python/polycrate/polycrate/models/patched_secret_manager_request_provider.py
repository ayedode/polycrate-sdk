from typing import Literal

PatchedSecretManagerRequestProvider = Literal[
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

PATCHED_SECRET_MANAGER_REQUEST_PROVIDER_VALUES: set[PatchedSecretManagerRequestProvider] = {
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


def check_patched_secret_manager_request_provider(value: str) -> PatchedSecretManagerRequestProvider:
    if value in PATCHED_SECRET_MANAGER_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_SECRET_MANAGER_REQUEST_PROVIDER_VALUES!r}")
