from typing import Literal

ApiV1BlocksDiscoverCreateIconUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_DISCOVER_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateIconUrlErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_discover_create_icon_url_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateIconUrlErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
