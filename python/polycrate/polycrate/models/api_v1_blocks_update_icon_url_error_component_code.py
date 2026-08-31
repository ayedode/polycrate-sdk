from typing import Literal

ApiV1BlocksUpdateIconUrlErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksUpdateIconUrlErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_icon_url_error_component_code(value: str) -> ApiV1BlocksUpdateIconUrlErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_ICON_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
