from typing import Literal

ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_workspace_templates_partial_update_is_default_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
