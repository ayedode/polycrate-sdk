from typing import Literal

ApiV1DomainsDomainRegistrarsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_VALUES: set[ApiV1DomainsDomainRegistrarsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_domain_registrars_list_state(value: str) -> ApiV1DomainsDomainRegistrarsListState:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_STATE_VALUES!r}"
    )
