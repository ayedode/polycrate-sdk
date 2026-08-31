from typing import Literal

ApiV1BlocksArchiveCreateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateActionsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_archive_create_actions_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
