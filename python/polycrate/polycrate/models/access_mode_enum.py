from typing import Literal

AccessModeEnum = Literal["read", "read_write"]

ACCESS_MODE_ENUM_VALUES: set[AccessModeEnum] = {
    "read",
    "read_write",
}


def check_access_mode_enum(value: str) -> AccessModeEnum:
    if value in ACCESS_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCESS_MODE_ENUM_VALUES!r}")
