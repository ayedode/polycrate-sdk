from typing import Literal

DomainContactSimpleKind = Literal["organization", "person"]

DOMAIN_CONTACT_SIMPLE_KIND_VALUES: set[DomainContactSimpleKind] = {
    "organization",
    "person",
}


def check_domain_contact_simple_kind(value: str) -> DomainContactSimpleKind:
    if value in DOMAIN_CONTACT_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_SIMPLE_KIND_VALUES!r}")
