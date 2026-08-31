from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentAttr = Literal["workspace_poly_template"]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentAttr
] = {
    "workspace_poly_template",
}


def check_api_v1_workspace_templates_archive_create_workspace_poly_template_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateWorkspacePolyTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
