from typing import Literal

ApiV1WorkspaceTemplatesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspace_templates_update_name_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateNameErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
