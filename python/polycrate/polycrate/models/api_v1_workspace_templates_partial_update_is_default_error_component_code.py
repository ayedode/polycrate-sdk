from typing import Literal

ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_partial_update_is_default_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesPartialUpdateIsDefaultErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
