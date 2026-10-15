from typing import Literal

AlertListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_LIST_STATE_VALUES: set[AlertListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_list_state(value: str) -> AlertListState:
    if value in ALERT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LIST_STATE_VALUES!r}")
