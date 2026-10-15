from typing import Literal

MembershipRoleUpdateRole = Literal["admin", "billing", "developer", "owner", "viewer"]

MEMBERSHIP_ROLE_UPDATE_ROLE_VALUES: set[MembershipRoleUpdateRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_membership_role_update_role(value: str) -> MembershipRoleUpdateRole:
    if value in MEMBERSHIP_ROLE_UPDATE_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMBERSHIP_ROLE_UPDATE_ROLE_VALUES!r}")
