from typing import Literal

MembershipCreateRequestRole = Literal["admin", "billing", "developer", "owner", "viewer"]

MEMBERSHIP_CREATE_REQUEST_ROLE_VALUES: set[MembershipCreateRequestRole] = {
    "admin",
    "billing",
    "developer",
    "owner",
    "viewer",
}


def check_membership_create_request_role(value: str) -> MembershipCreateRequestRole:
    if value in MEMBERSHIP_CREATE_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMBERSHIP_CREATE_REQUEST_ROLE_VALUES!r}")
