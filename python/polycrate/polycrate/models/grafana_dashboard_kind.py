from typing import Literal

GrafanaDashboardKind = Literal["generic"]

GRAFANA_DASHBOARD_KIND_VALUES: set[GrafanaDashboardKind] = {
    "generic",
}


def check_grafana_dashboard_kind(value: str) -> GrafanaDashboardKind:
    if value in GRAFANA_DASHBOARD_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_KIND_VALUES!r}")
