from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentAttr = Literal["workspace_name"]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentAttr
] = {
    "workspace_name",
}


def check_api_v1_workspace_templates_render_create_workspace_name_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
