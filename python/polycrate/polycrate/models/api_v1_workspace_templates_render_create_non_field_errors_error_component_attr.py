from typing import Literal

ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_workspace_templates_render_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesRenderCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_RENDER_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
