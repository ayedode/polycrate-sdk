from typing import Literal

PatchedOrganizationRequestKind = Literal["generic"]

PATCHED_ORGANIZATION_REQUEST_KIND_VALUES: set[PatchedOrganizationRequestKind] = {
    "generic",
}


def check_patched_organization_request_kind(value: str) -> PatchedOrganizationRequestKind:
    if value in PATCHED_ORGANIZATION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_REQUEST_KIND_VALUES!r}")
