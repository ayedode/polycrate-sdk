from typing import Literal

AlertRouterCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ALERT_ROUTER_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AlertRouterCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_router_criticality_type_3_type_1(value: str) -> AlertRouterCriticalityType3Type1:
    if value in ALERT_ROUTER_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
