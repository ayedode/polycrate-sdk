from typing import Literal

UserRoleEnum = Literal["admin", "billing", "developer", "owner", "viewer"]

USER_ROLE_ENUM_VALUES: set[UserRoleEnum] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_role_enum(value: str) -> UserRoleEnum:
    if value in USER_ROLE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_ROLE_ENUM_VALUES!r}")
