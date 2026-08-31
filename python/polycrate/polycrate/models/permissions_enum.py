from typing import Literal

PermissionsEnum = Literal["full", "read", "readwrite", "write"]

PERMISSIONS_ENUM_VALUES: set[PermissionsEnum] = {
    "full",
    "read",
    "readwrite",
    "write",
}


def check_permissions_enum(value: str) -> PermissionsEnum:
    if value in PERMISSIONS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PERMISSIONS_ENUM_VALUES!r}")
