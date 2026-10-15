from typing import Literal

AlertCategoryRequestKind = Literal["generic"]

ALERT_CATEGORY_REQUEST_KIND_VALUES: set[AlertCategoryRequestKind] = {
    "generic",
}


def check_alert_category_request_kind(value: str) -> AlertCategoryRequestKind:
    if value in ALERT_CATEGORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_REQUEST_KIND_VALUES!r}")
