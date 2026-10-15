from typing import Literal

PatchedLoadbalancerRegionRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedLoadbalancerRegionRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_loadbalancer_region_request_criticality_type_3_type_1(
    value: str,
) -> PatchedLoadbalancerRegionRequestCriticalityType3Type1:
    if value in PATCHED_LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_REGION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
