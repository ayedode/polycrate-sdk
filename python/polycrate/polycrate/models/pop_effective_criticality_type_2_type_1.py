from typing import Literal

PopEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

POP_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PopEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_pop_effective_criticality_type_2_type_1(value: str) -> PopEffectiveCriticalityType2Type1:
    if value in POP_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
