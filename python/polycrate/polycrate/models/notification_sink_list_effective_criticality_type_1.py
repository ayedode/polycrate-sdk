from typing import Literal

NotificationSinkListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[NotificationSinkListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_notification_sink_list_effective_criticality_type_1(
    value: str,
) -> NotificationSinkListEffectiveCriticalityType1:
    if value in NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SINK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
