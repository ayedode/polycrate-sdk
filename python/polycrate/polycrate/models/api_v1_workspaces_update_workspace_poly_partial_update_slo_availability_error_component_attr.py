from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
