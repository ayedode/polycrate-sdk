from typing import Literal

PatchedNotificationSinkRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedNotificationSinkRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_notification_sink_request_criticality_type_1(
    value: str,
) -> PatchedNotificationSinkRequestCriticalityType1:
    if value in PATCHED_NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
