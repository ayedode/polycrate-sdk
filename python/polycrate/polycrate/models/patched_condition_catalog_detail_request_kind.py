from typing import Literal

PatchedConditionCatalogDetailRequestKind = Literal["generic"]

PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES: set[PatchedConditionCatalogDetailRequestKind] = {
    "generic",
}


def check_patched_condition_catalog_detail_request_kind(value: str) -> PatchedConditionCatalogDetailRequestKind:
    if value in PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_KIND_VALUES!r}"
    )
