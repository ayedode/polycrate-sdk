from typing import Literal

EndpointCriticalityType1 = Literal["", "high", "low", "medium"]

ENDPOINT_CRITICALITY_TYPE_1_VALUES: set[EndpointCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_endpoint_criticality_type_1(value: str) -> EndpointCriticalityType1:
    if value in ENDPOINT_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_CRITICALITY_TYPE_1_VALUES!r}")
