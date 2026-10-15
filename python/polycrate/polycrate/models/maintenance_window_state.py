from typing import Literal

MaintenanceWindowState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_WINDOW_STATE_VALUES: set[MaintenanceWindowState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_window_state(value: str) -> MaintenanceWindowState:
    if value in MAINTENANCE_WINDOW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_STATE_VALUES!r}")
