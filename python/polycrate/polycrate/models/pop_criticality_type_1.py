from typing import Literal

PopCriticalityType1 = Literal["", "high", "low", "medium"]

POP_CRITICALITY_TYPE_1_VALUES: set[PopCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pop_criticality_type_1(value: str) -> PopCriticalityType1:
    if value in POP_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CRITICALITY_TYPE_1_VALUES!r}")
