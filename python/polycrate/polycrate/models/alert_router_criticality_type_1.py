from typing import Literal

AlertRouterCriticalityType1 = Literal["", "high", "low", "medium"]

ALERT_ROUTER_CRITICALITY_TYPE_1_VALUES: set[AlertRouterCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_router_criticality_type_1(value: str) -> AlertRouterCriticalityType1:
    if value in ALERT_ROUTER_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_CRITICALITY_TYPE_1_VALUES!r}")
