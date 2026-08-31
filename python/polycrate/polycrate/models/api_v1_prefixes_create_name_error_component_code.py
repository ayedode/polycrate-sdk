from typing import Literal

ApiV1PrefixesCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_PREFIXES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_prefixes_create_name_error_component_code(value: str) -> ApiV1PrefixesCreateNameErrorComponentCode:
    if value in API_V1_PREFIXES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
