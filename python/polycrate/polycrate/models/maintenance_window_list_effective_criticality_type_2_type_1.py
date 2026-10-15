from typing import Literal

MaintenanceWindowListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    MaintenanceWindowListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_window_list_effective_criticality_type_2_type_1(
    value: str,
) -> MaintenanceWindowListEffectiveCriticalityType2Type1:
    if value in MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_WINDOW_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
