from typing import Literal

DomainContactListKind = Literal["organization", "person"]

DOMAIN_CONTACT_LIST_KIND_VALUES: set[DomainContactListKind] = {
    "organization",
    "person",
}


def check_domain_contact_list_kind(value: str) -> DomainContactListKind:
    if value in DOMAIN_CONTACT_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_LIST_KIND_VALUES!r}")
