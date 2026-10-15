from typing import Literal

OrganizationRequestKind = Literal["generic"]

ORGANIZATION_REQUEST_KIND_VALUES: set[OrganizationRequestKind] = {
    "generic",
}


def check_organization_request_kind(value: str) -> OrganizationRequestKind:
    if value in ORGANIZATION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_KIND_VALUES!r}")
