from typing import Literal

ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_WORKSPACES_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_workspaces_repair_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
