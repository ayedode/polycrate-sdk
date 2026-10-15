from typing import Literal

UserAdminWriteRoleType3Type1 = Literal["", "admin", "billing", "developer", "owner", "viewer"]

USER_ADMIN_WRITE_ROLE_TYPE_3_TYPE_1_VALUES: set[UserAdminWriteRoleType3Type1] = {
    "",
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_admin_write_role_type_3_type_1(value: str) -> UserAdminWriteRoleType3Type1:
    if value in USER_ADMIN_WRITE_ROLE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_ADMIN_WRITE_ROLE_TYPE_3_TYPE_1_VALUES!r}")
