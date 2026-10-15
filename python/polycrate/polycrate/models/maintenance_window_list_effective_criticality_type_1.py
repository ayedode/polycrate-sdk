from typing import Literal

MaintenanceWindowListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[MaintenanceWindowListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_window_list_effective_criticality_type_1(
    value: str,
) -> MaintenanceWindowListEffectiveCriticalityType1:
    if value in MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
