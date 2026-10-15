from typing import Literal

AlertCategoryListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ALERT_CATEGORY_LIST_STATE_VALUES: set[AlertCategoryListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_alert_category_list_state(value: str) -> AlertCategoryListState:
    if value in ALERT_CATEGORY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_LIST_STATE_VALUES!r}")
