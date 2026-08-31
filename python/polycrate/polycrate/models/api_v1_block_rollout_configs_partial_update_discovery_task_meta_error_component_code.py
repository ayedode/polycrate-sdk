from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_partial_update_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
