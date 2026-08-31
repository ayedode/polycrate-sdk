from typing import Literal

ApiV1CatalogueAppsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CATALOGUE_APPS_LIST_STATE_VALUES: set[ApiV1CatalogueAppsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_catalogue_apps_list_state(value: str) -> ApiV1CatalogueAppsListState:
    if value in API_V1_CATALOGUE_APPS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_STATE_VALUES!r}")
