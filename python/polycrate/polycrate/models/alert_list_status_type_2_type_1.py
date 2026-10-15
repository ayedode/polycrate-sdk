from typing import Literal

AlertListStatusType2Type1 = Literal["firing", "pending", "resolved", "silenced"]

ALERT_LIST_STATUS_TYPE_2_TYPE_1_VALUES: set[AlertListStatusType2Type1] = {
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_alert_list_status_type_2_type_1(value: str) -> AlertListStatusType2Type1:
    if value in ALERT_LIST_STATUS_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LIST_STATUS_TYPE_2_TYPE_1_VALUES!r}")
