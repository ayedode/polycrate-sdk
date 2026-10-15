from typing import Literal

BlockCriticalityType3Type1 = Literal["", "high", "low", "medium"]

BLOCK_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[BlockCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_criticality_type_3_type_1(value: str) -> BlockCriticalityType3Type1:
    if value in BLOCK_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
