from typing import Literal

ApiV1DomainsDnsrecordsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_DNSRECORDS_LIST_STATE_NOT_VALUES: set[ApiV1DomainsDnsrecordsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_dnsrecords_list_state_not(value: str) -> ApiV1DomainsDnsrecordsListStateNot:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_STATE_NOT_VALUES!r}")
