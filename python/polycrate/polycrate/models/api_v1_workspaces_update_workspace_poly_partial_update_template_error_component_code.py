from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponentCode
] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
