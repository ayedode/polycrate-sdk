from typing import Literal

ApiV1WorkspaceTemplatesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACE_TEMPLATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspace_templates_list_state_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesListStateErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
