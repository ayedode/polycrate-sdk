from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "required"
]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_organization_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
