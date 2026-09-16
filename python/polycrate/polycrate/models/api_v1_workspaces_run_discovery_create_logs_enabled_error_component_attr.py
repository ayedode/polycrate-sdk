from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentAttr = Literal["logs_enabled"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentAttr
] = {
    "logs_enabled",
}


def check_api_v1_workspaces_run_discovery_create_logs_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateLogsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
