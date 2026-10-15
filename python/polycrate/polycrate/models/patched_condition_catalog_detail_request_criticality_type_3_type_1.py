from typing import Literal

PatchedConditionCatalogDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedConditionCatalogDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_condition_catalog_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedConditionCatalogDetailRequestCriticalityType3Type1:
    if value in PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
