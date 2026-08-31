from typing import Literal

ApiV1BlockRolloutsArchiveCreateStatusErrorComponentAttr = Literal["status"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_block_rollouts_archive_create_status_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateStatusErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
