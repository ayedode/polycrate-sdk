from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateKindErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
