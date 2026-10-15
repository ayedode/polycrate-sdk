from typing import Literal

MaintenanceRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[MaintenanceRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_maintenance_request_created_by_component_type_1(value: str) -> MaintenanceRequestCreatedByComponentType1:
    if value in MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
