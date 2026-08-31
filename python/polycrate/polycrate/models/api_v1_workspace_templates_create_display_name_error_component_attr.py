from typing import Literal

ApiV1WorkspaceTemplatesCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACE_TEMPLATES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspace_templates_create_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesCreateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
