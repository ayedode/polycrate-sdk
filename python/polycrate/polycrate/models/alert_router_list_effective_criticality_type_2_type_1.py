from typing import Literal

AlertRouterListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertRouterListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_alert_router_list_effective_criticality_type_2_type_1(
    value: str,
) -> AlertRouterListEffectiveCriticalityType2Type1:
    if value in ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
