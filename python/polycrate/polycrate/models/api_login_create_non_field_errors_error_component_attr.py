from typing import Literal

ApiLoginCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[ApiLoginCreateNonFieldErrorsErrorComponentAttr] = {
    "non_field_errors",
}


def check_api_login_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiLoginCreateNonFieldErrorsErrorComponentAttr:
    if value in API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_LOGIN_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
