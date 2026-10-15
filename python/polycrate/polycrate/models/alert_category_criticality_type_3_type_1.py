from typing import Literal

AlertCategoryCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ALERT_CATEGORY_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AlertCategoryCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_alert_category_criticality_type_3_type_1(value: str) -> AlertCategoryCriticalityType3Type1:
    if value in ALERT_CATEGORY_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
