from typing import Literal

PopRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PopRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pop_request_criticality_type_2_type_1(value: str) -> PopRequestCriticalityType2Type1:
    if value in POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
