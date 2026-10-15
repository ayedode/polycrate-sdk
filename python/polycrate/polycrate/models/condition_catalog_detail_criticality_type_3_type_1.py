from typing import Literal

ConditionCatalogDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ConditionCatalogDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_condition_catalog_detail_criticality_type_3_type_1(value: str) -> ConditionCatalogDetailCriticalityType3Type1:
    if value in CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
