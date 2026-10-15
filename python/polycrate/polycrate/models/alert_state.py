from typing import Literal

AlertState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_STATE_VALUES: set[AlertState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_state(value: str) -> AlertState:
    if value in ALERT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_STATE_VALUES!r}")
