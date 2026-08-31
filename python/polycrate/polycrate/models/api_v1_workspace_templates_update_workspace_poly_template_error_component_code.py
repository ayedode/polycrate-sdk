from typing import Literal

ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACE_TEMPLATES_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspace_templates_update_workspace_poly_template_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateWorkspacePolyTemplateErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
