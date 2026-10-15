from typing import Literal

BlockEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_effective_criticality_type_1(value: str) -> BlockEffectiveCriticalityType1:
    if value in BLOCK_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
