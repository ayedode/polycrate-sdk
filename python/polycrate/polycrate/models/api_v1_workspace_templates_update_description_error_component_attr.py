from typing import Literal

ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspace_templates_update_description_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
