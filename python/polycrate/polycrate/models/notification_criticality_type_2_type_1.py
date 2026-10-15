from typing import Literal

NotificationCriticalityType2Type1 = Literal["", "high", "low", "medium"]

NOTIFICATION_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[NotificationCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_notification_criticality_type_2_type_1(value: str) -> NotificationCriticalityType2Type1:
    if value in NOTIFICATION_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
