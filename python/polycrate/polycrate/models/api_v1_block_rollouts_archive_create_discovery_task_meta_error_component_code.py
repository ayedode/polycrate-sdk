from typing import Literal

ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_archive_create_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
