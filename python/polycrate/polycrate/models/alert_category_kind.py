from typing import Literal

AlertCategoryKind = Literal["generic"]

ALERT_CATEGORY_KIND_VALUES: set[AlertCategoryKind] = {
    "generic",
}


def check_alert_category_kind(value: str) -> AlertCategoryKind:
    if value in ALERT_CATEGORY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_KIND_VALUES!r}")
