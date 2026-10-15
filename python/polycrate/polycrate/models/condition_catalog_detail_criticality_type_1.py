from typing import Literal

ConditionCatalogDetailCriticalityType1 = Literal["", "high", "low", "medium"]

CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_1_VALUES: set[ConditionCatalogDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_condition_catalog_detail_criticality_type_1(value: str) -> ConditionCatalogDetailCriticalityType1:
    if value in CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
