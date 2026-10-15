from typing import Literal

MaintenanceWindowListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_WINDOW_LIST_STATE_VALUES: set[MaintenanceWindowListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_window_list_state(value: str) -> MaintenanceWindowListState:
    if value in MAINTENANCE_WINDOW_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_LIST_STATE_VALUES!r}")
