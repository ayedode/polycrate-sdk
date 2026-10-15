from typing import Literal

AlertRequestStatusType1 = Literal["", "firing", "pending", "resolved", "silenced"]

ALERT_REQUEST_STATUS_TYPE_1_VALUES: set[AlertRequestStatusType1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_request_status_type_1(value: str) -> AlertRequestStatusType1:
    if value in ALERT_REQUEST_STATUS_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_REQUEST_STATUS_TYPE_1_VALUES!r}")
