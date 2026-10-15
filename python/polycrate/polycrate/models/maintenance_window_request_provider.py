from typing import Literal

MaintenanceWindowRequestProvider = Literal[
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

MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES: set[MaintenanceWindowRequestProvider] = {
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


def check_maintenance_window_request_provider(value: str) -> MaintenanceWindowRequestProvider:
    if value in MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_REQUEST_PROVIDER_VALUES!r}")
