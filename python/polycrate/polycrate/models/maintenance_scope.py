from typing import Literal

MaintenanceScope = Literal["system", "user"]

MAINTENANCE_SCOPE_VALUES: set[MaintenanceScope] = {
    "system",
    "user",
}


def check_maintenance_scope(value: str) -> MaintenanceScope:
    if value in MAINTENANCE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_SCOPE_VALUES!r}")
