from typing import Literal

GrafanaDashboardListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

GRAFANA_DASHBOARD_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[GrafanaDashboardListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_grafana_dashboard_list_effective_criticality_type_1(
    value: str,
) -> GrafanaDashboardListEffectiveCriticalityType1:
    if value in GRAFANA_DASHBOARD_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GRAFANA_DASHBOARD_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
