from typing import Literal

ApiV1BlocksArchiveCreateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateActionsErrorComponentAttr
] = {
    "actions",
}


def check_api_v1_blocks_archive_create_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
