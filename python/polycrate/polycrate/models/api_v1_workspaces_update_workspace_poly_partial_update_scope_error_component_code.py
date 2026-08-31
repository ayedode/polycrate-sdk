from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_scope_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateScopeErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
