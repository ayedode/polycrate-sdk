from typing import Literal

LoadbalancerRegionRequestExternalTrafficPolicy = Literal["Cluster", "Local"]

LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES: set[LoadbalancerRegionRequestExternalTrafficPolicy] = {
    "Cluster",
    "Local",
}


def check_loadbalancer_region_request_external_traffic_policy(
    value: str,
) -> LoadbalancerRegionRequestExternalTrafficPolicy:
    if value in LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
