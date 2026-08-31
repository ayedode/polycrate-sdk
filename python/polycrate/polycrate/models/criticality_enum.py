from typing import Literal

CriticalityEnum = Literal["high", "low", "medium"]

CRITICALITY_ENUM_VALUES: set[CriticalityEnum] = {
    "high",
    "low",
    "medium",
}


def check_criticality_enum(value: str) -> CriticalityEnum:
    if value in CRITICALITY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CRITICALITY_ENUM_VALUES!r}")
