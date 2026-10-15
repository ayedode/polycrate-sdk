from typing import Literal

OrganizationKind = Literal["generic"]

ORGANIZATION_KIND_VALUES: set[OrganizationKind] = {
    "generic",
}


def check_organization_kind(value: str) -> OrganizationKind:
    if value in ORGANIZATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_KIND_VALUES!r}")
