from typing import Literal

CatalogueAppDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CATALOGUE_APP_DETAIL_LAST_STATE_VALUES: set[CatalogueAppDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_catalogue_app_detail_last_state(value: str) -> CatalogueAppDetailLastState:
    if value in CATALOGUE_APP_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CATALOGUE_APP_DETAIL_LAST_STATE_VALUES!r}")
