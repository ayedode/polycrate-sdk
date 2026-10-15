from typing import Literal

NotificationSinkRequestCriticalityType1 = Literal["", "high", "low", "medium"]

NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES: set[NotificationSinkRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_notification_sink_request_criticality_type_1(value: str) -> NotificationSinkRequestCriticalityType1:
    if value in NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
