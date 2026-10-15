from typing import Literal

HostCriticalityType3Type1 = Literal["", "high", "low", "medium"]

HOST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[HostCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_host_criticality_type_3_type_1(value: str) -> HostCriticalityType3Type1:
    if value in HOST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
