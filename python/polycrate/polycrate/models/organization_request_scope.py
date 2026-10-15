from typing import Literal

OrganizationRequestScope = Literal["system", "user"]

ORGANIZATION_REQUEST_SCOPE_VALUES: set[OrganizationRequestScope] = {
    "system",
    "user",
}


def check_organization_request_scope(value: str) -> OrganizationRequestScope:
    if value in ORGANIZATION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_SCOPE_VALUES!r}")
