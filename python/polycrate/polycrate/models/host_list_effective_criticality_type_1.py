from typing import Literal

HostListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[HostListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_host_list_effective_criticality_type_1(value: str) -> HostListEffectiveCriticalityType1:
    if value in HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
