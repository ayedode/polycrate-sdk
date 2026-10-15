from typing import Literal

PopRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

POP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PopRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pop_request_criticality_type_3_type_1(value: str) -> PopRequestCriticalityType3Type1:
    if value in POP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
