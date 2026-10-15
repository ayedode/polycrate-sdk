from typing import Literal

DomainPublicDetailScope = Literal["system", "user"]

DOMAIN_PUBLIC_DETAIL_SCOPE_VALUES: set[DomainPublicDetailScope] = {
    "system",
    "user",
}


def check_domain_public_detail_scope(value: str) -> DomainPublicDetailScope:
    if value in DOMAIN_PUBLIC_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_SCOPE_VALUES!r}")
