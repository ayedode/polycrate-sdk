from typing import Literal

PatchedContactRequestContactRole = Literal["admin", "billing", "developer", "viewer"]

PATCHED_CONTACT_REQUEST_CONTACT_ROLE_VALUES: set[PatchedContactRequestContactRole] = {
    "admin",
    "billing",
    "developer",
    "viewer",
}


def check_patched_contact_request_contact_role(value: str) -> PatchedContactRequestContactRole:
    if value in PATCHED_CONTACT_REQUEST_CONTACT_ROLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CONTACT_REQUEST_CONTACT_ROLE_VALUES!r}")
