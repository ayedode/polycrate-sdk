from typing import Literal

ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_WORKSPACES_REPAIR_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_workspaces_repair_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
