from typing import Literal

UserAPIKeyAccessMode = Literal["read", "read_write"]

USER_API_KEY_ACCESS_MODE_VALUES: set[UserAPIKeyAccessMode] = {
    "read",
    "read_write",
}


def check_user_api_key_access_mode(value: str) -> UserAPIKeyAccessMode:
    if value in USER_API_KEY_ACCESS_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_API_KEY_ACCESS_MODE_VALUES!r}")
