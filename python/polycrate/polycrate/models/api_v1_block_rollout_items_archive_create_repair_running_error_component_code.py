from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_archive_create_repair_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
