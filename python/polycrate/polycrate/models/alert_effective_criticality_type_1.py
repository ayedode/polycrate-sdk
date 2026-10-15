from typing import Literal

AlertEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ALERT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AlertEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_alert_effective_criticality_type_1(value: str) -> AlertEffectiveCriticalityType1:
    if value in ALERT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
