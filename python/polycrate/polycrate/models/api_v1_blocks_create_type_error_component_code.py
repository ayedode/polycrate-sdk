from typing import Literal

ApiV1BlocksCreateTypeErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateTypeErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_create_type_error_component_code(value: str) -> ApiV1BlocksCreateTypeErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
