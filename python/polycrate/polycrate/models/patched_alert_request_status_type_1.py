from typing import Literal

PatchedAlertRequestStatusType1 = Literal["", "firing", "pending", "resolved", "silenced"]

PATCHED_ALERT_REQUEST_STATUS_TYPE_1_VALUES: set[PatchedAlertRequestStatusType1] = {
    "",
    "firing",
    "pending",
    "resolved",
    "silenced",
}


def check_patched_alert_request_status_type_1(value: str) -> PatchedAlertRequestStatusType1:
    if value in PATCHED_ALERT_REQUEST_STATUS_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_REQUEST_STATUS_TYPE_1_VALUES!r}")
