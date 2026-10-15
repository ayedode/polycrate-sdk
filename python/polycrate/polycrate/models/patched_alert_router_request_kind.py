from typing import Literal

PatchedAlertRouterRequestKind = Literal["dummy", "generic"]

PATCHED_ALERT_ROUTER_REQUEST_KIND_VALUES: set[PatchedAlertRouterRequestKind] = {
    "dummy",
    "generic",
}


def check_patched_alert_router_request_kind(value: str) -> PatchedAlertRouterRequestKind:
    if value in PATCHED_ALERT_ROUTER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_ROUTER_REQUEST_KIND_VALUES!r}")
