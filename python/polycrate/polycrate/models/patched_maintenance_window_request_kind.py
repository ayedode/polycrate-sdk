from typing import Literal

PatchedMaintenanceWindowRequestKind = Literal["generic"]

PATCHED_MAINTENANCE_WINDOW_REQUEST_KIND_VALUES: set[PatchedMaintenanceWindowRequestKind] = {
    "generic",
}


def check_patched_maintenance_window_request_kind(value: str) -> PatchedMaintenanceWindowRequestKind:
    if value in PATCHED_MAINTENANCE_WINDOW_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_WINDOW_REQUEST_KIND_VALUES!r}")
