from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_logs_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
