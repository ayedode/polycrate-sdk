from typing import Literal

ApiV1WorkspaceTemplatesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_WORKSPACE_TEMPLATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_workspace_templates_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesListWorkspacesErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
