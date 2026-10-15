from typing import Literal

MaintenanceWindowCriticalityType1 = Literal["", "high", "low", "medium"]

MAINTENANCE_WINDOW_CRITICALITY_TYPE_1_VALUES: set[MaintenanceWindowCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_maintenance_window_criticality_type_1(value: str) -> MaintenanceWindowCriticalityType1:
    if value in MAINTENANCE_WINDOW_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_CRITICALITY_TYPE_1_VALUES!r}")
