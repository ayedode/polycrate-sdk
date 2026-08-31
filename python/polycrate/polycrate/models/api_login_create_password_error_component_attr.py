from typing import Literal

ApiLoginCreatePasswordErrorComponentAttr = Literal["password"]

API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_ATTR_VALUES: set[ApiLoginCreatePasswordErrorComponentAttr] = {
    "password",
}


def check_api_login_create_password_error_component_attr(value: str) -> ApiLoginCreatePasswordErrorComponentAttr:
    if value in API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_LOGIN_CREATE_PASSWORD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
