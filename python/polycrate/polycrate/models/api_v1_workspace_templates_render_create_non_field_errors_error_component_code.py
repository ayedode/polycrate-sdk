from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_render_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
