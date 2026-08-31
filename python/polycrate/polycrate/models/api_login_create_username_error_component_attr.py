from typing import Literal

ApiLoginCreateUsernameErrorComponentAttr = Literal["username"]

API_LOGIN_CREATE_USERNAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiLoginCreateUsernameErrorComponentAttr] = {
    "username",
}


def check_api_login_create_username_error_component_attr(value: str) -> ApiLoginCreateUsernameErrorComponentAttr:
    if value in API_LOGIN_CREATE_USERNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_LOGIN_CREATE_USERNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
