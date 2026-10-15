from typing import Literal

AlertRouterCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ALERT_ROUTER_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertRouterCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_router_criticality_type_2_type_1(value: str) -> AlertRouterCriticalityType2Type1:
    if value in ALERT_ROUTER_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
