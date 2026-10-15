from typing import Literal

PatchedPopRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedPopRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pop_request_criticality_type_2_type_1(value: str) -> PatchedPopRequestCriticalityType2Type1:
    if value in PATCHED_POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
