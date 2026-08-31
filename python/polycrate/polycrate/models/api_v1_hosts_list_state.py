from typing import Literal

ApiV1HostsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_HOSTS_LIST_STATE_VALUES: set[ApiV1HostsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_hosts_list_state(value: str) -> ApiV1HostsListState:
    if value in API_V1_HOSTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_STATE_VALUES!r}")
