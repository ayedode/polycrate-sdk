from typing import Literal

PrefixListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PREFIX_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PrefixListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_prefix_list_effective_criticality_type_3_type_1(value: str) -> PrefixListEffectiveCriticalityType3Type1:
    if value in PREFIX_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREFIX_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
