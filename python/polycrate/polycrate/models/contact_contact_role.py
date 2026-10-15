from typing import Literal

ContactContactRole = Literal["admin", "billing", "developer", "viewer"]

CONTACT_CONTACT_ROLE_VALUES: set[ContactContactRole] = {
    "admin",
    "billing",
    "developer",
    "viewer",
}


def check_contact_contact_role(value: str) -> ContactContactRole:
    if value in CONTACT_CONTACT_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_CONTACT_ROLE_VALUES!r}")
