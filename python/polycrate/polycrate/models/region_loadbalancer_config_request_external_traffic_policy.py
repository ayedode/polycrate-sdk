from typing import Literal

RegionLoadbalancerConfigRequestExternalTrafficPolicy = Literal["Cluster", "Local"]

REGION_LOADBALANCER_CONFIG_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES: set[
    RegionLoadbalancerConfigRequestExternalTrafficPolicy
] = {
    "Cluster",
    "Local",
}


def check_region_loadbalancer_config_request_external_traffic_policy(
    value: str,
) -> RegionLoadbalancerConfigRequestExternalTrafficPolicy:
    if value in REGION_LOADBALANCER_CONFIG_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGION_LOADBALANCER_CONFIG_REQUEST_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
