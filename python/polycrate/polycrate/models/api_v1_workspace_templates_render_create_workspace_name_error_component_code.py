from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspace_templates_render_create_workspace_name_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateWorkspaceNameErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_WORKSPACE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
