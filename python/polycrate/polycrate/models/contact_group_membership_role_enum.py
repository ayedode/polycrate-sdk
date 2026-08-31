from typing import Literal

ContactGroupMembershipRoleEnum = Literal["contributor", "maintainer", "owner"]

CONTACT_GROUP_MEMBERSHIP_ROLE_ENUM_VALUES: set[ContactGroupMembershipRoleEnum] = {
    "contributor",
    "maintainer",
    "owner",
}


def check_contact_group_membership_role_enum(value: str) -> ContactGroupMembershipRoleEnum:
    if value in CONTACT_GROUP_MEMBERSHIP_ROLE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_MEMBERSHIP_ROLE_ENUM_VALUES!r}")
