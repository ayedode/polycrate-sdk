from typing import Literal

AlertCategoryScope = Literal["system", "user"]

ALERT_CATEGORY_SCOPE_VALUES: set[AlertCategoryScope] = {
    "system",
    "user",
}


def check_alert_category_scope(value: str) -> AlertCategoryScope:
    if value in ALERT_CATEGORY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_SCOPE_VALUES!r}")
