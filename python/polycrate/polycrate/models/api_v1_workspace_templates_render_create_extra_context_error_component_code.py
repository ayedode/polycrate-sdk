from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_render_create_extra_context_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateExtraContextErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_EXTRA_CONTEXT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
