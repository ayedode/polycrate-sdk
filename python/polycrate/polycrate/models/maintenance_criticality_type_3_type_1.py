from typing import Literal

MaintenanceCriticalityType3Type1 = Literal["", "high", "low", "medium"]

MAINTENANCE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[MaintenanceCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_maintenance_criticality_type_3_type_1(value: str) -> MaintenanceCriticalityType3Type1:
    if value in MAINTENANCE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
