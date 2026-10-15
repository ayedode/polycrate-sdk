from typing import Literal

GrafanaDashboardState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

GRAFANA_DASHBOARD_STATE_VALUES: set[GrafanaDashboardState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_grafana_dashboard_state(value: str) -> GrafanaDashboardState:
    if value in GRAFANA_DASHBOARD_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_STATE_VALUES!r}")
