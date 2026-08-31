from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_block_rollout_items_archive_create_repair_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
