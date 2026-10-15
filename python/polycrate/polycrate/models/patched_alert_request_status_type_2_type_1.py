from typing import Literal

PatchedAlertRequestStatusType2Type1 = Literal["", "firing", "pending", "resolved", "silenced"]

PATCHED_ALERT_REQUEST_STATUS_TYPE_2_TYPE_1_VALUES: set[PatchedAlertRequestStatusType2Type1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_patched_alert_request_status_type_2_type_1(value: str) -> PatchedAlertRequestStatusType2Type1:
    if value in PATCHED_ALERT_REQUEST_STATUS_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_REQUEST_STATUS_TYPE_2_TYPE_1_VALUES!r}"
    )
