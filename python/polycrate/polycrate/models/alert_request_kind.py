from typing import Literal

AlertRequestKind = Literal["checkmk", "generic", "grafana"]

ALERT_REQUEST_KIND_VALUES: set[AlertRequestKind] = {
    "checkmk",
    "generic",
    "grafana",
}


def check_alert_request_kind(value: str) -> AlertRequestKind:
    if value in ALERT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_REQUEST_KIND_VALUES!r}")
