from typing import Literal

AccessEnum = Literal["read", "write"]

ACCESS_ENUM_VALUES: set[AccessEnum] = {
    "read",
    "write",
}


def check_access_enum(value: str) -> AccessEnum:
    if value in ACCESS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCESS_ENUM_VALUES!r}")
