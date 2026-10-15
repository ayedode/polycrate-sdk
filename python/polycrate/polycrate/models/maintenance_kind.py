from typing import Literal

MaintenanceKind = Literal["generic"]

MAINTENANCE_KIND_VALUES: set[MaintenanceKind] = {
    "generic",
}


def check_maintenance_kind(value: str) -> MaintenanceKind:
    if value in MAINTENANCE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_KIND_VALUES!r}")
