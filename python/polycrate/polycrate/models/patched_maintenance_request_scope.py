from typing import Literal

PatchedMaintenanceRequestScope = Literal["system", "user"]

PATCHED_MAINTENANCE_REQUEST_SCOPE_VALUES: set[PatchedMaintenanceRequestScope] = {
    "system",
    "user",
}


def check_patched_maintenance_request_scope(value: str) -> PatchedMaintenanceRequestScope:
    if value in PATCHED_MAINTENANCE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_REQUEST_SCOPE_VALUES!r}")
