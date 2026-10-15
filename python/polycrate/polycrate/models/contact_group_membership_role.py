from typing import Literal

ContactGroupMembershipRole = Literal["contributor", "maintainer", "owner"]

CONTACT_GROUP_MEMBERSHIP_ROLE_VALUES: set[ContactGroupMembershipRole] = {
    "contributor",
    "maintainer",
    "owner",
}


def check_contact_group_membership_role(value: str) -> ContactGroupMembershipRole:
    if value in CONTACT_GROUP_MEMBERSHIP_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_MEMBERSHIP_ROLE_VALUES!r}")
