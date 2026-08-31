from typing import Literal

ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_WORKSPACES_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_workspaces_check_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
