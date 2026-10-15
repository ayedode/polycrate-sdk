from typing import Literal

AlertRequestStatusType3Type1 = Literal["", "firing", "pending", "resolved", "silenced"]

ALERT_REQUEST_STATUS_TYPE_3_TYPE_1_VALUES: set[AlertRequestStatusType3Type1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_request_status_type_3_type_1(value: str) -> AlertRequestStatusType3Type1:
    if value in ALERT_REQUEST_STATUS_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_REQUEST_STATUS_TYPE_3_TYPE_1_VALUES!r}")
