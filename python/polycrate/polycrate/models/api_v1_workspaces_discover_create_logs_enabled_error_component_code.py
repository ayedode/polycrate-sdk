from typing import Literal

ApiV1WorkspacesDiscoverCreateLogsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_DISCOVER_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateLogsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_discover_create_logs_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateLogsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
