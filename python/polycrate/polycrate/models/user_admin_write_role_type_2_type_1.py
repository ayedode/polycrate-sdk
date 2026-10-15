from typing import Literal

UserAdminWriteRoleType2Type1 = Literal["", "admin", "billing", "developer", "owner", "viewer"]

USER_ADMIN_WRITE_ROLE_TYPE_2_TYPE_1_VALUES: set[UserAdminWriteRoleType2Type1] = {
    "",
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_admin_write_role_type_2_type_1(value: str) -> UserAdminWriteRoleType2Type1:
    if value in USER_ADMIN_WRITE_ROLE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_ADMIN_WRITE_ROLE_TYPE_2_TYPE_1_VALUES!r}")
