from typing import Literal

PopEffectiveCriticalityType1 = Literal["high", "low", "medium"]

POP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PopEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_pop_effective_criticality_type_1(value: str) -> PopEffectiveCriticalityType1:
    if value in POP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
