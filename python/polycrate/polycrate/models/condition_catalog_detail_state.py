from typing import Literal

ConditionCatalogDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_CATALOG_DETAIL_STATE_VALUES: set[ConditionCatalogDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_catalog_detail_state(value: str) -> ConditionCatalogDetailState:
    if value in CONDITION_CATALOG_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_STATE_VALUES!r}")
