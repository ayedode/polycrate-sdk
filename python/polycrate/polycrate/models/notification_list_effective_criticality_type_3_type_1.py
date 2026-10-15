from typing import Literal

NotificationListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

NOTIFICATION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[NotificationListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_notification_list_effective_criticality_type_3_type_1(
    value: str,
) -> NotificationListEffectiveCriticalityType3Type1:
    if value in NOTIFICATION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
