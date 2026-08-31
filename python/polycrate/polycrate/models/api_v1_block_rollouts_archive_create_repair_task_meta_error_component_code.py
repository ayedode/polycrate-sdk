from typing import Literal

ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_archive_create_repair_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateRepairTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
