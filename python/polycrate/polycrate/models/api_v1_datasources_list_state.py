from typing import Literal

ApiV1DatasourcesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DATASOURCES_LIST_STATE_VALUES: set[ApiV1DatasourcesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_datasources_list_state(value: str) -> ApiV1DatasourcesListState:
    if value in API_V1_DATASOURCES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_STATE_VALUES!r}")
