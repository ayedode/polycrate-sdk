from typing import Literal

ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponentAttr = Literal["workspace_poly_template"]

API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponentAttr
] = {
    "workspace_poly_template",
}


def check_api_v1_workspace_templates_partial_update_workspace_poly_template_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesPartialUpdateWorkspacePolyTemplateErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_WORKSPACE_POLY_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
