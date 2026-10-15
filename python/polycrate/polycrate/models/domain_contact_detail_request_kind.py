from typing import Literal

DomainContactDetailRequestKind = Literal["organization", "person"]

DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES: set[DomainContactDetailRequestKind] = {
    "organization",
    "person",
}


def check_domain_contact_detail_request_kind(value: str) -> DomainContactDetailRequestKind:
    if value in DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES!r}")
