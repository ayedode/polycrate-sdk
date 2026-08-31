from typing import Literal

EffectiveCriticalityEnum = Literal["high", "low", "medium"]

EFFECTIVE_CRITICALITY_ENUM_VALUES: set[EffectiveCriticalityEnum] = {
    "high",
    "low",
    "medium",
}


def check_effective_criticality_enum(value: str) -> EffectiveCriticalityEnum:
    if value in EFFECTIVE_CRITICALITY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EFFECTIVE_CRITICALITY_ENUM_VALUES!r}")
