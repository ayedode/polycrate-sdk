from typing import Literal

PatchedDomainContactDetailRequestKind = Literal["organization", "person"]

PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES: set[PatchedDomainContactDetailRequestKind] = {
    "organization",
    "person",
}


def check_patched_domain_contact_detail_request_kind(value: str) -> PatchedDomainContactDetailRequestKind:
    if value in PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_CONTACT_DETAIL_REQUEST_KIND_VALUES!r}"
    )
