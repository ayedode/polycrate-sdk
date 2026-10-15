from typing import Literal

BlockEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

BLOCK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BlockEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_block_effective_criticality_type_2_type_1(value: str) -> BlockEffectiveCriticalityType2Type1:
    if value in BLOCK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
