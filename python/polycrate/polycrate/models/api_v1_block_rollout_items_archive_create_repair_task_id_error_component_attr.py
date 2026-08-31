from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponentAttr = Literal["repair_task_id"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponentAttr
] = {
    "repair_task_id",
}


def check_api_v1_block_rollout_items_archive_create_repair_task_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
