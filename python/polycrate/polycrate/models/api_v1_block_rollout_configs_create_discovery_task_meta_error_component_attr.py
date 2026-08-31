from typing import Literal

ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponentAttr = Literal["discovery_task_meta"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponentAttr
] = {
    "discovery_task_meta",
}


def check_api_v1_block_rollout_configs_create_discovery_task_meta_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateDiscoveryTaskMetaErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
