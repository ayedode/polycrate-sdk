from typing import Literal

ContactGroupMembershipRequestRole = Literal["contributor", "maintainer", "owner"]

CONTACT_GROUP_MEMBERSHIP_REQUEST_ROLE_VALUES: set[ContactGroupMembershipRequestRole] = {
    "contributor",
    "maintainer",
    "owner",
}


def check_contact_group_membership_request_role(value: str) -> ContactGroupMembershipRequestRole:
    if value in CONTACT_GROUP_MEMBERSHIP_REQUEST_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_MEMBERSHIP_REQUEST_ROLE_VALUES!r}")
