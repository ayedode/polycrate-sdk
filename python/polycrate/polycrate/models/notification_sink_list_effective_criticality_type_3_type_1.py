from typing import Literal

NotificationSinkListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    NotificationSinkListEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_notification_sink_list_effective_criticality_type_3_type_1(
    value: str,
) -> NotificationSinkListEffectiveCriticalityType3Type1:
    if value in NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
