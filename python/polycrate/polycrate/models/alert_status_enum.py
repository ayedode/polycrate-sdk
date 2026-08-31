from typing import Literal

AlertStatusEnum = Literal["firing", "pending", "resolved", "silenced"]

ALERT_STATUS_ENUM_VALUES: set[AlertStatusEnum] = {
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_status_enum(value: str) -> AlertStatusEnum:
    if value in ALERT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_STATUS_ENUM_VALUES!r}")
