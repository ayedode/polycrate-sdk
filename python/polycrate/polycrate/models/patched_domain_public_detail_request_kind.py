from typing import Literal

PatchedDomainPublicDetailRequestKind = Literal["generic"]

PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES: set[PatchedDomainPublicDetailRequestKind] = {
    "generic",
}


def check_patched_domain_public_detail_request_kind(value: str) -> PatchedDomainPublicDetailRequestKind:
    if value in PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_KIND_VALUES!r}")
