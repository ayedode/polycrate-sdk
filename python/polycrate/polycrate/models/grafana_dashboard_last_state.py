from typing import Literal

GrafanaDashboardLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

GRAFANA_DASHBOARD_LAST_STATE_VALUES: set[GrafanaDashboardLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_grafana_dashboard_last_state(value: str) -> GrafanaDashboardLastState:
    if value in GRAFANA_DASHBOARD_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_LAST_STATE_VALUES!r}")
