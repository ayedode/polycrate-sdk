from typing import Literal

HostListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

HOST_LIST_STATE_VALUES: set[HostListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_host_list_state(value: str) -> HostListState:
    if value in HOST_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_LIST_STATE_VALUES!r}")
