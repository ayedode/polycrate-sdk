from typing import Literal

DowntimeState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOWNTIME_STATE_VALUES: set[DowntimeState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_downtime_state(value: str) -> DowntimeState:
    if value in DOWNTIME_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_STATE_VALUES!r}")
