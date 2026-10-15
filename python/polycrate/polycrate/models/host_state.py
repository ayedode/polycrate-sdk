from typing import Literal

HostState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

HOST_STATE_VALUES: set[HostState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_host_state(value: str) -> HostState:
    if value in HOST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_STATE_VALUES!r}")
