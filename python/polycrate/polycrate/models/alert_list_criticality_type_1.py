from typing import Literal

AlertListCriticalityType1 = Literal["high", "low", "medium"]

ALERT_LIST_CRITICALITY_TYPE_1_VALUES: set[AlertListCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_alert_list_criticality_type_1(value: str) -> AlertListCriticalityType1:
    if value in ALERT_LIST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LIST_CRITICALITY_TYPE_1_VALUES!r}")
