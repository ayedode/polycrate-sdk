from typing import Literal

UserMembershipRole = Literal["admin", "billing", "developer", "owner", "viewer"]

USER_MEMBERSHIP_ROLE_VALUES: set[UserMembershipRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_user_membership_role(value: str) -> UserMembershipRole:
    if value in USER_MEMBERSHIP_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_MEMBERSHIP_ROLE_VALUES!r}")
