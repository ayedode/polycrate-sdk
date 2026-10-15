from typing import Literal

NotificationSinkListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    NotificationSinkListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_notification_sink_list_effective_criticality_type_2_type_1(
    value: str,
) -> NotificationSinkListEffectiveCriticalityType2Type1:
    if value in NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
