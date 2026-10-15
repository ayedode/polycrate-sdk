from typing import Literal

PatchedBlockRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedBlockRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_block_request_criticality_type_1(value: str) -> PatchedBlockRequestCriticalityType1:
    if value in PATCHED_BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
