from typing import Literal

ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_workspace_templates_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
