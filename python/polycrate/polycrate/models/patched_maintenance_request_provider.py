from typing import Literal

PatchedMaintenanceRequestProvider = Literal[
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

PATCHED_MAINTENANCE_REQUEST_PROVIDER_VALUES: set[PatchedMaintenanceRequestProvider] = {
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


def check_patched_maintenance_request_provider(value: str) -> PatchedMaintenanceRequestProvider:
    if value in PATCHED_MAINTENANCE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_REQUEST_PROVIDER_VALUES!r}")
