from typing import Literal

MaintenanceWindowRequestKind = Literal["generic"]

MAINTENANCE_WINDOW_REQUEST_KIND_VALUES: set[MaintenanceWindowRequestKind] = {
    "generic",
}


def check_maintenance_window_request_kind(value: str) -> MaintenanceWindowRequestKind:
    if value in MAINTENANCE_WINDOW_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_REQUEST_KIND_VALUES!r}")
