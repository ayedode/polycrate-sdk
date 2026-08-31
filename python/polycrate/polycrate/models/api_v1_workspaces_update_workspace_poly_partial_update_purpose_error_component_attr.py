from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
