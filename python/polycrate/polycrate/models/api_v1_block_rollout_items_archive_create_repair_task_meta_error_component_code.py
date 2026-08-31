from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_items_archive_create_repair_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
