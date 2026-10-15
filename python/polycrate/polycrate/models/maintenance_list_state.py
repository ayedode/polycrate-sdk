from typing import Literal

MaintenanceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

MAINTENANCE_LIST_STATE_VALUES: set[MaintenanceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_maintenance_list_state(value: str) -> MaintenanceListState:
    if value in MAINTENANCE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_LIST_STATE_VALUES!r}")
