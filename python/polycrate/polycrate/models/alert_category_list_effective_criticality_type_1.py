from typing import Literal

AlertCategoryListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ALERT_CATEGORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AlertCategoryListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_alert_category_list_effective_criticality_type_1(value: str) -> AlertCategoryListEffectiveCriticalityType1:
    if value in ALERT_CATEGORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
