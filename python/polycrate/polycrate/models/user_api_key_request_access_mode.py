from typing import Literal

UserAPIKeyRequestAccessMode = Literal["read", "read_write"]

USER_API_KEY_REQUEST_ACCESS_MODE_VALUES: set[UserAPIKeyRequestAccessMode] = {
    "read",
    "read_write",
}


def check_user_api_key_request_access_mode(value: str) -> UserAPIKeyRequestAccessMode:
    if value in USER_API_KEY_REQUEST_ACCESS_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_API_KEY_REQUEST_ACCESS_MODE_VALUES!r}")
