from typing import Literal

PatchedMaintenanceWindowRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedMaintenanceWindowRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_maintenance_window_request_criticality_type_2_type_1(
    value: str,
) -> PatchedMaintenanceWindowRequestCriticalityType2Type1:
    if value in PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_WINDOW_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
