from typing import Literal

ContactRequestKind = Literal["generic"]

CONTACT_REQUEST_KIND_VALUES: set[ContactRequestKind] = {
    "generic",
}


def check_contact_request_kind(value: str) -> ContactRequestKind:
    if value in CONTACT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_REQUEST_KIND_VALUES!r}")
