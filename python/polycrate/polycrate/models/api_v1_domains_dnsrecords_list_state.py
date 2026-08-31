from typing import Literal

ApiV1DomainsDnsrecordsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DNSRECORDS_LIST_STATE_VALUES: set[ApiV1DomainsDnsrecordsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_dnsrecords_list_state(value: str) -> ApiV1DomainsDnsrecordsListState:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_STATE_VALUES!r}")
