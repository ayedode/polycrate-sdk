from typing import Literal

DomainRegistrarDetailRequestDefaultRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES: set[DomainRegistrarDetailRequestDefaultRenewalMode] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_domain_registrar_detail_request_default_renewal_mode(
    value: str,
) -> DomainRegistrarDetailRequestDefaultRenewalMode:
    if value in DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES!r}"
    )
