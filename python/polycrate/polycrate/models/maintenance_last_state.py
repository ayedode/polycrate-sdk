from typing import Literal

MaintenanceLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_LAST_STATE_VALUES: set[MaintenanceLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_last_state(value: str) -> MaintenanceLastState:
    if value in MAINTENANCE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_LAST_STATE_VALUES!r}")
