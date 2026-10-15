from typing import Literal

DomainListRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

DOMAIN_LIST_RENEWAL_MODE_VALUES: set[DomainListRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_domain_list_renewal_mode(value: str) -> DomainListRenewalMode:
    if value in DOMAIN_LIST_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_LIST_RENEWAL_MODE_VALUES!r}")
