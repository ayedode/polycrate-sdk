from typing import Literal

ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_workspaces_logs_reload_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateDebugModeErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
