from typing import Literal

BlockRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

BLOCK_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BlockRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_request_criticality_type_2_type_1(value: str) -> BlockRequestCriticalityType2Type1:
    if value in BLOCK_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
