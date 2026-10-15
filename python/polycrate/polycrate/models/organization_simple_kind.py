from typing import Literal

OrganizationSimpleKind = Literal["generic"]

ORGANIZATION_SIMPLE_KIND_VALUES: set[OrganizationSimpleKind] = {
    "generic",
}


def check_organization_simple_kind(value: str) -> OrganizationSimpleKind:
    if value in ORGANIZATION_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_SIMPLE_KIND_VALUES!r}")
