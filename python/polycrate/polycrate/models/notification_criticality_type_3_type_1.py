from typing import Literal

NotificationCriticalityType3Type1 = Literal["", "high", "low", "medium"]

NOTIFICATION_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NotificationCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_notification_criticality_type_3_type_1(value: str) -> NotificationCriticalityType3Type1:
    if value in NOTIFICATION_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
