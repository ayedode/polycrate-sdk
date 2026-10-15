from typing import Literal

DomainPublicDetailRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

DOMAIN_PUBLIC_DETAIL_RENEWAL_MODE_VALUES: set[DomainPublicDetailRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_domain_public_detail_renewal_mode(value: str) -> DomainPublicDetailRenewalMode:
    if value in DOMAIN_PUBLIC_DETAIL_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_PUBLIC_DETAIL_RENEWAL_MODE_VALUES!r}")
