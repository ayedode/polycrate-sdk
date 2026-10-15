from typing import Literal

HostEffectiveCriticalityType1 = Literal["high", "low", "medium"]

HOST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[HostEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_host_effective_criticality_type_1(value: str) -> HostEffectiveCriticalityType1:
    if value in HOST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
