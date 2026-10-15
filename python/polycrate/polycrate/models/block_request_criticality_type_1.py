from typing import Literal

BlockRequestCriticalityType1 = Literal["", "high", "low", "medium"]

BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES: set[BlockRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_request_criticality_type_1(value: str) -> BlockRequestCriticalityType1:
    if value in BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
