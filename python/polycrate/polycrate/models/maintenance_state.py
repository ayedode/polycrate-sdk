from typing import Literal

MaintenanceState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_STATE_VALUES: set[MaintenanceState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_state(value: str) -> MaintenanceState:
    if value in MAINTENANCE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_STATE_VALUES!r}")
