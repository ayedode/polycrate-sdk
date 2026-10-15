from typing import Literal

MaintenanceCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

MAINTENANCE_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[MaintenanceCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_maintenance_created_by_component_type_2_type_1(value: str) -> MaintenanceCreatedByComponentType2Type1:
    if value in MAINTENANCE_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAINTENANCE_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
