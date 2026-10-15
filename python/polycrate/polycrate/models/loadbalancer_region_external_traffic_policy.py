from typing import Literal

LoadbalancerRegionExternalTrafficPolicy = Literal["Cluster", "Local"]

LOADBALANCER_REGION_EXTERNAL_TRAFFIC_POLICY_VALUES: set[LoadbalancerRegionExternalTrafficPolicy] = {
    "Cluster",
    "Local",
}


def check_loadbalancer_region_external_traffic_policy(value: str) -> LoadbalancerRegionExternalTrafficPolicy:
    if value in LOADBALANCER_REGION_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
