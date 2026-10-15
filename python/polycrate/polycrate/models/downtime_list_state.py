from typing import Literal

DowntimeListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DOWNTIME_LIST_STATE_VALUES: set[DowntimeListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_downtime_list_state(value: str) -> DowntimeListState:
    if value in DOWNTIME_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_LIST_STATE_VALUES!r}")
