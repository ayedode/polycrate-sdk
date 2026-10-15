from typing import Literal

MaintenanceEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

MAINTENANCE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[MaintenanceEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_maintenance_effective_criticality_type_3_type_1(value: str) -> MaintenanceEffectiveCriticalityType3Type1:
    if value in MAINTENANCE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
