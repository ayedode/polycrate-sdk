from typing import Literal

AlertKind = Literal["checkmk", "generic", "grafana"]

ALERT_KIND_VALUES: set[AlertKind] = {
    "checkmk",
    "generic",
    "grafana",
}


def check_alert_kind(value: str) -> AlertKind:
    if value in ALERT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_KIND_VALUES!r}")
