from typing import Literal

PatchedPopRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_POP_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedPopRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pop_request_criticality_type_1(value: str) -> PatchedPopRequestCriticalityType1:
    if value in PATCHED_POP_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
