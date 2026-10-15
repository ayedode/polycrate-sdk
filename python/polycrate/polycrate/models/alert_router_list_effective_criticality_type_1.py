from typing import Literal

AlertRouterListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AlertRouterListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_alert_router_list_effective_criticality_type_1(value: str) -> AlertRouterListEffectiveCriticalityType1:
    if value in ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
