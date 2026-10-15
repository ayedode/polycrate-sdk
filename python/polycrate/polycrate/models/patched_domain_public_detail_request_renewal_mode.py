from typing import Literal

PatchedDomainPublicDetailRequestRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES: set[PatchedDomainPublicDetailRequestRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_patched_domain_public_detail_request_renewal_mode(value: str) -> PatchedDomainPublicDetailRequestRenewalMode:
    if value in PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES!r}"
    )
