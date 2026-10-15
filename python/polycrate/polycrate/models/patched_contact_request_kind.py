from typing import Literal

PatchedContactRequestKind = Literal["generic"]

PATCHED_CONTACT_REQUEST_KIND_VALUES: set[PatchedContactRequestKind] = {
    "generic",
}


def check_patched_contact_request_kind(value: str) -> PatchedContactRequestKind:
    if value in PATCHED_CONTACT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CONTACT_REQUEST_KIND_VALUES!r}")
