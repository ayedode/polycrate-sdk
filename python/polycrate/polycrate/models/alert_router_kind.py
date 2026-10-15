from typing import Literal

AlertRouterKind = Literal["dummy", "generic"]

ALERT_ROUTER_KIND_VALUES: set[AlertRouterKind] = {
    "dummy",
    "generic",
}


def check_alert_router_kind(value: str) -> AlertRouterKind:
    if value in ALERT_ROUTER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_KIND_VALUES!r}")
