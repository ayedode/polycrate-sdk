from typing import Literal

DomainPublicDetailRequestKind = Literal["generic"]

DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES: set[DomainPublicDetailRequestKind] = {
    "generic",
}


def check_domain_public_detail_request_kind(value: str) -> DomainPublicDetailRequestKind:
    if value in DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES!r}")
