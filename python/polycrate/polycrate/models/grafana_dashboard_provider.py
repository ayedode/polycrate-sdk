from typing import Literal

GrafanaDashboardProvider = Literal[
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

GRAFANA_DASHBOARD_PROVIDER_VALUES: set[GrafanaDashboardProvider] = {
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


def check_grafana_dashboard_provider(value: str) -> GrafanaDashboardProvider:
    if value in GRAFANA_DASHBOARD_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_PROVIDER_VALUES!r}")
