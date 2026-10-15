from typing import Literal

PatchedContactGroupRequestKind = Literal["dynamic", "generic"]

PATCHED_CONTACT_GROUP_REQUEST_KIND_VALUES: set[PatchedContactGroupRequestKind] = {
    "dynamic",
    "generic",
}


def check_patched_contact_group_request_kind(value: str) -> PatchedContactGroupRequestKind:
    if value in PATCHED_CONTACT_GROUP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_CONTACT_GROUP_REQUEST_KIND_VALUES!r}")
