from typing import Literal

AlertEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ALERT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_alert_effective_criticality_type_2_type_1(value: str) -> AlertEffectiveCriticalityType2Type1:
    if value in ALERT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
