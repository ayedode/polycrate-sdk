from typing import Literal

PatchedOrganizationRequestProvider = Literal[
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

PATCHED_ORGANIZATION_REQUEST_PROVIDER_VALUES: set[PatchedOrganizationRequestProvider] = {
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


def check_patched_organization_request_provider(value: str) -> PatchedOrganizationRequestProvider:
    if value in PATCHED_ORGANIZATION_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_REQUEST_PROVIDER_VALUES!r}")
