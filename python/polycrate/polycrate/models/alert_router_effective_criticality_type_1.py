from typing import Literal

AlertRouterEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ALERT_ROUTER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AlertRouterEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_alert_router_effective_criticality_type_1(value: str) -> AlertRouterEffectiveCriticalityType1:
    if value in ALERT_ROUTER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
