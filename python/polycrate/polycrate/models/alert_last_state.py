from typing import Literal

AlertLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_LAST_STATE_VALUES: set[AlertLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_last_state(value: str) -> AlertLastState:
    if value in ALERT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LAST_STATE_VALUES!r}")
