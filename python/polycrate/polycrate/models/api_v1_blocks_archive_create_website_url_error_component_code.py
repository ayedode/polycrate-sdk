from typing import Literal

ApiV1BlocksArchiveCreateWebsiteUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_ARCHIVE_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateWebsiteUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_archive_create_website_url_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateWebsiteUrlErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
