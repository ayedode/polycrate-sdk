from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateDebugModeErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
