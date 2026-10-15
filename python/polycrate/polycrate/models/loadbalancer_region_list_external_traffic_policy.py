from typing import Literal

LoadbalancerRegionListExternalTrafficPolicy = Literal["Cluster", "Local"]

LOADBALANCER_REGION_LIST_EXTERNAL_TRAFFIC_POLICY_VALUES: set[LoadbalancerRegionListExternalTrafficPolicy] = {
    "Cluster",
    "Local",
}


def check_loadbalancer_region_list_external_traffic_policy(value: str) -> LoadbalancerRegionListExternalTrafficPolicy:
    if value in LOADBALANCER_REGION_LIST_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_LIST_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
