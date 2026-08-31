from typing import Literal

ApiV1DomainsDomainsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DOMAINS_LIST_STATE_NOT_VALUES: set[ApiV1DomainsDomainsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_domains_list_state_not(value: str) -> ApiV1DomainsDomainsListStateNot:
    if value in API_V1_DOMAINS_DOMAINS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_STATE_NOT_VALUES!r}")
