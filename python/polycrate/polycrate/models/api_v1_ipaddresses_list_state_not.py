from typing import Literal

ApiV1IpaddressesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_IPADDRESSES_LIST_STATE_NOT_VALUES: set[ApiV1IpaddressesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_ipaddresses_list_state_not(value: str) -> ApiV1IpaddressesListStateNot:
    if value in API_V1_IPADDRESSES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_STATE_NOT_VALUES!r}")
