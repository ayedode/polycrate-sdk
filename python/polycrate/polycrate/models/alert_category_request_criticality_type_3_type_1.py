from typing import Literal

AlertCategoryRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AlertCategoryRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_category_request_criticality_type_3_type_1(value: str) -> AlertCategoryRequestCriticalityType3Type1:
    if value in ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
