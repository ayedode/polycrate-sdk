from typing import Literal

MaintenanceWindowScope = Literal["system", "user"]

MAINTENANCE_WINDOW_SCOPE_VALUES: set[MaintenanceWindowScope] = {
    "system",
    "user",
}


def check_maintenance_window_scope(value: str) -> MaintenanceWindowScope:
    if value in MAINTENANCE_WINDOW_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_SCOPE_VALUES!r}")
