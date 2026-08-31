from typing import Literal

ApiV1DomainsDomainRegistrarsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_NOT_VALUES: set[ApiV1DomainsDomainRegistrarsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_domain_registrars_list_state_not(value: str) -> ApiV1DomainsDomainRegistrarsListStateNot:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_NOT_VALUES!r}"
    )
