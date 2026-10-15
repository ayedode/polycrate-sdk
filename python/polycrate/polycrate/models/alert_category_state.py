from typing import Literal

AlertCategoryState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_CATEGORY_STATE_VALUES: set[AlertCategoryState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_category_state(value: str) -> AlertCategoryState:
    if value in ALERT_CATEGORY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_STATE_VALUES!r}")
