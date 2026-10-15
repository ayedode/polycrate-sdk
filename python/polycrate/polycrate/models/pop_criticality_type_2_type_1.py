from typing import Literal

PopCriticalityType2Type1 = Literal["", "high", "low", "medium"]

POP_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PopCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pop_criticality_type_2_type_1(value: str) -> PopCriticalityType2Type1:
    if value in POP_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
