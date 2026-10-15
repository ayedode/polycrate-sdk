from typing import Literal

CatalogueAppDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CATALOGUE_APP_DETAIL_STATE_VALUES: set[CatalogueAppDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_catalogue_app_detail_state(value: str) -> CatalogueAppDetailState:
    if value in CATALOGUE_APP_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_STATE_VALUES!r}")
