from typing import Literal

DomainRegistrarDetailDefaultRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

DOMAIN_REGISTRAR_DETAIL_DEFAULT_RENEWAL_MODE_VALUES: set[DomainRegistrarDetailDefaultRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_domain_registrar_detail_default_renewal_mode(value: str) -> DomainRegistrarDetailDefaultRenewalMode:
    if value in DOMAIN_REGISTRAR_DETAIL_DEFAULT_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_DEFAULT_RENEWAL_MODE_VALUES!r}"
    )
