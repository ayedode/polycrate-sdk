from typing import Literal

UserCreateRequestRole = Literal["admin", "billing", "developer", "owner", "viewer"]

USER_CREATE_REQUEST_ROLE_VALUES: set[UserCreateRequestRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_create_request_role(value: str) -> UserCreateRequestRole:
    if value in USER_CREATE_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_CREATE_REQUEST_ROLE_VALUES!r}")
