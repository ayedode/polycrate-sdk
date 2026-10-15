from typing import Literal

PatchedMaintenanceWindowRequestProvider = Literal[
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

PATCHED_MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES: set[PatchedMaintenanceWindowRequestProvider] = {
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


def check_patched_maintenance_window_request_provider(value: str) -> PatchedMaintenanceWindowRequestProvider:
    if value in PATCHED_MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES!r}"
    )
