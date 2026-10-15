from typing import Literal

AlertRouterListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_ROUTER_LIST_STATE_VALUES: set[AlertRouterListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_router_list_state(value: str) -> AlertRouterListState:
    if value in ALERT_ROUTER_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LIST_STATE_VALUES!r}")
