from typing import Literal

DomainPublicDetailRequestRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES: set[DomainPublicDetailRequestRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_domain_public_detail_request_renewal_mode(value: str) -> DomainPublicDetailRequestRenewalMode:
    if value in DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_REQUEST_RENEWAL_MODE_VALUES!r}")
