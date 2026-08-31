from typing import Literal

ApiV1BlocksCreateWebsiteUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateWebsiteUrlErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_create_website_url_error_component_code(
    value: str,
) -> ApiV1BlocksCreateWebsiteUrlErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
