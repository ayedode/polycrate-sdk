from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspace_templates_archive_create_workspace_poly_template_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
