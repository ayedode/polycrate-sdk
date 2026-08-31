from typing import Literal

ApiV1MaintenanceWindowsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_MAINTENANCE_WINDOWS_LIST_STATE_VALUES: set[ApiV1MaintenanceWindowsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_maintenance_windows_list_state(value: str) -> ApiV1MaintenanceWindowsListState:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_STATE_VALUES!r}")
