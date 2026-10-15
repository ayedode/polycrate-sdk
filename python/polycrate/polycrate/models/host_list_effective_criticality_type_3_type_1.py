from typing import Literal

HostListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[HostListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_host_list_effective_criticality_type_3_type_1(value: str) -> HostListEffectiveCriticalityType3Type1:
    if value in HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
