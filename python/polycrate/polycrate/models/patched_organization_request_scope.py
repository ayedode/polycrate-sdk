from typing import Literal

PatchedOrganizationRequestScope = Literal["system", "user"]

PATCHED_ORGANIZATION_REQUEST_SCOPE_VALUES: set[PatchedOrganizationRequestScope] = {
    "system",
    "user",
}


def check_patched_organization_request_scope(value: str) -> PatchedOrganizationRequestScope:
    if value in PATCHED_ORGANIZATION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_REQUEST_SCOPE_VALUES!r}")
