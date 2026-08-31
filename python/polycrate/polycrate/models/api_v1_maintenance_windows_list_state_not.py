from typing import Literal

ApiV1MaintenanceWindowsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_MAINTENANCE_WINDOWS_LIST_STATE_NOT_VALUES: set[ApiV1MaintenanceWindowsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_maintenance_windows_list_state_not(value: str) -> ApiV1MaintenanceWindowsListStateNot:
    if value in API_V1_MAINTENANCE_WINDOWS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_LIST_STATE_NOT_VALUES!r}")
