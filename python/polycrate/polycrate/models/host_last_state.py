from typing import Literal

HostLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

HOST_LAST_STATE_VALUES: set[HostLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_host_last_state(value: str) -> HostLastState:
    if value in HOST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_LAST_STATE_VALUES!r}")
