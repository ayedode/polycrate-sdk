from typing import Literal

PatchedEndpointRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedEndpointRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_endpoint_request_criticality_type_1(value: str) -> PatchedEndpointRequestCriticalityType1:
    if value in PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
