from typing import Literal

CatalogueAppListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CATALOGUE_APP_LIST_STATE_VALUES: set[CatalogueAppListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_catalogue_app_list_state(value: str) -> CatalogueAppListState:
    if value in CATALOGUE_APP_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_LIST_STATE_VALUES!r}")
