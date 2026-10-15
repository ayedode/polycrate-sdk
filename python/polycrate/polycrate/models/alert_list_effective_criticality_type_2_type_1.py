from typing import Literal

AlertListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ALERT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_alert_list_effective_criticality_type_2_type_1(value: str) -> AlertListEffectiveCriticalityType2Type1:
    if value in ALERT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
