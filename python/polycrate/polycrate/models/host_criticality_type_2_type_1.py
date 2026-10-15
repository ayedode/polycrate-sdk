from typing import Literal

HostCriticalityType2Type1 = Literal["", "high", "low", "medium"]

HOST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[HostCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_host_criticality_type_2_type_1(value: str) -> HostCriticalityType2Type1:
    if value in HOST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
