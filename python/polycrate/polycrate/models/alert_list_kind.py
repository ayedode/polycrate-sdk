from typing import Literal

AlertListKind = Literal["checkmk", "generic", "grafana"]

ALERT_LIST_KIND_VALUES: set[AlertListKind] = {
    "checkmk",
    "generic",
    "grafana",
}


def check_alert_list_kind(value: str) -> AlertListKind:
    if value in ALERT_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LIST_KIND_VALUES!r}")
