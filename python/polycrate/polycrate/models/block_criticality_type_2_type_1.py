from typing import Literal

BlockCriticalityType2Type1 = Literal["", "high", "low", "medium"]

BLOCK_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BlockCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_block_criticality_type_2_type_1(value: str) -> BlockCriticalityType2Type1:
    if value in BLOCK_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
