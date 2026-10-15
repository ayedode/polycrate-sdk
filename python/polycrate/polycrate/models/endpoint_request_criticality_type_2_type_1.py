from typing import Literal

EndpointRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[EndpointRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_endpoint_request_criticality_type_2_type_1(value: str) -> EndpointRequestCriticalityType2Type1:
    if value in ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
