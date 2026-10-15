from typing import Literal

PatchedConditionCatalogDetailRequestSeverity = Literal["critical", "info", "warning"]

PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES: set[PatchedConditionCatalogDetailRequestSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_patched_condition_catalog_detail_request_severity(value: str) -> PatchedConditionCatalogDetailRequestSeverity:
    if value in PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES!r}"
    )
