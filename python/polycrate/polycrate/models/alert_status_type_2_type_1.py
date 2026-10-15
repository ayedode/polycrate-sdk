from typing import Literal

AlertStatusType2Type1 = Literal["", "firing", "pending", "resolved", "silenced"]

ALERT_STATUS_TYPE_2_TYPE_1_VALUES: set[AlertStatusType2Type1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_status_type_2_type_1(value: str) -> AlertStatusType2Type1:
    if value in ALERT_STATUS_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_STATUS_TYPE_2_TYPE_1_VALUES!r}")
