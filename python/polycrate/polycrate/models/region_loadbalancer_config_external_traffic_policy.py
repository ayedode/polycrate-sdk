from typing import Literal

RegionLoadbalancerConfigExternalTrafficPolicy = Literal["Cluster", "Local"]

REGION_LOADBALANCER_CONFIG_EXTERNAL_TRAFFIC_POLICY_VALUES: set[RegionLoadbalancerConfigExternalTrafficPolicy] = {
    "Cluster",
    "Local",
}


def check_region_loadbalancer_config_external_traffic_policy(
    value: str,
) -> RegionLoadbalancerConfigExternalTrafficPolicy:
    if value in REGION_LOADBALANCER_CONFIG_EXTERNAL_TRAFFIC_POLICY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGION_LOADBALANCER_CONFIG_EXTERNAL_TRAFFIC_POLICY_VALUES!r}"
    )
