from typing import Literal

ConditionCatalogDetailRequestKind = Literal["generic"]

CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES: set[ConditionCatalogDetailRequestKind] = {
    "generic",
}


def check_condition_catalog_detail_request_kind(value: str) -> ConditionCatalogDetailRequestKind:
    if value in CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES!r}")
