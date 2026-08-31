from typing import Literal

ApiLoginCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[ApiLoginCreateNonFieldErrorsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_login_create_non_field_errors_error_component_code(
    value: str,
) -> ApiLoginCreateNonFieldErrorsErrorComponentCode:
    if value in API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
