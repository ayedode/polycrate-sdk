from typing import Literal

ApiLoginCreatePasswordErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_CODE_VALUES: set[ApiLoginCreatePasswordErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_login_create_password_error_component_code(value: str) -> ApiLoginCreatePasswordErrorComponentCode:
    if value in API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
