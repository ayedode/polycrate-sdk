from typing import Literal

MaintenanceListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[MaintenanceListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_list_effective_criticality_type_2_type_1(
    value: str,
) -> MaintenanceListEffectiveCriticalityType2Type1:
    if value in MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
