from typing import Literal

ApiV1SystemApiKeysCreateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1SystemApiKeysCreateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_system_api_keys_create_name_error_component_code(
    value: str,
) -> ApiV1SystemApiKeysCreateNameErrorComponentCode:
    if value in API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SYSTEM_API_KEYS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
