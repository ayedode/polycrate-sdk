from typing import Literal

AlertRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ALERT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_request_criticality_type_2_type_1(value: str) -> AlertRequestCriticalityType2Type1:
    if value in ALERT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
