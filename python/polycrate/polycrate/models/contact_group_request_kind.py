from typing import Literal

ContactGroupRequestKind = Literal["dynamic", "generic"]

CONTACT_GROUP_REQUEST_KIND_VALUES: set[ContactGroupRequestKind] = {
    "dynamic",
    "generic",
}


def check_contact_group_request_kind(value: str) -> ContactGroupRequestKind:
    if value in CONTACT_GROUP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_REQUEST_KIND_VALUES!r}")
