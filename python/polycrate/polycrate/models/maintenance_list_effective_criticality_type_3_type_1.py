from typing import Literal

MaintenanceListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[MaintenanceListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_list_effective_criticality_type_3_type_1(
    value: str,
) -> MaintenanceListEffectiveCriticalityType3Type1:
    if value in MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
