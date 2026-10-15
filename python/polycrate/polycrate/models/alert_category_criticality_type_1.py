from typing import Literal

AlertCategoryCriticalityType1 = Literal["", "high", "low", "medium"]

ALERT_CATEGORY_CRITICALITY_TYPE_1_VALUES: set[AlertCategoryCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_category_criticality_type_1(value: str) -> AlertCategoryCriticalityType1:
    if value in ALERT_CATEGORY_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_CRITICALITY_TYPE_1_VALUES!r}")
