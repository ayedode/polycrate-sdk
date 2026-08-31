from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponentAttr = Literal["pop_id"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponentAttr
] = {
    "pop_id",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_pop_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdatePopIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
