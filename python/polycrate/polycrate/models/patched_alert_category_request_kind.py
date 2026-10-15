from typing import Literal

PatchedAlertCategoryRequestKind = Literal["generic"]

PATCHED_ALERT_CATEGORY_REQUEST_KIND_VALUES: set[PatchedAlertCategoryRequestKind] = {
    "generic",
}


def check_patched_alert_category_request_kind(value: str) -> PatchedAlertCategoryRequestKind:
    if value in PATCHED_ALERT_CATEGORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_CATEGORY_REQUEST_KIND_VALUES!r}")
