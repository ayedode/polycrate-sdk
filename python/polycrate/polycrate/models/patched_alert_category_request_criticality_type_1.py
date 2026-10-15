from typing import Literal

PatchedAlertCategoryRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedAlertCategoryRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_alert_category_request_criticality_type_1(value: str) -> PatchedAlertCategoryRequestCriticalityType1:
    if value in PATCHED_ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
