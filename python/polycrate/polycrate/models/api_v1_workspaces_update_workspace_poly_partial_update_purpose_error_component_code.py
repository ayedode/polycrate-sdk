from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
