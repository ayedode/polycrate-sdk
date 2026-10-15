from typing import Literal

PatchedMembershipRoleUpdateRequestRole = Literal["admin", "billing", "developer", "owner", "viewer"]

PATCHED_MEMBERSHIP_ROLE_UPDATE_REQUEST_ROLE_VALUES: set[PatchedMembershipRoleUpdateRequestRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_patched_membership_role_update_request_role(value: str) -> PatchedMembershipRoleUpdateRequestRole:
    if value in PATCHED_MEMBERSHIP_ROLE_UPDATE_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MEMBERSHIP_ROLE_UPDATE_REQUEST_ROLE_VALUES!r}"
    )
