from typing import Literal

PatchedHostRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_HOST_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedHostRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_host_request_criticality_type_1(value: str) -> PatchedHostRequestCriticalityType1:
    if value in PATCHED_HOST_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_HOST_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
