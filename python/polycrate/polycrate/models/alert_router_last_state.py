from typing import Literal

AlertRouterLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_ROUTER_LAST_STATE_VALUES: set[AlertRouterLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_router_last_state(value: str) -> AlertRouterLastState:
    if value in ALERT_ROUTER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LAST_STATE_VALUES!r}")
