from typing import Literal

MaintenanceRequestScope = Literal["system", "user"]

MAINTENANCE_REQUEST_SCOPE_VALUES: set[MaintenanceRequestScope] = {
    "system",
    "user",
}


def check_maintenance_request_scope(value: str) -> MaintenanceRequestScope:
    if value in MAINTENANCE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_REQUEST_SCOPE_VALUES!r}")
