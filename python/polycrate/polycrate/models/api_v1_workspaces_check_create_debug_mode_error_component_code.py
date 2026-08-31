from typing import Literal

ApiV1WorkspacesCheckCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_check_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateDebugModeErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
