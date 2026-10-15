from typing import Literal

AlertRouterState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_ROUTER_STATE_VALUES: set[AlertRouterState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_router_state(value: str) -> AlertRouterState:
    if value in ALERT_ROUTER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_STATE_VALUES!r}")
