from typing import Literal

ApiV1BlocksDiscoverCreateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_discover_create_display_name_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateDisplayNameErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
