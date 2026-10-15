from typing import Literal

ConditionCatalogDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CONDITION_CATALOG_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    ConditionCatalogDetailEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_condition_catalog_detail_effective_criticality_type_2_type_1(
    value: str,
) -> ConditionCatalogDetailEffectiveCriticalityType2Type1:
    if value in CONDITION_CATALOG_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
