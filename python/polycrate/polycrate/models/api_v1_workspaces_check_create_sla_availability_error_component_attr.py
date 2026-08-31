from typing import Literal

ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_WORKSPACES_CHECK_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_workspaces_check_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
