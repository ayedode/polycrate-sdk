from typing import Literal

AlertRouterListKind = Literal["dummy", "generic"]

ALERT_ROUTER_LIST_KIND_VALUES: set[AlertRouterListKind] = {
    "dummy",
    "generic",
}


def check_alert_router_list_kind(value: str) -> AlertRouterListKind:
    if value in ALERT_ROUTER_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_LIST_KIND_VALUES!r}")
