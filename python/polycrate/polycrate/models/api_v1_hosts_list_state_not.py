from typing import Literal

ApiV1HostsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_HOSTS_LIST_STATE_NOT_VALUES: set[ApiV1HostsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_hosts_list_state_not(value: str) -> ApiV1HostsListStateNot:
    if value in API_V1_HOSTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_STATE_NOT_VALUES!r}")
