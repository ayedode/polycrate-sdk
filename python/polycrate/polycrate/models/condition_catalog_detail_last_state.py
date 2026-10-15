from typing import Literal

ConditionCatalogDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_CATALOG_DETAIL_LAST_STATE_VALUES: set[ConditionCatalogDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_catalog_detail_last_state(value: str) -> ConditionCatalogDetailLastState:
    if value in CONDITION_CATALOG_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_CATALOG_DETAIL_LAST_STATE_VALUES!r}")
