from typing import Literal

PatchedDomainRegistrarDetailRequestDefaultRenewalMode = Literal["AUTODELETE", "AUTORENEW"]

PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES: set[
    PatchedDomainRegistrarDetailRequestDefaultRenewalMode
] = {
    "AUTODELETE",
    "AUTORENEW",
}


def check_patched_domain_registrar_detail_request_default_renewal_mode(
    value: str,
) -> PatchedDomainRegistrarDetailRequestDefaultRenewalMode:
    if value in PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DOMAIN_REGISTRAR_DETAIL_REQUEST_DEFAULT_RENEWAL_MODE_VALUES!r}"
    )
