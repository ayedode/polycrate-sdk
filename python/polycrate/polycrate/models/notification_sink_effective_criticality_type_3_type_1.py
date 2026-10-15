from typing import Literal

NotificationSinkEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

NOTIFICATION_SINK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NotificationSinkEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_notification_sink_effective_criticality_type_3_type_1(
    value: str,
) -> NotificationSinkEffectiveCriticalityType3Type1:
    if value in NOTIFICATION_SINK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
