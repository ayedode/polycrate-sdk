from typing import Literal

PatchedLoadbalancerRegionRequestExternalTrafficPolicy = Literal["Cluster", "Local"]

PATCHED_LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES: set[
    PatchedLoadbalancerRegionRequestExternalTrafficPolicy
] = {
    "Cluster",
    "Local",
}


def check_patched_loadbalancer_region_request_external_traffic_policy(
    value: str,
) -> PatchedLoadbalancerRegionRequestExternalTrafficPolicy:
    if value in PATCHED_LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
