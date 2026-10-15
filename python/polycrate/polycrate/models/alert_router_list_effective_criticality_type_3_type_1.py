from typing import Literal

AlertRouterListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AlertRouterListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_alert_router_list_effective_criticality_type_3_type_1(
    value: str,
) -> AlertRouterListEffectiveCriticalityType3Type1:
    if value in ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
