from typing import Literal

AlertCategoryLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_CATEGORY_LAST_STATE_VALUES: set[AlertCategoryLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_category_last_state(value: str) -> AlertCategoryLastState:
    if value in ALERT_CATEGORY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_LAST_STATE_VALUES!r}")
