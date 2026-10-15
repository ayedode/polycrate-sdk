from typing import Literal

MaintenanceCriticalityType1 = Literal["", "high", "low", "medium"]

MAINTENANCE_CRITICALITY_TYPE_1_VALUES: set[MaintenanceCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_maintenance_criticality_type_1(value: str) -> MaintenanceCriticalityType1:
    if value in MAINTENANCE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_CRITICALITY_TYPE_1_VALUES!r}")
