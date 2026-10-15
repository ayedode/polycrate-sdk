from typing import Literal

ConditionCatalogDetailRequestSeverity = Literal["critical", "info", "warning"]

CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES: set[ConditionCatalogDetailRequestSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_condition_catalog_detail_request_severity(value: str) -> ConditionCatalogDetailRequestSeverity:
    if value in CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_REQUEST_SEVERITY_VALUES!r}")
