from typing import Literal

NotificationSinkRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NotificationSinkRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_notification_sink_request_criticality_type_3_type_1(
    value: str,
) -> NotificationSinkRequestCriticalityType3Type1:
    if value in NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
