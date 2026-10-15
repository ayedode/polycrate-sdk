from typing import Literal

MaintenanceCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

MAINTENANCE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[MaintenanceCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_maintenance_created_by_component_type_3_type_1(value: str) -> MaintenanceCreatedByComponentType3Type1:
    if value in MAINTENANCE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
