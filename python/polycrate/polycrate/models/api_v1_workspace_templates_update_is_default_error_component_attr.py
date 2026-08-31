from typing import Literal

ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_WORKSPACE_TEMPLATES_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_workspace_templates_update_is_default_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateIsDefaultErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
