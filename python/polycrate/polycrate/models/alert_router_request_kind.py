from typing import Literal

AlertRouterRequestKind = Literal["dummy", "generic"]

ALERT_ROUTER_REQUEST_KIND_VALUES: set[AlertRouterRequestKind] = {
    "dummy",
    "generic",
}


def check_alert_router_request_kind(value: str) -> AlertRouterRequestKind:
    if value in ALERT_ROUTER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_REQUEST_KIND_VALUES!r}")
