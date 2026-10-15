from typing import Literal

ConditionCatalogDetailKind = Literal["generic"]

CONDITION_CATALOG_DETAIL_KIND_VALUES: set[ConditionCatalogDetailKind] = {
    "generic",
}


def check_condition_catalog_detail_kind(value: str) -> ConditionCatalogDetailKind:
    if value in CONDITION_CATALOG_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_KIND_VALUES!r}")
