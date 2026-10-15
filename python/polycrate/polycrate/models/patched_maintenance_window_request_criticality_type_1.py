from typing import Literal

PatchedMaintenanceWindowRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedMaintenanceWindowRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_maintenance_window_request_criticality_type_1(
    value: str,
) -> PatchedMaintenanceWindowRequestCriticalityType1:
    if value in PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
