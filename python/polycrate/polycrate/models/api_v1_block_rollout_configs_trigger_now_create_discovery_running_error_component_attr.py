from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponentAttr = Literal["discovery_running"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponentAttr
] = {
    "discovery_running",
}


def check_api_v1_block_rollout_configs_trigger_now_create_discovery_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
