from typing import Literal

ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponentAttr = Literal["discovery_running"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponentAttr
] = {
    "discovery_running",
}


def check_api_v1_block_rollout_configs_create_discovery_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateDiscoveryRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
