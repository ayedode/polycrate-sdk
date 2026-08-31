from typing import Literal

ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_items_update_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
