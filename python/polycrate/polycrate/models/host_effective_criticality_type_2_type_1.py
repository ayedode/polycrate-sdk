from typing import Literal

HostEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

HOST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[HostEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_host_effective_criticality_type_2_type_1(value: str) -> HostEffectiveCriticalityType2Type1:
    if value in HOST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
