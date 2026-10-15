from typing import Literal

MaintenanceRequestKind = Literal["generic"]

MAINTENANCE_REQUEST_KIND_VALUES: set[MaintenanceRequestKind] = {
    "generic",
}


def check_maintenance_request_kind(value: str) -> MaintenanceRequestKind:
    if value in MAINTENANCE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_REQUEST_KIND_VALUES!r}")
