from typing import Literal

MaintenanceWindowKind = Literal["generic"]

MAINTENANCE_WINDOW_KIND_VALUES: set[MaintenanceWindowKind] = {
    "generic",
}


def check_maintenance_window_kind(value: str) -> MaintenanceWindowKind:
    if value in MAINTENANCE_WINDOW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_KIND_VALUES!r}")
