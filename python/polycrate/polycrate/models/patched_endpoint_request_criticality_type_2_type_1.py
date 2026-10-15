from typing import Literal

PatchedEndpointRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedEndpointRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_endpoint_request_criticality_type_2_type_1(value: str) -> PatchedEndpointRequestCriticalityType2Type1:
    if value in PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
