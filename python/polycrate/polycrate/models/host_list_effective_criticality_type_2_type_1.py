from typing import Literal

HostListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[HostListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_host_list_effective_criticality_type_2_type_1(value: str) -> HostListEffectiveCriticalityType2Type1:
    if value in HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
