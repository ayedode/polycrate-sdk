from typing import Literal

AlertStatusType3Type1 = Literal["", "firing", "pending", "resolved", "silenced"]

ALERT_STATUS_TYPE_3_TYPE_1_VALUES: set[AlertStatusType3Type1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_status_type_3_type_1(value: str) -> AlertStatusType3Type1:
    if value in ALERT_STATUS_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_STATUS_TYPE_3_TYPE_1_VALUES!r}")
