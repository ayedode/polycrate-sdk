from typing import Literal

ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponentAttr = Literal["discovery_running"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponentAttr
] = {
    "discovery_running",
}


def check_api_v1_block_rollout_configs_update_discovery_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateDiscoveryRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
