from typing import Literal

DomainPublicDetailKind = Literal["generic"]

DOMAIN_PUBLIC_DETAIL_KIND_VALUES: set[DomainPublicDetailKind] = {
    "generic",
}


def check_domain_public_detail_kind(value: str) -> DomainPublicDetailKind:
    if value in DOMAIN_PUBLIC_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_KIND_VALUES!r}")
