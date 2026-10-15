from typing import Literal

NotificationEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

NOTIFICATION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[NotificationEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_notification_effective_criticality_type_2_type_1(value: str) -> NotificationEffectiveCriticalityType2Type1:
    if value in NOTIFICATION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
