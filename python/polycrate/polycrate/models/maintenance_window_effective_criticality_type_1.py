from typing import Literal

MaintenanceWindowEffectiveCriticalityType1 = Literal["high", "low", "medium"]

MAINTENANCE_WINDOW_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[MaintenanceWindowEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_window_effective_criticality_type_1(value: str) -> MaintenanceWindowEffectiveCriticalityType1:
    if value in MAINTENANCE_WINDOW_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
