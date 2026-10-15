from typing import Literal

UserAdminWriteRequestRoleType1 = Literal["", "admin", "billing", "developer", "owner", "viewer"]

USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES: set[UserAdminWriteRequestRoleType1] = {
    "",
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_admin_write_request_role_type_1(value: str) -> UserAdminWriteRequestRoleType1:
    if value in USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES!r}")
