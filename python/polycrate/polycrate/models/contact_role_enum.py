from typing import Literal

ContactRoleEnum = Literal["admin", "billing", "developer", "viewer"]

CONTACT_ROLE_ENUM_VALUES: set[ContactRoleEnum] = {
    "admin",
    "billing",
    "developer",
    "viewer",
}


def check_contact_role_enum(value: str) -> ContactRoleEnum:
    if value in CONTACT_ROLE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ROLE_ENUM_VALUES!r}")
