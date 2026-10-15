from typing import Literal

MaintenanceRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

MAINTENANCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[MaintenanceRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_maintenance_request_criticality_type_3_type_1(value: str) -> MaintenanceRequestCriticalityType3Type1:
    if value in MAINTENANCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
