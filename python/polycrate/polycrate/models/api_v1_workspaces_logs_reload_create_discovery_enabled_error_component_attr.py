from typing import Literal

ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_workspaces_logs_reload_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
