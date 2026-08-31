from typing import Literal

ApiV1MaintenancesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_MAINTENANCES_LIST_STATE_VALUES: set[ApiV1MaintenancesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_maintenances_list_state(value: str) -> ApiV1MaintenancesListState:
    if value in API_V1_MAINTENANCES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_STATE_VALUES!r}")
