from typing import Literal

BlockListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BLOCK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BlockListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_block_list_effective_criticality_type_1(value: str) -> BlockListEffectiveCriticalityType1:
    if value in BLOCK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
