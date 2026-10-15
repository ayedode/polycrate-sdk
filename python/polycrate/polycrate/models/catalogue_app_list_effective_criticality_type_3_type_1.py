from typing import Literal

CatalogueAppListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

CATALOGUE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CatalogueAppListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_catalogue_app_list_effective_criticality_type_3_type_1(
    value: str,
) -> CatalogueAppListEffectiveCriticalityType3Type1:
    if value in CATALOGUE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
