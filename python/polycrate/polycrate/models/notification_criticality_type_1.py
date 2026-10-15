from typing import Literal

NotificationCriticalityType1 = Literal["", "high", "low", "medium"]

NOTIFICATION_CRITICALITY_TYPE_1_VALUES: set[NotificationCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_notification_criticality_type_1(value: str) -> NotificationCriticalityType1:
    if value in NOTIFICATION_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_CRITICALITY_TYPE_1_VALUES!r}")
