from typing import Literal

HostRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

HOST_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[HostRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_host_request_criticality_type_3_type_1(value: str) -> HostRequestCriticalityType3Type1:
    if value in HOST_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
