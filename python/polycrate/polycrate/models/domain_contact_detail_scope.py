from typing import Literal

DomainContactDetailScope = Literal["system", "user"]

DOMAIN_CONTACT_DETAIL_SCOPE_VALUES: set[DomainContactDetailScope] = {
    "system",
    "user",
}


def check_domain_contact_detail_scope(value: str) -> DomainContactDetailScope:
    if value in DOMAIN_CONTACT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_SCOPE_VALUES!r}")
