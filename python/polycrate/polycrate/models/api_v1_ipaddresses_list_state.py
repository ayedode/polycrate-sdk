from typing import Literal

ApiV1IpaddressesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_IPADDRESSES_LIST_STATE_VALUES: set[ApiV1IpaddressesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_ipaddresses_list_state(value: str) -> ApiV1IpaddressesListState:
    if value in API_V1_IPADDRESSES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_STATE_VALUES!r}")
