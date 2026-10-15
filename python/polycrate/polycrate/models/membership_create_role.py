from typing import Literal

MembershipCreateRole = Literal["admin", "billing", "developer", "owner", "viewer"]

MEMBERSHIP_CREATE_ROLE_VALUES: set[MembershipCreateRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_membership_create_role(value: str) -> MembershipCreateRole:
    if value in MEMBERSHIP_CREATE_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMBERSHIP_CREATE_ROLE_VALUES!r}")
