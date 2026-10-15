from typing import Literal

PrefixCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PREFIX_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PrefixCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_prefix_criticality_type_2_type_1(value: str) -> PrefixCriticalityType2Type1:
    if value in PREFIX_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
