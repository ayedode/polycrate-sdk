from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentAttr = Literal["extra_context"]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentAttr
] = {
    "extra_context",
}


def check_api_v1_workspace_templates_render_create_extra_context_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
