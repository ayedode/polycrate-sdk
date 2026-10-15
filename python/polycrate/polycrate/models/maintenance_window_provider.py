from typing import Literal

MaintenanceWindowProvider = Literal[
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

MAINTENANCE_WINDOW_PROVIDER_VALUES: set[MaintenanceWindowProvider] = {
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


def check_maintenance_window_provider(value: str) -> MaintenanceWindowProvider:
    if value in MAINTENANCE_WINDOW_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_PROVIDER_VALUES!r}")
