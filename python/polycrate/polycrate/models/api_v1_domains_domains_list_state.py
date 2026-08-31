from typing import Literal

ApiV1DomainsDomainsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DOMAINS_LIST_STATE_VALUES: set[ApiV1DomainsDomainsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_domains_list_state(value: str) -> ApiV1DomainsDomainsListState:
    if value in API_V1_DOMAINS_DOMAINS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_STATE_VALUES!r}")
