from typing import Literal

LoadbalancerRegionRequestCriticalityType1 = Literal["", "high", "low", "medium"]

LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_1_VALUES: set[LoadbalancerRegionRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_loadbalancer_region_request_criticality_type_1(value: str) -> LoadbalancerRegionRequestCriticalityType1:
    if value in LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
