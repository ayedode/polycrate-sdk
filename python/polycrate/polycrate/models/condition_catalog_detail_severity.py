from typing import Literal

ConditionCatalogDetailSeverity = Literal["critical", "info", "warning"]

CONDITION_CATALOG_DETAIL_SEVERITY_VALUES: set[ConditionCatalogDetailSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_condition_catalog_detail_severity(value: str) -> ConditionCatalogDetailSeverity:
    if value in CONDITION_CATALOG_DETAIL_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_SEVERITY_VALUES!r}")
