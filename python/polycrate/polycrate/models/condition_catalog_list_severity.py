from typing import Literal

ConditionCatalogListSeverity = Literal["critical", "info", "warning"]

CONDITION_CATALOG_LIST_SEVERITY_VALUES: set[ConditionCatalogListSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_condition_catalog_list_severity(value: str) -> ConditionCatalogListSeverity:
    if value in CONDITION_CATALOG_LIST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_LIST_SEVERITY_VALUES!r}")
