from typing import Literal

AlertScope = Literal["system", "user"]

ALERT_SCOPE_VALUES: set[AlertScope] = {
    "system",
    "user",
}


def check_alert_scope(value: str) -> AlertScope:
    if value in ALERT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_SCOPE_VALUES!r}")
