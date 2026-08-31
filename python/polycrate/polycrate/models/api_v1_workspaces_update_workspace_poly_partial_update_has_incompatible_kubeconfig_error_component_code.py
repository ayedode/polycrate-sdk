from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_has_incompatible_kubeconfig_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateHasIncompatibleKubeconfigErrorComponentCode:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_HAS_INCOMPATIBLE_KUBECONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
