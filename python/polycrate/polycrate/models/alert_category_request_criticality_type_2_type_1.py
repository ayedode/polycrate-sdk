from typing import Literal

AlertCategoryRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertCategoryRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_category_request_criticality_type_2_type_1(value: str) -> AlertCategoryRequestCriticalityType2Type1:
    if value in ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
