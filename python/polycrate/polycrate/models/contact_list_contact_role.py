from typing import Literal

ContactListContactRole = Literal["admin", "billing", "developer", "viewer"]

CONTACT_LIST_CONTACT_ROLE_VALUES: set[ContactListContactRole] = {
    "admin",
    "billing",
    "developer",
    "viewer",
}


def check_contact_list_contact_role(value: str) -> ContactListContactRole:
    if value in CONTACT_LIST_CONTACT_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_LIST_CONTACT_ROLE_VALUES!r}")
