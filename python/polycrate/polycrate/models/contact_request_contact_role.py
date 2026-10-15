from typing import Literal

ContactRequestContactRole = Literal["admin", "billing", "developer", "viewer"]

CONTACT_REQUEST_CONTACT_ROLE_VALUES: set[ContactRequestContactRole] = {
    "admin",
    "billing",
    "developer",
    "viewer",
}


def check_contact_request_contact_role(value: str) -> ContactRequestContactRole:
    if value in CONTACT_REQUEST_CONTACT_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_REQUEST_CONTACT_ROLE_VALUES!r}")
