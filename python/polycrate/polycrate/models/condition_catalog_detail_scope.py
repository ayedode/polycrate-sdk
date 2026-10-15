from typing import Literal

ConditionCatalogDetailScope = Literal["system", "user"]

CONDITION_CATALOG_DETAIL_SCOPE_VALUES: set[ConditionCatalogDetailScope] = {
    "system",
    "user",
}


def check_condition_catalog_detail_scope(value: str) -> ConditionCatalogDetailScope:
    if value in CONDITION_CATALOG_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_SCOPE_VALUES!r}")
