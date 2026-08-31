from typing import Literal

ApiV1MaintenancesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_MAINTENANCES_LIST_STATE_NOT_VALUES: set[ApiV1MaintenancesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_maintenances_list_state_not(value: str) -> ApiV1MaintenancesListStateNot:
    if value in API_V1_MAINTENANCES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_STATE_NOT_VALUES!r}")
