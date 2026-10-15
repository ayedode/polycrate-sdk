from typing import Literal

GrafanaDashboardListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

GRAFANA_DASHBOARD_LIST_STATE_VALUES: set[GrafanaDashboardListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_grafana_dashboard_list_state(value: str) -> GrafanaDashboardListState:
    if value in GRAFANA_DASHBOARD_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_LIST_STATE_VALUES!r}")
