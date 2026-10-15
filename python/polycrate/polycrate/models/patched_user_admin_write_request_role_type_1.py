from typing import Literal

PatchedUserAdminWriteRequestRoleType1 = Literal["", "admin", "billing", "developer", "owner", "viewer"]

PATCHED_USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES: set[PatchedUserAdminWriteRequestRoleType1] = {
    "",
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_patched_user_admin_write_request_role_type_1(value: str) -> PatchedUserAdminWriteRequestRoleType1:
    if value in PATCHED_USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_USER_ADMIN_WRITE_REQUEST_ROLE_TYPE_1_VALUES!r}"
    )
