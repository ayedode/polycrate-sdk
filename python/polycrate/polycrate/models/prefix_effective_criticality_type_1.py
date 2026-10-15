from typing import Literal

PrefixEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PREFIX_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PrefixEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_prefix_effective_criticality_type_1(value: str) -> PrefixEffectiveCriticalityType1:
    if value in PREFIX_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
