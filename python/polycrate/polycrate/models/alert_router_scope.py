from typing import Literal

AlertRouterScope = Literal["system", "user"]

ALERT_ROUTER_SCOPE_VALUES: set[AlertRouterScope] = {
    "system",
    "user",
}


def check_alert_router_scope(value: str) -> AlertRouterScope:
    if value in ALERT_ROUTER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_SCOPE_VALUES!r}")
