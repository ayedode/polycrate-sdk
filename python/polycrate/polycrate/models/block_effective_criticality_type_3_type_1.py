from typing import Literal

BlockEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

BLOCK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[BlockEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_block_effective_criticality_type_3_type_1(value: str) -> BlockEffectiveCriticalityType3Type1:
    if value in BLOCK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
