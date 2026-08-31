from typing import Literal

ApiV1WorkspaceTemplatesCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACE_TEMPLATES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspace_templates_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
