from typing import Literal

ConditionCatalogListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_CATALOG_LIST_STATE_VALUES: set[ConditionCatalogListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_catalog_list_state(value: str) -> ConditionCatalogListState:
    if value in CONDITION_CATALOG_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_LIST_STATE_VALUES!r}")
