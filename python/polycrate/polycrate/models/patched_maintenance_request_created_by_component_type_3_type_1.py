from typing import Literal

PatchedMaintenanceRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

PATCHED_MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    PatchedMaintenanceRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_maintenance_request_created_by_component_type_3_type_1(
    value: str,
) -> PatchedMaintenanceRequestCreatedByComponentType3Type1:
    if value in PATCHED_MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_MAINTENANCE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
