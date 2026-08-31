from typing import Literal

ApiV1BlocksRepairCreateWebsiteUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateWebsiteUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_repair_create_website_url_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateWebsiteUrlErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
