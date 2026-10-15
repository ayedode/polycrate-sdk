from typing import Literal

DomainContactDetailKind = Literal["organization", "person"]

DOMAIN_CONTACT_DETAIL_KIND_VALUES: set[DomainContactDetailKind] = {
    "organization",
    "person",
}


def check_domain_contact_detail_kind(value: str) -> DomainContactDetailKind:
    if value in DOMAIN_CONTACT_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_KIND_VALUES!r}")
