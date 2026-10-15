from typing import Literal

UserAdminWriteRequestRoleType3Type1 = Literal["", "admin", "billing", "developer", "owner", "viewer"]

USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_3_TYPE_1_VALUES: set[UserAdminWriteRequestRoleType3Type1] = {
    "",
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_admin_write_request_role_type_3_type_1(value: str) -> UserAdminWriteRequestRoleType3Type1:
    if value in USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_3_TYPE_1_VALUES!r}"
    )
