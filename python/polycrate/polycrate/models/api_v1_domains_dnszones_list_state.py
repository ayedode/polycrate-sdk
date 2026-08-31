from typing import Literal

ApiV1DomainsDnszonesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DNSZONES_LIST_STATE_VALUES: set[ApiV1DomainsDnszonesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_dnszones_list_state(value: str) -> ApiV1DomainsDnszonesListState:
    if value in API_V1_DOMAINS_DNSZONES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_STATE_VALUES!r}")
