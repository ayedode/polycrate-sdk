from typing import Literal

MaintenanceCriticalityType2Type1 = Literal["", "high", "low", "medium"]

MAINTENANCE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[MaintenanceCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_maintenance_criticality_type_2_type_1(value: str) -> MaintenanceCriticalityType2Type1:
    if value in MAINTENANCE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
