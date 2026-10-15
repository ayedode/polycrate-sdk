from typing import Literal

PatchedMaintenanceRequestKind = Literal["generic"]

PATCHED_MAINTENANCE_REQUEST_KIND_VALUES: set[PatchedMaintenanceRequestKind] = {
    "generic",
}


def check_patched_maintenance_request_kind(value: str) -> PatchedMaintenanceRequestKind:
    if value in PATCHED_MAINTENANCE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_REQUEST_KIND_VALUES!r}")
