from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponentAttr = Literal["encrypted"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponentAttr
] = {
    "encrypted",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_encrypted_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEncryptedErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENCRYPTED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
