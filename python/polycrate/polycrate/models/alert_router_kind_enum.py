from typing import Literal

AlertRouterKindEnum = Literal["dummy", "generic"]

ALERT_ROUTER_KIND_ENUM_VALUES: set[AlertRouterKindEnum] = {
    "dummy",
    "generic",
}


def check_alert_router_kind_enum(value: str) -> AlertRouterKindEnum:
    if value in ALERT_ROUTER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_ROUTER_KIND_ENUM_VALUES!r}")
