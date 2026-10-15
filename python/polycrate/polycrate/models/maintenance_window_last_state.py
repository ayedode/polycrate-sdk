from typing import Literal

MaintenanceWindowLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_WINDOW_LAST_STATE_VALUES: set[MaintenanceWindowLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_window_last_state(value: str) -> MaintenanceWindowLastState:
    if value in MAINTENANCE_WINDOW_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_LAST_STATE_VALUES!r}")
