from typing import Literal

GrafanaDashboardCriticalityType1 = Literal["high", "low", "medium"]

GRAFANA_DASHBOARD_CRITICALITY_TYPE_1_VALUES: set[GrafanaDashboardCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_grafana_dashboard_criticality_type_1(value: str) -> GrafanaDashboardCriticalityType1:
    if value in GRAFANA_DASHBOARD_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_CRITICALITY_TYPE_1_VALUES!r}")
