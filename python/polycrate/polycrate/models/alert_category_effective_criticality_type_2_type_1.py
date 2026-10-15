from typing import Literal

AlertCategoryEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ALERT_CATEGORY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[AlertCategoryEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_alert_category_effective_criticality_type_2_type_1(value: str) -> AlertCategoryEffectiveCriticalityType2Type1:
    if value in ALERT_CATEGORY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
