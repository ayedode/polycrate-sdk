from typing import Literal

ApiV1BlocksArchiveCreateIconUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateIconUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_archive_create_icon_url_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateIconUrlErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
