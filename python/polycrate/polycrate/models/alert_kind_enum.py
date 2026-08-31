from typing import Literal

AlertKindEnum = Literal["checkmk", "generic", "grafana"]

ALERT_KIND_ENUM_VALUES: set[AlertKindEnum] = {
    "checkmk",
    "generic",
    "grafana",
}


def check_alert_kind_enum(value: str) -> AlertKindEnum:
    if value in ALERT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_KIND_ENUM_VALUES!r}")
